# AMGT_RESAPP task order -- `AMGT-rk-43` -- honesty first: the CEO line prints the object's own states, an empty roster renders its reason, a zero-officer object is not SERVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-43</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~45</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected; the DISABLED task OpalResearch-ExecManagement is
  neither read nor written by this order (it is AMGT-rk-44's).
comp-iam: DECLARED-NOT-APPLICABLE -- this order redeploys the existing Lambda opal-amgt-scoped-api from HEAD under
  its existing execution role (module.scoped_amgt_api, infra/aws/terraform/harvest/scoped-amgt-api.tf:230); it
  grants no new permission, provisions no new resource, and writes no pool object.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~45`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/api/`
and `portal/src/pages/SecurityAnalysis/` exist (the last is a SEPARATE git repository checked out inside `portal/`,
branch `DEV`; if it is absent, STOP with a BLOCKING row -- R14-T6 provisions it, and this order cannot run without
it). **You hold `lib/research/api/scoped_amgt.py` WHOLE-FILE for this order's duration: that file is a single-writer
surface shared with other chains, and the COO sequences every other order that touches it after yours.** Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~45;`. **NEVER RUN AN INSTALL** (`bun install` against the
EXISTING portal lockfile is the one exception, and only if `portal/node_modules/.bin/tsc` is absent).

## 1. THE CELL, inlined in full -- `AMGT-rk-43` (R14-E1; FWD-17; intake rows E1, E4, E11; round-13 row W32-S2 folded here)

**The analysis row, verbatim** (`ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`): *"honesty first: the CEO line prints
four states honoring the object's own `absence_class`; an empty roster renders its reason; a zero-officer object is
not SERVED"* -- serves FWD-17, E1, E4, E11; co-sign YES.

**THE MEASURED STATE (read at HEAD `4f44431d34`; the pool read 2026-09-18 ~20:xxZ by the drafting seat -- RE-MEASURE
AT SPAWN).**
- The served plane: `management/v1/` carries 12 per-name objects (BA, BABA, COST, HD, SAP_GY at `2026-09-15`; ASML, HAL,
  INTU, KMB, NU, PBR, VLO at `2026-09-18`) plus two `_pool` objects. **12 read SERVED by status; 7 carry at least one
  officer; 5 (ASML, HAL, INTU, KMB, PBR) carry ZERO officers with `roster_status` UNRESOLVED-SOURCE** -- ASML/PBR because
  the persisted 20-F's Item 6 was cut EMPTY (`roster.py:534-540`), HAL/INTU/KMB because no declared shape read the
  section (`roster.py:461-465`). The adapter serves all 12 as `management_status: SERVED` because `read_management()`
  (`scoped_amgt.py:2305-2371`) flips SERVED the moment an object parses (`:2346-2348`), never reading the officer count.
- The page (`portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`, portal `625a0888`): `ManagementBody`
  (`:95-137`) renders any SERVED block as "N officer(s) from <item>" over the table -- for a zero-officer object that is
  "0 officer(s) from Item 6 ..." over an EMPTY table (E11); `roster_status` and `roster_reason` ride the payload
  (`:2350-2351` of the adapter) and are never rendered.
- The CEO line: `ceo_profile_reading()` (`scoped_amgt.py:2275-2302`) reads the M-1 object's `basis` SENTENCE with a
  regex (`_SERP_URL_COUNT_RE`, `:2272`) and maps "no url count named" to `NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY`
  (`:2291-2296`); `CeoProfile` (`ExecManagementTab.tsx:70-93`) then prints a HARD-CODED sentence for that value --
  *"the links it returned do not expose a readable host"* (`:87`). **For 7 of the 12 objects NO SEARCH RAN**: the
  producer returns before any query when the roster has no CEO (`enrich.py:417-421`, the five empty rosters) or when
  no IR domain is declared (`enrich.py:423-425`; NU and VLO -- `domains.json` declares only the five pilot names, row
  W32-S2). Every one of those objects carries `query: null` and the DEFAULT `absence_class: NOTHING_FOUND`
  (`enrich.py:414-416`), which the reader ignores. Measured split over the 12: **1 CONFIRMED (SAP), 4 searched with
  links not resolved to the IR host (CANNOT_SAY), 7 never searched.** The page tells the reader a search failed on
  seven names where none ran (E4) -- present-and-wrong, not absent-and-honest.
- The officer table's profile cell (`ExecManagementTab.tsx:43-51`) prints "ABSENT (no match)" for EVERY officer without
  a `profile_url` -- including the officers of names where Lusha was never called (`enrichment: NOT-ATTEMPTED`,
  `enrich.py:528-530`; `lusha_enrichment.status: SKIPPED` with its reason, `enrich.py:498-505`). That is W32-S2's
  fold: the reader is told a match was attempted and failed.
- One instrument trap, named so it is not repeated: the "opaque redirect wrapper" label on the four CANNOT_SAY objects is
  the producer's OWN and is STALE (brief UPDATE 3 s.10 item 1: 50 of 50 organic links were direct URLs on 18 Sep). The
  honest text for that state is "the search returned N link(s); none resolved to the company's IR domain; the module did
  not follow them" -- a fact about the module, never about the zone.

**RULED -- what this order builds.**
1. **The adapter (`lib/research/api/scoped_amgt.py`).**
   (a) `ceo_profile_reading(profile)` (`:2275-2302`) is rewritten to read the object's OWN FIELDS -- `status`, `url`,
   `query`, `absence_class`, `basis` -- and never to derive a state from a parsed sentence. Its readings, defined BY
   SUBTRACTION over every M-1 `ceo_public_profile` object (`management.schema.json:142-160`):
   - `CONFIRMED` -- `status == "RESOLVED"` and `url` non-null;
   - `NOT_SEARCHED` -- `status == "ABSENT"` and `query` is null (the producer returned before any query: no CEO on the
     roster, roster unresolved, or no declared IR domain -- `enrich.py:417-425`, `:532-536`);
   - `SEARCHED_NOTHING_FOUND` -- `status == "ABSENT"`, `query` set, `absence_class == "NOTHING_FOUND"`, and `basis` does
     not begin `"the SERP primitive raised"`;
   - `SEARCHED_LINKS_UNREADABLE` -- `status == "ABSENT"`, `query` set, `absence_class == "CANNOT_SAY"`;
   - `SEARCH_FAILED` -- `status == "ABSENT"`, `query` set, and `basis` begins `"the SERP primitive raised"`
     (`enrich.py:431-433`, the one path where the producer records a failure; today it leaves the DEFAULT
     `absence_class` NOTHING_FOUND in place, so the field alone would misread it -- this is the ONE string test kept,
     and it tests a fixed prefix the producer writes, not a free sentence);
   - `UNREADABLE_OBJECT` -- anything else (no dict, a status outside the enum): the reading prints the fields it saw.
   The returned dict carries `reading`, `reading_basis` (the FIELD NAMES the reading was taken from, e.g.
   `"status=ABSENT query=null"`), `reason` (the object's own `basis` text, verbatim, ASCII) and `urls_returned` (parsed
   from `basis` for information only, null when absent -- NEVER an input to the reading). PRD v0.13 @`1699960261`
   `C-EXEC-MANAGEMENT` (`:748-750`) names FIVE page states including "SEARCHED, NOTHING KEPT"; that fifth arrives with
   R14-E6's `ceo_profile` block and is NOT reachable on any object this order serves, so it is not a reading here --
   said, not omitted.
   (b) `read_management()` (`:2305-2371`): a document whose `roster_status` is not RESOLVED, OR whose `officers` list is
   empty, is served `management_status: ABSENT` with `absent_because: "ZERO_OFFICERS"` and `reason` = the object's own
   `roster_reason` (or the literal `"the object carries 0 officers and no roster_reason"` when that is null); the block
   KEEPS `as_of`, `roster_status`, `roster_reason`, `absence_reason_class`, `absence_reason_evidence`,
   `source_accession`, `source_item`, `officer_count: 0`, `management_read` (so a reader can tell "an object landed and
   is empty" from "nothing landed"). The no-object arm (`:2335-2342`) gains `absent_because: "NO_OBJECT"`; the
   READ_FAILED arm and the SERVED arm carry `absent_because: null`. The four postulates for that two-value field: the
   declared domain is the ABSENT blocks; the partition is "was a document read" (true = ZERO_OFFICERS, false =
   NO_OBJECT), which cannot leave a member out; same grain (one block); one intent (which absence); it moves no SERVED
   block. PRD v0.13 `C-EXEC-MANAGEMENT` (`:731-732`): *"A roster with ZERO officers is NOT SERVED. It is ABSENT with
   its reason."*
   (c) Nothing else in the file moves. `roster_source` (R14-E5), the pool read at `:2343` (R14-E3) and every other route
   are NOT this order's.
2. **The page (`portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx` + `portal/src/pages/SecurityAnalysis/types.ts`).**
   (a) `CeoProfileReading.reading` in `types.ts:680-684` becomes the six-value union above; `ManagementBlock`
   (`types.ts:692-715`) gains `absent_because?: 'NO_OBJECT' | 'ZERO_OFFICERS' | null` and a typed `lusha_enrichment`
   (`status`, `reason`, `domain`, `matched`, `credits_used`) in place of `Record<string, unknown>`.
   (b) `CeoProfile` (`:70-93`) renders ONE line per reading, `data-ceo-profile={reading}`, the text taken from the
   reading and the object's `reason` -- CONFIRMED with the link; NOT SEARCHED with the object's reason; SEARCHED,
   NOTHING FOUND; SEARCHED, LINKS UNREADABLE ("the search returned N link(s); none resolved to the company's IR domain;
   the module did not follow them"); SEARCH FAILED with its cause; UNREADABLE OBJECT with the fields. The sentence at
   `:87` ("do not expose a readable host") is REMOVED -- its count in the file is a planted negative below.
   (c) `ManagementBody` (`:95-103`): the non-SERVED branch prints `absent_because` and, when it is ZERO_OFFICERS, the
   object's `roster_status`, `roster_reason`, `source_item` and `source_accession` (`data-exec-status="ABSENT"`
   `data-exec-absent-because=...`). No table is rendered for a zero-officer object.
   (d) `OfficerRow` (`:43-51`): the profile cell reads the officer's own `enrichment` -- `MATCHED` = the link; `ABSENT` =
   "ABSENT (Lusha matched no profile)"; `NOT-ATTEMPTED` = "not attempted"; and ONE line under the table prints
   `lusha_enrichment.status` with its `reason` when the status is SKIPPED (W32-S2: the seven names whose officers all
   read "no match" today were never enriched).
3. **This is a served-output-moving deploy.** It needs a FRESH never-widen co-sign (the CTO half + the COO's half), each
   naming the BLAST RADIUS -- the `management` block of the `/thesis` route for all 33 keyed names (12 objects render
   differently: 5 flip SERVED to ABSENT, 7 CEO lines change reading), WRITER COUNT of the served property = 1 (this
   adapter; the page is a DEV-durability commit, nothing serves DEV) -- and a rollback read from the LIVE PRE-ACT
   `source_code_hash` of THIS act, never a prior act's. **Open the change-management entry BEFORE the first live act**
   (`python .tools/deploy_ledger.py`, the contract tool the rk-19 entry names -- read
   `org/critical_paths/change_management/20260917T1853Z_amgt-rk19-adapter-thesis-driver-second-join-20260917_deploy_completion.md`
   for the exact leg shape: TF apply 0 destroy + 0-diff replan + deployed `source_code_hash` equals the uploaded sha +
   verify-on-served over the 13 GET routes, LOST=[] GAINED=[]), close it on completion, per NEVER-2.

**Proven on the validation names or a dry run (`C-VALIDATION-NAMES`, PRD v0.13 `:1652-1655`):** the adapter logic is
proven OFFLINE on fixture objects through the adapter's own `_LocalPoolClient` (`scoped_amgt.py:1090-1148`, root from
the `AMGT_POOL_ROOT` environment variable -- confirm the exact name in `_pool_client()` before the first run) with the
planted negatives named in section 5; the live criteria READ the already-served plane for ASML, NU and SAP. **NO
producer runs, NO pool write, NO vendor call, NO re-run of the 33.**

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @`9c8e04cd9a` s.4 row R14-E1 (chain E, independent) and s.6
(W32-S2 carried to E1 + E7); the intake `CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` s.2B rows E1, E4, E11; the
CRO's brief `BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` s.1.2 items 1-2, s.4 item 1, s.5, s.10 item 1.
**PRD v0.13 @`1699960261`**: `C-EXEC-MANAGEMENT` (`:722-756`, replaced at v0.11, hygiene-trimmed at v0.13 -- the serp.py/enrich.py defect
citations now sit in s.10's evidence list `:1680-1682`, every rule unchanged: a zero-officer roster is not SERVED
`:731-732`; the page renders the object's own `absence_class` `:748-750`), `C-VALIDATION-NAMES` (`:1652-1658`),
`C-PRODUCTION-HOME` (`:1643-1650`; nothing here reads a worker's folder).

**ISSUER RULE -- ADAPTER SINGLE-WRITER QUEUE (`2.0.0_SA_COO~Z`, at the cut):** this order is one of the round-14 cells
that edit `lib/research/api/scoped_amgt.py` and/or redeploy `opal-amgt-scoped-api` (rk-36, rk-37, rk-43, rk-45, rk-53,
rk-61). The issuer spawns those cells ONE AT A TIME -- the next is cut from HEAD only after the previous has DRAINED --
so a worktree never carries adapter bytes behind the shared branch. Two obligations follow. (1) IMMEDIATELY BEFORE
`build-and-upload-scoped-amgt.sh`, run `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api
lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
and paste its output into the change-management entry: it MUST print nothing; if it prints a commit, STOP -- do not
build, do not apply -- file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and report; a deploy from bytes behind the
shared branch would REWIND another cell's served change. (2) The rollback target is the pre-act `CodeSha256` and the
artifact `VersionId` YOU read immediately before the apply (never a value copied from another order), recorded in the
entry before the build runs. THE ROLLBACK MECHANISM, as RULED on `1.0.0_SA_CTO~Z`'s source read (msg 23830): the Terraform
module (`infra/aws/terraform/modules/yang-lambda/main.tf:17-20`, `:38`) declares `data "aws_s3_object" "artifact"` with
bucket and key only and ALWAYS resolves the CURRENT version, so a rollback NEVER edits the module and never names a
VersionId to Terraform. Rollback = restore the pre-act bytes as the current version -- `aws s3api copy-object --bucket
opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source
"opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<pre-act VersionId>"` (bucket versioning
MEASURED `Enabled` by the issuer 2026-09-18 ~22:4xZ; RE-MEASURE it with `get-bucket-versioning` into the entry before the
build, and STOP if it reads anything else) -- then the SAME targeted `safe-apply`, and `get-function-configuration` must
print the pre-act `CodeSha256` again. Exercise nothing of this unless rolling back; record all of it before acting.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain E is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-43`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-43` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
portal/src/pages/SecurityAnalysis/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~45/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-43.management-honest-states.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you may read any `management/v1/` object from
  the pool, `lib/research/management/enrich.py` and `management.schema.json` to confirm the producer's field semantics);
  this block governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING (workspace):** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~45 <0.9.0_WK_AMGT_RESAPP~45@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). **COMMITTING (portal, a separate repo on `DEV`):** from inside `portal/`,
  `bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~45 <0.9.0_WK_AMGT_RESAPP~45@opal.agent>" -F <msgfile> -- src/pages/SecurityAnalysis/...`;
  if the tool refuses a non-workspace root, `git -C portal commit --author=... -F <msgfile> -- <paths>` and SAY SO in
  the report. Never push, merge, rebase, `checkout --`, `stash` or `clean`, in either repo.
- **DEPLOY:** Terraform only, the established mechanism -- `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  (the artifact is a transitive import CLOSURE, `:17-34`; run it from HEAD of your worktree AFTER your adapter commit)
  then `safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this` in `infra/aws/terraform/harvest/`. Never
  bare `terraform apply`, never `aws lambda update-function-code`. Read the LIVE `source_code_hash` BEFORE the apply and
  record it in the ledger entry as the rollback.

## 4. BOUNDS

PORTAL: **COMMIT YES / PROMOTE NO** on `DEV`. **THE PORTAL DEV PUSH IS RESERVED** (LD-0367/0368) and, by measurement,
nothing serves DEV (intake L10) -- the page commit is a DURABILITY act; the only path to a user is the PROD promote,
which is NOT this order's. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** **No vendor call** -- none is named. **No pool write.** No non-ASCII in anything you write. **PUSH: never;**
LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the "12 served / 7 with officers /
1-4-7 CEO split" figures above are this document's; re-measure them at spawn (AC1 prints them) and again after the
deploy (AC4).
**BEFORE YOU DEPLOY:** confirm the co-sign pair (CTO half + COO half) is on file for THIS diff and the ledger entry is
OPEN and COMMITTED; if either is missing, STOP and file a row.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W45-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** Two known
off-task facts you WILL meet and must not chase: the four CANNOT_SAY objects reflect the producer never following its
links (R14-E6's), and NOTHING_FOUND is only as honest as the SERP primitive that returns `[]` on a request failure
(intake E14, R14-E6's).

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-43"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
keys = []
for page in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='management/v1/'):
    keys.extend(o['Key'] for o in page.get('Contents', []))
names = sorted(k for k in keys if '/_pool/' not in k)
served = zero = 0
split = {}
for k in names:
    d = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    n = len(d.get('officers') or [])
    served += 1
    zero += 1 if n == 0 else 0
    p = d.get('ceo_public_profile') or {}
    state = ('CONFIRMED' if p.get('status') == 'RESOLVED' and p.get('url') else
             'NOT_SEARCHED' if p.get('query') is None else
             'SEARCH_FAILED' if str(p.get('basis') or '').startswith('the SERP primitive raised') else
             'SEARCHED_LINKS_UNREADABLE' if p.get('absence_class') == 'CANNOT_SAY' else 'SEARCHED_NOTHING_FOUND')
    split[state] = split.get(state, 0) + 1
    print(k, 'officers', n, 'roster_status', d.get('roster_status'), 'ceo', state)
print('DENOMINATOR objects', served, 'zero_officer', zero, 'with_officers', served - zero, 'ceo_split', json.dumps(split, sort_keys=True))
"</invocation><expect>the PRE-ACT count bar, read from the live store at spawn and printed with its denominator: N management objects (12 at the cut), of which K carry zero officers (5 at the cut: ASML, HAL, INTU, KMB, PBR) and N-K carry officers (7), and the CEO split by the object's OWN fields (1 CONFIRMED / 7 NOT_SEARCHED / 4 SEARCHED_LINKS_UNREADABLE / 0 / 0 at the cut) -- whatever is live is what is printed; this criterion establishes the numbers AC4 must reproduce on the served plane</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-43"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch/rk43pool/management/v1/ZERO_US_Equity .scratch/rk43pool/management/v1/FAILED_US_Equity .scratch/rk43pool/management/v1/NOTSRCH_US_Equity .scratch/rk43pool/management/v1/OK_US_Equity && python -c "
import json, os
root = '.scratch/rk43pool/management/v1/'
prof = lambda **kw: dict({'url': None, 'title': None, 'snippet': None, 'status': 'ABSENT', 'basis': None, 'ceo_name': None, 'query': None, 'ir_domain': None, 'absence_class': 'NOTHING_FOUND'}, **kw)
base = lambda key, officers, rs='RESOLVED', rr=None: {'security_key': key, 'as_of': '2026-09-18', 'roster_status': rs, 'roster_reason': rr, 'source_accession': '0001', 'source_item': 'Item 10', 'officers': officers, 'avg_tenure_years': None, 'generated': True}
off = {'name': 'A B', 'role': 'Chief Executive Officer', 'role_start': None, 'tenure_years': None, 'profile_url': None, 'lusha_title': None, 'source': 'filing', 'confirmed': True, 'enrichment': 'NOT-ATTEMPTED'}
docs = {
 'ZERO_US_Equity': dict(base('ZERO_US_Equity', [], 'UNRESOLVED-SOURCE', 'the persisted 20-F filing X carries an EMPTY officer section (Item 6)'), ceo_public_profile=prof(basis='the roster is UNRESOLVED-SOURCE: there is no confirmed CEO to search for')),
 'FAILED_US_Equity': dict(base('FAILED_US_Equity', [off]), ceo_public_profile=prof(query='site:x.com \"A B\"', ir_domain='x.com', ceo_name='A B', basis='the SERP primitive raised RuntimeError(zone)')),
 'NOTSRCH_US_Equity': dict(base('NOTSRCH_US_Equity', [off]), ceo_public_profile=prof(ceo_name='A B', basis='no declared IR domain for this name: a SERP not scoped to the company\'s own domain is not the contract\'s search')),
 'OK_US_Equity': dict(base('OK_US_Equity', [off]), ceo_public_profile=prof(status='RESOLVED', url='https://x.com/bio', query='site:x.com \"A B\"', ceo_name='A B', absence_class=None, basis='Bright Data SERP zone ... 3 url(s) returned, 1 on the IR domain')),
}
for key, doc in docs.items():
    with open(os.path.join(root, key, '2026-09-18.json'), 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=True)
os.environ['AMGT_POOL_ROOT'] = os.path.abspath('.scratch/rk43pool')
from lib.research.api import scoped_amgt as a
out = {k: a.read_management(k, identity={'security_key': k}) for k in docs}
for k, b in out.items():
    print(k, 'management_status', b['management_status'], 'absent_because', b.get('absent_because'), 'reason', (b.get('reason') or '')[:60], 'ceo', (b.get('ceo_profile_reading') or {}).get('reading'))
print('DENOMINATOR fixtures', len(docs))
assert out['ZERO_US_Equity']['management_status'] == 'ABSENT' and out['ZERO_US_Equity']['absent_because'] == 'ZERO_OFFICERS' and 'EMPTY officer section' in out['ZERO_US_Equity']['reason']
assert out['FAILED_US_Equity']['ceo_profile_reading']['reading'] == 'SEARCH_FAILED'
assert out['NOTSRCH_US_Equity']['ceo_profile_reading']['reading'] == 'NOT_SEARCHED'
assert out['OK_US_Equity']['management_status'] == 'SERVED' and out['OK_US_Equity']['ceo_profile_reading']['reading'] == 'CONFIRMED'
print('PLANTED-NEGATIVES PASS 4 of 4')
"</invocation><expect>on four fixture objects served through the adapter's own local pool client: the zero-officer object reads ABSENT with absent_because ZERO_OFFICERS and its roster_reason as the served reason (PLANTED: today it reads SERVED); the object whose basis is a primitive raise and whose absence_class is the producer's DEFAULT NOTHING_FOUND reads SEARCH_FAILED, never NOTHING_FOUND (PLANTED: the field alone misreads it); the never-searched object (query null) reads NOT_SEARCHED (PLANTED: today it reads NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY); the positive control reads SERVED + CONFIRMED; denominator 4 of 4 printed and the four assertions pass</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-43"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && ./node_modules/.bin/tsc -b 2>&1 | tail -30 && python -c "
import io
j = io.open('src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx', encoding='utf-8').read()
t = io.open('src/pages/SecurityAnalysis/types.ts', encoding='utf-8').read()
states = ['CONFIRMED', 'NOT_SEARCHED', 'SEARCHED_NOTHING_FOUND', 'SEARCHED_LINKS_UNREADABLE', 'SEARCH_FAILED', 'UNREADABLE_OBJECT']
for s in states:
    print('page', s, j.count(s), 'types', t.count(s))
print('page absent_because', j.count('absent_because'), 'ZERO_OFFICERS', j.count('ZERO_OFFICERS'), 'NOT-ATTEMPTED', j.count('NOT-ATTEMPTED'))
print('PLANTED stale sentence count', j.count('do not expose a readable host'))
print('DENOMINATOR states', len(states))
"</invocation><expect>tsc -b reports no NEW TypeScript error attributable to ExecManagementTab.tsx or types.ts; each of the six reading values occurs at least once in BOTH files (6 of 6, all read 0 in the page for the four new values before this order); absent_because, ZERO_OFFICERS and NOT-ATTEMPTED each occur at least once in the page (0 before); and the PLANTED stale sentence "do not expose a readable host" counts exactly 0 (it counts 1 at portal 625a0888)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-43"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda', region_name='us-east-1')
def get(key):
    payload = json.dumps({'rawPath': '/api/scoped/amgt/security/%s/thesis' % key, 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    body = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    return body.get('statusCode'), inner.get('management') or {}
for key in ('ASML_NA_Equity', 'NU_US_Equity', 'SAP_GY_Equity'):
    code, m = get(key)
    print(key, 'statusCode', code, 'management_status', m.get('management_status'), 'absent_because', m.get('absent_because'), 'officer_count', m.get('officer_count'), 'reason', (m.get('reason') or '')[:70], 'ceo', (m.get('ceo_profile_reading') or {}).get('reading'), 'ceo_reason', ((m.get('ceo_profile_reading') or {}).get('reason') or '')[:60])
print('DENOMINATOR names invoked 3 of 3 (ASML zero-officer, NU never-searched, SAP positive control)')
"</invocation><expect>on the LIVE deployed plane AFTER the redeploy: ASML_NA_Equity reads statusCode 200, management_status ABSENT, absent_because ZERO_OFFICERS, officer_count 0 and a reason naming the EMPTY officer section (it reads SERVED before this order); NU_US_Equity reads management_status SERVED with ceo reading NOT_SEARCHED and a ceo_reason naming "no declared IR domain" (it reads NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY before); SAP_GY_Equity reads SERVED with ceo reading CONFIRMED (the positive control, unchanged) -- three names, denominator printed, all three reads of already-served names, no producer run</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-43" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** AC1 runs BEFORE any edit; AC2 and AC3
run on your worktree before the deploy; AC4 runs AFTER the redeploy against the LIVE plane, never a local import.
**AC5 is a JUDGMENT criterion** -- "the rendered Exec Management tab tells the reader the truth about each of the 12
served names: a zero-officer name shows its reason and no table; a never-searched name says so; no line claims a search
that did not run" -- graded by `3.0.0_SA_CVO~Z` at L9 from a HEADED human session (s.3.5: mandatory MFA blocks every
headless authenticated capture; no headless criterion is cut). No verdict is yours to write; the instance records it
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO and the headed-session instrument.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~45/AMGT_RESAPP.TO-AMGT-rk-43.management-honest-states.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (AC5 is judgment, excluded from the mechanical grade;
rc 0 on AC1-AC4 plus the judgment row present is the verdict); flip `<status>` to `complete`; commit with
`--only -- <paths>`. Close the change-management entry. Report once, naming: the pre-act and post-act
`source_code_hash`, the portal commit hash on DEV (LOCAL, push state UNREAD -- never claim a push), and the AC1/AC4
count bars side by side.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing (both repos). Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~45</slot>
<fabric>site-z</fabric>
