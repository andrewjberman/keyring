# opal_ai / NFRA fabric -- status, next steps, dependencies

Prepared by 4.0.0_SA_CRO~O on 2026-10-01 at Andrew's request ("deep dive analysis of current state ... status across
their projects, associated next steps and dependencies"). Read-only. Measured 15:21-15:39Z (11:21-11:39 ET):
- each project's `project.json` and every task order's LAST `<status>` tag (denominators below);
- git since 04:30Z;
- the seats' drive logs and `fabric-check --agents`;
- the CTO's self-drive tick-13 log;
- the live gateway artifact (S3 git-ref) and `EC2_MANIFEST.json`;
- open deploy ledgers on 110 worktrees.

Times are ET.

## Headline

**The fabric is not stalled. It is waiting, mostly on you.** Overnight the seats shipped the entire opal-gateway
release train: 5 host releases and 4 Terraform acts, with no rollback. Of the four seats you named:
- 1 is working right now (COO~O, gateway release slot 5, mid-deploy);
- 1 is waiting on a scheduled run tonight (COO~MI);
- 2 are parked on acts only you can perform (COO~AI, COO~MS).

0 of 5 projects are complete. 3 can progress without you; 2 cannot.

## What landed overnight (the gateway release train)

| Slot | Release | Project | Live at (ET) | What it added |
|---|---|---|---|---|
| 1 | MX-r-7 | MCPINDEX | ~3:14 AM | Black Diamond fees tool + ETF positioning tool; BD reader role (TF #1) |
| 2 | MS-d-2 | MCPMSP | ~5:1x AM | MSP internal reader role, sender gate, admin refusals (no new tools) |
| 3 | OG-rl-1 | OPLGTW | 6:44 AM | 3 meeting-transcript tools, 2 mail tools, `/hx/transcripts` + `/hx/mail` headless routes; secrets + ALB rule (TF #2, #2b); principal rosters moved into Secrets Manager |
| 4 | MX-r-8 | MCPINDEX | ~8:36 AM | discover reads silver datasets; portal readers routed through the internal role (G-RDR) |
| TF #3 | MS-dn-1 | MCPMSP | ~11:2x AM | gateway identity DENIED firm data (3 firm keys explicitDeny, global key allowed; CTO-verified) |
| 5 | OG-rl-2 | OPLGTW | **in flight** | `/hx/mail` message-listing route. Ledger opened 11:32 AM; the live artifact already reads `0a1d9079c6`; read-back pending |

Every collision my 04:3xZ trace named (C1-C12) was handled inside these releases.

## Per project

### NFRA_OPLGTW (gateway) -- COO~O: WORKING

- Orders: 65 total; 56 complete, 4 superseded, 2 pending, 3 staged.
- **Now:** OG-rl-2 PHASE B deploy (both never-widen halves signed). Next: read-back, ledger close, then the L10 slug to
  the CTO.
- **Then:** the CTO's analysis, then the next enrichment round. It carries Z-S32 (`.env` shape), Z-S34 (roster log
  count), Z-W21-S19 (TF root must plan clean under safe-apply) and Z-W19-S13 (one contract source).
- **Held on you:**
  - OG-tx-2, live transcript reach: G-TEAMS-TX, the Teams transcript policy via Opal IT.
  - OG-g-1, OG-v-7, OG-v-8 (controlled identity, walkthrough grading): G-C, the Opal IT test user, and G-D, your
    walkthrough.
- **Laptop customer:** NFRA_TRNSPT's order 103564 (PDF bytes over `/hx/mail`) is MET. The listing route is laptop order
  103750.

### NFRA_MCPINDEX (index + data tools) -- COO~MI: IDLE (legitimate clock wait)

- Orders: 86 total; 50 complete, 34 superseded, 1 cancelled, 1 pending.
- **Round 6:** 5 of 6 terminal, and the CVO graded L8/L9 (7 rows to REMEDIATION_v5, MXV7-J1 PASS).
- **Waiting on a clock:** MX-s-16 closes only on tonight's scheduled `bd-silver-merge` run, ~8:1x PM ET. Then the
  slug, the CTO's round-6 analysis, and round 7.
- **Waiting on a person:** r6.J1 / MXV7-J2. Alyssa asks cold through her Schwab grant (positions + transactions).
  Slot 4 is live, so **this can happen today.**

### NFRA_MCPMSP (MSP Analyst) -- COO~MS: BLOCKED-SOVEREIGN

- Orders: 24 total; 21 complete, 3 staged.
- **Done:** round 2's build and both host and IAM acts (MS-d-2 live, MS-dn-1 Deny applied).
- **The ONLY gate on round 2:** **G-MSPID**, the MSP calling identity. You answered "Not yet" (msg 27426). It holds
  MS-sv-1 (live pilot refusal), MS-rn-1 (one replayable run) and MS-rx-1 (replay from record). There is no L8 or L10
  until they run.
- **Parked, not round-2 gates:** G-USER (Opal Analyst M365 user), G-IT-INF, G-ADVISOR, G-FIRM (partner onboarding),
  G-KEY (per-firm API key spend). Also G-MSPCL: Claude signed in under `Opal_MSP`, for the supervised session.

### NFRA_OPALAI (Opal Analyst runtime) -- COO~AI: BLOCKED-SOVEREIGN

- Orders: 37 total; 31 complete, 2 superseded, 4 pending.
- **Built and held:** OA-t-1 (product files move) and OA-t-3 (runtime launch-gate fence) pass 3/3 on held branches.
  They merge only in the cutover window.
- **Gate 1, G-PUSH:** promote opal_ai `r2-dev` to PROD (origin PROD still `fd8ab8a57f`), on your word via MSTR~Z
  (msg 27528).
- **Gate 2, the DAPI 8194 wall:** OA-f-10's Firewall script is built. Applying it is your admin act, and the apply is
  its own falsifier (Opal_Agent -> 8194 must read REFUSED, with 8790 and the operator still OPEN). Reason: OA-e-6
  measured that Opal_Agent reaches Bloomberg 8194 directly (my ~7:54 AM ET research brief @5d804ea419). MSTR~Z presented both to you
  side by side (msg 27882); no word yet.
- **After both:** the item-0 close run (the Analyst reads `agent/refs`; the CVO grades t-1 J2), then OA-e-8 (speed
  measure), then close.

### NFRA_MCPORTAL (dashboard grants) -- COO~MP: not seated (nothing it can do)

- Orders: 18 total; 13 complete, 3 superseded, 2 staged.
- **Done:** round 3's build (grant writer live).
- **Gated on you:**
  - G-CLOSE (MP-c-1): name a colleague, narrow their grant, they ask, widen it, they ask again.
  - G-2ND (MP-v-1): a person signs in as Opal Bloomberg in the worker's headed browser.

## Acts only you can perform, ranked by what each unblocks

1. **G-PUSH + the 8194 wall apply** (one sitting with MSTR~Z). Unblocks NFRA_OPALAI's cutover, close run and close.
2. **G-MSPID** (the MSP calling identity). The sole gate on NFRA_MCPMSP round 2.
3. **Alyssa's cold run (r6.J1)**, possible today. Closes MCPINDEX's FWD-1 judgment.
4. **G-CLOSE + G-2ND.** The sole gates on NFRA_MCPORTAL round 3.
5. **G-TEAMS-TX and G-C/G-D** (Opal IT plus your walkthrough). Unblock OPLGTW's live transcript and controlled-identity
   cells.
6. **The D9 placement card** (CVO verdict 27494; REC: move OPLGTW/MCPINDEX to D6 at round close). Bookkeeping only.

## What moves without you (next 24h)

- **COO~O:** finish OG-rl-2, then slug, then the CTO analysis, then the enrichment round.
- **COO~MI:** ~8:1x PM ET scheduled run, then MX-s-16 closes, then slug, then the CTO round-6 analysis, then round 7.
- **CTO~O:** self-drive armed, 60-minute ticks. Two analyses are owed, each on its slug.

## Risks and loose ends

- **REMEDIATION_v5:** 7 open rows from MCPINDEX round 6, for the round-7 cut.
- **One open deploy ledger** in scope on the shared tree: `nfra-mcpindex-r6-bd-merge-retire`. It is open by design
  until tonight's run.
- **Opal_MSP** also needs the 8194 wall. The CTO ruling covers both accounts.
- **`C:\blp\DAPI` is `Users FullControl`.** It is a tamper surface, surfaced to the box operator and not chased.
