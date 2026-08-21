# Skills

Two skills for Claude Code. Each one is a `SKILL.md` that tells Claude how to do the job, plus a `references/eval.md` checklist that Claude runs against its own output before it returns anything.

## better-writing

Edits a draft into clearer, more direct writing while keeping the writer's voice. It also runs in detect mode: name the AI patterns in a draft, quote the lines, suggest a fix, change nothing.

Orwell's six rules sit at the top and apply to every edit and to everything the skill writes itself. Below them sit a ban list (delve, leverage, robust, tapestry and the rest), metaphor nouns that hide a plain word (substrate, wedge, vector, flywheel), and the patterns that mark text as generated, such as binary contrasts, colon reveals, forced groups of three, fake-profound kickers, em dashes and inline-header lists.

Invoke it with `/better-writing` and paste the draft, or ask for a draft to be clearer, less AI-sounding, or audited.

## better-design

A set of evals for any work that touches an interface: web, mobile, desktop, marketing pages, design systems, generated UI images. Claude reads the full eval before designing, builds, then audits the rendered result against every point and fixes what fails.

The eval lists the recognizable defaults (component, copy, shadow, color, type, layout and motion tells), the execution failures that read as bugs (content hidden behind entrance animations, clipped descenders, nothing centered, unreadable forms), rules for mobile screens and redesigns, and what premium work does instead: a signature artifact, self-colored borders, springs that respond on press, licensed type.

It loads on its own for design work. The user's explicit direction beats any default in it.

## Install

Claude Code loads skills from `~/.claude/skills`. Link each folder there:

```bash
ln -s "$PWD/better-writing" ~/.claude/skills/better-writing
ln -s "$PWD/better-design" ~/.claude/skills/better-design
```

A symlink means edits here go live at once. A copy needs re-copying after each change.

## Layout

```
better-writing/
  SKILL.md            instructions Claude follows
  references/eval.md  checklist Claude runs on its own output
better-design/
  SKILL.md
  references/eval.md
```
