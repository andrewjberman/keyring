# AMGT_HARVST task order -- `HVST-n-6` -- ROUND 24 chain 5 of 5: `/timeline/day` -- PROFILE THE ~5.5 s ANSWER, THEN FIX IT IN CODE (proved locally; the deploy is a later paired act)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~60</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on timeline_api.py or the scoped API; this cell deploys nothing.
comp-iam: RUN at L5 -- S3 GET/LIST only (gold and silver the day route reads) and read-only Invokes of the deployed /timeline/day for the baseline timing; NO PUT, NO env change, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a "fix" timed on a warm local cache that the deployed function never has, or one that changes what the route returns. AC2 times the new code path against the same S3 reads the function makes, cold and warm; AC3 requires the response body byte-equal to today's for the same inputs.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO DEPLOY, NO S3 WRITE, NO ENV CHANGE, NO VENDOR CALL.** This cell profiles the deployed route and fixes the code,
   proved locally against the same S3 reads. Reaching users is a scoped-API redeploy under a never-widen pair, cut by the
   issuer after this cell drains. It is not this cell.
2. **The route's response must not change.** It is a speed fix only.
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/scripts/`; outputs named `n6_*`
   -- **never `.scratch/`.**
4. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/AMGT_HARVST.TO-HVST-n-6.timeline-day-profile-and-fix.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-n-6.timeline-day-profile-and-fix`.

<paths>
lib/research/harvest/timeline_api.py
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_timeline_routes.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL (routed from DSGN_AMGTV1 `ROUND_ANALYSIS.round7.md` @`0c498ee766` ruling 2; `AMGT_HARVST` round-23 analysis s.3 item 6)

**The problem:** the deployed `GET /api/scoped/amgt/security/{security_key}/timeline/day/{date}` answers in about 5.5 s,
warm, for a day with articles (CVO v9 section 2).
- The route is `timeline_api.get_timeline_day` with its loaders in `lib/research/api/scoped_amgt.py`, the timeline
  section ~:4160 onward.
- Its article loader reads silver and gold through `publication_gold`.

**Do this, in order:**
1. **PROFILE:** measure where the time goes, per step (each S3 list, each object read, each join), on the deployed path
   and on the same code locally.
2. **FIX** the dominant cost in code: for example, avoid listing or reading every silver part for one day. Keep the
   response byte-equal.

`scoped_amgt.py` is SHARED with AMGT_RESAPP. Touch only the timeline loaders, and state every hunk.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/scripts/n6_ac1_profile.py</invocation><expect>the BASELINE: the deployed /timeline/day timed for 3 days with articles (992_HK_Equity 2026-09-23, AMZN_US_Equity 2026-09-07, HD_US_Equity 2026-08-18), each 3 times, with the Lambda's own REPORT duration where readable; and the per-step breakdown of the OLD code path run locally against the same S3 reads (S3 list calls, objects read, bytes, seconds per step), the dominant step named</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-n-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/scripts/n6_ac2_new_path_timing.py</invocation><expect>the NEW code path, run locally against the same S3 reads for the same 3 days, cold and warm: per-step breakdown and total beside the OLD path's, with the S3 list and object-read counts OLD vs NEW; the ratio printed per day</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-n-6"><invocation>python -m pytest lib/research/harvest/tests/ lib/research/api/tests/test_timeline_routes.py -rA --tb=line</invocation><expect>both suites pass, with a new test NAMED that the day body for a fixture day is byte-equal before and after the change; and org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~60/n6_ac3_body_equality.txt records the 3 real days' bodies from the OLD and NEW paths as byte-equal (sha256 each); the pass count BEFORE and AFTER printed</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No deploy, no change to any route's response, no change to RESAPP's routes in `scoped_amgt.py`, no gold or silver write.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **From `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.3 item 6.** "LOCAL profile; the fix under a pair": the code is this
   cell, and the redeploy is a follow-on WORLD seat order under a pair, cut after this drains (the `i-2` -> `i-4`
   pattern).
2. **`scoped_amgt.py` is shared with RESAPP.** The deploy's pair traces the closure as for `i-4` and `yy-5`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>~60</slot>
<fabric>site-z</fabric>
