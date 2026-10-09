# AMGT_RESAPP task order -- `AMGT-ll-4` -- ONE DISPOSITION PASS OVER EVERY OPEN AMGT_RESAPP REMEDIATION ROW: CLOSED WITH ITS COMMIT, CARRIED WITH AN OWNER, OR DISMISSED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ll-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~348</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a records pass; no code, no store.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the repository only.
comp-adversary: RUN at the cut -- `comp-surprise --project AMGT_RESAPP --json` reads 505 remediation rows, 125 `closed: false` (owners: 2.0.0_SA_COO~W 37, ~Z 29, ~R1 15, 1.0.0_SA_CTO~Z 12, ~ZZZ 7, others); the REMEDIATION_v*.md files are 3.0.0_SA_CVO's lane and are never edited -- the ledger is what the CVO applies.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-348`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ll-4` (round 87, decomposition s.95)

CTO~DELL1 round-86 analysis R3. The domain is every AMGT_RESAPP remediation row reading `closed: false` (read it with
`python .tools/comp-surprise.py --project AMGT_RESAPP --json`, key `remediation_rows`; print the count first). For EACH, write one
ledger entry in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json` (a JSON list):
- `CLOSED` + `commit` (the hash that resolved it, found by reading the row's mechanism/remedy against the code or record at HEAD) +
  `basis` (one line: what you read that shows it resolved);
- `CARRIED` + `owner` (a seat serial) + `condition` (what clears it), when it is still live;
- `DISMISSED` + `reason` (why it is no longer a defect), when its object no longer exists or a later ruling retired it.
Read the code and records named in each row before deciding; never close a row on its age. Write a short
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_NOTES.md` with the count after the pass and every row you could not decide (those are CARRIED to
`2.0.0_SA_COO~R1` with the question as the condition). Do not edit any REMEDIATION, ADJUDICATION or INVESTIGATION file.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W348-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the two files below in your deliverables folder and, for a surprise, the investigation channel.
2. No code, no store write, no deploy, no SEC, vendor, model or Bloomberg call.
3. Standing: no S3 delete, no push of shared branches.
8. CLIENT DATA (0.0.0_AB_MSTR~DELL1 msgs 2720/2747/2766/2804): never open, search, copy or `git show` any
   `org/**/W73_S*_EVIDENCE.json`, the COTBKF ~74 / ~66 / ~70 cottonwood manifests, or the IRPT_DASHBD tie-out files, in the tree or
   in history. Search only inside named paths, never the whole repository.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ll-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_rows.py" --ledger "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json"; echo "exit=$?"</invocation><expect>every open remediation row is disposed exactly once, no id outside the open set, every CLOSED commit resolves, every CARRIED row names a seat and a condition, every DISMISSED row has a reason, and the count after the pass is printed; L1-L5 PASS; R87 ROWS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~348 <0.9.0_WK_AMGT_RESAPP~348@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/AMGT_RESAPP.TO-AMGT-ll-4.one-pass-disposition-of-the-open-remediation-rows.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- AC1's output lines, with the count after the pass;
- the rows you CARRIED to 2.0.0_SA_COO~R1 and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-86 analysis R3 (the CTO counted 99; comp-surprise reads 125 closed:false of 505 -- the check prints its own denominator). The CVO applies the ledger to REMEDIATION at L8/L9. Checks dry-run at the base: AC1 base FAIL as expected (no ledger; 0 of 125).

<status>pending</status>
<round>87</round>
<slot>0.9.0_WK_AMGT_RESAPP~348</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
