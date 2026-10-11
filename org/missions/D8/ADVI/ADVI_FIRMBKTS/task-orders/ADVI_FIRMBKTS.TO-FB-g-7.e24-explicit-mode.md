# ADVI_FIRMBKTS task order -- `FB-g-7` -- E_24 REFUSES TO WRITE A SERVED KEY UNLESS THE PLATINUM MODE IS SET EXPLICITLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~29</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- E_24 is a manual rebuild tool with no schedule or caller; no cron, rule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_e24.py` reads 3 of 4: E1 FAILS (the unset `--upload` run reaches the first read) and E2, E3 and E4 PASS as controls (the guard must not stop an explicit mode, a dry run, or break the file). With fake credentials and a dead endpoint every run ends before AWS. Blindness: the check cannot run the upload branch to its end without live data; it grades the guard at the entry.
EGRESS CLASS, declared: NONE (the check points the AWS endpoint at a dead local port).
</preflight>

## 1. THE CELL -- `FB-g-7` (round 4, enrichment item 5; the CTO's act-2 half, E_24 section; row D1-S14)

`data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py` writes one served key, `gold/artifacts/advisor_fee_efficiency.json`, through
`platinum_destination(ADVISOR_FEE_EFFICIENCY)` (lines ~254-258). The producers' destination seam
(`data/black_diamond/scripts/gold/lib/platinum_dest.py`) reads the mode from the environment variable `BD_PLATINUM_MODE`; UNSET means `legacy`. After the
window opens, a hand run of E_24 without the variable would silently write the legacy home, which no reader reads. The
CTO's ruling: E_24 refuses to write a served key unless `BD_PLATINUM_MODE` is set EXPLICITLY, so a hand run must choose.

### 1a. Behavior (the whole spec)

1. In `main()`, immediately after `dry_run` is computed and BEFORE the first S3 call, when `not dry_run` and
   `os.environ.get('BD_PLATINUM_MODE') is None`: `log` one line that names `BD_PLATINUM_MODE`, states that an upload must
   choose a mode (`legacy` or `canonical`), and `return 2`. Nothing is read or written first. (An empty string is "set":
   the seam itself refuses an empty or unknown mode with its `ValueError`, which stays as it is.)
2. A dry run (no `--upload`) is not refused: it writes no served key. An `--upload` with the variable set to `legacy` or
   `canonical` passes the guard and behaves exactly as before.
3. Add `import os` only if the file lacks it. Do not change the seam, any other file, the key, the payload or the log text
   of any existing line.
4. A test `data/black_diamond/scripts/gold/tests/test_e24_explicit_mode.py` (unittest, no network, no AWS): import the module the way the sibling tests
   in that folder import gold scripts (read two of them), monkeypatch `sys.argv` and the environment, and assert (i) the
   refusal returns 2 and names the variable before any `boto3` call (a stub whose every method raises), (ii) an explicit
   mode passes the guard (the stub is reached). If the file's name (dots) forces `importlib.util.spec_from_file_location`,
   use it.

## 2. BOUNDS

1. Files that change: the script and the new test. No other file, no deploy, no AWS call.
2. ASCII only (the script is ASCII today); LF endings. If something cannot be met within your paths, file a surprise row
   and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py
data/black_diamond/scripts/gold/tests/test_e24_explicit_mode.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~29/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~29/ADVI_FIRMBKTS.TO-FB-g-7.e24-explicit-mode.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-7"><invocation>cd /c/dev/wk-firmbkts-29 &amp;&amp; timeout 170 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_e24.py --arms refuse --root /c/dev/wk-firmbkts-29; echo "exit=$?"</invocation><expect>ROUND 4 E24 REFUSE: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-7"><invocation>cd /c/dev/wk-firmbkts-29/data/black_diamond/scripts/gold &amp;&amp; timeout 110 env -u FORCE_COLOR python -m unittest tests.test_e24_explicit_mode 2&gt;&amp;1 | tail -n 3</invocation><expect>^OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-7"><invocation>cd /c/dev/wk-firmbkts-29 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-29 --allow data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py --allow data/black_diamond/scripts/gold/tests/test_e24_explicit_mode.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~29/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 runs the script three ways under fake credentials and a dead endpoint (E1 the refusal, E2 the explicit modes, E3 the
dry run) and checks the file stays ASCII and compiles. AC2 is your test. AC3 is the write-surface bound. Each invocation
terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-7.e24-explicit-mode.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~29`.
Commit the script and the test, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W29-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs
and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** class LOCAL (a manual tool with no caller: 0 of 4,010 SendCommand events in 45 days, the CTO's measure).
The act-2 change-management entry carries the interim text ("any hand run of E_24 exports `BD_PLATINUM_MODE=canonical`")
until this lands. The guard is at the entry so the refusal costs no read.

<status>complete</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-7</to_id>
<slot>~29</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
