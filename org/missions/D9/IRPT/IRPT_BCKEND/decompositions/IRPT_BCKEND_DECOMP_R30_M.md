# IRPT_BCKEND decomposition -- ROUND 30, WORKSTREAM ~M (2026-10-07, 2.0.0_SA_COO~M2, dell2)

**Cut on:**
- 1.0.0_SA_CTO~DELL2 round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md`
  @e363a194ed, section 5, workstream ~M: one item, E-M1 (msg 156).
- The analysis's section 4 ruling 3 condition (one issuer per round) ruled MET by 1.0.0_SA_CTO~DELL2 msg 160, on laptop
  2.0.0_SA_COO~M's final handoff @1640a0e86e (laptop 1.0.0_SA_CTO msg 106037: that lane does no further act on IRPT_BCKEND).
- The last ~M decomposition is R29 (@0a656c46b1, cell IB-mr-291, complete). The STATUS~M next-list items 1 (BD r3 re-land,
  MDPF_SECCLASS, dell1) and 4 (`multi_asset` readers, retired by Andrew's six-class word) leave this workstream per the analysis.

**Rectangle:** the analysis's ENRICHMENT LIST for ~M (one item) plus remediations owned by ~M in REMEDIATION_v20 (zero rows: the
v20 slug names no row owned by ~M or ~M2, read 08:32Z).

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-301` | **FWD-5 replay on the served publication** (E-M1). Read each firm's newest served Holdings publication (`irpt/<firm>/platinum/holdings/current/manifest.json` -> the dated manifest -> its gold parquet, sha256 checked against the manifest). (1) Inflection split account `acc_015d15b45d7a8ac71f951a67` (****3282): its positions sum to its value. (2) One Cottonwood selection holding SPYI and PSLV ties the same way. (3) The before-and-after-overlay reconcile of unique underlying holdings at 49F, INF and COT on that publication (the producer's `reconcile_before_after` rule, `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:2746`), with denominators printed. Read-only: no write, no mint, no deploy. | FWD-5 (EXERCISED: replay at all three firms) | SERVED | none |

Chains: A = 301. M = 1. Slot `0.9.0_WK_IRPT_BCKEND~132` (1 + max over authors, issued_to and branches = 131).

**Ledgers:** the analysis says each ledger's leg S closes on its read. Both ledgers the STATUS~M walks named are already CLOSED:
`irpt-inf-split-positions-m-20261001` (@435c745d59, change_management `20261001T1948Z_..._deploy_completion.md`) and
`secclass-cot-seed-rows-m-20261001` (change_management `20261002T0200Z_..._deploy_completion.md`). The cell opens and closes
no ledger; its read is FWD-5 evidence.

**NOT ISSUED -- row IRPT_BCKEND-S352 (BLOCKING, ARMED, owner 2.0.0_SA_COO~M2).** The dell2 identity is refused on all three
firm buckets' Holdings manifests (HeadObject 403, 3 of 3; ListBucket explicit deny), so no dell2 worker can execute the cell.
The cell is issued, unchanged, when S352 un-parks: either a principal permitted on the firm buckets runs the read (a laptop
seat delivers a FILE; this seat files the row) or the bucket-policy owner admits the dell2 identity read-only. Routing that
is 1.0.0_SA_CTO~DELL2's call (asked by message). This decomposition is FROZEN as cut.

**Dated-work hold (laptop 1.0.0_SA_CTO 08:50Z ruling, msg 175):** the cell reads only the newest 2026 publication; no
pre-2024 date passes through `lib/trading_calendar.py`. This lane made no pre-2024-dated artifact on dell2 (0 rows owed).

## AMENDMENT 1 (2026-10-07 ~09:3xZ, 2.0.0_SA_COO~M2, before issuance)

Ruled by the issuer inside its own decomposition, on the first laptop read @e9993e95fa (row IRPT_BCKEND-S356). No gate limb
graded this amendment: no task order is staged, so `.tools/to-pipeline-gate.py` has nothing to grade.
- c2 reads as STATUS~M wrote it ("SPYI / PSLV"): every Cottonwood account holding SPYI or PSLV ties, with its denominator. The
  cut's "SPYI and PSLV" matched 0 accounts.
- c3's custody-total and served-reconcile arms read the platinum header (manifest `platinum_header`, or `platinum` on v1),
  and an absent field FAILs as ABSENT.
- The reader `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r30m_fwd5_replay_read.py` carries both changes. The result
  of a second laptop read is the FILE E-M1 is issued and graded from.
