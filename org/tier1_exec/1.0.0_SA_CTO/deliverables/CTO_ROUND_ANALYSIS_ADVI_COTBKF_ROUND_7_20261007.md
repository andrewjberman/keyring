# ADVI_COTBKF -- ROUND ANALYSIS, round 7

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~11:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 387):
ADJUDICATION_v6 @cfd9d3c4f4. Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_7_L9_GRADE_20261007.md`. ARMED 0.

## 1. Outcome state -- 4 of 9 REALIZED (was 3)

- **FWD-8 REALIZED** (MET by the CVO): an old Commonwealth account lines up with the same client's account today, and the 21
  near-matches are left for a person.
- **FWD-6 NOT MET** (CB7g3-AC3). The data is right: statements run 12 months, and tax forms cover 2 tax years. But the page is
  organized by storage table and gives one 2016-2026 range for all documents. A reader who is not told otherwise would take
  statements to reach 2016. The fix is one plain line per kind of record.
- **CB4d1-AC3 (the price store, FWD-3)** stays NOT MET until the laptop listing returns (relayed 10:50Z; Cottonwood still denied
  on dell2).

## 2. W23-S1 -- the transactions count

The applied silver table reads 1,416,497 rows. W2-S1 reported 1,415,137 after dropping exact duplicates. **The difference is
1,360, which is exactly the number of duplicates W2-S1 said it dropped.** The most direct reading is that the applied table still
holds them. That is a FWD-1 correctness question (one transaction list, nothing counted twice), not a wording question. **RULED:**
measure it before any page states a reason. Until it is measured, the coverage page says "under investigation" for this count and
gives no reason.

## 3. ENRICHMENT -- round 8, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The duplicate count** (W23-S1; FWD-1) | (1) the count of exact-duplicate rows in the applied table, by the same key W2-S1 used, is printed; (2) if it is 1,360, the cause (which write skipped the drop) is named with file:line; (3) the coverage page's line for transactions states the measured result, not a guess | LOCAL read |
| E2 | **FWD-6, one plain line per kind of record** (CB7g3-AC3) | (1) the page leads with one line per record kind (transactions, positions, statements, tax forms, CRM, prices), each naming what is covered, its date span and its count; (2) no line spans a range that kind does not have; (3) every "not covered" names its reason and row | LOCAL |
| E3 | **The re-apply, only if E1 finds duplicates** | (1) a corrected transactions apply under a new never-widen pair (both halves), its read-back reading 1,415,137 rows | SERVED |

E3 is cut only on E1's finding. The price store (FWD-3) follows the laptop listing. FWD-2's CRM half, FWD-4 and FWD-7 follow the
C-RESTRICTED apply on the laptop.

## CORRECTION 2026-10-07 ~11:0xZ (on `2.0.0_SA_COO~C2` msg 390) -- section 2's reading and E3 are WITHDRAWN

Section 2 was wrong. PRD v0.4 addendum item 1 (`prd/ADVI_COTBKF_PRD.md:204-206`), the C-SILVER row (`:114`) and
`commonwealth_transactions.py:13-15` all say every delivered record is one row and nothing is de-duplicated. With no transaction id, two
identical lines may be two real events, and dropping them would change flows and FWD-3's returns. 1,416,497 is the SPECIFIED count.
W2-S1's 1,415,137 predates that ruling. This seat read the gap against the older row instead of the PRD it governs under.
- **E3 is struck.** No re-apply.
- **E1 is kept as a measurement:** the count is measured, and the cause is cited from the PRD and the code.
- **E2 is unchanged.** The transactions line reads: 1,416,497 rows, of which 1,360 are exact repeats kept by C-SILVER.
- **FWD-1** ("nothing counted twice") is unaffected. A repeat kept as a separate real event is not a double count.

-- 1.0.0_SA_CTO~DELL2
