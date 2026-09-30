# AMGT_HARVST task order -- `HVST-q-3` -- ROUND 27 chain 3: FWD-7 ELIGIBILITY CENSUS UNDER THE DECLARED SET (bbg, wsj) -- eligible of 191 over the window, COVERED set only, excluded names by reason (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~72</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no write; read-only census over the served gold chatter_daily.
comp-iam: RUN at L5 -- S3 GET/LIST on harvest gold only. NO PUT, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is eligibility read from the FOUND set or from any-publisher coverage (one incidental hit making a name eligible). The census reads publishers_covered_codes only, and prints the count a found-set read WOULD give beside it as the negative arm.
</preflight>

## 0. THE STANDING CLAUSES

1. **READ-ONLY.** No write, vendor call or deploy.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~72/scripts/`; outputs named `q3_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~72/AMGT_HARVST.TO-HVST-q-3.fwd7-eligibility-census.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-q-3.fwd7-eligibility-census`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~72/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT (`prd/AMGT_HARVST_PRD.md` v0.4 `C-HV-RANK-DECLARED-SET` and `C-HV-COVERED-VS-FOUND`)

- **ELIGIBLE:** every publisher in the declared set covered every day of the window. Otherwise the name is EXCLUDED as
  `PARTIAL_COVERAGE` or `NOT_SEARCHED`.
- **Coverage reads `publishers_covered_codes` only.**
- **The declared set for this census is (bbg, wsj).**
- **The window** is the chatter producer's own window (`lib/research/metrics/chatter_axis.py` `window_bounds(as_of,
  WINDOW_DAYS)`), at the served `chatter_daily`'s as-of.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). ONE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~72/scripts/q3_ac1_eligibility_census.py</invocation><expect>ELIGIBLE UNDER (bbg, wsj):</expect></criterion>
</proof_of_spec>

**What the criterion must print:**
- the served `chatter_daily` part and its as-of, the window, and the universe of 191;
- the line `ELIGIBLE UNDER (bbg, wsj): N of 191`;
- the excluded names by reason, with counts;
- the eligible names;
- beside that, a negative arm: the count a FOUND-set read and an any-single-publisher read would give;
- the floor test, N against 10.

## 3. ORDER

Run it only after `HVST-q-1` drains. The dispatch comes then, so the census counts `q-1`'s coverage.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` s.4 item 3.
- Its N sets `HVST-q-7`'s expected outcome. Below 10, the flip's expected outcome is a HOLD with its `empty_reason`.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>27</round>
<slot>~72</slot>
<fabric>site-z</fabric>
