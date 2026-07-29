# SPEC: comp-legacywriter — the writer-contest lens (INFRASTRUCTURE.TOOLS)

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~16:30Z · **archetype:** IMPLEMENT(spec-only)
**Andrew-direct premise (my terminal, ~16:25Z):** legacy writers clobbering artifacts in
multi-stage pipelines is *"a recurring footgun that wastes hours and hours of time and system
confidence... hellish to debug and clean."* Wanted: trace the serving path from ingestion, census
WHAT WRITES at each level, then dossier each writer (age, commits, background) so
correct-vs-contested is assessable and decommission is streamlined.
**Live case study:** tonight's zombie hunt (CTO terminal) — static scans MISSED the MDPF writers
(dynamic key construction), `comp-clobber --live` cleared platinum (4 versions, 0 interleave) and
convicted the legacy `json/mdpf/*` plane (12 versions, 11 etags, INTERLEAVED — textbook two-writer
signature). Hours of ad-hoc composition that this tool makes one invocation.

## Design center: this is a JOIN of five existing instruments, not a new scanner

`comp-legacywriter <artifact-or-pipeline>` =
`pipescript` (path) × static-scan (declared-blind) × `comp-aws`/simulate (capability) ×
`comp-clobber --live` (observed) × `comp-heat`+git (dossier). The value is the JOIN + the verdict
table; every primitive already exists. Estimated build: wiring + output, not new detection.

## Phase 0 — SUBSTRATE COVERAGE PRECONDITION (added post-verification, Andrew's challenge)

**Measured 2026-07-29:** `pipescript` (the named-thread traversal — distinct tool from
`comp-pipescript`, both verified on disk) HAS an mdpf thread with full path schema
(trigger→runner→feeders→served→frontend, DDB included) — **but its data is a resolver SNAPSHOT
frozen 2026-06-15 (44d), and its own banner names the exhibit: the mdpf platinum key.** It serves
the underscore TWIN as "the primary served rollup, LIVE fresh" and lists a retired
freshness-checker as a producer. **A stale estate map actively DEFENDS zombies — it is a
legacy-writer preservation mechanism.** Therefore: the tool REFUSES to run (rc=2) if its path
substrate fails a freshness check — comp-kuzu provenance header must read CURRENT; the resolver
snapshot is legal only as the NAMING layer, never for load-bearing keys. `comp-clobber` coverage
is versioning-dependent: declared per-target (versioned buckets covered; DDB + unversioned =
UNVERIFIABLE-BY-THIS-INSTRUMENT).

## Phase 1 — PATH RESOLUTION (comp-kuzu canonical + pipescript thread naming)

Input: a served artifact (bucket/key or prefix) or a pipeline name. Walk the serving path BACKWARD
from serve → platinum → gold → silver → bronze via the **auto-refreshing canonical graph
(comp-kuzu, HEAD-advance refresh)** — pipescript's thread definitions supply the human names, the
graph supplies the live keys. Enumerate every LOCATION (stage output: S3 key/prefix, DDB table) on
the path. Output: the ordered location list — **each location is a potential clobber site;
multi-stage is why single-key tools miss the war.**

## Phase 2 — WRITER CENSUS per location, THREE INDEPENDENT AXES (the case study is the proof no
single axis suffices)

| axis | instrument | what it finds | DECLARED blindness (printed, per O2) |
|---|---|---|---|
| STATIC | repo scan for key-writers | code that names the key | dynamic construction → emit `UNRESOLVED-WRITER(file)`, never absent (the comp-iam silence law); deployed≠repo divergence |
| CAPABILITY | comp-aws / `simulate-principal-policy` (one resource per call) | every principal that CAN PutObject there | capability ≠ activity; a grant may be required-and-unobserved |
| OBSERVED | `comp-clobber --live` (S3 versions/ETags/interleave) + provenance stamps (`written_by`) where present + CloudTrail data events WHERE ENABLED | who actually wrote, when, contested or sequential | S3 versions don't record the principal; DDB has no version history (declare UNVERIFIABLE-BY-THIS-INSTRUMENT); pre-versioning history invisible |

Interleave classification from observed axis: **SOLE / SEQUENTIAL-HANDOFF (old writer stopped,
new started — healthy migration) / INTERLEAVED (live contest — the textbook signature) /
DORMANT-ZOMBIE (writer's trigger ENABLED but no recent writes)**.

## Phase 3 — WRITER DOSSIERS (the "comp-heat or other analysis" ask)

Per identified writer: **trigger** (comp-trigger, BOTH systems — Rules AND Scheduler, the
list-rules blindness is banked) + schedule state ENABLED/absent · **deploy identity** (deployed
md5 vs HEAD — which vintage actually runs) · **git background** (last N commits touching it,
authors, the commit that made it legacy if any) · **heat/age** (comp-heat recency) · **owner
lane** (PIPELINE_MAP / source-map / EC2_MANIFEST row) · **ledger mentions** (RETIRECOND retires:
entries, teardown-wave orders naming it). Classification: **CANONICAL-CANDIDATE / LEGACY
(superseded, retirement ordered or due) / ZOMBIE (trigger live, no sanctioned reader) /
DIAGNOSTIC (ad-hoc, unscheduled) / UNRESOLVED**.

## Phase 3b — THE EXERCISE COLUMN (folded per Andrew ~1655Z, from CTO base's 164909Z
never-exercised-write-path concept + my 165039Z judgment)

Every writer dossier carries an **EXERCISE VINTAGE**: first/last successful REAL write **since the
writer's last MATERIAL CHANGE** (code deploy, role/grant change, target re-point, trigger change —
a config change invalidates prior exercise evidence; the accrual bridge is the motivating incident:
"validated" by a dry-run, first-ever PutObject was its production fire, AccessDenied). Verdict is
**THREE-VALUED, hard requirement:**
- `EXERCISED` — positive evidence of ≥1 real completed write (run-log success line, provenance
  `written_by` stamp, or a new version in a single-writer location post-change), basis stated;
- `NEVER` — positive evidence of zero (complete run history holding only dry-runs/crashes, or the
  full declared write set showing no attributable version);
- `UNDETERMINABLE` — no instrument covers the path. **Absence of instrument is never evidence;
  rotated logs must read UNDETERMINABLE, not NEVER** — that distinction is what keeps the column
  honest.
Writers whose next SCHEDULED fire would be their first exercise get the flag + the date
(comp-trigger, both systems). **Entry point `--never-exercised`** runs just this column over the
declared-producer denominator (the three C-3 registries — never "all write sinks").
**A dry-run validates planning; it cannot validate permission. A green half is not a green whole.**

## Phase 4 — VERDICT TABLE + the decommission hand-off (the streamlining)

Per location: writer set + contest class + per-writer classification + **the recommended
disposition WITH ITS EVIDENCE BAR PRE-FILLED IN RETIRECOND FORM** — the tool emits ready-to-paste
`retires:` ledger entries (`what/kind/evidence_bar`, kind per the write|trigger|grant|object|route
enum + mechanism-not-storage rule). The decommission wave then starts from a machine-generated,
evidence-bearing kill list instead of a hunt. **The tool RECOMMENDS; the kill rides the owner's
lane + never-widen + the deploy ledger** (verifier/anti-clobber discipline unchanged).

## Output contract (O2-compliant from birth)

Denominator + page-1 shape per the head-truncation brief: every phase prints examined-N-of-M and
its axis blindness; `rc=2` on failed retrieval (empty path resolution, unreadable bucket) per the
comp-grep convention. NOT an alarm, NOT scheduled — an on-demand lens (moratorium-compatible; if
someone later wants it periodic, that is a separate Andrew-ask).

**READER LINE (added on the 165112Z incident):** the verdict table also lists KNOWN READERS per
location — producer-readers via comp-dataflow `origin` (SERVED-ORIGIN flags) + portal consumers via
the portal census — with the population of each reader axis STATED. Motivating incident, same hour:
`json/mdpf/*` was reported "no live consumer" from a PORTAL-scoped census while a gold producer
imported it as a value source (committed code, `dim_mdpf_aggregate_aua_timeseries.py:558-571`) —
its teardown is now blocked on a re-point, found only because one comp-dataflow origin call ran.
**Suppression without reader removal is the same defect as suppression without writer removal, one
direction over. A null is only as general as the population enumerated — the table names each
axis's population.**

## Acceptance battery (stated before build)

1. **The case-study regression:** pointed at `platinum/mdpf/cottonwood/aggregate-aua-timeseries`,
   must find the publisher as sole current writer (SEQUENTIAL states), the dispatch Stage-4 twin
   as a DISTINCT key's writer, and classify `json/mdpf/*` INTERLEAVED with two identified writers
   — reproducing tonight's multi-hour hunt in one invocation.
2. **Dynamic-construction control:** a writer with a constructed key must surface as
   `UNRESOLVED-WRITER(file)`, never silently absent (positive control: a static-keyed writer in
   the same run resolves).
3. **Two-trigger-system control:** a Scheduler-driven writer and a Rules-driven writer in one
   report, both with trigger identity (the 15:45Z two-driver minute is the live fixture).
4. **Negative control:** a single-writer healthy location reports SOLE with zero contest — the
   tool must be able to say "nothing wrong here" with its denominator, not manufacture findings.
5. **Exercise-column controls (Phase 3b):** a known-exercised path reads EXERCISED with its
   evidence cited (positive control); a fresh-deployed never-run fixture reads NEVER; **a path
   whose run logs are deliberately hidden reads UNDETERMINABLE, not NEVER** — the control that
   keeps the instrument honest.
6. **Reader-line control:** pointed at `json/mdpf/*`, the table must surface the
   `dim_mdpf_aggregate_aua_timeseries.py:567` producer-read (the consumer a portal-scoped census
   structurally missed).

## Routing

Rail-tool lane (0.8.0 when live / CTO's T-1 re-route decision governs). Sequenced AFTER the rc
flip + tonight's wave (one rail change at a time). Register in the manifest at birth
(comp-manifest-check registration invariant). CVO recuses from build; this spec + the acceptance
battery is the verification contract I will certify against.

— 3.0.0_SA_CVO
