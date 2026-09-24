# AMGT_RESAPP task order -- `AMGT-rk-42` -- the batch made correct BEFORE it can ever run: a version that moves with the contract, then skip-on-unchanged; dedupe by CIK; one writer; the newest vintage; the launcher quoted and read back

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-42</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~44</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- (comp-schedule --budget 500 ran at the cut, 2026-09-18 19:5xZ: scanned 5 of 5 carriers, denominators C1=23 C2=6 C3=12 C4=21 C5=334, 25 gates armed, 136 prose blocking fields unread by the tool; saved by the issuer) this order TOUCHES ONE EXISTING WINDOWS SCHEDULED TASK, `OpalResearch-FilingsAnalyzer`,
  which is registered DISABLED with its launcher path split at the space (measured 2026-09-18 via `schtasks /Query /XML`:
  Command `C:\Users\Opal`, Arguments `Bloomberg\Desktop\ajb_workspace\lib\research\filings\run_batch.cmd`,
  Enabled false). The order re-registers that task from its own exported XML with the launcher path QUOTED and
  `<Enabled>false</Enabled>` UNCHANGED, and reads it back. It arms NOTHING: the task stays DISABLED, activation is
  Andrew's word (batch.py:9-10), and no cron, alarm, monitor or cadence is created. `OpalResearch-ExecManagement`
  carries the same defect and is NOT touched (chain E's R14-E2).
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes no AWS resource (its pool acts are READS: a listing of
  `universe/v1/` and the `analyzer_version` of the stored analysis objects); it grants no permission, provisions
  nothing and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~44`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and every path in
section 3 exists; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~44;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-42` (R14-F5; FWD-18; Thesis T4-T7)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a):** *"the batch made correct BEFORE it can
ever run: an analyzer version that MOVES with the output contract, then skip-on-unchanged (in that order, or the skip
locks the stale analyses in); dedupe by CIK; one writer of `drafting/v1`; the newest universe vintage, not a typed date;
the task launcher path quoted and read back"* -- serves FWD-18, T4-T7; co-sign: no.

**The rules this serves (PRD v0.13 @1699960261).** `C-FILINGS-ANALYZER` `:689-690`: *"The analysis carries an ANALYZER
VERSION that MOVES whenever its output contract moves; a skip-on-unchanged rule is built only after that, never
before"*; `:697-699`: *"NO FLEET RUN AND NO RE-RUN ... The scheduled batch stays disabled until he activates it"*;
`C-VERBATIM-GATE` `:917-918`: *"The rule binds BOTH writers of `drafting/v1/<key>.json` (`batch.py:150`,
`analyze.py:1215`)"*; `C-PRODUCTION-HOME` `:1643-1650`: *"A production code path never reads or writes a WORKER'S
deliverables folder ... A dry run writes nothing, anywhere"*; section 10 `:1617-1618`: the population is the
crosswalk's MEASURED records, never a store listing or a hand list. Andrew's word on the batch (Thesis T11, intake
s.2.1): NOT NOW -- *"I dont care about rerunning until the process is completely validated end to end"*.

**1.1 The measured current state (read at HEAD; `lib/research/filings/` last moved @db6c40083f).**
- **T4 -- the version never moves:** `analyze.py:60` `ANALYZER_VERSION = "opal-filings-analyze/1.0.0"` and `:61`
  `PROMPT_VERSION = "rj6-two-pass/1"`; `build_analysis()` stamps both (`:922-923`). The output contract moved at
  `AMGT-rk-19` (the `thesis_driver.points` branch, `:776-834`) and the version did not: the intake measured six pool
  analyses -- four stale ones with no driver points and two with -- all carrying the IDENTICAL version. WARNING: A skip rule
  built on that field as it stands ("skip a name whose analysis carries the current version") would skip the ten stale
  analyses FOREVER. Hence the ORDER: the version moves first, the skip second.
- **T5 -- the task cannot launch:** measured 2026-09-18 by `schtasks /Query /TN OpalResearch-FilingsAnalyzer /XML`:
  `<Command>C:\Users\Opal</Command>`, `<Arguments>Bloomberg\Desktop\ajb_workspace\lib\research\filings\run_batch.cmd
  </Arguments>`, `<Enabled>false</Enabled>` -- the path split at the space in "Opal Bloomberg". `batch.py:119-130`
  `task_definition()` builds `/TR "%s"` with ONE pair of quotes (`:125-126`); `schtasks` strips that pair and splits
  the value, so the definition the module prints is the definition that registered wrong. Enabled as it is, the task
  would run nothing and read like a quiet week.
- **T6 -- a typed date:** `run_batch.cmd:9` pins `--universe universe/v1/2026-09-15.json`; `analyze.py:1095-1097`
  `DEFAULT_UNIVERSE_PATH` points at a WORKER's deliverables folder AND a typed date
  (`deliverables/0.9.0_WK_AMGT_RESAPP~19/universe.v1.2026-09-15.json`) -- a fourth instance of the class
  `C-PRODUCTION-HOME` retires, found reading this file. The newest vintage in the pool is `universe/v1/2026-09-16.json`
  (validation s.1, 250 names), written by `build_universe.union_main()` at `UNIVERSE_PREFIX + as_of + ".json"`
  (`build_universe.py:448`, `:861-862`) -- a date-keyed prefix a listing can order.
- **T6 -- duplicates:** the 16 Sep universe lists ASML twice under one CIK (Thesis brief s.1.2 #4); `batch.py:82-116`
  `plan()` builds `fetchable` one entry per ROW, so one issuer would be fetched and analyzed twice at model cost.
- **T7 -- two writers:** `batch.py:150` and `analyze.py:1215` each write `"drafting/v1/%s.json"`; a repo-wide census
  of `.py` files finds no third writer (`posture/packs.py:107` and `scoped_amgt.py:1336` READ the prefix).
- **D27:** `batch.py:198` announces every unresolved row as an object-to-be, while the real run skips rows with no
  `security_key` at `:233-236` -- the dry-run's 243 versus the run's 23.
- The dry run today (`:200-204`) prints denominators and returns before any client is built -- correct, and to be
  kept exactly so.

**1.2 What you build -- in THIS order.**
1. **The version MOVES with the contract** (`analyze.py`): `ANALYZER_VERSION` -> `"opal-filings-analyze/2.0.0"` (the
   contract already moved at rk-19); beside it `OUTPUT_CONTRACT_FINGERPRINT`, a sha256 over the SORTED key paths of the
   analysis object's shape (top-level keys; `items.<class>[]` keys; `thesis_driver` keys and its `points[]` keys;
   `denominators` keys; `passes` keys), computed by a function `output_contract_fingerprint(analysis)`; a test builds
   the fixture analysis (`test_filings.py`'s stub) and asserts `output_contract_fingerprint(analysis) ==
   OUTPUT_CONTRACT_FINGERPRINT`. A contract change fails that test until BOTH constants move -- the version cannot
   stand still while the shape moves. (`AMGT-rk-40` will move the shape again and bumps to 2.1.0 with a new fingerprint;
   if it lands before you, reconcile: the fingerprint test is yours, the bump is whoever lands second.)
2. **Then skip-on-unchanged** (`batch.py`): a new `--plan-only` mode (READ-ONLY: EDGAR submissions index per fetchable
   CIK, `head_object`/`get_object` on the pool's `<accession>.analysis.json`; NO document download, NO model call, NO
   write) prints per name `SKIP-UNCHANGED` when the pool holds `<key>/<accession>.analysis.json` for the issuer's LATEST
   accession of the expected form AND its `analyzer_version == ANALYZER_VERSION`, else `WOULD-RUN` with the reason
   (`no analysis`, `stale version X`, `new accession`). The real run honours the same rule. `--dry-run` stays what it is:
   no network, no write, denominators only.
3. **Dedupe by CIK** (`batch.py:82-116` `plan()`): fetchable entries are grouped by CIK; ONE fetch and ONE analysis per
   CIK; outputs written for EVERY security_key in the group (`filings/v1/<key>/...` and `drafting/v1/<key>.json`, the
   same bytes, `shared_cik_with` recorded on each); the plan line prints `distinct_cik` and `duplicate_keys`.
4. **One writer** (`analyze.py`): `write_outputs(source_object, analysis, drafting, write_pool=False, out_dir=None,
   client=None, drafting_only=False) -> receipts` is THE ONLY function in the package that names `drafting/v1/`;
   `analyze.main()` `:1210-1230` and `batch.run_one()` `:144-152` both call it; `drafting_only=True` is the entry
   `AMGT-rk-41`'s rebuild uses.
5. **The newest vintage, never a typed date**: `batch.load_universe("newest")` lists `universe/v1/` in the pool
   (paginated), takes the greatest `YYYY-MM-DD.json` and prints `UNIVERSE: newest universe/v1/<date>.json of N
   vintages`; `run_batch.cmd:9` passes `--universe newest`; `analyze.py:1095-1097` `DEFAULT_UNIVERSE_PATH` is REMOVED
   and `--universe` defaults to `newest` (resolved through the same function) -- no worker folder, no typed date.
6. **The launcher quoted and read back** (`batch.py:119-130`, plus the live task): `task_definition()` renders `/TR
   "\"<launcher>\""` (escaped inner quotes) and gains `xml` -- the exported task XML with `<Command>` set to the quoted
   full launcher path and `<Arguments/>` empty, `<Enabled>false</Enabled>` preserved from the export; a new
   `--register-task-xml PATH` reads the LIVE task's XML (`schtasks /Query /TN ... /XML`), rewrites only those two
   elements, writes it to PATH, and prints the command that re-registers it (`schtasks /Create /TN
   OpalResearch-FilingsAnalyzer /XML PATH /F`). You RUN that command (AC5), then read the task back; Enabled must read
   false BEFORE and AFTER. Creation from XML is atomic on the disabled state -- the task is never enabled, not even for
   a second.
7. **D27**: the `UNRESOLVED-SOURCE:` plan line (`:198`) prints the two partitions -- rows WITH a security_key (written
   by the run) and rows WITHOUT (skipped, out of scope, `AMGT-rk-21`'s) -- so the dry-run and the run agree.
8. Tests in `lib/research/filings/tests/test_batch.py` (the model and the pool stubbed).

**1.3 The validation bar (`C-VALIDATION-NAMES`) and what this order NEVER does.** Proven by TESTS and by a DRY RUN /
PLAN over a three-row universe file you write under `.scratch/` in the U-1 shape from the validation's rows
(`CAT_US_Equity` with `filing_identity {source: edgar, cik: 18230, form_expected: 10-K}`; `CSL_AU_Equity` and
`6861_JP_Equity` with `source: none`), plus READ-ONLY pool reads. **The batch is NEVER run for real, NEVER enabled,
NEVER run over the 33, and no analysis is written**: `--write-pool` is not passed anywhere in this order, and
`--plan-only` makes no model call. The one live act is the DISABLED task's re-registration (AC5).

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 row R14-F5 @9c8e04cd9a; intake T4 (corrected by
measurement: the version is stamped and never bumped), T5, T6, T7, E8 (the same registration defect on two tasks), and
the validation's D27 (@b527b93214). PRD v0.13 @1699960261: `C-FILINGS-ANALYZER` `:689-690`, `:697-699`;
`C-VERBATIM-GATE` `:917-918`; `C-PRODUCTION-HOME` `:1643-1650`; section 10 `:1617-1618`; `C-VALIDATION-NAMES`
`:1652-1658`. The COO's round-14 decomposition record for this cell in `AMGT_RESAPP_DECOMP.md` is the postulate
paragraph landed beside this order.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/batch.py
lib/research/filings/analyze.py
lib/research/filings/run_batch.cmd
lib/research/filings/__init__.py
lib/research/filings/tests/test_batch.py
lib/research/filings/tests/test_filings.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~44/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-42.batch-correct-before-run.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant; this block governs WRITES. In `analyze.py`
  you own the version constants and fingerprint (`:59-61` and beside them), `main()` `:1101-1231`, the writer block
  `:1210-1230` (becomes `write_outputs`) and `DEFAULT_UNIVERSE_PATH` `:1095-1097`; the passes, the resolver and
  `build_analysis` `:277-990` are `AMGT-rk-40`'s. `drafting_build.py` and `pipeline.py` are `AMGT-rk-41`'s; `fetch.py`
  is `AMGT-rk-38`/`AMGT-rk-39`'s; `lib/research/management/run_batch.cmd` and the `OpalResearch-ExecManagement` task are
  chain E's. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~44 <0.9.0_WK_AMGT_RESAPP~44@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **`run_batch.cmd` IS A DEPLOY THE MOMENT IT TOUCHES DISK** (site-Z scheduled tasks run the working tree; `integrations/
  bloomberg/READ_HERE.md` s.3) -- harmless while the task is DISABLED, which it is and stays; verify control flow before
  you save it.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker; the DISABLED task is corrected, never enabled.** Secrets through `comp-secrets` only; this order
needs none (no model call). **EGRESS, EXACTLY:** EDGAR submissions-index reads in `--plan-only` (CAT's CIK) and
read-only S3 listing/reads of `universe/v1/` and `filings/v1/*/*.analysis.json`; nothing else. **No pool write.**
**No non-ASCII in anything you write.** **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- running the batch is that route.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** (vintages listed; analysis objects
read; universe rows).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W44-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it)
and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/filings/tests -p "test_*.py" -q 2>&1 | tail -5</invocation><expect>ends "Ran N tests" and "OK", including: (1) the fingerprint test -- output_contract_fingerprint(fixture analysis) equals OUTPUT_CONTRACT_FINGERPRINT, and a PLANTED extra top-level key on a copy of the analysis changes the fingerprint (the test that makes the version unable to stand still); (2) skip rule, three arms with a stubbed pool: an analysis at the latest accession carrying ANALYZER_VERSION reads SKIP-UNCHANGED; the same at analyzer_version opal-filings-analyze/1.0.0 reads WOULD-RUN stale version; an analysis at an OLDER accession reads WOULD-RUN new accession; (3) dedupe: a two-row universe sharing one CIK plans distinct_cik 1, duplicate_keys 1, the stubbed model receives exactly TWO calls (one two-pass analysis) and write_outputs is invoked for BOTH keys; (4) task_definition().create carries the escaped inner quotes around the launcher path and the xml's Command element equals the quoted full path with Enabled false; (5) the D27 plan line prints both unresolved partitions and their sum equals unresolved_source</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import glob, io, os, re
files = sorted(glob.glob('lib/research/filings/*.py'))
hits = {}
for f in files:
    n = 0
    for line in io.open(f, encoding='utf-8'):
        if 'drafting/v1/' in line and not line.lstrip().startswith('#'):
            n += 1
    hits[f] = n
print('files', len(files), 'literal drafting/v1/ in code lines:', hits)
print('writers', sum(hits.values()))
"</invocation><expect>the ONE-WRITER census over every .py in lib/research/filings (file denominator printed): the literal drafting/v1/ occurs in exactly 1 code line, in analyze.py inside write_outputs, and 0 in batch.py (today: batch.py:150 and analyze.py:1215, N = 2); writers 1</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, os
os.makedirs('.scratch/batch', exist_ok=True)
doc = {'as_of': '2026-09-18', 'schema_version': 1, 'names': [
  {'security_key': 'CAT_US_Equity', 'filing_identity': {'source': 'edgar', 'cik': 18230, 'form_expected': '10-K'}},
  {'security_key': 'CSL_AU_Equity', 'filing_identity': {'source': 'none', 'cik': None, 'form_expected': 'none'}},
  {'security_key': '6861_JP_Equity', 'filing_identity': {'source': 'none', 'cik': None, 'form_expected': 'none'}}]}
json.dump(doc, open('.scratch/batch/validation_universe.json', 'w'))
" && AWS_ACCESS_KEY_ID=DRYRUN-INVALID AWS_SECRET_ACCESS_KEY=DRYRUN-INVALID AWS_PROFILE= AWS_EC2_METADATA_DISABLED=true python -m lib.research.filings.batch --universe .scratch/batch/validation_universe.json --dry-run; echo "rc=$?"; git status --porcelain | head -5; echo "tracked-changes-end"</invocation><expect>the DRY RUN on the validation names under INVALID AWS credentials (the control: any S3 call would fail loudly): rc=0; BATCH prints names 3, with_filing_identity 1, would_fetch 1, distinct_cik 1, duplicate_keys 0, unresolved_source 2 split as 2 with a key / 0 without; DRY-RUN prints "nothing fetched, no model call, no pool write, no task run"; git status --porcelain shows no tracked file changed by the run (the scratch file is untracked and under .scratch/) -- a dry run writes nothing, anywhere</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.filings import batch
key, n = batch.resolve_universe('newest')
print('UNIVERSE: newest', key, 'of', n, 'vintages')
"</invocation><expect>a read-only listing of universe/v1/ in the pool: the newest vintage by date order (2026-09-16 at the cut -- print whatever is live) with the vintage count as its denominator; never a typed date</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && schtasks /Query /TN OpalResearch-FilingsAnalyzer /XML > .scratch/batch/task_before.xml && python -m lib.research.filings.batch --register-task-xml .scratch/batch/task_fixed.xml && schtasks /Create /TN OpalResearch-FilingsAnalyzer /XML .scratch/batch/task_fixed.xml /F && schtasks /Query /TN OpalResearch-FilingsAnalyzer /XML > .scratch/batch/task_after.xml && python -c "
import re
for name in ('before', 'after'):
    xml = open('.scratch/batch/task_%s.xml' % name, encoding='utf-16').read()
    cmd = re.search(r'<Command>(.*?)</Command>', xml, re.S); arg = re.search(r'<Arguments>(.*?)</Arguments>', xml, re.S); en = re.findall(r'<Enabled>(.*?)</Enabled>', xml)
    print(name, 'Command', repr(cmd.group(1) if cmd else None), 'Arguments', repr(arg.group(1) if arg else None), 'Enabled', en)
"</invocation><expect>the LIVE registered task read back on both sides of the one act: before -- Command 'C:\Users\Opal', Arguments 'Bloomberg\Desktop\ajb_workspace\lib\research\filings\run_batch.cmd', Enabled false (the measured defect); after -- Command is the FULL launcher path ending run_batch.cmd (quoted), Arguments empty or absent, and EVERY Enabled element reads false. If schtasks emits UTF-16 with a BOM the read above handles it; if it emits another encoding, print the raw bytes' first 4 and adapt the read, recording what was measured. An Enabled true at any point is a FAIL of this criterion and is reverted immediately with schtasks /Change /TN OpalResearch-FilingsAnalyzer /DISABLE</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
from lib.research.filings import analyze
s3 = boto3.client('s3', region_name='us-east-1')
keys = []
token = None
while True:
    kw = {'Bucket': 'opal-data-harvest', 'Prefix': 'filings/v1/'}
    if token: kw['ContinuationToken'] = token
    page = s3.list_objects_v2(**kw)
    keys += [o['Key'] for o in page.get('Contents', []) if o['Key'].endswith('.analysis.json')]
    token = page.get('NextContinuationToken')
    if not token: break
versions = {}
for k in keys:
    doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    versions[doc.get('analyzer_version')] = versions.get(doc.get('analyzer_version'), 0) + 1
print('analysis_objects', len(keys), 'by_version', versions, 'current', analyze.ANALYZER_VERSION, 'would_skip_on_version_alone', versions.get(analyze.ANALYZER_VERSION, 0))
"</invocation><expect>the READ-ONLY census that proves the order of operations: every stored analysis object in the pool (the intake read 12; print the live count) carries analyzer_version opal-filings-analyze/1.0.0 and 0 of them carry the new ANALYZER_VERSION -- so the skip rule, built AFTER the bump, would skip NONE of the stale analyses. Nothing is written</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-42"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.batch --universe .scratch/batch/validation_universe.json --plan-only 2>&1 | tail -8</invocation><expect>the READ-ONLY plan on the validation names: for CAT_US_Equity the EDGAR submissions index is read (its latest 10-K accession printed), the pool is checked for filings/v1/CAT_US_Equity/<accession>.analysis.json and the line reads WOULD-RUN with its reason (no analysis, or stale version if AMGT-rk-38's battery wrote a source object but no analysis exists -- print what is found); the two source-none names print UNRESOLVED-SOURCE; "PLAN-ONLY: no document fetched, no model call, no pool write, no task run" is printed; the batch is not run</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC5 is a PowerShell-free sequence: `schtasks` is a native executable reachable from Git Bash; if `/XML` output
redirection produces an encoding your read cannot parse, record the bytes and adapt the read -- never the task.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~44/AMGT_RESAPP.TO-AMGT-rk-42.batch-correct-before-run.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, stating the task's Enabled value read back last.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~44</slot>
<fabric>site-z</fabric>
