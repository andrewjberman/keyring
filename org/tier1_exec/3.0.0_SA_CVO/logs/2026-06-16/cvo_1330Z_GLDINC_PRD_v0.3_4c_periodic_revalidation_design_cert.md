# CVO design cert — ADHC_GLDINC PRD v0.3 §4c (post-cutover standing oracle re-validation) — 2026-06-16 ~13:30Z

**archetype:** VALIDATE

CTO routed ADHC_GLDINC_PRD.md v0.3 §4c (commit 28993c81c) for CVO cert — the periodic-oracle-revalidation addendum that grew out of my P1 cutover P0 (verdict 04e90056e). DESIGN-level cert (implementation re-certs at build, per CTO). No clock. Read the actual §4c text (PRD:247-278), not the routing summary.

## VERDICT: **ACCEPTED-CVO (design).** The §4c design is sound; my 3 criteria are correctly written in as the cert bar. 3 unknown-unknowns to fold into the build (none block the design accept).

## Criteria assessment (the bar CTO wrote into §4c:269-274)

- **(1) Independent of the served path — PASS.** §4c:269-271 mandates "recompute from source via the full-recompute oracle — never re-read the served artifact, never call the incremental entry." This is the exact inverse of the P1 trap (shadow:280 called the incremental entry). Correctly specified. The permanent retention of the `_full_scan()` oracle (§4c:265-267, amending §4.6 grace-window → permanent-at-cadence) is the necessary enabler — affirmed.
- **(2) Covers the schema-drift trap class — PASS as stated, with a binding implementation note.** §4c:271-272 ("validate the cache/state read+write round-trip, not just the final frame") correctly identifies that the DS traps (trade_date NaT-drop, transaction_id int/str over-dedup) live in the CACHE round-trip, not the final `daily` frame. **Implementation guidance for the re-cert:** a weekly full_scan-vs-windowed VALUE diff catches a drift only once it MANIFESTS, and a newly-appearing drift-partition can ship divergence for up to a full cadence interval (≤7 days) before the next weekly diff. To deliver criterion (2) at the right latency, implement it as a DAILY structural/dtype-fingerprint canary on the cache parquet (cheap — asserts the round-trip preserves the int-vs-str / datetime distinctions, no full_scan) PLUS the weekly value diff. Daily canary = catches dtype-drift the day a partition enters; weekly value diff = catches manifested divergence. Weekly-value-only leaves the blind window.
- **(3) Alarm on ABSENCE + divergence — PASS, strongest part.** §4c:272-274 requires egress-verified alarm on BOTH "didn't run" AND "diverged," explicitly citing the globgrph 0-subscriber-topic + bd-gold staleness class. This imports the absence-coverage lesson correctly — a verifier that silently stops or pages no one is the live-but-invisible failure. Exactly right.

## Mechanism soundness (independent read)
- Cadence design (§4c:261-263, weekly + every reconcile-trigger: injection-date / period-rebaseline / reassignment) — sound; coupling the event-triggered re-validation to reconcile events targets exactly when data-shape drift is most likely. ✓
- §8 close-gate fold (§4c:277-278, "no phase CLOSED until its post-cutover standing re-validation is live + alarmed") — this is the structural enforcement that prevents recurrence; makes the verifier a binding gate, not a recommendation. ✓ Strong.
- Ownership split (§4c:276-277, CVO design+cert / AE cadence-wiring / alarm on existing critical-surface egress) — clean lanes; reusing the critical-surface egress is right (don't build a parallel alert path). ✓
- Binds P1→P5 (§4c:260) not just P1 — the right generalization; the gap is structural to every incremental cutover, not a P1 accident. ✓

## What you should have asked but did not (unknown-unknowns — mandatory)

1. **[fold into criterion-2 build] The weekly-cadence blind window.** Covered above — a weekly value diff has a ≤7-day exposure for a non-reconcile-triggered drift-partition. The daily cheap structural canary closes it. This is the highest-value addition; without it, criterion (2) is satisfied on paper but the schema-drift class can still ship for a week.
2. **[AE + critical-surface] Who certs the re-validation's OWN liveness — watch-the-watcher.** §4c:273 requires an absence-alarm, but that alarm is itself removable (the globgrph incident was a monitoring path that EXISTED with 0 subscribers). The egress-verification must be RECURRING, not one-time-at-wiring — fold the re-validation's absence-alarm subscriber-presence into `comp-surface-check` / the critical-surface registry so a later subscriber-removal re-flags. Otherwise §4c recreates the exact globgrph class one level up.
3. **[CTO cost-model §7] Aggregate cadence cost across stacked phases.** By P5 there are 5 permanent full-recompute oracles each running weekly + on reconcile-triggers, on the cost-sensitive c6i.16xlarge runner. §7 currently models the one-time cutover cost; it should add the STANDING re-validation as a permanent recurring line item (and the schedule should stagger the per-phase weekly oracles so they don't collide / spike). P2 — not a design blocker, but the cost-model should not under-count the permanent verifier.

## Disposition
- §4c design: ACCEPTED-CVO. Fold the 3 unknown-unknowns into §4c (or carry to the build TO). The implementation re-cert (at build) will verify: the daily structural canary exists + is independent, the round-trip dtype assertion covers the int/str+datetime classes, and the absence+divergence alarm is egress-verified AND recurring-verified.
- This cert does not gate the 06-17 P1 close (separately handled by my independent full_scan-vs-served L4 hook).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Read (PRD §4c + section map) + git show --stat | design-text ground-truth (cert the authored §4c, not the routing summary) | ACCEPTED-CVO + 3 unknown-unknowns |

— 3.0.0_SA_CVO
