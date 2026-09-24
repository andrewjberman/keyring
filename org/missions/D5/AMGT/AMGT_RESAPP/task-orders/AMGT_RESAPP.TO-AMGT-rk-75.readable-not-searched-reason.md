# AMGT_RESAPP task order -- `AMGT-rk-75` -- the NOT_SEARCHED CEO reason becomes a PLAIN-ENGLISH sentence from ONE rule table keyed by reason code, the status code moves to its OWN field (`ceo_public_profile.reason_code`), and the three validation names are re-projected in place from their stored `ceo_profile` -- no Bloomberg, Lusha or SERP call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-75</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~75</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and reads or writes no
  schedule; its one live act (AC5) is run once by hand for three named keys. It OPENS one deploy-ledger entry with
  .tools/deploy_ledger.py before that act and CLOSES it on the read-back (AC4 / AC7), as AMGT-rk-48 did for the same
  three keys.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, grant or Lambda is read or changed. The adapter
  (opal-amgt-scoped-api) is NOT redeployed: none of lib/research/management/ is in its packaged closure (0 of the 59
  paths AMGT-rk-74's AC3 enumerates), and it already serves ceo_public_profile whole (scoped_amgt.py:2562). The live
  write is three in-place object rewrites under management/v1/ in opal-data-harvest with the seat's existing
  credentials, exactly the keys AMGT-rk-48 wrote, and only under the never-widen pair named in section 4.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~75`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and every code path in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call
begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~75;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check
out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential. No secret is needed by this
order; none is read.

## 1. THE CELL, inlined in full -- `AMGT-rk-75` (round 19; row `AMGT_RESAPP-Z-S192`, the rk-48 as-landed pair)

**The ruling, verbatim (`ledger/NEVER_WIDEN_RK48_AS_LANDED_HALVES.md`, CTO half @1ed2e24638, COO half concurring
@0b71e7f5ab):** *"The degraded reason text is a real regression under Andrew's ~16:5xZ priority (a product ready for
managers). So retaining it comes with its remedy: a producer fix, cut as a round-19 cell ... the NOT_SEARCHED basis
keeps a READABLE sentence for the reader; the status code travels in its own field, never in the sentence; then the
three VALIDATION names are re-run under that cell's own pair ... It must land before the managers' review."*

**The round-19 ruling that shapes this order, verbatim (`ledger/ROUND_ANALYSIS.round18.md` s.4 @5f10ddf969, `:61-70`,
`1.0.0_SA_CTO~Z`, msg 24015):** *"CALL 1 -- R19-A: RULED re-projection, not a re-run. A plain `enrich --write-pool`
re-run would rebuild CSL's roster from the filings object `rk-72` just rewrote, make a LIVE Bloomberg call for CSL and
6861, and write new `raw/bloomberg/` stamps (`enrich.py:859-860`). That is the exact out-of-radius class Z-S192 caught
on `rk-48`. `--reproject-public-profile` replaces `ceo_public_profile` only (a readable basis plus a new `reason_code`
field): exactly 3 conditional puts, no vendor, roster or pool call, `ceo_profile` byte-equal (simulated on the 3 live
objects). It is a strict subset of the ruled re-run's writes and serves the whole ruled outcome. `management.schema.json`
gains `reason_code`. The pair covers the 3 management keys only. The reader sentence must be plain English: CSL's
stored reason uses internal terms ("verified_site ... filings battery") and becomes VISIBLE once R19-C serves its
roster. So the re-projection writes, for CSL: "No verified company website was found, so the CEO web search was not
run." The code stays in `reason_code`, never in the sentence."*

**THE MEASURED STATE, at HEAD `54066b102b` (SITEZ). RE-READ every line at your branch HEAD before editing:**
- **The writer of the degraded text is the PROJECTION, not the search.** `lib/research/management/ceo_search.py`
  (727 lines, non-ASCII byte delta 0, crlf 0), `project_ceo_public_profile` `:692-727`, builds `basis` at `:714-716`
  as `"%s / %s -- %d url(s), %d fact(s) verified of %d proposed" % (status, reason_code, ...)` for EVERY status. It
  is called at ONE production site, `enrich.py:640`, and in two test files (`test_management.py:248`,
  `test_bloomberg_fallback.py:186, :195`).
- **The stored `ceo_profile.reason` is NOT the reader sentence (the CTO's ruling above).** Each of the three
  as-landed objects carries `ceo_profile.status "NOT_SEARCHED"` with a `reason` written by the producer, not for a
  manager: CAT and 6861 -- `reason_code "NO_CEO_ON_ROSTER"`, `reason "no officer on the roster carries a
  chief-executive title"`; CSL -- `reason_code "NO_VERIFIED_SITE"`, `reason "no verified_site landed for this name
  (filings battery) -- never searched on a typed or guessed domain"` (internal terms). Each `ceo_profile.cost` reads
  `serp_requests 0`, `model_usd 0.0`, and `search.query null`. **`ceo_profile` is NOT changed by this order** -- the
  sentence lives in the PROJECTION only.
- **Which reason codes can travel with NOT_SEARCHED -- enumerated by SUBTRACTION, not recall.** Denominator: the 10
  `REASON_*` constants in `ceo_search.py:63-72` plus `None` = 11 values. Minus the 7 set only under another status:
  `VENDOR_FAILURE`, `CONFIG_FAILURE`, `TRANSPORT_FAILURE` (SEARCH_FAILED, `:540-544`); `ORIGINAL_EMPTY` (NOTHING_FOUND,
  `:547-551`); `NO_RESULT_ABOUT_PERSON` (NOTHING_FOUND, `:576-580`); `NO_PAGE_READABLE` (UNREADABLE, `:682-685`); `None`
  (CURATED, `:678-681`). **Remainder: 4** -- `NO_CEO_ON_ROSTER` (`:501-504`), `ROSTER_UNRESOLVED` (`:505-508`),
  `NO_VERIFIED_SITE` (`:512-516`), `STEP_NOT_CONFIGURED` (`:518-521`), the four early returns of `ceo_profile` before
  any search, while `status` still holds its `NOT_SEARCHED` default (`:487`). Measured by driving each branch offline
  (issuer, at HEAD `5f10ddf969`): 4 of 4 return `NOT_SEARCHED` with those codes. The ONE other producer of a
  NOT_SEARCHED block, `enrich.build_document`'s empty-roster literal (`enrich.py:621-639`), uses `NO_CEO_ON_ROSTER`,
  already in the 4. Both producers reach the projection through the SAME call, `enrich.py:640`.
- **The schema refuses a new key today.** `lib/research/management/management.schema.json` (446 lines, delta 0,
  crlf 0): `definitions.ceo_public_profile_block` has `additionalProperties: false` and properties `url, title,
  snippet, status, basis, ceo_name, query, ir_domain, absence_class` -- no `reason_code`. Measured by the issuer on a
  patched scratch copy: the fixed projection validates 0 of 3 under HEAD's schema and 3 of 3 once `reason_code
  {"type": ["string", "null"]}` is added (and the three as-landed objects stay valid under the patched schema, 3 of 3).
- **A plain re-run is the WRONG act (the census the rk-48 pair missed, row Z-S192).** `enrich.main` with
  `--write-pool` calls `build_document` (`enrich.py:570-654`), which (a) rebuilds the roster from the filings source
  object -- and CSL's was rewritten by `AMGT-rk-72` @c1fdd952e1; (b) calls `apply_bloomberg_fallback` for any
  unresolved roster -- CSL and 6861 -- which makes a LIVE Bloomberg `ReferenceDataRequest` and, because `write_raw =
  args.write_pool` (`:859-860`), puts a NEW `raw/bloomberg/<key>/<stamp>/exec_officers.json`
  (`bloomberg_fallback.py:147-180`); (c) calls Lusha when officers AND a declared domain exist (`:602`) -- all three
  read `SKIPPED`, no declared domain; (d) loads the SERP module when a key is in the environment. **This order
  therefore builds a RE-PROJECTION mode that calls none of them.**
- **What the adapter serves.** `scoped_amgt.ceo_profile_reading` (`:2388-...`, the URL-count regex at `:2374`, the
  NOT_SEARCHED branch `:2423-2428`) returns `reading NOT_SEARCHED`, `reason = basis` verbatim, `urls_returned` parsed
  from `returned (\d+) url` in the basis. `read_management` (`:2474-...`) serves `ceo_public_profile` and the reading
  ONLY for a RESOLVED roster with officers (`:2512-2530`); CSL and 6861 are `UNRESOLVED-SOURCE` and serve
  `management_status ABSENT / ZERO_OFFICERS` with no CEO reading. **So the served change is CAT's reason line (1 of 3
  names); CSL's and 6861's stored objects change but are not served by this route today.** Measured live on the
  thesis route: CAT reading `NOT_SEARCHED`, `urls_returned None`, reason `"NOT_SEARCHED / NO_CEO_ON_ROSTER -- 0 url(s),
  0 fact(s) verified of 0 proposed"`; CSL and 6861 `management_status ABSENT`, `absent_because ZERO_OFFICERS`.
- **Tests at the cut:** `lib/research/management/tests` `77 passed`; `lib/research/api/tests` `185 passed`.

**RULED, what you build:**
1. **`ceo_search.py`: ONE rule table, `NOT_SEARCHED_SENTENCES`**, a module-level dict keyed by reason code, with
   EXACTLY these 4 entries (the subtraction above), byte for byte:
   - `NO_VERIFIED_SITE` -> `"No verified company website was found, so the CEO web search was not run."` -- **the CTO's words, verbatim** (ruling above, `:69-70`).
   - `NO_CEO_ON_ROSTER` -> `"No officer on the roster has a chief-executive title, so the CEO web search was not run."` -- **`2.0.0_SA_COO~Z`'s L5 ruling**, the same register.
   - `ROSTER_UNRESOLVED` -> `"The roster lists a CEO without a usable name, so the CEO web search was not run."` -- `2.0.0_SA_COO~Z`'s L5 ruling.
   - `STEP_NOT_CONFIGURED` -> `"The CEO web search is not set up in this environment, so it was not run."` -- `2.0.0_SA_COO~Z`'s L5 ruling.
   **`project_ceo_public_profile`** then gains ONE field, `reason_code` (the profile's own `reason_code`, null when
   absent), on EVERY status, and for status `NOT_SEARCHED` ONLY sets `basis = NOT_SEARCHED_SENTENCES[reason_code]`.
   **THE NAMED FALLBACK RULE (a NOT_SEARCHED code the table does not carry, including `None`):** `basis` is the
   profile's stored `reason` when non-empty, else today's composed string -- never a crash and never an empty basis.
   No such code is emitted today (4 of 4 covered); the rule exists so a future code degrades to the old behaviour,
   and AC2's enumeration arm fails the day one appears uncovered. Every OTHER status keeps today's `basis` byte for
   byte. No other key of the projection changes. `absence_class` is unchanged (`CANNOT_SAY` for NOT_SEARCHED -- the
   RETAIN pair measured that the adapter never reads it on these names). **Because the ONE production call site
   (`enrich.py:640`) and the re-projection mode (item 3) both call `project_ceo_public_profile`, a future live enrich
   run and this re-projection print the SAME sentence by construction** -- there is no second copy of the table.
2. **`management.schema.json`**: add `reason_code` to `definitions.ceo_public_profile_block.properties` as
   `{"type": ["string", "null"], "description": ...}`, NOT required (every existing object stays valid).
3. **`enrich.py`: a `--reproject-public-profile` CLI mode.** With `--security-key` and `--as-of` required, it GETs
   the EXISTING `management/v1/<key>/<as_of>.json` (a missing object is exit code 1 with a named reason, nothing
   written), sets ONLY `document["ceo_public_profile"] = ceo_search.project_ceo_public_profile(document["ceo_profile"])`,
   validates with `validate()` (a failure is exit 1, nothing written), prints one line per changed
   `ceo_public_profile` leaf (old -> new), and writes through `write_document` ONLY with `--write-pool`. It NEVER calls
   `build_document`, `apply_bloomberg_fallback`, `bloomberg_fallback.*`, `prospecting_page`, `_lusha_client`,
   `_serp_module` or `roster.load_source_object`, and NEVER recomputes or writes `_pool/` (it behaves as if
   `--skip-pool` were given, and says so). `generated_at` and every other top-level key are left as stored.
4. **Tests, a NEW file `lib/research/management/tests/test_reproject_public_profile.py`** (offline, stub S3, per
   the package's own test pattern; names must match AC2's list):
   - `test_not_searched_basis_is_the_table_sentence` -- for each of the 4 table codes, a NOT_SEARCHED profile ->
     `basis` equals `NOT_SEARCHED_SENTENCES[code]` byte for byte (the two sentences in AC6's expect are asserted as
     literals, so a table edit cannot pass silently), `reason_code` set, and `ceo_profile_reading` on it returns
     `NOT_SEARCHED`, `urls_returned None`, `reason` equal to the sentence; a NOT_SEARCHED profile with an UNKNOWN code
     takes the named fallback (its stored `reason`).
   - `test_every_not_searched_code_the_producer_emits_has_a_sentence` -- the ENUMERATION arm: drive
     `ceo_search.ceo_profile`'s four early returns offline (ceo None; a CEO with a blank name; no verified domain; no
     `serp` and `BRIGHT_DATA_API_KEY` unset) and collect every `reason_code` returned with status `NOT_SEARCHED`; the
     collected set EQUALS `set(NOT_SEARCHED_SENTENCES)`, 4 of 4, printing both sets.
   - `test_other_statuses_keep_their_basis_byte_for_byte` -- the DISCRIMINATING arm: load the PRE-CHANGE
     `ceo_search.py` from the PINNED commit `83da68c00a75da15d4959f50b7e51f25f2f69504` (the last commit to touch it,
     2026-09-19) via `git show <hash>:lib/research/management/ceo_search.py` into a temp module, and show that for
     each non-NOT_SEARCHED status the new projection minus `reason_code` equals the pinned projection, while for
     NOT_SEARCHED the two DIFFER in `basis`. **Pin the hash -- never HEAD or a merge-base: after your merge those name
     your own code and the arm goes red on every tree (row Z-S193).**
   - `test_schema_admits_reason_code_and_the_pinned_schema_refuses_it` -- the new schema validates a projected
     block; the schema at the same pinned commit rejects it with an `additionalProperties` error.
   - `test_reproject_changes_only_the_projection` -- a stub S3 holding one as-landed-shaped object;
     `bloomberg_fallback.pull_exec_officers`, `enrich.prospecting_page`, `enrich._lusha_client`,
     `enrich._serp_module`, `enrich.build_document` and `roster.load_source_object` patched to RAISE; the mode with
     `--write-pool` performs exactly ONE put, to that key, and the written document differs from the stored one only
     at `ceo_public_profile.basis` and `ceo_public_profile.reason_code`.
   - `test_reproject_writes_no_pool_and_refuses_a_missing_object` -- no `_pool/` key is written; a missing key
     returns exit 1 with a named reason and zero puts.
   - `test_reproject_without_write_pool_writes_nothing` -- the dry form prints the leaf diff and performs zero puts.

**R19-C RUNS IN THE SAME ROUND.** `AMGT-rk-77` (R19-C, row Z-S194) changes `scoped_amgt.read_management` to serve a
non-empty Bloomberg-fallback roster with its `roster_source` and a true officer count, and redeploys the adapter. It
writes ONLY `lib/research/api/scoped_amgt.py` and its tests; **this order writes no path it touches, and it touches
none of yours.** Its effect on you: once it lands, CSL's and 6861's CEO reading becomes VISIBLE, which is why the
sentence must be plain English. AC6 is written to pass in EITHER order of the two drains.

**What this cell does NOT change:** `scoped_amgt.py` or anything in the adapter's closure (NO redeploy); the search
itself (`ceo_search.ceo_profile`); `enrich.ceo_public_profile` (the retired legacy function at `:432`);
`build_document`'s normal path; the roster; the Bloomberg fallback; any other name's object. Other names' stored
projections keep the old sentence until their next ordinary enrich run -- **this is not a fleet run and must not
become one** (Andrew's no-fleet-rerun word; C-VALIDATION-NAMES).

**THE VALIDATION BAR:** the three names are rewritten in place; CAT's served reason line reads the sentence; nothing
else in any of the three objects moves; no raw stamp, pool object or other key is written.

## 2. WHERE THIS CAME FROM

**ROUND 19**, decomposition s.27 (cut by `2.0.0_SA_COO~Z`), on the rk-48 as-landed pair
(`ledger/NEVER_WIDEN_RK48_AS_LANDED_HALVES.md`, complete @0b71e7f5ab), `1.0.0_SA_CTO~Z`'s round-18 analysis
(`ledger/ROUND_ANALYSIS.round18.md` @ac58e01116, s.4 rulings @5f10ddf969) and msgs 23976, 24011 and 24015.
Row `AMGT_RESAPP-Z-S192` (the out-of-radius writes of rk-48, whose writer census this order must not repeat).
Andrew-direct ~16:5xZ (record @c5532df80a: *"the major work here is getting a functional product live and ready for
review for the managers"*) sets the priority; ~15:12Z (record @1e2a54bf0f) the one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/ceo_search.py
lib/research/management/enrich.py
lib/research/management/management.schema.json
lib/research/management/tests/test_reproject_public_profile.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~75/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-75.readable-not-searched-reason.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`scoped_amgt.py`, `bloomberg_fallback.py`,
  `roster.py`, `crosswalk.py`, the existing management tests, the pair file). Scratch is `<your worktree>/.scratch/`
  only (never committed). The existing test files are WALLS: if one of them breaks, that is a finding (row), not an
  edit.
- **Collision check, done at the cut (names only):** no other open order writes `lib/research/management/`; round
  18's cells wrote `lib/research/filings/battery.py` (+test) and `lib/research/api/scoped_amgt.py` (+test), both
  drained. The held branch `wk-amgt-14-50` changes `lib/research/management/{domains.json,enrich.py,
  management.schema.json,tests/test_lusha_domain.py}` by NAME -- **`enrich.py` and `management.schema.json` are
  shared names with that held branch.** It is not merged and is never read here; the overlap is recorded for the
  issuer, and nothing in this order depends on it.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~75 <0.9.0_WK_AMGT_RESAPP~75@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**NO VENDOR, NO BLOOMBERG, NO MODEL CALL.** The live act runs with `BRIGHT_DATA_API_KEY`, `LUSHA_API_KEY` and
`ANTHROPIC_API_KEY` UNSET in its environment (AC5's `env -u`), and the re-projection mode reaches no module that
would use them. Never call `--bloomberg`, `blp_client`, any MCP Bloomberg tool, or `enrich.main` without
`--reproject-public-profile`.
**THE LIVE REWRITE (AC5) IS SERVED-PLANE AND RUNS ONLY UNDER A NEVER-WIDEN PAIR.** Both
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_RK75_COO_HALF.md` and
`..._CTO_HALF.md` must exist at your spawn, each with a heading naming `AMGT-rk-75` and signed. Its blast radius is
EXACTLY three keys, `s3://opal-data-harvest/management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/2026-09-19.json`,
one new version each, differing from the pre-act version ONLY at `ceo_public_profile.basis` and
`ceo_public_profile.reason_code`. **The as-of is PINNED to `2026-09-19`; a run dated today would CREATE a new key no
half covers.**
**THE STOP RULE (the guard the pair asks for):** if AC3 reads any of the three `ceo_profile.status` other than
`NOT_SEARCHED`, any `ceo_profile.cost.serp_requests` other than 0, or any latest VersionId other than the issuer's,
STOP before AC4 with a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) -- the signed pre-act state no longer holds.
PORTAL FROZEN (no portal change is needed: the page renders `ceo_profile_reading.reason`). **COLLECTION STAYS OFF.**
**NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH:
never** (LD-0522). **Never delete an S3 object** (a rollback is `copy_object` from a pre-act VersionId).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by a plain enrich re-run,
never by editing a WALL, never by a different as-of.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure both suite baselines (77 / 185) before you
edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W75-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; a `DISMISSED_WITH_REASON` row carries a
`dismissal_reason`. A pure disarm sets `DISMISSED_WITH_REASON`, never `GRADUATED`; the disposition of Z-S192 is the
CVO's L9 act, not yours.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120 except AC5, which runs under timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import hashlib, io, os, re; d = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/"; [print(h, "ABSENT") if not os.path.exists(d + h) else (lambda t: print(h, "sha256", hashlib.sha256(t.encode("utf-8")).hexdigest(), "rk75_headings", len([l for l in t.splitlines() if l.startswith("#") and "AMGT-rk-75" in l]), "of 1", "mentions_rollback", len(re.findall(r"(?i)rollback", t)), "mentions_VersionId", len(re.findall(r"VersionId", t)), "signed", len(re.findall(r"(?i)signed `", t))))(io.open(d + h, encoding="utf-8").read()) for h in ("NEVER_WIDEN_ROUND19_RK75_COO_HALF.md", "NEVER_WIDEN_ROUND19_RK75_CTO_HALF.md")]'</invocation><expect>both halves present, each printing a 64-hex sha256, rk75_headings 1 of 1, mentions_rollback at least 1, mentions_VersionId at least 1 and signed at least 1 -- the pair is on file and signed; an ABSENT half, 0 of 1 headings or signed 0 REFUSES this criterion, and AC4-AC7 are NOT run (AC2, AC3 and AC8 still run, read-only)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -2 && python -m pytest lib/research/management/tests/test_reproject_public_profile.py -v -p no:cacheprovider 2>&1 | tail -10 && python -m pytest lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -2</invocation><expect>the first run reads "84 passed" and 0 failed (the 77 at the cut plus this cell's 7 new arms; re-measure the baseline at spawn, and the bar is "baseline plus 7, failures 0"); the second names PASSED for test_not_searched_basis_is_the_table_sentence, test_every_not_searched_code_the_producer_emits_has_a_sentence, test_other_statuses_keep_their_basis_byte_for_byte, test_schema_admits_reason_code_and_the_pinned_schema_refuses_it, test_reproject_changes_only_the_projection, test_reproject_writes_no_pool_and_refuses_a_missing_object and test_reproject_without_write_pool_writes_nothing; the third reads "185 passed", 0 failed, UNCHANGED from the cut -- the adapter is untouched</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/rk75_pre && python -c 'import boto3, hashlib, io, json; s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"; W = {"CAT_US_Equity": "Gb71vifhZHBDVpvq2ZGODr.WwZg.j.VW", "CSL_AU_Equity": "YOJ.tfyEZbNNVLc.XW2Z9e1w64kyAepe", "6861_JP_Equity": "HQl_.COQdPLdSopmRf.tQisuZF0LsMjR"}; out = {}; exec("for k, w in W.items():\n    v = s3.list_object_versions(Bucket=B, Prefix=\"management/v1/%s/\" % k)\n    vs = v.get(\"Versions\", []); latest = [x for x in vs if x[\"IsLatest\"]][0]\n    r = s3.get_object(Bucket=B, Key=\"management/v1/%s/2026-09-19.json\" % k); body = r[\"Body\"].read(); d = json.loads(body); cp = d[\"ceo_profile\"]\n    io.open(\".scratch/rk75_pre/%s.json\" % k, \"wb\").write(body)\n    raw = [o[\"Key\"] for p in s3.get_paginator(\"list_objects_v2\").paginate(Bucket=B, Prefix=\"raw/bloomberg/%s/\" % k) for o in p.get(\"Contents\", [])]\n    ex = len([x for x in raw if x.endswith(\"/exec_officers.json\")])\n    out[k] = {\"latest\": latest[\"VersionId\"], \"versions\": len(vs), \"raw\": len(raw), \"exec\": ex, \"sha256\": hashlib.sha256(body).hexdigest()}\n    print(\"PRE\", k, \"keys\", sorted({x[\"Key\"].rsplit(\"/\", 1)[-1] for x in vs}), \"versions\", len(vs), \"delete_markers\", len(v.get(\"DeleteMarkers\", [])), \"latest\", latest[\"VersionId\"], \"equals_issuer\", latest[\"VersionId\"] == w, \"ceo_status\", cp.get(\"status\"), \"reason_code\", cp.get(\"reason_code\"), \"serp_requests\", (cp.get(\"cost\") or {}).get(\"serp_requests\"), \"raw_objects\", len(raw), \"exec_officers_stamps\", ex)"); pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]; last = sorted(pool, key=lambda o: o["Key"])[-1]; out["_pool"] = {"objects": len(pool), "newest": last["Key"], "etag": last["ETag"]}; print("POOL objects", len(pool), "newest", last["Key"], "etag", last["ETag"]); io.open(".scratch/rk75_pre/baseline.json", "w", encoding="utf-8").write(json.dumps(out, indent=2))'</invocation><expect>for each of CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity: keys ["2026-09-19.json"], versions 2, delete_markers 0, equals_issuer True, ceo_status NOT_SEARCHED, reason_code NO_CEO_ON_ROSTER (CAT, 6861) / NO_VERIFIED_SITE (CSL), serp_requests 0; raw_objects / exec_officers_stamps CAT 12 / 0, CSL 14 / 2, 6861 14 / 2; POOL objects 3 newest management/v1/_pool/2026-09-19.json etag "7a1197377a0fff0e4e861ebc5208cf4a" -- all measured exactly so at the cut. The pre-act bytes and this baseline are saved to .scratch/rk75_pre/ (the rollback source). Any equals_issuer False, any ceo_status other than NOT_SEARCHED or any serp_requests other than 0 is the STOP RULE of section 4: BLOCKING row, AC4-AC7 not run. Single-quoted; no dollar sign reaches the shell</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py open --slug amgt-rk75-readable-not-searched-reason --title "AMGT-rk-75 re-projection of ceo_public_profile: in-place rewrite of management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/2026-09-19.json" --author 0.9.0_WK_AMGT_RESAPP~75 --leg "L1|verify|management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/2026-09-19.json|3 keys, one new version each, diff only ceo_public_profile.basis and reason_code, schema-valid, no raw stamp, _pool untouched, CAT served reason readable"</invocation><expect>the ledger entry is OPENED and its sentinel lands in org/critical_paths/.open_deploys/ BEFORE any live write; the command prints the entry path; run only AFTER AC1 and AC3 pass, and BEFORE AC5</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u BRIGHT_DATA_API_KEY -u LUSHA_API_KEY -u ANTHROPIC_API_KEY python -c 'import sys; from lib.research.management import enrich; rcs = [(k, enrich.main(["--security-key", k, "--as-of", "2026-09-19", "--reproject-public-profile", "--write-pool"])) for k in ("CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity")]; print("RCS", rcs); sys.exit(max(rc for _, rc in rcs))'</invocation><expect>per name the mode prints its changed leaves -- exactly ceo_public_profile.basis (old "NOT_SEARCHED / <code> -- 0 url(s), 0 fact(s) verified of 0 proposed" -> new, CAT and 6861 "No officer on the roster has a chief-executive title, so the CEO web search was not run.", CSL "No verified company website was found, so the CEO web search was not run.") and ceo_public_profile.reason_code (absent -> the code) -- a line saying no _pool object is recomputed or written, and one "OK: uploaded s3://opal-data-harvest/management/v1/<key>/2026-09-19.json ... put True" line; RCS [("CAT_US_Equity", 0), ("CSL_AU_Equity", 0), ("6861_JP_Equity", 0)] and exit 0. No line mentions Bloomberg, Lusha or the SERP being called. Any other leaf printed, or a non-zero rc, is AC6's rollback branch</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, io, json; from lib.research.management import enrich, ceo_search; from lib.research.api import scoped_amgt; s3 = boto3.client("s3", region_name="us-east-1"); lam = boto3.client("lambda", region_name="us-east-1"); B = "opal-data-harvest"; base = json.load(io.open(".scratch/rk75_pre/baseline.json", encoding="utf-8")); exec("for k in (\"CAT_US_Equity\", \"CSL_AU_Equity\", \"6861_JP_Equity\"):\n    pre = json.loads(io.open(\".scratch/rk75_pre/%s.json\" % k, \"rb\").read())\n    v = s3.list_object_versions(Bucket=B, Prefix=\"management/v1/%s/\" % k); vs = v.get(\"Versions\", [])\n    now = json.loads(s3.get_object(Bucket=B, Key=\"management/v1/%s/2026-09-19.json\" % k)[\"Body\"].read())\n    top = sorted(x for x in set(pre) | set(now) if pre.get(x) != now.get(x))\n    a, b = pre[\"ceo_public_profile\"], now[\"ceo_public_profile\"]\n    leaves = sorted(x for x in set(a) | set(b) if a.get(x, \"<absent>\") != b.get(x, \"<absent>\"))\n    ok, errors = enrich.validate(now); r = scoped_amgt.ceo_profile_reading(b)\n    raw = [o[\"Key\"] for p in s3.get_paginator(\"list_objects_v2\").paginate(Bucket=B, Prefix=\"raw/bloomberg/%s/\" % k) for o in p.get(\"Contents\", [])]\n    print(k, \"keys\", sorted({x[\"Key\"].rsplit(\"/\", 1)[-1] for x in vs}), \"versions\", len(vs), \"was\", base[k][\"versions\"], \"delete_markers\", len(v.get(\"DeleteMarkers\", [])), \"changed_top\", top, \"changed_leaves\", leaves, \"ceo_profile_equal\", pre[\"ceo_profile\"] == now[\"ceo_profile\"], \"schema_valid\", ok, errors[:1], \"reading\", r[\"reading\"], \"urls_returned\", r[\"urls_returned\"], \"reason_is_table_sentence\", r[\"reason\"] == ceo_search.NOT_SEARCHED_SENTENCES.get(b.get(\"reason_code\")), \"basis\", repr(b.get(\"basis\")), \"reason_code\", b.get(\"reason_code\"), \"raw_objects\", len(raw), \"was\", base[k][\"raw\"])\n    ev = {\"rawPath\": \"/api/scoped/amgt/security/%s/thesis\" % k, \"headers\": {\"x-firm-id\": \"bd\"}, \"requestContext\": {\"http\": {\"method\": \"GET\"}}}\n    res = json.loads(lam.invoke(FunctionName=\"opal-amgt-scoped-api\", Payload=json.dumps(ev).encode())[\"Payload\"].read()); m = (json.loads(res[\"body\"]) if isinstance(res.get(\"body\"), str) else {}).get(\"management\") or {}; sr = m.get(\"ceo_profile_reading\") or {}\n    print(\"   SERVED\", k, res.get(\"statusCode\"), \"management_status\", m.get(\"management_status\"), \"absent_because\", m.get(\"absent_because\"), \"reading\", sr.get(\"reading\"), \"urls_returned\", sr.get(\"urls_returned\"), \"reason\", repr(sr.get(\"reason\")))"); pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]; last = sorted(pool, key=lambda o: o["Key"])[-1]; print("POOL objects", len(pool), "etag", last["ETag"], "equal_to_pre", last["ETag"] == base["_pool"]["etag"] and len(pool) == base["_pool"]["objects"])' 2>&1 | tee .scratch/rk75_ac6.txt</invocation><expect>for each of the three: keys ["2026-09-19.json"] (no new dated key), versions 3 was 2, delete_markers 0, changed_top ["ceo_public_profile"], changed_leaves ["basis", "reason_code"], ceo_profile_equal True, schema_valid True, reading NOT_SEARCHED, urls_returned None, reason_is_table_sentence True, reason_code NO_CEO_ON_ROSTER (CAT, 6861) / NO_VERIFIED_SITE (CSL), basis "No officer on the roster has a chief-executive title, so the CEO web search was not run." (CAT, 6861) / "No verified company website was found, so the CEO web search was not run." (CSL), raw_objects EQUAL to its was (12, 14, 14 at the cut -- no Bloomberg stamp written). SERVED, from the LIVE adapter (a different instrument from the in-process reading): CAT 200, management_status SERVED, reading NOT_SEARCHED, urls_returned None, reason "No officer on the roster has a chief-executive title, so the CEO web search was not run."; CSL and 6861 200 in EITHER of two states, both PASS: (i) R19-C (AMGT-rk-77) NOT yet deployed -- management_status ABSENT, absent_because ZERO_OFFICERS, no CEO reading (scoped_amgt.py:2512-2530 at the cut); or (ii) R19-C deployed -- management_status SERVED, reading NOT_SEARCHED, urls_returned None, reason "No verified company website was found, so the CEO web search was not run." (CSL) / "No officer on the roster has a chief-executive title, so the CEO web search was not run." (6861). Print which state each name is in. Any SERVED reason that is not the table sentence FAILS. POOL equal_to_pre True. ROLLBACK BRANCH (any other changed_top or leaf, ceo_profile_equal False, schema_valid False, a raw count moved, a new dated key, the pool moved, or a served reason that is not the table sentence): copy_object each rewritten key from its AC3 pre-act VersionId, read back sha256 equal to the AC3 baseline, file a BLOCKING row naming the branch; DELETE NOTHING</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py close-leg --slug amgt-rk75-readable-not-searched-reason --leg-id L1 --proof "$(cat .scratch/rk75_ac6.txt)" && python .tools/deploy_ledger.py close --slug amgt-rk75-readable-not-searched-reason && python .tools/deploy_ledger.py check</invocation><expect>leg L1 closed with AC6's read-back as its proof, the entry CLOSED, and the check lists no open entry for amgt-rk75-readable-not-searched-reason (its sentinel removed from org/critical_paths/.open_deploys/); the closed entry is COMMITTED with the instance, never left staged. (close-leg takes --proof only, measured at the cut; the same form AMGT-rk-48's AC5 ran.) On the rollback branch the leg closes with the rollback proof instead</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-75"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, json, subprocess; P = "83da68c00a75da15d4959f50b7e51f25f2f69504"; [print(f, "parses", (bool(json.loads(io.open(f, "rb").read().decode("utf-8"))) if f.endswith(".json") else bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec"))), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "| pinned_base", (lambda b: (len(b) - len(b.decode("utf-8"))) if b else "NEW")(subprocess.run(["git", "show", P + ":" + f], capture_output=True).stdout)) for f in ("lib/research/management/ceo_search.py", "lib/research/management/enrich.py", "lib/research/management/management.schema.json", "lib/research/management/tests/test_reproject_public_profile.py")]'</invocation><expect>all four files print parses True, crlf 0 and non_ascii_bytes 0; pinned_base 0 for the three existing files (read from the pinned pre-change commit, never assumed) and NEW for the test file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Also record in your deliverable the three before/after `ceo_public_profile` blocks (they carry no contact
field and no secret).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~75/AMGT_RESAPP.TO-AMGT-rk-75.readable-not-searched-reason.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>` (the closed ledger entry travels in this commit). Report
once: the suite counts before and after, the three before/after `basis` lines, CAT's served reason, the raw and pool
counts before and after, whether rollback fired, and the ledger entry's open and close.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/rk75/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>19</round>
<slot>~75</slot>
<fabric>site-z</fabric>
