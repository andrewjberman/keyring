# AMGT_HARVST task order -- `HVST-ac-3` -- ROUND 30 chain 3: THE PAIRED DAILY REBUILD -- `chatter_daily` READS ab-2's MENTION SNAPSHOT, SO 992_HK's DAYS CARRYING THE 2 IN-WINDOW bbg ARTICLES REACH THE PAGE (FWD-2, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ac-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~86</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer of harvest gold (the collector task is Disabled); this act is the one writer for its window.
comp-iam: RUN at L5 -- S3 GET/LIST on harvest gold, silver and run records; ONE PUT of a new chatter_daily part, never-overwrite. NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a rebuild that moves rows the pair does not name (a builder change or a new run record since signing). AC1 compares the written part row-for-row to the signed serializing dry run and its bytes; AC2 reads the two days through the served route.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/NEVER_WIDEN_HALF_COO_AC3.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
2. The issuer's act-start gate (`round30/checks/ac-3.signing.py`, without `--signing`) prints OK.
3. No other WORLD act of this project is in flight.

## 1. THE ACT (the command that reaches the put)

ONCE, from the code the halves name:
`python -m lib.research.harvest.publication_gold build-daily --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the UTC date of the act>`

It makes ONE never-overwrite put of `chatter_daily/date=<as-of>/part-<stamp>.parquet`. Then run AC1 and AC2. Rollback is
forward only.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~86/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ac-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/checks/ac-3.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ac-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round30/checks/ac-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round29.md` @`d0bc0a79f0` section 4 item 3, ruling 4.
- **The expected diff** is the 992_HK days that carry the 2 in-window bbg articles (2026-08-13, 2026-09-01), and nothing else.
  Their rolling fields on LATER 992_HK days (`trailing_7d_sum`, `trailing_30d_sum`, `cumulative_ytd`) move as a consequence.
  The signing dry run names every moved (row, field). "Nothing else" is graded against that printed list, never predicted.
- **The predecessor-code diff is required** (standing ruling 3), and so is the positive arm at the cut (RESAPP r53 ruling 1).
  `ac-3.signing.py` runs the producer's own `build_daily` through the real `write_gold` against a put-capturing client (the
  `aa-3` lesson), so the parquet serializes.
- **Round 29's 12 new run records** carry refused jobs only. The signing prints whether any of them credits coverage (it should
  not).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>30</round>
<slot>~86</slot>
<fabric>site-z</fabric>
