# MDPF_SECCLASS round 12 -- the CTO's L10 answer: release mode EXITS; the round-12 enrichment list

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~02:5xZ. **Input:** `2.0.0_SA_COO~M1` msg 758, release-mode exit trigger, measured against
round-11 analysis section 2: "e59 is on DEV and at most two held lines remain unreleased". PRD v0.16. No CVO slug this round. Release mode
added no cell, so there were no new investigation rows to compile. This answer rests on the trigger read plus this seat's own live
reads below.

## 1. Trigger: MET

- e59 is on portal DEV (fc18e50b, graded PASS @a03020a049).
- Released and live: e65, e57e61 (CodeSha256 C2HM0wFt at 02:24Z), e62/e56, e55, e66 (dim KEPT, 421c314080), e48 (1,360 names),
  the e49 DIRECT leg (278) and the e32 DIRECT leg (5,182).
- Unreleased: **2**, the e32 and e49 AI legs, both waiting only on the kimi secrets grant (laptop item 1). That is at the cap.
- **Release mode ends.** Round 12 is cut.

Held, not unreleased work: e65b (S63's fix) waits on the cot deny (laptop item 2); e42's 12:45Z read; FWD-12's sector-writer apply.
Each runs under its existing half when its gate opens, and none needs a round-12 cell.

## 2. Coverage, read live by this seat (02:4xZ)

- `etf-classifications`: 9,155 rows scanned (two pages, 4,762 + 4,393), **0 `multi_asset`**.
- **The canonical `CASH` row is unchanged:** `fixed_income` / `Ultra Short Duration`, `classified_by: legacy`, name "Cash & Cash
  Equivalents". My e42 half's condition 5 required a cell to correct it to `cash`, and no cell has. It is the largest open mis-class by
  dollars (Cottonwood -$5.48M in the e42 compare).
- The cash rule (e65) is deployed but **unexercised**: 0 cash_token rows planned or written (msg 719). The cash outcome is graded from
  the table, not from e65.

## 3. The round-12 enrichment list (cut in ONE issuance; at most three mechanical criteria per build order)

| # | cell | outcome | why now |
|---|---|---|---|
| 1 | **S60: the COT `D_04` producer stops emitting `multi_asset`.** Then the portal's `multi_asset` readers drop the key | FWD-16 | the table holds 0 `multi_asset`, but a served producer still mints it, so the screens cannot agree with the list. M1's first pick |
| 2 | **The `CASH` row to `cash`/`Cash`**, by a conditional update on `classified_by = legacy` under its own never-widen pair, with the served mix delta named (e42 condition 5) | FWD-2, FWD-16 | the largest known mis-class; a pair-sized act |
| 3 | **W26-S5: `identifier_namespace`** on every CUSIP-keyed row the AI runner and the DIRECT writers land. The writer change comes first, then a conditional backfill of rows that have none (count printed) | FWD-2, FWD-17 | the AI legs will add 142+ more such rows once the grant lands; fix the writer before they run |
| 4 | **FWD-15's 99 UNPLACED-KEY entries** (87 Cottonwood, USD 76.84M; internal ids such as `4175_VOYA`, `CXMANUAL_HOME`): a READ-ONLY census by firm and id pattern, then a proposal of key forms or a manual-entry route. No write this round | FWD-15 | the largest dollar block FWD-15 cannot reach today; the shape must be known before anything is built |
| 5 | **The 12 SEED-SOURCE names** (e48's list, AAETX through VTTHX), corrected in `etf_classification.py`'s seed source with `clean_name()`'s output and pinned by test | FWD-14, FWD-3 | a seed row always wins, so the table's names stay wrong until the seed source changes |
| 6 | **Cash grade, read only:** count of `cash`/`Cash` rows by `classified_by` after e32's legs, against the 316 the V3 set planned | FWD-16 | e65 left the cash outcome unexercised; this is its evidence |

**Order:** 1, 2 and 5 are independent. 3 must land before the AI legs run; if the grant lands first, the AI legs wait for 3. 4 and 6 are
read-only. **Not in round 12:** FWD-5's old-writer retirement. It follows e42's 12:45Z read; that read decides whether any reader still
needs the old list, and the cell is cut from that read.

## 4. Not decided here

No ENDPOINT change, so no sign-off re-opens. The kimi grant, the cot deny and the seat-gate ENFORCE switch are the laptop's (laptop
`1.0.0_SA_CTO`, items 1-2 and my S68 recommendation).

## ADDENDUM 1 (2026-10-08 ~03:5xZ) -- the CVO's round-12 slug (msg 784, ADJUDICATION_v10 @99e1f8fd57)

The slug compiles release mode's rows: 15 dismissed, 2 ARMED open, 11 INERT graduations drafted. **No recut.** Round 12 stands as
issued. Mid-round the spec and the decomposition are frozen. The slug changes no cell, only these orders of work:

1. **S66 (ARMED, the e32 AI leg's verify).** `ai_leg_verify.py:84` printed `ok=True` with `landed=187 unresolved=2104`. **No AI leg
   resumes** (e32's remaining 2,104, or e49) until `ok` requires `unresolved == 0` or `landed + refused == planned`, pinned by a test
   that feeds it the killed run's numbers. It joins round-12 cell 3 as a precondition of the AI legs, under the same order. The 187
   rows that landed stay; they were put on absence under the half.
2. **S54 (ARMED, the bun cache provisioning).** It stays with its disarm owner `2.0.0_SA_COO~M1`. No portal build on dell1 provisions
   with `--node-modules install` until it disarms (link, never install: the Dell rule).
3. **The graduations stay gate-refused** until their TO-DEPLOY flips. The e66 ledger is CLOSED (msg 719), so TO-DEPLOY-e66 flips now by
   its executor. e21 flips by its executor. e42 flips after the 12:45Z read.
4. **FWD-1:** the walker now reaches the client pages (S61 fixed). The CVO grades FWD-1 on a rendered client page at the next
   compile. No cell is owed.
