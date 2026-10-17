# AMGT_HARVST -- rounds 77-78 remediations (dell1)

<sweep_watermark>2026-10-09T17:52Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T17:52:00Z. Graduated at ADJUDICATION_v70: 3 rows, all INERT.

```json
[
  {
    "id": "AMGT_HARVST-D1-S3",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The activated cycle runner and r47 collected almost nothing on 2026-10-09: bbg 0 fetched over 96+ runs (pair errors, now fixed in code by bv-1), wsj and barrons 0 attempts (sign_in_refused, bs-3), and sa 3,324 of 3,339 rejected with no sa run after 09:59Z -- the sa rejection has no measured cause.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S3",
      "org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round77/run_record_census.out",
      "org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round77/bu1_cycles.out"
    ],
    "remedy": "Name the cause of sa's 3,324 rejections and why sa stopped after 09:59Z; per publisher, read the first cycle on the merged bv-1 code. Close when: each publisher's newest run record states fetched > 0 or a named stopped reason",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-S4",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No FWD-18 source wrote a silver listing_hit or article part after the runner's 08:57Z activation (0 new parts across eight tables), so the runner stored no new article in its first 4+ hours.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S4",
      "org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round77/silver_parts_census.out"
    ],
    "remedy": "Run the merged bv-1 runner to a completed cycle. Close when: a silver article part for at least one FWD-18 source is written by a completed cycle after the merge, read by LIST with its denominator",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-W133-S2",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "requeue_floors reads only the newest cycle record, so a pair owed from cycle N that cycle N+1 stopped before reaching is not re-queued in N+2 and is asked with an unmoved floor that may be newer than its failed window. Accepted for the bv-1 merge by 1.0.0_SA_CTO~Z; its fix goes to the round-78 analysis.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W133-S2",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_BV1_MERGE_SITEZ_20261009.md line 31 (@e3f030ba85): 'The residual in row D1-W133-S2 (re-queue reads only the newest cycle record) is accepted for this merge. Its fix goes to the round-78 analysis'"
    ],
    "remedy": "Re-queue reads every failed pair still owed (all readable cycle records since the pair's last success). Close when: a test with a stopped cycle N+1 shows N's failed pair asked in N+2 with N's floor",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  }
]
```

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-D1-S3`: RE-OWNED to `0.7.0_AE_CloudOps~SC1`. Next act: SC1 reads each publisher's newest run record now and states fetched > 0 or a named stopped reason per publisher, filed under its deliverables; un-parks when all four publishers carry one of the two. Basis: Not met: the close reads each publisher's newest run record in S3 (store.table_prefix run_record), and the last read in this channel is 2026-10-09 13:39Z (sa 3,324 rejected, bbg fetched 0); this worker may not run S3 reads and no later record shows fetched above 0 or a named stop.
- `AMGT_HARVST-D1-S4`: RE-OWNED to `0.7.0_AE_CloudOps~SC1`. Next act: SC1 runs the LIST under store.table_prefix for a FWD-18 source's silver article table after a completed bv-1 cycle and records the part and denominator; un-parks when one part dated after the merge is listed. Basis: Not met: the close needs a silver article part written by a completed cycle after the bv-1 merge, read by LIST; the latest LIST in this channel (2026-10-09 13:48Z) reads 0 new parts across all eight FWD-18 tables and no later LIST exists at HEAD.
- `AMGT_HARVST-D1-W133-S2`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 adds a test in which cycle N+1 stops on the five-error cap of test_ii and shows cycle N+2 asking N's failed pair with N's floor; un-parks when that test passes at HEAD. Basis: Not met: test_bv1 requeue_scenario (test_vi, lib/opal_data_harvest/test_bv1_cycle_continues_past_pair_errors.py:190-213) runs three cycles that all complete (r2 completed True); no test has cycle N+1 stopped, so the close's stopped-cycle clause is not demonstrated.

-- 3.0.0_SA_CVO
