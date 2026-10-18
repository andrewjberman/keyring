# Site Z box -- accomplishment report, 2026-10-16 to 2026-10-18 ~04:30Z

**By:** `1.0.0_SA_CTO~Z`. **Asked by:** ms (muse), on Andrew's word, via `0.0.0_AB_MSTR~Z` (bus 234854bd, msg 35618).

**Claim labels:**
- **[measured]** read this hour from git, the live host or a file;
- **[record]** taken from a seat's report that I did not re-measure;
- **[inferred]** a judgment.

## 0. First, a scope correction

**IRPT and the ticket center are not site Z work.** [measured]
- They are run from **dell2**: the seats are `2.0.0_SA_COO~D2`, `~Y2`, `~V2`, `~P2`, `~F2`, `~G2`, `1.0.0_SA_CTO~DELL2` and
  `3.0.0_SA_CVO~IRPT`.
- No site Z seat holds an IRPT or TCKT order.
- Site Z's live directives are D1, D4, D5, D6 and D12. IRPT and TCKT are in none of them.

Sections 1 and 2 are therefore a read of dell2's commits as they reached this box. dell2's CTO (`1.0.0_SA_CTO~DELL2`) is the
authority on both.

## 1. IRPT group work (dell2) -- read from the record

- **IRPT_ANLREQ, the analysis-request and commentary flow.** [record]
  - One synthetic end-to-end run went through the resident, the drafter and the packager under a signed pair (CTO half f0fbfde004).
  - It **stopped at the upload door with NOT_AUTHORIZED**, after a good mint and login (ledger irpt-commentary-e2e-20261017 CLOSED).
    Its deletes are done.
  - dell2's CTO ruled a read-only code trace of the door (TO-AR-y-400): is it a mint gap or a door gap? The same door gates window 5.
  - **Not yet passed by any run:** the upload door.
- **IRPT_DASHBD.** [record] An all-days Cottonwood rewrite pair is being prepared: 66 landed days, a scaling dry run first, then one
  republish. Its apply checker is built and self-tested (p201). The packet is still a draft, and the class_series publisher is ordered
  after the rewrite.
- **Other IRPT projects** (IRPT_BCKEND, IRPT_YCDGEN, DSGN_IRPTV1) read `active`; I did not read their rounds. [measured: status only]

## 2. Ticket center analysis flow (dell2) -- read from the record

- **TCKT_VNEXT (FWD-11, the Meeting Request journey).** [record]
  - The DEV leg was exercised and MET (outcome-line contrast 10.10:1).
  - The PROD leg was read-only MET: the real meeting ticket was read on https://opalinvest.dev, and Trade Request is absent from the
    New Ticket list.
  - **Still owed:** filing and confirming one synthetic Meeting Request ON PROD inside a routing window, then removing it. The pair
    is signed (amendment 8), to run on a weekday by 2026-10-23.
- **TCKT_EARLYWARN.** [record] TO-EWS-d2 is complete: six ews_check arms OK, the store persisted, ledger CLOSED.
- **The analysis request through the ticket center** is IRPT_ANLREQ above: it waits on the upload-door answer. [inferred: the same
  flow]

## 3. NFRA on site Z -- this box's own work

**Opal gateway (NFRA_OPLGTW)** [measured: git, live host reads by the appliers]
- **Three site Z releases went live:**
  - 9d5b712557 on 10-17 05:19Z;
  - efcc8ae19f on 10-17 18:11Z: the window tools moved off the event loop, so the first page fell from 29.75 s to 1.93 s;
  - d077cef043 on 10-18 00:02Z: the ETF peer tool's out-of-memory crash was repaired (475 MB, 4.5 s where it raised MemoryError),
    and the service now runs under a 1.4 GB memory ceiling.
  - Each was checked tool by tool against live before deploy (27 of 27 equal, or better where live failed). Each has a recorded
    rollback.
- **Two dell1 releases landed on the same host, with site Z clearing the window as host owner:**
  - 1753c741d9, harvest research;
  - 4257a2aa42 at 10-18 02:06Z, which adds `fund_relation` to research reports.
  - The next site Z release must carry dell1's file unchanged, and that is bound in the CTO half.
- **Round 41 closed (12 of 12 orders).** Round 42 is issued:
  - the page size was measured, and 30 was kept;
  - the "data absent" reason codes are documented in five client tools;
  - an SSRF audit of 18 outbound call sites;
  - a loopback-only, time-leased probe listener so the service itself can be tested without a standing credential. This was ruled
    after research by `4.0.0_SA_CRO~Z`.
- **The next release** (docs and test only) was signed by all three halves. It is now being re-cut for one wording fix the CVO
  raised: the fees tool must not call an empty list "a true zero" while source completeness is unmeasured.
- **Open:** the memory-hazard row (Z-S375) disarms only on a call through the service, which is what the probe listener is for. The
  window-tool row (Z-S338) waits on a real window call.

**MCP data catalog (NFRA_MCPINDEX)** [measured]
- Round 21: the served catalog was graded REALIZED. The host serves the signed blob 2cbe275d03, with 127 of 127 anchors.
- Carried: MX-s-19 (due 10-20) and the r7 ledger (to 10-21 06:02Z).

**MC Portal (NFRA_MCPORTAL)** [measured: git]
- FWD-20, the gateway breakdown page, is live. The email-deny guard was removed for andrew@ and opalbloomberg@; alyssa@ stays 403.
- The FWD-1 close run with Alyssa is postponed by Andrew ("def4 is postponed").

**Control plane (NFRA_CTLPLN)** [record]
- Round 30 is moving: the estate report blob prefetch is complete.
- The upload and QA run of the estate report runner are cut. One QA run read INSTRUMENT_FAILED on two strata, and that is open as row
  S9138.

## 4. Other significant site Z work

- **ETFS_RIVALS (rivalfunds; dell1 issues, site Z's Bloomberg Terminal seat executes).** [measured]
  - The held-price backfill was downloaded in full within the project's official limit, on Andrew's word.
  - A price-shift defect was found: late captures misdated closes, for example Lenovo (992 HK).
  - The corrected layer was **published to live S3 (256 objects; the live store went from 266 to 522)**, and Lenovo reads its true
    closes for 10-12 to 10-15.
  - Open at dell1: the next page build's check (72 h window) and one outlier (GQGU, about 25% change where every other fund changed
    93-100%).
- **MDPF_DEMQUE (Bloomberg demand queue).** [record] Fixes DQ-t-74/75 merged ahead of today's 14:00Z fire.
- **Cross-box duty.** [measured: messages and committed records]
  - Site Z cleared dell1's write or deploy windows on the shared gateway host and harvest gold: HVST cg-2, cg-3, cf-5 and ch-5, plus
    the C-10 harvest-rebuild window.
  - It ruled three cross-adjudications on 10-17 (XA-0e3e, XA-7bcd, XA-03dd).

## 5. What only Andrew can do (each cited in the site Z open-calls list)

1. Sign in once as Opal Bloomberg in the MP-v-2 headed window (f0d2).
2. Open /control-plane and /open-calls on the MC Portal (8ed7).
3. The Alyssa sitting (def4), postponed by him.
4. Have the named asset manager make one real harvest call through the gateway (5b35).

## 6. Infrastructure

The site Z infrastructure section (box passes, crossbox orders, seat liveness, relays) is `0.0.0_AB_MSTR~Z`'s, from its own record:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/SITEZ_BOX_REPORT_SECTION6_MSTR_20261018.md`. The combined text (11,227 B) went to ms on
the bus as MessageId `d7a74560-f044-4dd0-a004-559441d61c99` (SENT 04:4xZ; not acked by ms at msg 35622).

**Correction to section 3 (measured by MSTR~Z):** dell1's harvest release 1753c741d9 is in sitez HEAD. It was landed by `~NFRA1`
(OG-ap-37), drained by `2.0.0_SA_COO~O`, and is on origin/box/sitez and CLOUD.
