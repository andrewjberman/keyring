# TO MDPF_HEALGAP.TO-HG-t17 -- round 4 HG-t-17: each of the seven EXPOSED-MANUAL pulls gets a re-attempt or a named reason
<to_id>MDPF_HEALGAP.TO-HG-t17</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~14</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-17` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-17`. FWD-6 asks that no scheduled pull stays exposed to a lapsed login without an answer. The round-3 census
(`org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md`) read 164 scheduled pulls and graded seven
of them EXPOSED-MANUAL. The CTO's round-3 analysis (item 3) asks that each of the seven gets a re-attempt or a named reason why none is needed.
Your product is ONE markdown document, `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md`,
with ONE table row per pull. You read code and the census; you change no code and make no AWS write.

**The seven pulls (the first table cell of each row is EXACTLY this key, in backticks or not):**

| key | the census row | the code the census cites |
|---|---|---|
| `outlook-global-transcripts-pull-daily` | outlook transcripts pull (gateway mail bearer, gateway Microsoft sign-in) | `infra/aws/lambda/transcripts-pull/mail_handler.py` |
| `teams-global-transcripts-pull-hourly` | Teams transcripts pull (same gateway sign-in) | the files the census row cites (`pull.tf` and the Lambda's transport); find them from that row, they are not repeated here |
| `schwab-canonical-si2-08403355-pull-daily` | SDD master 08403355 | `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` |
| `canonical-schwab-si2-08242234-daily-pull` | SDD master 08242234 | same |
| `canonical-schwab-si2-08335338-daily-pull` | SDD master 08335338 | same |
| `astn-wsjft-3am-run` | ASTN WSJ/FT digest, the FT leg | `tools/astn_wsjft/scripts/run.py`, `tools/astn_wsjft/ARCHITECTURE.md` |
| `bd-asset-dim-pipeline-trigger` | Black Diamond asset-dim pull | `infra/aws/ssm/opal-bd-asset-dim-download.json`, `infra/aws/terraform/bd-pipeline/eventbridge.tf` |

**Where the answers are already half-written.** Section 3 of the census gives, for each row, the evidence, the person's act that renews the login
and where that act is listed when owed. Re-read each cited line at HEAD (the census is a read from 2026-10-11) and say if it still holds.

**The three dispositions (exactly one token per row, written in capitals):**
- `RE-ATTEMPT-BUILT`: a machine re-attempt for this pull exists and is live. ONLY `bd-asset-dim-pipeline-trigger` can carry it: the rule
  `blackdiamond-49f-asset-dim-reattempt-daily` (`cron(40 22 ? * MON-FRI *)`, added by HG-t-11, guard `hg_guard.py` in the SSM document). Cite the
  `.tf` rule block and the guard lines in the document; a read-only `aws events describe-rule --name blackdiamond-49f-asset-dim-reattempt-daily`
  is allowed and its output pasted into the row's because-cell is welcome.
- `RE-ATTEMPT-DESIGNED`: the right answer is a machine re-attempt that no cell builds yet. Write the design in the row: the rule time and why that
  time, the guard that makes a complete day a no-op, and the one place the login is read. You build nothing.
- `NAMED-REASON`: none is needed because the renewal is a PERSON's act that no scheduled re-attempt can perform and the pull refills itself once
  the person has acted (a catch-up window, a lookback, a skip-if-landed). The row must say the word `person`, name the act, name the place it is
  `listed` when owed (the census's "where listed" column; if it still has no file path, say so and cite the surprise row `MDPF_HEALGAP-D1-W9-S4`),
  and cite the line that shows the pull refills after the act.

**The row format (one markdown table, header row first; the key is the FIRST cell, the token appears once in the row):**

```
| pull | disposition | because (with at least one path:line that exists) |
|---|---|---|
| `astn-wsjft-3am-run` | NAMED-REASON | the FT cookie is re-harvested by a person running harvest_ft_session; the act is listed on the open-calls list of 1.0.0_SA_CTO when owed; a failed fetch is a warning and the next 3 AM run reads the new cookie (tools/astn_wsjft/scripts/run.py:53) |
```

That row is a SHAPE, not an answer: write each row from what you read. A `path:line` citation must name a file in this repository and a line
number inside it; a citation that does not resolve fails the check.

### ACCEPTANCE

<criterion id="HG4-t17-AC1" cell_refs="HG-t-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/hg_t17_dispositions.py</invocation><expect>DISP-OK 7 rows</expect></criterion>
`HG4-t17-AC1` -- the document carries exactly seven disposition rows, one per named pull, each with exactly one of the three tokens, a because-clause of at least 40 characters besides its citations, at least one `path:line` that resolves in the repository, no TBD, `RE-ATTEMPT-BUILT` only on the asset-dim row, and `person` and `listed` in every `NAMED-REASON` row.

<expected_criteria>HG4-t17-AC1</expected_criteria>

Run the invocation from the worktree root. It FAILS at the base (`DISP-BAD no document at ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only.** No AWS write, no Lambda invoke, no vendor call, no `terraform`, no secret read (`GetSecretValue`), no edit to any code or
  config. Read-only AWS describes and lists are allowed where a row needs one.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium). A `RE-ATTEMPT-DESIGNED` row is a design written
  in a document, not a build.
- **Honest rows.** If a cited line no longer says what the census says it says, write that in the row and file a surprise row; do not copy the
  census forward. If you cannot tell which disposition fits, choose `NAMED-REASON` only when the pull genuinely refills after a person's act; a
  pull that does not refill is `RE-ATTEMPT-DESIGNED`, with the design.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W14-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line endings and check
  `git diff --stat` shows only your added lines before committing.

<paths>
org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 4, the enrichment), cell `HG-t-17`.
<owned_cells>HG-t-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG4-t17-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/MDPF_HEALGAP.TO-HG-t17.fwd6-seven-pull-dispositions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG4-t17-AC1 --governing-order <this order file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the document path, the check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this order arms no gate and adds no schedule; it is a read-only document.
comp-iam: DECLARED-NOT-APPLICABLE this order changes no role, grant or policy; it reads code and the round-3 census.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-13 14:14Z: 0 cited commits, 10 cited paths (2 GONE: the deliverable and the proof instance, both written by the worker), 1 file:line cite, 0 proof instances, 0 unproven dependencies. The census rows are a 2026-10-11 read; the worker re-reads each cited line at HEAD and says if it no longer holds.
risk: LOCAL -- a document under a deliverables folder; no code, config or AWS write.
direct_act: false -- a document cell with a seven-row read of code across several pipelines is above the direct-act size floor; the full limbs run.
</preflight>

Source: CTO round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` section 3 item 3, ADDENDUM 1; the round-3 census (HG-t-12) section 3; PRD v0.3 FWD-6; decomposition round 4.
