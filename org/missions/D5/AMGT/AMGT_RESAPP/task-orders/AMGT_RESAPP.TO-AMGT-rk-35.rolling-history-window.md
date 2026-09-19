# AMGT_RESAPP task order -- `AMGT-rk-35` -- the rolling history window: the block ends at the issuer's LATEST CLOSED fiscal year, never a fixed date

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-35</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~39</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the model-block refresh
  cadence stays Andrew's (C-MODEL-WINDOW-AND-ROWS (3)); `scheduled_daily_pull.cmd` is not touched; the standing
  collection-stays-off / no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned prefixes this producer already
  writes (`raw/bloomberg/<key>/<stamp>/` and `derived/model_block/<key>/<stamp>/` in `opal-data-harvest`) under the
  credentials the producer already runs with on this box; it grants no permission, provisions no resource, deploys
  no Lambda and touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~39`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --short=10 HEAD`, and tests that `org/`,
`.tools/` and every path in section 3 exists; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN M's QUEUE
OF THREE orders, in this sequence: `AMGT-rk-35` (this one), `AMGT-rk-36`, `AMGT-rk-37`. All three edit
`integrations/bloomberg/research/model_block_pull.py`, and the last two each redeploy the ONE Lambda
`opal-amgt-scoped-api`, so this surface has ONE writer and each deploy is sequenced strictly after the one before it.
This order comes FIRST in the queue and comes AFTER `AMGT-rk-34` (slot `~38`), whose builder this order exercises
(section 1.2).** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~39;`. **NEVER RUN AN INSTALL.**
**Bloomberg, ANY scenario: READ `integrations/bloomberg/READ_HERE.md` FIRST** (two-phase budgeted sign-in; a refusal
names the SURFACE; the derived layer is current-day-only; never mint `data/bloomberg/`). This order makes Bloomberg
requests -- exactly two per validation name, six in all -- through the estate client
`integrations/bloomberg/mcp/blp_client.py` only, as the producer already does (`model_block_pull.py:147-156`, `:223`,
`:227-229`).

## 1. THE CELL, inlined in full -- `AMGT-rk-35` (R14-M2; FWD-1, FWD-16; Model brief M2; validation D4, D5)

**The analysis row, verbatim** (`ledger/ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`, chain M, `R14-M2 -> M3 -> M4`):
*"M2 the rolling history window (`HIST_END` fixed today); ..."* -- serves FWD-1, FWD-16, M2-M5, L8; co-sign **yes,
each**. The chain marker `->` means these three cells edit the SAME FILE and are sequenced (s.4 preamble).

**The measured state** (validation report @`b527b93214` D4 :183-184, *"the history end date is hardcoded to
2025-12-31, so FY2026 is excluded for every name"*; s.2 grid :61: CSL and Keyence blocks *"FY2026 missing (D4)"*;
D5 :185-186, *"3 hardcoded securities and no dry-run"*; Model brief M2 @`f48864fce6` :92 and s.4 row 3): at HEAD
`HIST_START = "2016-01-01"`, `HIST_END = "2025-12-31"`, `PERIODICITY = "YEARLY"` (`model_block_pull.py:100-102`);
`stage_pull` requests `[HIST_START, HIST_END]` (`:227-229`); `merge_by_fiscal_year` groups rows by the calendar year
of `date` (`:256-273`, C-FISCAL-YEAR-JOIN); `stage_derive` emits every group as `fiscal_years` (`:413-437`,
`:443-444`). Keyence's fiscal year ends in March and CSL's in June: FY2026 for both has ENDED and been REPORTED by
2026-09-18, and the fixed end date excludes it. `SECURITIES` (`:53`) is a three-name constant used as the default
population (`:507`); `cmd_pull` writes `pull_log.json` into worker `~1`'s deliverables folder (`_pull_log_path`,
`:464-467`) -- a `C-PRODUCTION-HOME` instance the PRD's list does not name.

**The PRD constraints this cell serves** (PRD v0.13 @`1699960261`):
- `C-MODEL-WINDOW-AND-ROWS` (`:872-885`), clause (1), verbatim: *"**The window rolls:** the history ends at each
  issuer's LATEST CLOSED fiscal year -- a year that has ENDED and been REPORTED -- never a fixed date (today
  `HIST_END = "2025-12-31"`, `model_block_pull.py:101`)."* Clause (3): the model block is an instantiation stage
  (section 10), pulled when a security is added, refreshed on a cadence Andrew sets. Clause (4): every Bloomberg
  call names the security as `<RESOLVED bloomberg id> Equity` or reads the block's own security string.
- `C-VALIDATION-NAMES` (`:1652-1658`): proven on Caterpillar / CSL / Keyence; a run on those three IS the validation;
  no fleet run, no re-run of the covered 33.
- `C-PRODUCTION-HOME` (`:1643-1650`): a production code path never writes a WORKER'S deliverables folder; a dry run
  writes nothing, anywhere. `C-UNIT-MAP-MEASURED` (`:848-859`): the map is built for EVERY name at instantiation.
- `C-RAW-BEFORE-DERIVED` (`:899-901`), `C-FISCAL-YEAR-JOIN` (`:887-889`), `C-BLOOMBERG-BASIS` (`:891-895`) -- unchanged
  and binding on every byte you add.

**RULED -- what you build, in `integrations/bloomberg/research/model_block_pull.py`:**

1. **The request window rolls.** `HIST_END` stops being a constant: `stage_pull` requests
   `[HIST_START, <pull date, UTC, YYYY-MM-DD>]`, and the request record in the pull log / ledger carries the actual
   `end_date` requested (`:230-240` already records it). Nothing about `HIST_START` or `PERIODICITY` moves.
2. **The derive stage names the latest CLOSED fiscal year and excludes what is not closed.** A fiscal-year group is
   CLOSED when it carries at least one REPORTED statement field (`SALES_REV_TURN` or `IS_EPS` non-null in the merged
   group -- both are in `HIST_FIELDS` `:80`, `:86`); a group carrying only price/ratio fields for a period Bloomberg
   returned ahead of the filing is NOT closed. `stage_derive` (i) emits ONLY closed groups as `fiscal_years` and
   `fiscal_year_line_item` figures; (ii) records every excluded group under `unresolved` with `scope`
   `fiscal_year_line_item`, its `fiscal_year`, and reason `"fiscal year not closed/reported: no statement field in the
   merged group"` -- COUNT IN EQUALS COUNT OUT stays true on the block's own accounting; (iii) writes a
   `history_window` object on the block: `{"start": HIST_START, "end_requested": <the pull's end_date read from the
   raw request record>, "latest_closed_fiscal_year": max(fiscal_years), "rule": "<the sentence in (ii)>"}`. The
   existing `orphan_price_rows` / `fiscal_year_row_count` fields keep their meaning over the CLOSED set.
3. **The population is never a constant.** `--securities` becomes REQUIRED for `pull` and `derive` (no default from
   `SECURITIES`; the constant is removed or reduced to documentation of the s-1 pilots); `--population crosswalk` is
   NOT added here (the fleet run is not this round's act) -- a caller that wants the 33 must name them. The
   three-per-invocation cap (`:509-510`, F2/G-24) stays.
4. **`--dry-run` for BOTH stages**: prints every request it would make (security string, fields, `start_date`,
   `end_date`, periodicity) and every key it would write, and writes NOTHING -- no S3 object, no ledger
   `record_run`, no pull log, no unit-map entry.
5. **`C-PRODUCTION-HOME` for the pull log:** `_pull_log_path` (`:464-467`) no longer names a deliverables folder. The
   pull log becomes `--pull-log <path>` (optional; default: no file -- the ledger's `record_run` at `:246` already
   records every landing). File a row naming the instance (`spec_asserts`: C-PRODUCTION-HOME; `world_is`:
   `model_block_pull.py:464-467` @<hash> wrote `deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json`).
6. **Units at instantiation.** `stage_derive` builds the security's unit-map entries THROUGH `AMGT-rk-34`'s builder
   (`integrations/bloomberg/research/build_unit_map.py`, section 1.2) when the map has no entry for that security,
   merging into the map's committed home beside the producer; a MEASURED entry is never overwritten. The resulting
   block carries NO figure refused for a missing map entry (Model brief s.6, "Instantiation": *"on each validation
   name, a block with no refused-for-map figure and no hand step"*). A unit the builder cannot measure stays
   UNRESOLVED with its reason and the figure stays REFUSED -- never inferred.
7. **The act:** `--dry-run` first (AC1), then `pull` then `derive` for exactly `"CAT US Equity" "CSL AU Equity"
   "6861 JP Equity"` (the validation report's own security strings, @`b527b93214` :30-32 -- the yellow key is
   appended, `C-MODEL-WINDOW-AND-ROWS` (4)). Six Bloomberg requests in all. **The 33 covered names are NOT pulled and
   NOT re-derived by this order** (AC4 proves it).

### 1.2 DEPENDENCY: `AMGT-rk-34` (slot `~38`) -- the discovery rule, run before any edit

`AMGT-rk-34` builds the unit map for every name from landed raw and lands the builder module. Before editing, print
(i) `test -f integrations/bloomberg/research/build_unit_map.py && echo BUILDER_PRESENT || echo BUILDER_ABSENT`;
(ii) the map's home: `python -c "import importlib.util as u; s=u.spec_from_file_location('m','integrations/bloomberg/research/model_block_pull.py'); m=u.module_from_spec(s); s.loader.exec_module(m); print('FIELD_MAP_HOME', m._FIELD_MAP_PATH)"`
-- it must NOT lie under `org/missions/` (that is rk-33's landing, which rk-34 depended on). If the builder is absent
or the home is still a worker's folder, **STOP and file a row** (`spec_asserts`: rk-34/rk-33 landed before rk-35;
`world_is`: what you printed at <hash>). Do not build the units yourself; the whole point of the sequence is ONE
builder. Record the builder's landing hash (`git log -1 --format=%h -- integrations/bloomberg/research/build_unit_map.py`).

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 chain M row `R14-M2` @`9c8e04cd9a`;
Model brief @`f48864fce6` s.1.2, s.4 row 3, s.5 item 2, s.6 "Window"; validation report @`b527b93214` D4, D5;
intake rows M2, M6. PRD **v0.13 @`1699960261`** (`C-MODEL-WINDOW-AND-ROWS` clauses (1), (3), (4), carried unchanged from v0.11 through v0.13;
`C-VALIDATION-NAMES`; `C-PRODUCTION-HOME`). Code cited @HEAD (draft-time HEAD `ced1f5f84d`; `model_block_pull.py`
carries no working-tree change; rk-34's edits will have moved the line numbers around `:286-336` -- re-read at spawn).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain M is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-35`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-35` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-35.rolling-history-window.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read `READ_HERE.md`, `blp_client.py`,
  `run_checks.py`, `scoped_amgt.py`, the pool, the crosswalk); this block governs WRITES. The unit map's home resolves
  under `integrations/bloomberg/research/` (rk-33's landing) and is covered by the directory grant; you commit the
  entries your derive adds. Nothing under `lib/` moves in THIS order. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~39 <0.9.0_WK_AMGT_RESAPP~39@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **THE POOL WRITE IS A LIVE ACT UNDER THE ROUND'S CO-SIGN DISCIPLINE** (analysis s.4 @`9c8e04cd9a` :158-160: every
  `yes` cell opens its change-management entry BEFORE the first live act and gets a never-widen pair naming its blast
  radius with each writer COUNTED). **Blast radius, stated exactly so the pair can name it:** three NEW keys
  `raw/bloomberg/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<stamp>/{refdata,histdata}.json` and
  `derived/model_block/<same three>/<stamp>/model_block.json`, plus the map entries for those three -- **none of the
  three is in the pool crosswalk, so NOTHING SERVED CHANGES until `R14-I1` lands their identity**; the 33 served
  blocks are untouched (AC4). Writers of `derived/model_block/`: ONE (`model_block_pull.py` `derive`); re-census at
  spawn as rk-34 did. ROLLBACK: nothing to roll back on the served plane; the three unserved keys are left in place
  (the reader ignores keys the crosswalk does not hold) and named in the entry. Open BEFORE the pull:
  `python .tools/deploy_ledger.py open --slug amgt-rk35-rolling-window-validation-names-20260918 --title "AMGT-rk-35: rolling history window; pull+derive on the three validation names (unserved keys); co-signed rk-35 pair" --author 0.9.0_WK_AMGT_RESAPP~39 --leg "L1|git|window rule + dry-run + pull-log home committed|commit hash" --leg "L2|activation|raw + derived landed for CAT/CSL/Keyence (3 keys, unserved)|key list + stamps" --leg "L3|verify|33 served stamps unchanged; validation blocks carry latest closed FY|AC2/AC3/AC4 output" --window-hours 4`
  and commit its sentinel. CLOSE with every leg proven before your grading read.

## 4. BOUNDS

**BLOOMBERG: exactly two requests per validation name (one `ReferenceDataRequest`, one `HistoricalDataRequest`),
six in all, on `"CAT US Equity"`, `"CSL AU Equity"`, `"6861 JP Equity"` -- and NOTHING for any of the 33 covered
names.** That pull is inside the validation Andrew set as the bar (`C-VALIDATION-NAMES`); a fourth name is a
violation. A DAPI refusal names its surface (READ_HERE) and is a row, never a retry loop. **No other vendor call.**
**PORTAL FROZEN** (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker; the cadence stays Andrew's.** No Lambda deploy in THIS order (the block's new `history_window`
key and shorter/longer `fiscal_years` are read by the adapter as-is: `read_model` serves `fiscal_years` from the block,
`scoped_amgt.py:2529`). No Terraform, no IAM. No non-ASCII in anything you write. **PUSH: never.** Your work is LOCAL;
LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- record the 33 names' newest stamps
at spawn (`pre_act_stamps.json` in your deliverables folder) BEFORE any act; AC4 compares against that file.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W39-S<k>`, `<k>` restarting at 1 and CONTINUING across the three orders of
your queue; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by textual splice inside the one
fenced JSON array (never re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND
KEEP WORKING.** Known candidates: D5's second half (`:246`, the ledger write goes around the S3 client it was given --
`ledger.py:64-66,87`) is NOT this cell's fix; row it if you touch that line.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-35"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import subprocess, boto3, datetime, re
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
keys = ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']
def count(prefix): return sum(1 for pp in pg.paginate(Bucket=B, Prefix=prefix) for _ in pp.get('Contents', []))
before = {k: (count('raw/bloomberg/' + k + '/'), count('derived/model_block/' + k + '/')) for k in keys}
st0 = subprocess.run(['git', 'status', '--porcelain', '--', 'integrations/', 'org/missions/'], capture_output=True, text=True).stdout
r = subprocess.run(['python', 'integrations/bloomberg/research/model_block_pull.py', 'pull', '--dry-run', '--securities', 'CAT US Equity', 'CSL AU Equity', '6861 JP Equity'], capture_output=True, text=True, timeout=100)
print('rc', r.returncode); print(r.stdout[-3000:]); print('STDERR', r.stderr[-600:])
today = datetime.datetime.utcnow().strftime('%Y-%m-%d')
print('today_utc', today, 'end_date_lines_with_today', len(re.findall('end_date.{0,6}' + today, r.stdout)), 'lines_with_2025-12-31', r.stdout.count('2025-12-31'))
after = {k: (count('raw/bloomberg/' + k + '/'), count('derived/model_block/' + k + '/')) for k in keys}
st1 = subprocess.run(['git', 'status', '--porcelain', '--', 'integrations/', 'org/missions/'], capture_output=True, text=True).stdout
print('s3_before', before); print('s3_after', after); print('s3_unchanged', before == after); print('porcelain_unchanged', st0 == st1)
print('pull_log_literal_in_source', open('integrations/bloomberg/research/model_block_pull.py', encoding='utf-8').read().count('0.9.0_WK_AMGT_RESAPP~1'))
"</invocation><expect>THE DRY RUN, BEFORE ANY LIVE ACT: rc 0; the printed plan names exactly three securities, each with one ReferenceDataRequest and one HistoricalDataRequest whose end_date is TODAY's UTC date (end_date_lines_with_today 3, lines_with_2025-12-31 0 -- the fixed date is gone from the request); s3_unchanged True and porcelain_unchanged True (a dry run writes nothing, anywhere -- no S3 key, no ledger row, no pull log, no map entry); pull_log_literal_in_source 0 (the producer no longer names worker ~1's folder anywhere in its source). Any write, any 2025-12-31, or a fourth security is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-35"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
for k, fye in [('CAT_US_Equity', 'December'), ('CSL_AU_Equity', 'June'), ('6861_JP_Equity', 'March')]:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    if not ks:
        print(k, 'NO_BLOCK'); continue
    b = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read())
    hw = b.get('history_window') or {}
    fys = [str(x) for x in b.get('fiscal_years') or []]
    unclosed = [u for u in b.get('unresolved') or [] if 'not closed' in str(u.get('reason'))]
    print(k, 'fye', fye, 'block', ks[-1], 'security', b.get('security'), 'raw_stamp_used', b.get('raw_stamp_used'))
    print('  fiscal_years', fys, 'fiscal_year_row_count', b.get('fiscal_year_row_count'), 'figures', len(b.get('figures') or []), 'unresolved', len(b.get('unresolved') or []))
    print('  history_window', json.dumps(hw, sort_keys=True))
    print('  latest_closed_fy', hw.get('latest_closed_fiscal_year'), 'max_fiscal_year', max(fys) if fys else None, 'unclosed_groups', [(u.get('fiscal_year'), u.get('reason')) for u in unclosed])
    fy26 = [f for f in b.get('figures') or [] if str(f.get('fiscal_year')) == '2026' and f.get('mnemonic') in ('SALES_REV_TURN', 'IS_EPS')]
    print('  FY2026_statement_figures', [(f.get('mnemonic'), f.get('value')) for f in fy26])
"</invocation><expect>THE WINDOW, ON THE THREE VALIDATION NAMES AFTER pull+derive: each has a block whose security string is the yellow-keyed form (CAT US Equity / CSL AU Equity / 6861 JP Equity); history_window carries start 2016-01-01, end_requested equal to the pull date, latest_closed_fiscal_year equal to max(fiscal_years), and the rule sentence; THE DISCRIMINATOR (D4): CSL (June FYE) and Keyence (March FYE) each show 2026 in fiscal_years with at least one FY2026 statement figure (SALES_REV_TURN or IS_EPS with a non-null value) -- exactly the year the fixed end date excluded -- while CAT (December FYE) shows latest_closed_fy 2025 and, if Bloomberg returned any 2026 group, that group appears under unclosed_groups with the not-closed reason and NOT in fiscal_years; fiscal_year_row_count equals len(fiscal_years). A validation name with no block, a 2026 group served for CAT as closed, or CSL/Keyence still ending at 2025 is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-35"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, sys
sys.path.insert(0, '.')
from lib.research.checkface.run_checks import check_block
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    if not ks:
        print(k, 'NO_BLOCK'); continue
    b = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read())
    cf = check_block(b.get('figures') or [])
    nyb = [c for c in cf if c['verdict'] == 'REFUSE' and 'NOT-YET-BUILT' in str(c['reason'])]
    other = [c for c in cf if c['verdict'] == 'REFUSE' and 'NOT-YET-BUILT' not in str(c['reason'])]
    prov = [c for c in cf if c['verdict'] == 'PROVISIONAL']
    print(k, 'checks', len(cf), 'PASS', sum(1 for c in cf if c['verdict'] == 'PASS'), 'REFUSE_NOT_YET_BUILT', len(nyb), 'REFUSE_OTHER', len(other), 'PROVISIONAL', len(prov))
    [print('  OTHER', c['figure_id'], c['reason']) for c in other]
"</invocation><expect>UNITS AT INSTANTIATION, ON THE THREE VALIDATION NAMES: each block's check face (the SAME check_block the Lambda runs) reads REFUSE_NOT_YET_BUILT 0 with checks greater than 0 -- the map entries for a NEW security were built by rk-34's builder inside this order's derive, with no hand step -- and every REFUSE_OTHER line is an UNRESOLVED-ON-<security> unit with its reason (listed) or a PROVISIONAL currency caveat, never an inferred unit. Any NOT-YET-BUILT refusal on a validation name is NOT met: it means the block was derived without the builder, which is the hand-step defect this cell retires</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-35"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
pre = json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/pre_act_stamps.json', encoding='utf-8'))
cw = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='crosswalk/v1/') for o in pp.get('Contents', []))
recs = json.loads(s3.get_object(Bucket=B, Key=cw[-1])['Body'].read()).get('records') or []
names = sorted(r['security_key'] for r in recs if r.get('security_key'))
moved = []
for n in names:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + n + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    now = ks[-1] if ks else None
    if now != pre.get(n): moved.append((n, pre.get(n), now))
raw_moved = []
for n in names:
    rk = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='raw/bloomberg/' + n + '/') for o in pp.get('Contents', []))
    if rk and rk[-1] > pre.get('_raw_newest', {}).get(n, ''): raw_moved.append((n, rk[-1]))
print('crosswalk', cw[-1], 'keyed_names', len(names), 'pre_act_recorded', len([n for n in names if n in pre]))
print('served_stamps_moved', len(moved), moved)
print('raw_landings_newer_than_pre', len(raw_moved), raw_moved)
"</invocation><expect>ISSUER REPAIR (2.0.0_SA_COO~Z, 2026-09-19 ~11:0xZ, row AMGT_RESAPP-Z-W39-S1): the negative control's population is the COVERED names -- the crosswalk-keyed names MINUS the three validation names this order is authorized to pull (CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity), because AMGT-rk-31 landed those three into the crosswalk (33 -> 36) before this order's live act, an ordering the chain M COO half signed. Print BOTH: the whole-crosswalk sweep as cut (36 swept, served_stamps_moved listing exactly the three validation keys and nothing else) AND the covered-name figure 'covered_names_moved 0 of 33'. PASS when the moved set equals exactly the validation set and the covered figure is 0 of 33; any other name moved is FAIL as cut. The original bar follows for the record: THE NEGATIVE CONTROL -- NO FLEET RUN, NO RE-RUN: over the crosswalk's keyed names read fresh (33 at the cut), pre_act_recorded 33 (the stamp list you wrote at spawn, AFTER rk-34's re-derive drained, so rk-34's stamps are the baseline), served_stamps_moved 0 and raw_landings_newer_than_pre 0 -- this order pulled and derived nothing for any covered name. pre_act_stamps.json carries, per name, the newest derived stamp and (under _raw_newest) the newest raw key at spawn. Any moved stamp or new raw landing on a covered name is NOT met and is a violation of C-VALIDATION-NAMES, reported as such</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1 runs BEFORE the live pull; AC2-AC4 after the derive has landed.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/AMGT_RESAPP.TO-AMGT-rk-35.rolling-history-window.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); the change-management entry
CLOSED with all three legs proven and its sentinel removal committed; flip `<status>` to `complete`; commit with
`--only -- <paths>`. **Do not stop here** -- `AMGT-rk-36` (forecasts FY1-FY3) is handed to you next as a
continuation in the SAME worktree; wait for it. Report once, naming: the six Bloomberg requests (security, type,
end_date), the three landed key sets, each block's `latest_closed_fiscal_year`, the rows filed.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~39</slot>
<fabric>site-z</fabric>
