# IRPT_DASHBD -- ROUND ANALYSIS, round 28 (B + BD)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~18:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1427), ADJUDICATION_v14 @d4b5aafcd8, and REMEDIATION_v12.
- 3 of 3 orders complete (DB-b-47, DB-b-48, DB-b-49). MAY-CLOSE. ARMED 0.
- W27-S1 is dismissed.
- W27-S2 (`~D2`) and S34 (this seat) are OPEN.

## 1. State

- **FWD-8, the split tie-out (DB-b-49), is BRANCH B** by the rule stated before the run: tied_both is 431 of 2,299, against a threshold
  of 1,149.5.
  - Left half (start to 2025-01-08): 2,220 of 2,299 tie.
  - Right half (2025-01-10 to end): 465 of 2,299 tie.
  - So the 2025-01-09 closure day is not the cause. Opal and BD diverge AFTER it.
- **S34 qualifies that reading.**
  - BD's own two halves, chained, fail to reproduce BD's full-period figure on 440 of 2,299 accounts (worst gap 724.16 pp).
  - For those accounts, a right-half miss is not yet an Opal-versus-BD finding, so no Opal repair is cut from branch B until they are
    classed. This is the CVO's decision, and this seat concurs.
- **DB-b-47:** the realized-lot key is `lot_id` plus quantity, unique on 175 of 175. **DB-b-48:** the lots stage is batched with peak
  memory flat at about 1.7 GB; at batch 250 it runs 905.7 s, over the 900 s limit (W27-S2).
- **No vendor call is owed in round 29.** Both new items read the 2,299 split objects and the earlier full-period pull, which are already
  landed. A further BD pull, such as a date-bisection, would need Andrew's per-use word. It is not proposed here.

## 2. ENRICHMENT -- round 29, ONE issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Class S34's 440 non-recomposing accounts** | (1) each of the 440 is assigned one cause class, with counts summing to 440. Candidates: an account opened or closed inside the segment, a fee or basis difference between the two pulls, a missing or zero half, the full-period figure annualized, and other (named). (2) the 724.16 pp account is traced, with its three BD figures printed (counts and percentages only, no client names). (3) the overlap of the 440 with the 1,834 right-half misses is printed: how many misses remain once the 440 are set aside. | LOCAL |
| E2 | **The shape of the right-half gap, for the misses outside the 440, from Opal's side only** | (1) the signed gap's distribution (median, p10, p90), and whether it scales with the right half's length; (2) the gap's correlation with Opal's flow, fee and income components over the right half, by account, with the top driver named; (3) a control: the 2,220 left-half ties show none of that driver's signature | LOCAL |
| E3 | **W27-S2: the lots stage under the 900 s limit at full scale** | (1) a batch size whose measured full-run time over the 7,604 accounts is at most 750 s, with peak memory printed; (2) the chosen size is set in the stage's configuration, and one full run reads under 750 s | LOCAL |

E1 and E2 together decide where round 30 cuts: an Opal repair, a BD-side explanation recorded as a reason (FWD-8 accepts "every day
they disagree carries a stated reason"), or a priced vendor bisection put to Andrew.

-- 1.0.0_SA_CTO~DELL2
