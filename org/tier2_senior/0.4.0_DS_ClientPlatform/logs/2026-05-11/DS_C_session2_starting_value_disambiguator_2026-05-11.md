# DS~C 2026-05-11 — Starting Value disambiguator (ADVI_INFGRO Stage -1 follow-up)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Trigger:** Andrew direct (via COO surface) — empirical disambiguator on the one ambiguous item from DS~B's Stage -1 audit.
**Outcome:** Strong INTERNAL/seed verdict. Five independent signals converge.

## TL;DR

`Contributions > Starting Value` (896 rows / $6.64M / 69 distinct accounts / 2021-01-26..2026-05-04)
is a **synthetic per-position opening-balance seed**, NOT real onboarding NNA. Recommend
classifying as `INTERNAL_TRANSFER` / ε bucket in the PRD §2 taxonomy.

## DS~B's primary disambiguator — empirical result

> Does any of the 896 SV rows co-occur with a "Merge In from Other Account" on the same date for the same account?

Empirical: **0 overlap** out of 69 SV (account, date) pairs vs 1,330 MI (account, date) pairs.

Per the rule:
- If YES → onboarding-NNA double-recorded → classify SV as INTERNAL (avoid double-counting)
- If NO → synthetic system seed → classify SV as INTERNAL

Both branches converge on `INTERNAL`. The empirical NO answer routes us to "synthetic seed,"
which I then validated against four additional signals.

## Five-signal evidence cascade

| # | Signal | Evidence | Direction |
|---|---|---|---|
| 1 | Same-date MI co-occurrence | 0 of 69 SV (account, date) pairs overlap with MI | NOT double-record |
| 2 | Per-account dates | median = max = 1 — every SV account has all its SV rows on exactly one date | Anchor pattern (not cash-flow pattern) |
| 3 | Descriptions | Security names ("Fidelity Government Cash Reserves" 31×, "Fidelity 500 Index Fund" 20×, "Fidelity International Index" 18×) — NOT cash descriptors | Per-position accounting |
| 4 | Cross-classification within Contributions | 43.5% of SV accounts (30 of 69) have non-SV Contributions (Client/Rollover/Employer) on OTHER dates — those accounts use proper sub-types for real cash | SV not used for real cash |
| 5 | Top-account shape | Account 4138: 503 rows / $1.16M / 1 date — 503 distinct security positions sized to MV on a single day | Classic onboarding anchor; real cash would be one Merge-In row |

## Same-date activity audit on SV dates

What ELSE happens on (account, date) pairs where SV fires?

| Other activity_category × type_desc | Row count |
|---|---:|
| Contributions > Starting Value (the SV rows themselves) | 896 |
| Exchange In > Buy Exchange | 10 |
| Exchange Out > Sell Exchange | 10 |
| Dividends and Interest > Dividend to Cash | 1 |
| Net Dividends/Interest/Gains Withdrawn > Income Reinvested | 1 |

**Zero** Client Contribution, Rollover Contribution, Merge In, Distribution, Advisory Fee on
SV dates. The 10 Exchange In/Out pairs are normal Fidelity cash-sweep mechanics on the anchor
day (cash → money-market fund), not economic flow. The two dividend pairs are noise.

## SV per-account shape

```
69 distinct accounts
median dates per account: 1
max dates per account:    1
median rows per account:  4
max rows per account:    503
median $ per account: ~$96K
$6.64M aggregate
```

Top 10 SV accounts by $ (all on a single anchor date):

| account_id | rows | total $ | dates |
|---:|---:|---:|---:|
| 4138 | 503 | $1,160,619 | 1 |
| 386 | 6 | $1,086,340 | 1 |
| 4140 | 7 | $522,386 | 1 |
| 1365 | 13 | $451,104 | 1 |
| 976 | 12 | $255,870 | 1 |
| 1421 | 14 | $255,806 | 1 |
| 606 | 2 | $188,239 | 1 |
| 303 | 1 | $175,000 | 1 |
| 891 | 31 | $168,214 | 1 |
| 1206 | 6 | $165,465 | 1 |

## Caveat — unrecorded onboarding cash for 39 accounts

39 of 69 SV accounts (56.5%) have ONLY Starting Value — no Client Contribution, no Rollover,
no Merge-In ever. For these accounts, the actual onboarding cash flow is **not in the
transaction ledger anywhere**. The economic event existed (positions came from somewhere)
but Orion didn't capture it as NNA. SV is the only trace.

**Implication:** classifying SV as INTERNAL means partner-facing NNA understates by some
subset of $6.64M (specifically the portion belonging to those 39 accounts). The alternative
(classify SV as CASHFLOW_IN) inflates NNA by mixing synthetic anchor rows with real cash.
Better to under-state than to mis-attribute synthetic accounting noise as economic flow.

The 39 accounts likely correspond to:
- Accounts onboarded BEFORE Orion started tracking (anchor row = first observation)
- Accounts moved between custodians where the move pre-dated Orion's view
- Closed accounts where the post-anchor activity stopped

For PRD §2: SV → INTERNAL_TRANSFER with a footnote that some non-trivial subset of
historical onboarding NNA is unrecorded in source. Not a blocker; data-gap acknowledgement.

## Materiality

- SV aggregate: **$6.64M**
- Total Merge-In economic flow (CASHFLOW_IN candidate): **$130.5M**
- SV as % of Merge-In: **~5%**

Non-trivial size — the classification choice does move the firm-wide NNA total by ~$6.64M.
But the evidence is decisive enough that the cost of mis-classifying-as-NNA (double-counting
risk on 30 accounts + synthetic-noise inflation on the other 39) outweighs the cost of
under-counting unrecorded onboarding.

## Recommendation

PRD §2 taxonomy entry:

```
type_desc = "Starting Value"
activity_category = "Contributions"
proposed_category = INTERNAL_TRANSFER
rationale = Per-position opening-balance seed when an account first joins Orion tracking.
            Empirical: zero same-date co-occurrence with Merge-In (DS~B's disambiguator);
            anchor-date pattern (1 date per account); descriptions are security names not
            cash descriptors; 43.5% of SV accounts use proper Contribution sub-types
            on other dates for real cash. Synthetic accounting, not economic flow.
caveat   = ~$6.64M unrecorded onboarding NNA on 39 SV-only accounts; data-gap footnote
           in partner-facing NNA documentation.
```

## Files / artifacts

No code changes. Read-only audit. Diagnostic script results captured inline above.

## Compiler tools

| Tool | Run | Result |
|---|---|---|
| Direct parquet scan | 1,510 silver/transactions partitions / 1,156,082 rows / 32-worker ThreadPool | ~25s wall |
| Co-occurrence test | (account, date) set intersection across SV + MI | 0 overlap empirical |
| `comp-pipescript io INF_C_01` | not re-run (already done in TO-8) | n/a |

## MCP / inbox

- Andrew → COO → DS~C (relay) for the disambiguator
- COO stand-down on Stage -1 audit (DS~B shipped first)
- DS~C verdict relayed to COO 21:10Z for Andrew

## Status

CLOSED for Stage -1 follow-up. Standing by for Bug A audit (INF_I_00 priced-holdings
2026-05-06..08 zero-MV regression) per COO 21:08Z routing estimate (15-30min ETA).
