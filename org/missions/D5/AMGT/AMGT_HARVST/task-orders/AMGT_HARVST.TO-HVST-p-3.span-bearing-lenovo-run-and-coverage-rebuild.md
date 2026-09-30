# AMGT_HARVST task order -- `HVST-p-3` -- ROUND 26 chain 3 of 4: ONE LENOVO bbg/wsj COLLECTION ON CURRENT CODE (a SPAN-BEARING run record), ITS UPLOAD, THEN THE `chatter_daily` COVERAGE REBUILD, UNDER A PAIR (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-p-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~68</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled, 0 triggers; this is ONE manual collection plus its upload plus one gold build. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to bbg and wsj by the collector script only (R-21 @b390c36444); S3 PUTs: the run record beside bronze (HVST-o-1's persist), the upload's bronze and silver, ONE chatter_daily snapshot part. NO DELETE, NO ft/barrons/sa call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a run on code that does not write the span (the o-5 case), or coverage "moved" by listing hits the run did not produce. AC1 reads the run record's reached_span per job and the S3 run-record object; AC2 compares the rebuilt chatter_daily to the signed expected coverage for Lenovo only.
</preflight>

## 0. BEGIN ONLY WHEN ALL FOUR HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/NEVER_WIDEN_HALF_COO_P3.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's checks exist in `.../round26/checks/`.
3. The code at the act is the code at signing, printed as the halves say.
4. `HVST-p-1` is complete. The coverage rebuild reads the newest mention snapshot.

## 1. THE ACT (each command that reaches a put, named per the round-25 ruling 1)

1. **The collection, ONCE:**
   `python -m lib.opal_data_harvest run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01 --new-only --security-json <Lenovo> --publishers bbg wsj --max-jobs 2 --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`
   - `--max-jobs 2` overrides `config.json` `jobs_per_run: 1`.
   - This queues to the local outbox, and persists the run record beside bronze (`o-1`: `store.bronze_put` source `amgt`,
     table `run_record`).
2. **The upload, ONCE:** `python -m lib.opal_data_harvest upload-harvest --max-objects 40 --retrieval-mode backfill --runtime-root <same>`.
3. **The coverage rebuild, ONCE:**
   `python -m lib.research.harvest.publication_gold build-daily --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the UTC date of the act>`.
   This reaches `build_daily` and then `write_gold`: one put of `chatter_daily`.
4. Run AC1 and AC2.
5. **A refusal is Branch B, recorded and not retried.**
6. **Rollback:** forward only. A delete is a human word.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~68/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-p-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-3.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-p-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round26/checks/p-3.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~68/AMGT_HARVST.TO-HVST-p-3.span-bearing-lenovo-run-and-coverage-rebuild.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-p-3.span-bearing-lenovo-run-and-coverage-rebuild`. Report once, with:
- each job's status and `reached_span`;
- the S3 keys written, per step;
- the Lenovo coverage and RESOLVED before and after;
- both criteria's output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- `ROUND_ANALYSIS.round25.md` @`300ea99310` s.4 item 3. This is the positive arm for FWD-7's gradable pair.
- **Checks and the COO half are issuer-written after `p-1` drains**, because the daily build reads the newest mention
  snapshot. They are then signed with a stub put-count dry run of all three commands (ruling 1).
- `p-2`'s fix to `worker.py`, if it merges first, changes the collection's run record. So `p-3` signs on the code at its
  signing, and the halves name that pin.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>26</round>
<slot>~68</slot>
<fabric>site-z</fabric>
