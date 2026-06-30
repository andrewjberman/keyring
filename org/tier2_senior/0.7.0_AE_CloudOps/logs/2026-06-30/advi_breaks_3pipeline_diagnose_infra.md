# ADVI_BREAKS P0 — AE infra diagnose across inf/49F/cot (TO-1/3/4) + thread-2 + TO-2/6 design

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE
**serial:** 0.7.0_AE_CloudOps
**window:** session start ~12:57Z -> 13:48Z (2026-06-30)

## Summary

AE infra half of ADVI_BREAKS P0 (CTO PRD d2cae58f9, COO decomp 66aadb975). Drove the
READ-ONLY infra forensic across all three broken pipelines + closed a refuted upstream
thread + locked the TO-2/TO-6 prevention design. All fixes coordination/GO-gated (none
applied). 3 RAVCs ACCEPTED (inf by COO+CTO; cot by base; 49F finding by CTO).

## inf TO-1 (ACCEPTED COO 132313Z + CTO 132351Z) — 3 answers + 1 gap

- **Trigger map:** `opal-data-inf/platinum/firm/header_metrics.json` has ONE daily
  producer-sequence on the inf-gold-layer-runner (EC2 **i-0ed5afded2ebd4ed4**) via
  `orion-gold-dispatch.sh`: INF_D_00 (132B stub, first) then INF_D_04 (28830B rich, last-wins).
  Triggered by inf-gold-trigger Lambda (primary=silver-aggregator event ~13:01Z; fallback=
  `inf_canonical_prices_daily` cron 14:00Z ENABLED). inf-portal-publisher (S3-notif on
  `gold/meta/...pipeline-complete.json`) does NOT write this key (red herring).
- **Off-cadence 06-29 eve (21:29/21:40/22:07Z, 3x 132B stub):** = 3 INF_D_00-only manual runs.
  CloudTrail mgmt events in-window show NO inf-gold StartInstances/SendCommand/StartSession;
  ~A confirms no committed `--single/--from INF_D_00` path. Only key-touching events =
  user/Andrew_Berman boto3 GetObject 1s after each write (IP 108.242.96.89) during his
  canonical/SSOT bootstrap (he RunInstances'd 3 canonical-schwab-runners 20:17-20:32Z). Verdict
  = manual Andrew-local INF_D_00 --upload single-stage. PutObject principal UNVERIFIABLE-by-log
  (see gap).
- **No 06-30 refresh = FALSE ALARM:** 06-30 full chain running normally — `dispatch-lock.json`
  run=lock-full-9785593f2535 started 13:01:44Z, 5400s lock. On 06-29 the same mode=full wrote
  D_00 14:29:42Z + D_04 14:34:06Z (~88min). 06-30 writes due ~14:30Z; verify queued (poller
  b3ji49dup watching the served key).
- **GAP (TO-6):** org trail S3 data-event selector = ReadWriteType=**ReadOnly** on
  opal-data-inf + opal-data-bd AND S3 server access logging OFF -> served-key WRITES
  unattributable (why the 06-29 PutObject is only inferable). Routed to 0.8.0~B / TO-6.

## 49F TO-3 (gate-critical, ACCEPTED CTO 134010Z) — gold D_03 failure, NOT clobber/as_of-pin

- Served `opal-data-bd/platinum/firm/header_metrics.json` FROZEN since 06-26T05:00:19Z (zero
  writes 06-27..06-30). bd-gold-trigger fires 2x/day through 06-30 + still StartInstances the
  runner (i-01003b035d2988dfb) daily -> trigger/runner HEALTHY.
- **Root (log-grounded, chain_full_* logs):** `D_03.composition_artifacts.py` fails
  "Firm composition returned empty -- check holdings_lots content" (rc=1) on EVERY run since
  06-26 23:00Z -> breaks gold->platinum header promotion (platinum_header_refs=0 on all failing
  runs). Last healthy run = 06-26 04:00 (D_03 ok, header promoted 05:00); FIRST FAILING =
  06-26 23:00. SHARP onset 06-26 23:00 (not gradual from 06-19 MFA death) -> CTO elevated
  change-event C (canonical-SSOT bootstrap) from refuted-as-clobber to IMPLICATED TRIGGER.
  Concrete support for the DATA_SSOTMG HOLD. DS~B owns the WHY (RPS zero-close).

## cot TO-4 (ACCEPTED base 133820Z) — BD $0-price data-quality, guard working

- cot-exporter (i-0643a5bee8a8feabf) bronze-run 06-29+06-30 (Success): "auth OK
  firm=cottonwood" both nights (login healthy); "REJECT: holdings @2026-06-29 non-zero-MV 0.0%
  < 50% floor" -> completeness guard correctly gates BD's $0-priced holdings -> data_as_of pins
  06-26. 06-30 sweep re-landed 06-23..06-26 (84-85% nzf), 06-29 still $0. Sidecars all
  landed_at=06-30T02:04Z -> BD T+N pricing lag. unrealized = 0 `<row>` elements (the 06-22
  DATEMODE template-break). F-axis GREEN (session->bronze->silver->gold all Success).

## 49F thread-2 (REFUTED, COO stand-down 134356Z corroborated)

- B_01 join (`schwab_to_bd` map from `gold/dimensions/schwab_bd_account_mapping.parquet`):
  xref schwab_account_id = clean 10-digit (0% z-prefix); bd_account_id = z-prefixed 100%
  (BY DESIGN, value-side). RPS account_id = clean 10-digit. **93.3% match (85280/91421)** ->
  join does NOT collapse on keying. z-prefix hypothesis dead. Side-obs: latest RPS partition
  date=20260623 written 06-25T18:13Z = schwab_rps frozen (separate Schwab-CRS freshness issue).

## TO-2/TO-6 prevention design (CTO-ruled, apply-gated)

- TO-2: 3 PER-FIRM firm-scoped guard Lambdas (CTO 134230Z, NEVER#1-clean — no cross-firm
  write), S3-ObjectCreated -> reject/quarantine shape-regressing writes, no-op on pass
  (loop-safe). Layered with 0.8.0~B item2d freeze-monitor (hourly detect, which now carries my
  STOPPED-WRITER detection-3 reconcile). Open design point RAVC'd CTO 134823Z: configurable
  grace-window vs drop-emit-first sequencing.
- TO-6: dedicated write-trail scoped to platinum/firm/ on inf+bd+cot (CTO 134230Z, not the org
  trail — blast-radius isolated, in my globgrph lane). org trail confirmed in globgrph/item2b.tf.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which | route trigger-forensic + bd-header-producer questions | PARTIAL (manifest backstop, ran the call myself) |
| pipescript --resource / advi-bd | header_metrics producers + the full bd gold trigger/runner map | PASS (found bd-gold-trigger/runner + platinum writers) |
| comp-iam service canonical-schwab-runner | close COO's lead: can the SSOT runner write opal-data-inf? | PASS (NO inf access -> definitively ruled out as the inf writer) |
| comp-grep | B_01 RPS<->BD join logic (account_id/schwab_to_bd) | PASS |
| comp-pipescript io | attempted (no-arg usage) | N/A (used pipescript instead) |

**What worked:** comp-iam cleanly refuted COO's canonical-schwab-runner-as-inf-writer lead
(IAM has no opal-data-inf grant). pipescript mapped the bd gold trigger->runner->platinum chain
in one call. **What failed:** comp-which routed both infra-trigger questions to the manifest
backstop (no rich tool for EventBridge/SSM/CloudTrail trigger forensics). **Gap found:** no
comp-tool covers CloudTrail/EventBridge/SSM trigger-and-dispatch forensics (the core of this TO)
— had to use raw aws cloudtrail/ssm/ec2 (rail-checked where gated). Candidate: a `comp-trigger`
that maps a served key -> its producer's full dispatch chain (Lambda/EventBridge/SSM/EC2-runner)
+ recent fire history.

## Current State

- All 3 pipelines DIAGNOSED from AE infra side; RAVCs accepted. No commits, no deploys, no
  applies (all read-only forensic + MCP coordination). ~24 MCP messages handled.
- inf 06-30 self-heal verify PENDING ~14:30Z — background poller b3ji49dup watching
  `opal-data-inf/platinum/firm/header_metrics.json` for the 06-30 write; exits on landing or
  ~69min timeout.
- TO-2 (per-firm guards) + TO-6 (dedicated write-trail) design locked by CTO; build pending
  CTO concurrence on the grace-window/sequencing (RAVC 134823Z) + COO+CTO apply GO. Both
  HALT-gated.

## Next Steps

- **[0.7.0_AE_CloudOps]** verify inf self-heal when poller fires (~14:30Z): rich 06-30 D_04
  lands last (~$202.13M Orion) + DLQ inf-gold-trigger-dlq empty + pipeline-complete fresh ->
  RAVC COO+CTO GREEN-on-F. Then build TO-2/TO-6 TF on CTO concurrence + GO.
- **[1.0.0_SA_CTO]** concur on TO-2 configurable-grace + drop-emit sequencing (RAVC 134823Z);
  rule TO-6 trail home (confirmed dedicated).
- **[0.4.0_DS~B]** source-confirm 49F WHY (holdings_lots/D_03 input diff 06-26-04:00-good vs
  23:00-empty + what the 06-26 canonical job touched) — the trigger source-confirm.
- **[0.4.0_DS~A]** inf TO-2 DS-lane: drop the INF_D_00 header emit (sequences with my guard).
