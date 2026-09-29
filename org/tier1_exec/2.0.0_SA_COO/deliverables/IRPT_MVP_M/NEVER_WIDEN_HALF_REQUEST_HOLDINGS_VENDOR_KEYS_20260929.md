# Never-widen half requested -- Holdings source vendor keys (FILLED 2026-09-29, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO`. Filled by `0.9.0_WK_IRPT_BCKEND~44` (TO-IB-m20-203, cell IB-mr-203)
from this session's own local-candidate measurements. **NOT SENT and NOT APPLIED.** Re-minting and serving
the three Holdings packages moves the SERVED document shape every consumer reads -- never-widen class per
this project's own precedent (`NEVER_WIDEN_HALF_REQUEST_HOLDINGS_READ_VERSIONS_20260928.md`,
`NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md`). This worker's bounds stop at code + local
candidate + this half; the re-mint itself waits for both signatures.

## Cause

CTO ruling UIC-14 (msg 102443, cell IB-mr-203): "the Holdings builder writes each snapshot's source
vendor keys (registry vendor keys) into its output, so the portal turns keys into words and no
function-name map exists" -- the portal side of UIC-14 (a client-words render of the Holdings source line)
was PARKED (`org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md`) because the producer names embed firm tokens
and a hand-typed producer-to-source map is refused by the LGIC naming gate. This cell (IB-mr-203) builds
the PRODUCER half only: each snapshot now carries `source_vendor_keys`, a top-level array of
`infra/logic/registry/systems.json` VENDOR-class keys, derived by `holdings_snapshot.source_vendor_keys()`
from the builder's own pre-existing `manifest["source"]` free-text description (word-bounded,
case-insensitive match against every registry VENDOR key -- never a per-firm constant, never a hand-typed
vendor key). An unrecognized source is REFUSED (raises), never silently labelled.

Riding the same cell, batched by AMENDMENT 1 (row IRPT_BCKEND-W44-S1): (R1) the COT assigned Rebalancer
strategy, lost when IB-mr-202 removed the MODEL_WRAPPER node, is restored as an `assigned_strategy` field
on the COT ACCOUNT node (never a node); (R2) the S71 re-arm trigger test now guards the three standalone
`irpt_holdings_{49f,inf,cot}` packages the enabled schedule's dispatch actually runs, in place of the
`investor_reporting` directory bundle it wrongly guarded before.

## The act

Re-mint the three Holdings packages (`irpt_holdings_49f`/`_inf`/`_cot`, `investor-reporting-holdings.tar.gz`
per firm; bundle members `holdings_snapshot.py`, `holdings_49f.py`, `holdings_inf.py`,
`holdings_membership.py` and the rest of the declared closure, already committed on this branch) under a
fresh ledger (e.g. `irpt-holdings-packages-m-vendorkeys-20260929`); the next scheduled
`irpt-holdings-snapshot` publication (or the next operator QA/PROD fire, whichever the issuer chooses) then
serves the new document shape. No Terraform, no IAM, no schedule state change -- this act is a CODE
re-mint + package upload only.

## Blast radius

**The served document shape per firm, from this worker's own local candidate (real S3 read, `qa=True`,
`upload=False`, no publish, business_date=2026-09-25)**
(`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_UIC14_VENDOR_KEYS_SUMMARY_20260929.json`):

| firm | new field | value | node count (unchanged) | schema_valid |
|---|---|---|---|---|
| 49financial | `source_vendor_keys` | `["schwab", "smartx"]` | 152,280 | true |
| inflection | `source_vendor_keys` | `["eclipse", "orion"]` | 32,405 | true |
| cottonwood | `source_vendor_keys` | `["blackdiamond"]` | 17,637 | true |

Every firm's node count and reconcile total is BIT-IDENTICAL to IB-mr-202's own real local build of the
same business_date (152,280 / 32,405 / 17,637 nodes; $1,826,940,340.65 / $208,110,999.41 / $553,689,995.59):
this cell adds one top-level array field and one optional per-account object field, moving no node, no
dollar and no existing field.

**COT's `assigned_strategy` field (AMENDMENT 1 R1), same real build:** 464 of 938 ACCOUNT nodes now carry
`assigned_strategy: {model_id: {namespace: "COT_REBALANCER_MODEL", value: ...}, name: ...}` -- the exact
population IB-mr-202's own commit measured as the removed MODEL_WRAPPER node count (464 -> 0). No amount,
classification or membership rule moves; the field only restores what a consumer reading the account's
assigned strategy lost when the node it lived on was removed.

**Schema:** `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` gains two ADDITIVE optional
members, both OPTIONAL under the v1 immutability rule (a v1 document that predates either is still valid):
top-level `source_vendor_keys` (array of registry vendor keys) and node-level `assigned_strategy` (COT
ACCOUNT nodes only).

**Consumers censused (read-only; none touched by this worker):**
- No portal reader of `source_vendor_keys` or `assigned_strategy` exists yet (censused: `Grep
  'source_vendor_keys|assigned_strategy'` under `portal/src/pages/InvestorReporting/` -- no hit). Serving
  this shape adds a field no consumer reads today; it changes no existing consumer's behavior.
- The lambda-tree contract copy (`infra/aws/lambda/investor-reporting/_contracts/`) is the DEPLOYED
  validator's own copy, per this runner's own docstring ("not this runner's to move"); it is NOT in this
  worker's `<paths>` and is NOT touched here. It needs both new members added before a re-mint is served,
  or the deployed handler's own validator refuses every document this shape produces -- named here as a
  precondition the issuer/CTO must confirm before the re-mint, not something this half signs (same shape
  as IB-mr-202's precedent for the `CATEGORY` node_kind).
- **UIC-14's portal half is NOT closed by this cell.** `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md` names
  the un-park condition as TWO parts: "`2.0.0_SA_COO~M` serves the snapshot's source vendor keys" (this
  cell, local-candidate only, not yet served) **and** "the registry vendor view lands" -- a GENERATED view
  in `lib/opal_naming.py` (the same path CTO 102351 set for IV-e-76) rendering a vendor key as a client
  word, which is outside this cell's `<paths>` (`lib/opal_naming.py`, `portal/`) and is not built here. The
  parked build/test sits at `.runtmp/parked/iv-e-87.source-client-words.test.ts` per that STATUS row.

**Amounts:** unchanged at every firm (see the node-count/reconcile-total identity above).

**Does not touch:** any bucket, key, IAM policy, schedule state, or Terraform resource; the flat
node/dollar identity of every ACCOUNT/CATEGORY/MODEL_LEAF/SECURITY/CASH node; `lib/opal_naming.py` or any
portal file.

## Rollback per key

Re-put the prior package version(s) (the packages carry a `members-sha256`; the previous mint's sha256 is
recorded in the ledger this act opens) and repoint the served index (`HoldingsPublication`'s per-firm
`current` pointer) back to the pre-change revision -- the same rollback shape as every prior Holdings
package re-mint on this project. No data is deleted; the schedule's ENABLED/DISABLED state is untouched by
this act either way.

## The ask

**NOT SENT.** `2.0.0_SA_COO~M` sends this half to `1.0.0_SA_CTO` when ready, together with confirmation
that the lambda-tree contract copy carries both new members and that the registry vendor view (portal
half of UIC-14) is tracked separately (it is not this cell's to build). This worker does not re-mint,
upload, publish or merge, and stops here per the order's own bound.

## COO half -- owed (issuer: 2.0.0_SA_COO~M)

## CTO half -- owed (1.0.0_SA_CTO)
