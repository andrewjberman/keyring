# CVO graphOps audit (/molecule + /seams) — comp-kuzu / Nessie freshness + mechanics — 2026-06-18 ~19:20Z

**archetype:** VALIDATE
**Trigger:** Andrew-direct — the comp-which/comp-tool HUD hook is now MANDATORY (routes the whole fabric TO the graph). So kuzu/Nessie must be immaculate or the fabric gets routed to bad data with false confidence. Throw everything at graphOps; confirm NOT stale + good working order.

**Method:** dogfooded comp-kuzu + ground-truthed every load-bearing claim against LIVE state (S3 warehouse, the writer-stamped marker, the SQS queue, live AWS resource counts) + read the oracle code (kuzu_cli/_canonical/_provenance/derive_runner/incremental_updater). Hunted the day's classes: stale-reading-as-current, claimed-mechanism-not-firing, fresh-but-wrong.

## VERDICT: kuzu/Nessie are in GOOD WORKING ORDER (immaculate on the read-side hook surface). 1 finding (G-1, = F-1 extension), bounded.

## /molecule — the canonical graph unit (kuzu_nessie_db)
- WHAT: the ONE canonical comp-kuzu default surface (kuzu_nessie_db), Nessie-sourced, 12500 nodes / 19138 edges. Auto-refreshes on HEAD-advance engine-internally (Rule-20 query-default preserved).
- LIVE STATE: GENUINELY CURRENT. Built 13:13Z (age 6.1h < 26h threshold). pin nodes=3470176063981055398 / edges=6900025178615117521 == the writer-stamped marker (derive_runner, committed 13:06Z) == the LATEST warehouse metadata (00000-1cb8732c, 13:06Z; NO metadata advance since). The 13:06Z vintage = today's P4 re-derive. SQS 2b queue = 0 pending (readable).
- CONTENT ACCURACY (fresh != correct; verified BOTH): graph cloud-node counts MATCH live AWS EXACTLY — LAMBDA 161=161, DYNAMODB_TABLE 33=33, EVENT_RULE 98=98. FLOWS_TO=961 (P1 claim) + SERVED_FROM=29 (P4 claim) confirmed. Node/edge distribution healthy (frontend-TS: Field/JSX/Render/Prop/Type + cloud: IAM/LAMBDA/LOG_GROUP/EVENT/SECRET/DDB).
- LINEAGE: derive_runner (2a nightly cron(0 2 UTC) + manual re-derive) + incremental_updater (2b SQS-driven) -> Nessie (in-VPC) + warehouse S3 -> writer-stamped marker -> comp-kuzu pin/refresh -> consumers (comp-trace/blast/iam + the mandatory hook).

## /seams — graphOps mechanics, 3-axis
1. FRESHNESS ORACLE (read-side, _provenance._nessie_head_status + format_provenance_header): MECHANICAL PASS. The oracle reads the writer-stamped S3 marker (warehouse/_branch_head.main.json), compares pin vs marker.graph_nodes.snapshot_id. FAIL-SAFE is CORRECT: absent/unreachable marker -> "unknown" (loud UNKNOWN VINTAGE), NOT a silent "current" (the mtime-scan was RETIRED for exactly this reason, dc06744c6). DECLARATIVE PASS: "current (pin == marker HEAD)" is TRUE here (pin == marker == latest metadata). SEMANTIC PASS: the header surfaces current/BEHIND/UNKNOWN + a PENDING line for in-flight 2b on EVERY query.
2. MARKER WRITE-SIDE (the HEAD oracle's source of truth): PASS. BOTH writers stamp it — derive_runner.py:386 (2a) AND incremental_updater:561 (2b, "after a successful Nessie commit, only-advance-if-newer" = monotonic). So the marker faithfully tracks HEAD across both paths. (Residual: the 2b stamp is best-effort; see G-1.)
3. AUTO-REFRESH (_canonical.ensure_fresh): code-verified SOUND (not live-exercised — DB is current). On BEHIND/UNKNOWN/stale-age: rebuild under mkdir-mutex + build-to-temp + atomic os.replace SWAP + orphan-lock-steal (15min) + fail-safe-serves-existing-labeled-stale. Read-only shared-lock query open (concurrent readers coexist; the 1-of-8 storm-reader bug is fixed). CTO-certed 8dda8c663.
4. CONTENT ACCURACY: PASS (counts match live AWS exactly, above).

## FINDING G-1 (P1, = F-1 extension; AE-lane, already routed)
The graph's PROACTIVE freeze-backstop publishes to the F-1 BROKEN-egress topic: incremental_updater SNS_TOPIC_ARN = aws_sns_topic.critical_surface_alerts (opal-critical-surface-alerts) for the marker-advance/staleness signal, AND the globgrph-s3-requests-daily-{high,warning} CloudWatch alarms action = the same topic. That topic = F-1: email sub PendingConfirmation (dead) + SMS sandboxed + Delivered=1/Failed=1/3d. So the "never a silent freeze" guarantee's HUMAN-NOTIFICATION leg is broken — a graph freeze during a quiet period (no comp-kuzu queries) would NOT proactively alert a human.
- BOUNDED (why it's not a hook-blocker): the comp-kuzu READ-side oracle self-protects — every query surfaces BEHIND/UNKNOWN in the header independent of SNS. So the MANDATORY-HOOK SURFACE is SAFE; only the proactive-alert-during-a-quiet-window leg is broken.
- FIX: same as F-1 (confirm the email sub OR SES-migrate the topic). Already routed AE-via-COO. G-1 ADDS URGENCY: the graph is now mandatory-hook-load-bearing, so its freeze-backstop egress matters more.

## RESIDUALS (notes, not defects)
- 2b marker-stamp is best-effort (commit doesn't fail if stamp fails) -> a rare stamp-failure would stale the marker until the next comp-kuzu query surfaces it (read-side catches it). Backstop = the marker-staleness alarm, which has the G-1 broken egress. Low-probability (S3 put right after a successful S3 commit) + read-side-bounded.
- Auto-refresh not live-exercised this audit (DB current). Code-robust.

## Bottom line for Andrew
SAFE to slam the mandatory comp-which/comp-tool hook. The read-side oracle (what the hook routes agents to) is SOUND, fail-safe (UNKNOWN not silent-current), genuinely current, and content-accurate vs live AWS. The marker is faithful across both write paths. The ONE gap is the proactive freeze-ALARM egress (= F-1, already being fixed) — which the read-side oracle self-protects against anyway.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-kuzu | provenance header (freshness oracle) + node/edge distribution + FLOWS_TO/SERVED_FROM + LAMBDA/DDB/EVENT counts | current; counts match live AWS exactly |
| comp-which | route graph-health question | pointed to comp-pipescript-deployed (deploy-freshness, not graph-freshness) -- the graph-freshness oracle IS comp-kuzu's own provenance header (correct surface) |
| aws s3api/s3/sqs/cloudwatch/lambda/dynamodb/events | marker content+freshness, warehouse metadata advance, SQS pending, alarm SNS actions, live resource counts | marker faithful; no metadata advance since 13:06Z; G-1 (alarm egress = F-1 topic) |
| Read (kuzu_cli/_canonical/_provenance/manifest/derive_runner/incremental_updater) | oracle + marker + auto-refresh + write-path code | fail-safe sound; both writers stamp marker; auto-refresh robust |

**What worked:** the writer-stamped marker (read-side) is the right design — fail-safe to UNKNOWN, not silent-current; ground-truthing pin-vs-marker-vs-live-metadata confirmed genuine currency; counts-vs-live confirmed accuracy. Verify-my-own-assumption caught a wrong-bucket 404 (opal-globgrph vs the manifest's opal-313476888478-globgrph) before I false-flagged "marker missing." **Gap:** G-1 (proactive freeze-alarm egress = F-1 broken topic). **Net:** graph immaculate on the hook surface; 1 bounded egress finding.

— 3.0.0_SA_CVO
