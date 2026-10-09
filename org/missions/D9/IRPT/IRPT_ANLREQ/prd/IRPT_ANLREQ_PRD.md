# IRPT_ANLREQ -- one Analysis Request end to end: the Ticket Center form to a finished package on the same open ticket

```json
{
 "project": "IRPT_ANLREQ",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.3",
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
  FWD-1  One Analysis Request goes from the Ticket Center form to a finished package on the same open ticket, with no person in between
         DONE WHEN  EXERCISED -- on DEV, a seat files ONE request through the form (analysis type, Opal-model checkboxes, other ETFs, holdings Excel) for a
                    49financial client with an eligible advisor; with nobody touching it, the ticket ends up carrying the report, the branded Opal PDF with
                    the investment commentary, and the original Excel, each opened from the ticket page; Alyssa's own first real request grades it again
                    (the organic arm)
         ACCEPT     an Opal person opens the still-open ticket and finds the report, the branded PDF with the commentary and the advisor's original Excel,
                    without asking anyone and without anyone having forwarded a file
         SOURCE     Andrew 2026-10-08 ~22:3xZ; CRO trace hops 1-9

  FWD-2  The form fits the request and catches a bad request before it files
         DONE WHEN  EXERCISED -- the form offers the analysis types and the Opal models as checkboxes plus a field for other ETFs; a mistyped ETF is caught
                    and a correction offered, and a swap is accepted, before the ticket is created
         ACCEPT     a person who types an ETF wrong is told before filing and can pick the right one; a holding that is unknown or cannot be priced is
                    kept if Opal or yfinance can price it, and otherwise replaced before filing by a proxy ETF chosen from Opal's own registry for
                    its asset class and sub-class (the security swap, C-SWAP), never by an unverified guess; the advisor sees and can change it
         SOURCE     Andrew ("typo check and swap ability completely ironed out"); CRO trace hops 1-2

  FWD-3  The investment commentary is written from the report itself, and stays a draft until a person sends it
         DONE WHEN  EXERCISED -- the commentary for FWD-1's request is drafted from that report's key surfaces (abstract fields only, no client identity)
                    and shown on the ticket as a DRAFT
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

  FWD-7  An Analysis Request runs end to end without YCharts
         DONE WHEN  EXERCISED -- FWD-1's request is traced hop by hop and shows zero YCharts calls: the typo check, the swap, the prices, the report
                    and the overlays all come from Opal's own data, with yfinance and Bloomberg as named fallbacks
         ACCEPT     the finished package is produced with no YCharts call anywhere in the request's trace; a figure Opal could not source says so
         SOURCE     Andrew 2026-10-09 ~04:4xZ ("I do not think we actually need YCHARTS for anything")
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
| C-ONE-JOURNEY: FWD-1 is driven, never waited on | this project | Round 1 decomposes over the nine hops of FWD-1. A hop that waits on another box parks that ONE hop in STATUS.md with its owner and un-park condition, and the driver moves to the next hop in the same tick (the CRO's no-stop rule). Alyssa's own filing is the organic arm, never the gate. |
| C-SOURCES: contracts are cited, not copied | this project | C-PACKAGE, C-ONE-DOOR and C-TYPE live in `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`. C-KIMI and C-WIPE-GATE live in `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md`. The upload door and E5 live in IRPT_BCKEND. This PRD cites each at its path and never restates it, so each rule has one home. |
| C-PACKAGER: one principal attaches the package | this project | The package's last hop is the branded PDF render, which runs after the commentary. That hop's principal is the ONE `package_principal` named in the type definition. It is firm-bound by its PROFILE row (internal-caller narrowing, IB-pr-387), and never ALL. |
| C-FIRM: firm reach | consumed | Every principal on the journey reaches exactly the request's firm: svc-commentary by tenant-bound `get()`; the test filer by its PROFILE row [49financial]; the packager by its row. ALL never admits. |
| C-ABSORB: what MOVES into this project (the brief's "compress into ONE project") | this project | **Moves in, owned and issued here.** (a) IRPT_BCKEND `~Y2`'s Analysis lane: the upload door and resolution `infra/aws/lambda/investor-reporting/intake/{uploads,upload_resolution,upload_suggestions,resolution_kimi}.py`, the security swap (today `KIMI_WEB_SEARCH_UNVERIFIED`, `resolution_kimi.py:159-165`; candidates from `etf-classifications`, ex-IRPT_YCDGEN FWD-16), and generation submit. (b) IRPT_YCDGEN whole: the Opal engine and brand `ycharts/generate/{resident_worker,durable_job,comparison_catalogue,publication_worker}.py`, `ycharts/research/{opal_producer,layout_overview}.py`, report types and vendor retirement. (c) NFRA_TRNSPT FWD-10 and FWD-11: the commentary drafter `data/transcripts/scripts/commentary/*` and its Lambda `commentary.tf`. (d) The READY event H1 (from `~P2`'s queue). (e) TCKT_VNEXT's Analysis Request scope: the `analysis_request` type definition, `POST /tickets/{id}/package`, `portal/src/pages/TicketCenter/` Analysis Request parts. **Keeps the remainder:** IRPT_BCKEND (`~P2`: auth, routes, directory, holdings, `irpt-export-render` as the shared renderer); NFRA_TRNSPT (FWD-1..9: transcripts, company read, mail); TCKT_VNEXT (non-analysis types). **Lanes:** `~Y2` is the ONE driver, issuing the FWD-1 thread and the round analysis. `~G2` (engine and brand), `~T2` (commentary) and `~V2` (ticket) continue as this project's workstreams with disjoint write surfaces, each issuing only into its own workstream scope (rule 27). No hop of FWD-1 parks on another project's cell. Each source PRD gains a one-line addendum pointing here at its next round boundary; in-flight orders and signed pairs complete where they are. |
| C-SWAP: the security swap, one pass per unknown holding (Andrew ~04:4xZ; CRO research @9ae5d353d1 section 2) | this project | (1) KNOWN: the ticker or CUSIP in `etf-classifications` and MDPF_SECHIST; a typo suggestion is verified against the registry and yfinance, never YCharts. (2) YFINANCE CHECKER: one paced call; if it has history, the holding is KEPT, a registry row is added and its prices land in MDPF_SECHIST. (3) CLASSIFY only if yfinance has nothing: SECCLASS's classifier with a web-search tool, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED. (4) PROXY, deterministic, no model: the designated registry ETF for that pair, else the class default, and it must have prices. (5) RECORD: the holding keeps the client's name, with `proxy_for`, `proxy`, `method`, `confidence`, `low_confidence` and `sources`. `resolution_kimi`'s model-proposed swap is retired. The designated-proxy table is MDPF_SECCLASS's (dell1), a pre-arranged input. |
| C-PRICES: where prices come from | this project | MDPF_SECHIST's per-security series first, then yfinance (paced), then Bloomberg only when both lack it (through its queue, CLAUDE.md). The performance overlays of variants 2 and 3 use IRPT_DASHBD's daily TWR engine, ported with zero flows. No YCharts price or figure. |
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
2. FWD-3: the commentary drafted from the report's key surfaces, shown as DRAFT on the ticket.
3. FWD-4: each driven failure named on the ticket.
4. FWD-5: another firm refused the ticket and each package file, repeatably.
5. FWD-6: the Analysis tab as the manual path, landing on the same ticket.

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
| 4 | typo check and swap, frontend and backend | FWD-2. A mistyped ETF gets a correction offer; an unknown or unpriceable holding is SWAPPED for a confirmed `etf-classifications` candidate. The backend is `intake/upload_suggestions.py` and `resolution_kimi.py` (C-ABSORB a); the frontend is S1. Proof gap: `KIMI_WEB_SEARCH_UNVERIFIED` today |
| 5 | a ticket in the open Ticket Center page | FWD-1. An `analysis_request` ticket, open until the package lands. S2. Proof gap: 0 filed end to end |
| 6 | the backend generates the full report | FWD-1. Generation submit and the Opal engine (C-ABSORB a, b). S3 and S4 |
| 7 | commentary from the report's key surfaces | FWD-3. The drafter reads the report's composition through `get()`, tenant-bound, with abstract fields only (C-KIMI). S5 |
| 8 | the package attached: report, branded PDF with commentary, original Excel | FWD-1. `POST /tickets/{id}/package`, pointers only (C-PACKAGE), by the one packager (C-PACKAGER). S2 and S6. Proof gap: no signed-link open yet (hop 9) |
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

