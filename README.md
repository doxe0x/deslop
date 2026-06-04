# deslop

A Claude skill that audits and rewrites text so it stops reading like AI.

The idea behind it: AI prose reads as AI because it is statistically average. Safe claims, generic transitions, neat symmetry, no real position, almost no concrete detail. Swapping out words like "delve", "leverage", and "robust" is the smallest lever. The skill works down five layers (vocabulary, filler phrases, structure, rhythm, tone) and pushes for the three things a model cannot fake on its own: specificity, a position the author actually holds, and rhythm.

## Contents

- `SKILL.md` — the skill itself. It runs in two modes: AUDIT (flag what reads as AI, with a sharper rewrite for each span) and REWRITE (produce a de-slopped version).
- `references/kill-lists.md` — the full vocabulary and phrase lists, the research behind them (the PubMed "delve" study, the detector-reliability findings), a crypto/DeFi note on which on-chain terms are real terms vs. slop, and a prompt pack for use in other models.
- `deslop.skill` — the same two files packaged for a one-step install.

## Install (Claude Code)

A skill is a folder containing `SKILL.md`. Put it where Claude Code looks, so that `~/.claude/skills/deslop/SKILL.md` exists. Two ways:

- Clone this repo into `~/.claude/skills/deslop`, or
- Unzip `deslop.skill` inside `~/.claude/skills/` (the archive already contains a `deslop/` folder).

Claude picks it up on requests like "does this sound like AI?", "de-slop this", "make it sound like me", or when writing prose that should not sound machine-generated.

## The one rule that overrides the rest

Never invent specifics. When a draft needs a number, name, or example the source material does not supply, the skill inserts a `[TODO]` marker instead of fabricating one. Fake specificity is worse than vague honesty.
