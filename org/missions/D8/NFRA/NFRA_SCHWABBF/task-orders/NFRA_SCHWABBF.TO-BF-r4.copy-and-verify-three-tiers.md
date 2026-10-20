# TO NFRA_SCHWABBF.TO-BF-r4 -- copy and verify the state, silver and bronze tiers of 08403355 with the move tool (no delete)

<to_id>NFRA_SCHWABBF.TO-BF-r4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending`; do not act before that flip.

---

## WORKER FACE

### GO

(not yet written. It will read: inside 2026-10-21 12:00-20:00Z; `TO-BF-r3` complete and its legs L1-L3 closed; the gateway pair ready; the commit to run the tool from.)

### THE CELL

`BF-r-4`, release act(s) R4a, R4b, R4c of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

Run from a repo checkout at the commit the GO line names, under YOUR identity (never on the box). The tool is `data/canonical/schwab/keyform/move_bronze_key_form.py` (`plan`, `copy [--apply] --concurrency 8`, `verify`); it has NO delete verb. Outside the pull fires (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z). For each tier in this order, STATE then SILVER then BRONZE:
1. `plan --tier <state|silver> --master 08403355 --out <plan file>` (bronze: no `--tier`). Print the `MOVE-PLAN`, `MOVE-COUNT` and `MOVE-OTHER` lines. Expected at the cut (2026-10-20 ~19:5xZ): state 6,930 (complete 765, conversions 6,101, pulls 31, daily_pull 32, backfill_status 1), silver 7,581 over 18 tables, bronze 6,074 (events=6074); the numbers may be larger by new days since. STOP the tier if `foreign` is not 0 or `unrecognized` is not 0.
2. `copy --plan <plan file>` WITHOUT `--apply` (the dry run); print its summary. Then `copy --plan <plan file> --apply --concurrency 8`; print the tail and the exit code.
3. `verify --plan <plan file>`: size and sha256, source against destination; print the summary; exit code must be 0. A mismatch STOPS the order: report; do not delete anything.
4. After the BRONZE copy ONLY (R4c): the 6,074 copies each fire the schwab converter. Start R4c only if `date -u` is at or before 20:30Z (the CTO's rule: R5 must finish by 21:30Z and no pull fire may fall between R4c and R5; otherwise STOP after the silver tier and report). Then WAIT for the events to drain: poll every 5 minutes (printing each) the converter's CloudWatch `Invocations`, `Errors` and `Throttles` for `opal-assets-silver-schwab` and the depth of `opal-assets-silver-dlq` (`get-queue-attributes`); drained = invocations stop and DLQ depth 0. Any Lambda error count above 0 or DLQ depth above 0 is a STOP and a report with the first error log lines (`filter-log-events`).
5. Count the destination after each tier with `list-objects-v2` (paginated; count client-side; print the denominator): bronze under `s3://opal-data-assets/schwab/49financial/bronze/` keys containing `/08403355.`; silver under `schwab/49financial/silver/` keys ending `/08403355.parquet`; state under `s3://opal-data-49financial/schwab/49financial/state/` keys containing `/08403355.`. Print each beside the plan's count.
6. Close ledger legs L4, L5, L6 as each tier verifies (`close-leg ... --proof <output path>`). Do NOT close the entry. Save outputs under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r4/`, commit paths-only, report.
ROLLBACK: the old keys are untouched and the new keys are inert until the readers move: if anything fails, STOP, report, and do not delete the new keys unless the issuer says so (an S3 delete needs a human confirmation).

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r4-AC1" cell_refs="BF-r-4"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r4.copy-and-verify-three-tiers.proof_of_spec.json BF6-r4-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r4-AC1` -- all three tiers of 08403355 are copied to the firm form and verified (size and sha256, exit 0), the converter events drained with 0 errors and an empty DLQ, legs L4-L6 closed; no key deleted.

<expected_criteria>BF6-r4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file.
- **Never:** `terraform apply` outside `safe-apply`; any apply, copy or write outside the legs this order names; deleting an S3 object or version; touching `08242234`, `08335338` or any other master's keys or grants; reading or printing a Schwab token or any secret value; a second concurrent Schwab session; enabling or editing an EventBridge rule; stopping an instance.
- **Window.** The CTO's window is 2026-10-21 12:00-20:00Z. Outside it you do nothing in this order except what its GO line allows. Any failure rolls back that order's legs in the same window (rollback per step below) and is reported at once.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R3-S<k>`; read the investigation file for the highest `R3-S<k>` and use the next; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise. Append the row at the BYTE level (the file mixes CRLF and LF: do not use an editor that rewrites line endings).

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-4`.
<owned_cells>BF-r-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r4-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r4.copy-and-verify-three-tiers.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r4-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** per tier: the plan, copy and verify lines, the destination counts, the event-drain readings, the closed legs, any stop, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- the copy identity writes `opal-data-assets` (`schwab/49financial/`) and `opal-data-49financial` (`schwab/49financial/state/`) under its own role; the converter's firm grants and fence variant were applied by `BF-r-3`; BLIND: the live IAM plane beyond the printed read of `BF-r-1`.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) the bronze copy fires the converter 6,074 times by design (the event-order branch in the plan); (2) bronze is copied LAST so the converter's state and silver writes land after the byte copies; (3) a pull fire between R4c and R5 would write the old-form keys (the puller upload is R5).
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-4.
