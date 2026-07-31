# Session close 1824Z(07-30) - 0215Z(07-31) — Schwab behavior map, the world-model kill-list walk, two teardowns, and the tombstone gate

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, DEPLOY, IMPLEMENT

**Serial:** `0.7.0_AE_CloudOps` (base) · **PID 33920** · watcher Monitor `b4prt8zkw`
**Window:** 2026-07-30T18:24Z → 2026-07-31T02:15Z · **14 commits** (`c4169c6312` → `08ed48aee6`)
**Predecessor boundary:** `e445642c5f` (18:03Z, LD-0351 O_EXCL fix) is the PREDECESSOR's, not mine.

---

## CURRENT STATE (written for zero prior context — this is the handoff surface)

**Seat.** I took the base serial after Andrew killed the predecessor mid-session. Its PID (33636)
had **already been reused by `msedge.exe`** when I measured it — the cleanest possible proof of
death, and the exact PID-reuse residual the predecessor had itself flagged. Registered as sole
holder, session serial file written, watcher armed and round-trip-proven (it delivered live CTO mail
during the turn it was armed).

**Applied changes to the estate this session — the complete list, nothing else was touched:**

1. **`seeking-alpha-news-daily` + `seeking-alpha-analysis-daily` → DISABLED** (`0817abd006`).
   Step 1/5 of the Andrew-GO'd teardown. Reversible via `enable-rule`.
2. **`crawl-harness` stack DESTROYED — 16 resources** (`b6d033ae00`), both legs closed, ledger
   opened at deploy-start and CLOSED at completion.
3. **`shared-infra/s3.tf` — 11 resource declarations removed** across 3 block-sets (`03aed078e9`).
   **APPLY DELIBERATELY WITHHELD** (see Blockers).
4. **Tombstone gate BUILT + wired into `safe-apply.sh`** (`e21fb2c85a`), exercised end-to-end.

**Deliverables committed (all under `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/`):**
- `SCHWAB_INGESTION_BEHAVIOR_MAP_20260730.md` @`c4169c6312` — cited as authority in CTO's session log.
- `KILL_LIST_20260730.md` @`715bf4d83f` — 6 of 22 queue items walked, verdicts + evidence.
- `RESOURCE_ENRICHMENT_20260730.md` @`3b1bae6cea` — 16 of 72 resources annotated, 6 contradictions.
- `TF_DEBT_RUNNING_LIST_20260730.md` @`08ed48aee6` — the session-long tracker Andrew ordered.
- `docs/briefs/terraform-fixes-before-decommission-20260730.md` @`47141d08eb`.
- `infra/aws/terraform/tombstones.json` + `.tools/tombstone-gate.py` @`e21fb2c85a`.

**Scope posture (Andrew standing ruling ~2215Z):** writes unrestricted, SCOPE restricted. Authorized
= kill-list mandate · seeking-alpha teardown (A1-A3 then T1-T4) · storage enrichment pass · the
tombstone gate · **the Aug-1 14:00Z ETFS fire**. Everything else in my tracker is a BACKLOG, not a
warrant — I corrected my own overclaiming sentence in place rather than silently (see below).

**Aug-1 ETFS fire — VERIFIED ARMED, ~36h out at session close.** `etfs-reports-monthly-run`
(EventBridge **Scheduler**, not a Rule), **ENABLED**, `cron(0 10 1 * ? *)` `America/New_York` →
`etfs-reports-orchestrator`. I am the named detection for it.

---

## WHAT I FOUND (the substance)

### The Schwab map — the named box was the wrong box
`canonical-schwab-runner` (i-0ed92…, **Linux, stopped**) is a build orchestrator that never held
SI2. The real autoschwab box is **`quartz-si2-spike` (i-0f3d…, Windows, RUNNING)**. Both daily-pull
rules target the running one; the pull succeeded today on both masters (0824: 240 enumerated/11
downloaded; 0833: 278/13; guard `ok=true`, T-1 frontier correct). The token-minter hypothesis
INVERTED: the box IS the REST ingester (`sdd-daily-pull.ps1:293`); the Lambdas do silver conversion.
`schwab/sdd/session` was written ONCE (2026-07-10) and its consumer `schwab_sdd_ingest.py` **does not
exist in the repo**.

### The seeking-alpha channel died 2026-04-14 and reported its own nothing for 107 days
Today's manifest: `news_urls_found: 0` across all 20 categories, 1.379s. Two-stage decay measured
from the manifests: 04-13 → 402 URLs/96s · **04-14 → 0**/23s · 06-15 onward → 0/**1.4s** (stopped
even trying). **No live S3 consumer.** DDB `opal-news-articles` IS live and portal-read, but its
live writer is `news-ingestion-scheduler`, NOT seeking-alpha — so the teardown starves nothing.

### `terraform destroy` is the instrument that MANUFACTURES the resurrection hazard
Measured: the moment the crawl destroy completed, `plan` read **20 TO ADD** — all resources gone,
all still declared. **A destroy without its second leg is more dangerous than no destroy**, because
the resources are gone (nobody watching) while the declaration is armed. The zero-window procedure —
delete the blocks FIRST, plan reads "N to destroy", apply — has no window at any point.

### Six contradictions vs Andrew's semantic notes
Highest-consequence: **`opal-data-news-v2`'s deletion gate has a TWO-PLANE answer** — the note guesses
no portal consumers, but the same producer feeds the DDB corpus `portal_data_proxy` reads. Also:
globgrph carries an **unapplied 60-day expiration** on the world-model substrate; mdpf is condemned
but NOT dead; four deleted buckets kept their declarations.

---

## DEPLOYMENT SEQUENCE + VERIFICATION (AE requirement — ACTUAL output)

**1. crawl-harness destroy** — ledger `org/critical_paths/change_management/20260730T2015Z_crawl-harness-destroy_deploy_completion.md`
```
plan -destroy   -> Plan: 0 to add, 0 to change, 16 to destroy.   (EXACTLY the pre-enumerated manifest)
safe-apply      -> Apply complete! Resources: 0 added, 0 changed, 16 destroyed.
```
LIVE-plane verify (not the apply's self-report — NEVER#5):
```
i-010f195f1798b40ad -> terminated
dc2-test1-offpeak-harness -> ResourceNotFoundException
dc1-crawl-run SSM docs -> 0
POSITIVE CONTROL news-api-100pm -> ENABLED   (the probe discriminates)
```
Leg 2: `plan` then read **20 to add** → removed all 5 tracked TF sources + 7 `tfplan.*` artifacts.

**2. seeking-alpha step 1**
```
disable-rule seeking-alpha-news-daily      -> describe-rule State: DISABLED
disable-rule seeking-alpha-analysis-daily  -> describe-rule State: DISABLED
POSITIVE CONTROL news-api-100pm            -> ENABLED
```

**3. shared-infra tranche 1** — 11 declarations removed; `terraform validate: Success`;
`Plan: 0 to add, 1 to change, 0 to destroy`. **APPLY WITHHELD** — the 1 change is not mine.

**4. tombstone gate** — 6 unit controls + 2 E2E, TRUE rc read WITHOUT a pipe:
```
resurrect->2 · clean->0 · DDB replace->2 · missing register->3 · malformed plan->3 · override->0
E2E: safe-apply apply -auto-approve on a stack declaring a tombstoned bucket -> BLOCKED rc=2,
     bucket VERIFIED still 404 afterwards (nothing created)
E2E: same wiring, nothing to create -> CLEAN, "Apply complete", rc=0
```

---

## COMPILER TOOLS

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-which` (A.3 exercise probe) | startup | **PASS** | 97/97 resolve bare AND a forwarder RAN (banner) — not just `command -v` |
| `comp-surface-check` (via safe-commit) | every commit | **PASS** | 6 surfaces screened, no critical surface touched |
| `comp-pulse diff` (risk-reflex) | every commit | **PASS** | measured, denominator printed (1 file vs 1622 danger nodes) |
| `.tools/commit-gate.sh` | `tombstone-gate.py` | **PASS** | py_compile + AST + ruff clean |
| `.tools/safe-apply.sh` | crawl-harness destroy | **PASS** | HALTGT + tagauthz gates cleared; now also carries my tombstone gate |
| `.tools/safe-commit.sh` | 14 commits | **PARTIAL** | one BLOCK on a directory pathspec (correct — see Gap) |
| `terraform validate/plan/show -json` | shared-infra, crawl-harness | **PASS** | plan-as-JSON is the gate's input contract |

**What worked:** the risk-reflex and surface-check ran on every commit and printed denominators, so
"clean" was never a silent claim. `safe-apply`'s existing plan-render pattern was directly reusable
for the new gate — no new machinery.

**What failed:** `safe-commit` BLOCKED my crawl-harness commit on a **directory** pathspec
(`infra/aws/terraform/crawl-harness`) because it swept a stray untracked `org/` telemetry dir.
Scoping to explicit files cleared it. **The gate was right** — a broad pathspec on a destructive
change is exactly what it exists to catch.

**Gap found:** no comp-tool answers *"which TF-declared resources no longer exist?"* I built the
detection by hand (`grep` declarations → set-diff vs live) and **the hand-rolled instrument
false-positived on `opalinvest-portal`, the dashboard's front door.** A `comp-tfdrift`-shaped tool
is the missing rail; the tombstone gate covers only the resurrection half.

---

## BLOCKERS (evidence-cited)

1. **`shared-infra` apply is BLOCKED for everyone, not just me.**
   `aws_s3_bucket_lifecycle_configuration.global_graph` declares `ms-heat-snapshots-expire-60d` — a
   **60-day expiration on `warehouse/ms_heat/snapshots/`** (`shared-infra/s3.tf:360-369`), authored
   and never applied. It is the only change in an otherwise-clean plan. **Any** shared-infra apply
   silently arms a destructive-by-schedule rule on the world-model substrate. **Needs a ruling.**
2. **A6/A7 NOT AUTHORIZED** — `opal-data-aaii-v2` + `opal-market-data-v2` declaration removal. My
   sweep found them AFTER Andrew's A1-A3 approval, so they fall outside it. CTO is carrying the
   one-word ask to Andrew. **Surfaced, not self-dispatched.**

---

## MCP TRAFFIC

~12 messages, all with `1.0.0_SA_CTO` except one broadcast to `0.0.0_AB_MSTR`. Significant:
kill-list dispatch ACK · Q-15/Q-13/Q-22 milestone reports · seeking-alpha GO received + HALT-and-
report accepted · tranche plan approved · the ~2215Z scope ruling + my self-correction · boundary
confirmation (mdpf annotation is census, not project — row stands). **Broadcast limb discharged**:
3 Andrew rulings to MSTR verbatim; COO limb MOOT (seat killed).

---

## NEXT STEPS

1. **[Andrew]** Rule on `ms-heat-snapshots-expire-60d` — it gates every future shared-infra apply.
2. **[Andrew]** One word on A6/A7 (CTO has the ask in front of him).
3. **[0.7.0_AE_CloudOps]** **Aug-1 14:00Z ETFS fire** — armed and verified; I am the detection.
4. **[0.7.0_AE_CloudOps]** Seeking-alpha T1-T4 remain, at a seam: T1 selective capture (article
   payloads only — news ≤2026-04-13, analysis ≤2026-02-23; SKIP the 107 days of zero-manifests and
   SAY SO) → T2 7 lambdas + DDB `seeking-alpha-article-urls` (**NOT** `opal-news-articles`) → T3
   `news_layer3_curation:52` + deploy → T4 bucket + TF destroy + 2 EC2 + E1 grants (**the only
   tranche needing a ledger entry**).
5. **[1.0.0_SA_CTO]** The declared-vs-live sweep is owed for DDB / Lambda / EventBridge / SSM / IAM —
   I covered the S3 slice only.

---

## RETRIEVAL TRAPS HIT THIS SESSION (all caught, all recorded — this is the transferable part)

Six confident-but-wrong results, every one caught by a control rather than by care:

1. **`--author` substring-matches** — `git log --author="0.7.0_AE_CloudOps"` swept in `~B`'s
   ESTATE_REPORT work. Email-pinning separated them. *I nearly logged another lane's commits as mine.*
2. **`git --since` reads LOCAL time** — `--since="2026-07-30 17:00"` returned **3** of my **14**
   commits. UTC-explicit fixed it. (Memory item (11), reproduced exactly.)
3. **`aws events list-rules` paginates at 100** — `length(Rules)` returned `100` then `42`;
   the real total is **142**.
4. **Name-filtered sweeps measure the naming convention, not the estate** — filtering on `crawl`
   missed a declared bucket and an applied rule (named `dc2-*`) in the crawl stack itself.
5. **Wrong SERVICE entirely** — the Aug-1 fire is an EventBridge **Scheduler** schedule; no amount
   of `list-rules` would ever have found it.
6. **`comm` set-difference false-positived** on `opalinvest-portal` — the LIVE SPA origin. A
   set-difference row is a CANDIDATE, never a verdict.

**The through-line: "I searched and found nothing" is worthless without the denominator.** Every one
of these produced a clean, confident, wrong answer, and printing what was actually scanned is what
broke them.
