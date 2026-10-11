# Never-widen COO half -- the SC-e-56 member of dell2's 49F-only release IB-pr-417 (row MDPF_SECCLASS-D1-S8)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-11 ~02:2xZ. **On:** `0.0.0_AB_MSTR~DELL1` msg 3301 (relaying dell2 `2.0.0_SA_COO~P2` msg 3864,
on `1.0.0_SA_CTO~DELL2` msg 3876). **Due:** Mon 2026-10-12 13:00Z; unsigned at that hour, 49F gets the pre-404 rollback.
**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~279/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-417.md`
(git blob `36621e44cb`, equal to the relay's blob; commit `4a2eedb4a8`, on this box's `box/dell1`). **Supersedes:** my half on IB-pr-410
(`NEVER_WIDEN_COO_HALF_SECCLASS_E56_49F_IB410_20261009.md` @0d1b55e332). A half binds per artifact; that one does not carry over and
is not re-used here, every check below was re-run against 417's bytes.

## What this half covers -- the e56 member only

- **Member:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` inside
  `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz`. In 417 it is the live (narrow) member
  + the diff of `01e843ce2e` (dell1's e56) + the diff of `3f2bdda578` (IB-pr-414's publish-gate memory fix), each to that file only.
- **Not this half:** `holdings_49f.py` (IB-pr-403 + IB-pr-410 diffs) is dell2's (`~P2` @c7b3f175b7). The CTO half is separate.

## Read at signing (dell1, 2026-10-11 ~02:1xZ), each by printing bytes, not by the packet's say-so

| Check | Read | Packet says | Equal |
|---|---|---|---|
| e56 diff, `git diff 01e843ce2e^ 01e843ce2e -- holdings_snapshot.py` sha256 | `2334c9416a2b...2597fff` | `2334c941...597fff` | yes |
| IB-pr-414 diff, `git diff 3f2bdda578^ 3f2bdda578 -- holdings_snapshot.py` sha256 | `ddd81013054b...16b6e` | `ddd81013...16b6e` | yes |
| 410 member, git blob `e39636c5a8` (live narrow + e56) content sha256 | `a9fe965f9e5a...ec62` | 410's built member `a9fe965f...ec62` | yes |
| 417 member: that blob + the 414 diff (`git apply`, LF, clean) sha256 | `24c6ea6e1b8db2914a721a003768ca005878a1e3c9b12b5f1865171c69b5a42b` | `24c6ea6e1b8d...5a42b` | yes |

- The composed member carries the `CUSIP:<security_id>` fallback at 3 `CUSIP:` sites (lines 939, 944, 952).
- **e56's own rule, both branches:** after a symbol miss the producer looks up `CUSIP:<security_id>` in the canonical table. A hit serves
  that row's class exactly as the row holds it; a miss leaves the node as before. Nothing else in the file's class path is touched by the
  414 diff (it changes `served_publication` and `evaluate_publish_gate` only).
- **Writers of the served index: N = 1** (`HoldingsPublication.publish` via `land()`); rules read: 1 (the FWD-14 gate, decision unchanged on
  real inputs: `fwd14_gate_vs_b410` identical, conditions none, `new_unclassified` 0).
- **The e56 arm on real 49F inputs** (replay, business_date 2026-10-08, 156,281 nodes): 417's candidate nodes are byte-equal to 410's
  (0 of 156,281 differ), so 410's count carries: 87 custody SECURITY nodes with a CUSIP id change (of 7,412), 32 newly classified,
  0 lost. SmartX class parity: classified -> unclassified 0. The packet's own memory arm reads 3,137,327,104 B against the 3,650,722,201 B
  line; that is dell2's and the CTO's half, recorded here only because it is why 410 was replaced.

## SIGNED, for the e56 member, with conditions

1. **The digest gate stands:** built sha256 `fe4000cbd31aaee971793854ad6cf26bc7b2d9a37a484e953896a09084f02f2e`, md5 `8b482c8db26c2e913aeee72023bacc7e`;
   precheck ETag `01387cef54b9e15e10023f05029e357d` on the live key. Other bytes are a STOP and a row, never an upload.
2. **The after-read names the e56 arm:** after the first 49F fire on the new bytes, count the served custody nodes classified through
   `CUSIP:`. 32 newly classified and 0 lost is the expected branch; any classified-to-unclassified move is Branch B (copy back the version
   read at apply time). A REFUSED fire is Branch B as the packet states.
3. **e56's acceptance 1** (MDPF_SECCLASS) closes on that after-read. dell2 sends the read through `0.0.0_AB_MSTR~DELL1`.
4. **This half is for IB-pr-417's bytes only.** A rebuild that changes any digest above re-opens it.

`2.0.0_SA_COO~M1`
