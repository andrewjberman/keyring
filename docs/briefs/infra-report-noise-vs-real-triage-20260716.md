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

## THE GOVERNING FRAME (Andrew-direct, 2026-07-16 ~15:4xZ / ~11:4x ET, same terminal) — VERBATIM

> "Yeah I think the way this whole audit should work is not necessarily "fixing" the calibrations if the
> calibrations are just wrong. The idea is to identify what is actually important, what are actually good ideas
> in this report, and then we grab those and refine as needed, and throw out all the trash. That is a good
> framework through which to guide this analysis process."

**THIS SUPERSEDES "noise vs real" AS THE UNIT OF ANALYSIS.** The verdict is no longer rendered on a *line of
today's output* — it is rendered on **the CHECK ITSELF**. This is a **SALVAGE**, not a repair:

```
KEEP     the idea is good AND the implementation works  -> promote it, it is being drowned
REFINE   the idea is good, the implementation is broken -> keep the idea, rebuild the mechanism
DISCARD  the check is not a good idea                   -> delete it. Do NOT recalibrate it.
```

**THE DISCRIMINATOR (the blade this frame hands us): _if this check fires, is there something a human would
DO?_ If no -> TRASH, regardless of whether it is ACCURATE.** This is sharper than noise-vs-real because some
checks are *accurate and still worthless*: "this DynamoDB table uses the AWS-owned default key" is ~true and
entirely unactionable. Accuracy is not the bar. **Actionability is.**

**AND IT CORRECTS THE OBVIOUS-BUT-WRONG REMEDY.** The instinct (mine, and MSTR's charter constraint as first
drafted) was *"add the missing suppression layer"*. But **suppressing a bad check KEEPS the bad check** -- its
maintenance cost, its confusion cost, and the standing risk that someone un-suppresses it in six months and
re-earns the fatigue. A check that can never produce an action should be **deleted, not muted**. Suppression is
the right remedy ONLY for a *good* check whose findings are *accepted/known* (the INF hold, the deprecated
artifacts). The two remedies are not interchangeable, and conflating them is how a monitor accretes forever.

**COROLLARY (why 83.6% is a design verdict, not a tuning problem):** if a check's output is unactionable **by
construction** -- as the AWS-managed-policy `Resource:*` rule is, since AWS ships those policies that way and
they are not grantable per-resource -- then no threshold, exclusion list, or severity tweak rescues it. Tuning
it to exclude AWS-managed policies leaves a check whose remaining yield is ~0 findings. **That is not a
calibration bug. It was never a good check.**

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

---

# THE SALVAGE LEDGER — what we grab, what we refine, what we throw out

*Per the governing frame. Verdict is on the CHECK, not the line. Blade: **would a human DO something?***

## KEEP — good idea, working implementation. These are being DROWNED and should be PROMOTED.

| Check | Why it is good | Evidence it earns its place |
|---|---|---|
| **SNS egress verification** ("does this alarm reach a human?") | **The best idea in the report.** Nothing else in the estate asks it. It is the only check here that tests a control's LAST HOP rather than its existence. | Found 10 topics paging NOBODY — incl. `inf-gold-dispatch-release-alarm`, the AMEND-62 kill-switch, and `bd-allocation-file-missing`, which is the exact alarm for the exact bd outage happening right now. COO elevated it to a CTO supervision condition within the hour. |
| **INERT never-widen tripwire detection** | Tests whether a guard **can fire at all** — the rarest and most valuable class of check. Directly instantiates verification law #4. | Found 5 tripwires naming 0 live IAM role across 2 contracts. A NEVER-rule surface with a decorative guard. |
| **UNCONTRACTED SEV1 detection** ("LOUD unreviewed") | Reports what it **cannot** see instead of silently omitting it. This is false-clean discipline done right. | Found `advisor_intelligence` + `model_portfolios.headline` ungoverned. |
| **Deprecation labeling w/ reason + date** | Distinguishes *dead-on-purpose* from *dead-by-accident* — the exact distinction the rest of the report lacks. | `inf_gold_fee_rate_history` and `yang_volatility_data` are handled **correctly**, with reason, date, and owning TO. This is the model for everything else. |
| **`BD-source-bound` freshness basis** | Genuinely sophisticated: binds a derived artifact's freshness to its SOURCE's as-of rather than wall-clock. | It **caught the real cot 07-09 freeze** and correctly rated it WATCH (fail=None). Working as designed. |
| **`serving-day` vs `wall-clock` basis mapping** | The trading-calendar discipline (NEVER#1) encoded as a pure function of cadence. Correct design. | `business-daily`/`vendor-daily` -> calendar-aware. Not the defect anywhere I looked. |
| **Self-reported blindness** (`31/46 assessable`, `manifest stale`, `loaded NO baseline`) | The instinct to **report its own coverage** is excellent and rare. | Every blind spot I found, the report had already ADMITTED. It just rated them below the blind readings. |
| **Cost: per-pipeline + biggest movers** | The section Andrew values; per-pipeline is how the firm thinks. | Works. See REFINE for the denominator. |

## REFINE — the idea is right, the mechanism is broken. Keep the idea; rebuild the mechanism.

| Check | Keep | Broken because | Refine to |
|---|---|---|---|
| **Served-artifact FRESHNESS** | The idea is **THE** signal this firm gets bitten by (CVO 06-16 was right). | **The manifest has no invoker** (D-2). Frozen 2026-06-17; the estate moved on. It now indicts a HEALTHIER estate every morning. | Give the generator a scheduler/CI leg **and** a retirement path (an artifact whose consumers were repointed must leave the set — cf. `accounts_dim`, repointed 06-30). |
| **Blindness reporting** | Reporting coverage is right. | Blindness is rated **BELOW** the readings taken while blind (WATCH under an OVERALL: RED). | **A blind monitor's blindness must OUTRANK its readings.** If the manifest is stale, the freshness verdict is UNKNOWN, not RED. |
| **`[standing]` vs `[NEW]`** | The discriminator **already exists in the data**. | The rollup ignores it — today's ONE `[NEW]` sits among ~25 `[standing]` at equal volume. | Promote to the rollup. **Cheapest highest-yield fix in the document.** |
| **TF drift coverage** | Knowing what drifted is right. | 15 `archive_file` "ERROR"s are the monitor's OWN env missing zips — **blindness framed as estate breakage**. The 4 `DENY` lines are by-design and already `[recorded]` correctly. | Reframe: "the drift check is blind on 33% of modules" = ONE finding, not 15 errors. |
| **Cost per-pipeline** | Right axis (pipelines, not services). | `(untagged) $255.24 = 70% of MTD` — attribution covers 30% of spend and reports `OVERALL: OK`. | State the coverage denominator; tag the estate. An attribution over 30% is not OK. |
| **EC2 right-size** | Real money, real idea. | **Wrong axis**: 14d-avg CPU on a BATCH box. `inf-gold-layer-runner` (c6a.4xlarge, 0.9%) runs ~80min/night **by design** — that is a healthy batch box, not waste. | Measure CPU **while running**, or measure idle-hours-billed. Avg-over-14d structurally defames every batch box. |
| **AI error triage** | Triage is the whole point (CVO: "the actionability engine"). | **Falsified 3/3. It ANTI-triages** — no window discipline, no state model. Rated a live degrading security control LOW and a fixed function MEDIUM. | Rebuild with: window discipline (is this error IN the window?), a state model (is it already fixed?), and a mandate to say **"I don't know"**. Until then it is **negative value** — see DISCARD. |

## DISCARD — not a good check. Delete it. Do NOT recalibrate.

| Check | Count | Why it is trash (the blade: what would a human DO?) |
|---|---:|---|
| **AWS-managed-policy `Resource:*`** (`AWSLambdaBasicExecutionRole` x53, `AmazonSSMManagedInstanceCore` x48, `AmazonECSTaskExecutionRolePolicy` x1) | **102** | **Nothing. There is no action.** AWS ships these policies with `Resource:*`; `ssmmessages`/`ec2messages` are **not grantable per-resource**, and `AWSLambdaBasicExecutionRole` is on every Lambda on earth. Unactionable **by construction** -> no threshold rescues it. **Worse: it is ANTI-correlated with good work** — today's `+2 HIGH` is our own new `consolidation-gold-runner-role` being flagged for having AWS's standard SSM policy attached. **A metric that punishes correct infrastructure will be ignored, and should be.** |
| **DynamoDB "Table encryption not enabled"** | **11** | **Factually impossible.** DynamoDB encrypts at rest by default since 2018 and **it cannot be disabled**. The scanner reads `SSEDescription == null` and renders "not enabled" — but null means **AWS-owned default key**. Control: 11+ other tables DO populate `SSEType: KMS`, so the field works. Same conflation class as cot's "missing/unreadable": **a conclusion the observation cannot support.** (If CMK-vs-default is a real policy, that is a *different*, informational check — not a HIGH.) |
| **AI security briefing's "TREND: No prior baseline / establish T0"** | — | Contradicts the deterministic `TREND (vs 2026-07-15): HIGH +2` **in the same document**. It has been declaring T0 against an existing baseline. Delete the narrative trend; the mechanical one is right. |
| **cot rows in THIS monitor** | 5 | **Architectural, not calibration.** The monitor is IAM-denied on `opal-data-cot` **BY DESIGN** (firm separation, CLAUDE.md #13 — gate + IAM enforced). Proven: target implicitDeny, 2 isolated positive controls allowed. **Do NOT widen a role across a firm boundary to make a report green.** Either cot gets its own monitor inside its boundary, or these rows leave. |
| **"Idle functions: 88"** | — | CVO already called this in 06-16 and it survived: an event-driven function that did not fire in 24h is not broken. Conflates supposed-to-be-idle with dead cruft. (Refine target, if wanted: "idle >30d AND not event-wired".) |
| **`employee_leaderboard` row** | 1 | Watches a key that does not exist; the real file is `leaderboard.json`. A wrong key is not a finding about the estate. |

## FIX (trivial, not a design question)

- **D-1 the header lies by 4h.** `cron(0 13 ? * MON-FRI *)` with no `ScheduleExpressionTimezone` = UTC, fires 09:00 ET, stamps "13:03 **ET**". Violates the CLAUDE.md quick-ref (times to Andrew = ET, never UTC).
- **"SECURITY (Daily 7 AM Sweep)"** — the sub-report honestly stamps `12:02 UTC` = **08:02 ET**. The "7 AM" label is hardcoded for EST and is wrong for ~8 months of the year. Same TZ family as D-1.

## THE SCORE, UNDER THE FRAME

| | |
|---|---|
| SECURITY | **122 HIGH -> 9 non-trash -> ~5 genuinely real** (3 shared Lambda roles/SOC2 CC6.2; patricia console w/o MFA — already investigated 07-14; 1 unencrypted EBS snapshot). The 4 SG findings are 2 on a zero-instance ALB (the AI itself says suppress) + 2 on a **public WordPress site** — a public web server on 80/443 is not a finding. **~96% of the headline number is trash.** |
| FRESHNESS | 18 flagged -> **4 confirmed FALSE, 7 retired-path noise, 3 REAL, 2 real-and-known, 2 correct-as-is.** The one that matters: `model-portfolios 0/3` (producer freeze 2026-07-12, 4 trading days, calendar-resolved) — **which is also an UNCONTRACTED SEV1 surface.** |
| AI TRIAGE | **3/3 falsified.** Negative value as implemented. |
| **The keepers** | SNS egress · INERT tripwires · UNCONTRACTED SEV1 · deprecation labeling · BD-source-bound basis · self-reported blindness · cost-by-pipeline. **These are good. They are drowning.** |

**The one-line answer to "is this business useful":** *the report's real product today is not information — it is
camouflage.* A live, degrading, hourly **security control** (`access-anomaly-scanner`, 50% timeout, failure mode
== success mode == silence) was rated **LOW** and sat under a `122 HIGH` headline that is ~96% AWS-managed-policy
noise. **The noise did not merely waste attention. It hid the one thing on the page that mattered.**

---

## NOT YET ASSESSED — do not read absence here as a clean bill

Freshness per-line (bd/inf/cot/model-portfolios), the 7 erroring functions individually, cost/right-size axis,
and the 122-HIGH composition. **Explicitly open**, per false-clean discipline.
