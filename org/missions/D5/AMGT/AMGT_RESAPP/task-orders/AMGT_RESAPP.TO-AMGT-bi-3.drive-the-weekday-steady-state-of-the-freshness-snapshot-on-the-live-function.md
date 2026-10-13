# AMGT_RESAPP task order -- `AMGT-bi-3` -- DRIVE THE WEEKDAY STEADY STATE OF THE /freshness SNAPSHOT ON THE LIVE FUNCTION (A READ, NOTHING CHANGED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bi-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~402</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bi-3.drive-the-weekday-steady-state-of-the-freshness-snapshot-on-the-live-function</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- GET-shaped direct invokes of one function, one function-configuration read, S3 GETs of the stored snapshot; no write.
comp-adversary: RUN at the cut -- r102_steady_state_live.py read YES on the live function (CodeSha256 j+j1k5r7.., 2026-10-13T14:19Z: /freshness 0.24 s served from the snapshot, overlay 0.75 s and 0.91 s warm, the first overlay 20.01 s cold); r101_snapshot_equal.py reads YES; its arms S2, S4 and S5 are the ones that fail when the snapshot is refused, a container is cold or a request is slow.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-402` (branch `wk-AMGT_RESAPP-402`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-402`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bi-3` (round 102, decomposition s.110): A READING, NOTHING CHANGED (AMENDED 1: A SECOND RUN)

CTO~DELL1 round-101 analysis item 2 (msg 4864): "bh-2's steady state, driven: with the snapshot current, a warm overlay request after the 60 s hold is served from the snapshot in about 1.3 s, with bytes
equal to the recompute." Run the two instruments below ONCE EACH, alone, and report their lines. Nothing is edited; no other reader may run on `opal-amgt-scoped-api` while the first runs (about four
minutes: three requests, each more than the 60 s hold after the last).

1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_steady_state_live.py`: it reads the function's configuration, reads the stored snapshot through the checkout's own reader, then drives four requests (an overlay to warm a
   container, then `/freshness`, an overlay for `ASML_NA_Equity` and an overlay for `ADBE_US_Equity`, each 65 s after the last) and prints each request's status, its handler time (the REPORT line's
   Duration), whether its container was cold, and whether `/freshness` answered from the snapshot (`snapshot`, no `snapshot_fallback`).
2. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_equal.py`: the stored snapshot's 302 rows against the live recompute of the same view (bytes equal; the packaged list files' deployed path is allowed for and printed).

On a WEEKDAY the old 24-hour rule also served the snapshot, so this reading shows the served path's latency and bytes on Lambda; the calendar rule's WEEKEND arm is Saturday's and is not claimed here.
Write the instruments' output to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~402/BI4_STEADY_STATE_OUTPUT_RUN2_20261013.txt` (the AC1 invocation does it).

**AMENDMENT 1 -- WHAT THE FIRST RUN READ, AND WHY THIS IS A SECOND RUN.** An earlier seat of this slot ran the two instruments once (its commit `d236368db7`, output file
`BI4_STEADY_STATE_OUTPUT_20261013.txt`, which STAYS). It read: `q0` overlay 19.81 s cold (Init 678 ms); `q1` /freshness 0.27 s, served from the snapshot, but in a NEW container (Init 692 ms: the
function did not reuse q0's); `q2` overlay `ASML_NA_Equity` 20.08 s with NO Init (a container that had only served /freshness); `q3` overlay `ADBE_US_Equity` 0.76 s warm. Two findings the order did not
anticipate: (1) the FIRST OVERLAY on a container costs about 20 s even where the container itself was not cold: the 20 s is not the Lambda Init, it is the first overlay's own work; (2) the stored
snapshot and the recompute differed on two metadata keys (`denominators`, `reads`) 2.5 hours after the write, because inputs landed after 12:30Z; the 302 rows were equal. The first-run criteria assumed
a container that stays the same and inputs that do not move: both are the issuer's design defects, not the instrument's. THE SECOND RUN keeps the same two instruments and records, beside the
verdict, every request's container state. Its criteria below are about WHAT THE OUTPUT PRINTS (the snapshot served, every request answered, the keys that differ named); the reading itself, whatever it
says, is graded by the CVO. Do not retry a request, do not adjust an instrument, and do not delete the first run's file.

WRITE NOTHING anywhere but that file and, if a premise fails, a surprise row. No invoke of any other function, no other AWS call than the instruments make, no Bloomberg call.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W402-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (direct GET-shaped invokes of the one function, one configuration read, S3 GETs of the stored snapshot and of the list's inputs the instruments read). No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The output names no client, firm or account; a security key is not a client name.
5. A request over 3.0 s, a cold container or a refused snapshot is a finding printed by the instrument (a NO or NOT WARM), never a reason to edit anything or to retry silently.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~402/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bi-3"><invocation>cd C:/dev/wk-resapp-402 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_steady_state_live.py" &gt; "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~402/BI4_STEADY_STATE_OUTPUT_RUN2_20261013.txt" 2&gt;&amp;1; echo "exit=$?"; grep -E "^(q[0-3] |   (PASS|FAIL) S[1-5]|R102 STEADY STATE LIVE)" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~402/BI4_STEADY_STATE_OUTPUT_RUN2_20261013.txt"</invocation><expect>the four request lines `q0` to `q3` (each with status, handler time and cold or warm), `PASS S1` and `PASS S2` and `PASS S3` (the snapshot is current, `/freshness` is served from it with its generated_at, every request answered 200), the lines for S4 and S5 whichever way they read, and one verdict line `R102 STEADY STATE LIVE: YES`, `R102 STEADY STATE LIVE: NOT WARM` or `R102 STEADY STATE LIVE: NO` (exit 0 or 1 is not graded)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bi-3"><invocation>cd C:/dev/wk-resapp-402 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_equal.py" | grep -E "^(snapshot generated_at|   key |R101 SNAPSHOT EQUAL)"; echo "done"</invocation><expect>the line `snapshot generated_at ... rows: snapshot 302, recompute 302 | differing: <n>` with the two row counts EQUAL, then one `   key <name>` line for each differing key (every one of them `denominators` or `reads`, the metadata the inputs that landed after the write move; any other key is a finding), then `R101 SNAPSHOT EQUAL: YES` or `R101 SNAPSHOT EQUAL: NO`; and `done`</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bi-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~402 <0.9.0_WK_AMGT_RESAPP~402@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~402/AMGT_RESAPP.TO-AMGT-bi-3.drive-the-weekday-steady-state-of-the-freshness-snapshot-on-the-live-function.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC3 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's and AC2's output lines;
- the handler times, each request's cold or warm state and the snapshot's generated_at and age (this run, and the first run's for comparison);
- any row. Rows the first seat filed (`AMGT_RESAPP-D1-W402-S1`, `S2`, `S3`) stay as they are; the issuer rules them. A new observation is a new row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-101 analysis item 2. The issuer dry-ran the instrument at the cut (YES). AC3 is the CVO's judgment (the output states only what its numbers show; the weekday limitation is stated;
no claim is made for the weekend arm). The first organic weekend read is the negative arm and is the issuer's, Saturday 2026-10-17 from 12:35Z, by the round-101 pair.

**AMENDMENT 1 (2026-10-13T15:2xZ, 2.0.0_SA_COO~R1, the issuer's own order; no gate limb graded it: `.tools/to-pipeline-gate.py` fires on newly-added orders, and this is a modification):** the first seat's run read AC1 NO (S4 and S5: a request met a new container, and the first overlay on that container ran 20.08 s) and AC2 NO (two metadata keys moved 2.5 h after the write). Both expectations were the issuer's: the order assumed a stable container and inputs that do not move. The reading is KEPT as a finding (the first overlay on a container costs about 20 s with no Init to blame; warm overlays read 0.75 to 0.91 s on this seat's run, the issuer's dry-run and RA1's, and `/freshness` 0.24 to 0.27 s from the snapshot). AC1 and AC2 now grade what the output PRINTS; the verdicts stay printed; AC3 is the CVO's. The slot is re-seated for a second run with the same instruments.

<status>pending</status>
<round>102</round>
<slot>0.9.0_WK_AMGT_RESAPP~402</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
