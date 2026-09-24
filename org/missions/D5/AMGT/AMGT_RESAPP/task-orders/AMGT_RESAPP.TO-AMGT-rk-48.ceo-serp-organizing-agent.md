# AMGT_RESAPP task order -- `AMGT-rk-48` -- the CEO search as a SERP on the NAME with an organizing agent: FAILED distinct from EMPTY in the primitive FIRST, title and snippet kept, a namesake test, every fact quoted verbatim

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-48</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~49</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the weekly
  OpalResearch-ExecManagement task stays DISABLED and is neither read nor written; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  s3://opal-data-harvest management/v1/ prefix this project already writes) under the box's existing AWS
  credentials; it grants no permission and provisions no resource; no Lambda, no Terraform. The Bright Data
  key and zone and the Anthropic key reach the process only as environment variables the caller exports from
  comp-secrets (enrich.py:27-31), never a new grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~49`, and THIS ORDER RUNS ONLY AFTER `AMGT-rk-47` IS TERMINAL on this same slot**
(it is handed to you as a continuation; if you are reading it as a first spawn prompt, STOP and confirm with the
COO that `AMGT-rk-47`'s instance is on file and its `<status>` reads `complete`). Both orders edit
`lib/research/management/enrich.py::build_document`; the sequence is what keeps that file at one writer. Every
Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~49;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-48` (R14-E6; FWD-17; Exec Management brief s.9 and s.10; PRD v0.13 `C-EXEC-MANAGEMENT`)

**THE ANALYSIS ROW, VERBATIM** (`ledger/ROUND_ANALYSIS.round13.md:135` @`9c8e04cd9a`): *"E6 the CEO search as a SERP on
the name with an organizing agent -- FAILED distinct from EMPTY in the primitive FIRST, title and snippet kept, a
namesake test, every fact quoted verbatim"* -- serves FWD-17, cards 1 and s.9; co-sign YES; sequenced after E5.

**ANDREW'S WORD, VERBATIM** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md:34-35`
@`4f44431d34`): *"We should also do that, search the CEO's name with Bright Data SERP, and have an agent go through it
and pull/organize the relevant results."* Read narrow (`:38-45`): the CEO ONLY; a SERP on the NAME, not today's single
`site:<IR domain>` query; then a model step that reads the results and organizes the relevant ones. The ~18:4xZ
addendum (`:47-56`) authorized ONE exploration subagent (10 SERP requests, a US$5 model cap, three sample CEOs, no
Lusha, no S3 write, no repo change) -- **its design is your specification**:
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CEO_STEP_IMPLEMENTATION_DESIGN_20260918.md` @`4f44431d34` (the commit
whose message records *"verbatim rule held (101/101 kept, 163/163 mutants refused); the 'opaque redirect' label is
stale; the SERP primitive errs both ways (captcha = 200 with 0 bytes read as nothing found; a rewritten empty query
returns 9 URLs); the role term fixes common-name identity"*).

**THE RATIFIED TEXT YOU IMPLEMENT** -- PRD v0.13 `C-EXEC-MANAGEMENT`, `prd/AMGT_RESAPP_PRD.md:740-751` @`1699960261`:
- `:740-741`: *"The CEO profile comes from a Bright Data SERP on the CEO's NAME, followed by an agent that reads the
  results and pulls and organizes the relevant ones. The CEO is the only officer searched."*
- `:742-743`: *"A FAILED search (a request error or an unparseable body) is recorded as FAILED, with its cause -- never
  as an EMPTY search. Today the primitive breaks silently and returns a list (`data/find/dualbiz/scripts/serp.py:264-272`),
  and the caller records 0 urls as NOTHING_FOUND (`lib/research/management/enrich.py:434-439`)."*
- `:744`: *"Each organic result keeps its title and snippet, not the url alone."*
- `:745`: *"An identity test (this person, at this company, in this role) comes before any result is kept; a namesake
  is refused."*
- `:746-747`: *"Every organized fact carries its url and a quote that re-locates VERBATIM in the fetched page. A fact
  with no quote is HELD and never shown. The agent adds nothing from its own knowledge."*
- `:748-750`: the page's FIVE states -- CONFIRMED; NOT SEARCHED, with the reason; SEARCHED, NOTHING FOUND; SEARCHED,
  NOTHING KEPT; SEARCH FAILED, with its cause -- rendered from the object's own field (the PAGE is not yours; the
  OBJECT must carry a field those five states can be read from).
- `:751`: *"Bright Data calls, like Lusha calls, run only under Andrew's per-use word."*
- `:757`: *"Open at L4, not decided here: whether a Bloomberg-fallback CEO is searched."* -- you record
  `name_source` on the block (FILING | BLOOMBERG_FALLBACK, from `AMGT-rk-47`'s `roster_source`) so the L4 can settle
  the policy on a measured field; for the validation names you search whichever CEO the roster carries.

**THE MEASURED STATE, at HEAD (`da7b0b1804`; `serp.py` and the management package are byte-identical from
`9c8e04cd9a` through HEAD):**
- **The primitive errs in BOTH directions** (design s.1.5, `:112-119`, MEASURED on 10 of 10 authorized requests):
  a vendor captcha arrives as HTTP 200 with a 0-BYTE body and the failure only in `x-brd-status-code: 502` /
  `x-brd-error-code: captcha`; `json.loads("")` raises, `serp.py:269-272` `break`s, `[]` returns, and
  `enrich.py:436-439` records NOTHING_FOUND -- wrong. A bad zone is HTTP 400, `except Exception: break` at
  `serp.py:267-268`, `[]`, NOTHING_FOUND -- wrong. A GENUINELY empty query returns HTTP 200 JSON with
  `spelling.original_empty: true` and a NON-EMPTY `organic[]` for Google's rewritten query (9 urls measured) --
  treated as results -- wrong. `serp_brightdata` (`serp.py:245-286`) returns URLS ONLY (`:281-283` keeps `link`
  and drops `title`/`description`). `num=10` is stripped by the zone (`x-brd-serp-warn ... removed: num`, design
  `:91`).
- **The "opaque redirect wrapper" label is STALE** (design s.1.4, brief s.10 item 1): 50 of 50 organic links across 6
  responses were DIRECT urls; wrappers occur only in non-organic blocks and one un-followed GET reading `Location`
  resolves one. The 4 "links unreadable" objects reflect the module never resolving links, not the zone.
- `serp_brightdata` has THREE production callers (design `:277-283`): `serp.py:47` (`serp_search` feeding the
  FIND_DUALBIZ sweeps), `data/find/dualbiz/scripts/casec.py:80`, and `enrich.py:430`. The first two expect
  `list[str]`; **its return type does not change**.
- `enrich.py::ceo_public_profile` (`:404-453`) is today's one `site:<ir_domain> "<name>"` query with a host test;
  `find_ceo` (`:384-388`) matches `roster._CEO_RE` (`roster.py:154`) on the role; the call site is `:532-536`; the
  print line `:666-669`. `_serp_module()` (`:370-381`) loads the estate module by path and injects the key and zone
  from `BRIGHT_DATA_API_KEY` / `BD_SERP_ZONE`.
- The schema's `ceo_profile` definition (`management.schema.json:142-160`) carries the stale redirect claim at
  `:155-158`; `ceo_public_profile` is REQUIRED (`:14`).
- The adapter reads `ceo_public_profile` by name and derives `ceo_profile_reading` from its `basis` string
  (`lib/research/api/scoped_amgt.py:2275-2302`, `:2367-2368`). **It is NOT your surface** (chain B), and the R14-E1
  cell (analysis `:131`) makes it honor `absence_class`. So you keep `ceo_public_profile` PRESENT as a projection of
  the new block (below) so nothing the adapter reads today disappears mid-round.
- The verbatim locator already exists: `lib/research/filings/passages.py::Locator` (`:82-135`; `find(span)` returns
  the ORIGINAL character range or None, `contains(span)` refuses a needle under 12 characters `:118-119`). The
  one-seam model call form is `lib/research/filings/analyze.py` `anthropic_call` (design `:372-374`), so tests stub it.
- Identity, MEASURED in the prototype (design s.2.3-2.4, s.3.4): `"Jeff Miller" "Halliburton"` returned 0 of 9
  results about him; `"Jeff Miller" Halliburton CEO` returned 9 of 9; the deterministic anchor (surname and company
  token within 500 characters of page text) passed 18 of 18 positives and rejected 4 of 4 readable negatives; the
  verbatim control rejected 163 of 163 one-word mutants (drop 57/57, swap 54/54, splice 52/52, `:256-257`). Cost:
  about US$0.14 per CEO in model spend (`:323-325`).
- The CRO's exploration ran inside a scratch folder and committed NO code (`:47-56` of the cards record; the design
  s.6 lists `identity_offline.py` and `verbatim_control.py` as its own prototype files). You build from the design;
  you do not copy a worker's or a seat's scratch into production (`C-PRODUCTION-HOME`, PRD `:1643`).

**RULED -- what you build, IN THIS ORDER (the primitive FIRST, proven by a mutant pair, before any live search):**
1. **`data/find/dualbiz/scripts/serp.py`**: add a PURE classifier `classify_serp_attempt(http_status, headers, body)
   -> (status, failure)` and `serp_brightdata_records(query, max_pages=1, gl="us", hl="en", retries=2) -> dict` BESIDE
   `serp_brightdata` (design s.3.1, `:285-320`): same POST to `https://api.brightdata.com/request` with zone
   `_bd_serp_zone()` and `"format": "raw"`; URL `https://www.google.com/search?q=<q>&gl=us&hl=en` (no `num`);
   `FAILED` on a transport exception, HTTP >= 400, `x-brd-status-code != 200`, an `x-brd-error` header, a 0-byte
   body or a non-JSON body, with `failure.kind` VENDOR | CONFIG | TRANSPORT | UNPARSEABLE; `EMPTY` when the JSON parses
   and (`organic == []` or `spelling.original_empty` is true), records KEPT but flagged as answering `detected_query`;
   `OK` otherwise; retry ONLY a captcha or a 5xx, never a 4xx; return `{status, failure, attempts[], query,
   detected_query, query_rewritten, original_empty, gl, results_cnt, records[{rank, link, link_form, host, title,
   snippet, display_link, source}]}` with `snippet` from `description`; `enrich.scrub` over the parsed body with
   `general.mobile` EXEMPT (a device flag, design `:313-314`); wrapper resolution as a separate helper applied only to
   `google.com/goto?url=` links, one GET without redirect-following reading `Location`. **`serp_brightdata` becomes
   `[r["link"] for r in serp_brightdata_records(...)["records"]]`** and prints one `WARN:` line on FAILED, so
   FIND_DUALBIZ's contract (`list[str]`) is unchanged and its captcha silence becomes visible. A lane note for the
   COO travels in your report: `serp.py` is FIND_DUALBIZ's file (design `:321-322`); your `<paths>` grant covers the
   edit.
2. **`lib/research/management/ceo_search.py`** (new; design s.3.2-3.4): `ceo_profile(ceo, company, verified_domain,
   serp=None, model=None, fetcher=None, max_pages=3) -> dict` with the steps: NOT_SEARCHED (no CEO: `NO_CEO_ON_ROSTER`;
   empty roster: `ROSTER_UNRESOLVED`; no key/zone in the environment: `STEP_NOT_CONFIGURED`); the query
   `"<name>" <company short name> CEO` (the company short name = the crosswalk entity name with The / Inc /
   Corporation / Company / SE / plc / Holding(s) / Group stripped, the rule printed on the block); `SEARCH_FAILED` with
   the failure record on FAILED; `NOTHING_FOUND` with `ORIGINAL_EMPTY` on EMPTY; contact-broker hosts dropped; **Call
   A** triage over the SERP records into SAME_PERSON / DIFFERENT_PERSON / COMPANY_ONLY / UNCERTAIN with a prompt that
   forbids memory; `NOTHING_FOUND` with `NO_RESULT_ABOUT_PERSON` when none is SAME_PERSON; fetch at most `max_pages`
   SAME_PERSON pages directly with a browser UA (PDF via `pypdf` if installed, else `found_not_read` with the reason;
   NO install), text contact-scrubbed; **the deterministic anchor**: surname and company token within 500 characters
   of the page text, else `not_kept` with that reason; **Call B** extraction over surname-centred windows (each a
   substring, capped at 7,000 characters per page); **verification with `passages.Locator`**: a fact whose quote does
   not re-locate is DROPPED AND COUNTED (the identity quote must re-locate; it need not itself carry the surname);
   `CURATED` if at least one item is kept, `UNREADABLE` if results were about the person but no page could be read and
   verified; `found_not_read[]` for links only (HTTP 403/429/999, `WRAPPED_UNRESOLVED`, and every `linkedin.com` page,
   which is LINK-ONLY by this order and never fetched). `source_kind == official_bio` ONLY when the host is the
   verified company domain or a subdomain of it (never the model's label); duplicate facts removed by normalised
   quote; a final contact check over the serialised block, 0 or nothing is written. No unlocker zone is used
   (`serp_opal` only, the design's `:328-329` reading of Andrew's FIND_DUALBIZ cost ruling). The model call is the
   one-seam `anthropic_call` form so tests stub it; `stop_reason` is checked before parsing.
3. **The block** `ceo_profile` (design s.3.3, `:388-407`): `status` CURATED | NOTHING_FOUND | UNREADABLE |
   SEARCH_FAILED | NOT_SEARCHED; `reason_code`; `reason`; `ceo_name`, `name_source` (FILING | BLOOMBERG_FALLBACK from
   the object's `roster_source`), `company`, `role`; `search{...attempts[]...}`; `triage{...}`; `items[]{url, host,
   title, source_kind, why_kept, identity{anchor_distance_chars, quote, verified}, read{...}, facts[]{topic, quote,
   char_range}}`; `found_not_read[]`; `counts{results, about_person, pages_read, facts_proposed, facts_verified,
   facts_dropped_unverified, contact_strings_scrubbed}`; `cost{serp_requests, fetches, model_input_tokens,
   model_output_tokens, model_usd}`; `generated_at`. Fact topics: `current_role, prior_role, tenure_or_appointment,
   education, board_or_outside_role, stated_view_or_priority` -- NO `other` (design `:410-412`). **The quote IS the
   fact; there is no paraphrase field.**
4. **The schema** (`management.schema.json`): add `ceo_profile` as a REQUIRED closed definition with the same `not`
   clauses against contact keys at block, item and fact level; KEEP `ceo_public_profile` REQUIRED and correct its
   stale `:155-158` text -- it becomes a PROJECTION of `ceo_profile`: `url` = the first `official_bio` item's url else
   the first item's url else null; `status` RESOLVED when CURATED else ABSENT; `absence_class` null on CURATED,
   NOTHING_FOUND on NOTHING_FOUND, CANNOT_SAY on UNREADABLE / SEARCH_FAILED / NOT_SEARCHED; `basis` = the
   `ceo_profile.status`, `reason_code` and the counts in one sentence naming the url count. That keeps
   `read_management` (`scoped_amgt.py:2367-2368`) and the R14-E1 cell's reading intact; serving `ceo_profile` itself
   is the adapter cell's act, not yours (STATE, s.21c).
5. **The call site** `enrich.py:532-536` becomes `document["ceo_profile"] = ceo_search.ceo_profile(find_ceo(officers),
   ...)` plus the projection; `find_ceo` (`:384-388`) reads a BLOOMBERG_FALLBACK roster's officers too (the title is in
   `role`); `ceo_public_profile()` (`:391-453`) and `_serp_module`'s use for it are RETIRED; the `SERP:` print
   (`:666-669`) prints `ceo_profile.status`, `reason_code`, `name_source`, the counts and `cost.model_usd`; every
   dependency resolves BEFORE the first billable call (`:507-512`, row W22-S2). `enrich.main` keeps `--skip-pool`
   from `AMGT-rk-47` and every live write here passes it. Nothing in `batch.py` changes (`:128` already routes
   through `build_document`).
6. **The tests** (`lib/research/management/tests/test_ceo_search.py`, offline, fixtures from the MEASURED shapes):
   the primitive's four shapes; the OLD-vs-NEW discriminating pair (the same captcha fixture: `serp_brightdata`
   returned `[]` before -- now returns `[]` AND the records call reads FAILED); **a MUTANT classifier that maps a
   captcha to EMPTY must be REFUSED** (the test applies the mutant to `classify_serp_attempt` and asserts the
   assertion fires); the namesake: a fixture page mentioning the CEO's name beside a DIFFERENT company with the
   company token more than 500 characters away is `not_kept` by the anchor, and a positive-control page within 500
   characters is kept; the verbatim control: for a fixture profile, every kept quote re-locates and every one-word
   drop / swap / splice mutant is REFUSED, counts printed; `official_bio` assigned only on the verified host; a
   contact string planted in a fetched page never reaches the block. The model is a stub in every test.
7. **The live run, on the three validation names only**: `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` -- the
   CEO name from the roster `AMGT-rk-47` wrote (re-read at spawn); `BRIGHT_DATA_API_KEY` exported from `comp-secrets get
   find-insure/bright-data/api-key --reveal` (the key `serp.py:206-208` names) and `BD_SERP_ZONE=serp_opal` (the zone
   `serp.py:239-241` defaults to), as `enrich.py:27-31` requires; `ANTHROPIC_API_KEY` from `comp-secrets get
   anthropic-api-key --reveal` (`lib/research/filings/analyze.py:229`); ONE page per name, at most 2 retries on
   captcha/5xx (a hard cap of 9 SERP requests over the
   run, printed), at most 3 pages fetched per name, a model cap of US$2.00 over the run (the prototype measured
   US$0.14 per CEO), every figure printed. **Keyence's roster may carry no chief-executive title** (`_CEO_RE` at
   `roster.py:154`): then that name reads NOT_SEARCHED / `NO_CEO_ON_ROSTER`, which IS the honest outcome and one of
   the five states -- record it, file a row naming the Japanese title form for the L4, and do not widen `_CEO_RE`.
   A verified company domain for `official_bio` comes from the filings object only where `AMGT-rk-38` has landed one
   (its order names the field); absent that, every kept item is `third_party_bio` or another kind, and the block says
   so.

**This is a served-output-moving deploy (it REWRITES the three `management/v1/<key>/<as_of>.json` objects
`AMGT-rk-47` landed, on a served prefix). It needs a FRESH never-widen co-sign (CTO half + your COO's half) naming
that blast radius -- exactly those three keys, their `ceo_profile` and projected `ceo_public_profile` blocks -- with the
writers COUNTED (the same three as `AMGT-rk-47`'s pair) and a rollback read from the LIVE pre-act state of THIS act
(the sha-256 metadata `write_pool` stamps, `crosswalk.py:625-640`; print each key's pre-act `document-sha256`; rollback =
re-put the pre-act version by `VersionId`, bucket versioning the net). Open a NEW change-management ledger entry
BEFORE your first `--write-pool` act (never re-use `AMGT-rk-47`'s), close it on completion, per NEVER-2.**

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis `ledger/ROUND_ANALYSIS.round13.md` s.4 row `R14-E6` (`:135`)
@`9c8e04cd9a`; Andrew-direct ~17:2xZ and ~18:4xZ (`ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md:29-56`
@`4f44431d34`); the Exec Management brief s.9-s.10 (`:239-330`) and the CRO's prototype record
`CEO_STEP_IMPLEMENTATION_DESIGN_20260918.md` @`4f44431d34`; the CTO's intake (`CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:208-223`).
PRD v0.13 @`1699960261`: `C-EXEC-MANAGEMENT` (`:722-757`), `C-PRODUCTION-HOME` (`:1643`), `C-VALIDATION-NAMES` (`:1652`).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain E is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-48`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-48` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

**ISSUER BIND on `1.0.0_SA_CTO~Z`'s withheld half (msg 23833):** the live CEO search for a validation name runs ONLY
when that name's filings source object carries a `verified_site` landed by `AMGT-rk-38` (the ratified clause: the domain
comes from the filings battery, never from a hand list -- `domains.json` is NOT a source for any validation name and is
not read by this order's live arm); a name without one is recorded `NOT_ATTEMPTED` with reason `NO_VERIFIED_SITE` in AC4/AC5
and counted in the denominator, never searched on a typed or guessed domain. The issuer spawns this order after `rk-38`
drains (s.22d), so the honest outcome on the three names is measurable.

## 3. SURFACES -- what you may read and write

<paths>
data/find/dualbiz/scripts/serp.py
lib/research/management/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~49/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-48.ceo-serp-organizing-agent.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read `lib/research/filings/passages.py`,
  `lib/research/filings/analyze.py`, `data/find/dualbiz/scripts/casec.py`, `lib/research/api/scoped_amgt.py`, the CRO's
  design and the pool); this block governs WRITES. `lib/research/api/scoped_amgt.py`, `portal/`, `lib/research/filings/`,
  `data/find/dualbiz/scripts/casec.py`, `data/find/imo/` and `integrations/` are WALLS. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~49 <0.9.0_WK_AMGT_RESAPP~49@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **POOL WRITES** go through `crosswalk.write_pool` via `enrich.write_document` (`:619-622`) -- never a bare `put_object`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF** -- this cell is not collection. **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets` only, exported into the environment
of the one shell call that runs the live criterion, never written to a file. **THE VENDOR CALLS THIS ORDER NAMES:
(a) Bright Data SERP (`serp_opal` zone) on the three validation names' CEOs, at most 9 requests over the run, under
Andrew's ~17:2xZ design word recorded above and PRD `:740` @`1699960261` -- and ONLY IF the COO's spawn prompt states
that the per-use word for the validation run is on file (PRD `:751` and `:1656` name the per-use rule; the ~17:2xZ
record's own narrow reading `:44-45` left the running validation's Bright Data use to Andrew); if the spawn prompt does
not state it, AC4-AC6 are REFUSED with a row and AC1-AC3 still close; (b) Anthropic, the project's own analyzer
instrument, at most US$2.00 over the run, printed.** No Lusha (`AMGT-rk-49`'s cell), no Seeking Alpha, no unlocker.
No LinkedIn page is ever fetched. No contact data point is stored at any level. No non-ASCII in anything you write.
**PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-read the three management
objects at spawn: their `roster_source`, their CEO (via `find_ceo`) and whether a filings object with a verified site
has landed for any of them.
**THE PRIMITIVE FIX LANDS FIRST AND CLOSES OFFLINE (AC1-AC3) BEFORE ANY LIVE REQUEST (AC4-AC6).**
**NO FLEET RUN, NO RE-RUN:** the three keys are the only targets; the batch is never run.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W49-S<k>`, `<k>` continuing from where `AMGT-rk-47`'s rows left off;
`"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by textual splice inside the one fenced
JSON array (never re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND
KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_ceo_search -v 2>&1 | tail -n 40</invocation><expect>the module ends "OK" with its "Ran N tests" denominator and the run lists, by name, at least these tests passing: captcha (HTTP 200, 0-byte body, x-brd-error-code captcha) classifies FAILED kind VENDOR and is retried exactly 2 times (attempts 3); HTTP 400 "zone not found" classifies FAILED kind CONFIG with attempts 1 (never retried); a body with spelling.original_empty true and 9 organic entries classifies EMPTY with 9 records kept and flagged; a well-formed body classifies OK with title and snippet on every record; the old wrapper serp_brightdata returns the same list of links the records call holds; the MUTANT classifier that maps captcha to EMPTY is REFUSED (the test passes only because the assertion fired against the mutant); the namesake page fails the 500-character anchor and the positive-control page passes it; every kept quote of the fixture profile re-locates and drop/swap/splice mutants are refused with printed counts of the form "mutants refused N of N"; a planted contact string in a fetched page never reaches the serialised block</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.management import enrich
serp = enrich._serp_module()
import inspect
print('has serp_brightdata_records', hasattr(serp, 'serp_brightdata_records'))
print('has classify_serp_attempt', hasattr(serp, 'classify_serp_attempt'))
src = inspect.getsource(serp.serp_brightdata)
print('wrapper delegates', 'serp_brightdata_records' in src, 'lines', len(src.splitlines()))
for hs, hdr, body, want in [(200, {'x-brd-status-code': '502', 'x-brd-error-code': 'captcha'}, b'', 'FAILED'), (400, {}, b'zone \"x\" not found', 'FAILED'), (200, {'x-brd-status-code': '200'}, b'{\"organic\": [], \"spelling\": {\"original_empty\": true}}', 'EMPTY'), (200, {'x-brd-status-code': '200'}, b'{\"organic\": [{\"link\": \"https://example.com/a\", \"title\": \"t\", \"description\": \"d\"}], \"general\": {\"query\": \"q\", \"detected_query\": \"q\"}}', 'OK')]:
    status, failure = serp.classify_serp_attempt(hs, hdr, body)
    print(hs, dict(hdr), want, '->', status, (failure or {}).get('kind'), 'PASS' if status == want else 'FAIL')
print('DENOMINATOR: 4 measured shapes classified')
"</invocation><expect>both hasattr lines read True; the wrapper delegates True; the four measured shapes from the design's s.1.5 print FAILED VENDOR, FAILED CONFIG, EMPTY, OK in that order, each PASS, denominator 4 of 4 -- this is the same classifier AC1 tests, exercised through the path enrich.py actually loads the module by (a different instrument from the unittest import)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.management import enrich
schema = json.load(open(enrich.SCHEMA_PATH, encoding='utf-8'))
req = schema['required']
print('required has ceo_profile', 'ceo_profile' in req, 'keeps ceo_public_profile', 'ceo_public_profile' in req)
defs = schema['definitions']
print('ceo_profile statuses', defs['ceo_profile_block']['properties']['status']['enum'] if 'ceo_profile_block' in defs else 'DEFINITION NAME DIFFERS -- print the actual one')
print('fact topics', defs.get('ceo_fact', {}).get('properties', {}).get('topic', {}).get('enum'))
text = json.dumps(schema)
print('stale redirect claim present', 'opaque redirect' in text)
print('contact keys forbidden at fact level', 'not' in defs.get('ceo_fact', {}))
print('DENOMINATOR: 1 schema file, %d definitions' % len(defs))
"</invocation><expect>required has ceo_profile True and keeps ceo_public_profile True; the status enum reads exactly CURATED, NOTHING_FOUND, UNREADABLE, SEARCH_FAILED, NOT_SEARCHED (if the worker named the definitions differently it prints the actual names and the same enums); the topic enum is the six topics with NO "other"; the stale "opaque redirect" claim is ABSENT (False); the fact definition carries a not clause against contact keys; the definitions count is printed</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && export BRIGHT_DATA_API_KEY="$(comp-secrets get find-insure/bright-data/api-key --reveal)" && export BD_SERP_ZONE="serp_opal" && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal)" && python -c "
import boto3, datetime, json
s3 = boto3.client('s3', region_name='us-east-1'); B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
key = 'management/v1/CAT_US_Equity/%s.json' % as_of
h = s3.head_object(Bucket=B, Key=key); print('PRE-ACT', key, 'sha', h['Metadata'].get('document-sha256'), 'version', h.get('VersionId'))
from lib.research.management import enrich
rc = enrich.main(['--security-key', 'CAT_US_Equity', '--as-of', as_of, '--write-pool', '--skip-pool', '--json'])
print('RC', rc)
doc = json.loads(s3.get_object(Bucket=B, Key=key)['Body'].read())
cp = doc.get('ceo_profile') or {}
print('POST-ACT status', cp.get('status'), 'reason_code', cp.get('reason_code'), 'name_source', cp.get('name_source'), 'ceo', cp.get('ceo_name'), 'query', (cp.get('search') or {}).get('query'))
print('counts', json.dumps(cp.get('counts')), 'cost', json.dumps(cp.get('cost')), 'attempts', len((cp.get('search') or {}).get('attempts') or []))
print('items', len(cp.get('items') or []), 'found_not_read', len(cp.get('found_not_read') or []), 'projection', json.dumps(doc.get('ceo_public_profile')))
print('DENOMINATOR: 1 of 3 validation names (CAT); facts_verified %s of facts_proposed %s' % ((cp.get('counts') or {}).get('facts_verified'), (cp.get('counts') or {}).get('facts_proposed')))
"</invocation><expect>PRE-ACT prints the live sha and version of the CAT object AMGT-rk-47 wrote (the rollback baseline); RC 0; POST-ACT status is ONE of the five states with a reason_code, name_source printed (expected BLOOMBERG_FALLBACK unless a RESOLVED filing landed), the query in the form "<name>" Caterpillar CEO; counts carry facts_verified equal to facts_proposed minus facts_dropped_unverified; attempts at most 3; cost.model_usd printed and under 2.00; the projection carries status/absence_class/basis consistent with the block; the secret values never appear in the output (the exports are outside the printed program)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && export BRIGHT_DATA_API_KEY="$(comp-secrets get find-insure/bright-data/api-key --reveal)" && export BD_SERP_ZONE="serp_opal" && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal)" && python -c "
import boto3, datetime, json
s3 = boto3.client('s3', region_name='us-east-1'); B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
from lib.research.management import enrich
done = 0
for k in ['CSL_AU_Equity', '6861_JP_Equity']:
    key = 'management/v1/%s/%s.json' % (k, as_of)
    h = s3.head_object(Bucket=B, Key=key); print('PRE-ACT', key, 'sha', h['Metadata'].get('document-sha256'), 'version', h.get('VersionId'))
    rc = enrich.main(['--security-key', k, '--as-of', as_of, '--write-pool', '--skip-pool'])
    doc = json.loads(s3.get_object(Bucket=B, Key=key)['Body'].read()); cp = doc.get('ceo_profile') or {}
    done += 1 if rc == 0 else 0
    print('POST-ACT', k, 'RC', rc, 'status', cp.get('status'), 'reason_code', cp.get('reason_code'), 'name_source', cp.get('name_source'), 'ceo', cp.get('ceo_name'), 'items', len(cp.get('items') or []), 'counts', json.dumps(cp.get('counts')), 'cost', json.dumps(cp.get('cost')))
print('DENOMINATOR: %d of 2 remaining validation names written' % done)
"</invocation><expect>both PRE-ACT baselines printed; both RC 0; CSL reads one of the five states with its reason_code (its CEO comes from the roster AMGT-rk-47 wrote); Keyence reads either a searched state or NOT_SEARCHED with NO_CEO_ON_ROSTER when its roster carries no chief-executive title (the honest outcome, recorded as a row for the L4 -- not repaired by widening _CEO_RE); every counts block carries facts_verified consistent with facts_proposed minus facts_dropped_unverified; the running total of SERP requests over AC4 and AC5 is at most 9 and of model_usd at most 2.00, both stated in the report; denominator 2 of 2</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, datetime, json
from lib.research.management import enrich
from lib.research.filings.passages import Locator
s3 = boto3.client('s3', region_name='us-east-1'); B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
total = relocated = contact = 0; objects = 0
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    key = 'management/v1/%s/%s.json' % (k, as_of)
    doc = json.loads(s3.get_object(Bucket=B, Key=key)['Body'].read()); objects += 1
    ok, errors = enrich.validate(doc)
    contact += len(enrich.contact_fields_present(doc))
    cp = doc.get('ceo_profile') or {}
    for item in cp.get('items') or []:
        page = (item.get('read') or {}).get('text_sha256_16')
        for fact in item.get('facts') or []:
            total += 1
            relocated += 1 if fact.get('char_range') and fact.get('quote') else 0
    print(k, 'schema-valid', ok, 'errors', errors[:2], 'status', cp.get('status'), 'facts', sum(len(i.get('facts') or []) for i in cp.get('items') or []))
print('DENOMINATOR: %d objects read back; facts with a verbatim quote and char_range %d of %d; contact fields stored %d' % (objects, relocated, total, contact))
"</invocation><expect>3 objects read back from the pool, each schema-valid True with no errors; every fact carries a quote and a char_range (relocated equals total; if total is 0 across all three the line says so and the report states the vacuous case explicitly rather than reading it as a pass); contact fields stored 0 of 3 objects -- a read-back through get_object and validate(), a different instrument from the writer's own print</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. **AC1-AC3 write nothing and run before the live acts; AC4 and AC5 run AFTER your NEW change-management entry is
OPEN and the never-widen pair is on file; AC6 after both.** If the spawn prompt does not state the per-use word for
the validation run's Bright Data calls, AC4-AC6 are REFUSED with a row and the order is terminal on AC1-AC3 plus that
refusal.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~49/AMGT_RESAPP.TO-AMGT-rk-48.ceo-serp-organizing-agent.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; close the change-management entry; commit with `--only -- <paths>`. Report once; your queue ends here.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~49</slot>
<fabric>site-z</fabric>
