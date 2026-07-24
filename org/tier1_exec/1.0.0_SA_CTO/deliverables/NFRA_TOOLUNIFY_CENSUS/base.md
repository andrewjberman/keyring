# NFRA_TOOLUNIFY Estate Census — LANE base — Iceberg/Nessie globgraph CORE

**lane:** section2.base, `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md`
**agent:** `0.8.0_AE_CloudComp` (base serial — not a `~` lane)
**vintage:** all measurements below taken 2026-07-24 ~2130Z-2245Z, live/source, denominator stated per item
**sidecar:** `base.sidecar.json` (full tabular detail — schemas, exact columns, all quoted sources); this document is the narrative + grounding trail
**discipline held:** read-only throughout (no apply/deploy/re-point/regenerate); reported to `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` only per the plan's isolation clause; no main-fabric contact this pass

---

## Mission recap

Completely characterize the versioned-truth substrate: every Iceberg table in the Nessie/Iceberg globgraph lakehouse + the derive pipeline that maintains it. Must-close: full table inventory (producer/trigger/cadence/failure-watcher), the 46-ref Nessie topology, the `incremental_updater` Lambda, and the MECHANISM (not just the date) behind the two frozen artifacts — `graph_contracts` (06-16) and `stitch_graph.json` (07-07).

**Boundary held:** I own the Iceberg/Nessie truth substrate + its producers. I did not map tool-consumption (lane `~D`'s boundary) or live-AWS/graph count parity (lane `~A`'s boundary), except where understanding a producer required reading code that also happens to touch those areas.

---

## 1. The Iceberg table inventory — corrected from the plan's first-pass list

**Denominator + method:** full `ListObjectsV2` over `warehouse/` (171,309 keys, one AWS-CLI-v2 auto-paginated call, no truncation observed), grouped by path segment, Iceberg-table status confirmed by presence of a `metadata/*.metadata.json` file (the structural signature no amount of Glue registration can substitute for).

**Finding that corrects the plan's section1 table:** what CTO~Z's first pass called "Iceberg obs/ontology layers" (`code_heat`, `ms_heat`, `tool_activity`, `axes_history`, `snap_ingest`, `cse_ingest`, plus the `fedobs_*` family) is **not one uniform class**. Direct inspection shows:

- **10 distinct table names / 11 physical directories are true Iceberg tables** (have a `metadata/` folder under `warehouse/globgrph/<name>_<uuid>/`): `graph_nodes`, `graph_edges`, `graph_contracts`, `resource_summaries`, `code_heat_snap`, `cse`, `cse_test` (**anomaly:** two separate physical UUID-directories both named `cse_test` — see §6), `fedobs_coevolution_snap`, `fedobs_coverage_snap`, `ms_heat_snap`.
- **9 sibling top-level prefixes are plain, non-Iceberg object stores** living beside the Iceberg core in the same bucket: `code_heat/`, `tool_activity/`, `fedobs_obs_findings/`, `fedobs_signals/`, `axes_history/`, `cse_ingest/`, `cse_ingest_staging/`, `ms_heat/`, `snap_ingest/`. Three of these (`code_heat`, `tool_activity`, `fedobs_obs_findings`→registered as `obs_findings`) are additionally Glue-Data-Catalog-registered as plain external Parquet tables (Athena-queryable) — Glue registration is **not** evidence of Iceberg-ness; none carry a `table_type=ICEBERG` parameter, which the true Iceberg tables (managed entirely through the Nessie REST catalog) never register in Glue at all.

Full per-table schema (columns + types), partition specs, exact S3 key counts, and producer/trigger/cadence/failure-watcher detail: see `base.sidecar.json` → `iceberg_tables[]` and `plain_object_stores_not_iceberg[]`. Highlights:

| Table | Cols | Last write | Producer | Cadence | Failure-watcher |
|---|---|---|---|---|---|
| `graph_nodes` | 9 | 2026-07-24T15:04:11Z | `derive_runner.py` (nightly full) + `incremental_updater` Lambda (event-driven) | 02:00 UTC daily + continuous | SNS on commit-failure — **see §7, delivery in question** |
| `graph_edges` | 6 | 2026-07-24T02:08:58Z | `derive_runner.py` only (nightly full) | 02:00 UTC daily | same SNS chain |
| `graph_contracts` | 13 | 2026-06-16T18:53:51Z | one-time manual governance load (TO-2b) | none — by design | N/A, see §5 |
| `resource_summaries` | 11 | 2026-07-18T21:11:05Z | `resource_summaries_store.py`, manual `ecs run-task` | none found — ad-hoc | none (no schedule to watch) |
| `code_heat_snap` | 12 | 2026-07-16T15:28:06Z | `snap_store.py` ← `code_heat_emit.py` | dev-box/manual cadence | `freshness_alarm` registry — **could not verify live target list** |
| `cse` | 24 | 2026-07-24T03:30:53Z | `cse_store.py`/`cse_emit_*.py` family | 03:30 UTC daily (fresh, on-cadence) | not confirmed |
| `cse_test` ×2 | 24 | 2026-07-08 (both) | test/seed harness | none — not production | N/A |
| `fedobs_coevolution_snap` | 9 | 2026-07-17T17:43:21Z | `snap_store.py` ← `fedobs_observe.py`/`fedobs_emit.py` | 04:30 UTC nominal, timestamp doesn't align — see could-not-verify | `freshness_alarm` registry, unconfirmed |
| `fedobs_coverage_snap` | 8 | 2026-07-16T15:28:07Z | same fedobs family | same | same |
| `ms_heat_snap` | 14 | 2026-07-17T18:11:09Z | `snap_store.py` ← `ms_cloud_extract.py` (rides item2a nightly) | 02:00 UTC nominal, timestamp doesn't align | same (also lane `~C`'s boundary) |

**Technical note carried at the metadata layer:** every table's `metadata.json` lists exactly 1 snapshot. This is **by design**, not a gap — `derive_runner.py`'s own commit code (`_overwrite_with_retry`) documents that every Nessie commit produces a fresh single-snapshot metadata (an explicit CTO ruling, A1, after a prior parent-mismatch detector false-rejected every valid commit). The true version history lives in **Nessie's commit graph** (the 43 daily tags — §2), not in Iceberg snapshot lineage. Anyone reading "snapshots: 1" off a `metadata.json` and inferring "this table has only ever been written once" would be wrong for every table except the two that genuinely have (`graph_contracts`, and effectively `resource_summaries`/`code_heat_snap`/etc. which are lightly-written).

---

## 2. Nessie ref/branch topology — 46 refs, fully enumerated

**Denominator + method:** `aws dynamodb scan --table-name opal-globgrph-nessie-_refs` → 46 items, `ScannedCount == Count == 46`, no `LastEvaluatedKey` — an exhaustive single-page scan (no pagination needed). (Sibling table `opal-globgrph-nessie-_objs` holds 55,787 items / 74.4MB — the Nessie content-object store, not further characterized this pass — object-count, not ref-count, is a different question than the plan asked for here.)

- **1 branch:** `refs/heads/main` — the single mutable branch every producer (nightly full derive + incremental Lambda + all the `_snap`/`cse` producers) commits against.
- **43 tags:** `refs/tags/audit-baseline-YYYY-MM-DD`, one per successful nightly full-derive (`derive_runner.py` Step 3 stamps this on `main`'s HEAD after a successful commit). Range: 2026-06-10 through 2026-07-24. **Gap observed:** 2026-06-13 and 2026-06-14 have no tag (sequence jumps 06-12 → 06-15) — stated as a fact, not investigated further (plausibly pre-stabilization; this pipeline's known P0-recovery window was mid-June per `item2b.tf`'s own comments).
- **2 internal bookkeeping keys:** `:int/repo`, `:int/refs` — Nessie's own storage-internal entries, not user-facing refs.

**Reachability boundary (load-bearing for this whole section):** the Nessie REST catalog itself (`http://nessie.opal-globgrph.local:19120`, ECS-Fargate-hosted, VPC-internal) is **unreachable from this local agent session** — confirmed via a CTO~Z relay of lane `~C`'s (M365) independent finding. Everything above was grounded through the **DynamoDB-backed ref store** (reachable) and **S3 warehouse metadata** (reachable), which the plan's own §1 already anticipated as the fallback proxy. Anything requiring Nessie-native semantics beyond ref *names* (e.g., what a given commit's parent/diff looks like, or resolving the `cse_test` anomaly definitively) is disclosed as could-not-verify, not asserted.

---

## 3. The `incremental_updater` Lambda — full mechanism

`opal-globgrph-incremental-updater`: Python 3.12, 512MB, 180s timeout, in-VPC.

**Trigger chain (event-driven, not scheduled):** CloudTrail mutating-management events → EventBridge rule `opal-globgrph-cloudtrail-mgmt` (a DENYLIST pattern — `readOnly=false` minus log/metric plumbing noise, across 13 graph-relevant service namespaces; CTO's own design note: denylist-the-noise is complete by construction, an allowlist of mutating verbs could not be) → SQS `opal-globgrph-incremental-events` (1hr retention, DLQ after 3 failed receives) → Lambda Event Source Mapping (batch_size=100, **2-minute debounce** window, **max concurrency capped at 2** — a direct scar from a 2026-06-09/10 incident where uncapped concurrency raced Nessie commits into a 298k-message DLQ pileup).

**Reads:** the triggering CloudTrail event's resource ARN(s) → maps to a resource class → runs a **bounded** re-derive (single resource, not account-wide — that's `derive_runner.py`'s job) → also detects and propagates delete events.

**Writes:** `graph_nodes` only, as far as the handler code shows (`_ensure_graph_nodes_table`, `commit_batch` targeting nodes). **I did not find it writing `graph_edges`** — and `graph_edges`' own last-write timestamp (02:08Z, ~8 minutes after the 02:00Z nightly cron, with no later intraday advance the way `graph_nodes` shows) is independently consistent with that. Both producers coordinate through a shared branch-head marker (`warehouse/_branch_head.main.json`) and retry-with-backoff on Nessie's `CommitFailedException` (HTTP 409) when they race the same commit.

**Failure mode — the best-engineered failure handling found anywhere in this census:**
- Per-record isolation (`ReportBatchItemFailures`): one bad CloudTrail event doesn't fail its batch-siblings.
- SQS DLQ after 3 receives — bounded blast radius on poison messages.
- Nessie commit conflicts retried with backoff; on **exhausted** retries, the code explicitly SNS-publishes (`_publish_commit_failure`) to `opal-critical-surface-alerts`.

That publish path is real and well-designed. Whether it currently reaches anyone is a separate question — see §7.

---

## 4. `stitch_graph.json` — ACTIVE, currently-broken pipeline (not a quiet by-design freeze)

CTO~Z relayed CVO~Z's framing mid-census: the freeze is a grain sentinel that *correctly* trips and refuses to publish, plus a hook that exits 0 and notifies nobody — asked me to confirm or refute at source. **Confirmed as the right high-level frame, refined with exact mechanism and current numbers below; one part of the relayed framing ("hook exits 0") turned out to be even more precisely characterizable than "a hook" — it's a whole trigger layer (two of them) whose definition of success doesn't cover the work inside.**

**Architecture:** a 2-leg hybrid. LEG-1 (`​.github/workflows/stitch-source-push.yml`, triggered on push:CLOUD to specific paths, or manual `workflow_dispatch`) zips a repo source subset → uploads `s3://opal-313476888478-globgrph/stitch-source/source.zip`. LEG-2 (EventBridge `opal-stitch-produce-nightly`, `cron(0 3 * * ? *)`, confirmed **ENABLED** live) → CodeBuild project `opal-stitch-produce`, buildspec runs `derive_stitch.py` → writes artifact-first/marker-last on success.

**Why LEG-1 exists at all:** `portal/` is a bare git gitlink (mode 160000) with **no `.gitmodules` entry** — not a registered submodule — so a default checkout leaves it empty. LEG-1's extra checkout step (pinned SHA, private-repo PAT) is the workaround.

**CodeBuild history, fully enumerated (`list-builds-for-project` + `batch-get-builds`, 20 builds = the project's entire lifetime, 2026-07-07 through 2026-07-24):**

**All 20 builds are FAILED. Zero have ever succeeded.** The 3 earliest (07-07, manual triggers, matching the original root-cause investigation session log) and all 17 automated nightly firings since (07-08 through 07-24, each at 03:00:12Z exactly matching the cron) fail identically: `derive_stitch.py ... exit status 2` — the exact code path for a grain-sentinel refusal.

**The frozen S3 object (`stitch/stitch_graph.json`, LastModified 2026-07-08T02:27:52Z) was never produced by this CodeBuild pipeline at all.** Its timestamp *precedes* the first automated nightly build (03:00:12Z that same morning) by 33 minutes, and every automated build since has failed before reaching the upload step. The artifact-then-marker write pattern (3 seconds apart) matches the buildspec's own upload order exactly, so the most likely explanation is a manual local run + upload — not independently confirmed, but the timing makes the CodeBuild pipeline itself impossible as the source.

**Today's (2026-07-24) live grain-sentinel output, pulled from CloudWatch Logs directly (`/aws/codebuild/opal-stitch-produce`, stream `fab8c734-…`):**

```
EXTERNAL_ENDPOINT:      0 vs baseline 3   = 0.00x
REACT_QUERY_KEY:        0 vs baseline 32  = 0.00x
PORTAL_COMPONENT:       0 vs baseline 27  = 0.00x
API_ROUTE:             82 vs baseline 263 = 0.31x
SQS_QUEUE:             12 vs baseline 4   = 3.00x
ECS_TASK_DEFINITION:    7 vs baseline 2   = 3.50x
SCHEDULE:              10 vs baseline 3   = 3.33x
IAM_USER:               4 vs baseline 1   = 4.00x
```

**Two distinct, additive causes, both still live today:**

1. **The original 07-07 defect is UNFIXED in practice.** `REACT_QUERY_KEY`/`PORTAL_COMPONENT` still read exactly 0 — the identical signature to the original root-cause finding. The workflow file **on disk right now already contains the fix** (the explicit second portal checkout, gated on `secrets.PORTAL_REPO_PAT`). But `stitch-source/source.zip`'s own LastModified is **2026-07-07T13:46:19Z — unchanged for 17 days.** `gh run list` shows the workflow has fired repeatedly since (15 times just today, 2026-07-24 alone — plausibly this census's own commits triggering it), **conclusion=failure every time.** The best-grounded inference (not source-confirmed — repo secrets aren't readable even for presence-check without exercising `gh secret list`, which I did not do): the required `PORTAL_REPO_PAT` secret was never actually provisioned, so the fix's own new checkout step fails, and the source zip has stayed on its broken pre-fix content the entire time.
2. **A separate magnitude-drift layer**: `SQS_QUEUE`/`ECS_TASK_DEFINITION`/`SCHEDULE`/`IAM_USER` all trip the *high* side (3.00x–4.00x). Most plausibly genuine estate growth outrunning an uncalibrated baseline, not a data defect — not independently confirmed. **Both causes have to clear for this gate to ever go green**, even once cause 1 is fixed.

**Failure-watcher: none.** `aws cloudwatch describe-alarms` (both a scoped `opal-stitch*` query and a full 51-alarm account-wide sweep) returns **zero alarms** tied to this CodeBuild project. The EventBridge rule's job is only `codebuild:StartBuild` — which succeeds regardless of what happens inside the build. A `FAILED` build status has sat in CodeBuild history, unremarked, for 18 consecutive nights.

---

## 5. `graph_contracts` — FROZEN-BY-DESIGN, fully proven, not a defect (a clean contrast to §4)

This is the cleanest possible case in the whole census: **there is nothing broken here.**

`graph_contracts` is not a continuously-running pipeline output. `contract_engine.py`'s own comment states the table "starts EMPTY (CVO TO-3 authors rows)" — it is an append-only, human-governance-gated table populated **only** through explicit, Andrew-ratified, manual load events. Exactly one such event has ever occurred: **NFRA_GCONTR.TO-2b, 2026-06-16** (`org/critical_paths/change_management/20260616T155426Z_nfra-gcontr-to2b-benchmark-row-load_deploy_completion.md`, CLOSED COMPLETE same day at 16:08Z), loading the Andrew-ratified benchmark-model-portfolios SEV1 contract row from a CVO-authored YAML source (`contracts/graph_contracts.yaml`). That deploy **is** the table's last write, to the second (S3 LastModified 2026-06-16T18:53:51Z; the Iceberg metadata's own `last-updated-ms` independently agrees).

**Why it has stayed frozen since:** the owning project is **Andrew-direct suspended, indefinitely**, as of 2026-07-20 (`org/projects/NFRA_GCONTR.json`, verbatim): *"Pause GCONTR we are not addressing htat, it should be rendered as indefinite/suspended i do not want to fucking hear about it again."* Per that record, do not resurface it — this census states the mechanism as a factual finding only and takes no position on reopening it. (One loose thread I did **not** chase, being out of this lane's substrate-mechanism boundary: the project file also claims "3/5 rows loaded" pre-suspension, but only the single 06-16 deploy-completion ledger entry was found — a project-history-provenance question for COO/CTO, not a producer-mechanism one.)

**§4 vs §5, side by side — the point of grounding the mechanism instead of the date:** both artifacts are "frozen." One (`graph_contracts`) is frozen because it was *designed* to be written rarely, by a human, and that human has since ordered the whole project stood down — there is no defect and nothing to watch. The other (`stitch_graph.json`) is frozen because an *automated, scheduled* pipeline has been silently failing every single night for 18 nights straight, for a diagnosed-but-incompletely-applied reason, with zero alerting anywhere in the chain. A denominator/date alone ("frozen since a date in the past") cannot distinguish these; only reading the producer's own trigger history and exit codes can.

---

## 6. The `cse_test` anomaly (disclosed, not resolved)

Two physically distinct Iceberg table directories both named `cse_test` exist simultaneously (`cse_test_24458e6c…`, 57 keys, last-write 2026-07-08T15:51:17Z; `cse_test_bb57a916…`, 13 keys, last-write 2026-07-08T01:37:22Z), identical 24-column schema. Both date to 2026-07-08, the same day as a batch of synthetic-test seed fixtures in `cse-seed/` (`cvo_probe_overrides.json`, `cvo_synthetic_null.jsonl`, `cvo_synthetic_positive.jsonl`, `cse_test_baseline_v03.jsonl`). Plausible read: a table drop+recreate during test-harness setup left an orphaned physical location whose Nessie ref no longer points to it. **Not confirmed** — resolving it needs a Nessie-native ref/table lookup, and the REST catalog is unreachable this session (§2). Flagged for a future pass with VPC access, not adjudicated here.

---

## 7. Cross-cutting finding: the shared critical-surface alert channel appears effectively dead

This surfaced while grounding `incremental_updater`'s failure-watcher (§3) and turned out to matter for **both** `graph_nodes`/`graph_edges`.

`opal-critical-surface-alerts` (SNS) is the shared publish target for both `derive_runner.py`'s nightly critical-surface scan and `incremental_updater`'s commit-failure path. Its own Terraform (`item2c_surface_alarm.tf`) documents that as of a 2026-06-17 sweep it "shipped with 0 confirmed subscribers... paged NOBODY," and records the fix: an email subscription to `andrew@opalinvest.com` (needing one-time click-confirmation) plus a retained-as-stopgap SMS subscription explicitly noted **in the same comment** as non-delivering (account SNS-SMS is sandboxed).

**Live state found this census:** exactly 2 subscriptions exist — an SQS queue (`opal-critical-surface-alerts-coo`) and the same SMS number. **No email subscription is present, confirmed or pending.** The documented primary fix does not appear to be live. The SQS queue (created 2026-06-25) currently holds **477 messages, 0 in-flight, and zero Lambda event-source-mappings target it** — nothing is consuming it.

**Net effect:** a well-designed alert-on-failure code path (§3) is publishing into a channel that, on the evidence gathered here, is not currently reaching a human. I did not rule out an occasional manual/ad-hoc drain of that queue by COO — only the absence of an automated consumer is confirmed, so I'm stating this as strong evidence of a dead channel, not a certainty. This is the same *class* of finding as §4's "silent hook" — a second, independently-discovered instance of the same pattern (a well-intentioned alert wired at the source, invisible at the destination) — worth CTO~Z/CVO~Z treating as one structural theme across the consolidation, not two unrelated bugs.

---

## 8. Andrew-direct input (live chat, 2026-07-24) — recorded verbatim, addressed

**On the non-Iceberg tables:** *"Yeah the non-iceberg iceberg tables are probably just light tables and analytics derived from iceberg."* Checked against the producer scripts rather than accepted as given (§1, `plain_object_stores_not_iceberg` in the sidecar): **partially right, refined.** True for `resource_summaries` (a real Iceberg table, but itself computed *from* `graph_nodes`/`graph_edges` — genuinely light-and-derived), and directionally true for the `code_heat`/`tool_activity` plain parquet dumps (lighter sibling outputs of the same emit scripts that also feed the heavier `_snap` Iceberg series). **Not quite true** for `fedobs_obs_findings`, `fedobs_signals`, `axes_history`, `cse_ingest` — these are independent object stores with no Iceberg twin found; they're upstream staging inputs or standalone stores, not downstream analytics derived from the Iceberg content.

**On manifesting resources cleanly + Terraform-everything:** *"it is a good finding in the sense that we should make sure to manifest our resources cleanly so it is very obvious what is where and what purpose the resource has. All of them should be terraformed appropriately as well."* Recorded durably here and in the sidecar as direct input to CTO~Z's consolidation decision. Concrete evidence supporting it, gathered incidentally while doing the substrate census: most scheduled producers *do* have a dedicated `.tf` file (`item2a.tf`, `item2b.tf`, `stitch-produce.tf`, `cse_producer.tf`, `fedobs_producer.tf`, `resource_summaries_producer.tf`, etc.) — but the plain object-store prefixes (§1) have **no Terraform resource declaring their purpose** at all; they exist purely because a script happens to call `s3.put_object()` there. `derive-build.tf`'s CodeBuild project has **no trigger configuration found** (no schedule, no GH webhook) — manual-invoke-only, which may be intentional but is not documented as a choice anywhere I found. This mixed pattern — some resources self-describing via Terraform, others existing only as an emergent side-effect of code — is precisely the ambiguity Andrew is naming.

*(Per this lane's isolation clause, this is recorded here and surfaced to CTO~Z/CVO~Z rather than broadcast to the main fabric. If Andrew wants it pushed to COO/MSTR now, that's his or CTO~Z's call, not mine to make unilaterally while off-fabric.)*

---

## 9. Acceptance self-check (against the plan's §2.base bar)

> "Every Iceberg table has a named producer + named failure-watcher, or is declared FROZEN-BY-DESIGN with the mechanism proven. The two frozen tables' mechanisms grounded at source."

- **Both frozen artifacts: mechanism grounded at source, live-verified, not inferred from date.** `graph_contracts` = FROZEN-BY-DESIGN, proven (§5). `stitch_graph.json` = ACTIVE BROKEN PIPELINE, proven via 100% CodeBuild failure history + live grain-sentinel log content, not by-design (§4).
- **Every table has a named producer.** ✓ (table above / sidecar).
- **Failure-watchers:** named for every table; **3 explicitly confirmed-questionable** (the shared SNS/SQS channel, §7) and **several explicitly could-not-verify** rather than asserted (the `freshness_alarm` registry's actual live target list — my attempt to read its live Lambda configuration did not resolve a working function name in the time available, and I did not locate its owning `.tf` resource by name search either; this is a genuine, disclosed gap, not a paved-over one).

Full could-not-verify list (9 items) in `base.sidecar.json` → `could_not_verify_summary`. None of them were converted into a claimed result; each is stated as unresolved.

---

## 10. What I did not do (boundary discipline)

No apply, deploy, re-point, regenerate, or schema change at any point. No frozen artifact was touched or re-run. Read-only throughout: `aws s3api`/`glue`/`dynamodb`/`codebuild`/`logs`/`sns`/`sqs`/`cloudwatch`/`lambda` describe/get/list/scan calls only, plus source reads and one `gh run list`. Did not map tool-consumption of this substrate (lane `~D`) or live-AWS-vs-graph count parity (lane `~A`) beyond what was needed to understand a producer. Did not adjudicate NFRA_GCONTR's suspension or attempt to resolve the `cse_test` anomaly beyond disclosing it.

— `0.8.0_AE_CloudComp`, 2026-07-24
