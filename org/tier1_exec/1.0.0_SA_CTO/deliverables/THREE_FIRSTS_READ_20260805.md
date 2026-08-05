# THREE-FIRSTS READ — 2026-08-05 13:00Z scheduled cycle

**Author:** 1.0.0_SA_CTO. **Read performed:** 2026-08-05 ~1255–1435Z.
**Scheduled proof** carried on the CTO board from the 08-04 session close: *"tomorrow 13:00Z =
THREE firsts read on separate evidence lines (12:05Z JWT mint / F-B gate line / consolidated spine
cycle-1)"*. Observation duty was assigned to `0.7.0_AE_CloudOps`; that seat was **not live** at the
mark, so the read was performed at the CTO seat rather than deferred.

## Verdict: 3/3 CONFIRMED — and the acceptance event fired

All three landed on **one scheduled run**, `run_id=mdpf_daily_20260805_130109`, which is the point:
the 08-04 water-test record left **NEVER#4 acceptance explicitly OPEN** (post-test queue item 5:
*"a SCHEDULED run proving the chain is the acceptance event; today's direct invokes are
operator-ordered interim, never acceptance evidence"*). Today's run is scheduled, not invoked.
**That acceptance is now DISCHARGED.**

| # | First | Evidence (each on its own line, none inferred from another) |
|---|---|---|
| 1 | **F-A: JWT mint on the shifted cron** | DESIRED `cron(5 12 * * ? *)` @`eventbridge.tf:34`; APPLIED `aws events describe-rule opal-inf-jwt-fetch` → `cron(5 12 * * ? *)` ENABLED; **EXERCISED** `/aws/lambda/inf-jwt-trigger` — invoked **12:05:26.063994Z**, `Orion JWT advanced in SM (len=452)`, `Eclipse JWT written to SM ... expires_at=2026-08-05T22:06:13Z`, 48.1s duration. Token object `orion/jwt/current.json` written **12:06:06Z**. |
| 2 | **F-B: stage-0 token gate, clean line** | `step STAGE0-TOKEN-GATE rc=0 dur=1s status=ok` — the acceptance criterion worded verbatim in the wiring commit @308fbbd824 (*"Acceptance OPEN until a scheduled cycle prints the clean gate line"*). Followed by `step STAGE0-BRONZE rc=0 dur=15s status=ok` — **no 401**. |
| 3 | **Consolidated spine, cycle-1** | `[modelb-spine] bindings asserted current (schema + bucket + firm set + C-1 custody row)`; `step STAGE6-REVAMP rc=0 dur=75s status=ok`; 7 keys staged + `cycle-complete.json`. Every gate PASS (cross-axis 49F/inflection/global, global composition, custody 437/437). |

**Chain terminal state: `complete`.**

## The measurement that matters most — the standing expired-token window is RETIRED

The 08-04 root cause was a **standing daily 07:02Z–13:01Z window in which the estate's only Orion
token was expired**, with the mint colliding to the minute with the 13:00Z clock-v3 floor and losing
by 12 seconds on a cold EC2.

Measured today: mint **complete 12:06:06Z**, floor **13:00Z** → **~54 minutes of real lead**
(the geometry predicted ≥55 min EDT from the 12:05 schedule mark; the delta is the 66s cold-start,
i.e. the very race that caused the incident now costs 1 minute of a 55-minute margin instead of
losing by 12 seconds). The window is closed by **geometry (F-A)** and, structurally, by the
**gate (F-B)** — and F-B is the load-bearing half: geometry narrows the race, the gate removes the
class. Both were exercised on the same scheduled cycle.

## A staleness reading that is NOT a finding — recorded so nobody re-raises it

OWNTS printed `WARN: latest consumed platinum source_vintage=2026-08-04 status=BEHIND`.
**This is healthy.** 2026-08-05 is a Wednesday; a T-1 pipeline's correct vintage IS 08-04. Per
CLAUDE.md NEVER#1 the instrument's own `BEHIND` verdict is not a second opinion — it is a
flat-hours read of a trading-day frontier. **No action. Do not open a staleness item on it.**

Likewise: served `json/portfolios/aum-timeseries.json` frozen at **2026-07-27** is **correct and
deliberate** — Andrew retired that write 2026-07-29 and the explicit IAM deny is the guard enforcing
it. See the separate Stage-3.5 finding below; the freeze is not the defect.

## Finding opened by this read — Stage 3.5 LEGACY-EMIT (committed-but-never-deployed)

`step LEGACY-EMIT rc=1 status=error` on **today's run and both 08-04 runs**: AccessDenied,
**explicit deny**, PutObject → `opal-data-portal-v2/json/portfolios/aum-timeseries.json`.

- **Repo** @`32e953198a` (2026-07-29 **07:48Z**): both writes retired, Stage 3.5 emits nothing, `return 0`.
- **Deployed** on S3: **2026-07-29 03:48:45Z** — *four hours older than the retirement commit*.
- `comp-pipescript deployed build_legacy_compat_emit.py --pipeline mdpf` → **STALE**
  (local `70149a08…` vs s3 `edc29140…`).

The retirement is correct in the repo and was never deployed to the runner. **Fix = deploy the
already-committed script; no code change.** Not urgent, nothing client-facing is wrong. Routed to
COO for owner assignment (`backfill/` sits outside Rule 13's DS-owned `{gold,silver,bronze}` set,
and mdpf is deploy-gated since 08-04 @8b18200096).

**Why it is worth fixing rather than tolerating:** a permanently-red stage in a scheduled chain is a
dead signal — a *genuine* Stage 3.5 failure is now indistinguishable from the standing one. This is
the second instance of that class found in one session (the other: `test_never_rules_gate.sh` red on
every run since LD-0367 for an unrelated stale expectation). **An assertion that is always red has
stopped being an assertion.**

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| `comp-grep` (cron shift, aum-timeseries consumers) | PASS | denominators printed (6213/7800, 7173/8764 files scanned) |
| `comp-pipescript deployed … --pipeline mdpf` | **STALE (the finding)** | `--pipeline` supplied; flagless is rc=2 REFUSED |
| `comp-which` (JWT refresher routing) | near-tie, read descriptions | routed me to source rather than guessing |
| `comp-freshness` (mdpf/aum grep) | no rows | did not carry the artifacts I needed; went to live primitives |
| `aws events describe-rule` / `logs filter-log-events` / `s3api head-object` | PASS | APPLIED + EXERCISED layers per Rule 22a — a TF read alone would have been DESIRED-only |

**What worked:** discriminating *fired* from *succeeded* on the mint, and *deployed* from *absent*
on the gate — both are fail-open shapes where "no failure" is not evidence.
**What I nearly got wrong:** the 07-27 served freeze reads exactly like a P0 outage; it took the
retirement ruling at source (`build_legacy_compat_emit.py:912`) to establish it was a guard working.
Grounding the mechanism before escalating is the only reason this is a deploy ticket and not a
false outage.
