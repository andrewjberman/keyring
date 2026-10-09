# AMGT_RESAPP -- ROUND 80, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 1680, `surprise-channel/adjudications/ADJUDICATION_v98.md` @741eb4a489 (4 of 4 terminal, real
run YES, no BLOCKING open), `REMEDIATION_v26.md` (4 rows), and the drain-end packet
`deliverables/2.0.0_SA_COO~R1/round80/DRAIN_END_PACKET.md`. This is the first analysis written on dell1.

## 1. Graded

- **FWD-1 (AMD): REALIZED on DEV.** Its DONE WHEN is met on portal DEV `8d2a08a92b5e` against the live API: the segment table is drawn
  equal to the served `segment_table` (CVO viewed capture 014). One defect sits on the page, not in this project: the filing panel
  under the table says "no segment breakdown is shown". That goes to DSGN_AMGTV1 (section 2, R4). A PROD release is an enrichment
  outcome, not the thread.
- **FWD-7: REALIZED on DEV.** 95 rows, stalest first, Lenovo flagged.
- **FWD-18 (ASML NA): NOT REALIZED.** dd-1 landed the extraction code. Its census reads **0 of 5** stored 20-F names carrying a business
  section, and 4 of 5 risk items came from the removed fallback heading. So the store half is owed for all five 20-F names, not only
  ASML NA.
- **R2 (citation headings): MET.** Served citations with a letterless heading read 0 of 271, against 4 of 271 before, on live `OUOsYXa`.
  41 of 1,122 STORED records still carry one. No reader serves them, so no cell is cut: the served path is the outcome.
- **FWD-16:** unchanged. It is held by Andrew (2026-09-15).

## 2. Rulings

- **R1, the store half runs on dell1, with PyMuPDF installed as box parity, not as a code change.** fetch and analyze fail to import on
  dell1 because `document.py:56` imports PyMuPDF at module top. Andrew-direct ~03:5xZ: dell1 is laid out like dell2 and handles its own
  needs. So the missing package is a box-layout gap for `0.0.0_AB_MSTR~DELL1`, and the tree is unchanged. That avoids a site-Z
  producer change and its half. Fallback, only if the install is refused: one lazy-import cell under `1.0.0_SA_CTO~Z`'s half.
- **R2, the store half's rollback writes no delete.** Each served key's rollback re-writes the prior version as the newest part. The
  prior VersionIds are named in the pair. A new silver part is superseded, never deleted. That keeps the act inside the pair and off
  the human-confirm list.
- **R3, the route resolves typed names.** Ruled @9e03417c14 (DSGN ledger `CTO_RULING_ROUND57_R1A_R6_20261009.md` ADDENDUM 1). One
  candidate resolves, several return the list, none keeps the 404. There is no coverage gate.
- **R4, the "no segment breakdown is shown" sentence is DSGN_AMGTV1's.** Where a served `segment_table` is drawn, the filing panel does
  not say the breakdown is absent. That is a round-58 item for `2.0.0_SA_COO~D1`, named in this file, with no cell here.
- **R5, rows routed to this seat:**
  - **D1-W317-S1** (walker disarm needs `ssm:DeleteParameter`, denied by design): the ui-walk skill's disarm proves dormancy without a
    delete, using the account disabled, the hash replaced and a read-only proof. The skill is a shared-branch file, so this goes to
    `0.0.0_AB_MSTR~DELL1` to carry to its owner. The parameter policy is unchanged.
  - **D1-S6** (`reconcile-deployed` writes no `artifact_sha256` for a no-record function; the harvest root's `CHANGELOG.json` is refused
    by the naming limb on two existing names): both are tooling owners' work, carried by `0.0.0_AB_MSTR~DELL1`. The naming refusal is a
    missing registry row under `infra/logic/registry/` (Rule 30), never a hand-typed workaround.

## 3. ENRICHMENT LIST (round 81, ONE issuance by `2.0.0_SA_COO~R1`)

1. **R1 store half, five 20-F names, ASML NA first** (row D1-S3): re-fetch, silver part, re-analysis, draft rebuild. It runs under a
   never-widen pair with no-delete rollback (R2), after PyMuPDF imports on dell1. Then a FWD-18 walk on ASML NA, whose stored text is
   read first and is the business section.
2. **The name-resolving route** (R3), with its three arms tested: one candidate, several, none.
3. **/freshness date form** (row D1-S1): the producer emits the house long form, or a structured date the page formats. Close: one
   served read shows a single date form.
4. FWD-16 waits on Andrew's hold.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Lifting his 2026-09-15 hold on the news collection's mechanism and cadence (FWD-16).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~04:3xZ) -- R1 changes to the fallback (`0.0.0_AB_MSTR~DELL1` msg 1692)

PyMuPDF 1.28.2 installs on dell1 but does not import. The box has no VC++ 2015-2022 x64 runtime (`msvcp140.dll`), and installing it
needs an elevated session, which only a person at dell1 can run. Round 81 does not wait on that:
- **Round 81 item 1 is preceded by ONE lazy-import cell:** `document.py` imports PyMuPDF only on the PDF path. The SEC `.htm` path
  imports without it. The negative arm: a PDF-path call without PyMuPDF raises a named error, never a silent skip. The path is a site-Z
  producer path, so the cell's deploy needs `1.0.0_SA_CTO~Z`'s never-widen half. The store half then runs on dell1.
- **The VC++ runtime install** is listed as an act for a person at dell1 (box parity with dell2, which `0.0.0_AB_MSTR~DELL1` is
  measuring). It is not a precondition for anything in round 81.
