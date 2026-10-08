# ADVI_COTBKF decomposition -- ROUND 20 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-08 ~17:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-19 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_19_20261008.md` @c015b6de3d (msg 1355):
the ruling on D2-S30 (a custodian's designated core cash position is a sweep vehicle, rule (b); 316067107 goes on sweeps-v2 with its
designation source, no source = no entry) and the ENRICHMENT LIST E1 (class the 163 MATCH -> DIFF months, persist month grades) and
E2 (sweeps-v2, re-grade, control).

**Rule 24.** Domain: E1, E2. Two cells, one chain: E2 reads E1's classing and E1's persisted month grades, and both write
`commonwealth_sweep_regrade.py`, so E2 depends on E1 and they run on one worker in order.

## Measured constraints

1. Round 19's real run on the trunk (@bf424e274b): `months_before=1685/1931/78977 months_after=2057/1522/79014 control_same=True`;
   verdict moves DIFF->MATCH 543, MATCH->DIFF 163 (`deliverables/0.9.0_WK_ADVI_COTBKF~40/sweep_regrade.md`).
2. The round-19 runner keeps day parquet under `--data-dir` but no month grades beside the report, so a later re-grade cannot be
   compared month by month (the analysis's E1 item 2).
3. 316067107 Fidelity Government Cash Reserves: 232 accounts, 8,768 rows since 2023-03-17, monthly `dv`/`dvr`, 91% same-day paired
   (the CVO's census, row D2-S30). It is in the round-19 rejected candidates as a money-market fund.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-t-1` | E1: class the 163 MATCH -> DIFF months by account (holds 316067107 / holds another unlisted money-market fund / neither); persist month grades before and after beside the report | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~41` |
| `CB-t-2` | E2: sweeps-v2 -- 316067107 under rule (b) with its custodian-designation source and behavior census (no source = no entry); the same census for the other money-market funds, as a list only; re-grade v1 -> v2 with E1's 163 months shown, and the control | FWD-3 | LOCAL | `CB-t-1` | `0.9.0_WK_ADVI_COTBKF~41` (continued) |

**Fan-out:** `1 of 1 chains, cap 8` (a chain of two cells).
