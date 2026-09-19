# AMGT_RESAPP task order -- `AMGT-rk-31` -- ONE "add a security" step: one Bloomberg call lands identity in the POOL crosswalk

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-31</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~35</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected; the chatter Lambda's daily schedule is neither
  read nor written (it reads universe/v1, which this order does not touch).
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to two prefixes of the pool bucket this project
  already writes (s3://opal-data-harvest crosswalk/v1/ and raw/bloomberg/<KEY>/<stamp>/) under the device's
  existing credentials; it grants no permission, provisions no resource and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>
# pipeline-override: COVERAGE limb at DECOMP -- this is the ROUND-14 issuance (31 orders, every cell of decomposition v1.8 s.22, rk-31..rk-61); the 69 other cells of the decomposition belong to rounds 1-13 and are owned by task orders TERMINAL at HEAD (97 of 97, _open_tos_census 0 open @9e0ff02a70); no cell of this round is left uncovered and none of a prior round is re-cut

**You are `0.9.0_WK_AMGT_RESAPP~35`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`,
`lib/research/identity/` and `integrations/bloomberg/mcp/blp_client.py` exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~35;`. **NEVER RUN AN
INSTALL.** This order is chain I's entry cell and depends on no other round-14 order; `AMGT-rk-32` (chain I,
slot ~36) and `AMGT-rk-33` (chain H, slot ~37) do not touch your files and you do not touch theirs.

## 1. THE CELL, inlined in full -- `AMGT-rk-31` (R14-I1; FWD-2, V1; co-sign class POOL WRITES)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a, :121):** ONE "add a security" step:
one Bloomberg call lands identity in the POOL crosswalk -- name, exchange, LEI, SEC id, CIK, the yellow key
appended; registers the four unregistered corpus folders (Alphabet, Eli Lilly, Quanta Services, UnitedHealth).

**The constraint it implements -- `C-INSTANTIATION-ENTRY` (PRD v0.13 @1699960261, :1637-1641), verbatim:** ONE
"add a security" step lands a new security's identity in the POOL crosswalk -- name, exchange, LEI, SEC id and
CIK, from ONE Bloomberg call with the yellow key appended -- and every downstream stage runs from that record in
dependency order. Every reader behind the page keys on the pool crosswalk, so a security produced end to end
elsewhere renders nothing until this step has run (measured on CAT, CSL and Keyence). A security whose identity
cannot be resolved is UNRESOLVED with its reason, and no downstream stage runs for it.

**THE MEASURED STATE (code @075227f4c0, the validation @b527b93214).**
- The crosswalk is built ONLY from the coverage list `deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json`
  (`crosswalk.py:71-74` COVERAGE_PATH_DEFAULT; `build_crosswalk()` :391-436 reads nothing else). There is no
  entry point for a name that is not a corpus folder with a ONE PAGER workbook -- validation :59 ("None. Needs a
  ONE PAGER workbook folder in OneDrive, then 4 manual runs") and D2 :177-178. Four corpus folders already have
  no record (the analysis names Alphabet, Eli Lilly, Quanta Services, UnitedHealth; RE-MEASURE at spawn, AC1).
- The three validation names read UNRESOLVED in the served crosswalk (validation :41: 0 of 89 records for each
  of CAT, CSL, 6861; Boeing 1 of 89 as the positive control). The validation's ONE Bloomberg identity call
  returned name, exchange, LEI and SEC ID for all three (validation s.7 item 1, :263-265; Bloomberg's
  `CENTRAL_INDEX_KEY_NUMBER` and `LEGAL_ENTITY_IDENTIFIER` are the fields the CRO measured on 22 names,
  THESIS_FOREIGN_FILINGS_CHANNELS_20260918.md :41-42).
- The crosswalk's `bloomberg` field carries NO yellow key ("CAT US"); a Bloomberg call without one returned 33
  of 33 security errors (PRD :878-880). Appending the yellow key to an id `C-ONE-IDENTITY` has already resolved
  is not a second identity -- the alias index already carries the `<id> Equity` form (`crosswalk.py:462`).
- The population of record is `crosswalk/v1/2026-09-15.json`, MEASURED = 33, records = 89 (analysis :36-37).
  `load_crosswalk()` with no path reads the pool's lexicographically NEWEST key (`crosswalk.py:513-530`, :529),
  so the object this order writes becomes what EVERY reader resolves through the moment it lands.
- Existing disciplines you REUSE, never re-invent: `_parse_bloomberg()` :213-247 (never guessed as US, never
  appended, never stripped); `_record_for()` :257-384 (the record shape, ONE disposition per name);
  `harvester_key()` :178-198 (the association key: a pilot's bare root, else `security-` + SHA256(folder)[:16]);
  the collision refusal at build :407-413; `serialise()` :439-441 (ASCII, LF, no clock); `write_pool()`
  :609-657 (put with `document-sha256` metadata, conditional on ETag :628, head read-back :638-649; an
  unchanged digest is NOT rewritten); the BINARY dry-run stdout :678-685; the raw landing family
  `raw/bloomberg/<security_key>/<stamp>/` with put-if-absent (`model_block_pull.py:184-198`, :242-245); the
  raw client `integrations/bloomberg/mcp/blp_client.py` `reference_data(securities, fields)` :135-145, loaded
  by path exactly as `model_block_pull._load_blp_client()` :147-156 does (no package marker under mcp/); the
  workbook reader `build_universe.discover_bloomberg_ticker()` :191-238 over `_find_one_pager_files()` :134-144;
  the shared-placeholder rule :241-290 and `_KNOWN_TEMPLATE_PLACEHOLDER_TICKERS` :109.

**RULED -- what you build.**
1. **ONE step, one CLI:** `python -m lib.research.identity.add_security --bloomberg "<ROOT> <CC>" [--folder
   "<corpus folder name>"] --as-of YYYY-MM-DD (--dry-run | --write-pool)`. `--folder` alone (no `--bloomberg`)
   reads that ONE folder's ONE PAGER through `discover_bloomberg_ticker()` to obtain the id; a folder with no
   workbook or no MEASURED ticker is registered UNRESOLVED with that reason and makes NO Bloomberg call; a
   workbook value that is a known template placeholder (:109) or that is already MEASURED on another record is
   refused as ambiguous, never merged. The id is NEVER derived from a folder name.
2. **ONE Bloomberg call per registration**, `reference_data(["<ROOT> <CC> Equity"], IDENTITY_FIELDS)` -- the
   yellow key appended AT THE CALL (PRD :878-880), never stored without it in `bloomberg`. IDENTITY_FIELDS =
   `NAME`, `EXCH_CODE`, `LEGAL_ENTITY_IDENTIFIER`, `CENTRAL_INDEX_KEY_NUMBER`. "SEC id" and "CIK" in the row are
   ONE identifier in the validation (CAT's "SEC ID 18230" IS its CIK, validation :97): the record carries `cik`
   as the integer and `sec_id` as EDGAR's own 10-digit form (`CIK%010d`, `fetch.py:187`). If the DAPI field
   dictionary carries a DISTINCT SEC-identifier field, you may add it to the SAME call and say which; never a
   second call. `COMPANY_WEB_ADDRESS` may ride in the same call for the F1 battery (validation :114 shows it
   can be wrong; it is recorded, never trusted). A security-level `__error__` (`blp_client.py:143`) is
   UNRESOLVED with the vendor's own text; a field-level absence is recorded verbatim in `field_errors`.
3. **Raw before derived (`C-RAW-BEFORE-DERIVED`, PRD :899):** under `--write-pool` the response lands FIRST at
   `raw/bloomberg/<KEY>/<stamp>/identity.json` (put-if-absent, a fresh stamp) -- an EXISTING address family,
   so Rule 30's builder does not bind here (its non-application: an existing pipeline family). Under
   `--dry-run` nothing lands and the record is shown from the in-memory response.
4. **The registration record lives beside the producer, under version control:**
   `lib/research/identity/registrations.json` -- one row per registered id: `folder` (or null), `bloomberg`,
   `security_key`, `identity` (below), `registered_at`, `raw_source` (the landed key, null on a dry run). It is
   CONFIG in `C-PRODUCTION-HOME`'s sense (the human's act of adding a security), read by `build_crosswalk()` as
   a SECOND input after the coverage list. Re-registering an id already in the file makes NO Bloomberg call and
   no write, and prints `already-registered` (idempotent; the call ceiling in s.4 depends on this).
5. **The crosswalk record for a registration** is `_record_for()`'s shape built from a synthesized coverage-row
   entry (`bloomberg_ticker` MEASURED with evidence = the raw landing key), PLUS ONE appended `identity` object:
   `bloomberg_security` (the string sent, with the yellow key), `name`, `exchange` (EXCH_CODE as returned -- a
   disagreement with the id's exchange token is a FINDING recorded on the record, never smoothed), `lei`, `cik`,
   `sec_id`, `source` (the raw key), `registered_at`, `field_errors`; and a `provenance.identity` sentence
   naming the call. A registration WITH a folder gets `harvester_key(folder)`'s association key exactly as a
   coverage row does; WITHOUT a folder it gets only the pack-key and model-key forms and the provenance says
   why (the harvester's rule keys on a source folder that does not exist). `crosswalk.schema.json` admits the
   additions as OPTIONAL properties only (`identity` on a record; `source_row.folder` nullable :129-132;
   `registrations_source` top-level; `denominators.registered`) -- the 2026-09-15 object must still validate.
6. **Nothing existing moves:** a coverage record's bytes are UNCHANGED (AC6 is the never-widen on the
   population of record); the fixed point holds (`registered_at` is an INPUT read from the file, so two runs on
   unchanged inputs are byte-identical, `test_crosswalk.py:192-199`); ASCII only (:201-203); a registration
   whose key collides with an existing record is REFUSED before any write (the build's own :407-413).
7. **No downstream stage runs.** This step registers identity and stops. It does not pull a model block, run
   the battery, the analyzer, peers or posture, and it does not touch `universe/v1` (the "universe row" is a
   separate stage, PRD :1623). C-INSTANTIATION-ENTRY's "every downstream stage runs from that record" is what
   the OTHER round-14 chains build against the record you land.

**Co-sign class: POOL WRITES** (analysis s.4 :121; s.4's co-sign discipline :158-160 binds cells marked `yes`,
which this is not). This order moves no Lambda and no page, but the newest crosswalk object is what every reader
resolves through, so the write is REACHABLE by every served route. Therefore: (a) open a change-management
entry with `.tools/deploy_ledger.py open` BEFORE the first `--write-pool` (legs: L1 git -- the commit; L2 verify
-- the `write_pool()` receipt read back: key, ContentLength, document-sha256; L3 verify -- AC6's DELTA=0 line),
close every leg with its proof, `close` at the end; (b) the pre-act newest object `crosswalk/v1/2026-09-15.json`
is NEVER modified -- and READ THE MECHANISM RIGHT (`1.0.0_SA_CTO~Z`, msg 23819, verified at `crosswalk.py:627-628`):
`write_pool()` puts a NEW key with `IfNoneMatch "*"`, skips an existing key with the same document-sha256, but
OVERWRITES an existing key with different bytes under `IfMatch <ETag>`. So the protection of the population of record
is the KEY ARGUMENT you pass, not a refusal inside `write_pool()`. BOUND: `add_security.py` derives its key from
`--as-of` and REFUSES (non-zero rc, nothing written, the reason printed) any `--as-of` that is not TODAY in UTC
whenever `--write-pool` is given -- a past date would rewrite the record, a future date would win
`_read_pool_latest`'s `sorted(keys)[-1]` (`:513-530`) and become the served crosswalk at once. AC8 plants both;
(c) **THIS ORDER IS CO-SIGNED (issuer ruling at the cut, concurred by `1.0.0_SA_CTO~Z` @44702e4e90): the
never-widen pair is OWED before the first `--write-pool`.** The COO half is on file at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_I_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_I_CTO_HALVES.md`. Before AC4: READ both files,
confirm each carries a section headed `AMGT-rk-31` naming `crosswalk/v1/<as_of>.json` and `raw/bloomberg/<KEY>/` as
the blast radius and the per-key rollback (the pre-act newest object untouched; delete the one new key), and paste
both files' sha256 into the change-management entry. If EITHER file is absent or lacks the `AMGT-rk-31` section,
run AC1-AC3 only, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and STOP -- never write the pool on one half.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c (round-14 block), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.2 (:49-61,
the one pattern), s.4 row R14-I1 (:121) @`9c8e04cd9a`; PRD v0.13 @`1699960261` s.10 (:1608-1685):
`C-INSTANTIATION-ENTRY` :1637-1641, `C-PRODUCTION-HOME` :1643-1650, `C-VALIDATION-NAMES` :1652-1658; the
three-name validation @`b527b93214` (the identity row :59, D1-D3 :174-181, s.7 item 1 :263-265).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/add_security.py
lib/research/identity/crosswalk.py
lib/research/identity/crosswalk.schema.json
lib/research/identity/registrations.json
lib/research/identity/tests/test_crosswalk.py
lib/research/identity/tests/test_add_security.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~35/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-31.add-a-security-entry.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_I_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant: you read `build_universe.py`,
  `blp_client.py`, `model_block_pull.py` and the corpus root (`build_universe.CORPUS_ROOT` :74-77, OneDrive,
  read-only) without writing them. Scratch is `<your worktree>/.scratch/` only.
- **The coverage list's own home** (`crosswalk.py:71-74`, worker ~4; validation D2) is NOT this cell's
  surface. Do not move it; if it blocks you, a row.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~35 <0.9.0_WK_AMGT_RESAPP~35@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only. No non-ASCII in anything you write. **PUSH: never.**
Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**VENDOR CALLS -- the ceiling is NAMED:** Bloomberg `reference_data` only, at most ONE call per registered id,
on the validation names (C-VALIDATION-NAMES: a Bloomberg pull on CAT, CSL, Keyence is INSIDE the bar Andrew
set, PRD :1652-1658) and on the unregistered corpus folders AC1 prints (4 at the cut). Ceiling for this order:
3 validation ids + the unregistered set + AC2's dry run + AC3's planted negative = 9 at the cut (re-count
after AC1; a re-run after a genuine instrument failure is recorded by the tool's own `bloomberg_calls` line).
NO `historical_data`. No Seeking Alpha, no Lusha, no web. **NO FLEET RUN, NO RE-RUN** of the 33 (Andrew,
verbatim: "I dont care about rerunning until the process is completely validated end to end").
**POOL WRITES:** `crosswalk/v1/<as_of>.json` and `raw/bloomberg/<KEY>/<stamp>/identity.json` -- nothing else.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure the crosswalk
(33 MEASURED of 89 records at 2026-09-15) and the unregistered folder set (4) at spawn; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W35-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os
from lib.research.identity import build_universe, crosswalk
root = build_universe.CORPUS_ROOT
folders = sorted(n for n in os.listdir(root) if os.path.isdir(os.path.join(root, n)))
doc, _i, _a = crosswalk.load_crosswalk(refresh=True)
known = set(r['source_row']['folder'] for r in doc['records'] if r['source_row'].get('folder'))
unreg = [f for f in folders if f not in known]
print('crosswalk_as_of', doc['as_of'], 'records', len(doc['records']), 'MEASURED', doc['denominators']['MEASURED'])
print('corpus_folders', len(folders), 'registered', len(set(folders) & known), 'unregistered', len(unreg))
for f in unreg: print('UNREGISTERED', repr(f))
"</invocation><expect>the pool crosswalk's as_of, records and MEASURED printed (2026-09-15 / 89 / 33 at the cut; print whatever is live), the corpus folder denominator printed, and the UNREGISTERED set listed with its count -- the analysis names 4 (Alphabet, Eli Lilly, Quanta Services, UnitedHealth); the PRINTED set, whatever its size, is the population AC5 registers, and a difference from the analysis's four is a row, never a silent edit</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, hashlib, subprocess, sys
s3 = boto3.client('s3', region_name='us-east-1')
def count(p):
    n = 0
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix=p): n += len(page.get('Contents', []))
    return n
def sha(p):
    try: return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
    except FileNotFoundError: return 'ABSENT'
before = (count('crosswalk/v1/'), count('raw/bloomberg/CAT_US_Equity/'), sha('lib/research/identity/registrations.json'))
r = subprocess.run([sys.executable, '-m', 'lib.research.identity.add_security', '--bloomberg', 'CAT US', '--as-of', '$(date -u +%Y-%m-%d)', '--dry-run'], capture_output=True, timeout=100)
print('rc', r.returncode); print(r.stdout.decode('utf-8', 'replace')[-3000:]); print(r.stderr.decode('utf-8', 'replace')[-800:])
after = (count('crosswalk/v1/'), count('raw/bloomberg/CAT_US_Equity/'), sha('lib/research/identity/registrations.json'))
print('before', before); print('after', after); print('nothing_written', before == after)
"</invocation><expect>rc 0; the printed record reads security_key CAT_US_Equity, bloomberg 'CAT US', identity.bloomberg_security 'CAT US Equity' (the yellow key appended at the call), identity.name containing CATERPILLAR, identity.lei and identity.cik non-null (cik 18230 -- the validation's measured value, :97 -- and sec_id '0000018230'), and a line `bloomberg_calls 1`; nothing_written True (the crosswalk/v1/ count, the raw prefix count and the registrations file are all unchanged by a dry run)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, hashlib, subprocess, sys
s3 = boto3.client('s3', region_name='us-east-1')
def count(p):
    n = 0
    for page in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix=p): n += len(page.get('Contents', []))
    return n
def sha(p):
    try: return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
    except FileNotFoundError: return 'ABSENT'
before = (count('crosswalk/v1/'), count('raw/bloomberg/ZZZZQQ_US_Equity/'), sha('lib/research/identity/registrations.json'))
r = subprocess.run([sys.executable, '-m', 'lib.research.identity.add_security', '--bloomberg', 'ZZZZQQ US', '--as-of', '$(date -u +%Y-%m-%d)', '--dry-run'], capture_output=True, timeout=100)
print('rc', r.returncode); print(r.stdout.decode('utf-8', 'replace')[-1500:]); print(r.stderr.decode('utf-8', 'replace')[-800:])
after = (count('crosswalk/v1/'), count('raw/bloomberg/ZZZZQQ_US_Equity/'), sha('lib/research/identity/registrations.json'))
print('nothing_written', before == after)
"</invocation><expect>THE PLANTED NEGATIVE: rc is non-zero, the output reads resolution UNRESOLVED with security_key None and a reason carrying the vendor's OWN security-error text (blp_client's __error__), no key is minted, no record is shown as MEASURED, and nothing_written True -- an id Bloomberg cannot resolve is UNRESOLVED with its reason and no downstream stage runs for it</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && for id in "CAT US" "CSL AU" "6861 JP"; do python -m lib.research.identity.add_security --bloomberg "$id" --as-of "$(date -u +%Y-%m-%d)" --write-pool 2>&1 | tail -2 || echo "RC=$? for $id"; done && python -c "
from lib.research.identity import crosswalk
doc, _i, _a = crosswalk.load_crosswalk(refresh=True)
print('as_of', doc['as_of'], 'records', doc['denominators']['records'], 'MEASURED', doc['denominators']['MEASURED'], 'UNRESOLVED', doc['denominators']['UNRESOLVED'], 'registered', doc['denominators'].get('registered'))
for form in ('CAT US', 'CSL AU', '6861 JP', 'CAT US Equity', 'CAT_US_Equity'):
    r = crosswalk.resolve(form); print(form, '->', r['security_key'], r['resolution'], r.get('matched_as'))
"</invocation><expect>three write-pool runs each print their write_pool receipt (key crosswalk/v1/<today>.json, document-sha256, ContentLength read back) and the raw landing key raw/bloomberg/<KEY>/<stamp>/identity.json; the pool's newest crosswalk then reads MEASURED = 33 + 3 = 36 with registered 3 (re-measure: 33 is the cut's value), and every form of each validation name resolves to its canonical key -- CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity -- with resolution MEASURED; a name whose call failed is UNRESOLVED in the object with its reason and is counted, never dropped</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os, subprocess, sys
from lib.research.identity import build_universe, crosswalk
root = build_universe.CORPUS_ROOT
folders = sorted(n for n in os.listdir(root) if os.path.isdir(os.path.join(root, n)))
doc, _i, _a = crosswalk.load_crosswalk(refresh=True)
known = set(r['source_row']['folder'] for r in doc['records'] if r['source_row'].get('folder'))
unreg = [f for f in folders if f not in known]
print('unregistered_before', len(unreg), 'of', len(folders))
for f in unreg:
    r = subprocess.run([sys.executable, '-m', 'lib.research.identity.add_security', '--folder', f, '--as-of', '$(date -u +%Y-%m-%d)', '--write-pool'], capture_output=True, timeout=25)
    tail = r.stdout.decode('utf-8', 'replace').strip().split('\n')[-1:]
    print('FOLDER', repr(f), 'rc', r.returncode, tail)
crosswalk._CACHE.clear()
doc, _i, _a = crosswalk.load_crosswalk(refresh=True)
known = set(r['source_row']['folder'] for r in doc['records'] if r['source_row'].get('folder'))
print('unregistered_after', len([f for f in folders if f not in known]), 'of', len(folders), 'MEASURED', doc['denominators']['MEASURED'], 'UNRESOLVED', doc['denominators']['UNRESOLVED'])
"</invocation><expect>every unregistered folder is DISPOSITIONED -- printed with rc 0 and a last line naming its disposition: MEASURED with its security_key (the id read from the folder's own ONE PAGER through discover_bloomberg_ticker(), then ONE Bloomberg call), or UNRESOLVED with its reason (no workbook, no MEASURED ticker, a template placeholder, or an ambiguity) and NO key minted, never guessed from the folder name; unregistered_after 0 of N; MEASURED + UNRESOLVED == records; the analysis's four are among the dispositioned set or the difference is a row</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
def get(k): return json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read().decode('utf-8'))
base = get('crosswalk/v1/2026-09-15.json')
keys = []
for page in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='crosswalk/v1/'): keys += [o['Key'] for o in page.get('Contents', [])]
newest = sorted(keys)[-1]; new = get(newest)
canon = lambda r: json.dumps(r, sort_keys=True)
new_by_folder = {r['source_row']['folder']: r for r in new['records'] if r['source_row'].get('folder')}
same = sum(1 for r in base['records'] if r['source_row']['folder'] in new_by_folder and canon(new_by_folder[r['source_row']['folder']]) == canon(r))
print('base 2026-09-15 records', len(base['records']), 'MEASURED', base['denominators']['MEASURED'])
print('newest', newest, 'records', len(new['records']), 'MEASURED', new['denominators']['MEASURED'], 'registered', new['denominators'].get('registered'))
print('base_records_byte_identical_in_newest', same, 'of', len(base['records']))
"</invocation><expect>NEVER-WIDEN on the population of record: newest is the object this order wrote (not 2026-09-15.json, which is untouched); base_records_byte_identical_in_newest N of N with N == the base's record count (89 at the cut -- MEASURED and UNRESOLVED alike, every coverage record unchanged to the byte, no `identity` key added to a coverage record); newest MEASURED == base MEASURED + the count of registrations that resolved; DELTA=0 on the 33</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/identity/tests -p "test_*.py" -q 2>&1 | tail -4 && python -c "
import hashlib, subprocess, sys
outs = []
for _ in range(2):
    r = subprocess.run([sys.executable, '-m', 'lib.research.identity.crosswalk', '--as-of', '$(date -u +%Y-%m-%d)', '--dry-run'], capture_output=True, timeout=50)
    outs.append(hashlib.sha256(r.stdout).hexdigest()); print('rc', r.returncode, 'bytes', len(r.stdout), 'sha', outs[-1][:16], 'ascii', len(r.stdout) == len(r.stdout.decode('ascii', 'replace')))
print('fixed_point', outs[0] == outs[1])
"</invocation><expect>the unit arms pass (the count printed, 0 failures, 0 errors) INCLUDING new arms in test_add_security.py for: a registration record's shape and its association keys with and without a folder; the planted vendor error -> UNRESOLVED, no key; a colliding key -> refused before any write; the 2026-09-15 object and a registration record both validating against crosswalk.schema.json (jsonschema if importable, else a printed SKIP naming the reason); and fixed_point True with ascii True -- two dry runs over unchanged inputs (coverage list + registrations.json) are byte-identical</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rk-31"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, subprocess, sys
s3 = boto3.client('s3'); B = 'opal-data-harvest'
def census():
    ks = [o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(Bucket=B, Prefix='crosswalk/v1/') for o in p.get('Contents', [])]
    et = {k: s3.head_object(Bucket=B, Key=k)['ETag'] for k in ks}
    return ks, et
ks0, et0 = census(); print('PRE keys', len(ks0), 'newest', sorted(ks0)[-1])
for asof in ('2026-09-15', '2099-01-01'):
    r = subprocess.run([sys.executable, '-m', 'lib.research.identity.add_security', '--bloomberg', 'CAT US', '--as-of', asof, '--write-pool'], capture_output=True, text=True, timeout=60)
    print('PLANTED', asof, 'rc', r.returncode, '|', (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else '(no output)')
ks1, et1 = census(); print('POST keys', len(ks1), 'newest', sorted(ks1)[-1], 'etags_unchanged', et0 == et1, 'keys_unchanged', ks0 == ks1)
"</invocation><expect>both planted runs REFUSE: rc non-zero, the last line names the --as-of and says it is not today UTC (the past date would rewrite the population of record; the future date would win the newest-key sort); POST keys == PRE keys, newest unchanged, etags_unchanged True, keys_unchanged True -- no put reached the bucket on either planted date. Run this BEFORE AC4 (it is the negative control for AC4's write) and again AFTER AC6 (it must still refuse once the today-dated key exists)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC4-AC6 run only after the change-management entry is OPEN (and, if the spawn prompt says so, the
never-widen pair is on file); the entry's legs are closed with AC4's receipts and AC6's line, and the entry is
closed before you report.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~35/AMGT_RESAPP.TO-AMGT-rk-31.add-a-security-entry.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once: the calls made (count against the
ceiling), the registrations landed (MEASURED / UNRESOLVED with reasons), the newest crosswalk key and its
denominators, and the change-management entry's slug and CLOSED line.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~35</slot>
<fabric>site-z</fabric>
