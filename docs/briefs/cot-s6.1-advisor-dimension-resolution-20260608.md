# ADVI_COTETL §6.1 RESOLUTION — Cottonwood Advisor Dimension: Outcome B (skip advisor analytics for v1)

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-08
**Project:** ADVI_COTETL
**Resolves:** PRD §6.1 open-decision (the sole remaining gate on the P1 bronze build)
**Source artifacts (Andrew-captured 2026-06-08):** `bd3.bdreporting.com3.har`, `CW_Advisor_Allocation_EXP.xlsx` (Snapshot, qt=1), `CW_Advisor_Allocation_NonSnap.xlsx` (Allocation, qt=5), cross-referenced against `CW_Transactions_Rich (1).xlsx` (6-month history).

---

## 0. Ruling

**§6.1 = Outcome B: Cottonwood carries no usable advisor dimension. Skip C_07 (advisor attribution), the architect/implementor leaderboards (D_00c), and the advisor cohort in partner_analytics (D_01) for v1.** AUA, NNA, geo (client-domicile), and client views are the v1 advisor-independent surface and proceed unchanged. **Revisit only if Cottonwood's rep-tagging discipline matures** (see §3).

Andrew tested two BD DataMining angles — the **Snapshot** function (qt=1) and the **Allocation** function (qt=5) — both with the full advisor/Team field set. The conclusion is identical across both, so it is a data fact, not a query-angle artifact.

---

## 1. The advisor fields are empty across BOTH probe approaches

Population measured on both probe exports (account grain):

| Advisor field | Snapshot (qt=1) | Allocation (qt=5) |
|---|---|---|
| DST Rep Name | empty | empty |
| Advisor of Record Name & B2B ID | 100% sentinel | 100% sentinel |
| Manager | 100% sentinel | 100% sentinel |
| Managed Account Manager Name | 100% sentinel | 100% sentinel |
| Team Name - Salentica | 100% sentinel | 100% sentinel |
| **Rep Code** | **96% populated** | **96% populated** |
| Team / Team Display Name | single value `"Cottonwood Capital Advisors"` | same |
| Team City / State / Address (office) | all empty | all empty |

The entire 49F advisor model (architect/implementor/consultant/local_ops + the Salentica/Advisor-of-Record fields) has **no Cottonwood equivalent in the data**. "Team" is a single firm-level label — there are no sub-offices and no office geo. The only populated advisor signal is **Rep Code** — analyzed in §2.

---

## 2. Rep Code is a 2-founder joint-coverage model, not a segmentation

Per-account rep-code **set** distribution (Allocation qt=5, 639 distinct accounts, $371.2M AUA):

| Rep-code set on the account | Accounts | Acct % | AUA | AUA % |
|---|---|---|---|---|
| **G46018202 + G46018211** (both, paired) | 589 | 92.2% | $356.8M | 96.1% |
| No RepCode Assigned | 48 | 7.5% | $14.3M | 3.9% |
| G46018202 + G46018211 + G46018204 (all three) | 2 | 0.3% | $34K | 0.0% |

- **G46018202 and G46018211 always appear together** (591 of 639 accounts, never separate) = **two founders jointly on essentially the entire book** (a fee-split partnership). You cannot separate "founder A's book vs founder B's book" — they're the same accounts under both codes.
- **48 accounts (7.5%) carry no rep code.**
- **G46018204** is on just **2 accounts** — investigated in §3.

There is no segmentation here: one joint 2-founder unit covers ~96% of AUA. A rep-based advisor leaderboard/cohort would compare a book against itself — meaningless.

---

## 3. The third rep code (G46018204): a 5-year FA only now being tagged, on new business only

Andrew's read (two founders + a third financial advisor, ~5 years tenure, "wouldn't surprise me if they just didn't tag things to her") is confirmed by the data.

**The two accounts carrying G46018204:** both **Schmitt family** (Lionel & Jesko Schmitt), $17,248 each, Fidelity IWS — each carrying *all three* codes (the two founders **+** G46018204, added on top).

**Both are brand-new accounts** (cross-referenced into the 6-month history, window 12/06/2025–06/05/2026):
- First activity **05/01/2026** for both — zero transactions before that in the window.
- Opening signature: **Wire Transfer / Cash Deposit (Contribution) → Buy Money Market** = fresh-funded new-account openings, not transferred-in legacy.

So **G46018204 first appears ~05/01/2026** — a tagging practice that began in the *last month* of the window. **Interpretation:** the third advisor exists and *is* now getting coded, but **only on new business**, added on top of the founders; the legacy book was never tagged to her. The rep-code data therefore **understates** her involvement — she almost certainly services more than 2 accounts, but isn't coded on the legacy book.

**Consequence:** the rep tagging does not reflect who actually services accounts (founders joint-on-everything; FA under-tagged 2 of 639). Advisor analytics built on it would be wrong. Confirms Outcome B.

**Forward note (revisit trigger):** the *infrastructure* is present (Rep Code 96% populated), only the data *quality/discipline* is immature. If Cottonwood begins consistently coding the FA (and any future advisors) on their actual accounts, a rep-based advisor cut could become viable in a later version. Worth re-checking at the next major data refresh; not v1.

---

## 4. Probe-angle finding (Snapshot vs Allocation) — bonus for the port

For the advisor question the two are equivalent (both show absence). For the **allocations/AUA table** the **Allocation function (qt=5, `NonSnap`) is the correct angle**:
- It carries **Account / Relationship / Cash Market Value + Account / Cash Allocation** + Account Owner + Data Provider — the AUA amounts the gold layer needs, matching 49F's `silver/allocations` schema.
- It gives **clean account numbers** (`638354607`). The **Snapshot (qt=1) masks them** (`****7711 RjExODI5MjI4MQ==`) and is billing-config-oriented (no market-value amounts) — wrong shape for the allocations table.

Confirms the port mapping: **use qt=5 (Allocation) for the allocations bronze table** (not the Snapshot). Folds into `docs/briefs/cot-bronze-silver-port-spec`.

---

## 5. Net impact on the port

| Gold component | v1 disposition |
|---|---|
| C_07 advisor_attribution | **SKIP** (no source data; was held pending §6.1 — now resolved to skip) |
| D_00c architect/implementor leaderboards | **SKIP** |
| D_01 partner_analytics **adv** view (architect cohort) | **SKIP** (the adv cohort only; aua/nna/geo/cla views stay) |
| A_00/B_/C_ dims, NNA (C_01), AUA, geo (client_state), client views | **PROCEED** unchanged |
| `office_mapping` config + Lusha pass | **NOT NEEDED** for v1 (no advisor/office dimension to map) |

This also **removes the Lusha-enrichment cost** from the COT estimate entirely (P3-prep had already flagged it as likely-unneeded; §6.1 confirms it).

---

## 6. Bottom line

§6.1 resolves to **Outcome B**: Cottonwood has no usable advisor dimension — the rich advisor fields are empty, and Rep Code is a 2-founder joint-coverage model with a third advisor under-tagged (only 2 new accounts, first seen 05/01/2026). The data is tagging-incomplete and non-segmenting, so advisor analytics (C_07 / leaderboards / adv-cohort) are scoped **out of v1** (revisit if tagging discipline matures). Everything else — AUA, NNA, geo, client — proceeds, and the qt=5/Allocation angle is confirmed for the allocations table. **The sole remaining gate on the P1 bronze build is cleared.** C_07 hold flips to "skip for v1."
