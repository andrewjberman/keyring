# /work tick — AC4 v0.1.1 acceleration formula fix per CVO SUBSTANCE-META YELLOW (2f2ec094d)

**Agent:** 0.1.0_DS_MarketIntelligence~D
**Trigger:** CVO SUBSTANCE-META YELLOW finding 2026-05-28T01:32Z via MCP `[CORROBORATE-with-additives + 1 SUBSTANCE-META finding YELLOW]`
**Class:** SUBSTANTIVE (CVO-finding-fix)
**Wall:** ~10min CVO-finding receipt → fix-shipped (01:32Z → 01:42Z)

## Step 0 — HALT-gate + identify
- Watcher-exit notification fired (task `b8mihngys` completed); routine probe pulled CVO finding from broker
- Lane COO: 2.0.0_SA_COO

## Step 1 — Watcher + registration
- Watcher PROCESS-OK; relaunched tracked (`bz03y40ks`) post-exit
- Registration LIVE

## Step 2 — Inbox classification
- 1 message: CVO_FINDING class from 3.0.0_SA_CVO `[CORROBORATE-with-additives + 1 SUBSTANCE-META finding YELLOW]` on FIND_INSURE.028 AC4 Signal #2 hiring-velocity acceleration formula

## Step 3 — Substantive work — AC4 v0.1.1 formula fix

**CVO finding substance:** v0.1 §2 formula `(hiring_velocity_90d / 3) / (hiring_velocity_180d / 6)` mathematically incorrect — denominator `hiring_velocity_180d / 6` is average monthly pace over the WHOLE 180-day window INCLUDING the recent 90 days. The comment claimed "prior-90d-monthly-pace" but it was actually "all-180d-monthly-average." This dampens true acceleration by ~2x.

**Worked example from CVO:**
- IMO with 9 recent + 3 prior 90d postings (true 3x acceleration):
  - v0.1 formula: `(9/3) / (12/6) = 1.5` (UNDER-fires HIGH-CONVICTION-BUILDOUT threshold `>= 1.3`; reads as marginal acceleration)
  - v0.1.1 fix: `(9/3) / (3/3) = 3.0` (true 3x acceleration — correctly classifies)

**Fix shipped** (1 file, 13 insertions/3 deletions):

```
prior_90d_count = hiring_velocity_180d - hiring_velocity_90d
                  # mutually-exclusive prior 90-day window (days 91-180 back)

hiring_velocity_acceleration =
    (hiring_velocity_90d / 3) / (prior_90d_count / 3)
    # ratio of recent-90d-monthly-pace to PRIOR-mutually-exclusive-90d-monthly-pace
    # Edge cases:
    #   prior_90d_count == 0  AND  hiring_velocity_90d == 0  -> 1.0 (quiet)
    #   prior_90d_count == 0  AND  hiring_velocity_90d > 0   -> clamp 5.0 (all-recent)
```

**Decision-relevance thresholds (§2 lines 75-78) UNCHANGED** — v0.1 thresholds were correctly calibrated against intuition that maps to CORRECT formula. v0.1 formula was under-firing those thresholds. v0.1.1 surfaces previously-missed HIGH-CONVICTION-BUILDOUT IMOs at first-empirical-run.

**Downstream schema UNCHANGED** — `hiring_velocity_acceleration` field semantics now match comment + intent without breaking `aggregate.json` (§6) or `serving/hiring_signals.json` (§7) consumers.

## Step 4 — Blockers
- None this tick. Concurrent git-lock encountered during commit; cleared via until-loop poll.

## Step 5 — Ship + CVO confirm

- Commit `2f2ec094d` via safe-commit.sh `--only` 1-file pathspec (Rule 14a)
- Lineage v0.1.1 amendment block documents fix + worked example + downstream-impact assessment
- `[SUBSTANCE-META-FIX-LANDED]` MCP to 3.0.0_SA_CVO with formal diff summary + verification against CVO's worked example + edge-case additive over the finding + Bloomberg Jobs v0.2 follow-on observation noted
- `[CC SUBSTANCE-META-FIX]` MCP to ws COO per LD-0012 routing
- Per LD-0116: T2/3 no direct MSTR comms (CVO CC'd MSTR + CTO in original finding; my fix-confirm stays in CVO + COO channel)

## Step 6 — Heartbeat
- Heartbeat: "CVO SUBSTANCE-META YELLOW fix landed: AC4 v0.1.1 acceleration formula corrected (2f2ec094d). ~10min CVO-finding-to-fix latency. Resuming STANDBY-γ for Andrew HAR."

## META-class invariant outcome
- MECHANICAL: clean
- NOVEL: signal-class-definition-sound (unchanged from v0.1; was always correct in concept)
- META: **YELLOW → GREEN** post-fix; formula now matches comment matches intent per LD-0012 (d) invariant

## Pattern banked
- Worker-side SUBSTANCE-META YELLOW receipt → driver-fix path = ~10min wall when finding cites specific formula + specific line + worked example. Fast-iteration pattern: CVO surface specific defect + driver fix in single tick + CVO confirm via ACK MCP. Companion to [[feedback_corroborate_with_concern_verdict_shape]] empirical-acceleration pattern but at worker tier (vs Tier-1 ratify-cycle tier).
- Calibration interaction: §9 EMPIRICAL-FIRST-RUN threshold tuning operates against CORRECT formula at first-empirical-run rather than compensating against defective formula; v0.1.1 ships clean for first-empirical-RAVC2 author proposal moment.

## Cycle log
- Commit-tag: `work-cycle:0028-006` covering AC4 v0.1.1 fix
- Per-tick file: THIS file (CVO-finding-fix substantive class)
