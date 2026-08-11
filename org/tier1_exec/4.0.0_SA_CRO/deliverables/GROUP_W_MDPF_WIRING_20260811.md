# GROUP W (mdpf) -- THE SCHEDULING-ATOM WIRING PAGE FOR THE TARGET FORM

**Author:** 4.0.0_SA_CRO · **2026-08-11 ~0756Z** · **archetype:** IMPLEMENT (design)
**Commission:** the refactor spec's P0 act ("Group-W instantiation for mdpf"), executed on Andrew's
"Option A, proceed" (~0754Z). This is ~A's F-2 remedy applied to the mdpf target form: **pack 01's
five atoms declared per leg BEFORE build decomposition** -- the one page the INF nine-day freeze
post-mortem says was missing. Atoms sourced from RECON-1's measured A4 table (@41692cd3d2,
CERTIFIED) + the ruled clocks (RP-W3) + the target-form contracts; nothing invented.
**One law binds every row: an EVENT ACCELERATES, a CLOCK FLOORS. No leg's ONLY trigger may be
another pipeline's success** (the measured 9-day freeze class, twice tonight).

| Leg (target form) | A1 write-card. | A2 date-label | A3 trigger predicate | A4 re-delivery | A5 settle | Floor + dispatch path |
|---|---|---|---|---|---|---|
| **L1 vendor pulls -> bronze** (smartx/orion/eclipse/schwab/BD per firm) | single/day per key | content as-of where the vendor carries it; run-date otherwise (declared per vendor) | per-vendor clock (e.g. 03:30Z TUE-SAT smartx crons; 06:00Z BD rebalancer -- both measured live) | idempotent skip on existing key | **vendor-owned, measured-not-fixed** (BD custody >=2d measured; schwab unmeasured-marked) | the pull cron IS the floor; dispatch = the puller's own schedule, never a sentinel |
| **L2 bronze -> silver** (per vendor/firm) | single/day per table | partition date = bronze delivery's as-of | **S3 ObjectCreated on the bronze landing (ratified law)** | converter idempotent (etag-skip, measured pattern in cot silver) | inherits L1's A5 | **floor: a daily catch-up clock sweeps unconverted bronze partitions** (event lost != day lost); dispatch = Lambda per vendor family |
| **L3 gold builders -> portal/gold/mdpf/{scope}/{table} parquet** | single/day per (scope,table,date); version-guard refuses downgrades (ported from :1315) | data-as-of derived from silver content, never the run clock | **events off silver landings ACCELERATE; the RP-W3 ruled clock FLOORS (pulls 13:02Z, floor 13:30Z)** | put-with-readback + version-guard (consolidator semantics ported) | n/a | floor 13:30Z; dispatch-path CENSUS row required per builder (the CVO cell): every route that can invoke the builder, enumerated -- no untraced second path |
| **L4 platinum publisher -> opal-data-portal-v2/platinum/mdpf/{scope}/*.json** | daily per family; ONLY JSON producer | as-of carried in manifest | gold-completion event accelerates; **13:50Z clock floors (measured live cadence)** | re-serve-last-good (measured) | n/a | one publisher, one schedule, hyphen spelling at THIS boundary only |
| **Serving bells (per-firm account-distribution successor)** | daily per firm | latest-as-of | publisher leg (folds into L4 when the park lifts -- PARKED-INHERITED until Andrew's word) | overwrite | n/a | 11:30Z legacy cadence noted; successor rides L4's floor |
| **Sunday/weekend semantics** | no-op days produce NO new date keys (trading calendar resolves first -- T-1 law) | -- | floors skip non-trading days via lib/trading_calendar.py (the ONE frontier definition) | -- | -- | never a Sunday rebuild without declared union-preserve semantics (the INF lesson) |

**MODE-HOMING + HOST-MUTEX rows (CTO's ruled remedy class, carried):** every builder declares its
runtime home (Lambda vs runner) and a single-mode invariant -- the same code must not run from two
homes in one window; the dispatch-path census is the check.

**WHAT DIES WITH THE LEGACY WIRING, restated from the spec's M-rows:** the INF pipeline-complete
sentinel as mdpf's ONLY trigger (M3 -- the dead-sentinel class), the OnSuccess-only smartx
deviation, the partner_roster-in-code read (M4), and the untraced 08-06 manual-fire path (RECON-1's
UNTRACED cell) -- the dispatch census makes that class visible by construction.

**Acceptance for this page (COO decomposition consumes it):** every builder/publisher TO cites its
row here; a leg with no row does not decompose; changes to any A3/floor cell re-run the composition
law's four sentences against adjacent legs (pack 01).
