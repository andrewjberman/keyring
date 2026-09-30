# AMGT_HARVST task order -- `HVST-m-3` -- ROUND 23 chain 3 of 3: RE-GRADE FWD-8 / FWD-9 FROM THE SERVED STORE (read-only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-m-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~55</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on the harvest prefixes; this cell writes nothing to S3.
comp-iam: RUN at L5 -- S3 GET/LIST only on s3://opal-data-harvest/ (bronze, silver, the newest gold parts, any run or plan records). NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is "history since 2026-01-01" read off the daily table's ROW range (every day has a row by construction, whether or not anything was collected) instead of off the ARTICLES; and an "undelivered" count taken from a source this machine cannot see presented as a measurement. AC2 reads first/last ARTICLE dates; AC1 names its source or prints NOT MEASURABLE HERE.
</preflight>

## 0. THE STANDING CLAUSES

1. **READ-ONLY. NO S3 WRITE OR DELETE, NO VENDOR CALL, NO CODE CHANGE, NO DEPLOY.** This cell MEASURES; it grades
   nothing. The CTO grades at L10.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~55/scripts/`; outputs named `m3_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~55/AMGT_HARVST.TO-HVST-m-3.regrade-fwd-8-9.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-m-3.regrade-fwd-8-9`.
4. **Whatever this machine cannot see** (for example files held only on another desktop) **is printed as NOT MEASURABLE
   HERE, with the reason.** It is never estimated.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~55/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE TARGETS, VERBATIM (`org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`)

- **FWD-8** -- Articles already collected but never delivered reach the store. DONE WHEN EXERCISED -- every article and
  link held only on the collecting desktop is in the store, with none duplicated. (Source: field map A, "83 bodies, 84
  links, 0 uploaded".)
- **FWD-9** -- Each company on the list has its publication history since 1 January 2026 in the store and on its
  timeline. DONE WHEN EXERCISED -- for each security Andrew's list names (Lenovo first), the backfill has run from
  2026-01-01; the number of listing pages each publisher would be asked for was printed before the run; every day from
  2026-01-01 has a row on the daily series; and running it again adds nothing.

**Where things live:**
- Store: `s3://opal-data-harvest/` (`lib/research/harvest/store.py` has the key builders).
- The covered list is the pool universe the securities file is built from
  (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`, 191 securities).
- Field map A and the round-10 analysis (`org/missions/D5/AMGT/AMGT_HARVST/ledger/`) record where the undelivered
  desktop articles were counted. Search the repo for that inventory: an import manifest, a file list, an upload ledger.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-m-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~55/scripts/m3_ac1_fwd8_undelivered.py</invocation><expect>FWD-8 MEASURED: the inventory of collected-but-undelivered articles and links named by source (file path or record), with its counts by publisher (83 bodies / 84 links at the field-map reading); for each, whether it is now in the store (matched by article key or URL) and whether any is stored twice; or, if no inventory is readable from this machine, NOT MEASURABLE HERE with the paths searched and the reason. Denominators printed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-m-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~55/scripts/m3_ac2_fwd9_history.py</invocation><expect>FWD-9 MEASURED: per covered security (Lenovo first), the first and last ARTICLE date in silver and in the served mention part, and whether the first is on or before the 2026-01-01 floor, with the securities short of the floor listed and counted over the covered denominator; whether the daily series has a row for every day from 2026-01-01 to its last day per security (missing-day count); any stored backfill plan or run record showing listing pages per publisher printed before a run, else NOT MEASURABLE HERE; and duplicate article keys across runs (the "again adds nothing" clause)</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No grade, no backfill, no upload of desktop articles, no write of any kind, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):** from `ROUND_ANALYSIS.round22.md` @`9d7bd0e4f9` s.4 item 3. Round 10's table was the last
measured state. Risk is LOCAL: it reads the store and writes deliverables only.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>23</round>
<slot>~55</slot>
<fabric>site-z</fabric>
