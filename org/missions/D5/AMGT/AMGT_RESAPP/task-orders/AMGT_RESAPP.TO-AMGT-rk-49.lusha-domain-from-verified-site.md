# AMGT_RESAPP task order -- `AMGT-rk-49` -- Lusha enrichment as an instantiation step: the domain ONLY from the battery's verified site; no verified domain = NOT ATTEMPTED with its reason -- GATED ON `AMGT-rk-38`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-49</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~50</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the weekly
  OpalResearch-ExecManagement task stays DISABLED and is neither read nor written; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  s3://opal-data-harvest management/v1/ prefix this project already writes) under the box's existing AWS
  credentials; it grants no permission and provisions no resource; no Lambda, no Terraform. The Lusha key
  reaches the process only as LUSHA_API_KEY exported by the caller from comp-secrets (enrich.py:243-248).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~50`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`,
`lib/research/management/` and `data/find/imo/scripts/_util/lusha_client.py` exist; if any is absent, STOP with a
BLOCKING row. **THIS ORDER IS GATED: it is fed to you only after `AMGT-rk-38` (the filings battery, R14-F1) is
terminal, because the domain this cell uses exists nowhere except on the filings object that order lands. Your
second act reads `AMGT-rk-38`'s order file in `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/` (glob
`AMGT_RESAPP.TO-AMGT-rk-38.*.md`) and its instance, and names in your report the EXACT field on the filings source
object that carries the battery's VERIFIED site; if `AMGT-rk-38`'s `<status>` is not `complete`, STOP with a
BLOCKING row.** `AMGT-rk-47` and `AMGT-rk-48` (slot `~49`) edit `enrich.py::build_document` before you; your edits
are confined to `domain_for()` and the Lusha block, so a drain after theirs merges cleanly -- if your worktree's
`enrich.py` lacks `roster_source` or `--skip-pool`, they have not drained yet: STOP with a row. Every Bash call
begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~50;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-49` (R14-E7; FWD-17; Andrew's card 2 and card 4; PRD v0.13 `C-EXEC-MANAGEMENT`, `C-VALIDATION-NAMES`)

**THE ANALYSIS ROW, VERBATIM** (`ledger/ROUND_ANALYSIS.round13.md:136` @`9c8e04cd9a`): *"R14-E7 -- Lusha enrichment as an
instantiation step (card 2): domain ONLY from the battery's verified site; no verified domain = NOT ATTEMPTED with
its reason"* -- serves FWD-17, card 2; **gated on R14-F1** (= `AMGT-rk-38`).

**ANDREW'S WORD, VERBATIM.** Card 2 (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md:13`
@`4f44431d34`): *"2.) Yes they should."* to *"Should LinkedIn profile lookups (Lusha, a paid service at 2 credits a
company) be part of setting up a new security?"*; read narrow (`:21-22`): *"Lusha profile links are a step of
instantiating a new security. He chose not to wait for the validation."* Card 4, the Lusha calls INSIDE the
three-name validation (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md:9`
@`4de34f0d95`): *"2.) Yes full egress."* -- ruled at `:19`: *"Lusha calls are authorized inside the instantiation
validation (Caterpillar, CSL, Keyence) with NO credit ceiling ... scoped to the call it answered -- Lusha within the
validation -- and NOT as a standing grant for Lusha across the covered population."* Landed as PRD v0.13
`C-VALIDATION-NAMES`, `prd/AMGT_RESAPP_PRD.md:1656-1657` @`1699960261`.

**THE RATIFIED TEXT YOU IMPLEMENT** -- PRD v0.13 `C-EXEC-MANAGEMENT`, `:735-739` @`1699960261`: *"Enrichment (Lusha
profile link and title) is a step of instantiating a new security. It attaches to an officer that the roster's own
source confirmed; Bloomberg-fallback officers are enrichable, and the label says which source applies. The company
domain comes ONLY from the site the filings battery VERIFIED as the right entity -- never a hand list, never
Bloomberg's raw web address. A name with no verified domain records Lusha as NOT ATTEMPTED, with that reason. Lusha
is never the roster. Each Lusha call is billed and runs only under Andrew's per-use word."* And `C-PRODUCTION-HOME`
(`:1643-1650`): configuration lives beside its producer under version control; a dry run writes nothing, anywhere.

**THE MEASURED STATE, at HEAD (`da7b0b1804`; the management package is byte-identical from `9c8e04cd9a` through HEAD):**
- `lib/research/management/enrich.py::domain_for` (`:138-146`) reads the HAND TABLE `domains.json` (`:56`, `:133-135`)
  -- five declared names (`domains.json:31-62`: BA, COST, HD, SAP, BABA); a name not in it returns no domain and the
  reason *"no declared domain ... in domains.json (%d name(s) declared)"* (`:143-145`). The table's own `basis`
  (`domains.json:29`) says why a guessed domain is refused: *"a guessed domain would silently enrich one company's
  roster with another company's people"*. **That rule stays; its SOURCE changes.**
- `build_document` (`:490-550`): the Lusha block is built at `:497-505` (`lusha_meta`, `absence_reason_class`
  pull-missed while SKIPPED, `:501-505`); the one billable call is `prospecting_page` (`:272-311`) via `_lusha_client`
  (`:236-256`, key from `LUSHA_API_KEY`, exported from `comp-secrets get find-insure/lusha-ai/api-key`, `:246-248`);
  the c-suite filter (seniority 9) is tried first and a refused filter is charged nothing (`:277-283`); `scrub` runs
  before anything is built (`:515`); `attach_profiles` (`:341-363`) matches on surname plus a compatible given name
  (`name_matches` `:321-338`), a near-miss is never a match; the MEASURED `creditsCharged` is recorded, never clipped
  to the bound (`:516-526`, `CREDIT_BOUND_PER_NAME = 2` at `:51`); officers with no domain read `NOT-ATTEMPTED`
  (`:528-530`). The Lusha client's per-call meta carries `credits_charged` from `billing.creditsCharged`
  (`data/find/imo/scripts/_util/lusha_client.py:55`, `:263-273`).
- The schema's `lusha_meta` (`management.schema.json:161-179`) carries `status CALLED | SKIPPED`, `domain`,
  `credits_used` (*"the MEASURED creditsCharged ... never clipped to the bound"*), `matched`, `reason`,
  `absence_reason_class` (*"pull-missed while SKIPPED (a domain this project has not yet declared ...)"*). It has no
  field saying WHERE the domain came from.
- Bloomberg's raw web address is NOT a domain source: it points at a subsidiary or branch site for HSBC, ICICI Bank
  and SSE (Exec Management brief `:92`, `:164-165`, `:218-220`), and CSL's hint `www.csl.com.au` is not where the report
  is hosted (`investors.csl.com`, validation report `:117-118`).
- **The battery's VERIFIED site** is the Thesis battery's step 4 -- *"the company's own site, found by web search"*
  with the entity test (a) *"the right entity"* (Thesis brief `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md:229-241`;
  validation report s.3, acceptance test (a)). MEASURED on the validation names (`INSTANTIATION_VALIDATION_REPORT_20260918.md:86-137`):
  CSL's winner is step 4 on `investors.csl.com` (PASS on name, ABN and ASX code); Keyence's winner is step 4 on its
  IR library (PASS: the cover's English name matches Bloomberg); **CAT's winner is step 1 (EDGAR) -- no company-site
  step ran for it.** So at this cut CAT is the ORGANIC negative arm of this cell (no verified site => NOT ATTEMPTED
  with that reason) unless `AMGT-rk-38` records a verified site for every name; you read what it landed and say which.
- The filings source object is built at `lib/research/filings/fetch.py:425-448` and persisted at `pool_key`
  (`:451-452`) under `filings/v1/<security_key>/<accession>.source.json`; `roster.load_source_object`
  (`roster.py:472-498`) reads the LATEST accession, and `build_document` already holds that object as `source_object`
  (`enrich.py:493`) -- the verified site is read from THAT object, no second read.
- The management objects for the three validation names are the ones `AMGT-rk-47`/`AMGT-rk-48` wrote at
  `management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json`; their officers are FILING or
  BLOOMBERG_FALLBACK rows (`roster_source`), each with `source` filing | bloomberg. **Re-measure at spawn.**
- A full `build_document` re-run would re-pull Bloomberg and RE-BILL the CEO search (`AMGT-rk-48`'s SERP and model
  calls). This cell must not.

**RULED -- what you build:**
1. **`domain_for(security_key, source_object)`** (`enrich.py:138-146`, signature widened; `domains.json` no longer read on
   this path): the domain comes ONLY from the filings object's verified-site field as `AMGT-rk-38` named it. Returns
   `(company_domain, ir_domain, reason, basis)` where `basis` is `{domain_source: "battery-verified-site",
   verified_site: <url or host as landed>, verified_host: <host>, rule: <the label rule applied>}`. **The rule, DECLARED
   and printed, never an eTLD+1 guess:** `company_domain` = the verified host with exactly ONE leading label removed
   when that label is in the allow-list `("www", "ir", "investors", "investor", "corporate")`, otherwise the host
   unchanged (`investors.csl.com` -> `csl.com`; `www.keyence.co.jp` -> `keyence.co.jp`; a bare `boeing.com` stays);
   `ir_domain` = the verified host. No verified site on the object (field absent, null, empty, or the object itself
   absent or UNRESOLVED) returns `(None, None, "<the reason naming the field and the battery step>", basis with
   domain_source null)`. **Nothing reads `domains.json` for a Lusha decision any more**; the file stays on disk for
   `batch.plan`'s dry-run census (`batch.py:97`, not your surface) and gains one line in its `basis` saying it is
   RETIRED as a Lusha input by this cell. A `bloomberg_web_address`-shaped field on the source object, if any, is
   IGNORED by construction (a planted test proves it).
2. **The Lusha block** (`:497-505`, schema `:161-179`): `lusha_meta` gains `domain_source` (enum
   `["battery-verified-site", null]`), `verified_site`, `domain_rule`; `reason` on SKIPPED reads the verified-site
   reason; `absence_reason_class` stays `pull-missed` while SKIPPED (no verified site is the battery not having
   verified one, never a fact about the company -- keep the description honest to that). Officers stay
   `NOT-ATTEMPTED` on SKIPPED (`:528-530`), `enrichment` MATCHED | ABSENT per officer on CALLED, and the label of which
   roster source confirmed the officer is the row's own `source` (`filing` | `bloomberg`) -- Bloomberg-fallback
   officers ARE enrichable (`:735-736`), nothing filters them out.
3. **`--enrich-only`** on `enrich.main`: loads the NEWEST existing management object for the name from the pool (the
   newest `<as_of>.json` under `management/v1/<key>/`, never a listing split on `/`), loads the filings source object
   the same way `build_document` does, runs ONLY steps 1-2 above on that object's officers (no Bloomberg pull, no
   SERP, no model call), validates, and with `--write-pool --skip-pool` writes it back under the SAME `as_of` through
   `write_document`. With `--dry-run` it prints the decision and the derived domain and writes NOTHING and calls
   NOTHING (`_lusha_client` is never constructed -- a counter proves it). The `LUSHA:` print (`:659-663`) gains
   `domain-source <s> verified-site <v> rule <r>`, and `credits-used N` stays the MEASURED value -- **the credit cost
   is the denominator of every live call and is printed on every line and summed in your report.**
4. **The tests** (`lib/research/management/tests/test_lusha_domain.py`, offline, a stubbed Lusha client): (a) a source
   object whose verified site is `https://investors.csl.com/...` derives `csl.com` with the rule printed; (b) a source
   object with NO verified site => SKIPPED, `NOT-ATTEMPTED` on every officer, the reason names the field and the step,
   the client constructor counter reads 0; (c) a verified site with an EMPTY officer list => SKIPPED with reason "no
   officers to enrich"; (d) **the planted hand-list negative**: `BA_US_Equity`, which `domains.json` declares, with a
   source object carrying no verified site => SKIPPED (the hand list no longer feeds a call); (e) **the planted
   Bloomberg-address negative**: a source object carrying `bloomberg_web_address: "www.example-branch.com"` and no
   verified site => SKIPPED, and the address never appears in `lusha_meta.domain`; (f) a CALLED path with a stub
   returning two records and `credits_charged: 2` matches by `name_matches`, records `credits_used 2`, `domain_source
   battery-verified-site`, and `contact_keys_removed` counts a planted `email` key; (g) `validate()` passes on every
   object above and `contact_fields_present()` is 0.
5. **The live run, on the three validation names only**, `--enrich-only --write-pool --skip-pool`, `LUSHA_API_KEY`
   exported from `comp-secrets get find-insure/lusha-ai/api-key --reveal` in the same shell call: one prospecting page
   per name that has a verified domain and at least one officer (`CREDIT_BOUND_PER_NAME` stays 2, the module's own
   design bound -- Andrew's "no credit ceiling" removes the CARD's ceiling, not the module's per-name rule);
   expected spend at most 6 credits, MEASURED and printed. **This is the authorized Lusha call: inside the
   validation, on these three names, under `C-VALIDATION-NAMES` `:1656` @`1699960261`.** Any name without a verified
   site reads SKIPPED / NOT ATTEMPTED with its reason -- that is the cell's rule working and is recorded as such.

**Served output:** this order rewrites the same three `management/v1/<key>/<as_of>.json` objects `AMGT-rk-47` and
`AMGT-rk-48` wrote (the `lusha_enrichment` block and the officers' `profile_url` / `lusha_title` / `enrichment`
fields). The analysis marks this cell *gated on R14-F1*, not co-sign; the COO states in your spawn prompt whether the
chain-E never-widen pair already names these keys' rewrite (the same three keys, the same three writers) or whether
a fresh pair is on file -- **you make no live write until the spawn prompt says which.** Print each key's pre-act
`document-sha256` and `VersionId` (the rollback baseline) before the write.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis `ledger/ROUND_ANALYSIS.round13.md` s.4 row `R14-E7` (`:136`)
and s.5 card 4 (`:166-172`, `:188-189`) @`9c8e04cd9a`; Andrew-direct ~17:1xZ card 2 and ~19:4xZ card 4 (records cited
above); the Exec Management brief s.8.2 (`:211-228`) and the CTO's intake (`CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:202-205`).
PRD v0.13 @`1699960261`: `C-EXEC-MANAGEMENT` (`:722-757`), `C-PRODUCTION-HOME` (`:1643`), `C-VALIDATION-NAMES` (`:1652-1657`).
Upstream: `AMGT-rk-38` (the battery; the verified site on the filings object), `AMGT-rk-47` (`roster_source`, the
enrichable fallback rows, `--skip-pool`), `AMGT-rk-48` (the CEO block this cell must not re-bill).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~50/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-49.lusha-domain-from-verified-site.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read `lib/research/filings/fetch.py`,
  `data/find/imo/scripts/_util/lusha_client.py`, `AMGT-rk-38`'s order and instance, and the pool); this block governs
  WRITES. `lib/research/filings/`, `data/find/`, `integrations/`, `lib/research/api/` and `portal/` are WALLS.
  `lib/research/management/batch.py` and `bloomberg_fallback.py` and `ceo_search.py` are inside your grant but NOT
  yours to edit (other cells' work); your edits are `enrich.py` (`domain_for`, the Lusha block, `--enrich-only`,
  the print), `management.schema.json` (`lusha_meta`), `domains.json` (one `basis` line) and the new test file.
  Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~50 <0.9.0_WK_AMGT_RESAPP~50@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **POOL WRITES** go through `crosswalk.write_pool` via `enrich.write_document` (`:619-622`) -- never a bare `put_object`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only, exported into the environment of the one shell call that
runs the live criterion, never written to a file, never printed. **THE ONE VENDOR CALL THIS ORDER NAMES is Lusha
`contacts/prospecting`, one page per validation name that carries a verified domain and officers, authorized inside
the validation by Andrew's card-4 word (*"Yes full egress"*, PRD `:1656` @`1699960261`) -- and NOT a standing grant:
no other name, no re-run, no second page.** No Bloomberg, no Bright Data, no Anthropic, no Seeking Alpha call on this
order (`--enrich-only` makes none by construction; if the `SERP:` or `BLOOMBERG-FALLBACK:` print shows a call, STOP and
file a row). No contact data point is stored at any level (`scrub`, `validate`). No non-ASCII in anything you write.
**PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular, a name with no verified site is
NEVER given a domain from `domains.json`, from Bloomberg's web address, or from your own knowledge to make AC3 read
CALLED.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure at spawn, per
validation name: whether a filings object exists and carries the verified-site field, and how many officers the
management object carries.
**NO FLEET RUN, NO RE-RUN:** the three keys are the only targets; the batch is never run; the 33 are untouched.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W50-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** One known
candidate for a row, not a widening: a name the battery resolves at EDGAR (step 1) never reaches step 4, so a US name
has no verified site and no enrichment under this rule -- the L4's to settle, recorded with CAT's measured outcome.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-49"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_lusha_domain -v 2>&1 | tail -n 30</invocation><expect>the module ends "OK" with its "Ran N tests" denominator (N at least 7) and lists, by name, the seven cases of section 1 item 4 passing: the CSL-shaped verified site derives csl.com with the rule printed; no verified site reads SKIPPED with NOT-ATTEMPTED on every officer and a client-constructor count of 0; a verified site with no officers reads SKIPPED "no officers to enrich"; the PLANTED hand-list name BA_US_Equity with no verified site reads SKIPPED (domains.json no longer feeds a call); the PLANTED bloomberg_web_address is never used as a domain; the stubbed CALLED path records credits_used 2, domain_source battery-verified-site and a scrubbed planted email key; every object validates with 0 contact fields</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-49"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import datetime, io, contextlib
from lib.research.management import enrich
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
calls = {'n': 0}
orig = enrich._lusha_client
def counting(*a, **k):
    calls['n'] += 1
    return orig(*a, **k)
enrich._lusha_client = counting
decided = 0
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = enrich.main(['--security-key', k, '--as-of', as_of, '--enrich-only', '--dry-run'])
    out = buf.getvalue()
    lusha = [l for l in out.splitlines() if l.startswith('LUSHA:')]
    print(k, 'RC', rc, lusha[0] if lusha else 'NO LUSHA LINE')
    decided += 1 if lusha else 0
print('DENOMINATOR: %d of 3 names decided; lusha client constructed %d time(s); nothing written (dry run)' % (decided, calls['n']))
"</invocation><expect>every RC is 0; each name prints ONE LUSHA: line reading either "SKIPPED ... domain-source None verified-site None ... -- <reason naming the verified-site field and battery step 4>" or "WOULD-CALL ... domain-source battery-verified-site verified-site <host> rule <rule>" (the dry run never reads CALLED); at this cut CSL and Keyence are expected to carry a verified site and CAT is expected SKIPPED (EDGAR winner, no site step) -- record what is measured, either way is the rule working; the client was constructed 0 times; denominator 3 of 3</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-49"><invocation>cd "$(git rev-parse --show-toplevel)" && export LUSHA_API_KEY="$(comp-secrets get find-insure/lusha-ai/api-key --reveal)" && python -c "
import boto3, datetime, io, contextlib, json
from lib.research.management import enrich
s3 = boto3.client('s3', region_name='us-east-1'); B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
credits = 0; written = 0
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    key = 'management/v1/%s/%s.json' % (k, as_of)
    h = s3.head_object(Bucket=B, Key=key); print('PRE-ACT', key, 'sha', h['Metadata'].get('document-sha256'), 'version', h.get('VersionId'))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = enrich.main(['--security-key', k, '--as-of', as_of, '--enrich-only', '--write-pool', '--skip-pool'])
    out = buf.getvalue()
    for line in out.splitlines():
        if line.startswith(('LUSHA:', 'LUSHA-UNMATCHED:', 'OK: uploaded', 'BLOCKED:', 'SERP:', 'BLOOMBERG-FALLBACK:')):
            print(k, line)
    doc = json.loads(s3.get_object(Bucket=B, Key=key)['Body'].read()); meta = doc.get('lusha_enrichment') or {}
    credits += int(meta.get('credits_used') or 0); written += 1 if rc == 0 else 0
    print('POST-ACT', k, 'RC', rc, 'status', meta.get('status'), 'domain', meta.get('domain'), 'domain_source', meta.get('domain_source'), 'credits_used', meta.get('credits_used'), 'matched', meta.get('matched'), 'of', len(doc.get('officers') or []), 'reason', (meta.get('reason') or '')[:100])
print('DENOMINATOR: %d of 3 objects written; credits charged in total %d (bound 2 per name, 6 over the run)' % (written, credits))
"</invocation><expect>three PRE-ACT baselines printed; every RC 0; each POST-ACT line reads status CALLED with domain_source battery-verified-site, a MEASURED credits_used (expected 2, printed whatever it is) and "matched M of K" officers -- OR status SKIPPED with credits_used 0, domain None and the verified-site reason; no SERP: and no BLOOMBERG-FALLBACK: line reports a call; the total credits line prints the run's whole cost as its denominator (at most 6 expected; a value above 2 on any one name is reported as the WARN the module already writes, never hidden); the secret value never appears in the output</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-49"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, datetime, json
from lib.research.management import enrich
s3 = boto3.client('s3', region_name='us-east-1'); B = 'opal-data-harvest'
as_of = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
hand = set((enrich.load_domains().get('domains') or {}).keys())
objects = 0; contact = 0; hand_hits = 0; consistent = 0
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    doc = json.loads(s3.get_object(Bucket=B, Key='management/v1/%s/%s.json' % (k, as_of))['Body'].read()); objects += 1
    ok, errors = enrich.validate(doc); contact += len(enrich.contact_fields_present(doc))
    meta = doc.get('lusha_enrichment') or {}
    hand_hits += 1 if (k in hand and meta.get('status') == 'CALLED' and meta.get('domain_source') != 'battery-verified-site') else 0
    offs = doc.get('officers') or []
    if meta.get('status') == 'SKIPPED':
        consistent += 1 if all(o.get('enrichment') == 'NOT-ATTEMPTED' for o in offs) else 0
    else:
        consistent += 1 if all(o.get('enrichment') in ('MATCHED', 'ABSENT') for o in offs) and meta.get('domain_source') == 'battery-verified-site' else 0
    print(k, 'schema-valid', ok, errors[:2], 'status', meta.get('status'), 'domain_source', meta.get('domain_source'), 'verified_site', meta.get('verified_site'), 'roster_source', doc.get('roster_source'), 'linked', sum(1 for o in offs if o.get('profile_url')), 'of', len(offs))
print('DENOMINATOR: %d objects read back; officer/meta consistent %d of %d; hand-list-fed calls %d; contact fields stored %d' % (objects, consistent, objects, hand_hits, contact))
"</invocation><expect>3 objects read back, each schema-valid True; officer/meta consistency 3 of 3 (SKIPPED objects have every officer NOT-ATTEMPTED; CALLED objects have every officer MATCHED or ABSENT and domain_source battery-verified-site); hand-list-fed calls 0 (the discriminator against the retired domains.json path); contact fields stored 0; the linked counts printed beside each officer count -- a get_object read-back and validate(), a different instrument from the writer's own print</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. **AC1 and AC2 write nothing and call nothing; AC3 runs only after the spawn prompt's word on the never-widen
pair (section 1, last paragraph) and is the ONE billable act of this order; AC4 after AC3.**

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~50/AMGT_RESAPP.TO-AMGT-rk-49.lusha-domain-from-verified-site.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, with the total credits charged and the exact
verified-site field name on the first line.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**PARTIAL SUPERSEDE (2026-09-22, CTO ruling msg 24263, on the COO's round-28 issuance note 2):** this order's
DOMAIN-FROM-VERIFIED-SITE half is SUPERSEDED by `AMGT-rk-110` (round 28), drained @`1c8140c9d8`. With no domains.json
row, `enrich.domain_for` / `lusha._cli` now fall back to `verified_domain_for(source_object)`, and never to
`ceo_public_profile` or a seed URL. The REMAINDER of this order (the live Lusha enrichment, gated on the key ROTATION)
stays HELD, and its status stays open until Andrew says the key is rotated. The `wk-amgt-14-50` worktree is untouched.

<status>pending</status>
<round>14</round>
<slot>~50</slot>
<fabric>site-z</fabric>
