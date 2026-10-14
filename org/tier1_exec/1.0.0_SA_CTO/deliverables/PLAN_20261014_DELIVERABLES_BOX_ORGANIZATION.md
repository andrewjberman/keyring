# PLAN 2026-10-14 ~18:2xZ (1.0.0_SA_CTO, cluster lead) -- organizing the four boxes against Andrew's "Deliverables" dates

**Order:** `ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md` (his voice note, transcribed verbatim).
**Denominator:** 25 active projects, read from every `org/missions/D*/*/*/project.json` with status active at ~18:2xZ: dell1 10,
dell2 9, site Z 3, laptop 3.

## 1. The four items, mapped to projects

| item | date | projects that serve it | box today |
|---|---|---|---|
| **P2 Ticket Center, all three channels** | **Oct 24** | IRPT_ANLREQ (analysis request, 4 attachments; primary); IRPT_YCDGEN (the report engine); NFRA_TRNSPT (its commentary half); TCKT_VNEXT (trade request and meeting request channels) | dell2 |
| **P1 Investor Reporting / performance module** | **Nov 15** internal (Dec 1 external) | IRPT_DASHBD (performance tab, all clients at all firms; holdings tab); IRPT_BCKEND (its data); DSGN_IRPTV1 (its design) | dell2 |
| **P3 Advisor Intelligence** | full force after P1 checks out; **before Dec 1** | ADVI_FIRMBKTS (firm-specific buckets), MDPF_CANON (canonical flow, no forks), ADVI_BDPRCE; cottonwood back-end data and the portfolio-group check (no project yet) | dell1 |
| **P4 MCP infrastructure** (secondary) | year end | NFRA_OPLGTW, NFRA_MCPINDEX (with the opal-data-harvest tool set) | site Z, in the background |
| close or hold | now | NFRA_CTLPLN (laptop), NFRA_MCPORTAL (site Z) | |
| **secondary** ("every other project is secondary to these three") | -- | dell1: AMGT_RESAPP, AMGT_HARVST, ETFS_RIVALS, MDPF_DEMQUE, MDPF_SECCLASS, MDPF_SECHIST, MDPF_STRATID; dell2: ADVI_BILLING, NFRA_OPSWKF; laptop: COMM_ASSIST, NFRA_SPMOVE | |

## 2. The problem the dates expose

Both items with the nearest dates, P2 (Oct 24) and P1 (Nov 15), sit on **dell2 alone**. dell2 also carries ADVI_BILLING and
NFRA_OPSWKF. dell1 and the laptop hold mostly secondary work. If boxes stay as they are, dell2 is the bottleneck for both dates.

## 3. Organization (as ANSWERED by Andrew ~18:3xZ-18:4xZ, `ANDREW_DIRECT_20261014_183xZ_FIVE_CALLS_ANSWERED_AND_BD_ASOF_CITATION.md`)

**Andrew's answers override the recommendations below where they differ:**
- **No box moves.** dell2 keeps all three Ticket Center channels ("it's all so connected, and DELL2 has the capacity").
- **No dell1 seat goes to P1.** dell1 drives ADVI_FIRMBKTS through completion, ongoing testing and decommission, so that
  ADVI is ready with the canonical pipeline and bucket design.
- **The laptop takes none of the four items** and keeps driving COMM_ASSIST and NFRA_CTLPLN at the normal pace ("does not
  lose us any ground").

The original recommendations follow for the record.

**dell2: P2 to Oct 24, then P1.**
- IRPT_ANLREQ stays the lead. Its remaining blockers are Andrew's: `f61b` (the PROD execution ID), and approvals `c8c3` and
  `1f3e`.
- IRPT_DASHBD and IRPT_BCKEND continue on P1 alongside.
- ADVI_BILLING and NFRA_OPSWKF are parked now.

**laptop: takes TCKT_VNEXT's two lesser channels (MOVE, needs yes).**
- The trade request channel is an upload of a trade request form. Build it now with a placeholder; the real form is a
  swap when it arrives in about a week.
  - Its first read is NFRA_OPSWKF's resume packet. NFRA_OPSWKF is held on dell2 with its trade-request scope: external
    and internal trade request, and the live 409 "not a trade_request ticket" defect on engine submit. Packet:
    `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/RESUME_PACKET_NFRA_OPSWKF_20261014.md`
    (1.0.0_SA_CTO~DELL2, its msg 7797).
- The meeting request channel is in-house, with no Calendly. Every request goes to Jeanette's queue, and she confirms or
  reschedules on the dashboard.
- Both are portal work that lands through the new merge-forward route. The laptop has room for it:
  - NFRA_DEVPLN is closed;
  - NFRA_CTLPLN closes or holds (below);
  - COMM_ASSIST drops to secondary.
- This frees dell2 for the analysis request and P1.

**dell1: P3 groundwork now, full force from Nov 15.**
- MDPF_CANON and ADVI_FIRMBKTS continue: the canonical flow and firm-specific gold buckets are the long pole of P3.
- A new P3 cell takes cottonwood's back-end data and the portfolio-group check.
- The number audit (every displayed number) is cut once P1 checks out.
- The secondary dell1 projects are held after their current round drains: the AMGT pair, ETFS_RIVALS and the four MDPF
  side projects. Their seats move to P3.
- **Ask, needs yes:** whether dell1 also lends a seat to P1 (the performance tab's per-firm data). The firm-bucket work is
  shared with P1.

**site Z: P4 in the background.**
- NFRA_OPLGTW and NFRA_MCPINDEX continue at normal pace; the opal-data-harvest assessment is already in.
- NFRA_MCPORTAL finishes its open close runs (your acts `21d9`, `21c5`, `8ed7`, `f0d2`), then closes or holds.

**laptop's own projects:**
- NFRA_CTLPLN finishes what is in flight (round 13, the dell1 FWD-11 restart tonight), then closes or holds.
- COMM_ASSIST keeps muse running with no new rounds after CA-j-14/15/16, unless Andrew says otherwise.
- NFRA_SPMOVE stays parked.

## 4. Dated milestones (the cluster lead reads them at each hourly tick)

| date | P2 (Ticket Center) | P1 (Investor Reporting) | P3 (Advisor Intelligence) |
|---|---|---|---|
| Oct 17 | analysis request end to end on DEV, 4 attachments on a ticket | coverage census: every client at every firm, tab by tab (denominator printed) | cottonwood back-end census and portfolio-group read |
| Oct 21 | analysis request on PROD (Andrew's approvals); meeting request on DEV | gaps from the census cut as one round | canonical-flow migration plan per pipeline |
| Oct 24 | **all three channels on PROD** (trade request with the real form if it has arrived, else the placeholder stated) | | |
| Nov 1 | | performance tab working on every firm in the census | firm buckets live for 49F and cottonwood |
| Nov 15 | | **P1 complete** (internal) | full force begins: the every-number audit |
| Dec 1 | | external date | **P3 complete** |

## 5. What waits on Andrew

1. ANSWERED ~18:3xZ: no box moves (see section 3).
2. The P2 blocker still in his queue: `f61b` (dell2). `c8c3` and `1f3e` are approved.
3. The trade request form (arrives in about a week, per his note).
4. Jeanette's mailbox spelling, to confirm (the transcript reads "Jeanette at opalinvest.com").
