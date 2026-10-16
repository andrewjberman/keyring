# Tonight's Anthropic spend: attribution, securities done versus remaining, cost per security (2026-10-16 ~08:5xZ)

**Asked by:** Andrew via Muse ("have your CRO look into MDPF_SECCLASS -- it looks like it is on a rampage with the API"),
relayed by `1.0.0_SA_CTO~DELL1` (msg 6610). **Seat:** `4.0.0_SA_CRO~DELL1`.

## Verdict: AIFILL, not SECCLASS -- the CTO's attribution is confirmed

All $124.61 sits in two clusters, and each matches an AMGT_RESAPP AIFILL run to the minute:

| Vendor charges (Muse) | AIFILL run | Measured from |
|---|---|---|
| 03:45-04:05Z, $56.21 | First 95-name run, unmetered: documents generated 03:38:20Z-04:06:37Z | `generated_at` in the 95 raw files, `2.0.0_SA_COO~R2/round107_aifill_close/live95/raw/` |
| 08:05-08:36Z, $68.40 | Metered re-run after gu-1 (`rerun95.py` @3ee0c109c2): script saved 08:06Z, ledger closed 08:38Z, `DONE spent_usd=63.1620` | `round109_close/rerun95_stdout.txt`, `live95/spend_ledger.jsonl` (95 lines) |

**SECCLASS cannot be the source.** Its three lambdas (`infra/aws/lambda/mdpf-secclass/`: `ai-index`, `new-security-classifier`,
`sector-writer`) and `data/mdpf/scripts/demque/secclass_sync.py` contain no Anthropic, Claude, Bedrock or OpenAI call (0 matches).

**Reconciliation (inferred; the vendor console is the only billed figure):**
- Re-run metered $63.16 against $68.40 billed in its window. The $5.24 gap fits the meter's assumptions: list rate card 5/25 USD
  per Mtok, $0.01 per web search.
- First run: block-recorded cost is $43.52 at 5/25. Blocks under-record; on the re-run, metered cost was 1.70 times the recorded
  cost, which puts the first run at about $74. $56.21 was billed in its window. Charges of $10-13 look like prepaid top-ups, so
  a window's charges need not equal a run's exact cost.

## Securities done versus remaining

- **In scope (census_v5):** 95 securities, 95 resolved, 0 failed.
- **Done:** 95 of 95 regenerated in the metered re-run (all `OK`, all blocks HELD/PASS) and stored. The second 95-key store write
  was done at 08:44Z under the round-109 never-widen pair (@190579b2b5).
- **Remaining in scope: 0.** The served page still holds the documents until a fresh CVO five-name read reads MET.
- **Outside scope:** the harvest resolves 243 securities, so about 148 have no AI-fill document (derived: 243 - 95). At tonight's
  measured mean, one pass over them would cost about $98 (inferred).

## Cost per security (metered re-run, 95 securities)

| | USD |
|---|---|
| Total | 63.16 |
| Mean | 0.66 |
| Median | 0.60 |
| Lowest | 0.03 (NOW_US_Equity) |
| Highest | 1.62 (ICICIBC_IN_Equity); then MER_PM 1.47, SSE_LN 1.42, GPN_US 1.41, 992_HK 1.38 |

- **Spread:** 13 securities under $0.25, 25 at $0.25-0.50, 41 at $0.50-1.00, 16 at $1.00 or more.
- **Calls:** 659 model calls, 6.9 per security.
- **First run:** about $0.78 per security (inferred from the 1.70 ratio; not metered).

## Other model spend to expect (not in tonight's charges)

- **08:47Z:** R2's real run of the CVO's five names at the merged gu-1 head (@c4d4df8ea1). About $3 at the measured mean; it
  falls after the second window and will show in the next charge.
- **`OpalResearch-FilingsAnalyzer`:** a scheduled task on dell1, enabled about 05:36Z for the G4 filings first fire (@722ebf99de).
  - It has not run yet: Task Scheduler result 267011 means never run.
  - First fire is **11:30Z today (07:30 ET)**, daily, capped at 20 securities (about $14 a run per R1's estimate).
  - It is the only enabled LLM batch task on dell1; ExecManagement and Scores are disabled.

## Not read
- The Anthropic usage console (billed truth by run).
- The CVO five-name run's own spend.
- Any non-AIFILL Anthropic key use on other boxes.
