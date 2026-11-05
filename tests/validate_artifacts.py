"""Validate ACIE JSON schemas, fixtures, YAML contracts, and required files."""
from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
FIXTURES = ROOT / "tests" / "fixtures"

pairs = [
    (SCHEMAS / "mission.schema.json", FIXTURES / "mission.valid.json"),
    (SCHEMAS / "event-envelope.schema.json", FIXTURES / "event.valid.json"),
]
for schema_path, fixture_path in pairs:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    instance = json.loads(fixture_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        raise SystemExit(f"FAIL {fixture_path.name}: " + "; ".join(e.message for e in errors))
    print(f"PASS schema+fixture: {schema_path.name}")

for schema_path in [SCHEMAS / "governance-decision.schema.json", SCHEMAS / "adaptation-proposal.schema.json"]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    print(f"PASS schema meta-validation: {schema_path.name}")

contracts = yaml.safe_load((ROOT / "contracts" / "component-contracts.yaml").read_text(encoding="utf-8"))
assert contracts["apiVersion"] == "acie/v1"
assert len(contracts["components"]) == 8
assert len({c["id"] for c in contracts["components"]}) == 8
print("PASS component contract registry: 8 unique components")

required = [
    ROOT / "chapters" / "23_governance_autonomy_adaptation_models.md",
    ROOT / "chapters" / "24_evaluation_methodology.md",
    ROOT / "appendices" / "A_component_contracts.md",
    ROOT / "appendices" / "B_event_mission_schemas.md",
    ROOT / "appendices" / "C_evaluation_checklist.md",
    ROOT / "appendices" / "D_glossary_index.md",
    ROOT / "appendices" / "E_reference_register.md",
    ROOT / "appendices" / "F_personality_kernel_audit.md",
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
if missing:
    raise SystemExit("Missing required deliverables: " + ", ".join(missing))
print("PASS required manuscript and appendix files")
