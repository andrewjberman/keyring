# PIVOT AGGREGATE -- Andrew's six voice memos (2026-10-13 morning) against what the four boxes are actually doing

**Author:** `4.0.0_SA_CRO` (laptop), 2026-10-13 ~17:1xZ. **For:** `1.0.0_SA_CTO` (laptop) and Andrew, to decide how work is
repositioned across the boxes.

**Inputs (all in this folder):**
- the six transcripts `*_TRANSCRIPT.md`;
- the six alignment reports `alignment/*_ALIGNMENT_20261013.md`. Five were written by research subagents and the laptop one by this
  seat. Each was read-only and measured, with sources inline;
- today's four box status reports and their aggregate (`AGGREGATE_4_of_4_20261013.txt`, 66 projects: CLOSE 26, KEEP 22, PARK 17,
  MERGE 1).

Every claim below is carried from an alignment report with its source. Section 7 names what was not measured.

---

## 1. The one-paragraph read

Across all six memos Andrew asks for the same thing: a few named outcomes on each box, closed fast as working V1s. The measurement
says the boxes are busy but **pointed at the wrong things**:
- **Effort runs opposite to his ranking on five of six surfaces.**
- **The outcomes he wants most break at the joins between projects,** where no single project or seat owns the hand-off.
- **Six to eight decisions of his would unblock most of it at once.**

Nothing here needs a new seat. It needs existing seats re-pointed, a few small outcomes added to existing PRDs, and one small new
project.

## 2. Effort vs Andrew's ranking (measured)

| box / macro | Andrew's #1 | where the effort actually goes (7-day commits, seats) | verdict |
|---|---|---|---|
| dell1 / AMGT | Security Analysis V1: all 93 names load fast and complete; AI fill of thin sections; harvest access for asset managers | Harvest collection, his "own pace" item: 3 seats. Page V1: 2 seats working on cold-start log lines. AI fill and harvest access: 0 seats. First load still ~20 s (warm ~1.3 s). | INVERTED |
| dell1 / MDPF | CANON proceeds; DEMQUE<->SECCLASS synced; YCharts explored as a quota-free source | SECCLASS 697 commits, the largest spend. DEMQUE<->SECCLASS sync: 0 seats, no rule in either PRD. YCharts: 0 seats, and DEMQUE's PRD excludes it. 6 MDPF COO seats on dell1. | INVERTED |
| dell1+dell2 / ADVI | FIRMBKTS locked in with a migration and decommission plan; billing without duplication; backfill for active accounts only | FIRMBKTS fits (617). COTBKF full-history backfill, which he called a "deep, deep, deep" historical item: 622 commits, 80 rounds. Billing: 0 seats. Its new fee panel duplicates the existing QTD/YTD panel. | INVERTED |
| dell2 / IRPT+TCKT | ONE end-to-end workflow: ticket -> report -> AI commentary -> 4 attachments | P1 already holds 4 of 7 COO and 3 of 4 CloudOps seats. Rounds 10-21 went to hardening the upload reader. YCDGEN and TCKT rounds cut nothing. 3 lanes wait on one human act. | MIS-DIRECTED |
| site Z / NFRA | MC Portal as the one control panel for the gateway; MCP Index; Bloomberg agent works | OPLGTW 614 commits (mostly upkeep) vs MC Portal 171. MCP Index's own box CRO recommends PARK. The Bloomberg agent is degraded with no owner. | INVERTED |
| laptop / NFRA | CTLPLN, DEVPLN (one session today), COMM_ASSIST via muse; tailnet ops today | CTLPLN: 1 open order of 69, round 12 not cut. DEVPLN: registered today, PRD stage, no COO seat. COMM_ASSIST: moved here today; the muse thread is planned for round 16 but not yet in the PRD. | STALLED |

## 3. Where Andrew's outcomes break: the joins no one owns

1. **dell2: ticket -> report.**
   - Opal's report engine is switched on for Andrew's sign-in only. Every ticket filing goes to the YCharts path, which last failed
     2026-10-11.
   - Fix: put the Ticket Center's service principal on the C-SWITCH allow list. Needs Andrew's word.
2. **dell2: ticket -> commentary.**
   - The form saves "Add commentary" on the ticket but never sends `commentary_requested` with the report request. The drafter
     runs only when that field is true.
   - Ticket and request do not point to each other.
3. **dell2: the shared wait.** Ticket, report and commentary all wait on an Opal staff member filing a test request (call `2e30`).
   Andrew says Opal users never use the Ticket Center.
4. **MDPF: DEMQUE <-> SECCLASS.** DEMQUE's PRD relies on SECCLASS for security identity; SECCLASS never mentions DEMQUE.
5. **AMGT -> gateway: harvest access.**
   - The gateway catalog returns "not catalogued" for harvest data.
   - The catalog project (MCPINDEX, site Z) is parked and never chartered harvest. The gateway project (OPLGTW) covers Schwab and
     Black Diamond only.
6. **site Z: MC Portal "control".** FWD-20 is a read-only page (built, not released). No outcome lets the panel change a
   person's tools, channels or tier, or show poll cadence and backfill depth.
7. **ADVI: billing -> the existing Fee Summary panel.** ADVI_BILLING's PRD has no contract with it, so a second panel was built.
8. **ADVI/MDPF: active-account scope for backfill.**
   - COTBKF's price need is sized over the whole Commonwealth delivery: 4,634 securities, 3.42M security-days.
   - DEMQUE ranks former clients last but still draws them.
   - No "active Cottonwood account set" exists. Nor does a reverse match listing every current account with its predecessor or
     "none".

## 4. Unowned work that needs a home (smallest correct home named)

| need | home | box |
|---|---|---|
| AI fill of thin text sections (management bio, recent developments) for all 93 names | AMGT_RESAPP PRD addendum (model calls and machine-prose marking already exist) | dell1 |
| Harvest data reachable by asset managers through the gateway | one short round on the parked NFRA_MCPINDEX (catalog rows) plus an NFRA_OPLGTW grant; dell1 supplies the servable prefixes | site Z |
| YCharts as a quota-free source: first measure coverage of DEMQUE's 17 items | new small project. L1 brief by the laptop CRO; reuse the closed YALP_MDSRC endpoint map and its 3 deployed, idle YCharts functions | laptop brief -> dell1 |
| DEMQUE <-> SECCLASS sync rule | one cell in each project's next round, under the one dell1 CTO | dell1 |
| Bloomberg agent works for people (daily pull, intake identity pin, Teams answer) | re-home OPAL_BBGTML or reopen it; a read-only trace first | site Z |
| MC Portal control and depth (FWD-21) | NFRA_MCPORTAL PRD addendum after FWD-20 | site Z |
| Retiring legacy OPERATIONS after the firm-bucket moves; a written Inflection/Cottonwood plan | ADVI_FIRMBKTS FWD addendum | dell1 |
| Active Cottonwood account set plus reverse match; draws limited to it | one read-only ADVI_COTBKF cell plus a DEMQUE `rank.py` filter | dell2 + dell1 |
| IRPT_DASHBD "default performance report" from the 49 Financial template | IRPT_DASHBD outcome (none names it today) | dell2 |

## 5. Proposed positioning per box (for the CTO to rule)

| box | drive this week (fast defined outcomes) | re-point | park / close / merge |
|---|---|---|---|
| **laptop** | 1. Tailnet SSH finished: key-only, tailnet-only, password off on 4 boxes, muse into the laptop (CTLPLN FWD-27). 2. DEVPLN forward rule: one approved feature merges to DEV. 3. COMM_ASSIST muse thread: "what is waiting on me" answered from the dell2 folder. | CTLPLN round 12 narrowed to the tailnet chain plus the fence fix. Seat COO lanes for DEVPLN and COMM_ASSIST (3 laptop COOs = limit). | 19 closes and the SPMOVE park already recorded (pare-down record). Laptop CloudOps `~ANL`/`~FBL` stand down once the Dell grants land. |
| **dell2** | 1. A synthetic partner advisor files one request; with no hands, the ticket shows upload + form + Opal report. 2. Commentary attaches automatically. 3. (P2) DASHBD default report from the 49 Financial template. | ANLREQ `~Y2` drives; TCKT_VNEXT's ticket fixes merge into it as named tasks; YCDGEN `~G2` stays (it owns the report engine); TRNSPT keeps its commentary half under ANLREQ; BCKEND `~P2` does the one acceptance release first. | Drain and park ADVI_COTBKF after one active-set cell. Park TRNSPT's transcripts-database half only. Do NOT park YCDGEN or TRNSPT whole: that conflicts with the dell2 CRO rec. |
| **dell1** | 1. Security Analysis V1: promote the staff-only page, a per-name completeness census, a cold-start fix to a number Andrew sets. 2. MDPF_HEALGAP closes (5/6). 3. DEMQUE card complete plus Andrew's depth pick. 4. FIRMBKTS: 49F cutover closed plus the Inflection/Cottonwood plan. | RESAPP from log lines to the three V1 items, plus the AI-fill addendum. One DEMQUE<->SECCLASS sync cell each. | Park MDPF_SECHIST (fold later into DEMQUE/SECCLASS); grade STRATID once, then close. That frees 2-3 dell1 COO seats, which can take the AMGT V1 and AI fill. |
| **site Z** | 1. MC Portal FWD-20 live and read by Andrew (meets OPLGTW's own close condition). 2. FWD-21 control and depth. 3. Bloomberg agent trace and repair. | OPLGTW COO's next round feeds the panel (backfill-status, cadence) instead of upkeep. One MCPINDEX round: catalog links for every served tool, plus harvest rows. | Park NFRA_OPALAI and NFRA_MCPMSP (frees no live seat; both COOs have no process). Close site Z's 2 COMM_ASSIST calls (the project moved to the laptop). |

## 6. Decisions only Andrew can make (consolidated; each from an alignment report)

**Unblocks the most:**
1. **dell2, ticket path engine.** Put the Ticket Center's service principal on the C-SWITCH allow list so tickets use the Opal
   engine. REC yes, for ticket-filed requests only. Without it no ticket can produce a report.
2. **dell2, test filing.** May an agent drive the end-to-end test as a synthetic partner-firm advisor (minted and deleted under a
   never-widen pair) in place of the Opal-staff filing (call `2e30`)? REC yes. Three lanes wait on that one act.
3. **dell1, Security Analysis PROD promote.** The page is staff-only, so the promote (call `e7f2`) needs no word of yours. Confirm,
   and dell1 promotes after checking that the bundle changes no client-facing page. REC yes.
4. **MDPF, DEMQUE depth for the largest backfill item.** REC option D: about 13 days of Bloomberg quota, inside your 2-week budget.
5. **ADVI, former Cottonwood clients.** Exclude them from every vendor draw rather than rank them last. REC yes.
6. **ADVI, firm buckets.** Answer the four decisions held since 2026-09-14 that block every Inflection step. RECs:
   - retire the Door 6 marker with its watcher;
   - keep the B2 credential;
   - log write events on the legacy buckets;
   - `mockadv` follows 49F.
7. **laptop, tailnet.** Delegate the four password-off lines to the laptop CloudOps seat, and approve a laptop local account for key
   SSH. REC yes to both. Your "today" depends only on these.

**Shape and scope:**
8. **AMGT AI fill provider.** REC the existing Anthropic path with its server-side web search. Choose OpenAI only if you want it
   specifically.
9. **AMGT "load fast".** REC under 3 s for the first request of the day.
10. **AMGT harvest scope for asset managers.** REC derived layers and article links only in V1, not raw publisher text.
11. **ADVI billing.** REC the custodian fee feeds the EXISTING Fee Summary panel; no second panel on PROD.
12. **MDPF YCharts.** REC a separate small project; step one measures coverage of the 17 DEMQUE items.
13. **site Z control.** REC yes: MC Portal edits tools, channels and tiers per person (FWD-21), with writes Andrew-only.
14. **site Z Bloomberg mirror.** REC keep the Bloomberg account mirroring your grants until you have read FWD-20. One gateway is
    acceptable: no merge is needed.
15. **dell2 "templates sent last week".** Name the files and one approver. REC start from the IRPT_CUSTDY-built 49F template.
16. **laptop.** Confirm that "news" in the memo means muse. REC yes.

## 7. Corrections this measurement makes to earlier reads today

- **MDPF_CANON's Global fold is LIVE:** deployed 14:05Z today. It was not live when the 10-12 End of Day post said it was.
- **AMGT_HARVST and MDPF_DEMQUE belong to dell1.** Site Z only runs legs of them; the four-box aggregate lists each twice.
- **There is ONE gateway.** `opal-gateway-bbg` is a second client-side login entry pointing at the same server.
- **Out-of-date box report figures:**
  - HEALGAP is 5/6, not 3/6.
  - SECHIST's Bloomberg pull landed at 14:39Z.
  - The site Z AMGT block names a superseded issuer and a withdrawn WSJ/Barron's ask.
  - The dell1 report lists no Andrew acts for FIRMBKTS, though four are held.

## 8. Not measured here

- **Live AWS state:** mostly read from box reports and round analyses, not re-read.
  - Exceptions: the gateway catalog query (AMGT); the YCharts Lambda listing and session probe (MDPF); public HTTPS reads (site Z).
- **Site Z work not yet on CLOUD:** the reports read the laptop checkout.
- **ADVI open-order counts:** come from the box reports; the agent's own order scan timed out.
- **The portal ticket client `src/api/endpoints/tickets.ts`:** not read. It decides whether a partner filing can record its report
  link (dell2 J2).
