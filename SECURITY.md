# Security policy

## What deslop can do

The skill is instructions only (`SKILL.md`, `references/kill-lists.md`). It declares no tools, runs nothing, and fetches nothing at runtime. Drafts it edits are treated as material, not instructions.

`scripts/build_bundle.py` is a maintainer tool for packaging. The skill never calls it.

## Verifying what you install

- `deslop.skill` is rebuilt deterministically from the sources. CI fails when the bundle, `SHA256SUMS`, and the sources drift apart, or when zero-width, bidi, Unicode tag characters, or HTML comments appear in the bundled files.
- Check a downloaded bundle against `SHA256SUMS` from the same commit: `shasum -a 256 deslop.skill` (macOS) or `sha256sum deslop.skill` (Linux).
- Pin a clone to the commit you reviewed and read the diff before updating (`git log -p HEAD..origin/main`).

## Reporting a problem

Use GitHub's private vulnerability reporting on this repository if it is enabled. Otherwise open an issue titled "security contact" without exploit details, and a private channel will be arranged. Include the affected file and steps to reproduce.
