# PRD ROUND -- SESSION ORDER, 2026-08-24 (position + dependencies + proposed ordering)

**Author:** `1.0.0_SA_CTO` -- **archetype:** COORDINATE
**Status:** v0.1 PROPOSED at ~15:1xZ, pending Andrew's ratification (his ask at the terminal, ~15:0xZ:
*"let's identify how we want to proceed with ordering/structuring the PRDs/issuances for this session.
There are many moving pieces with various dependencies ... we need to map those out and assess our
position up front before getting started."*)
**Governs:** the PRD-per-directive round he ordered at ~13:3xZ (record
`ANDREW_DIRECT_20260824_FABRIC_CLOSEOUT_LOG_THEN_PRDS.md`), against the Monday push order
(`ANDREW_DIRECT_20260824_MONDAY_PUSH_ORDER_BY_DIRECTIVE.md`).
**Push state of this file:** landed LOCAL, rides MSTR integration.

## 1. POSITION -- measured this session (14:2x-15:1xZ) unless marked

| piece | state | needs |
|---|---|---|
| **MDPF Global** (live break) | 13:31Z run: Cottonwood HEALED (@1daf1913dd; aggregate reconciliation PASS in the manifest); **Global REFUSED on an independent gate** (CROSS-AXIS COHERENCE / foreign-day roster: ~469-account excursion 08-19/20). Publisher rewrote all four platinum scopes 13:50:50Z (s3api, UTC); served vintage per scope pinned in s.1a. | a DS data ruling; **no owner today** (every lane closed-out) |
| **D4 ETF page** | Round 1 DELIVERED; artifact LIVE; decomp certified. Promote STAGED+HELD (`origin/PROD 8a96c916` unwritten). TrueShares capture WIRED @4e5800fde0, NOT deployed (2 asks at AE; each uncaptured day lost). TO-5 schedule COMMITTED-NOT-APPLIED (cron(0 13) UTC). | Andrew's two words + AE two applies + COO round-close |
| **D2 49F switch** | HELD on two conditions (COO 08-21 reference). Parity TOs **P1/P2/P3 all `staged`, never started** (P1 "activates at respawn"). JD2 role-loss untraced; leaderboard -20 untraced; office = 285 branch codes vs 9 offices (grain mismatch); state = `fact_acc.ac_st` 100% populated, 48 distinct (unbuilt dim over held data). | DS + CRO + CVO seats |
| **D2 sourcing** (new project `ADVI_49FSRC`) | The two Schwab masters are ONE BOOK: fact_acc 2026-08-21 = 7,238 shared accounts of 7,336 (0833) / 7,258 (0824); balances CENT-IDENTICAL on every shared account (7,238/7,238 at frontier; 3,930/3,930 at 2024-07-08). "Blend" = union by account_id, 0833 authoritative, 0824 fills the pre-2024-07-08 tail + its 20 exclusives; never summed. Valuation floor: 2024-07-08 (0833) -> 2024-05-24 (0824 silver) -> **2024-01-12 (0824 bronze; ~92 days un-converted)**. Legacy 2020-01-02-> series is BD `account_performance` (D_00b) -- unreachable from Schwab. Run: `ADVI_49FSRC_ATOMDECOMP/run_20260824.md`. | CTO PRD (today) -> COO decomp |
| **D1 taxonomy** | Stage-3 decomp LANDED @3b103f129 (14 cells); **CVO cert PENDING**; zero TOs. IMMEDIATE TERM (his diagnosis: Cottonwood Opal-Advised assets untracked -> Global by proxy). | CVO cert -> COO TOs -> DS gold + DE portal |
| **D0** | 0.8.0_AE_CloudComp not spawned; packet brief not written. | CTO brief -> MSTR spawn |
| **D3** | Pends D1 + D2. The exact-join spec is early-startable -- and the overlap measurement above IS the Schwab-plane join. | folds into the D2 sourcing PRD as a section |
| **D6** | comp-state packet ready (self-test 4/4 PASS, run 14:3xZ); site-Z seats closed-out. | MSTR bridge -> CTO~Z |
| D5 / D7 / D9 | HOLDING (his word). D8 DONE. | -- |
| **Fabric** | Live: MSTR, CRO (with Andrew), CTO. COO / CVO / DS / DE / DT / AE ALL closed-out -> every issuance needs a spawn. | MSTR |
| Records | 4 corrected @78f24c2efc (local). Gaps surfaced, not chased: `ADVI_BDPARITY` / `ADVI_IDSPINE` carry TOs with NO project JSON; no `DAILY_SPRINT_2026-08-24.md`; 194 open findings past `review_by` in `org/critical_paths/.open_findings/`. | hygiene, owner TBD |

### 1a. MDPF served vintage per scope (pinned 15:1xZ, live read of `platinum/mdpf/{scope}/aggregate-aua-timeseries.json`, all four written 13:50:48-51Z by `opal-assets-mdpf-portal-publisher`)

| scope | `as_of_last` | publisher source key | read |
|---|---|---|---|
| 49financial | **2026-08-21** | `.../49financial/aggregate-aua-timeseries/2026-08-21.json` | T-1, healthy |
| inflection | **2026-08-21** | `.../inflection/aggregate-aua-timeseries/2026-08-21.json` | T-1, healthy |
| global | **2026-08-19** | `.../global/aggregate-aua-timeseries/2026-08-19.json` | 2 trading days behind -- the foreign-day-roster refusal, correct refusal |
| **cottonwood** | **2026-08-19** | `.../cottonwood/aggregate-aua-timeseries/2026-08-19.json` | **2 trading days behind AFTER the 13:31Z gold heal.** The publisher's source prefix `portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/` has NO 2026-08-20 or 2026-08-21 partition (newest = 2026-08-19.json, written 08-20T13:31:09Z; positive control: 49financial's 2026-08-21.json landed 08-24T13:31:07Z). So "COTTONWOOD HEALED" (13:3xZ close-out read) was TRUE AT THE MANIFEST PLANE and is NOT TRUE at the served plane: the guard is silent, but the per-date portal/gold partition the publisher reads was not written. Mechanism UNTRACED (candidates: the leg writes the legacy `gold/mdpf_revamp/cottonwood/` root the manifest names; or the fold is skipped when the global coherence gate refuses). A DS/CTO-lane trace, same cell as the Global roster ruling. |

T-1 for a Monday 08-24 read = Friday 08-21 (NEVER#1: trading days, not wall-clock).

## 2. DEPENDENCIES

```
 ANDREW WORD promote ------------> D4 page LIVE (DT, ~10 min)
 ANDREW WORD TrueShares deploy --> D4 constituents fill (AE)         D4 CLOSE <- TO-5 apply (AE) + COO round-close

 CVO cert --> COO cuts D1 TOs --> DS gold + DE portal --> D1 DONE -------------------+
 Global roster ruling (DS) --> Global serving resumes                                 +--> D3 build (6-7 wks)
 D2 sourcing PRD (CTO) --> COO decomp --> DS/AE TOs: history + geo + office + roles  +
 D2 parity P1 -> P2 -> P3 (DS + CRO; CVO grades)   [independent of sourcing]         |
 hold(A) sources --+                                                                 |
 hold(B) P4I-3 activation (AE, 3 named steps) --+--> DE flip --> DT promote (D2 switch)
 D0 packet --> 0.8.0 spawn --> pipeline gates (decomp_ref check, TO lint) -- helps every round, blocks none
 D6 packet --> site-Z gap map (CTO~Z)
```

## 3. PROPOSED ORDER

- **Phase 0 (now, cost zero):** Andrew's two D4 words -- promote; TrueShares deploy-now vs at-restart.
- **Phase 1 (CTO paper, parallel with spawns):** (1) this map committed as the session order; (2) **D2
  sourcing PRD** -- register `ADVI_49FSRC`, PRD + atomdecomp run, with the D3 exact-join spec as a
  section; (3) **D0 packet brief**; (4) D4 PRD s.11 status refresh (small). **D1 needs no CTO paper** --
  its next acts are the CVO cert and COO's TO cut.
- **Phase 2 (spawns, in this order):** COO + CVO first (D1 cert / TOs; D2 decomp), then DS (Global
  roster ruling -> D1 gold -> parity P1), DE (D1 portal), AE (D4 two applies; D2 P4I-3 readiness),
  0.8.0 (D0).
- **Phase 3:** execution rounds under the pipeline (Rule 27); CVO mans the surprise channel.

## 4. CALLS AT ANDREW THAT CHANGE THE ORDER

1. Promote word (D4).
2. TrueShares deploy now, or at restart.
3. **D2 history fork:** accept the Schwab floor (2024-01-12 after one silver conversion, ~2.6 yrs) /
   a ONE-TIME frozen BD history import for 2020-01..2024-01 (closed-period-immutable, Rule 25 kind --
   not a standing dependency) / a Schwab historical-file request. The PRD carries all three; his lean
   sets s.3.
4. Confirm Phase 2 ordering (COO + CVO spawn for D1 while CTO drafts D2) -- CTO recommendation.

## 5. WHAT THIS FILE IS NOT
Not a gate (Rule: no gates without his word), not a dispatch (COO issues TOs), not a ruling on the
history fork. It is the position map he asked for, with the ordering CTO recommends.
