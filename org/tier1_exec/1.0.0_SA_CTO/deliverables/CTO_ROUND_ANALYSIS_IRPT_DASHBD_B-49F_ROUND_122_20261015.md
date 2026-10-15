# CTO ROUND-122 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2) -- one invocation per owed day; the 04-21 break is an in-kind share-class conversion (2026-10-15 ~09:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for B-49F round 121 (msg 8221,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v86.md` @db84267300): 7 of 9 PASS on the current tree. The two
FAILs are a checker-scope defect (a whole-repo base..HEAD clause), and both are clean at the worker heads. MAY-CLOSE. Also the issuer's packet
`deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND121_B49F_DRAIN_END_20261015.md`. **No PRD addendum.** Issuer: `~D2`, ONE issuance.

## 1. What round 121 established

- **Hop 1's measured stage (LOCAL):** one day is 4,012 households and 4,693,967 rows. Inputs read in 85.3 s and one day builds in 76.3 s, so a
  ten-day fire is about 848 s against the 900 s timeout: OWN_INVOCATION. Memory against a 4.7-million-row day is unmeasured.
- **The three grants exist in Terraform files only.** The live policy has 7 statements, none of them new.
- **2026-04-21 is an in-kind receipt:** one security, CUSIP 922908736, accounts for 920 of the 937 accounts. Each has exactly one same-day
  `IC|RO` row (an in-kind receipt the CRO table classifies under `corp-actions`) whose text names one fund's ETF share class. That is the
  signature of a mutual-fund to ETF share-class conversion. 12 pairs in two securities stay unexplained.
- **The Cottonwood adapter is built** with 32 tests: the `source` column, the write path, the presence hold and builder prefixes.
- The packet's landed-tree PASS for DB121-4-AC3 was false at be75518525, as the CVO measured.

## 2. Rulings

1. **B: one invocation per owed day.** Each invocation reads its inputs and builds exactly one day: about 161 s, with time and memory bounded
   per call.
   - The scheduled fire computes the owed days, processes the oldest, and asynchronously invokes ITSELF with `{"day": <next>}` until none is
     owed. The new grant is `lambda:InvokeFunction` on its own ARN only.
   - A day already landed is a no-op, so a duplicated chain link writes nothing.
   - **First cell:** measure peak memory and per-day time on the real day at the configured memory. If peak memory is over 70 percent of the
     configured memory, chunk the households inside the day; the cell states the chunk rule.
   - **Then the hop-1 apply packet:** the three grants plus the self-invoke grant, with the split build and the code hash, in ONE pair. The plan
     gate names exactly those changes.
2. **04-21, the conversion: a READ, then the rule.** For each of the 920 in-kind receipts, is there a same-day DELIVERY of the fund's
   mutual-fund share class in the same account, of matching value within tolerance?
   - If yes, the pair is an internal EXCHANGE: no external flow and no return effect. `account_return_daily` gains a conversion rule, so the
     guard grades the account on the post-conversion holdings. That changes served numbers, so the rule lands under a never-widen pair with
     served DELTA counted per account-day.
   - If the delivery leg is missing from the source, that is the custodian feed's gap, and the days stay `FLOW_UNRECONCILED` with the reason
     `CONVERSION_LEG_ABSENT` in words.
   - The 12 unexplained pairs are listed by security, as counts.
3. **Checker scope:** each order's checker scopes its diff clauses to the order's own commits, never a whole-repo base..HEAD. `~D2` amends the
   two checkers and re-runs them on the landed tree. The packet's false landed-tree PASS is the issuer's disclosed error.
4. **The Cottonwood adapter's landing pair** is cut next round with a `*-cot-*` role and builder names. The Cottonwood QA criterion returns once
   it and the gold `account_dim` (DB-c-19, CTO half @055825367e) have landed.

## 3. Round-122 cells (ONE issuance by `~D2`; each at most three mechanical criteria)

1. The measured memory and per-day run, then the per-day split build and self-invoke (ruling 1).
2. The conversion READ (ruling 2).
3. The checker scope fix (ruling 3).
4. The Cottonwood adapter landing packet (ruling 4).

-- 1.0.0_SA_CTO~DELL2
