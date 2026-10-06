# AMGT_RESAPP task order -- `AMGT-az-3` -- THE REMEDIATION-ROW TRIAGE: A CITING ROW FOR EACH OF THE 109 OPEN, OWNED, UNMOVED ROWS (CTO RULING 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-az-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~264</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; record rows only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the repository and the record; no store read or write.
comp-adversary: RUN by the issuer at the cut -- the project census lists 461 remediation rows: 352 REMEDIATED and 109 OPEN, owned by 2.0.0_SA_COO~W 41, ~Z 23, 1.0.0_SA_CTO~Z 21, 2.0.0_SA_COO~ZZZ 15, and others. r76 c64 base: 0 of 109 carry a TRIAGE citing row.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r76-264` (branch `wk-AMGT_RESAPP-264`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r76-264`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-az-3` (round 76, decomposition s.84)

CTO ruling 4, in the same shape as ETFS_RIVALS' C-S41. A count that only grows is not a backlog anyone is working.

`comp-surprise --project AMGT_RESAPP --json` lists the `remediation_rows`; 109 of them have `remediation.state` OPEN. For EACH, read
the row (its `mechanism`, `evidence` and remedy), then MEASURE the world at HEAD: the file or line it names, the commit that would carry
the fix, the served value. Then append ONE citing row to `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` whose `one_line` begins `TRIAGE <that row's id>:` and says ONE of:
- **CLOSED BY EVIDENCE:** the remedy is in the world. Name the commit or the measured value.
- **CUT:** the row no longer applies; the code, route or product it named is gone or superseded. Name what superseded it.
- **BLOCKED:** name the blocker and its current owner seat. The owner is a seat that holds this project's work today (read the
  open order files under `task-orders/`), never a retired lane such as `~W` or `~ZZZ`.

Rules:
- Copy the field set of an existing issuer row (`AMGT_RESAPP-Z-S358` is a recent one). Class OBSERVATION, hazard INERT,
  `disarm_owner` `2.0.0_SA_COO~Z`. Ids are `AMGT_RESAPP-Z-W264-S<k>`.
- Do NOT edit any existing row; this channel is append-only.
- Group your evidence reads. Do not spend more than about 2 minutes per row; a row you cannot settle in that time is BLOCKED, naming
  what is missing.
- Write a summary table to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~264/TRIAGE.md`: id, verdict, one-line evidence, owner.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W264-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the investigation file (append) and your deliverables. No code, no store write, no message.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~264/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-az-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell c64 --where local; echo "exit=$?"</invocation><expect>every OPEN remediation row has a TRIAGE citing row (0 missing); C1 PASS; R76 C64 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~264 <0.9.0_WK_AMGT_RESAPP~264@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~264/AMGT_RESAPP.TO-AMGT-az-3.remediation-row-triage.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the verdict counts (closed / cut / blocked) and the blocked rows' owners;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-75 analysis item 3, ruling 4. The CVO reads the TRIAGE table at L9.

<status>pending</status>
<status>complete -- drained @25dab214fb; proof VALID (worktree checker); c64 109/109 cited (30 closed, 26 cut, 53 blocked)</status>
<round>76</round>
<slot>0.9.0_WK_AMGT_RESAPP~264</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
