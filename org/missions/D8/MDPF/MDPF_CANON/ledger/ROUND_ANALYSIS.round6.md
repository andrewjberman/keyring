# MDPF_CANON -- ROUND 6, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~14:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 5588, `surprise-channel/adjudications/ADJUDICATION_v9.md` @5f5db8eebe. MAY-CLOSE. The issuer's packet is
`deliverables/2.0.0_SA_COO~D1/round6/ROUND6_DRAIN_END.md` @e647498179 (msg 5582).

## 1. Graded

- **TO-CN-f-1 AC4: MET** (D1-C-S67), on the CVO's re-runs after the first folded scheduled fire, 2026-10-14 13:30Z.
  - The fold readback passes 9 of 9.
  - R1: 0 model lines held by fewer than two firms.
  - R2: min_firms 2, detail from 2026-05-15, and a 264-character statement that names no model.
  - R4, R5 and R6: headline, identity and firm scopes are equal.
  - R9: the commit equals the package.
- **FWD-3: REALIZED, EXERCISED.** The bar (PRD DEC-7) is "that the reason is written and can be pointed at".
  - The reason is written in two places: `X2_GLOBAL_BASIS.md` (aggregation level, minimum firms, why no per-firm row survives) and the served object's own statement.
  - As of today's fire, the served object makes it TRUE: no combined line is held by fewer than two firms (R1).
  - The CVO's L9 read is the act the DONE WHEN names: someone asked what the combined figure reveals, and pointed at the written statement.
  - Moving the ledger's X2 row from OWED to GRANTED is Andrew's later acknowledgement card (DEC-7), not a gate on FWD-3.
- **The third arm (a refused day leaves the prior Global object's VersionId unchanged): NOT EXERCISED.** No one-firm as_of occurred. It is DRIVEN, not waited on:
  section 3, item 3.
- **FWD-1 and FWD-7** stand REALIZED. FWD-5 is in progress. FWD-2, 4, 6 and 8 are as in round 5. FWD-9 is the round-7 Trend grouping (CN-i-1).

## 2. Information for Andrew, no decision owed (the CN-f-1 pair's promise, line 33): what `/portfolios` shows since the 13:30Z fire

The fold was ruled by the cluster lead (fe9b (A)), and it moves the page by served DATA. Read by the CVO on the 10-13 as_of; the issuer's "Total Holdings 8,607 -> 8,607" was a
wrong-date read (row D1-S24) and is corrected here:
- **Total Holdings 8,607 -> 8,430 (-177).** The pair named -185; the 8-account gap is roster drift.
- **The five archetype cards together -$43.6M.** Intermediate -$21.3M/-183, Long -$18.2M/-160, Short -$4.0M/-23, Ultra-Long and Ultra-Short under $0.2M.
- **A new "Other Models" card: $69,190,304.67, 205 accounts.** The pooled lines held by fewer than two firms now sit here, as FWD-3 requires.
- **Trend:** 14 series -> 6, and the per-model history now starts 2026-05-15 (it was 2024-11-01).
- **Core quarter cells:** 10 of 20 are now absent (Q2 and Q3 for all five archetypes), because no two-firm history exists there.
- The headline AUA is unchanged on every common date (R4).

## 3. This seat's ARMED rows, ruled

1. **D1-W16-S2 and D1-W16-S4: on a day with no pool, the Other Models card shows stale dollars as current.** The rule is the same as SECHIST ADDENDUM 2: a carried value
   carries its date, or it is blank.
   - **Cell:** the aum-metrics frontier fallback stamps `as_of` on any carried Other Models value, and the card renders "as of <date>" when that date differs from the page's.
   - **Arms:** (a) the pool present today -> no stamp, value current; (b) no pool today -> value from the last pooled date, with the stamp; (c) no pooled date within 4
     calendar days -> blank.
   - It is a served change under its own pair; any card text is a client-facing portal rung under the push law.
2. **D1-W16-S5: the unfolded staged copy has unidentified readers.**
   - **Cell:** a READER CENSUS of the staged key: comp-pipescript consumers, the IAM grants on the prefix, and the S3 GetObject data events if the trail covers that
     bucket. The denominator is printed.
   - Any reader that reaches a partner-facing surface is re-pointed to the folded object under a pair. A census of zero readers is recorded, and the row disarms on it.
3. **D1-W16-S1, the refusal arm, DRIVEN:** one QA run of the gold consolidator over a COPY of the inputs with a single-firm pool planted, writing to a QA prefix only.
   - **Arms:** Global is refused WHOLE; the prior Global object's VersionId is unchanged (the served prefix is listed before and after: 0 writes); the run logs the refusal.
   - QA, never production evidence (CLAUDE.md). The organic one-firm day remains the negative arm, read when it occurs.

## 4. ENRICHMENT LIST (round 7, ONE issuance by `2.0.0_SA_COO~D1`)

1. The staged cells: **CN-h-1** (frontier counts), **CN-i-1** (FWD-9 Trend grouping) and **CN-j-1** (history leaf), plus the **D1-S23** repair (the equality tool hashes
   the working tree).
2. **The Other Models dated-carry cell** (section 3, item 1).
3. **The staged-copy reader census** (section 3, item 2).
4. **The refusal-arm QA run** (section 3, item 3).
5. **D1-S24:** `portfolios_card.py` defaults to the documented run date, and prints the date it read on its first line. A wrong-date read must be visible in its own output.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **Any client-facing `/portfolios` PROD push** that renders the "as of" stamp (section 3, item 1) waits on his word (CLAUDE.md Agent Autonomy).
- **The X2 register row OWED -> GRANTED** is his acknowledgement (PRD DEC-7). It is a card, not a gate.

-- 1.0.0_SA_CTO~DELL1
