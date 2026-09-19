# AMGT_RESAPP task order -- `AMGT-rk-34` -- the unit map built for EVERY name from the raw bytes already landed; the 348 refusals cleared on the served figures

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-34</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~38</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written. The model-block
  refresh cadence stays Andrew's (C-MODEL-WINDOW-AND-ROWS (3)); nothing here schedules it.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to an already-provisioned prefix this producer already
  writes (`derived/model_block/<key>/<stamp>/` in `opal-data-harvest`, the pool bucket) under the credentials the
  producer already runs with on this box; it grants no permission, provisions no resource, deploys no Lambda and
  touches no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~38`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --short=10 HEAD`, and tests that
`org/`, `.tools/` and every path in section 3 exists; if any is absent, STOP with a BLOCKING row. Your SECOND act is
the dependency read in section 1.2 (`AMGT-rk-33` must have landed before this order does anything else). Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~38;`. **NEVER RUN AN INSTALL.** **Bloomberg, ANY
scenario: READ `integrations/bloomberg/READ_HERE.md` FIRST** -- although THIS order makes NO Bloomberg call at all
(section 4), the raw bytes it reads are Bloomberg's and the reading rules there bind their interpretation.

## 1. THE CELL, inlined in full -- `AMGT-rk-34` (R14-M1; FWD-10; Model brief M1)

**The analysis row, verbatim** (`ledger/ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`, chain M, `R14-M1`): *"the unit
map built for EVERY name; re-derive from the raw bytes already landed (no new pull). Clears the 348 refusals"* --
serves FWD-10, M1; co-sign **yes (served figures change)**.

**The root cause this cell retires** (analysis s.2 @`9c8e04cd9a`, lines 55-61; PRD v0.13 @`1699960261`
`C-UNIT-MAP-MEASURED` :854-859): the producer `integrations/bloomberg/research/model_block_pull.py` takes each figure's
unit from a map that lives in a WORKER'S deliverables folder -- `_FIELD_MAP_PATH` (`:286-288` @HEAD) =
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`. That map (32 fields) carries
per-security units for exactly the three pilot names (`SAP GY Equity`, `BA US Equity`, `BABA US Equity`,
`field_map.json:2-6`); for every other name `_resolved_unit` (`:302-318`) returns the pointer text
`"SEE field_map.json (per-field, per-security MEASURED unit -- not yet built)"` (`:318`), and the check face
`lib/research/checkface/run_checks.py:54-55` maps any unit text carrying `"not yet built"` or `"SEE field_map.json"`
to `NOT-YET-BUILT`, which the figure rule REFUSES (`lib/research/rules/figure.py:104-105`: reason
`"<field>: unit/sign convention is 'NOT-YET-BUILT', not MEASURED"`). **Measured 2026-09-18 by `4.0.0_SA_CRO~Z`
(Model brief s.1.1 @`f48864fce6`): PASS 5,926 / REFUSE 348 / PROVISIONAL 103 over 33 names; the 348 are
`IS_DIV_PER_SHR` 297, `EQY_FREE_FLOAT_PCT` 29, `SHORT_INT_RATIO` 12, `SI_PERCENT_EQUITY_FLOAT` 10 -- every one a
missing map entry, not bad data.** RE-MEASURE THIS AT SPAWN (AC1 before the act); it may have moved.

**The PRD constraints this cell serves** (PRD v0.13 @`1699960261`):
- `C-UNIT-MAP-MEASURED` (`:848-859`): *"Every mapped field carries a MEASURED unit and sign, never an inferred one,
  and the measurement is per field."* v0.11 amendment: *"The map is built for EVERY name at instantiation, not the
  three pilots. Its home is version control beside the producer that reads it (`C-PRODUCTION-HOME`) ... Building the
  map needs NO new pull: the `derive` stage re-reads the raw block from the pool. A field whose unit is not measured
  stays REFUSED; it is never inferred to clear a refusal."*
- `C-PRODUCTION-HOME` (`:1643-1650`): *"Configuration (for example the unit map) lives under version control beside
  the producer that reads it ... A dry run writes nothing, anywhere."*
- `C-VALIDATION-NAMES` (`:1652-1658`): proven on Caterpillar / CSL / Keyence or on a dry run; no fleet run, no
  re-run of the covered population. **What "no re-run" means HERE:** the act of this cell is a LOCAL `derive` over
  raw bytes ALREADY LANDED (`stage_derive`, `model_block_pull.py:369-461`, reads
  `raw/bloomberg/<key>/<stamp>/{refdata,histdata}.json` back from S3, `:374-376`) -- ZERO vendor calls, and the
  analysis row itself names it ("re-derive from the raw bytes already landed (no new pull)"). A derive is not a
  pull and is not the fleet run Andrew's word forbids. If ANY step you take would issue a Bloomberg request, STOP.
- `C-BLOOMBERG-BASIS` (`:891-895`): adopt Bloomberg's definitions, state the basis beside the number.

**RULED -- what you build:**

1. **`AMGT-rk-33` (chain H) MOVES the map's HOME** to a config file beside the producer under version control. **This
   order does NOT choose that home; it DISCOVERS it** (section 1.2) and builds INTO it. The map's schema is rk-33's
   as landed; you EXTEND it per security, you do not redesign it.
2. **A production builder beside the producer**, `integrations/bloomberg/research/build_unit_map.py`, generalising
   the estate's existing art `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/build_field_map.py`
   (its method: F4's magnitude-vs-known-scale classification per family, `classify_unit` `:135-186`,
   `classify_sign` `:189-207`, the CAPITAL_EXPEND/NET_DEBT sign conventions `:49-58`, the self-consistent PE
   cross-check `detect_reporting_currency_mismatch` `:233-309`). That file STAYS where it is as `~1`'s proof artifact
   and is never imported by production; the new module carries the method. Differences that are NOT optional:
   - the bucket is the PRODUCER'S (`model_block_pull.py:44`, `HARVEST_BUCKET` default `opal-data-harvest`, the
     same bucket `lib/research/coverage/pool_reader.py:72` reads) -- the old builder hard-codes `opal-data-research`
     (`build_field_map.py:29`), which is NOT where the served blocks live; a builder reading the wrong bucket
     measures nothing and reports UNRESOLVED for every name;
   - the population is never a constant list (`build_field_map.py:30`): `--securities <'X US Equity' ...>` for named
     runs, or `--population crosswalk` = the crosswalk's MEASURED records read from the pool at run time (the
     newest `crosswalk/v1/<date>.json`, records carrying `security_key`; MEASURED = 33 at the cut, RE-READ, never
     typed). The security STRING the map is keyed by is the raw object's own top-level key (the
     `<ticker> Equity` form `stage_pull` requested, `:223`, `:242-245`) -- "reads the block's own security string",
     `C-MODEL-WINDOW-AND-ROWS` (4);
   - every entry records `raw_stamp` (the landing it was derived from), `derived_by` (this module's path), and
     `unit_status` / `sign_status` = `MEASURED` or `UNRESOLVED-ON-<security>: <why the magnitude did not
     discriminate>` (a zero dividend, an absent value, an out-of-band magnitude). **An unmeasured unit is written as
     UNRESOLVED with its reason, never guessed, and the figure stays REFUSED** (C-UNIT-MAP-MEASURED);
   - additive merge: a run never overwrites an existing `MEASURED` entry for a security unless `--remeasure` is
     passed; a run for a security with NO raw landed under `raw/bloomberg/<key>/` prints
     `UNRESOLVED: no raw landed under raw/bloomberg/<key>/` and writes nothing for it -- an explicit terminal state,
     never a silent skip (PRD section 10, the battery's shape);
   - `--dry-run` prints exactly what a real run would write (entries per security, statuses) and writes NOTHING --
     no file, no S3 object, no log.
3. **The producer's reader** (`_field_map` `:292-299`, `_resolved_unit` `:302-318`, `_resolved_sign` `:321-336`,
   `_currency_caveat` `:352-366`) reads the new home and honours per-security entries as it does today. **Two placeholder
   texts are CONTRACT STRINGS, not filenames, and MUST keep their literals:** (a) a security with NO entry keeps the
   existing pointer text unchanged in its two load-bearing fragments `SEE field_map.json` and `not yet built`; (b) a
   security whose entry is present but `UNRESOLVED` returns
   `"UNRESOLVED-ON-<security>: <reason> -- SEE field_map.json: a MEASURED unit is not yet built for this security"`.
   WHY: three consumers key on those literals and NONE is on this order's surface -- the check face
   (`run_checks.py:54`, refuses), the provenance validator (`lib/research/provenance/validate.py:23`,
   `UNRESOLVED_UNIT_PREFIX = "SEE field_map.json"`) and the print renderer (`lib/research/provenance/render_print.py:83`,
   the same prefix). Keeping the literal means this order changes NO Lambda-packaged file and needs NO redeploy: the
   served figures move through the POOL alone (the adapter reads the newest stamp per key at request time,
   `lib/research/api/scoped_amgt.py:980-1051`, `candidates[-1]` at `:1017`). Put a comment beside the literal naming
   the three consumers by path so the next editor does not "tidy" it.
4. **The act: re-derive the 33 keyed names from their landed raw** (`python integrations/bloomberg/research/model_block_pull.py derive --securities ...`,
   in batches of at most three -- the `main()` cap at `:509-510` is F2/G-24's PULL budget and you do NOT lift it; eleven
   invocations of three is the honest cost). Each derive mints a NEW stamp (`:452-454`, `s3_put_if_absent`, STORE_CONTRACT
   rule 1) and the adapter serves the newest, so the served figures for all 33 change the moment the derive lands. **That
   is why this order is co-signed and opens a change-management entry BEFORE the first derive write** (section 4).
5. **Validation names FIRST, on a dry run.** CAT / CSL / Keyence have NO raw landed in the pool at the cut (the validation
   ran every stage SERVED-LOCAL, report @`b527b93214` s.2 row "Bloomberg model block", *"output exists in scratch only"*).
   Your `--dry-run` over `"CAT US Equity" "CSL AU Equity" "6861 JP Equity"` must print the explicit UNRESOLVED terminal
   state for each name whose raw is absent, and `WOULD-WRITE` for any whose raw HAS landed (chain M's `AMGT-rk-35` may
   land them while you run) -- and write nothing either way (AC4). The unit map for those three is then built by
   `AMGT-rk-35` THROUGH YOUR BUILDER at its derive (that is the "built for EVERY name at instantiation" half); you build
   the module and the 33, rk-35 exercises it on the new names.

### 1.2 DEPENDENCY: `AMGT-rk-33` (chain H, `C-PRODUCTION-HOME`) -- the DISCOVERY RULE, run before anything else

You cannot see rk-33's order. **The rule:** the unit map's home is *the path `model_block_pull.py` reads at the HEAD
of your worktree*. Print it:
`python -c "import importlib.util as u,pathlib as p; s=u.spec_from_file_location('m','integrations/bloomberg/research/model_block_pull.py'); m=u.module_from_spec(s); s.loader.exec_module(m); print('FIELD_MAP_HOME', m._FIELD_MAP_PATH, 'exists', p.Path(str(m._FIELD_MAP_PATH)).exists())"`
- If the printed path still lies under `org/missions/` (any `deliverables/` folder), **rk-33 has NOT landed: STOP,
  file a row `AMGT_RESAPP-Z-W38-S<k>` (`spec_asserts`: C-PRODUCTION-HOME moved the map beside the producer;
  `world_is`: the producer at <hash> still reads <path>), and do nothing else** -- building into the worker folder
  would be the defect this cell exists to retire.
- If the constant has been RENAMED by rk-33, read the file (`comp-read integrations/bloomberg/research/model_block_pull.py --for "where is the unit map read from"`)
  and apply the same test to whatever `_field_map()` opens. The test is on the PATH OPENED, not on a variable name.
- Record the discovered home, the rk-33 commit hash that landed it (`git log -1 --format=%h -- <home>`), and the
  map's landed schema (top-level keys) in your report. Every later act names that path.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c (round-14 postulate records), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 chain M
row `R14-M1` and s.2 (the worker-folder root cause) @`9c8e04cd9a`; Model brief `BRIEF_MODEL_CURRENT_TO_DESIRED_20260918.md`
@`f48864fce6` s.1.1 and s.5 item 1; intake `CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` row M1 and "The pattern
V2, V7 and M1 share". PRD **v0.13 @`1699960261`** (`C-UNIT-MAP-MEASURED` as amended at v0.11; `C-PRODUCTION-HOME` and
`C-VALIDATION-NAMES` new at v0.11; nothing in v0.12 or v0.13 moved this cell's constraints). Code cited @HEAD (draft-time HEAD
`ced1f5f84d`; the cited files carry no working-tree change) -- re-read every line you rely on at spawn.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain M is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-34`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-34` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~38/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-34.unit-map-every-name.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (you read the pool, `run_checks.py`,
  `scoped_amgt.py`, `build_field_map.py` in `~1`'s folder, the crosswalk); this block governs WRITES. The unit map's
  discovered home MUST resolve under `integrations/bloomberg/research/` (that is what "beside the producer" means);
  if rk-33 put it elsewhere, that is a row and a STOP, not a grant you infer. Scratch is `<your worktree>/.scratch/`
  only. **You never write under `lib/`** (nothing Lambda-packaged moves; section 1 item 3 is the mechanism).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~38 <0.9.0_WK_AMGT_RESAPP~38@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **THE POOL WRITE IS A DEPLOY OF SERVED OUTPUT.** Before the first `derive` write: (i) the writer census is PRINTED
  and recorded -- the ONE writer of `derived/model_block/` is `model_block_pull.py:453-454` (`derive_fye_fixed.py:119`
  writes the SEPARATE `derived/model_block_fye/` store, `scoped_amgt.py:133-136`); its readers are
  `scoped_amgt.py:172/:995`, `lib/research/scores/run_scores.py:70`, `lib/research/peers/universe.py:79`,
  `lib/research/print/render_pack.py:22` -- re-census at spawn with a python walk over `lib/` and `integrations/`
  for the literals `derived/model_block` and `derived/{ENGINE}`, denominator printed; (ii) the per-key PRE-ACT newest
  stamp for all 33 is recorded to your deliverables folder (`pre_act_stamps.json`) -- that list IS the rollback
  target; (iii) the change-management entry is OPENED:
  `python .tools/deploy_ledger.py open --slug amgt-rk34-unit-map-rederive-20260918 --title "AMGT-rk-34: unit map built for every name; 33 keyed blocks re-derived from landed raw (no pull); co-signed rk-34 pair" --author 0.9.0_WK_AMGT_RESAPP~38 --leg "L1|git|build_unit_map.py + map entries for 33 names committed|commit hash" --leg "L2|activation|derived/model_block/<key>/<new stamp>/ for 33 keys (pool write, no Lambda)|per-key new stamp list + pre/post NOT-YET-BUILT counts" --leg "L3|verify|served-plane read on 3 covered names + pool-plane census over 33|AC1 and AC3 output" --window-hours 4`
  and its sentinel COMMITTED, not staged. CLOSE it (every leg proven) before your grading read. **ROLLBACK, named in
  the pair and executable by you:** re-derive the affected keys with the PRE-ACT map bytes (`git show <pre-act
  hash>:<home>` into `.scratch/`, pointed at by the env/flag your builder exposes for exactly this) -- a NEWER stamp
  carrying the old units, which the adapter serves next; NO S3 delete (an S3 delete needs human confirmation and is
  never your act). The pair's CTO half and COO half each name this blast radius (33 keys, one writer, four readers)
  and this rollback; a pair that does not is not the pair this order requires.

## 4. BOUNDS

**NO BLOOMBERG CALL. NO VENDOR CALL OF ANY KIND.** This order's only inputs are bytes already in the pool and files in
the repo. A `pull` invocation is a violation, not a shortcut. **No fleet run, no re-run of the 33**: the derive over the
33 is a LOCAL re-derivation the analysis row names; if that sentence and Andrew's word ever seem to conflict to you,
STOP and file a row -- do not resolve it yourself. **PORTAL FROZEN** (not your surface). **COLLECTION STAYS OFF.** **NO
alarm, monitor, SNS/SES-send, notification or freshness checker.** No Lambda deploy, no Terraform, no IAM. No
non-ASCII in anything you write (the map is production config: ASCII only, `OK:`/`WARN:`/`ERROR:` tokens). **PUSH:
never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. In particular: **a refusal that survives because a
magnitude genuinely does not discriminate (a zero dividend every year) is NOT cleared by inference** -- it is listed
under AC1's `REFUSE_OTHER` with its `UNRESOLVED-ON-<security>` reason, and the bar "0 NOT-YET-BUILT" is still met
because the entry now EXISTS and says why.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- AC1 runs BEFORE the act (the 348)
and AFTER (the 0); record both outputs byte-for-byte.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W38-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** Two you are
likely to meet: `cmd_pull` writes `pull_log.json` into `~1`'s folder (`model_block_pull.py:464-467`, a
C-PRODUCTION-HOME instance the PRD's list does not name -- rk-35's to fix, your row if rk-35 has not); and
`build_field_map.py:29`'s wrong bucket (record it; do not edit `~1`'s folder).

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-34"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, sys
sys.path.insert(0, '.')
from lib.research.checkface.run_checks import check_block
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
cw = sorted(o['Key'] for p in pg.paginate(Bucket=B, Prefix='crosswalk/v1/') for o in p.get('Contents', []))
recs = json.loads(s3.get_object(Bucket=B, Key=cw[-1])['Body'].read()).get('records') or []
names = sorted(r['security_key'] for r in recs if r.get('security_key'))
print('crosswalk', cw[-1], 'keyed_names', len(names))
blocks = 0; tot = 0; nyb = 0; other = []; per_field = {}; stamps = {}
for n in names:
    ks = sorted(o['Key'] for p in pg.paginate(Bucket=B, Prefix='derived/model_block/' + n + '/') for o in p.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    if not ks:
        print('NO_BLOCK', n); continue
    blocks += 1; stamps[n] = ks[-1]
    blk = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read())
    for c in check_block(blk.get('figures', [])):
        tot += 1
        if c['verdict'] == 'REFUSE':
            if 'NOT-YET-BUILT' in str(c['reason']):
                nyb += 1; m = c['figure_id'].split(':')[1]; per_field[m] = per_field.get(m, 0) + 1
            else:
                other.append((n, c['figure_id'], c['reason']))
print('names_with_block', blocks, 'of', len(names), 'figures_checked', tot)
print('REFUSE_NOT_YET_BUILT', nyb, 'per_field', per_field)
print('REFUSE_OTHER', len(other)); [print('  OTHER', o) for o in other]
print('newest_stamps', json.dumps(stamps, sort_keys=True))
"</invocation><expect>THE POOL-PLANE CENSUS, run TWICE and both outputs recorded: BEFORE the act it re-measures the cut's figure (issuer's read from the Model brief: keyed_names 33, names_with_block 33 of 33, REFUSE_NOT_YET_BUILT 348 with per_field IS_DIV_PER_SHR 297 / EQY_FREE_FLOAT_PCT 29 / SHORT_INT_RATIO 12 / SI_PERCENT_EQUITY_FLOAT 10 -- print whatever is actually live, it may have moved); AFTER the act, over the SAME 33 names read fresh from the crosswalk, REFUSE_NOT_YET_BUILT reads 0 and names_with_block reads 33 of 33, every newest_stamps value is NEWER than the pre-act list recorded in pre_act_stamps.json, and every REFUSE_OTHER line carries a reason other than NOT-YET-BUILT (an UNRESOLVED-ON-<security> unit written by the builder with its cause, or a PENDING currency caveat) -- listed, never hidden. A post-act count with any NOT-YET-BUILT remaining, or fewer than 33 blocks, is NOT met. The check is the SAME function the Lambda runs (scoped_amgt.py:1965-1967 calls run_checks.check_block) over the SAME newest block it serves (scoped_amgt.py:1013-1017), so this is the served figure set on a different instrument, not a self-report ISSUER REPAIR (2.0.0_SA_COO~Z, on rows W38-S2/S4; the classification collision the CTO's chain M half names as M-DISAGREE-1(a)): the builder must SPLIT the classification -- a (security, mnemonic) pair whose map entry EXISTS but whose landed raw carries NO value is written as `UNRESOLVED-ON-<security>: <cause>` (its own REFUSE bucket, listed under REFUSE_OTHER with the cause), and NOT-YET-BUILT is reserved for a pair with NO map entry. With that split, REFUSE_NOT_YET_BUILT reads 0 over the keyed names WITH landed raw; the keyed names without any landed raw (the 3 validation names rk-31 registered -- 36 keyed at spawn, 33 with raw) are printed as `no_raw <n>` and EXCLUDED from names_with_block's denominator (33 of 33). A second derive over the 33 is the same co-signed act shape (a NEW stamp per key; pre-act stamps re-read fresh; a NEW change-management entry).</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-34"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import importlib.util as u, json, pathlib as p, boto3, sys
sys.path.insert(0, '.')
from lib.research.checkface.run_checks import unit_status_for
s = u.spec_from_file_location('m', 'integrations/bloomberg/research/model_block_pull.py'); m = u.module_from_spec(s); s.loader.exec_module(m)
home = p.Path(str(m._FIELD_MAP_PATH)); print('FIELD_MAP_HOME', home, 'under_org_missions', str(home).replace(chr(92), '/').startswith('org/missions/'))
doc = json.loads(home.read_text(encoding='utf-8'))
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
cw = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='crosswalk/v1/') for o in pp.get('Contents', []))
recs = json.loads(s3.get_object(Bucket=B, Key=cw[-1])['Body'].read()).get('records') or []
keyed = sorted(r['security_key'] for r in recs if r.get('security_key'))
mnems = sorted(set(m.HEADER_FIELDS) | set(m.HIST_FIELDS)); print('producer_mnemonics', len(mnems))
fields = {f.get('mnemonic'): f for f in doc.get('fields', [])}
covered = []; missing = []; unresolved = []
for k in keyed:
    sec = k.replace('_', ' ')
    ok = True
    for mn in mnems:
        f = fields.get(mn)
        u_ = (f or {}).get('unit'); det = (f or {}).get('per_security_detail') or {}
        has = (sec in det) or (isinstance(u_, dict) and sec in u_)
        if f is None or not has:
            ok = False; missing.append((k, mn))
        elif isinstance(u_, dict) and (u_.get(sec) is None or str(u_.get(sec)).startswith('UNRESOLVED')):
            unresolved.append((k, mn, u_.get(sec)))
    covered.append(k) if ok else None
print('securities_with_entry_for_every_mnemonic', len(covered), 'of', len(keyed))
print('missing_pairs', len(missing), missing[:15])
print('unresolved_pairs', len(unresolved)); [print('  UNRESOLVED', x) for x in unresolved]
print('entries_carry_raw_stamp', all('raw_stamp' in str(f) for f in doc.get('fields', [])), 'entries_carry_derived_by', 'derived_by' in json.dumps(doc))
print('PLANTED_NO_ENTRY unit_text', m._resolved_unit('IS_DIV_PER_SHR', 'HOLLOW_NONEXISTENT US Equity'))
print('PLANTED_NO_ENTRY status', unit_status_for({'unit': m._resolved_unit('IS_DIV_PER_SHR', 'HOLLOW_NONEXISTENT US Equity'), 'sign': 'POSITIVE'}))
"</invocation><expect>THE MAP'S HOME AND COVERAGE: FIELD_MAP_HOME is a path under integrations/bloomberg/research/ with under_org_missions False (rk-33's home, discovered per section 1.2, never typed); producer_mnemonics PRINTED (32 distinct at the cut: HEADER_FIELDS 15 + HIST_FIELDS 19 minus the two shared, PX_LAST and EQY_DVD_YLD_IND -- re-count, do not cite); securities_with_entry_for_every_mnemonic reads 33 of 33 with missing_pairs 0 -- every (security, mnemonic) pair the producer can emit has a PER-SECURITY entry (the security appears in that field's per_security_detail, the landed schema's own per-name record, or in a per-security unit dict; a string unit measured on the three pilots does NOT count for a 34th name -- adapt the two field names to rk-33's landed schema if it renamed them, and say so); unresolved_pairs lists every entry the builder wrote as UNRESOLVED-ON-<security> WITH its reason (a legitimate, honest residue, and each one corresponds to an AC1 REFUSE_OTHER line); every entry carries raw_stamp and derived_by (True, True). THE PLANTED NEGATIVE: a security with NO entry (HOLLOW_NONEXISTENT US Equity) still returns the pointer text carrying the literals SEE field_map.json and not yet built, and unit_status_for maps it to NOT-YET-BUILT -- the refusal path for an unbuilt name is intact and the three consumers named in section 1 item 3 lose nothing. A HOME under org/missions/, a missing pair, or a planted status other than NOT-YET-BUILT is NOT met ISSUER REPAIR (2.0.0_SA_COO~Z, on row W38-S4): the denominator is the keyed names WITH landed raw (33 at spawn), printed beside `no_raw <n>` for the keyed names without any raw stamp (the 3 validation names rk-31 registered); securities_with_entry_for_every_mnemonic reads 33 of 33 and missing_pairs 0 over THAT set -- a raw-less name cannot carry per-security entries and is not owed any until rk-35 lands its raw.</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-34"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
for key in ['BA_US_Equity', 'HD_US_Equity', 'BP%2F_LN_Equity']:
    payload = json.dumps({'rawPath': '/api/scoped/amgt/security/' + key + '/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
    body = json.loads(resp['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    cf = inner.get('check_face') or []
    nyb = [c for c in cf if c.get('verdict') == 'REFUSE' and 'NOT-YET-BUILT' in str(c.get('reason'))]
    other = [c for c in cf if c.get('verdict') == 'REFUSE' and 'NOT-YET-BUILT' not in str(c.get('reason'))]
    print(key, 'statusCode', body.get('statusCode'), 'model_status', (inner.get('model_status') or (inner.get('model') or {}).get('model_status')), 'checks', len(cf), 'REFUSE_NOT_YET_BUILT', len(nyb), 'REFUSE_OTHER', len(other), 'unit_of_IS_DIV_PER_SHR_FY2024', [f.get('unit') for f in inner.get('fiscal_year_figures') or [] if f.get('mnemonic') == 'IS_DIV_PER_SHR' and str(f.get('fiscal_year')) == '2024'])
"</invocation><expect>THE SERVED PLANE, after the act, on three COVERED names read through the deployed adapter (never a local import): each of BA_US_Equity, HD_US_Equity and the slash-keyed BP%2F_LN_Equity (sent in the page's own %2F shape, rk-23's lesson) answers statusCode 200 with model_status SERVED, checks greater than 0, REFUSE_NOT_YET_BUILT 0, and the served IS_DIV_PER_SHR FY2024 unit is a MEASURED per-share text (or an UNRESOLVED-ON text WITH a reason, never the bare not-yet-built pointer). REFUSE_OTHER is printed, not required to be 0. The Lambda was NOT redeployed by this order (its CodeSha256 before and after the act is the same value -- record aws lambda get-function-configuration --function-name opal-amgt-scoped-api --query CodeSha256 in your report); the served figures moved through the pool alone, which is the whole mechanism of section 1 item 3. A statusCode other than 200 on the slash key is a row against R14-T7, not a repair here ISSUER REPAIR (2.0.0_SA_COO~Z, on rows W38-S2/S3): model_status is read from the payload's top level (with the nested `model` block as the fallback -- the invocation is corrected); REFUSE_NOT_YET_BUILT 0 holds under the classification split AC1 names (an UNRESOLVED-ON unit with its cause is REFUSE_OTHER, printed, never NOT-YET-BUILT); the CodeSha256 equality before/after stands.</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-34"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import subprocess, boto3, importlib.util as u, pathlib as p
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
keys = ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']
def count(prefix): return sum(1 for pp in pg.paginate(Bucket=B, Prefix=prefix) for _ in pp.get('Contents', []))
before = {k: (count('raw/bloomberg/' + k + '/'), count('derived/model_block/' + k + '/')) for k in keys}
s = u.spec_from_file_location('m', 'integrations/bloomberg/research/model_block_pull.py'); m = u.module_from_spec(s); s.loader.exec_module(m)
home = str(m._FIELD_MAP_PATH); pre = p.Path(home).read_bytes()
r = subprocess.run(['python', 'integrations/bloomberg/research/build_unit_map.py', '--dry-run', '--securities', 'CAT US Equity', 'CSL AU Equity', '6861 JP Equity'], capture_output=True, text=True, timeout=100)
print('rc', r.returncode); print(r.stdout[-3000:]); print('STDERR', r.stderr[-800:])
after = {k: (count('raw/bloomberg/' + k + '/'), count('derived/model_block/' + k + '/')) for k in keys}
print('s3_counts_before', before); print('s3_counts_after', after); print('s3_unchanged', before == after)
print('map_bytes_unchanged', p.Path(home).read_bytes() == pre)
st = subprocess.run(['git', 'status', '--porcelain', '--', 'integrations/bloomberg/research/', 'org/missions/'], capture_output=True, text=True).stdout
print('porcelain_lines_after_dry_run', st.count(chr(10)), repr(st[:400]))
"</invocation><expect>THE VALIDATION NAMES, ON A DRY RUN THAT WRITES NOTHING: rc 0; for each of CAT US Equity, CSL AU Equity and 6861 JP Equity the builder prints ONE explicit terminal state -- UNRESOLVED: no raw landed under raw/bloomberg/<key>/ (the state at the cut, validation @b527b93214 s.2: the three blocks exist in scratch only) OR WOULD-WRITE <n> entries (if AMGT-rk-35 has landed their raw meanwhile), never a silent skip; s3_unchanged True; map_bytes_unchanged True; and porcelain_lines_after_dry_run equals the count you recorded IMMEDIATELY BEFORE this invocation (record that pre-count in your evidence -- the comparison is before-vs-after THIS run, not against zero, because your own uncommitted work may be present). A dry run that changes a byte anywhere, or a name with no printed terminal state, is NOT met (C-PRODUCTION-HOME: a dry run writes nothing, anywhere)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1 is recorded TWICE (pre-act and post-act); AC3 runs only AFTER the derive has landed and the change-management
entry's L2 leg carries the per-key stamp list.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~38/AMGT_RESAPP.TO-AMGT-rk-34.unit-map-every-name.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); the change-management entry
CLOSED with all three legs proven and its sentinel removal committed; flip `<status>` to `complete`; commit with
`--only -- <paths>`. Report once, naming: the discovered map home and rk-33's hash; the pre-act and post-act AC1
figures; the per-key stamp list's location; the Lambda CodeSha256 read before and after (unchanged); every row filed.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>14</round>
<slot>~38</slot>
<fabric>site-z</fabric>
