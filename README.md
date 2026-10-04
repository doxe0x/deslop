# deslop

<p align="center">
  <img src="assets/banner.png" alt="deslop" width="100%">
</p>

A Claude skill that audits and rewrites text so it stops reading like AI.

The idea behind it: AI prose reads as AI because it is statistically average. Safe claims, generic transitions, neat symmetry, no real position, almost no concrete detail. Swapping out words like "delve", "leverage", and "robust" is the smallest lever. The skill works down five layers (vocabulary, filler phrases, structure, rhythm, tone) and pushes for the three things a model cannot fake on its own: specificity, a position the author actually holds, and rhythm.

It works in any language, not only English: the structural, rhythm, and tone layers are language-agnostic, and the skill hunts local calques of the same patterns instead of translating the English kill-list word for word. It always answers in the language of the draft.

## Contents

- `SKILL.md`: the skill itself. It runs in two modes. AUDIT flags what reads as AI and gives a sharper rewrite for each span. REWRITE produces a de-slopped version.
- `references/kill-lists.md`: the full vocabulary and phrase lists, the research behind them (the PubMed "delve" study, the detector-reliability findings), a crypto/DeFi note on which on-chain terms are real versus slop, and a prompt pack for use in other models.
- `deslop.skill`: the same two files packaged as a single zip for a one-step install.
- `SHA256SUMS`: the checksum of `deslop.skill`.
- `scripts/build_bundle.py`: rebuilds the bundle deterministically and checks it in CI. The skill itself never runs it.
- `SECURITY.md`: what the skill can do and how to report a problem.

## Install (Claude Code)

A skill is a folder that holds a `SKILL.md`. You want the file to end up at `~/.claude/skills/deslop/SKILL.md`. Pick one of the methods below, then verify it loaded.

### Method 1: clone the repo

macOS and Linux:

```
git clone https://github.com/doxe0x/deslop.git ~/.claude/skills/deslop
```

Windows (PowerShell):

```
git clone https://github.com/doxe0x/deslop.git $env:USERPROFILE\.claude\skills\deslop
```

Windows (cmd):

```
git clone https://github.com/doxe0x/deslop.git %USERPROFILE%\.claude\skills\deslop
```

Cloning also leaves `README.md`, `LICENSE`, `deslop.skill`, and a `.git` folder in the skill directory. That is harmless, because Claude Code only reads `SKILL.md` and the `references` files.

Pin the commit you reviewed and update deliberately, reading the diff first:

```
git -C ~/.claude/skills/deslop checkout <commit-you-reviewed>
git -C ~/.claude/skills/deslop fetch
git -C ~/.claude/skills/deslop log -p HEAD..origin/main
```

### Method 2: unzip the bundle

Download `deslop.skill`, check it against `SHA256SUMS` from the same commit (`shasum -a 256 deslop.skill` on macOS, `sha256sum deslop.skill` on Linux), and unzip it into your skills folder. The archive already nests everything under a `deslop/` folder, so you get the right layout.

macOS and Linux:

```
mkdir -p ~/.claude/skills
unzip deslop.skill -d ~/.claude/skills/
```

Windows (PowerShell):

```
Expand-Archive -Path deslop.skill -DestinationPath $env:USERPROFILE\.claude\skills\
```

If your unzip tool refuses the `.skill` extension, rename the file to `deslop.zip` first. It is a plain zip.

### Verify it loaded

Claude Code reads skills when a session starts, so open a new session (or restart Claude Code) after installing. Then run `/skills` and check that `deslop` is listed. If it is missing, make sure the file sits at exactly `~/.claude/skills/deslop/SKILL.md` and not at `~/.claude/skills/deslop/deslop/SKILL.md`.

Once it is loaded, Claude uses it on requests like "does this sound like AI?", "de-slop this", "make it sound like me", or when you ask it to write prose that should not sound machine-generated.

### Install for one project only

To scope the skill to a single repo instead of your whole machine, put the same folder under that project: `<project>/.claude/skills/deslop/SKILL.md`. Same layout, just under the project root instead of your home directory.

## Install (Claude app)

In the Claude web or desktop app, open Settings, find the Skills section, choose to upload a skill, and pick `deslop.skill`. Upload the bundle as is. Do not unzip it; unzipping is only for the Claude Code method above. If the upload dialog accepts only `.zip`, rename `deslop.skill` to `deslop.zip` first. Custom skills need a plan that has the skills feature turned on.

## Is it safe to run

This skill is plain instructions and nothing else. It declares no tools, makes no network calls, runs no scripts, and reads nothing beyond the text you give it. The whole skill is `SKILL.md` and `references/kill-lists.md`, both plain text you can read before you install.

Drafts are treated as material, not instructions: if a pasted text carries lines aimed at an AI, the skill edits them as prose and points them out instead of acting on them.

The bundle is rebuilt deterministically by `scripts/build_bundle.py`, and CI fails if `deslop.skill`, `SHA256SUMS`, and the sources drift apart or if hidden text appears in them. See `SECURITY.md`.

## The one rule that overrides the rest

Never invent specifics. When a draft needs a number, name, or example that the source material does not supply, the skill inserts a `[TODO]` marker instead of making one up. Fake specificity is worse than vague honesty.

## Rebuilding the bundle

After editing `SKILL.md` or `references/kill-lists.md`, rebuild the bundle and its checksum from inside the repo:

```bash
python3 scripts/build_bundle.py
```

`python3 scripts/build_bundle.py --check` verifies without writing; CI runs it on every push and PR. The zip is deterministic, so the same sources always give the same SHA-256.

## License

MIT. See `LICENSE`.
