# AMGT_HARVST task order -- `HVST-q-1` -- ROUND 27 chain 1 (FIRST): `p-3(b)` -- ONE LENOVO bbg/wsj COLLECTION ON THE SIGNED CODE (a PERSISTED, SPAN-BEARING run record), ITS UPLOAD, AND THE `chatter_daily` REBUILD THAT READS IT, UNDER A PAIR (FWD-7, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~70</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled, 0 triggers; ONE manual collection, its upload, ONE gold build. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to bbg and wsj by the collector script only (R-21 @b390c36444); S3 PUTs: ONE persisted run record (amgt/harvest/bronze/run_record/), the upload's bbg/wsj bronze and silver, ONE chatter_daily part. NO DELETE, NO ft/barrons/sa call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is coverage credited to the run that the listing hits alone produce (the p-3(a) state), or a run on code that writes no span. AC2 computes Lenovo's coverage from the persisted run record ALONE (run_record_spans, no listing hits) and requires bbg/wsj spans from it.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P5.md` @`dadba8badd`;
   - `1.0.0_SA_CTO~Z`'s half, signed at this cut.

   **Act only inside them.**
2. The code at the act is the code at signing: `git diff --stat 2023d17e46 HEAD -- lib/opal_data_harvest lib/research/harvest`
   prints NOTHING. Round-27 cells `q-2` and `q-4`..`q-6` change these libs and merge only after this cell drains.
3. `python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-5.before.py` prints OK.

## 1. THE ACT (each command that reaches a put, named per the round-25 ruling 1)

1. **Collection, ONCE:**
   `python -m lib.opal_data_harvest run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01 --new-only --security-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~65/o5_lenovo.security.json --publishers bbg wsj --max-jobs 2 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`
   - `--max-jobs 2` overrides `config.json` `jobs_per_run: 1`.
   - It queues to the local outbox and makes ONE S3 put: the run record, via `worker._persist_run_record` ->
     `store.bronze_put("amgt","run_record",...)`.
   - Record `p5_run.json` shaped exactly
     `{"run_id": "<id>", "persisted_key": "<S3 key>", "jobs": [{"publisher": "...", "status": "...", "reached_span": ...}]}`.
     The jobs are copied from the run record.
2. **Upload, ONCE:** `python -m lib.opal_data_harvest upload-harvest --max-objects 60 --retrieval-mode backfill --runtime-root <same>`.
3. **Run AC1.**
4. **Coverage rebuild, ONCE:**
   `python -m lib.research.harvest.publication_gold build-daily --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the act's UTC date>`.
   This is one put.
5. **Run AC2.**

A refusal is Branch B, recorded and not retried. Rollback is forward only; a delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~70/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-5.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-5.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~70/AMGT_HARVST.TO-HVST-q-1.span-bearing-lenovo-run.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-q-1.span-bearing-lenovo-run`. Report once, with:
- each job's status and `reached_span`;
- the run record's per-key outcomes and `keys_stored_join` (`p-2`'s fields);
- the S3 keys per step;
- both criteria's output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` @`ff4405d3d5` s.4 item 1, rulings 6 and 4.
- The COO half and checks were signed @`dadba8badd` and re-measured at this cut: the snapshot is identical and the lib pin is
  unchanged. The CTO half is signed at the cut.
- The slot `~70` is the one its checks read (`p5_common.WK`).
- It also exercises `p-2`'s per-key outcomes on a real run (FWD-3).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>27</round>
<slot>~70</slot>
<fabric>site-z</fabric>
