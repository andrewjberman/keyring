# AMGT_HARVST -- round 85 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-14T14:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T14:00:00Z. L8 packet: 2.0.0_SA_COO~W1 msg 5587, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round85/L8_PACKET_ROUND85_20261014.md` @b7a0107d55 (blob 1c5c865c8444, verified).
4 orders: 3 complete, bz-11 CANCELLED NOT MET. round-close-check --round 85: MAY-CLOSE.

**Rows:** 7 of 7 since v79's watermark: 2 graduated INERT, 5 dismissed.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S50",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:00:00Z",
    "one_line": "ROUND 85 L8: MAY-CLOSE (3 of 3 complete with proofs, bz-11 CANCELLED NOT MET). The one-refresh seam fires and does not cure the expiry; the wsj/barrons journey is not shown.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "ROUND 85 L8 read, on this seat's re-runs. Packet @b7a0107d55 (blob 1c5c865c8444, verified), msg 5587. round-close-check --round 85: orders=4, 3 complete, proof_ok 3, judgment 0, MAY-CLOSE; bz-11 reads <status>cancelled. bz-11: the committed close read deliverables/0.7.0_AE_CloudOps~ZW/round85/bz11_AC1.out reads 'PUBLISHER=wsj VERDICT=NOT_CURED', 'PUBLISHER=barrons VERDICT=NOT_CURED', 'CLOSE=NOT_MET' rc=0; AC2 re-run here: 10 passed. bz-12's guard is at HEAD: lib/opal_data_harvest/backfill_driver.py:59 REFRESH_PUBLISHERS = frozenset({'wsj', 'barrons'}) and :404 gates the refresh on it (3d88eccbc3 is an ancestor of HEAD). WHAT THE ROUND SHOWS: the refresh fires once and reports done (17 s, 16 s) and the next job of the same publisher is refused 'expired' again (Z-S121). The journey the project exists for, a wsj and barrons cycle that completes without an expiry stop, is NOT shown. Not read by this seat: the site-Z checkpoint files and cycle_runner.log (site Z; the committed AC1 output is the read). Z-S119 stays OPEN in REMEDIATION_v17 with 2.0.0_SA_COO~W1; Z-S121 is its evidence. The park after round 85 (Andrew-direct via CTO msg 5209) or a round 86 is the CTO's analysis.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_HARVST --round 85: MAY-CLOSE",
        "deliverables/0.7.0_AE_CloudOps~ZW/round85/bz11_AC1.out: CLOSE=NOT_MET",
        "3.0.0_SA_CVO pytest round85/test_bz11_close_read.py: 10 passed",
        "git grep REFRESH_PUBLISHERS lib/opal_data_harvest/: backfill_driver.py:59, :404"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The round's L8 read record."
  },
  {
    "id": "AMGT_HARVST-D1-C-S51",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:00:00Z",
    "one_line": "GRADUATED to REMEDIATION_v18, INERT: Z-S121 (refresh fires, expiry not cured; why unread) to the CTO; Z-S120 (STOP file's parent directory never created) to ~W1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S121",
      "AMGT_HARVST-Z-S120"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v18, INERT: Z-S121 (the bz-11 NOT_MET evidence: refresh done, next job refused 'expired' again, DETAIL 'SignInRefused: 401 under --no-sign-in: no refresh'; no seat read a session, credential or producer source, so WHY is unread) -> 1.0.0_SA_CTO~DELL1, whose round-85 analysis decides park or round 86. Z-S120 (nothing creates the runner's STOP file's parent directory, so the graceful stop cannot be signalled as documented) -> 2.0.0_SA_COO~W1, carried to the park record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_HARVST-Z-S121, AMGT_HARVST-Z-S120"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "AMGT_HARVST-D1-C-S52",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:00:00Z",
    "one_line": "DISMISSED 5 round-85 rows (2 BLOCKING resolved in the round), each with its own reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S16",
      "AMGT_HARVST-D1-W139-S3",
      "AMGT_HARVST-D1-W139-S1",
      "AMGT_HARVST-D1-W139-S2",
      "AMGT_HARVST-D1-W140-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, 5 rows: D1-S16: BLOCKING, resolved: bz-12 limits the refresh to REFRESH_PUBLISHERS {wsj, barrons} (backfill_driver.py:59, :404 at HEAD; merged 3d88eccbc3 under CTO ADDENDUM 1). D1-W139-S3: BLOCKING, resolved: the issuer corrected decomp_ref.to_ref after the merge (8821b89159); round-close-check reads bz-9's proof OK. D1-W139-S1: Order-premise note on the run record's field list; no defect served. D1-W139-S2: Test-harness note on the installer -Plan test; no defect served. D1-W140-S1: The test helper's default publisher moved to wsj; AC2 100 passed after it; no defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows named",
        "git grep REFRESH_PUBLISHERS at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, 5 rows: D1-S16: BLOCKING, resolved: bz-12 limits the refresh to REFRESH_PUBLISHERS {wsj, barrons} (backfill_driver.py:59, :404 at HEAD; merged 3d88eccbc3 under CTO ADDENDUM 1). D1-W139-S3: BLOCKING, resolved: the issuer corrected decomp_ref.to_ref after the merge (8821b89159); round-close-check reads bz-9's proof OK. D1-W139-S1: Order-premise note on the run record's field list; no defect served. D1-W139-S2: Test-harness note on the installer -Plan test; no defect served. D1-W140-S1: The test helper's default publisher moved to wsj; AC2 100 passed after it; no defect."
  },
  {
    "id": "AMGT_HARVST-D1-C-S53",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:00:00Z",
    "one_line": "L10 record: round 85 MAY-CLOSE; 7 of 7 rows since the watermark dispositioned; Z-S119 stays open.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L10 PRECONDITION MET: round 85 MAY-CLOSE on this seat's run; every investigation row after ADJUDICATION_v79's watermark (2026-10-13T21:20Z) is dispositioned: 7 of 7 (C-S51 2 graduated, C-S52 5 dismissed). Open with owners: Z-S119 (REMEDIATION_v17, 2.0.0_SA_COO~W1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this file's rows C-S50..C-S52"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 record."
  }
]
```
