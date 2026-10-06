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

## ADDENDUM 2 (2026-10-06 ~21:0xZ) -- FWD-12's re-run half is HELD; Andrew questions the button (CRO~Z msg 30295)

`4.0.0_SA_CRO~Z` reports (its notes' ADDENDUM 1 @225555fa61) that Andrew, at the CRO~Z terminal, asked why a re-run button exists
at all, given a scheduled morning job and no intraday data. He has NOT ruled.

- **HELD:** ADDENDUM 1's FWD-12 re-run cell (the market_data re-run, the cost gate, the consumer wiring pair) is NOT cut until
  Andrew answers.
- **NOT held:** FWD-12's provenance half (round 76 az-2, `input_provenance`), and all of FWD-20.
- **If Andrew retires the re-run:** FWD-12's DONE WHEN loses "a re-run of one input alone". That is an ENDPOINT amendment (PRD
  addendum, with the ratified-text half re-signed by the CVO). The `/refresh` "declared" no-op (`scoped_amgt.py:6859-6876`) is
  still retired, because a button that does nothing breaks PRD `:1393-1395` either way.
- **This seat's recommendation to Andrew is to retire it.** The inputs refresh on the scheduled morning pull and carry no
  intraday data, so a press returns the data already served. The one case a press would help is a failed or refused scheduled
  fire, and that is an operator recovery (round-37 ruling 3), not a page action.

## ADDENDUM 3 (2026-10-06 ~21:2xZ) -- Andrew's four rulings applied (record `ANDREW_DIRECT_20261006_211xZ_ALL_RECS_APPROVED_CTOZ_OPEN_CALLS_FOUR_CARDS.md`)

1. **FWD-12's re-run half is RETIRED** (PRD v0.41 ADDENDUM E; the CVO re-signs the ratified half). ADDENDUM 2's hold ends as a
   withdrawal. ADDENDUM 1's re-run cell is struck. One cell replaces it: remove the `/refresh` "declared" no-op and its page
   control. FWD-12 is graded on the provenance half alone (az-2's `input_provenance`, read against `/freshness`).
2. **Three one-time Bloomberg research pulls are authorized.** They are cut by `2.0.0_SA_COO~Z` in its next issuance, and each is
   a SERVED act under its own never-widen pair:
   - **The segment pull for the 83 names** (row Z-W240-S1). It serves FWD-1.
   - **The executive-officer pull for the 84 names** (row Z-W227-S1).
   - **FWD-2's first uncovered-name pull:** one real name the firm has never covered, pulled and read.

   **Conditions, as approved:**
   - They run AFTER the firm's 7:00 AM ET vehicle run on the day they run.
   - They run ONE AT A TIME, each finishing and being read before the next starts.
   - Each states its Bloomberg call count before it runs.
   - A capacity refusal stops the sequence and is reported. It is not retried the same day.

   They are scripted pulls under `integrations/bloomberg/research/` (research is outside the no-modify order, record
   `ANDREW_DIRECT_20261006_201xZ_...`). No agent signs in to the Terminal: a signed-out Terminal is Branch C, and nothing is pulled.
3. **FWD-14's owner is Andrew, for both lists** (the publishers the page may quote; the company-to-social-accounts map), until
   he hands either on. One cell:
   - Each list carries its owner and its last-reviewed date.
   - A list past its review age reads OUT OF DATE on the page (the `/freshness` page is its home), naming the owner.
   - That on-page statement is the "somebody is told". **No email, SNS or alert is built** (CLAUDE.md section 5 moratorium).
   - Proof: a planted stale review date turns the line on, and a current one turns it off.
