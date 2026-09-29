# AMGT_CORPUS task order -- `CRPS-p-4` -- ROUND 14: the six unmet outcomes re-graded on the DEPLOYED function, read-only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-p-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only invocations of the deployed function and S3 reads; no grant moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 14. Serves **FWD-10, FWD-11, FWD-12, FWD-15, FWD-16, FWD-18 (the render halves AMGT_RESAPP owns)**.

## 1. THE CELL -- `CRPS-p-4`

**Where this came from.** Round 13's evidence pass (`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/FWD_EVIDENCE_ROUND13.json`)
read these six UNMET, owner AMGT_RESAPP: the dossier carries the data, but the deployed API (`opal-amgt-scoped-api`, its /thesis
route) and the portal page did not serve it. AMGT_RESAPP's cell `AMGT-ww-1` redeploys that function onto
`amgt/harvest/gold/research_dossier/` under ONE NEVER-2 change entry (`org/critical_paths/change_management/` +
`org/critical_paths/.open_deploys/`). The deployed code before it: CodeSha256 `CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`.

**RULED -- what you build:** `FWD_EVIDENCE_ROUND14_SERVED.json` + `.md` in your deliverables.
1. FIRST read the ww-1 entry: find the change entry whose title names AMGT_RESAPP ww-1 / the redeploy on the canonical prefix
   (`org/critical_paths/change_management/*.md` and `.open_deploys/*.json`, read with `git ls-tree`/`ls -a`, never `ls -1`). Record
   `"entry": {"slug": <slug or "none opened">, "status_read": <OPEN/CLOSED/absent + the time you read it>}`. Read the deployed
   function's configuration (`.tools/aws lambda get-function-configuration --function-name opal-amgt-scoped-api`): record
   `"deployed_function": {"name", "code_sha256", "last_modified"}`.
2. **If the entry is CLOSED:** re-measure each of the six fences (verbatim from the PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md`, with every
   addendum under it) on the
   DEPLOYED function: invoke its /thesis route read-only the way AMGT_RESAPP's own capture library does
   (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py`, used by
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC3.py`) for at least IMB_LN_Equity,
   AZN_LN_Equity, AMD_US_Equity and ADBE_US_Equity, plus the population the fence names with its denominator; a render clause is
   read from the portal source at the DEV branch of the `portal` submodule (`git -C portal show DEV:<path>`; name the commit).
   **If the entry is OPEN or absent:** do not wait and do not invoke; record all six `unmeasurable` with the reason naming the entry
   and its status.
3. Rows: `{"id", "fence_quote" (VERBATIM), "instrument", "output_excerpt", "denominator", "state": met|unmet|unmeasurable, "reason"
   (unmeasurable), "exercising_act" + "owner" (not met; owner one of AMGT_CORPUS, AMGT_RESAPP, DSGN_AMGTV1; an act is driven on
   demand, never a wait), "notes"}`. `state` is your measurement of the clause as written.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND14_SERVED.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND14_SERVED.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-4.served-regrade-six.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive. Scratch `.scratch/p4/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call. Read-only: no S3 write, no Lambda update, no Terraform, no portal edit; a function invocation is a read of the /thesis route only.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W4-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-p-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p4_AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-p-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p4_AC2.sh</invocation><expect>p4 fence_quotes_verbatim 6 of 6</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-p-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p4_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the file's shape: 6 of 6 rows complete with denominators, the entry and the deployed function read; AC2 fence quotes verbatim; AC3 the bound.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-p-4.served-regrade-six.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the entry's slug and status, the deployed CodeSha256, and the six states with owners.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-13 analysis s.4 item 4 @`f1c482d24f` (msg 26603). Checks dry-run at the base `dbafd14c52`: p4_AC1 FAIL (MISSING); p4_AC2 FAIL (MISSING); p4_AC3 PASS (paths_outside_grant 0).
SPAWNED on an event: ww-1's entry closes, or p-1/p-2/p-3/p-5 drain (decomposition v14.0 s.1a, s.9).
<risk>SERVED</risk>
<status>pending</status>
<round>14</round>
<slot>~4</slot>
<fabric>site-z</fabric>
