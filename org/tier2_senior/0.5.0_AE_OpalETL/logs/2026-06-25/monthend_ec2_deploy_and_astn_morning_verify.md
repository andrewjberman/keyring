# Session Log -- 0.5.0_AE_OpalETL -- month-end ETFS report EC2 (deploy+verify) + ASTN morning-digest verify + comp-schedule note

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Date:** 2026-06-25 | **Window:** ~22:05Z -> 23:55Z (since heatmap_o1_converge_and_monthend_ec2_start)

## Summary

Built, deployed, and VERIFIED end-to-end the month-end ETFS report cloud-run (transient EC2 +
orchestrator Lambda + EventBridge 1st@10ET + SES email). The e2e test caught 3 latent bugs BEFORE the
07-01 first-fire. Ground-corrected COO's ungrounded structural-catch premise + made it true. Then
(Andrew-direct, live) verified the ASTN_WSJFT CEO digest will go out this morning to austin@, and filed
a comp-schedule tool request to CTO.

## 1. Month-end ETFS report cloud-run -- DEPLOYED + VERIFIED (ledger etfs-reports-monthend CLOSED)

New TF root infra/aws/terraform/etfs-reports/ (backend etfs-reports/tfstate). Resources (16 added, then
2 in-place updates): transient EC2 etfs-reports-reporter (i-070477bf35fc54409, t3.medium AL2023+SSM+
IMDSv2+chromium, astn clone) + orchestrator Lambda etfs-reports-orchestrator (start->SSM render_month_end
--month last --pdf->verify->SES-email->always-stop) + EventBridge Scheduler etfs-reports-monthly-run
cron(0 10 1 * ? *) America/New_York + etfs-reports-monthly-absence-check cron(0 14 1 * ? *) + SNS
etfs-reports-alerts. FIRM-CLEAN: reads opal-data-etfs only, writes platinum/reports/* only, zero firm
bucket. First scheduled fire 2026-07-01 10:00 ET (renders 2026-06). DE owns render_month_end.py; I own
the infra. 0.7.0 registered the EC2_MANIFEST entry (their lane; owned-paths correctly blocked me).

E2E TEST (4 invokes, --month last = 2026-05): final run rendered etf_ownership.pdf (189054B) + .html to
s3://opal-data-etfs/platinum/reports/2026-05/; SSM Success rc=0; orchestrator Lambda 0 errors; box
self-stopped each run (cost-guard finally-stop works); SES identities verified (austin@/andrew@/opalinvest.dev).

3 LATENT BUGS the e2e caught pre-fire (the value of verify-not-trust on REAL artifacts, not a dry-run):
1. Stray daily/inflection/holdings_2026-06-24.json (my old fan-in artifact) crashed render_month_end
   (no date-key guard) -- was IN-RANGE for the real June fire. Fix: Andrew-confirmed S3 delete + DE
   date-key guard (ba57d9b12).
2. associate_public_ip_address drift forced an instance REPLACE on every post-stop plan (would destroy
   the EBS chromium cache + break the instance-scoped IAM ARN + manifest). Fix: lifecycle ignore_changes (04400d0a2).
3. Full Chrome-for-Testing HANGS under --print-to-pdf on AL2023 (zygote/GCM, rc=124 timeout -> HTML-only).
   On-box probe proved chrome-headless-shell renders cleanly in <1s. Fix: symlink headless-shell to
   /usr/local/bin/chromium (c3a5e3701; probe.sh committed as the diagnostic asset).

Plus a STRUCTURAL-CATCH fix (a43dc2238): COO's RAVC asserted the absence-guard publishes to
opal-critical-surface-alerts (the channel they poll every /drive) -- FALSE as-built (my _alert went only
to etfs-reports-alerts). Grounded + RESOLVED: _alert now dual-publishes to BOTH the local topic (Andrew
email) AND opal-critical-surface-alerts (+ sns:Publish grant + CRITICAL_SNS_TOPIC env), so a 07-01
failure/no-show is caught structurally. COO owned the miss + credited the catch.

## 2. ASTN_WSJFT CEO digest -- morning go-out verified (Andrew-direct, live)

Andrew-direct: ensure the ASTN WSJ/FT digest goes out this morning to austin@opalinvest.com. Verified
(NOT my lane -- astn-pipeline/CTO -- but Andrew-directed; read-only verify, no changes made):
- EventBridge: astn-wsjft-3am-run + astn-wsjft-4am-absence-check both ENABLED (aws scheduler get-schedule;
  comp-which found NO eventbridge comp-tool -> raw aws is the tool, rail-confirmed). Fires 3:00 ET ~07-26.
- Deployed recipient (s3 artifact code/scripts/config.py, the code the 3am run pulls): SES_TO=
  austin@opalinvest.com (single), SES_FROM=digest@opalinvest.dev. EXACTLY Andrew's ask. NOTE drift:
  LOCAL source is newer (austin@+andrew@ multi + morningbrief@ sender) but NOT deployed -> this morning
  sends austin-only per deployed.
- SES gate: account sandbox (ProdAccess=false) BUT austin@opalinvest.com = verified + opalinvest.dev =
  verified -> deliverable. Full chain clear; 4am absence-guard catches a no-show.

## 3. comp-schedule tool request -> CTO (Andrew-direct)

Filed to 1.0.0_SA_CTO (235422Z): build comp-schedule to check ALL scheduled automation (EventBridge
schedules/rules, crons, Airtable automations) -- name/state/expression/target/next-fire. Motivating gap:
comp-which had no eventbridge checker today (routed to comp-platinum backstop) -> raw-aws fallback = the
exact Rule-21 coverage-gap signal.

## Deployment Sequence + Verification (AE)

- etfs-reports: build (TF root) -> commit ed506fbd3 -> init -> plan 16-add -> safe-apply HALTGT -> 16 added
  -> 0-diff. ledger 20260625T2224Z opened 4 legs, CLOSED all 4.
- fixes: f6f0f07b9 (chromium discoverable) -> 04400d0a2 (ignore_changes, killed the REPLACE drift) ->
  c3a5e3701 (headless-shell, probe-proven) -> a43dc2238 (dual-publish critical-surface). Each: gate ->
  commit -> plan (0-add/N-change) -> safe-apply -> 0-diff -> push.
- verify: 4th orchestrator {mode:run} -> PDF 189KB in S3 + 0 Lambda errors (paste above).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-which | "where is astn EC2 infra" / "check eventbridge enabled" | ROUTED/backstop -- no eventbridge tool exists (-> CTO comp-schedule request) |
| comp-iam (implicit, design) | etfs-reports firm-sep | PASS (read etfs only, write reports only, zero firm bucket) |
| ds-commit-gate | orchestrator Lambda (x3 edits) | PASS each |
| safe-commit surface-check | all etfs-reports commits | PASS (no critical surface) |
| safe-apply (HALTGT) | etfs-reports apply x4 | PASS (16-add then in-place) |
| terraform | plan/apply + 0-diff verify | PASS |

**What worked:** testing the REAL render against REAL artifacts (not a dry-run) surfaced all 3 latent
bugs the 07-01 fire would have eaten. Grounding the deployed-vs-source config (verify-against-served) on
ASTN caught the drift -- the DEPLOYED austin-only is what ships, not the newer local. Grounding COO's
wiring premise (Rule 22 up-chain) caught a non-existent structural catch.
**What failed:** my first two chromium fixes were partial (discoverable-but-full-chrome-hangs) -- the
on-box probe (not a guess) gave the deterministic headless-shell answer.
**Gap found:** no comp-schedule tool for eventbridge/cron/airtable state (-> CTO request).

## Current State

- etfs-reports month-end report cloud-run LIVE + verified + ledger CLOSED. First fire 2026-07-01 10:00 ET.
  Failure/no-show dual-alerts to andrew@ email + opal-critical-surface-alerts (COO /drive poll).
- ASTN_WSJFT digest armed for this-morning 3am ET -> austin@opalinvest.com (deployed config + SES verified).
- comp-schedule requested to CTO.

## Next Steps

- **[Andrew]** (DEFERRED per Andrew "deal with it later") confirm the May test-email RECEIPT + final report
  inbox (wired andrew@opalinvest.com; send-no-throw to verified != delivered).
- **[1.0.0_SA_CTO]** build comp-schedule (Andrew-direct backlog).
- **[0.4.0_DE]** optional _to_pdf hardening (prefer headless-shell + broaden globs + subprocess timeout) --
  DE logged as a follow-on; will ping me to re-verify on-box sans-symlink.
- **[Andrew/0.7.0]** SES presentation-push recipient list -> activate (DROP-EVERYTHING priority on arrival).
