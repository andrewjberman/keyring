# AMGT_RESAPP task order -- `AMGT-rk-44` -- the management batch census: real filings only, never a placeholder; keys cut slash-safe; the launcher quoted and read back; the population unpinned

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-44</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~46</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- (comp-schedule --budget 500 ran at the cut, 2026-09-18 19:5xZ, saved by the issuer) this order TOUCHES ONE EXISTING, DISABLED Windows scheduled task, `OpalResearch-ExecManagement`
  (created DISABLED by AMGT-rj-8; measured 2026-09-18 by `schtasks /Query /V`: Status Disabled, Scheduled Task State
  Disabled, Last Result 267011 = has never run, Weekly SUN; its action is split at the space in the path -- Execute
  `C:\Users\Opal`, the rest an argument). It corrects that task's ACTION to the quoted launcher path with
  `schtasks /Change /TR` (which does not touch the enabled state) and reads it back. It arms NO cadence, NO alarm, NO
  monitor, creates NO task, and NEVER enables this one: the task is DISABLED before and DISABLED after (AC3 prints both),
  and activation stays Andrew's word (`batch.py:9-11`). The standing collection-stays-off / no-monitor moratorium is
  unaffected. If `schtasks /Change /TR` is refused on this box, the fallback is `/Create /F` immediately followed by
  `/Change /DISABLE` in the SAME shell call, and the report says so with the seconds between them (the trigger is SUN
  07:00, so no run can fall in that window).
comp-iam: DECLARED-NOT-APPLICABLE -- this order reads the pool (list + get under filings/v1/ and crosswalk/v1/) under the
  existing credentials, writes NO pool object, grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~46`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and `lib/research/management/`
exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~46;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-44` (R14-E2; FWD-17; round-13 row W32-S3; intake rows E6, E7, E8)

**The analysis row, verbatim** (`ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`): *"the batch census: real filings only,
never a placeholder; keys cut slash-safe (`batch.py:81-84`); launcher quoted, universe unpinned"* -- serves FWD-17,
W32-S3, E6-E8; co-sign no.

**THE MEASURED STATE (read at HEAD `4f44431d34`; the pool and the box read 2026-09-18 ~20:xxZ by the drafting seat --
RE-MEASURE AT SPAWN).**
- **The census splits S3 keys on `/`.** `persisted_filing_keys()` (`lib/research/management/batch.py:76-86`) walks every
  key under `filings/v1/`, does `obj["Key"].split("/")` and takes `parts[2]` as the name, requiring `parts[3]` to end
  `.source.json` (`:83-85`). For `filings/v1/BP/_LN_Equity/<x>.source.json` the parts are
  `['filings','v1','BP','_LN_Equity','<x>.source.json']`, `parts[3]` is `_LN_Equity`, and the name is NEVER added -- so
  `BP/_LN_Equity` and `NG/_LN_Equity` can never be built, and the run reports success (row W32-S3 measured the same
  slash class one prefix over: `posture/v1/BP/_LN_Equity/...` landed one level deeper). Measured live: `filings/v1/`
  carries **190 `.source.json` keys under 190 distinct name prefixes, two of them slash names (`BP/_LN_Equity`,
  `NG/_LN_Equity`)**.
- **The census counts placeholders as filings.** Of those 190 keys, **178 are `UNRESOLVED-SOURCE.source.json`
  placeholders** (the explicit objects AMGT-rk-24's producer half writes for every unfiled name --
  `lib/research/filings/batch.py:198`, `:222`) and **12 are real accessions**. `persisted_filing_keys()` returns 188
  names (190 minus the 2 slash names it drops), so `plan()` (`:89-110`) would build 188 -- and `run_one()` (`:127-142`)
  would write ~176 zero-officer rosters that the adapter serves as SERVED until AMGT-rk-43 lands (intake E7: "one enable
  would turn 7 real rosters into 183 'served' ones, 176 of them empty").
- **The launcher is split at the space.** The registered task's action is `Execute = C:\Users\Opal` with the remainder
  as an argument (intake E8; `schtasks /Query /V` 2026-09-18 shows `Task To Run` wrapping across the space). The
  `/Create` string `task_definition()` builds (`batch.py:119-120`) wraps the path in ONE pair of quotes, which
  `schtasks /TR` consumes as the argument delimiter and then splits the unquoted path at "Opal Bloomberg" -- the exact
  class banked for this device (an unquoted path with a space, success shape). Last Result 267011: it has never run.
- **The population is pinned to a typed date.** `run_batch.cmd:12` runs
  `--universe universe/v1/2026-09-15.json`; the pool carries `universe/v1/2026-09-16.json` already, and
  `crosswalk/v1/2026-09-15.json` (the population of record, MEASURED = 33) is the only crosswalk vintage. The batch
  reads `document.get("names")` from the universe (`:95`), which is the 256-name union, not the keyed population.
- The other batch driver, `integrations/bloomberg/research/management_posture_batch.py` (AMGT-rk-22), already takes the
  population from the newest crosswalk's MEASURED records (`keyed_population()` `:83-93`) and tests each name's LATEST
  `filings/v1/<key>/` object for `status == "RESOLVED"` with a per-name prefix (`filed_status()` `:96-107`) -- slash-safe
  and placeholder-safe. Two drivers now disagree about the population; this order makes the SCHEDULED one (`batch.py`)
  correct and leaves the reconciliation of the two as a stated residue, not a silent one.

**RULED -- what this order builds (all in `lib/research/management/`; no other file).**
1. **The population is the crosswalk's MEASURED records, resolved to the NEWEST vintage, never a typed date and never a
   store listing** (PRD v0.13 @`1699960261` s.10 `:1617-1618`: *"A stage's population is the crosswalk's MEASURED records
   (`crosswalk/v1/<date>.json`), never a store listing, a hand list or a worker's folder"*). `batch.py` reads it through
   the existing `lib.research.identity.crosswalk.load_crosswalk()` (`crosswalk.py:496-510`, which already resolves
   `crosswalk/v1/<latest>` from the pool at `:513-530` and honours a local override path / `AMGT_CROSSWALK_PATH`) --
   build ladder step 2, no new reader. `--universe` is RETIRED; `--crosswalk <local path>` is the QA override. The dry
   run prints the vintage it resolved. The `names_in_union` universe read inside `compute_pool` is AMGT-rk-45's, not this
   order's.
2. **The census: real filings only, slash-safe.** `persisted_filing_keys()` is replaced by a census that, for the
   population's keys, lists `filings/v1/<key>/` PER NAME (a prefix S3 resolves whatever the key contains), classes the
   name by the key NAME first -- an accession `<digits>.source.json` versus the placeholder
   `UNRESOLVED-SOURCE.source.json` -- and then reads the LATEST accession object and requires `status == "RESOLVED"`.
   No key is ever split on `/`; where a name must be cut from a full key, it is `key[len(FILINGS_PREFIX):].rsplit("/", 1)[0]`
   (the accession segment carries no slash; the name may). The plan prints FOUR partitions from ONE pass whose sum is the
   population -- `real-filing` (would-build), `placeholder-only`, `no-object`, and `unresolved-accession` (an accession
   object whose status is not RESOLVED; expected 0, printed anyway) -- and `would_build == real-filing`.
3. **A status count never travels alone.** `main()`'s BATCH DONE line (`:193-195`) prints `RESOLVED-with-officers` (>= 1
   officer) beside `RESOLVED` (status) and beside `built`, per PRD v0.13 `C-EXEC-MANAGEMENT` `:731-732` (*"Every census
   and report prints the content count ... beside the status count"*). `roster_source` FILING/BLOOMBERG_FALLBACK counts
   are R14-E5's and are not printed here.
4. **The launcher, quoted and read back.** `task_definition()` (`:113-124`) builds the `/Create` string with the launcher
   path in ESCAPED inner quotes -- `/TR "\"<launcher>\""` -- and gains a `change_action` string
   (`schtasks /Change /TN <task> /TR "\"<launcher>\""`) and a `read_back` string
   (`powershell -NoProfile -Command "(Get-ScheduledTask -TaskName '<task>').Actions | Format-List Execute,Arguments"`).
   The existing DISABLED task's action is corrected with `change_action` (enabled state untouched) and read back:
   `Execute` is the full path ending `run_batch.cmd` and `Arguments` is empty. The task STAYS DISABLED.
5. **`run_batch.cmd:12`** becomes `python -m lib.research.management.batch --write-pool` -- no typed date anywhere in the
   file.
6. **Tests** (`tests/test_management.py`): `TaskDefinitionTest` (`:473-494`) is updated for the quoted `/TR` and the
   subtraction over the four partitions; a new census test PLANTS, on a `_StubS3` (`:255-273`) and a local crosswalk
   document with five MEASURED records, exactly these keys -- `filings/v1/BP/_LN_Equity/000000000000000001.source.json`
   (RESOLVED), `filings/v1/NG/_LN_Equity/UNRESOLVED-SOURCE.source.json`,
   `filings/v1/CAT_US_Equity/UNRESOLVED-SOURCE.source.json`, `filings/v1/6861_JP_Equity/000000000000000002.source.json`
   (RESOLVED), nothing under `filings/v1/CSL_AU_Equity/` -- and asserts real-filing == {`BP/_LN_Equity`,
   `6861_JP_Equity`}, placeholder-only == {`NG/_LN_Equity`, `CAT_US_Equity`}, no-object == {`CSL_AU_Equity`}, 5 == 2+2+1+0.
   The three validation names and the two slash names are the planted cases, exactly as the round's bar names them.

**THE TASK STAYS DISABLED. No run. No pool write. No vendor call.** The proof is the unit test, the batch's own
`--dry-run` against the live pool (a read), and the task action read-back. Andrew's word stands over any enable
(`C-VALIDATION-NAMES`, PRD v0.13 `:1652-1655`: no fleet run before the process is validated end to end).

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @`9c8e04cd9a` s.4 row R14-E2 (chain E, independent) and s.6
(W32-S3 carried to E2); the intake `CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` s.2B rows E6, E7, E8 and the
cross-panel rows "Scheduled-task registration" and "Key census by splitting a path on `/`"; the CRO's brief
`BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` s.1.2 item 4, s.4 items 2-3, s.5 "Census", s.6 traps 2-3.
**PRD v0.13 @`1699960261`**: s.10 population rule (`:1617-1618`), `C-PRODUCTION-HOME` (`:1643-1650`; config beside its
producer -- `run_batch.cmd` and `task_definition()` are that config), `C-EXEC-MANAGEMENT` content-beside-status
(`:731-732`), `C-VALIDATION-NAMES` (`:1652-1658`). (v0.13 moved only hygiene text out of the CONTRACTS body; every
rule cited here stands.)

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/batch.py
lib/research/management/run_batch.cmd
lib/research/management/tests/test_management.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~46/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-44.management-batch-census.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `enrich.py` and `roster.py` are chain-E siblings' files (rk-45, rk-46)
  and are READ ONLY here; `integrations/bloomberg/research/management_posture_batch.py` is read for its population
  pattern and is not edited. A READ needs no grant. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~46 <0.9.0_WK_AMGT_RESAPP~46@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer; every `.py` edit passes `.tools/commit-gate.sh`). Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **THE TASK STAYS DISABLED -- you never run
`schtasks /Change /ENABLE`, never run `run_batch.cmd`, never run the batch without `--dry-run`.** **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** **No vendor call** -- none is named, and `--dry-run` makes none
(`batch.py:179-183`). **No pool write.** No non-ASCII in anything you write. **PUSH: never;** LD-0522 puts the push
with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the "190 keys / 178 placeholders /
12 real / 33 MEASURED" figures above are this document's; AC2 re-measures them at spawn.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W46-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** Two known off-task
facts you WILL meet: `roster.load_source_object()` (`roster.py:472-498`) takes `sorted(keys)[-1]`, so a name carrying
BOTH a real accession and a placeholder would pick the placeholder (`U` sorts after every digit) -- that is
AMGT-rk-46's file and its order names it; and the two batch drivers' population rules now differ -- file ONE row naming
both and keep working.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-44"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_management -v 2>&1 | tail -40</invocation><expect>every test passes ("OK" on the last line, "Ran N tests" printed with N >= 27 -- 25 at HEAD plus at least the planted census test and the quoted-launcher test); the output names a census test whose planted keys are the three validation names (CAT_US_Equity placeholder-only, CSL_AU_Equity no-object, 6861_JP_Equity real) and the two slash names (BP/_LN_Equity real, NG/_LN_Equity placeholder-only) and asserts 5 == 2 + 2 + 1 + 0; and a task-definition test that asserts the /TR argument carries the launcher path inside ESCAPED inner quotes and that run_batch.cmd carries no typed date</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-44"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.management.batch --dry-run 2>&1 | tail -20</invocation><expect>the dry run against the LIVE pool prints the crosswalk vintage it resolved (crosswalk/v1/2026-09-15.json at the cut, or newer -- never a typed date), a POPULATION line with the MEASURED count (33 at the cut), and the four partitions whose sum equals it -- real-filing (12 at the cut; re-measure), placeholder-only (21 at the cut), no-object (0), unresolved-accession (0) -- with the placeholder-only list naming BP/_LN_Equity and NG/_LN_Equity BY NAME (today both are silently absent from every list the batch prints); WOULD-BUILD equals the real-filing list; the last line is the DRY-RUN line stating nothing built, no Lusha call, no SERP call, no pool write, no task run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-44"><invocation>cd "$(git rev-parse --show-toplevel)" && powershell.exe -NoProfile -Command "\$t = Get-ScheduledTask -TaskName 'OpalResearch-ExecManagement'; \$t.Actions | Format-List Execute,Arguments; Write-Output ('STATE ' + \$t.State); Write-Output ('SETTINGS-ENABLED ' + \$t.Settings.Enabled)" 2>&1 | tail -12</invocation><expect>run ONCE BEFORE the change and ONCE AFTER, both outputs recorded: BEFORE, Execute reads "C:\Users\Opal" with the remainder of the path in Arguments (the split); AFTER, Execute reads the ONE full path ending "\lib\research\management\run_batch.cmd" and Arguments is empty; in BOTH, STATE reads Disabled and SETTINGS-ENABLED reads False -- the task was never enabled by this order (denominator: 1 task, 2 reads)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-44"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, re
b = io.open('lib/research/management/batch.py', encoding='utf-8').read()
c = io.open('lib/research/management/run_batch.cmd', encoding='utf-8').read()
print('run_batch.cmd typed dates', len(re.findall(r'20[0-9]{2}-[0-9]{2}-[0-9]{2}', c)))
print('run_batch.cmd --universe', c.count('--universe'))
print('batch.py split(\"/\") occurrences', b.count('.split(\"/\")'))
print('batch.py UNRESOLVED-SOURCE.source.json guard', b.count('UNRESOLVED-SOURCE.source.json'))
print('batch.py load_crosswalk', b.count('load_crosswalk'))
print('DENOMINATOR files 2')
"</invocation><expect>run_batch.cmd carries 0 typed dates and 0 occurrences of --universe (1 and 1 at HEAD); batch.py carries 0 occurrences of .split("/") (1 at HEAD :83), at least 1 occurrence of the placeholder guard string UNRESOLVED-SOURCE.source.json (0 at HEAD) and at least 1 of load_crosswalk (0 at HEAD) -- two files, denominator printed</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC3's BEFORE read is taken as your first act after the worktree check, before any edit.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~46/AMGT_RESAPP.TO-AMGT-rk-44.management-batch-census.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once, naming the AC2 partition counts and the AC3 before/after action strings.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~46</slot>
<fabric>site-z</fabric>
