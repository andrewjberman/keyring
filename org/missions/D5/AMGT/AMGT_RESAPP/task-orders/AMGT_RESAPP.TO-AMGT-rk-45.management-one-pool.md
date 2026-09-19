# AMGT_RESAPP task order -- `AMGT-rk-45` -- one pool: `compute_pool` reads the newest object per name across dates, as its own docstring and the contract say

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-45</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~47</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the DISABLED task
  OpalResearch-ExecManagement is neither read nor written (AMGT-rk-44's); the standing collection-stays-off /
  no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes ONE object to an already-provisioned prefix the project already
  writes (s3://opal-data-harvest/management/v1/_pool/) under the existing credentials, and redeploys the existing
  Lambda opal-amgt-scoped-api under its existing execution role; it grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~47`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/management/`
and `lib/research/api/` exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~47;`. **NEVER RUN AN INSTALL.**
**SEQUENCING YOU MUST HONOUR:** this order's producer half (`lib/research/management/enrich.py`) is yours from the
start; its ONE-LINE adapter half (`lib/research/api/scoped_amgt.py:2343`) touches a single-writer file that
`AMGT-rk-43` (`0.9.0_WK_AMGT_RESAPP~45`) holds whole-file -- **do not edit `scoped_amgt.py` until the COO's continuation
message says rk-43 has drained**, and if the COO's message says instead that the line was folded into rk-43's deploy,
AC5 is proven against that deploy and you edit nothing there.

## 1. THE CELL, inlined in full -- `AMGT-rk-45` (R14-E3; FWD-17; intake rows E5, E5')

**The analysis row, verbatim** (`ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`): *"one pool: `compute_pool` reads the
newest object per name across dates, as its own docstring and the contract say"* -- serves FWD-17, E5'; co-sign YES.

**THE MEASURED STATE (read at HEAD `4f44431d34`; the pool read 2026-09-18 ~20:xxZ by the drafting seat -- RE-MEASURE
AT SPAWN).**
- **The docstring promises one thing and the code does another.** `compute_pool(as_of, ...)`
  (`lib/research/management/enrich.py:582-616`): its docstring (`:583-588`) says *"THE POOL AVERAGE over EVERY name of
  the union universe that has a roster object today"*; the code lists `management/v1/` and keeps only keys ending
  `/<as_of>.json` (`:594`: `mine = [k for k in keys if k.endswith("/%s.json" % as_of) and ...]`) -- so each run pools
  ONLY the objects written with ITS OWN date. Two authorities say otherwise and agree with each other: the docstring,
  and PRD v0.13 @`1699960261` `C-EXEC-MANAGEMENT` (`:752-753`): *"the average tenure is the mean over OFFICERS across
  EVERY current FILING roster -- the newest object per name across all dates, within the union universe -- never over
  one run's objects"* (the PRD's s.10 evidence list `:1680-1682` cites `enrich.py:582-594` as the defect).
- **Measured on the served plane:** `management/v1/_pool/2026-09-15.json` = `pool_avg_tenure_years 4.08`,
  `names_in_union 256, names_with_roster 5, officers_with_role_start 40` (the five pilot objects);
  `management/v1/_pool/2026-09-18.json` = `pool_avg_tenure_years null`, `names_in_union null, names_with_roster 2,
  officers_with_role_start 0` (NU and VLO, whose officers carry no role start; the five zero-officer objects are
  UNRESOLVED and skipped by `:599-600`). `names_in_union` is null on the 18 Sep pool because `read_universe(as_of)`
  (`:569-579`) reads `universe/v1/<as_of>.json` at the SAME date and no 18 Sep universe vintage exists (the pool
  carries `universe/v1/2026-09-15.json` and `2026-09-16.json`).
- **The adapter binds the pool to the name's date.** `read_management()` reads the pool object at the SAME `as_of` as
  the name's object (`scoped_amgt.py:2343`: `read_pool_object(MANAGEMENT_PREFIX, MANAGEMENT_POOL_NAME,
  as_of=document.get("as_of"))`), so the five 15 Sep names are served the 15 Sep pool and NU/VLO are served the empty
  18 Sep pool -- **two pools on one page**, and NU/VLO show the pool ABSENT (intake E5). `read_pool_object()` without
  `as_of` already returns the NEWEST object under the prefix (`:1155-1157`, `:1179-1191`).
- **Three writers of `management/v1/_pool/`, one rule.** `enrich.main()` (`:689-690`), `batch.main()` (`:190-191`) and
  `integrations/bloomberg/research/management_posture_batch.py` (`:194-195`) each call `compute_pool()` then
  `write_pool_object()`; none computes a pool of its own. **N = 3 writers, ONE computing function** -- fixing
  `compute_pool` moves all three together (the never-widen half prints this count).
- The pool's tenure figure today is the mean of each object's STORED `tenure_years` (`:605-606`), which each object
  measured at its OWN `as_of` (`roster.py:553`) -- a 15 Sep object's tenures are 3 days stale in an 18 Sep pool.

**RULED -- what this order builds.**
1. **`compute_pool(as_of, client=None, universe_key=None)` (`enrich.py:582-616`) becomes what its docstring says.** It
   lists `management/v1/` ONCE, groups keys by NAME -- `name = key[len(MANAGEMENT_PREFIX):].rsplit("/", 1)[0]`, never
   `split("/")[n]` (a name may carry a slash: `BP/_LN_Equity`, row W32-S3) -- drops `_pool`, keeps the NEWEST dated
   object per name (the file segment is an ISO date, so max() in string order is the newest), and reads only those.
   A name counts toward `names_with_roster` only when its newest object has `roster_status == RESOLVED` AND at least
   one officer (PRD v0.13 `:731-732`: a zero-officer roster is not a roster). Each officer's tenure is RECOMPUTED at the
   POOL's `as_of` from the officer's own `role_start` with `roster.tenure_years(role_start, as_of)` (`roster.py:245-258`)
   -- never the stored `tenure_years` measured at another date. The returned meta (`:616`) prints `objects_listed`,
   `names_seen`, `newest_per_name`, `dates_spanned` beside the existing `objects`/`tenures`/`universe`.
2. **`read_universe()` (`:569-579`) resolves the NEWEST `universe/v1/<date>.json` vintage** when no explicit
   `universe_key` is given (listing the prefix, last key in order -- the same convention `read_pool_object` uses), and
   returns which vintage it read in its label; `names_in_union` is null ONLY when no universe object exists at all.
   The pool object gains `universe_vintage` (string or null) so the number printed beside it names its denominator's
   source; `pool.schema.json` (`:15-31`, `additionalProperties: false`) admits that one field.
3. **A `--pool-only` mode on `enrich.main()` (`:633-702`)**: `--security-key` is not required with it; the run computes
   the pool from EXISTING objects and prints the POOL line (`:692-696` shape, plus the new meta), writing NOTHING unless
   `--write-pool` is also given, in which case it writes exactly ONE object, `management/v1/_pool/<as_of>.json`
   (`write_pool_object`, `:625-630`, through `crosswalk.write_pool`'s put + read-back). **No `build_document` call, no
   Lusha, no SERP, no per-name object is touched -- this is a DERIVED object over what already landed, not a re-run.**
4. **The adapter's ONE line (`scoped_amgt.py:2343`)**: `read_pool_object(MANAGEMENT_PREFIX, MANAGEMENT_POOL_NAME)` --
   without `as_of` -- so every served name reads the NEWEST pool object. Nothing else in that file moves. Sequenced
   behind `AMGT-rk-43` (the file's holder); see the sequencing paragraph above.
5. **Tests** (`tests/test_management.py`, `PoolAverageTest` `:289-327`): PLANT on the `_StubS3` (`:255-273`): the same
   name at TWO dates (counted ONCE, the newest wins, the older object's officers never counted); a RESOLVED object with
   ZERO officers (never counted); a slash name `management/v1/BP/_LN_Equity/2026-09-18.json` (grouped as one name,
   never split); two `_pool` objects (never counted as names); a role_start whose tenure at the pool's `as_of` differs
   from the stored `tenure_years` (the recomputed value is used); `universe/v1/` at two vintages with no object at the
   pool's `as_of` (the newest vintage is read and named). The existing three tests keep passing with their denominators
   re-stated.

**This moves served output twice** -- the ONE pool write (`_pool/<today>.json` is overwritten if today's exists: it
does at the cut, `_pool/2026-09-18.json`, the null-value object) and the adapter redeploy -- so it needs a FRESH
never-widen co-sign (CTO half + COO half) naming: BLAST RADIUS = the pool line of every served management block (7
names with officers after rk-43; 12 objects today) and the one `_pool` key; WRITERS of `_pool/` = 3, all through
`compute_pool` (counted above); ROLLBACK = the pre-act BYTES of `_pool/<today>.json` snapshotted to `.scratch/` and
re-put with `crosswalk.write_pool`, plus the live pre-act `source_code_hash` for the adapter. Open the change-management
entry (`python .tools/deploy_ledger.py`, the rk-19 precedent shape) BEFORE the pool write, close it after AC5.

**Proven on a dry run first** (`C-VALIDATION-NAMES`, PRD v0.13 `:1652-1655`): AC3 computes the pool over the live
objects WITHOUT writing; AC4 is the one co-signed write; no producer runs on any name, no vendor call, no re-run of the
33. `C-PRODUCTION-HOME` (`:1643-1650`): nothing here reads a worker's folder; the pool address is the existing
`management/v1/_pool/<as_of>.json` (`enrich.py:557-558`), unchanged.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @`9c8e04cd9a` s.4 row R14-E3 (chain E, independent of every
cell but for the one adapter line, which the COO sequences behind rk-43); the intake
`CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` s.2B rows E5 (`:164`) and E5' (`:175`); the CRO's brief
`BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` s.1.2 item 3, s.3 step 7, s.4 item 4, s.5 "Pool".
**PRD v0.13 @`1699960261`**: `C-EXEC-MANAGEMENT` the pool clause (`:752-753`; the clause's NOT-CHANGED list keeps the
mean over officers and Andrew's no-fleet-run word), the zero-officer rule (`:731-732`), s.10 evidence list
(`:1680-1682`), `C-VALIDATION-NAMES` (`:1652-1658`), `C-PRODUCTION-HOME` (`:1643-1650`).

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
files exist in your worktree, each carries a section headed `AMGT-rk-45`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-45` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/enrich.py
lib/research/management/pool.schema.json
lib/research/management/tests/test_management.py
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~47/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-45.management-one-pool.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `roster.py` (rk-46's) and `batch.py` (rk-44's) are READ ONLY here --
  `roster.tenure_years` is imported, not edited. `scoped_amgt.py` is granted for ONE line and only after the COO's
  continuation (above). A READ needs no grant. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~47 <0.9.0_WK_AMGT_RESAPP~47@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer; every `.py` edit passes `.tools/commit-gate.sh`). Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY (adapter line only, after rk-43 has drained):** `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  from HEAD of your worktree, then `safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this` in
  `infra/aws/terraform/harvest/`. Never bare `terraform apply`, never `aws lambda update-function-code`. Read the live
  `source_code_hash` BEFORE the apply.

## 4. BOUNDS

PORTAL FROZEN (not your surface; the page's pool line already prints whatever denominators the adapter serves,
`ExecManagementTab.tsx:57-68`). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** **No vendor call** -- none is named; `--pool-only` makes none. **ONE pool write, co-signed, and no
other pool write** -- never `enrich.py --write-pool` with a `--security-key`, never `batch.py --write-pool`, never
`management_posture_batch.py management --write-pool`. No non-ASCII in anything you write. **PUSH: never;** LD-0522 puts
the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the "12 objects, 7 with officers,
40 officers with a role start, 4.08 years, universe 2026-09-16 = 250 names" figures are this document's; AC2 and AC3
re-measure them at spawn; AC3's dry POOL line is the bar AC4's written object must reproduce byte-for-byte in its
fields.
**BEFORE THE POOL WRITE (AC4):** confirm the co-sign pair is on file for THIS diff and the ledger entry is OPEN and
COMMITTED, and snapshot the pre-act `_pool/<today>.json` bytes (if any) to `.scratch/` -- that snapshot IS the rollback
named in the COO half. If either is missing, STOP and file a row.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W47-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** One known off-task
fact you WILL meet: BABA, NU and VLO carry officers with no role start (a parser gap, rk-46's) -- they count toward
`names_with_roster` and contribute 0 tenures; that is correct, not a defect to chase.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-45"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_management.PoolAverageTest -v 2>&1 | tail -30</invocation><expect>every PoolAverageTest passes ("OK" on the last line; "Ran N tests" with N >= 7 -- three at HEAD plus at least four planted: same-name-two-dates counted once with the newest winning, zero-officer RESOLVED object never counted, slash name BP/_LN_Equity grouped as one name, tenure recomputed at the pool as_of from role_start and the universe vintage resolved to the newest when none matches the pool as_of); the test names print in the -v output</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-45"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
P = 'management/v1/'
keys = []
for page in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix=P):
    keys.extend(o['Key'] for o in page.get('Contents', []))
newest = {}
for k in keys:
    name = k[len(P):].rsplit('/', 1)[0]
    if name == '_pool':
        print('POOL', k, s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read().decode().replace(chr(10), ' ')[:200])
        continue
    if name not in newest or k > newest[name]:
        newest[name] = k
with_officers = 0
for name, k in sorted(newest.items()):
    d = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    n = len(d.get('officers') or [])
    with_officers += 1 if d.get('roster_status') == 'RESOLVED' and n else 0
    print(name, k.rsplit('/', 1)[-1], d.get('roster_status'), 'officers', n, 'with_role_start', sum(1 for o in d.get('officers') or [] if o.get('role_start')))
print('DENOMINATOR keys', len(keys), 'names', len(newest), 'names_with_officers_across_dates', with_officers)
"</invocation><expect>the PRE-ACT count bar from the live store: every _pool object printed (two at the cut: 2026-09-15 with 4.08 over 5 names / 40 officers, 2026-09-18 with null over 2 names / 0), the newest object per name with its date and officer count (12 names across two dates at the cut), and names_with_officers_across_dates printed with its denominator (7 of 12 at the cut) -- this is the number the one pool must carry as names_with_roster</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-45"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.management.enrich --pool-only --as-of "$(date -u +%F)" 2>&1 | tail -8</invocation><expect>a DRY pool computation over the live objects, nothing written (a DRY line is the last line): the POOL line prints pool_avg_tenure_years as a number (about 4.1 at the cut: 40 tenures recomputed at today's as_of), names_in_union from the NEWEST universe vintage (250 from universe/v1/2026-09-16.json at the cut, the vintage named), names_with_roster equal to AC2's names_with_officers_across_dates (7 at the cut), officers_with_role_start 40 at the cut, and the meta line prints objects_listed, names_seen, newest_per_name and dates_spanned (2 at the cut) with their denominators</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-45"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.management.enrich --pool-only --as-of "$(date -u +%F)" --write-pool 2>&1 | tail -8 && python -c "
import boto3, json, datetime
s3 = boto3.client('s3', region_name='us-east-1')
k = 'management/v1/_pool/%s.json' % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
h = s3.head_object(Bucket='opal-data-harvest', Key=k)
d = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
print('READ-BACK', k, 'document-sha256', h['Metadata'].get('document-sha256', '')[:16], json.dumps(d, sort_keys=True))
"</invocation><expect>the ONE co-signed pool write: an OK: uploaded line for management/v1/_pool/<today>.json with its read-back sha256, then the object read back from the store carrying the SAME pool_avg_tenure_years, names_with_roster, officers_with_role_start, names_in_union and universe_vintage as AC3's dry line (byte-for-byte in those fields), and NO other key under management/v1/ changed (state the pre-act and post-act key counts from AC2's listing: 14 and 14 at the cut)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-45"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3, datetime
lam = boto3.client('lambda', region_name='us-east-1')
today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
def get(key):
    payload = json.dumps({'rawPath': '/api/scoped/amgt/security/%s/thesis' % key, 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    body = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    return body.get('statusCode'), inner.get('management') or {}
for key in ('BA_US_Equity', 'NU_US_Equity', 'HOLLOW_NONEXISTENT_KEY_Equity'):
    code, m = get(key)
    pr = m.get('pool_read') or {}
    print(key, 'statusCode', code, 'management_status', m.get('management_status'), 'name_as_of', m.get('as_of'), 'pool_object_key', pr.get('object_key'), 'pool_avg', m.get('pool_avg_tenure_years'), 'pool_denominator', json.dumps(m.get('pool_denominator')))
print('EXPECTED pool_object_key management/v1/_pool/%s.json for both served names; DENOMINATOR 3 names invoked (BA a 2026-09-15 object, NU a 2026-09-18 object, one planted nonexistent key)' % today)
"</invocation><expect>on the LIVE deployed plane after the adapter line lands (in this order's own redeploy, or in rk-43's if the COO folded it): BA_US_Equity (a 2026-09-15 object) and NU_US_Equity (a 2026-09-18 object) BOTH serve pool_object_key management/v1/_pool/<today>.json with the SAME non-null pool_avg and the SAME pool_denominator (names_with_roster 7 at the cut) -- today BA serves the 2026-09-15 pool and NU serves pool ABSENT; the PLANTED nonexistent key serves management_status ABSENT with pool_avg null (no object, no pool line -- the negative control that the newest-pool read never invents a pool for a name with no roster)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1-AC3 run on your worktree with NO write; AC4 runs ONLY after the co-sign pair and the ledger entry exist; AC5 runs
AFTER the adapter line is live, against the deployed plane, never a local import.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~47/AMGT_RESAPP.TO-AMGT-rk-45.management-one-pool.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Close the change-management entry. Report once, naming: the pre-act
`_pool/<today>.json` bytes' sha256 (the rollback), the written object's sha256, and -- if you deployed -- the pre-act
and post-act `source_code_hash`.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~47</slot>
<fabric>site-z</fabric>
