# Client Ops Early Warning -- current state, 2026-10-19 ~20:00Z (3:00pm CT)

**Project:** TCKT_EARLYWARN (D7 / macro TCKT, fast-path on Andrew's word) | **Author:** `4.0.0_SA_CRO~DELL1` (dell1)
**Record of every Andrew decision:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md` (addenda 1-7)
**Standing rule (addendum 5):** findings only. The system surfaces what happened, since when, and the evidence. It never recommends or
drafts client or advisor action.

---

## 1. In one paragraph

Four of the six scanners are built, replay-tested against this year's history, and merged. The three Schwab scanners (Sleeping Money,
Fee Tripwire, Payday Guard) run in AWS in one always-on container that keeps its store in S3. The email scanner (Inbox Radar) is built,
but it is switched OFF in the container: it has no mail access yet. Until it does, a stopgap version runs from this Claude session on
dell1, reading Andrew's mailbox every 30 minutes on weekdays. Nothing sends anywhere. The 10/19 design for a client-ops store with
9am/4pm scans and gateway tools for users is written and waits on Andrew's tenancy decision.

## 2. What is running right now

### 2a. The deployed service (AWS)

| Item | Value |
|---|---|
| Code | `infra/aws/ec2/client-ops-early-warning/` (on box/dell1; merged to origin) |
| Infrastructure | `infra/aws/terraform/client-ops-early-warning/` |
| Runtime | ECS Fargate, cluster `opal-clientops-ews-cluster`, task `opal-clientops-ews-task`, 0.25 vCPU / 1 GB (about $10-15/mo, approved) |
| Identity | role `opal-clientops-ews-role`. It reads the two Schwab silver prefixes of `opal-data-assets` and the secret `opal/ews/graph-app-cert`, and reads and writes one store key. It has no send, no delete, and no other S3 write. |
| What it runs | Sleeping Money, Fee Tripwire and Payday Guard over Schwab silver, on a timer loop (the daily T-1 file) |
| What it does NOT run | **The mail poller is OFF** by launcher (terraform main.tf lines 19-20). It has no mail access yet (section 4). |
| Store | SQLite persisted to `s3://opal-data-49financial/schwab/49financial/state/ews_store/current/ews.db` (builder address; the role is admitted to the 49financial fence for that one prefix). |
| Logging | each pass logs `items_opened rule=<name> n=<int>` per rule; no client data in logs |
| Deploy orders | TO-EWS-d1 (one container), complete @7d64231f73. TO-EWS-d2 (persist store plus log items), complete @c094fdcc1c. Both by `0.7.0_AE_CloudOps~TM1`, issued by `2.0.0_SA_COO~Q1`. |
| First durable pass (10/17, 573 dates) | Sleeping Money opened 2,829 (114 open), Fee Tripwire 751 (96 open, all measured), Payday Guard 125 (0 open). The CTO ruled the volume is real signal; the thresholds stand. |
| Open surprise row | TCKT_EARLYWARN-D1-S8: the TO-EWS-d1 deploy ledger entry still reads OPEN at HEAD although the order is complete. It is bookkeeping. |

### 2b. The stopgap Inbox Radar (this Claude session, dell1)

| Item | Value |
|---|---|
| What it does | Read-only. It lists new mail in Andrew's mailbox (which receives 49@ and inflection@) since the last run. An item opens when an advisor or partner sent the last message, the message is a real request, and no Opal reply came after it. Items age in business hours: OPEN, then WARN at 3h, then OVERDUE at 4h. It reports changes. |
| Where it lives | This Claude Code session on dell1, following `RADAR_RUNBOOK.md`. It reads mail through the opalgateway using Andrew's delegated sign-in. Its state is `radar_state.json`, in the session scratchpad (not the repo). |
| Trigger | Session cron job `aa8d1b56`: :13 and :43 past each hour, 9am-6pm ET (8am-5pm CT), weekdays |
| Limits | It dies when this session closes and auto-expires about 10/24. It sees only mail that reached Andrew's mailbox. It cannot read encrypted (Purview) messages. |
| Today | It caught and later cleared Stulack, Funderburke and Cobb; Manav or Alyssa replied to each. During a gateway outage (~12:53-1:28pm CT, reported to `0.0.0_AB_MSTR~DELL1`, since cleared) the scan was skipped and caught up afterwards. |

## 3. The six scanners

| Scanner | Watches | Build | Replay proof | Live |
|---|---|---|---|---|
| Inbox Radar | advisor or partner requests with no Opal reply, or not executed; SLA 4 business hours | BUILT | fired on 20 of 21 YTD dropped-request failures; flagged 3 of 4 measured cases earlier (median 5.8 days) | stopgap only (2b); OFF in the container |
| Sleeping Money Alarm (deck tile: "Static Cash Alarm") | a new account untraded for 5 business days; idle cash for 5 trading days | BUILT | Victor ...0650 fires 9/29 (funded 9/22) | LIVE in the container |
| Fee Tripwire | fee on a never-traded account; cash negative 2+ days after a fee | BUILT | Victor fee 10/13; Tracey ...6385 | LIVE in the container |
| Payday Guard | recurring withdrawal not covered 2 business days ahead | BUILT | 0 short last cycle; the 11/2 preview showed 40 of 105 short (informational) | LIVE in the container |
| Rule Change Relay | custodian or Opal rule changes against accounts in flight | DESIGNED | the manual scan found the Schwab $10M / 9/15 cutoff not communicated | not built |
| Report Proofer | numbers checked before they reach advisors or partners | DESIGNED | -- | not built (last) |

Approved settings (addendum 6):
- Sleeping Money: 5 business days for a new account, 5 trading days for idle cash.
- Stale items expire after 10 quiet business days; a dismiss needs a reason.
- Owners: Inbox Radar = Manav; Sleeping Money / Payday Guard / Fee Tripwire = Menachem; Rule Change Relay = Yang.
- Digest: daily at 8am CT to a Teams channel (renderer built; it cannot send; the channel is not named).

## 4. Access and infrastructure checklist

| Item | State | Detail |
|---|---|---|
| Project code and registry rows | DONE | TCKT_EARLYWARN @b6f505b393; 6 Schwab silver reader rows @ec8ff2668d |
| Graph app registration | DONE | `opal-client-ops-early-warning`, client `3d9262d1-36a0-476b-b176-cf8e0fa427ed`, tenant Opal Capital |
| Certificate credential | DONE | key in Secrets Manager `opal/ews/graph-app-cert` (thumbprint 4EC53E1D...C5B8); the public `.cer` was given to Andrew for upload |
| Admin consent for Mail.Read (application) | **PENDING: Global Admin** | Andrew holds Cloud Application Administrator, which cannot consent. The note for AJ is ready. |
| Mailbox group + ApplicationAccessPolicy | **PENDING: Exchange Admin** | Members approved: Andrew, Manav, Menachem, Yang, Alyssa, Jeanette, Jim. Proof is Test-ApplicationAccessPolicy (member Granted, non-member Denied). |
| Gateway `/hx/mail` bearer + 5-domain table (the container's bridge mode) | **ROUTED, status unconfirmed** | Sent to `1.0.0_SA_CTO~DELL1` for the NFRA_OPLGTW release owner on 10/17; no confirmation seen. Domains: 49financial.com, inflectionwealth.com, cottonwoodmail.com, alongsideria.com, opalinvest.com. |
| Real account numbers for Opal staff in gateway tools | **ROUTED** | Andrew: "Yes they should show real acct numbers" (addendum 3); a gateway change in the NFRA_OPLGTW lane |
| Daily digest | BUILT, NOT SENDING | the channel is still to be named by Andrew |
| TV screen | LATER | after streaming; TV hardware not identified |

## 5. Current findings

**Inbox Radar (stopgap), as of 2:54pm CT:**

| Item | Firm / sender | State | Note |
|---|---|---|---|
| Portfolio Insight | 49 / F. Lyles | OVERDUE (since noon CT) | Encrypted message, unreadable by the scan. One-time passcodes were requested at 10:15, 10:16 and 1:24pm CT. No Opal reply visible. |
| Client Questions \| 49 Financial | 49 / L. Day | OPEN | A client opening a managed brokerage account asks how stocks are chosen, plus more. OVERDUE Tue 8:38am CT. |

**Schwab danger list** (from the 10/17 full scan of 7,675 49 Financial accounts; dated, not re-run since):
- RED:
  - Victor ...0650: untraded; fee took cash negative.
  - Tracey ...6385: -$758.79.
  - Weber ...3350: -$808.15.
  - Firm-wide: the Schwab $10M / 9/15 cutoff not communicated.
- AMBER:
  - Allen IRA ...4581.
  - Pettis LP ...2137 (with the family accounts, about $1.58M uninvested).
  - Grubbs Trust ...2597.
  - Whalen IRA ...3029.
  - Strain ...1955, Shank ...9757, Dean ...0486.
  - Chiles ...5115: SMA 145, offer unanswered.
  - Nishizaki ...4282: 259/133 leverage.
  - Griffin ...7070: temporary sleeve 9+ months at 1.0%.
  - Five November withdrawals short.
  - 16 accounts (about $24.6M) holding an unidentified $1.00-unit line.
- Full detail: `Client Ops Early Warning - Scanner Status 2026-10-17.pdf` on the dell1 Desktop.

## 6. The 10/19 design: the client-ops store and user access

`docs/briefs/tckt-earlywarn-clientops-store-design-20261019.md` @715f261f39 (Andrew addendum 7).
- **Shape:** the harvest pattern, end to end. Scanners write tiered findings: raw, then an event log, then history and snapshots, then
  served JSON. `clientops_*` gateway tools read the served tier. The MCPINDEX catalog lists them. The dashboard and the TV read the
  same objects.
- **Scans:** EventBridge Scheduler at 09:00 and 16:00 America/New_York. The 5 s mail stream logs in between.
- **Tools (proposed):** `clientops_list_warnings`, `clientops_get_warning`, `clientops_get_history`, `clientops_get_summary`,
  `clientops_describe_rules`. Findings only; Opal staff; each user's firm grant enforced by the tools.
- **Tenancy (Andrew decides):**
  - **Shape A (recommended):** `opal-data-clientops` holds the system only. Each firm's findings stay in its own bucket. The live store
    already does this for 49 Financial.
  - **Shape B:** one shared bucket split by firm prefix. It needs an R20 deviation Andrew signs.
- The builders do not know "clientops" yet; the missing registry rows are named in the brief.

## 7. Open with Andrew

1. Tenancy: Shape A or Shape B.
2. Whether scans also run on weekends and holidays ("every day"; Schwab files arrive on trading days only).
3. The Teams channel for the 8am digest.
4. Forward the consent note to AJ (Global Admin): consent, then the mailbox group, then the access policy and its two test results.
5. Deck tile naming: "Static Cash Alarm" (on the deck) vs "Sleeping Money Alarm" (in the code).

## 8. Key artifacts

| What | Where |
|---|---|
| Andrew decisions (addenda 1-7) | `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md` |
| Streaming design | `docs/briefs/client-ops-early-warning-design-20261016.md` @0cfd2572f3 |
| Store and access design | `docs/briefs/tckt-earlywarn-clientops-store-design-20261019.md` @715f261f39 |
| Code merges | Day 1 @02562d59cc; Day 2 @004c4df6a9; approved settings @b21f7bb5a7; registry @ec8ff2668d |
| Deploy orders | `org/missions/D7/TCKT/TCKT_EARLYWARN/task-orders/` (TO-EWS-d1, TO-EWS-d2, both complete) |
| Deploy manifest | `org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/EWS_DEPLOY.json` |
| Postmortem evidence | 49-row YTD ledger and the 48-card Word docs (INTERNAL and ANON) on the dell1 Desktop |
| Decks and status | `Client Ops Early Warning v2.pptx`; `Client Ops Early Warning - Scanner Status 2026-10-17.pdf` (dell1 Desktop) |
