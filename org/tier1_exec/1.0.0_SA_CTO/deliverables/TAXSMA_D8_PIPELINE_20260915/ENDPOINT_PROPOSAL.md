# MDPF_TAXSMA: proposed endpoint for confirmation

Author: `1.0.0_SA_CTO~A`. Phase: L2 /endpoint --forward.
Status: **PROPOSED; Andrew's DONE WHEN confirmation pending.**
Placement proposal: D8 / MDPF / laptop. Registration and PRD authoring are already commissioned.

Input brief: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md`
generated: 2026-09-15
byte size: 16917
SHA-256: `db713efb61f69fc4b1c1988abdb9ee389d046bf53e5df4e97e3b878dd4366191`

The input incorporates the supplied COO brief, Andrew's D8 placement and his traded-versus-sales correction, after the live SharePoint and custodian research. This projection reads the completed L1 brief for its outcomes. Administrative placement/collision research was a separate preparatory act and did not define these outcomes.

PRD home: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md`
Section home: `ENDPOINT (step 2, /endpoint --forward)`
**NOT YET LANDED**: the PRD does not yet exist. The block below is ready to carry verbatim after confirmation. IDs are permanent once landed.

## ENDPOINT (step 2, /endpoint --forward)

**FWD-1 — Live Tax SMA accounts are clearly separated from prospects and untraded accounts.**

DONE WHEN: **EXERCISED** — a deliberate walkthrough demonstrates the membership distinction.

ACCEPT: An operator explains why each account belongs in the live group or stays outside it; a funded account that has not entered the strategy stays outside.

SOURCE: brief §I.O1, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:28`.

**FWD-2 — Workbook accounts can be reconciled to the intended Schwab accounts without guessing.**

DONE WHEN: **EXERCISED** — a controlled comparison demonstrates both matches and disagreements.

ACCEPT: An operator can follow each live account to its custodian record, see missing or conflicting matches, and review additional candidates without calling them live automatically.

SOURCE: brief §I.O2, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:32`.

**FWD-3 — Newly traded accounts and later status changes reach the whole data path.**

DONE WHEN: **EXERCISED** — a controlled activation and correction have been followed through to their results.

ACCEPT: An operator changes a controlled account case from pending to traded, then corrects it, and sees the right dated inclusion without manually patching the list of accounts being processed.

SOURCE: brief §I.O3, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:36`.

**FWD-4 — Daily Tax SMA assets have a consistent value and a traceable date.**

DONE WHEN: **EXERCISED** — a deliberate comparison demonstrates the value and its stated basis.

ACCEPT: An operator traces the reported assets back to the dated account values and can explain the treatment of cash and borrowing; sales estimates and old quarterly figures do not stand in for daily assets.

SOURCE: brief §I.O4, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:40`.

**FWD-5 — Incomplete or outdated information cannot look like a complete current total.**

DONE WHEN: **EXERCISED** — controlled missing and delayed information has demonstrated the visible limitation.

ACCEPT: A reader can tell when accounts or current values are missing, distinguish that from a true zero, and see the relevant date without mistaking a partial amount for the complete total.

SOURCE: brief §I.O5, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:44`.

**FWD-6 — Tax SMA assets add to 49 Financial and Global exactly once.**

DONE WHEN: **EXERCISED** — a controlled before-and-after comparison demonstrates the intended totals.

ACCEPT: A reader sees the Tax SMA amount included in its category and in both intended totals exactly once, with the Client amount and other firms unchanged.

SOURCE: brief §I.O6, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:48`.

**FWD-7 — Authorized operators can explain the result while private account information stays protected.**

DONE WHEN: **EXERCISED** — a deliberate review demonstrates traceability and the information boundary.

ACCEPT: An authorized operator can explain an inclusion, exclusion and exception from the supporting records, while the ordinary report reveals no client names or complete account numbers.

SOURCE: brief §I.O7, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:52`.

**FWD-8 — The pipeline runs reliably and can be recovered without duplicate contributions.**

DONE WHEN: **EXERCISED** — controlled failures, repeated runs and recovery have demonstrated the behavior.

ACCEPT: An operator deliberately causes a failed run, sees what failed, recovers it and repeats it; the result is correctly dated, includes no duplicate contribution and preserves existing reports.

SOURCE: brief §I.O8, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:56`.

## Provenance and flow position

NOT READ for Phase 0 outcome derivation: register, task orders, project JSON.

L1: commissioned brief written after the source audit. L2: this concrete proposal awaits confirmation of its DONE WHEN bars. L3: project registration follows the confirmed endpoint. L4: the CTO will close specification decisions in the PRD, then route independent L4-R reviews through the canonical notifier. No TO or deployment is issued by this proposal.

The confirmation is required by `.claude/skills/canonical-flow/SKILL.md`, through its authoritative spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L2: “Andrew confirms the `DONE WHEN` line of every outcome here”. It confirms the completion standard for this new project; it does not repeat permission to research, register or write the PRD. Earlier NFRA_OPLGTW approvals are not reused.
