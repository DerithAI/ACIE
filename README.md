# ACIE — Adaptive Cognitive Infrastructure Engineering

**ACIE** is a discipline for designing persistent, governable, adaptive computational environments. This repository is the canonical public home for the ACIE v1.0 whitepaper, its formal models, schemas, component contracts, evaluation materials, and reference artifacts.

## Release status

- **Specification:** ACIE v1.0
- **Repository:** `DerithAI/ACIE`
- **Default branch:** `main`
- **Publication state:** repository initialized; source package and release assets are being published in staged commits.
- **Normative boundary:** ACIE defines the discipline and architectural concepts. LUMEN is discussed as a reference implementation candidate, not as proof that every ACIE property is implemented or conformant.

## Repository map

| Path | Purpose |
|---|---|
| `chapters/` | Whitepaper chapters |
| `appendices/` | Component contracts, schemas, evaluation checklist, glossary and audits |
| `schemas/` | JSON Schemas for mission, event, governance and adaptation artifacts |
| `contracts/` | Canonical component contracts |
| `formalization/` | State machines and executable state models |
| `diagrams/` | Architecture source diagrams and rendered figures |
| `tests/` | Validation and state-model tests |
| `references/` | Reference register and source notes |
| `build/` | Reproducible document build tooling and generated outputs |

## Core cognitive lifecycle

**Observe → Interpret → Route → Deliberate → Govern → Act → Reflect → Learn → Persist**

## Validation

The source package includes artifact validation and state-model tests. Run the checks from the repository root:

```bash
python -m unittest discover -s tests -v
python tests/validate_artifacts.py
```

The build tool and its dependencies are documented under `build/`.

## Project principles

- Persistent continuity is an architectural property, not a chat-session assumption.
- Autonomy is bounded by explicit governance, permissions, approval and audit semantics.
- Adaptation is staged, evaluated and reversible rather than silently self-modifying.
- Runtime, memory, cognition and governance are treated as cooperating system layers.
- LUMEN implementation details remain distinct from ACIE's discipline-level specification.

## Security and responsible disclosure

See [SECURITY.md](SECURITY.md). Do not publish credentials, tokens, private user data or production secrets in issues or pull requests.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should preserve the distinction between normative ACIE definitions, implementation examples and research proposals.

## Citation

A citation file will be added with the publication metadata once the canonical author and release metadata are finalized. Please cite the versioned whitepaper rather than an unpinned branch when referencing ACIE.

## License

No license is asserted by this repository initialization. All rights remain with the respective rights holder until an explicit license is added. Public visibility does not itself grant permission to reuse, modify or redistribute the contents.
