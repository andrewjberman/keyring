# AMGT_RESAPP task order -- `AMGT-rk-47` -- the Bloomberg COMPANY_EXEC_OFFICERS fallback for the officer TABLE only, labelled, `roster_source` on every object, the filing's own failure reason travelling with it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-47</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~49</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the weekly
  OpalResearch-ExecManagement task stays DISABLED and is neither read nor written; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  s3://opal-data-harvest management/v1/ and raw/bloomberg/ prefixes this project already writes) under the
  box's existing AWS credentials, the same ones AMGT-rk-22's batch used; it grants no permission and
  provisions no resource; no Lambda, no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~49`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`,
`lib/research/management/` and `integrations/bloomberg/mcp/blp_client.py` exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD A QUEUE OF TWO ORDERS ON ONE SLOT, in this sequence: `AMGT-rk-47` (this one), then
`AMGT-rk-48` (the CEO search), handed to you as a continuation when this one is terminal.** Both edit
`lib/research/management/enrich.py::build_document`, which is why they share one worker and never run side
by side. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~49;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-47` (R14-E5; FWD-17; Andrew's card 1 and PRD v0.13 `C-EXEC-MANAGEMENT`)

**THE ANALYSIS ROW, VERBATIM** (`ledger/ROUND_ANALYSIS.round13.md:135` @`9c8e04cd9a`): *"E5 Andrew's card 1: the
Bloomberg `COMPANY_EXEC_OFFICERS` fallback for the TABLE only, labelled, `roster_source` on every object, the
filing's own failure reason travelling with it"* -- serves FWD-17, cards 1 and s.9; co-sign YES.

**ANDREW'S WORD, VERBATIM** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md:13`
@`4f44431d34`): *"1.) Yes."* to *"When there's no filing, should Bloomberg's executive list fill the table?"*,
recommended and read narrow as: *"labelled as coming from Bloomberg, with tenure left blank and the reason stated"*
(`:6-7`, `:17-20`).

**THE RATIFIED TEXT YOU IMPLEMENT** -- PRD v0.13 `C-EXEC-MANAGEMENT`, `prd/AMGT_RESAPP_PRD.md:722-733` @`1699960261`:
- `:723-726`: *"When the filing yields no RESOLVED roster, Bloomberg's `COMPANY_EXEC_OFFICERS` (name and title only,
  names kept verbatim) fills the officer TABLE and is labelled on the page as a Bloomberg fallback. Role start,
  tenure and the pool comparison stay ABSENT, with the reason that Bloomberg carries no role start. A RESOLVED filing
  roster replaces the fallback on the next build."*
- `:727`: *"Every management object carries `roster_source` = FILING | BLOOMBERG_FALLBACK. The fallback never hides why
  the filing failed: when a filing roster failed (an empty officer-section cut, or a section no declared shape reads),
  its own `roster_status` and `roster_reason` stay on the object beside the Bloomberg officers, and the page shows them."*
- `:731-732`: *"A roster with ZERO officers is NOT SERVED. It is ABSENT with its reason. Every census and report prints
  the content count (names with at least one officer) beside the status count, and counts FILING and
  BLOOMBERG_FALLBACK separately."*
- `:735-736`: Bloomberg-fallback officers are ENRICHABLE and the label says which source applies (the enrichment
  itself is `AMGT-rk-49`'s cell, not yours; you only make the officer rows carry their source).
- `:757`: *"Open at L4, not decided here: whether a Bloomberg-fallback CEO is searched."* -- you decide nothing on
  it; `AMGT-rk-48` records `name_source` and the L4 settles the policy.

**THE MEASURED STATE, at HEAD (`da7b0b1804`; the management package is byte-identical from `9c8e04cd9a` through
HEAD, `git diff --stat` empty):**
- `lib/research/management/roster.py::build_roster` (`:501-566`) is the only roster builder; when the filing is
  absent (`:522-525`), UNRESOLVED (`:528-531`), cut empty (`:534-540`) or read by no declared shape (`:542-545`), the
  document leaves with `roster_status: "UNRESOLVED-SOURCE"`, `roster_reason` set and `officers: []`. There is NO
  second source anywhere in the package (`__init__.py:3-8`: *"never a guessed roster, and never a roster built from
  Lusha"*).
- `lib/research/management/enrich.py::build_document` (`:490-550`) calls `build_roster` at `:494` and then classes
  the absence (`:540-546`, `classify_roster_absence` `:165-195`). `officers` drives everything after it (`:506-536`).
- `lib/research/management/management.schema.json` has no `roster_source`; `officer.source` is `const: "filing"`
  (`:130`) and `confirmed` is *"true only when the person was read from the filing's officer section"* (`:131-134`).
- The estate's Bloomberg client is `integrations/bloomberg/mcp/blp_client.py::reference_data(...)` (`:135`) with
  `health()` (`:125`), loaded by PATH exactly as `integrations/bloomberg/research/model_block_pull.py::_load_blp_client`
  does (`:147-155`; no package marker under `mcp/`). `COMPANY_EXEC_OFFICERS` is a BULK field on a
  `ReferenceDataRequest`; the CRO pulled it that way beside `NAME` at
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_TAB_SCORE_REVIEW_20260915_W/measure.py:355-370`, and measured
  it POPULATED for all 21 keyed names without a filing, NAME and TITLE only, no role start (Exec Management brief
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md:91`, `:188-192`).
  Each entry reads `"<name>,  <title>"` with TWO spaces, nicknames and honorifics inside the name
  (`Manveen Kaur "Pam"`, `Dr Thomas Schinecker`), kept verbatim (brief `:204-207`).
- Raw Bloomberg responses land at `raw/bloomberg/<security_key>/<stamp>/<name>.json` BEFORE anything derives
  (`model_block_pull.py:5-11`, `s3_put_if_absent` `:184-198` never overwrites an existing key). The management
  pipeline is an EXISTING pipeline, so Rule 30's builder requirement does not apply to this landing (Rule 30
  NON-APPLICATION); you use that existing convention with the file name `exec_officers.json`.
- The adapter `lib/research/api/scoped_amgt.py::read_management` (`:2305-2371`) copies NAMED fields off the object
  (`:2346-2369`) -- it does not pass an unknown field through. **The adapter and the page are NOT your surface**
  (the R14-E1 cell, analysis `:131`, owns the served label; chain B owns `scoped_amgt.py`). Your object carries the label text and
  the source so that cell has something to serve.
- The Bloomberg terminal on this box must be SIGNED IN for any pull (`integrations/bloomberg/READ_HERE.md:26-60`).
  `blp_client.health()` is the cheap first read; a `could not start blpapi session` is a HUMAN sign-in with a 2-attempt
  budget (`:41-48`) -- NEVER yours. If health reads `ok: false`, STOP the live criteria and file a BLOCKING row.
- Pool state for the validation names, MEASURED by the CRO's validation subagent 2026-09-18
  (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/INSTANTIATION_VALIDATION_REPORT_20260918.md:37-53`): `management/v1/`
  0 keys, `filings/v1/` 0 keys, crosswalk 0 records for CAT, CSL and Keyence. **Re-measure at spawn** -- `AMGT-rk-38`
  (the filings battery) may have landed a filings object for one of them by then, and then the filing wins.

**RULED -- what you build:**
1. **A new module `lib/research/management/bloomberg_fallback.py`** with `pull_exec_officers(security, blp=None, s3=None,
   write_raw=False) -> dict`: one `ReferenceDataRequest` on `[security]` with fields `["NAME", "COMPANY_EXEC_OFFICERS"]`
   through `blp_client.reference_data`; the FULL response landed untouched at
   `raw/bloomberg/<security_key>/<stamp>/exec_officers.json` when `write_raw` is true (never on a dry run); each
   entry parsed on the FIRST `,  ` (two spaces) into `name` and `title`, name kept verbatim after the package's
   declared ASCII fold (`roster.py:157-171`); a `__field_errors__` entry, a transport exception or an empty response
   returns `status: FAILED` with the cause; a well-formed response with zero entries returns `status: EMPTY`; otherwise
   `status: OK` with `entries_returned`, `officers`. **FAILED is never EMPTY** -- the same rule `C-EXEC-MANAGEMENT`
   `:742` sets for the SERP.
2. **`build_document` gains the fallback** at `enrich.py:494-496`: when `roster_status != RESOLVED`, call the fallback
   (the FILING result is kept whole: `roster_status`, `roster_reason`, `source_accession`, `source_key`, `source_item`,
   `parse_strategy` all stay as `build_roster` left them). On `OK` with at least one officer: `officers` = the
   Bloomberg rows, each `{name, role: <title>, role_start: null, role_start_basis: "absent", tenure_years: null,
   profile_url: null, lusha_title: null, source: "bloomberg", confirmed: true, enrichment: "NOT-ATTEMPTED", age: null}`;
   `roster_source: "BLOOMBERG_FALLBACK"`; `avg_tenure_years: null`; a top-level `fallback` block
   `{label: "officers per Bloomberg COMPANY_EXEC_OFFICERS -- no filing roster; Bloomberg carries no role start, so
   role start, tenure and the pool comparison are ABSENT", security: <yellow key>, field: "COMPANY_EXEC_OFFICERS",
   status, entries_returned, officers_parsed, raw_key, pulled_at, reason}`. On `EMPTY` or `FAILED`: `officers: []`,
   `roster_source: null`, the `fallback` block carrying the status and reason. When the filing IS RESOLVED:
   `roster_source: "FILING"`, the fallback is NOT called (call count 0 -- the planted control), and no `fallback`
   block is minted beyond `{status: "NOT-CALLED", reason: "the filing roster is RESOLVED"}`. `absence_reason_class`
   (`:540-546`) keeps classing the FILING's absence exactly as today -- the fallback never rewrites it.
3. **The schema** (`management.schema.json`): `roster_source` REQUIRED, enum `["FILING", "BLOOMBERG_FALLBACK", null]`
   with the rule in its description (null only when neither source produced an officer); `officer.source` enum
   `["filing", "bloomberg"]`; `confirmed` re-described as *"true when the person was read from the roster's own
   source"*; `fallback` block defined, `additionalProperties: false`, the same `not` clauses against contact keys.
   `validate()` (`enrich.py:460-472`) must pass on every object you write.
4. **The prints**: `enrich.main` (`:652-676`) adds `ROSTER-SOURCE: <FILING|BLOOMBERG_FALLBACK|NONE> officers N` and
   `BLOOMBERG-FALLBACK: status <s> entries <n> officers <n> raw <s3 key or none> -- <reason>`; the batch's census
   `integrations/bloomberg/research/management_posture_batch.py::cmd_report` (`:132-140`) adds ONE line
   `MANAGEMENT CONTENT: FILING <a> BLOOMBERG_FALLBACK <b> zero-officer <c> of <N> served object(s)` read from the
   newest object per served name (`:116-129` already lists served names). **You do not change what the batch
   RUNS** (`filed_names` `:110-113` stays the batch's ceiling; a fleet widening is a later cell after validation).
5. **A `--skip-pool` flag on `enrich.main`** so a per-name write (`:685-688`) does NOT recompute and rewrite
   `management/v1/_pool/<as_of>.json` (`:689-699`): the R14-E3 cell (analysis `:133`) owns the pool this round, and rewriting
   `_pool/2026-09-18.json` (rk-22's vintage) would move the pool comparison served on every 18-Sep object. Every
   live write in THIS order passes `--skip-pool`.
6. **The three validation names, and nothing wider**: `CAT US Equity` (`CAT_US_Equity`), `CSL AU Equity`
   (`CSL_AU_Equity`), `6861 JP Equity` (`6861_JP_Equity`) -- the canonical key is `<ROOT>_<CC>_Equity`
   (`lib/research/identity/crosswalk.py:334` @HEAD; `model_block_pull.py:63-64` `security.replace(" ", "_")`). A
   Bloomberg pull on these three is inside the validation Andrew set as the bar (`C-VALIDATION-NAMES`, PRD `:1652-1655`
   @`1699960261`). NO fleet run, NO re-run of the 33.

**This is a served-output-moving deploy (pool writes under `management/v1/`, a served prefix). It needs a FRESH
never-widen co-sign (CTO half + your COO's half), each naming the blast radius -- EXACTLY the three keys
`management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json` plus three raw landings at fresh stamps --
with the writers of that property COUNTED (three: `enrich.write_document` `:619-622` which this order runs;
`management_posture_batch.py` `management` which is NOT run; `batch.py` which is DISABLED and NOT run) and a rollback
read from the LIVE pre-act state of THIS act (the three keys are expected ABSENT pre-act: print `head_object` on each
and record 404 or the ETag; rollback = `delete_object` per key back to that state, bucket versioning the net).
Open your change-management ledger entry BEFORE your first `--write-pool` act, with `.tools/deploy_ledger.py` exactly
as `org/critical_paths/change_management/20260918T0031Z_amgt-rk25-thesis-bundle-as-of-date-20260917_deploy_completion.md`
records the shape; close it on completion, per NEVER-2.**

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis `ledger/ROUND_ANALYSIS.round13.md` s.4 row `R14-E5` (`:135`)
and s.5 card context @`9c8e04cd9a`; Andrew-direct ~17:1xZ card 1 (`ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md`
@`4f44431d34`); the Exec Management brief s.8.1 (`:186-209`) and the CTO's intake row E9 (`CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:176`).
PRD v0.13 @`1699960261`: `C-EXEC-MANAGEMENT` (`:722-757`), `C-PRODUCTION-HOME` (`:1643`), `C-VALIDATION-NAMES` (`:1652`).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain E is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-47`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-47` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/
integrations/bloomberg/research/management_posture_batch.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~49/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-47.bloomberg-officer-fallback.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read `integrations/bloomberg/mcp/blp_client.py`,
  `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/READ_HERE.md`,
  `lib/research/identity/crosswalk.py` and the pool); this block governs WRITES. `lib/research/api/scoped_amgt.py`,
  `portal/`, `lib/research/filings/` and `data/find/` are WALLS. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~49 <0.9.0_WK_AMGT_RESAPP~49@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **POOL WRITES** go through `lib/research/identity/crosswalk.py::write_pool` (`:609-640`, sha-256 metadata, read-back,
  `IfNoneMatch` on a fresh key) via `enrich.write_document` (`:619-622`) -- never a bare `put_object` on `management/v1/`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF** -- unrelated to this cell. **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets` only (this cell needs NONE: the
Bloomberg pull is the terminal's loopback pipe). **THE ONE VENDOR CALL THIS ORDER NAMES is Bloomberg DAPI on the
three validation names, inside the validation Andrew set as the bar** (PRD `:1652-1655` @`1699960261`). **No Lusha,
no Bright Data, no Anthropic, no Seeking Alpha call on this order** -- `domain_for` (`enrich.py:138-146`) returns no
domain for the three keys, so `build_document` makes neither call for them (`:511-514`, `:532`); if you ever see a
`LUSHA: CALLED` or a `SERP: query` other than `<none>` in your output, STOP and file a row. No non-ASCII in anything
you write (the fold at `roster.py:157-171` is what keeps Keyence's officers ASCII). **PUSH: never.** Your work is
LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure at spawn whether
`management/v1/<key>/` and `filings/v1/<key>/` exist for the three keys (the validation report read 0 and 0); if a
RESOLVED filing has landed for a name, that name's roster comes from it and `roster_source` reads FILING -- that is
the rule working, not a failure of AC3.
**NO FLEET RUN, NO RE-RUN:** the three keys above are the only `--write-pool` targets; the batch is never run.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W49-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** One known
candidate: Keyence's Bloomberg list may carry a "President" with no chief-executive title, so `find_ceo`
(`enrich.py:384-388`) finds nobody -- a row for `AMGT-rk-48`'s reader, not a defect of this cell.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-47"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_bloomberg_fallback -v 2>&1 | tail -n 25</invocation><expect>the new test module runs at least SIX named tests and ends "OK" with its "Ran N tests" denominator: (1) a RESOLVED filing fixture leaves roster_source FILING and the fallback call counter at 0; (2) an UNRESOLVED filing fixture (the empty-section reason from roster.py:534-540) plus a stubbed Bloomberg response of three "<name>,  <title>" entries yields roster_source BLOOMBERG_FALLBACK, three officers with source "bloomberg", role_start null, tenure_years null, AND the object still carries roster_status UNRESOLVED-SOURCE with the filing's own roster_reason; (3) a stubbed EMPTY response yields officers [] and roster_source null with fallback.status EMPTY; (4) a stubbed __field_errors__ / raised exception yields fallback.status FAILED with the cause, and the test asserts FAILED != EMPTY; (5) a name with two spaces and a nickname in quotes parses with the name kept verbatim; (6) validate() passes on the fallback object and on the FILING object, and contact_fields_present() is 0 on both</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-47"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import importlib.util, json, pathlib
spec = importlib.util.spec_from_file_location('blp_client', pathlib.Path('integrations/bloomberg/mcp/blp_client.py'))
blp = importlib.util.module_from_spec(spec); spec.loader.exec_module(blp)
print('health', blp.health())
from lib.research.management import bloomberg_fallback as fb
names = ['CAT US Equity', 'CSL AU Equity', '6861 JP Equity']
ok = 0
for sec in names:
    r = fb.pull_exec_officers(sec, blp=blp, write_raw=False)
    ok += 1 if r['status'] == 'OK' else 0
    print(sec, 'status', r['status'], 'entries', r.get('entries_returned'), 'officers', len(r.get('officers') or []), 'reason', r.get('reason'))
    for o in (r.get('officers') or [])[:3]:
        print('   ', json.dumps(o, ensure_ascii=True))
print('DENOMINATOR: OK %d of %d validation names; raw written: NONE (write_raw=False)' % (ok, len(names)))
"</invocation><expect>health prints ok True (if it prints ok False, STOP: a human sign-in per integrations/bloomberg/READ_HERE.md section 2, file a BLOCKING row, refuse AC2-AC4); each of the three validation names prints status OK or a stated FAILED/EMPTY reason (never a silent empty), officers with name and title as Bloomberg returned them, ASCII only; the DENOMINATOR line reads "OK N of 3" with N printed as measured; nothing is written to the pool on this criterion</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-47"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, datetime, json, subprocess, sys
s3 = boto3.client('s3', region_name='us-east-1')
B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
keys = ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']
def etag(k):
    try: return s3.head_object(Bucket=B, Key=k)['ETag']
    except Exception as e: return 'ABSENT (%s)' % type(e).__name__
pool_key = 'management/v1/_pool/%s.json' % as_of
print('PRE-ACT pool object', pool_key, etag(pool_key))
for k in keys:
    print('PRE-ACT', 'management/v1/%s/%s.json' % (k, as_of), etag('management/v1/%s/%s.json' % (k, as_of)))
for k in keys:
    rc = subprocess.call([sys.executable, '-m', 'lib.research.management.enrich', '--security-key', k, '--as-of', as_of, '--write-pool', '--skip-pool'])
    print('RC', k, rc)
print('POST-ACT pool object', pool_key, etag(pool_key))
written = 0
for k in keys:
    key = 'management/v1/%s/%s.json' % (k, as_of)
    try:
        doc = json.loads(s3.get_object(Bucket=B, Key=key)['Body'].read())
        written += 1
        print('POST-ACT', key, 'roster_source', doc.get('roster_source'), 'roster_status', doc.get('roster_status'), 'officers', len(doc.get('officers') or []), 'fallback', (doc.get('fallback') or {}).get('status'), 'raw', (doc.get('fallback') or {}).get('raw_key'), 'roster_reason', (doc.get('roster_reason') or '')[:90])
    except Exception as e:
        print('POST-ACT', key, 'READ FAILED', type(e).__name__)
print('DENOMINATOR: %d of %d management objects written; pool object unchanged' % (written, len(keys)))
"</invocation><expect>the PRE-ACT lines print the live state of the three management keys (expected ABSENT -- record whatever is measured, it is the co-sign's rollback baseline) and of the pool object; every RC is 0; each POST-ACT line shows roster_source BLOOMBERG_FALLBACK with officers greater than 0, fallback OK and a raw key under raw/bloomberg/<key>/<stamp>/exec_officers.json -- OR, for a name whose filing AMGT-rk-38 has landed RESOLVED by spawn time, roster_source FILING with fallback NOT-CALLED -- OR a stated EMPTY/FAILED with roster_source null and officers 0, never a silent skip; the roster_reason of the FILING side is still on the object whenever the filing did not resolve; the pool object's ETag is IDENTICAL before and after (the --skip-pool control); the DENOMINATOR reads 3 of 3</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-47"><invocation>cd "$(git rev-parse --show-toplevel)" && python integrations/bloomberg/research/management_posture_batch.py report 2>&1 | grep -E "KEYED POPULATION|MANAGEMENT CEILING|MANAGEMENT CONTENT"</invocation><expect>the report prints its existing KEYED POPULATION and MANAGEMENT CEILING lines unchanged in shape, plus the new line "MANAGEMENT CONTENT: FILING a BLOOMBERG_FALLBACK b zero-officer c of N served object(s)" where a + b + c equals N and N is the count of served names read live (the three validation keys are NOT in the crosswalk, so they are counted only if served_names lists them -- state which); the report makes no vendor call and writes nothing</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. **AC3 runs AFTER your change-management entry is OPEN and the never-widen pair is on file; AC2 and AC4 write
nothing and may run before.**

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~49/AMGT_RESAPP.TO-AMGT-rk-47.bloomberg-officer-fallback.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; close the change-management entry; commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-48`
(the CEO search) is handed to you next as a continuation on this same slot; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~49</slot>
<fabric>site-z</fabric>
