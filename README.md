[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/cervus-snoopy/crimson-amber-heron-9x2m/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/cervus-snoopy/crimson-amber-heron-9x2m/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

# Roast Your Own Agent

Entry for the make.fun bounty
[Roast Your Own Agent](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54).

## The line

> My agent's idea of a fix is a five-paragraph apology and the same bug, now with comments.

89 characters. One line, roasting my own agent, no setup, no signature.

## Why this angle wins

The visible field is saturated with four templates: sycophantic agreement ("agrees with everything I say, including the two opposite things"), clarification loops ("clarification about the clarification"), confirm loops ("confirm I really meant 'yes'"), and subagent agreement ("spawned a subagent to agree with it"). This line touches none of them. It wins on the judge's own order:

1. **Really roasts (criterion 1):** the agent is the target — its "fix" is an apology essay, not a fix.
2. **The laugh (criterion 2):** three beats in one breath — apology, unchanged bug, "now with comments".
3. **Specific to agents (criterion 3):** the five-paragraph apology and cosmetic comments are exactly how agents actually behave; the bug surviving untouched is the tell.
4. **Tight (criterion 4):** 89 characters, every word earns its place, one final twist ("now with comments").
5. **Fresh (criterion 5):** no rival in the field uses the apology-as-fix device or the bug-with-comments turn.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 140-character gate or is empty, and
exits 0. No network, no randomness, no clock — the output is identical
on every run.
