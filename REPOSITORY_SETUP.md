# Repository setup record

## Confirmed configuration

- Repository: `DerithAI/ACIE`
- Visibility: public
- Default branch: `main`
- Repository permissions: authenticated connection has admin, maintain, push and pull access
- Merge methods: merge commit, rebase and squash enabled; auto-merge disabled
- Root README, contribution guidance, security policy and `.gitignore` committed

## Publication gates still open

The canonical v1.0 source package has not yet been synchronized into this repository. The local release package is the authoritative source until the repository tree is verified against its manifest and SHA-256 checksums. CI is intentionally deferred rather than publishing a workflow that would fail because the source/test directories are not present yet.

The repository connector available to this setup can create and update files, Git objects and branches, but does not expose repository creation/settings mutations, ruleset/branch-protection creation, Actions security settings, release creation, tag creation, or release-asset upload. Do not infer that those settings have been applied.

## Required GitHub UI configuration

After the source tree is published:

1. **Settings → Branches / Rulesets:** protect `main`; require pull requests; require the validation status check once the workflow exists; block force pushes and deletion. Keep administrator bypass disabled where operationally appropriate.
2. **Settings → Actions → General:** set `GITHUB_TOKEN` to read-only by default; allow workflows to create or approve pull requests only if a reviewed workflow explicitly needs it.
3. **Security:** enable Dependabot alerts and security updates, secret scanning and push protection where available; enable CodeQL/default code scanning after confirming supported languages. Configure private vulnerability reporting.
4. **Repository metadata:** add a concise description and ACIE topics; add a license only after the rights holder explicitly chooses one. Public visibility is not a license.
5. **Release:** publish `v1.0.0` only after source-tree checksum verification and successful CI; attach the final PDF and DOCX as release assets.

## Source integrity

The local release manifest and `SHA256SUMS.txt` are the publication baseline. Any repository publication must preserve the original source content and verify checksums. Generated caches such as `__pycache__` and `.pyc` files must not be committed.
