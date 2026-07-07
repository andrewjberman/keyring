# Respawn Orientation -- 0.6.0_AE_PartnerETL

**archetype:** MIXED (DIAGNOSE -> COORDINATE)
**session:** 2026-07-07, respawn per 2.0.0_SA_COO drive-cycle-2 (`drive_log_20260707T1330Z.md`) --
lane was flagged STUCK-RESOLVABLE (dead/unstaffed, blocking 3 active work items), respawn-request
fired to MSTR. This session is that respawn.

## Summary
Startup protocol (org/XXX.md) + /watcher run clean (was NOT REGISTERED -> re-registered, Monitor
armed task beiyjk4y9). Read last session's park record (07-07 close, 49F un-freeze + durables) and
the 3 pending TOs from get_agent_status (ADHC_GLDINC.SS4c, ADVI_BDAPIMIG.P1, ADVI_COTETL.L4-GUARD).
Ground-truthed the respawn hook + current pipeline freshness rather than trusting stale TO
`<status>pending` tags at face value (all 3 TOs are far more advanced than their file text alone
suggests -- see Compiler Tools / commit-archaeology below).

## Ground-truth findings this session
1. **--full-rebuild condition 4 (park-log respawn hook):** the 07-07 04:00Z nightly chain_full log
   shows A_00 took the INCREMENTAL path (self-heal coerce fired), NOT --full -- the fix is deployed
   but unexercised. Root: `bd-gold-layer-monthly-trigger` (the only mode=full source,
   `eventbridge.tf:228-238`) is `state=DISABLED` -- passive waiting would never close this.
   Escalated to CTO (ask: operator-fire mode=full now, y/n). **RULING: (b) hold** -- the
   NEVER-ad-hoc-gold-run rule binds even for a designed code path when the firing reason is
   validation. Disposition: condition 4 logged OPEN/DEFERRED, exercise-pending on a genuine
   business-driven full-rebuild (re-enabled schedule / real need / Andrew exception) -- do NOT
   re-enable the monthly trigger just to manufacture the run.
2. **bd_gold_firm_composition FAIL + all bd_platinum_* content-stale (2td, as_of 07-02 vs 07-07
   frontier)** despite silver+most-of-gold refreshing clean this morning. Root: D_03 was made
   non-fatal (51a46de30, skip-on-empty not rc=1-halt) during the 07-02 un-freeze, so it degrades
   quiet-not-crash while its input (B_01.holdings_lots.py:489 calendar-day holiday-window bug --
   my own park-log Finding 5, routed to DS) stays unfixed. **cot has the identical pattern**
   (cot_platinum_* content-stale 2td, cot's own `data/cot/scripts/gold/B_01.holdings_lots.py` is a
   separate Model-B-ported file, same bug class likely forked into both before either got fixed) --
   so this is cross-firm, not bd-only. DS is currently NOT REGISTERED (not live) and its recent logs
   show no work on this fix -- looks unpicked-up. Escalated to COO (2 messages: bd finding + cot
   fast-follow) since the owning agent isn't live to self-drive it.
3. **ADHC_GLDINC.SS4c**: canary + IAM + EventBridge daily rule are deployed
   (`infra/aws/terraform/bd-pipeline/gldinc-ss4c.tf`); scorecards landed 06-23/06-24/07-01 (weekly
   cadence, next due ~07-08 -- not yet stale). TO's own text (06-25 grounded-status note) already
   showed the core build RAVC2-accepted/CloudOps-gated/DS-clean; remaining items are watch-the-watcher
   registration + NFRA_COSTAWS cost-line, both explicitly NEAR-TERM-not-a-fire. No action taken this
   session -- not yet due for a check-in.
4. **ADVI_COTETL.L4-GUARD**: commit archaeology shows PIECE-2 activated + oracle cleared + CVO SOUND
   + COO live-verified 06-26 (tag cot-pipeline-v0.6.0), plus further CTO-B auth-chain hardening
   (F1/F2, 4619a0dc4) deployed+ledger-closed by 0.7.0~A on 07-02. The TO file's `<status>pending`
   looks stale against this -- did not chase a full reconciliation this session (time-boxed to the
   two live findings above); flagged as a follow-up.
5. **ADVI_BDAPIMIG.P1**: commit trail (07-02 through 07-06) shows extensive P1a REST-productionize
   work landed and ledger-closed (WS-2a runner idempotency+chunking, D2 bd-silver-merge Lambda,
   bd-served-vintage-alarm fail-loud metric). TO file also looks stale vs the JSON project phase text
   ("Phase-1 wave DISPATCHED 2026-07-02: P1a 0.6.0 / P1b 0.7.0~A / P1c 0.6.2"). Not fully reconciled
   this session -- follow-up.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| comp-freshness chain bd | ground served-artifact freshness before trusting the park-log's "resolved" framing | FAIL on firm_composition + WARN(content-stale) on all bd_platinum_* -- real finding, escalated |
| comp-freshness chain cot | cross-check whether the same bug class hits cot | WARN(content-stale) on all cot_platinum_* -- confirms cross-firm, escalated |
- What worked: comp-freshness caught a real, live, degrading-quiet production gap that a status-only read of my park log would have missed (the park log's "self-heals... currently last-good 07-03" read as resolving; ground truth shows it hasn't moved and cot has it too).
- Gap: did not run comp-blast/comp-pipescript on the SS4c/L4-GUARD/BDAPIMIG.P1 reconciliation -- time-boxed this session to the two live/escalatable findings; the 3-TO staleness reconciliation is flagged as a follow-up, not silently dropped.

## Current State
- Watcher: live (task beiyjk4y9). Registration: live.
- CTO ruling received + closed this session (condition 4 -> OPEN/DEFERRED, no further chase absent a real business need).
- COO messaged (2x): bd firm_composition/platinum staleness + cot parallel. Awaiting COO disposition (DS respawn-request vs wait).
- 3 pending TOs (SS4c/BDAPIMIG.P1/COTETL.L4-GUARD) ground-truthed as more-advanced-than-filed but not fully reconciled to accurate `<status>`.

## Next Steps
1. **[COO, awaiting reply]** disposition on the firm_composition/platinum content-staleness (DS respawn vs wait for DS's natural wake).
2. **[0.6.0, follow-up]** reconcile ADVI_COTETL.L4-GUARD and ADVI_BDAPIMIG.P1 TO `<status>` against the actual (far more advanced) ground truth -- likely several sub-legs closeable or already-closed-but-unmarked.
3. **[0.6.0, on COO/CTO signal]** pick up whichever of the 3 TOs has a live, actionable next leg once reconciled.

## Blockers
None. Awaiting COO/CTO replies on the two escalations; continuing TO reconciliation in the meantime.
