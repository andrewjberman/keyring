# Y-5 packet 2 (the Kimi web-search swap) -- SUPERSEDED

Ruling: `1.0.0_SA_CTO~DELL2` msg 120, 2026-10-07 08:15Z. It cites the brief
`docs/briefs/irpt-check-swap-ai-autosuggest-ux-brief-20261007.md` @3d0ecacb0b, section 4.1.

- Superseded by IRPT_YCDGEN S32 (FWD-16): the swap candidates come from etf-classifications, and the model ranks or words
  them but never invents one.
- Why: kimi-k3 rejects the tool echo (the QA in this folder, 9 runs), and CTO batch 218 ruled the catalogue-first
  direction.
- The check and swap UI changes (R1-R9) go to IRPT_YCDGEN as a PRD addendum, not to IRPT_BCKEND workstream Y.

Marked by `2.0.0_SA_COO~Y2`. The QA receipts in this folder are kept as evidence.
