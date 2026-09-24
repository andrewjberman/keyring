# AMGT_RESAPP task order -- `AMGT-rk-87` -- the Lusha channel gets ONE harvest writer, SILVER ONLY: an ALLOW-LIST projection of each prospecting result (officer match, title, ONE public professional-profile URL) written through H0-store to `lusha/harvest/silver/contact_match`, with NO bronze by rule, every contact field dropped, `bronze_key` null, and a bucket fetch-key check before any call; CODE ONLY -- built and tested offline, off by default, wired into nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-87</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~87</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds one library module and one test file; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none, and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; every test runs offline against a
  stub S3 with AWS credentials pointed at a non-existent profile (AC4), and nothing is written to AWS by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~87`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist (the two new files excepted); if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~87;`. **NEVER RUN AN INSTALL.**
**Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an EXPOSED LUSHA
CREDENTIAL. This cell is designed from HEAD and the PRD only.** No secret is needed or read by this order.

## 1. THE CELL, inlined in full -- `AMGT-rk-87` (round 22, cell H4; contract `C-LUSHA-EXCEPTION`)

**The contract, verbatim (PRD v0.17 `prd/AMGT_RESAPP_PRD.md:877-883` @1f7459456a, ADMITTED -- ratified-text signed by
`3.0.0_SA_CVO~Z`, brief by `4.0.0_SA_CRO~Z`):** *"C-LUSHA-EXCEPTION (a declared departure, Rule 30 R20; Andrew-direct
2026-09-21 ~19:5xZ, "Yes on Exception"). Lusha keeps NO bronze, and its silver DROPS every contact field: emails,
phone numbers, postal addresses, and any personal messaging or social handle. It keeps the officer match, the title,
and ONE public professional-profile URL. That URL is the "profile link" `C-EXEC-MANAGEMENT` enriches with and the
page shows; it is kept because it is that served field, not as a channel for reaching the person. Nothing else a
person could be reached through is kept. This departs from `C-BRONZE-AS-RECEIVED` and `C-SILVER-PARQUET` for Lusha
only. Its silver rows carry `fetched_at` and `record_hash`, and `bronze_key` is null by rule."*

**The other contracts that bind, verbatim (same file):** `:885-890` *"C-DEDUPE-BY-KEY (one writer per fetch key).
Each channel names a FETCH key and a RECORD key. Before any vendor call, the writer checks the bucket for the fetch
key. Exactly one writer holds a channel's fetch keys at a time ... A silver writer skips an unchanged `(record key,
record_hash)` and writes a changed row as a new row, never an update ... The bucket is the authority for what has
been fetched, never a file on one desktop."* `:856-864` C-HARVEST-HOME: every address is `address()` output.

**The design source (plan `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
s.5.7 @1a9f1c4469):** *"Record key / dedupe. Fetch key `(company domain, endpoint)`, never re-queried inside a window
(credits). Silver key `(domain, person id)`."* The decomposition proposal (`.scratch/r21_drafts/
HARVEST_CHAIN_DECOMP_PROPOSAL.md:151`, cell H4): *"`management/enrich.py:571-630` -> `silver_append("lusha",
"contact_match")`, contact fields dropped | none (code) | no | H0 store, rk-79 drained"*. rk-79 DRAINED @a13b0fc140.

**THE MEASURED STATE, at HEAD `3863a8200d` (SITEZ). RE-READ every line at your branch HEAD before editing:**
- **The Lusha call today** (`lib/research/management/enrich.py`, 1294 lines, sha256 prefix `b1f2edb2550c037c`):
  `prospecting_page(client, company_domain)` `:300` makes ONE billable page and returns `{results, total, credits,
  filter, status, note}`; `build_document` calls it at `:659` and folds the result into the management document as
  `lusha_enrichment` (`:636-676`); `attach_profiles` `:369-393` takes `jobTitle` (str or `{title}`) and
  `socialLinks.linkedin`; `name_matches` `:349` is the estate's match rule; `scrub` `:91` and `is_contact_key` `:85`
  are the estate's contact rule. **No Lusha object of its own exists** (plan s.5.7; measured read-only at the cut: `list_objects_v2`
  over `s3://opal-data-harvest/lusha/`, paginated = **0 objects**).
- **Lusha call sites, census by subtraction** (`Grep 'prospecting_page\(|contacts_prospecting\(|_lusha_client\(|LushaClient\('`
  over the 6664 tracked `*.py` files): **45 hit lines; minus 25 in test files, 13 in the FIND pipeline
  (`data/find/**`, a different pipeline) and 2 in a CTO measurement script (`org/tier1_exec/**`) = 5 AMGT lines**, all
  in `enrich.py`: `:264` and `:300` (the two `def`s), `:284` (the client constructor), `:334` (the billable call inside
  `prospecting_page`) and `:659` (`build_document`'s call) -- **ONE AMGT call path**, writing into
  `management/v1/<key>/<date>.json` only.
- **The builder, LIVE at HEAD** (`lib/opal_naming.py`, `validate()` 0 refusals; the duplicate `harvest` scope row was
  deleted @10bace8916, row Z-S203 disarmed by Z-S205): `address("lusha","harvest","silver","contact_match",
  "date=2026-09-21","part-20260921T120000Z.parquet")` = `s3://opal-data-harvest/lusha/harvest/silver/contact_match/
  date=2026-09-21/part-20260921T120000Z.parquet`. The bronze address resolves too
  (`s3://opal-data-harvest/lusha/harvest/bronze/company_contacts/...`) and is NEVER used (the contract).
- **H0-store** (`AMGT-rk-81`, `lib/research/harvest/store.py`; its interface `.scratch/r21_drafts/H0_STORE_INTERFACE.md`,
  fixed at issuance): `silver_append(source, table, rows, record_key_fields, run_stamp, client=None)` REFUSES a Lusha
  row whose `bronze_key` is not None and any row carrying a `CONTACT_FIELDS` key (`LushaExceptionError`); `bronze_put`
  raises `LushaExceptionError` for `source == "lusha"`; `silver_latest(source, table, record_key_fields, client=None)`
  returns the newest row per record key. **The store enforces the exception; this cell must not re-implement it.**
- **Test baselines at the cut:** `lib/research/management/tests` **95 passed** (13 subtests), 0 failed.
  `lib/research/harvest/tests` does not exist at the cut; it arrives with rk-81 (re-measure at spawn).

**RULED, what you build (a NEW module; no existing file changes):**
1. **`lib/research/harvest/lusha.py`**, module constants: `SOURCE = "lusha"`, `TABLE = "contact_match"`,
   `ENDPOINT = "contacts/prospecting"`, `RECORD_KEY = ("domain", "person_id")`, `NO_RESULT_PERSON_ID = "__no_result__"`,
   and **`KEPT_FIELDS`, the ALLOW-LIST**, exactly: `("domain", "endpoint", "person_id", "first_name", "last_name",
   "job_title", "seniority", "profile_url", "matched_officer", "results_total", "fetched_at", "bronze_key")`.
2. **`contact_match_rows(results, company_domain, fetched_at, officers=None, results_total=None) -> list[dict]`** --
   PURE. One row per result, built ONLY from `KEPT_FIELDS` by ONE construction: a `candidate` dict is the result's
   own keys plus the derived snake_case fields below, and the row is `{k: candidate.get(k) for k in KEPT_FIELDS}` --
   so `KEPT_FIELDS` is the single control on what is kept (AC3 widens it and must see a contact field leak).
   `person_id` from the result's own id field (`id`,
   `personId` or `contactId`, first present, stringified; a result with none is skipped and counted in a returned
   `skipped` attribute or second return value -- your choice, documented); `job_title` from `jobTitle` (str or
   `{title}`), `profile_url` = `socialLinks.linkedin` ONLY (every other link, handle or messaging field is never read);
   `matched_officer` = the officer name `enrich.name_matches` pairs with this result, else None; `bronze_key = None`.
   A value is ASCII-folded with `roster.asciify` exactly as `attach_profiles` does. **A zero-result fetch returns ONE
   sentinel row** with `person_id = NO_RESULT_PERSON_ID` and every other vendor field None, so the bucket records the
   fetch (C-DEDUPE-BY-KEY). **Nothing outside `KEPT_FIELDS` ever enters a row** -- an allow-list, not a deny-list.
3. **`already_fetched(company_domain, since, client=None) -> bool`** -- the bucket fetch-key check: True if
   `store.silver_latest(SOURCE, TABLE, RECORD_KEY, client)` holds any row with this `domain` and `fetched_at >= since`.
4. **`write_contact_match(rows, run_stamp, client=None) -> dict`** -- calls `store.silver_append(SOURCE, TABLE, rows,
   RECORD_KEY, run_stamp, client)` and returns its receipt. It never calls `store.bronze_put`, never builds a URI and
   never imports `boto3`, a Lusha client, `urllib` or `requests`.
5. **Not wired.** No existing file imports `lib.research.harvest.lusha`; `enrich.py` and `ceo_search.py` stay
   BYTE-EQUAL to the pin; the move cell wires the writer in later, under its own pair.
6. **Tests, a NEW file `lib/research/harvest/tests/test_lusha.py`** (offline; a stub S3 client of the store's own
   test idiom -- read `lib/research/harvest/tests/test_store.py` and reuse its stub if it exports one). Arms, names
   must match AC1:
   - `test_allow_list_drops_every_contact_field` -- a fixture result carrying `emails`, `phones`, `phoneNumbers`,
     `emailAddresses`, `address`, `location`, `socialLinks.twitter`, `socialLinks.facebook`, `whatsapp`: the row's keys
     are a subset of `KEPT_FIELDS`, no value contains `@`, and no value matches a phone-number shape.
   - `test_profile_url_is_the_linkedin_link_only`.
   - `test_matched_officer_uses_the_estate_name_rule` -- a match and a near-miss (same surname, different given name).
   - `test_zero_result_fetch_writes_one_sentinel_row`.
   - `test_silver_append_writes_lusha_silver_with_null_bronze_key` -- through the stub: one part under
     `lusha/harvest/silver/contact_match/date=<fetch date>/`, rows carrying `bronze_key` None and a `record_hash`.
   - `test_already_fetched_reads_the_bucket` -- True inside the window after a write, False with `since` after it.
   - `test_module_never_calls_bronze_put_and_the_store_refuses_lusha_bronze` -- an AST read of `lusha.py` finds no
     `bronze_put`, and `store.bronze_put("lusha", ...)` raises `store.LushaExceptionError`.
   - `test_module_imports_no_client_or_network` -- an AST read of `lusha.py` imports none of `boto3`, `urllib`,
     `requests`, `lusha_client`, `LushaClient`.
   - `test_patched_store_is_the_one_production_reaches` -- the W85-S1 identity arm (CTO round-21 analysis `:29-33`): the test imports
     `lib.research.harvest.store` and `lib.research.harvest.lusha` by their QUALIFIED names, asserts
     `lusha.store is store`, then monkeypatches `store.silver_append` with a recording fake and asserts that
     `lusha.write_contact_match(...)` reached that fake (so the patched object IS the one the production caller
     reaches). Every other arm that patches across modules also uses the qualified names.

**What this cell does NOT change:** `enrich.py`, `ceo_search.py`, `roster.py`, `management.schema.json` (AC5 proves
byte-equality to the pin), `lib/research/harvest/store.py` (rk-81's; a WALL), any management object, any S3 object.
**No served change.** It retires no phrase any test pins (standing rule, CTO msg 24100): it edits no existing file.

## 2. WHERE THIS CAME FROM

**Rulings of record for round 22** (`1.0.0_SA_CTO~Z`, `ledger/ROUND_ANALYSIS.round21.md` @`739eb5f288`, msg 24119,
quoted verbatim):
- `:29-33` (row W85-S1): *"Disarmed for this project by a cutting rule, binding from round 22: every AMGT test that
  patches or asserts on code outside its own module imports the QUALIFIED `lib.<package>.<module>` name, never a
  relative or bare one. Each order's criteria include one arm proving the patched object is the one the production
  caller reaches (an `is` identity check against the qualified import)."* -- this order's arm `test_patched_store_is_the_one_production_reaches`.
- `:34-35`: *"The COO's cutting note from W84-S1 is adopted alongside: a criterion with a backslash escape inside
  `python -c` is written as a file its invocation runs."* -- this order's criteria carry NO backslash escape (AC5 reads
  lines with `splitlines()`, AC6 counts CRLF with `bytes([13, 10])`), so each stays a literal `python -c`; a
  criterion that needs an escape is written as a file under your scratch dir and its invocation runs that file.
- `:43` (rk-88's two calls): *"(a) SERP bronze keeps the raw public results body, and silver is scrubbed; (b) a Lusha
  zero-result lands as a placeholder SILVER row, not a state object, so "asked and found nothing" is a record with
  its fetch key."*  This order's zero-result design already satisfies (b): `test_zero_result_fetch_writes_one_sentinel_row`
  writes ONE silver row carrying the fetch key `domain`, with `person_id = NO_RESULT_PERSON_ID`.

**ROUND 22**, decomposition s.30 (cut by `2.0.0_SA_COO~Z`), cell H4 of the harvest format-migration chain, accepted by
`1.0.0_SA_CTO~Z` (msg 24090: *"ROUND 21: waves 1 + 2 (H0-store, H0-iam, H1-H6) = 8 cells is ACCEPTED ... (iii) rk-79
has drained, for H4/H5"*; msg 24098: v0.17 ADMITTED). Andrew-direct ~19:5xZ (*"Yes on Exception"*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_195xZ_AMGT_RESAPP_KEYENCE_SEARCH_YES_LUSHA_R20_YES.md`
@4bcfed0e0d) is the departure this cell implements. Andrew-direct ~15:12Z governs the one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/lusha.py
lib/research/harvest/tests/test_lusha.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~87/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-87.lusha-silver-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`store.py`, `test_store.py`, `enrich.py`,
  `roster.py`, the PRD, the plan). Scratch is `<your worktree>/.scratch/r87/` only (never committed).
- **Collision check, done at the cut** (a `<paths>` census over round 21's other drafts): rk-81 `lib/research/harvest/
  {__init__.py, store.py, tests/test_store.py}`; rk-82 two `infra/aws/terraform/harvest/*.tf`; rk-83 `harvest/
  {bloomberg.py, tests/test_bloomberg.py}`; rk-84 `harvest/{filings.py, tests/test_filings.py}`; rk-85 seven
  `integrations/seekingalpha/*` and `lib/opal_data_harvest/*` files; rk-86 `lib/research/social/*`; rk-88 `harvest/
  {bright_data_serp.py, tests/test_bright_data_serp.py}`. **Zero code-path overlap.** The only shared file is
  `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~87 <0.9.0_WK_AMGT_RESAPP~87@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**THIS CELL IS CODE ONLY: NO LUSHA CALL, NO S3 WRITE OR READ, NO DEPLOY, NO NEVER-WIDEN PAIR.** No credit is spent;
no secret is read (Andrew's rotation of the Lusha key is deferred by his word, and this cell needs no key). **NO
BRONZE FOR LUSHA, EVER** (C-LUSHA-EXCEPTION). **COLLECTION STAYS OFF. NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** PORTAL not your surface. No non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing `store.py`,
`enrich.py` or any file outside `<paths>`, and never by keeping a field outside `KEPT_FIELDS`.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure both suites before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W87-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; `disarm_owner` is never a worker serial
(name `2.0.0_SA_COO~Z`). A pure disarm sets `DISMISSED_WITH_REASON` with a `dismissal_reason`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import importlib, os
print("store_file", os.path.exists("lib/research/harvest/store.py"))
s = importlib.import_module("lib.research.harvest.store")
need = ["SCOPE", "HARVEST_BUCKET", "CONTACT_FIELDS", "LushaExceptionError", "SilverRowError", "address_of", "date_partition", "stamp", "bronze_put", "silver_append", "silver_latest", "record_hash"]
print("store_names_present", sum(1 for x in need if hasattr(s, x)), "of", len(need), "missing", [x for x in need if not hasattr(s, x)])
from lib import opal_naming as n
r = n.validate()
print("validate_refusals", len(r[0]) if isinstance(r, tuple) else r)
print("silver", n.address("lusha", "harvest", "silver", "contact_match", "date=2026-09-21", "part-20260921T120000Z.parquet"))
'</invocation><expect>"store_file True"; "store_names_present 12 of 12 missing []"; "validate_refusals 0"; "silver s3://opal-data-harvest/lusha/harvest/silver/contact_match/date=2026-09-21/part-20260921T120000Z.parquet". Any other reading -- store absent (rk-81 not merged), a missing name, a refusal, or a bucket other than opal-data-harvest -- is a STOP: file a BLOCKING row (disarm_owner 2.0.0_SA_COO~Z) and edit nothing</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_lusha.py -v -p no:cacheprovider 2>&1 | tail -14</invocation><expect>a final line "9 passed" and 0 failed, the PASSED lines naming test_allow_list_drops_every_contact_field, test_profile_url_is_the_linkedin_link_only, test_matched_officer_uses_the_estate_name_rule, test_zero_result_fetch_writes_one_sentinel_row, test_silver_append_writes_lusha_silver_with_null_bronze_key, test_already_fetched_reads_the_bucket, test_module_never_calls_bronze_put_and_the_store_refuses_lusha_bronze, test_module_imports_no_client_or_network, test_patched_store_is_the_one_production_reaches</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>two lines: first "N passed" and 0 failed where N is the harvest suite's count re-measured at spawn (rk-81's own tests plus any sibling cell already merged) plus this cell's 9 (measured at 739eb5f288: harvest 28 = rk-81 11 + rk-83 9 + rk-84 8, so 37 if no sibling merges first); then "95 passed" (13 subtests) and 0 failed, UNCHANGED from the cut -- re-measure both before you edit and print the two baselines in your instance</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import datetime, importlib
m = importlib.import_module("lib.research.harvest.lusha")
at = datetime.datetime(2026, 9, 21, 12, 0, tzinfo=datetime.timezone.utc)
res = [{"id": 7, "firstName": "Ada", "lastName": "Doe", "jobTitle": {"title": "CEO"}, "emails": ["a@x.com"], "phones": ["+1 212 555 0100"], "socialLinks": {"linkedin": "https://www.linkedin.com/in/ada", "twitter": "@ada"}}]
real = m.contact_match_rows(res, "x.com", at)
rows = real[0] if isinstance(real, tuple) else real
print("real_keys_subset_of_allow_list", all(set(r) <= set(m.KEPT_FIELDS) for r in rows), "rows", len(rows))
m.KEPT_FIELDS = tuple(m.KEPT_FIELDS) + ("emails", "phones")
try:
    mut = m.contact_match_rows(res, "x.com", at)
    mrows = mut[0] if isinstance(mut, tuple) else mut
    leaked = any(("emails" in r) or ("phones" in r) for r in mrows)
except Exception as e:
    leaked = "raised " + type(e).__name__
print("mutant_allow_list_widened_leaks_or_raises", leaked)
'</invocation><expect>"real_keys_subset_of_allow_list True rows 1", then "mutant_allow_list_widened_leaks_or_raises" followed by True or "raised <Error>" -- proving the projection is DRIVEN by KEPT_FIELDS (widening the allow-list is what lets a contact field in, so the allow-list is the control), never False. If the mutant prints False, the projection ignores KEPT_FIELDS: REFUSE and fix the module so KEPT_FIELDS is the only source of kept keys</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && env -u AWS_ACCESS_KEY_ID -u AWS_SECRET_ACCESS_KEY -u AWS_SESSION_TOKEN AWS_PROFILE=__rk87_no_such_profile__ AWS_CONFIG_FILE=/nonexistent AWS_SHARED_CREDENTIALS_FILE=/nonexistent python -m pytest lib/research/harvest/tests/test_lusha.py -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"9 passed" and 0 failed with every AWS credential source pointed at nothing -- the tests make no AWS or network call (a live call would raise a credentials or profile error)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import ast, hashlib, subprocess
PIN = "3863a8200d382e8b9943f7d03141326b93a86d26"
files = [f for f in subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True).stdout.splitlines() if f]
files += [f for f in ("lib/research/harvest/lusha.py", "lib/research/harvest/tests/test_lusha.py") if f not in files]
importers, bad = [], 0
for f in files:
    try: tree = ast.parse(open(f, "rb").read().decode("utf-8"))
    except Exception: bad += 1; continue
    for node in ast.walk(tree):
        mods = []
        if isinstance(node, ast.Import): mods = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module: mods = [node.module] + [node.module + "." + a.name for a in node.names]
        if any(x == "lib.research.harvest.lusha" for x in mods): importers.append(f); break
print("py_files", len(files), "unparsed", bad, "importers", sorted(set(importers)))
for f in ("lib/research/management/enrich.py", "lib/research/management/ceo_search.py"):
    base = subprocess.run(["git", "show", PIN + ":" + f], capture_output=True).stdout
    print(f, "byte_equal_to_pin", open(f, "rb").read() == base, "pin_sha16", hashlib.sha256(base).hexdigest()[:16])
'</invocation><expect>"unparsed 0" and "importers ['lib/research/harvest/tests/test_lusha.py']" -- the new writer is imported by its own test ONLY, wired into nothing; then enrich.py "byte_equal_to_pin True pin_sha16 b1f2edb2550c037c" and ceo_search.py "byte_equal_to_pin True pin_sha16 2b5da242faf81c50" (measured at the cut, PINNED commit, never HEAD or a merge-base -- row Z-S193)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-87"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import io
for f in ("lib/research/harvest/lusha.py", "lib/research/harvest/tests/test_lusha.py"):
    b = io.open(f, "rb").read()
    print(f, "compiles", bool(compile(b.decode("utf-8"), f, "exec")), "crlf", b.count(bytes([13, 10])), "non_ascii_bytes", len(b) - len(b.decode("utf-8")))
'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0 (both are NEW, absent at the pin)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~87/AMGT_RESAPP.TO-AMGT-rk-87.lusha-silver-writer.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip the order's
status to `complete`; commit with `--only -- <paths>`. Report once, naming both suite counts before and after, the
row count and keys from AC3, and the AC5 importer list.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r87/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**Issuer notes (not for the worker):** spawn only after rk-81 DRAINS (AC0 stops otherwise). Open questions carried to
the issuer at draft time: (1) the zero-result SENTINEL row (`person_id "__no_result__"`) is this draft's answer to
C-DEDUPE-BY-KEY for a fetch with no results -- without it an empty fetch leaves nothing in the bucket and the next run
pays again; the alternative is a state object under `amgt/harvest/state/`; (2) the fetch-key window for
`already_fetched` is left to the caller (`since`); the move cell fixes it; (3) the store's `CONTACT_FIELDS` is a
snake_case set, while Lusha returns camelCase (`emailAddresses`, `phoneNumbers`) -- this cell's ALLOW-LIST keeps those
out regardless, but the store's own guard would not catch them; named for rk-81's owner.

<status>complete</status>
<round>22</round>
<slot>~87</slot>
<fabric>site-z</fabric>
