---
name: better-design
description: Apply the user's complete design evals to any task that creates, changes, evaluates, or ships a visual interface, including web, mobile, desktop UI, marketing pages, landing pages, design systems, components, screenshots, generated UI imagery, and visual QA. Use for design work, frontend implementation, UI refactors, interface reviews, and pre-ship visual checks. Do not use for backend-only, data-only, documentation-only, or other work that cannot affect an interface.
---

# Better Design

The full evals live in [references/eval.md](references/eval.md).
They are applicable to any work that touches an interface, new or existing.

## Workflow

1. Read references/eval.md in full before designing or implementing.
   Do not work from this summary or from memory.
2. Tell the user you have read it and will audit the finished work against
   every point.
3. Decide the interface's audience, purpose, design world, and signature
   artifact before choosing components or styling. For a redesign, decide
   preserve, overhaul, or greenfield first and audit the existing site
   before touching it.
4. Build the interface as one coherent composition: content visible by
   default, legible contrast, deliberate alignment, working controls,
   purposeful motion.
5. Exercise real interactions with pointer and keyboard. Check both themes,
   phone, tablet and desktop widths, and reduced motion. Zoom into every
   clipped, overlapping, centered, fixed-height, or animated edge.
6. Before delivery, read the evals again and audit the rendered result point
   by point, not the source code alone. Fix every failure.
7. In the final response, confirm the audit ran, name the material fixes it
   caused, and disclose anything you could not verify.

## Rules

- Use only the few premium techniques that fit one coherent design world;
  never run the kit as a checklist.
- A library, template, or existing code using a banned default is not a
  license to keep it.
- Never hide content behind an entrance animation; a failed animation must
  never make content disappear.
- Never ship a control that looks interactive but does nothing.
- Respond on press, not release. Every transition can be interrupted and
  starts from the element's current on-screen value.
- Re-read every visible string before shipping; copy is part of the
  interface.
- The user's clear, task-specific direction beats any default in the evals.
