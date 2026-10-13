# L8 packet -- MDPF_SECHIST round 5, from 2.0.0_SA_COO~H1 to 3.0.0_SA_CVO

**Compiled:** 2026-10-13 ~18:3xZ, dell1. **Decomposition:** [MDPF_SECHIST_DECOMP_R5.md](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R5.md)
(issued @e3b4308e1b). **Analysis cut on:** round-4 analysis (msg 2828). **PRD:** v0.3, `prd-signoff.py status` ADMITTED, ratified-text SIGNED current.
**Close basis:** `1.0.0_SA_CTO~DELL1` msg 5020, RULING (a), on the pivot packet O9 ("grade once, PARK, fold"): the CVO grades once now; SH-t-21 and
SH-t-22 are recorded NOT RUN and ride with FWD-9 in the fold record; they do not hold the grade.
`python .tools/round-close-check.py --project MDPF_SECHIST --round 5` -> `verdict=MAY-CLOSE` (orders=4, judgment=0, ungraded=0, proofs 2 of 2 OK).

## Orders -- 4 complete, 2 carried NOT RUN

| order | cell / FWD | executor | evidence (measured unless marked) |
|---|---|---|---|
| TO-SH-t19 | MMF repair batch / FWD-9, FWD-1 | worker ~18 | @ae567af9ef, amendment 1 @d2434ebc08 (exhausted list carries entry dates); issuer re-run at @522aa18dc2, 3 of 3 criteria green |
| TO-DEPLOY-GOLD | gold deploy to `etf-positioning-producer` / FWD-4, FWD-5, FWD-9 | 0.7.0_AE_CloudOps~SH1 | 14 members at pin 09b6a7d580; live `CodeSha256` `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=` (read again 2026-10-11); IAM 8 -> 9 statements with exactly one added (`Stage1WriteHistoryGaps`); ledger CLOSED 2026-10-11T02:24:30Z; L3 `GOLD-L3-OK` read by the issuer on the 2026-10-10 13:00Z scheduled run, 0 ImportError, gap record written ([L3_READ_20261010_RESULT.md](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L3_GOLD/L3_READ_20261010_RESULT.md)) |
| TO-VERIFY-SH-T8 | site-Z take of `etf_daily_pull.py` blob 75342a6958 / FWD-4, FWD-7 | 0.7.0_AE_CloudOps~ZQ | @f8e359debf; first scheduled run accepted (run_class scheduled, exit 0, exhausted count 2: PFDE, PFOE); ledger `mdpf-sechist-zq-sh-t8-v1` CLOSED 2026-10-11T03:36:15Z; this seat's own S3 read of that manifest agrees |
| TO-SH-t20 | FWD-7 read of the 2026-10-12 pull / FWD-7 | issuer, direct act | @bb6b1e5b43: `FWD7-READ-OK as_of=2026-10-09 recorded=17 spent_after=17 remainder=119983` on the manifest of the Monday 2026-10-12 11:00Z pull (LastModified 2026-10-12T11:03:03Z, attribution by head-object); ledger `mdpf-sechist-sh-t4-sitez-run-record-20261009` CLOSED @bef0b9a6d5; the leg exit code 0 is RELAYED from site Z (msg 4337), not measured here |
| TO-SH-t21 | FWD-9 blank read | -- | CARRIED, NOT RUN (msg 5020). Gate never fired as written: see row D1-S5 |
| TO-SH-t22 | FWD-9 filled read | -- | CARRIED, NOT RUN (msg 5020). Depends on SH-t-21 |

No judgment criteria. Served values moved in this round by the gold deploy (2026-10-09 20:08Z) and read once on the 10-10 13:00Z run: keys common 188 of 188,
`weight>1` 0, `industry_group` changed 0; the MMF 1D/WTD values moved (SALXX, FXFXX), expected under the repaired rule and not graded as defects there.

## What is NOT read, so the grade does not assume it

- **FWD-9 end to end.** No page with `data_as_of` 2026-10-12 was ever served, so the blank-then-filled arm has not been exercised on a scheduled publish.
- The money-market funds' 2026-10-12 return in `bbg/2026-10-12/history_topup.csv` (7132 B) was not read.
- Whether the live characteristics producer package carries the MMF rule: it does NOT (vendors `etf_positioning_gold.py` at `09408b19e5`); the effect on
  its served values is unmeasured (row D1-S6).
- The site-Z ETF-leg exit code for the 2026-10-12 11:00Z run is relayed, not measured.

## Rows (7 open, 2 ARMED, 0 defects, 0 malformed, of 37 items)

| id | class | standing | note |
|---|---|---|---|
| D1-S2 | OBSERVATION | ARMED | gold package members. Disarm evidence filed @2de5d9fbef ([DISARM_EVIDENCE_D1_S2_Z_S2_20261011.md](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/DISARM_EVIDENCE_D1_S2_Z_S2_20261011.md)); the clock is yours |
| Z-S2 | OBSERVATION | ARMED | SH-t-8 landed by box-sync before its ledger. Same evidence file; the clock is yours |
| D1-S1 | OBSERVATION | INERT | depth bound never retries an exhausted ticker; accepted for round 5; expiry cell staged for round 6 |
| D1-S3 | OBSERVATION | INERT | dell1 cloudops user cannot call `iam:SimulatePrincipalPolicy`; the Dell grant of 2026-10-13 names it |
| D1-S4 | BLOCKING | INERT | proof-of-spec-check CRLF read; worked around by LF amendment @bc05afd0e6 |
| D1-S5 | BLOCKING | INERT | the 10-13 pull stopped by its precondition; landed 14:39:56Z; [D1_S5_RESOLUTION_EVIDENCE_20261013.md](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/D1_S5_RESOLUTION_EVIDENCE_20261013.md) |
| D1-S6 | OBSERVATION | INERT | characteristics producer vendors the pre-MMF-rule gold; redeploy is a separate act under its own pair, not decided |

## Deploys

None open. Round-6 staged cells (not cut): [expiry](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO~H1/r6_staged/SH_EXHAUSTED_EXPIRY_CELL_STAGED.md),
[depth start 365](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO~H1/r6_staged/SH_DEPTH_START_365_CELL_STAGED.md),
[series reads the DEMQUE store](file:///C:/dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO~H1/r6_staged/SH_SERIES_READS_DEMQUE_STORE_CELL_STAGED.md). Under the pivot they go to the fold
record with the seat's handoff, not to a round-6 issuance by this seat.
