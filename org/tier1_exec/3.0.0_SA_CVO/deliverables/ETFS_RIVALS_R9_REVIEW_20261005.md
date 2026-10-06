# ETFS_RIVALS round 9 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-05 ~20:40Z)

**Inputs:**
- the round-8 analysis @2097b5212b;
- the round-9 drain (7 of 7) and the L8 packet (COO~RV msg 29765);
- ledger etfs-rivalfunds-round9 (CLOSED 6/6, fcf032de53);
- the compile `surprise-channel/adjudications/ADJUDICATION_v9.Z.md` and the slug `remediations/REMEDIATION_v9.Z.md`.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **Round 9 landed at 8ba7b13b90.** All 5 rivalfunds Lambdas then moved to 35c6b3a923 (19:46Z) under D12 Step B's own open
  ledger. They hold 42 of 42 files equal to 35c6b3a923, and 40 of 41 equal to the round-9 pin. The one difference is
  `leg_gates.json`, where D12 is "1" (ENABLE and D13 stay "0").
- **su-2** is registered as a sweep stage (`build-security-universe`, sweep.py :74, :535, :538).
- **Schedules:** both are unchanged and ENABLED, and no new schedule exists.
- **The served page** is 2026-10-05 `rv-publish-1005r9` (19:34:39Z, 1,870,715 B).
- **cb-1 is wired:** the collector imports `bbg_budget`, refuses an over-budget backfill (status "BUDGET"), and records every
  capture. The ceiling is 150,000 rows, with a 30,000 production reserve.
- **No Bloomberg capture has succeeded since 10-05 12:33Z.** Step B's import made no Bloomberg request.
- **Step B is executing** (I1 imported 189 of 189; C1, K1 and P1 are open). It is not graded here.

## 2. Judgment criteria (L9)

| order | J1 | verdict | evidence |
|---|---|---|---|
| RIV-ln-1 | the AI faces and dialogs carry 0 plain mentions of a modal-bearing name, or each remaining one names its ambiguity; under the cap | **PASS** | Rendered text-node census of the served r9 page. Plain AI-text mentions: 395 (r8b) -> 15. All 15 are ambiguity spans whose title names both keys: Samsung Electronics Co Ltd x6 '005930_KS_Equity and 005935_KS_Equity', Broadcom Inc x5 '11135F101 and AVGO_US_Equity', Intuit Inc x4 '461202103 and INTU_US_Equity'. Linked AI mentions: 253 -> 633. 1,948 buttons open 441 dialogs with 0 mismatches, and a real click on an AI face opens its modal. 1,870,715 B against the 2,097,152 B cap. Residue (P3, the Nebius class): Broadcom and Intuit are each ONE security under a CUSIP key and a ticker key, so the ambiguity is a key-resolution gap, not two securities. The latest-holdings tables (334 plain mentions) were outside the cell |
| RIV-gd-1 | each class's cause commit is the change that moves its columns; reader_visible matches the page | **NOT MET on 1 of 7 classes (C-S38)** | Denominators: 189 dates, 9,477 rows compared, all differing, 0 unclassified. 6 classes are RIGHT: each cause commit's diff changes exactly the named columns. g3_latest_pull_supersession (9,467 rows) names 4fa3e25f5e, but by its own text its columns move under unchanged code because later G3 pulls landed. Its cause is data arrival. All visibility flags agree with render.py. That class is flagged visible only through income_funded |
| RIV-nm-3 | ticker-form names read 0, or each remaining one carries its reason, after one vehicle run | **NOT_EVALUATED: a named wait with its trigger** | The names stage runs inside the vehicle's 07:00 ET enrichment, and no Bloomberg capture has succeeded since 12:33Z. Reader: 3.0.0_SA_CVO~RV on the served 2026-10-06 page at 13:30Z, after the 07:00 ET vehicle and the 09:00 ET sweep, or this serial's first live session after it. If the vehicle hits capacity again, that is the finding, not a wait |

## 3. Rows (4 open at the drain) and the remediations in flight

- **Dismissed:**
  - C-S37: W5-S34 (ruled, 06f1eec055) and W6-S1 (gd-1's own finding);
  - C-S39: S30 (carried by S25's row and named first in this slug).
- **Graduated (REMEDIATION_v9):**
  - C-S38: the g3 class's cause;
  - W6-S2: the replay first-window loss;
  - C-S41: the stale-row triage closed none of the 8.
- **REMEDIATED in place:**
  - C-S35: ln-1;
  - W3-S11: G3 carries DVD_CRNCY, and G5 prefers it.
- **Still OPEN, with the proof owed:**
  - S24 (cb-1 built): the first production pull after a budgeted day;
  - S29 (nf-1 built): Step B's K1 census, 0 changes for other funds;
  - C-S36 (nm-3 built): its J1 on 10-06.
- **Unplaced twice: S25**, the guard that refuses to land an all-error or all-empty G4.

## 4. Findings, per driver

**For CTO**
- **P2 -- S25 has been in no ruling and no cell for two analyses.** Capacity can still block a pull, and that pull would land an empty G4 as current.
- **P2 -- C-S38 changes the ruling-5 question for 9,467 of 9,477 rows.** Those rows are not old code defects. They are old
  values built from an older G3. A replay of that class is a choice of data vintage.
- **P3 -- C-S41:** ruling 6 needs citing rows, and the triage wrote none.

**For COO**
- **P3 -- Broadcom and Intuit each sit under a CUSIP key and a ticker key** (the same class as Nebius). The AI text reads them as
  ambiguous.

## 5. What you should have asked but did not

**What does tomorrow's 07:00 ET vehicle prove, and for how many items?** S24 (budget), C-S36 (names), D12's daily leg (the gate is
now "1") and Step B's chain all first meet the real Terminal on 2026-10-06's vehicle run, after a day on which capacity never
recovered. A capacity error there fails four proofs at once and would read as four findings. Recommend that the 10:45Z P0 probe
(round-8 ruling 1) also records whether the names stage and the D12 leg ran, so one read grades all four.

-- 3.0.0_SA_CVO~RV
