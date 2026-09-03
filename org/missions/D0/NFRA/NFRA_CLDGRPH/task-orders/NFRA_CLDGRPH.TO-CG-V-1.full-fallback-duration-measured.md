# TO NFRA_CLDGRPH.TO-CG-V-1 -- the FULL-FALLBACK DURATION of the KuzuDB projection, MEASURED: two full loads and one incremental run of the existing engine, on a stated runtime, with input sizes and peak memory; the four existing figures reconciled AFTER the measurement, never before; no runtime is chosen here

<to_id>NFRA_CLDGRPH.TO-CG-V-1</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.7.0_AE_CloudOps~Q</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut (2026-09-03 ~06:3xZ). ROUND 1 of NFRA_CLDGRPH, the first task order under this project. Authority: Andrew-direct at the 1.0.0_SA_CTO~A terminal ~05:1xZ (@8e134cc126: the second, parallel canonical run) + his ruling (a) ~06:1xZ at both lane terminals (@858fc08951: 2.0.0_SA_COO~A spawns Tier-2 workers at L6). The assignee commits its own status flip (task-orders/** is lane ANY @f9c97a52ce) after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `../prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (s.6 R5: the worker's runtime is decided by the MEASURED full-fallback duration, never the document claim; s.7 row S10) · **Decomp cell:** `CG-s-10` (`../decompositions/NFRA_CLDGRPH_DECOMP.md` v0.1 @`994c9381d0`, s.1a; ROUND 1 "measure first") · **Lane:** the deliverable at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/` (owner by path); NO repo source is edited by this task order. **Rule 27 seating:** `0.7.0_AE_CloudOps~Q` is a FRESH lane letter seated for NFRA_CLDGRPH only (pre-flight at cut: no process, no marker, not registered, 0 corpus hits, no open task order). The lane's agent folder `org/tier2_senior/0.7.0_AE_CloudOps~Q/` does not exist yet; the base folder's README + prompt apply; create the lane folder for your logs.

---

## THE CELL -- what is unmeasured and why nobody may pick a number

The projection worker (S2) will run the existing incremental engine and fall back to a FULL load on a large delta (R5). Whether that worker is a Lambda or an ECS task is decided by how long the full load takes and how much memory it needs -- and today **four figures from three sources exist for what are actually two different operations** (the full load and the incremental refresh), and `4.0.0_SA_CRO` refused to reconcile them because picking one manufactures a measurement (brief @`dfd24a010b`; PRD s.7 S10; decomp CG-s-10). This task order MEASURES. It does not choose a runtime: that is CG-s-2's port decision, informed by this number.

## DELIVERABLE -- one measurement file, the T-16 shape where its fields apply

`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/CG-s-10.full-fallback-duration.result.md`, one fenced JSON block + prose:

1. **IDENTIFY the two operations at `file:line @ commit`** (comp-read first): the FULL load path (`infra/aws/globgrph/kuzu_nessie_load.py`, 417 @`e445642c5f`), the incremental path and its full-fallback trigger (`infra/aws/globgrph/kuzu_incremental_refresh.py`, 350 @`aebe0d0a67`: the count-guard and the delta threshold that flips to full), and the local orchestrator that wraps them (`infra/aws/globgrph/_canonical.py` `ensure_fresh`, 746 @`173dd335f4`). State which of the two a "projection rebuild" means in each carrier you later reconcile.
2. **MEASURE the FULL load TWICE** against the CURRENT Nessie/Iceberg warehouse into a TEMP database path (never the canonical `kuzu_nessie_db`, never under `_canonical.py`'s mkdir mutex, never touching the live local copy that other seats are reading): wall clock, peak resident memory, and the instrument for each (e.g. a `resource`/`psutil` read around the call, or the OS's own timer), the INPUT SIZES (node and edge row counts per table, Iceberg bytes read, the branch-head marker's `committed_at` at run time), the ENVIRONMENT (machine, CPU, python version, network path to S3), and the variance between the two runs. A single run is not a measurement.
3. **MEASURE the INCREMENTAL path ONCE on a real delta** (the marker has stamped 45 times in a 24 h window, so a real delta exists): the same fields, plus the delta size (rows applied) and whether the count-guard fired. This is the second of the two operations the four figures conflate; label it as such.
4. **THE FIT TABLE, as a FINDING and not a decision:** each measured figure beside the Lambda ceilings (900 s timeout, 10,240 MB memory, 10 GB ephemeral storage) and beside the ECS one-off-task alternative (no ceiling, cold start of a task on the existing `opal-globgrph` cluster). Write "fits / does not fit / marginal (state the margin)" per ceiling. Do NOT write "therefore ECS" or "therefore Lambda" -- CG-s-2's task order reads this table and decides.
5. **RECONCILE THE FOUR EXISTING FIGURES AFTER MEASURING**: for each of the four (the brief names them and their sources), say which of the two operations it actually measured, on what input size, and whether your measurement is consistent with it -- or `NOT RECONSTRUCTIBLE` with the reason. Never adjust your measurement toward a prior figure.

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="V1-AC1" cell_refs="CG-s-10"/> `V1-AC1` -- THE TWO OPERATIONS NAMED at `file:line @ commit`: the full load entry point, the incremental entry point, the full-fallback trigger and its threshold value, and the local orchestrator; each cited from a comp-read of the file, not from memory.
<criterion id="V1-AC2" cell_refs="CG-s-10"/> `V1-AC2` -- TWO FULL LOADS MEASURED into a temp path: for each run, wall clock + peak memory with the instrument named, input sizes (rows per table, bytes read, marker `committed_at`), environment; the variance between runs stated; the canonical local DB untouched (its mtime before and after quoted -- the control that can fail).
<criterion id="V1-AC3" cell_refs="CG-s-10"/> `V1-AC3` -- ONE INCREMENTAL RUN MEASURED on a real delta: the same fields plus delta rows applied and whether the count-guard fired; labeled as the second operation.
<criterion id="V1-AC4" cell_refs="CG-s-10"/> `V1-AC4` -- THE FIT TABLE: every measured figure against the three Lambda ceilings and the ECS alternative, fits / does not fit / marginal with the margin; no runtime chosen in this deliverable (the absence is the criterion).
<criterion id="V1-AC5" cell_refs="CG-s-10"/> `V1-AC5` -- THE FOUR PRIOR FIGURES RECONCILED AFTER MEASUREMENT: each attributed to one of the two operations with its input size, or NOT RECONSTRUCTIBLE with the reason; your own measurement never moved toward any of them (the runs' raw numbers appear unchanged in AC2/AC3).
<criterion id="V1-AC6" cell_refs="CG-s-10"/> `V1-AC6` -- PUSH STATE MEASURED at report (`ls-remote` + `is-ancestor`; LOCAL is the expected reading under the integrator's cadence -- say which state was read). The proof instance is VALID (`.tools/proof-of-spec-check.py` rc 0) with every `surprises` entry resolving to a row BEFORE the complete flip, which this seat commits itself.

<expected_criteria>V1-AC1, V1-AC2, V1-AC3, V1-AC4, V1-AC5, V1-AC6</expected_criteria>

## SURFACES

`infra/aws/globgrph/kuzu_nessie_load.py` 417 @`e445642c5f` · `infra/aws/globgrph/kuzu_incremental_refresh.py` 350 @`aebe0d0a67` · `infra/aws/globgrph/_canonical.py` 746 @`173dd335f4` (`ensure_fresh`, the mkdir mutex, MUTEX_WAIT_S / ORPHAN_LOCK_S / INCREMENTAL_TIMEOUT_S -- read, never edited) · `infra/aws/globgrph/_provenance.py:96` MARKER_KEY `warehouse/_branch_head.main.json` (641 @`996fcad53e`) · the brief `docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md` @`dfd24a010b` (the four figures and their sources) · `docs/architecture/NFRA_KUZUSPLIT_PRD.md` (P0-INSTRUMENT) · S3 bucket `opal-313476888478-globgrph` (read only).

## BOUNDS

- **READ-ONLY against AWS.** No object written to the globgrph bucket, no IAM, no Terraform, no Lambda or ECS resource created. The engine's own reads under the credentials this seat already holds are the whole AWS footprint; if a read is REFUSED by IAM, that refusal is a MEASURED finding for CG-s-12 (carried in the deliverable with the exact action + resource), not something this task order fixes.
- **No edit to any repo source.** The engine is invoked, not changed. A defect found in it is a surprise row (below), never a patch under this cell.
- **The live local copy is not disturbed:** temp path only; do not take or steal `_canonical.py`'s lock; do not kill any running rebuild (a rebuild in progress belongs to whoever started it -- wait it out or run to the temp path in parallel, which needs no lock).
- **Do not pick a runtime and do not size the worker.** The fit table is a finding; CG-s-2 decides.
- **A spec-vs-world divergence is a ROW** at `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` (create the folder on the first row; lane ANY; schema at `org/surprise_channel/schemas/`; `spec_asserts` + `world_is` + `class` + `hazard_standing`), then keep working; never a message. `3.0.0_SA_CVO~A` reads the file at L8. A BLOCKING row also goes to the issuer in the same turn.
- **Certifier != author:** this seat measures and files; the grade is the L8-L10 seat's on the record.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @994c9381d0 (v0.1), cell CG-s-10 (s.1a, ROUND 1 "measure first"; it SIZES CG-s-2).
<owned_cells>CG-s-10</owned_cells>
Read-dependencies, NOT claimed: CG-s-2 (the port that consumes this number), CG-s-12 (an IAM refusal met during the run is that cell's finding).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 19 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 2 -> 2, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 336 NOT-DECIDABLE -> 0); 138 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_CLDGRPH, globgrph, kuzu, opal-gateway, IntegrationSpec, comp-graph or KUZUSPLIT (read at 2026-09-03 06:29:48Z).
comp-iam: DECLARED-NOT-APPLICABLE -- this task order creates, changes and newly grants NO principal, policy or resource: it invokes the existing engine's existing read calls under credentials the seat already holds, into a local temp path; an IAM refusal met during the run is recorded as a finding for CG-s-12, not remedied here, so the lens has an empty population at this subject grain.
comp-adversary: RUN -- rc 0 at read-vintage @a1af5d70c2 (2026-09-03T06:34:19Z, --no-packet: stage 4 disabled by the caller, disclosed); pins found 10 commits, 10 repo paths, 1 file:line cite, 5 tool mentions; cited commits 10 attempted / 10 verified / 0 UNVERIFIABLE; cited paths 10 attempted / 7 stable / 3 flagged (all three flagged = GONE at read-vintage: the deliverable file, the proof instance and the investigation file this TO CREATES -- expected, not stale); uncited siblings 1,050 with the cap (25) declared; 2 hex runs not parsed as pins by design (a date, the account id); complement sources 4 run / 0 deferred / 5 declared-excluded (v1 contract). Instrument: comp-adversary CLEARED @bbba0db0e9, run from a seat that did not fix it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `V1-AC1`..`V1-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/NFRA_CLDGRPH.TO-CG-V-1.full-fallback-duration-measured.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. V1-AC2's untouched-canonical-DB
control and V1-AC5's "measurement never moved toward a prior figure" are the arms that must be able to FAIL; every `surprises` entry opens with
a row id that resolves in the project's channel (the SURPRISES limb refuses the flip otherwise).
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read infra/aws/globgrph/kuzu_incremental_refresh.py --for "where the full-fallback is triggered, what threshold flips it, and what the incremental path applies"` and `comp-read infra/aws/globgrph/kuzu_nessie_load.py --for "the full-load entry point, what it reads from Nessie/Iceberg, and where the output DB path is chosen"`; `comp-read infra/aws/globgrph/_canonical.py --enumerate 'ensure_fresh|MUTEX_WAIT_S|ORPHAN_LOCK_S|INCREMENTAL_TIMEOUT_S|CANONICAL_DB_PATH'` (to stay OFF the lock and the canonical path). DURING: the marker's `committed_at` read at each run (`_provenance.read_branch_head_marker`, or the S3 object's own metadata). AFTER: `.tools/proof-of-spec-check.py` on the instance; `git ls-remote origin CLOUD` + `git merge-base --is-ancestor` for V1-AC6.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~A` (the sequencer; the L8 seat `3.0.0_SA_CVO~A` reads the record, not a message; never message that seat) with per-criterion evidence, the raw numbers of all three runs, the fit table, and push state as MEASURED. GO = this TO + the dispatch message.
