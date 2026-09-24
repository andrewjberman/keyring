# AMGT_RESAPP task order -- `AMGT-rk-54` -- MEASURE, not build: why `publication-links/v1` covers 3 names -- ingestion (nothing fetched) or association (fetched, not keyed to the name) -- per name, with denominators

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-54</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~54</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and runs no
  harvester; the harvester's own recurring schedule is registered DISABLED (lib/opal_data_harvest/config.json
  recurring_schedule_enabled false, automatic_uploads_enabled false) and is neither read as a trigger nor written;
  the chatter schedule is untouched; the no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes NOTHING to AWS: its live acts are READ-ONLY listings and
  gets on the standing pool bucket opal-data-harvest (publication-links/v1/, publications/v1/, crosswalk/v1/) under
  the device's existing credentials; it grants no permission, provisions nothing and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~54`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~54;`. **NEVER RUN AN INSTALL.** **THIS IS A MEASURE CELL: you
build nothing, run no producer, run no harvester, write no pool object, edit no code.** Your only writes are the
measurement record under your deliverables folder, surprise rows, and this order's status flip.

## 1. THE CELL, inlined in full -- `AMGT-rk-54` (R14-L2; FWD-4, FWD-11, FWD-16; Lead Panel L3, L4)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-L2 `:140`):** *"MEASURE, not
build: why `publication-links/v1` covers 3 names -- ingestion (nothing fetched) or association (fetched, not keyed
to the name). Its answer is this seat's next L4"* -- serves FWD-4, FWD-11, FWD-16, L3, L4; co-sign no. The CTO's
own s.7 row (`:225`) waits on this cell: *"L4 on the chatter source after R14-L2 reports"*.

**The question, as the Lead Panel intake framed it** (`CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:44-45`):
L3 -- *"The article store covers 3 names (BA, COST, HD); 188 of 191 have zero articles; AAPL/NVDA/MSFT/JPM/TSLA have
no lookup key at all ... the diagnostic question the art never asked -- ingestion (nothing fetched) or association
(fetched, not keyed to the name); the empty lookup keys point at association"*; L4 -- *"The news feed and both
chatter lists are ONE gap -- all read `publication-links/v1`"*. You answer L3 with numbers; you do not fix anything.

**The rules this serves (PRD v0.13 @1699960261).** `C-ONE-STORE` (`:530-547`): the pool is THE article store; the
association is `publication-links/v1/{security_key}/{publisher}/{digest}.json`, the body
`publications/v1/{publisher}/{digest}.json`; *"one article counts ONCE per associated security"*; *"the owner of
the writer: the harvest lane, whose mechanism and cadence stay reserved to Andrew by name"*. `C-HARVESTER-COMPUTE`
(`:1193-1199`) and `C-VENDOR-WORD-HARVESTERS` (`:1240-1246`): the harvesters are Andrew's word, time-scoped -- **you
do not run one.** `C-PRODUCTION-HOME` (`:1643-1650`) names the class you will meet again below (a worker folder
read by production config) -- you RECORD it, you do not fix it.

**THE MEASURED MECHANISM, at HEAD (`lib/opal_data_harvest/` last moved @8b11d236c4; cite these lines):**
- **Association is made BY THE JOB, never by the article's content.** `worker.py:57` `run_job(publisher, security)`
  asks the publisher client for articles FOR that security (`:102` `client.articles(security, limit)`) and stores
  each through `catalog.store(article, security)` (`:116`); `catalog.py:74` builds the link key
  `publication-links/v1/{security['key']}/{publisher}/{digest}.json` from the JOB's security. So a name gets a link
  only if a job ran FOR it, and under the KEY FORM that job carried. There is no content-side association step.
- **Which securities ever get a job:** `__main__.py:66` -- `config["pilot_securities"]` unless `--all-securities`;
  `universe()` `:12-36` admits a row as a PILOT when its company name matches one of the five in `config.json`
  (`pilot_securities`: BA, COST, HD, HAL, VLO) and gives every OTHER row the key form `security-<sha256(folder)[:16]>`
  (`:29`); `config.json`: `jobs_per_run 1`, `recurring_schedule_enabled false`, `automatic_uploads_enabled false`,
  `enabled_publishers` five, and `universe_source` = `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
  0.9.0_WK_AMGT_RESAPP~3/universe.json` -- a WORKER'S deliverables folder read by production config
  (`C-PRODUCTION-HOME`'s class; record it as a row, do not fix it).
- **The ingestion ledger exists on THIS device:** `worker.py:21` opens `<runtime_root>/progress.sqlite3`
  (`config.json` `runtime_root: .runtime/opal-data-harvest`, relative to the MAIN tree); tables `jobs`
  (`:28`: id, started_at, publisher, security_key, status, ...) and `articles` (`:26-27`: publisher, security_key,
  article_id, body_sha256, path); `catalog.py:44-49` adds `article_objects`, `article_links(security_key,
  article_key, path)` and `upload_outbox(object_key, ..., status, attempts, error_code)`. Measured at the cut:
  `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/progress.sqlite3`, 282,624 bytes,
  mtime 2026-09-15 00:58 (gitignored; ABSENT in any linked worktree -- read the main tree's by absolute path,
  READ-ONLY).
- **The read side keys on the crosswalk:** `lib/research/coverage/pool_reader.py:267-330` `list_links(identity)`
  lists `publication-links/v1/<form>/` for EVERY alias the crosswalk holds for the identity
  (`default_alias_fn` `:209-231` -> `crosswalk.aliases()` `lib/research/identity/crosswalk.py:588-595`, the
  record's `association_keys`; `_alias_forms` `:455-465`); a name the crosswalk does not hold is probed AS ITSELF
  and nothing is invented (`IDENTITY-ONLY`). The pilots' persisted keys are `BA`, `COST`, `HD`; every non-pilot's is
  `security-<16 hex>` (`crosswalk.py:37-40`, `:178-198`). So "no lookup key" (L3) is a crosswalk record whose
  `association_keys` is empty.
- The population of record is `crosswalk/v1/2026-09-15.json` MEASURED = 33 (analysis s.1) -- the denominator of
  your per-name table. The harvester's own universe (`__main__.py universe`) and the chatter Lambda's union
  universe (191 at the intake) are SECOND denominators you print beside it, never in place of it.

**RULED, what you measure (five instruments, every count with its denominator; nothing is written outside your
deliverables folder):**
1. **The pool's association layer.** Paginated `list_objects_v2` over `publication-links/v1/` with `Delimiter='/'`:
   every key form present (CommonPrefixes), objects per form, total objects; `publications/v1/` objects per
   publisher. Print `key_forms=N objects=M publishers=P`.
2. **Key form -> crosswalk identity.** For each key form from (1): `crosswalk.resolve(form)` -> MEASURED
   (`security_key`) or UNRESOLVED; and for each of the 33 crosswalk records: `aliases(security_key)` (its forms) and
   the link count over those forms via `pool_reader.list_links(security_key, dedupe=True, counters=...)`. Print
   `records=33 with_links=K without_alias=J unresolved_forms_in_pool=U`.
3. **The ingestion ledger.** `sqlite3.connect("file:<abs path>?mode=ro", uri=True)` on the main tree's
   `progress.sqlite3`: jobs per (publisher, security_key, status); articles per (publisher, security_key);
   `article_links` per security_key; `upload_outbox` per status and error_code. Print each table's row count as
   the denominator. If the file is absent on this box, print `ABSENT <path>` and class every name UNMEASURED on
   this axis -- never infer.
4. **The harvester's own universe and switches.** `python -m lib.opal_data_harvest universe` (read-only; prints
   `denominator` and every security with its key form) and the six `config.json` values named above, read back
   verbatim. Print how many of the universe rows are PILOT-matched (5 expected) vs `security-` keyed.
5. **The per-name table** over the 33 crosswalk records, one class each, classes by SUBTRACTION from 33:
   `COVERED` (links in the pool under a crosswalk alias); `STORED-NOT-KEYED` (articles or links in the ledger, or
   objects in the pool, under a form the crosswalk does NOT hold for this name -- association);
   `JOBBED-NOTHING-STORED` (a job ran for the name, 0 articles -- ingestion, and the job's status/error is named);
   `NEVER-JOBBED` (no job for any alias of the name -- ingestion: the mechanism never ran for it). Print the four
   counts and check they sum to 33. Then ONE paragraph: the dominant cause with its count over 33, the second
   cause with its count, and the exact code lines that produce each (from the mechanism above) -- the CTO's L4
   input. If the runtime ledger is ABSENT, the ingestion split is UNMEASURED and the paragraph says so.

**What this cell does NOT do:** run a harvester or a publisher client; call any vendor; write to the pool; edit
`lib/opal_data_harvest/`, `config.json`, the crosswalk, or the chatter producer; re-key or migrate a link; propose
the fix (that is the CTO's L4). A finding about the mechanism (for example the worker-folder `universe_source`) is
a surprise ROW, not a remedy.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD `:1652-1658`):** a measurement over the crosswalk's 33 keyed names is
a READ, not a run; the three validation names (CAT, CSL, Keyence) each get their own row in the table and their
class is stated by name in the paragraph.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.4 row R14-L2 (`:140`), s.2
(`:49-63`, every reader keys on the POOL crosswalk) and s.7 (`:225`); the Lead Panel intake rows L3, L4
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:44-45`, `:402`). PRD
v0.13 @1699960261: `C-ONE-STORE` (`:530-547`), `C-HARVESTER-COMPUTE` (`:1193-1199`), `C-VENDOR-WORD-HARVESTERS`
(`:1240-1246`), `C-PRODUCTION-HOME` (`:1643-1650`), section 10's stage table row *"chatter and news ... its source
covers 3 names"* (`:1633`); FWD-4 (`:307`), FWD-11 (`:363`), FWD-16 (`:419`).

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-54.publication-links-coverage-measure.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant: read `lib/opal_data_harvest/` (`worker.py`,
  `catalog.py`, `__main__.py`, `config.json`, `contracts.json`), `lib/research/coverage/pool_reader.py`,
  `lib/research/identity/crosswalk.py`, and the MAIN tree's `.runtime/opal-data-harvest/progress.sqlite3`
  (read-only URI) freely. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~54 <0.9.0_WK_AMGT_RESAPP~54@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- Your record: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/PUBLICATION_LINKS_COVERAGE_MEASURE_20260918.md`
  (the five instruments' printed outputs verbatim, the per-name table, the paragraph) and beside it
  `PUBLICATION_LINKS_COVERAGE_MEASURE_20260918.json` (`{"population": 33, "vintage": "crosswalk/v1/2026-09-15.json",
  "names": [{"security_key", "aliases", "links", "jobs", "articles", "class", "evidence"}], "classes": {...},
  "pool": {...}, "ledger": {...}, "measured_at": "<ISO>"}`), every count carrying `"claim": "measured"`.

## 4. BOUNDS

**MEASURE ONLY.** **NO harvester run, NO publisher client, NO vendor call** (Seeking Alpha, FT, WSJ, Bloomberg,
Barrons -- none; `C-VENDOR-WORD-HARVESTERS` is time-scoped to the harvest lane and you are not it). **NO pool
write** -- every S3 act is a list or a get. **NO code edit.** **COLLECTION STAYS OFF.** **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets` only (none is needed). No
non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- "3 names", "188 of 191", the
five no-lookup-key names and the ledger's mtime are the cut's figures; re-measure every one at spawn and print
what you read.
**THE LEDGER IS DEVICE-LOCAL:** the runtime root is gitignored and lives in the MAIN tree only; a worktree read of
`.runtime/` is ABSENT by construction and is NOT evidence about ingestion -- read the absolute main-tree path named
above, read-only, and print its size and mtime beside every count you take from it.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W54-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-54"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
s3 = boto3.client('s3')
pg = s3.get_paginator('list_objects_v2')
forms = {}
total = 0
for page in pg.paginate(Bucket='opal-data-harvest', Prefix='publication-links/v1/'):
    for o in page.get('Contents', []):
        total += 1
        parts = o['Key'][len('publication-links/v1/'):].rsplit('/', 2)
        form = parts[0] if len(parts) == 3 else '<malformed>'
        forms[form] = forms.get(form, 0) + 1
pubs = {}
ptotal = 0
for page in pg.paginate(Bucket='opal-data-harvest', Prefix='publications/v1/'):
    for o in page.get('Contents', []):
        ptotal += 1
        pub = o['Key'].split('/')[2]
        pubs[pub] = pubs.get(pub, 0) + 1
print('LINKS key_forms', len(forms), 'objects', total)
for k in sorted(forms): print('  form', k, 'links', forms[k])
print('BODIES publishers', len(pubs), 'objects', ptotal, sorted(pubs.items()))
"</invocation><expect>the association layer listed WHOLE (paginated, never a page): every key form present under publication-links/v1/ with its link count and the object total as the denominator (3 forms -- BA, COST, HD -- at the intake; re-measure and print what is there, malformed keys counted under <malformed>), and the body layer per publisher with its total; a LIVE listing, read-only</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-54"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.identity import crosswalk
from lib.research.coverage import pool_reader
doc, _i, _a = crosswalk.load_crosswalk()
recs = [r for r in doc['records'] if r.get('resolution') == crosswalk.RESOLUTION_MEASURED]
with_links = 0; no_alias = 0
for r in recs:
    forms = crosswalk.aliases(r['security_key'])
    counters = {}
    links = pool_reader.list_links(r['security_key'], dedupe=True, counters=counters)
    if not forms: no_alias += 1
    if links: with_links += 1
    print(r['security_key'], 'aliases', len(forms), 'links', len(links), 'states', {k: v for k, v in counters.items() if v})
print('RECORDS measured', len(recs), 'of', len(doc['records']), 'with_links', with_links, 'without_alias', no_alias)
"</invocation><expect>one line per MEASURED crosswalk record (33 of 33 at the cut; re-measure) naming its alias count, its deduped link count over EVERY alias the crosswalk holds, and any read state raised, then the summary line RECORDS measured 33 of 33 with_links K without_alias J -- K is the read side's own coverage figure (3 at the intake) and J the count of names with NO lookup key (the L3 claim about AAPL/NVDA/MSFT/JPM/TSLA, measured on the record, not the brief)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-54"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os, sqlite3, datetime
p = 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/progress.sqlite3'
if not os.path.isfile(p):
    print('ABSENT', p); raise SystemExit(0)
st = os.stat(p)
print('LEDGER', p, 'bytes', st.st_size, 'mtime', datetime.datetime.utcfromtimestamp(st.st_mtime).isoformat() + 'Z')
db = sqlite3.connect('file:' + p + '?mode=ro', uri=True)
for t in ('jobs', 'articles', 'article_objects', 'article_links', 'upload_outbox'):
    try:
        n = db.execute('SELECT COUNT(*) FROM ' + t).fetchone()[0]
    except sqlite3.Error as e:
        print('TABLE', t, 'UNREADABLE', e); continue
    print('TABLE', t, 'rows', n)
print('JOBS by publisher, security_key, status:')
for row in db.execute('SELECT publisher, security_key, status, COUNT(*) FROM jobs GROUP BY 1,2,3 ORDER BY 2,1,3'): print('  ', row)
print('ARTICLES by publisher, security_key:')
for row in db.execute('SELECT publisher, security_key, COUNT(*) FROM articles GROUP BY 1,2 ORDER BY 2,1'): print('  ', row)
print('LINKS by security_key:')
for row in db.execute('SELECT security_key, COUNT(*) FROM article_links GROUP BY 1 ORDER BY 1'): print('  ', row)
print('OUTBOX by status, error_code:')
for row in db.execute('SELECT status, error_code, COUNT(*) FROM upload_outbox GROUP BY 1,2 ORDER BY 1,2'): print('  ', row)
"</invocation><expect>the harvester's own ingestion ledger read READ-ONLY from the MAIN tree's absolute path with its size and mtime printed, each table's row count as its denominator, then jobs per (publisher, security_key, status), articles and links per security_key, and the upload outbox per status/error -- the instrument that separates NEVER-JOBBED from JOBBED-NOTHING-STORED from STORED; if the file is ABSENT the invocation prints ABSENT and the path and the ingestion axis is recorded UNMEASURED (never inferred)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-54"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, subprocess, sys
cfg = json.load(open('lib/opal_data_harvest/config.json', encoding='utf-8'))
for k in ('universe_source', 'jobs_per_run', 'recurring_schedule_enabled', 'automatic_uploads_enabled', 'enabled_publishers', 'articles_per_security'):
    print('CONFIG', k, '=', json.dumps(cfg.get(k)))
print('CONFIG pilot_securities', [s['key'] for s in cfg.get('pilot_securities', [])], 'count', len(cfg.get('pilot_securities', [])))
r = subprocess.run([sys.executable, '-m', 'lib.opal_data_harvest', 'universe'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=100)
print('universe rc', r.returncode)
if r.returncode == 0:
    u = json.loads(r.stdout)
    secs = u['securities']
    pilots = [s for s in secs if not s['key'].startswith('security-')]
    print('UNIVERSE denominator', u['denominator'], 'securities', len(secs), 'pilot_keyed', len(pilots), [s['key'] for s in pilots], 'security_hash_keyed', len(secs) - len(pilots))
else:
    print(r.stderr[-2000:])
"</invocation><expect>the six config switches read back verbatim (universe_source names a worker deliverables folder, jobs_per_run 1, recurring_schedule_enabled false, automatic_uploads_enabled false, five publishers, five pilots at the cut; re-measure) and the harvester's own universe command printing its denominator with the split pilot_keyed (5) vs security_hash_keyed (the rest) -- the mechanism's own statement of which names can ever carry a BA-style key and which carry security-<hash>; rc 0, or the stderr recorded and the axis marked UNMEASURED</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-54"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
p = 'org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/PUBLICATION_LINKS_COVERAGE_MEASURE_20260918.json'
d = json.load(open(p, encoding='utf-8'))
names = d['names']
classes = {}
for n in names: classes[n['class']] = classes.get(n['class'], 0) + 1
allowed = {'COVERED', 'STORED-NOT-KEYED', 'JOBBED-NOTHING-STORED', 'NEVER-JOBBED', 'UNMEASURED'}
print('population', d['population'], 'rows', len(names), 'classes', classes, 'sum', sum(classes.values()), 'unknown_classes', sorted(set(classes) - allowed))
print('validation_names', {n['security_key']: n['class'] for n in names if n['security_key'].split('_')[0] in ('CAT', 'CSL', '6861')})
print('answer', json.dumps(d.get('answer'))[:600])
"</invocation><expect>the JSON record carries exactly population 33 rows (one per MEASURED crosswalk record; re-measure), every row in one of the four classes (UNMEASURED only when AC3 read ABSENT), the class counts summing to 33, unknown_classes empty, the three validation names each classed by name, and an answer object naming the dominant cause (ingestion or association) with its count over 33, the second cause with its count, and the code lines that produce each -- the CTO's L4 input, measured and never inferred</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order. AC1-AC4 are the instruments; AC5 grades the record you write from them.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~54/AMGT_RESAPP.TO-AMGT-rk-54.publication-links-coverage-measure.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once, with the answer paragraph verbatim.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~54</slot>
<fabric>site-z</fabric>
