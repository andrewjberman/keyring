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

## Phase 1 — PATH RESOLUTION (reuse pipescript/graph)

Input: a served artifact (bucket/key or prefix) or a pipeline name. Walk the serving path BACKWARD
from serve → platinum → gold → silver → bronze, enumerating every LOCATION (stage output: S3
key/prefix, DDB table) on the path. Output: the ordered location list — **each location is a
potential clobber site; multi-stage is why single-key tools miss the war.**

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

## Routing

Rail-tool lane (0.8.0 when live / CTO's T-1 re-route decision governs). Sequenced AFTER the rc
flip + tonight's wave (one rail change at a time). Register in the manifest at birth
(comp-manifest-check registration invariant). CVO recuses from build; this spec + the acceptance
battery is the verification contract I will certify against.

— 3.0.0_SA_CVO
