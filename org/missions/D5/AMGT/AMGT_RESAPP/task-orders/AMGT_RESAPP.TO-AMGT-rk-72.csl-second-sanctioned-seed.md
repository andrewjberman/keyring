# AMGT_RESAPP task order -- `AMGT-rk-72` -- the filings battery gains ONE rule-derived second seed for step 4, the exchange's own listing page (keyed by exchange code + ticker, never by issuer), tried AFTER Bloomberg's COMPANY_WEB_ADDRESS; CSL is re-run on it and ends either RESOLVED on a document that passes the unchanged entity/current/family test, or UNRESOLVED-SOURCE BY DESIGN carrying every attempt

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-72</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~72</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one producer module and its tests and runs it once by
  hand for one validation name; it arms no cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; the one live AWS act (AC5, a
  put + read-back of one object under filings/v1/CSL_AU_Equity/ in opal-data-harvest) runs under the seat's existing
  credentials exactly as AMGT-rk-38's pool write did, and only under the never-widen pair named in section 4.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~72`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~72;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-72` (R18-C; row `AMGT_RESAPP-Z-W40-S1`)

**The ruling, verbatim (`ledger/ROUND_ANALYSIS.round17.md` @4a2f054389 s.3, `:66-74`, `1.0.0_SA_CTO~Z`):**
*"RULED: a second sanctioned seed, falling back to UNRESOLVED-by-design. Not another egress path: routing around a
box-level TCP reset through a vendor is egress. Andrew's Bright Data yes (~16:1xZ) covers the CEO web search on the
three validation names, one time. It does not cover a filings seed, and this seat reads it no wider. The cell tries
seeds the battery already knows how to entity-test, from non-vendor sources: Bloomberg's own company-website field
for CSL, then the exchange's listing page. The first seed that passes the entity test (right entity, current, known
document family) wins. If none passes, the cell records `UNRESOLVED-SOURCE` BY DESIGN, carrying every attempt and
its failure. **A hand-typed URL is never a seed**, which is the clause the `rk-38` worker correctly refused under.
There is no design fork here that needs CRO research. The battery shape is already ratified, and this only adds
attempts to it."* s.4 `:84`: write surface *"the filings battery for CSL only"*; served output *"pool write for one
name (CSL), a validation name, not a fleet run"*.

**The row this cell answers, `AMGT_RESAPP-Z-W40-S1`** (`INVESTIGATION_v1.md:9443`, OBSERVATION, INERT,
UNDER_INVESTIGATION, filed 2026-09-19T06:35:50Z by `0.9.0_WK_AMGT_RESAPP~40`), `one_line` verbatim: *"Bloomberg's own
COMPANY_WEB_ADDRESS for CSL ('www.csl.com.au') resets the TCP connection on every GET this worker tried (default
urllib, a curl-style UA, and fetch.py's SEC User-Agent, all timed out or RemoteDisconnected) while DNS resolves fine
-- the ONE entity-tied seed step 4 has for CSL is unreachable from this box, so AC3 REFUSES rather than reaching
investors.csl.com (the host the validation report itself names as the eventual winner)."* Its evidence also records
EDGAR's `website`/`investorWebsite` both BLANK for CIK 0001274152, and `https://investors.csl.com/` answering 200
(87330 bytes) -- which is NOT a sanctioned seed and MUST NOT become one here (it would be a hand-typed URL).

**THE MEASURED STATE, at HEAD `16ff1b4a0f` (SITEZ; `lib/research/filings/` unchanged since the analysis @4a2f054389
-- `git diff 4a2f054389 HEAD -- lib/research/filings` empty; last change to `battery.py` @abbbdd23ec). RE-READ every
line below at your branch HEAD before editing:**
- `lib/research/filings/battery.py` -- 1256 lines, non-ASCII byte delta 0, crlf 0.
  - `BLOOMBERG_FIELDS` `:75-83` already carries `COMPANY_WEB_ADDRESS` and `EXCH_CODE`; `keys_from_bloomberg` `:462`
    maps them to `keys["web_address"]` and `keys["exchange"]` (`:524-526`, record built `:535-543`, which also
    carries `ticker_root`). **The code already reads the Bloomberg website field**; CSL's value is the one that fails.
  - `_step4_company_site` `:886` (`max_pages=40, max_depth=3, delay=2.0`): seeds = `keys["web_address"]` then
    `prior_seeds` (EDGAR website/investorWebsite from steps 1-2), `:888-893`; no seed -> a named attempt `:900-906`.
    Crawl admission is `_host_allowed(host, seed_hosts, seed_labels)` `:181-196` (seed host, same registrable
    domain, host contains a seed's registrable-domain LABEL, or an `investor`/`ir` host).
  - **A step-4 win sets `verified_site = {"host": winner["host"], ..., "source": "winning-document-host"}`
    `:1044-1047`.** PRD `:736-738` makes that the ONLY source of the company domain Lusha reads (*"The company domain
    comes ONLY from the site the filings battery VERIFIED as the right entity -- never a hand list, never Bloomberg's
    raw web address"*). **An exchange host must therefore NEVER become `verified_site`** -- see RULED item 3.
  - `run_battery` `:1119`: steps 1-5 in order, each outcome cached per step under `--cache-dir`
    (`_load_step_cache` `:1103`; crawl state `_crawl_state_path` `:865`) -- a stale cache short-circuits a step, so
    every live run below uses a FRESH cache directory.
  - CLI `main()` `:1180`: `--keys-json` (`:1185`) overrides `--bloomberg`; `--write-pool` writes
    `fetch.pool_key(security_key, accession)` = `filings/v1/<key>/<accession or UNRESOLVED-SOURCE>.source.json`
    (`fetch.py:61`, `:415-416`) via `crosswalk.write_pool` (`battery.py:1240-1248`).
- **CSL's current battery record (committed evidence, not S3):** `deliverables/0.9.0_WK_AMGT_RESAPP~40/
  AMGT_RESAPP.TO-AMGT-rk-38.filings-battery-in-code.proof_of_spec.json`, criterion AC3, status
  `N/A-BY-CONSTRUCTION`: `UNRESOLVED-SOURCE`, 5 of 5 steps attempted -- step 1 name guard REFUSED ('CSL' = CARLISLE
  COMPANIES INC, 10438 rows searched); step 2 CIK 1274152 = 'CSL LTD', no 10-K (11 filings of 5 distinct forms);
  step 3 LEI 529900ECSECK5ZDQTE14 HTTP 404; step 4 seeds `['https://www.csl.com.au']`, pages_visited 1 of 40,
  candidates 0; step 5 no adapter for AU; `verified_site null`. **Pool receipt in that evidence:
  `s3://opal-data-harvest/filings/v1/CSL_AU_Equity/UNRESOLVED-SOURCE.source.json`, sha256
  `c2be777242734f8003278c5347a69375fc1235be6eda213b02893d947324cc47`, ContentLength 3879.**
- **Test baseline at the cut, measured:** `lib/research/filings/tests/test_battery.py` (295 lines, delta 0, crlf 0)
  `16 passed`; the whole `lib/research/filings/tests` suite `73 passed`, 0 failed.
- **Keys WITHOUT a Bloomberg call, measured:** every key the battery needs for CSL is recorded in that committed
  AC3 evidence. AC3 below derives them by regex into `.scratch/r72/csl_keys.json` -- measured at the cut:
  `legal_name "CSL Ltd"`, `ticker_root "CSL"`, `exchange "AU"`, `cik "1274152"`, `lei "529900ECSECK5ZDQTE14"`,
  `web_address "https://www.csl.com.au"`, `null_fields []`. This is Bloomberg's own recorded reply, re-read, not a
  typed value.

**RULED, what you build:**
1. **`battery.py` -- ONE rule table `EXCHANGE_LISTING_PAGES`**, keyed by the battery's own `keys["exchange"]` code,
   each value a URL TEMPLATE parameterised ONLY by `{ticker_root}`, with exactly ONE entry this round: `"AU"`, the
   ASX's own public company page for a listed ticker. The template is taken from the exchange's own site as you
   measure it (record the GET, its status and byte count in your deliverable); it names NO issuer and is not a
   CSL URL. A helper `_exchange_listing_seed(keys) -> (url or None, reason)` fills it; an exchange absent from the
   table, or a missing `ticker_root`, returns `None` with a NAMED reason.
2. **`_step4_company_site`** appends that seed AFTER `web_address` and `prior_seeds` (the ruling's order: Bloomberg's
   field first, then the listing page), de-duplicated, and records in the step-4 attempt BOTH which seeds were tried
   and, per seed, its source label (`bloomberg-web-address` / `edgar-website` / `exchange-listing-page`). A seed
   that fails to fetch stays in `page_log` with its error, as today. Crawl bounds (`max_pages=40`, `max_depth=3`,
   `delay=2.0`) are UNCHANGED and shared across seeds. The entity/current/family test is UNCHANGED.
3. **`verified_site` never names an exchange.** A step-4 win whose winning document's registrable domain equals an
   `EXCHANGE_LISTING_PAGES` host's registrable domain keeps the document (the win stands) but sets `verified_site`
   to `None` with `verified_site_reason` naming the exchange host (*"winning document hosted by the exchange listing
   page, not the issuer"*). A win on any other host is recorded exactly as today (`winning-document-host`).
4. **Tests, in `lib/research/filings/tests/test_battery.py`** (stubbed `http_get`, offline, per the file's own
   docstring). New arms (names must match AC1's list):
   - `test_exchange_listing_seed_derived_by_rule` -- keys `exchange "AU"`, `ticker_root "CSL"` -> the filled
     template; `exchange "ZZ"` -> `None` with a named reason; no `ticker_root` -> `None` with a named reason.
   - `test_exchange_seed_follows_bloomberg_web_address` -- the seed list is `[web_address, <edgar seeds>,
     <exchange listing>]` in that order, and the attempt records each seed's source label.
   - `test_head_copy_has_no_exchange_seed` -- the DISCRIMINATING arm: load HEAD's `battery.py` bytes via
     `subprocess.run(["git", "show", "HEAD:lib/research/filings/battery.py"])` (merge-base with SITEZ if HEAD has
     moved -- record which) into a temp file, import it under another name, and show that on the same keys and stub
     its step 4 tries ONLY the web_address seed -- proving arm 2 discriminates.
   - `test_unreachable_bloomberg_seed_falls_through_to_listing_page` -- the W40-S1 shape: the web_address seed
     raises a connection error, the listing seed answers a page linking an issuer-host PDF that passes the stubbed
     test -> the run is RESOLVED at step 4 on the issuer host, and `verified_site` is that issuer host.
   - `test_exchange_hosted_win_sets_no_verified_site` -- the winning PDF lives on the exchange host -> the source
     object is RESOLVED, `verified_site` is `None`, and the reason names the exchange host.
   - `test_every_seed_failing_is_unresolved_carrying_both_seeds` -- both seeds fail -> `UNRESOLVED-SOURCE`, the
     step-4 attempt names both seeds with their source labels, and all 5 steps are still recorded.

**What this cell does NOT change:** steps 1-3 and 5; the entity/current/family acceptance test; `keys_from_bloomberg`
and `BLOOMBERG_FIELDS`; `fetch.py` (a WALL -- a member of the production-home census deferred past manager review);
`crosswalk.py` (a WALL); the crawl bounds. **No other security is run** -- CSL only (C-VALIDATION-NAMES, PRD
`:1652-1655`: *"no cell is a fleet run or a re-run of the covered population"*).

**THE VALIDATION BAR:** CSL, one validation name, one live battery run on keys re-read from committed evidence, then
ONE pool object under the pair. Both outcomes are the ruling's sanctioned outcomes; neither is a failure of the cell.

## 2. WHERE THIS CAME FROM

**ROUND 18**, decomposition s.26 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-17 analysis
`ledger/ROUND_ANALYSIS.round17.md` @4a2f054389 (s.3 ruling `:62-74`, s.4 cell R18-C `:84`, disjointness `:87-89`)
sent as msg 23958 (*"R18-C: W40-S1, ruled. Try a second sanctioned seed for CSL from non-vendor sources the battery
can entity-test (Bloomberg's company-website field, then the exchange listing page). If none passes, record
UNRESOLVED by design, carrying every attempt. No hand-typed URL, and no vendor egress"*). Row `AMGT_RESAPP-Z-W40-S1`
(surfaced by `0.9.0_WK_AMGT_RESAPP~40` under `AMGT-rk-38`). Andrew-direct ~14:58Z (record @9bf58c4b95) and ~15:12Z
(record @1e2a54bf0f) govern this round's width and its one-slug issuance. No PRD addendum (analysis s.5 `:104-105`).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/battery.py
lib/research/filings/tests/test_battery.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~72/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-72.csl-second-sanctioned-seed.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`fetch.py`, `crosswalk.py`, `document.py`,
  the rk-38 deliverable, the ruling, the row). Scratch is `<your worktree>/.scratch/r72/` only (never committed).
- **Collision check, done at the cut:** `AMGT-rk-65..70` are all `complete` and write `roster.py`,
  `management_posture_batch.py` (+tests), `.tools/wk-provision.sh`, `.tools/comp-secrets` (+test), `crosswalk.py`
  (+test), `.tools/surprise-row-gate.py` (+test), `model_block_pull.py` (+test) -- none in `lib/research/filings/`.
  The direct act `AMGT-rk-48` (`~71`) has drained (@5a2ebfa1e1). Round 18 is TWO cells (Andrew-direct ~16:5xZ,
  record @c5532df80a): R18-A writes `lib/research/api/scoped_amgt.py` + tests and redeploys the adapter; R18-B is
  deferred and R18-D' parked, so neither writes this round.
  The held branch `wk-amgt-14-50` changes only `lib/research/management/{domains.json,enrich.py,
  management.schema.json,tests/test_lusha_domain.py}` plus AMGT org files (names only). **Zero overlap with
  `battery.py` / `test_battery.py`.** The only shared file is `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~72 <0.9.0_WK_AMGT_RESAPP~72@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**EGRESS, EXACTLY:** (a) steps 1-3 as `AMGT-rk-38` ran them -- EDGAR (`data.sec.gov`, `www.sec.gov`) and
`filings.xbrl.org`; (b) `www.csl.com.au`, Bloomberg's recorded seed, through the battery's own fetch only (no
UA, TLS or proxy variation -- W40-S1 already measured three); (c) the ASX's own public company page filled from the
`AU` template, and the hosts the bounded crawl then admits under `_host_allowed`, within `max_pages=40`. **Authority
for (c) is the CTO ruling s.3 `:69-70` (*"the exchange's listing page"*); no Andrew-level record naming
`asx.com.au` was found at the cut.** Nothing else: **no search engine, no vendor (Bright Data covers the CEO search
only), no proxy or alternate egress path, and never a hand-typed seed -- in particular never `investors.csl.com`.**
**NO BLOOMBERG CALL.** `AMGT-rk-38`'s ONE `ReferenceDataRequest` is spent and no authority for a second one on CSL
was found at the cut. The keys come from AC3's re-read of committed evidence. If you judge those keys insufficient
for the run, REFUSE AC4 with a row (disarm_owner `2.0.0_SA_COO~Z`). Never call `--bloomberg`, `blp_client` or any
MCP Bloomberg tool.
**THE POOL WRITE (AC5) IS SERVED-PLANE AND RUNS ONLY UNDER A NEVER-WIDEN PAIR.** The file
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18C_CSL_POOL_HALVES.md` must exist at your spawn with
BOTH halves signed: the COO half by `2.0.0_SA_COO~Z` and the CTO half by `1.0.0_SA_CTO~Z`. Its blast radius is ONE
prefix, `s3://opal-data-harvest/filings/v1/CSL_AU_Equity/`, in two branches: an UNRESOLVED run OVERWRITES
`UNRESOLVED-SOURCE.source.json` (before: sha256 `c2be7772...24cc47`, 3879 bytes), and a RESOLVED run ADDS
`doc-<sha16>.source.json` beside it. If the file is absent or a half is unsigned, AC5 is REFUSED with a row and
**`--write-pool` is never passed.** Never write any other key, and never run `analyze`, `batch` or any other
writer of `filings/v1/`.
PORTAL FROZEN. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No
secrets are needed; if one is, it goes through `comp-secrets` only and is never printed. No non-ASCII in anything
you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. In particular: never by a typed seed, never by a
second Bloomberg call, never by another egress path, never by relaxing the entity/current/family test, and never by
editing a WALL.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure the suite baselines (16 / 73) before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W72-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. **A pure disarm (for example, W40-S1
closed by this run's outcome) sets `DISMISSED_WITH_REASON`, never `GRADUATED`** -- and W40-S1's disposition is the
CVO's L9 act, not yours: name the outcome in your report and file nothing on its behalf.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC4 and AC5, which run under timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_battery.py -v -p no:cacheprovider 2>&1 | tail -30</invocation><expect>a final line "22 passed" (the 16 at the cut plus this cell's 6 new arms) and 0 failed, the PASSED lines naming test_exchange_listing_seed_derived_by_rule, test_exchange_seed_follows_bloomberg_web_address, test_head_copy_has_no_exchange_seed, test_unreachable_bloomberg_seed_falls_through_to_listing_page, test_exchange_hosted_win_sets_no_verified_site and test_every_seed_failing_is_unresolved_carrying_both_seeds -- the third proving the second discriminates (HEAD's copy tries only the web_address seed on the same stub)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -3</invocation><expect>"79 passed" and 0 failed -- the spawn-time baseline (73 passed at the cut) plus exactly this cell's 6 new arms; re-measure the baseline before you edit, and the bar is "baseline plus 6, failures 0"</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, json, os, re, glob; p = glob.glob("org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~40/*rk-38*.proof_of_spec.json")[0]; d = json.load(io.open(p, encoding="utf-8")); ev = [c for c in d["acceptance"] if c.get("criterion_id") == "AC3"][0]["output_evidence"]; g = lambda rx: (re.findall(rx, ev) or [None])[0]; k = {"legal_name": g(r"expected legal name .([^\x27]+). \(normalised"), "ticker_root": "CSL", "exchange": g(r"STEP 5 route=national-regulator key=([A-Z]+) "), "cik": g(r"STEP 2 route=edgar-bloomberg-cik key=([0-9]+) "), "lei": g(r"STEP 3 route=esef-lei key=([0-9A-Z]{20}) "), "web_address": g(r"STEP 4 route=company-site key=(\S+) "), "source": "committed-evidence:" + os.path.basename(p) + "#AC3"}; k.update({x + "_reason": (None if k[x] else "absent from the committed rk-38 AC3 evidence") for x in ("legal_name", "cik", "lei", "web_address")}); os.makedirs(".scratch/r72", exist_ok=True); io.open(".scratch/r72/csl_keys.json", "w", encoding="utf-8", newline="\n").write(json.dumps(k, indent=2, sort_keys=True) + "\n"); print(json.dumps(k, sort_keys=True)); print("null_fields", sorted(x for x in k if k[x] is None and not x.endswith("_reason")))'</invocation><expect>one JSON line carrying cik "1274152", exchange "AU", legal_name "CSL Ltd", lei "529900ECSECK5ZDQTE14", ticker_root "CSL", web_address "https://www.csl.com.au", and source naming the rk-38 proof file #AC3; then "null_fields []" -- measured exactly so at the cut. Single-quoted; no dollar sign reaches the shell</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && rm -rf .scratch/r72/battery && python -m lib.research.filings.battery --security-key CSL_AU_Equity --keys-json .scratch/r72/csl_keys.json --exchange AU --cache-dir .scratch/r72/battery --out-dir .scratch/r72/out 2>&1 | tail -20</invocation><expect>ONE of the two sanctioned outcomes, with "NOT-UPLOADED (no --write-pool)" last. EITHER RESOLVED at step 4: the step-4 line names BOTH seeds (https://www.csl.com.au and the filled AU listing page) with their source labels, a winning document URL, entity PASS on "CSL Ltd", current PASS and a known family, and a verified_site line that is the issuer host, or "verified_site null" naming the exchange host if the document is exchange-hosted. OR UNRESOLVED-SOURCE BY DESIGN: 5 STEP lines, steps 1-3 and 5 matching the rk-38 record in section 1, and step 4 naming both seeds, each with its own fetch outcome in the crawl log. Print which outcome occurred; both PASS this criterion. A run that tried only the web_address seed FAILS it</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && test -f org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18C_CSL_POOL_HALVES.md && python -m lib.research.filings.battery --security-key CSL_AU_Equity --keys-json .scratch/r72/csl_keys.json --exchange AU --cache-dir .scratch/r72/battery --out-dir .scratch/r72/out --write-pool 2>&1 | tail -4</invocation><expect>the same outcome as AC4, served from AC4's step cache (no new fetch), then exactly one "OK: uploaded s3://opal-data-harvest/filings/v1/CSL_AU_Equity/..." line whose key is UNRESOLVED-SOURCE.source.json on the UNRESOLVED branch or doc-sha16.source.json on the RESOLVED branch, with its sha256 and ContentLength. Run ONLY after reading both halves signed in the pair file; if it is absent, the test -f short-circuits, nothing is written, and AC5 is REFUSED with a row</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-72"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, subprocess; base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip(); [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "| base", (lambda b: len(b) - len(b.decode("utf-8")))(subprocess.run(["git", "show", base + ":" + f], capture_output=True).stdout)) for f in ("lib/research/filings/battery.py", "lib/research/filings/tests/test_battery.py")]'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0, each equal to its base figure printed beside it (0 and 0 at the cut, read from the merge-base, never assumed)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Also record in your deliverable the listing-page template's measuring GET (URL, status, bytes) and, for AC4,
every page_log entry of step 4.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~72/AMGT_RESAPP.TO-AMGT-rk-72.csl-second-sanctioned-seed.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the suite counts before and after, which AC4 outcome
occurred (RESOLVED or UNRESOLVED-by-design) with the step-4 seeds and their fetch outcomes, and the AC5 receipt or its
refusal.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r72/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>18</round>
<slot>~72</slot>
<fabric>site-z</fabric>
