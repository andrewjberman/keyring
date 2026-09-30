# ANDREW-DIRECT 2026-09-30 ~17:4xZ -- "go 3.14": site Z standardizes on Python 3.14

**Channel:** Andrew, in the 0.0.0_AB_MSTR~Z Claude Code session (site Z). **Recorded by:** 0.0.0_AB_MSTR~Z, same turn.

## Verbatim

> "That is not a long-lived solution. Is there any reason why we cannot just use 3.14? Is 3.14 really so different
> that it requires a meaningful lift to adjust python processes to it?"

then, after MSTR~Z's measured answer and plan:

> "go 3.14"

## The plan the word approves (as put to him, nothing wider)

1. Repair the gutted Python 3.14.7 (standard library removed by the 2026-09-26 installer Modify) from the installer
   components cached at `C:\ProgramData\Package Cache\...v3.14.7150.0\` -- one elevated prompt, no download.
2. Reinstall the Python 3.11 package set into 3.14 from PyPI -- internet egress, authorized by this word for this
   install only.
3. Smoke-test the broker server (`org/mcp/server.py`) and the key imports under 3.14; keep 3.11 installed as fallback.

## Why

The Python314 Machine PATH entries were re-added three times (the last with no Windows Installer event), so something
outside the installer keeps 3.14 first on PATH. Removing them does not hold; making 3.14 whole makes them correct.
Measured: 1 import of a post-3.11-removed module across 49,509 repo files (a vendored numpy test in a Lambda layer).
