# AMGT_HARVST task order -- `HVST-k-2` -- ROUND 21 chain 2 of 2: THE UPDATED-TIME CENSUS -- does silver carry an updated or modified time per article? Measurement only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-k-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~50</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest silver or bronze prefixes; this cell writes nothing served.
comp-iam: RUN at L5 -- S3 GET/LIST only on Opal's own harvest bucket (silver article parts, and the bronze objects they were built from where a silver field is absent). NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a census that reads a time field present on a FEW publishers and reports "silver carries an updated time", or one that equates a field's presence with a value distinct from published_utc. AC1 prints per publisher both the presence count and the DISTINCT-value count, each with its denominator.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO CODE CHANGE, NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** Read only what is already in Opal's harvest
   bucket. A page's `dateModified` counts only if it is already stored in bronze or silver; nothing is fetched.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~50/scripts/`; outputs named `k2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~50/AMGT_HARVST.TO-HVST-k-2.updated-time-census.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-k-2.updated-time-census`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~50/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE QUESTION (`ledger/ROUND_ANALYSIS.round20.md` @`4b8bd40242`, s.2 ruling 3 and s.4 item 2)

HD's served event is led by a barrons article stored at `published_utc` 2026-08-17 16:24Z, a day before the results it
reports. It is most likely a preview that was re-headlined after the results. Choosing the earliest `published_utc`
promotes it, and the span starts a day early.

The CTO rules the lead on this census:
- If silver carries an updated or modified time, the lead is the earliest member by that time.
- If it does not, the early start is disclosed.

**Answer, and do not rule:**
1. Which timestamp fields do the silver article rows carry, per publisher? Name every field whose name or content is a
   time (for example `published_utc`, `updated`, `modified`, `dateModified`, `last_modified`, a vendor listing time).
2. For each such field, per publisher: in how many articles is it PRESENT, and in how many does its value DIFFER from
   `published_utc`?
3. Where silver lacks a time field, do the bronze objects the silver rows were built from carry one (a page's
   `dateModified`, a listing's updated time)? Report the same two counts. Read bronze only through the keys silver
   records.
4. **HD's barrons lead, by name** (the article in HD's served event that leads it): every time value found for it in
   silver and in bronze.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). ONE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-k-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~50/scripts/k2_ac1_updated_time_census.py</invocation><expect>A CENSUS OVER THE SILVER ARTICLES AS LANDED TODAY (120 at the cut, denominator printed and per publisher): (a) every time-bearing field in the silver rows, per publisher, with PRESENT and DIFFERS-FROM-published_utc counts, each over that publisher's article count; (b) the same for the bronze objects the silver rows point to, with the number of bronze objects read and the number that could not be read, each named; (c) HD_US_Equity's served-event lead, by article key and headline, with every time value found for it; (d) a one-line summary per publisher: UPDATED-TIME AVAILABLE on k of n articles, or NONE. PASS only if (a)-(d) all print with their denominators</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No code change, no gold write, no fetch from any vendor, no deploy. It records NO ruling on the lead; that is the CTO's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Independent of `k-1`** (disjoint write surfaces). The two run in parallel, `~49` and `~50`.
2. **Vendor boundary:** Seeking Alpha is at HTTP 402 (row `Z-W37-S4`, renewal pending). This cell reads only what is
   already stored, so the 402 does not bear on it.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>21</round>
<slot>~50</slot>
<fabric>site-z</fabric>
