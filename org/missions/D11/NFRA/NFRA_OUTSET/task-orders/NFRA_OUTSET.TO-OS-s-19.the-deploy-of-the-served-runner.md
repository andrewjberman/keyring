# TO NFRA_OUTSET.TO-OS-s-19 -- THE DEPLOY: the single S3 upload that puts the runner the estate READS at HEAD's version

<to_id>NFRA_OUTSET.TO-OS-s-19</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-06</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.3** and the CTO's ROUND-1 ANALYSIS @`a0500abe18`. Decomposition v0.3. ⛔ SEQUENCED SECOND, BEHIND `OS-s-18`: that cell proves the seam is readable by the runner's own role and this one REPLACES the runner. Deploying first puts a new binary in front of a seam it cannot yet read, and grades OS-s-18 against a runner that changed underneath it.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.3 (s.7 row OS-s-19) · **Decomp cell:** `OS-s-19` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.3, s.7-s.10) · **outcome_ref:** FWD-2, FWD-4, FWD-7 · **verb:** deploy · **depends_on:** OS-s-11 (COMPLETE), and SEQUENCED behind OS-s-18

---

## THE CELL

`OS-s-19` (PRD s.7, evidence **absent**): the served runner is dated **2026-08-25** and the upload belongs to NO cell. Rows `S14`, `W1-S25`, `W1-S26`.

⛔ **THIS IS THE CELL THAT MAKES ROUND 1 REAL OR LEAVES IT ON PAPER.** Measured at the issuer's seat on a live `s3api` read: `s3://opal-estate-report/code/estate_report_runner.py`, 125,857 B, `LastModified Tue, 25 Aug 2026 05:36:35 GMT`, carrying **0** occurrences of `_outset_read`, `OUTSET_ANSWER_STATE_TO_STATUS` and `ESTATE_OUTSET_SEAM_PREFIX` against **4 / 3 / 5** at HEAD, with the positive control `_stratum(` at **11 served vs 15 at HEAD** proving it is the same program at an older vintage. ⚠ Two tokens quoted in `W1-S25` -- `rerun_recipe` and `tool_invocation` -- are zero at HEAD as well and discriminate NOTHING; do not reuse them (row `S14`).

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-deploy-of-the-served-runner.result.md` -- what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`.**
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium). **NEVER-AUTO-DELETE (PRD R-5) is absolute.**
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **THIS IS A NEVER-2 CELL AND THE LEDGER IS NOT OPTIONAL.** Open a change-management entry in `org/critical_paths/change_management/` BEFORE the upload and CLOSE it at completion. **NEVER leave a confirmed deploy half-landed** -- finish in-session or roll back and escalate loud. ⛔ **Before acting on ANY open or red entry you find, MEASURE THE ARTIFACT** (`head-object` plus a content diff against the pinned commit, with a positive control): an entry a device left OPEN proves only that THAT device saw no completion, and re-executing an overtaken promote is a REWIND. ⛔ **An IMAGE-class act names every consumer of what it moves** -- here the estate report is the single consumer and the daily 09:00 window is its schedule, so state plainly whether your upload lands inside or outside that window.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`.

<criterion id="O19-AC1" cell_refs="OS-s-19"><invocation>timeout 300 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os19_served_matches_head.py</invocation><expect>SERVED MATCHES HEAD</expect></criterion>
AMENDED 2026-09-09 ~13:4xZ BY THE ISSUER on row `NFRA_OUTSET-S18`, the same defect and the same remedy as OS-s-18's O18-AC1 (see that face's amendment note for the measured mechanism): the invocation PATH moves from `.tools/tests/` (lane TOOL_BATTERIES, no CloudOps member; a `<paths>` block grants only a `0.9.0_WK_*` serial) to this order's own deliverables folder (clause 4, the serial in the path, PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's own resolver run). `<expect>` unchanged. The `.tools/tests/` line in the `<paths>` block below is INERT for this seat and is left so the record shows what was cut. Ruled under this issuer's L6 authority; `1.0.0_SA_CTO` and `3.0.0_SA_CVO` told in the drive read.
`O19-AC1` -- a check you write, proving the SERVED bytes match the graded commit's: `head-object` for the vintage AND a CONTENT diff, never filename or timestamp alone (Rule 22a). ⛔ **Every token in a presence/absence census needs its OWN positive control -- a census of four tokens is four detectors, not one** (`W1-S27`). This criterion CANNOT pass before the upload; that is correct and is the point of the cell.

<criterion id="O19-AC2" cell_refs="OS-s-19" judgment="true"/>
`O19-AC2` -- THE LEDGER AND THE WINDOW: the change-management entry opened and closed, what you measured before acting, and whether the upload fell inside or outside the 09:00 window the report runs on. Evidence with vintage. NO VERDICT.

<expected_criteria>O19-AC1, O19-AC2</expected_criteria>

<paths>
infra/aws/ec2/estate-report-runner/
.tools/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **`org/critical_paths/change_management/` and `.open_deploys/` are granted BECAUSE THIS CELL CAN DEPLOY**, not because it edits them incidentally. A deploy cell whose order does not grant the ledger can do the work and cannot record it -- the same shape as round 1's `<paths>` omissions. ⛔ `infra/system/06_current_state.{json,md}` is deliberately NOT granted: the comp-system gate keys on `.tools/comp-` and `org/modules/graph/`, and `OS-s-14` measured `NOT_APPLICABLE` rc 0 on both arms for this same runner file. If it fires anyway, that is a CUT DEFECT and it is the issuer's.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.3, cell `OS-s-19`.
<owned_cells>OS-s-19</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-06 ~03:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 24.562 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report runner, the consumption seam or comp-heat. BLIND SPOT, stated because a denominator without one is half an answer: this lens reads the GATE LEDGER, so it can say no armed gate names these surfaces and it CANNOT say whether an S3 deploy or an IAM grant is otherwise constrained -- that is comp-iam's plane and is required separately below.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the same disposition OS-s-6 and OS-s-7 carried, where comp-iam was the subject of the work rather than a check on it. This issuer did not run it and does not claim to. THE ASSIGNEE MUST -- each reads or changes a live principal or resource. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use; the census carries a 24 h TTL and nothing refreshes it (measured 27 days stale once). Three false-deny modes are known and all three are live: a CONDITIONED grant, a batched multi-ARN call poisoning sibling verdicts, and a resource ARN at the WRONG GRAIN returning implicitDeny even for a `*`-on-`*` principal. Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: the `<paths>` block IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) while this order is NON-TERMINAL at HEAD, plus this seat's own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O19-AC1`, `O19-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-19.the-deploy-of-the-served-runner.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O19-AC1,O19-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED with "NO proof-of-spec instance was found beside it" while a valid instance sits on disk. Round 1 carried that defect on 16 of 17 faces (row `NFRA_OUTSET-S4`).
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order at HEAD): flip only when every MECHANICAL criterion PASSES and the instance validates rc=0. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, once, with per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so.
