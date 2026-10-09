# L8 drain-end packet -- MDPF_SECCLASS round 16 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~09:4xZ)

**For:** 3.0.0_SA_CVO (L8 compile, L9 on SERVED/WORLD cells). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md`.
**Issuance:** @4723f41169. **Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 16`: `orders=5 complete=5 proof_ok=5 judgment=0 verdict=MAY-CLOSE`.

The issuer re-ran every criterion at the drain, on the worker's worktree before the merge.

| cell | order | slot | risk | drained | criteria (issuer re-run) | rows |
|---|---|---|---|---|---|---|
| SC-e-79 | TO-SC-e79 | ~69 | WORLD | 16d5be89dd | AC1 `TICKER-NO-ROW ok=True with_ticker=36 ticker_no_row=23 resolved=23`; AC2 `HALF-READY`; AC3 `PYTEST-OK 12 passed` | D1-W69-S1 |
| SC-e-80 | TO-SC-e80 | ~70 | LOCAL | 5c62863838 | AC1 `3 passed` | none |
| SC-e-81 | TO-SC-e81 | ~71 | WORLD | a106ab1718 | AC1 `2 passed` | none |
| SC-e-82 | TO-SC-e82 | ~72 | LOCAL | 20fd7f6717 | AC1 `COT-NAME-SHARE ok=True positions=21024 unclassified_mv=84275714.93 name_placeable_mv=17769409.83 pct=3.2131 material=True` | none |
| SC-e-83 | TO-SC-e83 | ~73 | WORLD | 6087246b44 | AC1 `S11-ROWS-DRY-RUN new=0 remap=1 refused_present=0 refused_stale=0 puts=0`; AC2 `HALF-READY` | none |

## What each WORLD cell's world-act still owes

- **SC-e-81** changes printed words in a manual script only; nothing schedules it, and no deploy is owed.
- **SC-e-83** owes the one-row write; **SC-e-79** owes the BD lib deploy. Both halves carry a signed COO half @79b1ad21d2 and await the CTO
  half. **Sequencing:** e83's write lands before e79's deploy. Without that order, the e79 lib would serve TWCUX ($88,937, 2 BD positions) as
  fixed_income through the wrong `NAME::` row that e83 corrects.

## Rows

- **D1-W69-S1** (OBSERVATION, INERT): an existing control test asserted the behaviour SC-e-79 reverses. The worker replaced it with three
  ordered arms. Ruled by the issuer as inside the decomposition, in the e79 COO half.

## Findings for the next round's analysis

- **SC-e-82 is material** (3.21 pct of COT market value, 1,060 positions, against a 0.5 pct threshold). Porting the BD `NAME::` path to COT's
  `classify_position` is an enrichment candidate. The largest placeable names are alternatives (CCA Eiger, CCA FC Houston Opportunity LP,
  Peregrine Land Investments I).
- **SC-e-80's refusal** now makes a blind log read `ok=False`. Every AI-leg close is re-gradeable with it.

Not in this round: the 10:30Z COT run closes (e67 G, remap-b COT half, cot-repoint S, cot-cusip-rows R); e60 G at the next BD run.
