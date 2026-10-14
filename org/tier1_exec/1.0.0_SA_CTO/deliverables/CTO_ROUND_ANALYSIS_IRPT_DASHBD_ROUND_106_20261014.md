# CTO ROUND-106 ANALYSIS -- IRPT_DASHBD -- answering the round-105 L10 slug (2026-10-14 ~14:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_105_L9_GRADE_20261014.md` and
`surprise-channel/adjudications/ADJUDICATION_v65.md` @c196c507a8 (3.0.0_SA_CVO~DELL2 msg 7682), on the drain-end
`deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND105_B_DRAIN_END_20261014.md` @220bdbd631. **No PRD addendum.** Issuer: `2.0.0_SA_COO~D2`,
ONE issuance. **Thread (O3):** one 49 Financial account as the default performance report, with nothing that misinforms a client.

## 1. Rulings

| item | ruling |
|---|---|
| **DB105-2-J1 FAIL (narrower)** | Accepted. Round 104's counts 2 and 3 are fixed, and so is count 1 on the Activity Summary. Two instances remain: the p.7 household Net Gain, and the p.2/p.5 allocation chart notes. |
| **Why the cross-table rule missed p.7: it is a FORWARD LIST** (6 hand-picked pairs) | Rule 24 (i): coverage is hunted by subtraction from a denominator, never by a forward list. **The rule is rebuilt over the whole document.** The denominator is EVERY absent cell, keyed by its contract member, entity and window. For each one, the rule searches EVERY printed cell in the rendered document for the same key. A hit is a FAIL. The check prints the denominator (absent cells scanned) and the count of keys it could not map, and an unmapped key is a FAIL, not a skip. It includes a planted mutant: one absent cell whose figure prints on another page. |
| **An absent CHART whose values print** (p.2, p.5) | A chart is not a figure. Its absence takes no `kind`, and it never claims "needs more history". If its values print elsewhere, the note reads "Chart not drawn in this report; the values are in the table on page N", with N computed. Otherwise the chart's slot is dropped. The whole-document rule above covers chart notes too: a chart note that names a reason while its values print is a FAIL. |
| **The split columns** (Contributions, Withdrawals, Income; the CVO's reading) | Their kind is `NO_SOURCE_YET`, not `INSUFFICIENT_HISTORY`: Opal does not split Net Additions yet, and Net Additions prints. The words say that ("Opal does not split net additions into contributions, withdrawals and income yet."). |
| **W167-S6** (a dash with no footnote for a window the account did not span) | A dash means only "not held" (the contract's print rule, round 105). A window the account did not span is an absent form with its own words, never the dash. It is in the same render cell, with a test. |
| **The disclosure page** | Still a release gate on Andrew's call `dell2-20261014T123227Z-a252`. It is not graded. |
| **ARMED 10 to 6** | The 6 that remain stay with their owners as ADJUDICATION_v65 states. W158-S1, S4, S6 and W167-S3 are dismissed on the owners' disarms. |

## 2. Round-106 cells (ONE issuance; LOCAL)

1. **Wire the DB-b-204 model-windows reader into the builder** (it replaces `~159`'s model_series). Re-render 49 Financial and print
   how many of the 32 benchmark members fill. (Answered to the issuer in msg 7681.)
2. **The render remedy (J1 re-grade, the CVO's).** The chart notes, the split-column words, and the W167-S6 window words.
3. **The whole-document absent-vs-printed rule**, replacing the 6-pair rule, with its denominator, its unmapped count, and the planted
   mutant. This is the mechanical half of J1, so a class of defect the CVO had to find by eye becomes a check.

## 3. Behind the thread

Unchanged from round 105: Cottonwood (silver stops 2026-06-23; ADVI_COTBKF's input), then Inflection. DB-b-183 (FDRXX) is applied.

-- 1.0.0_SA_CTO~DELL2
