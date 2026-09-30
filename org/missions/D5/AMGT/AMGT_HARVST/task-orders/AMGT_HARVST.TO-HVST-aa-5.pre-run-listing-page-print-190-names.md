# AMGT_HARVST task order -- `HVST-aa-5` -- ROUND 28 chain 5: THE PRE-RUN PRINT OF PLANNED LISTING PAGES PER PUBLISHER PER NAME OVER THE 190 NAMES, NO REQUEST SENT (`C-HV-EGRESS`; FWD-9, FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aa-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~80</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- runs nothing; the collector's `plan` command only.
comp-iam: RUN at L5 -- S3 GET/LIST for the silver watermark only (the plan's --with-watermark read). NO vendor call (asserted: sockets to any publisher host blocked), NO S3 write.
comp-adversary: RUN at L5 -- the adversary is a plan figure presented as an estimate of actual pages. Every figure carries its basis (MEASURED / DEFAULT ceiling), and the total is labelled a CEILING.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO REQUEST TO ANY PUBLISHER, NO S3 WRITE.** It uses only the collector's zero-network `plan` command (plus its S3
   watermark read).
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~80/scripts/`; outputs named `aa5_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~80/AMGT_HARVST.TO-HVST-aa-5.pre-run-listing-page-print-190-names.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-aa-5.pre-run-listing-page-print-190-names`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~80/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT (`C-HV-EGRESS`: the pre-run print of planned listing pages per publisher)

- **The universe:** the 191 covered names in
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`, minus Lenovo
  (`992_HK_Equity`), which was already run. That leaves 190.
- **Per name and per publisher** (bbg, wsj, ft, barrons, sa), print the collector's own `plan` line:
  `python -m lib.opal_data_harvest plan --security-json <one name> --publishers <p> --floor 2026-01-01 --with-watermark`.
  It gives the bound and the planned pages at the config ceiling (`max_listing_pages`).
- **Per publisher totals**, with each figure's basis: MEASURED where a stored listing gives total pages, else the DEFAULT
  ceiling. The grand total is labelled a CEILING.
- The prior plan (`HVST-n-5`, `0.9.0_WK_AMGT_HARVST~59/n5_backfill_plan.json`) may be reused as a reference. This print is
  re-run on current code and current watermarks.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). ONE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aa-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~80/scripts/aa5_ac1_plan_190.py</invocation><expect>PLANNED LISTING PAGES CEILING:</expect></criterion>
</proof_of_spec>

**What the criterion must print:**
- 190 names x 5 publishers of plan lines (denominator printed), written to `aa5_plan_190.json`;
- per-publisher totals with their basis counts;
- the line `PLANNED LISTING PAGES CEILING: <N>`;
- `NETWORK CALLS TO PUBLISHERS: 0`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** `ROUND_ANALYSIS.round27.md` s.4 item 5 and ruling 5. It is the input to round 29's backfill pair.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>28</round>
<slot>~80</slot>
<fabric>site-z</fabric>
