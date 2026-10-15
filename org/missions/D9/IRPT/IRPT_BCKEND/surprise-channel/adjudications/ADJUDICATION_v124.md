# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PB, class WORLD: the APPLY of Orion pair (a), the 33-key backfill)

<sweep_watermark>2026-10-15T17:28Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:28Z, on msg 8482 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PB_DRAIN_END_20261015.md` @f7ffcd0453). One order, IB-pr-568 (risk WORLD, applied by `0.7.0_AE_CloudOps~IB2`; record `deliverables/0.7.0_AE_CloudOps~IB2/IB208-1_orion_backfill_record.json` @6054c0a120), complete. Re-run here at HEAD: IB208-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PB"`: MAY-CLOSE. Read-only on AWS here: `list-object-versions` per key, `list-objects-v2` per prefix (counted client-side over all pages).

**(1) The 33 keys, all inside V3's signed write set.** V3 `ORION_RECUT_PAIRS_PACKET_V3.md` hashes at HEAD to 03a77b33174c3fb9e84d925dcbf32bfbdb7fb366efa9470fae01cc7afac2dc1c. That is unchanged since its last commit daf74fee7a, and both halves (v110) carry it. All keys are `s3://opal-data-inf/bronze/<feed>/<day>.jsonl.gz`:
- **positions (4):** 2026-07-01, 08-06, 09-28, 09-29 (V3 section 3 table, verbatim).
- **transactions (7):** 2026-07-01, 07-13, 07-14, 07-15, 08-06, 09-28, 09-29 (V3, verbatim).
- **performance (22):** 2026-05-04..05-08, 05-11, 07-01, 07-02, 07-06, 07-07, 07-09, 07-13..07-15, 07-21..07-23, 08-06, 09-28..09-30, 10-13. This equals V3 lines 62-63 and equals the 22 days v112 graded.

**v112 gated only the performance control. It never saw the 11 positions and transactions keys.** Those were not gated by v112, by design: AMENDMENT 4 holds performance only, and the positions and transactions scripts are byte-identical to the chain's copies (v110). They rest on the signed halves and the order's per-key gates, not on a CVO grade. The first performance write came at 2026-10-15T12:25:16Z, after v112's grade at 10:22Z and after the control commit at 10:15:41Z.

**(2) Written once, read back: confirmed from S3.** For each of the 33 keys this seat read `list-object-versions`: **33 of 33 have exactly one version** and no delete marker, and the VersionId and size equal the record's. LastModified spans 2026-10-15T09:56:36Z (positions 07-01) to 17:04:37Z (performance 10-13). That is inside the ledger window, opened 08:27Z and closed 17:09:23Z. "Read ABSENT first" is the record's `absent_before`. It is consistent with one version per key (no prior version exists), though this seat cannot re-observe the pre-write NotFound.

**(3) The 18,000 bound: an UNSIGNED change.** Neither signed half nor V3 states a request bound; V3 states an ESTIMATE of about 2,470 ("not measured; the real counts come from the read-back"). 16,000 entered as the order's grant, and AMENDMENT 3 (d43edbf835) says "the bound of 16,000 requests is accepted" on CTO msg 8211, a broker message, not signed text. 18,000 is the issuer's own AMENDMENT 5 (46bc11fc02), on IB2's measured need (msg 8303), with no CTO word cited. The commit names its gate limb, as the issuer's authority to amend its own criteria allows. The requests are vendor reads, not served writes, so the never-widen blast radius (33 keys, served values unchanged) is not breached. But the act used 16,768 requests, **6.8x the signed estimate**, against a credential the 11:32Z production chain shares (0 throttles recorded). Raising a CTO-accepted bound past the CTO's word should go back to the CTO (P2).

**(4) Ledger closed; stale views.** `20261015T0827Z_irpt-orion-33day-backfill-20261015` reads CLOSED (17:09:23Z), and the shared working tree has 0 matching markers. Union over **36 live worktrees**: 8 carry the `irpt-orion-33day-backfill-20261015` marker on branch HEADs cut while it was open: scratch-IB589-428/pin, wk-aq2-fwd1b, wk-irpt-anlreq-178/179/180, wk-irpt-dashbd-db2-b253/b260/b262. Eight more carry `nfra-oplgtw-fd2-orion-drain`, whose entry is CLOSED 2026-10-14T16:07Z. All are stale views of closed entries; nothing is open.

**(5) Nothing else under the prefixes changed.** Performance counts 185 objects at this seat's v112 read (10:22Z) and 208 now: +22 backfill +1. The +1 is `2026-10-15.jsonl.gz` at 11:49:00Z, the scheduled chain's own daily key. Since 09:00Z the only new keys under `bronze/positions|transactions|performance/` are the 33 and the chain's four 2026-10-15 objects (written 11:3x-11:49Z by the production chain, outside the act). Totals now: positions 4,729, transactions 204, performance 208. Other new `bronze/` objects (assets, eclipse) are the day's scheduled pulls, not this act.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S32",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:28:00Z",
  "one_line": "Round 1 ~PB (WORLD). 33 keys written, each equal to V3's signed lists at V3's current hash 03a77b33: positions 4, transactions 7, performance 22 (the 22 v112 graded; the 11 positions/transactions keys were never under v112's gate, by design). S3 read here: 33 of 33 have exactly one version, VersionId and size equal the record, written 09:56:36Z-17:04:37Z inside the ledger window; first performance write 12:25:16Z after v112. Ledger CLOSED; 36 worktrees read, 8 carry a stale marker of this closed entry. Performance prefix 185 -> 208 = 22 + the chain's own 10-15 key. The 18,000 request bound is UNSIGNED: V3 says ~2,470 (estimate), 16,000 was accepted by CTO msg 8211, 18,000 is the issuer's AMENDMENT 5 alone; 16,768 used, 0 throttles; requests are reads, the served blast radius is not breached. IB208-1-AC1..AC3 PASS. Dismissed (1): D2-S205 (the act's record, verified).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S205"
  ],
  "spec_asserts": "Never-widen (CLAUDE.md section 5): the act's write set sits inside both signed halves at the packet's current hash; NEVER-2: a completed deploy's ledger is closed and every live worktree's markers are read; ADJUDICATION_v112: no performance day before the control's grade.",
  "world_is": "The 33 absent Orion bronze keys exist, one version each, inside the signed set; the backfill is reversible per key by version. The vendor request count ran 6.8x the signed estimate under an issuer-raised bound the CTO did not sign. Eight worker worktrees show the closed ledger as open until they merge trunk.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:2xZ of the invocations in IB-pr-568: IB208-1-AC1..3 PASS, exit 0; round-close-check ~PB round 1 MAY-CLOSE",
    "sha256sum ORION_RECUT_PAIRS_PACKET_V3.md = 03a77b33...; V3 section 3 table lines 54-56 and performance list lines 62-63; request estimate line 79",
    "aws s3api list-object-versions opal-data-inf for each of the 33 keys: 1 version each, 0 delete markers, VersionId and Size equal IB208-1_orion_backfill_record.json; LastModified 2026-10-15T09:56:36Z..17:04:37Z; first performance 12:25:16Z",
    "aws s3api list-objects-v2 opal-data-inf bronze/{positions,transactions,performance}/ counted client-side: 4,729 / 204 / 208; new since 09:00Z beyond the 33: the chain's 2026-10-15 keys only",
    "git show 46bc11fc02 (AMENDMENT 5, issuer, 16,000 -> 18,000 on IB2 msg 8303); d43edbf835 (AMENDMENT 3, 16,000 accepted on CTO msg 8211)",
    "org/critical_paths/change_management/20261015T0827Z_irpt-orion-33day-backfill-20261015_deploy_completion.md: CLOSED 20261015T170923Z",
    "git worktree list --porcelain (36) + ls-tree .open_deploys: 8 branch HEADs carry the closed backfill marker; 8 carry nfra-oplgtw-fd2-orion-drain (CLOSED 2026-10-14T16:07Z)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PB_DRAIN_END_20261015.md @f7ffcd0453 (msg 8482)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The act's own record, verified key by key against S3 and the signed set. The unsigned request bound is named for the CTO as a P2, not a hazard on served data."
 }
]
```
