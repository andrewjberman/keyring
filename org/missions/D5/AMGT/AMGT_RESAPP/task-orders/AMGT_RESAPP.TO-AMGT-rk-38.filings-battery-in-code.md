# AMGT_RESAPP task order -- `AMGT-rk-38` -- the filings battery in code: the ratified order, one acceptance test per step, UNRESOLVED-SOURCE carrying every attempt

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-38</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~40</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the scheduled
  batch task `OpalResearch-FilingsAnalyzer` is neither read nor written here (it is AMGT-rk-42's) and stays DISABLED.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to the already-provisioned pool prefix
  `filings/v1/` in `opal-data-harvest` through the existing `crosswalk.write_pool` path under the credentials this
  project already writes with; it grants no permission, provisions no resource and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~40`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and every path in
section 3 exists; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~40;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-38` (R14-F1; FWD-18; Thesis rows T1, T8, T10, T15)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a):** *"the battery in code: US order EDGAR ->
Bloomberg-resolved CIK -> IR page; each step's acceptance test (right ENTITY, current, known document FAMILY);
UNRESOLVED-SOURCE carrying every attempt; the family recorded. Includes tier 1 (Bloomberg `CENTRAL_INDEX_KEY_NUMBER`
as a CIK fallback, +6 names)"* -- serves FWD-18, T1, T8, T10, T15; co-sign: pool writes.

**RATIFIED SINCE THAT ROW -- the INTERNATIONAL order is Andrew's (PRD v0.13 @1699960261, `C-FILINGS-ANALYZER`
`:663-699`; Andrew-direct ~19:4xZ *"Yes."*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`).** So this
order builds the FULL ordered battery, not only the US steps:

| step | route | key it searches with | US order | international order |
|---|---|---|---|---|
| 1 | EDGAR by TICKER -- the LIVE SEC ticker table (`https://www.sec.gov/files/company_tickers.json`, its row count printed) with the name guard applied to EVERY listing, US included; then the LIVE submissions index for the CIK found | ticker root | 1 | 1 |
| 2 | EDGAR by the Bloomberg-resolved CIK (`CENTRAL_INDEX_KEY_NUMBER`) -- tier 1, the +6 names | Bloomberg CIK | 2 | 2 |
| 3 | ESEF / UKSEF repository by LEI (`https://filings.xbrl.org/api/entities/<LEI>/filings`; HTTP 404 = not held) | Bloomberg LEI | -- | 3 |
| 4 | the company's own site: a BOUNDED crawl from the entity-tied seeds (section 1.2), the issuer's IR page surfacing the document | legal name; web address as a HINT only | 3 | 4 |
| 5 | the national regulator, ONE adapter per jurisdiction, built only for a name that step 4 fails -- NO adapter is built by this order; the step is declared and records `no adapter for jurisdiction <cc>` | jurisdiction id | -- | 5 |
| terminal | UNRESOLVED-SOURCE, persisted with EVERY step's attempt, the key it used and its failure reason | -- | yes | yes |

**ONE acceptance test, every step (PRD `:674-681`), the first document passing it WINS:**
- **(a) RIGHT ENTITY** -- the document names the listed issuer, checked against Bloomberg's legal name and the LEI where
  the document carries one; otherwise the legal name plus a national registry identifier. A subsidiary's report on the
  parent's domain FAILS (measured: Roche Holdings Inc, RWE Finance Europe BV, Zurich Life -- PRD `:1668-1669`).
  Mechanism you build: the FULL legal name (normalised: casefold, punctuation and whitespace collapsed, legal-form
  aliases Inc/Incorporated, Ltd/Limited, Corp/Corporation, Co/Company, plc, AG, NV, SA, KK) must occur as a substring of
  the document's cover region (first three pages of a PDF; the SEC entity name for steps 1-2), AND a 20-character LEI in
  the document must equal Bloomberg's, AND a contradicting legal form or an extra subsidiary token in the cover's issuer
  line (`Holdings, Inc.` against `Holding AG`; `Finance`, `Europe B.V.`, `Life`) FAILS. Record `entity_evidence`: what
  matched, where, and what was compared.
- **(b) CURRENT** -- an annual report for a fiscal year ended within the last 18 months of the run date. EDGAR gives
  `reportDate` in the submissions index; a PDF's period end comes from `document.period_end(text, family)` (AMGT-rk-39).
- **(c) KNOWN FAMILY** -- a document family the section cutter and the roster can parse: `document.detect_family()` and
  `document.cut()` (AMGT-rk-39) return a family in its declared set with at least one named item cut OK; a family the
  cutter does not know FAILS (c) with the reason and NEVER passes as a section (D9). Language is RECORDED
  (`document.detect_language()`), never tested.
- A failing document is recorded with its reason and the NEXT step runs. The source object carries the winning step, the
  key it used, the family, the language, the entity evidence and the whole attempt log.

**1.1 The measured current state (every line read at HEAD; `lib/research/filings/` last moved @db6c40083f).**
- Only battery step 1 exists in code, and it reads a stale subset: `lib/research/identity/build_universe.py:503-508`
  looks the ticker up in a 33-ticker cache in a WORKER folder (`SEC_CACHE_DEFAULT` `:450-453`) and reports a miss as
  absence from the 10,422-row table; the name guard at `:510` fires only for non-US listings. **That step-1 fix in
  `build_universe.py` belongs to the analysis's cell R14-I2 (chain I), NOT to this order -- this order writes its OWN
  live step 1 inside the battery and does not touch `build_universe.py`.**
- `lib/research/filings/fetch.py:377-448` `build_source_object(security_key, cik, form_expected)` is EDGAR-only: no cik
  -> UNRESOLVED-SOURCE (`:382-387`); the form patterns are 10-K and 20-F only (`:103-152`); a document from any other
  route has no path in. `unresolved_source_object()` (`:359-374`) carries ONE reason string and no attempt log.
  `latest_filing()` (`:177-215`) reads the submissions index by CIK and returns `entity_name`; it does not return
  `reportDate`, `website` or `investorWebsite`, which the same JSON carries.
- `pool_key()` (`:451-452`) keys a RESOLVED object by EDGAR accession; a company-site document has none.
- Bloomberg supplies keys, never text: the validation's one `ReferenceDataRequest` returned `NAME`, `LONG_COMP_NAME`,
  `LEGAL_ENTITY_IDENTIFIER`, `CENTRAL_INDEX_KEY_NUMBER` (`0000018230` for CAT), `COMPANY_WEB_ADDRESS`, `CNTRY_OF_DOMICILE`,
  `EXCH_CODE` through `integrations/bloomberg/mcp/blp_client.py::reference_data(securities, fields, overrides=None,
  timeout_s=30.0)` (`:135-145`; a security-level error is `{"__error__": msg}`, a field-level error is OMITTED from the
  dict -- a missing key is measured by its absence, never assumed). `health()` (`:125-132`) is the cheap first read.
- The pool crosswalk record (`lib/research/identity/crosswalk.py:257-336`) carries `security_key`, `bloomberg`,
  `display_ticker`, `model_key`, `exchange`, `association_keys` -- and NO cik, LEI or legal name today; those land with
  `C-INSTANTIATION-ENTRY` (the analysis's cell R14-I1, chain I). So the battery takes its keys as an injected `keys`
  record and `keys_from_crosswalk()` returns what the record carries today with each absent key NAMED.
- The three-name validation (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/INSTANTIATION_VALIDATION_REPORT_20260918.md`
  @b527b93214 s.3) measured the whole battery by hand: CAT wins at step 1 on the LIVE table (10,438 rows; SEC ID 18230;
  10-K filed 2026-02-13 for the year to 2025-12-31); CSL: step 1 `CSL` is Carlisle Companies (SEC ID 790051) and the name
  guard refuses it, step 2 Bloomberg CIK 0001274152 is "CSL LTD" with 11 ADR/registration filings and no annual report
  (FAILS (b)), step 3 LEI `529900ECSECK5ZDQTE14` 404, step 4 wins on `investors.csl.com` (year to 2026-06-30; the
  Bloomberg hint `www.csl.com.au` is NOT the host); Keyence: step 1 `6861` misses, step 2 the CIK field is not applicable
  to the security, step 3 LEI `529900M7PQBS7A89DZ11` 404, step 4 wins on `www.keyence.co.jp` (the FY57 Yuho, Japanese,
  regulator code E01967, year 2025-03-21 to 2026-03-20). Step 5 for Keyence is EDINET, which needs a subscription key:
  NOT-RUN, recorded.

**1.2 What you build.**
1. NEW `lib/research/filings/battery.py`: `run_battery(security_key, keys, run_date=None, http_get=fetch.http_get,
   search_fn=None, cache_dir=None, document_layer=None) -> source_object`, with one function per step, `acceptance(doc,
   keys, run_date) -> {entity, current, family, language, passed, reason}`, `keys_from_crosswalk(security_key)`,
   `keys_from_bloomberg(bloomberg_securities)` (ONE `reference_data` call for the fields named in 1.1), and a CLI:
   `python -m lib.research.filings.battery --security-key K --bloomberg "ROOT EX Equity" --exchange EX [--keys-json
   PATH] [--legal-name-override NAME] [--no-site-crawl] [--cache-dir DIR] [--out-dir DIR] [--write-pool]`.
   `--keys-json` supplies the keys record from a file (the planted controls); otherwise `keys_from_bloomberg`.
   `--cache-dir` persists every step's attempt as it completes (`<cache>/battery/<security_key>/step<n>.json`, plus any
   downloaded document by sha256) so a run killed by a criterion's `timeout 120` RESUMES at the next step on re-invocation
   -- the same remedy the pass-1 cache took (`analyze.py:308-317`). The FINAL invocation is the one a criterion records.
2. **Step 4's seeds are ENTITY-TIED, never a hand list:** the Bloomberg `COMPANY_WEB_ADDRESS` hint, and the `website` /
   `investorWebsite` fields of any EDGAR submissions record a prior step resolved for THIS entity (even when that step
   failed (b) or (c): CSL's ADR-paperwork CIK still names CSL's own site). The crawl is BOUNDED and printed: at most 40
   pages, depth 3, 2 s between requests, hosts limited to the seed hosts, their registrable domain and hosts linked from
   a fetched page whose name contains the registrable-domain label or `investor`/`ir`; candidate documents are links
   whose href or anchor text matches an annual-report vocabulary (`annual report`, `annual securities report`,
   `statutory`, `10-K`, `20-F`, `integrated report`, and the Yuho title `\u6709\u4FA1\u8A3C\u5238\u5831\u544A\u66F8`
   written as an escape, never as glyphs); each candidate is downloaded (cap 25 MB), hashed and put through the
   acceptance test, and EVERY candidate's result is recorded on the attempt. `search_fn` is a SEAM and is NOT wired: no
   web-search primitive is authorized for this cell (the estate's SERP primitive is E6's, and E14 measured it returning
   an empty list on failure); when the crawl yields no candidate the attempt records
   `search: NOT-ATTEMPTED (no authorized search primitive)`.
3. `fetch.py`: `build_source_object` gains the battery path -- a RESOLVED object now carries `battery: {order: [...],
   attempts: [{step, route, key, url, http_status, document_sha256, tests: {entity, current, family}, language, reason,
   seconds}], winner: {step, route, key}}`, `family`, `language`, `entity_evidence`, and **`verified_site`** (section
   1.3); `unresolved_source_object(security_key, reason, filing_identity=None, battery=None)` carries the same `battery`
   block; `latest_filing()` also returns `report_date`, `website`, `investor_website`; `pool_key()` accepts a document id
   `doc-<sha256[:16]>` for a non-EDGAR winner; `PARSER_VERSION` -> `opal-filings-fetch/2.0.0` (the object contract
   moved). The EDGAR-by-CIK path (`--cik --form`) keeps working unchanged for callers that already resolved a CIK.
4. Tests in `lib/research/filings/tests/test_battery.py`: stubbed `http_get` and stubbed document layer; the planted
   negatives named in section 5.

**1.3 The field cell AMGT-rk-49 (R14-E7, Lusha) reads -- state it exactly, because that cell is gated on this one.**
Every source object this battery writes carries `verified_site`: either
`{"host": "<hostname>", "url_root": "https://<hostname>/", "step": <n>, "source": "winning-document-host" |
"edgar-submissions.investorWebsite" | "edgar-submissions.website", "evidence": "<the acceptance-test (a) result the host
is tied to>"}` or `null` beside `verified_site_reason` (for example *"step 1 wins on EDGAR and the submissions record
carries no website field"*). The host is ENTITY-TESTED: it is the host the winning document was fetched from (steps 3-5)
or the site EDGAR's own record names for the winning CIK (steps 1-2). Bloomberg's web address NEVER populates it
directly. AMGT-rk-49 reads `source_object["verified_site"]["host"]` and, when it is null, records NOT ATTEMPTED with
`verified_site_reason` -- so this field is the contract, and a value that is not entity-tested must not appear in it.

**1.4 The validation bar (`C-VALIDATION-NAMES`, PRD `:1652-1658`).** This cell is proven on CAT (`CAT US Equity`,
US 10-K), CSL (`CSL AU Equity`, company site only) and Keyence (`6861 JP Equity`, Japanese) -- and on planted controls.
NO fleet run, NO run over the covered 33, NO re-run (Andrew, verbatim: *"I dont care about rerunning until the process
is completely validated end to end"*). The ONE Bloomberg reference call for the three validation names is within the bar
(analysis s.4; the validation's own precedent). The +6 tier-1 names are BUILT for (step 2) and proven on CAT and on a
planted control -- they are NOT run.

**1.5 Sequencing.** Test (c), the family cut, the language detector and the PDF period end are AMGT-rk-39's document
layer (`lib/research/filings/document.py`). The COO sequences AMGT-rk-39 before this order on `fetch.py`. If you find
`document.py` absent in your worktree, STOP and file a BLOCKING row: without it CSL and Keyence can only fail (c), and
this order's criteria on them would be REFUSED, not passed.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 row R14-F1 @9c8e04cd9a, s.2 (the pattern), s.5 card 1
(international battery order -- ANSWERED YES, ratified PRD v0.12, carried v0.13 @1699960261). PRD v0.13 @1699960261:
`C-FILINGS-ANALYZER` `:663-699` (the battery, the acceptance test, live step 1, no fleet run), `C-FILINGS-TRANSLATION`
`:703-720` (language recorded, not tested), `C-PRODUCTION-HOME` `:1643-1650`, `C-VALIDATION-NAMES` `:1652-1658`,
section-10 evidence list `:1663-1671`. The COO's round-14 decomposition record for this cell in `AMGT_RESAPP_DECOMP.md`
is the postulate paragraph landed beside this order.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/battery.py
lib/research/filings/fetch.py
lib/research/filings/__init__.py
lib/research/filings/tests/test_battery.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~40/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-38.filings-battery-in-code.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read `lib/research/filings/document.py`,
  `lib/research/identity/crosswalk.py`, `integrations/bloomberg/mcp/blp_client.py` and the pool); this block governs
  WRITES. `build_universe.py` is chain I's (R14-I2); `document.py` is AMGT-rk-39's; `batch.py` and `analyze.py` are
  AMGT-rk-42's and AMGT-rk-40's -- you edit none of them. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~40 <0.9.0_WK_AMGT_RESAPP~40@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **THE POOL WRITE:** `filings/v1/<security_key>/<accession-or-doc-id>.source.json` and
  `filings/v1/<security_key>/UNRESOLVED-SOURCE.source.json` for the THREE validation keys only, through
  `crosswalk.write_pool` (`crosswalk.py:609-657`, put + read-back). No other prefix. The served plane keys on the pool
  crosswalk, which carries none of the three names, so no served output moves.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only; this order needs none. **EGRESS, EXACTLY:** EDGAR
(`data.sec.gov`, `www.sec.gov`), `filings.xbrl.org`, the three validation issuers' own domains reached by the bounded
crawl, and ONE Bloomberg `ReferenceDataRequest` for the three validation securities. **Nothing else, no search engine,
no other vendor.** If `blp_client.health()` reads `ok: false`, the terminal is signed out: STOP the Bloomberg criterion
and file a row -- the sign-in is a budgeted human act (`integrations/bloomberg/READ_HERE.md` s.2), never yours.
**No non-ASCII in anything you write** -- a Japanese title in code is a `\u` escape (`len(b) - len(b.decode('utf-8'))
== 0` on every file you touch). **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- a hand-typed document URL is such a route.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** (the SEC table's row count; the crawl's
page count; the attempt count).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W40-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/filings/tests -p "test_*.py" -q 2>&1 | tail -5</invocation><expect>the last lines read "Ran N tests" and "OK" with N at least the pre-existing count plus the new battery tests, which include: (1) a stubbed run whose every step fails terminates UNRESOLVED-SOURCE with exactly one attempt per declared step, each carrying step, route, key and reason; (2) PLANTED (a): a cover reading "Roche Holdings, Inc." against legal name "Roche Holding AG" FAILS entity, and "Caterpillar Inc." against "Caterpillar Inc" PASSES; (3) PLANTED (b): a period end 20 months before the run date FAILS current; (4) PLANTED (c): a document whose family is UNKNOWN fails family with the reason and is never cut as a section; (5) a keys record with no CIK, LEI or web address records step 2, 3 and 4 as "no key" attempts, never a silent skip; (6) the first passing document wins and later steps are NOT run (attempt count equals the winning step number)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.battery --security-key CAT_US_Equity --bloomberg "CAT US Equity" --exchange US --cache-dir .scratch/battery --out-dir .scratch/battery/out --write-pool 2>&1 | tail -12</invocation><expect>the FINAL invocation (the run resumes from .scratch/battery across invocations if an earlier one hit the 120 s bound) prints STEP 1 with the LIVE SEC ticker table's row count (the validation read 10,438), entity CATERPILLAR INC, CIK 18230, a 10-K with its filing_date and report_date, tests entity PASS / current PASS / family PASS (family 10-K, language en), WINNER step 1, attempts 1, verified_site printed as a host with source edgar-submissions.investorWebsite or edgar-submissions.website, or as null WITH verified_site_reason -- and the pool receipt "OK: uploaded s3://opal-data-harvest/filings/v1/CAT_US_Equity/<accession>.source.json" with its read-back sha256 and ContentLength</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.battery --security-key CSL_AU_Equity --bloomberg "CSL AU Equity" --exchange AU --cache-dir .scratch/battery --out-dir .scratch/battery/out --write-pool 2>&1 | tail -16</invocation><expect>the FINAL invocation prints the international order with one recorded attempt per step reached: step 1 the live table hit "CSL" = Carlisle Companies REFUSED by the name guard (entity FAIL, the reason naming both names); step 2 Bloomberg CIK 0001274152 entity "CSL LTD" with no annual form in its recent window (current/family FAIL with the forms seen counted); step 3 LEI 529900ECSECK5ZDQTE14 http 404 "not held"; step 4 the bounded crawl printing pages visited (at most 40), candidates found, and the winning PDF on host investors.csl.com with entity PASS (legal name matched on the cover; the LEI absent from the document recorded as such), current PASS (year to 2026-06-30), family PASS (ANNUAL-REPORT via document.py), language en; WINNER step 4; verified_site host investors.csl.com, source winning-document-host; the pool receipt for filings/v1/CSL_AU_Equity/doc-<sha16>.source.json. If the crawl cannot reach the document, the object reads UNRESOLVED-SOURCE with all four attempts and this criterion is REFUSED with the crawl log -- never passed on a typed URL</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.battery --security-key 6861_JP_Equity --bloomberg "6861 JP Equity" --exchange JP --cache-dir .scratch/battery --out-dir .scratch/battery/out --write-pool 2>&1 | tail -16</invocation><expect>the FINAL invocation prints step 1 miss against the live table with its row count; step 2 "no key" (Bloomberg's CIK field not applicable to this security, the field's absence from the reference reply recorded, never guessed); step 3 LEI 529900M7PQBS7A89DZ11 http 404; step 4 the crawl reaching the FY57 Yuho PDF on www.keyence.co.jp with entity PASS (the cover's English name matched; regulator code E01967 recorded), current PASS (2025-03-21 to 2026-03-20), family PASS (YUHO), language ja, translation_required true; WINNER step 4; step 5 NOT reached; verified_site host www.keyence.co.jp; the pool receipt. If the crawl cannot reach the document the criterion is REFUSED with the crawl log, exactly as AC3</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, os
os.makedirs('.scratch/battery', exist_ok=True)
json.dump({'legal_name': 'Hollow Nonexistent Corp', 'ticker_root': 'HOLLOWQZX', 'exchange': 'US', 'cik': None, 'lei': None, 'web_address': None, 'domicile': 'US'}, open('.scratch/battery/hollow.keys.json', 'w'))
" && python -m lib.research.filings.battery --security-key HOLLOWQZX_US_Equity --keys-json .scratch/battery/hollow.keys.json --exchange US --no-site-crawl --out-dir .scratch/battery/out 2>&1 | tail -10</invocation><expect>the PLANTED terminal negative: step 1 misses against the live table (row count printed); steps 2, 3 and 4 record "no key" / "no seed" attempts; step 5 records "no adapter for jurisdiction US"; the object reads UNRESOLVED-SOURCE with battery.attempts length 5, every attempt carrying a reason; written to .scratch only -- the line "NOT-UPLOADED (no --write-pool)" is printed and no pool key is touched</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.battery --security-key CAT_US_Equity --bloomberg "CAT US Equity" --exchange US --legal-name-override "Roche Holdings, Inc." --no-site-crawl --cache-dir .scratch/battery_wrong_entity --out-dir .scratch/battery_wrong_entity/out 2>&1 | tail -10</invocation><expect>the PLANTED wrong-entity control on the LIVE path: steps 1 and 2 both find CATERPILLAR INC's 10-K and BOTH record entity FAIL (the reason naming "CATERPILLAR INC" against "Roche Holdings, Inc."); the 10-K is NOT served; the object reads UNRESOLVED-SOURCE with the (a) failures recorded on every attempt that found a document; nothing is written to the pool (no --write-pool). Compared with AC2, the ONLY input that differs is the legal name, and the outcome flips -- the entity test discriminates</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-38"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
keys = ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']
served = 0
for k in keys:
    listing = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='filings/v1/%s/' % k)
    objs = [o['Key'] for o in listing.get('Contents', []) if o['Key'].endswith('.source.json')]
    for key in objs:
        doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=key)['Body'].read())
        b = doc.get('battery') or {}
        print(key, doc.get('status'), 'winner', (b.get('winner') or {}).get('step'), 'attempts', len(b.get('attempts') or []), 'family', doc.get('family'), 'language', doc.get('language'), 'verified_site', (doc.get('verified_site') or {}).get('host'), 'reason', doc.get('verified_site_reason'), 'parser', doc.get('parser_version'))
        served += 1
print('objects read', served, 'of', len(keys), 'validation keys')
"</invocation><expect>3 of 3 validation keys carry a source object written by THIS battery (parser_version opal-filings-fetch/2.0.0): each prints its status, winning step, attempt count, family, language and either a verified_site host or a verified_site_reason -- the exact read cell AMGT-rk-49 performs. A key whose object is absent or still carries parser_version 1.0.0 fails this criterion</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC2-AC4 may need more than one invocation under the 120 s bound; record EVERY invocation and mark the final one.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~40/AMGT_RESAPP.TO-AMGT-rk-38.filings-battery-in-code.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~40</slot>
<fabric>site-z</fabric>
