# Never-widen half, MDPF_SECCLASS item 4 -- E_18's scheduled trigger: the Black Diamond gold dispatcher at CLOUD, with the calendar guard switched off

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 08:2xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO` to sign the second half.
**Authority:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` batch 68 @85931f56b7,
`SECCLASS-E18-TRIGGER-DISPATCHER-20261001` items 1-4; row `MDPF_SECCLASS-W10-S2` (E_18 has no trigger). **Status of the
act: NOT RUN.** One read-only exercise ran before signing (below); nothing is deployed.

## The act: ONE key

| | value |
|---|---|
| key | `s3://opal-data-bd/code/gold/gold_dispatch.sh` |
| live now | VersionId `Ar2kBAqtNnkXz7BDSvRYOS7daMqTgYyM`, ETag `6e6483449644bc600a7b9153c3e8fd37`, 66,915 bytes, 2026-07-17T18:12:19Z; equals repo commit `606263dd22` (blob `76256eca8f`, md5 read with `git show`) |
| candidate | commit `6f4bde6b6a`, blob `631d6e6f4a`, md5 `d6ab79987610f5144ad393bcacb5b171`, 74,731 bytes, 0 CR bytes |
| how | `aws s3api put-object` of the `git show 6f4bde6b6a:` bytes; the returned ETag must read `d6ab7998...b171` or the step stops. The deploy hook never carries a `.sh` (`safe_deploy_core.py` returns early on a path not ending `.py`); the precedent is a hand `s3 cp` (`change_management/20260624T2035Z_bd-A01-advisor-assignments-incremental-flip_deploy.md` step 3). `deploy-to-ec2.sh` is NOT used: it syncs the whole prefix |
| rollback | `copy-object` from VersionId `Ar2kBAqt...` onto the same key (a new version; no delete), ETag read back as `6e648344...fd37`. It takes effect at the next boot, like the deploy |

**Writers of this key: 2, both by hand, none scheduled** -- a single-file `s3 cp` and `deploy-to-ec2.sh`'s prefix sync.
**Readers: 2** -- the runner's boot sync (`infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh:90`, then
`run_gold_layer.sh` calls `gold_dispatch.sh --chain full`) and the dispatcher's own `sync_scripts` (`aws s3 sync
code/gold/` into `/tmp/gold_layer_scripts/`, where the running copy lives). No other key is written. E_18's own bytes are
already live and unchanged (ETag `a7820a20...bff6`, deployed 06:12Z under BD_THREAD_R3).

## What the candidate changes against the live bytes (135 lines added, 7 removed)

1. **Not mine, already on CLOUD since 2026-08-29: the calendar guard** (`0.7.0_AE_CloudOps`, held build-only).
   The three hunks between `606263dd22` and CLOUD before this commit are all the guard: the sentinel comment, the function
   `_expected_last_trading_day`, and its call in `check_freshness`. **It ships SWITCHED OFF** (ruling item 1):
   `check_freshness` calls it only when `GOLD_CALGUARD_ENABLE` is `1`; unset is the default and nothing sets it: in the
   repo the name occurs in this one file (5 occurrences, 1 file, outside `org/`), and on the runner a search of
   `/etc/environment`, `/etc/systemd`, `/etc/profile*`, `/root` and `/opt` plus the gold units' `Environment` read 0 hits
   (SSM, 08:23Z).
2. **Mine: E_18's slot.** One catalog line (`E_18|E_18.detect_new_securities.py|--upload`); `CHAIN_CANONICAL` runs it
   between B_01b and B_02; the parallel dispatcher (the path every scheduled fire takes) gains `PHASE_B3b: E_18`, alone,
   between PHASE_B3 and PHASE_B4. Every other phase is unchanged.
3. **Mine: E_18 is NON-FATAL** (`NONFATAL_IDS="E_18"`). `run_script` prints `E_18 done (rc=N)`, then on a non-zero code
   `WARN: E_18 exited N -- NON-FATAL step, the chain continues.` and returns 0. Reason: a failed detection step must not
   stop B_02 onward, which is every served Black Diamond artifact. No checkpoint is written on failure.
4. **Mine: `--dry-run` drops E_18's `--upload`** (the script has no `--dry-run` argument; no flag is its dry run).

## Log lines that differ from the live bytes, switch off

- **The freshness gate: none.** Test section 2 runs both versions of `check_freshness` side by side over four cases
  (silver newer; silver equal; no silver listing; no gold header): output byte-identical and the same return code, with the
  calendar module absent AND present. No `CALGUARD` line and no "Silver effective" line print with the switch unset.
- **A proceeding chain gains** `--- PHASE_B3b: E_18 ---`, `STARTED E_18 (pid N)`, E_18's banner, two telemetry lines,
  E_18's own output (its detection summary), `CHECKPOINT E_18 -> gold/.checkpoints/<run_date>/E_18.done`,
  `E_18 done (rc=N)`, `[PHASE] PHASE_B3b complete (Ns)`; `perf_report.json: N script(s) merged` reads one higher.
- **`--help`** lists E_18 in the full chain.

**Additive keys each proceeding run now writes** (logs and markers; none is read by a page): the checkpoint marker above,
`logs/gold-layer/telemetry/bd-gold-layer-runner/E_18/<run_id>.jsonl`, and one E_18 record inside `gold/perf_report.json`
and its `gold/perf_history/` archive.

## What E_18 does when the chain runs it -- every branch

| branch | what is written | served effect |
|---|---|---|
| A. plan empty (TODAY: measured on the runner 07:16Z and 08:17Z -- 4 new names, 1 with a real ticker, that 1 not resolvable directly) | nothing | none |
| B. a new real ticker that bd-securities classifies directly against the canonical vocabulary | one NEW row per ticker in `etf-classifications`, `classified_by: scheduled`, `updated_by: e18-scheduled`, written with `attribute_not_exists(ticker)` -- an existing row is never touched | from the same run on, that ticker's class on C_06 / D_03 / D_04 and on the Holdings route comes from the canonical row, not the bd-securities fallback. This is the PRD's FWD-7 outcome, and the row's values come from the same bd-securities input the fallback reads |
| C. E_18 exits non-zero (refusal rc 2 when the shared modules are missing; any exception) | nothing, or the rows written before the exception | the chain continues; the WARN line is the record |
| D. the freshness gate skips the run | E_18 does not run | none |

Rollback of a branch-B row, where its class is wrong: the seed source (seed always wins) corrects it with no delete. A
`delete-item` is a destructive act and needs Andrew's word; two seat signatures are not that.

## Exercise -- DONE before signing, read-only (SSM command `e4844f73-3e86-403d-a265-b9cf86f0e184`, 08:17:50Z-08:18:00Z)

The candidate bytes were carried to a scratch folder on the runner (`/tmp/e18cand/`, md5 `d6ab7998...b171` verified
there) and run as `gold_dispatch.sh --single E_18 --dry-run --no-shutdown` while the BD_THREAD_R3 exercise run was in flight:

- `bash -n` clean on the runner's bash 5.1.16; `DISPATCH_RC=0`.
- E_18 ran under the real `runner-telemetry.py` / `gold_prof.py` wrap with no flag: `E_18 done (rc=0)`, 4.5 s wall, peak
  1,443 MB, the same detection summary as 07:16Z (candidates 1, written 0 / refused 0, unresolved 1).
- The synced copy the live chain executes stayed the live bytes: `/tmp/gold_layer_scripts/gold_dispatch.sh` md5
  `6e648344...fd37` before and after.
- Side effects, all additive: the checkpoint marker for 2026-10-01, one telemetry file, a log upload, and a perf report
  merge (28 scripts) with its archive copy. No served key and no table row was written.

Local, at the candidate: `MDPF_SECCLASS_M/R7_CHECKS/test_gold_dispatch_e18_slot.sh` 19 of 19 PASS (the switch's difference
control included: switch set + module present clamps and turns a proceed into a skip);
`data/black_diamond/scripts/gold/test_adhc_compil_002_gate.sh` 8 passed, 0 failed.

**Not exercised:** `PHASE_B3b` inside a full parallel chain (`run_background` + `wait_phase`). `wait_phase` aborts only on a
non-zero wait status, and `run_script` returns 0 for E_18 on every path (test 4.1); the first proceeding scheduled fire is
its first real run.

## Window and acceptance

- **Window (invariants, each read live into the ledger with its UTC time):** (i) the gold runner reads `stopped` before the
  put, so no chain is mid-run and no `sync_scripts` can swap the file under a running bash; (ii) the put and its ETag
  readback complete at least 30 minutes before the next scheduled gold fire (`bd-gold-nightly-fallback` `cron(0 23 ? *
  MON-SAT *)`, `bd-canonical-prices-daily` `cron(0 4 * * ? *)`; `bd-gold-layer-monthly-trigger` reads DISABLED).
  Planned gap: today, after the BD_THREAD_R3 exercise run stops the runner and before 22:30Z.
- **Acceptance:** the first scheduled gold fire after the put whose freshness gate PROCEEDS, read from its log under
  `s3://opal-data-bd/logs/gold-layer/`: (1) `PHASE_B3b: E_18` then `E_18 done (rc=0)` and `[PHASE] PHASE_B3b complete`;
  (2) the count of `CALGUARD` lines is 0; (3) the chain completes with exit code 0 and PHASE_B4 onward ran; (4) E_18's
  "Scheduled rows written / refused" figure equals the number of `updated_by: e18-scheduled` rows the table gained
  (expected 0 and 0 today). A fire the gate SKIPS is neither a pass nor a fail: the leg stays open to the next fire.
- **Rollback triggers:** the dispatcher fails to parse or aborts before PHASE_B4 for a reason in these bytes; a `CALGUARD`
  line appears; E_18 writes a row to an existing ticker. `E_18 done (rc!=0)` with the chain continuing is NOT a rollback
  (branch C): it is a FAIL of acceptance (1) and the next item.
- **BD_THREAD_R3 shares the 23:00Z fire** (its leg A1: C_06, D_03, D_04 exit 0). The two acts change disjoint keys;
  attribution is by log line: a failure at C_06 / D_03 / D_04 is R3's, a failure at PHASE_B3b or in the dispatcher is this act's.
- **Ledger:** one new entry, `secclass-e18-trigger-dispatcher-m-20261001`, opened before the put, recording the prior
  VersionId; legs D (put + ETag) and A (acceptance).

## Not covered by this half

- **Turning the guard on** (ruling item 4): `0.7.0_AE_CloudOps`'s separate act under its own two halves, after
  `lib/trading_calendar.py` is deployed (it reads 404 on `code/gold/lib/` at 08:18Z) and the skip arm is observed.
  `docs/references/FRESHNESS_GATE_MANIFEST_20260717.md` R3 (route the compare through the trading calendar) stays open on it.
- **Cottonwood's and Inflection's triggers.** `data/cot/scripts/gold/gold_dispatch.sh` is a different file outside this
  seat's grant, and Inflection has no caller (row `MDPF_SECCLASS-S2`). This act schedules Black Diamond's E_18 only.
- **The shared-infra write grant** (row W6-S2), unchanged.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 08:2xZ)

Signed on the blast radius above: one key, its rollback by VersionId, the four branches of E_18, and both arms of the
freshness gate (unchanged from the live bytes with the switch unset, by test). Read at signing: the live key's VersionId
and ETag (`list-object-versions`, 08:18Z); the candidate md5 from `git show 6f4bde6b6a:`; the three gold rules' schedules
and states (`events list-rules`, 08:18Z); the calendar module's 404 (08:18Z); the runner exercise's output (above).
I deploy only in a gap that meets (i) and (ii), and I stop on any deviation this file does not name.

## CTO half -- (unsigned)
