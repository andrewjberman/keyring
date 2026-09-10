# AMGT_RESAPP.TO-AMGT-s-7 -- THE COVERAGE-FRESHNESS VIEW: every covered name with its last-refreshed date, in one place a person OPENS -- a view, never a monitor

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~7</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-7; manifest row S7; verb: wire)

```
AMGT-s-7. THE COVERAGE-FRESHNESS VIEW -- every covered name with its last-refreshed date, in one place
a person OPENS. A view, never a monitor, alarm or scheduled checker.

FWD-7's bar, verbatim: "Adam can see which covered companies have gone stale. DONE WHEN EXERCISED --
Adam has used it to find a stale name. ACCEPT: Adam looks in one place, sees every company the team
covers with the date its research was last refreshed, and finds one that has gone stale without
opening any folders."

WHAT "WIRE" MEANS AT THIS CUT: no page until the design spec is approved (C-DESIGN-SPEC-FIRST). This
cell delivers the DATA FACE the page renders and the generator a person runs; the .tsx is a later order.

WHAT TO PRODUCE, under lib/research/freshness/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~7/:

  (a) THE GENERATOR  lib/research/freshness/build_view.py -- reads AMGT-s-12's universe.json (every
      covered name and its security_key) and the store's prefixes (packs/<key>/, raw/<vendor>/<key>/
      per AMGT-s-6's STORE_CONTRACT.md: the LATEST stamp under each prefix), and writes
      coverage_freshness.json: [{name, security_key, last_refreshed: <stamp>|NEVER, per_input:
      {bloomberg: <stamp>|NEVER, seekingalpha: <stamp>|NEVER, ...}, rot: <from AMGT-s-15's
      rot_signal.json if present, else "no rot signal at this vintage">, generated_at}]. NEVER is a
      VALUE, never a blank, never an omitted name: every universe entry appears.

  (b) IDEMPOTENT AND ON-DEMAND: running it twice with no store change produces identical output except
      generated_at. It is invoked by a person (or by the page's build); it schedules nothing.

  (c) SPEC_SECTION_freshness.md for AMGT-s-5: the one place on the page, sorted stale-first, NEVER
      rendered as its own state, the rot signal beside the list.
```

## DEPENDENCIES

`AMGT-s-6` (the store whose prefixes it reads). Same slot (~7), second in `AMGT-s-6 -> AMGT-s-7 ->
AMGT-s-14`; continue on the same context. Reads `AMGT-s-12`'s universe.json and, if landed,
`AMGT-s-15`'s rot_signal.json; their absence is recorded, never invented.

## BOUNDS -- what this cell may not cross

```
⛔ G-20: a VIEW a person opens. No schedule, no alarm, no SNS, no SES, no EventBridge rule, no "checker"
that runs on its own. AC4.
⛔ G-24: no vendor call; the view reads the store and sibling deliverables. AC5.
⛔ C-MARK-NOT-DEGRADE: NEVER is rendered as NEVER; a name with no research is on the list, not off it.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`; listing a bucket's prefixes for ~90 keys fits with
paginated list calls; state the page size.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
AMGT-s-6's STORE_CONTRACT.md (landed): raw/<vendor>/<key>/<stamp>/, derived/<engine>/<key>/<stamp>/,
    packs/<key>/<stamp>/; the latest stamp under a prefix is the read.
AMGT-s-12's universe.json (landed): the denominator of names, printed.
AMGT-s-15's rot_signal.json (if landed): "somebody is told" under G-20 is THIS view rendering it.
comp-schedule (RUN): 25 gates armed, none this project's; G-20 binds this cell absolutely.
KeyCount is absent when the CLI auto-paginates -- count client-side over the listed keys.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/freshness/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-7.coverage-freshness-view-one-place.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~7/`. The store and sibling deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W7-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-7"><invocation>python -c "import json; u=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json')); v=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/coverage_freshness.json')); print('universe', len(u['names']), '| view rows', len(v['rows']), '| NEVER', sum(1 for r in v['rows'] if r['last_refreshed']=='NEVER'), '| refreshed', sum(1 for r in v['rows'] if r['last_refreshed']!='NEVER'), '| blank last_refreshed', sum(1 for r in v['rows'] if not r.get('last_refreshed')))"</invocation><expect>"view rows" EQUAL to "universe", "blank last_refreshed 0", and NEVER plus refreshed equal to the row count -- every covered name is on the view with a value, and a name with no research says NEVER rather than vanishing</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-7"><invocation>python -m lib.research.freshness.build_view --out .scratch/fv1.json &amp;&amp; python -m lib.research.freshness.build_view --out .scratch/fv2.json &amp;&amp; python -c "import json; a=json.load(open('.scratch/fv1.json')); b=json.load(open('.scratch/fv2.json')); a.pop('generated_at',None); b.pop('generated_at',None); print('idempotent', a==b)"</invocation><expect>"idempotent True" -- two runs with no store change agree except for generated_at; a view that differs between runs is reading something it should not (amendment 1: the two scratch paths are worktree-relative under .scratch/, which exists in the worker's tree; an absolute /tmp path is converted by the shell for the argv and left alone inside the Python string on this box, so the writer and the reader named two different directories)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-7"><invocation>python -c "import json; v=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/coverage_freshness.json')); rows=[r for r in v['rows'] if r['last_refreshed']!='NEVER']; print('refreshed rows', len(rows), '| every refreshed row names per_input stamps', all(any(s!='NEVER' for s in r['per_input'].values()) for r in rows), '| rot field present on every row', all('rot' in r for r in v['rows']))"</invocation><expect>"every refreshed row names per_input stamps True | rot field present on every row True" -- a refreshed name says WHICH input refreshed it (FWD-12's clocks differ), and the rot signal from the list register is carried on every row or its absence is stated</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-7"><invocation>grep -r -c -i -E 'aws_cloudwatch|aws_scheduler|schedule_expression|cron\(|rate\(|sns|ses\b|EventBridge|smtplib|while True' lib/research/freshness/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: nothing under the module schedules, loops forever, alarms or sends; it is a view a person builds and opens (G-20)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-7"><invocation>grep -r -c -i -E 'blpapi|brightdata|seekingalpha\.com|requests\.get|urllib\.request|httpx' lib/research/freshness/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no vendor call; the view reads the store</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-7" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, a census): every covered name, with a value. The denominator is the universe's.
- **AC2** (mechanical): idempotent.
- **AC3** (mechanical): per-input clocks and the rot signal ride on every row.
- **AC4**, **AC5** (mechanical, NEGATIVE): not a monitor; not a fetcher.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): sorted as the spec section describes, would Adam find the stalest name in one glance without opening a folder -- and does a NEVER read as "never researched" rather than as an error?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q7, second in `AMGT-s-6 -> AMGT-s-7 -> AMGT-s-14`; slot ~7 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim. The view-not-monitor cut is G-20 applied literally: FWD-7's ACCEPT is "Adam looks in one place", which a generated JSON and a page satisfy and a scheduled checker would violate.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-20 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell reads the store and writes a library
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the store this cell reads is created by AMGT-s-6
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library and a JSON view; no deployed resource changes.

**Amendment 1 (2026-09-10T22:17Z, 2.0.0_SA_COO~ZZZ, before the hand-off):** AC2's two scratch paths moved from `/tmp/fv1.json` / `/tmp/fv2.json` to `.scratch/fv1.json` / `.scratch/fv2.json`. Measured on this box before the amendment: a `/tmp/...` argument handed to native Python by the shell arrives as `C:/Users/<user>/AppData/Local/Temp/...` (path conversion), while `open('/tmp/...')` inside the Python string resolves to `C:\tmp\...` -- the writer and the reader of the same criterion named two different directories, so a correct build could not print "idempotent True". A worktree-relative path is left alone by both. The proposition (two runs agree except generated_at) is unchanged; no other criterion moved. Same class as the surprise-channel rows this fabric has already banked on `/tmp` (site-Z path split).
