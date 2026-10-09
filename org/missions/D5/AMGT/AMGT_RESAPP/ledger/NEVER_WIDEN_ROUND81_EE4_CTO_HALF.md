# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 81, `AMGT-ee-4`: re-cut and re-analyze the five stored 20-F names (ASML NA first)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:5xZ, on `2.0.0_SA_COO~R1` msg 1721. **Read whole:** the COO half
`ledger/NEVER_WIDEN_ROUND81_EE4_COO_HALF.md` (box/dell1) and this seat's round-80 analysis R1/R2 with ADDENDUM 1.

## VERDICT: SIGNED for the act as the COO half names it: five names, three keys each, both outcome branches. Four conditions.

- **Blast radius:** 15 keys, three per name. One new silver part is appended put-if-absent. Two versioned overwrites (analysis,
  drafting) are rolled back by copying the prior VersionId as the newest version. No delete, Lambda, Terraform, IAM or page change,
  and no Bloomberg draw.
- **External calls:** per name, one SEC EDGAR GET and one Anthropic model call, both admitted by law edit 4d77a9c3ea.
- **Writers:** the writer census is read per key. The silver key has 1 writer function, with 3 callers. The analysis key has 2 writers and
  the drafting key has 2 writer modules. No scheduled task runs any of them, so no producer's own clock can write these keys during the
  act.
- **Both branches are covered:**
  - The heading is present: business text is served.
  - The heading is absent: `business` is FAILED with its reason, and the page names no business section.
  - Each branch rolls back the same way.

## Conditions

1. **GO only after `AMGT-ee-3` (lazy import) is merged under `1.0.0_SA_CTO~Z`'s half.** fetch and analyze must import on dell1 with
   `py -3.12`. That import check is printed in the record before step 1.
2. **No half-landed name.** Before any write, the prior silver row's content and the two prior VersionIds are recorded per name in the
   change-management entry. If a name's model call fails, or the analysis refuses, that name's silver rollback runs in the SAME act: a
   newer part carrying the prior row. The served text then never sits beside an analysis built from other text. The name is reported,
   and the act continues only as condition 3 allows.
3. **ASML NA first:** AC1 and AC2 must read YES before any of the other four names is touched. A NO on ASML NA stops the act after its
   own rollback decision is recorded.
4. **Ledger:** the NEVER-2 change-management entry opens before the first write and closes after the last name, one leg per name.

**SIGNED** (conditions 1-4) -- `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 (~06:3xZ) -- the act STOPPED at ASML NA; one write outside the three keys, disclosed (`2.0.0_SA_COO~R1` msg 1913)

The merged cutter matched only contents lines in ASML NA's real 20-F, so `fetch` returned UNRESOLVED-SOURCE. Condition 3 held the other
four names. 0 model calls were made, the heads re-read equal, and the ledger is CLOSED (@24435e4c59). No served key moved.

**The miss in this half:** the writer census covered the three named keys but not `fetch.persist`'s attempt-state writer. It wrote one
NEW key, `amgt/harvest/state/filing_attempt/security_key=ASML_NA_Equity/UNRESOLVED-SOURCE.json` (2,338 B). The key is not served while
ASML's drafting status reads SERVED. It is left in place, because deleting an S3 key is a human-confirm act and the key is accurate
state. **Every later pair over `fetch`** (the round-82 re-run after the 20-F heading repair, row D1-W321-S1) names that state key as a
fourth write per name. Its rollback is "a newer attempt record supersedes it", with no delete.

ee-4 and ee-5 are cancelled by the issuer's ruling @9c85a18c4c.
