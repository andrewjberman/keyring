# AMGT_RESAPP.TO-AMGT-s-1 -- THE MODEL BLOCK: a covered name's figures from Bloomberg on this box, raw bytes landed before anything derives, every unit and sign MEASURED on three securities

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-1; manifest row S1; the head of the longest chain)

```
AMGT-s-1. THE MODEL BLOCK -- ~20 line items x 10 fiscal years + ~25 header scalars for a COVERED
name, pulled from Bloomberg DAPI on this box by a BOX-SIDE job, raw vendor bytes landing in the
version store BEFORE any derivation. Every mapped field carries a MEASURED unit and sign, re-measured
per field on at least two securities beyond the one the brief mapped (a US name; an ADR). Fiscal year
is the join key. Bloomberg's basis stated beside every number.

FWD-1's bar, verbatim: "An analyst gets a first-draft pack for a covered name without opening a
spreadsheet or a data terminal. DONE WHEN EXERCISED -- an analyst has actually done it, not merely
could." This cell builds the block; the EXERCISED bar is served by the page and is not claimed here.

THE SEAM IS NOT THIS CELL'S. A covered name is served by the pattern the daily dashboard pull already
runs in production on this box: a job ON THE BOX pulls, then lands to S3, and the page reads the
snapshot. Nothing crosses inbound from AWS. An uncovered name typed into a page is AMGT-s-2's and
needs the request path designed; do not design it here.

WHAT TO PRODUCE, the code under
    integrations/bloomberg/research/
and the deliverables under
    org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/

  (a) FIRST ACT, BEFORE ANYTHING ELSE:  timeout 120 python integrations/bloomberg/auth/dapi_check.py
      "DAPI: UP" continues. Anything else: the terminal is signed out or down -- file a BLOCKING row
      and STOP. ⛔ DO NOT SIGN IN. The sign-in is a 2-attempt budgeted act owned by another seat
      (integrations/bloomberg/READ_HERE.md s.2); a worker that types a password into a login window
      has left its order. "Up" is PERISHABLE on this box (a mid-session sign-out was measured today
      with no automatic recovery): re-run the check before each pull, not once.

  (b) THE PULL  integrations/bloomberg/research/model_block_pull.py
      For a Bloomberg ticker: the header scalars by ReferenceDataRequest and the fiscal-year history by
      HistoricalDataRequest, through the estate's raw client integrations/bloomberg/mcp/blp_client.py
      (raw blpapi; it is what makes this runnable under `python` = Python311, which has blpapi AND boto3;
      the cma interpreter has no boto3 -- READ_HERE s.3 says do not unify them). Start from the CRO's
      measured field map:
          org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_BLOOMBERG_FIELD_MAP_20260910.md
      (15 of 16 header scalars and 17 of 19 line items mapped on SAP GY Equity; the BAD_FLD ones listed
      -- do not retry those as written).

  (c) RAW BEFORE DERIVED (C-RAW-BEFORE-DERIVED; a CORRECTNESS rule, not an optimisation: Bloomberg's
      derived fields have no backfill). The FULL vendor response bytes land FIRST at
          s3://opal-data-research/raw/bloomberg/<security_key>/<YYYYMMDDTHHMMSSZ>/refdata.json
          s3://opal-data-research/raw/bloomberg/<security_key>/<YYYYMMDDTHHMMSSZ>/histdata.json
      and ONLY THEN the derived block at
          s3://opal-data-research/derived/model_block/<security_key>/<YYYYMMDDTHHMMSSZ>/model_block.json
      <security_key> = the ticker with spaces as underscores (AMGT-s-6's STORE_CONTRACT.md states the
      grammar; read it if it has landed). ⛔ IF THE BUCKET DOES NOT EXIST when you reach (c), that is a
      BLOCKING row (AMGT-s-6 creates it in this round) -- do NOT create a bucket, do NOT land anywhere else.

  (d) THE FIELD MAP, RE-MEASURED ON THREE SECURITIES  .../deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json
      The brief's map was measured on ONE security and says so (PRD s.6). Re-measure every mapped
      field's UNIT and SIGN on exactly THREE: SAP GY Equity (the control -- your reading must
      reproduce the CRO's), one US-listed name and one ADR, both chosen from the coverage universe
      by a rule you state (the corpus at C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research\
      names 89 covered companies; AMGT-s-12's universe.json enumerates them if it has landed). Per
      field: {mnemonic, unit, unit_status, sign, sign_status, measured_on: [...], basis} where
      *_status is MEASURED only when you read the value on that security and compared it against a
      known magnitude (F4's method), else UNRESOLVED-ON-<security>. A US name and an ADR are where
      F4's conventions are most likely to differ; a field that differs is a FINDING, recorded, and
      its unit is per-security in the map.

  (e) THE FISCAL-YEAR JOIN (C-FISCAL-YEAR-JOIN). Price and fundamentals land on different dates in
      one response (F5: 14 rows for 10 fiscal years; a date-string join drops 40% of the history).
      Join on fiscal year. check_join.py prints, per security, the FY row count and the orphan count,
      and one summary line (AC4).

  (f) THE BASIS BESIDE EVERY NUMBER (C-BLOOMBERG-BASIS, Andrew-ruled): every figure in model_block.json
      carries {value, unit, sign, basis: {mnemonic, definition}, vintage, source: "bloomberg-dapi"}.
      ⛔ Adopt Bloomberg's definitions. No mnemonic reproduces FactSet's recurring EPS across 8 tested;
      that normalization is proprietary and is NOT reverse-engineered into a lookalike (AC6).

  (g) THE COST AXIS (F2): the binding constraint is UNIQUE SECURITIES TOUCHED, not volume. This order
      touches at most THREE securities. pull_log.json records every security requested.
```

## DEPENDENCIES

**NONE in the manifest.** In the world: (c) needs `opal-data-research`, which AMGT-s-6 creates this
round (the issuance spawns this slot after that cell lands, and the decomposition's investigation row
AMGT_RESAPP-Z-S1 records the unlisted edge). Three cells wait on this one: AMGT-s-2, AMGT-s-3, and via
-3, AMGT-s-5; AMGT-s-9 needs it too.

## BOUNDS -- what this cell may not cross

```
⛔ integrations/bloomberg/READ_HERE.md BINDS IN FULL. Health first (a); on anything but "DAPI: UP",
STOP and row. NO SIGN-IN by this worker. Credentials reach a process ONLY through
integrations/bloomberg/auth/bbg_credentials.py's `--` exec wrapper and you need NONE: a DAPI session
on this box is loopback and unauthenticated from the client's side. Never mint data/bloomberg/.

⛔ C-RAW-BEFORE-DERIVED: raw bytes first, derived second, a stamp per write, never a write to a path
that exists. AC2 reads the stamps.

⛔ C-UNIT-MAP-MEASURED: a mnemonic-only map is silently wrong by 100x in some cells and 1e6 in others.
Every field carries a MEASURED unit and sign or says UNRESOLVED-ON-<security>; there is no inferred
unit in this deliverable.

⛔ C-FISCAL-YEAR-JOIN: fiscal year is the join key. Never the date string.

⛔ C-BLOOMBERG-BASIS: adopt and state; never reverse-engineer a vendor's proprietary normalization.

⛔ F2 / G-24: at most THREE unique securities, all COVERED names (inside the licensed use the daily pull
already exercises). An UNCOVERED name is AMGT-s-2's and carries its own vendor-word question; do not
touch one here.

⛔ C-STAGE-PERSISTS: the pull and the derivation are two stages, each persisting its own output and
each re-runnable alone. A single function that pulls-and-derives in memory and writes once is a
violation.

⛔ NO IAM CHANGE. If landing to the bucket is refused (AccessDenied), that is a BLOCKING row naming the
principal `python` ran as; do not attach a policy.

⚠ BOUND EVERY CALL. Each invocation runs under `timeout 120`; a timeout is the recorded output. One
security's full 10-year history was measured at ~180 points / ~3.4 KB / one call (F2) -- three
securities fit; do not widen.

⚠ A FIELD RETURNING EMPTY WITH NO ERROR has three indistinguishable causes (READ_HERE s.4: bad NAME,
wrong REQUEST TYPE, not ENTITLED). blp_client surfaces __field_errors__; read it and record it per
field rather than writing a null.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
bloomberg_health at ~19:48Z (0.0.3_BG_BBGTerminal, msg 21049): ok:true, confirmed by real reference
    reads on both interpreters (SPX Index PX_LAST 7589.71 dated 2026-09-10; dapi_check.py "DAPI: UP").
    That seat spent ONE of two sign-in attempts to get there. It read ok:false for ~50 minutes before
    that with no automatic recovery -- hence (a) before EVERY pull.

F2, F3, F4, F5 (CITED, the field map deliverable): 180 points / 3.4 KB / one call for one security;
    32 of 35 line items mapped on SAP GY Equity; units inconsistent across Bloomberg's own field
    families; 4 of 10 years split on the date string. EVERY ONE is re-measured by (d) and (e).

opal-data-research: MEASURED ABSENT at 12:24:50Z (graph) and 13:30-16:00Z (live). AMGT-s-6 creates it;
    (c) checks before landing.

comp-iam stats (RUN): 195 roles / 188 services; the principal `python` runs as on this box is whatever
    the daily pull's publish_to_portal.py uses to reach S3 -- read integrations/bloomberg/pipeline/README.md
    for it; if it cannot write opal-data-research, that is a BLOCKING row, not a policy edit.

comp-schedule (RUN to completion): 25 gates armed, none this project's; G-24 and G-19 bind this cell.
Interpreter: `python` on PATH = C:\Users\Opal Bloomberg\AppData\Local\Programs\Python\Python311\python.exe,
    blpapi + boto3 + pyarrow importable (measured at the cut). This is the PY_AWS interpreter the daily
    vehicle's landing legs use for exactly this reason.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-1.model-block-bloomberg-covered-name.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`, inside the granted prefix. blp_client,
dapi_check, READ_HERE, the field map, the corpus and AMGT-s-6/-12's deliverables are READ. S3 writes and
DAPI reads are operational and are not path-gated. `integrations/bloomberg/mcp/` and `pipeline/` are NOT
in your write surface and MUST NOT BE MODIFIED.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W1-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-1"><invocation>python integrations/bloomberg/auth/dapi_check.py</invocation><expect>a line containing "DAPI: UP" -- the terminal is signed in and an entitled session answered a real request at the moment this worker started; anything else is the signed-out signature and this criterion is REFUSED with a BLOCKING row, never rescued by a sign-in</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-1"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/check_landing.py</invocation><expect>one line of the exact shape "LANDING: raw 6 objects across 3 securities; derived 3 objects; raw-before-derived True; overwrites 0" -- read back from S3 by this script (list the prefixes, compare each security's raw stamp to its derived stamp), never from the pull's own log; "raw-before-derived False", fewer than 6 raw objects, or "overwrites" above 0 is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-1"><invocation>python -c "import json; m=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json')); f=m['fields']; three=[x for x in f if x['unit_status']=='MEASURED' and x['sign_status']=='MEASURED' and len(x['measured_on'])>=3]; inf=[x for x in f if 'INFERRED' in (x['unit_status'],x['sign_status'])]; print('fields', len(f), 'measured-on-3', len(three), 'inferred', len(inf), 'securities', sorted(set(s for x in f for s in x['measured_on'])))"</invocation><expect>"measured-on-3" of at least 20, "inferred 0", and exactly three securities listed of which one is "SAP GY Equity" -- the map is MEASURED per field on the control plus a US name and an ADR, with no inferred unit anywhere; fewer than 20 measured on all three is a finding to record per field but leaves this criterion NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-1"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/check_join.py</invocation><expect>a summary line "JOIN: 3 of 3 securities at 10 FY rows; orphan price rows 0" -- the fiscal-year join yields exactly ten rows for ten fiscal years on every security with no price row left unjoined; "14 rows" anywhere, or an orphan count above 0, is the date-string defect and is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-1"><invocation>python -c "import json,glob; ps=sorted(glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_*.json')); n=0; ok=0; [(n:=n+1, ok:=ok+(1 if all(k in fg and fg[k] not in (None,'') for k in ('value','unit','sign','basis','vintage','source')) else 0)) for p in ps for fg in json.load(open(p))['figures']]; print('figures', n, 'carrying value+unit+sign+basis+vintage+source', ok, 'complete', n>0 and n==ok)"</invocation><expect>"complete True" with "figures" above 0 -- every figure in every derived block carries the six fields an analyst defends a number with (C-BLOOMBERG-BASIS: the basis stated beside the number); a copy of each landed model_block.json is written to the deliverables folder under model_block_&lt;security_key&gt;.json for this read</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-1"><invocation>grep -r -c -i -E 'factset|recurring.?eps|normali[sz]ed.?eps|capiq|IQ_' integrations/bloomberg/research/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no file under the module names FactSet, CapIQ or a normalized-EPS reconstruction; the basis is Bloomberg's and is stated, never reverse-engineered</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-1"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json')); print('unique securities requested', len(set(l['securities'])), '| requests', len(l['requests']))"</invocation><expect>"unique securities requested 3" (or fewer, never more) -- NEGATIVE: the cost axis is unique securities touched (F2) and this order is capped at three covered names; a fourth is a widening and is NOT met</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-s-1" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, the pre-check): the terminal is up NOW, by a real request. The one criterion this worker may not rescue.
- **AC2** (mechanical, read from S3): raw landed before derived, a stamp per write, nothing overwritten. C-RAW-BEFORE-DERIVED and C-STAGE-PERSISTS, read from the artifact.
- **AC3** (mechanical, a census): the map is measured on three securities with no inferred unit. F4 re-measured beyond one security -- the thing PRD s.6 says nobody has done.
- **AC4** (mechanical): ten fiscal years, ten rows, zero orphans. The 40% drop (F5) cannot pass this.
- **AC5** (mechanical): every figure carries its basis, unit, sign, vintage and source. What FWD-3 will lean on.
- **AC6** (mechanical, NEGATIVE): no lookalike EPS. Andrew's ruling as a grep.
- **AC7** (mechanical, NEGATIVE): three securities, not more. The quota axis, bounded at the cut.
- **AC8** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): pick one figure from the ADR's block -- could an analyst, challenged "where is that from, on what basis, as of when", answer from the record alone? And where a unit DIFFERED between SAP and the US name or the ADR, is that difference in the map as a per-security fact rather than smoothed into one convention?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- one security per call, three securities, no sweep.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q1, the root of `AMGT-s-1 -> AMGT-s-3 -> AMGT-s-5`; slot ~1 drains that queue. AMGT-s-2 (Q2) and AMGT-s-9 (Q3's tail) also depend on this cell.
**SPAWN SEQUENCING (not an edge; the spec is frozen):** this slot spawns AFTER AMGT-s-6 lands and AFTER a fresh `bloomberg_health` reads ok:true at spawn time. The manifest draws no S1 -> S6 edge; C-RAW-BEFORE-DERIVED makes the landing depend on the store, and the decomposition's row AMGT_RESAPP-Z-S1 records it. The terminal read ok:false for ~50 minutes this afternoon (0.0.3_BG_BBGTerminal msg 21049) and "up" is perishable.
**Provenance:** the cell text is the decomposition's row verbatim. The three-securities cap is this issuer's application of F2's cost axis to a first pull; the US-name-plus-ADR choice is PRD s.6's own naming of where F4's conventions are likeliest to differ. The seam exclusion is the decomposition's s.1b finding: the estate has no browser-to-box precedent and this cell does not need one.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, C1=23 C2=6 C3=12 C4=20 C5=335, 25 gates armed, none this project's; G-19 and G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 167 Lambda / 21 EC2 / 1084 operations / 304 gaps; the box principal's write to the new bucket is unmeasured and a refusal is a BLOCKING row by the face
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors, DESIRED plane, no desktop origin; the seam is AMGT-s-2's, not this cell's
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; opal-data-research absent, created by AMGT-s-6 this round
bloomberg_health: RUN -- ok:false at ~18:5xZ and ~19:3xZ; ok:true at ~19:48Z after 0.0.3_BG_BBGTerminal's sign-in (one attempt spent); re-read at spawn
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a box-side script and S3 objects under a new bucket; no existing resource is changed. comp-pipescript DECLARED-NOT-APPLICABLE: not a medallion-tree gold script (the store is opal-data-research, outside data/*/scripts/).
