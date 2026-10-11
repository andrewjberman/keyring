# TO MDPF_HEALGAP.TO-HG-t12 -- round 3 HG-t-12: the FWD-6 census re-swept against a fresh count, with the third honest answer
<to_id>MDPF_HEALGAP.TO-HG-t12</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~9</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-12` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-12`. FWD-6 (PRD v0.3): every scheduled data pull whose login is refreshed elsewhere has an answer. v0.3 admits a THIRD answer for a
pull whose login only a person can renew: `EXPOSED-MANUAL`, which must name the person's act and where that act is listed when owed.
The census must be counted against a FRESH count of every scheduled pull (round 2's 162 was stale against a live 164). Read-only.

**How to find the population (read-only):** scheduled EventBridge rules (`aws events list-rules`, ALL pages, every rule with a
`ScheduleExpression`) and EventBridge Scheduler schedules (`aws scheduler list-schedules`, ALL pages). Count them yourself and print the
count and the command as the `FRESH-COUNT` line; the `DENOMINATOR` is the number of scheduled pulls you read and it MUST equal the fresh
count (a schedule you read and excluded as no-vendor-login still counts in the denominator and is listed in section 3 of the document).
For each pull, read what credential or session it uses (Lambda env, code under `infra/aws/lambda/`, Terraform under `infra/aws/terraform/`,
`secretsmanager:DescribeSecret` -- NEVER `GetSecretValue`) and which other job refreshes that login. Use `comp-find` / `comp-which` for
code search (a recursive grep is denied by the rail). The prior census is `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md`:
read it first and re-verify, do not copy.

**Build:** NEW `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md` with:
1. `DENOMINATOR: <n> scheduled pulls read` and `FRESH-COUNT: <n> scheduled pulls via <the command and time>` (same n);
2. a markdown table with columns `pull | schedule | login kept alive by | answer | grounding | person's act | listed on`, the 49F login
   chain's pull FIRST; `answer` is exactly `RECOVERS`, `NOT-EXPOSED because <reason>` or `EXPOSED-MANUAL because <reason>`;
   `grounding` cites file:line or the read that decided it; `person's act` and `listed on` are filled for every `EXPOSED-MANUAL` row
   (the act: the person's re-login; `listed on`: the open-calls list, named as the place it is queued when owed -- you do NOT write to it);
3. a short list of the schedules you read and excluded (no vendor login), so the denominator is checkable.
Required rows by name: `schwab-canonical-si2-08403355-pull-daily` and `teams-global-transcripts-pull-hourly` (both unanswered in round 2),
`canonical-schwab-si2-08242234-daily-pull`, `canonical-schwab-si2-08335338-daily-pull`, `astn-wsjft-3am-run` (the SI2 and FT pulls are
marked with the third answer if no machine renews their login), `bd-asset-dim-pipeline-trigger` (answer `RECOVERS` is claimed ONLY by the
re-attempt of HG-t-11 once applied: today it reads `NOT-EXPOSED`/`EXPOSED` per what you read, state which) and `cot-rebalancer-runner`.

### ACCEPTANCE

<criterion id="HG3-t12-AC1" cell_refs="HG-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t12_census.py</invocation><expect>CENSUS-OK</expect></criterion>
`HG3-t12-AC1` -- the census has equal DENOMINATOR and FRESH-COUNT lines, the seven columns, a valid answer and grounding on every row, the person's act and where it is listed on every `EXPOSED-MANUAL` row, the seven named pulls, 49F first (completeness of the population is graded by the CVO).

<expected_criteria>HG3-t12-AC1</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base: `CENSUS-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Read-only AWS reads are allowed.
- **Never** call `secretsmanager:GetSecretValue`, never invoke a function, never call a vendor. 49 Financial data never enters another firm's tree.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W9-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line endings and check
  `git diff --stat` shows only your added lines before committing.

<paths>
org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, the enrichment), cell `HG-t-12`.
<owned_cells>HG-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG3-t12-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/MDPF_HEALGAP.TO-HG-t12.fwd6-census-resweep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t12-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the cell sweeps every schedule and prints that DENOMINATOR and the FRESH-COUNT in its document (AC1).
comp-iam: DECLARED-NOT-APPLICABLE read-only calls; no grant, no write.
comp-adversary: DECLARED-NOT-APPLICABLE read-only.
risk: LOCAL -- a document; read-only AWS calls; no write outside the deliverables folder.
direct_act: false -- a worker order (above the size floor).
</preflight>

Source: PRD v0.3 ADDENDUM and FWD-6; CTO round-2 analysis @1974b85f4e section 3 item 5 and section 2.1; batch @6c538a0bfd sections E and K.
