# KIMI SEMANTIC VERTICAL PIPELINE — end-to-end research (pre-PRD)

**Author:** `1.0.0_SA_CTO~B`, 2026-08-04 ~1730Z. **Order:** Andrew-direct this session — trace
the pipeline end to end (artifact pooling, dataflow, resource manifest, terraform, MSTR's
position), census the breaks beyond the MSTR-ask symptom, then PRD + `OPAL_KIMIPIPELINE`
registration with direct TOs (explicitly NOT through COO).
**NAMING ACT (Andrew-direct, this session): the system is the "Kimi Semantic Vertical
Pipeline"** — the standing token for humans grasping for it and agents searching for it.
Current estate names it `estate-report` / `SemanticEvolution`; the PRD carries the rename
(TF tags included).
**Prior art this builds on (not duplicated):** CVO's Andrew-directed e2e validation this
morning, `KIMI_PIPELINE_E2E_VALIDATION_20260804.md` @f022ca3e05 (~04:53Z, G1–G8) — every gap
re-verified live by this seat ~17:2xZ before restating; deltas since CVO's run are marked.

## 1. What the pipeline IS (one paragraph)

A daily 9a-ET vertical that reads the estate's day of change (9a→9a commit window via a
read-only GitHub PAT), compiles a DETERMINISTIC changed-resource report (ladder-bucketed
against the semantic canon's own registries), asks **Kimi/K3** for an exec summary plus
**semantic-prose evolution proposals** (prose fields only — deterministic fields are compiled
and unproposable), lands report + per-day manifest in S3, and then runs a human-sovereign
loop: **pipeline SUGGESTS → Andrew RATIFIES → CVO LANDS → MSTR backstops the flip and
landed-vs-ratified parity.** Its purpose is to keep the semantic canon's prose alive — the
same canon `comp-estate` reads from (`estate-coverage-resolver.json`).

## 2. Dataflow + where artifacts pool

```
EventBridge Scheduler estate-report-0900et            cron(0 9 * * ? *) America/New_York  [DISABLED]
  -> Lambda estate-report-orchestrator                (live; fire-and-forget, 60s)
    -> EC2 estate-report-runner  i-04981b6aec3bed86b  (t3.medium, TRANSIENT: stopped between runs)
       systemd oneshot estate-report.service on boot
       estate_report_runner.py:
         manifest/{date}.json -> RUNNING              (manifest-FIRST, contract v2 — a dying run
                                                       stays durably visible; guard shares no
                                                       failure mode with the guarded)
         GitHub PAT (secret estate-report/github-token, value out-of-band)
           -> commit window 9a->9a ET
         deterministic compile: changed paths -> 3 registries (incl. estate-coverage-resolver.json
           + lambda-source-map.json spine) -> ladder buckets + day-over-day set-delta
         Kimi K3 call (secret astn/kimi/api-key, REUSED from astn-pipeline by ARN — deliberately
           not redeclared) -> exec summary + prose proposals   [has NEVER succeeded: KIMI_EMPTY]
         daily/YYYY/MM/DD/estate-report-{md,json}
         manifest -> PENDING  (FAILED+reason on caught error)
         instance self-stop
  -> CVO /estate-pull: manifests vs config/_EPOCH.json -> classify (MISSING/RUNNING-stale/FAILED/
       PENDING) -> pull -> ADJUDICATE WITH ANDREW -> land x3 (repo org/estate-reports/{date}.md,
       s3 adjudicated/YYYY/MM/DD/, manifest flip ADJUDICATED|NO-SEMANTIC-CHANGES) — flip LAST
  -> MSTR-base backstop (LD-0356): verify flips + landed-vs-ratified parity; the startup ask
       ("surface the report, ask Andrew for changes") — carried in XXX.md Step 1b-F + ajb.ps1
```

**S3 pooling (bucket `opal-estate-report`, versioned, SSE, lifecycle):** `daily/` reports ·
`manifest/` per-day gates · `adjudicated/` CVO copies · `code/` deployed runner (upload IS the
deploy) · `logs/` run logs · `config/` epoch anchor (**EMPTY — see B5**).
**Repo pooling:** `org/estate-reports/` = the granted day-record home (@005d4e8e52) —
**currently empty**; the one day record sits in the interim home
`org/tier1_exec/3.0.0_SA_CVO/deliverables/estate-report-day-records/2026-07-30.md` @3271a27cf.
**Future v4 (RULING 8 @150d45b5b7, SPEC ONLY):** day-first `{YYYY-MM-DD}/` roots, five folders
(text-input, change-cochange, deployment-motion, kimi-report, signed-review), manifest at day
root.

## 3. Resource manifest (all verified live this session)

| Resource | State |
|---|---|
| S3 `opal-estate-report` | live; exactly ONE report day (2026-07-30) |
| Scheduler `estate-report-0900et` | **DISABLED** (get-schedule, live) — cron 9a ET, targets orchestrator |
| Lambda `estate-report-orchestrator` | live |
| EC2 `estate-report-runner` `i-04981b6aec3bed86b` | stopped (correct between-runs state); tags Project=ESTATE_REPORT, System=SemanticEvolution, ManagedBy=Terraform |
| IAM | scheduler/orchestrator/runner/selfstop/capture-writer roles all applied; runner denied CVO prefixes (measured w/ positive control, per iam.tf) |
| Secrets | `estate-report/github-token` (value out-of-band) · `astn/kimi/api-key` (reused) |
| systemd `estate-report.service` | on-boot oneshot, on the instance |
| CVO skill `/estate-pull` | exists; FIRST-ON-LOAD duty in CVO prompt.md |
| MSTR rule LD-0356 | landed in both carriers (XXX.md MSTR row + ajb.ps1 directive) |

**TERRAFORM: ALREADY EXISTS — no new root needed.** `infra/aws/terraform/estate-report/`
(main/instance/orchestrator/iam/secrets .tf) covers bucket+lifecycle, instance+SG, scheduler,
orchestrator, all IAM, secret. PRD work is a RENAME/TAG pass to the new token, not a build.
Hygiene: 12 untracked local `tfplan.*` binaries in the root (clean); `EC2_MANIFEST.json`
records a STALE instance_id (`i-09fa5115b3282d6ea`, a build-iteration predecessor — live is
`i-04981b6aec3bed86b`).

## 4. Status: NOT accumulating — one shakedown fire ever

2026-07-30 report, fired MANUALLY 07-31T00:40Z (not by schedule): deterministic half clean
(248 commits → 214 paths, honest zeros), AI half **KIMI_EMPTY twice → AI_SECTION_ABSENT**
(loud marker). Adjudicated **this morning 05:07Z** as NO-SEMANTIC-CHANGES (Andrew via MSTR
relay 050242Z; repo @3271a27cf) — G2/G8 of CVO's census moved this morning. Nothing else has
ever run; days 07-31 → 08-04 have no report, no manifest, and **nothing that could notice**
(B5).

## 5. Break census (B1–B8; CVO G-numbers in parens; all re-verified live ~17:2xZ)

| # | Break | State |
|---|---|---|
| B1 (G1) | **Scheduler DISABLED** — the primary break; deliberate hold during the v4 migration (iam.tf:24 names it) | OPEN |
| B2 (G3) | **Kimi/K3 call has NEVER produced output** (KIMI_EMPTY x2 on the only run); diagnosis owned by 0.7.0_AE_CloudOps~B but **gated: C3L.1 UNISSUED + CTO "3-5 fence" stands** — queued for "the next Andrew touchpoint," which is THIS session | OPEN — needs Andrew's word |
| B3 (G4) | **Deployed runner code STALE**: v3 corpus census @82f87697e8 committed 16 min after the last upload, never re-uploaded (upload IS the deploy) | OPEN |
| B4 (G5) | **v4/RULING-8 layout ratified but SPEC-ONLY**; XXX.md + MEMORY.md charter MSTR's backstop on v4 keys **nothing writes** — the backstop's documented oracle path does not exist in the live bucket | OPEN — record+build convergence |
| B5 (G7) | **`config/_EPOCH.json` never written** (go-live flip) → ABSENT-day detection structurally impossible → loop + backstop **correctly inert**; 4 missing days were invisible BY CONTRACT | OPEN |
| B6 (G6) | **Text-input capture half-built**: extractor `.tools/estate-capture.py` works (fail-closed, corpus-measured) but has NO S3 upload code; writer IAM role live; zero text-input keys; site-Z second device undone | OPEN |
| B7 | **Day-record home split**: `org/estate-reports/` granted + empty; the record lives in CVO's interim home; the session-start AD residue is cleared | MINOR — CVO move pending |
| B8 | **Two go-live anchors in the records**: XXX.md says the backstop binds "from its first report-day" (happened 07-30); the skill/backstop contract keys on `_EPOCH` (absent). MSTR's non-ask is CORRECT under the epoch anchor, a MISS under the XXX phrasing. **The record split, not the agent, is the defect** | OPEN — pick ONE anchor (recommend `_EPOCH`) |

## 6. Where MSTR fits, and the direct answer to "MSTR never asked me"

MSTR-base holds LD-0356: surface the daily report at startup, take Andrew's semantic review,
land ratified adjustments; plus the RULING-5 integrity half (verify the reference artifact
matches what Andrew ratified — accepted on the first live e2e fire). **The ask is the LAST
link of the chain, and every link upstream is dead**: scheduler off (B1) → stale runner (B3)
→ zero AI proposals ever (B2) → no epoch so no absence detection (B5) → nothing to surface.
CVO's validation put it exactly: *"the pipeline never lied about being complete; it is simply
not complete."* MSTR's silence is the correct inert behavior under the deployed contract —
made to LOOK like a miss by B8's record split. (Also observed: no MSTR session log exists for
today; its only trace is the 05:02Z relay.)

## 7. Ordered close path (CVO's, still valid; deltas applied)

1. **KIMI_EMPTY diagnosis** — ~B on clearance; **blocked on Andrew: C3L.1/fence word** (B2).
   Nothing downstream matters until the AI half produces once.
2. **Implement v4/RULING-8 layout** (~B) + reconcile /estate-pull skill, XXX.md, MEMORY.md to
   the ONE layout (CVO lands record fixes) (B4, B8).
3. **Deploy current runner** — re-upload after (2) (B3).
4. **Capture uploader + site-Z** (B6).
5. **Go-live flip**: CVO writes `_EPOCH`; Andrew's word enables `estate-report-0900et` (B5, B1).
6. **First real adjudication = the acceptance event** (RULING-5).
   Cross-cutting: token rename pass (TF tags, EC2_MANIFEST instance_id fix, tfplan cleanup,
   day-record move) — folds into the PRD's TOs.

## 8. Next step (per Andrew's order this session)

PRD `OPAL_KIMIPIPELINE` + registry entry, TOs cut by this seat DIRECTLY to the needed agents
(Andrew spawns; NOT routed through COO). Open calls to Andrew embedded in the PRD gate:
(a) C3L.1/fence clearance for ~B's Kimi diagnosis — the critical path;
(b) confirm sequencing v4-layout-before-re-enable (CVO's order) vs diagnose-first-then-migrate;
(c) the single go-live anchor ruling (B8 — recommend `_EPOCH`).
