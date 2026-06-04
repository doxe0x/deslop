---
name: deslop
description: Audit and rewrite text so it stops reading like AI. Use this whenever the task involves checking a draft for AI tells, removing AI "slop" from generated text, making writing sound human, editing an article/post/note/email for voice, or writing something new that should not sound machine-generated. Trigger it for any request like "does this sound like AI", "make this less AI", "de-slop this", "humanize this draft", "edit for voice", "rewrite this so it sounds like me", or when producing original prose (posts, articles, analysis) that needs to avoid the generic AI register. Apply it even when the user does not say the word "AI" but is clearly asking for writing to sound sharper, more specific, or more human.
---

# Deslop: making text stop sounding like AI

## The core idea (read this first)

AI text does not read as AI because of one word or one em-dash. It reads as AI because it is **statistically average**: correct structure, safe claims, no real position, generic transitions, too much symmetry, and almost no concrete detail. The model writes the mean of everything ever written on the topic. Competent, and dead.

So the fix is not a "humanize" button or a word-swap. The fix is to add the three things a model cannot generate on its own and then break the patterns it falls into by default:

1. **Specificity** the model does not have (real numbers, names, dates, mechanisms, first-hand observation).
2. **A position** the author actually holds (what they think, not "there are several factors").
3. **Rhythm and friction** that a person produces and a model smooths away.

Everything below serves those three. Vocabulary cleanup matters, but it is the smallest lever. If a rewrite only swaps words and keeps the average-internet shape, it has failed.

**One hard rule that overrides everything: never invent specifics.** When a draft needs a number, name, or example and the source material does not supply it, do not fabricate one. Insert a `[TODO: specific figure/example]` marker and tell the user what is missing. Fake specificity is worse than vague honesty, and for analytical or factual work it is a serious failure.

## Two modes

This skill runs in one of two modes. Decide which the user wants; if unclear, default to AUDIT and offer REWRITE.

- **AUDIT** — Scan a draft and report what reads as AI, without rewriting the whole thing. Output: a list of flagged spans, each with (a) the quoted text, (b) a one-line reason it reads as AI, (c) a sharper rewrite. End with the two or three highest-leverage fixes, not every nitpick.
- **REWRITE** — Produce a de-slopped version, either by fixing a supplied draft or writing something new. Follow the rewrite workflow below. Show the result, and briefly note the main changes and any `[TODO]` markers where specifics are needed.

## What to flag: the five detection layers

Work down from the layer that matters most. The lower layers (structure, rhythm, tone) are stronger tells than the top one (vocabulary), and most people over-index on vocabulary.

### Layer 1 — Vocabulary (weakest tell, easiest fix)
Flag clustered AI-favored words. No single one is banned; **density is the signal**. If a paragraph stacks several, clean it.
> delve, leverage, harness, utilize, foster, navigate (figurative), underscore, bolster, unlock, unleash, embark, elevate, streamline, facilitate, showcase, illuminate, spotlight, pave the way, robust, pivotal, crucial, vital, seamless, cutting-edge, innovative, transformative, game-changing, groundbreaking, comprehensive, multifaceted, nuanced (as empty praise), holistic, meticulous, paramount, tapestry, landscape (figurative), realm, ecosystem, mosaic, beacon, cornerstone, testament, symphony, journey, fabric

Swap for plain words: utilize→use, facilitate→help, leverage→use, comprehensive→full, pertinent→relevant, in order to→to, due to the fact that→because. See `references/kill-lists.md` for the full list and the empirical basis.

### Layer 2 — Filler phrases (almost always deletable)
These add no information. The test: delete it; if the meaning survives, it was slop.
> "it's important to note", "it's worth noting", "in today's fast-paced world", "in an increasingly complex landscape", "let's dive in", "let's unpack this", "this raises important questions", "at the end of the day", "here's the thing", "here's where it gets interesting", "the result?", "in conclusion", "to sum up", "needless to say", "moreover", "furthermore", "additionally" (when not needed)

### Layer 3 — Structure (strong tell)
- **The negation frame: "it's not just X, it's Y."** The single most recognizable AI structure. Roughly one per paragraph in generated text. Rewrite into a plain claim with a reason.
- **The rule of three / triads.** "faster, cheaper, more scalable." One element is fine, three on a metronome is a tell. Use one, or two, or four. People do not count their lists into clean threes.
- **Fake symmetry.** "Strategy without execution is just planning. Execution without strategy is just activity." Reads like a LinkedIn fortune cookie. Cut or make it real.
- **Rhetorical-question scaffolding.** "So what does this mean for investors?" → just say it: "For investors, the main risk is dilution."
- **Empty transition sentences.** "The time to act is now." "Several interconnected factors are at play." Moves the text without adding information. Delete.
- **Generic intro + summary conclusion.** Opens with a definition or broad context, closes by restating itself. Cut the throat-clearing first paragraph and the recap last paragraph; the draft usually gets 20-40% shorter and better.
- **Listicle-itis.** Every section becoming a 3-5 item bulleted list with bold lead-ins of equal length. Break it into prose where the content is an argument, not an inventory.

### Layer 4 — Rhythm and cadence (strong tell, often missed)
Cadence is now a bigger giveaway than punctuation. Flag:
- Five paragraphs in a row of the same length.
- Every sentence roughly the same length (all 17-24 words). Human writing varies hard: a long winding sentence, then a short one that lands.
- Every line trying to be a punchline ("The result? Devastating." / "Not X. Not Y. Just Z."). That is TED-talk / sales-page rhythm, not writing.
- Every list item built on the same template.
Fix by varying sentence length on purpose: drop in a three-word fragment, then let one sentence run long, then a normal one. Read it aloud; if it has a uniform beat, intervene.

### Layer 5 — Tone (the deepest tell)
- **Too balanced.** Fake "both sides" when the position is obvious. "There are both opportunities and challenges." Replace with the actual call: "The opportunity is real, but the unit economics do not work unless fees fall another 60-70%."
- **Too safe.** Hedging away from any sharp claim. "This could potentially create some concerns." → "Users are underwriting the risk, and the docs do not say it plainly."
- **Too polished.** Perfectly smooth text reads dead. Human text has a short aside, an unexpected example, a stated doubt, a small qualification, normal unevenness.
- **No mind behind it.** The deepest problem (Ann Handley's point): good writing shows the author saw something, decided something, rejected something, has taste. AI gives competent prose with no judgment in it. If the draft could have been written by anyone about anything, that is the tell.

## What makes text human: the fixes

For every flag, reach for one of these. They are listed by power.

1. **Specificity.** The strongest human signal. Replace abstractions with numbers, names, dates, product names, exact quotes, a real example, "I thought X, then Y changed my mind", what specifically was surprising, what does not add up. Weak: "This protocol has strong potential." Human: "The interesting part is not the 12% headline APY. It is that 7% comes from emissions that unlock before the next borrow-cap review." (Never invent these — see the hard rule. Mark `[TODO]` if absent.)
2. **Position.** Answer the question "what does the author actually think?" Weak: "There are several factors to consider." Human: "I would not size this as yield. I would size it as an airdrop option with yield attached."
3. **Friction.** People write through disagreement. "This part is weird." "I don't buy this." "The docs say X, but the incentives point to Y." AI smooths everything into one agreeable shape; put a bump back in.
4. **Voice from speech.** The text should read like a slightly more thoughtful version of how the author talks, not like a different, more corporate person. Test: would they say this in a voice note? If not, rewrite. If they would not say "leverage" out loud, do not write it.
5. **Real progression.** Each paragraph must add a new idea, not rephrase the last. Good writing goes somewhere; by the end the reader thinks differently, not just receives a tidy summary. AI often says one thing ten ways.

## REWRITE workflow

When fixing a supplied draft, run these passes in order. (When writing fresh, start at "Before generation" below, then draft, then run these passes on your own output.)

**Before generation (if writing new):**
- Do not start from "write about X." Start from a position and an audience. Bad: "Write an article about AI writing." Good: "Argue that AI writing fails because it removes the writer's judgment, not because of bad punctuation. Audience: crypto-native readers who see too much generic content. Use concrete examples, no moralizing, no generic intro."
- If raw material exists (notes, theses, examples, the user's own take), organize that. Do not invent an argument the user did not give.
- Pick one sharp claim, not a topic. Structure as an argument, not Intro / Benefits / Challenges / Conclusion.

**Pass 1 — Delete.** Remove the generic first paragraph, the summary last paragraph, every filler phrase from Layer 2, and any paragraph that restates an earlier one. Most drafts lose 20-40% here and improve.

**Pass 2 — De-template.** Hunt the Layer 3 structures: "not just X", "from X to Y", "whether X or Y", rhetorical questions, triads, identical headings, identical paragraph lengths. Break the symmetry.

**Pass 3 — Add evidence.** On every significant claim, add one concrete thing: a number, an example, a comparison, a failed assumption, a first-hand observation. Only from the source material; mark `[TODO]` where it is missing rather than inventing it.

**Pass 4 — Voice.** Rewrite anything the author would not say aloud. Allow "And"/"But" openers, short sentences, normal rhythm, one rough edge if it helps. Preserve the actual claim.

**Pass 5 — Anti-slop scan.** Search the text for the Layer 1 words and the Layer 2 phrases. Do not auto-delete everything, but if density is high, clean it. Confirm the rhythm varies and the tone takes a position.

Do not make it more polished. Make it more specific.

## The division of labor (the principle that keeps this honest)

AI should help with **structure, options, compression, finding weak spots, and edits**. It should not supply the **judgment**. Good uses: "give me 5 angles", "find the generic claims", "cut 30%", "reformat", "run an anti-slop pass". Bad uses: "write my opinion for me", "make it sound human", "add personality", "make it engaging", "make it viral" — those just take the average internet and make it glossier. When a request is one of the bad ones, redirect: ask for the user's actual take, then organize it.

## Applying a target voice (optional)

By default, preserve the voice already in the draft and only strip the AI patterns above. Do not impose a house style the author did not ask for, and do not "upgrade" plain true sentences into polished ones. Plain is allowed.

When a specific voice is wanted, ask for two or three writing samples (or explicit rules) and extract the profile before rewriting: sentence-length pattern, how the author opens and closes, words they use and avoid, how they express uncertainty. The style-extraction prompt in `references/kill-lists.md` does this. If the user gives their own rules, have them phrase the rules as direct first-person statements ("I lead with the claim", "I don't use em-dashes", "I end on one line") rather than third-person description; models follow first-person rules more reliably.

A few guardrails are close to universal and safe to apply even without a sample, because they remove slop rather than impose taste:
- Open on the first real line. Cut throat-clearing and setup paragraphs.
- Prefer specifics (numbers, names, mechanisms) over abstractions.
- End on one line, not a stack of clever closers.
- Drop the engagement-bait closing question ("What do you think?") unless the user wants it.
- Em-dash overuse is a common tell; if the target voice does not lean on em-dashes, prefer periods, commas, or parentheses.
- The voice-note test: if the author would not say a line out loud, rewrite it.

## Honest caveats (state these; do not overcorrect)

- **No word or structure proves AI.** These are frequency patterns, not laws. People legitimately use em-dashes, triads, and "delve". The diagnostic is clustering and density. Hold conclusions loosely.
- **Do not chase AI detectors.** They are unreliable: OpenAI withdrew its own classifier (26% true-positive rate), and detectors falsely flag non-native English writers at very high rates (one study: 61% of TOEFL essays). Write genuinely better; do not optimize for a detector score.
- **Do not add fake humanity.** No random slang, no deliberate typos, no manufactured "imperfections". Human texture comes from specificity, position, and rhythm, not from sprinkled errors.
- **The tells move.** Vocabulary shifts across model generations, and humans now copy AI words back into their own writing. Refresh the lists periodically rather than trusting them forever.
- **Plain is allowed.** The goal is specific and honest, not ornate. Do not "improve" plain true sentences into fancier ones; that is the direction that creates slop.

## Reference files
- `references/kill-lists.md` — the full vocabulary and phrase lists, the empirical basis (the PubMed "delve" study and detector-reliability findings), a crypto/DeFi domain note on which on-chain terms are legitimate versus slop, and a portable prompt pack (style-extraction, anti-AI editor, specificity pass, voice pass, compression pass, "make it less LinkedIn") for use in other models. Read it when you need the exhaustive lists, when editing crypto/DeFi text, or when setting up a reusable prompt for a different tool.
