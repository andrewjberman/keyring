# RULING 2026-10-13 ~17:3xZ (1.0.0_SA_CTO, laptop, cluster lead) -- cluster positioning on the pivot aggregate

**Input:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md` @d737bd0ed1 (sections 5-6),
read with the six transcripts and today's six Andrew-direct records. **Asked by:** Andrew, ~17:3xZ ("review these so we can
identify how best to proceed across all boxes"). **State read 17:31Z:** since the aggregate, the Dell admin-group grant is ruled
(@d2f79ea8dd), NFRA_DEVPLN v0.2 and COMM_ASSIST v0.6 are signed, and NFRA_CTLPLN round 12 is issued (@f94216ea59, frozen).

**Status: PROPOSED.** The box acts in section 2 go out on Andrew's go. Section 3 lists the calls only he can make.

## 1. The read

The CRO's read holds: on five of six surfaces the effort runs opposite to Andrew's ranking, and his top outcomes break at the
joins between projects. The fix is to re-point seats that already exist, plus a few small PRD addenda and one small new project.
No new seat is needed.

## 2. Positioning per box (ruled; acts on Andrew's go)

| box | drive (the only work until done) | re-point | park / close |
|---|---|---|---|
| dell2 | ONE workflow: an analysis request filed on the Ticket Center produces 4 attachments on the ticket (upload, form, Opal report, AI commentary), with no hands | IRPT_ANLREQ `~Y2` leads. TCKT_VNEXT merges into it. YCDGEN `~G2` keeps the report engine. TRNSPT keeps its commentary half under ANLREQ. Fix `commentary_requested` in the form's request (a code defect; no word needed). IRPT_DASHBD default report is P2. | ADVI_COTBKF: one active-account-set cell, then park. TRNSPT transcripts-database half: park. DSGN_IRPTV1, NFRA_OPSWKF, ADVI_BILLING: park until the workflow is live. |
| dell1 | (1) Security Analysis V1: all 93 names complete and fast; (2) AI fill of thin sections (RESAPP addendum); (3) FIRMBKTS migration and decommission plan; (4) DEMQUE<->SECCLASS sync rule, one cell in each | RESAPP from cold-start log lines to the V1 items. Freed MDPF COO seats take AMGT V1 and AI fill. | MDPF_SECHIST and MDPF_STRATID: the CVO grades each once; close if met, else park. HEALGAP closes at 6/6. |
| site Z | MC Portal as the one control panel: FWD-20 (read) live and read by Andrew, then FWD-21 (edit tools, channels and tiers per person, writes Andrew-only) | OPLGTW's next round feeds the panel (backfill status, cadence) instead of upkeep. One MCPINDEX round: catalog rows for every served tool plus harvest. Bloomberg agent: a read-only trace first. | NFRA_OPALAI, NFRA_MCPMSP: park (his memo: "does not really matter"). Close site Z's 2 COMM_ASSIST calls; the project moved to the laptop. |
| laptop | NFRA_CTLPLN round 12 as issued (tailnet, fence, gates); NFRA_DEVPLN (`~DV`); COMM_ASSIST through muse (`~CA`). 3 COOs = the limit. | Laptop CloudOps `~ANL`/`~FBL` stand down when the Dell admin-group grant is read back on each Dell. | Pare-down closes already recorded; SPMOVE parked. |

Ruled here without a further word, because Andrew's memo or a standing law already decides it:
- Security Analysis PROD promote (call `e7f2`): the page is staff-only, so the push law needs no word. dell1 promotes after it
  checks that the bundle changes no client-facing page.
- "news" in the laptop memo means muse: his written word at ~14:3xZ.
- Billing: custodian fees feed the EXISTING Fee Summary panel; no second panel on PROD ("we don't want to duplicate").
- Former Cottonwood clients are excluded from every vendor draw, not ranked last ("we don't need to waste quota on this").
- YCharts: a separate small project that feeds DEMQUE ("may be a separate project"). The laptop CRO writes the L1 brief; step one
  measures coverage of the 17 DEMQUE items.
- One gateway, two logins (`opal-gateway-bbg` stays as a login entry), both visible and managed in MC Portal ("so be it, but it
  has to be visible and managed there").
- Harvest for asset managers in V1: derived layers and article links only, no raw publisher text. Andrew can widen this.

## 3. Calls only Andrew can make

1. dell2: put the Ticket Center's service principal on the C-SWITCH allow list (ticket-filed requests only). Without it no ticket
   reaches the Opal engine. REC yes.
2. dell2: an agent files the end-to-end test as a synthetic partner-firm advisor, minted and deleted under a never-widen pair, in
   place of the Opal-staff filing (call `2e30`). REC yes.
3. laptop tailnet: delegate the four password-off lines to laptop CloudOps, and approve a laptop local account for key SSH. REC yes
   to both.
4. ADVI_FIRMBKTS: the four decisions held since 2026-09-14. RECs: retire the Door 6 marker with its watcher; keep the B2
   credential; log write events on the legacy buckets; `mockadv` follows 49F.
5. AMGT AI fill provider. His memo says "open AI calls". REC the existing Anthropic path with server-side web search, unless he
   means OpenAI specifically.
6. AMGT "load fast": the number. REC under 3 s for the first request of the day.
7. dell2 "templates sent last week": name the files and one approver. REC start from the IRPT_CUSTDY-built 49F template.

DEMQUE depth (aggregate decision 4) stays with Andrew's dell1 session; he said he is handling DEMQUE there.

## 4. Routing after the go

Each box's lead CTO (`1.0.0_SA_CTO~DELL1`, `~DELL2`, `~Z`) receives its row through `0.0.0_AB_MSTR`, with this file as the
carrier. Mid-round specs stay frozen: each re-point lands at that project's next round-N analysis, never inside a live round.
