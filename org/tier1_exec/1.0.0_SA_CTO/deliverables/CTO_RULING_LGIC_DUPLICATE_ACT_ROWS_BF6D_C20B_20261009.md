# LGIC duplicate act rows: close bf6d and c20b as DUPLICATE (1.0.0_SA_CTO~DELL1, 2026-10-09 ~11:3xZ)

**Ruled by the laptop `1.0.0_SA_CTO`** (bus 146f557f), relayed by `0.0.0_AB_MSTR~DELL1` msg 2340:
- The dell1 open-call rows `dell1-20261009T110120Z-bf6d` and `dell1-20261009T110121Z-c20b` duplicate
  `-838c`/`-5f4b` and `-69ef`. All of them cover the same deletes, and all come from the same `ROUND12_DRAIN_END.md`.
- Close bf6d and c20b as DUPLICATE, so Andrew sees each act once.
- Keep 838c, 5f4b and 69ef as Andrew's acts: the two tfstate object deletes and the log group
  `/aws/lambda/opal-assets-absence-check`.

This reverses the hold this seat placed on 838c and 5f4b as duplicates (msg 2320, @6aa052bb8d). Those two rows are Andrew's acts again.

-- 1.0.0_SA_CTO~DELL1

## Context
dell1 open-call rows bf6d and c20b duplicate 838c, 5f4b and 69ef. All five are the same LGIC deletes from the same
`ROUND12_DRAIN_END.md`. The laptop `1.0.0_SA_CTO` ruled at bus 146f557f (relayed in msg 2340) that bf6d and c20b close as
DUPLICATE.

## Position
Close bf6d and c20b as DUPLICATE. Keep 838c, 5f4b and 69ef open as Andrew's acts.

## Why it gave pause
### Ambiguity
None on the facts. The rows were CROSS-BOX because the tfstate bucket is shared, so the tool refused a close resting on a
bus message alone.
### Out of pattern
This reverses this seat's own earlier hold (msg 2320), which treated 838c and 5f4b as the duplicates.
### Other solutions
Hold bf6d and c20b instead of closing them. That was rejected because Andrew would still see each act twice.
