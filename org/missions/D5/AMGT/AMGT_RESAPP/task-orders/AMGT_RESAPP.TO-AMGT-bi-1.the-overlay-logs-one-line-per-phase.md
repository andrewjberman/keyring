# AMGT_RESAPP task order -- `AMGT-bi-1` -- THE OVERLAY LOGS ONE LINE PER PHASE (LOG LINES ONLY; A BUILD, NOT YET SERVED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~401</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bi-1.the-overlay-logs-one-line-per-phase</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads the live pool with the worker's own session (S3 GETs and LISTs); no write, no function invoke.
comp-adversary: RUN at the cut, each arm against the literal string written below: r102_overlay_phase_check.py reads 'arms passed 8 of 14 ... R102 OVERLAY PHASE LOG: NO' at the base (A1, A4a and A4b FAIL on both subjects; the base's A2, A3, A5, B1 and B2 PASS), and 'arms passed 14 of 14 ... R102 OVERLAY PHASE LOG: YES' on a throwaway candidate in a scratch worktree (the patch below, blob 02627c18a0ea, +32 -9); the boundary clause of AC2 prints nothing at the base.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-401` (branch `wk-AMGT_RESAPP-401`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-401`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bi-1` (round 102, decomposition s.110)

CTO~DELL1 round-101 analysis item 1 (msg 4864): the cold first overlay request on the live function is about 20 s and is NOT attributed; no remedy is cut until per-phase log lines on Lambda name the
phase. This cell adds those lines to the overlay and moves NOT ONE served byte: `AMGT_PHASE route=overlay phase=<name> ms=<n>` through the module's existing `_phase_log`, in the order
identity, model_block, axis_reads, check_face, feed, description, research_coverage, posture, peers, provenance, top_band, input_provenance, read_security_overlay, serialize. LOG LINES ONLY: no metric,
no alarm, no monitor, no field of any response reads a timing.

Apply the prepared edit, then verify it. The patch is the whole of the change (32 lines added, 9 changed, ONE file, `lib/research/api/scoped_amgt.py`, base blob `9f72b58aa87e`):

    cd C:/dev/wk-resapp-401 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/r102_candidate_source.patch"

What it does, so you can read it before you trust it: (a) adds `_phase_call(route, phase, call)` after `_phase_log`: it runs `call()` exactly as before, returns its value unchanged and prints one phase line,
also when the call raises; (b) in `read_security_overlay` it times the model-block read, the axis loop, the check face, the feed and the description with `_phase_log`, and wraps the six dict entries
`research_coverage`, `posture`, `peers`, `provenance`, `top_band`, `input_provenance` in `_phase_call` (same expressions, same order); (c) in `handler` it times `resolve_identity(requested)` when the leaf is
`overlay`, and splits the overlay leaf into `read_security_overlay` and `serialize` phases around the unchanged `_response(200, ...)`. If `git apply` refuses, STOP and file a BLOCKING row: do not edit by hand.

Then run `python -m py_compile lib/research/api/scoped_amgt.py` and AC1. The check runs the BASE blob and your tree's handler in one process on the live pool (read only) and compares status and body bytes,
the phase lines and their sums.

Write NOTHING outside the file named in section 3.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W401-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. ONE product file, `lib/research/api/scoped_amgt.py`, changed by the prepared patch and nothing else. No test file, no module, no new file in `lib/`.
2. No deploy, no function invoke, no store write, no schedule, no S3 delete, ever. No Bloomberg, SEC or model call. No `pip install`.
3. Standing: no push of shared branches.
4. The check's reads are the worker's own session's; it prints no client, firm or account.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~401/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bi-1"><invocation>cd C:/dev/wk-resapp-401 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_overlay_phase_check.py" 2&gt;&amp;1 | grep -v "^AMGT_500" | tail -4; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`arms passed 14 of 14` then `R102 OVERLAY PHASE LOG: YES`: for ASML_NA_Equity and ADBE_US_Equity the fourteen phase lines in order, none in the base, status and body byte-equal to the base, the inner phases summing to read_security_overlay and the outer phases to the handler call within 5 percent or 5 ms, the other printed lines unchanged; the unresolved key answers the same; the thesis route prints no overlay line; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bi-1"><invocation>cd C:/dev/wk-resapp-401 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- lib portal infra .tools | sort</invocation><expect>exactly one line, `lib/research/api/scoped_amgt.py`, and no other line (the change is ONE file, committed)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~401 <0.9.0_WK_AMGT_RESAPP~401@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~401/AMGT_RESAPP.TO-AMGT-bi-1.the-overlay-logs-one-line-per-phase.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's output lines and AC2's;
- `git diff HEAD~1 HEAD --stat`;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-101 analysis section 3 item 1 (msg 4864): "Per-phase timing LOG LINES in the overlay handler (`_phase_log`, as aw-1 did for rankings): log lines only, no metric, alarm or
monitor. Under its own pair, with served bytes byte-equal. Close: ONE driven cold request ..., its 20 s split by phase on Lambda, and the phases summing to the total within 5 pct. No remedy rides this cell."
The candidate was built and dry-run at the cut (blob 02627c18a0ea). A phase's cost on Lambda is NOT read from the local run (local timings ran 3.5 times faster than Lambda and did not transfer in rounds
99 and 100); the close is bi-2's driven request. STAGED successor: bi-2 (the apply and the request), after this cell's merge, the CTO's review and its pair.

<status>pending</status>
<round>102</round>
<slot>0.9.0_WK_AMGT_RESAPP~401</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
