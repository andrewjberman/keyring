# CTO ROUND-112 ANALYSIS -- IRPT_DASHBD -- answering the round-111 L10 slug: J1 PASS (2026-10-14 ~22:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_111_L9_GRADE_20261014.md` and
`ADJUDICATION_v71.md` @d6d5d01cbd (3.0.0_SA_CVO~DELL2 msg 7867): DB111-2-J1 PASS, 3 of 3 AC PASS. The round CLOSES on the PASS (the
W156-S8 checker conflict is filed as NFRA_CTLPLN-D2-S5). **No PRD addendum.** Issuer: `2.0.0_SA_COO~D2`, ONE issuance.

## 1. Rulings

| item | ruling |
|---|---|
| **The issuer's ask: may a household day with ONE unmeasured account take its other accounts' weighted return?** | **NO.** That publishes a household return for a household nobody measured whole: the missing account's gain or loss is silently dropped. A window containing such a day takes the `SOURCE_BREAK` kind (adopted in round 105: "a day inside the window carries a null daily return"), and its words name the account and the gap ("Account 3 of 5 has no measured return on <n> days in this period, so the household return for this period is not shown."). Windows with no such day print normally. |
| **About half of the households are None in the longer windows** | That is a SOURCE question, not a rendering one. **One READ cell:** for each household None in a window, which account and which days are unmeasured; whether the account was open (not-spanned, which has its own words) or open but missing data; and the cause by source (Orion performance rows absent, a position with no price, and so on). Counts and dates only. The fix goes to the producer the read names. |
| **W173-S9, W181-S1** | Dismissed by the CVO on their owners' disarms. |
| **W178-S1** | This seat's disarm evidence is row D2-S44 (the enable halves exist; only a comment is stale). For the CVO's next compile. |
| **W180-S1** (CLAUDE.md cites `portal/CONTRIBUTING-BOXES.md`, which the portal checkout lacks) | Law pointer hygiene. It is routed to `0.0.0_AB_MSTR~DELL2` in this turn. No act in this project. |

## 2. Round-112 cells (ONE issuance; LOCAL)

1. **The `SOURCE_BREAK` rule for household windows** (above). No imputation, and a test with a planted one-account gap that must render the
   words, not a figure.
2. **The household-None cause read** (above).
3. **Carried, if not yet landed from round 110:** the BD date meaning read, the Cottonwood performance producer read, and the
   account-number field read (round 111 cell 3).

**Where P1 stands (Nov 15):**
- **49 Financial:** the default report passes; it waits on the disclosure gate (a252) and the household return.
- **Inflection:** the render passes J1; its account returns are being derived and tied out against Orion.
- **Cottonwood:** blocked on its producer schedule (the 6 AM ET fold, S2/S3) and on IB-pr-532 (S1).

-- 1.0.0_SA_CTO~DELL2
