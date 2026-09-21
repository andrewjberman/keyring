# AMGT_RESAPP task order -- `AMGT-rk-79` -- Keyence's roster reason becomes a READABLE sentence with no literal missing value, a Japanese-listed "President" is read as the chief executive when no officer carries a CEO title, and ONE live CEO web search for Tetsuya Nakano (6861_JP_Equity) runs under Andrew's per-use word, landing in ONE write to management/v1/6861_JP_Equity/2026-09-19.json, plus ONE no-search write re-deriving CSL's roster reason as a readable sentence from its CURRENT filings object (management/v1/CSL_AU_Equity/2026-09-19.json), plus ONE no-search write marking CAT's roster INCOMPLETE-NO-CEO because its 10-K's Item 10 points to an Item 1D the stored filing does not hold (management/v1/CAT_US_Equity/2026-09-19.json)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-79</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~79</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and reads or writes no
  schedule; its three live acts (AC5, AC6, AC7) are each run once by hand for ONE named key. It OPENS one deploy-ledger entry with
  .tools/deploy_ledger.py before those acts and CLOSES it on the read-back (AC4 / AC9), as AMGT-rk-48 and AMGT-rk-75
  did for the same keys.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, grant or Lambda is read or changed. The adapter
  (opal-amgt-scoped-api, CodeSha256 hP+6OO5P... since AMGT-rk-77) is NOT redeployed (CTO ruling (c), msg 24058): none of lib/research/management/
  is in its packaged closure (0 of the 58 paths AMGT-rk-77's AC3 enumerated), and it serves the stored management
  object whole. The live acts are three in-place rewrites of three objects under management/v1/ in opal-data-harvest with
  the seat's existing credentials, plus the vendor egress (6861 only) the pair in section 4 names, the shape AMGT-rk-48
  and AMGT-rk-75 ran.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~79`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and every code path in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call
begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~79;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check
out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential. **The two secrets this order
needs reach the process ONLY as `export NAME="$(comp-secrets get <secret> --reveal --value-only)"` followed by an
empty-key guard, inside AC5's one call (AC6 and AC7 need no secret). Never print, echo, log, quote or write a secret value, anywhere.**

## 1. THE CELL, inlined in full -- `AMGT-rk-79` (round 20, R20-A; rows `AMGT_RESAPP-Z-S195`/`Z-S196`, `Z-S197`, `Z-S200`, `Z-S202`)

**THE RULING OF RECORD, verbatim (`1.0.0_SA_CTO~Z`, msg 24049, 2026-09-21T20:04:57Z, answering the issuer's five
calls on this order):**
*"1. rk-75's pinned arm: ACCEPTED. Amend that ONE arm and name it superseded under v0.16's readable-reasons rule.
2. Failure prefix: ACCEPTED for this cell. "the SERP primitive raised: the CEO web search did not complete (...)"
keeps the adapter's SEARCH_FAILED signal with no redeploy, and it only shows if the one search fails. But the prefix
is jargon on a reader line, so it is NAMED DEBT: the next adapter redeploy moves ceo_profile_reading to key on the
reason_code field rk-75 added, and the prefix goes. Record it in the order's not-covered list.
3. L5 wording: APPROVED as written. That covers the Yuho sentence, the no-reason sentence, and the five
searched-status sentences (missing numbers print as 0, missing kinds as "unknown", a missing name never appears).
4. Locale: ACCEPTED, en-US default. It is one search, Keyence has English IR pages, and per Andrew's ~16:5xZ word
translation is not a priority.
5. Z-S200 (disarm owner: me): WIDEN R20-A to a SECOND write, CSL's roster_reason only, re-derived as a readable
sentence from the CURRENT filings object (rk-72's rewrite, which names both seeds). The limits:
- no search, Bloomberg call or pool write on CSL, and no other CSL field;
- ONE pair naming both keys;
- the Bright Data search stays 6861 only, at most 3 requests, at most USD 1.00, never re-run.
With CSL now a written key, AC6's sibling check becomes: CAT unmoved, CSL changed ONLY at roster_reason (plus its
evidence mirror, if it carries one)."* (Its AC6 is this order's AC8.)

**THE SECOND RULING OF RECORD, verbatim (`1.0.0_SA_CTO~Z`, msg 24058, `ledger/ROUND_ANALYSIS.round19.md` s.2-s.4;
the file was UNCOMMITTED at the draft -- the issuer pins its commit at the cut):** s.2: *"The COO's fold is accepted:
R20-A and R20-B both write `roster.py`, so they are ONE cell."* ... *"(iv) S202: the Item 10 cut follows a
cross-reference to the section it names, and **a roster with no chief executive is never served RESOLVED** -- it is
marked incomplete; CAT re-derived from its stored filing"*. s.3: *"(a) CAT's stored filing may not hold Item 1D.
RULED: no new fetch in round 20. The cell uses what is stored. - If the stored object holds Item 1D's text, follow the
cross-reference and re-derive CAT's roster. - If it does not, CAT is served incomplete, with a readable reason naming
the unread section ("the 10-K lists its executive officers in Item 1D, which was not read")."* *"(b) The census of
RESOLVED rosters with no CEO across the 15 names. RULED: every hit joins rk-79's write set. ... - The census runs
BEFORE the pair is signed. The pair prints the literal key list: 6861, CSL, CAT, plus each census hit. - The extra keys
get no vendor call, no fetch and no Bloomberg re-pull. Each is re-derived from stored objects only. - If the census is
0 beyond CAT, the write set stays 3, and the pair says so with the denominator printed (15)."* *"(c) ... RULED: no
adapter redeploy in round 20. - Carry incompleteness in a field the deployed adapter already passes verbatim, which
the drafter measures against the DEPLOYED bytes, not the repo. `roster_status` is the first candidate. - If no such
field exists, STOP and report before the cut."* s.4: *"Z-S202: ... It disarms when CAT reads back either with a CEO
or as incomplete. It must never read RESOLVED with no CEO."*

**The contract, verbatim (PRD v0.16 @2d0da569e7, `prd/AMGT_RESAPP_PRD.md` `:764-767`, `C-EXEC-MANAGEMENT`):**
*"**Who the CEO is:** the officer carrying a chief-executive title; for a Japanese-listed issuer with no such officer,
a "President" or "Representative Director and President" is the chief executive. The rule is not extended to another
jurisdiction without evidence for that jurisdiction. A served reason is always a readable sentence; a missing value
is never printed into it as a literal."* The same clause (`:768`, `:777`): *"A FAILED search (a request error or
an unparseable body) is recorded as FAILED, with its cause -- never as an EMPTY search."* and *"Bright Data calls,
like Lusha calls, run only under Andrew's per-use word."*

**The word, verbatim (Andrew-direct ~19:5xZ 2026-09-21, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_195xZ_AMGT_RESAPP_KEYENCE_SEARCH_YES_LUSHA_R20_YES.md`
@4bcfed0e0d, addendum @6e09c649aa, `:8`):** *"Yes on Keyence and Yes on Exception."* Read by its recorder (`:13-15`):
*"Keyence: YES -- the vendor per-use word for ONE Bright Data CEO search on `6861_JP_Equity`, with its "President"
read as the chief executive (PRD v0.16 `C-EXEC-MANAGEMENT`). One name, one search. It does NOT cover any other name,
a repeat, or a schedule. It rides round 20's cell R20-A, after v0.16 is signed."* The CTO (msg 24039): *"R20-A now
does four things: the roster.py reason wording, the JP title rule, the ONE search, and ONE write to 6861's management
object. That is one pair for all of it."* The word also settles, for this ONE name, the PRD's open L4 question
(`:783`, *"whether a Bloomberg-fallback CEO is searched"*): Nakano is a Bloomberg-fallback officer and the word names
him.

**THE MEASURED STATE, at HEAD `14bc8021af` (SITEZ). RE-READ every line at your branch HEAD before editing:**
- **The stored object** `s3://opal-data-harvest/management/v1/6861_JP_Equity/2026-09-19.json`: 3 versions, 0 delete
  markers, latest `1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G` (AMGT-rk-75, 2026-09-21T19:03:39Z, 3827 bytes, sha256
  `29e6a8732a26723a7aa0482388e32a9cb9f9a8c29167a583dd7827d4d72c349e`). `roster_status UNRESOLVED-SOURCE`,
  `roster_source BLOOMBERG_FALLBACK`, `source_accession doc-1defdb68a7ffd3b7`, `source_item ''`, ONE officer
  `{name "Tetsuya Nakano", role "President", source "bloomberg"}`. `roster_reason` AND `absence_reason_evidence` BOTH
  read *"the persisted None filing doc-1defdb68a7ffd3b7 carries an EMPTY officer section (no item label): the item
  was not cut from the primary document"*. `ceo_profile`: `NOT_SEARCHED / NO_CEO_ON_ROSTER`, `ceo_name None`,
  `company "Keyence Corp"`, `search.query None`, `cost.serp_requests 0`.
- **Served today** (live invoke of `/api/scoped/amgt/security/6861_JP_Equity/thesis`): `management_status SERVED`,
  `roster_source BLOOMBERG_FALLBACK`, `officer_count 1`, `roster_reason` the "None" sentence above -- manager-visible.
- **CSL's stored object** `s3://opal-data-harvest/management/v1/CSL_AU_Equity/2026-09-19.json` (measured 2026-09-21
  ~20:1xZ): 3 versions, latest `u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS` (AMGT-rk-75, 19:03:38Z, 9494 bytes).
  `roster_status UNRESOLVED-SOURCE`, `roster_source BLOOMBERG_FALLBACK`, 14 officers, `source_accession None`,
  `absence_reason_class pull-missed`. **`roster_reason`** (728 chars) = `"the persisted filing is itself
  UNRESOLVED-SOURCE: " + <the filings object's reason as of 2026-09-19>` (written by `roster.py:936-938`), and
  **`absence_reason_evidence`** (678 chars) = that SAME filings reason WITHOUT the prefix (written by
  `enrich.classify_roster_absence`, `enrich.py:193`, whose UNRESOLVED branch `:215-219` returns the source object's own
  reason). **THE MIRROR FIELD IS `absence_reason_evidence`** -- not a byte copy of `roster_reason`, but the same
  source text it is derived from. BOTH are STALE: each names only the `https://www.csl.com.au` seed (0 mentions of
  the ASX page), from before AMGT-rk-72. Served today, beside the 14 Bloomberg officers (row Z-S200).
- **CSL's CURRENT filings object** `filings/v1/CSL_AU_Equity/UNRESOLVED-SOURCE.source.json`, latest VersionId
  `GzAiBH5LVctrkT8atzKoSYbZnwtVZ4_9` (AMGT-rk-72): `status UNRESOLVED-SOURCE`, 5 battery attempts -- step 1
  `edgar-ticker` ("name guard REFUSED: SEC ticker table names 'CARLISLE COMPANIES INC' ..."), step 2
  `edgar-bloomberg-cik` ("... no 10-K in the issuer's recent window ..."), step 3 `esef-lei` ("not held (HTTP
  404)"), step 4 `company-site` (seed_sources `bloomberg-web-address` https://www.csl.com.au and
  `exchange-listing-page` https://www.asx.com.au/markets/company/CSL, "crawl bound reached ..."), step 5
  `national-regulator` ("no adapter for jurisdiction UNKNOWN"). `enrich.classify_roster_absence` on it returns
  class `pull-missed` (unchanged from the stored class) and evidence = its current reason, which names BOTH seeds.
- **Population the new sentence rule reads, measured:** 180 `UNRESOLVED-SOURCE.source.json` objects under
  `filings/v1/`; exactly **2** carry battery attempts (`6861_JP_Equity`, `CSL_AU_Equity`), the other 178 are
  pre-battery objects with a `reason` and no `battery.attempts`. A scratch prototype of RULED item 1b over all 180
  printed a literal `None` in **0 of 180** sentences.
- **Where the "None" comes from:** `lib/research/management/roster.py:943-947`, `"the persisted %s filing %s carries
  an EMPTY officer section (%s): ..." % (source_object.get("form"), source_object.get("accession"), ...)`. The filings
  source object `filings/v1/6861_JP_Equity/doc-1defdb68a7ffd3b7.source.json` carries `form None`, `family "YUHO"`,
  `status RESOLVED`, `officer_section {}`.
- **CENSUS BY SUBTRACTION of reason-building formats in `lib/research/management/`:** 6 modules, 140 string-format
  sites (`%`, `.format`, f-string; AST walk); 18 of them build reason or filing text. Subtract the 14 that are CLI
  print lines or an exception message, never stored (`batch.py:212,217`; `enrich.py:834,950,955,956,965,978`;
  `roster.py:892,999,1001,1003,1006,1008`): 4 build a STORED reason. Of the 4, THREE can print a missing value as a
  literal: **`roster.py:937`** (`"... UNRESOLVED-SOURCE: %s" % source_object.get("reason")` -- None when the filing
  object has no reason), **`roster.py:943-947`** (`form` / `accession` None), and **`ceo_search.py:741`** (the composed
  `"%s / %s -- ..." % (status, reason_code, ...)` basis: `reason_code` is None on every CURATED block, so a CURATED
  search -- this order's expected branch -- would serve *"CURATED / None -- ..."*). The fourth, `roster.py:931`,
  prints a label or FILINGS_PREFIX, never None. The two stored-reason writers the text filter does not catch never
  receive None either: `roster.py:951` (`parse_officer_section`'s reason is a string on every empty-officers path,
  `:769-824`) and `enrich.py:625` (`roster_status` is an enum). Live census of ALL 15 stored management objects:
  exactly 2 fields carry a literal "None" -- 6861's `roster_reason` and `absence_reason_evidence`.
- **CEO detection:** `enrich.find_ceo` (`enrich.py:412-416`) returns the first officer whose role matches
  `roster._CEO_RE = r"chief\s+executive\s+officer|\bceo\b"` (`roster.py:192`). "President" never matches.
- **The jurisdiction, measured:** the crosswalk `crosswalk/v1/2026-09-19.json` carries `exchange` on every keyed record,
  and the security key's `_<EXCH>_Equity` suffix EQUALS that field on **36 of 36** keyed records (0 disagree). Two
  carry `JP` (`9433_JP_Equity`, `6861_JP_Equity`); of the 15 names with a management object, ONLY `6861_JP_Equity` is
  JP. So the listing exchange is read from the key suffix -- the crosswalk's own convention -- and the rule changes no
  other stored name's CEO.
- **The search's domain:** `ceo_search.ceo_profile` requires `verified_domain` (`:528-531`), which comes ONLY from the
  filings battery's `verified_site` (`enrich.verified_domain_for`, `:166-174`). 6861's source object carries
  `verified_site.host "www.keyence.co.jp"` (step 4, `winning-document-host`). **So the SEARCHED branch is expected.**
- **What ONE search costs, read from the code:** ONE SERP call, `serp_brightdata_records(query, max_pages=1)`
  (`ceo_search.py:545`), which retries ONLY a captcha or a 5xx, at most 2 times (`data/find/dualbiz/scripts/serp.py:400,
  :459-462`): **at most 3 SERP requests**. At most `max_pages=3` result pages fetched (`:609`, LinkedIn never fetched).
  At most 4 model calls (1 triage + up to 3 extracts), each `max_tokens 2000` on `claude-opus-5` at US$5 / US$25 per
  million tokens (`:108-110`), page window 7000 characters (`:107`): **worst case about US$0.35**.
- **CAT's stored object** `management/v1/CAT_US_Equity/2026-09-19.json` (measured ~20:3xZ): 3 versions, latest
  `tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU` (AMGT-rk-75). `roster_status RESOLVED`, `roster_source FILING`, ONE officer
  `{Derek Owens, Chief Legal Officer and General Counsel}`, `roster_reason None`, `section_refers_to None`,
  `absence_reason_class None`, `ceo_profile NOT_SEARCHED / NO_CEO_ON_ROSTER`. Served today as SERVED, 1 officer, no
  CEO -- a roster served as complete when it is not (row Z-S202, ARMED).
- **CAT's stored filing** `filings/v1/CAT_US_Equity/000001823026000008.source.json` (latest
  `G8qBiPSVoZvsUCQ6_M92Gyp3_8K3ov6O`, 167186 bytes; the ONLY object under `filings/v1/CAT_US_Equity/`): form 10-K,
  `officer_section.item` "Item 10. Directors, Executive Officers and Corporate Governance" (27766 chars), whose
  text reads *"Identification of Executive Officers and Business Experience | Information required by this Item
  appears in Item 1D of this Form 10-K."*; `excerpt.items` holds ONLY `Item 1A. Risk Factors` and `Item 7.
  Management's Discussion and Analysis`. The full primary document (555436 text chars, `cat-20251231.htm`) is NOT
  stored: 0 other keys for this accession across all 17 top-level pool prefixes, and 0 local files. **So Item 1D's
  text is NOT held -- the "incomplete" branch of ruling (a) applies, and no fetch is made (the one EDGAR fetch is
  carded to Andrew by the CTO).**
- **Why today's parser misses it:** `roster.parse_officer_section` already knows this shape (its docstring `:53-56`
  names *"CAT's Item 10"* as a section that points elsewhere), but its pointer path (`:809-816`) fires ONLY when the
  section yields 0 candidates; CAT's Item 10 yields ONE stray row (Derek Owens), so the pointer never fires.
- **The pointer, measured over all 8 RESOLVED rosters' stored sections (the negative control):** the generic
  `_find_reference_pointer` fires on 4 of 8 (BA, CAT, HD, VLO -- their Item 10 incorporates the DIRECTORS by
  reference while listing the officers itself), so it cannot be the trigger. An EXECUTIVE-OFFICER pointer (a sentence
  naming "executive officers" and then "appears in / included in / set forth in / see" + a Part I or Item label)
  fires on **1 of 8: CAT only** (`Item 1D`). BA (12 officers), HD (10) and VLO (5) are the negative control: generic
  pointer YES, executive-officer pointer NO, CEO present, unchanged.
- **THE CENSUS, ruling (b), measured over all 15 names' newest management objects:** RESOLVED rosters whose officers
  include no chief executive (after the v0.16 JP rule) = **1 of 15: `management/v1/CAT_US_Equity/2026-09-19.json`**
  (8 RESOLVED in all; the other 7 -- BABA 7, BA 12, COST 13, HD 10, NU 9, SAP 6, VLO 5 officers -- each carry one).
  **The pair's literal key list is therefore 6861, CSL, CAT: 3 keys, denominator 15.** AC3 re-runs the census at
  spawn and STOPS if the set differs.
- **The deployed adapter, measured against its DEPLOYED BYTES (ruling (c)):** `get-function` on `opal-amgt-scoped-api`
  (CodeSha256 `hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=`, LastModified 2026-09-21T19:20:04Z); the zip's
  `lib/research/api/scoped_amgt.py` sha256 `9832f57a6e169d1c...` EQUALS the repo HEAD file. `read_management`
  routes a document with officers, `roster_source` other than BLOOMBERG_FALLBACK and `roster_status != "RESOLVED"` to
  `management_status ABSENT`, `absent_because ROSTER_UNRESOLVED_NO_FALLBACK`, `roster_status` VERBATIM, `reason` =
  the stored `roster_reason`, `officer_count` = the REAL count, `officers []` (repo `:2615-2634`, identical in the
  deployed bytes). **So `roster_status` passes verbatim with a truthful served class; no redeploy is needed.** The
  schema (`management.schema.json:38-41`) admits only `RESOLVED` and `UNRESOLVED-SOURCE` today.
- **Test baselines at the cut:** `lib/research/management/tests` **84 passed** (8 subtests); `lib/research/api/tests`
  **191 passed**.

**RULED, what you build (the issuer's L5 rulings, named as such where the contract does not fix the wording):**
1. **`roster.py`, readable reasons, never a literal missing value.** One helper `_filing_label(source_object)` and the
   two None-capable sites rewritten through it:
   - `:943-947` (empty officer section) becomes EXACTLY *"The {label} was found, but its officer section is empty, so
     no officers could be read from the filing."*, where `{label}` is `"{form} filing"` when `form` is set, else
     `FILING_LABELS[family]` when the family is in a ONE-entry table `{"YUHO": "Japanese annual securities report
     (Yuho)"}`, else `"{family} filing"` when a family is set, else `"filing"`. The accession is NOT in the sentence;
     it stays in `source_accession` (already stored). For 6861 the sentence is *"The Japanese annual securities report
     (Yuho) was found, but its officer section is empty, so no officers could be read from the filing."* (L5 wording.)
   - **1b. `:937` (an UNRESOLVED-SOURCE filing) -- SUPERSEDED by ruling 5 (msg 24049), which widens this cell to
     CSL's reason: the old "keeps its text byte for byte" clause is withdrawn.** A helper
     `_unresolved_filing_sentence(security_key, source_object)` builds the reason BY RULE from the source object's
     own `battery.attempts`, never per name: *"No filing could be matched to {root}: {step 1}; {step 2}; ...; and
     {step N}."* where `{root}` is the security key's `_<EXCH>_Equity` prefix (`CSL_AU_Equity -> CSL`; any other
     key shape -> `this company`) and each step phrase comes from ONE route table keyed on `attempt.route`, the
     outcome read from that attempt's own `reason`/`http_status`/`seed_sources` (L5 wording, named for the CTO):
     - `edgar-ticker`: reason contains "name guard REFUSED" -> `the SEC ticker belongs to a different company`;
       else `the SEC ticker lookup found no matching company`.
     - `edgar-bloomberg-cik`: reason contains "no 10-K" -> `the company files no recent 10-K with the SEC`;
       reason names no CIK/key -> `Bloomberg carries no SEC identifier for the company`; else `the SEC lookup by
       Bloomberg's identifier found no usable annual report`.
     - `esef-lei`: HTTP 404 or "not held" -> `no European (ESEF) annual report is filed under its LEI`; no LEI ->
       `no LEI is on record to look up a European (ESEF) filing`; else `the European (ESEF) lookup found no usable
       annual report`.
     - `company-site`: the seeds from `seed_sources`, each through ONE label table (`bloomberg-web-address` ->
       `the company website`, `edgar-website` -> `the website the SEC lists`, `exchange-listing-page` -> `the
       {exchange name} listing page`, exchange names `{AU: ASX, JP: Tokyo Stock Exchange, LN: London Stock
       Exchange}` else `exchange`); two or more seeds -> `neither A nor B led to an annual report`, one seed -> `A
       did not lead to an annual report`, none -> `no company website was on record to search`; plus ` within the
       crawl limit` when the reason says the crawl bound was reached.
     - `national-regulator`: `there is no national-regulator source for this listing yet`.
     - any other route: `the {route, hyphens as spaces} step found no annual report`.
     No battery attempts (the 178 pre-battery objects): *"No filing could be matched to {root}; the filing
     search's own notes are kept as the evidence."* (the evidence field carries the object's reason). No sentence
     ever contains a literal missing value. **For CSL, measured by the prototype on the CURRENT filings object:**
     *"No filing could be matched to CSL: the SEC ticker belongs to a different company; the company files no recent
     10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the company website nor the
     ASX listing page led to an annual report within the crawl limit; and there is no national-regulator source for
     this listing yet."* (L5 wording, named for the CTO.)
   - The approved no-reason sentence (*"The filing search did not resolve a filing for this name, and it recorded no
     reason."*) is RETIRED by 1b: an UNRESOLVED object with neither attempts nor a reason takes 1b's no-attempts
     sentence, which claims no reason exists only as "the filing search's own notes" -- never a false "none".
   `build_roster` uses both helpers, so a future live build writes the same sentences as these re-derivations.
2. **The JP-President rule**, in ONE place: `enrich.listing_exchange(security_key)` returns the `_<EXCH>_Equity` suffix
   (`"6861_JP_Equity" -> "JP"`, `"BP/_LN_Equity" -> "LN"`, `"CAT_US_Equity" -> "US"`, anything else `None`), and
   `enrich.find_ceo(officers, exchange=None)` keeps today's rule first (the first officer matching `_CEO_RE`) and ONLY
   when none matches AND `exchange == "JP"` returns the first officer whose role, case-folded and whitespace-collapsed,
   EQUALS `"president"` or `"representative director and president"`. Nothing else ("Vice President", "Senior
   Executive Vice President", any non-JP exchange) is read as CEO. `build_document` passes
   `exchange=listing_exchange(security_key)`.
3. **Readable searched reasons (`ceo_search.project_ceo_public_profile`).** The `NOT_SEARCHED` table is UNCHANGED. For
   every OTHER status the composed `"%s / %s -- ..."` basis is replaced by ONE rule table of sentences (L5 wording),
   where `n` = `search.results_returned` (0 when absent), `k` = number of kept items, `v` =
   `counts.facts_verified`, `a` = number of SERP attempts, `kind` = the failure kind:
   - `CURATED`: *"The CEO web search returned {n} url(s); {k} page(s) about the CEO were kept, with {v} fact(s)
     checked word for word against the page."*
   - `NOTHING_FOUND / ORIGINAL_EMPTY`: *"The CEO web search returned {n} url(s), but none matched the exact name."*
   - `NOTHING_FOUND / NO_RESULT_ABOUT_PERSON`: *"The CEO web search returned {n} url(s), none of them about the CEO."*
   - `UNREADABLE / NO_PAGE_READABLE`: *"The CEO web search returned {n} url(s) about the CEO, but no page could be read
     and checked."*
   - `SEARCH_FAILED / *`: *"the SERP primitive raised: the CEO web search did not complete ({kind} failure, {a}
     attempt(s))."* -- this sentence BEGINS with the adapter's own served failure signal
     (`scoped_amgt._SERP_PRIMITIVE_RAISED_PREFIX = "the SERP primitive raised"`, `:2384`, read at `:2442`), so a failed
     search serves as `SEARCH_FAILED` and never as "links unreadable" (the contract's "recorded as FAILED, with its
     cause"). Every other sentence carries `"returned {n} url"`, which the adapter's `_SERP_URL_COUNT_RE`
     (`:2385`) reads into `urls_returned`.
   A missing number is printed as `0`, a missing kind as `unknown`, a missing name never appears. No sentence ever
   contains the literal `None`. `reason_code` still travels in its own field. **This supersedes AMGT-rk-75's arm
   `DiscriminatingStatusTest.test_other_statuses_keep_their_basis_byte_for_byte`** (`test_reproject_public_profile.py`
   `:198-231`), which pinned the OLD composed basis for the four searched statuses: amend THAT ONE ARM so it asserts the
   new sentence for each searched status against the same pinned module (`83da68c00a`), keeping its NOT_SEARCHED
   half unchanged. No other existing test is edited. Live census: 0 of 15 stored objects carry a searched status, so
   no served text moves except 6861's.
4. **ONE mode, `enrich.py --research-stored-ceo`**, the ONLY path AC5 runs (AC6 and AC7 run RULED item 4b's mode). `research_stored_ceo(args,
   client=None, serp=None, model=None, fetcher=None)`:
   - GETs the EXISTING `management/v1/<key>/<as_of>.json` (missing -> exit 1, nothing written) and the filings source
     object through `roster.load_source_object(security_key, client=...)` (a READ; `pick_source_key` picks
     `doc-1defdb68a7ffd3b7` for 6861). **Refuses (exit 1, nothing searched, nothing written)** when the source object's
     `accession` differs from the stored `source_accession`, or when the stored `ceo_profile.search.query` is already
     set (ONE search, never a repeat).
   - Re-derives `roster_reason` through RULED item 1's helper and `absence_reason_evidence` through
     `classify_roster_absence` (the class stays `pull-missed`). **`officers`, `fallback`, `roster_status`,
     `roster_source`, `source_accession`, `source_key`, `source_item`, `lusha_enrichment` and every other top-level key
     are left byte-equal.** It never calls `build_roster`, `build_document`, `apply_bloomberg_fallback`,
     `bloomberg_fallback.*`, `prospecting_page`, `_lusha_client`, `compute_pool` or `write_pool_object`.
   - Runs `ceo_search.ceo_profile(find_ceo(stored officers, exchange=listing_exchange(key)), stored
     ceo_profile.company, verified_domain_for(source_object), serp=<the SERP module, resolved only when the key is in
     the environment>, roster_source=stored roster_source, model=model, fetcher=fetcher)` ONCE, then
     `project_ceo_public_profile`.
   - **Hard caps, checked BEFORE the write:** `cost.serp_requests <= 3` and `cost.model_usd <= 1.00`; either exceeded
     -> BLOCKED, nothing written.
   - Validates (`enrich.validate`; a failure is exit 1, nothing written), prints one `CHANGED:` line per changed
     top-level key, one `SEARCH:` line (status, reason_code, ceo_name, serp_requests, fetches, model_usd), one
     `SKIP-POOL:` line, and writes through `write_document` ONLY with `--write-pool` -- exactly ONE conditional put.
4b. **ONE second mode, `enrich.py --rederive-roster-reason`**, the ONLY path AC6 (CSL) and AC7 (CAT) run, NO search
   and NO secret. It re-derives from STORED objects only.
   `rederive_roster_reason(args, client=None)`: GETs the EXISTING `management/v1/<key>/<as_of>.json` (missing -> exit
   1) and the CURRENT filings source object through `roster.load_source_object(security_key, client=...)`;
   It re-runs `build_roster` on the source object for its REASON FIELDS ONLY, applies RULED item 7's guard, and may
   change ONLY `roster_status` (and only `RESOLVED -> INCOMPLETE-NO-CEO`), `roster_reason`, `section_refers_to`,
   `absence_reason_class` and `absence_reason_evidence`; EVERY other top-level key stays byte-equal -- `officers`,
   `fallback`, `roster_source`, `ceo_profile`, `ceo_public_profile`, `generated_at` included. **Refuses (exit 1,
   nothing written)** when the re-derived officers would differ from the stored ones on a FILING roster, when a
   BLOOMBERG_FALLBACK roster's `roster_status` would change, when a `roster_status` would change to anything but
   `INCOMPLETE-NO-CEO`, or when the source object's accession differs from the stored `source_accession` (for an
   UNRESOLVED source, the placeholder key). For CSL, measured: only `roster_reason` (1b) and `absence_reason_evidence`
   (current filings reason, class `pull-missed` unchanged) move. For CAT, measured: `roster_status RESOLVED ->
   INCOMPLETE-NO-CEO`, `roster_reason None -> the Item 1D sentence`, `section_refers_to None -> "Information required
   by this Item appears in Item 1D of this Form 10-K."`, `absence_reason_class None -> pull-missed`,
   `absence_reason_evidence None -> the Item 1D sentence`; officers byte-equal. It never calls
   `ceo_search.*`, `build_roster`, `build_document`, `apply_bloomberg_fallback`, `bloomberg_fallback.*`,
   `prospecting_page`, `_lusha_client`, `compute_pool` or `write_pool_object`. Validates, prints one `CHANGED:` line
   per changed key and one `SKIP-POOL:` line, and writes through `write_document` ONLY with `--write-pool` -- exactly
   ONE conditional put.
5. **Tests**, a NEW file `lib/research/management/tests/test_jp_president_and_readable_reasons.py`, offline (stub S3,
   stub serp/model/fetcher), ELEVEN arms whose names match AC2:
   - `test_jp_president_is_ceo_when_no_chief_executive_title` -- `President` and `Representative Director and
     President` on a JP roster; a JP roster that also carries a CEO-titled officer returns the CEO-titled one.
   - `test_president_is_not_ceo_outside_jp_or_when_qualified` -- `exchange "US"` and `None` return `None`; JP
     `"Vice President"` and `"Senior Executive Vice President"` return `None`.
   - `test_listing_exchange_reads_the_key_suffix` -- the four cases in RULED item 2.
   - `test_empty_section_and_unresolved_reasons_never_print_none` -- `build_roster` on a RESOLVED source with `form
     None`, `family "YUHO"`, empty section -> the 6861 sentence exactly, no `None`, no accession in the text,
     `source_accession` set; an UNRESOLVED source with no attempts and no reason -> 1b's no-attempts sentence, no
     `None`.
   - `test_unresolved_reason_is_built_from_the_attempts` -- a stub UNRESOLVED object carrying CSL's five measured
     attempts (routes, reasons, http_status, seed_sources copied into the test as literals) -> the CSL sentence in
     RULED item 1b EXACTLY; a one-seed `company-site` attempt -> "... did not lead to an annual report"; an unknown
     route -> the generic phrase; no sentence contains `None`, a URL or a `seeds=[` fragment.
   - `test_rederive_roster_reason_writes_once_and_touches_two_fields` -- stub S3 holding a CSL-shaped stored object
     and the current source object; `ceo_search.ceo_profile`, `build_roster`, `build_document`,
     `apply_bloomberg_fallback`, `prospecting_page`, `_lusha_client`, `compute_pool` and `write_pool_object`
     patched to RAISE; exactly ONE `put_object`, on the management key; the written object differs from the stored
     one ONLY at `roster_reason` and `absence_reason_evidence`; plus the three refusals (stored roster RESOLVED,
     source RESOLVED, a class change) each write NOTHING. (It also covers the CAT shape below: exactly one put, and only
     the five reason fields move.)
   - `test_exec_officer_pointer_marks_roster_incomplete` -- a CAT-shaped RESOLVED source (Item 10 with the measured
     pointer sentence and one stray officer row, no Item 1D held) -> `INCOMPLETE-NO-CEO`, the officer KEPT,
     `section_refers_to` the pointer sentence verbatim, the Item 1D sentence exactly; the SAME section with an Item 1D
     cut held in `excerpt.items` and a CEO row in it -> parsed from Item 1D, `RESOLVED` with that CEO (branch A);
     NEGATIVE CONTROL: a BA-shaped Item 10 (directors incorporated by reference, officers listed inline with a CEO) ->
     `RESOLVED`, unchanged, no pointer.
   - `test_resolved_roster_without_ceo_is_incomplete` -- a RESOLVED roster of two non-CEO officers and no pointer ->
     `INCOMPLETE-NO-CEO` with the no-pointer sentence; a JP roster with a sole `President` -> stays `RESOLVED` (the
     v0.16 JP rule finds the CEO); a US roster with a CEO -> unchanged; `enrich.validate` accepts
     `INCOMPLETE-NO-CEO` and still rejects an unknown value.
   - `test_searched_basis_is_a_readable_sentence_the_adapter_reads` -- for each of the five searched rows: no `None`
     in `basis`; `scoped_amgt.ceo_profile_reading` maps CURATED -> `CONFIRMED`, NOTHING_FOUND ->
     `SEARCHED_NOTHING_FOUND`, UNREADABLE -> `SEARCHED_LINKS_UNREADABLE`, SEARCH_FAILED -> `SEARCH_FAILED`; and
     `urls_returned == n` on the four non-failure rows.
   - `test_research_stored_ceo_writes_once_and_never_rebuilds` -- stub S3 holding the stored object and the source
     object; `build_roster`, `build_document`, `apply_bloomberg_fallback`, `prospecting_page`, `_lusha_client`,
     `compute_pool` and `write_pool_object` patched to RAISE; exactly ONE `put_object`, on the management key; the
     written object differs from the stored one ONLY at `roster_reason`, `absence_reason_evidence`, `ceo_profile`,
     `ceo_public_profile`; plus the three refusals (accession mismatch, stored query already set, a stub search
     reporting 4 SERP attempts) each write NOTHING.
   - `test_pinned_copy_withholds_president_and_prints_none` -- the DISCRIMINATING arm: `roster.py` and `enrich.py`
     loaded from the PINNED pre-change commit `1be0b89406b56282a260b9bc00cfa4f5034d8c20` (the last commit to touch
     `roster.py`, `ceo_search.py`, `enrich.py` and `test_reproject_public_profile.py` at the cut -- never HEAD, never a
     merge-base, row Z-S193): its `find_ceo` returns `None` on the JP President roster, its `build_roster` prints
     `"the persisted None filing"` on the same source object, and on the CSL-shaped UNRESOLVED object it prints
     `"the persisted filing is itself UNRESOLVED-SOURCE: "` + the raw reason (with its `seeds=[` fragment), and on the
     CAT-shaped section it returns `RESOLVED` with the one stray officer and no reason.

6. **`roster.py`, the executive-officer pointer (ruling (a)).** ONE compiled pattern `_EXEC_OFFICER_POINTER`: a
   sentence naming `executive officers` followed, within 160 characters and the same sentence, by `appears in` /
   `included in` / `included under` / `set forth in` / `set forth under` / `see` and then `Part I` or `Item <n><letter>`.
   `build_roster` checks the section text for it BEFORE accepting a parse: when it fires, `section_refers_to` is set
   to that pointer sentence VERBATIM (the existing field) and the named label is looked up in the source object's
   held text (`officer_section` and `excerpt.items`); if the named section IS held, it is parsed as the officer
   section instead (branch A); if it is NOT held (branch B -- CAT, measured), the roster keeps whatever officers the
   cut section yielded and is handed to RULED item 7 with the pointer attached. The generic
   `_find_reference_pointer` and its 0-candidate path are UNCHANGED.
7. **The no-CEO guard (ruling (b)) and ONE new status value (ruling (c)).** `roster.ROSTER_INCOMPLETE =
   "INCOMPLETE-NO-CEO"`, added to `management.schema.json`'s `roster_status` enum (one value; the description gains
   one sentence). `enrich.completeness_guard(document, security_key)`, called in `build_document` after the roster and
   in RULED item 4b: a document whose `roster_status` is `RESOLVED`, whose officers are non-empty and for which
   `find_ceo(officers, exchange=listing_exchange(security_key))` is `None` becomes `roster_status INCOMPLETE-NO-CEO`
   with `roster_reason` a readable sentence (L5 wording): with an executive-officer pointer from item 6 --
   *"The {form} lists its executive officers in {Item/Part label}, which was not read, so this roster is
   incomplete."* (for CAT, measured: *"The 10-K lists its executive officers in Item 1D, which was not read, so this
   roster is incomplete."*, the CTO's own words plus the closing clause); without one -- *"The filing's roster names
   no chief executive, so this roster is incomplete."* Officers are KEPT (they are real officers from the filing).
   `absence_reason_class` / `absence_reason_evidence` come from the existing `classify_roster_absence` (a RESOLVED
   source -> `pull-missed`, evidence = the new reason). Served by the DEPLOYED adapter as ABSENT /
   `ROSTER_UNRESOLVED_NO_FALLBACK` / `roster_status INCOMPLETE-NO-CEO` / the sentence / the real `officer_count` --
   never RESOLVED with no CEO (ruling s.4). A roster WITH a CEO is untouched.

**What this cell does NOT change:** the adapter; the portal; `management.schema.json` beyond the ONE `roster_status` value RULED item 7 adds (every
status and reason code the search can produce is already in its enums -- `ceo_profile_block.status` and
`.reason_code`, measured); any security's object other than 6861's, CSL's and CAT's; any CSL field other than
`roster_reason` and `absence_reason_evidence`; any CAT field other than the five RULED item 4b names; CAT's
`officers`; any fetch (the EDGAR fetch of CAT's 10-K is carded to Andrew, not this cell's); the
NOT_SEARCHED sentence table; `_CEO_RE`; the pool.
**NAMED DEBT, not covered (ruling 2, msg 24049):** the SEARCH_FAILED sentence keeps the jargon prefix "the SERP
primitive raised" because the adapter keys its failure reading on it; *"the next adapter redeploy moves
ceo_profile_reading to key on the reason_code field rk-75 added, and the prefix goes."*
**CONTEXT ONLY, NOT SCOPE:** two open rows touch the same page and are NOT this cell's -- `AMGT_RESAPP-Z-S201`
(the Exec Management tab prints a double full stop after every not-searched CEO line, and a "from the filing"
subtitle over a Bloomberg table: portal-side) and `AMGT_RESAPP-Z-S202` (CAT's roster misses its Item 1D officers) -- **Z-S202 is now IN this cell (folded, ruling
s.2)**; only Z-S201 stays out (portal, `AMGT-rk-80`, cut in the same slug). **NO portal change is in this cell.**

## 2. WHERE THIS CAME FROM

**ROUND 20**, decomposition s.28 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s msgs 24036 (PRD v0.16 @2d0da569e7,
round 20 = ONE cell on ONE key) and 24039 (the Keyence search added under Andrew's word), and the round-19 L10.
msg 24049 (the five calls ruled, the CSL second write added), msg 24055 (S202 pre-ruled) and msg 24058 (the S202 fold,
the no-fetch / census / no-redeploy rulings, `ROUND_ANALYSIS.round19.md`). Rows `AMGT_RESAPP-Z-S195` (the finding) / `Z-S196`
(its disarm against the ruling), `Z-S197` (OPEN; `Z-S198`'s disarm of it is VOID under `Z-S199`), `Z-S200` (CSL) and `Z-S202` (CAT, ARMED).
Andrew-direct ~16:5xZ (record @c5532df80a: *"the major work here is getting a functional product live and ready for
review for the managers"*) sets the priority; ~15:12Z (record @1e2a54bf0f) the one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/roster.py
lib/research/management/ceo_search.py
lib/research/management/enrich.py
lib/research/management/management.schema.json
lib/research/management/tests/test_jp_president_and_readable_reasons.py
lib/research/management/tests/test_reproject_public_profile.py
lib/research/management/tests/test_management.py
lib/research/management/tests/test_bloomberg_fallback.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~79/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`scoped_amgt.py`, `bloomberg_fallback.py`,
  `crosswalk.py`, `data/find/dualbiz/scripts/serp.py`, the other management tests, the pair
  files, the word record). Scratch is `<your worktree>/.scratch/` only (never committed). In
  `test_reproject_public_profile.py` you may edit ONLY the one arm RULED item 3 names; every other existing test is a
  WALL: if one breaks, that is a finding (row), not an edit.
- **Collision check, done at the cut (names only):** no other open order writes `lib/research/management/`; round 19's
  cells are drained (`AMGT-rk-75..78`; rk-78's portal branch awaits its DEV push and touches no workspace path here). The held branch `wk-amgt-14-50` changes
  `lib/research/management/{domains.json,enrich.py,management.schema.json,tests/test_lusha_domain.py}` by NAME --
  **`enrich.py` is a shared name with that held branch.** It is not merged and is never read here.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~79 <0.9.0_WK_AMGT_RESAPP~79@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**VENDOR EGRESS, EXACTLY ONE SEARCH (Andrew's word, one name, one search, no repeat):** in AC5 only, ONE
`ceo_search.ceo_profile` call for `6861_JP_Equity`'s stored officer Tetsuya Nakano, reaching: Bright Data
(`serp_opal`) for **at most 3 SERP requests** (one request plus the code's own captcha/5xx retries -- never a retry you
add); **at most 3** result-page GETs to the hosts the search returns (LinkedIn never fetched); and Anthropic
(`claude-opus-5`) for **at most 4 calls and at most US$1.00** (worst case read from the code, about US$0.35). Secrets:
`find-insure/bright-data/api-key` as `BRIGHT_DATA_API_KEY`, `BD_SERP_ZONE=serp_opal`, `anthropic-api-key` as
`ANTHROPIC_API_KEY`, each ONLY via `comp-secrets get <secret> --reveal --value-only` with the empty-key guard AC5
carries; `LUSHA_API_KEY` UNSET (`env -u`). **No other name, no second search, no schedule, no Lusha, no Bloomberg call
(never `--bloomberg`, `blp_client`, any MCP Bloomberg tool, or `enrich.main` without `--research-stored-ceo`), no
roster rebuild.**
**THE LIVE WRITE (AC5) IS SERVED-PLANE AND RUNS ONLY UNDER A NEVER-WIDEN PAIR.** Both
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND20_RK79_COO_HALF.md` and `..._CTO_HALF.md` must exist at
your spawn, each with a heading naming `AMGT-rk-79` and signed. Its blast radius is EXACTLY THREE keys -- the census's literal list, 3 of 15: (a)
`s3://opal-data-harvest/management/v1/6861_JP_Equity/2026-09-19.json`, one new version, differing from the pre-act
version ONLY at `roster_reason`, `absence_reason_evidence`, `ceo_profile` and `ceo_public_profile` (AC5); (b)
`s3://opal-data-harvest/management/v1/CSL_AU_Equity/2026-09-19.json`, one new version, differing ONLY at
`roster_reason` and `absence_reason_evidence` (AC6, no search); (c)
`s3://opal-data-harvest/management/v1/CAT_US_Equity/2026-09-19.json`, one new version, differing ONLY at
`roster_status`, `roster_reason`, `section_refers_to`, `absence_reason_class` and `absence_reason_evidence` (AC7, no
search, no fetch). **The as-of is PINNED to `2026-09-19` for all three; a run dated today would CREATE a new key no
half covers.** Zero `raw/bloomberg/` writes, zero `_pool/` writes, zero `filings/` writes, zero writes to any other
management key, zero vendor calls on CSL or CAT, zero EDGAR fetches.
**THE STOP RULE:** if AC3 reads the 6861 latest VersionId other than `1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G`, a stored
`ceo_profile.search.query` already set, `cost.serp_requests` other than 0, a source-object accession other than
the stored `source_accession`, the CSL latest VersionId other than `u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS`, or the CSL
filings latest VersionId other than `GzAiBH5LVctrkT8atzKoSYbZnwtVZ4_9`, the CAT latest VersionId other than
`tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU`, the CAT filings latest VersionId other than `G8qBiPSVoZvsUCQ6_M92Gyp3_8K3ov6O`,
or a census (RESOLVED rosters with no CEO, all 15 names) other than exactly `[CAT_US_Equity]`, STOP before AC4 with a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`). If AC3 reads NO
`verified_site` on the source object, the act still runs: the search then returns `NOT_SEARCHED / NO_VERIFIED_SITE`
with `ceo_name "Tetsuya Nakano"` and spends NOTHING -- the second sanctioned branch; say which branch occurred.
PORTAL FROZEN. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No
non-ASCII in anything you write. **PUSH: never** (LD-0522). **Never delete an S3 object** (a rollback is `copy_object`
from the pre-act VersionId).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by a plain enrich re-run,
never by a second search, never by a search on CSL or CAT, never by an EDGAR fetch, never by editing a WALL, never by a different as-of.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure both suite baselines (84 / 191) before you
edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W79-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; a `DISMISSED_WITH_REASON` row carries a
`dismissal_reason`. The dispositions of Z-S195..Z-S198 are the CVO's L9 act, not yours.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC3, AC5 and AC8, which run under timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import hashlib, io, os, re
d = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/"
print("word_record_at_HEAD", os.path.exists("org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_195xZ_AMGT_RESAPP_KEYENCE_SEARCH_YES_LUSHA_R20_YES.md"))
for half in ("NEVER_WIDEN_ROUND20_RK79_COO_HALF.md", "NEVER_WIDEN_ROUND20_RK79_CTO_HALF.md"):
    p = d + half
    if not os.path.exists(p):
        print(half, "ABSENT"); continue
    b = io.open(p, "rb").read(); t = b.decode("utf-8", "replace")
    heads = [l for l in t.splitlines() if l.startswith("#") and "AMGT-rk-79" in l]
    keys = [k for k in ("management/v1/6861_JP_Equity/2026-09-19.json", "management/v1/CSL_AU_Equity/2026-09-19.json", "management/v1/CAT_US_Equity/2026-09-19.json") if k in t]
    print(half, "sha256", hashlib.sha256(b).hexdigest(), "rk79_headings", len(heads), "names_keys", len(keys), "of 3", "mentions_rollback", len(re.findall(r"(?i)rollback", t)), "mentions_VersionId", len(re.findall(r"VersionId", t)), "names_serp_cap", len(re.findall(r"3 SERP", t)), "signed", len(re.findall(r"(?im)^\*\*Signature[^\n]*signed `", t)))
'</invocation><expect>word_record_at_HEAD True; both halves present, each printing a 64-hex sha256, rk79_headings at least 1, names_keys 3 of 3 (the literal list: 6861, CSL, CAT), mentions_rollback at least 1, mentions_VersionId at least 1, names_serp_cap at least 1 and signed 1; an ABSENT half, 0 headings, names_keys below 3 or signed 0 REFUSES this criterion and STOPS the order before AC3</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -2 && python -m pytest lib/research/management/tests/test_jp_president_and_readable_reasons.py -v -p no:cacheprovider 2>&1 | tail -16 && python -m pytest lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -2</invocation><expect>the management suite's final line reads "95 passed" (the 84 at the cut plus this cell's 11 new arms; the amended rk-75 arm is the same test, not a new one) and 0 failed -- re-measure the baseline at spawn and the bar is "baseline plus 11, failures 0"; the new file shows 11 PASSED lines naming test_jp_president_is_ceo_when_no_chief_executive_title, test_president_is_not_ceo_outside_jp_or_when_qualified, test_listing_exchange_reads_the_key_suffix, test_empty_section_and_unresolved_reasons_never_print_none, test_unresolved_reason_is_built_from_the_attempts, test_searched_basis_is_a_readable_sentence_the_adapter_reads, test_research_stored_ceo_writes_once_and_never_rebuilds, test_rederive_roster_reason_writes_once_and_touches_two_fields, test_exec_officer_pointer_marks_roster_incomplete, test_resolved_roster_without_ceo_is_incomplete and test_pinned_copy_withholds_president_and_prints_none; the api suite reads "191 passed" UNCHANGED, 0 failed (no adapter file is edited)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/rk79_pre && python -c '
import boto3, hashlib, json, re
from lib.research.management import enrich
s3 = boto3.client("s3", region_name="us-east-1"); lam = boto3.client("lambda", region_name="us-east-1"); B = "opal-data-harvest"
EXP = {"6861_JP_Equity": "1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G", "CSL_AU_Equity": "u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS", "CAT_US_Equity": "tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU"}
FEXP = {"filings/v1/CSL_AU_Equity/UNRESOLVED-SOURCE.source.json": "GzAiBH5LVctrkT8atzKoSYbZnwtVZ4_9", "filings/v1/CAT_US_Equity/000001823026000008.source.json": "G8qBiPSVoZvsUCQ6_M92Gyp3_8K3ov6O", "filings/v1/6861_JP_Equity/doc-1defdb68a7ffd3b7.source.json": None}
for k, want in EXP.items():
    K = "management/v1/%s/2026-09-19.json" % k
    v = s3.list_object_versions(Bucket=B, Prefix="management/v1/%s/" % k); vs = v.get("Versions", [])
    latest = [x for x in vs if x["IsLatest"]][0]; body = s3.get_object(Bucket=B, Key=K)["Body"].read(); d = json.loads(body)
    open(".scratch/rk79_pre/%s.json" % k, "wb").write(body)
    print("PRE", k, "versions", len(vs), "delete_markers", len(v.get("DeleteMarkers", [])), "latest", latest["VersionId"], "equals_issuer", latest["VersionId"] == want, "sha256", hashlib.sha256(body).hexdigest())
    print("   roster_status", d.get("roster_status"), "roster_source", d.get("roster_source"), "officers", len(d.get("officers") or []), "section_refers_to", d.get("section_refers_to"), "class", d.get("absence_reason_class"), "reason_has_None", bool(re.search(r"\bNone\b", d.get("roster_reason") or "")))
for fk, want in FEXP.items():
    fv = [x for x in s3.list_object_versions(Bucket=B, Prefix=fk).get("Versions", []) if x["Key"] == fk and x["IsLatest"]]
    print("FILING", fk.split("/")[2], "latest", fv[0]["VersionId"] if fv else None, "equals_issuer", (fv[0]["VersionId"] == want) if (fv and want) else "n/a")
d6 = json.load(open(".scratch/rk79_pre/6861_JP_Equity.json", encoding="utf-8")); cp = d6.get("ceo_profile") or {}
print("6861 ceo", cp.get("status"), cp.get("reason_code"), "query", (cp.get("search") or {}).get("query"), "serp_requests", (cp.get("cost") or {}).get("serp_requests"))
names = sorted(c["Prefix"].split("/")[2] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/", Delimiter="/") for c in pg.get("CommonPrefixes", []) if not c["Prefix"].endswith("_pool/"))
census = []
for n in names:
    mk = sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/%s/" % n) for o in pg.get("Contents", []))[-1]
    d = json.loads(s3.get_object(Bucket=B, Key=mk)["Body"].read()); offs = d.get("officers") or []
    if d.get("roster_status") == "RESOLVED" and offs and enrich.find_ceo(offs, exchange=enrich.listing_exchange(n)) is None:
        census.append(n)
print("CENSUS RESOLVED-without-CEO", len(census), "of", len(names), census)
cnt = lambda p: sum(1 for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
print("RAW", {k: cnt("raw/bloomberg/%s/" % k) for k in EXP}, "MANAGEMENT_OBJECTS", cnt("management/v1/"), "FILINGS_OBJECTS", cnt("filings/v1/"))
pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]
print("POOL objects", len(pool), "etag", sorted(pool, key=lambda o: o["Key"])[-1]["ETag"])
served = {}
for n in names:
    ev = {"rawPath": "/api/scoped/amgt/security/%s/thesis" % n, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    b = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    m = (json.loads(b["body"]) if isinstance(b.get("body"), str) else {}).get("management") or {}
    served[n] = hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest()
    print("SERVED", n, b.get("statusCode"), m.get("management_status"), m.get("absent_because"), m.get("roster_status"), m.get("officer_count"), served[n][:12])
json.dump(served, open(".scratch/rk79_pre/served.json", "w"))
print("CODE", lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")["CodeSha256"])
'</invocation><expect>This criterion runs AFTER your code edits (it imports your enrich.find_ceo(exchange=) and enrich.listing_exchange) and BEFORE AC4. MEASURED AT THE CUT: PRE 6861_JP_Equity versions 3 delete_markers 0 latest 1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G equals_issuer True sha256 29e6a8732a26723a7aa0482388e32a9cb9f9a8c29167a583dd7827d4d72c349e (UNRESOLVED-SOURCE, BLOOMBERG_FALLBACK, 1 officer, reason_has_None True); PRE CSL_AU_Equity versions 3 latest u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS equals_issuer True (UNRESOLVED-SOURCE, BLOOMBERG_FALLBACK, 14 officers, class pull-missed); PRE CAT_US_Equity versions 3 latest tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU equals_issuer True (RESOLVED, FILING, 1 officer, section_refers_to None, class None); FILING CSL_AU_Equity latest GzAiBH5LVctrkT8atzKoSYbZnwtVZ4_9 True, CAT_US_Equity G8qBiPSVoZvsUCQ6_M92Gyp3_8K3ov6O True, 6861 n/a; 6861 ceo NOT_SEARCHED NO_CEO_ON_ROSTER query None serp_requests 0; CENSUS RESOLVED-without-CEO 1 of 15 [CAT_US_Equity]; RAW CAT 12 CSL 14 6861 14; POOL objects 3 etag "7a1197377a0fff0e4e861ebc5208cf4a"; 15 SERVED lines, all 200, CAT SERVED None RESOLVED 1, CSL and 6861 SERVED BLOOMBERG_FALLBACK-shaped; CODE hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=. Pre-act bytes of the 3 keys and the 15 served hashes saved to .scratch/rk79_pre/ (the rollback baseline). ANY STOP-RULE value in section 4 differing -- a VersionId, a census other than exactly [CAT_US_Equity], a stored query, an accession, a moved CodeSha256 -- STOP, BLOCKING row, no live act</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py open --slug amgt-rk79-keyence-search-and-roster-reasons --title "AMGT-rk-79: one CEO web search for 6861_JP_Equity under Andrew's per-use word plus readable roster reasons; in-place rewrites of management/v1/{6861_JP_Equity,CSL_AU_Equity,CAT_US_Equity}/2026-09-19.json" --author 0.9.0_WK_AMGT_RESAPP~79 --leg "L1|verify|management/v1/6861_JP_Equity/2026-09-19.json|one new version, diff only roster_reason/absence_reason_evidence/ceo_profile/ceo_public_profile, SERP at most 3, model_usd at most 1.00" --leg "L2|verify|management/v1/CSL_AU_Equity/2026-09-19.json|one new version, diff only roster_reason/absence_reason_evidence, no vendor call" --leg "L3|verify|management/v1/CAT_US_Equity/2026-09-19.json|one new version, diff only roster_status/roster_reason/section_refers_to/absence_reason_class/absence_reason_evidence, officers byte-equal, no vendor call, no fetch"</invocation><expect>the ledger entry is OPENED with 3 legs and its sentinel lands in org/critical_paths/.open_deploys/ BEFORE any live act; the command prints the entry path; run only AFTER AC1 and AC3 pass, and BEFORE AC5</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && export BRIGHT_DATA_API_KEY="$(comp-secrets get find-insure/bright-data/api-key --reveal --value-only)" && export BD_SERP_ZONE=serp_opal && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" && [ -n "$BRIGHT_DATA_API_KEY" ] && [ -n "$ANTHROPIC_API_KEY" ] && env -u LUSHA_API_KEY python -m lib.research.management.enrich --research-stored-ceo --security-key 6861_JP_Equity --as-of 2026-09-19 --write-pool 2>&1 | tail -20</invocation><expect>the key-presence guard passes (both exports non-empty; --value-only returns the BARE value -- never the bare "$(comp-secrets get X --reveal)" idiom behind row W50-S4); CHANGED lines for exactly roster_reason, absence_reason_evidence, ceo_profile and ceo_public_profile and no other key; the roster_reason CHANGED line ends in "The Japanese annual securities report (Yuho) was found, but its officer section is empty, so no officers could be read from the filing."; one SEARCH line with ceo_name Tetsuya Nakano, serp_requests at most 3, fetches at most 3, model_usd at most 1.00, and a status of CURATED, NOTHING_FOUND, UNREADABLE or SEARCH_FAILED (the searched branch, expected -- verified_site www.keyence.co.jp at the cut) or NOT_SEARCHED with reason_code NO_VERIFIED_SITE and serp_requests 0 (only if the source object carries no verified_site at spawn); one SKIP-POOL line; exactly ONE "OK: uploaded s3://opal-data-harvest/management/v1/6861_JP_Equity/2026-09-19.json" line; no line mentioning Bloomberg, Lusha, a fallback pull or a pool write. A BLOCKED line (refusal, cap exceeded, validation failure) means nothing was written: record it, file a BLOCKING row, never re-run the search</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u BRIGHT_DATA_API_KEY -u ANTHROPIC_API_KEY -u LUSHA_API_KEY python -m lib.research.management.enrich --rederive-roster-reason --security-key CSL_AU_Equity --as-of 2026-09-19 --write-pool 2>&1 | tail -10</invocation><expect>no secret in the environment; CHANGED lines for exactly roster_reason and absence_reason_evidence and no other key; the roster_reason CHANGED line reads "No filing could be matched to CSL: the SEC ticker belongs to a different company; the company files no recent 10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the company website nor the ASX listing page led to an annual report within the crawl limit; and there is no national-regulator source for this listing yet." (measured by the issuer's prototype on the CURRENT filings object); the absence_reason_evidence CHANGED line carries the current filings reason naming both seeds (www.csl.com.au and www.asx.com.au); one SKIP-POOL line; exactly ONE "OK: uploaded s3://opal-data-harvest/management/v1/CSL_AU_Equity/2026-09-19.json" line; no SEARCH line and no line mentioning Bright Data, a SERP, Bloomberg, Lusha or a pool write. A refusal writes nothing: record it and file a BLOCKING row</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u BRIGHT_DATA_API_KEY -u ANTHROPIC_API_KEY -u LUSHA_API_KEY python -m lib.research.management.enrich --rederive-roster-reason --security-key CAT_US_Equity --as-of 2026-09-19 --write-pool 2>&1 | tail -10</invocation><expect>no secret in the environment; CHANGED lines for exactly roster_status, roster_reason, section_refers_to, absence_reason_class and absence_reason_evidence and no other key (officers NOT among them); roster_status RESOLVED -> INCOMPLETE-NO-CEO; roster_reason "The 10-K lists its executive officers in Item 1D, which was not read, so this roster is incomplete."; section_refers_to "Information required by this Item appears in Item 1D of this Form 10-K."; absence_reason_class pull-missed; one SKIP-POOL line; exactly ONE "OK: uploaded s3://opal-data-harvest/management/v1/CAT_US_Equity/2026-09-19.json" line; no SEARCH line, no fetch, and no line mentioning Bright Data, EDGAR, Bloomberg, Lusha or a pool write. A refusal writes nothing: record it and file a BLOCKING row</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, hashlib, json, re
from lib.research.management import enrich
s3 = boto3.client("s3", region_name="us-east-1"); lam = boto3.client("lambda", region_name="us-east-1"); B = "opal-data-harvest"
ALLOWED = {"6861_JP_Equity": ["absence_reason_evidence", "ceo_profile", "ceo_public_profile", "roster_reason"], "CSL_AU_Equity": ["absence_reason_evidence", "roster_reason"], "CAT_US_Equity": ["absence_reason_class", "absence_reason_evidence", "roster_reason", "roster_status", "section_refers_to"]}
nonefree = lambda s: not (isinstance(s, str) and re.search(r"\bNone\b", s))
for k, allowed in ALLOWED.items():
    K = "management/v1/%s/2026-09-19.json" % k
    pre = json.load(open(".scratch/rk79_pre/%s.json" % k, encoding="utf-8")); post = json.loads(s3.get_object(Bucket=B, Key=K)["Body"].read())
    v = s3.list_object_versions(Bucket=B, Prefix="management/v1/%s/" % k)
    changed = sorted(x for x in set(pre) | set(post) if pre.get(x) != post.get(x))
    ok, errors = enrich.validate(post)
    print("POST", k, "versions", len(v.get("Versions", [])), "delete_markers", len(v.get("DeleteMarkers", [])), "changed_top", changed, "equals_allowed", changed == allowed, "schema_valid", ok, "contact_fields", enrich.contact_fields_present(post), "officers_equal", pre.get("officers") == post.get("officers"))
    print("   roster_status", post.get("roster_status"), "| reason_none_free", nonefree(post.get("roster_reason")), "| roster_reason", post.get("roster_reason"))
cp = json.loads(s3.get_object(Bucket=B, Key="management/v1/6861_JP_Equity/2026-09-19.json")["Body"].read()).get("ceo_profile") or {}; cost = cp.get("cost") or {}
print("6861 ceo", cp.get("status"), cp.get("reason_code"), "ceo_name", cp.get("ceo_name"), "serp_requests", cost.get("serp_requests"), "fetches", cost.get("fetches"), "model_usd", cost.get("model_usd"))
names = sorted(c["Prefix"].split("/")[2] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/", Delimiter="/") for c in pg.get("CommonPrefixes", []) if not c["Prefix"].endswith("_pool/"))
census = []
for n in names:
    mk = sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/%s/" % n) for o in pg.get("Contents", []))[-1]
    d = json.loads(s3.get_object(Bucket=B, Key=mk)["Body"].read()); offs = d.get("officers") or []
    if d.get("roster_status") == "RESOLVED" and offs and enrich.find_ceo(offs, exchange=enrich.listing_exchange(n)) is None:
        census.append(n)
print("CENSUS_AFTER RESOLVED-without-CEO", len(census), "of", len(names), census)
cnt = lambda p: sum(1 for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
print("RAW", {k: cnt("raw/bloomberg/%s/" % k) for k in ALLOWED}, "MANAGEMENT_OBJECTS", cnt("management/v1/"), "FILINGS_OBJECTS", cnt("filings/v1/"))
pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]
print("POOL objects", len(pool), "etag", sorted(pool, key=lambda o: o["Key"])[-1]["ETag"])
served_pre = json.load(open(".scratch/rk79_pre/served.json")); same = []
for n in names:
    ev = {"rawPath": "/api/scoped/amgt/security/%s/thesis" % n, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    b = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    m = (json.loads(b["body"]) if isinstance(b.get("body"), str) else {}).get("management") or {}
    eq = hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest() == served_pre[n]
    if n in ALLOWED:
        rd = m.get("ceo_profile_reading") or {}
        print("SERVED", n, b.get("statusCode"), "equal_pre", eq, m.get("management_status"), m.get("absent_because"), "roster_status", m.get("roster_status"), "officer_count", m.get("officer_count"), "reason_none_free", nonefree(m.get("reason")) and nonefree(m.get("roster_reason")), "reading", rd.get("reading"), "reading_none_free", nonefree(str(rd.get("reason") or "")))
    elif eq:
        same.append(n)
print("SIBLINGS_UNCHANGED", len(same), "of", len(names) - len(ALLOWED), same)
' | tee .scratch/rk79_ac8.txt</invocation><expect>POST 6861_JP_Equity versions 4, changed_top [absence_reason_evidence, ceo_profile, ceo_public_profile, roster_reason] equals_allowed True, the Yuho sentence; POST CSL_AU_Equity versions 4, changed_top [absence_reason_evidence, roster_reason] equals_allowed True, roster_status UNRESOLVED-SOURCE, the "No filing could be matched to CSL: ..." sentence; POST CAT_US_Equity versions 4, changed_top [absence_reason_class, absence_reason_evidence, roster_reason, roster_status, section_refers_to] equals_allowed True, roster_status INCOMPLETE-NO-CEO, the Item 1D sentence; all three schema_valid True, contact_fields [], officers_equal True, reason_none_free True, delete_markers 0; 6861 ceo ceo_name Tetsuya Nakano, serp_requests at most 3, fetches at most 3, model_usd at most 1.00; CENSUS_AFTER 0 of 15 []; RAW and MANAGEMENT_OBJECTS/FILINGS_OBJECTS equal to AC3's; POOL objects 3 with the AC3 etag; SERVED 6861 200 equal_pre False SERVED (fallback) with reason_none_free True and a reading consistent with the status (CURATED -> CONFIRMED, NOTHING_FOUND -> SEARCHED_NOTHING_FOUND, UNREADABLE -> SEARCHED_LINKS_UNREADABLE, SEARCH_FAILED -> SEARCH_FAILED, NOT_SEARCHED -> NOT_SEARCHED) with reading_none_free True; SERVED CSL 200 equal_pre False SERVED reason_none_free True; SERVED CAT 200 equal_pre False ABSENT ROSTER_UNRESOLVED_NO_FALLBACK roster_status INCOMPLETE-NO-CEO officer_count 1 reason_none_free True -- never RESOLVED with no CEO; SIBLINGS_UNCHANGED 12 of 12. ROLLBACK TRIGGER (any one): equals_allowed False, officers_equal False, a moved sibling, a raw/pool/filings count change, schema_valid False, a contact field, a served literal None, CENSUS_AFTER not 0, or CAT served RESOLVED -- then copy_object each written key from its AC3 pre-act VersionId, read back its sha256 equal to AC3's, and file a BLOCKING row. Never delete a version</expect></criterion>
  <criterion id="AC9" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py close-leg --slug amgt-rk79-keyence-search-and-roster-reasons --leg-id L1 --proof "$(cat .scratch/rk79_ac8.txt)" && python .tools/deploy_ledger.py close-leg --slug amgt-rk79-keyence-search-and-roster-reasons --leg-id L2 --proof "$(cat .scratch/rk79_ac8.txt)" && python .tools/deploy_ledger.py close-leg --slug amgt-rk79-keyence-search-and-roster-reasons --leg-id L3 --proof "$(cat .scratch/rk79_ac8.txt)" && python .tools/deploy_ledger.py close --slug amgt-rk79-keyence-search-and-roster-reasons && python .tools/deploy_ledger.py check</invocation><expect>legs L1, L2 and L3 closed with AC8's read-back as proof, the entry CLOSED, and the check lists no open entry for amgt-rk79-keyence-search-and-roster-reasons (its sentinel removed); the closed entry is COMMITTED with the instance, never left staged. The check's own rc may be non-zero from OTHER projects' open entries: record which, and that none names this slug. On the rollback branch each leg closes with the rollback proof instead</expect></criterion>
  <criterion id="AC10" cell_refs="AMGT-rk-79"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, json, subprocess; P = "1be0b89406b56282a260b9bc00cfa4f5034d8c20"; [print(f, "parses", bool(json.loads(io.open(f, "rb").read().decode("utf-8")) if f.endswith(".json") else compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "| pinned_base", (lambda b: (len(b) - len(b.decode("utf-8"))) if b else "NEW")(subprocess.run(["git", "show", P + ":" + f], capture_output=True).stdout)) for f in ("lib/research/management/roster.py", "lib/research/management/ceo_search.py", "lib/research/management/enrich.py", "lib/research/management/management.schema.json", "lib/research/management/tests/test_reproject_public_profile.py", "lib/research/management/tests/test_jp_president_and_readable_reasons.py")]'</invocation><expect>all six files print parses True, crlf 0 and non_ascii_bytes 0; pinned_base 0 for the five existing files (read from the pinned pre-change commit, never assumed) and NEW for the new test file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
Never paste a secret value into the instance, the session log, a row or a commit message; AC5's exports are recorded as
the literal invocation text, which carries no value. Run order: AC1, AC2 (after your edits), AC3, AC4, AC5, AC6, AC7,
AC8, AC9, AC10.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~79/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8,AC9,AC10` (rc 0 is the verdict); flip the
order's status tag to complete; commit with `--only -- <paths>` (the closed ledger entry travels in this commit).
Report once: the suite counts before and after, which branch occurred (searched or not searched) with the search's
status, reason_code, serp_requests, fetches and model_usd, the before/after roster_reason and basis lines, 6861's
served reading, CSL's and CAT's before/after roster_reason and CAT's served class, the census before and after, the raw and pool counts before and after, whether rollback fired, and the ledger entry's open and
close.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/rk79/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES at the cut (`2.0.0_SA_COO~Z`):** the search's branch is decided by the live object, not by this order;
every branch ends in ONE write per key, three keys (the census's literal list, 3 of 15). Rulings of record: msg 24049
(five calls; CSL added) and msg 24058 (S202 folded; no fetch; census; no redeploy). L5 wordings NEW since msg 24049's
approval, named for the CTO before its half is signed: RULED item 1b (the UNRESOLVED-filing rule sentence and its
route table, which RETIRES the no-reason sentence 24049 approved) and RULED item 7 (the two INCOMPLETE-NO-CEO
sentences) and the status value `INCOMPLETE-NO-CEO` itself. The amended rk-75 arm is a declared supersession under PRD
v0.16's readable-reasons rule. The issuer pins `ROUND_ANALYSIS.round19.md`'s commit at the cut (uncommitted at the
draft). Not in scope and routed elsewhere: rendering CAT's new reason on the RESOLVED path is unnecessary (CAT serves
ABSENT, whose reason the page already prints); the portal text fixes are AMGT-rk-80's.

<status>pending</status>
<round>20</round>
<slot>~79</slot>
<fabric>site-z</fabric>
