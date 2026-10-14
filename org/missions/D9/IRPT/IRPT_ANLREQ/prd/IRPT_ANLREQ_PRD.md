# IRPT_ANLREQ -- one Analysis Request end to end: the Ticket Center form to a finished package on the same open ticket

```json
{
 "project": "IRPT_ANLREQ",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.6",
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
                    Center (shown to Opal users only, Andrew 2026-10-14 ~15:2xZ), CHOOSES the partner firm the request is filed under, fills the
                    Analysis Request form and uploads a holdings CSV or XLSX. The form carries the variant chosen
                    (Overview, Comparison, Multi-Comp) and the report produced is that variant, the Opal-model checkboxes and other tickers. Every
                    downstream hop binds to the chosen firm. Nobody touches anything after Submit. The still-OPEN ticket then carries four attachments, each opened from the ticket
                    page by an Opal person: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal
                    producer, not YCharts), (4) the AI commentary draft. A partner-firm filing (Alyssa's first real request) grades it again (the
                    organic arm, never the gate)
         ACCEPT     an Opal person opens the still-open ticket and finds the four items, without asking anyone and without anyone having forwarded
                    a file; the branded Opal PDF with the commentary inside is a later enrichment, not FWD-1
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
| C-PACKAGER: one principal attaches the package | this project | The package is four separate items: the original upload, the form as filled, the Opal report and the commentary draft. Its last hop attaches them after the commentary; the branded PDF is a later enrichment, not this hop. That hop's principal is the ONE `package_principal` named in the type definition. It is firm-bound by its PROFILE row (internal-caller narrowing, IB-pr-387), and never ALL. |
| C-FIRM: firm reach | consumed | Every principal on the journey reaches exactly the request's firm: svc-commentary by tenant-bound `get()`; the synthetic partner-firm advisor (FWD-1's filer) by its PROFILE row; the packager by its row. ALL never admits. |
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
6. After FWD-1: the branded Opal PDF with the commentary inside, rendered by the Opal engine's layout (L4 ruling 1, S4), attached as one more
   package kind (brief item 8; ADDENDUM v0.5).

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
| 4 | typo check and swap, frontend and backend | FWD-2. A mistyped ETF gets a correction offer verified against the registry and yfinance. An unknown or unpriceable holding takes C-SWAP's one pass: KNOWN, then the yfinance check (KEEP), then classify, then a deterministic proxy from the designated-proxy table (MDPF_SECCLASS, dell1, a pre-arranged input), then RECORD with `proxy_for` / `method` / `confidence`. The model-proposed swap is retired. The frontend is S1. Proof gap: the C-SWAP path exercised on one unknown holding |
| 5 | a ticket in the open Ticket Center page | FWD-1. An `analysis_request` ticket, open until the package lands, filed by a partner-firm advisor. Opal staff do not file in the Ticket Center (Andrew's 10-13 memo), the driven arm is a synthetic partner-firm advisor, and `2e30` is SUPERSEDED (ADDENDUM v0.5). S2. Proof gap: the synthetic advisor's filing end to end; that identity is never minted or left live outside its never-widen pair |
| 6 | the backend generates the full report | FWD-1. Generation submit and the Opal engine (C-ABSORB a, b). S3 and S4 |
| 7 | commentary from the report's key surfaces | FWD-3. The drafter reads the report's composition through `get()`, tenant-bound, with abstract fields only (C-KIMI). S5 |
| 8 | the package attached | FWD-1 carries the four items of the 10-13 memo: the original upload, the form as filled (J6, a new package kind), the Opal report and the commentary draft, each a pointer through `POST /tickets/{id}/package` (C-PACKAGE) by the one packager (J5). The brief's branded Opal PDF with the commentary moves to section 3 as a named enrichment (memo section 1.1; direction :152-155). S2 and S6. Proof gap: four pointers set on one ticket, each opened from the ticket page |
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
