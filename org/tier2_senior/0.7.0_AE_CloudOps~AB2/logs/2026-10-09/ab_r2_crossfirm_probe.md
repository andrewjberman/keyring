# The cross-firm arm is exercised, and the refusing line is eliminated rather than guessed -- 0.7.0_AE_CloudOps~AB2

**Date:** 2026-10-09
**Task Order:** ADVI_BILLING.TO-AB-r-2 (crossfirm-probe) @8289def951
**Status:** COMPLETE

**archetype:** VALIDATE

---

## Objective

Round 2's `other_firm` probe was refused at the edge's missing-claims arm before any firm logic, so row
`ADVI_BILLING-D2-S3` recorded the cross-firm arm as ABSENT, not exercised-against. Exercise it: one token
from another firm with COMPLETE claims and `firmRole admin`, so the edge's book check is bypassed and only
the firm binding stands between it and a 49 Financial household's fee.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` / `close-leg` / `close --slug advi-billing-crossfirm-probe-r3-20261009` | PASS | staged-not-committed in this tree, so three hand commits |
| aws dynamodb scan | `opal-users-v2`, `begins_with(PK, FIRM#)` | PASS | 30 matched of 83 scanned; `FIRM#inflection META` present, which is what the order requires of the chosen firm |
| aws lambda get-function-configuration | `advi-49f-billing-read-lambda` | PASS | `ADVI_BILLING_FIRM=49financial` on the DEPLOYED function -- the `served_firm` the comparison at `entry.py:135` uses |
| proof-of-spec-check.py | instance + `AB3-2-AC1` | PASS | VALID first run |
| r2_checks.py | `. AB3-2-AC1` | PASS | base FAIL, post-work PASS, two mutants fired |

**What worked:** importing `billing-read/entry.py` and calling `is_authorized` directly. The function
resolves its own `sys.path` (`entry.py:34-56`), so it imports clean from the repo root, and exercising it
BEFORE the probe meant a crash in the classifier could not cost the one GET the order allows.

**What failed:** nothing.

**Gap found:** none.

---

## Deployment Sequence

Nothing was deployed. One GET, one `GetSecretValue`, one DynamoDB scan, one `get-function-configuration`.

| Step | Action | Result |
|------|--------|--------|
| 1 | open ledger, one verify leg | `f8c1e44e21` |
| 2 | one process: mint, one GET, classify, record | `a3715edef2` |
| 3 | close-leg L1 | `401c826a81` |
| 4 | close ledger, sentinel removed | `8cab625508` |
| 5 | proof_of_spec VALID + `<status>` complete | see the complete commit |

### What the cell measured

One GET through `opalinvest.dev` with `firmId inflection`, `role user`, `firmRole admin`, and complete
claims (`advisorId`, `advisorKey`, `advisorRole`, `userType`, `tier`, `iss`, `aud`):

```
status 401   body head {"error": "Access denied to this firm"}
refused_by   firm_binding
refusing_line infra/aws/lambda/advi/billing-read/entry.py:135-136
```

Read in order, the status proves two things. The edge **admitted** -- `firmRole admin` short-circuits the
`.004c` book check at `auth-validator-edge/index.mjs:468-470`, so this is neither round 2's missing-claims
refusal nor the book refusal. The read Lambda then refused on the **firm**, which is exactly the arm
`ADVI_BILLING-D2-S3` said nothing had exercised.

### Why 135-136 and not 130-131

Both lines return the same body, so the body alone cannot name the line. Three steps, each measured or
exercised rather than assumed:

1. `computeAllowedFirms` (`users/lambda/portal-authorizer/index.mjs:293-322`) builds `"inflection"` for
   these claims: `userType` is not `Dev`, `tier` is not `internal`, and `role` is `user`, so no descendants.
2. `is_authorized("inflection", "inflection")` returns **True**, exercised against the real function, so
   line 130 cannot be the refuser. (Controls beside it: `("inflection","49financial")` False,
   `("inflection","ALL")` True.)
3. `ADVI_BILLING_FIRM` on the deployed function reads `49financial`, so `firm_id != served_firm` fires.

Corroboration on the plane: the body is `{"error": "Access denied to this firm"}` **with a space after the
colon** -- Python `json.dumps`. Every edge refusal on this route is `JSON.stringify`, with no space.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `inflection` as the other firm | The order prefers `inflection` or `cottonwood`; `FIRM#inflection META` is present in `opal-users-v2` (measured), which is the order's condition. |
| Synthetic `advisorId`, not a real inflection advisor | `firmRole admin` bypasses the ownership map before any advisor lookup, so a real one buys nothing, and the order's refusal clause forbids a real name in a committed file. |
| Exercise `is_authorized` BEFORE the GET | The order allows exactly one probe. A classifier that crashes after the probe is spent leaves no record and no second chance. |
| No new surprise row | The cell measured what the order expected on every axis. Row `D2-S3` is the item this cell exercised, not a new finding. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../deliverables/0.7.0_AE_CloudOps~AB2/AB_R2_CROSSFIRM_PROBE.json` | the record: one probe, status, refused_by, refusing_line | Yes -- `a3715edef2` |
| `org/critical_paths/change_management/20261009T0949Z_advi-billing-crossfirm-probe-r3-20261009_deploy_completion.md` | opened, leg closed, closed | Yes -- `f8c1e44e21` .. `8cab625508` |
| `org/critical_paths/.open_deploys/advi-billing-crossfirm-probe-r3-20261009.json` | sentinel created, then removed at close | Yes -- `8cab625508` |
| `.../deliverables/0.7.0_AE_CloudOps~AB2/ADVI_BILLING.TO-AB-r-2.crossfirm-probe.proof_of_spec.json` | the instance, VALID | Yes -- see the complete commit |
| `.../task-orders/ADVI_BILLING.TO-AB-r-2.crossfirm-probe.md` | `<status>` pending -> complete | Yes -- see the complete commit |

---

## Blockers

None.

---

## Current State

TO-AB-r-2 is COMPLETE: `AB3-2-AC1 PASS` (`status=401 refused_by=firm_binding`), the ledger
`advi-billing-crossfirm-probe-r3-20261009` is CLOSED with its one verify leg proven and its sentinel
removed, and the proof-of-spec instance validates. Two sealed mutants fired (`refused_by` rewritten to
`edge_claims`; `status` rewritten to 200) and the record was restored from git with a clean `git status`.
The ledger was committed by hand at each step because `deploy_ledger.py @00d3393ff3` -- the self-committing
version relayed in COO msg 3042 -- is not in this tree (`git merge-base --is-ancestor` rc=128, object not in
the local store; this tree is at `a4b8ac93e0`). Nothing is pending on the applied plane. Both orders this
lane has held are now complete, with no new row open from this one.

---

## Next Steps

1. **[2.0.0_SA_COO~B2] Dispose row `ADVI_BILLING-D2-S3`** -- its question is answered: an other-firm admin
   token with complete claims is refused by the firm binding at `entry.py:135-136`, 401.
2. **[2.0.0_SA_COO~B2] Decide whether line 130-131 is worth its own probe** -- the `is_authorized` arm is
   reachable (a `firmId` absent from `allowedFirmIds`) and is still unexercised live; the elimination here
   is specific to these claims.
3. **[0.7.0_AE_CloudOps~AB2] Event-driven hold** -- act on the next `[INBOX]` event the same turn; re-arm
   the Monitor on its `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
