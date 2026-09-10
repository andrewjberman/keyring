# AMGT_RESAPP.TO-AMGT-s-12 -- THE IDENTITY LAYER: four keys per security, each RESOLVED or SAYING SO, and F6 re-measured on the corpus

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~3</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-13; manifest row S12; THE ROOT four surfaces hang off)

```
AMGT-s-12. THE IDENTITY LAYER -- THE ROOT. Bloomberg ticker, SA symbol, IR domain, social account:
four keys, the social one with no shared identifier. Two sources are never shown together until
resolved; where they cannot be, the page SAYS SO. F6 re-measured as the failure instance. Resolves
the SA-symbol KEY and binds nothing about the SA fetch path.

FWD-13's bar, verbatim: "Everything on one page is about the same company. DONE WHEN EXERCISED --
checked on a name that more than one business uses, and found not mixed."

WHY THIS CELL IS ROUND 1 AND WHY IT IS THE ROOT: the coverage reader (S4), the peer set (S8), the
social feed (S13) and the list register (S15) all hang off it, and it is the direct remedy for the
ONLY defect this project has measured in production -- 48 of 54 existing one-pagers carrying another
company's peer set (F6). Cutting any of those four before this lands rebuilds F6 on a new axis.

WHAT TO PRODUCE, all under
    org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/
and the module under
    lib/research/identity/

  (a) THE RESOLVER MODULE  lib/research/identity/resolver.py
      resolve(bloomberg_ticker: str) -> a record with EXACTLY these four keys:
          bloomberg_ticker, sa_symbol, ir_domain, social_account
      each key a cell {value, status, evidence, resolved_at} where status is ONE of the closed set
          MEASURED | INFERRED | UNRESOLVED
      (MEASURED = read from an artifact you name in `evidence`; INFERRED = derived by a stated rule and
      never presented as measured; UNRESOLVED = you do not know, and the page must SAY SO.)
      and a function render_together(record, sources: list) that REFUSES (raises) whenever any source
      named depends on a key whose status is UNRESOLVED. That refusal is C-IDENTITY-RESOLVED made
      mechanical: two sources are never shown side by side until their identity is confirmed.

  (b) THE COVERAGE UNIVERSE  .../deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json
      Enumerate the research corpus that syncs to this device (READ-ONLY, outside the repo):
          C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research\
      One entry per name folder. For each: the folder name, and the Bloomberg-format ticker of the
      SUBJECT company read from that folder's *ONE PAGER*.xlsx workbook (openpyxl, data_only=True) --
      status MEASURED with the workbook path and sheet/cell as evidence, or UNRESOLVED when the
      workbook is absent or carries none. Record `denominator_folders` (how many folders you found)
      and a partition of statuses that sums to it. Do NOT assume 89: the brief measured 89 on
      2026-09-10; you measure yours and print it.

  (c) THE SA-SYMBOL KEY -- INFERRED AT MOST, NEVER MEASURED HERE. PRD v0.3 s.3a measured that the SA
      key is the ticker slug plus a numeric sa_id that ONE vendor call returns. That call is a
      procurement act and this order is NOT a procurement order: AMGT-s-b4 confirms sa_ids for the
      tickers it fetches and writes them back; here you may set sa_symbol to an INFERRED slug by a
      stated rule (state the rule; a US name's slug is its ticker; an ex-US name is INFERRED with
      lower confidence or UNRESOLVED) and the sa_id stays UNRESOLVED. No sa_symbol cell is MEASURED
      by this order and AC5 refuses one that is.

  (d) IR DOMAIN AND SOCIAL ACCOUNT -- UNRESOLVED AT THIS CUT, AND THE RECORD SAYS SO. Resolving them
      needs a SERP zone request and social lookups, each a vendor call this order does not carry the
      word for (G-24). The layer's job now is to KNOW and SAY: both keys UNRESOLVED with evidence
      "no vendor word at this cut". A later order with the word fills them.

  (e) F6 RE-MEASURED  .../deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.json + f6_remeasure.py
      The brief's F6 (CITED, re-derived by nobody): "48 of 54 one-pagers carry a stale telecom peer
      set copied from a KPN workbook". Re-measure it on the corpus with the CRO's own method, stated
      in that seat's deliverable: read every *ONE PAGER*.xlsx workbook's `CSC` sheet, extract
      Bloomberg-format tickers, score overlap against the KPN telecom set (KPN, Vodafone, BT,
      Orange, Telenor, Telekom Austria, Rogers, Telus, Swisscom, AT&T, Verizon, Telefonica). Print
      the denominator (workbooks found), and a partition: carries-the-stale-set / own-set / no-CSC.
      Agreement or disagreement with 48 of 54 is a FINDING you record; it is not a criterion.

  (f) A SELF-TEST  lib/research/identity/self_test.py, runnable as `python -m lib.research.identity.self_test`,
      that asserts: the record has exactly the four keys; the status set is exactly the three values;
      render_together REFUSES on a record with one UNRESOLVED key (the difference arm: the SAME
      record with that key MEASURED is ADMITTED); and prints ONE line
          IDENTITY SELF-TEST: 4 keys, 3 statuses, unresolved-refused=True, resolved-admitted=True: PASS
```

## DEPENDENCIES

**NONE.** No cell of this round precedes it. Four cells wait on it: AMGT-s-4, AMGT-s-8, AMGT-s-13,
AMGT-s-15 (and AMGT-s-b4 consumes its key). Land it and they become cuttable.

## BOUNDS -- what this cell may not cross

```
⛔ G-24 / C-VENDOR-EGRESS: NO VENDOR CALL. No Bright Data zone request (SERP included), no Seeking
Alpha fetch, no social lookup. This order carries no per-use word and may neither spend nor assume
one. AC4 refuses a module that names any such host.

⛔ C-IDENTITY-RESOLVED: two sources are never displayed together until resolved; where they cannot
be, the page SAYS SO. render_together's refusal is that rule and it must be exercised, not reasoned.

⛔ THIS ORDER IS NOT A PROCUREMENT ORDER (Andrew-direct @d09e26e1b1, scope confirmed by
1.0.0_SA_CTO~Z msg 21056): the SA key is resolved as a KEY, at most INFERRED; the fetch path is
AMGT-s-b4's. Do not read the SA auth investigation as authorising a call from this order.

⛔ THE CORPUS IS READ-ONLY. It is Adam's team's SharePoint library synced to this box. Read it; write
nothing into it; copy nothing out of it into the repo except the measurements you derive.

⛔ C-NO-CONTACT: no seat contacts Adam Muller. Nothing here reaches him.

⛔ A VALUE MUST CARRY ITS CLAIM: every key cell carries its status; an INFERRED value is never
rendered as MEASURED, and a consumer may reject on the status field.

⚠ BOUND EVERY READ. Each invocation runs under `timeout 120` and a timeout IS the recorded output.
Reading 54 workbooks with openpyxl fits inside that if you read only the sheets you need; iterate
with a stated cap rather than loading whole workbooks.

⚠ THE CORPUS IS A LIVE SYNC. Its root mtime moved this morning. Record the vintage (the directory
listing's timestamp and your read time) beside every count; a count without its vintage is not a
measurement.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F6 (CITED, the brief @19ce7d5b4d; the CRO's method in
    org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_LAMBDAS_PEERS_IRSCAN_20260910.md s.2):
    "Population: all 54 *ONE PAGER*.xlsx workbooks across the 89 name folders. Method: read each CSC
    sheet, extract Bloomberg-format tickers, score overlap against the peer set found on the SAP
    sheet." 48 stale / 4 own / 2 no-CSC. YOU RE-MEASURE IT (e); the PRD carries it as CITED.

PRD v0.3 s.3a (@f68818832b): "the SA key is the ticker slug plus the numeric id underneath it, and ONE
    call returns both. The map is cheap and should be persisted." -- the call is AMGT-s-b4's; the
    persisted map is fed by that cell; this cell defines the record it fills.

comp-find --corpus aws (vintage 2026-09-10 12:24:50 UTC): the research corpus is NOT in AWS; it is a
    SharePoint sync on this device. No bucket, no Lambda, no secret is touched by this order.

comp-schedule (RUN to completion, --budget 500, 5 of 5 carriers): 25 gates armed, none this
    project's. G-24 (vendor egress) binds this cell and is in BOUNDS. G-14 (never a producer's
    self-report) binds AC6.

Interpreter: `python` on PATH resolves to C:\Users\Opal Bloomberg\AppData\Local\Programs\Python\Python311\python.exe,
    with openpyxl, boto3, jsonschema importable (measured at the cut). Use it; do not install anything.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/identity/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~3/`, inside the granted prefix. The corpus
under OneDrive is READ (not path-gated, not in the repo); the PRD, the decomposition and the CRO's
deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W3-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-12"><invocation>python -m lib.research.identity.self_test</invocation><expect>the single line "IDENTITY SELF-TEST: 4 keys, 3 statuses, unresolved-refused=True, resolved-admitted=True: PASS" -- the four keys exist, the status vocabulary is exactly MEASURED|INFERRED|UNRESOLVED, and render_together REFUSES on an UNRESOLVED key while ADMITTING the same record once that key is MEASURED (the difference arm); any other output, or no output, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-12"><invocation>python -c "import json; u=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json')); s={'MEASURED':0,'INFERRED':0,'UNRESOLVED':0}; [s.__setitem__(n['bloomberg_ticker']['status'], s[n['bloomberg_ticker']['status']]+1) for n in u['names']]; print('universe', len(u['names']), 'of', u['denominator_folders'], 'folders; ticker statuses', s, 'partition', 'OK' if sum(s.values())==len(u['names'])==u['denominator_folders'] else 'BROKEN')"</invocation><expect>a line ending "partition OK" in which the first two numbers are EQUAL (every folder found is an entry) and the three status counts sum to them -- the denominator is printed, never assumed to be 89; "partition BROKEN", a KeyError, or no file is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-12"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.py</invocation><expect>a line of the exact shape "F6 RE-MEASURED: stale-set N / own-set M / no-CSC Z of D workbooks; vintage YYYY-MM-DDTHH:MMZ" where N+M+Z equals D and D is the workbook count the script FOUND -- the CRO's 48 of 54 is quoted beside it in the deliverable as CITED, and agreeing or disagreeing with it is a finding, not this criterion; an unprinted denominator or a partition that does not sum is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-12"><invocation>grep -r -c -i -E 'brightdata|seekingalpha\.com|api\.brightdata|serp_opal|/api/v3/|requests\.get|urllib\.request|httpx' lib/research/identity/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no file under the module names a vendor host, a proxy zone, the SA API path, or an HTTP client at all; this order carries no vendor word (G-24) and the identity layer is a resolver over artifacts you already hold, not a fetcher</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-12"><invocation>python -c "import json; u=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json')); print('sa_symbol MEASURED', sum(1 for n in u['names'] if n['sa_symbol']['status']=='MEASURED'), '| ir_domain MEASURED', sum(1 for n in u['names'] if n['ir_domain']['status']=='MEASURED'), '| social_account MEASURED', sum(1 for n in u['names'] if n['social_account']['status']=='MEASURED'))"</invocation><expect>"sa_symbol MEASURED 0 | ir_domain MEASURED 0 | social_account MEASURED 0" -- NEGATIVE and structural: none of the three vendor-dependent keys is presented as MEASURED by this order; INFERRED (with its rule in evidence) or UNRESOLVED are the only honest statuses here, and a MEASURED one would mean a vendor call was made or a claim was inflated</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-12" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the layer exists with the four keys and the three-valued status, and the one rule that matters -- never together until resolved -- is EXERCISED in both directions.
- **AC2** (mechanical, a census): the universe carries its own denominator and a partition that closes. The number is yours, not the brief's.
- **AC3** (mechanical, a census): F6 is re-measured with the method stated, the denominator printed and the vintage beside it. Whether it still reads 48 of 54 is a finding.
- **AC4** (mechanical, NEGATIVE): no vendor host, no HTTP client. The one bound that decides whether this order stayed inside its word.
- **AC5** (mechanical, NEGATIVE, structural): the three keys this order cannot measure are not presented as measured. A value carries its claim.
- **AC7** -- there is no AC7; **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): does the deliverable SAY, plainly and per key, what it could not resolve and why -- and would a reader re-running `f6_remeasure.py` against the same corpus at the same vintage get the same partition? A layer that hides its UNRESOLVED keys behind a confident-looking map has not moved FWD-13.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- read only the sheets you need.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q3, the root of `AMGT-s-12 -> AMGT-s-4 -> AMGT-s-9`; slot ~3 drains that queue.
**Provenance:** the cell text is the decomposition's row verbatim. The vendor-call bound (d) is this issuer's application of G-24 to a root cell that would otherwise have reached for SERP: the layer is cut to KNOW AND SAY rather than to resolve by a call it has no word for, which is C-IDENTITY-RESOLVED's own shape. The SA-key limb (c) is cut to the scope Andrew confirmed (@d09e26e1b1; 1.0.0_SA_CTO~Z msg 21056): this is not a procurement order.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, C1=23 C2=6 C3=12 C4=20 C5=335, 25 gates armed, none this project's; G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 167 Lambda / 21 EC2 / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors, DESIRED plane; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites, 94 keys, 0 type mismatches; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the corpus this cell reads is a SharePoint sync on this device, not in AWS
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: this cell creates a library module and JSON deliverables and changes no deployed resource.
