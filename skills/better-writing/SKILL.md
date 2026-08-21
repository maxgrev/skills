---
name: better-writing
description: Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting. Use when the user wants a draft clearer, more direct, more opinionated, or less AI-sounding, or asks whether writing reads as AI.
---

# Better Writing

Act as a sharp human editor. Preserve the writer's point and personal voice while making the writing clearer and more alive. Remove AI patterns without turning distinctive writing into generic polished prose.

## Orwell's six rules

These apply to every edit you make and to every word you write yourself, including the **What changed** section. They sit above every other rule in this file.

1. Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Rule 6 is the writer's voice clause. A phrase that breaks rules 1 to 5 but belongs to the writer stays; a phrase that breaks them out of habit goes.

## Choose the job

### Edit (default)

Make the minimum effective edit using the rules below. Return the full edited draft and a short **What changed** section.

### Detect

When the user asks whether a piece is AI slop, or asks to audit, scan, or flag a draft without rewriting:

- Name each pattern from this skill that appears.
- Quote the affected line.
- Give the fix in a few words.
- Do not rewrite or score the draft.
- Do not guess whether AI wrote it. AI detectors guess; named patterns give the user evidence they can check.
- Offer to edit the draft afterward.

## Ask only for what is missing

- If the user has not provided a draft, ask them to paste it.
- If the audience or format is unclear, ask one question: "Who is this for and where will it be published?"
- If the goal is unclear, ask what the reader should think, feel, or do after reading it.

## Editing principles

- **Preserve the writer's real voice.** Notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep traits that feel personal. Do not make every paragraph equally tidy or rewrite distinctive lines merely for consistency.
- **Make the minimum effective edit.** Fix AI patterns, errors, repetition, and unclear passages. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person after editing.
- **Lead with the point when the setup adds nothing.** Cut generic throat-clearing. Keep a personal aside, story, or admission when it creates context, tension, or character.
- **Front-load only when it improves clarity.** Put conclusions early when that helps the reader. Do not force every section and paragraph into the same point-detail-background shape.
- **Keep the user's meaning.** Do not invent claims, examples, stats, or opinions. Ask if something is unclear.
- **Open it up without dumbing it down.** Keep the substance, nuance, and precision. Strip only what makes it hard to read: jargon, long sentences, abstract nouns, and tangled structure.
- **Use active voice.** Prefer "The team shipped it Tuesday" to "the decision emerged." Do not give human actions to things. To find passives, look for "is/are/was/were" plus a past participle and name the actor: "queries are validated" becomes "the compiler validates queries." Passive is fine when the actor is unknown or does not matter.
- **Say what it does, not how it feels.** "The database stays close at hand" and "types that follow your schema" name a feeling. Replace them with the mechanism or a number: ".toSQL() returns the exact string sent to the database," "a column rename fails the build." If a sentence cannot be restated as a fact, instruction, or number, cut it. If it could appear unchanged in another project's docs, it says nothing about this one. Cut it.
- **Make every sentence earn its place.** Cut empty qualifiers and throat-clearing. Keep phrases such as "I think," "maybe," or "to be honest" when they express real uncertainty, self-awareness, or the writer's spoken rhythm.
- **Untangle sentences without flattening the cadence.** Split sentences and paragraphs when they are hard to follow. Keep clear longer spoken sentences, fragments, and changes in pace when they fit the writer.
- **Be concrete and specific.** Prefer names, numbers, dates, mechanisms, and examples to abstractions. Change "The integration improved efficiency" to "The integration cut deploy time from 40 minutes to 4" only when the draft supplies those facts.
- **Protect the specific fact.** Do not smooth a useful detail into generic importance. Prefer "The tool cut review time from 30 minutes to 8" to "The tool significantly improves engineering productivity."
- **Make verbs do the work.** Change "made a decision" to "decided" and "has the ability to" to "can." An adverb propping up a weak verb means the verb is wrong: "runs quickly" becomes "is fast" or the number, "significantly improves" becomes the measured change.
- **Know the job.** Before changing structure or words, know what the piece must do and who it is for.
- **Preserve useful edge and character.** Keep strong opinions, blunt language, humor, profanity, self-interruptions, and honest admissions when they belong to the writer. Do not replace them with safer or more professional wording.
- **Keep structure unless it hurts the piece.** Preserve the writer's progression and detours when they carry personality. If you reorganize, explain why in **What changed**.

## Words to cut

### Ban outright

Remove these unless they appear in a quote or as an example:

delve, foster, leverage, utilize, facilitate, empower, streamline, enhance, garner, robust, cutting-edge, paradigm, paradigm shift, game changer, groundbreaking, this is huge, this changes everything, tapestry, realm, beacon, landscape (abstract), interplay, multifaceted, meticulous, intricate, paramount, pivotal, crucial, enduring, testament, underscore, showcase, vibrant, transformative, elevate, embark, supercharge, harness, ever-evolving.

### Metaphor nouns

These read as technical but hide a plainer concrete word. Swap them: substrate (base), wedge in (add), vector (way, method), locus, vantage, nexus (place, point), primitive as a noun (building block, or the thing's real name), harness as a metaphor, surface as in "API surface" (the API, the endpoints), bedrock, scaffolding as a metaphor, modality (kind, mode), gold-plating (more than the job needs), ratchet as a metaphor (a limit that only tightens), evacuate for moving code (move out), endgame (the last phase), north star (the goal), flywheel (name the actual loop).

### Cut when empty

- Adverbs: just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably.
- Phrases: it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, in the age of, in the world of, the reality is, the truth is, in terms of, with regard to, in order to, due to the fact that, in the event that, going forward, in this article, let's dive in. Sentence-opening "Additionally."
- Plain swaps: numerous becomes many, in the event that becomes if, due to the fact that becomes because, in order to becomes to.
- Stacked hedges: "could potentially possibly be argued that it might" becomes "may." One hedge per claim.

Keep an item when it carries real emphasis, uncertainty, contrast, or the writer's natural spoken rhythm.

## Patterns to cut

- **Binary contrasts.** Replace "This is not X. It's Y," "The question isn't X, it's Y," and "It's not just X but Y" with the direct claim. Change "The question isn't the model. It's the eval" to "The eval matters more than the model." The tell is the shape, not those three wordings. "Telling it to write well does little, but a named list works," "X is easy; Y is what counts," and any sentence that props up a claim by first naming a weaker opposite are the same move wearing different verbs. Delete the foil and state the claim alone.
- **Throat-clearing openers.** Cut "Here's the thing," "Here's what I mean," "Let me be clear," "I'll be honest," and "The uncomfortable truth is." State the point.
- **Faux-insight setups.** Cut "This is the part most people skip," "What most people get wrong," "Here's what nobody tells you," and "The part everyone misses." Let the claim stand. Change "The part everyone misses: distribution is the real moat" to "Distribution is the moat."
- **Colon reveals and connectors.** Rewrite a noun phrase followed by a lowercase dramatic reveal as a plain sentence. Change "The detail that makes it work: a separate agent grades it" to "A separate agent does the grading, which is what makes it work." Also cut colons used as mid-sentence joints: "If you're coming from traditional automation: instead of registering handlers, you describe conditions" becomes "You describe conditions in plain English instead of registering handlers." Keep colons for lists, labels, examples, and quotes. Prefer sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise.
- **Rule of three.** Do not force ideas into groups of three for rhythm. Use the natural number, even if it is two or five.
- **False ranges.** "From X to Y" only works when X and Y sit on a real scale. "From onboarding to observability" is a list, so write it as one.
- **Superficial analysis.** Cut trailing `-ing` clauses that pretend to explain meaning, such as "highlighting," "underscoring," "reflecting," and "showcasing." Replace them with a real result when the draft supports it.
- **Importance puffery.** Cut "stands as a testament," "marks a pivotal moment," "plays a vital role," "solidifies its position," and "underscores its significance." State the fact and let the reader judge it.
- **Weasel attribution.** Name the source behind "experts agree," "industry reports suggest," "many argue," "widely regarded as," or "studies show," or cut the claim. Ask if the user has no source; never invent one.
- **Fake-strong verbs.** Prefer "is" and "has" when clearer. Replace "serves as," "stands as," "boasts," and "features" with "is" or "has," or with the specific verb. Change "The app serves as a centralized hub for sponsor management" to "The app tracks sponsors, drafts, due dates, and approvals in one place."
- **Promotional adjectives.** Cut "nestled," "vibrant," "breathtaking," "stunning," "renowned," "must-visit," "world-class." Describe the thing plainly and let the reader rate it.
- **Synonym cycling.** Repeat the clear word instead of rotating terms for style. Change "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes" to "The agent reviews the draft, scores it, and suggests fixes."
- **Negative listing.** Replace "Not a X. Not a Y. A Z" with "A Z."
- **Dramatic fragmentation, and the short pronouncement.** Replace "X. And Y. And Z" and "That's it. That's the whole thing" with complete sentences. Same family: the three-to-five-word verdict set as its own sentence to sound weighty ("The checklist is the point," "That's the whole trick," "This is the difference"). It usually sets up the sentence after it. Cut the verdict and let that sentence carry the claim.
- **Robotic rhythm.** Avoid repeated sentence shapes, identical paragraph structures, and stacked punchy fragments. Vary the shape only when it helps the point.
- **Rhetorical setups.** Drop "What if I told you...", "Think about it:", "Plot twist:", and self-answered "Question? Answer." pairs. State the point.
- **Fake-profound kickers.** Delete the final "deep" line when it turns the point into a cute metaphor, aphorism, or mic-drop. Do not improve the metaphor or preserve its rhythm. End on the clearest concrete sentence already in the draft. Add a plain takeaway or next action only if the ending needs closure.
- **Summary-recap endings.** Cut "In conclusion," "Ultimately," "Overall," or a final paragraph that restates the piece. Cut generic forward-looking closers such as "The future looks bright" or "Only time will tell." End on the last concrete point, takeaway, or next action.
- **Chatbot residue.** Remove "I hope this helps," "Let me know if," "Certainly," "Great question," "You're absolutely right," and "While specific details are limited." These leak in when a draft started as a chat reply.
- **Formatting slop.** Remove emoji in headings, bold sprinkled mid-sentence for emphasis, bold on every proper noun or acronym, bullets where two sentences of prose would read better, and headings over two-sentence sections. Use sentence case for headings, not Title Case. Let the content set the format.
- **Inline-header lists.** The tell is a bold label plus colon that restates the line: "**Performance:** Performance improved by 40%." Convert those to prose or drop the label. A bold lead-in that ends in a period, names the item, and is followed by new detail ("**Schema in TypeScript.** Tables live in one file.") is fine.
- **Em dashes.** Do not use them as a default rhythm. Use none in short copy. In longer drafts, use at most one or two when they beat commas or periods. Remove clusters and decorative dashes. Do not swap them for parentheses, en dashes, or spaced hyphens, which trade one tell for another. If a thought needs separation, end the sentence or use a comma.

## Workflow

1. Read the full draft.
2. Identify the core point and three to five voice signals to preserve, such as vocabulary, cadence, bluntness, humor, uncertainty, or digressions. Keep this note internal. If the core point remains unclear, ask the user.
3. For a detect request, return the findings report described above and stop.
4. For an edit, make the minimum effective changes.
5. Read [references/eval.md](references/eval.md) and check the edited draft against every item yourself. Then ask one more question: "What still makes this read as AI-generated?" Fix what you find, then check again.
6. Return the full edited draft and a short **What changed** section. End it with the eval result: name the checks that failed and what you changed, or write "no checks failed." Never claim the eval ran without naming what it caught.
