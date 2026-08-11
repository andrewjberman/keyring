# 49F GOLD ANALYTICS RUNNER -- GROUP W SPEC (WIRING: THE SCHEDULING/ORCHESTRATION ATOMS)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0745Z** · **archetype:** IMPLEMENT (design)
**Commission:** CTO 073811Z under the RATIFIED-TENTATIVE set -- ADVREVIEW F-2 ACCEPTED (CRO~A):
the sequence deferred scheduling to "runner wiring," and tonight's INF freeze is the measured cost
of shipping a shape without these atoms. **One page, deliberately: this is the page the INF
post-mortem says was missing.** Pre-build blocker: build decomposition does not open until W stands.

---

## 1. THE PER-LEG SCHEDULING TABLE (pack-01 A1-A5, declared per leg -- no leg undeclared)

| Leg | A1 write-cardinality | A2 date-label semantics | A3 trigger (floor + accelerator) | A4 re-delivery | A5 settle window |
|---|---|---|---|---|---|
| silver upstream (Schwab CRS conversion -- NOT this program's leg, its CONTRACT declared) | single/day per table | `date={D}` = statement close D (T-1 delivery) | AE-owned conversion flow | idempotent (skip converted, --force rewrites) | T-1 by construction |
| A-group dims | single/day | content as-of = the silver partition consumed | **FLOOR: clock, after the silver landing window; ACCELERATOR: silver completion event where one exists. An event-only trigger is PROHIBITED (the mdpf/INF Door-6 defect, twice-measured)** | overwrite-idempotent at `date={D}` | inherits T-1 |
| B-group canonicals | single/day | as-of = valuation date (statement close) | FLOOR: clock, sequenced after A (same dispatch, ordered stages -- one runtime per leg, atom 5) | overwrite-idempotent | T-1 |
| C-group engine | single/day (daily) + period artifacts on month-boundary crossings | as-of = r(t) date; periods labeled by period-end | FLOOR: same dispatch, after B | overwrite-idempotent; geometric re-link is deterministic replay | T-1; BD-class settle lags N/A (Schwab statement basis) |
| D emitters | per family, single/day | as-of in manifest; served key spelling per census | **FLOOR per family (D-group requirement -- the VALUES live here): default = the census's observed cadence per family, ruled at W review** | last-good re-serve on upstream refusal (serve stale-not-garbage; the REFUSE chain above guarantees stale is honest) | T-1 |

## 2. THE DISPATCH TOPOLOGY (single-homed by construction)

- **ONE dispatch path per runtime. The 49F runner has exactly one sanctioned entry** (the scheduled
  dispatch); ad-hoc QA runs use THE SAME entry with a QA flag (run-and-read; never production
  evidence). **A second entry path is a defect, not a convenience** -- the INF fifth-path
  collision (direct SSM, no env/no lock) is the type specimen.
- **DISPATCH-PATH CENSUS cell (the enumerate-then-close discipline):** at build, enumerate EVERY
  armed way the runner can start (EventBridge rules AND Scheduler schedules -- BOTH namespaces, the
  single-namespace sweep fails toward "no schedule exists" -- plus lambda invoke paths, SSM
  documents, cron entries); the census lands in W's manifest; all but the sanctioned path CLOSE
  before first production fire. The mutex (below) is sized against this MEASURED N, never assumed.
- **HOST MUTEX + MODE-SINGLE-HOMING:** one host-level lock per runner (the chain refuses to start
  under a live lock -- loud, never queued silently); run MODE (production/QA/backfill) resolves
  ONCE at dispatch and propagates via env to every stage (one-read-propagated; no stage re-derives
  mode -- the mode-incoherent-input class the INF guard correctly refused tonight).
- **Completion signal:** the runner's LAST act writes the completion manifest (atom 3) --
  **consumed as an ACCELERATOR only, never as any leg's ONLY trigger** (the completion-marker
  starvation class: mdpf went dark 11 days on a dead upstream sentinel).

## 3. THE FLOOR VALUES (proposed; ruled at W review)

Silver landing observed ~daily (AE flow, T-1). Proposed: **A+B+C on ONE dispatch, clock floor
daily 14:30Z** (after the observed silver window with margin; TUE-SAT following the statement
calendar -- exact hour tuned to the measured landing distribution at build, a RULED event on the
distribution per the B_03-class qualifier). **D emitters: per-family floors from the D_00 census's
observed cadences** (defaults land with the census; each floor is a value in W's manifest, ruled).
Backfill mode: same entry, explicit `--backfill` window, mutex-held, never scheduled.

## 4. ACCEPTANCE

- Every leg has all five A1-A5 cells declared (a blank cell fails the spec gate -- "undeclared" is
  the defect class this page exists to kill).
- The dispatch census prints its denominator (paths found / paths closed / the one sanctioned).
- Mutex exercised: a second concurrent dispatch REFUSES LOUD (the control that fails).
- Event-only trigger grep over the built wiring: zero legs whose only trigger is another
  pipeline's success (the CLAUDE.md defect class, mechanically checked).
- Mode propagation: a QA-flagged dispatch reaches every stage as QA (one poisoned-env mutant).

-- 3.0.0_SA_CVO
