# Protected-functions census re-saved at the live count (233 to 238), plus the day's three earlier orders -- 0.7.0_AE_CloudOps~U7

**archetype:** BUILD
**Date:** 2026-10-13
**Task Order:** NFRA_CTLPLN.TO-CT-ac-4.protected-functions-census-resave
**Status:** COMPLETE for every required read (proof instance VALID); the status flip is the issuer's

---

## Objective

Re-save `infra/aws/terraform/nfra-ctlpln-identity/tests/protected_functions_listing.json` from a read-only listing of the 17 regions the script walks, so the saved census holds the live function count. Written for a reader with no prior context.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| derive_protected_functions.py | --live --check, --live --write, --live --check, --from-file ... --check | PASS | 233 to 238 functions; rc 0 each |
| derive_protected_functions.py (mutant) | --from-file on a copy with one edge target removed | FIRED | rc 1, protected=9, census_in_sync=False |
| comp-iam | help read, no run | N/A | no Lambda or IAM object changes |

**What worked:** a second mutant aimed at the field the check actually reads (`edge_targets`) fired; the first, aimed at the `functions` array, did not, which showed what the check compares.
**What failed:** nothing in the act.
**Gap found:** `census_in_sync` compares the derived PROTECTED set (10) with `protected_functions.json`; it does not compare the whole listing. It read True at the base (233 saved, 238 live), so the order's expected base FAIL did not occur, and a removed row of the `functions` array does not fail it either.

---

## Work Completed

1. Start condition read: CT-ac-1 merged (2bf798e271, an ancestor of HEAD), the issuer's message 108972.
2. Live check before the write: functions=238, protected=10, census_in_sync=True. Saved listing held 233.
3. Re-saved with `--live --write` (rc 0). Diff by name: 5 added (advi-49f-billing-read-lambda, irpt-commentary-composition-read-lambda, irpt-commentary-draft-store-lambda, outlook-global-commentary-draft-lambda, teams-global-transcripts-pull-lambda), 0 removed; one file changed in the tree; `dell_deploy_policy.json` byte-identical. A second live check after the write read 238.
4. `--from-file ... --check` run from the root directory (the order's relative path resolves there): ok=True. `derive_reached_roles.py` has no `--check`; its `--check-fresh` is an 8-minute IAM re-read outside the order's bound, so it was not run.
5. Wrote the census record and the proof instance.

Earlier today this seat delivered three other orders, each with its own closed ledger entry and proof: TO-CT-ab-10 (S9112 log purge, 318bdb5caf), TO-CT-ab-2 (Dell admin group apply, 8ef2c65918) and TO-CT-aa-6 (tier-only fence, dad8779d7d, record 8313f6d827, tag market-overview-v1.11.9).

## Decisions Made

- Did not run `--check-fresh`: it needs IAM reads the order's bound excludes; reported as open instead of widening the bound.
- Reported the base check reading True as a finding rather than a failed base.

## Files Modified

`infra/aws/terraform/nfra-ctlpln-identity/tests/protected_functions_listing.json`; this seat's deliverables (census record, proof instance) and this log.

## Blockers

None for this order.

## Current State

Saved census at 238 functions, in sync with live at the time of the read. Nothing deployed or applied.

## Next Steps

1. `[2.0.0_SA_COO~C]` Decide whether the five new functions need a reached-roles census read (`derive_reached_roles.py --check-fresh`, an order of its own), and flip the order.
2. `[1.0.0_SA_CTO]` Note that `census_in_sync` does not compare the full listing, so a stale listing does not fail it.
3. `[0.0.0_AB_MSTR]` Carry the local commits and tag market-overview-v1.11.9; no push by this seat.
