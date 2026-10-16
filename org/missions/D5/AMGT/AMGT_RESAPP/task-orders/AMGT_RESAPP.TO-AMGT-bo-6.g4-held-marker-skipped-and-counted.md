# AMGT_RESAPP task order -- `AMGT-bo-6` -- THE FILINGS BATCH SKIPS AND COUNTS A NAME WHOSE STORED UNRESOLVED-SOURCE DIFFERS, INSTEAD OF RAISING (G4: THE STOP-ON-ONE-MARKER FIX)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bo-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~480</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bo-6.g4-held-marker-skipped-and-counted</to_id>
<placeholders>NONE</placeholders>
<workstream>G4HELD</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing is scheduled, registered, enabled or run by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is made by anything this order adds; its tests stub every S3 and runner boundary.
comp-adversary: RUN at the cut -- at the base `python -m pytest lib/research/filings/tests/test_batch_held_continue.py -q` reads `no tests ran`, rc 4 (FAIL as expected); `python -m pytest lib/research/filings/tests lib/research/harvest/tests/test_filing_attempt_skip_held.py -q` reads `350 passed`, short of the 355 the criterion needs (FAIL as expected). The behaviour at the base was read on the first fire of the filings task (2026-10-16 07:30 ET): the run stopped on its first name with exit 1 after one `.HELD.json` marker.
EGRESS CLASS, declared: NONE. No S3, no network, no model call, no Windows task.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-480` (branch `wk-AMGT_RESAPP-480`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-480`.

## 1. THE CELL -- `AMGT-bo-6` (round 108, decomposition s.117b)

`lib/research/harvest/filings.py` `state_put_filing_attempt` writes an `UNRESOLVED-SOURCE.json` once per name. A later attempt whose outcome DIFFERS from the stored one does NOT overwrite it: it writes a sibling `UNRESOLVED-SOURCE.HELD.json` and raises `FilingAttemptChangedError` (a `store.HarvestStoreError` subclass with a `differing_field` string; `lib/research/harvest/tests/test_filing_attempt_skip_held.py` is its test). `lib/research/filings/batch.py` does not catch it, so ONE such name ends the whole run with exit 1: on the first fire of the scheduled filings task (2026-10-16) the first universe row (AAPL) raised, the run stopped after one marker, and the other names were never reached. The CTO ruled that a name whose stored marker differs is SKIPPED and COUNTED, never raised.

**Build exactly this, in `lib/research/filings/batch.py` only (plus a new test file).**
1. Catch `FilingAttemptChangedError` (import it from `lib.research.harvest.filings`) at the batch's per-name boundaries: (a) around each `run_group(...)` call in `main()`'s fetch loop (a group's names are held together; one entry per group), and (b) around the `hf.state_put_filing_attempt(...)` call in `main()`'s unresolved loop (one entry per name). The marker the harvest module writes BEFORE it raises is the record: write nothing more.
2. A caught name prints one line `HELD: <security_key or the group's keys, comma-separated> <differing_field>` and the batch CONTINUES with the next group or name. It is counted in a `held` counter that is NOT folded into the analyzed, UNRESOLVED-SOURCE or written counters.
3. The two existing summary lines keep their words and numbers for what they count (`BATCH DONE: ...`, `UNRESOLVED-SOURCE DONE: ...`); after them print one new line `HELD DONE: <n> name(s) held (a stored UNRESOLVED-SOURCE differs from the fresh attempt; a sibling UNRESOLVED-SOURCE.HELD.json was written by the harvest module)` ALWAYS (n may be 0). The exit code stays 0 when the only failures were held names; any OTHER exception still propagates as today.
4. Tests, a new file `lib/research/filings/tests/test_batch_held_continue.py`, at least 5, each stubbing every S3, EDGAR and model boundary (no network, no subprocess): T1 two groups, the first raises `FilingAttemptChangedError`: the second group still runs and its result is reported; the HELD line names the first; exit 0; T2 the unresolved loop: the second name's `state_put_filing_attempt` raises, the third name is still written, `unresolved_written` counts the two written, the HELD count is 1; T3 no held names: the `HELD DONE: 0 name(s) held` line prints and every other line is the same as before; T4 a non-held exception (a `RuntimeError` from a group) still propagates; T5 `--write-pool` off: no held handling is reached and nothing is printed as HELD. Read `lib/research/harvest/tests/test_filing_attempt_skip_held.py` and the existing batch tests under `lib/research/filings/tests/` for the stubbing style.
5. Nothing else: do not touch `lib/research/harvest/filings.py` (its raise stays: `battery.py` and its own tests depend on it), `analyze.py`, `fetch.py` or any other module; register, enable and run nothing.

**Do this in order.** (1) Run AC1 and AC2 once on the unchanged tree and record what they print. (2) Write the tests first (item 4), run them red. (3) Build items 1 to 3. (4) Run AC1 and AC2. (5) Every `.py` edit passes `.tools/commit-gate.sh`: keep the file pure ASCII.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only `lib/research/filings/batch.py`, the new test file, your deliverables and the channel. Never register, enable or run a Windows task; never call AWS; never run the filings batch for real.
2. No new alert, monitor or notification of any kind. The batch's behaviour for every name that does not raise is unchanged byte for byte.

## 3. SURFACES

<paths>
lib/research/filings/batch.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~480/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bo-6"><invocation>cd C:/dev/wk-resapp-480 &amp;&amp; timeout 300 python -m pytest lib/research/filings/tests/test_batch_held_continue.py -q; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 5, no `failed`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bo-6"><invocation>cd C:/dev/wk-resapp-480 &amp;&amp; timeout 600 python -m pytest lib/research/filings/tests lib/research/harvest/tests/test_filing_attempt_skip_held.py -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>a line `<n> passed` with n at least 355 (the 350 now plus at least 5), no `failed`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~480 <0.9.0_WK_AMGT_RESAPP~480@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~480/AMGT_RESAPP.TO-AMGT-bo-6.g4-held-marker-skipped-and-counted.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-bo-6.g4-held-marker-skipped-and-counted.md` from `C:/dev/wk-resapp-480` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the pre-edit runs of AC1 and AC2 and the post-edit runs, with their output lines;
- the verdict line of the instance check;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's msg 6673, item 2: "A separate cell: one name's mismatched marker is skipped and counted, not raised. It lands before unattended full-universe fires." Evidence at the cut: the first fire's one written object (`amgt/harvest/state/filing_attempt/security_key=AAPL_US_Equity/UNRESOLVED-SOURCE.HELD.json`, 11:30:26Z) and its text (`differing_field: filing_identity: {'source': 'none'} -> {'source': 'edgar', 'cik': 320193, 'form_expected': 'none'}`); a read-only run of the same row without `--write-pool` exits 0, so the stop is the write path's raise. The exception is raised by a module `battery.py` also catches (line 1645) and by its own tests: it is left as is on purpose. Independent of `AMGT-bo-5` (a different module); the re-enable of the filings task waits on `bo-5` and a new pair half, NOT on this cell, because the key-list run never reaches a `none`-form name; this cell must land before any unattended FULL-universe fire. Baseline measured at the cut: `lib/research/filings/tests` plus `lib/research/harvest/tests/test_filing_attempt_skip_held.py` read 350 passed, rc 0 (11 s).

<status>complete</status>
<round>108</round>
<slot>0.9.0_WK_AMGT_RESAPP~480</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
