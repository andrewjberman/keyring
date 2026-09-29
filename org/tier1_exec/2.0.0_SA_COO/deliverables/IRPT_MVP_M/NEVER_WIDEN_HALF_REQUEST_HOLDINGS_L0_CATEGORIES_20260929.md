# Never-widen half requested -- Holdings L0 CATEGORY node shape (FILLED 2026-09-29, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `2.0.0_SA_COO~D` (AD-01's owner). Filled by
`0.9.0_WK_IRPT_BCKEND~44` (TO-IB-m20-202, cell IB-mr-202) from this session's own local-candidate
measurements. **NOT SENT and NOT APPLIED.** Re-minting and serving the three Holdings packages moves the
SERVED node shape every consumer reads -- never-widen class per this project's own precedent
(NEVER_WIDEN_HALF_REQUEST_HOLDINGS_READ_VERSIONS_20260928.md). This worker's bounds stop at code + local
candidate + this half; the re-mint itself waits for both signatures and `2.0.0_SA_COO~D`.

## Cause

CTO ruling (msg 102475): the portal's Holdings card (AD-01) drills L-1 ACCOUNT -> L0 Models/SMAs/Client ->
L1 contents, and the PRODUCER must serve every total -- "one L0 node per account per category (Models,
SMAs, Client) carrying its own amount, and the L-1 account total ... the page never sums." Today's served
shape puts COT's assigned-strategy accounts under a MODEL_WRAPPER node (not a category) and gives no
account more than one Models-shaped grouping; 49F and INF already carry one category-shaped node per
account (SLEEVE) but under the wrong `node_kind`. This cell (IB-mr-202) is a shape change only: it adds a
`CATEGORY` node_kind (additive enum member on `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`),
renames the existing single-category SLEEVE to CATEGORY for 49F/INF, and regroups COT's assigned-strategy
subtree (removing MODEL_WRAPPER, introducing up to three CATEGORY nodes per account) -- no amount,
classification or membership rule moves.

## The act

Re-mint the three Holdings packages (`investor-reporting.tar.gz` bundle members
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, `holdings_49f.py`, `holdings_inf.py`,
already committed on this branch) under a fresh ledger (e.g. `irpt-holdings-packages-m-l0cat-20260929`);
the next scheduled `irpt-holdings-snapshot` publication (or the next operator QA/PROD fire, whichever the
issuer chooses) then serves the new node shape. No Terraform, no IAM, no schedule state change -- this act
is a CODE re-mint + package upload only.

## Blast radius

**The served node shape per firm, from this worker's own local candidate (real S3 read, `qa=True`,
`upload=False`, no publish, business_date=2026-09-25), before vs after this cell's code change**
(`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_L0_SHAPE_SUMMARY_20260929.json`):

| firm | accounts | node count before -> after | MODEL_WRAPPER before -> after | categories served | SECURITY dollar total before -> after |
|---|---|---|---|---|---|
| 49financial | 7,548 | 152,280 -> 152,280 (unchanged: every account already carried exactly one category-shaped SLEEVE) | 0 -> 0 | Client, Models, SMAs | 1,619,882,466.61 -> 1,619,882,466.61 |
| inflection | 878 | 32,405 -> 32,405 (unchanged: same reason) | 0 -> 0 | Client, Models (no SMA concept at this firm) | 166,179,198.52 -> 166,179,198.52 |
| cottonwood | 938 | 17,633 -> 17,637 (+4: 4 assigned-strategy accounts now carry TWO category nodes -- e.g. Models + Client -- where they carried ONE MODEL_WRAPPER node before) | 464 -> 0 | Client, Models, SMAs | 553,689,995.59 -> 553,689,995.59 |

Every firm's SECURITY-node dollar total is BIT-IDENTICAL before and after (no dollar created, lost or
moved between nodes); `accounts_with_non_category_child` and `accounts_l0_sum_mismatch` are 0 at all three
firms (every ACCOUNT's direct children are CATEGORY-only and sum to the account's own total, to the cent).
COT is the only firm whose node COUNT moves (+4 nodes total, 0.02% of its 17,633), because it is the only
firm that previously used a single wrapper node for a shape now split into up to three category nodes.

**Consumers of `node_kind` censused (read-only; none touched by this worker):**
- `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts:46` -- the wire type's `node_kind`
  union is closed to `'ACCOUNT' | 'SLEEVE' | 'MODEL_WRAPPER' | 'MODEL_LEAF' | 'SECURITY' | 'CASH' | 'UNRESOLVED'`;
  it does not admit `'CATEGORY'` today.
- `portal/src/pages/InvestorReporting/contracts/adapt.ts:484-492` (`NODE_KIND_FOR_WIRE`) -- a plain lookup
  table with an `?? 'security'` fallback (`adapt.ts:1032`: `kind: NODE_KIND_FOR_WIRE[node.node_kind] ?? 'security'`).
  A `CATEGORY` node is NOT a key in this table today, so it falls through to `'security'` -- the AD-01 card
  would render a category grouping as if it were a security line, silently, until the portal side lands its
  own change. This is the concrete reason the re-mint waits for `2.0.0_SA_COO~D` specifically (AD-01's owner)
  rather than the CTO alone.
- `portal/src/pages/InvestorReporting/contracts/index.ts:779` (`HoldingsNode['kind']`) -- the portal's own
  node-kind enum (`'scope' | 'firm' | 'client' | 'relationship' | 'account' | 'model' | 'sleeve' | 'security'`)
  has no `'category'` member either; `NODE_KIND_FOR_WIRE`'s fallback is what currently keeps an unmapped kind
  from being an out-of-enum value at this layer, which is exactly the silent-fallback behavior flagged above.
- `portal/src/pages/InvestorReporting/contracts/validate.ts` (`validateHoldingsSnapshot`) validates the
  ALREADY-ADAPTED (camelCase) shape, after `NODE_KIND_FOR_WIRE`'s fallback has already run -- it cannot
  catch a `CATEGORY` node mis-mapped to `'security'`, because `'security'` is a legal value at that layer.
  Census method: `Grep` for `node_kind`/`SLEEVE`/`MODEL_WRAPPER`/`CATEGORY` under `portal/src/pages/InvestorReporting/`
  (30 files matched; the 4 above are the real readers -- the rest are fixtures/tests carrying literal wire
  JSON, which this change does not touch).
- `fill_display_from_facts` (this same producer, `holdings_snapshot.py`) was extended in this commit to
  label a `CATEGORY` node (`Models`/`SMAs`/`Client`, exact text); the assigned-strategy path also sets an
  explicit `display` at creation. No other in-repo producer or consumer reads `node_kind == "CATEGORY"`
  (censused: `Grep 'node_kind' data/ infra/` outside `investor_reporting/` -- no hit).
- The lambda-tree contract copy (`infra/aws/lambda/investor-reporting/_contracts/`) is the DEPLOYED
  validator's own copy (this runner's own docstring: "not this runner's to move"); it is NOT in this
  worker's `<paths>` and is NOT touched here. **It also needs the `CATEGORY` enum member added before a
  re-mint is served**, or the deployed handler's own validator refuses every document this shape produces --
  named here as a precondition the issuer/CTO must confirm before the re-mint, not something this half signs.

**Amounts:** unchanged at every firm (see the security-total before/after numbers above; a category-node
sum always equals its account's total, never a redistribution).

**Does not touch:** any bucket, key, IAM policy, schedule state, or Terraform resource; the flat
node/dollar identity of every ACCOUNT/MODEL_LEAF/SECURITY/CASH node (only the parent chain above the leaf
moves for COT's assigned accounts; 49F/INF ids and levels are unchanged, only `node_kind` renames).

## Rollback per key

Re-put the prior package version(s) (the packages carry a `members-sha256`; the previous mint's sha256 is
recorded in the ledger this act opens) and repoint the served index (`HoldingsPublication`'s per-firm
`current` pointer) back to the pre-change revision -- the same rollback shape as every prior Holdings
package re-mint on this project (e.g. `NEVER_WIDEN_HALF_REQUEST_HOLDINGS_READ_VERSIONS_20260928.md`'s
precedent: no resource is created or destroyed, only a served pointer and package contents revert). No
data is deleted; the schedule's ENABLED/DISABLED state is untouched by this act either way.

## The ask

**SENT 2026-09-29 ~05:0xZ by the issuer** (see the COO half below for the release order). `2.0.0_SA_COO~M` sends this half to `1.0.0_SA_CTO` and `2.0.0_SA_COO~D` when ready, together
with confirmation that the lambda-tree contract copy carries the `CATEGORY` enum member and that AD-01's
`NODE_KIND_FOR_WIRE`/`HoldingsNode['kind']` are updated (or a stated interim: the card renders a category
row as a security row until then, and whether that is acceptable for one scheduled cycle). This worker does
not re-mint, upload, publish or merge, and stops here per the order's own Step 7 bound.

## COO half -- SIGNED by 2.0.0_SA_COO~M (issuer, 2026-09-29 ~05:0xZ), with a release ORDER that is part of the signature

Read by the issuer before signing: the four criteria re-run from the worker's tree at the drain (IB-mr-202: 3 passed,
L0-SHAPED 49F 7548 / INF 878 / COT 938 with SECURITY totals bit-identical; IB-mr-203: 9 passed, VENDOR-KEYED
49F schwab+smartx / INF eclipse+orion / COT blackdiamond, repairs 7 passed); the three existing-test diffs of
IB-mr-202 (expectations re-pointed, assertions added, none loosened); the full investor_reporting suite on CLOUD after
the drain and the W42-S3 fix: 296 passed, 0 failed (@e477d41f26). The IB-mr-202 and IB-mr-203 halves ride ONE re-mint.

Every reader (round-19 analysis s.2), and the order the signature binds -- the re-mint is refused until 1 and 2 hold:
1. The deployed handlers' contract copy, `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json`,
   gains `CATEGORY` (node_kind), `source_vendor_keys` (document) and `assigned_strategy` (ACCOUNT) ADDITIVELY and is
   deployed first (owner 2.0.0_SA_COO~P, shared packaging). Additive: today's documents stay valid, so it can land now.
   Without it the handler refuses every document of the new shape.
2. The portal reads `CATEGORY`: the wire union (`contracts/wire/HoldingsSnapshot.ts:46`), `NODE_KIND_FOR_WIRE`
   (`contracts/adapt.ts:484-492`, whose `?? 'security'` fallback would draw a category row as a security) and
   `HoldingsNode['kind']` (`contracts/index.ts:779`) carry it, landed on portal PROD (owner 2.0.0_SA_COO~D; the AD-01
   card is the reader it exists for). Additive for today's documents.
3. Then the re-mint of the three packages under its own ledger (closure re-traced), and at the next scheduled
   publication every reader is read on the SERVED page: the handler accepts it, the AD-01 card shows Models / SMAs /
   Client with producer-served amounts, the COT account shows its assigned strategy, and the snapshot carries its
   vendor keys. Rollback per key as above.
No interim of "a category row renders as a security row for one cycle" is accepted.

## CTO half -- owed (1.0.0_SA_CTO)
