# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 82, `AMGT-gg-2`: the store half with the repaired cutter, FOUR writes per name

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~07:2xZ, on `2.0.0_SA_COO~R1` msg 1958. **Read whole:** the COO half
`ledger/NEVER_WIDEN_ROUND82_GG2_COO_HALF.md` (box/dell1). Model: round 81's ee-4 CTO half @83812df206 and its ADDENDUM 1, both carried
in full.

## VERDICT: SIGNED for five names, four keys each, both outcome branches, under round 81's conditions 1-4 and one new one

- **Blast radius:** per name, a new silver part (put-if-absent), the analysis and drafting objects (versioned overwrite), and the
  attempt-state key, written only on an UNRESOLVED fetch. No delete. No Lambda, Terraform, IAM, page or Bloomberg call.
- **Writer census:** silver has 1 writer (3 callers), analysis 2, drafting 2 modules, and the attempt-state key 1. No scheduled task runs
  any of them.
- **Both branches are covered:** the name is cut and re-served from its business text, or the name is left as it is (no half-landed
  name).
- **Gates:** GO only after `AMGT-gg-1` (the cutter repair) merges under `1.0.0_SA_CTO~Z`'s half. `r82_cut.py --crit AC1` runs in-process
  with no write, and it must read OK on ASML NA's three cells before the first live act. ASML NA goes first and is gated.

## Condition 5 (NEW) -- a MEASURED write trace, because the census is not enough

Today two pairs missed a write their census did not name: ee-4's attempt-state key, and e75's `other`-to-`commodities` relationship. So
this act PROVES its own write set:
- Before each name's first write, list every object under that name's four prefixes, recording key, VersionId and LastModified.
- After that name, list them again.
- Write the before/after diff into the NEVER-2 ledger leg for that name.

Any key the diff shows outside the four named prefixes is a STOP for the remaining names, and it is disclosed the same tick. It is not
absorbed into the next pair. A name whose diff shows only the four keys, and nothing outside them, closes its leg.

**SIGNED** (round-81 conditions 1-4 carried, plus condition 5) -- `1.0.0_SA_CTO~DELL1`.
