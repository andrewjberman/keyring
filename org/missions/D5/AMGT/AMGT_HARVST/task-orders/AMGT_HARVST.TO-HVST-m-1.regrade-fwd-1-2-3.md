# AMGT_HARVST task order -- `HVST-m-1` -- ROUND 23 chain 1 of 3: RE-GRADE FWD-1 / FWD-2 / FWD-3 FROM THE SERVED STORE (read-only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~53</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest prefixes; this cell writes nothing to S3.
comp-iam: RUN at L5 -- S3 GET/LIST only on s3://opal-data-harvest/ (bronze, silver, and any discovery/listing records the store holds). NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a pass rate over a filtered population (for example only JSON bronze, or only the publishers that happen to parse), or a "byte-exact" check against a hash the reader itself computed. AC1 prints per publisher the full denominator, and the hash compared is the one RECORDED at ingest.
</preflight>

## 0. THE STANDING CLAUSES

1. **READ-ONLY. NO S3 WRITE OR DELETE, NO VENDOR CALL, NO CODE CHANGE, NO DEPLOY.** This cell MEASURES; it grades
   nothing. The CTO grades at L10.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/scripts/`; outputs named `m1_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/AMGT_HARVST.TO-HVST-m-1.regrade-fwd-1-2-3.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-m-1.regrade-fwd-1-2-3`.
4. **Whatever this machine cannot see is printed as NOT MEASURABLE HERE, with the reason.** It is never estimated.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE TARGETS, VERBATIM (`org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`)

- **FWD-1** -- Every article we collect can be read again exactly as the publisher sent it. DONE WHEN EXERCISED -- for one
  run on the validation security, every article from each of the five publishers, and the listing page that found it, is
  re-opened from our store and matches what was received, byte for byte.
- **FWD-2** -- Everything a publisher tells us about an article is kept, in a clean queryable form, with nothing lost.
  DONE WHEN EXERCISED -- every field present in the received article (including language, paywall flags, the
  publisher's own ticker tags, sentiment, themes and summary where sent) appears typed in the queryable table, rebuilt
  from the stored original, and a query by company and date returns it.
- **FWD-3** -- For any article, we can say how we found it. DONE WHEN EXERCISED -- every stored article states whether it
  came from the publisher's own list for that company or from a search, with the search words and its position in the
  results; a second run the same day fetches no article we already hold.

Store: `s3://opal-data-harvest/` (the harvest bronze, silver and listing prefixes). `lib/research/harvest/store.py` holds
the key builders and the bronze metadata (including the recorded hash). The five publishers are barrons, bbg, ft, sa and
wsj. The validation security is the one the PRD names (Lenovo, `992_HK_Equity`).

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-m-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/scripts/m1_ac1_fwd1_reread.py</invocation><expect>FWD-1 MEASURED: per publisher, bronze article objects re-read and compared byte-exact against the hash RECORDED at ingest (matched / mismatched / no recorded hash / unreadable, over that publisher's denominator); the same for the listing pages that found them (listing objects linked from the article's discovery record, and how many articles have no linked listing object); a separate line for the validation security's articles. Every count carries its denominator</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-m-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/scripts/m1_ac2_fwd2_fields.py</invocation><expect>FWD-2 MEASURED: per publisher, the field names present in bronze (the received article) versus the columns present in the silver row built from it, with the count of articles missing at least one bronze field in silver and the most common missing fields named; the named fields (language, paywall flags, ticker tags, sentiment, themes, summary) reported per publisher as SENT-AND-KEPT / SENT-AND-LOST / NOT SENT; and one query by company and date (the validation security, one date) returning its rows from silver</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-m-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~53/scripts/m1_ac3_fwd3_provenance.py</invocation><expect>FWD-3 MEASURED: per publisher, stored articles with a discovery record stating LIST or SEARCH, with the search words and result position where SEARCH (present / absent counts over the denominator); and the dedupe evidence the store holds (duplicate article keys across runs, and whether a same-day re-run fetched an already-held article, from run records if any exist, else NOT MEASURABLE HERE with the reason)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No grade, no fix, no write of any kind to S3, no vendor call, no re-collection.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **From `ROUND_ANALYSIS.round22.md` @`9d7bd0e4f9` s.2 ruling 3 and s.4 item 1:** seven FWDs have gone ungraded since
   round 10 (a Grep of rounds 11-22 read 0 hits). This cell measures FWD-1, FWD-2 and FWD-3 for the CTO's grade.
2. **Risk LOCAL:** it reads the served store and writes only deliverables.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>23</round>
<slot>~53</slot>
<fabric>site-z</fabric>
