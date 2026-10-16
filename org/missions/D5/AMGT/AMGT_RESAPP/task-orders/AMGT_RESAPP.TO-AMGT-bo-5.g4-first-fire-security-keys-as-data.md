# AMGT_RESAPP task order -- `AMGT-bo-5` -- THE FILINGS BATCH'S FIRST FIRE TAKES A LIST OF SECURITY KEYS FROM THE DATA FILE (G4: THE 8 NEW ANALYZABLE NAMES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bo-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~479</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bo-5.g4-first-fire-security-keys-as-data</to_id>
<placeholders>NONE</placeholders>
<workstream>G4KEYS</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled, registered, enabled or run by this order; the three Windows tasks stay Disabled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is made by anything this order adds; its tests stub every runner.
comp-adversary: RUN at the cut -- at the base `python -m pytest lib/research/llm_batch/tests/test_security_keys.py -q` reads `no tests ran`, rc 4 (FAIL as expected); `python -m lib.research.llm_batch.run filings --print-command` reads `LLM-BATCH task=filings command=python -m lib.research.filings.batch --universe newest --write-pool --limit 20` (the line the criterion refuses: it carries `--limit 20` and no `--security-key`; FAIL as expected); `python -m pytest lib/research/llm_batch/tests -q` reads `32 passed`, short of the 40 the criterion needs (FAIL as expected). The 8 names were read by `python -m lib.research.filings.batch --universe newest --dry-run`: 13 fetchable names with a real expected form, 5 already analyzed.
EGRESS CLASS, declared: NONE. No S3, no network, no model call, no Windows task.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-479` (branch `wk-AMGT_RESAPP-479`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-479`.

## 1. THE CELL -- `AMGT-bo-5` (round 108, decomposition s.117b)

`lib/research/llm_batch/` (round 107 `AMGT-bn-6`, round 108 `AMGT-bo-4`) runs the filings batch when its event says so. `run.py` holds `load_limits(path)` and `command_for(task, limits)` (the filings argv gets `--limit N` when `first_fire_limit.json` carries a positive integer for it). The first fire stopped on its first universe row, so the CTO ruled: name the 8 analyzable new names instead of capping a count. The filings batch already takes `--security-key KEY` (repeatable; it "keeps only the named security key(s) in the plan, both the fetch groups and the unresolved partitions, and refuses before any fetch if a named key is in neither"); do not change that module.

**Build exactly this, nothing else.**
1. `lib/research/llm_batch/first_fire_limit.json` becomes `{"limits": {"filings": null}, "security_keys": {"filings": ["ASML_US_Equity", "BA_US_Equity", "COST_US_Equity", "HAL_US_Equity", "HD_US_Equity", "INTU_US_Equity", "KMB_US_Equity", "VLO_US_Equity"]}, "claim": "held", "basis": "<one ASCII sentence: cluster CTO ruling XA-20261016T050756Z-844a and the CTO's addendum (msg 6673): the filings first fire names the 8 analyzable new names; the first fire of 20 rows stopped on AAPL>"}`. Pure ASCII.
2. In `run.py`: `load_security_keys(path)` returns `{}` when the file is absent, else the file's `security_keys` object (a missing `security_keys` key reads as `{}`); it RAISES `ValueError` when `security_keys` is present but is not an object, or any entry is not a non-empty list of non-empty strings (a malformed list must never read as "no filter", because that would run the whole universe). `command_for(task, limits, keys=None)` appends `--security-key K` for each key of `keys.get(task.key)` in list order, then `--limit N` as before when the limit is a positive integer; the argv is unchanged when both are absent. `run_task` takes a `keys` keyword (default `None`) and passes it; `main()` passes `load_security_keys(LIMITS_PATH)`. The plan-only command is NOT changed.
3. `--print-command` prints the argv `command_for` returns, as before.
4. Tests, a new file `lib/research/llm_batch/tests/test_security_keys.py`, at least 8, each stubbing every runner (no subprocess, no S3): T1 filings with 8 keys: argv ends with the eight `--security-key` pairs in list order and carries no `--limit`; T2 keys AND a limit: keys first, then `--limit`; T3 no keys and no limit: argv unchanged; T4 a key list for another task does not touch filings; T5 `load_security_keys` reads the committed file and returns the 8 names above; T6 a missing path returns `{}`; T7 malformed: `security_keys` a list, an entry `"ASML_US_Equity"` (a string, not a list), an entry `[]`, an entry `[""]`, an entry `[1]` each raise `ValueError`; T8 `run_task` hands the runner the keyed argv and the plan-only argv unchanged. Update `tests/test_first_fire_limit.py` only where it reads the committed file's value `{"filings": 20}` (its T4): it now reads `{"filings": None}`; touch nothing else in that file.
5. Nothing else: do not touch `tasks.py`, `register.py`, `trigger.py`, `inputs.py`, the launchers or any other module; register and enable nothing; `register --plan` still prints `PLAN: 3 task(s), 0 created`.

**Do this in order.** (1) Run AC1 to AC3 once on the unchanged tree and record what they print. (2) Write the tests first (item 4), run them red. (3) Build items 1 to 3. (4) Run AC1 to AC3 and `python -m lib.research.llm_batch.register --plan | tail -1`. (5) Every `.py` edit passes `.tools/commit-gate.sh`: the package is pure ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the files named above (the data file, `run.py`, the two test files, your deliverables, the channel). Never register, enable or run a Windows task; never call AWS; never run the filings batch for real.
2. No new alert, monitor or notification of any kind. No change to what a batch does.

## 3. SURFACES

<paths>
lib/research/llm_batch/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~479/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bo-5"><invocation>cd C:/dev/wk-resapp-479 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests/test_security_keys.py -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 8, no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bo-5"><invocation>cd C:/dev/wk-resapp-479 &amp;&amp; timeout 120 python -m lib.research.llm_batch.run filings --print-command; echo "exit=$?"</invocation><expect>exactly one stdout line `LLM-BATCH task=filings command=python -m lib.research.filings.batch --universe newest --write-pool --security-key ASML_US_Equity --security-key BA_US_Equity --security-key COST_US_Equity --security-key HAL_US_Equity --security-key HD_US_Equity --security-key INTU_US_Equity --security-key KMB_US_Equity --security-key VLO_US_Equity`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bo-5"><invocation>cd C:/dev/wk-resapp-479 &amp;&amp; timeout 300 python -m pytest lib/research/llm_batch/tests -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 40 (the 32 now plus at least 8), no `failed`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~479 <0.9.0_WK_AMGT_RESAPP~479@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~479/AMGT_RESAPP.TO-AMGT-bo-5.g4-first-fire-security-keys-as-data.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bo-5.g4-first-fire-security-keys-as-data.md` from `C:/dev/wk-resapp-479` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the pre-edit runs of AC1 to AC3 and the post-edit runs, with their output lines;
- the output of `python -m lib.research.llm_batch.register --plan | tail -1`;
- the verdict line of the instance check;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's msg 6673 (item 1: "Cut the cell for the 8 new analyzable names (about 5.6 USD), then a new COO half; I sign it, then re-enable"). The 8 names are the 13 fetchable names with a real expected form (read by `filings.batch --universe newest --dry-run`: 163 `none`, 7 `10-K`, 6 `20-F`) minus the 5 that `--plan-only` reads SKIP-UNCHANGED (ASML NA, BABA US, NU US, PBR US, SAP GY). Cost: about USD 5.6 is 8 x the mean of five stored 20-F analyses (0.6947); seven of the eight are 10-K filers whose per-analysis cost is NOT measured; the CTO's condition (a mean above 0.80 returns to the CTO before anything widens) stands. The batch's `--security-key` was read in `filings/batch.py` lines 513-518 and 555-558. The trigger keeps reading the unfiltered `--plan-only` count (171 WOULD-RUN): the task stays due daily while that count is above zero, and a second day's run over the 8 skips them as unchanged (no spend). The re-enable waits for a new COO half, which states whether the one HELD marker the first fire wrote is inside its blast radius (it is not in the first half's list: see `ledger/G4_FILINGS_FIRST_FIRE_RESULT_20261016.md`).

<status>complete</status>
<round>108</round>
<slot>0.9.0_WK_AMGT_RESAPP~479</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
