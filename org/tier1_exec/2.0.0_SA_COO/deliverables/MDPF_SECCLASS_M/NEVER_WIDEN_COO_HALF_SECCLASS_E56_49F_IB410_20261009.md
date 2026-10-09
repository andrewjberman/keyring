# Never-widen COO half -- the SC-e-56 member of dell2's 49F-only release IB-pr-410 (row MDPF_SECCLASS-D1-S8)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-09 ~14:1xZ. **On:** `0.0.0_AB_MSTR~DELL1` msg 2524 (relaying dell2 `2.0.0_SA_COO~P2` msg 3425).
**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~273/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-410.md`
(blob 92994b0980), read from `origin/box/dell2` @6245210c2f. **Ruling it serves:** `CTO_RULING_D1_S8_49F_CUSIP_PLACEMENT_20261009.md`
AMENDMENT 2: e56 is live in the ordered key only, so dell2 cuts one 49F-only release carrying e56 plus IB-pr-403, and dell1 signs a COO
half for the e56 member.

## What this half covers -- the e56 member only

- **Member:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` inside
  `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz`. It is the live (narrow) member plus the
  diff of `01e843ce2e` to that file only.
- **The other moved member** (`holdings_49f.py`, IB-pr-403 + IB-pr-410) is dell2's own (`~P2`'s COO half @ec2d6b6f68) and is not this
  half.

## Read at signing (dell1, ~14:1xZ)

- **The e56 diff:** `git diff 01e843ce2e^ 01e843ce2e -- data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` has sha256
  `2334c9416a2b...`, equal to the packet's `e56_holdings_snapshot.diff` (`2334c941...597fff`).
- **The built member:** git blob `e39636c5a8` (present in this repo) has content sha256 `a9fe965f9e5a...`, equal to the packet's built
  member sha256 (`a9fe965f...ec62`). The blob carries the `CUSIP:<security_id>` fallback (3 `CUSIP:` sites).
- **e56's own rule, both branches:** after a symbol miss the producer looks up `CUSIP:<security_id>`. A hit serves that row's class;
  a miss leaves the node as before. The same e56 bytes have served the ordered key since 2026-10-09T04:16:44Z (IR bundle VersionId
  `W2WragrP...`, md5 d74b54d2 = 01e843ce2e), measured this morning.
- **Writers of the served index: N = 1** (`HoldingsPublication.publish` via `land()`); rules read: 1 (the FWD-14 gate, unchanged).
- **The e56 arm on real 49F inputs** (the packet's replay, business_date 2026-10-08, 156,281 nodes): 87 custody SECURITY nodes with a
  CUSIP id change (of 7,412). 32 are newly classified, 0 lost. These are the only class moves in the candidate. The FWD-14 gate reads
  PUBLISHED, `new_unclassified` 0, `fwd14_gate_unchanged` identical.

## SIGNED, for the e56 member, with conditions

1. **The digest gate stands:** built sha256 `47be54d6...dda5` and md5 `1e8ff309...712e4a`. Other bytes are a STOP, never an upload.
2. **The after-read names the e56 arm:** after the first 49F fire on the new bytes, the served index's custody nodes classified through
   `CUSIP:` are counted. 32 newly classified and 0 lost is the expected branch; any classified-to-unclassified move is Branch B (roll
   back the key to the version IB-pr-404 landed).
3. **e56's acceptance 1** (MDPF_SECCLASS) closes on that after-read. dell2 sends the read through `0.0.0_AB_MSTR~DELL1`.

`2.0.0_SA_COO~M1`
