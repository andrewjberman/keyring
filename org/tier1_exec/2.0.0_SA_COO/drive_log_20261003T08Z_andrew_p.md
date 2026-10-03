# Drive log -- 2.0.0_SA_COO~P -- 2026-10-03 07Z-08Z (ticks 77-78)

Leases FULL (IRPT_BCKEND, IRPT_DASHBD).

## Tick 77 (07:3xZ-07:4xZ): drained IB-pr-306

- IB-pr-306 merged @eb707844ba.
- **The change:** PATH A is retired for 49 Financial. `PathARetiredForFirm(ProviderPathNotComposed)` is raised first in `_compute`, for
  both a fresh request and a retained reopen.
- **Public code:** OBJECT_NOT_COVERED, per the issuer ruling on W109-S1 (the reason the base code already maps to).
- **Grading:** AC1 and AC2 PASS on the issuer re-run; the performance suite is at 251.
- **Rows:** W109-S2 and S3 INERT.
- Worktree 109 removed. 0 worker worktrees remain.

## Tick 78 (07:5xZ-08:3xZ): the P-2 packet (E1)

**Pins** @7f80b51429: six staged members moved to HEAD's bytes.
- read and export take `enforce.py`'s reporting_read delegate (IB-pr-302);
- export takes `entry.py` and the two contracts (IB-pr-301/302);
- the adapter takes `retained.py` (IB-pr-306).

Four lagging pins are left behind, with reasons in the commit:
- `opal_naming` + `reporting_policies`, which have no consumer;
- ~Y's `maintained_sources` for the export and the adapter;
- the adapter's other registry members;
- `rebalancer_schemas` (MSTR's hold).

**Artifacts** @66a931244a: read Wzf2qS5P, export WDAv+kWK, adapter NU6YVERL.
- Each verified map = S3 bytes = S3 content-sha256, with members = build input.
- Each diffed against its live zip: the adapter differs by exactly 1 member (`retained.py`).
- The adapter was built with BAU_PARITY_SKIP=1 for the three tooling files (absent from the zip).
- The live zips are saved as rollback copies.

**Plans:**

| root | plan |
|---|---|
| gold | 0/1/0 |
| publish | 1/2/0 (code, the ListBucket grant, the summaries schedule) |
| read | 2/2/0 (code + env, the GetObjectVersion grant, the render-grant policy, the summary route) |
| export | 0/1/0, after `init -reconfigure`: the cached backend was the same bucket, key and region |
| performance | 0/1/0 |

**Measured:**
- The 49F bucket is versioned.
- The gold holds 562 partitions x 6 rows; the population is 7,570; platinum holds 6 accounts.
- The method move's two branches, from the R4/R8 tie-out records: 13 of 14 pairs move (-0.74 to +0.73 pp) and 1 is unchanged.
- The local v2 rehearsal was stopped. Its inception scan runs about 12 h over the laptop link (P2_SCALE_R5).

**Found:** PROD portal 6169edd9's tab reads PATH B, but its print and export still call PATH A. Adapter B3 therefore lands only after
PROD carries ~D's readers (B2, `0.0.0_AB_MSTR` on Andrew's word).

**Packet** @855fdad77c, blob f3532bf5b9: `IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md`.
- COO half SIGNED.
- The CTO half is asked for (inbox 20261003T083407Z), with one call: open the window only with Andrew's PROD word for the same
  session.

**~D (msg 104587, acked):**
- The P-3 and P-6 page halves are complete on held branch `coo-d-p3-client-summary` @b847c9f0, now with the frozen `as_of` beside
  the export. They land in the window on ~P's word.
- G4 Download is on DEV at 3ff86a54.
- B1's commit at the window is b847c9f0. The packet's c16a31e9 is its ancestor P-6 commit, and the ledger names the commit
  actually landed.

**CTO half SIGNED** (batch 222, `CTO_HALF_IRPT_DASHBD_P2_WINDOW_20261003.md` @e67cba94ac, msg 104588, acked) for A, B and V.
The opening condition is ruled as recommended, with two additions:
1. The whole run must finish before the next scheduled trading-day fire.
2. If B2 is refused or fails, Group A rolls back in the same session.

**Carded `0.0.0_AB_MSTR` for Andrew's B2 word** (inbox 20261003T084251Z). The window is estimated at ~3 h (inferred: the backfill
upper bound is 1.1 h, P2_SCALE_R5).

**Next:** the window opens on that word. Monday 10-05's A1 reads are unchanged.
