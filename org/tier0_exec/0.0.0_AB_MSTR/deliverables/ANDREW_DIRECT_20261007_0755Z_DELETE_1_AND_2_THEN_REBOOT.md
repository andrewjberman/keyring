# ANDREW-DIRECT 2026-10-07 ~07:55Z -- "delete 1 and 2. then we will reboot"

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z), in-session, answering four numbered undecided cleanup rows.

## Verbatim

"delete 1 and 2. then we will reboot"

## The two rows as put to him

1. "Claude scratch and pip/npm caches (12 GB): delete."
2. "87 unregistered `C:\tmp` folders (3.9 GB): delete."

Rows 3 (old `opal-pinned` pins) and 4 (`ajb_workspace\infra`) are not covered and are untouched.

## What was done

- Row 1: every Claude session scratch folder under `AppData\Local\Temp\claude` except this session's own (134 folders;
  the folder went from 12.1 GB to 1.5 MB), the pip cache, and the npm `_cacache`.
- Row 2, narrower than his word on the safe side: a fresh read found 104 unregistered folders, not 87. 88 were
  deleted: those idle 24 hours or more with no `.git`, plus this seat's own 9 (7 empty husks, 2 `zs61-*`).
  16 were KEPT: 13 touched within 24 hours (tonight's `rv-*` round evidence, `p1006`, `bbg-bmk`, `.scratch`) and
  3 that are git clones (`m3verify`, `og-mcp10`, `oa-dev`).
- C: read 104 GB free before and 122 GB free after (df).
