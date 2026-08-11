# Paste-ready handoff block: 49F Group A/B/C/D specs -> 4.0.0_SA_CRO~A (adversarial review + INF/COT derivation)

Authored by 3.0.0_SA_CVO at Andrew's direct ask (mid-session ~0726Z), for Andrew to send verbatim.

---

TO 4.0.0_SA_CRO~A — TWO COMMISSIONS ON THE 49F GROUP A/B/C/D SPECS (from Andrew, via the CVO's handoff block)

THE OBJECT: four sequential design specs for the 49 Financial gold analytics runner — the archetype all future firm runners instantiate (shape-transposition doctrine @6e180df78e). Authored by 3.0.0_SA_CVO under commission @5e4b8dda98, each reviewed by 1.0.0_SA_CTO with amendments folded same-window. You are attacking the RULED state (specs + folded amendments), not pre-review drafts.

THE FOUR SPEC FILES (all under C:\Users\AndrewBerman\Desktop\ajb_workspace\):
- Group A (dimensions/reference/boundary): org\tier1_exec\3.0.0_SA_CVO\deliverables\SPEC_49F_GROUP_A_DIMENSIONS_20260811.md — @9c294bbf15, amended @6fba62393b (calendar = JOIN of lib/trading_calendar.py x partition tree, never a second authority)
- Group B (holdings/valuation canonicals): org\tier1_exec\3.0.0_SA_CVO\deliverables\SPEC_49F_GROUP_B_VALUATION_20260811.md — @d57bbf7229, amended @39c41163cd (1bp tolerance ex-ante-provisional w/ ruled recalibration; accrual-if-material = atom-8 named computation)
- Group C (flow ledger / GIPS TWR engine / validation / lineage): org\tier1_exec\3.0.0_SA_CVO\deliverables\SPEC_49F_GROUP_C_TWR_ENGINE_20260811.md — amended @f882b91ce2 (debit_credit semantic-boundary verification at build; anomaly-threshold ruled-recalibration)
- Group D (serving up to the emitters, SHAPE-FROZEN): org\tier1_exec\3.0.0_SA_CVO\deliverables\SPEC_49F_GROUP_D_SERVING_20260811.md — @1e11389af8

CTO REVIEW RECORDS (the rulings the specs now embed): inbox messages 071857Z (A: approved + calendar amendment), 072235Z (B: approved + three qualifiers), 072553Z (C: approved + the debit_credit amendment), 072915Z (D: approved, no amendment — the census-staleness window closed by the acceptance design) — in org\mcp\inbox\3.0.0_SA_CVO\read\. All four groups APPROVED; CTO routes the whole-sequence ratification ask to Andrew separately.

GOVERNING LAW: the GIPS standard FILE C:\Users\AndrewBerman\Desktop\GIPS_TWR_Reconstruction_Standard.rtf (requirements verbatim — the spec IS this document) · pattern spec v1.0 @d272021791 (9 atoms + the 5-member must-calculate exception set) · shape-transposition @6e180df78e (MANUFACTURABLE = named computation + verified raw inputs, else refuse) · commission @5e4b8dda98.

THE SUBSTRATE (your own seat's work, which the specs bind to):
- org\tier1_exec\4.0.0_SA_CRO\deliverables\GIPS_TWR_FEASIBILITY_ATOMDECOMP_20260811.md @e323c1cfac (DAILY-TWR verdict; the 5 refinement cells)
- org\tier1_exec\4.0.0_SA_CRO\deliverables\SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.{json,md} @a876ee6ae9 (187 codes / 2.98M rows; materiality CLEARED)
- org\tier1_exec\4.0.0_SA_CRO\deliverables\PAIR_MATCHING_AND_FEE_SPECIMEN_20260811.md @5bb3b2626d + org\tier1_exec\4.0.0_SA_CRO\scripts\pair_match_engine.py (fee family VERIFIED; the FRM-leg collection-account boundary discriminator; the IC debit_credit=POSITION-SIDE trap)
- Run records DIR: workflows\atom_decomposition\runs\ (gips-twr-schwab-feasibility\20260811T0635Z + advi-model-holdings-account-join\20260811T0530Z + opal-data-mdpf-colocation\20260811T0440Z)
- The silver estate: s3://opal-data-assets/schwab/08335338/silver/ (20 tables; 08335338 = the ADVI account, NEVER 08242234/MDPF — write the full 8 digits)
- The existing runner corpus (quality-partition input): data\assets\scripts\gold\runners_49f\ (a00/a01 + c00-c04 + fit harness)
- Transposition seed you already authored: org\tier1_exec\4.0.0_SA_CRO\deliverables\GIPS_TRANSPOSITION_INF_COT_20260811.md
- RECON-4 (identity legs, all three firms): org\tier1_exec\4.0.0_SA_CRO\deliverables\RECON4_GOAL3_JOIN_FEASIBILITY_20260811.md (49F map-path 99.65% end-to-end; INF native-key 100.0% real-account; COT fact_model_assignment account-grain)

COMMISSION 1 — ADVERSARIAL REVIEW of the four specs, the standing discipline (@3c8418e34b applied in reverse: the certifier's own work gets the cross-examination). Attack the load-bearing cells against live state, not the specs' citations. The seams the author would attack first, offered so you start where it hurts: (a) Group A's product-root default (mints portal/gold/advi/49financial — is atom-1 conformance worth the two-home transition window?); (b) D_00's three-leg census — is the deployed-FE-bundle leg actually extractable for every surface (comp-cache's coverage is the load-bearing assumption); (c) B_02's materiality gate — the 112-asset rate-bearing predicate rests on interest_rate-nonzero, itself a CRO instrument correction; (d) C_00's EXTERNAL-BY-DEFAULT on unmatched pairs — conservative per the standard, but it prices the residual INTO returns (quantify the r(t) sensitivity of the $204.3M unmatched class before accepting); (e) every place a spec says a number from your deliverables — re-derive, don't trust the relay.

COMMISSION 2 — DERIVE THE INFLECTION + COTTONWOOD SPECS from the archetype, per @6e180df78e: same A/B/C/D shape, the two pattern parameters swapped ({scope} and the intermediate-plane fan-out), A-layer sources per firm (INF: Orion — your INF_ATOMDECOMP substrate incl. the TWR dim already landing daily; COT: Black Diamond Rebalancer — the three-tier ingest measured live in the RECON-4 addendum, relationship-grain collapse discipline per Andrew 08-04). Per-firm constituent-field sourcing verdicts (RAW / MANUFACTURABLE / ABSENT-with-shape) with the MANUFACTURABLE bar: named computation + verified raw inputs, else the cell refuses. The D-group census discipline transposes verbatim: each firm's served surfaces get their own deployed-FE byte-schema census before any emitter is specced.

Sequencing note from the CVO seat: certification of anything built from these specs returns to 3.0.0_SA_CVO by Rule 14e; your derived INF/COT specs land in the same review protocol (CTO per group).

---
-- 3.0.0_SA_CVO
