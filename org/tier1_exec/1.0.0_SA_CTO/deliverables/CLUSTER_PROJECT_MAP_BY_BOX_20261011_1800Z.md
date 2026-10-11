# Cluster project map by box -- 2026-10-11 ~18:00Z (1.0.0_SA_CTO, cluster lead; /draw on Andrew's word)

Sources: 50 `project.json` files, 31 `status: active` (placement field); seat-to-project mapping from commit authors on
origin/CLOUD in the last 8 h (denominator printed in the session); per-project cards from each project's latest round analysis,
newest orders and surprise channel, read 17:4x-17:5xZ; open calls from `open-calls.py list --all --cloud` 16:57Z (11 OPEN).
Corrections applied to the raw reads: CT-i-11's release was RULED YES this morning (XB-b98e), c290 closed (text received),
NFRA_OPSWKF gains the XB-74e2 FWD, LGIC_BLANKFIX is CLOSED and not drawn.

```
OPAL CLUSTER -- every active project, by box, with intent / status / next / blockers (2026-10-11 ~18:00Z)

1. The production plane -- how work is produced: 4 boxes, 1 trunk, 1 cloud queue of Andrew's calls

   BOX (branch)            SEATS LIVE ON IT (measured: commit authors, last 8 h)         PROJECTS       TRUNK / CLOUD
   ────────────            ──────────────────────────────────────────────────────         ────────       ─────────────
  ┌──────────────────┐    ┌──────────────────────────────────────────────────────┐
  │ LAPTOP           │───►│ 0.0.0_AB_MSTR (integrator) · 1.0.0_SA_CTO (cluster   │  3 active  ──┐
  │ box/laptop       │    │ lead, /loop :37) · CloudOps ~ANL, ~FBL (crossbox     │  (1 live,     │  box-sync every
  │ 100.96.167.100   │    │ executors for dell2 / dell1 pairs)                   │   2 parked)   │  /govern tick :00
  └──────────────────┘    └──────────────────────────────────────────────────────┘               │
  ┌──────────────────┐    ┌──────────────────────────────────────────────────────┐               │   ┌─────────────────┐
  │ SITEZ            │───►│ MSTR~Z · CTO~Z · CVO~Z · COO~O (OPLGTW, the ONE      │  7 active  ──┼──►│ CLOUD           │
  │ box/sitez        │    │ gateway-release issuer) · ~MI ~MP ~ZI · CloudOps ~Z  │  (4 driving,  │   │ one writer:     │
  │ 100.99.180.19    │    │ ~IR ~MX                                              │   3 parked)   │   │ 0.0.0_AB_MSTR   │
  └──────────────────┘    └──────────────────────────────────────────────────────┘               │   │ merge back to   │
  ┌──────────────────┐    ┌──────────────────────────────────────────────────────┐               │   │ every box/*     │
  │ DELL1            │───►│ MSTR~DELL1 · CTO~DELL1 · CRO~DELL1 · COO~B1 ~C1 ~R1 │ 11 active  ──┤   │ (:00 :06 :12    │
  │ box/dell1        │    │ ~W1 ~V1 ~D1 ~Q1 ~G1 ~M1 ~S1 · CloudOps ~FB1 ~RA1     │  (all driving)│   │  :18 per box)   │
  │ 100.79.95.44     │    │ ~ZC ~ZQ ~ZV ~ZW ~DELL1 · workers 0.9.0_WK_*          │               │   └────────┬────────┘
  └──────────────────┘    └──────────────────────────────────────────────────────┘               │            │ add/close
  ┌──────────────────┐    ┌──────────────────────────────────────────────────────┐               │            ▼
  │ DELL2            │───►│ MSTR~DELL2 · CTO~DELL2 · 3.0.0_SA_CVO (base) · COO   │ 10 active  ──┘   ┌─────────────────┐
  │ box/dell2        │    │ ~P2 ~Y2 ~G2 ~D2 ~C2 ~V2 ~T2 · CloudOps ~DELL2 ~IB2   │  (8 driving,      │ S3 open-calls   │
  │ 100.104.84.87    │    │ ~YC2 ~TV2 ~CB2 · workers 0.9.0_WK_*                  │   2 no lane)      │ fabric/open-    │
  └──────────────────┘    └──────────────────────────────────────────────────────┘                   │ calls/v1/box=*  │
   pacing on every box: /govern 60 m, /canonical-drive 60 m, /self-drive 60 m, /keep-driving OFF   │ 11 OPEN (1 fork │
   cross-box: files only (XB-*.json via agentbus), rulings by the laptop CTO, relays by each MSTR    │ 10 acts) 80 clsd│
                                                                                                     └─────────────────┘

   ── LAPTOP ─────────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌ NFRA_CTLPLN ── r6 · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────────────┐
  │ INTENT  the four-device control plane: laptop plans, site Z integrates, dells execute; one round, one writer   │
  │ STATUS  FWD-1..26 graded 10-09: 0 REALIZED, 18 advanced, 6 not served (1/4/6/9/11/13), 2 moved to COMM_ASSIST  │
  │ NEXT    enrichment E1-E8 in one issuance by COO~C (E1 re-based live thread, E2 Dell deploy read-back, E3 click  │
  │         route on a Dell, E4 12-message cross-box matrix); LD-0644 OpenSSH wave 2 is Andrew's act on all 4 boxes│
  │ BLOCK   CVO re-sign of PRD v0.22 ratified half before E1; 155 OBSERVATION rows undispositioned; no laptop COO   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ LGIC_LGCTFM ── r10 · 2026-09-20 · PARKED (CTO stop ruling) ────────────────────────────────────────────────────┐
  │ INTENT  the LENS: walk any product's AWS resources, render current vs canonical LGIC form, hand back a plan    │
  │ STATUS  8 of 10 FWDs REALIZED; round 10 closed 09-19 (32 orders, 31 terminal, 0 open)                          │
  │ NEXT    nothing cut; a round 11 needs an in-engine outcome to move                                             │
  │ BLOCK   FWD-4 = Andrew's read of ANDREW_CARD.md; FWD-6 = LGIC_CANON's C6 practice wave (49 Financial)           │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_SPMOVE ── r0 · 2026-10-01 · PARKED (no COO) ──────────────────────────────────────────────────────────────┐
  │ INTENT  standing job: Schwab transactions (masters 08242234, 08335338) as monthly workbooks to SharePoint AWS/ │
  │ STATUS  PRD v0.3 admitted, both halves signed, FWD-1..6 confirmed by Andrew 09-17; no decomposition, no orders │
  │ NEXT    L5 decomposition + L6 issuance (confirm site + tier, path grammar via LGIC_NAMING) once a lane exists   │
  │ BLOCK   coo_lane null -- a lane on Andrew's placement or when one frees; recipient switch (Menachem) OFF        │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

   ── SITEZ ──────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌ NFRA_OPLGTW ── r33 closed, r34 cut · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────┐
  │ INTENT  read-only Schwab questions + CSV downloads in Claude for Opal staff via the Gateway; also the release  │
  │         host for MCPINDEX, MCPORTAL and COMM_ASSIST                                                            │
  │ STATUS  r33: 10 of 10 orders terminal; 11 rows open, Z-S85 ARMED; last FWD tally 0 REALIZED / 2 NOT / 6 HELD  │
  │ NEXT    r34 one issuance: E1-E5 + E6 Z-S85 allowlist drain-back (first), E7 Z-S77, E8 caller census; ships     │
  │         MX-r-10 and NFRA_CTLPLN CT-i-11 (ruled YES by the laptop CTO this morning, XB-b98e) after OG-ap-6      │
  │ BLOCK   Z-S85 ARMED; OG-rl-16 waits on dell2 locating the Q3 SMArtX statement                                  │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_IAMROLES202609 ── r7 closed, r8 issued · 2026-10-11 · DRIVING ────────────────────────────────────────────┐
  │ INTENT  least privilege across every IAM role: a posture number with denominator, unused-permission read,      │
  │         re-runnable assessment, declared-vs-live reconciler                                                    │
  │ STATUS  r7: 6 of 6 terminal (x-3 narrow fail); 8 of 16 undeclared roles now in code; r8 IAM-y-1/y-2 pending   │
  │ NEXT    r8: E1 disarm Z-S42 first, E2 dead-global-bucket read-only sweep, E4 disposition tokens               │
  │ BLOCK   Z-S42 ARMED; FWD-4 needs an adopting lane; E3 retire lambda-test-role HELD on Andrew's word            │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_MCPORTAL ── r5 · 2026-10-11 · DRIVING, close run at Andrew ────────────────────────────────────────────────┐
  │ INTENT  mcp.opalinvest.dev operator console, Andrew only: tool library + grants, call log, kill switch,        │
  │         Control Plane, users, analytics, health, cost                                                          │
  │ STATUS  rounds 3-4 analysis: FWD-14 NOT REALIZED, 16 DEFERRED; r5 shipped MP-x-3/x-4, CP2 live (MP-r-2)        │
  │ NEXT    MP-x-5 close run (Andrew opens the Control Plane page, names one box's projects from it), then MP-q-1, │
  │         MP-v-2, MP-c-2; FWD-15..17 after FWD-14 grades REALIZED                                                 │
  │ BLOCK   sitez-21c5 + sitez-8ed7 = Andrew's walk; sitez-f0d2 = his second-account sign-in; MP-c-2 = Alyssa's   │
  │         sitting; watch Z-S27 cold read 3.9 s -> 10.6 s                                                          │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_MCPINDEX ── r9 closed · 2026-10-11 · PARKED at ROUND_CLOSE ───────────────────────────────────────────────┐
  │ INTENT  every Opal data property answerable in Claude from ONE versioned catalog (discover family, per-        │
  │         property tools, typed fallback query, fenced read roles)                                               │
  │ STATUS  r9: 5 of 5 complete, MX-r-10 live @c3af8687e4; FWD-18 REALIZED, FWD-19 NOT, FWD-11 HELD at Andrew      │
  │ NEXT    un-parks when a FWD-19 producer serves, Andrew books Alyssa's run (J1), or MX-s-19's 10-13 runs land   │
  │ BLOCK   Z-S97 ARMED (round-close suite 19 of 24; fix routed to COO~C); FWD-19 waits on dell2's ADVI_BILLING +  │
  │         NFRA_OPSWKF producers; FWD-11 waits on Andrew booking Alyssa                                           │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ COMM_ASSIST ── r14 · 2026-10-11 · PARKED at ROUND_CLOSE ───────────────────────────────────────────────────────┐
  │ INTENT  every Teams/Outlook message addressed to Andrew reaches his phone as a text with a draft in his voice; │
  │         nothing sends without his "1"                                                                          │
  │ STATUS  FWD-3/FWD-4 APPLIED not REALIZED; channel_poll fails loudly 30 of 30 (route=teams 404)                 │
  │ NEXT    on un-park: D2 read after CT-i-11 ships (ruled YES, XB-b98e; OPLGTW r34 carries it), check_e1_mail_day,│
  │         Z-S9 batch repair                                                                                      │
  │ BLOCK   CT-i-11 not yet shipped by site Z; sitez-058e (Andrew's test mail / sending mailbox); sitez-a519 (one  │
  │         Teams message, Andrew's act); client-branch yes/no (sitez-c719)                                        │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_MCPMSP ── r3 closed · 2026-10-09 · PARKED (G-MSPID) ──────────────────────────────────────────────────────┐
  │ INTENT  one Opal-hosted Teams agent serving partner firms (Inflection, Cottonwood first) from each firm's own  │
  │         data, the gateway assuming the asking firm's AWS role                                                  │
  │ STATUS  r3: 2 of 2 terminal, Z-W7-S1 REMEDIATED; enrichment list empty                                         │
  │ NEXT    after Andrew's G-MSPID word: re-cut MS-sv-1, MS-rn-1, MS-rx-1, then FWD-6/FWD-7                        │
  │ BLOCK   G-MSPID = Andrew supplies and signs in the MSP calling identity ("not yet" 09-30); FWD-2 on G-IT-COT   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_OPALAI ── r2 issued 09-28 · last 2026-10-01 · STALE 10 d (no r2 analysis) ───────────────────────────────┐
  │ INTENT  the Opal Analyst as a product: one Teams-facing agent over the indexed Opal MCP (opal_ai submodule),   │
  │         run from a released copy under its own non-admin account                                               │
  │ STATUS  r1: 0 REALIZED, 4 HELD, 9 NOT; r2 14 orders, 31 of 35 order files terminal by 10-01; identity gate pass│
  │ NEXT    OA-t-1/t-3 parent halves, OA-e-6/e-8 after the Z-S50 launcher fix; then item-0 close run              │
  │ BLOCK   OA-f-10 needs the Bloomberg Terminal on :8194; Andrew ships opal_ai DEV->PROD and runs the cutover     │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

   ── DELL1 ──────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌ ADVI_FIRMBKTS ── r4 issued · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────┐
  │ INTENT  move legacy bd/inf/cot buckets into spelled-out firm buckets, each firm cut over invisibly, each       │
  │         legacy bucket retired after a proven quiet window                                                      │
  │ STATUS  PRD v1.3; r1-3 closed (r3 13 orders: 8 complete, 5 parked); FWD-1 PARTIAL 184/209; r4 = FB-g-1..9     │
  │ NEXT    r4: the grant (g-2/g-8), two readers, WAF reconcile; then parked cutover acts 2/3/4/4b/4c              │
  │ BLOCK   D1-S17 ARMED (stale ownership map); D1-S21 act 4 waits on CTO; c290 CLOSED today (text received ->    │
  │         SNS routing fix proceeds, no Support case)                                                             │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ AMGT_RESAPP ── r95 executing · 2026-10-11 · DRIVING ───────────────────────────────────────────────────────────┐
  │ INTENT  the analyst's single-name research pack as the Security Analysis portal page, figures defensible from │
  │         the page and its print                                                                                 │
  │ STATUS  r94 closed MAY-CLOSE (CVO ADJUDICATION_v114); r95: aa-1..aa-6, 1/2/3 pending, 5/6 staged              │
  │ NEXT    aa-1 verifier stated_value (D1-S24), aa-2 withhold disagreeing row (D1-S26), aa-3 /compare 500s, aa-5 │
  │ BLOCK   e7f2 PROD promote = Andrew NO for now (visual smoke + breakdown given); D1-S24/S26 ARMED; aa-6 waits  │
  │         on MDPF_DEMQUE CRNCY; FWD-16 on his 09-15 hold; key rotation (86a2, done)                              │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ AMGT_CORPUS ── r47 issued · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────┐
  │ INTENT  the team's research corpus as a measured substrate; sector templates, fund forms, per-name             │
  │         continuation artifacts for Security Analysis                                                           │
  │ STATUS  r46 graded: 19 of 22 FWDs REALIZED (FWD-15 pending CVO re-sign); FWD-12/FWD-20 PARTIAL; r47 aw-1..8    │
  │ NEXT    aw-1 vendor-field labels, aw-2 Model tab, aw-3/13 number format, aw-4 redeploy, aw-5 portal DEV        │
  │ BLOCK   PROD release rides e7f2 (NO for now); FWD-12 master arm needs a FactSet template (63 master_absent)    │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ AMGT_HARVST ── r79 next · 2026-10-09 · DRIVING (slow) ─────────────────────────────────────────────────────────┐
  │ INTENT  harvest every publisher mention (SA, Bloomberg, Barron's, WSJ, FT) with provenance into bronze/silver/ │
  │         gold; chatter series + event spine                                                                     │
  │ STATUS  r78 analysis 10-09: runner fix merged, no live completed cycle read; FWD-18 unmet; 18 stale rows        │
  │ NEXT    r79 (COO~W1): bbg live cycle read 242/242, FWD-18 hop 3, disposition 18 rows, reconcile 39 orders       │
  │ BLOCK   Andrew's hand sign-in for WSJ/Barron's (site Z call 9f24); FT held ("don't attempt until I return")     │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ ETFS_RIVALS ── r28 closing · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────┐
  │ INTENT  six rival ETFs' daily holdings in one canonical shape with trade schedules; a daily research page with │
  │         AI analyses at /rivalfunds                                                                             │
  │ STATUS  PRD v0.21; r28 workstreams terminal, L9 addenda 1-9: wc/tw/wg/wh J1 MET, tc-1 NOT MEASURED             │
  │ NEXT    close r28 on three paired acts: aw-1 Lambda deploy, tc-1 merge, RIVALFUNDS_HISTORY_OWED switch-on      │
  │ BLOCK   site-Z producers need CTO~Z pairs; open ledger etfs-rivalfunds-r27 needs a dell1 L2 owner              │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_CANON ── r5 next · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────────┐
  │ INTENT  all MDPF gold to opal-data-mdpf as vintaged parquet, each firm's served slice in its own bucket, the   │
  │         two legacy gold trees retired on proof (page contract protects the served JSON)                        │
  │ STATUS  PRD v2.8; r4 graded (CN-d-1..5 MET); FWD-1 PARTIAL, FWD-3 NOT, FWD-5/7 in progress, 2/4/6/8 unstarted  │
  │ NEXT    r5 (COO~D1): CN-d-1 deploy D1/D2 under signed pair, runner code sync, 10-12 13:30Z gold fire read     │
  │ BLOCK   fe9b X2 global fold (a)/(b) at Andrew (rec A); deploy waits on MDPF_STRATID APPLY-R2 close; FWD-2/6    │
  │         wait on ADVI_FIRMBKTS cutover                                                                           │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_DEMQUE ── r9 · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────────────┐
  │ INTENT  price, rank and draw every history backfill within the Bloomberg + Yahoo budgets without crowding a   │
  │         production pull                                                                                       │
  │ STATUS  r8 closed MAY-CLOSE (5/5); FWD-3 APPLIED not REALIZED; C-PRICES NOT met 127/141; r9 under way          │
  │ NEXT    standing T-1 price-store extender (141 files end 06-23), lock reads latest partition, 14 rejected names│
  │ BLOCK   D1-S9 / D1-W22-S1 open; two ~40%-agreement names may be wrong securities; FWD-3 ACCEPT reads Mon 10-12│
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_HEALGAP ── r3 · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  the Cottonwood Rebalancer bronze heals itself the same day a lapsed vendor login fails the morning pull│
  │ STATUS  PRD v0.3; FWD-1/2/4 REALIZED, FWD-3 PARTIAL, FWD-5/6 NOT; r3 orders t9, t11-t14 complete               │
  │ NEXT    HG-t9 13:15Z stamp-gated satellites, HG-t5 after it, FWD-3 repair act, re-count 164 scheduled pulls    │
  │ BLOCK   FWD-6 item 5 waits on CVO re-sign; D1-S12 induce-restore condition; Schwab SI2 needs a person's login │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_SECCLASS ── r20 decomposed · 2026-10-11 · DRIVING ────────────────────────────────────────────────────────┐
  │ INTENT  one canonical per-security classification table (DynamoDB etf-classifications) read by every holdings │
  │         surface; legacy ticker-class copies retired                                                            │
  │ STATUS  r19: reads only, MAY-CLOSE, no FWD REALIZED (e84, remap-b MET; e79 NOT); r20 = SC-e-87/88/89           │
  │ NEXT    e-87 BD served-path reach, e-88 C_06 total-vs-class-sum trace, e-89 crossbox-deploy-check limbs        │
  │ BLOCK   D1-S23/S25/S26/S27 open (CTO~DELL1's); e57e61 FWD-10 apply HELD on its trigger; e56 member at dell2    │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_SECHIST ── r5 issued · 2026-10-09 · DRIVING ──────────────────────────────────────────────────────────────┐
  │ INTENT  fill every security's history to its ingestion depth and keep it complete day over day inside one     │
  │         Bloomberg budget                                                                                       │
  │ STATUS  PRD v0.3; r4: builds merged and green; D1-W14-S1 graduated (history_gaps PutObject missing)            │
  │ NEXT    r5: C-MMF repair batch, gold deploy pair with the history_gaps IAM statement, reads on the 10-12 11:00Z│
  │ BLOCK   4 stale rows need owners; the IAM statement is a STOP if the plan shows any other change              │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ MDPF_STRATID ── r2 · 2026-10-09 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  identify every Opal ETF Strategy and SMA sleeve at intake; count each once in the Global aggregate     │
  │ STATUS  PRD v0.3; FWD-1 REALIZED 10-09 (Global PFDE 410,420.98); u1/u2/W2-1..3 complete; APPLY-R2, W2-b pending│
  │ NEXT    close APPLY-R2 (leg L4 owed) + W2-b silver wiring deploy; FWD-2/6/7 read on scheduled fires            │
  │ BLOCK   Global output changes need the laptop's never-widen pair; Muni rule UNDETERMINED; gates MDPF_CANON     │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

   ── DELL2 ──────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌ IRPT_BCKEND ── r117-118 compiled · 2026-10-11 · DRIVING ───────────────────────────────────────────────────────┐
  │ INTENT  Investor Reporting backend (FWD-2/7/9/10): directory ingestion, scoped authz, provider normalization,  │
  │         YCharts generation, holdings joins, export                                                             │
  │ STATUS  PRD v0.38 signed by the CVO 10-11; r117-118 compiled by COO~P2, held by the gate on pending orders     │
  │ NEXT    two read-only witness tables (type field; 1,044 priced fund-dates), then an addendum; sleeve read       │
  │ BLOCK   Andrew: a vendor figure as Cottonwood's Performance answer (PRD:498, 09-28 word); no slug yet          │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ IRPT_ANLREQ ── r10 (ws Y) · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────┐
  │ INTENT  one Analysis Request end to end: Ticket Center form -> finished package (report, branded PDF with      │
  │         commentary, original Excel) on the same open ticket                                                    │
  │ STATUS  release 6 live (DbvBUxTG) but no product path reaches it; packager token minted 16:43Z (XB-282e, laptop│
  │         executed); 3 orders pending                                                                            │
  │ NEXT    AR-y-101 fallback on held candidate 5f64f409b0, y-102 composition-read build, y-103 return census      │
  │ BLOCK   D2-S51 ARMED; Andrew: PROD push for release 5's return (client-facing) + dell2-3cb1 (Alyssa files one  │
  │         request, "later"); laptop agent identity reads every secret (S1, standing, listed once)                │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ IRPT_YCDGEN ── r14 · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  Opal's own script calls YCharts, keeps every answer, generates Overview/Comparison/Multi reports in    │
  │         Opal branding; FWD-1 = one live Cottonwood Overview                                                    │
  │ STATUS  FWD-1 NOT MET, not yet run; eight reconciling irpt-jobs writes done 15:3xZ (XB-ca7a); resident st32    │
  │         installed, unexercised                                                                                 │
  │ NEXT    disarm plan for D2-W7-S1 and S16; attach path (token read, binding after ANLREQ release 6); st32 dry   │
  │         rollback                                                                                               │
  │ BLOCK   Andrew: FWD-1 sitting (asked 15:17Z) + svc-irpt-analysis on the producer allow list; ARMED D2-S38,     │
  │         D2-S45, D2-W7-S1, S16                                                                                   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ DSGN_IRPTV1 ── r23 · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  re-render Investor Reporting (header, Performance, Holdings, Analysis tabs) on the panel system;       │
  │         FWD-1 = one Cottonwood account read end to end                                                         │
  │ STATUS  84 of 84 orders terminal; six changes on portal DEV c3a03c24, PROD at 37aa1247, none walked on served  │
  │ NEXT    PROD candidate record, ask the laptop's /ui-walk of DEV, Holdings totals (D2-S14), hygiene cell         │
  │ BLOCK   Andrew: FWD-1 sitting on an Opal report + the client-facing PROD push (e7f2 covers the same DEV)        │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ IRPT_DASHBD ── r71 · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  client reporting dashboard: Opal-shape gold with GIPS total return, per-account gzip series; FWD-1 =   │
  │         one 49 Financial account in ~2 s                                                                       │
  │ STATUS  r70 made no served write; thresholds fix built, live function still oNgy4rnr; FWD-11/12 parked         │
  │ NEXT    count 49F manifests per prefix, census ten readers of the returns manifest, R45 REFRESH 4 packet       │
  │ BLOCK   Andrew: S3 delete of prior manifest versions (asked after reads); Monday 13:00Z fire writes one more   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ ADVI_COTBKF ── r71 · 2026-10-11 · DRIVING ─────────────────────────────────────────────────────────────────────┐
  │ INTENT  the Cottonwood 10-year Commonwealth backfill into opal-data-assets: kept as received, typed history,   │
  │         documents indexed, sensitive details held only where Andrew decided                                    │
  │ STATUS  r71 CTO analysis: all four judgments MET, nothing served moved; PRD v0.7 signed                         │
  │ NEXT    dividend adjustment test on 9 funds; correction list (2022 spin-off factor, 46-vs-43 day files)         │
  │ BLOCK   none at Andrew; ADDENDUM v0.7 holds re-serving until one re-serve carries every open correction        │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ TCKT_VNEXT ── r4 · 2026-10-11 · DRIVING ───────────────────────────────────────────────────────────────────────┐
  │ INTENT  Ticket Center takes typed requests, Analysis Request first: holdings file through the upload door,     │
  │         finished report returned on the ticket (WS-1, WS-2)                                                    │
  │ STATUS  FWD-1 NOT REALIZED (run 4 stopped at the resident's vendor session); 20 of 20 orders complete; fifth   │
  │         run's pair SIGNED @f439ec72a8                                                                           │
  │ NEXT    R4-pk1 package door binds firms from env list, creator-branch codes, fifth run once st32 installed      │
  │ BLOCK   Andrew: dell2-fbb1 close test ticket TCK-20261009 ("later"), staff notification list; PRD v0.1 DRAFT   │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_TRNSPT ── r23 issued · 2026-10-11 · DRIVING ──────────────────────────────────────────────────────────────┐
  │ INTENT  the Opal communications database (opal-data-transcripts): Teams transcripts, market updates,           │
  │         investment feedback, a draft-commentary service                                                        │
  │ STATUS  r23 = 5 cells (TR-mp23, tv23, om23, tt23, mf23); FWD-1 APPLIED (ACCEPT owed); FWD-2 0/4; FWD-3 NOT     │
  │ NEXT    mp23 re-apply mail pull (disarms D2-S22), readers.auto.tfvars, 4 missing Monday meetings, 10-12 fire   │
  │ BLOCK   Andrew: dell2-01c5 Research Team Meeting folder link; dell2-e260 FWD-8 second-reader roll (Opal_       │
  │         Terminal key, never used); his Monday FWD-5 read; D2-S22 ARMED                                          │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ ADVI_BILLING ── r3 · 2026-10-09 · PARKED (no lane) ────────────────────────────────────────────────────────────┐
  │ INTENT  advisory fees from Opal's own data (FWD-1..6), 49 Financial household z08219260 for 2026Q3 first, so   │
  │         Andrew can choose buy or build                                                                         │
  │ STATUS  FWD-1 EXERCISED on DEV only; FWD-2..6 unstarted; 12 of 12 orders complete over r1-3                    │
  │ NEXT    release packet E2 (tool + one s3:PutObject grant via site Z), land the Q3 statement, re-emit v2         │
  │ BLOCK   PROD push of the fee panel is Andrew's (client-facing); Q3 statement location unknown; his billing      │
  │         answers; also gates NFRA_MCPINDEX FWD-19                                                               │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ┌ NFRA_OPSWKF ── r1 complete · 2026-10-09 · PARKED (no lane) + NEW FWD TODAY ────────────────────────────────────┐
  │ INTENT  trade submission through Opal led by the ops lead's Excel workflow; FWD-1 = one trade request advisor │
  │         -> ops lead -> back, nothing typed twice                                                               │
  │ STATUS  r1: 7 of 7 complete (OW-e1/e2/e3, i1, k1, l1, p1); no CTO round analysis yet; D2-S1, D2-W1-S1 filed    │
  │ NEXT    new FWD: trade-dashboard-api internal-only check (CTO ruling XB-74e2 17:3xZ, MEDIUM, one cell), PRD    │
  │         addendum, round-2 cut; then FWD-2..7                                                                    │
  │ BLOCK   COO~O2 taken down -- the XB-74e2 cell needs a lane re-seated; Andrew's sit-down with the ops lead      │
  └────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

2. The query plane -- how you reach any of this from a terminal
    YOU (terminal, any box)
        │  "what is dell2 doing, and what is waiting on me?"
        ▼
   ┌────────────────────┐  picks the lens: open-calls.py list --all --cloud (S3, no pull) / Control Plane page
   │ 1.0.0_SA_CTO       │  (mcp.opalinvest.dev, MP-x-5) / project.json + latest ROUND_ANALYSIS per project /
   │ cluster lead       │  commit authors on origin/CLOUD (who is live, by proof of work)
   └─────────┬──────────┘
             │ reads, rules what is not yours, relays through each box's 0.0.0_AB_MSTR (agentbus, XB-*.json)
             ▼
   ┌────────────────────┐── hourly :37 ──► this map, re-read; rulings as CTO_RULING_XB_*.md; your calls listed once
   │ /loop (cron)       │
   └────────────────────┘
             ▼
   ANSWER back in your terminal: "dell2: 8 driving, 2 parked; waiting on you: IRPT FWD-1 sittings, PROD push of
   release 5's return, three dell2 acts (01c5, e260, 3cb1, fbb1); nothing else blocked on a decision."

  The "a box is a factory, CLOUD is the warehouse" model is exact and deliberate:
  ┌──────────────────────────┬──────────────────────────────────────────────────────────────────────┐
  │  factory (box)           │  warehouse + dock (CLOUD, S3 open-calls, crossbox files)             │
  ├──────────────────────────┼──────────────────────────────────────────────────────────────────────┤
  │ one COO lane per project │ one integrator (0.0.0_AB_MSTR) writes CLOUD, hourly per box           │
  │ workers never messaged   │ cross-box asks travel as files (XB-*.json), ruled by the laptop CTO  │
  │ /govern tick = shift bell│ open-calls S3 copy = the dock manifest; ABSENT is not empty          │
  │ surprise row = defect tag│ Andrew's acts stay on the manifest until his word, never decided      │
  └──────────────────────────┴──────────────────────────────────────────────────────────────────────┘
```

Stories: the production plane is the capacity story (31 active, 23 driving, 6 parked, 2 stale/no-lane, and exactly which lane
holds each); the cards are the blocker story (11 of the waits are yours by name, the rest are ARMED rows or cross-box pairs with a
named owner); the query plane is the reachability story: one command and one page answer "what is happening" without a seat.
