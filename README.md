# Skills

Two skills in the [Agent Skills](https://agentskills.io) format. They work with any agent that reads a `SKILL.md`: Claude Code, Codex, Cursor, Zed, Warp, Cline and the rest.

Each skill is a `SKILL.md` the agent follows, plus a `references/eval.md` checklist it runs against its own output before returning anything. The checklist is the point. Telling an agent to "write well" or "avoid slop" does little, but a list of named patterns it must check itself against works.

## The skills

- **[better-writing](skills/better-writing/SKILL.md).** Edits a draft into clearer, more direct writing while keeping the writer's voice. Also runs in detect mode: name the AI patterns in a draft, quote the lines, give the fix, change nothing. Orwell's six rules sit on top. Below them, a ban list (delve, leverage, robust, tapestry), metaphor nouns that hide a plain word (substrate, wedge, vector, flywheel), and the patterns that mark text as generated, such as binary contrasts, colon reveals, forced groups of three, fake-profound kickers, em dashes and inline-header lists.
- **[better-design](skills/better-design/SKILL.md).** Evals for any work that touches an interface: web, mobile, desktop, marketing pages, design systems, generated UI images. The agent reads the full list before designing, builds, then audits the rendered result point by point and fixes what fails. It covers the recognizable defaults (component, copy, shadow, color, type, layout and motion tells), the failures that read as bugs (content hidden behind entrance animations, clipped descenders, nothing centered, unreadable forms), mobile screens, redesigns, and what premium work does instead: a signature artifact, self-colored borders, springs that respond on press, licensed type.

## Install

One command, any agent:

```bash
npx skills add maxgrev/skills
```

The CLI asks which skills and which agents, then symlinks each skill into the agent's skills folder. Add `-g` to install for all your projects rather than the current one, and `--copy` where symlinks will not work.

One skill, one agent, globally:

```bash
npx skills add maxgrev/skills --skill better-writing -g -a claude-code
```

### By hand

Clone the repo and link or copy each skill folder into the agent's skills directory.

| Agent | Project | Global |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.codex/skills/` |
| Cursor | `.agents/skills/` | `~/.cursor/skills/` |
| Zed, Warp, Cline, Amp | `.agents/skills/` | `~/.agents/skills/` |

The [skills CLI README](https://github.com/vercel-labs/skills#supported-agents) lists the other agents.

```bash
git clone https://github.com/maxgrev/skills.git
cd skills
ln -s "$PWD/skills/better-writing" ~/.claude/skills/better-writing
ln -s "$PWD/skills/better-design" ~/.claude/skills/better-design
```

A symlink picks up edits at once. A copy needs re-copying after each change.

## Use

Once installed, the agent loads a skill when the task matches its description. You can also ask for it by name:

> Use better-writing on this draft.

> Use better-design and review the landing page before we ship.

In Claude Code, `/better-writing` also works.

## Layout

```
skills/
  better-writing/
    SKILL.md            what the agent does
    references/eval.md  what it checks its output against
  better-design/
    SKILL.md
    references/eval.md
```

## License

MIT.
