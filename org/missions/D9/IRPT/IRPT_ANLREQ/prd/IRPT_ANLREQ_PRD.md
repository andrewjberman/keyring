# IRPT_ANLREQ -- one Analysis Request end to end: the Ticket Center form to a finished package on the same open ticket

```json
{
 "project": "IRPT_ANLREQ",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md@2b21a349d1",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
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
         ACCEPT     a person who types an ETF wrong is told before filing and can pick the right one; a person who wants a model swapped can say so in the form
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
| C-NAMES: rule 30 | consumed; LGIC | Every new S3 address and resource name is `lib/opal_naming.py` `address()` / `name()` output, printed in the order that writes it. |

## 2. THREAD -- FWD-1, round 1

The thread is one seat-driven request on DEV, for a 49financial client with an eligible advisor (E5), through hops 1 to 9. Each hop is read
on its own artifact.
- Round 1 cuts one cell per MISSING or INCOMPLETE hop it can build now.
- It parks the hops whose owner is another project's open cell (4 and 6), naming the owner and the un-park condition.

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
| S3 | FWD-1 | the upload door, E5 and `POST .../analysis` | IRPT_BCKEND (~Y2) | SERVED at deploy |
| S4 | FWD-1, 3 | the Opal engine's layout (commentary section) and the PDF render | IRPT_YCDGEN (~G2) | resident release |
| S5 | FWD-1, 3 | the commentary Lambda and its READY trigger (H1) | NFRA_TRNSPT (~T2), IRPT_BCKEND (~P2) | SERVED at deploy |
| S6 | FWD-1, 5 | the ticket page's package files, opened through IRPT's signed-link reader | this project, portal | product file |
| S7 | FWD-6 | the Analysis tab under `portal/src/pages/InvestorReporting/`, the manual path | this project, after FWD-1 | product file |

## 6. BRIEF COVERAGE

| Brief item | Where |
|---|---|
| Hops 1-2 (form, check and swap) | FWD-2, S1 |
| Hops 3-9 | FWD-1, the THREAD |
| Commentary from the report | FWD-3, S5 |
| No-stop rule | FWD-4, C-ONE-JOURNEY |
| Firm fence | FWD-5, C-FIRM |
| The Analysis tab after | FWD-6, S7 |

-- 1.0.0_SA_CTO~DELL2
