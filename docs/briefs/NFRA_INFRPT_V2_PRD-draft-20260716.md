# NFRA_INFRPT_V2 — The Daily Infrastructure Report, Redesigned

**Status:** DRAFT (Andrew-direct, 2026-07-16) · **Author:** `0.7.0_AE_CloudOps~B`
**Supersedes:** NFRA_INFRPT P1 (the 2026-06-16 CVO revamp, shipped) · **Foundation for:** `SCTY_INFRPT` (sub-project under the existing SCTY macro, per MSTR 2026-07-16)
**Evidence base:** `docs/briefs/infra-report-noise-vs-real-triage-20260716.md` (@ `04a1dca43` → `e3aaec0b0`) — every claim below is live- or source-grounded there.
**Predecessor analysis:** `docs/briefs/infra-report-revamp-proposal-20260616.md` (CVO)

---

## 0. Commission

Andrew-direct, 2026-07-16, VERBATIM:

> "we need to go through it line by line to idenitfy what is noise and what is real … currently it is just
> blaring red alert every day … the briefing will ultimately serve as not only the fix to the reporting system,
> but the foundation for an upcoming SCTY project which will be patching the holes"

And the governing frame, later the same session, VERBATIM:

> "not necessarily "fixing" the calibrations if the calibrations are just wrong. The idea is to identify what is
> actually important, what are actually good ideas in this report, and then we grab those and refine as needed,
> and throw out all the trash."

**This is a salvage, not a repair.** The verdict is rendered on **the CHECK**, never on a line of today's output.

---

## 1. The finding, in one page

### 1.1 The measured state

| Section | Headline | Truth |
|---|---|---|
| SECURITY | `122 HIGH` | **~5 real.** 102 are AWS's own managed policies flagged for `Resource:*` (`AWSLambdaBasicExecutionRole` ×53, `AmazonSSMManagedInstanceCore` ×48, `AmazonECSTaskExecutionRolePolicy` ×1); 11 are DynamoDB "encryption not enabled" — **factually impossible** (on by default since 2018, cannot be disabled; `SSEDescription==null` means the AWS-owned default key). **~96% trash.** |
| FRESHNESS | `OVERALL: RED` | 18 flagged → **4 provably false, 7 retired-path noise, 3 real, 2 real-and-known, 2 correct.** Driven by a manifest frozen at **2026-06-17** with **no invoker**. |
| AI TRIAGE | 5 confident root-causes | **3/3 falsified** where tested. Anti-triages: rated a live degrading **security control** LOW and an already-fixed function MEDIUM. |
| DRIFT | 15 `ERROR` + 25 `[standing]` | The 15 are the monitor's **own env** missing zips (blindness framed as breakage). Exactly **one `[NEW]`** finding, buried at equal volume. |
| SNS EGRESS | `RED`, 10 topics | **Correct. The best check in the report.** |

### 1.2 The instrument defects (defects IN the monitor)

- **D-1 — the header lies by 4h.** `cron(0 13 ? * MON-FRI *)`, no `ScheduleExpressionTimezone` → UTC. Fires 09:00 ET, stamps "13:03 **ET**". (Same family: "SECURITY (Daily **7 AM** Sweep)" — the sub-report honestly says `12:02 UTC` = 08:02 ET; "7 AM" is hardcoded for EST and wrong ~8 months/year.)
- **D-2 — the freshness manifest has no invoker.** `.tools/freshness_manifest_gen.py` is hand-run. Manifest `generated_at 2026-06-17T14:47:36Z`, S3 `LastModified 2026-06-17 10:48:12`, commit `1591d9ef8` = its build day. `comp-grep` denominator: **20 refs repo-wide, ZERO crons/CI/TF**. Architecture: the generator emits the artifact **SET + thresholds**; the Lambda head-objects **live** → **ages are live, the set is 29 days frozen.** Rated `WATCH` **under an `OVERALL: RED`**.
- **D-3 — the `[standing]`/`[NEW]` discriminator exists in the data and the rollup ignores it.**
- **D-4 — self-contradiction ×2 in one document.** SmartX served `OK 1.5h` vs AI "investor-facing data is stale"; Security `TREND +2` vs AI briefing "No prior baseline available."
- **D-5 — the AI has no window discipline and no state model.** It reads a log, finds *an* error, explains it — without asking whether it is *the* error, *in* the window, or *already fixed*.

### 1.3 The root cause — architectural, not cosmetic

**V1 is a UNION OF INDEPENDENT CHECKS.** Each section observes alone, rates alone, and the top line is a `max()`
over them. Every symptom falls out of that one property:

- Sections **contradict** each other, because nothing reconciles them.
- **Convergences are invisible**, because nothing joins them. The report contained *both halves* of three separate incidents and never joined either half to its partner (§3.3).
- **Blindness is rated beside readings** instead of above them, because a union has no notion of precedence.
- **Chronic and new shout equally**, because a union has no memory.
- **Unactionable checks survive forever**, because a union has no birth gate and no death gate.

> **And the 2026-06-16 lesson, which V2 exists to not repeat:** that revamp correctly diagnosed *"raw counts of
> everything"* and shipped its **ADD** half (freshness, drift, graph, contracts, cost-depth, re-homed AI). Its
> **TRIAGE** half — *"new-vs-chronic"*, *"suppress the chronic-accepted baseline"*, *"a RED-only interrupt …
> alert on state-changes"* — did not ship. **One month later the sovereign says it blares daily.** Adding
> signals to a union produces alarms-for-everything. **That is a repeatable monitoring-design failure, and the
> anti-regression rule in §6 is the deliverable that prevents V3 from re-earning it.**

---

## 2. The salvage verdicts

### 2.1 KEEP — good idea, works, **being drowned. Promote.**

| Check | Why |
|---|---|
| **SNS egress verification** | **The best idea in the report.** The only check that tests a control's **LAST HOP** rather than its existence. Found 10 topics paging nobody — incl. the AMEND-62 kill-switch alarm and `bd-allocation-file-missing`, the exact alarm for the bd outage happening now. |
| **INERT never-widen tripwire detection** | Tests whether a guard **can fire at all**. Verification law #4 as a live check. Found 5 naming 0 live roles. |
| **UNCONTRACTED SEV1 ("LOUD unreviewed")** | Reports what it cannot see rather than omitting it. False-clean discipline, correct. |
| **Deprecation labelling w/ reason + date + owning TO** | **The model for the whole report.** `inf_gold_fee_rate_history`, `yang_volatility_data` are handled *right*: dead-on-purpose, cited. |
| **`BD-source-bound` freshness basis** | Binds a derived artifact's freshness to its **source's as-of**, not wall-clock. **Caught the real cot 07-09 freeze.** |
| **`serving-day` vs `wall-clock` basis mapping** | NEVER#1 encoded as a pure function of cadence. Correct. |
| **Self-reported coverage/blindness** | Every blind spot found this session, the report had already **admitted**. Excellent instinct, mis-ranked. |
| **Cost per-pipeline + biggest movers** | Right axis. The firm thinks in pipelines. |

### 2.2 REFINE — good idea, broken mechanism

| Check | Refine to |
|---|---|
| Served-artifact freshness | **Give the generator an invoker AND a retirement path.** An artifact whose consumers were repointed must leave the set (cf. `accounts_dim`, repointed 2026-06-30 by ADVI_INFREF P1 LEG-1 — the manifest predates the fix by 13 days). |
| Blindness reporting | **Blindness must OUTRANK the readings taken while blind.** Stale manifest ⇒ freshness verdict is `UNKNOWN`, not `RED`. |
| `[standing]` / `[NEW]` | Promote to the rollup. **Cheapest highest-yield fix in the document.** |
| TF drift coverage | Reframe: "the drift check is blind on 33% of modules" = **one** finding, not 15 errors. (The 4 `DENY` lines are by-design and already `[recorded]` correctly — that part works.) |
| Cost attribution | **State the denominator.** `(untagged) $255.24` = 70% of MTD; attribution covering 30% of spend must not report `OVERALL: OK`. |
| EC2 right-size | **Wrong measure.** `inf-gold-layer-runner` was found **running 14h past its job at 1.2% CPU** — a real finding, but the fix is **stop the box**, not downsize it (the type is right for its 80-min job). Measure **idle-hours-billed**, not average CPU. |
| Deploy-drift | **Discriminate.** "stale artifact OR out-of-band deploy" is a compound verdict; CloudTrail resolves it in **one call** (it did: `UpdateFunctionCode` on `opal-partners-data`, 2026-06-03, `Andrew_Berman`). And **rate an out-of-band deploy far higher** — it means the deployed state is **unreproducible**: that hand-fix exists only in the Lambda, and the next `bd-pipeline` apply reverts it. |
| AI triage | **Scope it to what it is measurably good at.** See §4. |

### 2.3 DISCARD — not a good check. **Delete. Do not recalibrate.**

| Check | # | Why |
|---|---:|---|
| AWS-managed-policy `Resource:*` | **102** | **No action exists.** AWS ships these that way; `ssmmessages`/`ec2messages` are not grantable per-resource; `AWSLambdaBasicExecutionRole` is on every Lambda alive. Unactionable **by construction** → no threshold rescues it; excluding AWS-managed policies leaves ~0 yield. **And it is ANTI-CORRELATED WITH GOOD WORK**: today's `+2 HIGH` is our own new `consolidation-gold-runner-role` flagged for carrying AWS's standard SSM policy. *A number that rises when you do the right thing is not a metric; it is a tax.* |
| DynamoDB "Table encryption not enabled" | **11** | **Factually impossible.** Reads `SSEDescription==null` → prints "not enabled". Null = AWS-owned default key. Control: 11+ tables **do** populate `SSEType: KMS`. (CMK-vs-default may be a policy question — that is a *different*, informational check, not a HIGH.) |
| AI briefing's "TREND: No prior baseline / T0" | — | Contradicts the deterministic trend in the same document. |
| **cot rows in THIS monitor** | 5 | **Architectural.** The role is IAM-denied on `opal-data-cot` **BY DESIGN** (firm separation, CLAUDE.md #13; proven: target `implicitDeny`, 2 **isolated** positive controls `allowed`). Files EXIST and are FRESH. **The fix is NOT to grant the portal role cot read** — widening a role across a firm boundary to make a report green is gate-blocked and IAM-denied anyway. Either cot gets its own monitor inside its boundary, or the rows leave. **Do not let these be closed by grant.** |
| "Idle functions: 88" | — | CVO called this in 06-16 and it survived. An event-driven function that did not fire in 24h is not broken. |
| `employee_leaderboard` row | 1 | Watches a key that does not exist (real file: `leaderboard.json`). A wrong key is not a finding about the estate. |

### 2.4 FIX — trivial

- **D-1**: add `ScheduleExpressionTimezone: America/New_York` (or render ET explicitly). CLAUDE.md quick-ref: *times to Andrew = ET, never UTC*.
- The `"Daily 7 AM Sweep"` literal → derive from the schedule, don't hardcode.
- `trade-parquet-batch-export`: `config.py:8` `'trade-submissions'` → `'opal-trade-submissions'`. **One missing prefix.** (The AI prescribed a permanent IAM grant to a **non-existent table** instead.)

---

## 3. THE V2 ARCHITECTURE

### 3.0 The one-line thesis

> **V1 is a UNION of checks. V2 is a PIPELINE.**
> `REGISTER → OBSERVE → NORMALIZE → CORRELATE → SUPPRESS → RANK → RENDER → MEASURE`
> Each stage exists to kill one named V1 failure. **The pipeline's product is a to-do list, not a status page.**

```
  ┌─ L0 REGISTER ──── every check declares action_on_fire. No action -> IT DOES NOT SHIP.   (kills: 113 trash checks)
  ├─ L1 OBSERVE ───── emit OK | FINDING | UNKNOWN + denominator + evidence-layer.           (kills: silence-as-green)
  ├─ L2 NORMALIZE ─── NO COMPOUND VERDICTS. "missing/unreadable" is illegal.                (kills: DENIED read as ABSENT)
  ├─ L3 CORRELATE ─── join findings on shared entities; join every CONTROL to its READER.   (kills: two half-findings)
  ├─ L4 SUPPRESS ──── accepted/chronic collapse -- owner + reason + EXPIRY required.        (kills: alarms-for-everything)
  ├─ L5 RANK ──────── BLIND > CONTROL-DEAD > REAL-NEW > REAL-CHRONIC > ACCEPTED.            (kills: severity inversion)
  ├─ L6 RENDER ────── action-first. "Nothing to do today" MUST be expressible.              (kills: the green wall)
  └─ L7 MEASURE ───── track whether anyone acted. Unactioned 30d -> deletion review.        (kills: V3 re-earning this)
```

### 3.1 L0 — REGISTER: the birth gate

Every check is a registered object. **The registry is the deletion mandate made mechanical.**

```yaml
- id: sns.egress.subscriber_present
  owner: 0.7.0_AE_CloudOps
  question: "If this alarm fires, does it reach a human?"
  action_on_fire: "Subscribe a real endpoint, or document the topic as intentionally unread."  # REQUIRED, non-empty
  evidence_layer: applied          # desired | applied | exercised   (Rule 22a)
  discriminates: [subscribed, unsubscribed, non-delivering]          # must not collapse these
  severity_class: control-dead
```

- **`action_on_fire` is REQUIRED and must name a human act.** If you cannot write it, **the check does not ship.**
  *This single field would have prevented 113 of today's 122 HIGH findings from ever existing.*
- **`evidence_layer` is REQUIRED** (Rule 22a). A `desired`-only check may never assert an `applied` claim.
- **`discriminates` is REQUIRED** where an ambiguity exists — it is what L2 enforces.

**The blade, stated once, mechanically:** *if this check fires, is there something a human would DO?* **No → it is
trash, REGARDLESS OF ACCURACY.** Accuracy was never the axis. `"this table uses the AWS-owned default key"` is
~true and worthless.

### 3.2 L1 — OBSERVE: `UNKNOWN` is a first-class verdict

Every check returns exactly one of `OK` / `FINDING` / `UNKNOWN` — **never silence** — with a **declared
denominator** (Rule 22: *print the denominator of every scan you reason from*).

> **Why `UNKNOWN` is the load-bearing addition:** *"there is no channel for 'I don't know', so not-knowing renders
> as confidence"* (verification law #5). V1 has no such channel, and it shows: `access-anomaly-scanner` times out
> → emits nothing → **its silence is byte-identical to its "No access anomalies" success**. Broken and clean are
> indistinguishable. V2 gives not-knowing a channel and **ranks it above knowing** (§3.5).

### 3.3 L2 — NORMALIZE: **no compound verdicts**

**The single most repeated defect in V1 is a conclusion the observation cannot support.** Every instance:

| V1 says | Observation actually supports | Truth |
|---|---|---|
| `served artifact missing/unreadable` | `ABSENT` **or** `DENIED` | **DENIED** — files exist, fresh; IAM boundary by design |
| `Table encryption not enabled` | `SSEDescription == null` | **DEFAULT_KEY** — encryption cannot be disabled |
| `stale artifact OR out-of-band deploy` | artifact_mtime < deploy_mtime | **OUT-OF-BAND** — CloudTrail, one call |
| `Root Cause: <ValueError>` | "an error exists somewhere in this log" | **fabricated** — 0 occurrences in-window |
| `AccessDeniedException ⇒ grant this ARN` | "denied **or** absent **or** condition-unmet" | **ABSENT** — the table does not exist |

> **RULE: a rendered finding MAY NOT CONTAIN "or". If the check cannot discriminate, it emits `UNKNOWN` and names
> the query that would.** Every ambiguity above was resolvable in **one API call**.

**Corollary, and it earned its own line today:** **`AccessDenied` does not mean the resource exists.** AWS returns
it *without revealing existence* — deliberately. It is a **three-way** ambiguity (no-permission / no-resource /
condition-unmet). V1's AI collapsed it to the first and prescribed a permanent grant to a phantom table.

### 3.4 L3 — CORRELATE: **the join V1 never performs**

**This is where the value is, and it is entirely absent from V1.** The report contained **both halves of three
separate incidents** and never joined either half to its partner:

| Half A (one section) | Half B (another section) | The joined incident |
|---|---|---|
| `model-portfolios 0/3 fresh` — producer freeze 07-12 | `model_portfolios.headline` **UNCONTRACTED SEV1** | **The surface nothing governs is the surface that is stale.** |
| `bd_silver_allocations` dead 3 weekdays | `bd-allocation-file-missing`: **0 subscribers** | **The exact right control for the exact failure — alarming into the void every weekday.** |
| `inf-gold-layer-runner` running 14h idle | `ec2-auto-shutdown-alerts`: **0 subs** · `ec2-long-running-alerts`: **non-delivering** | **Two alarms for this exact condition. Both page nobody.** |

**The join IS the finding. Neither half alone would move anyone.**

**And the meta-join — the SCTY foundation (RV-0050-CVO, routed by CTO 2026-07-16):** every governance review ever
run has walked **2 of 13 audit logs**. The four never walked are, by name, exactly where a bypass would land:
`org/mass-deletion-audit.log`, `org/mcp/sovereign-registry-override-audit.log`, `org/safe-deploy-bypass-audit.log`,
`org/halt-gate-override-audit.log`. **`safe-deploy-bypass-audit.log` is the log that exists to catch precisely the
out-of-band deploy this session found via CloudTrail — and nobody has ever read it.** CVO: *"not a weak control;
the absence of one."*

> ### **THE UNIFYING FINDING OF THIS ENTIRE AUDIT**
>
> | Control | Built? | Well-designed? | Last hop |
> |---|---|---|---|
> | 10 SNS alarm topics | yes | yes | **0 subscribers — nobody reads** |
> | 4 audit logs (deploy-bypass, halt-gate, mass-deletion, sovereign-override) | yes | yes | **never walked — nobody reads** |
> | 5 never-widen tripwires | yes | yes | **name 0 live roles — cannot fire** |
> | `access-anomaly-scanner` | yes | yes | **times out silently — cannot report** |
> | `comp-surface-check` | yes | yes | **no baseline → NO-OP, printed under `[OK]`** |
> | freshness manifest | yes | yes | **no invoker — never refreshes** |
> | **this report** | yes | yes | **96% unactionable — nobody can act** |
>
> **Nobody built a bad control. Everybody built a good control and nobody wired the last hop.**
> **L3 therefore carries a standing join: EVERY control ⋈ ITS READER. A control with no reader is a `CONTROL-DEAD`
> finding — including this report.**

### 3.5 L4 — SUPPRESS: only for **good** checks, and never forever

**Suppression is NOT the remedy for a bad check** — suppressing one *keeps* it, with its upkeep and the standing
risk that someone un-suppresses it in six months and re-earns the fatigue. **Bad checks are deleted at L0.**
Suppression exists solely for a **good** check whose findings are known:

- `accepted` — a real finding, deliberately held. **Requires: owner + reason + EXPIRY.** (the INF hold; the
  correctly-deprecated artifacts). **No permanent suppression** — the expiry forces re-review, which is exactly
  what a frozen manifest never got.
- `chronic` — the same finding N days running → **collapse to a one-line count with a pointer**, never repeated at
  full volume.
- **`NEW` vs `CHRONIC` is the PRIMARY SORT KEY.** V1 already computes this and throws it away: today's single
  `[NEW]` drift finding sits among ~25 `[standing]` at identical volume.

### 3.6 L5 — RANK: severity that means something

**The inversion fix.** Precedence, highest first:

| Rank | Class | Meaning | Why it outranks |
|---|---|---|---|
| 1 | **BLIND** | the monitor cannot see | **You cannot rate what you cannot see.** A stale manifest ⇒ freshness is `UNKNOWN`, not `RED`. V1 rated its own blindness `WATCH` *under an `OVERALL: RED`* — it ranked its blindness **below the readings it took while blind.** |
| 2 | **CONTROL-DEAD** | a control exists and cannot fire / has no reader | inert tripwires, 0-subscriber topics, unwalked audit logs, a NO-OP surface-check. **This is the whole SCTY class, and V1 rates every member `WATCH`.** |
| 3 | **REAL-NEW** | a new finding with an action | the only class that should ever wake anyone |
| 4 | **REAL-CHRONIC** | known, unfixed | a count + pointer |
| 5 | **ACCEPTED** | held, with owner + expiry | one line |

### 3.7 L6 — RENDER: action-first, and **"nothing to do" must be sayable**

```
INFRASTRUCTURE — 2026-07-16 09:03 ET            <- ET. Derived from the schedule, not a literal.

DO TODAY (2)
  1. access-anomaly-scanner is failing 50% of runs (timeout 60s, avg 38.0->48.5s RISING).
     It is the hourly CloudTrail access-anomaly detector. Its failure mode is SILENCE and its
     success mode is "No access anomalies" -- broken and clean are indistinguishable.
     DO: raise timeout + paginate.            OWNER: 0.7.0_AE_CloudOps   EVIDENCE: Duration.Max=60000 x2d
  2. model_portfolios: producer frozen since 2026-07-12 (4 trading days, business-daily)
     AND model_portfolios.headline is an UNCONTRACTED SEV1 surface. Same surface. [JOINED]
     DO: restart producer + write the contract.  OWNER: 2.0.0_SA_COO      EVIDENCE: s3 mtime + graph_contracts

CHANGED SINCE YESTERDAY (1)
  * shared-infra: aws_s3_bucket_lifecycle_configuration.global_graph now drifts from code.  [NEW]

I COULD NOT SEE (2)          <- ranked ABOVE anything it "found" while blind
  * FRESHNESS: manifest 694h stale (no invoker). Verdict for this section: UNKNOWN, not RED.
  * TF DRIFT: blind on 15/46 modules (archive_file missing in the monitor env). Coverage 67%.

CONTROLS WITH NO READER (16)     <- the SCTY class, promoted out of WATCH
  * 10 SNS topics, 0 subscribers (incl. inf-gold-dispatch-release-alarm = the AMEND-62 kill-switch)
  * 4 audit logs never walked (deploy-bypass, halt-gate, mass-deletion, sovereign-override)
  * 5 never-widen tripwires naming 0 live IAM role
  * comp-surface-check: loaded no baseline -> NO-OP

CHRONIC (3, unchanged)   accounts_dim retired-not-removed; opal-partners-data deployed-ahead; ...
ACCEPTED (2)             INF hold [CTO, expires 07-18]; deprecated artifacts [2]
MONEY  $366.82 MTD ($22.93/d). Attribution covers 30% of spend (70% untagged) -- NOT "OK".
       inf-gold-layer-runner: RUNNING 14h past its job at 1.2% CPU. DO: stop it (not downsize).
```

**A green report must be possible.** V1 structurally cannot say *"nothing to do today"* — and a report that can
never say that is not measuring anything.

### 3.8 L7 — MEASURE: **the report measures its own actionability**

**The anti-regression engine.** Every rendered finding carries an id. The report tracks whether **anything
happened** — a commit, a dispatch, a suppression, an explicit dismissal.

- A check whose findings are **unactioned for 30 days** is auto-flagged **DELETION REVIEW** and named in the
  report itself.
- The report publishes its own **action rate**. *A monitor nobody acts on is a monitor that should be deleted —
  and that includes this one.*

> This is the loop the 06-16 revamp lacked. **It shipped signals and had no way to learn that nobody was acting
> on them.** L7 is what makes V2 self-correcting instead of accreting.

---

## 4. The AI layer — scoped by measurement, not by taste

**We measured both modes. The verdict is not an opinion:**

| AI mode | Result | Disposition |
|---|---|---|
| **Diagnosis** (`Root Cause:`, `Fix:`) | **3/3 FALSIFIED.** `smartx` (recommended a fix that landed 7h earlier) · `access-anomaly-scanner` ("metric misclassification" on a real degrading timeout → rated LOW) · `opal-assets-silver-schwab` (root-caused to an error with **0 in-window occurrences**; already fixed 18h prior). And it reached **opposite conclusions from identical evidence in one document**: `bd-silver-merge` "consistent with a timeout" (HIGH, correct) vs `access-anomaly-scanner` "no actual error" (LOW, wrong). | **FORBID.** Its severity ratings carry no information. |
| **Prioritization** (top-N) | **CORRECT.** Its security "TOP URGENT ISSUES" — MFA, key rotation, the website SG, IMDSv2 — picked the genuinely real items out of 122. | **KEEP, scoped.** |

**Design call: the AI's job is TRIAGE (grouping, ranking, phrasing), never DIAGNOSIS.** Deterministic checks state
facts; the AI orders them. It failed at causation and succeeded at prioritization — so it gets prioritization.

**Binding constraints on the AI layer:**
1. **It may only see findings, never raw logs.** Fabrication came from free-reading logs and explaining whatever it hit.
2. **Window discipline is enforced upstream** — it cannot see out-of-window data, so it cannot cite it.
3. **`"root cause" / "proof" / "definitively" / "source-confirmed" are RESERVED WORDS** (CLAUDE.md Rule 22) — **legal only on a SOURCE-CONFIRMED claim.** V1's AI printed **`Root Cause:` in bold on every finding**, none of them source-confirmed. V2: it emits `hypothesis:` and must cite grounding or say nothing.
4. **It must be able to say "I don't know."** Give it the `UNKNOWN` channel or it will keep rendering not-knowing as confidence.

---

## 4b. THREE LAWS EARNED AFTER THIS DRAFT WAS WRITTEN (2026-07-16 ~17:00-17:50Z, F-A/RV-0050)

*Added post-draft. Each was MEASURED in the F-A thread, not reasoned. They are the sharpest content here.*

### LAW 1 — **A cadence's corpse problem is not solved by adding a cadence. It is solved by ALARMING ON THE CADENCE'S DEATH.** (1.0.0_SA_CTO, 2026-07-16)

**The mechanism was measured THREE times in one afternoon, in three unrelated systems:**

| Instrument | Mechanism | Rot |
|---|---|---|
| freshness manifest | snapshot + stated cadence, **no invoker** | authoritative **29 days** after its keeper stopped |
| `org/audit/archive/` | snapshot + stated cadence, **no invoker** | rotted in **3 days**, into a **FALSE CLEAN** |
| CVO's F-A criterion (`git ls-files`) | reads the **INDEX**, not HEAD | would have certified a fix **never committed** |

**The audit-archive case is the one to carry, because it is Andrew's own directive rotting.** `.owned-paths.yaml:52`
records **Andrew-direct 2026-07-13 (RV-0049)**: the audit logs were untracked, *"erased by a fresh clone or a
dead disk, with their **ABSENCE INDISTINGUISHABLE FROM 'no overrides ever happened'**."* The remedy was a
snapshot archive. It ran **once** — `2026-07-13T144931Z` — and never again (comp-grep: **0 invokers**). Six
hours after that snapshot, `2.0.0_SA_COO~Z` overrode a sovereign `[STOP]` from MSTR **twice**. Neither entry
was in any durable record until CTO landed the tracking at `b150952ba` (verified: `git cat-file -e
origin/CLOUD:` 4/4; the durable log now carries 3 entries, 2 real).

> **AND THE FALSE CLEAN WAS A COMPOSITION OF TWO CORRECT DECISIONS.** (a) *snapshot, not track* — sound
> integrity reasoning (*"a log anyone may rewrite is not a log"*). (b) *every census filters
> `agent=TEST_SERIAL`* — sound, the fixture is contamination. **Compose them and the archive returns ZERO
> halt-gate overrides ever** — Andrew's exact stated failure mode, reproduced **by the remedy for it**, in
> three days. **Nobody erred. The composition is the defect** — which is precisely why it survived two
> reviews, a ruling, and RV-0050. **V2 corollary: an L0 registry gates checks one at a time; nothing in this
> design gates their COMPOSITION. That is the next hole, and it is named here rather than left silent.**

### LAW 2 — **A file's own header is a CENSUS-POISONING SURFACE. Count ENTRIES (`^[0-9]{4}-`), never pattern hits.** (ruled by CTO; earned by three agents failing)

**Three wrong counts over ONE 16-line file in ONE afternoon, by the finder AND the validator:**

```
THE FILE:   org/halt-gate-override-audit.log -- 16 lines. 13 header. 3 data.
~B:         grep -c 'HALT-OVERRIDE'   -> 4    TRUE 3   (the header's FORMAT-SPEC line contains the literal)
CVO:        grep -vc 'TEST_SERIAL'    -> 12   TRUE 0   (the 12 header COMMENT lines are not TEST_SERIAL)
~B earlier: --filter-pattern '[ERROR]' -> matched START/END/REPORT (CloudWatch parses [..] as a BRACKET
                                          PATTERN, not a literal)
CAUSE:      identical -- a file's preamble is INDISTINGUISHABLE FROM ITS DATA to a pattern match.
DIRECTIONS: opposite. One inflated the numerator, one inflated the denominator.
CAUGHT BY:  the number disagreeing with the visible lines. NOT by care, NOT by knowing the failure mode.
FIX:        timestamp anchor. Converged INDEPENDENTLY by both agents.
```

**Three wrong counts over a sixteen-line file is not three mistakes. It is a property of the file.** It
defeated the person who found the problem, the person validating the finding, and it would defeat every future
census in whichever direction that census happens to grep. This is CLAUDE.md's `grep -c` trap and
`objects=0`/`outcome:"ok"` class, **measured live, three times, in one afternoon.** It is the strongest
argument in this document for **§3.2's declared denominator** and for *put the control on the RETRIEVAL, not
the pattern*.

### LAW 3 — **FALSE REFUTATION: an instrument error that kills a TRUE finding, with a citation.** (the failure mode this estate has no name for)

CVO's `12` was aimed at a **correct escalation**. In their own words: *"Had I sent the first number, I would
have 'corrected' a true escalation into a false one, with a citation."* Not a false alarm (costs credibility),
not a false clean (costs the outage) — **a third direction: a true finding destroyed by a wrong number
carrying institutional authority.** The estate has controls against the first two and **none against this**.
**The only thing between it and the record was that they looked at the tail and the count did not match** —
`CONTROLS_OVER_CARE` verbatim (*"Look at what actually came back"*), validated twice in ten minutes by two
agents, independently, on one file, in opposite directions.

> **THE META-FINDING, and it is the honest close of this audit:** the two agents who spent the afternoon
> cataloguing instruments that lie **were, that same afternoon, lied to by their own instruments — five times
> between them** (~B: the `[ERROR]` bracket pattern, the `grep -c` header, the "bd has no scheduler"
> hypothesis, the "batch box defamed by a 14d average" hypothesis; CVO: the `git ls-files` criterion, the
> `grep -vc` header). **Every one was caught by a control failing, not by care** — a count disagreeing with
> visible lines, a positive control returning nonsense for a role named `trade-submission`, a live check
> killing a hypothesis. **Knowing a failure mode by name does not immunize you against writing it.**
> That is not a caveat on this document. **It is the argument for it.**

---

## 5. Phasing

| Phase | Deliverable | Why first |
|---|---|---|
| **P0 — DELETE** | Remove the 113 trash checks (AWS-managed `Resource:*`, DDB encryption, cot rows, idle-count, the wrong key). Fix D-1 (TZ) + the `trade-parquet` prefix typo. | **Deletion precedes suppression.** Building suppression first would preserve 113 checks that should not exist. Instant ~96% security-noise reduction, zero new machinery. |
| **P1 — RANK + SUPPRESS** | L4 + L5: blindness outranks readings; `NEW`/`CHRONIC` split (the data already exists); accepted-with-expiry. | Cheapest high-yield. `[standing]`/`[NEW]` is a **rollup change**, not a new check. |
| **P2 — CORRELATE** | L3: entity joins + the standing **control ⋈ reader** join. **The SCTY_INFRPT core.** | Where the real value is; needs P1's vocabulary. |
| **P3 — REGISTRY + MEASURE** | L0 + L7: `action_on_fire` gate; unactioned-30d deletion review. | The anti-regression. Makes V2 self-correcting. |
| **P4 — INVOKER + DELIVERY** | Freshness manifest scheduler **+ retirement path** (D-2); RED-only state-change interrupt; agent-consumable JSON feed. | **Deliberately last: a fresh manifest over an un-triaged report just re-points the noise.** |

---

## 6. Acceptance criteria (machine-checkable)

1. **No check ships without a non-empty `action_on_fire`.** Registry lint blocks it.
2. **No rendered finding contains "or".** Compound verdicts fail the render; the check emits `UNKNOWN` + the discriminating query.
3. **`UNKNOWN` outranks every non-blind verdict from the same check.** A blind section may not publish a `RED`.
4. **Every suppression carries owner + reason + expiry.** No permanent suppression; an expired suppression re-fires.
5. **The report can render "nothing to do today."** Prove it with a fixture.
6. **Every alarm topic and every audit log resolves to a named reader or a documented exemption** (SCTY foundation cell, RV-0050-CVO).
7. **The AI layer never emits a reserved word** (`root cause`/`proof`/`definitively`/`source-confirmed`) and never sees a raw log.
8. **The report publishes its own action rate**, and any check unactioned 30d appears under DELETION REVIEW.
9. **`freshness_manifest_gen` has an invoker AND a retirement path** — a repointed artifact leaves the set.
10. **Every timestamp shown to Andrew is ET, derived from the schedule, never a hardcoded literal.**

### The anti-regression rule (the one that matters)

> **No check ships without an action. No check survives 30 days of unactioned findings.**
>
> The 06-16 revamp added the right signals and re-earned alert fatigue in one month because nothing could delete a
> check and nothing measured whether anyone acted. **§3.1 (birth gate) and §3.8 (death gate) exist solely so V3 is
> not written in August.**

---

## 7. Open / not assessed

- **Ownership:** build = AE (Lambda + AWS planes) + DS (freshness wiring); CTO architecture sign-off; CVO stays in the verify lane. Charters as **`SCTY_INFRPT` under the existing SCTY macro** (MSTR, 2026-07-16) — **not** a new top-level project.
- **Andrew-gated:** the SNS subscriber fix (07-01 SNS rule, per COO). It is patch candidate #1 and rides SCTY_INFRPT with a standing-release dependency.
- **Architectural, at CTO/MSTR:** the cot rows — own-monitor-inside-the-boundary vs drop. **Not** closeable by grant.
- **Not assessed this session** (do not read as clean): `bd-silver-merge`, `opal-assets-silver-orion` (2/72), `opal-assets-silver-etf` (2/7), the GRAPH-HEAD section, `PRODUCER-DRIFT`.
- **INFERRED, not confirmed:** the prefix newest-mtime aging mechanism (a backfill of an old partition may reset the freshness clock with no new data → the monitor may **FALSE-CLEAN**). Requires reading the Lambda's aging code. **This is the most dangerous open item in the document** — false-alarm costs credibility; **false-clean costs the outage.**
