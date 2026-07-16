# Daily Infrastructure Report — Line-by-Line Triage: What Is Noise, What Is Real

**Date:** 2026-07-16 · **Author:** `0.7.0_AE_CloudOps~B` · **Status:** IN PROGRESS (live session with Andrew)
**Subject:** The daily `OPAL INFRASTRUCTURE REPORT` (`opal-infrastructure-monitor` Lambda).
**Predecessor:** `docs/briefs/infra-report-revamp-proposal-20260616.md` (CVO, 2026-06-16) — **largely SHIPPED**; this
briefing is the *second* pass, on the revamped report.

---

## Commission (Andrew-direct, 2026-07-16 ~13:1xZ / ~09:1x ET, terminal at `0.7.0_AE_CloudOps~B`) — VERBATIM

> "There is a lot going on here in the infrastructure report and we need to go through it line by line to
> idenitfy what is noise and what is real. I want to take this session with you to analyze this report and
> make sure it is actually business useful because currently it is just blaring red alert every day. Some of
> these things do need to get resolved, but we need to go step by step and assess. Our task today will begin
> with this, and the briefing will ultimately serve as not only the fix to the reporting system, but the
> foundation for an upcoming SCTY project which will be patching the holes"

**Two deliverables, as stated:** (1) the **fix to the reporting system**; (2) the **foundation for SCTY**, the
project that patches the real holes. **Method is Andrew-set: line by line, in-session, step by step.**

---

## THESIS — the report is not merely noisy; its severity is INVERTED

The 2026-06-16 CVO revamp diagnosed *"raw counts of everything"* and fixed it by **adding the missing signals**
(freshness, drift, graph-HEAD, contract-integrity, per-pipeline cost, re-homed AI triage). Those shipped. But the
revamp's **triage half did not**: the proposal explicitly called for *"new-vs-chronic"*, *"suppress the
chronic-accepted baseline"*, and *"a RED-only interrupt … alert on state-changes"* (lines 60, 36, 92). None of
that exists. So the report went from *counts of everything* to **alarms for everything** — which is the same
disease at a higher volume.

The result is a document that is **loud about the safe and quiet about the broken**:

| It renders **RED / ACT** on… | It renders **WATCH / OK** on… |
|---|---|
| Known, deliberate, sovereign-held state (the INF chain hold) | **5 never-widen tripwires that name 0 live IAM role → they CANNOT FIRE** |
| An artifact set frozen by its own un-invoked generator | **2 SEV1 surfaces UNCONTRACTED** — nothing governs them |
| A vendor 500ing, already diagnosed + fixed 8h earlier | A `comp-surface-check` that **loaded no baseline and NO-OP'd**, under an `[OK]` heading |
| Batch boxes "idle" at 0.9% CPU — measured on the wrong axis | **33% of Terraform modules unassessable** (the drift monitor is blind) |

**A report that is alarmist on the safe and silent on the broken trains its reader to ignore it.** That is the
business defect, and it is the same class CLAUDE.md NEVER#1 already names: *a false outage is not a safe error —
it spends credibility and manufactures pressure to "fix" what is working.* Alert fatigue **is** that cost, paid
daily.

---

## MEASURED DEFECTS IN THE INSTRUMENT ITSELF (grounded, not inferred)

These are defects in the *reporting system*, not things it reports. Each is source- or live-confirmed.

### D-1 — The header lies by 4 hours (UTC rendered as ET) · CONFIRMED
- **Claim:** header reads `2026-07-16 13:03 ET`; AI section reads `13:02 ET`.
- **Ground truth:** true time at read was `13:13Z` = **09:13 ET**. A 13:03 ET stamp is ~3h50m in the FUTURE.
- **Mechanism (live):** `aws scheduler get-schedule infrastructure-monitor-daily` →
  `cron(0 13 ? * MON-FRI *)`, **no `ScheduleExpressionTimezone`** → EventBridge defaults **UTC**. It fires
  13:00**Z** = 09:00 ET and stamps the wall clock with an "ET" literal.
- **Why it matters:** CLAUDE.md quick-ref — *"Times to Andrew: US Eastern only (never UTC)"*. Every age the
  reader anchors by hand is off by 4h. This is the **same TZ-confusion class** that already bit this estate
  (the "22:04Z raws were EDT renders of 02:04–03:03Z" correction, 2026-07-16 WP1).
- **Severity:** LOW risk, **HIGH credibility cost** — it is the first line of the document, and it is false.

### D-2 — The FRESHNESS manifest has NO INVOKER; the top-line RED runs off a 29-day-frozen artifact set · CONFIRMED
- **Claim (the report's own):** `WATCH: manifest itself stale (694.2h old, commit 1591d9ef821b) -- generator may
  be frozen`. It renders this as a **WATCH**, under an **OVERALL: RED**.
- **Ground truth:** `git log 1591d9ef8` → **2026-06-17 10:45:32 -0400 (14:45Z)**, author `0.7.0_AE_CloudOps`,
  subject *"NFRA_INFRPT.P1 increment-1 — DATA FRESHNESS section (B)"*. 694.2h before the run = 2026-06-17
  ~14:51Z. **The manifest is the build-day artifact. It has never been regenerated.**
- **Mechanism:** `.tools/freshness_manifest_gen.py` is a **hand-run repo tool**. `comp-grep` denominator =
  **20 references repo-wide** (gitignore + submodule aware); **ZERO** are a cron, CI job, Terraform resource, or
  scheduler. The rest are comments, tests, and shared-module imports. **A producer nothing invokes.**
- **The architecture (from its own docstring):** the generator emits the artifact **SET + cadence + thresholds +
  `freshness_basis`**; the Lambda **head-objects each artifact at runtime** and ages it. So — precisely:
  **the AGES are live; the SET and THRESHOLDS are frozen at 2026-06-17.**
- **Consequence:** any artifact retired, re-pathed, re-cadenced, or added in the last 29 days is scored against a
  June 17 belief. That is the leading candidate mechanism for the `missing/unreadable` and multi-thousand-hour
  entries — **to be proven per-line, not assumed.**
- **Why the report cannot catch this itself:** it *does* print the fact, then rates it **WATCH** — i.e. the
  instrument correctly observed that it is blind and did not let that outrank the readings taken while blind.
  **Verification law #5: an instrument that cannot fail is not an instrument.** Here it is worse — it reported
  its own blindness at lower severity than its blind readings.

### D-3 — Only ONE finding in the entire DRIFT section is NEW; it is buried among ~25 chronic ones · OBSERVED
The drift section already carries the `[standing]` vs `[NEW]` primitive. Every ERROR / RED / DENY line is tagged
`[standing]` **except one**:

> `RED shared-infra infra drift -- 1 resource(s) differ from code:`
> `aws_s3_bucket_lifecycle_configuration.global_graph [update] `**`[NEW]`**

**The discriminator exists and the rollup ignores it.** Today's only genuinely new infra drift is rendered at the
same volume as 25 things that have been true for weeks. *This single line is the whole thesis in miniature: the
report already knows what is new and declines to say so.*

### D-4 — The report contradicts itself, in two places, in one document · OBSERVED
- **SmartX.** §SMARTX PIPELINE: `Overall: OK`, served artifacts **1.5h old**, writer `opal-smartx-ingestion-pipeline`
  ok. §AI ERROR ANALYSIS on `smartx-assets-daily-pull`: *"Investor-facing portfolio data is stale."* **The AI
  asserts an impact the report's own freshness section refutes 40 lines earlier.** This is exactly CLAUDE.md's
  *"NEVER trust a producer's self-report — verify against the SERVED artifact"*, violated by the monitor itself.
  (Note the 2026-06-16 proposal killed a SmartX **false-STALE**; the section now reads correctly and the *AI layer*
  reintroduced the false alarm on a different leg.)
- **Security.** §SECURITY: `TREND (vs 2026-07-15): HIGH +2 … TOTAL +6`. §AI SECURITY BRIEFING, same run:
  *"TREND: No prior baseline available. Establish today as T0."* **The AI narrative denies the baseline the
  deterministic section just used.** The briefing has been declaring "T0" against an existing baseline.

### D-5 — The AI layer attributes a file it likely never read · SUSPECTED (to be ground-truthed)
The AI names `schwab_runtime.py` as the retry/backoff site for **`smartx-assets-daily-pull`** — a SmartX pull, not
a Schwab one — and again for `opal-assets-silver-schwab`. **The real retry defect was at the EventBridge Scheduler
layer** (default RetryPolicy, 185 attempts/24h) and was **fixed 2026-07-16 ~05–06Z** by `0.7.0_AE_CloudOps`
(explicit `retry_policy` 2/3600s, live-read on `smartx-pipeline-v1.6.0`). The AI is recommending, at CRITICAL, a
fix that (a) points at a plausible-but-probably-wrong file and (b) **landed 7 hours before the report ran**.
→ **Rule 22 applies to the monitor**: a causal claim is a HYPOTHESIS until source-confirmed, and this one carries
"Root Cause" in bold.

### D-6 — 122 HIGH is inflated by AWS's own managed policy · STRONG SIGNAL (to be counted)
Three of today's `[HIGH]` NEW findings are the **same AWS-managed policy** on one role:
`consolidation-gold-runner-role` … `Resource:* with dangerous actions in policy `**`AmazonSSMManagedInstanceCore`**
— split into 3 findings by action-group (`ssm:Put*`, `ssmmessages:Create*`, `ec2messages:DeleteMessage`).
`AmazonSSMManagedInstanceCore` is **AWS's own required policy for SSM-managed instances**; `Resource:*` on
`ssmmessages`/`ec2messages` is **how AWS ships it** — it is not grantable per-resource. Flagging it is a false
positive; flagging it **three times** inflates the count. If this pattern generalizes across the estate's SSM
roles, it is a large fraction of the 122. **Next step: compute the composition of the 122 — findings by rule, by
AWS-managed vs inline, by chronic vs new.** A number nobody can decompose is a number nobody will act on.

---

## SEVERITY INVERSION — the things rated too LOW (the SCTY seed)

These are the report's **quietest lines and its realest holes.** Each is a control that does not control.

### S-1 — 5 never-widen tripwires name 0 live IAM role → they CANNOT FIRE · rated `WATCH`
> `INERT: 5 never-widen tripwire(s) name 0 live IAM role (cannot fire) across 2 contract(s)`
> `aum-model-portfolios: ['smartx-exporter-role']`
> `benchmark-model-portfolios: ['news-pipeline-role', 'opal-generate-benchmark-returns', 'smartx-ingestion-role', 'smartx-model-monthly-pull']`

**"Never-widen" is a CLAUDE.md NEVER-rule.** A tripwire whose `forbidden_writers` name role-ids that do not exist
is a guard that **cannot ever fire** — it is decoration. Verification law #4: *a guard nothing invokes == no
guard.* Doctrine: *a control that cannot fail is not a control.* This is rated **WATCH**, below a weekend-stale
ticker file. **This is the single most SCTY-relevant line in the document.**

### S-2 — 2 SEV1 surfaces are UNCONTRACTED → structurally uncheckable · rated `WATCH`
> `BLIND: 2 SEV1 surface(s) UNCONTRACTED … CANNOT be checked (LOUD unreviewed):`
> `['advisor_intelligence', 'model_portfolios.headline']`

SEV1 = must-always-be-right. No `graph_contracts` row governs them, so the daily BMKAUD-class catch **cannot see
them at all**. Credit where due: the instrument says **LOUD unreviewed** rather than silently omitting — that is
the false-clean discipline working. But the *rating* buries it. **And `model_portfolios` is simultaneously the
one pipeline at `0/3 fresh` (§Freshness RED).** The surface that is uncontracted is the surface that is stale.
That convergence is not visible anywhere in the report because the two sections never speak.

### S-3 — `comp-surface-check` loaded NO baseline and NO-OP'd — printed under `[OK] comp` · rated `WATCH`/`[OK]`
> `[OK] comp: drift_state 0.7h old`
> `  WATCH comp-surface-check scan loaded NO baseline (.comp-graph absent in CI?) -> NO-OP; cannot assess`

**A NO-OP is being rolled up as `[OK]`.** This is the exact tool CLAUDE.md Rule 20 already warns *"IS NOT A GATE —
IT CANNOT BLOCK … never treat silence or an unblocked commit as a pass."* The report reproduces the very error the
rule was written against: **silence rendered as green.**

### S-4 — The drift monitor is blind on 33% of Terraform, reported as 15 ERROR lines · rated ERROR (wrong frame)
> `coverage 31/46 assessable (67%) (RED) + 4 deny-blocked-by-design [recorded] | 15 ERROR gap(s)`

The ~10 `Error: Archive creation error` lines are **one class**: `data.archive_file` cannot build a zip because the
source artifact is absent **in the monitor's environment**. These are **not 15 infra defects — they are 15 modules
the monitor cannot see.** Framed as ERROR, they read as estate breakage and get scrolled past; framed correctly
(*"the drift check is blind on a third of the estate"*), it is a single, fixable, real finding.
The 4 `DENY` lines are **by-design** and correctly `[recorded]` — that part works.

### S-5 — 10 SNS alert topics page NOBODY · rated `RED` (correctly!) — and this is the SCTY core
> `RED inf-gold-dispatch-release-alarm: 0 confirmed subscribers -- a real alert here pages NOBODY`
> …and 9 more, incl. 3 topics whose only subscriber is **SMS of UNKNOWN sandbox status → NON-DELIVERING**.

**This section is the report's best work** and it is the SCTY foundation: alarms that fire into the void. Note
`inf-gold-dispatch-release-alarm` — that is the **AMEND-62 kill-switch** alarm. Also note the instrument reports SMS
sandbox as **UNKNOWN** and then rules NON-DELIVERING — **that is a verdict from a non-observation**, and it is
*measurable* (`aws sns get-sms-sandbox-account-status`). Fix the instrument to measure it rather than assume it.

---

## WORKING TRIAGE LEDGER (filled line-by-line, in session)

Verdicts: **NOISE** (suppress/fix instrument) · **REAL** (fix the thing) · **KNOWN** (accepted/held — suppress to a
count) · **INSTRUMENT** (the monitor is broken, not the estate) · **OPEN** (not yet grounded).

| # | Line | Verdict | Basis |
|---|---|---|---|
| D-1 | header "13:03 ET" | **INSTRUMENT** | live schedule `cron(0 13)` no-TZ = UTC; true 09:13 ET |
| D-2 | freshness manifest 694.2h | **INSTRUMENT** | commit 1591d9ef8 = 2026-06-17; 0 invokers of 20 refs |
| D-3 | ~25 `[standing]` vs 1 `[NEW]` drift | **INSTRUMENT** | discriminator present, rollup ignores it |
| D-4 | smartx "data is stale" / security "no baseline" | **INSTRUMENT** | contradicted by the same report |
| D-5 | AI names `schwab_runtime.py` for a SmartX pull | **OPEN** | fix landed 05–06Z same day; file attribution unverified |
| D-6 | SECURITY 122 HIGH | **OPEN → likely NOISE-inflated** | `AmazonSSMManagedInstanceCore` ×3 = AWS-shipped `Resource:*` |
| S-1 | 5 INERT never-widen tripwires | **REAL (under-rated)** | guard cannot fire; NEVER-rule surface |
| S-2 | 2 UNCONTRACTED SEV1 surfaces | **REAL (under-rated)** | structurally uncheckable; converges with model-portfolios RED |
| S-3 | comp-surface-check NO-OP under `[OK]` | **REAL (under-rated)** | silence rendered green; Rule 20 |
| S-4 | 15 TF "ERROR" | **INSTRUMENT** | monitor-env archive_file failures = blindness, not drift |
| S-5 | 10 SNS topics, 0 subscribers | **REAL** | incl. the AMEND-62 kill-switch alarm |

*(Freshness per-line, automation per-function, cost, and the security composition are walked next, in session.)*

---

## NOT YET ASSESSED — do not read absence here as a clean bill

Freshness per-line (bd/inf/cot/model-portfolios), the 7 erroring functions individually, cost/right-size axis,
and the 122-HIGH composition. **Explicitly open**, per false-clean discipline.
