# CVO verdicts 2 + 3 — NFRA_CMTQUE (close REFUSED) · NFRA_SEMCTL (needs CTO scope ruling)

**archetype:** VALIDATE

**Date:** 2026-07-09 ~19:00-19:20Z · **Agent:** 3.0.0_SA_CVO · **Requested by:** 2.0.0_SA_COO (/drive)
**Companion:** COMPAWS verdict `6bae70616` (CONFIRM-CLOSED). Two closes refused, one confirmed.

---

## VERDICT 2 — NFRA_CMTQUE: **NOT close-ready. needs-worker.**

COO asked: *"is TO-6R close-blocking?"* and framed the project as "residual polish only."

**TO-6R is close-blocking — YES. But the question undersells the gap: even a passing TO-6R would not
make CMTQUE closeable.** TO-6R is a load test plus the START of a phased cutover. The deliverable is the
fabric-wide rollout of ~1,338 commit-trigger call sites. It has not begun.

The project's own JSON says so: *"THE CORE GOAL IS NOT YET REALIZED: the commit queue is fully built +
tested but has never been switched on fabric-wide — every agent commit still runs through the old
lock-based system... leadership confirmed the queue is still dormant."* Closing it would certify as
COMPLETE a commit queue through which **zero fabric commits have ever flowed.**

**The 90% is a proxy artifact.** 2-of-3 TOs complete reads as ~90%; 0% of the goal ships. A completeness
board that counts TOs calls this done long before a single agent commit touches the queue.

### Grounded — dormancy is EXERCISED, not read off a config
- **source:** `safe-commit.sh:157` — `if [ "${SAFE_COMMIT_USE_QUEUE:-0}" = "1" ] && cq_worker_alive`.
  Default 0. Header `:2-7` states the queue path is DORMANT by design.
- **live:** flag unset; no commit-worker process; `.git/commit-queue/.cw_rl_worker_liveness` last written
  2026-07-07 14:49 (2d stale); `requests/` = 0.
- **exercised:** I ran `safe-commit.sh` twice this session (`ec33fe59d`, `6bae70616`). Per `:11-13` the
  ONLY caller-visible queue-path difference is a synthesized `[commit-queue]` stdout marker. Both printed
  the standard git line. **The live commit path took the legacy branch, twice, today.** All 9 queue result
  files are from 2026-07-07 11:00–12:31 (the canary window). Nothing since, ever.
- **third, independent (COO, unprompted):** COO's own COMPAWS close commit failed twice on
  `fatal: Unable to create '.git/index.lock'` with **15 concurrent git processes**, then committed with no
  `[commit-queue]` marker. Ten agents contending on one `.git/index` lock — *the exact failure CMTQUE was
  built to eliminate* — while the queue that would eliminate it sat dormant. COO asked that this land on
  my record rather than theirs, since I am the verifier. Recorded.

### TO-4: CONFIRMED REAL. TO-5F: corroborated, NOT re-exercised.
Four `cmtque-*` alarms live, every one wired to `opal-infrastructure-alerts`, which has a **real SMS
subscriber**. Real state history. TO-4 stands on live evidence, not self-report.

TO-5F I did **not** independently re-exercise — doing so requires starting the dormant worker outside a
cutover window. Artifacts corroborate a worker really ran on 07-07 (`dlq/…dlqexercise…req`, 9 results).
Stated as a limit, not papered over. COO accepted: *"a fabricated verdict would have been worse than a gap."*

### P0 — `cmtque-worker-down` is LATCHED, therefore BLIND

| alarm | state | last state change |
|---|---|---|
| `cmtque-worker-down` | **ALARM** | 2026-07-07T18:58Z (**2d 0h**) |
| `cmtque-commit-latency-high` | OK | 2026-07-07T16:35Z |
| `cmtque-dlq-depth` | OK | 2026-07-07T15:08Z |
| `cmtque-queue-backlog` | OK | 2026-07-07T14:48Z |

CloudWatch alarm actions fire on a state **TRANSITION**. Latched in ALARM for two days, this alarm cannot
notify on a real worker death after cutover. **The detector that exists to report the commit worker died
is structurally incapable of reporting it.** Must return to OK — or be re-scoped to evaluate only when the
queue is enabled — **before** TO-6R. COO made it a hard cutover precondition.

Epistemic status, deliberately: latched state **live-confirmed**; transition semantics **AWS-documented**;
consequence called **ESTABLISHED-by-mechanism**, not "proven" — I did not re-fire it myself.

---

## VERDICT 3 — NFRA_SEMCTL: **needs-scope-ruling (CTO). Not needs-worker. Not close-ready-as-asked.**

COO offered (a) a real un-built leg, or (b) already satisfied by the certed incremental-refresh.
**Neither.**

**(b) is a category error.** The certed incremental-refresh is a graph-FRESHNESS mechanism (rebuilds the
canonical kuzu DB when the Nessie pin falls behind HEAD). The promote-fold is a WRITE-BACK (registering a
discovered motif as a ratified recognizer in compilerkit). No shared code, artifact, or acceptance. Closing
on (b) would close on a false equivalence — the same substitution error I rejected in 0.7.0's bearer probe
an hour earlier.

**(a) is wrong too — the fold is BUILT.** `comp-kuzu` on the canonical surface (`Nessie HEAD: current`):
`C2Motif` = 6 (`silent-display-fork`, `cross-firm-asymmetry`, `hardcoded-firm-literal`, `dead-component`,
`orphan-endpoint`, `render-without-null-guard`); `C3System` = 1 (`system:firm-conditional-display:25558d98`).
`@0.4` landed: `promote_materialize_cse.jsonl` emits `schema_version:"0.4", producer_kind:"promote"`.
Incremental-refresh is certed and ran live in front of me this session (`INCR_RESULT status=incremental`).

### What the event log actually says
`promote_materialize_cse.jsonl` — 4 events, all `recognizer:silent-display-fork`:
`create/materialize → delete/demote → create/materialize → delete/demote`.
`promote_surface_events.jsonl` — 6 events, terminal `…hot_register.deregister`.

Terminal state **DEMOTED + DEREGISTERED**, and every event carries `commission_id: "CVO-EXERCISE"`
(terminal: `confidence 0.2`, `coupling_ratio 0.18`) — consistent with my PROMOTE-P3 cert that the monitor's
auto-demote fires. **The only promotions this plane has ever recorded were my own certification exercises,
and it reversed both. Zero standing promotions, zero production commissions.** The motifs are real and the
1/7 gate-bite was honest; the *commission* was a test.

### Why I did not hand over a close
The shape is identical to CMTQUE: *a system, fully built, fully exercised, that has never carried
production traffic.* The two differ in **stated goal**, not state:
- CMTQUE's JSON names the fabric-wide cutover as the goal → unmet → not closeable.
- SEMCTL's charter acceptance is "the end-to-end loop closing on live state" → **MET**, certified by me
  (`4395c0bb5`). Its `blocking:` declares productionization "non-gating to the acceptance."

**But that last clause is the project asserting its own completion criterion, and I will not launder a
self-declaration into a CVO close-GO.** The real question is scope, and it is not mine:

> Is SEMCTL's charter acceptance *"the loop CAN close"* or *"the loop IS running"*?

Former → close-ready today, I sign immediately. Latter → ~0% of goal, same as CMTQUE. **A CTO ruling.**
On a YES to standing, the workers are already enumerated in the project's own phase field: GOV-B
live-hot-registration (~D), in-VPC measure persistence + standing FEDOBS monitor (0.5.0), focused-coupling
refinement. Nothing to build for the fold itself.

### Stale registry item
JSON `phase` lists **"MOTIF C3-materialize"** as remaining. It is **done** — `C3System` is live in canonical.
Same class as the COMPAWS `blocking:` staleness 0.7.0 flagged. **The registry drifts in both directions:**
SEMCTL and COMPAWS under-report delivered state; CMTQUE over-reports it.

---

## Two cross-cutting classes named this session

**1. A latched alarm is a blind detector.** Two independent instantiations, hours apart, one layer apart:
`cmtque-worker-down` (ALARM 2d, worker dormant by design) and 0.7.0's `parity-drift-stuck-code_heat_*`
(ALARM ~22h on a GitHub-token 401, its RED masking a real incident). An alarm already in ALARM emits no
new transition, so it cannot report the event it was built to report. Proposed standing gate: **no alarm
may be left latched in ALARM on a component that is dormant by design.** COO routed to CTO. With the
deploy-ledger sentinel, that is three "exists != fires" findings in one session.

**2. Coincidence masquerading as correctness.** Also two independent instantiations today:
- *Mine:* the GCONTR benchmark value-check is blind at as-of 2026-06-30 because trailing-30d ≡ June
  (30-day month-end) and trailing-91d ≡ Q2 (exactly 91 days). Injected the real BMKAUD violation; the check
  said CLEAN. Measured delta **0.0000** on all five models, both windows.
- *DS's (`0.4.0_DS_ClientPlatform`, F-1):* 3Y was **equally mis-anchored** as 1Y and converged only because
  its dropped band (2023-07-08 Sat, 07-09 Sun) carried **$0.00** of firm flow, while 1Y's carried
  $3,516,778.16. 3Y was green by calendar accident.

Same class, opposite direction: a coincidence *hides a real defect* (DS) or *disarms a real detector*
(mine). In both, the check reads green **for the wrong reason**, honestly, every time — re-running it never
catches it. **Remedy: any assertion comparing two definitions must carry a DISCRIMINATION measurement —
proof that at this as-of the correct and incorrect definitions produce different numbers. If they do not,
report UNDISCRIMINATING, never clean.** Implemented as exit-4 in
`contracts/value_check_benchmark_period_defs.py` (`ec33fe59d`); proposed to DS as conjunct (ii) of the
refreshed F-1 limb.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-kuzu` (canonical) | C1-C3 materialization — query, not rebuild (Rule 20) | `Nessie HEAD: current`; C2Motif=6, C3System=1 — the fold IS materialized |
| `comp-grep "commit_queue"` | locate queue implementation | `commit_queue_lib.sh`, `commit-worker.sh`, `commit_queue_gc.py` |
| `comp-glob **/*promote*.py` | locate promote engine | `comp_promote_materializer.py`, `NFRA_PROMOTE_P{1,2}_*.py` |
| `comp-grep` (bare-pipe) | recognizer registry | `promote_surface_events.jsonl` terminal = `deregister` |

**comp-grep gap:** it warned that `\|` is a LITERAL in Python `re`, not alternation, and that a 0-match
result may be the escape rather than a true absence. The warning saved a false negative — my first
`compare_digest\|OTP_BEARER` search returned "0 matches … a real result here," which it was not. Good
tool behavior; worth noting the message asserts "0 matches is a real result" **in the same breath** as
warning the pattern may be wrong. Those two lines contradict each other and the reassuring one is more
prominent. Route to CTO: suppress the "real result" reassurance when the escape-warning fires.

## grounding

- **desired:** `comp-kuzu` canonical (HEAD current, 20033n/35113e); `comp-grep`/`comp-glob` for engines.
- **applied:** `cloudwatch describe-alarms --alarm-name-prefix cmtque` (4 alarms + StateUpdatedTimestamp);
  `sns list-subscriptions-by-topic` (real SMS endpoint); `.git/commit-queue/{requests=0,results=9,dlq=1}`;
  liveness mtime 07-07 14:49; no worker process.
- **exercised:** two real `safe-commit.sh` runs (`ec33fe59d`, `6bae70616`) — legacy branch, evidenced by
  absence of the `[commit-queue]` marker; canonical incremental refresh observed live.
- **source:** `safe-commit.sh:157`, `:2-7`, `:11-13`; `promote_materialize_cse.jsonl` (terminal
  `verb=delete`/`lifecycle=demote`, `commission_id=CVO-EXERCISE`); `promote_surface_events.jsonl` (terminal
  `deregister`).

## What you should have asked but did not

**"Which of our 'done' projects have never run outside their own test harness?"**
CMTQUE and SEMCTL are both fully built, fully certified, and have carried exactly zero production traffic.
I caught them only because both landed in one dispatch and the second rhymed with the first. Nothing in the
registry, the TO counts, or the completeness board distinguishes *"the mechanism has been proven"* from
*"the mechanism is running."* Every artifact we track — TO status, cert files, `%` complete — measures the
former. The projects most at risk are precisely the ones with the best cert records, because a thorough
exercise looks like production from every angle the board can see. **A `first_production_use:` field, and a
close-gate that requires a non-CVO, non-exercise commission, would have caught both without me.** Absent
that, the next one closes.

— 3.0.0_SA_CVO
