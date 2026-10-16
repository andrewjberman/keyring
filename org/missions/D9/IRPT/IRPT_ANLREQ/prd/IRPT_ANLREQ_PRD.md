# IRPT_ANLREQ -- one Analysis Request end to end: the Ticket Center form to a finished package on the same open ticket

```json
{
 "project": "IRPT_ANLREQ",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.22",
 "step": 4,
 "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md@2b21a349d1",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

Author `1.0.0_SA_CTO~DELL2`. Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_ANLREQ_20261009.md` @670ded26ed.
Registered @07d6672dbe, under D9/IRPT, placement DELL2.

**Interim driver:** `2.0.0_SA_COO~Y2` (CVO verdict msg 1889), under `/closer`.

**Andrew's words:**
- 2026-10-08 ~22:3xZ @2b21a349d1;
- the build word, given as this seat's discretion, 2026-10-09 ~03:4xZ @35fabf20c8.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  One Analysis Request goes from the Ticket Center form to FOUR attachments on the same open ticket, with no person in between
         DONE WHEN  EXERCISED -- on DEV, a SYNTHETIC Opal staff user (minted and deleted under a never-widen pair) signs in, opens the Ticket
                    Center (shown to Opal users only), CHOOSES the partner firm the request is filed under, fills the
                    Analysis Request form and uploads a holdings CSV or XLSX. The form carries the variant chosen
                    (Overview, Comparison, Multi-Comp) and the report produced is that variant, the Opal-model checkboxes and other tickers. Every
                    downstream hop binds to the chosen firm. Nobody touches anything after Submit. The still-OPEN ticket then carries four attachments, each opened from the ticket
                    page by an Opal person: (1) the original holdings upload, (2) the form selections as filed, (3) the Opal-generated report (the Opal
                    producer, not YCharts), (4) the AI commentary as a STANDALONE branded Opal PDF, marked DRAFT. A partner-firm filing (Alyssa's first real request) grades it again (the
                    organic arm, never the gate; it waits on the Ticket Center being shown to client users)
         ACCEPT     an Opal person opens the still-open ticket and finds the four items, without asking anyone and without anyone having forwarded
                    a file; each of the four is its own attachment (the commentary is not a page inside the report PDF)
         SOURCE     Andrew 2026-10-08 ~22:3xZ; Andrew's dell2 voice memo 2026-10-13 ("they should see the CSV or XLSX that the advisor uploaded.
                    They should see the form ... the generated report ... the commentary that we AI generated ... That is the deliverable");
                    call 2 approved ~17:4xZ (synthetic advisor); pivot direction XB-20261013T180328Z-d4a5 O1; the filer is re-pointed
                    to Opal staff by Andrew-direct 2026-10-14 ~15:2xZ (ADDENDUM v0.6)

  FWD-2  The form fits the request and catches a bad request before it files
         DONE WHEN  EXERCISED -- the form offers the analysis types and the Opal models as checkboxes plus a field for other ETFs; a mistyped ETF is caught
                    and a correction offered, and a swap is accepted, before the ticket is created
         ACCEPT     a person who types an ETF wrong is told before filing and can pick the right one; a holding that is unknown or cannot be priced is
                    kept if Opal or yfinance can price it, and otherwise replaced before filing by a proxy ETF chosen from Opal's own registry for
                    its asset class and sub-class (the security swap, C-SWAP), never by an unverified guess; the advisor sees and can change it
         SOURCE     Andrew ("typo check and swap ability completely ironed out"); CRO trace hops 1-2

  FWD-3  The investment commentary is written from the report itself, and stays a draft until a person sends it
         DONE WHEN  EXERCISED -- the commentary for FWD-1's request is drafted from that report's key surfaces (abstract fields only, no client identity),
                    rendered as a standalone branded Opal PDF marked DRAFT, and opened from the ticket
         ACCEPT     the commentary talks about this report's portfolio and comparison, not a generic text; it says DRAFT; nothing is sent to an advisor
                    without a person
         SOURCE     Andrew ("running over key surfaces in that report to feed the investment commentary summary"); NFRA_TRNSPT FWD-10, C-KIMI

  FWD-4  A broken hop never silently stops the request
         DONE WHEN  EXERCISED -- a request is driven through each failure on purpose (the generator down, the commentary refused, the attach refused), and
                    each time the ticket says which step failed and what happens next
         ACCEPT     an Opal person looking at a stuck request can tell from the ticket alone where it stopped and why; no request sits silently unfinished
         SOURCE     Andrew ("agents ... get held up on some random block ... and then they just stop working"); CRO no-stop rule

  FWD-5  Another firm never sees the request, the package or the commentary
         DONE WHEN  EXERCISED -- a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand
         ACCEPT     someone signed in for a different firm is refused the ticket and every file in its package; a statement that it is refused does not count
         SOURCE     TCKT_VNEXT FWD-2; C-PACKAGE firm check; "ALL never admits"

  FWD-6  The Analysis tab is the manual path for the unusual case
         DONE WHEN  EXERCISED -- one request the automatic path cannot finish (a swap the form cannot express) is completed by a person from the Analysis
                    tab, and the package lands on the same ticket
         ACCEPT     an Opal person finishes an unusual request by hand from the Analysis tab, and the ticket ends up the same as an automatic one
         SOURCE     Andrew ("frontend work on the actual Analysis tab will be completed after the fact ... only for unusual cases")

  FWD-7  An Analysis Request runs end to end on Opal's data, with prices taken from Yahoo first and YCharts second, per symbol
         DONE WHEN  EXERCISED -- FWD-1's request is traced hop by hop: the typo check, the swap, the report and the overlays come from Opal's own data;
                    each security's price comes from, in order: the estate's own stores where they hold it; Yahoo (yfinance, cut at T-1); YCharts
                    through the stored session, one symbol per call; then the backend replacement (C-SWAP); else the report runs without that
                    security and says so in words. Bloomberg is not in this chain. No YCharts report, figure or PDF is used
         ACCEPT     the finished package's trace shows each price with its source as a claim field (estate store, yfinance, ycharts or
                    replaced), every YCharts call is for a price only, and a security Opal could not price is named in the report
         SOURCE     Andrew 2026-10-09 ~04:4xZ ("I do not think we actually need YCHARTS for anything"); relaxed for pricing data by Andrew-direct
                    2026-10-14 ~15:5xZ ("I am ok with a single data call to YCharts for pricing data."), SUPERSEDED by Andrew-direct
                    2026-10-14 ~17:5xZ ("we use Yahoo as first round pick, we use Ycharts as second round pick")
```

## 1. What exists (the CRO's nine-hop trace @9076346655, plus this session's measured changes)

| Hop | Trace state | Since the trace |
|---|---|---|
| 1. Form | MISMATCHED | TCKT_VNEXT's Analysis Request form exists. It has no Opal-model checkboxes and no other-ETF field |
| 2. Check and swap | INCOMPLETE | the upload door's findings exist. There is no typo correction or swap in the form |
| 3. Ticket created | WORKS (0 filed) | TCKT_VNEXT FWD-1 has never run end to end. A seat arm is being re-cut to one firm (msg 034330Z) |
| 4. Trigger | MISSING | H1 (the report's READY event to the commentary Lambda) is ruled for ~P2 after IB-pr-383 |
| 5. Generation | INCOMPLETE | the Opal engine's brand is live in st27 (Andrew-only). The seat F1 runs on 49financial under st28 |
| 6. Commentary | MISSING | NFRA_TRNSPT FWD-10: the drafter and the svc-commentary ticket write are built. The Lambda's apply pair waits on round 17 (commentary.tf) and ~P2's composition read |
| 7. Package PDF | MISSING | the Opal engine's HTML layout is the one renderer (the CRO's close). It has no commentary section yet |
| 8. Attach to the ticket | MISSING | `POST /tickets/{id}/package` is LIVE and refuses every caller (`package_principal` is empty), per C-PACKAGE |
| 9. Ticket page | MISSING | the ticket page shows the draft and the package refs as text (portal 44c31b8e on DEV). There is no signed-link open |

## CONTRACTS

| Contract | Owner | Text |
|---|---|---|
| C-ONE-JOURNEY: FWD-1 is driven, never waited on | this project | Round 1 decomposes over the nine hops of FWD-1. A hop that waits on another box parks that ONE hop in STATUS.md with its owner and un-park condition, and the driver moves to the next hop in the same tick (the CRO's no-stop rule). Alyssa's own filing is the organic arm, never the gate; it waits on the Ticket Center being shown to client users. |
| C-SOURCES: contracts are cited, not copied | this project | C-PACKAGE, C-ONE-DOOR and C-TYPE live in `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`. C-KIMI and C-WIPE-GATE live in `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`. The upload door and E5 live in IRPT_BCKEND. This PRD cites each at its path and never restates it, so each rule has one home. |
| C-PACKAGER: one principal attaches the package | this project | The package is four STANDALONE items: the original holdings upload, the form selections as filed, the Opal report, and the AI commentary as a standalone branded Opal PDF marked DRAFT. Its last hop attaches them after the commentary. The combined package PDF (the report with a commentary page inside) is never posted as an attachment. That hop's principal is the ONE `package_principal` named in the type definition. It is firm-bound by its PROFILE row (internal-caller narrowing, IB-pr-387), and never ALL. |
| C-FIRM: firm reach | consumed | Every principal on the journey reaches exactly the request's firm: svc-commentary by tenant-bound `get()`; the packager by its row. FWD-1's filer, an Opal staff principal, CHOOSES the firm from the served partner tenants, and the choice must be in its explicit `allowedFirmIds` (the CREATE path's server check); every hop binds to that choice. A partner-firm user's firm is the signed-in user's and is never a choice. ALL never admits and never substitutes for the choice. |
| C-ABSORB: what MOVES into this project (the brief's "compress into ONE project") | this project | **Moves in, owned and issued here.** (a) IRPT_BCKEND `~Y2`'s Analysis lane: the upload door and resolution `infra/aws/lambda/investor-reporting/intake/{uploads,upload_resolution,upload_suggestions,resolution_kimi}.py`, the security swap (today `KIMI_WEB_SEARCH_UNVERIFIED`, `resolution_kimi.py:159-165`; candidates from `etf-classifications`, ex-IRPT_YCDGEN FWD-16), and generation submit. (b) IRPT_YCDGEN whole: the Opal engine and brand `ycharts/generate/{resident_worker,durable_job,comparison_catalogue,publication_worker}.py`, `ycharts/research/{opal_producer,layout_overview}.py`, report types and vendor retirement. (c) NFRA_TRNSPT FWD-10 and FWD-11: the commentary drafter `data/transcripts/scripts/commentary/*` and its Lambda `commentary.tf`. (d) The READY event H1 (from `~P2`'s queue). (e) TCKT_VNEXT's Analysis Request scope: the `analysis_request` type definition, `POST /tickets/{id}/package`, `portal/src/pages/TicketCenter/` Analysis Request parts. **Keeps the remainder:** IRPT_BCKEND (`~P2`: auth, routes, directory, holdings, `irpt-export-render` as the shared renderer); NFRA_TRNSPT (FWD-1..9: transcripts, company read, mail); TCKT_VNEXT (non-analysis types). **Lanes:** `~Y2` is the ONE driver, issuing the FWD-1 thread and the round analysis. `~G2` (engine and brand), `~T2` (commentary) and `~V2` (ticket) continue as this project's workstreams with disjoint write surfaces, each issuing only into its own workstream scope (rule 27). No hop of FWD-1 parks on another project's cell. Each source PRD gains a one-line addendum pointing here at its next round boundary; in-flight orders and signed pairs complete where they are. |
| C-SWAP: the security swap, one pass per unknown holding (Andrew ~04:4xZ; CRO research @9ae5d353d1 section 2; restated v0.14 to the CTO replacement ruling @5deb868819) | this project | (1) KNOWN: the ticker or CUSIP in `etf-classifications` and MDPF_SECHIST; the form's typo hint is C-FILING-HINT, verified against the registry and yfinance, never YCharts. (2) PRICED: Yahoo, then YCharts per symbol (C-PRICES); if either has history, the holding is KEPT, a registry row is added and its prices land in MDPF_SECHIST. Every holding the door filed UNRESOLVED (a kept `TICKER_NOT_FOUND`, a `TICKER_DATA_NOT_ENTITLED`) enters this pass; the filer is never asked for a replacement (v0.18). (3) CLASSIFY only if neither has prices: SECCLASS's classifier on kimi-k2.6 with a web-search tool and the tool-call loop, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED. (4) REPLACE: from the class-matched pool (registry rows plus model proposals that pass the class match and have Yahoo history), the longest Yahoo history wins, ties by ticker. (5) RECORD: the holding keeps the client's name, with `proxy_for`, `proxy`, `method`, `confidence`, `low_confidence` and `sources`, and the report names the replacement. No designated-proxy table exists (provider QA @30ceaa97fa, finding 9). |
| C-PRICES: where prices come from (restated v0.13; Andrew-direct 10-14 ~17:5xZ, CTO price ruling ADDENDUM 2 @ac60268494) | this project | Per security, in order: (0) the estate's own stores where they hold the symbol (the DEMQUE price store, the Opal ETFs' Bloomberg history), read, not called; (1) Yahoo (yfinance), cut at T-1, `source: yfinance`; (2) YCharts through the stored session, one symbol per call, prices only, `source: ycharts`; (3) the backend replacement C-SWAP step 2 (class-matched pool, longest Yahoo history, ties by ticker), named in the report; (4) else the report runs WITHOUT the security and says so in words, never blocking. Bloomberg is OUT of this chain. Every price carries its source as a claim field. **There is no price-date input (v0.16, Andrew-direct 10-15 ~20:4xZ):** every price, share-quantity valuations included, is the most recent close, the T-1 frontier of `lib/trading_calendar.py`, stated in the report as the as-of. The performance overlays of variants 2 and 3 use IRPT_DASHBD's daily TWR engine, ported with zero flows. No YCharts report, figure or PDF. |
| C-FILING-HINT: the unmatched-ticker decision tree at filing (v0.12; restated v0.15, v0.18; restated v0.19 to Andrew-direct 10-15 ~21:5xZ, the decision tree; v0.22 yfinance first) | this project | **The door's check asks yfinance first (v0.22, Andrew-direct 10-16 ~15:2xZ): a holding yfinance keeps at T-1 is KNOWN with no YCharts call; YCharts is asked only for a symbol yfinance does not keep.** Every holding the upload door cannot match is CHECKED by the door, then: (A) **the ticker does not exist** (`TICKER_NOT_FOUND`): it is treated as a possible typo, and the form shows 'Did you mean <symbol> (<name>)?' (the door's own provider-verified `suggestion`) with three answers. **Yes** accepts the suggestion (the same upload re-posted with that correction). **Replace** opens an input where the filer types the replacement ticker(s), which are re-posted as corrections and CHECKED AGAIN by the same tree; a replacement that also fails gets the same prompt. **No** files the holding UNRESOLVED, and the form says 'Opal Staff will manage the replacement.' With no suggestion, the prompt offers Replace and No only. (B) **the ticker exists but Opal cannot price it** (`TICKER_DATA_NOT_ENTITLED` and every other unpriceable-as-given class): there is no typo prompt; it files UNRESOLVED with the words 'Opal Staff will manage the replacement.' Every UNRESOLVED holding goes to C-SWAP in the backend, and the report names its replacement. The form NEVER asks the filer to name a proxy: `NAME_PROXY` is retired from every filer-facing finding, and no text tells the filer to replace without an input to do it. Replace is the filer CORRECTING their own ticker, not picking a proxy (swaps are not the filer's, Andrew 10-15 ~14:xxZ). It works for the staff filer after a firm is chosen, and makes no vendor call at the form. |
| C-HOP-FAILURE: how a failed hop reaches the ticket (v0.20; design fork from `2.0.0_SA_COO~T2` msg 8900, research by this seat) | this project | The ticket READS the failure; no service writes a note to the ticket, and no new ticket route or principal exists for it. (1) The analysis-request ticket page calls the existing status route `getJobStatus(report_ref.request_id, firm)` and shows the state, the failed step and its words. (2) `irpt-status` returns a CLOSED failure code (`^[A-Z0-9_]+$`, an enumerated set) beside the state. Each code maps to words in one table in `status.py` that name the step and what happens next; an unmapped code reads as its step's generic words, never as blank. (3) The generator hops already write the job row in `irpt-jobs` (ATTENTION or FAILED, with `detail.code`). The silent hops write ONE set-once sibling attribute `hop_failure` = {hop, code, at} on that row, beside the receipt, never overwriting READY. The silent hops are the ready-signal send, the commentary draft and the packager. The packager writes it through the resident's existing jobs-table client. The commentary writes it through a `fail` op on the existing draft-store invoke. (4) Writers of `hop_failure`: exactly those three hops, one value per request. (5) A recovered hop (v0.21): the page shows a failure ONLY while the request is unfinished (no package attached). A request whose package is attached shows its completion, and the set-once value stays on the row as history. |
| C-NAMES: rule 30 | consumed; LGIC | Every new S3 address and resource name is `lib/opal_naming.py` `address()` / `name()` output, printed in the order that writes it. |

## 2. THREAD -- FWD-1, round 1

The thread is one seat-driven request on DEV, for a 49financial client with an eligible advisor (E5), through hops 1 to 9. Each hop is read
on its own artifact.
- Round 1 cuts one cell per MISSING or INCOMPLETE hop. Every hop is this project's own cell under C-ABSORB, including 4 (H1) and 6 (the
  commentary Lambda), so none parks on another project.
- A hop that waits on another box (for example a laptop KMS key-policy grant) parks that ONE hop with its owner, date and un-park condition,
  as a pre-arranged input, and the driver moves on in the same tick.

## 3. ENRICHMENT BACKLOG (ordered)

1. FWD-2: the form's Opal-model checkboxes, the other-ETF field, the typo check and the swap.
2. FWD-3: the commentary drafted from the report's key surfaces, rendered as a standalone branded Opal PDF marked DRAFT on the ticket.
3. FWD-4: each driven failure named on the ticket.
4. FWD-5: another firm refused the ticket and each package file, repeatably.
5. FWD-6: the Analysis tab as the manual path, landing on the same ticket.
6. RETIRED into FWD-1 by ADDENDUM v0.10: the commentary is its own standalone branded PDF, not a page inside the report PDF.

## 4. Rulings closed at L4

1. **The renderer** is the Opal engine's own HTML layout, which gains a commentary section (CRO trace hop 7). There is no second render stack.
2. **The package holds pointers only** (C-PACKAGE). No bytes are stored on a ticket.
3. **The commentary path carries abstract fields only** (C-KIMI). Kimi needs no per-use word (law edit 4d77a9c3ea).
4. **The seat arm runs on 49financial** (advisor census @ad2b877d88). Cottonwood has no E5-eligible owner.

## 5. SURFACE MANIFEST (step 4 -> step 5)

| id | FWD | surface | owner lane | risk |
|---|---|---|---|---|
| S1 | FWD-1, 2 | `portal/src/pages/TicketCenter/` (the Analysis Request form: models, other ETFs, typo check, swap) | this project, portal review route | product file |
| S2 | FWD-1, 4 | `infra/aws/lambda/ticket_center/lambda_function.py` (the package route's principal, failure states on the ticket) | this project with TCKT_VNEXT | SERVED at deploy |
| S3 | FWD-1, 2 | the upload door, E5, `POST .../analysis`, and the backend security swap (`intake/*`) | this project, `~Y2` (C-ABSORB a) | SERVED at deploy |
| S4 | FWD-1, 3 | the Opal engine's layout (commentary section) and the PDF render | this project, workstream `~G2` (C-ABSORB b) | resident release |
| S5 | FWD-1, 3 | the commentary Lambda and its READY trigger (H1) | this project, workstream `~T2` (C-ABSORB c, d) | SERVED at deploy |
| S6 | FWD-1, 5 | the ticket page's package files, opened through IRPT's signed-link reader | this project, portal | product file |
| S7 | FWD-6 | the Analysis tab under `portal/src/pages/InvestorReporting/`, the manual path | this project, after FWD-1 | product file |

## 6. BRIEF COVERAGE (one row per brief item; brief @2b21a349d1, 14 items)

| # | Brief item | Carried as (content, path, guard, proof gap) |
|---|---|---|
| 1 | the type of analysis | FWD-2. The form offers the report types the engine serves (Overview, Comparison, Multi-Comp; `ycharts/generate/comparison_catalogue.py`). S1 |
| 2 | Opal-model checkboxes and an other-ETF input | FWD-2. Model checkboxes from the comparison catalogue; free ETF tickers, each resolved before filing. S1 and S3 |
| 3 | the holdings Excel attached | FWD-1. Through the upload door (C-ONE-DOOR, TCKT_VNEXT); the ticket stores the handle, never the bytes. S3 |
| 4 | typo check and swap, frontend and backend | FWD-2. The form shows one catalogue "Did you mean" hint (C-FILING-HINT); swaps are never offered on the form. In the backend an unknown or unpriceable holding takes C-SWAP's one pass: KNOWN, then Yahoo, then YCharts, then classify with web search (kimi-k2.6, with the tool-call loop), then the replacement from the class-matched pool (registry rows plus model proposals that pass the class match and Yahoo), longest Yahoo history, ties by ticker, then RECORD with `proxy_for` / `method` / `confidence`, named in the report. The frontend is S1. Proof gap: one unknown holding (BREIT, SREIT or KPEC) through that pass |
| 5 | a ticket in the open Ticket Center page | FWD-1. An `analysis_request` ticket, open until the package lands, filed by an Opal staff user who chooses the partner firm (the Ticket Center is shown to Opal users only; ADDENDUM v0.6). The driven arm is a synthetic Opal staff user; `2e30` stays SUPERSEDED. S2. Proof gap: the synthetic staff user's filing end to end; that identity is never minted or left live outside its never-widen pair |
| 6 | the backend generates the full report | FWD-1. Generation submit and the Opal engine (C-ABSORB a, b). S3 and S4 |
| 7 | commentary from the report's key surfaces | FWD-3. The drafter reads the report's composition through `get()`, tenant-bound, with abstract fields only (C-KIMI). S5 |
| 8 | the package attached | FWD-1 carries the four items of the 10-13 memo: the original upload, the form selections as filed (J6, a new package kind), the Opal report and the commentary as a standalone branded Opal PDF (Andrew-direct 2026-10-14 ~16:0xZ, ADDENDUM v0.10), each a pointer through `POST /tickets/{id}/package` (C-PACKAGE) by the one packager (J5). S2 and S6. Proof gap: four pointers set on one ticket, each opened from the ticket page |
| 9 | ONE workflow, the form primary | FWD-1 and C-ONE-JOURNEY |
| 10 | the Analysis tab after, as the manual path | FWD-6. S7, cut after FWD-1 |
| 11 | measure each COO workstream | Section 1, the nine-hop state measured per lane (`~Y2`, `~G2`, `~T2`, `~V2`, `~P2`) |
| 12 | the closer-style trace, then the frontend | Section 1 (the CRO trace @9076346655) and the backlog order: backend hops before the Analysis tab |
| 13 | COMPRESS into ONE project | C-ABSORB. The cells and paths that move in, the remainder per source project, one driver plus workstream lanes |
| 14 | the defect: stopping on another agent's or box's deliverable | FWD-4, C-ONE-JOURNEY, and C-ABSORB (no hop parks on another project's cell; a cross-box wait is a pre-arranged input with owner and date) |

## v0.2 (2026-10-09 ~04:4xZ, `1.0.0_SA_CTO~DELL2`) -- on `4.0.0_SA_CRO~DELL2`'s brief-half refusal (msg 2416, review @5e8b383ce6)

- **R1:** C-ABSORB is added. S3-S5 move into this project, and hops 4 and 6 become its own cells.
- **R2:** FWD-2's swap is the security swap, and its backend owner is named.
- **R3:** BRIEF COVERAGE now has one row per brief item (14), each with its content.

FWD-2's ACCEPT changed, so the CVO's ratified-text half re-opens too.

-- 1.0.0_SA_CTO~DELL2

## v0.3 (2026-10-09 ~05:0xZ, `1.0.0_SA_CTO~DELL2`) -- Andrew-direct ~04:4xZ-05:1xZ: the swap method, no YCharts, prices yfinance-first

- **Source:** `4.0.0_SA_CRO~DELL2` msg 2485, with Andrew's words verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261009_SECURITY_SWAP_AND_NO_YCHARTS.md` @9ae5d353d1.
- **FWD-2:** ACCEPT reworded to the swap method.
- **FWD-7 is new:** no YCharts call end to end.
- **New contracts:** C-SWAP and C-PRICES.
- **C-ABSORB (b):** IRPT_YCDGEN's engine is absorbed; its YCharts path is retired by FWD-7, and its cells S31 and S32 are filled by C-SWAP.
- **ENDPOINT and CONTRACTS changed.** Both halves re-open.


## ADDENDUM v0.4 -- what a stored input is bound to when the reader changes; and the round-16 analysis for workstream Y (L10; CONTRACTS changed: the ratified-text half re-opens)

- **Author:** `1.0.0_SA_CTO~DELL2`, 2026-10-12 ~02:0xZ. **Answers:** the reviewer's slug for rounds 14 and 15
  (`surprise-channel/remediations/REMEDIATION_v8.md` @ff1c8da149, grade file `IRPT_ANLREQ_ROUNDS_14_15_Y_L9_GRADE_20261011.md`) and
  `2.0.0_SA_COO~Y2` msg 6285. **This analysis is two hours late: the slug was cut at 23:38Z and this seat did not answer it; the
  lane sat idle with four free slots meanwhile.**
- **Read by this seat:** `infra/aws/lambda/investor-reporting/intake/uploads.py:516-555` at HEAD; the grade file's first two
  sections; the revert's message (@114c77fb01). NOT read: the reverted reader, the form, the tests.

**CONTRACT C-STOREDINPUT.**

1. **What is there today (`uploads.py:532-539`).** For a template upload, reading a stored input re-reads the retained original
   with the RUNNING reader and requires the result to EQUAL the template stored at acceptance. So any change to what the reader
   returns refuses every input stored before it. That is why the round-14 reader was taken off the trunk.
2. **"Compare the holdings alone" is refused as the repair.** The new reader stops counting a totals row as a holding and refuses
   a sheet holding two accounts, so the holdings themselves differ on exactly the sheets it exists to catch.
3. **THE CONTRACT. The template stored at acceptance records the reader's version.** One member, written at acceptance from a
   constant in the reader's own file, changed in the same commit as any change to what the reader returns. A stored input with
   no such member is read as the version before this contract.
   - **Version equal to the running reader's:** the re-read must equal the stored template, as today.
   - **Version different, or absent:** the re-read is NOT compared. The input stays bound by what `read_input` already checks and
     this contract leaves in place: the original's bytes against its stored digest (`:537`), the frozen document against its own
     (`:522-524`), the artifact references, the owner and the source (`:550`).
   - **The reader's new findings apply at the upload door only.** They never refuse an input already accepted.
4. **What this gives up, said plainly:** for an input stored under an earlier reader, nothing re-derives the template from the
   original at read time. Its template is what the earlier reader made of it, held by digest. A defect of the earlier reader on
   that sheet (two accounts merged; a totals row counted) stays in that stored input until the person uploads again. The count
   of stored template inputs is item 1 of the list below, so that this is a number and not a phrase.
5. **The proof, driven offline on the product code:** an input stored by the reader at the round's base is read by the new reader
   and returns its document unchanged; an input stored by the new reader, with one byte of its stored template altered, is
   refused; an original whose bytes are altered is refused under both versions.

**ROUND-16 ENRICHMENT LIST (workstream Y), in this order.**
1. **A count first, read-only:** stored inputs by lane, and for the template lane how many originals the NEW reader would read
   differently from their stored template, by cause (totals row; repeated header; account column). Counts only, no account
   value, no holding. This is the census that should have preceded round 14's build; it precedes this one.
2. **The reader's re-land, as one cell, on C-STOREDINPUT**, with the reviewer's two repairs made first (row D2-S64): the
   account-header list built from header forms in real use or matched on the leading word with the named exclusions kept, and
   checked against a population that holds account columns; and the repeated-header words say what is seen and ask, never tell a
   person to split.
3. Row TCKT_VNEXT-D2-S48, the investor-reporting internal reader and a caller with no users row: one read, then a cell in the
   shape TCKT_VNEXT round 7 used.
4. `commentary_sent` on the ticket page; arm F2 on the original-file route. As parked, each under its own pair.
5. NOT cut: SUBTOTAL, SUM, ALL (stays parked; `Subtotal` was left out of the totals list on this seat's earlier ruling); the form sending `commentary_requested` (waits on
   IRPT_BCKEND's release, which waits on Andrew's sitting or his allow-list word).

- **Row D2-W53-S9** (four unpinned members of the generate function differ from live and ship on any rebuild): no rebuild of that
  function is cut by any lane until each of the four is either pinned or released under its own pair. Owner this seat.
- **Acts only Andrew can do:** none new.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.5 (2026-10-13 ~19:0xZ, 1.0.0_SA_CTO~DELL2; re-cut ~19:1xZ on the CVO's refusal @3e8061163e) -- the pivot direction's O1, written into the ENDPOINT

Authority: crossbox ORDER `XB-20261013T180328Z-d4a5`, body `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md`
(ACCEPTED by Andrew ~17:4xZ), section 2 O1 and section 8 act 4; Andrew's dell2 voice memo (section 1.1 there, verbatim).

1. **FWD-1 is re-worded (above).** The package is four separate items (original upload, the form as filled, the Opal report, the
   commentary draft), and the branded PDF is out of FWD-1. The driven arm is a synthetic partner-firm advisor; `2e30`, the Opal-staff
   filing, is SUPERSEDED. The ratified-text half re-opens on this ENDPOINT change, so `3.0.0_SA_CVO` re-signs it.
2. **FWD-1 is the only open thread.** No reader-hardening round opens unless it is a hop of FWD-1. AR-y-242..252 and AR-y-261..265
   finish, because Andrew raised them in his own test.
3. **Constraints that bind the form** (Andrew's memo):
   - C-FIRM: the firm is the signed-in user's, and a multi-firm partner user never chooses a firm outside its own domain; the staff
     picker stays out of the advisor path.
   - The variant the advisor selects is the variant produced (not inferred from the comparison count).
   - Opal staff do not file in the Ticket Center.
4. **The hop cells, cut at the next issuance by `2.0.0_SA_COO~Y2` (the ONE driver, C-ABSORB):**
   - J1: the form sends `commentary_requested` (the backend half is IRPT_BCKEND IB-pr-456).
   - J2: the request id is recorded on a partner-firm filer's ticket (the SUBMIT-FORM path or a named service does it; the advisor
     never needs the REPORT route).
   - J3: the C-SWITCH release for ticket-filed requests (`~G2`), ruled in `CTO_DELL2_PIVOT_FIRST_ACTS_20261013.md` act 2, with the
     principal read first.
   - J5: the packager principal is named, and it runs after the commentary.
   - J6: the form is the fourth attachment (a package kind for it).
   - J4: the orchestration stays client-side for V1, as ruled here. Either way FWD-4 holds: a failed hop shows on the ticket. Andrew's
     silent submit (AR-y-265) is the first proof of that.
5. **Commentary model:** ship on the wired Kimi K3 so the chain is proved. Andrew's "Astra" is one card on dell2's list; it becomes
   a setting once the first draft lands.

## ADDENDUM v0.6 (2026-10-14 ~15:3xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~15:2xZ: Opal staff file for testing; the Ticket Center is internal-only for now

Authority: Andrew at the dell2 terminal, verbatim: "Opal staff should not be "held" from filing, they can file they just realistically
won't, but we should have that available for testing. Ticket Center does not need to be displayed for client users at this time, only
opal users need to see it, so that part is accurate." Record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_152xZ_OPAL_STAFF_MAY_FILE_TICKET_CENTER_INTERNAL_ONLY.md` @011515bb70.

1. **FWD-1's driven arm is a SYNTHETIC Opal staff user** (above). This supersedes ADDENDUM v0.5's "the driven arm is a synthetic
   partner-firm advisor" and its "Opal staff do not file in the Ticket Center". The four attachments, the ACCEPT and "nobody touches
   anything after Submit" are unchanged. The ENDPOINT changed, so the ratified-text half re-opens and `3.0.0_SA_CVO` re-signs it.
2. **C-FIRM, restated:** an Opal staff filer CHOOSES the request's firm from the served partner tenants, and every hop binds to that firm.
   A partner-firm user's firm is the signed-in user's and is never a choice. The partner UI path is out of FWD-1 while the Ticket Center
   is internal-only; its API path stays guarded (release 29b, the owner check on `input_id` for CLIENT-class callers).
3. **New hop cell J7:** the internal-user submit hold is a defect against his word. The form's "Choose the firm this request is filed
   under" must accept a chosen firm (`filingFirm` returns `''` for internal users, `AnalysisRequestParts.tsx:100-104`; the hold at
   `analysisRequest.ts:227`, both @6a5926fc). It is a portal candidate under the approval route; the class (client-facing or
   Opal-internal) is read from the pages it touches.
4. **Parked, not cancelled:** the partner-firm UI reach cells (AR-y-282, AR-y-283; `isPartnerDevReach`, `firmAccess.ts:141-153`) wait
   until Andrew shows the Ticket Center to client users. Row S97 (a partner advisor's own-input analysis refused
   CLOSED_COMPOSITION_REQUIRED) leaves FWD-1's critical path: the internal viewer's analysis was accepted in release 29's sitting (D6b).
   It stays a defect for the partner path, fixed under the next intake pair.
5. **Release 29b's positive arm** (an owner's own client filing, 201) no longer rides the FWD-1 run, because the FWD-1 filer is internal
   and its submit is not owner-checked. Until a client-class filing exists, the 201 path is covered by its 21 unit tests. The CTO half's
   condition 3 (a 400 on the FWD-1 owner filing rolls the code back) is therefore inert.
6. **What FWD-1 still waits on:** IB-pr-456 (`commentary_requested` on the backend; Andrew's act f61b), the portal sending
   `commentary_requested` (AR-y-317, an approval row), and J7.

-- 1.0.0_SA_CTO~DELL2

## v0.7 (2026-10-14 ~15:4xZ, 1.0.0_SA_CTO~DELL2) -- on `3.0.0_SA_CVO~DELL2`'s refusal of the v0.6 ratified-text half (msg 7714, review @57cea3c90c)

C-FIRM is restated in the CONTRACTS table as ADDENDUM v0.6 item 2 states it, plus the CREATE path's `allowedFirmIds` check (`2.0.0_SA_COO~Y2`
msg 7713). FWD-1's DONE WHEN loses the dated attribution (it stays in SOURCE) and reads "the original upload". The partner organic arm, in
FWD-1 and C-ONE-JOURNEY, waits on the Ticket Center being shown to client users. ENDPOINT and CONTRACTS both changed, so both halves are
owed at these bytes.

-- 1.0.0_SA_CTO~DELL2

## v0.8 (2026-10-14 ~15:4xZ, 1.0.0_SA_CTO~DELL2) -- on `4.0.0_SA_CRO~DELL2`'s brief-half refusal R1 (review @6f40d4010f): BRIEF COVERAGE row 5 names the Opal staff filer. Row 8 (the commentary as a branded PDF, R2) waits on Andrew's answer to the CRO.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.9 (2026-10-14 ~16:0xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~15:5xZ: one YCharts data call for pricing data

Authority: Andrew at the dell2 terminal, verbatim: "I am ok with a single data call to YCharts for pricing data." Record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_155xZ_SINGLE_YCHARTS_DATA_CALL_FOR_PRICING_OK.md` @14360692df.

1. **FWD-7 and C-PRICES are re-worded (above).** The ENDPOINT changed, so the ratified-text half re-opens for `3.0.0_SA_CVO`.
2. **Where his word is silent, this seat reads it NARROWLY, and Andrew may widen it by one word:**
   - "single": ONE call per request, batched for every security still missing a price. It is not one call per security.
   - "for pricing data": prices only. Returns and risk are computed by Opal from those prices; no YCharts-computed figure.
   - Its place: AFTER the estate's verified store (MDPF_SECHIST) and BEFORE yfinance. A paid vendor's price outranks an UNVERIFIED one
     (CTO ruling 7546 keeps yfinance UNVERIFIED).
3. **The call is a data call:** the gateway's YCharts data API, never the retired signed-in browser path. Its time, its securities count
   and its source label go into the request's trace. A failed call falls through to yfinance and says so.
4. **The trace's hop 9** (the CRO's gap brief, sequence item 2, "a report worth reading") is the first enrichment after FWD-1. It is now:
   compose SECHIST plus the one YCharts call into the Opal producer.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.10 (2026-10-14 ~16:0xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~16:0xZ: the commentary is a standalone branded PDF; four standalone attachments

Authority: Andrew at the dell2 terminal, verbatim: "Yes it should be a standalone branded PDF. If you mean the original holdings csv as
the "form" then yes that is an attachment. If you mean the results from the form selection on the ticket issuance, yes that is also a
standalone attachment." Record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_160xZ_COMMENTARY_STANDALONE_BRANDED_PDF_AND_ATTACHMENTS.md`
@98eacceda3 (answers the CRO's R2).

1. **FWD-1 and FWD-3 are re-worded (above).** The four attachments are standalone:
   - the original holdings upload;
   - the form selections as filed;
   - the Opal report;
   - the AI commentary as a standalone branded Opal PDF, marked DRAFT.
   The "branded PDF is a later enrichment" line and backlog item 6 are retired. The ENDPOINT changed, so both halves re-open.
2. **New hop (from the CRO trace, hops 15 and 19):** no standalone commentary PDF renderer exists. The drafter writes JSON text, and
   `opal_packager.py` renders only the combined package PDF. The ticket page has no commentary reader. Two cells join round 41's thread:
   - a commentary-PDF renderer in the Opal brand, reusing the packager's branded layout. The commentary is its only body; the
     DRAFT mark and Opal's disclaimer stay;
   - the ticket page's reader for that PDF. It replaces the round-41 ADDENDUM's item 5, "commentary reader and branded-PDF reader".
3. **The combined package PDF** (report plus a commentary page) is NOT an attachment of FWD-1. If the packager keeps rendering it, it is
   not posted as a fifth item.

-- 1.0.0_SA_CTO~DELL2

## v0.11 (2026-10-14 ~16:1xZ, 1.0.0_SA_CTO~DELL2) -- on `3.0.0_SA_CVO~DELL2`'s refusal of the v0.10 ratified-text half (review @2af2238cdb)

C-PACKAGER is restated in CONTRACTS as ADDENDUM v0.10 states it: four standalone items, the commentary as a standalone branded Opal PDF
marked DRAFT, the combined package PDF never posted, and one `package_principal` that is never ALL. Two sections outside the ratified
text are aligned in the same bump: the round-1 thread item 2 and BRIEF COVERAGE row 8 ("the form selections as filed"). Before this bump,
a sweep of the ratified sections (lines 1-169) for "later enrichment", "commentary draft", "form as filled" and "partner-firm advisor"
found only these lines.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM v0.12 (2026-10-15 ~15:2xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~14:xxZ: "Did you mean" at the filing point; swaps stay in the backend

Andrew, verbatim (recorded by `4.0.0_SA_CRO~DELL2A`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261015_14xxZ_ANLREQ_PROD_PROMOTE_DEV_FILING_FIX_DID_YOU_MEAN_PRICES_PARALLELIZE.md` @cb91dbe30a):
*"We do need to sort out the "Did You Mean" at the Request filing point. The swaps can be handled later in the backend process, because swaps
are not up to the filer."*

**CONTRACTS gain C-FILING-HINT** (the ENDPOINT is unchanged, so under the proportionate sign-off rule only a formality re-sign is owed):
1. On the Ticket Center filing form, a holding whose symbol is not in the served catalogue shows ONE suggestion: "Did you mean <symbol>
   (<name>)?". It is the closest catalogue entry by exact CUSIP or ISIN match first, then the ticker edit distance, then the name.
2. The filer accepts it (the row takes the suggested symbol) or keeps their own. **Nothing is replaced without the filer's click.** A kept
   unknown symbol files as typed and goes to the backend.
3. **Swaps are not the filer's:** C-SWAP (the class-matched replacement, the longest history winning) runs only in the backend producer, after
   filing, and the report names any swap. The form never offers a swap.
4. The suggestion reads only the served catalogue the form already loads (no new vendor call at filing) and works for the staff filer (J7)
   after a firm is chosen.

**Prices (unchanged, restated):** C-PRICES as ruled at hop 9: the estate stores, then Yahoo (yfinance, cut at T-1), then YCharts per symbol,
then C-SWAP, else the report runs without the security and names it.

## v0.13 (2026-10-15 ~15:2xZ, 1.0.0_SA_CTO~DELL2) -- on `3.0.0_SA_CVO~DELL2`'s review of v0.12 (msg 8382)

1. **FWD-7 and the C-PRICES row are restated** to the price order Andrew set on 10-14 (~17:5xZ: "we use Yahoo as first round pick, we use
   Ycharts as second round pick"), as the CTO price ruling's ADDENDUM 2 (@ac60268494) already stated. The old text (at most ONE YCharts
   call, BEFORE yfinance, Bloomberg as a fallback) is superseded. This is an ENDPOINT change, so the ratified-text half re-opens for
   `3.0.0_SA_CVO~DELL2`.
2. **C-FILING-HINT now has its table row** (from ADDENDUM v0.12).

## v0.14 (2026-10-15 ~15:4xZ, 1.0.0_SA_CTO~DELL2) -- on the CRO's brief-half refusal (msg 8388, @7e209401ae) and the CVO's owed SOURCE line (msg 8389)

1. **BRIEF COVERAGE row 4 carries the current swap path**, in the CRO's correction text: the form's one "Did you mean" hint; the backend
   pass KNOWN, Yahoo, YCharts, classify with web search, the class-matched pool (the CTO replacement ruling @5deb868819). The
   designated-proxy table is gone: none exists (provider QA @30ceaa97fa, finding 9).
2. **FWD-7's SOURCE adds Andrew's ~17:5xZ quote** and marks the ~15:5xZ single-call quote superseded. The DONE WHEN text is unchanged.
3. **The C-SWAP contract row is restated the same way** (it carried the same retired proxy-table text). This is a CONTRACTS change, so
   the ratified-text half re-opens for `3.0.0_SA_CVO~DELL2`.

## v0.15 (2026-10-15 ~15:5xZ, 1.0.0_SA_CTO~DELL2) -- on `2.0.0_SA_COO~Y2`'s design read of C-FILING-HINT (msg 8415, AR-y-350 @039f9279c4)

The read found three things in v0.12's wording that cannot be built: the file carries no CUSIP or ISIN; the catalogue is 5 models plus
named ETFs; and the door already returns a provider-verified suggestion. C-FILING-HINT is restated:
1. **The hint source is the door's own `suggestion`** on a `TICKER_NOT_FOUND` finding. Use re-posts the same upload with a correction.
   This is portal-only work for `~Y2`.
2. **The CUSIP/ISIN rank and the catalogue source are dropped.**
3. **Keep-as-typed is NOT dropped.** Andrew 10-15 ~14:xxZ: "swaps are not up to the filer". A kept unknown symbol (BREIT, SREIT, KPEC)
   must file and reach C-SWAP; it cannot be refused until the filer swaps it. That is a change to the upload door: a kept
   `TICKER_NOT_FOUND` holding files as UNRESOLVED for C-SWAP. It rides the one resident release in the ENGINE lane (`2.0.0_SA_COO~G2`,
   the C-SWAP owner). Until it lands, the door refuses as today and the form says so in words.

This is a CONTRACTS change, so the ratified-text half re-opens.

## v0.16 (2026-10-15 ~20:4xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~20:4xZ: no price-date selection; prices are always the most recent data

Authority: Andrew at the dell2 terminal, verbatim (recorded by `4.0.0_SA_CRO~DELL2`,
`ANDREW_DIRECT_20261015_204xZ_NO_PRICE_DATE_SELECTION_LATEST_CLOSE.md` @89c40cc943): "By the way there is no point in giving them date
selection for prices. The prices should always be whatever the most recent data is. Doing T+1 is most logical, which is what we'd be able
to provide internally as well as all our API solutions to my knowledgds".

**The term is T-1, confirmed by Andrew the same minute, verbatim: "T-1 is the correct terminology, let's just stick to that".** Every price
is the T-1 close: the T-1 frontier of `lib/trading_calendar.py`, which is what Yahoo (cut at T-1), YCharts and Bloomberg deliver. No
record, field or label says "T+1".
1. **C-PRICES gains one sentence:** no price-date input; every price is the T-1 frontier close, stated as the report's as-of.
2. **The form loses its price-date field** (`TicketCenter.tsx:411` sends `priceDate: ''`). That is FILING `~Y2`'s portal cell.
3. **The server derives the date and never requires it** (share quantities, `intake/portfolio.py:208-212`, AR-y-242..245). The door
   change rides `~G2`'s one resident release, with the keep-as-typed door change (v0.15). A `priceDate` a client still sends is ignored
   and logged, never honoured.

This is a CONTRACTS change, so the ratified-text half re-opens. The ENDPOINT is unchanged.

## v0.17 (2026-10-15 ~21:4xZ, 1.0.0_SA_CTO~DELL2) -- Andrew's PROD read: the door asks the filer for a proxy; swaps are not the filer's

Authority: `ANDREW_DIRECT_20261015_214xZ_J4_PROD_FIRM_CHOOSER_WORKS_TICKER_SWAP_MISSING.md` (his PROD filing showed "Name a similar ticker
to stand in for it (a proxy)" and filed nothing), read with his 10-15 ~14:xxZ word "swaps are not up to the filer".

1. **C-FILING-HINT and C-SWAP cover EVERY holding Opal cannot price as given,** not only a kept `TICKER_NOT_FOUND`. That includes
   `TICKER_DATA_NOT_ENTITLED` (a real security the provider does not cover).
   - Such a holding FILES, marked UNRESOLVED, and C-SWAP's backend pass replaces it (class-matched pool, longest Yahoo history), named in
     the report.
   - The door never asks the filer for a proxy, and the `NAME_PROXY` action is retired from every filer-facing finding.
2. **The words the filer sees for such a holding are informational, not a correction:** "Row N: <symbol> is not covered by our price
   data. The analysis will use a similar security in its place and the report will say which." The filing proceeds.
3. **Where:** the door and its finding words run in `irpt-ycharts-generate`, so this rides `2.0.0_SA_COO~G2`'s r33 with the
   keep-as-typed and price-date changes.
   - `2.0.0_SA_COO~Y2`'s form shows the door's words as they come and offers no proxy input; the hint candidate already never shows
     `NAME_PROXY`.
   - FWD-1 run 3 includes one such holding (BREIT, SREIT or KPEC) and reads that it filed, with the replacement named in the report.

This is a CONTRACTS change, so the ratified-text half re-opens. The ENDPOINT is unchanged.

## v0.18 (2026-10-15 ~21:5xZ, 1.0.0_SA_CTO~DELL2) -- on `3.0.0_SA_CVO~DELL2`'s note on v0.17

v0.17 stated its rule only in its addendum. Its items 1 and 2 are now folded into the CONTRACTS table:
- **C-FILING-HINT:** every unpriceable-as-given holding, `TICKER_DATA_NOT_ENTITLED` included, files UNRESOLVED with the informational
  words, and `NAME_PROXY` is retired.
- **C-SWAP step (2):** every UNRESOLVED holding enters the backend pass, and the filer is never asked.

This is a CONTRACTS change, so the ratified-text half re-opens. The ENDPOINT is unchanged.

## v0.19 (2026-10-15 ~21:5xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~21:5xZ: the unmatched-ticker decision tree (Yes / Replace / No)

Authority: `3.0.0_SA_CVO~DELL2`'s record `ANDREW_DIRECT_20261015_215xZ_TICKER_DECISION_TREE_YES_REPLACE_NO.md` @78ed0c8908, verbatim: "...it
is a decision tree. If there is a ticker that doesn't connect, we check it. If the ticker doesn't exist outright, we assume it may be a typo
and the agent can do a "did you mean?" prompt and the user can say yes, replace, or no. If yes, we accept the swap, if replace we try it
with the replaced ticker(s) and rerun the process for those, if no, then we say that Opal Staff will manage the replacement."

**Ruled:**
1. **C-FILING-HINT is restated to his tree** (the table row above). Use/Keep becomes Yes/Replace/No, and Replace re-runs the check on
   the filer's typed ticker(s).
2. **His "doesn't exist outright" decides where the typo prompt applies:** only `TICKER_NOT_FOUND`. A ticker that EXISTS but cannot be
   priced (`TICKER_DATA_NOT_ENTITLED`, the PROD case) takes the No branch directly, because it is not a typo and choosing its stand-in
   would be a filer swap.
3. **The words of the No branch replace v0.18's informational sentence:** "Opal Staff will manage the replacement." The backend's
   C-SWAP does the replacing, and the report names it.
4. **Owners:**
   - `2.0.0_SA_COO~Y2`: the form (three answers, the Replace input, re-post and re-check). This is a new portal candidate, opal-internal,
     superseding 469b's Use/Keep; it needs my approval as before.
   - `2.0.0_SA_COO~G2`: the door's findings and words in r33. `NAME_PROXY` is retired, and every unpriceable class files UNRESOLVED.
   - FWD-1 run 3 exercises all three branches plus one (B) holding.

This is a CONTRACTS change, so the ratified-text half re-opens. The ENDPOINT is unchanged.

## v0.20 (2026-10-16 ~02:4xZ, 1.0.0_SA_CTO~DELL2) -- FWD-4: the ticket reads a failed hop; it is never written a note

Authority: design fork from `2.0.0_SA_COO~T2` (msg 8900; the routes map `deliverables/0.9.0_WK_IRPT_ANLREQ~220/FWD4_TICKET_WRITE_ROUTES_MAP.md`).
`4.0.0_SA_CRO~DELL2` was dark (its inbox unread for about 4 h), so this seat ran the research itself. Every claim carries file:line evidence
in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md`.

**Ruled:** C-HOP-FAILURE (the contract row above). The design is option (b), hybrid. Option (a) is refused: a new ticket route plus a
resident principal would be built for a status that is one read away, and the page does not display the ticket's `events` anyway.
Option (c) is refused: the generator half can land now.

**Owners, under this project's workstreams (C-ABSORB):**
- `2.0.0_SA_COO~T2` holds FWD-4 and cuts the cells. The commentary `fail` op is its own surface.
- `~G2`: `hop_failure` in `durable_job.py` and `resident_worker.py`, covering the packager and the ready-signal send. Also the
  `irpt-status` code and words, `status.py` plus the closed code in `ops/owned_status.py`, released as the r33 pair released `status.py`.
- `~V2`: the ticket page read, `AnalysisRequestParts.tsx`. Opal-internal, so this seat approves the portal candidate.

The one-drain rule applies: the `hop_failure` contract and its first writer land in one merge. The DONE WHEN is unchanged. Each failure
is driven on purpose, and the ticket names the step and what happens next.

This is a CONTRACTS change, so the ratified-text half re-opens. The ENDPOINT is unchanged.

## v0.21 (2026-10-16 ~02:4xZ, 1.0.0_SA_CTO~DELL2) -- on `3.0.0_SA_CVO~DELL2`'s v0.20 review (@d502747f6b): a recovered hop

The CVO's owed point: `hop_failure` is set-once, so a hop that fails, is retried and succeeds would still show its failure on a finished
request. **Ruled:** C-HOP-FAILURE clause (5). The page shows the failure only while no package is attached. A package attached is the
completion, and the stored value stays as history. This adds no writer and no attribute; `hop_recovered_at` is not needed, because the
package is already the one completion signal the page reads (C-PACKAGER). The ENDPOINT is unchanged.

## v0.22 (2026-10-16 ~15:3xZ, 1.0.0_SA_CTO~DELL2) -- Andrew-direct ~15:2xZ: yfinance first, YCharts second, everywhere in this process

**His words, verbatim** (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_152xZ_YFINANCE_FIRST_YCHARTS_SECOND_EVERYWHERE_AND_YCHARTS_PACING.md`):
*"Yeah we should consolidate on yfinance first and ycharts second as a general rule for any part of this process. Also want to examine the
requests/second pacing for ycharts calls, because maybe that is not calibrated well."*
**Research:** `4.0.0_SA_CRO~DELL2`, `RESEARCH_20261016_YCHARTS_PACING_AND_YFINANCE_FIRST.md` @e36af2fe2f. The firewall trips after about 4 to 6
lookups per several minutes from this host, whether 1.5 s or 90 s apart, so every YCharts call saved matters more than any spacing.

**RULED: the CRO's option (2), the rule as he stated it.**
1. **The upload door's identity check asks yfinance FIRST.** A holding yfinance keeps (history at T-1) is KNOWN without a YCharts call.
   YCharts is asked only for a symbol yfinance does not keep, and the C-FILING-HINT tree is unchanged from there. **C-FILING-HINT gains
   that sentence; this is a CONTRACTS change, so the ratified-text half re-opens for the CVO.**
2. **Report pricing runs the C-PRICES chain as already written** (estate, then Yahoo, then YCharts, then C-SWAP). The resident's
   `opal_pricing` switch is turned ON in the release that carries (1). No contract text changes for this.
3. **No step may require a YCharts security id for a holding Yahoo prices.** `2.0.0_SA_COO~G2` traces every YCharts-id dependency left in
   report generation and removes it in the same release, or names it as the one remaining call with its count. FWD-7's DONE WHEN ("no
   YCharts call end to end") is the test.
4. **Pacing:** the door's lease adopts the research runner's rule, a COUNT per window rather than a spacing, with the budget set from one
   measured read. After a 390 s rest, six known-symbol lookups about 90 s apart, then six about 5 s apart, to tell a per-window count from
   a bot-detection cutoff. The bounded WAF backoff (AR-g-129) stays as the fallback.
5. **Run 3** proceeds on the current resident only within its signed amendments. The release carrying (1) to (3) is its own resident
   pair, which this seat signs.

-- 1.0.0_SA_CTO~DELL2
