# Session Close -- cot durable auto-login: t3.small->t3.large, RESEEDED + freeze CLOSED; 49F tonight-reseed solved autonomously; device-trust root-caused with SCREENSHOT evidence; singular-process directive propagated

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-25 | **Window:** ~20:54Z -> 23:56Z (since the prior log b69a5faf6)

## TL;DR
Drove BOTH firms' BD durable auto-login to LIVE reseeds via the single firm-parameterized script: 49F tonight-reseed SOLVED autonomously (no manual paste), Cottonwood's INVISIBLE 2-day MFA-freeze DISCOVERED + CLOSED. Cot needed an Andrew-direct t3.small->t3.large bump (the Kimi vision loop raced the 10-min OTP expiry + SSM timeout on 2 vCPU). Device-trust root-caused with SCREENSHOT evidence (Andrew-direct "evidence not speculation"). Propagated Andrew's singular-process-flow directive fabric-wide. Accepted CTO's durable-swap Option-A (capability bearer). Certed ETFS_CANON Dynamo lane. Health-checked the graph SQS/Kuzu (all green). Banked the evidence-not-speculation lesson.

## Work done (this window)

### BD durable auto-login -- BOTH firms reseeded LIVE
- **49F tonight-reseed SOLVED AUTONOMOUSLY** (the day's P-item): the proven relay loop (login->MFA->I-grab-OTP-via-gateway->enter->cookie) wrote a fresh .bd.identity to blackdiamond/49f/session @21:13:25Z. MINT-VERIFIED HTTP 200 bearer=True. NO Andrew manual paste -- "resolve don't attest" to its conclusion (classified the 19:51Z creds-write, then drove the auto-login to completion). COO-closed.
- **COTTONWOOD freeze CLOSED** (silent-since-06-23, no alarm -- worse than 49F): same single script, BD_FIRM_ID=cot derives blackdiamond/cot/*. Reseeded @22:53Z + 23:31Z, MINT-VERIFIED HTTP 200. The 06-23 freeze is un-stuck.
  - **t3.small was the blocker (GROUNDED):** 2 cot runs on t3.small (i-0643a5bee8a8feabf) -- the Kimi-VL loop is CPU-bound; node ran >9min, raced the 10-min OTP expiry AND the 540s SSM timeout -> node KILLED pre-cookie-capture. NOT a script bug (trace truncated at step3 post-code by the timeout). Andrew-direct fix: bump to t3.large -> the complete-fix ran to completion: step5 LOGGED_IN, cookie written, the otpEntered guard fired ("OTP already entered -> awaiting .bd.identity") = the re-read hang fixed.
- **The complete-fix arc (0.6.0, my redirects):** capture-by-cookie-presence + otpEntered guard (kills the re-read hang) + Andrew-direct "CONTINUE signing in" (Continue+Remember-My-Device+land THEN capture, for appearances + device-trust). Kimi classify refined (LOGGED_IN incl. the loading dashboard).

### Device-trust -- ROOT-CAUSED WITH EVIDENCE (Andrew-direct: evidence, not speculation)
- Ran the cot diagnostic with BD_DEBUG_SHOTS=1 + BD_DEBUG_FORM=1. EVIDENCE (3-part):
  1. Read-back log: "device-trust: Remember-My-Device via=dom checked=FALSE" -> the DOM click did NOT toggle the box.
  2. SCREENSHOT (s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/debug/2026-06-25T23-27-26-585Z/step3_MFA_OTP.png, pulled + viewed): the "Remember My Device" checkbox is visibly UNCHECKED.
  3. Post-login cookie-names dump: ["__cf_bm",".AspNetCore.Antiforgery...","idsrv.session","idsrv",".bd.identity","receptivePingSent","receptiveNotificationCount"] -> NO device/trust cookie at all.
- ROOT: the checkbox is an UNLABELED <input type=checkbox> (no id/name; "Remember My Device" is a detached sibling LABEL) -> the bare selector isn't toggling it. Fix shipped (0.6.0 28c929c52: label-click / force-check / vision-locate + verify checked=true). VERIFY queued for the next run (Andrew: fold in, no dedicated login).
- Screenshot pipeline now WORKS end-to-end (BD_DEBUG_SHOTS -> S3 -> Read renders PNGs) = visual evidence for any future BD-login question.

### Singular-process directive (Andrew-direct) -- propagated fabric-wide
"Singular process flow ... don't duplicate work or make alt versions." Broadcast to CTO/COO/0.5.0/0.7.0/0.6.0: ONE self-contained script (Playwright->Kimi CV->OTP via GraphAPI MCP gateway->enter->cookie), ONE owner (0.6.0), firm-PARAMETERIZED (BD_FIRM_ID) NOT forked for 49F+cot, ONE OTP mechanism (inline gateway read; app-reg DEAD, relay=bridge). 0.6.0 confirmed the script already implements it (157a6fbb0: BD_FIRM_ID + hard firm-sep guard).

### Durable-swap -- CTO ruled Option A, I accepted (tighter than my B-advocacy)
CTO ruled the box->gateway OTP read = Option A (a STATIC CAPABILITY BEARER scoped to ONLY /otp/fetch, NOT a box-held Andrew-identity token). Corrected my B-advocacy: B-now reaches the full Graph surface (AS only issues aud=/mcp today); A is isolated by construction + zero human-touch. My 2 cert conditions MET tighter (box reads ONLY blackdiamond/49f/otp-gateway-token; /otp/health liveness probe, COO-owned). Folded into the new PREMCP project (PREMCP_PRD.md s4, 53699876b). 0.7.0 building A.

### Other lanes
- **ETFS_CANON Dynamo cert PASS** (independent): etfs-canon-fanin-role firm-sep clean (only opal-data-etfs/daily/* read + the etfs_ownership_daily table write, ZERO firm-bucket); NO partner-tenant route resolves the table (comp-grep'd all 28 refs -> writer + DE's internal monthly reader only); internal-only. Closed.
- **Graph SQS/Kuzu health check** (Andrew-direct, heavy-traffic day): opal-globgrph-incremental-events = 0 backlog, DLQ = 0; updater Lambda 12h = 68 inv / 0 err / 0 throttle; comp-kuzu = current (pin==marker HEAD), rebuilt 0.1h ago. ALL GREEN. (comp-graph-status local-cache "STALE" = the tool's 300s TTL scratch caches, NOT the canonical graph.)

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-iam service etfs-canon-fanin-role | ETFS_CANON firm-sep cert | PASS | only etfs prefixes, zero firm-bucket |
| comp-iam service bd-49f-auto-login-role | re-cert post BrightData-drop | PASS | proxy grant removed, debug PutObject scoped |
| comp-kuzu / comp-graph status | graph health (heavy-traffic check) | PASS | kuzu current, SQS 0-backlog/0-DLQ |
| comp-grep "etfs[_-]ownership[_-]daily" | find table readers (no-route check) | PASS | writer + internal monthly reader only |
| comp-which | route ASTN-method + SQS/kuzu | PARTIAL | backstop-routed, ran the primitive |

**What worked:** comp-iam gave the firm-sep certs cleanly; comp-kuzu's marker-oracle header = the authoritative graph-freshness signal. **Gap/none:** the bulk was LIVE operational validation (boto3 SM/SSM completing-runs, m365-gateway OTP reads, mint-checks, EC2 describe/resize-coordination) -- off-rail by design (no comp-tool drives a live BD login + OTP-grab + mint). Several rail-checked Bash markers logged for the SQS/Lambda-metric/EC2 ops.

## Blockers
None. cot t3.small slowness RESOLVED (t3.large, Andrew-direct). Device-trust = a known non-urgent gap (root-caused, fix shipped, verify queued -- cot works without it via the OTP-grab). All else event-driven.

## Current State (handoff)
- **BD durable auto-login: ONE firm-parameterized script** infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js (BD_FIRM_ID selects firm -> blackdiamond/<firm>/{credentials,session,otp-relay}; hard firm-sep guard). 0.6.0 latest 28c929c52. Boxes: 49F i-0fa1846f04ed7e337 (t3.medium), cot i-0643a5bee8a8feabf (t3.LARGE -- bumped; 0.7.0 to STOP it overnight, start-on-demand).
- **Both cookies LIVE + mint-verified @23:50Z:** blackdiamond/49f/session (21:13Z, cap ~6h -> ~03:13 death, PAST the 02:00 runner +alarmed), blackdiamond/cot/session (23:31Z, fresh). Overnight COVERED -- no manual reseed obligation. Relays (49f+cot otp-relay) CLEARED (ROE).
- **OTP mechanism:** TODAY = relay bridge (CVO grabs OTP from Andrew@opalinvest.com via the m365 gateway -> put-secret-value -> box polls). CONFIRMED multi-firm (cot OTP same mailbox/sender noreply@bdreporting.com, subject "Authentication Code You Requested", regex Authorization code:\s*(\d{6})). GOING-FORWARD = Option-A capability-bearer gateway /otp/fetch (0.7.0 building) = fully unattended, no CVO-in-loop.
- **Device-trust:** root-caused (unlabeled checkbox not toggling -> no device cookie); fix shipped 28c929c52; VERIFY queued (next run, BD_DEBUG_SHOTS=1, fold-in no dedicated login). Evidence at debug/2026-06-25T23-27-26-585Z/.
- **Memory banked:** feedback_evidence_not_speculation_flaky_egress_not_failure.md (don't infer target-failure from a hung agent-side check; ground in secret-state/trace/mint).

## Next Steps
- **[0.7.0_AE_CloudOps]** STOP the cot box i-0643a5bee8a8feabf overnight; BUILD durable-swap Option-A (/otp/fetch capability-bearer endpoint + the gateway-token); the /otp/health liveness probe (COO-owned).
- **[0.6.0_AE_PartnerETL]** verify the device-trust checkbox fix on the next cot run (BD_DEBUG_SHOTS=1 -> checked=true + does BD set a device cookie); BUILD cot's detection layer (cot-keepalive/freshness/opal-bd-cot-cookie-alerts SNS -- the invisible-failure gap).
- **[3.0.0_SA_CVO self]** verify the durable-swap end-to-end + cert (capability-scope + liveness probe) when 0.7.0 lands it; verify device-trust with screenshots; verify cot detection layer firm-separated; the ETFS inf-overstatement fix + tie-out gate on 0.5.0's inf-repoint rerun.
- **[0.5.0_AE_OpalETL]** inf ETFS repoint rerun -> signal CVO for the overstatement verify + tie-out cert.

## MCP traffic
~50 messages this window (heavy BD coordination). Significant: dispatched the cot unfreeze + the t3.large bump (Andrew-direct); broadcast the singular-process directive (CTO/COO/0.5.0/0.7.0/0.6.0); accepted CTO Option-A; multiple device-trust fix redirects (cookie-presence -> complete-sign-in -> checkbox-evidence) to 0.6.0; RAVC'd COO cot-reseed-CONFIRMED (mint 200); answered CTO's wind-down sweep (clean, overnight covered).
