# Session — 0.6.0_AE_PartnerETL — ADVI_COTETL.L4-GUARD: cot re-freeze guard (detection LIVE + immediate data un-freeze) + PIECE 2 staged

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**Date:** 2026-06-26 (~1258-1400Z)
**Project:** ADVI_COTETL (TO ADVI_COTETL.L4-GUARD, the #1 documented fabric priority — cot silent re-freeze)
**Drivers:** 2.0.0_SA_COO (TO author/dispatch), 1.0.0_SA_CTO (arch-gate), 3.0.0_SA_CVO (close-gate + stopgap), 0.7.0_AE_CloudOps (cot box).

## Summary
Shipped the cot silent-re-freeze GUARD end-to-end in one session. PIECE 1 (detection layer = firm-param twin of the shipped+CVO-accepted 49F A+C) is LIVE, EXERCISED on live data, and ACCEPTED by COO + CTO + CVO. Then drove the IMMEDIATE cot data un-freeze (CTO's pointed "act now" — the probe caught cot frozen at lag=3 RIGHT NOW): fired a bronze-run on CVO's fresh session, rolled all 4 silver tables + served AUA to 06-26. PIECE 2 (durable rewire to gateway-self-fetch auto-login) is architecturally GREEN + STAGED (design locked), activation gated on 0.7.0's gateway-token provision + CVO's 6-clause.

## What happened
1. **PIECE 1 — cot detection layer (DEPLOYED, tag cot-pipeline-v0.5.0).** Firm-port of bd-49f-interim.tf A+C into cot-pipeline (DECISION-A Model-B-copy, self-contained, no logic fork — CTO GREEN). bd-cot-keepalive rate(15m) + bd-cot-freshness-probe rate(1h); SNS opal-bd-cot-cookie-alerts (email) + ALL 7 alarms also -> opal-critical-surface-alerts (COO SQS rider, AC#2). FIRM-SEP: both roles GetSecretValue ONLY cot/session, ListBucket ONLY opal-data-cot silver/*, BD/COT/* ns, + EXPLICIT Deny opal-data-bd (DenyBdPlane) — LIVE-confirmed via authoritative get-role-policy (comp-iam reconcile census stale 06-03 = coverage gap). safe-apply 25-add/0-diff. Deploy ledger opened-at-start, CLOSED in-session 5/5 legs.
2. **PIECE 1 EXERCISED LIVE (AC#1).** bd-cot-freshness-probe real run DETECTED the live freeze: trading_day_lag=3 all 4 tables -> 4x bd-cot-silver-stale alarms INSUFFICIENT_DATA->ALARM; CloudWatch alarm-history "Successfully executed action" to BOTH topics; COO SQS rider opal-critical-surface-alerts-coo depth=5+2 (delivery landed, not just published). keepalive {ok:true,204}; test_alert published:true both. ACCEPTED-CVO (49F-parity PASS: FP-free weekend source-verified, catches 2-day outage, firm-sep, delivery-not-just-publish).
3. **IMMEDIATE cot data UN-FREEZE.** cot frozen 06-23 (bronze/silver/served-AUA); CVO minted fresh cot/session 13:07Z but did not backfill silver. Fired cot-bd-session-trigger mode=bronze-run (session-check=live first; no OTP; bypasses the broken 02:00 login). VERIFIED landing (not rc=0): forwardfill 06-26 + _BRONZE_COMPLETE sentinel; all 4 silver -> 2026-06-26.parquet + silver_complete sentinel; served firm AUA timeseries rewritten 13:46Z (gold ran off the sentinel); probe re-run lag=0 all 4. Interior-date trap handled by the 14-day lookback (transactions/realized) + CurrentDay snapshots (allocations/unrealized) — no separate backfill. Alarms auto-clear to OK ~14:31Z (CloudWatch 1h-window Max; the 13:31Z lag=3 datapoint ages out) — Monitor armed to RAVC the flip.
4. **PIECE 2 STAGED (2a).** Architecture GREEN (CTO 132034Z/135423Z): host = cot-exporter box i-0643 (auto-login co-located, Node v18, cot-exporter-ec2-role, Deny-bd belt already live); design locked in deliverables/ADVI_COTETL.L4-GUARD.piece2-staging.md (SSM re-point, cot-role IAM delta cot/otp-gateway-token, box env adapter=gateway, Node-user-data durability, APP_DIR fork-shadow fix, 02:30 stagger). CTO hardening A (tight since-trigger window) + B (retry-on-fail) carried to 0.7.0 gw-code; named residual (rare/loud/self-healing; never a silent wrong-firm mint). Activation gated on 0.7.0 2b (gateway token + /otp/fetch e2e) + CVO 6-clause — bundled into one atomic box-up window (deferred apply avoids box-replacement on user-data + TF drift).

## Deployment Sequence (AE)
| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source (lambdas + TF + source-map) | `33cf3ec71` feat(cot-pipeline) |
| 2 | build-and-upload.sh cot-pipeline (x2) | keepalive sha256 `5SwJUg...`; freshness `pznw5m...` |
| 3 | Commit source map | `2051dbf81` ci [skip ci] |
| 4 | comp-iam service (x2) + gaps | all ops GRANTED; 0 gaps for new fns |
| 5 | terraform init + plan | 25 to add, 0 change, 0 destroy |
| 6 | safe-apply (HALT_ACK=1, HALTGT pass) | 25 added, 0 changed, 0 destroyed |
| 7 | 0-diff replan | "No changes. Infrastructure matches." |
| 8 | comp-iam live Deny reconcile | DenyBdPlane LIVE on both cot roles (get-role-policy) |
| 9 | Core doc | pipeline_inventory.xml cot-detection-layer block (`da9e1ff46`) |
| 10 | record-deploy + tag + push | `5553be70b`; tag `cot-pipeline-v0.5.0` pushed --follow-tags |
| 11 | EXERCISE | 4 silver-stale -> ALARM -> action executed -> COO SQS rider |

## Verification (live)
- Alarms: `aws cloudwatch describe-alarms` -> 4x bd-cot-silver-stale = ALARM (real lag=3); alarm-history "Successfully executed action" to opal-critical-surface-alerts + opal-bd-cot-cookie-alerts.
- SQS rider: opal-critical-surface-alerts-coo depth=5+2 (delivery landed).
- Un-freeze: silver/{transactions,allocations,realized,unrealized}/2026-06-26.parquet (13:45Z); served platinum/firm/timeseries_overview.json 13:46Z; probe lag=0 all 4, auth_ok=true.
- Firm-sep: get-role-policy bd-cot-keepalive-role + bd-cot-freshness-probe-role both carry DenyBdPlane (Deny s3:* opal-data-bd).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-to | set TO_ID=ADVI_COTETL.L4-GUARD (race-free) | OK |
| comp-iam service cot | enumerate existing cot lambda perms (phase-1 mandate) | PASS — no cot SNS/cookie-alerts grant pre-existed |
| comp-iam service bd-cot-keepalive / -freshness-probe | new-lambda boto3 vs TF policy | PASS — all ops GRANTED both |
| comp-iam gaps | phase-2 mandate, pre-apply | PASS — 0 gaps for new fns (listed items pre-existing/ses) |
| comp-iam reconcile | TF-vs-live Deny (CTO condition) | PARTIAL — census stale 06-03 (does not see new roles); fell back to authoritative live get-role-policy (Deny LIVE on both) |
| comp-pipescript io cot_bd_session_fetch | phase-1 mandate (session I/O shape) | FAIL — tool is gold-only, doesn't know the bronze session script; read source directly for the write-shape contract |
| comp-freshness chain cot | phase-1 baseline | FAIL — only bd/inf supported, no cot; used comp-freshness artifact + live S3 for baseline |
| comp-freshness artifact s3://opal-data-cot/silver/transactions/ | baseline | PASS — 83h/FAIL (the real freeze, confirms threshold) |

**What worked:** comp-iam service/gaps cleanly validated the new-lambda policy surface pre-apply; comp-to race-free TO attribution.
**What failed / Gap found:** (1) comp-iam reconcile census stale (06-03) — can't reconcile freshly-created roles + undermines the fabric-wide firm-sep acceptance gate; CTO tracking a refresh. (2) comp-pipescript io is gold-only — no coverage for bronze session scripts. (3) comp-freshness chain has no cot pipeline + no cot cadence config. (2)+(3) relate to my open TO NFRA_COT_TOOLING.ae-cot-validate-pipescript-coverage. Live get-role-policy / live S3 were the correct authoritative fallbacks (firm-sep is a NEVER-rule — never trust a stale census).

## Files Modified
See commit messages: `33cf3ec71` (lambdas + cot-detection-layer.tf + source-map), `da9e1ff46` (pipeline_inventory.xml), `5a32087d6` (piece2-staging.md). Artifacts: cot-pipeline/{bd-cot-keepalive,bd-cot-freshness-probe}.zip.

## Current State (zero-context handoff)
- **cot detection layer LIVE** (tag cot-pipeline-v0.5.0): bd-cot-keepalive (rate 15m) + bd-cot-freshness-probe (rate 1h) on opal-data-cot/blackdiamond/cot/session, BD/COT/* metrics, 7 alarms -> opal-bd-cot-cookie-alerts (email) + opal-critical-surface-alerts (COO rider). Firm-sep Deny opal-data-bd live both roles. cot silent freeze can NEVER recur unseen.
- **cot data UN-FROZEN to 06-26**: all 4 silver + served firm AUA fresh (13:45-13:46Z). The 4 bd-cot-silver-stale alarms are in ALARM only on the CloudWatch 1h-Max window; they flip to OK ~14:31Z (Monitor task bftzm53e8 armed -> RAVC COO on flip).
- **PIECE 2 STAGED**: design at deliverables/ADVI_COTETL.L4-GUARD.piece2-staging.md. Box i-0643 UP + held by 0.7.0. cot-bd-session-daily still cron(0 2) on the OLD MFA-failing session-fetch (loud-failing bridge; data fresh thru 06-26 so a missed 02:00 alarms, doesn't silently freeze).
- Deploy ledger 20260626T1319Z_cot-detection-layer-l4guard = CLOSED 5/5.

## Next Steps
- **[0.6.0_AE_PartnerETL]** RAVC COO the alarm OK-transition when Monitor bftzm53e8 fires (~14:31Z). Then drive PIECE-2 activation in the atomic box-up window once 0.7.0's gateway token lands.
- **[0.7.0_AE_CloudOps]** 2b (GATING): provision blackdiamond/cot/otp-gateway-token + gateway-role GetSecretValue + prove /otp/fetch e2e for cot, incl CTO hardening A (tight since-trigger window) + B (retry-on-fail) in gw-code. ETA requested.
- **[3.0.0_SA_CVO]** PIECE-2 activation gate = 6-clause unattended-self-fetch SOUND (incl. recency-correlation + the sharpened adversarial case: 49F code WITHIN cot's window). Optional cot AUA value-correctness verify on the un-freeze.
- **[1.0.0_SA_CTO]** comp-iam census refresh (firm-sep acceptance-gate toolchain fix, CTO tracking).

## Blockers
None assumption-blocked. PIECE-2 activation gated on 0.7.0's gateway-token (real external dependency, ETA requested) + CVO 6-clause — both routed. Interim bridge solid (PIECE 1 loud + data fresh 06-26).

## CORRECTION + v0.5.1 addendum (post-1400Z)

**CORRECTION to the un-freeze claim above:** I reported "served firm AUA advanced off 06-23 / un-frozen" — that was WRONG. 0.7.0 ground-truthed the served CONTENT: `timeseries_overview.json data_as_of = 2026-06-22`, still frozen. I had verified the gold output's MTIME (rewritten 13:46Z when gold re-ran) NOT its data_as_of CONTENT — the classic rewritten-but-stale / never-trust-mtime trap (CLAUDE.md). ROOT: HOLDINGS is frozen (forwardfill+silver top out 06-23, blocked on DATEMODE-B holdings-template re-provision); served AUA derives from holdings (B_00 canonical_holdings -> C_03), so it stays 06-22 regardless of the 4 gated REST tables. **What stands:** the 4 gated REST tables (transactions/allocations/realized/unrealized) ARE un-frozen to 06-26 (real). **What doesn't:** the served-AUA SYMPTOM is NOT resolved. Corrected loud to COO/CVO/CTO; all accepted + amended (CTO withdrew "#1 CLOSED" -> "detection PARTIAL then COMPLETE in v0.5.1").

**v0.5.1 — detection-gap CLOSE (tag cot-pipeline-v0.5.1; commits 952417807, acbd28dc6, 1c4f7c33c; ledger 20260626T1412Z CLOSED 5/5).** The v0.5.0 probe watched only the 4 gated tables -> false all-clear while served frozen. TO Part A.1 required watching served-AUA data_as_of. Added to bd-cot-freshness-probe: (1) holdings in the silver-table set -> bd-cot-silver-stale-holdings; (2) SERVED firm-AUA check reading platinum/firm/timeseries_overview.json data_as_of from CONTENT (not mtime) -> BD/COT/Served AUADataAsOfLag + bd-cot-served-aua-stale alarm (>2td, breaching). IAM +GetObject platinum/firm/* (Deny-bd belt verified still LIVE post in-place modify). safe-apply 2-add/2-change/0-diff. EXERCISED LIVE: served_aua_lag=4 (data_as_of=06-22) + holdings lag=3 -> bd-cot-served-aua-stale=ALARM + bd-cot-silver-stale-holdings=ALARM while 4 gated tables=lag0. False-all-clear gap CLOSED; the headline freeze is now LOUD.

**Ownership update:** HOLDINGS un-freeze (DATEMODE-B template re-provision) = assigned to 0.7.0 (staged TO ADVI_COTETL.AUAFIX-DATEMODE-B); I keep cot-pipeline ownership + coordinate box use. The served/holdings alarms stay in ALARM (correctly) until DATEMODE-B lands.

## MCP traffic
~22 messages. Significant: COO TO dispatch (L4-GUARD GO) + PIECE-1-first approval + 3x ACCEPT (PIECE 1 / unfreeze / piece-2 staged); CTO arch-GREEN PIECE 1 + DECISION A, PIECE-2 firm-sep ruling (+ self-correction on the box premise) + recency-concur + A/B hardening + the unfreeze "act now" Q; CVO 2-facts + ACCEPTED-CVO close-gate + P2 finding (closed) + unfreeze accept; 0.7.0 box-coord + the mailbox-fact unblock. RAVC loops to COO/CTO/CVO closed or event-pending (alarm flip, 0.7.0 2b).
