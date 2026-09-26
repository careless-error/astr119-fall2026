# ASTR-119 course repository (Fall 2026)

This is your working folder for ASTR-119, Introduction to Scientific Computing, at UC Santa Cruz. You cloned it into `astr119` in your home folder during setup. Everything you write for this course lives here, and git keeps a history of it.

## What is in it

| Folder or file | What it is for |
|---|---|
| `module-1/` | Setup and first scripts (Sep 24 to Oct 8). Your comet script, `quadratic.py`, HW1. **AI-free.** |
| `module-2/` | Loops, lists, functions (Oct 13 to 22). Pod work on exoplanet temperatures, HW2. |
| `module-3/` | numpy arrays and tables (Oct 27 to Nov 5). HW3, the pixel fixer, with its test images. |
| `module-4/` | Plotting and fitting (Nov 10 to 19). HW4, HW5 with the MaNGA galaxy catalog. |
| `module-5/` | How a language model works (Nov 24 to Dec 3). Files arrive later. |
| `project/` | Your final project: proposal, code, report, AI-use log. |
| `data/` | Shared data sets added during the quarter. |
| `docs/` | The Protocol on one page, the AI-use note template, how to export a transcript. |
| `environment.yml` | The list of Python packages the course uses. The setup guide used it to build the `astr119` environment. |
| `CLAUDE.md` | Rules the AI agent follows in this repository. Read it; do not edit it. |
| `.claude/settings.json` | Permission settings for the agent. Do not edit it. |

Each module folder has a README saying what goes in it and which starter files it contains. Starter files are named `*_starter.py`. Copy a starter to the name the assignment asks for (`poke_starter.py` to `poke.py`), and work on the copy, so you can always go back to the original.

## The four git commands

From a terminal inside this folder, every time, in this order:

```
git status                          # what changed since the last snapshot?
git add -A                          # include everything in the next snapshot
git commit -m "before the agent"    # take the snapshot, with a label
git push                            # copy it to GitHub
```

Commit before you ask the agent for anything, after you finish a piece of homework that works, and at the end of every pod session. `git diff` shows what changed since the last commit; from October 8 on, that is how you read what the agent did.

## Working with the agent

The first two weeks, through Thursday October 8, are AI-free: no Claude Code, no other AI tool, on anything in `module-1/`. After that, the agent is expected on most work, under the Protocol in `docs/protocol.md`: commit first, read what it wrote, predict, run, ask one "why", read the diff. With every homework from HW2 on, you submit your exported transcript and a 150-word AI-use note (`docs/ai-use-note-template.md`).

## Where things are

- Course site: Canvas. The calendar there is the authority on dates.
- Questions: the course Slack. Help with installs: the discussion section, run by the TA.
- Setup guides for Mac and Windows: Canvas, Module 1.
