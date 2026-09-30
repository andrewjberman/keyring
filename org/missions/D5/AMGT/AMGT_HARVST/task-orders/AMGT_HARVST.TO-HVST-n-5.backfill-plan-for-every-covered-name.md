# AMGT_HARVST task order -- `HVST-n-5` -- ROUND 24 chain 4 of 5: THE BACKFILL PLAN FOR EVERY COVERED NAME, PRINTED BEFORE ANY RUN (FWD-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~59</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest prefixes; this cell runs no backfill.
comp-iam: RUN at L5 -- S3 GET/LIST only (the stored listing objects and silver/bronze keys the collector already holds); NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a plan whose page counts are guesses for publishers or names with no stored listing size, printed as if known. AC1 marks every page count's basis (MEASURED from a stored listing size, or DEFAULT with the default named) and counts each kind.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL, NO BACKFILL RUN, NO S3 WRITE, NO DEPLOY.** This cell PLANS. The run is a vendor act under the
   harvester's scripted grant (R-21), and Seeking Alpha's leg waits on the account's renewal.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~59/scripts/`; outputs named `n5_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~59/AMGT_HARVST.TO-HVST-n-5.backfill-plan-for-every-covered-name.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-n-5.backfill-plan-for-every-covered-name`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~59/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round23.md` @`d1ec6f4118`, s.2 ruling 5)

**FWD-9 DONE WHEN (PRD):** "for each security Andrew's list names (Lenovo first), the backfill has run from 2026-01-01;
**the number of listing pages each publisher would be asked for was printed before the run**; every day from 2026-01-01
has a row on the daily series; and running it again adds nothing."

**Measured last round:**
- Of the 191 covered names, 11 reach the 2026-01-01 floor, 54 start after it, and 126 have no article.
- A plan exists only for Lenovo: `deliverables/0.9.0_WK_AMGT_HARVST~10/plan.json`, 5 publishers x 25 pages.

**Produce the plan for ALL 191 covered names** (`deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`):
- pages per publisher per name back to 2026-01-01, from the listing sizes the collector already knows;
- the per-name total, the per-publisher total and the grand total;
- the Seeking Alpha leg marked as waiting on the renewal.

Use the collector's own planning code if it has one (`lib/opal_data_harvest/`; the `~10` plan's producer) rather than a
new formula, and name it.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). ONE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-5"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~59/scripts/n5_ac1_backfill_plan.py</invocation><expect>A PLAN written to deliverables/0.9.0_WK_AMGT_HARVST~59/n5_backfill_plan.json and printed: for each of the 191 covered names (Lenovo first), pages per publisher back to 2026-01-01 with each count's basis (MEASURED from a stored listing size, or DEFAULT with the default named), the per-name, per-publisher and grand totals, the count of MEASURED vs DEFAULT page figures, the Seeking Alpha leg marked WAITS-ON-RENEWAL, and the planning code named by file:line. PASS only if all 191 names appear and every page count carries its basis</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No backfill run, no fetch, no vendor call, no write outside its deliverables folder.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):** from `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.3 item 5. The backfill run is NOT a cell until
this plan is read (analysis NOT-cells).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>~59</slot>
<fabric>site-z</fabric>
