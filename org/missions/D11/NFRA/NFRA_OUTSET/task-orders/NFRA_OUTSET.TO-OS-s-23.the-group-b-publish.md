# TO NFRA_OUTSET.TO-OS-s-23 -- THE GROUP-B PUBLISH: `comp_fedobs_coevolution.json` derived and published to the seam as a second artifact on the cloud-side publisher's fire

<to_id>NFRA_OUTSET.TO-OS-s-23</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.6** @`be662c311f` (mid-round addendum on the S24 ruling @`5f39f3a512`, on Andrew's 2026-09-03 scope-change word), s.7 row OS-s-23; decomposition v0.6 s.23-s.26. BUILDABLE NOW on the publisher OS-s-21 built; its ACCEPT reads on a served day after that publisher fires with both artifacts.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.6 (s.7 row OS-s-23) · **Decomp cell:** `OS-s-23` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.6, s.23-s.26) · **outcome_ref:** FWD-3 · **verb:** build · **depends_on:** OS-s-21 (the cloud-side publisher @`9ba4fdd9e9` and its role; the Put widened to the group-B key ONLY, one read line on the CSE log's location), OS-s-20 (DONE on the act @`2686fc81d6`)

---

## THE CELL

`OS-s-23` (PRD s.7, evidence **absent**): neither group-B key has a producer (W2-S15). With the seam prefix configured under OS-s-20, `_stratum_cochange` walks `OUTSET_GROUP_B_SOURCES` (`comp_cochange.json`, then `comp_fedobs_coevolution.json`), only absence advances, and when every source is absent it returns `INSTRUMENT_FAILED` BY CONTRACT (`estate_report_runner.py:1424-1436`: "a prefix IS configured, so a publish was expected ... never a silent fall-through to the host stand-in"). Row `S24`: the same variable that turned group A ON turned group B's declared stand-in OFF, and 2026-09-10's served report renders B as FAILED. **That FAILED is the honest interim by the CTO's ruling (1): no revert of the switch, no stand-in re-enabled, no ceiling raised.** This row is what changes it.

⛔ **THE MECHANISM, AS THE RULING SHARPENED IT -- DERIVED, NOT COPIED.** The seam artifact is `outset/comp_fedobs_coevolution.json` at FILE-PAIR grain from the CSE log (the runner's own reproduce line names its producer, `comp-fedobs coevolution --json`, published through `org/modules/heatmap/outset_seam.py`), the artifact OS-s-14 already built the consumer for. The fedobs nightly (`emit_fedobs_snap.py`) writes a STAGED HEALTH SNAPSHOT to the globgrph bucket -- a DIFFERENT artifact at a DIFFERENT grain. **A copy of a served artifact to a second key is the duplicate output path CLAUDE.md s.5 forbids; a change to the fedobs ECS producer or its shared image is an image act under R13. Neither is this cell.** The producer is THE PUBLISHER OS-s-21 ALREADY BUILT: CodeBuild on a blobless clone under the minimum-Put role, a SECOND artifact on the SAME fire, after the fedobs nightly (04:30Z) and before the 13:00Z run; `comp-fedobs coevolution` reads the CSE log from the cloud, so it is clone-invariant like freshness.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-group-b-publish.result.md` -- what you measured, what you built, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`). The push gate on the publisher's fire is CARDED to `0.0.0_AB_MSTR` for Andrew (LD-0522); the S3-sourced entrypoint (Rule 12's shape) is your design call under TO-OS-s-21 and removes it for both publishers.
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`.**
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium; a pipeline trigger is not a monitor). **NEVER-AUTO-DELETE (PRD R-5) is absolute**: the R2 probe and the OS-s-22 probe stay where they are.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **WRITES EXACTLY ONE MORE KEY**: `outset/comp_fedobs_coevolution.json`, through `publish_artifact`. The publisher's role gains `s3:PutObject` on THAT key only (`iam.tf` under `safe-apply`; the applied reach re-read after) and one read line on the CSE log's location. The freshness key, the drift keys, the two probes: untouched. `org/modules/heatmap/outset_seam.py` is READ, never edited (lane NFRA_HEATMAP; a needed change is a BLOCKING row).

⛔ **THE SEARCH ORDER STAYS.** `OUTSET_GROUP_B_SOURCES` reads the resource-grain key (`comp_cochange.json`) first; W2-S15, its producer, is a LATER row the ruling names and does not cut. This cell publishes the second source and changes no consumer code (OS-s-22 owns the consumer's deploy).

⛔ **THE TRIGGER IS THE PUBLISHER'S OWN SCHEDULE, and a failed nightly is convicted honestly**: a failed fedobs nightly leaves a stale CSE-log vintage on the derived artifact and the consumer's ceiling convicts it; never success-of-upstream as the trigger, never a watcher on the nightly.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O23-AC1" cell_refs="OS-s-23"><invocation>timeout 300 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os23_group_b_publish.py</invocation><expect>OS23-GROUP-B-PUBLISHED</expect></criterion>
`O23-AC1` -- a battery you write, proving THE ACCEPT AS THE PRD WRITES IT on a SERVED DAY: group B renders FROM THE SEAM ARTIFACT with its grain disclosed (`[grain=file-pair, NOT resource-grain]`, the runner's own line) and a NON-ZERO row count EQUAL to the artifact's row count read independently (W2-S21's lesson as the control: the artifact re-downloaded and its rows counted by a second reader, never the report's own number), the artifact's vintage inside the ceiling AND later than that day's fedobs nightly (04:30Z). ⛔ **THE NEGATIVE ARMS**: with the publish disabled (a real day before this row landed, or the R5-style stale mutant) the stratum reads `INSTRUMENT_FAILED` by contract, NEVER the stand-in; OUT-OF-CORPUS printed if the CSE log the tool read was empty (a zero over an empty population is refused, not rendered QUIET). The artifact must be DERIVED (its `answer_state`, denominators and producer recipe name `comp-fedobs coevolution`), never a byte-copy of the nightly's snapshot (an arm asserts the two differ in schema and grain). **This criterion CANNOT pass before the publisher fires with both artifacts and a scheduled 13:00Z run reads them; that is correct.**

<criterion id="O23-AC2" cell_refs="OS-s-23" judgment="true"/>
`O23-AC2` -- THE SECOND ARTIFACT ON THE SAME FIRE: how the publisher derives it (the read line on the CSE log, the tool invocation, the publish path), the role's Put reach on exactly the one key read on the APPLIED plane before and after the grant, the fire's ordering against the fedobs nightly and the 13:00Z run, and what a failed nightly renders. Evidence with vintage. NO VERDICT.

<expected_criteria>O23-AC1, O23-AC2</expected_criteria>

<paths>
infra/aws/terraform/estate-report/
infra/aws/lambda/estate-report-orchestrator/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat on this round's census (the terraform module where the publisher and its role live, the orchestrator Lambda, both ledger folders, this deliverables folder by clause 4, the channel by lane ANY). Your battery lives in your deliverables folder. The publisher's entrypoint lives where OS-s-21 put it under `infra/aws/terraform/estate-report/`; if the S3-sourced shape moves it, say so in a row.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.6, cell `OS-s-23`.
<owned_cells>OS-s-23</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~15:5xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 26.594 s of a 90 s default. GATES ARMED: 26 (one more than the 15:3xZ run; the new sentinel is the D12 SMS filing's ledger entry, not this project's). REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=335. ZERO of the 26 armed gates names NFRA_OUTSET, the estate-report host or runner, the consumption seam, comp-heat or fedobs (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot say whether a Put grant or a CodeBuild change is otherwise constrained -- comp-iam's plane, required of the assignee below.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the publisher role's `s3:PutObject` reach is read on the APPLIED plane before and after the one-key widening, and the CSE log's read reach likewise. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use (24 h TTL). FOUR false-deny modes are live (a CONDITIONED grant, a batched multi-ARN call, a WRONG-GRAIN resource ARN, and the census's role-only reach per S20). Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat, plus this seat's own deliverables folder by clause 4.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O23-AC1`, `O23-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-23.the-group-b-publish.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O23-AC1,O23-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when the MECHANICAL criterion PASSES on a SERVED DAY and the instance validates rc=0. The build lands when the publisher carries the second artifact; the flip waits for the served day. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the second artifact is built into the publisher and its grant applied (the act; the accept still pending the served day), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
