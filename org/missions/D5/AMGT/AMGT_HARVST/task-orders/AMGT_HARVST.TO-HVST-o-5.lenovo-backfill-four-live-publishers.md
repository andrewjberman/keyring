# AMGT_HARVST task order -- `HVST-o-5` -- ROUND 25 chain 4 of 4: LENOVO'S BACKFILL FROM 2026-01-01 ON THE FOUR LIVE PUBLISHERS (barrons, bbg, ft, wsj), UNDER A PAIR -- then the same run again fetches nothing (FWD-9, then FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-o-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~65</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector's Scheduled Task is Disabled, 0 triggers; this act is ONE manual invocation of the collector's own script (and one repeat), not a schedule. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to barrons, bbg, ft and wsj by the collector script only (R-21 @b390c36444: scripted, never an agent turn); S3 PUT of new bronze and silver objects, never-overwrite. NO DELETE, NO sa call (the sa leg waits on the renewal), NO deploy.
comp-adversary: RUN at L5 -- the adversary is a run that "succeeds" on a stale catalog (fetching nothing because the worktree's own empty runtime root was used, or everything because the held catalog was not read), or objects written outside the pair. The act runs on the ONE runtime root named below; AC1 compares every written key to the halves; AC2 reads the repeat's run record.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/NEVER_WIDEN_HALF_COO_O5.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's checks exist at `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/`
   (`o-5.before.py`, `o-5.AC1.py`, `o-5.AC2.py`).
3. `o-5.before.py` has been run and its BEFORE snapshot written. It must match the halves' BEFORE state; otherwise STOP
   and report.

## 1. THE ACT (from the worktree's code at CLOUD HEAD; the runtime root is the MAIN tree's)

1. **The security.** Write Lenovo's entry (`key` `992_HK_Equity`) from
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json` to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~65/o5_lenovo.security.json`. It is not in
   `config.json`'s `pilot_securities`.
2. **The plan, zero-network, printed first:**
   `python -m lib.opal_data_harvest plan --security-json <that file> --publishers barrons bbg ft wsj --floor 2026-01-01 --with-watermark`.
   Save it as `o5_plan.txt`.
3. **The run, ONCE:**
   `python -m lib.opal_data_harvest run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01 --new-only --security-json <that file> --publishers barrons bbg ft wsj --runtime-root "C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest"`.
   - Save stdout and stderr as `o5_run1.txt`.
   - Record the run record's path and `run_id` in `o5_run_ids.json`.
4. **The repeat, ONCE, the same command, the same day.** Save it as `o5_run2.txt`, and add its run record to
   `o5_run_ids.json`.
5. Run AC1 and AC2.
6. **A publisher that challenges, denies or fails is a RESULT, not a retry loop.** Record it and go on. Do not log in,
   solve a challenge, or repeat a batch to provoke one.
7. **Rollback** (named in the halves): no overwrite is possible (never-overwrite). Removing a new object is a delete,
   which is a human word. Report the keys.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~65/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-o-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/o-5.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-o-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round25/checks/o-5.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~65/AMGT_HARVST.TO-HVST-o-5.lenovo-backfill-four-live-publishers.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-o-5.lenovo-backfill-four-live-publishers`. Report once, with:
- the plan;
- each run's per-publisher job status, pages walked, the oldest date reached, and keys fetched and skipped;
- both criteria's output;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **Source:** `ROUND_ANALYSIS.round24.md` @`6c5b4339a1` ruling 3 and s.4 item 5.
2. **Vendor authority:** R-21 @`b390c36444` ("all recs approved, and you have all the egress you want for vendors"), on
   its stated mechanism: the collector script, not an agent turn.
   - The HARVST commissioning record's "gradual backfill budget ... reserved to Andrew" (`HARVEST_COMMISSIONING_20260915_W.md:127`)
     predates R-21.
   - The CTO's ruling 3 cites R-21 for this run. This seat does not re-open it. The budget of this one run is bounded by
     the plan: 4 publishers x at most 25 listing pages.
3. **Dispatched only after both halves are committed.** The COO half is measured at signing.
4. **Checks are issuer-written before dispatch.** This is the same departure as `n-4`: the BEFORE snapshot has to be
   taken at signing.
5. **This run feeds `HVST-o-1`'s coverage.**
   - If it lands before `o-1` merges, its run record lacks the reached-span field. `o-1`'s rule then falls back to the
     listing-hit spans.
   - The record stays in the runtime root either way.
6. **FWD-9 grades on this run** (ruling 2: the plan is a labelled ceiling). The other 190 names follow next round, on
   this run's actual page counts.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>25</round>
<slot>~65</slot>
<fabric>site-z</fabric>
