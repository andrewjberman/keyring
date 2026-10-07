# AMGT_CORPUS -- ROUND 38 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~18:4xZ

**Input:** CVO slug msg 30187, `surprise-channel/adjudications/ADJUDICATION_v44.md` @8a796bc632 (+ REMEDIATION_v3). The L10
precondition is MET: 1 ARMED row (`Z-S88`), dispositioned OPEN on its remedy. The packet is `ROUND38_DRAIN_END_PACKET.md`
@31aa103a37.

## 1. WHAT THE ROUND DELIVERED

- **an-2 (SERVED):** count and ratio fields carry no currency. The CVO's independent read: 34,894 count/ratio figures over
  96 of 96 blocks, 0 of them with a currency. `Z-W1-S35` is DISARMED.
- **an-3:** the 10-06 fire pulled 0 (`Z-S88`, the same-day skip keyed on the derived stamp). The same-day pull under
  AMENDMENT 2 landed 96 of 96, with 2,276 values moved.
- **an-6/an-7:** the page sweep and the coverage census.

**Round 38 is CLOSED.**

## 2. THE BOARD

- **REALIZED:** FWD-19 (83 + 13 + 1 = 97, read-only census).
- **REVERTED:** FWD-22 is NOT REALIZED. The first scheduled fire on pin `6f6e472641` re-pulled 0 of 96.
- **NOT REALIZED:**
  - FWD-10, 11, 12, 15, 16 and 18 each have one undriven limb, named in the adjudication table.
  - FWD-14 sums to 96 of 97.
  - FWD-20 has three page defects.
  - FWD-21 clips 2028E at 1440 px.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **FWD-14: 96 of 97, and no class for "unresolved"** | **ENDPOINT amended, PRD v0.8 ADDENDUM C:** four classes, the fourth being FWD-19's `unresolved-with-reason`. The ratified-text half is re-owed to `3.0.0_SA_CVO~Z`. The round-39 census reads the four-class sum. | The partition was not exhaustive over its declared domain (rule 24 i). Fixing Brookfield fixes one instance, not the partition. |
| 2 | **FWD-20 defect 1:** the header-fact line drops the currency on every name (`modelSheet.ts:431`) | **Round-39 portal cell:** `v3Facts` carries the served `currency`, and the line renders it the way the table rows do. | A one-line page fix. The served object already holds the currency. |
| 3 | **FWD-20 defect 2:** TSM EPS/DPS/P-E history reads 30 unmarked "--" cells | **The same portal cell:** every in-row "--" carries a cell mark. Where the served block has no history at all for the line, the mark reads "Bloomberg reports no history for this line". | This is the page's job: the served block truthfully holds no figure. No served change, so no pair. |
| 4 | **FWD-20 defect 3:** reasons in machine words beside a bare raw figure | **The same portal cell:** each `UNMEASURED:` basis maps to PM words, and the bare raw figure is SUPPRESSED, never shown beside the reason. Proof is TSM EV and net debt plus one control name with a resolved EV. | A raw number next to "not resolved" is a misread waiting to happen. FWD-20's last clause asks for a PM's words. |
| 5 | **FWD-21:** 2028E clipped on TSM and ASML at 1440 px | **A round-39 portal cell (separate):** the table fits FY+3 at 1440 px. Proof is a capture on TSM and ASML at 1440 px, plus history byte-unchanged. | A clipped column is a missing column. |
| 6 | **FWD-22 reverts** | **The round-39 skip-key cell (CTO msg 30045):** the same-day skip keys on the PULL date. It is proved by a 03:00Z re-derive plant followed by a fire that still pulls. Acceptance is the first SCHEDULED fire after the cell lands, read by the CVO. | The revert is a real regression in a reachable state. `Z-S88` stays ARMED until the cell lands. |
| 7 | **Pull-scoped half conditions** (the AMENDMENT 2 wording) | For future halves on a pull, the condition reads "values move only where the new PULL moves them", never "the new close". The 1 history revision (ORA FP) is inside the blast radius, so it is not a widening. **No cell.** | The narrower wording mis-describes what a vendor pull does. |
| 8 | **FWD-10, 11, 12, 15, 16 and 18: one undriven limb each** | **A round-39 drive cell (read-only):** drive exactly the limbs the adjudication names. These are the FWD-10 opener; FWD-11 ABSENT plus roster unchanged; the FWD-12 template comparison; FWD-15 header posture cited plus byte-unchanged; the FWD-16 docx before/after; the FWD-18 term filter. Each limb gets a named capture or read. | These are walks, not builds. Each one is either REALIZED or becomes a named defect. |
| 9 | `Z-S87` (round-37 capacity refusal) | Unchanged, and carried. | It is not moved by this round. |

## 4. ENRICHMENT LIST (round 39, ONE issuance by `2.0.0_SA_COO~X`)

1. **The skip-key cell** (ruling 6). It disarms `Z-S88`.
2. **The FWD-20 page cell** (rulings 2-4): three criteria, the header currency, the cell marks and the PM words.
3. **The FWD-21 fit cell** (ruling 5).
4. **The drive cell** (ruling 8), read-only, run after cells 2 and 3 land on DEV.
5. **The FWD-14 four-class census** (ruling 1), after the CVO signs v0.8.

## 5. ACTS FOR ANDREW (cited)

None. Cells 2 and 3 reach DEV under the portal's normal candidate path (CTO render review).
