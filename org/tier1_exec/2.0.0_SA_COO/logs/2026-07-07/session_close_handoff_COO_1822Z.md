# COO Session-Close Handoff -- 2026-07-07T18:22Z (Huntress memory-leak escalating, reboot anticipated)

**Trigger:** Rio.exe (Huntress EDR) memory leak MSTR flagged mid-session (~34MB/min) is worsening; Andrew has signaled another device reboot is coming. This is a recurring pattern today -- at least 2 prior Huntress-triggered reboots already happened (see `session_close_handoff_COO_1238Z.md` and the WIND-DOWN handoffs referenced in git log before this session started). Writing exact-restart state now so the next COO session picks up cold with zero re-derivation.

**This is a checkpoint, not a wind-down.** Nothing below is "parked" by choice -- every open item has a live owner or an explicit external gate. On restart: re-run `/watcher` -> `org/XXX.md` startup -> `/drive` per the standing COO protocol, then read this file top-to-bottom before doing anything else.

---

## Fabric snapshot at checkpoint (8 live agents)

| Serial | State |
|---|---|
| `0.0.0_AB_MSTR` | LIVE. CMTQUE dormant (confirmed, not yet switched on fabric-wide), Rio.exe leak actively tracked, awaiting COO's CPU quiet-window signal for TO-6R load-test. |
| `0.1.0_DE_MarketIntelligence` | LIVE, idle/event-driven. MKOV_RETFIX TO-1 fully shipped+PROD-verified. Awaiting Andrew's next portal DEV batch. |
| `0.4.0_DS_ClientPlatform` | LIVE. Mid-flight on ADVI_COTETL.AUAFIX-L6 (see below) -- the session's highest-priority open item. |
| `0.7.0_AE_CloudOps` | LIVE. Queue: bd-client-detail P3 follow-up (needs DS coordination), DS~B graph-edge follow-up pending reply, `globgrph-stitch-produce` L4 blocked on `PORTAL_REPO_PAT` (Andrew-only, see below). |
| `0.7.0_AE_CloudOps~B` | LIVE, idle. Just closed SCTY_PREMCP secrets-rotation-runbook (RAVC sent, needs COO commit on restart -- see Immediate Actions). |
| `1.0.0_SA_CTO` | LIVE. Working pending queue; mid-research on the MDPF_COTMDL follow-on when last checked. |
| `2.0.0_SA_COO` (this session) | 15 `/drive` cycles run this session, cron armed at 20m cadence (`org/mcp/.last-drive-2.0.0_SA_COO` marker current as of cycle 15, ~18:08Z). |
| `3.0.0_SA_CVO` | LIVE, event-driven standing. Owns 2 pending verification asks (ETFS_AVGCAP diff, AUAFIX-L6 served-verify re-cert) -- see below. |

Whole `0.4.0_DS_ClientPlatform` family (base+~A+~B) died mid-session to a Huntress/SIGTERM-correlated event and was respawned by MSTR ~17:48Z -- base is back live; ~A has NOT been confirmed live since (see NFRA_MOTIF below).

---

## IMMEDIATE ACTION on restart (uncommitted working-tree file)

`org/tier1_exec/2.0.0_SA_COO/task_orders/SCTY_PREMCP.secrets-rotation-runbook.md` has a closure draft from `0.7.0_AE_CloudOps~B` sitting **uncommitted** in the working tree (ANY_EXEC lane -- AE can't commit under `org/tier1_exec/2.0.0_SA_COO/`). Status=complete, evidence cites `docs/runbooks/m365-gateway-secrets-rotation.md` commit `465a9ba7f`. **Commit this file first thing** via `safe-commit.sh` under the COO author line -- it's reviewed-and-ready, just needs landing.

---

## The one genuinely urgent open thread: ADVI_COTETL.AUAFIX-L6

A live ~$3M understatement in served Cottonwood AUA, found this session (a 2026-06-23 batch reconcile-close had falsely marked it DONE; source-grounded re-verification proved the fix never landed).

- **Part (a) LANDED+DEPLOYED** 18:18Z -- AP/dormant exclusion gate removed cot-wide (commit `fa7792b70`, deployed+verified against live S3). DS also proactively swept the whole cot gold tree and found+fixed a **3rd instance** of the same bug (inline in `C_06.client_mix_timeseries.py`) that the original reopen note missed.
- **Served-verify PENDING** -- next natural cot gold chain run, **02:00 UTC nightly** (no ad-hoc run per CLAUDE.md). Corrected AUA ~$365.7M expected vs ~$362.6M currently served. **If the next COO session starts after ~02:30 UTC, check whether this has landed and RAVC CTO+CVO with the confirmed served figure.** If before, it's still pending -- don't chase it early.
- **Parts (b)/(c) IN PROGRESS**, not urgent. DS found a real new risk before touching cube-build logic: a naive `<$100` dust-floor flip on the BD-zeroed rule could let a stale-cube ghost account leak ~$2.26M INTO AUA as a new overstatement (concrete example: acct `z0812933851`, $0.04 silver vs $2.26M stale cube). DS is grounding a reconciliation-aware fix against live silver/allocations before proposing anything. (c) also carries an Andrew-veto flag on the dust-floor threshold itself.
- CTO + CVO are both looped in and expecting the served-verify RAVC. CVO owns re-certifying (their original 06-22 cert record referenced this item and needs the correction on record).

**Full detail + evidence:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_COTETL.AUAFIX-L6.ds-exclusion-rule-snapshot-zeroed-only.md`.

**Related, same batch audited (no further action needed):** L2/L3 had the same stale-paperwork status field but real underlying work -- both corrected to `complete` this session. Confirmed isolated to L6, not a systemic reconcile-close reliability gap (CTO concurred).

---

## Other open threads, by urgency

### Awaiting a peer response (event-driven, no COO action needed unless it stalls)
- **ETFS_AVGCAP vs MDPF_ASSETS WS-D.2 methodology overlap**: real overlap confirmed this session (two different per-partner ETF-ownership computations for the same 4 ETFs/3 partners). CTO's lean is "ETFS_AVGCAP supersedes WS-D.2" but wants an empirical diff first (49F figure, same date, both methods) before ruling. **Dispatched to CVO ~18:02Z, response not yet received as of this checkpoint.** If it lands mid-session-gap, CVO reports directly to CTO for same-day ruling -- check for that thread on restart.

### Staged, deliberately not dispatched (owner-focus judgment call, confirmed correct by CTO)
- **MDPF_COTMDL.TO-1** (verify Portfolio Strategy field populated for Cottonwood, new PRD this session) -- assigned to `0.4.0_DS_ClientPlatform`, same lane as AUAFIX-L6. Staged behind it on purpose. GO once L6 lands or DS signals spare bandwidth. TO: `org/tier1_exec/2.0.0_SA_COO/task_orders/MDPF_COTMDL.TO-1.verify-portfolio-strategy-populated.md`.

### Real findings from the /prd-delta dashboard sweep, awaiting Andrew's steer (asked, not yet answered as of checkpoint)
- **`NFRA_MOTIF`**: its stated gates (CSE-P1, FEDOBS-P1) are BOTH already cleared -- the real remaining blocker is TSGRAPH's P2-2 (cluster-materialize) re-home, conceptually assigned to MOTIF weeks ago but never actually dispatched as its own TO. Owner `0.4.0_DS_ClientPlatform~A` has not been confirmed live since the family outage (base was respawned, ~A was not separately verified). **Asked Andrew whether to author+dispatch the P2-2 TO now (queued behind that lane's other work) or route to a different lane (e.g. `0.8.0_AE_CloudComp`, doing the COMPILERKIT counterpart).** No answer yet.
- **`ADVI_INFFEE`**: billing audit (TO-1) finished 5 days ago, overturned the original premise (missing price data, not truly-unbilled accounts). Registry says "GO issued" for TO-2/TO-3 but **no TO has actually been filed for either** -- reads like a real stall. Same owner family (`0.4.0_DS~A`). **Asked Andrew whether to move on this now.** No answer yet.

### Purely external -- nothing for COO to do
- **`PORTAL_REPO_PAT`** GitHub secret missing -- blocks `globgrph-stitch-produce` L4, has been PAST-WINDOW all session (RED-suppressed, re-alerts every 4h, currently 6.6h age). Andrew-only.
- **`NFRA_WEBSITE`**: Andrew's 5 open decisions (hosting approach, email provider, Cloudflare-proxy-status, CloudFront timing, DNS record shape). Zero technical blocker, just needs his call whenever.
- **`ADHC_PREFLT`**: correctly sequenced behind `ADVI_INFREF`'s cutover settling -- checked, INFREF genuinely hasn't reached its "safe to retire old pipeline" checkpoint yet (real data bugs still being found+fixed as of 07-06). Not stale, still a live wait.
- **`NFRA_PROMOTE`**: correctly last-in-sequence by design, gated on FEDOBS's measurement layer + MOTIF's candidates, neither of which exist yet. Working as intended.
- **SCHWABAUTO Gate-2**: Andrew's ToS/fraud-risk call on browser-session token extraction. CTO already escalated, still pending.
- **Standing-access-class Directive**: gates `NFRA_COMPTEAM.B2-ACTIVATE` + `NFRA_AGENTBUS.AB-ACTIVATE`. Still pending.
- **`NFRA_CMTQUE.TO-6R` load-test**: gated on a CPU quiet-window (<60% sustained + Rio.exe handle-count flat/dropping) that has NOT materialized all session -- CPU has bounced 65-94% the whole time, and the Huntress leak Andrew's now flagging as worsening makes this LESS likely to clear soon, not more. MSTR is holding correctly; don't force it.

---

## Session wins (context for the next session, not action items)

- **MKOV_RETFIX** fully shipped: TO-1 promoted to PROD (`portal-v2.1.132`, commit `f3ce600c`, CI SUCCESS, all 7 acceptance criteria independently verified down to the exact deployed bundle content). TO-2 closed-to-access-gate (mechanism isolated, Bloomberg-terminal pull flagged to Andrew, follow-on PRD `MKOV_TRSRCE` already spun out + narrowed to v1.1).
- **`partner-etl-ops-alerts` P1** (alarm paging nobody) fully closed -- CVO delivery-verified in Andrew's actual mailbox.
- **`bd-client-detail`** dead route fully decommissioned (Lambda+route+doc, live-verified gone).
- **`ses-sender-lint`** built + landed as a BLOCK-mode commit-gate check (CLAUDE.md Rule 23) -- found+fixed 4 real live violators (copy-pasted `EMAIL_FROM` defaults across all 4 trade-pipeline Lambdas) during discovery, not just theoretical prevention.
- **`comp-grep` reliability finding** resolved -- a regex-dialect footgun (`\|` BRE-vs-Python-re), not a real indexing bug. Fixed with a loud warning (commit `bb9d7e803`); Rule 21's trust premise holds.
- **`/prd-delta` dashboard cleanup**: 14 stale registry `phase`/`status` fields corrected across the fabric with cited evidence (all understating real progress -- `MKOV_RETFIX`, `NFRA_CMTQUE`, `NFRA_COMPILERKIT`, `ADVI_BREAKS`, `SCTY`, and 9 others). The false-closure audit on the AUAFIX batch (above) came out of this same sweep.
- **`MDPF_COTMDL`** PRD landed (Cottonwood Model Portfolios, Cohort 3) -- mostly a wiring job per CTO's own scoping (existing cohort architecture + BD REST access both already live), TO-1 staged and ready.

---

## Drive/allocation loop state

- `/drive` cron armed, 20m cadence, still active (survives reboot only if re-armed post-restart -- **confirm `CronList` on restart and re-arm if it dropped**).
- `org/mcp/.last-drive-2.0.0_SA_COO` marker is current as of cycle 15 close (~18:08Z) -- the next cycle's movement-check window starts from there.
- 15 drive logs + 15 allocation briefs written this session, all committed, all in `org/tier1_exec/2.0.0_SA_COO/{drive_log_*,briefs/allocation_*}`.

---

## Restart checklist (do these in order)

1. `/watcher` (self-heal inbox).
2. `org/XXX.md` startup protocol.
3. Commit the uncommitted `SCTY_PREMCP.secrets-rotation-runbook.md` closure (see Immediate Action above).
4. `CronList` -- confirm `/drive` cron survived; re-arm if not.
5. `/drive` -- will naturally pick up: AUAFIX-L6 served-verify status check (if past 02:00 UTC), any CVO response on the ETFS_AVGCAP diff, any Andrew response on the NFRA_MOTIF/ADVI_INFFEE asks.
6. Check `python .tools/fabric-check.py --blocks` fresh -- 8 agents were live at checkpoint; confirm which survived the reboot vs need MSTR respawn (expect most/all to need respawn -- a device reboot kills everything, unlike the DS-family-only outage earlier this session).
