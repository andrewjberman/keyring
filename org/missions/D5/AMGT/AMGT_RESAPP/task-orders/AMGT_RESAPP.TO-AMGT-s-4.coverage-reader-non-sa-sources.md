# AMGT_RESAPP.TO-AMGT-s-4 -- THE COVERAGE READER, NON-SA SOURCES: recent commentary ranked by recency and frequency, every item admitted by a stated rule, one unscoped pass per name -- the engine, exercised on what has landed and on fixtures, with the live IR scan named as needing a word this order does not carry

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~3</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-4; manifest row S4, the non-SA half)

```
AMGT-s-4. THE COVERAGE READER, NON-SA SOURCES -- the company's investor-relations channel located by
SERP (the real domain is in `display_link`; `link` is an obfuscated redirect -- F11, re-measured first)
and trusted publications per the allowlist `AMGT-s-15` owns; ranked by recency and frequency; each
item admitted by the news rule `AMGT-s-11` states, PLUS one unscoped pass over the whole population
per name.

FWD-4's bar, verbatim: "An analyst reads what has recently been said about the company without
leaving the page. DONE WHEN EXERCISED -- an analyst has read one and followed it out." The EXERCISED
bar is a person's; this cell builds the reader.

WHAT THIS ORDER CAN AND CANNOT DO, STATED SO NO CRITERION ASKS FOR THE IMPOSSIBLE:
  - It CAN build the reader engine and exercise it on (i) the Seeking Alpha raw JSON AMGT-s-b4 has
    landed under raw/seekingalpha/ by the time you run (that cell is a sibling of this one; read
    whatever exists, and record how many keys you found), and (ii) FIXTURES for the IR-channel and
    publication sources, including the CRO's measured F11 shape.
  - It CANNOT run the live IR scan: a SERP zone request is a Bright Data vendor call and this order
    carries NO per-use word for it (G-24). The scan is BUILT and its fixture exercised; the LIVE run is
    a later order that arrives with the word. AC5 refuses a live call from this order.

WHAT TO PRODUCE, under lib/research/coverage/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~3/:

  (a) THE READER  lib/research/coverage/reader.py -- read(security_key, sources) -> coverage_items.json:
      one entry per item {item_id, source_class: ir|publication|sa, source_domain, title, published_at,
      url, display_domain, admitted: PASS|REFUSE|PROVISIONAL, rule_reason, mentions}, ranked by
      published_at desc then by mentions desc (frequency = how often the item's subject is cited across
      the set). Admission is AMGT-s-11's item rule (lib/research/rules) -- import it; at this cut that
      rule is held_back with no threshold, so its verdict is PROVISIONAL with the reason; the reader
      records that honestly rather than inventing a threshold.

  (b) THE F11 TRAP, MEASURED INTO CODE: a SERP-shaped record's `link` is an obfuscated redirect and its
      `display_link` carries the real domain. The reader stores display_domain from display_link and
      NEVER resolves or stores the redirect as the domain. Fixture: the CRO's own sample shape from
      org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_LAMBDAS_PEERS_IRSCAN_20260910.md s.3.

  (c) THE UNSCOPED PASS (C-SHARED-DEFECT): across every security processed in one run, no two
      securities may carry an IDENTICAL item set (the F6 shape on a new axis). The pass refuses the
      run and names the pair. Fixture: two securities handed the same items -> REFUSE.

  (d) THE IR SCAN, BUILT, NOT RUN: lib/research/coverage/ir_scan.py takes a company name and returns
      the SERP query it WOULD issue and the parser that reads display_link -- exercised on the fixture
      only. Its docstring states: "requires Andrew's per-use word (G-24); not run by AMGT-s-4".

  (e) THE SPEC SECTION  .../deliverables/0.9.0_WK_AMGT_RESAPP~3/SPEC_SECTION_coverage.md for AMGT-s-5.
```

## DEPENDENCIES

`AMGT-s-12` (the identity layer: the reader keys items by the security's resolved identity and refuses
to attach an item whose source identity is UNRESOLVED -- use render_together's rule). `AMGT-s-11` (the
item rule). Same slot (~3) as AMGT-s-12, second in its queue. `AMGT-s-15`'s allowlist and `AMGT-s-b4`'s
SA raw are consumed IF landed; their absence is recorded, never invented.

## BOUNDS -- what this cell may not cross

```
⛔ G-24 / C-VENDOR-EGRESS: NO LIVE SERP, NO Bright Data zone request, NO Seeking Alpha fetch. This order
carries no word. The SA content you read is what AMGT-s-b4 LANDED as raw JSON; you fetch nothing. AC5.
⛔ C-IDENTITY-RESOLVED: an item from a source whose identity key is UNRESOLVED for that security is not
attached to it. The reader says so per item.
⛔ C-RULE-MUST-EXIST / C-CHECK-MUST-REFUSE: the item rule is applied as it stands (held_back, PROVISIONAL);
no threshold is invented here. Admission by keyword match alone is exactly what FWD-4/FWD-11 forbid.
⛔ NO HTML PARSING of Seeking Alpha: the raw JSON is the source (C-SA-NAMED-SOURCE as amended). AC6.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`; the reader runs over local JSON and fixtures.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F11 (CITED): serp_opal returned 10 correct organic results for one name; the link field is an
    obfuscated Google redirect; display_link carries the real domain. An enumerator built on the obvious
    field stores unresolvable URLs and looks like it worked. Fixture (b).
F7 (CITED): the landed SA CORPUS (10,245 objects) is an ARCHIVE, not a feed -- dates stop at 2026-04,
    0 of 200 sampled carry a ticker. Do not read it; read AMGT-s-b4's per-ticker raw JSON.
PRD v0.3 s.3a (@f68818832b): the SA route is symbols/{ticker} -> sa_id -> virtual_analysts/{sa_id};
    analysis|news -> articles/{id}. The raw objects AMGT-s-b4 lands are those bodies.
AMGT-s-11 (landed): the item rule exists with a refusal fixture, threshold None, held_back True,
    produced_by naming this cell among others. Your PROVISIONAL verdicts are the honest state.
comp-schedule (RUN): 25 gates armed, none this project's; G-24 binds this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-4.coverage-reader-non-sa-sources.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~3/`. lib/research/identity, lib/research/rules,
the store's raw/seekingalpha/ prefix and the CRO's deliverable are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W3-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-4"><invocation>python -m pytest lib/research/coverage/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "5 passed" with no "failed" -- (1) ranking by recency then frequency on a fixture with a known order; (2) the F11 trap: a SERP-shaped record stores display_domain from display_link and never the redirect; (3) the unscoped pass REFUSES two securities with identical item sets; (4) the same pass ADMITS two securities with different sets (the difference arm); (5) an item whose source identity is UNRESOLVED is not attached</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-4"><invocation>python -c "import json,glob; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/coverage_items_*.json'); n=0; v={}; [ (n:=n+1, v.__setitem__(i['admitted'], v.get(i['admitted'],0)+1)) for f in fs for i in json.load(open(f))['items']]; print('securities', len(fs), '| items', n, '| verdicts', v, '| sa keys found at run', json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/run_summary.json'))['sa_raw_keys_found'])"</invocation><expect>at least 1 security with at least 1 item, every item carrying a verdict from the closed set PASS|REFUSE|PROVISIONAL, and "sa keys found at run" printed as a number (0 is honest if AMGT-s-b4 had not landed; it is recorded, not hidden) -- the reader runs end to end on what exists</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-4"><invocation>python -c "import json,glob; bad=0; n=0; [ (n:=n+1, bad:=bad+(1 if ('google.com/url' in (i.get('display_domain') or '') or (i.get('display_domain') or '').startswith('http')) else 0)) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/coverage_items_*.json') for i in json.load(open(f))['items']]; print('items', n, 'with a redirect or URL stored as the domain', bad)"</invocation><expect>"with a redirect or URL stored as the domain 0" -- NEGATIVE: F11's trap did not reach the output; every display_domain is a bare domain</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-4"><invocation>python -c "import io; t=io.open('lib/research/coverage/ir_scan.py',encoding='utf-8').read(); print('ir_scan declares the word it lacks', 'per-use word' in t and 'G-24' in t and 'not run by AMGT-s-4' in t)"</invocation><expect>"ir_scan declares the word it lacks True" -- the live scan is BUILT and says on its face that it is not run by this order and why; a scan that runs silently, or one that is absent, is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-4"><invocation>grep -r -c -i -E 'brightdata|serp_opal|api\.brightdata|seekingalpha\.com|requests\.get|urllib\.request|httpx' lib/research/coverage/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no vendor host, no proxy zone, no HTTP client under the module; the reader reads landed JSON and fixtures</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-4"><invocation>grep -r -c -i -E 'BeautifulSoup|lxml|html\.parser|<div|selectolax' lib/research/coverage/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no HTML parsing anywhere on the path (C-SA-NAMED-SOURCE as amended: the API artifact is the source)</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-4" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the reader's four behaviours, each with its refuse and admit arm.
- **AC2** (mechanical): it runs end to end on what exists and says how much existed.
- **AC3** (mechanical, NEGATIVE): F11's trap did not reach the output.
- **AC4** (mechanical): the live scan is built, declares its missing word, and does not run.
- **AC5**, **AC6** (mechanical, NEGATIVE): no vendor call, no HTML parsing.
- **AC7** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): for one security that had SA raw landed, read the ranked list -- is the order one an analyst would recognise as "most recent, most discussed", and is every PROVISIONAL verdict carrying a reason a reader could act on?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q3, second in `AMGT-s-12 -> AMGT-s-4 -> AMGT-s-9`; slot ~3 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim (the non-SA half of S4 after the split on @8c609decf7). The "built, not run" cut of the IR scan is this issuer's application of G-24 to a cell whose live limb needs a word no order carries; a criterion demanding the live scan would be one a correct build cannot satisfy. Andrew's SA scope (@d09e26e1b1; 1.0.0_SA_CTO~Z msg 21056): this cell consumes SA content only to the extent AMGT-s-b4 has landed it.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource beyond reading the store
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the reader reads raw/seekingalpha/ from the store AMGT-s-6 creates
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library and deliverables; no deployed resource changes.
