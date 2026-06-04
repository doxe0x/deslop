# Kill-lists, empirical basis, and prompt pack

This file backs the main SKILL.md. Read it when you need the exhaustive lists, the evidence behind them, or a ready-to-paste prompt for a different model (GPT, Grok, etc.).

## 1. The empirical basis (why these lists exist)

The vocabulary tells are not folklore. They were measured. Kobak, González-Márquez, Horvát, and Lause, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary" (*Science Advances*, 2025), analyzed 15.1 million PubMed abstracts from 2010-2024 using an "excess vocabulary" method. They found a step-function spike in 2024 style words. The largest frequency jumps (2024 frequency vs. the projected counterfactual) were "delves" (about 28x), "underscores" (about 14x), and "showcasing" (about 11x). Unlike earlier vocabulary spikes that were content words (during COVID: "respiratory", "remdesivir"), the 2024 excess was almost entirely style words. At least 13.5% of 2024 abstracts showed LLM fingerprints, rising to around 40% in some subfields. A companion study (Juzek and Ward, "Why Does ChatGPT 'Delve' So Much?") traced the cause to RLHF and human-evaluator feedback, not the training data, which is why the jump looks like "someone pulled a switch."

The root mechanics, in one paragraph: models predict the most likely next token, so they default to the safe middle of the distribution. RLHF (reinforcement learning from human feedback) then rewards agreeable, positive, balanced answers because annotators prefer them, which amplifies hedging and sycophancy. And alignment training induces "mode collapse" toward typical, familiar phrasings, which is why every output sounds like it came from the same seminar. Understanding this is the point: the tells are symptoms of averaging, so the cure is anything that moves the text off the average (specificity, position, rhythm).

On detectors, be honest and do not chase them. OpenAI withdrew its own AI Text Classifier in 2023 for low accuracy (it caught only about 26% of AI text while flagging about 9% of human text). Liang et al. (*Patterns*, 2023) found seven detectors falsely flagged about 61% of non-native English (TOEFL) essays, and nearly all essays were flagged by at least one detector. Vanderbilt and others disabled Turnitin's detector over false-positive risk. Detectors measure proxies (perplexity, burstiness), not truth. Improving those proxies improves writing, but a detector score is never a verdict.

## 2. Full vocabulary list (density is the signal, not any single word)

Inflated / abstract verbs:
> delve, delve into, leverage, harness, utilize, foster, navigate (figurative), underscore, bolster, unlock, unleash, embark, elevate, streamline, facilitate, showcase, illuminate, spotlight, unpack, shed light on, pave the way, dive into, spearhead, supercharge, amplify, catalyze

Inflated adjectives:
> robust, pivotal, crucial, vital, seamless, cutting-edge, innovative, transformative, game-changing, groundbreaking, comprehensive, multifaceted, intricate, nuanced (as empty praise), holistic, vibrant, meticulous, paramount, unparalleled, myriad, ever-evolving, fast-paced

"Borrowed grandeur" nouns:
> tapestry, landscape (figurative), realm, mosaic, ecosystem, beacon, cornerstone, bedrock, testament, symphony, journey, odyssey, fabric, paradigm, synergy

Signposting / connective slop:
> moreover, furthermore, additionally, notably, importantly, consequently, thus, hence (when ornamental)

Plain-word swaps:
> utilize -> use; facilitate -> help; leverage -> use; harness -> use; comprehensive -> full or complete; pertinent -> relevant; in order to -> to; due to the fact that -> because; a myriad of -> many; in the realm of -> in; navigate the complexities of -> handle or work through

Note on context: in crypto/DeFi some of these (ecosystem, unlock, protocol) are sometimes legitimate domain terms. The problem is still density. "ecosystem, unlock, robust, seamless, landscape" in one paragraph is slop; one accurate "unlock" referring to a token unlock is fine.

## 3. Full phrase list (delete-on-sight unless they carry real meaning)

> it's important to note that; it's worth noting that; in today's fast-paced world; in an increasingly complex/digital world; in a world where; let's dive in; let's unpack this; this raises important questions; the future holds many possibilities; at the end of the day; the result?; here's the thing; here's where it gets interesting; in conclusion; to sum up; needless to say; whether you're X or Y; from X to Y, Z is changing everything; when it comes to; this highlights; this underscores; this serves as a reminder; one thing is clear; only time will tell

Test for each: delete it. If the sentence still says what it said, the phrase was filler.

## 4. Structural patterns (the stronger tells)

- "It's not just X, it's Y" / "This isn't just A; it's B." Rewrite to a plain claim plus a reason.
- Triads on a metronome ("secure, transparent, efficient"). Vary the count.
- Fake symmetry / chiasmus ("X without Y is just P; Y without X is just Q").
- Rhetorical-question scaffolding ("So what does this mean for...?"). Answer it directly instead.
- Empty transition sentences ("Several interconnected factors are at play.", "The time to act is now.").
- Generic definitional intro + self-summarizing conclusion.
- Reflexive bulleting: every section a 3-5 item list with bold lead-ins of equal length.
- Title-case headings everywhere; uniform paragraph length; uniform sentence length.

## 5. Crypto / DeFi domain note: legitimate term vs slop

In crypto and DeFi writing, several words from the kill list are often precise technical terms rather than inflation. The whole question is whether the word points to a specific, checkable mechanism or is just decoration. Flag only the decorative use, and leave the technical use alone. The test for every instance is simple: ask "what exactly, and what number?" If the word survives that question it is a term; if it dissolves into vibe it is slop.

Legitimate when they name a real mechanism:
> ecosystem (only when naming an actual set of connected protocols or chains, not "the DeFi ecosystem" as backdrop); protocol (a named one, or the category used precisely); unlock (a token unlock or vesting cliff with a real date); liquidity (depth, pools, slippage, something measurable); yield (when tied to a number and a source); leverage (only as the literal financial term: borrowed exposure, a ratio, a liquidation level); bridge, oracle, validator, settlement, collateral, perp, funding (concrete infrastructure or instruments).

Slop when they are decoration (cut or replace):
> "the DeFi ecosystem/landscape" as scene-setting; "unlock opportunities / value / potential" (figurative unlock); "robust / seamless / secure infrastructure" with no number; "navigate the complexities of" anything; "transformative / revolutionary / next-generation protocol"; "harness the power of" anything; "vibrant community", "thriving ecosystem", "the future of finance".

The same word can be both in one paragraph. "The token unlock on March 3 adds 12% to circulating supply" uses "unlock" as a term. "This protocol unlocks new possibilities for users" uses it as slop. Keep the first, kill the second.

## 6. The portable prompt pack (for GPT, Grok, or any model)

These are ready to paste into another tool. They encode the same system as the skill.

### A. Style-extraction prompt (build a voice profile from samples)
```
Analyze these writing samples. Do not write new content. Build a style profile:
1. sentence-length patterns
2. paragraph rhythm
3. recurring words
4. words this writer avoids
5. how they open
6. how they close
7. how much context they assume
8. how they express uncertainty
9. what makes the voice specific
10. what would sound fake if added
[paste 10-20 samples]
```

### B. Anti-AI editor prompt (audit, do not polish)
```
You are editing for AI fingerprints, not for polish. Rewrite for specificity and voice.
Flag and fix: generic intro; empty transitions; symmetrical sentences; fake depth;
inflated vocabulary; repeated cadence; hedging without purpose; rule of three;
"not just X, it's Y"; any paragraph that repeats the previous one; any claim without an example.
For each issue: (1) quote the sentence, (2) say why it reads as AI, (3) give a sharper rewrite.
Do not invent facts. Where a specific is missing, mark [TODO].
```

### C. Specificity pass
```
Make this draft more specific. For every abstract claim ask: what exactly? according to whom?
what number? what mechanism? what example? what changed? what would make this false?
Only add details supported by the notes below. If the notes do not support a detail,
leave a [TODO] instead of inventing it.
[paste notes]
```

### D. Voice pass
```
Rewrite this as a slightly more thoughtful version of how I would say it out loud.
Rules: no corporate phrasing; no generic intro; no "it's important to note";
no "not just X, it's Y"; no neat three-part lists unless necessary; vary sentence length;
keep one rough edge if it helps voice; preserve the actual claim.
```

### E. Hard compression pass
```
Cut 30% of this draft.
Remove: throat-clearing; repeated ideas; transitions that add no information;
generic conclusions; sentences explaining things the audience already knows.
Do not remove: numbers; examples; caveats; strong claims; author judgment.
```

### F. "Make it less LinkedIn" pass
```
This sounds like LinkedIn. Fix it. Remove: motivational tone; grand claims;
leadership/innovation language; "future of" framing; safe both-sides phrasing;
inspirational ending. Make it sound like a smart operator explaining what is actually happening.
```

## 7. Sources

Primary research and credible voices, for refreshing the lists later:
- Kobak et al., "Delving into LLM-assisted writing..." (*Science Advances*, 2025) — the excess-vocabulary study.
- Juzek & Ward, "Why Does ChatGPT 'Delve' So Much?" — RLHF as the cause.
- Liang et al., "GPT detectors are biased against non-native English writers" (*Patterns*, 2023) — detector unreliability.
- Zhang et al., "Verbalized Sampling" (2025) — mode collapse and a generation-time fix (ask for several responses with probabilities, sample the tails).
- Wikipedia, "Signs of AI writing" — the best community field guide to patterns.
- Search Engine Journal, "This Writing Style Screams AI" — cadence as the primary tell.
- Ann Handley, "What AI Would Delete From Great Writing" — voice and "evidence of a mind behind the work".
- Dragonfly Editorial, "Beyond the Em-Dash Debate" — empty transitions as the real tell.
- Jeff Goins; Sean Kernan ("13 Signs You Used ChatGPT"); Atom Writer (the "statistical average problem").
- Strunk & White; Gary Provost (sentence-length variation, "write music"); Paul Graham ("Write Like You Talk", "Write Simply") — the pre-AI authorities the whole system rests on.
