# Contributing to ACIE

Thank you for helping improve ACIE. Contributions should make the discipline clearer, more testable, safer, or easier to implement.

## Before opening a change

1. Search existing issues and pull requests to avoid duplicate work.
2. For substantial architectural changes, open an issue or proposal first.
3. State whether the change is normative (changes ACIE meaning), informative (clarifies or illustrates), or implementation-specific.
4. Preserve the distinction between ACIE, ACI, COS and the LUMEN reference implementation.

## Pull requests

- Keep changes focused and explain the motivation.
- Update relevant chapters, glossary, schemas, contracts, diagrams and tests together.
- Include evidence for changed claims and avoid presenting proposals as established facts.
- Run `python -m unittest discover -s tests -v` and `python tests/validate_artifacts.py` when applicable.
- Do not commit secrets, generated caches, temporary files or unrelated binaries.

## Specification changes

Normative changes must explain compatibility impact and include an updated versioning proposal. Changes to governance, autonomy, identity, persistence or adaptation semantics require explicit rationale and testable acceptance criteria.
