# TO IRPT_BCKEND.TO-IB-pr-420 -- IB-pr-416's irpt-performance-adapter and irpt-narrative applied on lane ~IB2, source-map entries landed first

<to_id>IRPT_BCKEND.TO-IB-pr-420</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the pair: packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-416.md` (blob 43ea93d2ee); COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_416_THREE_FUNCTIONS_ONE_TREE_COO_HALF.md` @c362f7e0fb; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_416_THREE_FUNCTIONS_ONE_TREE_CTO_HALF.md` @d29ccddb17 (SIGNED, conditions 1-9; AMENDMENTS 1 and 2) | **Decomp cell:** `IB-pr-420` (decomposition section 111) | **outcome_ref:** FWD-2

---

## WORKER FACE

Apply TWO functions, in this order: `irpt-performance-adapter`, then `irpt-narrative`. **irpt-status is NOT in this order** (its apply is
`2.0.0_SA_COO~Y2`'s, TO-APPLY-Y1 AMENDMENT 8, after your adapter apply on the shared ops root). Read the packet and both halves in full
first. Run after IB-pr-413's landing work; its first-fire read may still be pending, the surfaces are disjoint.

| function | the only bytes that may land (CodeSha256) | expect live before | rollback S3 version |
|---|---|---|---|
| irpt-performance-adapter | `9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=` | `o/643qVECx5UU4Z9sknDp5yUJZb81Zfvp873yDNsc1w=` | `P2.k8l8dqM7nlKcd8O1.Hzo5ugCCceiR` |
| irpt-narrative | `x0SqAx2US8UXLnn7Xqy5l3Ttd0Iv1TZQ2jlxgCQtflU=` | `iEwSFL34JQJbihTmChB79GkjXwJaEl9WzMJY2sBEs4k=` | `Tuz7VAl4qh0fd6c_7OcSTNY.PRgBCsc3` |

Steps:
0. **Open-deploy read (CLAUDE.md NEVER-2), then the ledger.** Open ONE ledger entry naming all three functions of the pair (the two you
   apply and irpt-status as "not in this act, applied by 2.0.0_SA_COO~Y2"), and COMMIT the open and its sentinel before any upload.
1. **Source map first (condition 2; row D2-W278-S2).** In `infra/aws/lambda/ci/lambda-source-map.json`, replace the `functions` entries of
   `irpt-performance-adapter`, `irpt-narrative` and `irpt-status` with the same-named entries of
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/candidate_source_map.json` (its `functions` object only; none
   of its `_..._IB_pr_416` keys). Change no other key. ONE commit touching only that file. Send the issuer its hash at once:
   `2.0.0_SA_COO~Y2` pins irpt-status to it.
2. **Per function, precheck.** `get-function-configuration` CodeSha256 equals "expect live before", and the rollback S3 version is still
   present and still the latest. A moved version is a STOP and a row for that function only; the other function is unaffected.
3. **Per function, digest control (condition 1).** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <function>`
   prints the table's digest, or ABORT. Then the same without BUILD_ONLY, then the module's Terraform path through `safe-apply`
   (`s3_object_version` + `source_code_hash` only). Print the plan line by line; any line for another resource or function is a STOP.
   Never `aws lambda update-function-code`.
4. **Per function, the live-call arm within a minute of the promote (condition 6).**
   - adapter: one GET `/api/scoped/investor-reporting/performance/{accountSetId}` as a caller outside the 49F case;
   - narrative: one GET `/api/scoped/investor-reporting/narrative/{reportId}` as a firm user.
   Expect a typed answer: no 500, and 0 `TypeError` lines in the function's log group from the promote time on. A failure is Branch B
   at once.
5. **Close the ledger** and write
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB118-1_two_function_release_after_reads.json`:
   `{ledger:{state,slug}, source_map_commit, functions:[{function, built_sha256, live_before, rollback_version,
   build_only_digest_matched, rolled_back, live_call:{route, status, typeerror_lines, window_start}, widenings}]}`.
   No account id, balance or client figure goes in it: counts, sha256, status codes and reason codes only.

**Branch B.**
- adapter (condition 4): after a landed apply that reads a 500 or a `TypeError`, redeploy S3 version
  `P2.k8l8dqM7nlKcd8O1.Hzo5ugCCceiR` through the same Terraform path, after re-reading that it is still present. `5nyq8P6v` is a
  target on NO branch.
- narrative: redeploy S3 version `Tuz7VAl4qh0fd6c_7OcSTNY.PRgBCsc3` through the same Terraform path, re-read first.

**The CTO half's conditions, verbatim (section 4 and AMENDMENT 1 section A2).** Conditions 3 (second sentence), 5 and the irpt-status
part of 9 bind `2.0.0_SA_COO~Y2`'s apply, not this order; they are carried so you know what the pair holds.

1. **Digest control:** at apply, `BUILD_ONLY=1` prints the digest of section 1 for that function, or the applier ABORTS.
   This is the only control on the zips nobody outside the worker has read.
2. **Source map first:** the three candidate entries land in `infra/aws/lambda/ci/lambda-source-map.json` before any build
   (row D2-W278-S2).
3. **Order:** irpt-performance-adapter first. irpt-status does not start until IRPT_ANLREQ release 1's pair has cleared
   (2.0.0_SA_COO~Y2, TO-APPLY-Y1 AMENDMENT 8).
4. **Adapter Branch B is the COO half's, not the packet's:** after a landed apply that reads a 500 or a `TypeError`,
   redeploy S3 version `P2.k8l8dqM7nlKcd8O1.Hzo5ugCCceiR` through the same Terraform path, after re-reading that it is
   still present. That version fails closed on one operation, which is a better state than a function answering 500.
   `5nyq8P6v` is a target on no branch.
5. **The widening is exercised, both arms, in irpt-status's after-reads:** as `svc-custody-statement`, one
   `analysis-request-read` of a request owned by its own firm answers; one of a request owned by another firm is refused
   `NOT_AUTHORIZED`. If the subject cannot be driven in the sr1 window, the ledger records the widening as
   APPLIED, UNEXERCISED, and the close says so in those words.
6. **Per function:** a moved live version at the precheck is a STOP and a row for that function only. The live-call arm
   (one GET, typed answer, no 500, no `TypeError` in the log group) runs within a minute of each promote; a failure is
   Branch B at once. One ledger entry per act, opened and committed before the first upload, naming all three functions.
7. The apply comes by a new order of 2.0.0_SA_COO~P2 carrying these conditions verbatim.
8. **Reach read before each of the two applies:** the issuer prints, from the BUILT zip, the handlers reachable from that
   function's declared routes and the count of call sites among them that call `artifacts.put`, `retention.reserve` or an
   `ArtifactRepository.get` on `ANALYSIS_COMMENTARY`. Denominator printed (routes read, handlers walked). A count above 0
   is a STOP and comes back to this seat; 0 lets the apply proceed.
9. **The ledger close for the adapter and for irpt-status states both A1 widenings as APPLIED, UNEXERCISED on that
   function,** unless condition 8 found a reaching route and it was exercised on both arms.

**Condition 8, done by the issuer:** `deliverables/2.0.0_SA_COO~P2/checks/r118/REACH_READ_IB416_BUILT_ZIPS_20261011.txt`.
RULED by the CTO half AMENDMENT 2 (section A4, @d29ccddb17; msg 3980): a reached put, reserve or get that can carry
`ANALYSIS_COMMENTARY` counts, including a site whose family is caller-supplied; a literal other family does not.
- irpt-performance-adapter (digest re-hashed `9kYLdR64...`, equal): 1 route, 58 modules, 778 defs, 480 reached; references to
  `ANALYSIS_COMMENTARY` in reached code 0; the only callers of the repository's put / persist in the whole zip are `retained.py:321`
  (literal `PERFORMANCE_SOURCE_EVIDENCE`) and `retained.py:330` (literal `PERFORMANCE`); the inner reserves pass those through.
  **Count 0: the adapter proceeds.**
- irpt-narrative: 0 put, 0 persist, 0 reserve, 0 references. Neither A1 file is among its changed members.

**Condition 9, yours at the close:** the adapter's `widenings` field and the ledger close state, in these words, that
`svc-commentary on retention reserve (ANALYSIS_COMMENTARY)` and `svc-irpt-packager reading ANALYSIS_COMMENTARY` are
`APPLIED, UNEXERCISED` on irpt-performance-adapter, and that `analysis-request-read for svc-custody-statement` is packaged in both
functions with no route answering it there. irpt-narrative carries neither A1 widening.

<criterion id="IB118-1-AC1" cell_refs="IB-pr-420"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r118/p118_cells.py" . IB118-1-AC1</invocation><expect>IB118-1-AC1 PASS</expect></criterion>
<criterion id="IB118-1-AC2" cell_refs="IB-pr-420"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r118/p118_cells.py" . IB118-1-AC2</invocation><expect>IB118-1-AC2 PASS</expect></criterion>
<criterion id="IB118-1-AC3" cell_refs="IB-pr-420"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r118/p118_cells.py" . IB118-1-AC3</invocation><expect>IB118-1-AC3 PASS</expect></criterion>

<expected_criteria>IB118-1-AC1, IB118-1-AC2, IB118-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Two Lambda code packages and one source-map file. No IAM, route, schedule, layer,
  environment or table change; no other function.
- **No vendor call**, no monitor, alarm, SNS or SES.
- **Refusal clause:** STOP, file a row, and apply nothing more (Branch B if landed) on any of these: a moved live version; a digest
  miss; a plan line for another resource; a refused upload; a failed read-back; a live-call arm reading 500 or a `TypeError`. A function
  rolled back leaves its criterion FAIL; never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>`. Write the message file with the Write tool, OUTSIDE
  the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-420.adapter-and-narrative-one-tree-applied.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 111 (round 118, workstream ~P), cell `IB-pr-420`.
<owned_cells>IB-pr-420</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB118-1-AC1, IB118-1-AC2, IB118-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-420.adapter-and-narrative-one-tree-applied.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** report twice. After step 1: the source-map commit hash. After the close: per function the live CodeSha256, the live-call
status and TypeError count, whether it was rolled back, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two Lambda code packages (irpt-performance-adapter, irpt-narrative) and three source-map entries; 13 and 9 changed members; the adapter is failing closed on performance-report now (5 requests refused since 2026-10-09T15:41Z).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the live-call arm reads two existing routes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p118_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~03:1xZ: AC1 FAIL (entries differ), AC2 FAIL (adapter live == o/643qVE), AC3 FAIL (narrative live == iEwSFL34); commit-gate clean.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only.
</preflight>
