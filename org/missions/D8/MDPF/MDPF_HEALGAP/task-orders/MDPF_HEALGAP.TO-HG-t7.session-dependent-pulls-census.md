# TO MDPF_HEALGAP.TO-HG-t7 -- round 2 HG-t-7: every other scheduled pull that leans on a login kept alive elsewhere, answered
<to_id>MDPF_HEALGAP.TO-HG-t7</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~6</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-7` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-7`. FWD-6: the owner of the data estate has a list of every scheduled data pull whose success depends on a vendor login kept alive
by something else, each marked `RECOVERS` (recovers the same way FWD-1 now does) or `NOT-EXPOSED because ...`; a pull left without an
answer fails. The 49F login chain first; no claim that it is exposed until read.

**How to find the population (read-only):** scheduled EventBridge rules (`aws events list-rules`, all pages) and EventBridge Scheduler
schedules (`aws scheduler list-schedules`, all pages) whose targets run a data pull; for each, read what credential or session it uses
(Lambda env / code under `infra/aws/lambda/`, Terraform under `infra/aws/terraform/`, `secretsmanager:DescribeSecret` -- NEVER
`GetSecretValue`) and which other job refreshes that login. Use `comp-which` / `comp-find` for code search. Print the count of schedules
you read as the denominator.

**Build:** NEW `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md` with:
1. a line `DENOMINATOR: <n> scheduled pulls read` (every schedule you swept, exposed or not), and how you swept (commands, time);
2. a markdown table with columns `pull | schedule | login kept alive by | answer | grounding`, the 49F login chain's pull(s) FIRST and a
   row for `cot-rebalancer-runner`; `answer` is exactly `RECOVERS` or `NOT-EXPOSED because <reason>`; `grounding` cites the file:line or
   the read that decided it;
3. a short list of the schedules you read and excluded (no vendor login), so the denominator is checkable.

### ACCEPTANCE

<criterion id="HG2-t7-AC1" cell_refs="HG-t-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t7_census.py</invocation><expect>CENSUS-OK</expect></criterion>
`HG2-t7-AC1` -- the census has its denominator, the five columns, an answer and grounding on every row, 49F first and the Cottonwood runner present (completeness of the population is graded by the CVO).

<expected_criteria>HG2-t7-AC1</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base: `CENSUS-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every deploy and apply is the
  issuer's, at the drain. Read-only AWS reads are allowed where a criterion names them.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W6-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row.
- Never call `secretsmanager:GetSecretValue`, never invoke a function, never call a vendor.

<paths>
org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `HG-t-7`.
<owned_cells>HG-t-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG2-t7-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/MDPF_HEALGAP.TO-HG-t7.session-dependent-pulls-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG2-t7-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the cell itself sweeps every schedule and prints that DENOMINATOR in its document (AC1).
comp-iam: DECLARED-NOT-APPLICABLE read-only calls; no grant, no write.
comp-adversary: DECLARED-NOT-APPLICABLE read-only.
risk: LOCAL -- a document; read-only AWS calls; no write outside the deliverables folder.
direct_act: false -- a worker order (above the size floor).
</preflight>

Source: PRD v0.2 ENDPOINT FWD-6; CTO round-1 analysis @475c742f71 section 3; decomposition round 2.
