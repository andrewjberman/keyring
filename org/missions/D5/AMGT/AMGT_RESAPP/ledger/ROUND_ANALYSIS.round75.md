# AMGT_RESAPP -- ROUND 75 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~13:3xZ

**Input:** CVO slug msg 30043, `surprise-channel/adjudications/ADJUDICATION_v90.md` @10d8b331a8 (57 lines, read in full;
precondition MET). Packet: `round75/DRAIN_END_PACKET.md` @85cf2591dd. Deployed: `D29LJCXh`, with the `/freshness` snapshot, its grant
and its daily schedule (CTO half @452acb4e68).

## 1. WHAT THE ROUND DELIVERED

6 of 6 orders are terminal; the issuer's run reads 16 of 16 YES.
- **The print:** per-figure dates, with 0 false "as of" stamps and "Printed" once; the drafted thesis, risks and recommendation.
- **`/freshness`:** served from one snapshot (cold 825-980 ms, from 7.5 s), with the daily writer ENABLED.
- **The names-phase cut.**
- **Segment labels and table passages.**
- **The walk.**

**Round 75 is CLOSED.**

## 2. THE BOARD (CVO L9): REALIZED 20 of 30

Newly REALIZED: **FWD-5** (the BA print: Lato, 0 false stamps, the drafted thesis as on the page). The 10 NOT REALIZED, by cause:

| cause | FWD |
|---|---|
| **built; waits only on Andrew's portal DEV push** | **7** (the page: a 2.0 s first paint, real staleness); **18** (the driver-chart passage); **1** (segments). All three were walked on a local merge, and the CVO grades on the deployed page per v0.40 |
| **NOT YET BUILT** | **16** (the top of the page: the company in one line plus the day's items); **12** (each input's provenance, and a re-run of one input alone); **20** (the house forward FCF forecast and its Divergence) |
| needs a source or Andrew | **11** (social discussion: no admitted social source); **2** (the uncovered pull, a vendor use); **14** (list owners); **37** (a qualified wait) |

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **The DEV push** | The `/freshness` page candidate `6de76f0509` gets **this seat's review FROM A RENDER** (my rule since round 73). It then goes to Andrew as ONE DEV push with DSGN rounds 43+44 (`1d6d2573`, approved @0c9b9db840). After the push, the CVO names companies per v0.40, and FWD-7, 18 and 1 are graded on DEV. |
| 2 | **FWD-16: buildable now, the NEWS half** | Round 76 builds the top of the page, above the tabs and beside the ranked list: the company's one-line description, and the day's news items from the served gold mentions (each with its url since HARVST rebuild #7), newest and most-discussed, each one followable. **The social half waits on FWD-11's source** and is stated on the page as "no social source is admitted yet", never left as an empty box. Page work goes to DSGN; served data to RESAPP. |
| 3 | **FWD-12 and FWD-20 are DESIGN FORKS** (self-drive Step 1) | **FWD-12's per-input re-run** is a write path started from a page (auth, cost, who may press it). **FWD-20's house forecast** is a methodology (an independent FCF projection from filings and history). Both go to `4.0.0_SA_CRO~Z` for the estate's past patterns, and this seat rules each on the tick the research lands. **FWD-12's provenance half** (where each input came from, when it last ran, whether it worked) is already served by `/freshness` and the ledger, and goes into round 76's page cell. |
| 4 | **109 OPEN owned remediation rows unmoved for 2+ rounds** (disclosed by the gate) | **A round-76 triage cell**, in the same shape as ETFS_RIVALS' C-S41: each row gets a citing row that cuts it, closes it with its evidence, or names its blocker and owner. A count that only grows is not a backlog anyone is working. |
| 5 | **The cold read** (still above about 2 s; locally 3.5-4.0 s after the names cut) | One more phase-table read on `D29LJCXh` in round 76. If no single remaining phase above about 1 s is cuttable, the free cuts are exhausted. Then provisioned concurrency is **this seat's recommendation** on Andrew's list (spend), with the phase table as its evidence. |

## 4. ENRICHMENT LIST (round 76, ONE issuance by `2.0.0_SA_COO~Z`)

1. **FWD-16, the news half:** served data for the top of the page (description plus the day's items with urls).
2. **FWD-12, the provenance half:** served per input.
3. **The remediation-row triage** (ruling 4).
4. **The cold-read phase table** (ruling 5).
5. **The redeploy, under a pair.**
6. **The walk,** after the DEV push: FWD-7, 18 and 1 on DEV.

**DSGN round 45, ONE issuance by `2.0.0_SA_COO~D`:** the top-of-page band (FWD-16 news half) and the provenance panel (FWD-12), drawn
from round 76's served fields.

## 5. ACTS FOR ANDREW (cited)

- **The portal DEV push** of DSGN rounds 43+44 plus the `/freshness` page, once ruling 1's render review passes (product files; PROD is his
  separate word).
- **Provisioned concurrency,** if ruling 5 finds the free cuts exhausted (spend).
- **Vendor uses:** FWD-2 (the uncovered pull), Z-W240-S1 (segments for 83), Z-W227-S1, and any social source for FWD-11.
- **FWD-14's list owners** (C-NO-CONTACT). **The walker accounts.**

## ADDENDUM 1 (2026-10-06 ~18:1xZ) -- ruling 3's two design forks, ruled on CRO~Z's pattern notes

**Input:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DESIGN_FORKS_FWD12_FWD20_PATTERNS_20261006.md` @e9a0f5b32e (msg 30179).
The pause lifted with the Bloomberg hold (Andrew-direct @8555ce7e12). Both forks are cut into the next RESAPP issuance by
`2.0.0_SA_COO~Z`, after round 76.

**FWD-12, re-running one input from the page: the AMGT pull shape, keyed per (security_key, input_class).**
1. The flow: JWT route -> enqueue -> status object REQUESTED -> one SQS send -> the class's registered stage runs where its source
   lives (the box) -> the page polls the status object.
2. **`ledger.rerun`'s registry is the one press list.** A class with `stage: None` renders its refusal with the reason, never a
   button (PRD `:1393-1395`).
3. **Three gaps close in the same cell:**
   - (a) the role check is server-side and is the same predicate the browser uses;
   - (b) one run in flight per (key, class), by a conditional write on the status object, which also retires `record_run`'s
     unlocked read-modify-write;
   - (c) a per-class cost gate, on the YCharts consent pattern, which defaults to REFUSED-with-reason.
4. **v1 is market_data only.** The other five classes refuse with their reasons. The `/refresh` "declared" no-op
   (`scoped_amgt.py:6859-6876`) is retired in the same cell.
5. Consumer wiring and the `sqs:*` grant are a new never-widen act, under their own pair (the round-12 carrier sign-off forbade
   both).
6. **Reserved to Andrew, and the cost gate stays closed until he answers:** who may press (internal analyst, or admin only); and
   whether a page press counts as his per-use word for a Bloomberg pull. The cell builds and proves the path with the gate
   refusing, and a plant opens it in QA only.

**FWD-20, the house forward FCF forecast: CRO~Z's trailing-trend v1, accepted.**
1. The model: per name, annual, FY1-FY3, FCF = revenue x FCF margin.
   - Revenue grows at the median of the name's last 3-5 annual changes.
   - The margin is the trailing median of FCF / revenue.
   - Both come from the model block's reported history.
   - No consensus field is read by the producer (the 09-15 adjudication `:59-61`).
2. **D runs through the existing `divergence.py`** against `BEST_ESTIMATE_FCF` FY1.
   - The sd(D) >= 0.25 gate runs before anything is served (PRD `:1400-1408`). A name short of history is ABSENT with its reason.
   - **Added:** the producer also prints the cross-sectional correlation of house FCF to consensus FCF, as a reported figure
     beside the gate, not a gate. The 0.25 floor catches a near-zero spread only, and CRO~Z's caveat is that a trailing
     trend can track consensus without being seeded from it.
3. **The filing-reference gap: option (a) for v1.** A driver's reference is the Bloomberg reported fiscal period plus its
   announcement date.
   - It is stored under a field that names it as that (`source: bloomberg_reported_period`), never labelled as a filing id,
     so a consumer can reject it.
   - (b), an EDGAR XBRL companyfacts pull, is the enrichment. It is egress off Opal infrastructure and needs Andrew's word.
   - The PRD text at `:703-733` ("the filing it came from") is met in v1 by the reported period, under that label. The
     CONTRACT wording moves at this round's PRD addendum.
