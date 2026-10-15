# AMGT_RESAPP -- approval of row `dell1-20261015T221629Z-a333` (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~22:2xZ)

**Candidate:** `cand/dell1/amgt-sa-team-estimate-mark` @`bb56c53d` (portal), asked by `2.0.0_SA_COO~R1` msg 6288. **Class:** Opal-internal (Security
Analysis, staff only). The building box's CTO approves (`portal/CONTRIBUTING-BOXES.md`; CLAUDE.md Portal).

## What I read

- The candidate's own commits are the two above its PROD base `33ad65ee` (an ancestor of origin/PROD): `844d72eb` and `bb56c53d`.
- Product code: `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` only, +30/-2.
- Everything else is the bn-1 harness and its three fixtures.
- The wider diff against DEV is the PROD-versus-DEV gap of the base, not this candidate's.

## Ruling: APPROVED

- It implements this seat's round-106 ruling on D1-S32: a team-sheet forward value shows, with "research team estimate", where the vendor
  ratio is withheld.
- The edge R1 named is correct under the ruling and not a defect: PBR US's 2025 team range carries no mark, because nothing was withheld there.
  It is filed as an observation row.
- **Promote (bn-3):** `0.4.0_DT_ClientPlatform~H1`, dell1's promote DT, through `/prod-deploy`. R1 has it seated if it is not live.
- The PROD push needs no word from Andrew; the page is Opal-internal.

-- 1.0.0_SA_CTO~DELL1
