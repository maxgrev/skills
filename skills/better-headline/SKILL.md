---
name: better-headline
description: Write, rewrite, compare, or critique headlines for articles and long posts, especially X Articles. Use when a user wants title options for a draft, a stronger headline, or help choosing between headlines. Grounds X-specific advice in a dated research sample and checks that each promise matches the content. Also writes the first two preview lines when requested. Use for the headline itself; full sales copy, email campaigns, UI labels, and general prose edits need broader guidance.
---

# Better Headline

Write a headline that gives the intended reader a clear reason to open the piece. Start with the value in the article. Preserve its facts, subject, audience, and voice.

This skill draws on *how to write better headlines* by @fuckgrowth, dated September 28, 2026, and its linked research and tools. The bundled sample covers X Articles posted January 1 through September 26, 2026. Its patterns guide choices on X; they do not establish rules for every channel or predict a new article's views.

## Choose the job

- **Write or rewrite:** Generate distinct angles, check them, and recommend the strongest truthful option.
- **Compare:** Read the supplied headlines against the same draft and audience. Explain the main difference and choose one. Create alternatives only if requested or needed to fix a shared flaw.
- **Critique:** Quote the weak wording, name its cost to the reader, and give a concrete fix. Respect requests for diagnosis without a rewrite.
- **Headline and preview:** Choose a headline, then write the opening with [references/hooks.md](references/hooks.md).

Keep the user's requested scope and number of options. A request for one headline should receive one headline, even if you explore more internally.

## Establish what the article earns

Read the draft or extract these facts from the brief:

- reader and their reason to care;
- channel and length or style limits;
- subject, named tools or people, and what the reader already knows;
- useful outcome, finding, argument, or story;
- supported numbers, results, timeframes, and first-person experience;
- actual depth: overview, experiment, tutorial, complete setup, or something else;
- voice and any wording the user wants to keep.

Ask only for missing information that would change the result. If a draft supplies it, proceed. When the brief supports a useful title without extra facts, write it without those facts.

State the value internally in one plain sentence: "After reading this, the reader can ___" or "The reader will understand ___." Then explain the subject in a few words a person with no context could follow. If neither answer works, identify the missing value before polishing the title. Suggest a concrete article fix; do not add a result the draft lacks.

## Use the references where they help

- For X Articles, read [references/research.md](references/research.md) before scoring or making claims about performance. It defines the seven move families, the failure marks, and the limits of the evidence.
- For substantial generation, read [references/patterns.md](references/patterns.md). It holds shapes, exact source examples, and failures. For another channel, use the craft guidance while treating the X figures as context.
- For X Articles, sample relevant rows with [scripts/find_examples.py](scripts/find_examples.py). Filter to the topic, look at several strong headlines, then check examples from smaller accounts. Use their decisions as examples; preserve the user's subject and write fresh wording.
- Read [references/hooks.md](references/hooks.md) when the preview or first two lines are in scope.
- Before delivering, read [references/eval.md](references/eval.md), fix the failures, and check again.

Resolve script and reference paths relative to this skill's directory. Both helpers use Python 3's standard library and work without network access. Do not load the whole CSV into the conversation.

```bash
python3 scripts/find_examples.py --topic Marketing --limit 6
python3 scripts/find_examples.py --topic AI --small-accounts --limit 6
python3 scripts/find_examples.py --topic Career --levels L1 L2 L3 L4 --limit 6
```

The CSV contains 6,835 articles above 100k views. The negative examples and comparison rates come from the research, not this winner-only export. The snapshot cannot establish what is trending now. If current popularity matters, use recent evidence or the user's facts; otherwise use the relevant name already in the draft.

## Develop distinct candidates

For a substantial writing request, explore at least ten candidates internally. Change the reason to read: usable result, demonstrated result, mechanism, resource, finding, argument, story, or real announcement. A list that swaps adjectives around one idea does not count as ten angles. Keep fewer when the task is a small edit or comparison.

For X, favor clear promises and supported specifics. Aim for L3 or L4 when the article naturally supplies the moves. Let the material decide which shape fits:

- How-to: an action the article teaches.
- Guide or resource: the useful scope the article covers.
- First-person result: something the author actually did.
- Announcement: something genuinely being introduced.
- Direct finding, claim, or story: an editorial piece whose value is not a tutorial.

Name a tool, person, or company when it helps readers recognize the subject. Add a timeframe only when it describes a real duration or supported path. Distinguish the author's result from a result promised to every reader. Add a completeness tag only when the piece supplies the full steps or resources for the stated scope.

Keep the promise visible. Curiosity may hold back the answer, method, or story ending while making the subject and value clear. Cut generic labels, filler, stale recap framing, forced questions, and inflated claims when a direct title serves the reader better. Preserve a question, explanation, recurring-series name, or other form when it serves the user's actual purpose.

Use plain words, concrete verbs, and the user's voice. Keep proper names spelled correctly. Do not add title case, all lowercase, an emoji, a colon reveal, a binary contrast, or a dramatic fragment as a default style. Read the shortlist aloud. Length matters when it affects clarity or the channel limit, not because nine words is a magic target.

## Check patterns, then judge the promise

For X candidates, run [scripts/headline_check.py](scripts/headline_check.py):

```bash
python3 scripts/headline_check.py "How to plan a month of content with Claude"
python3 scripts/headline_check.py --file candidates.txt --names "Acme,Notion" --json
```

Put one candidate per line in a UTF-8 file. The checker reports the matched families, L0-L4, failure marks, names, and length. Custom names appear as relevance signals; they do not inherit the measured effect of the historical AI-tool family.

The level counts wording patterns. It cannot judge truth, completeness, relevance, or whether the article delivers. L4 can still carry a failure mark. Inspect those separately, and never turn the level into a quality score or a forecast. The example finder shows the source's stored tags; the checker uses the documented definitions with the matching changes noted in the research reference, so their levels can differ.

Reject unsupported candidates first. Among the rest, choose by reader value, fit to the article, clarity, voice, and then useful pattern strength. A sound L2 title can beat a strained L4. A failed regex match can still describe a useful idea; judge the actual text.

## Return usable copy

Lead with the recommended headline. For an open-ended request, show up to five strong alternatives with different angles and a brief reason for the choice. For a comparison or critique, give the decision or findings first. Show levels and matched moves only when they help the user compare options or the user asks for them.

If requested, put the first two lines directly below the chosen headline. Mention only material assumptions. Do not require an approval round to finish a writing task.

Apply the user's feedback to the current work. Save feedback or results only when the user asks to keep a record, and use their chosen location. Compare real results across several posts before drawing a lesson from them.
