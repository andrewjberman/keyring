# SSOT RECON MATRIX — the CTO oversight tracker (Andrew-direct mandate @3c8418e34b)

**Owner:** 1.0.0_SA_CTO · opened 2026-08-11 ~0540Z · updated on every recon delivery/cert event.
**Purpose:** ONE place that says, per pipeline × pattern-leg, what is GROUNDED, who holds it, and
what remains — so the design/implementation phases start from an adversarially-established SSOT,
never from records (6 of 10 records were FALSE on the last measured run — the catalog is not
trusted; only certified ground truth enters this matrix as DONE).

## THE STATE MACHINE PER CELL

`OPEN` → `HELD(seat)` → `DELIVERED(@commit)` → `CERTIFIED(CVO verdict)` — only CERTIFIED cells
feed the cutover/design phases that touch live serving. (Non-serving design work may proceed on
DELIVERED with the cert noted pending.)

## THE SIX PATTERN LEGS (Andrew verbatim ~0535Z; grounding question per leg)

| leg | the pattern says | the recon must ground |
|---|---|---|
| L1 ingestion | vendor endpoint → `opal-data-assets/{vendor}/{firm}/bronze` | what lands, from which endpoint, on what trigger; raw-untouched conformance (Rule 17a) |
| L2 bronze→silver | an EVENT TRIGGER processes raw → silver parquets | does the trigger exist; event or cron; what fires it; silver = dedup/dtype only (Rule 17) |
| L3 silver | parquet queryable | schemas, partitions, freshness basis, provenance cols |
| L4 gold | `portal/gold/{product}/{scope}` — code + tables + ALL deps COLOCATED | colocation delta (what still lives outside the root); derivation legitimacy (atom-8 three-bucket) |
| L5 publish | a publisher pulls gold → `platinum/{product}/{scope}` | ONE publisher per product; spelling law; schedule floor |
| L6 portal read | FE reads platinum | what the deployed FE ACTUALLY reads (not what docs say) |

## THE MATRIX (state as of 0540Z — updated in place)

| pipeline × product | L1 | L2 | L3 | L4 | L5 | L6 | held by / record |
|---|---|---|---|---|---|---|---|
| **mdpf (product-global + per-firm)** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | **CERTIFIED** | CRO base @41692cd3d2; **CVO CERTIFIED @cc62267d89 055116Z, ZERO refused cells — CUTOVER GATE RELEASED.** Riders (neither holds cert): act-(ii) precondition DISCHARGED 0615Z — producer = mdpf-gold-lambda in-process (TWO-runtime atom-5 violation found; **Andrew RULED ~0615Z @727c2df067: the LAMBDA survives**; chain Stage 3 = disable-after-verified-fed; X-ii = re-base the lambda leg's inputs onto the canonical plane — AE's 3-co-factor zeros mechanism MEASURED: exact-date-only reads × chain-written feeds dark × the now-RETIRED vacuous-PASS carve-out; zeros-with-PASS structurally closed; 13:30Z expected = serve green + loud A7 ERROR no-write, escalation not fired). Remediation-register line "consolidator carry-forward on stale staging inputs" stands at COO (row 13). CVO correction: mdpf-scheduled-floor IS live (SCHEDULER namespace) but targets the CONSOLIDATOR — delta row 4 stands: nothing clocks the EC2 chain |
| **advi × 49F/bd (08335338)** | HELD(CRO~A) | OPEN | HELD(CRO~A) | HELD(CRO~A) — the ARCHETYPE decomp, Andrew instruction 3 | OPEN | OPEN | archetype spec forthcoming; endpoint catalog + PATH_DISCOVERY exist |
| **advi × inf** | PARTIAL — endpoint catalog + 03 audit | PARTIAL — stop-mechanism record grounds the chain trigger | PARTIAL — silver dims read (TWR dim) | **CERTIFIED-WITH-ONE-REFUSAL @08215b39a3** — three-bucket map certified; REFUSED: "TWR dim read NOWHERE" (D_00c/D_02/D_04 have read it since 04-28; precise form: **C_02, producer of served growth, reads it nowhere**). **W-B reshapes: RE-POINT of served growth + DEDUP of a 3-reader fan-out, not first introduction; coherence question (any surface serving vendor TWR beside residual growth simultaneously?) answers BEFORE W-B's acceptance bar freezes — one rendered-payload read per surface. W-0 lands the membership predicate (49 files vs "~44 chain")** | OPEN | OPEN | CRO~A: 01/02/03 records; ~A amends the 03 clause per write-out-never-silently-fix. **Ch.01 stop-mechanism CERTIFIED @1c6068a0a7 zero refusals (restore recounted exact from the live object; effectiveness PENDING-EXERCISE, folds with the CPR-4 serve delta-cert at the 13:47Z fire — one read, two folds). Unknown-unknown routed: INF-runner DISPATCH-PATH CENSUS (5 armed start paths) = R-a mutex's named precondition (enumerate-then-close before sizing). Coverage gap closed 0625Z; CPR-4 verdict = SPLIT @e6e0fe85c6 (steps 1-3 CERTIFIED byte-exact; SERVE OUTCOME WITHHELD — served platinum still 07-31 vintage, step 4 unexecuted). Step-4 trigger RULED: the production 13:47Z cycle's D-chain serve, never an ad-hoc republish; DS ticks ledger with trigger+owner; residual STAYS TRANSITIONAL, §3 amendment HELD until CVO's delta-cert of the flipped surface; first unreconciled_aua may be legitimately NEGATIVE (retired clamp's hidden debt). 01 stop-mechanism cert pass running.** |
| **advi × cot** | **LIVE-UNMAPPED** (3rd inversion on this cell, @314689f20a: the Rebalancer ingest EXISTS LIVE — bronze `rebalancer_*` daily 06:00Z; goal 1 = EXTENSION of a live puller, not a build; Andrew ~0547Z correction @a4d5147211 named the source, the at-rest measurement found the pipeline) | OPEN | **LIVE-UNMAPPED** — silver `fact_model_*` incl. account-grain `fact_model_assignment` (921 accounts) + gold `dim_model_portfolio`, completion markers daily to 08-10; PLUS custody inversion record @562cbd444d | OPEN | OPEN | OPEN | **RECON-5 — UNHELD** (5a endpoint inventory rides RCN-0001; 5b after archetype stabilizes); cot goal-3 collapses to spine-overlap measurement, same shape as the other firms; CVO flagged for delta-cert |
| **cross-cutting** | **RECON-4 FULLY CLOSED at CVO** (base @4918e8b48f + delta @da62a742c5 + delta-4 @fca75880f7: the INF 11 unmatched were DESIGNED $0 portfolio stubs — real-account join **550/550 = 100.0%**, $144.9M matched, zero AUA unjoined; grain-labeled figures 98.0% raw-row / 100.0% real-account; CVO's leak hypothesis self-superseded in a dated addendum). **DELTA-CERT @da62a742c5**: cot ingest-live confirmed 3 tiers; 49F TRUE END-TO-END = **99.65%** (7,205/7,230 — the 99.8% was the map-side leg only; 25 feed allocations reach no spine account, the build TO carries that denominator). **JOIN-TO TRAP (CVO hit it live): the map's column NAMED account_id is a SmartX UUID; the digits live in account_number — TO names the pair explicitly (allocation_id→account_number→zfill(10))**; map-universe==feed-universe invariance = one puller source read before the join serves. **GOAL-3 MEASUREMENT SET COMPLETE-MEASURED @579d7020da** — three firms, THREE identity mechanisms: INF native-key 98.0% · 49F one-hop-map 99.8% · cot INTERMEDIARY-REQUIRED (structured 0.0% at every form — different numbering systems; candidates unchased pending RECON-5a: rebalancer_accounts bronze at rest / custody Relationship×Account / BD account-detail). No uniform join design exists and the recon says so with per-firm denominators BEFORE the build. +census finding: ~100 prose-length values inside cot's account_number key column (content contamination → 2a field registry). **RECON-4 CERTIFIED @4918e8b48f** (3/3 load-bearing cells recomputed exact; reverse crosswalk DISPROVED by measurement so identity-acquisition hardens — the map-table join is the only path; INF's 11 unmatched = a perfect len-12-14 format partition, namespace leak not attrition; ONE refused item: run-census metadata drift 20/2/2-vs-21/1/2 — CRO regenerates, writer derives census from cells) — was DELIVERED @be316d868c: goal-3 join = THREE problems — 49F/bd 0.0% (identity-acquisition: feed account_id IS the SmartX allocationId, custodian hardcoded None; the allocation→custodian-account question rides ~A's RECON-2 under the standing SMARTX lift) · INF 98.0% joinable today (prototype the overlay here) · COT no model-holdings feed (goal 3 runs THROUGH goal 1 — a measured dependency edge) · RECON-6 **HELD(CRO base)** (the ~B spawn ask was retracted pre-spawn — premise false once RECON-4 delivered; RECON-5a queued behind it, same seat) · 49F identity question ANSWERED AT REST (no egress needed): `smartx/platform/silver/fact_allocation_account_map` allocation_id→8-digit account_number, 7,262 rows daily; residual = key-form test (8- vs 10-digit), ~A running; double name-vs-content specimen banked for the 2a field registry · ~~exception set~~ ~~pattern ratification~~ **BOTH RATIFIED ~0542Z @d272021791** | | | | | | |

**L1 KEY-ANNOTATION RULE (0546Z, from the measured three-family collision):** advi×49F/bd and
advi×cot L1 cells land under ONE shared vendor prefix (`opal-data-assets/blackdiamond/{49f,cottonwood}`).
Every L1 count carries the census KEY it was taken with.
**OPEN CHECK — COMMIT-GATE HALF MEASURED 0556Z: the gate is BLIND to the shared-prefix shape.**
`ds-precommit-check.py:61-64` matches FOREIGN BUCKET NAMES only (`data/cot/`→{opal-data-bd,
opal-data-inf}; `data/black_diamond/`→{opal-data-cot}) — `opal-data-assets` is in neither tuple
and key prefixes below a bucket are never inspected, so a `data/black_diamond/` script reading
`opal-data-assets/blackdiamond/cottonwood/*` passes the commit gate TODAY. (comp-firmsep-sweep is
credential-plane — wrong axis for this check.) **GATE CANDIDATE (proposed to Andrew, NOT
implemented — widening a deny needs his word): extend `_CROSS_FIRM_FOREIGN_BUCKETS` to
foreign-KEY-PREFIX tuples.** IAM half still unmeasured: one `simulate-principal-policy` per runner
role against an exact cottonwood key, isolated positive control beside it.

## THE QUALITY PARTITION (Andrew-direct instruction 4, ~0552Z via CRO~A record + MSTR relay)

**The recon's PRODUCT is a partition, not just a map: every script/engine/subsystem in the census
lands in EXACTLY ONE side — EXTRACT (quality structure, carried into the canonical build) or
DISCARD (patchy/fragile/methodologically unacceptable) — with grounded evidence per item.** Type
specimen (sovereign-confirmed, independently the audit's ILLEGITIMATELY-DERIVED #1):
transaction-engine holdings valuation → DISCARD. This binds ALL recon chapters' deliverable form;
L4 cells carry a `partition:` field from here forward. Existing certified cells are not reopened —
the partition field back-fills on each chapter's next touch.

**Axis form (CTO ruling 0555Z, Rule-24 two-field remedy):** `partition: EXTRACT|DISCARD` (binary,
exactly-one-side) + `discard_reason: patchy|fragile|methodologically-unacceptable` (discard side
only). Never three coordinate values on the partition axis.
**Census UNIT (CTO-ruled 0559Z adopting CRO's leaf-grain form, closing COO's postulate-(ii)
catch — the units "script/engine/subsystem" NEST): THE PARTITION IS LEAF-GRAIN ONLY.** Every
census header DECLARES its leaf unit; EXTRACT|DISCARD attaches to LEAVES and nothing else; any
parent aggregate (engine/subsystem/service) carries a **DERIVED SUMMARY** (n_extract/n_discard +
the discard leaves enumerated), **never a partition value of its own** — binary-exactly-one-side
holds by construction, and two censuses can only disagree at declared leaves. Declared leaves:
RECON-6 = ENDPOINT FAMILY per vendor · code censuses (RECON-2/3/5b) = SCRIPT-LEVEL DERIVATION
CAPABILITY (the type specimen — transaction-engine holdings valuation — IS such a leaf; the
engine gets a summary).

## ADVERSARIAL DISCIPLINE (the mandate's word: "adversarially establish SSOT")

1. **CVO cross-examines every recon deliverable** — independent re-derivation of load-bearing
   cells against LIVE state, never the artifact's own citations (Rule 22a). A cert that only reads
   the artifact is a rubber stamp and is refused as a cert.
2. **Believed-vs-actual is the required shape** — every recon delivery carries the delta table
   (the @41692cd3d2 form); a delivery with no belief-inversions found must say so explicitly and
   show the records it checked.
3. **Marked holes over silent coverage** — UNREVIEWED/UNMEASURED cells are stated with the exact
   call that would fill them (the truth-JSON convention).
4. **Instruments are suspects too** — comp-pipescript layer blindness + comp-estate stale-snapshot
   404s are OPEN CTO fixes; until landed, any matrix cell resting on those tools carries a caveat.
   Banked from the mdpf cert (CVO, live): **schedule-existence questions MUST sweep BOTH
   EventBridge namespaces** (`events list-rules` AND `scheduler list-schedules`) — a
   single-namespace sweep returns a clean, complete-looking absence, which is the deletion-warrant
   direction. Method line routed to ~A (scheduling-axes/tool-adapters).
   Banked 0602Z (CRO + my own run, independent): **a TIMEOUT-BACKGROUNDED Bash task's output file
   is not a complete render** — comp-pipescript's "1-of-6-layers" observation reproduces only under
   that harness shape (CRO: 13 lines via task-file read; my clean `> file` redirect run: 59 rows,
   6/6 layers healthy). For any long-running tool, redirect to an explicit file; never quote a
   timeout-backgrounded task file's contents as the tool's full output. One deliberate repro of the
   harness shape pends before any tool patch; DS's triple-homed rendering gap is the one
   confirmed-live TOOL defect.

## RULED DESIGN CONSTRAINTS (0617Z, from the night's three name-vs-content specimens + the universe finding)

- **THE SINGLE-HOMING LAW — four instances in one night, one principle: DECLARE THE FAN-OUT ONCE,
  AT THE CONVERGENCE POINT.** (1) producers: two runtimes on one key → Andrew ruled the lambda
  @727c2df067; (2) scope predicates: map/feed universes aligned by coincidence → single-homed
  predicate; (3) dispatch modes: five caller-local mode carriers → on-host resolution + mutex;
  (4) deploy targets: cot_bronze_ingest ONE source, TWO targets, ONE served leg → sanctioned
  second-target declaration in safe_deploy_core (the bd-side Model-B copy froze 08-04 while
  executing daily for 49F — the placement is SANCTIONED design, the missing redeploy leg was the
  defect; my "unsanctioned mirror" ruling CORRECTED 0630Z on AE's consumer read — search-FOR-the-
  path was the only reason the consumer surfaced; the delete never fired because the ruling itself
  blocked on that read).
- **SCOPE PREDICATES ARE SINGLE-HOMED (ruled (a), @dd93cad9a2 finding):** two independently-mutable
  scope definitions that happen to agree = two runtimes on one key, one layer up. Every consumer
  derives from ONE declared universe predicate. The 49F map/feed alignment (coincidence today)
  becomes an invariant by construction — a NAMED ROW in the join build TO; serve is preconditioned
  on it; build is not. Not a monitor (moratorium, and its stated reason).
- **A BUILD TO CARRIES THE FULL-PATH DENOMINATOR, never a leg's** (the 99.8-leg vs 99.65-path
  correction, COO self-caught @ad93eaa14d).
- **The 2a FIELD REGISTRY keys on (table, column, measured content-grade), NEVER column name alone**
  (three specimens in one night: "bd" family collision · `account_number` clean-in-smartx vs
  prose-contaminated-in-cot · `account_id` carrying a SmartX UUID). A name is a label to be
  verified, not an identity.

## STAGED POST-RECON DELIVERABLES (Andrew-direct via MSTR @f73ad4d22a, LD-0393 — TRIGGER IS HIS
TIMING WORD, not a dispatch; routing CTO/COO at trigger)

Once recon is done and certified ("really sure of themselves"): THREE /artifact-design builds —
(1) **mdpf FINAL structure**, vendors → opal-data-assets → portal-v2 serving, EXHAUSTIVE (every
lambda, trigger, bronze→silver event trigger, code pull, dependency); (2) **advi**, same form,
ingestion→serving; (3) **the 49F archetypal gold runner** — scripts in order + WHAT CHANGES under
the raw-figures ethos. All three express the ratified pattern spec verbatim. PRE-TRIGGER item
already routed: Schwab performance-focused fact table + attribution shape → CRO~A RECON-2 input
(custodian-native performance = the rawest archetype leg, per "performance is not a residual").

## OPEN ROUTING (CTO oversight queue)

- RECON-5 (cot advi) seat assignment — with COO (5a can ride RCN-0001 now).
- RECON-6 (endpoint-delta census) seat — fronts atom-8 conformance testing.
- comp-estate snapshot staleness fix + comp-pipescript denominator fix — CTO, in progress.
- L5/L6 columns for advi (publisher + portal read) — likely ONE sweep across all three firms once
  the archetype's L4 shape stabilizes; sequencing with COO.
