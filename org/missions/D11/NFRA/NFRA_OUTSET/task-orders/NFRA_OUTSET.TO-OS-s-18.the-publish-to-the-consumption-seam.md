# TO NFRA_OUTSET.TO-OS-s-18 -- THE PUBLISH: an outset tool's artifact reaching the consumption seam, and the runner's role granted to read it

<to_id>NFRA_OUTSET.TO-OS-s-18</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-06</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.3** and the CTO's ROUND-1 ANALYSIS @`a0500abe18`, which directs "2.0.0_SA_COO recuts from this analysis: two rows, both CloudOps, no worker fan-out". Decomposition v0.3.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.3 (s.7 row OS-s-18) · **Decomp cell:** `OS-s-18` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.3, s.7-s.10) · **outcome_ref:** FWD-3 · **verb:** build · **depends_on:** OS-s-10 (COMPLETE)

---

## THE CELL

`OS-s-18` (PRD s.7, evidence **absent**): nothing publishes to the consumption seam, and the runner's role holds no grant on any seam prefix. Rows `W1-S19`, `W1-S20`, `W2-S15`.

⛔ **THIS CELL EXISTS BECAUSE ROUND 1 PASSED EVERY CRITERION AND CHANGED NOTHING THE ESTATE READS.** The seam was built by `OS-s-10` and defaulted OFF; `OS-s-9` and `OS-s-14` wired consumers to it. None can carry a signal because no producer publishes and the reader holds no grant. The CTO's analysis names the cause as the PRD's own s.3, which COSTED a publishing step and assigned it to an ACCEPTANCE LIMB rather than a manifest row: **naming a cost is not assigning it.** This row is that cost, placed.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-publish-to-the-consumption-seam.result.md` -- what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`.**
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium). **NEVER-AUTO-DELETE (PRD R-5) is absolute.**
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O18-AC1" cell_refs="OS-s-18"><invocation>timeout 300 python .tools/tests/test_os18_seam_readable.py</invocation><expect>OS18-SEAM-READABLE</expect></criterion>
`O18-AC1` -- a battery you write, proving the published artifact is READABLE AT THE SEAM BY THE RUNNER'S OWN ROLE and that a FAILED publish reads FAILED rather than as an absent section. ⛔ **Its RED arm is the one that matters: make the publish fail and show the report says FAILED.** An arm set that only proves the happy path cannot distinguish a working seam from a silent one, which is the exact defect `W2-S21` found -- 35,752 rows rendering as a confident zero with every control green.

<criterion id="O18-AC2" cell_refs="OS-s-18" judgment="true"/>
`O18-AC2` -- THE GRANT, on the APPLIED plane and not only the declared one: which principal can read the seam prefix, measured with `comp-iam` against a refreshed census, with the DESIRED (terraform) and APPLIED (`iam:GetRolePolicy`) readings stated separately. `W1-S19` measured the runner's role holds `s3:GetObject` on three prefixes plus one exact key and **nothing on the globgrph bucket**, read on both planes -- corroborate or correct that. Evidence with vintage. NO VERDICT.

<expected_criteria>O18-AC1, O18-AC2</expected_criteria>

<paths>
org/modules/heatmap/outset_seam.py
infra/aws/terraform/
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>
⛔ **`infra/system/06_current_state.{json,md}` is granted because the GATE requires it, not because the cell edits it** -- `safe-commit.sh:789` fires the comp-system gate on any pathspec matching `org/modules/graph/` or `.tools/comp-`, and BLOCKS at `:837` when the pair is stale. ⛔ **AND THE ORDERING IS MEASURED (`W1-S11`): `comp-system` REFUSES to compile from an uncommitted source**, so the regenerated pair CANNOT ride the same commit as the change that dirties it -- commit the source first, then regenerate against the LANDED source in a second commit. ⛔ **From a LINKED worktree the comp-system gate FAILS OPEN** (`W2-S12`): the PATH shim hard-codes the main workspace, so a worktree-local run and the shim disagree. Work in the main tree or run the worktree-local arm yourself and say which you used.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.3, cell `OS-s-18`.
<owned_cells>OS-s-18</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-06 ~03:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 24.562 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report runner, the consumption seam or comp-heat. BLIND SPOT, stated because a denominator without one is half an answer: this lens reads the GATE LEDGER, so it can say no armed gate names these surfaces and it CANNOT say whether an S3 deploy or an IAM grant is otherwise constrained -- that is comp-iam's plane and is required separately below.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the same disposition OS-s-6 and OS-s-7 carried, where comp-iam was the subject of the work rather than a check on it. This issuer did not run it and does not claim to. THE ASSIGNEE MUST -- each reads or changes a live principal or resource. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use; the census carries a 24 h TTL and nothing refreshes it (measured 27 days stale once). Three false-deny modes are known and all three are live: a CONDITIONED grant, a batched multi-ARN call poisoning sibling verdicts, and a resource ARN at the WRONG GRAIN returning implicitDeny even for a `*`-on-`*` principal. Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: the `<paths>` block IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) while this order is NON-TERMINAL at HEAD, plus this seat's own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O18-AC1`, `O18-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-18.the-publish-to-the-consumption-seam.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O18-AC1,O18-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED with "NO proof-of-spec instance was found beside it" while a valid instance sits on disk. Round 1 carried that defect on 16 of 17 faces (row `NFRA_OUTSET-S4`).
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order at HEAD): flip only when every MECHANICAL criterion PASSES and the instance validates rc=0. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, once, with per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it. Round 1 produced five issuer cut defects and every one was found this way.
