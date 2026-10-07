# L8 packet -- MDPF_SECHIST round 1 (the FWD-1 thread), from 2.0.0_SA_COO~H1 to 3.0.0_SA_CVO

**Compiled:** 2026-10-07 ~08:3xZ, dell1. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP.md` (issued @f8a41e7902,
`fanout: 2 of 2 chains, cap 8`). **PRD:** v0.1 @b4b995dc14 (L4-R ADMITTED).

## Task orders -- 2 of 2 terminal

| order | cell | risk | final drain | proof instance (VALID at drain) | issuer re-run at drain |
|---|---|---|---|---|---|
| `MDPF_SECHIST.TO-SH-t2` | `SH-t-2` gold pin | LOCAL (direct act) | @78595434c2 | `deliverables/0.9.0_WK_MDPF_SECHIST~2/MDPF_SECHIST.TO-SH-t2.gold-reads-backfill-rows.proof_of_spec.json` | SH1-t2-AC1 `GOLD-TESTS-OK` |
| `MDPF_SECHIST.TO-SH-t1` | `SH-t-1` per-security depth in the site Z ETF pull | LOCAL (code); its site Z deploy is WORLD | first pass @099e082db2; amendment 1 (C-BUDGET) @20a69d5a62 | `deliverables/0.9.0_WK_MDPF_SECHIST~1/MDPF_SECHIST.TO-SH-t1.per-security-history-depth.proof_of_spec.json` | SH1-t1-AC1 `PLAN-TESTS-OK` (5 of 5 named), SH1-t1-AC2 `SEAM-OK planned=15 CSCO@2025-09-29 BX@2025-09-29` |

No judgment criteria were cut this round; nothing is owed to L9 for grading beyond the rows below and the FWD-1 real run.

## Rows -- 3, all OBSERVATION / INERT, `investigations/INVESTIGATION_v1.md`

- `MDPF_SECHIST-W2-S1`: two sibling Positioning gold tests fail at import run bare from the gold folder (`etf_classifications_dynamodb` lives under `infra/aws/lambda/v2_portal/_shared/`). Not caused by this round.
- `MDPF_SECHIST-W1-S1`: the need rule never converges for a security with under a year of real history (2602335D, PFDE, PFOE are re-planned every run); a bound is an enrichment.
- `MDPF_SECHIST-W1-S2`: the first-pass isolation test now pins `RIVALFUNDS_BBG_BUDGET_DIR` to a temp dir so it cannot touch a shared ledger; no assertion changed.

## The site Z deploy -- the round's one WORLD act

Never-widen pair: COO half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md` @c21432885a;
CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md` (REFUSED @451db20b50 on C-BUDGET, SIGNED @6afcd4859d with a
ledger-directory condition). Branch `q/dell1/MDPF_SECHIST/r1` published by `0.0.0_AB_MSTR~DELL1` @40ed09cdf2 (ls-remote read); the deploy note went to the laptop and the
site Z queue. **Not yet deployed** at this packet's compile.

## FWD-1 real run -- OPEN

Owed by this seat after the first scheduled run of the leg with the change: CSCO, BX and a security an Opal ETF newly bought, read on the Positioning page (class, sector, clean
name, 1D..1Y). The thread reads `n` until then. This packet is re-issued with that read appended.

## Issuer notes

- A hazard amendment (interior gaps for CSCO/BX/LNVGY) was drafted and WITHDRAWN before commit: the census was over `history_topup` only, and gold also reads the 2026-10-06
  gap-fill CSVs at `bbg-testpull/tickers/<T>/gap_20261001_20261005/history.csv`, which carry those days.
