# BRIEF -- bringing dell1 and dell2 in now: what goes where, in light of the control plane, for the three quarterly goals

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-06 ~18:5xZ (2:5x PM Eastern); RDP section added ~19:0xZ.
- **Order:** Andrew-direct ~18:3xZ, verbatim with his voice transcript in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`.
  This is his "Document 2". Document 1, the census it stands on, is `docs/briefs/project-census-two-boxes-20261006.md`
  ("the census"; sections cited).
- **Consumers:** Andrew (section 8 decisions); `1.0.0_SA_CTO` (placement, the control plane's round 2, new registrations);
  `0.0.0_AB_MSTR` (the quarterly goals into `org/missions/GOALS.yaml`; seating).
- **Claim marks:** MEASURED = read today at the file or command named. PROPOSED = this brief's recommendation.

---

## 1. The answer in seven lines

1. **The Dells can take work as soon as they are standing; the control plane is closer than it looks.** Round 1 is done
   and graded: publishing a branch no longer deploys (FWD-5), every box is named once in one register (FWD-2), each box
   writes its own append files (FWD-8), and every project has a box field (FWD-7) (census section 5).
2. **What still stands between a Dell and real work is four things, all one round:** the Dell set up and registered; its
   message queue; its own cloud identity that cannot deploy; and a way for its finished round to reach the trunk
   (section 3). The bidding operation is NOT on that path: first placements are the CTO's call, which you approved.
3. **Start new work on the Dells; move in-flight work only at round ends.** New projects carry no state to migrate.
   MDPF_SECHIST (the securities database, your "pipeline aggregation") has a signed PRD and no round yet: it is the
   ideal first real round on dell1 (section 4).
4. **Target layout:** laptop = planning seats + the control-plane lane only; site Z = its in-flight research and
   gateway work + integration, deploys and Bloomberg; dell1 = Investor Reporting and the ticketing workflow; dell2 =
   the securities and Cottonwood data spine (section 5).
5. **Capacity:** the laptop runs 4 to 5 execution lanes today against a limit of 3; site Z runs about 6. The Dells add
   4 to 6 lanes. That covers moving the laptop's lanes off it and starting the quarterly work, with little to spare
   (section 6).
6. **The three quarterly goals are written down here** and offered to the fabric manager for the goals register
   (section 7). Q-1 needs one programme brief that ties its eight projects to the January 1 date; Q-2 and Q-3 start as
   research now.
7. **Seven decisions for you** (section 8). The one that gates everything: confirm the Dells are physically set up, so
   the control plane's round 2 can be cut today.
8. **Your added requirement, NOT yet in the control plane: Remote Desktop on every box, reachable over the tailnet,
   above all from your MacBook** (section 3a). Today it works for the laptop and site Z only, by setup, not by design;
   the Dells are not on the tailnet yet. It goes to the CTO as a new outcome.

---

## 2. The control plane today, measured

| Outcome | What it gives | State |
|---|---|---|
| FWD-5 | pushing any branch other than the trunk deploys nothing | **PASS**, live on the laptop; on site Z once it pulls `66b1b42a71` |
| FWD-2 | one register of boxes, `org/devices/DEVICES.json`; every script reads it | **PASS** (laptop, site Z registered); adding a third box is round 2 |
| FWD-8 | per-box append files, a commit check that refuses the wrong box's file | **PASS** |
| FWD-7 | a box field on every project, a placement read | **PASS**; 26 cross-box write overlaps found, mostly the shared deploy ledgers |
| FWD-1 | the thread: one round planned on the laptop, worked on dell1, merged by site Z, graded on the laptop | **not started**: needs dell1 |
| FWD-3 | messages to and from any box | **not built**: the queues exist for laptop and site Z only |
| FWD-10 | each box's own identity; a Dell cannot deploy | **not built** |
| FWD-4 | publish and integrate (the round queue) | **not built** |
| FWD-6 | site Z's standing push rule | **text approved by you**; lands with FWD-4, never before |
| FWD-13 | moving work between boxes by bid | **not built**: `remote-job.py` reads the register now, but bids CPU and memory only and its awards still go through LDO-001 |
| FWD-9, 11, 12 | leases, restart safety, one decision list | **not built** |

The seat that built round 1 (`2.0.0_SA_COO~C`) is now running the Cottonwood backfill (ADVI_COTBKF). Nobody is assigned to
the control plane's round 2.

---

## 3. The shortest path to a working Dell (PROPOSED: the control plane's round 2, cut today)

| Step | What | Owner | Can run in parallel with |
|---|---|---|---|
| 1 | dell1 and dell2 set up from the new-device kit (`Opal_New_Device_Kit_20261005.zip`), signed in, the workspace cloned, `AGENTBUS_DEVICE` set | **you** (hardware, Windows and account sign-in) | 2, 3 |
| 2 | each Dell added to `DEVICES.json` with role "execution", lane limit 2 to start, and its fabric manager serial `0.0.0_AB_MSTR~DELL1` / `~DELL2` | the control-plane lane | 1, 3 |
| 3 | one inbound message queue per Dell (FWD-3), named by the builder; applied from the deploy box | the control-plane lane, applied by site Z | 1, 2 |
| 4 | a cloud identity per Dell that can read and test but cannot deploy, apply infrastructure or write production data (FWD-10) | the control-plane lane, applied by site Z | 1-3 |
| 5 | **publish:** the Dell's fabric manager pushes the finished round as `q/<device>/<PROJECT>/r<N>` (safe now: FWD-5 means it deploys nothing) | the Dell's fabric manager | -- |
| 6 | **integrate, interim:** until the queue and the standing push rule land (FWD-4, FWD-6), site Z's fabric manager merges the round branch and pushes the trunk **on your word**, exactly as today's rule requires | site Z's fabric manager; you | -- |
| 7 | the thread exercised once (FWD-1): the round is graded on the laptop with each hop's time printed | the CVO | -- |

**Step 1 also includes, on your word (section 3a):** each Dell joins the tailnet with Remote Desktop on, reachable from
your MacBook.

**Why step 6 is acceptable:** it uses the push rule that is in force today, so nothing waits on new law. Its cost is that
each integration needs your word. Recommended: one word per integration window (morning and evening), not per round,
until FWD-6 lands.

**What is deliberately NOT on this path:** the bid (FWD-13), leases (FWD-9), the decision list (FWD-12). They matter when
four boxes are under load; they do not block the first rounds. They are the control plane's round 3, worked in parallel
by the same lane.

**Hard rules the Dells keep from day one:** they never push the trunk, deploy, call a vendor or write a register (the
PRD's C-ROLES). Any round that ends in a deploy (an S3 write, a Lambda, a Terraform apply) hands its deploy to site Z.

---

## 3a. Remote Desktop over the tailnet on every box (Andrew-direct ~18:5xZ; NOT covered by the control plane today)

Your words: "we need RDP on all devices accessible via tailnet" and "we are going to need to have that RDP ability from
any device in the tailnet, namely the macbook" (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_185xZ_CTLPLN_RDP_ON_ALL_DEVICES_VIA_TAILNET.md`).

**Is it covered? No.** MEASURED: the NFRA_CTLPLN PRD, its STATUS file, the device register, the brief and the proposal
mention Remote Desktop, RDP, Tailscale or the tailnet zero times. It is a new outcome for the CTO to add.

**What exists today (MEASURED from the laptop, ~19:0xZ):**

| Tailnet device | Address | Remote Desktop port 3389 over the tailnet |
|---|---|---|
| laptop (`andrew`, Windows) | 100.96.167.100 | answers; Remote Desktop is enabled in Windows |
| site Z (`opal-bloomberg`, Windows) | 100.99.180.19 | answers |
| your MacBook (`andrews-macbook-pro`, macOS) | 100.98.173.75 | the client; on the tailnet |
| iPhone (`iphone181`) | -- | offline 13 days |
| `muse` | -- | on the tailnet; unidentified |
| dell1, dell2 | -- | **not on the tailnet yet** |

The tailnet account is `Andrew@opalinvest.com` (MSTR record, 2026-08-18). Site Z joined it on 2026-08-18.

**What the outcome should say (PROPOSED, for the CTO's endpoint):** from the MacBook (or any device on the tailnet),
Andrew opens a Remote Desktop session to any box in the device register, laptop, site Z, dell1 and dell2; the register
records each box's tailnet name and address; and Remote Desktop answers over the tailnet only, not on the public
internet. Proven by one session from the MacBook to each of the four boxes.

**Not measured:** whether each box's Remote Desktop is limited to the tailnet by firewall scope, or open on every
network; whether the MacBook has a Remote Desktop client installed; who `muse` is.

---

## 4. The first real round on a Dell (PROPOSED)

**MDPF_SECHIST round 1 on dell1.** It is the securities database you described in the transcript ("our securities
database ... the inflowing securities through the positioning ETF channel, through models, through investor reporting,
through Advisor Intelligence"). Its PRD v0.1 is signed and no round has started (census 3.1), so nothing migrates. It
feeds Q-1 directly (every performance report needs every security's history). Its overlaps with MDPF_SECCLASS (laptop,
round 7) are the reason to check its write set first with the placement read; if they overlap, it goes to the same box
as SECCLASS when SECCLASS moves (section 5).

Fallback if the CTO finds an overlap: ADVI_COTBKF's round 2 (the Cottonwood backfill's silver and document index), which
begins after round 1 closes on the laptop.

---

## 5. What goes where (PROPOSED)

The rule: a project or workstream sits whole on one box; two boxes never write the same files; in-flight work moves only
between rounds; new work starts where it will live.

| Box | Holds | Moves in | Moves out |
|---|---|---|---|
| **laptop** (control plane) | CTO, CRO and CVO seats and their research lanes; the control-plane lane (NFRA_CTLPLN) | -- | every other execution lane, each at its next round end |
| **site Z** (integrator, deploys, Bloomberg) | its in-flight work until each closes: AMGT_RESAPP, AMGT_CORPUS, AMGT_HARVST, DSGN_AMGTV1, ETFS_RIVALS, NFRA_OPLGTW and the opal_ai family, NFRA_SPRINTWIN, ADVI_49F; plus every Dell's deploy step and the integration | -- | nothing mid-project; quiet rows (NFRA_REPORT, NFRA_IAMROLES202609, NFRA_OPSEC202609, NFRA_MCPORTAL) closed or parked by the CTO |
| **dell1** (Q-1 reporting and the ticketing workflow) | MDPF_SECHIST round 1 (the thread); then IRPT_YCDGEN (the YCharts in-house report, the first ticketing workflow) and NFRA_TRNSPT (investor commentary); then IRPT_DASHBD and DSGN_IRPTV1 when you lift the hold | MDPF_SECHIST now; IRPT_YCDGEN at its round-6 end; NFRA_TRNSPT revived | -- |
| **dell2** (Q-1 data spine) | MDPF_SECCLASS, ADVI_COTBKF, and the new Cottonwood consolidation adapter (Commonwealth history joined to daily Black Diamond data) | ADVI_COTBKF at its round-1 end; MDPF_SECCLASS at its round-7 end; the adapter as a new project | -- |
| **laptop, staying for now** | IRPT_BCKEND and ADVI_PERFRP (COO~P) | move to dell1 after the thread passes and the queue runs under load | -- |

**Why YCharts and commentary go to dell1, not dell2:** they are one workflow end to end (YCharts inflow, the in-house
report, AI investor commentary), which you named the ticketing system's first workflow. Keeping them on one box keeps
that workflow's files together.

**The vendor question for dell1:** IRPT_YCDGEN calls YCharts and Yahoo, and Dells never call a vendor. Those calls today
run on the cloud resident host, not on the laptop's disk; if every vendor call stays in the cloud (or on site Z), the
lane can sit on dell1. The CTO confirms this before the move.

---

## 6. Capacity (PROPOSED numbers; nothing measured on a Dell yet)

| | laptop | site Z | dell1 | dell2 |
|---|---|---|---|---|
| Execution lanes today | 4 to 5 (C, M, P, Y, D held) | about 6 (Z, X, RV, H, O, D) | 0 | 0 |
| Target | 1 (control plane) | 6 now, falling as its research projects close | 2, then 3 | 2, then 3 |
| Lanes it will carry | NFRA_CTLPLN | as today | SECHIST (thread), YCDGEN, TRNSPT; later DASHBD/IRPTV1, BCKEND/PERFRP | SECCLASS, COTBKF, the Cottonwood adapter |

Demand for new lanes this quarter: the Cottonwood adapter, the Q-1 programme's missing pieces (section 7), and later the
Q-3 build. Supply: 4 to 6 Dell lanes plus site Z's lanes as they free up. **It is tight but it fits, provided the quiet
projects are closed and the held design work stays held until a lane frees.** Research for Q-2 and Q-3 runs in CRO
research lanes on the laptop, which are planning seats, not execution lanes.

**One measured hazard:** the lane letter `D` is live on both boxes at once (census section 2). Before any lane moves
between boxes, the per-box serials (the PRD's C-SERIALS) must be in force, or two seats will share one name on a third box.

---

## 7. The three quarterly goals (persisted here; offered to `org/missions/GOALS.yaml`)

Your words are in the record named at the top. The deadline is yours: "it has to be done by january 1st".

### Q-1 -- Investor reporting from the custodian level, replacing Black Diamond (by 2027-01-01)

- **What done looks like:** performance reporting done natively from the custodian for every advisor at 49 Financial
  (first, through Schwab) and Cottonwood (next), with a report template per advisor firm. Inflection is low priority.
- **Projects already serving it:** IRPT_BCKEND, IRPT_DASHBD, ADVI_PERFRP, ADVI_49F (reporting and performance);
  MDPF_SECCLASS, MDPF_SECHIST (securities); ADVI_COTBKF (Cottonwood history); DSGN_IRPTV1 (the page); cold:
  ADVI_BDPARITY, ADVI_STITCH, ADVI_COTKEY.
- **Gaps (no project):** (a) the Cottonwood consolidation adapter: Commonwealth history plus daily Black Diamond data in
  one shape; (b) per-advisor-firm report templates; (c) one plan that ties these eight-plus projects to the January
  date, with the order of work.
- **Phase now:** PLANNING. PROPOSED: this seat writes one programme brief for Q-1 next, covering the gaps and the order.

### Q-2 -- Billing: buy or build

- **What done looks like:** you know who runs billing for these advisors today and how; whether Opal fronts an existing
  platform (your lead hypothesis: a simple interface that sends advisors to the Morningstar Wealth platform you named,
  transcribed as "buy all") or builds; what information billing needs, where it goes, and which workflows overlap.
- **Projects:** none.
- **Phase now:** RESEARCH. PROPOSED: a CRO research lane starts now from public sources; your counterparty conversations
  feed it as they happen. The integrations you named (Plaid for banking, DTCC for insurance and annuity data, a home-value
  API) are, by your own correction in the transcript, a separate later project, not Q-2.

### Q-3 -- The requirements for a trade-submission flow through Opal

- **What done looks like:** by January 1 you have at least a clear picture, if not the pipeline: a ticketing workflow
  that feeds your operations lead's system. The ticketing system's first workflow is the YCharts inflow (an advisor
  uploads holdings, the in-house report runs, AI investor commentary follows).
- **Projects already serving it:** IRPT_YCDGEN and NFRA_TRNSPT (the first workflow); cold or inactive: OPAL_TICKET_VNEXT,
  TRSB_LEDGER; the portal's trade-submission page exists (graded by the CVO this week).
- **Phase now:** RESEARCH, after Q-1's planning. PROPOSED: a CRO research lane maps today's trade-submission path with
  your operations lead.

---

## 8. Decisions for you

1. **Are dell1 and dell2 set up** (kit installed, signed in)? If yes, the control plane's round 2 is cut today; if not,
   setting them up is the first act and only you can do it.
2. **Round 2 as section 3**, with the bid, leases and the decision list as round 3 in parallel. REC: yes.
3. **The first real Dell round: MDPF_SECHIST round 1 on dell1.** REC: yes; ADVI_COTBKF round 2 as the fallback.
4. **Interim integration:** site Z's fabric manager merges Dell rounds and pushes on your word, one word per morning and
   evening window, until the standing push rule lands. REC: yes.
5. **The layout of section 5**, each move made by the CTO at a round end. REC: yes.
6. **Close or park the quiet projects** (NFRA_REPORT, NFRA_IAMROLES202609, NFRA_OPSEC202609, NFRA_MCPORTAL, and the
   cold flat-registry rows), adjudicated by the CTO. REC: yes; it frees site Z capacity.
7. **Start Q-1 planning and Q-2, Q-3 research now** (one programme brief from this seat; two CRO research lanes), and put
   the three goals into the goals register. REC: yes.

**One question, not a decision:** the transcript names your operations lead's software as "monocums". Please give the
correct name so Q-3's research starts from it.

---

## 9. What this brief does not claim

- No Dell was seen or measured. Lane limits of 2 to 3 are your estimate.
- Site Z's state after 2026-10-05 23:58 is not visible from the laptop (census header).
- MDPF_SECHIST's write set was not checked against MDPF_SECCLASS; the CTO runs the placement read first.
- Whether every IRPT_YCDGEN vendor call already runs in the cloud was not verified.
- No cost was estimated for the Dells' identities, queues or model usage.
- The research lanes for Q-2 and Q-3 have no start date until you say go.

## REFS

```
  THIS FILE        docs/briefs/four-box-acceleration-plan-20261006.md
  CENSUS           docs/briefs/project-census-two-boxes-20261006.md
  ORDER            org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md
  CONTROL PLANE    org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md (v0.3); STATUS.md beside it; org/devices/DEVICES.json;
                   .tools/placement-check.py; .tools/remote-job.py
  GOALS REGISTER   org/missions/GOALS.yaml (owner 0.0.0_AB_MSTR)
  MEASURED AT      2026-10-06 ~18:3xZ to ~19:1xZ, laptop
```
