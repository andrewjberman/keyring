# TO MDPF_HEALGAP.TO-HG-t20 -- round 5 HG-t-20: the transcripts pull.tf header says the live rules are live (a comment-only correction)
<to_id>MDPF_HEALGAP.TO-HG-t20</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~17</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-20` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 5) |
**outcome_ref:** FWD-6 (D1-W14-S4), CTO round-4 analysis item 3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-20`. `infra/aws/terraform/transcripts/pull.tf` opens with a three-line header that says the file is "DESIRED ONLY: this file is planned, never
applied by the order that wrote it". That is stale: the Teams rule it declares, `teams-global-transcripts-pull-hourly`, is live and ENABLED, as is the
mail rule `outlook-global-transcripts-pull-daily` that `mail_pull.tf` (same root) declares (read live 2026-10-13 by worker `0.9.0_WK_MDPF_HEALGAP~14`:
`describe-rule` ENABLED, `cron(0 13-22 ? * MON-FRI *)` and `cron(30 23 * * ? *)`). The CTO ruled a COMMENT-ONLY correction (round-4 analysis section 2,
D1-W14-S4). You rewrite those first three comment lines (lines 1-3) so that the header: names both live rules, says they are live, carries the read
date `2026-10-13`, and no longer says `DESIRED ONLY` or `never applied`. Keep the rest of the header (lines 4 onward) as it is.

**Every other byte of the file stays: not one non-comment line changes**, so that a `terraform plan` in the root reads no change (the issuer runs it
at the drain). Do not add a line that is not a `#` comment; do not touch `mail_pull.tf` or any other file.

Suggested replacement for lines 1-3 (use your own words if you prefer, but keep ASCII only and satisfy the check):

```
# transcripts -- hop 1's CLOCK and the WRITER principal (NFRA_TRNSPT TR-i-1). LIVE: teams-global-transcripts-pull-hourly (declared here) and
# outlook-global-transcripts-pull-daily (declared in mail_pull.tf) are both ENABLED, read live 2026-10-13. The apply was a release act under
# CTO+COO halves with a change-management entry; this header was corrected by MDPF_HEALGAP round 5 (comment only, row D1-W14-S4).
```

### ACCEPTANCE

<criterion id="HG5-t20-AC1" cell_refs="HG-t-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_CHECKS/hg_t20_comment_only.py</invocation><expect>COMMENT-OK</expect></criterion>
`HG5-t20-AC1` -- every non-comment, non-blank line of `pull.tf` is identical, in order, to its base blob; the first 30 lines name both live rules, say they are live (the word `live` or `ENABLED`), carry `2026-10-13`, and no longer say `DESIRED ONLY` or `never applied`; the file is ASCII only.

<expected_criteria>HG5-t20-AC1</expected_criteria>

Run the invocation from the worktree root. It FAILS at the base (`COMMENT-BAD the header ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Comments only.** No `terraform init`, `plan` or `apply`, no AWS call that writes, no edit to any other file. The plan reading no change is the
  issuer's proof at the drain.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W17-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken the check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line endings and check
  `git diff --stat` shows only your changed comment lines (and the appended row, if any) before committing.

<paths>
infra/aws/terraform/transcripts/pull.tf
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 5, the enrichment), cell `HG-t-20`.
<owned_cells>HG-t-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG5-t20-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~17/MDPF_HEALGAP.TO-HG-t20.transcripts-pull-header-comment-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG5-t20-AC1 --governing-order <this order file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the lines changed (`git diff --stat`), the check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this order arms no gate and adds no schedule; it changes three comment lines.
comp-iam: DECLARED-NOT-APPLICABLE this order changes no role, grant or policy; it changes comments only.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-13 17:2xZ: 0 cited commits, 5 cited paths (1 GONE: the proof instance), 0 proof instances, 0 unproven dependencies. The check compares non-comment lines against the base blob ebabe8dad4 by content, so a hidden code edit reads BAD.
risk: WORLD -- a Terraform file of a live root (the floor its path implies); the change is comments only and its proof is a plan reading no change, run by the issuer.
direct_act: false -- the class is WORLD.
</preflight>

Source: CTO round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` section 2 (D1-W14-S4) and section 3 item 3, msg 4962; row D1-W14-S4; decomposition round 5.
