# THE TIGHTENING ENUMERATION SPEC -- the four joints of the truth-establishment machine (4.0.0_SA_CRO~A, 2026-08-18)

**Authority:** Andrew-direct 2026-08-18 ~1530Z at the CTO terminal, verbatim *"I would task 4.0.0_SA_CRO~A
with the tightening enumeration work"* -- record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260818_ALL_RECS_APPROVED_49F_END_TO_END_PUSH_AND_MDPF_UNUSED_DELETE.md`
(third instruction); launch block `CRO_A_LAUNCH_BLOCK_TIGHTENING_ENUMERATION_20260818.md` (same folder).
**Author:** 4.0.0_SA_CRO~A (recon -> specs; this document dispatches nothing and builds nothing).
**Route:** 1.0.0_SA_CTO (ratify) · cc 2.0.0_SA_COO (decompose) · cc 0.0.0_AB_MSTR (record).
**Method:** every claim below is grounded on a read taken THIS SESSION (2026-08-18 ~1550-1720Z) or cites
file:line @ commit vintage; inference is marked INFERRED. Non-goals honored: no gates, no
alarms/monitors, no production code, no TO issuance, no re-litigation of ratified law.

**Grounding set (vintages):** push plan @a2f27c8d0a · phase framework @78a2559d5a · pattern spec
@a9c159f134 (ratified @d272021791) · PROOF_OF_SPEC schema + checker @8d77cd1537 · state_scan.py
@aaa9364dc6 · d00 census @2417f7a366 · parity bar @0d72d36f48 · FE-2 promote ledger @00e12cb15a ·
to-check.py @668fe63317 · the four P4/P5 TOs issued 2026-08-18T16:05Z (paths in J4).

---

## 0. SUMMARY TABLE (one page)

| joint | exists today | the gap | measured cost | smallest remedy (ladder rung) | owner (suggested; COO staffs) | must precede |
|---|---|---|---|---|---|---|
| **J1** derived phase board | 44 schema-valid proof instances on disk; to-check.py census engine; proof-of-spec-check validator; comp-state last-touch map | the per-firm x per-phase board is hand-typed in 2 homes (framework CURRENT STATE, project JSON) + hand-counted in the plan; no reader derives it from instances | framework stale since 08-11 ~1750Z; project JSON said "P4 live/held" from 08-12 until CTO hand-rolled it 08-18; the plan's own hand count ("13 PROOF_OF_SPEC_49F_*") measures **14** by glob, same day it was written | ONE read-only mode folded into to-check.py (`--proof-board`), rung 2 (reuse: to-check census frame + proof-of-spec-check parse + comp-state's bulk last-touch map) | 0.8.0_AE_CloudComp (comp-tool lane) | phase-close attestations from P1-close (08-19) onward; NOT gating -- CTO can attest without it |
| **J2** comp-state cp1252 crash | comp-state self-test PASS 3/3; full run PASSES under PYTHONUTF8=1 (19.6s, 2479 records x 400 commits); the correct pattern already in-estate at `comp_missions.py:36-37` | `state_scan.py:68` `text=True` with NO `encoding=` -> default-env full run CRASHES (reproduced this session, rc=1) | the drift linter the push leans on is dead by default on this box (banked since 08-14, CTO log); 33 sibling unencoded sites of 184 subprocess sites; failure mechanism is the swallowed-reader-thread class (stdout=None at rc==0) | ONE line at `state_scan.py:68`: `encoding="utf-8", errors="replace"` (rung 6) + a planted-byte self-test leg; siblings SURFACED, not swept | 0.8.0_AE_CloudComp / DS~B (comp-tool lane per launch block) | 08-19 EOD -- the instrument is in daily push use |
| **J3** atom-conformance runner | pattern spec SS2-SS3 conformance tests in PROSE @a9c159f134; d00 census + fit_harness + c03_twr_lineage.py as partial per-atom instruments | no runner: every proof row cites atoms by hand; 5 of 9 atoms are mechanically checkable TODAY and nothing checks them | INF + COT bind as parameters at P2/P4 -> 3 firms x 9 atoms x every phase event of hand-checks; atom-5's measured violation class (no schedule floor) froze a client product 6 days (NEVER#4 record) | minimal runner `comp-atomcheck` (rung 7, heavy reuse) emitting rows {atom, scope, verdict, evidence, denominator}; verdict enum CONFORMS/VIOLATES/NOT-CHECKABLE-BY-THIS-RUNNER; v1 = the 5 checkable atoms only | 0.8.0_AE_CloudComp (runner) + DS~B (atom-8 lineage declarations per family) | 49F P4 emit (08-20) usable; INF bind at P2-open |
| **J4** P4 rendered+behavioral acceptance | AC-P3 precedent fully recorded @00e12cb15a; the four P4 TOs (16:05Z) already carry the pattern BY NAME (P4R-3, P4X-4, CVO pin/cert TO); ui-smoke.mjs exists (portal, fs-verified 8,550 B) | NO artifact enumerates the PER-KEY oracles: which surface renders each key, what MUST change at flip, what MUST NOT, and the mutant each read must catch | FE-2's pixel read was measured NON-DISCRIMINATING (mutant delta 60 of 3,378,240 px) and was discovered MID-promote; unenumerated, the same discovery recurs per key, on flip day, x15 keys | ONE committed oracle-table artifact (rung 1-2: NO new tool -- rows the existing TOs' criterion sets reference), schema in J4.4 | DE (read-surface rows) + CVO (discriminating-value rows); COO folds refs into P4R-3/P4X-4 | pins 08-21 / flip 08-22 -- table committed by 08-21 |

**The four joints share one spine:** each replaces a HAND-CARRIED truth (a typed board, an env-var
workaround, a human atom-read, an unenumerated acceptance) with a DERIVED one -- same direction as the
estate's own laws (a predicate is not a roster; the record is not the plane; controls over care).

---

## J1 -- THE PHASE BOARD IS HAND-TYPED: spec for a DERIVED board

### J1.1 EXISTS-TODAY

- **The instances (the substrate -- it already exists and is clean):** 45 files match
  `org/**/PROOF_OF_SPEC*.json`; minus the schema itself = **44 instances**, 0 malformed
  (json.load + key read on all 44, this session). Distribution: DS base 30 · CRO 7 · AE 0.7.0 3 ·
  DS~O 2 · DT 2. Every instance carries machine-readable `to_id`, `phase` (the framework's five-value
  enum + INVESTIGATION/NON-BUILD-OTHER), `spec_ref.vintage_commit`, `assignee`, per-criterion
  `acceptance[]` rows with `status`, and `artifacts_produced[].deployed_state`
  (`org/standards/PROOF_OF_SPEC.schema.json` @8d77cd1537 -- required keys, `additionalProperties:false`).
- **The validator:** `.tools/proof-of-spec-check.py` @8d77cd1537 -- structural + conditional rules +
  coverage vs an expected-criterion set; exit 0/1/2 contract.
- **The census frame:** `.tools/to-check.py` @668fe63317 -- workspace-wide TO enumeration, project
  grouping, BY-AGENT rollup, parse-errors surfaced never dropped, ASCII discipline. The exact rendering
  conventions the board needs, already registered and in daily use (XXX.md Step 1b B.1).
- **The vintage machinery:** `state_scan.py:96-110` @aaa9364dc6 `build_last_touch_map()` -- ONE
  streaming `git log --name-only` walk -> {path: last-commit-ts}, measured 4.1s total vs 277ms/call
  per-file (its own docstring). The board's per-instance vintage read, already written.
- **The hand-typed boards it would replace as FIRST READ (they remain the attestation record):**
  `docs/architecture/GOLD_MIGRATION_PHASE_FRAMEWORK.md` "CURRENT STATE" @78a2559d5a (self-dated
  2026-08-11 ~1750Z, instruction "update in place at each phase event") and
  `org/projects/OPAL_ADVIPOINTERS.json` (rolled by CTO 08-18 as their FIRST WRITE after finding it
  still said "P4 live/held" from 08-12 -- CTO handoff `2026-08-18_1510Z.md` SS1 row 1).

### J1.2 GAP

No reader derives (firm x phase -> instance count / verdict mix / newest vintage) from the instances.
The board exists only as prose two seats hand-roll, and counts of instances appear in dated plans as
typed digits. **The schema carries NO firm field** -- firm is recoverable only from the `to_id` /
criterion-id grammar (`{firm}-{group}-{artifact}-{check}`, parity bar SS5) or the filename, and that
derivation is currently done in heads.

### J1.3 COST-MEASURED

1. CTO's 08-18 successor's FIRST WRITE was hand-rolling both stale boards (handoff SS1 row 1: framework
   "stale", project JSON "STILL says P4 live/held from 08-12") -- a recurring per-successor tax.
2. The push plan @a2f27c8d0a SS4 hand-types *"the 13 `PROOF_OF_SPEC_49F_*` instances"*; the glob
   measures **14** (13 OVERLAY + PARTNER_ANALYTICS_TRIO), same day the plan was written. One off,
   harmless today, structural: a typed count in a fresh document already disagrees with its own glob.
3. Three keying methods produce three different "the 49F count" answers (this session's mini-read):
   name-glob = 14; framework's A/B/C-leg count = 13 (49F 4 + INF 5 + COT 4, a DIFFERENT 13 than the
   plan's); naive to_id-prefix parse = 12 with 5 UNPARSED. **Not an error in any one source -- the
   absence of ONE declared derivation.** (Rule 24: three grains on one axis.)

### J1.4 REMEDY (smallest; BUILD LADDER rung 2 -- the estate already has every part)

**ONE read-only mode folded into `to-check.py`: `--proof-board`.** No new tool, no new file format, no
schedule, no monitor. Composition (all reuse): glob `org/**/PROOF_OF_SPEC_*.json` -> parse via the
schema's own required keys (structural failures LISTED as `MALFORMED`, never dropped -- to-check's
existing PARSE-ERROR convention) -> key rows by `(firm, phase)` -> render the per-firm x per-phase
table with per-cell: instance count, PASS/FAIL/UNCOMPUTABLE row mix, newest `spec_ref.vintage_commit`,
newest git last-touch (comp-state's bulk map pattern).

Board contract (each item is a constraint from the launch block, made mechanical):

1. **Firm derivation is DECLARED and printed.** v1 rule: leading token of `to_id` matched against the
   ratified firm set {49F, INF, COT, MDPF} per the criterion-id grammar; no match -> **`UNPARSED`
   rendered as its own row, never guessed** (measured today: 5 instances -- the P1_B* group -- carry no
   firm token in `to_id`; they render UNPARSED until re-keyed or the grammar is amended). A `firm`
   field in the schema would make this exact; that is a **schema act to PROPOSE to CTO** (optional
   field, additive), not part of this build.
2. **UNKNOWN is a rendered value.** A (firm, phase) cell with no instance prints `UNKNOWN (0 instances)`
   -- never "not started", never blank (the block's constraint verbatim). Today's true cells: 49F
   P3-REPOINTS = 0 instances, 49F P4-PUBLISHERS = 0 instances (this session's read).
3. **Denominators printed:** `N instances parsed of M files matched; K MALFORMED (listed)`.
4. **Provenance header:** the read's own vintage (HEAD sha + timestamp) -- the comp-estate lesson
   (Rule 21): a board without a vintage is a snapshot wearing a live read's clothing.
5. **Read-only; run-and-read.** No S3, no writes, no cron. The board is an INSTRUMENT for the
   attestation owner; the framework's CURRENT STATE prose remains the attested RECORD (this does not
   re-home the record; one fact one home is undisturbed -- the board is a derivation, not a second home).
6. Registered per the comp-tool convention (comp-which routable; manifest row) -- the gate-maintained
   count absorbs it.

### J1.5 OWNER (suggested)

**0.8.0_AE_CloudComp** -- the comp-tool lane (owned-paths: base enumerated for comp-tool builds
2026-07-02; `.tools/` engine convention). COO staffs; CRO does not dispatch.

### J1.6 ACCEPTANCE-THAT-FAILS-IF-WRONG

- **A1 (reproduces today):** on the 2026-08-18 tree the board must print: total 44 of 45 files (schema
  excluded), 0 MALFORMED; 49F/P1-SCRIPTS nonzero with newest vintage = an 08-11-dated commit; 49F
  P3-REPOINTS and P4-PUBLISHERS cells = UNKNOWN(0). Wrong keying, dropped files, or inferred cells fail
  this against the numbers measured above.
- **A2 (mutant, malformed):** a hand-planted instance with a missing required key must appear as
  `MALFORMED: <path>` in the output AND flip the denominator line -- silence = FAIL (proof-of-spec-check
  self-test pattern).
- **A3 (mutant, phase flip):** a planted valid instance with `phase: P4-PUBLISHERS`, to_id `49F-...`
  must flip the 49F P4 cell UNKNOWN(0) -> 1. A board that cannot see one new instance is not derived.
- **A4 (UNPARSED honesty):** the 5 P1_B* instances must render UNPARSED, not 49F -- a board that
  silently absorbs them into a firm has inferred.

### J1.7 SEQUENCING

Serves the P1-close attestation (08-19) and every phase event after; **not gating** -- CTO attests from
raw instances today. Build window: with J2 (same lane), before 08-20.

---

## J2 -- THE DRIFT LINTER LIMPS: the cp1252 crash, pinned, censused, spec'd

### J2.1 EXISTS-TODAY (and the true mechanism, measured this session -- it is sharper than the banked description)

- Site: `org/modules/graph/state_scan.py:67-69` @aaa9364dc6 --
  `subprocess.run(["git", *args], cwd=_WS, capture_output=True, text=True)`; `text=True` with **no
  `encoding=`** decodes with `locale.getpreferredencoding(False)` = **cp1252** on this box (measured:
  `python -c "import locale; ..."` -> cp1252).
- **Reproduced:** default env (`PYTHONUTF8`/`PYTHONIOENCODING` unset), `python .tools/comp-state` ->
  crash, **true rc=1**. Control: `PYTHONUTF8=1` -> full run completes -- 400 commits, 2,479 records,
  19.6s, report renders.
- **The mechanism (this corrects the shorthand in the banked note):** the `UnicodeDecodeError`
  (`'charmap' codec can't decode byte 0x90 in position 214544`) is raised **inside the subprocess
  READER THREAD** (`subprocess.py:1599 _readerthread`), which dies; `communicate()` then returns
  `stdout=None` **with `returncode==0`** -- so `_git`'s own `rc==0` guard at `:69` PASSES and returns
  `None`, and the crash surfaces one frame later as `AttributeError: 'NoneType' object has no attribute
  'split'` at `load_commits` **`state_scan.py:77`**. The thread's UnicodeDecodeError prints separately
  on stderr, disconnected from the final traceback. **This is the instruments-that-lie class the estate
  already names** (a retrieval failure returning a VALUE): the tool is one caller-guard away
  (`raw or ""`) from a SILENT EMPTY CORPUS -- every record would verdict QUIET, well-formed, wrong.
  Today it fails loud-but-cryptic; the fix should keep it from ever failing at all.
- **Specimen (in-corpus):** commit `389d604c08` (2026-08-12, author 4.0.0_SA_CRO~Z) carries a raw
  `0x90` byte in its body -- 1 of the last 400 commits (measured; `git log -n 400 --format="%B" | grep
  -c $'\x90'` = 1). The crash reproduces as long as ANY such commit is in the corpus window; the window
  moves, so the regression control must PLANT one (J2.4).
- **The tool's own precedent, same file:** `state_scan.py:51-58` fixes the identical class on the
  OUTPUT stream (`sys.stdout.reconfigure(encoding="ascii", errors="backslashreplace")`, comment: a
  status field's U+2192 "killed the render under cp1252"). **The input stream was never given the same
  treatment -- the asymmetry IS the bug.**
- **The correct pattern, already in-estate:** `.tools/comp_missions.py:36-37` --
  `subprocess.run(..., text=True, encoding="utf-8", errors="replace")` (+ loud SystemExit on rc!=0).
  Rung-2 reuse: copy this call shape.
- Banked since 08-14 (CTO log; carried in the 08-18 CTO handoff SS1 residual bank row) -- consistent
  with everything measured here.

### J2.2 GAP

One missing `encoding=` argument on the one subprocess helper every comp-state read flows through
(`_git` is the sole git entry point: `load_commits:75`, `build_last_touch_map:101`,
`_last_touch_file:92` all route through `:67-69`).

### J2.3 COST-MEASURED

- The instrument that catches "the record says X, the commits say Y" -- named by the launch block as
  what the push depends on -- is **dead by default invocation on this box** and has been for >=4 days;
  it runs only for operators who know the env-var incantation. An instrument with an incantation is an
  instrument half the fabric isn't running.
- **Census (denominator printed):** grep over `.tools/ + org/modules/` `*.py` for
  text-mode subprocess calls (`text=True|universal_newlines`) without `encoding=` on the same line:
  **34 line-hits; 1 false positive on inspection** (comp_missions.py:36 -- its `encoding=` sits on the
  continuation line) = **33 unencoded sites across 29 files**, of **184 total subprocess call sites in
  91 files**. Method honesty: line-based grep; a multi-line call with `encoding=` on a later line
  false-positives and a split `text=True` false-negatives -- the fixing lane re-verifies per site.
  Risk-classed by upstream: **git-content readers (same class as the crash, arbitrary user-authored
  bytes):** `comp_gitdrill.py:40` (reads commit content by design), `rcg_sweep_verify.py:70`,
  `comp_blast_universe.py:309`, `object_freshness.py:37`, `state_scan.py:68` (the patient), plus
  filename-grade git reads (`_comprail.py:166`, `nerves_resolve.py:128`, `comp_aws_cli.py:2273` --
  ASCII-shaped output, latent). **Tool-output/commit-message readers (medium):**
  `audit-archive-invoker.py:545` (safe-commit output quotes commit messages), `comp_system.py:77` +
  `compproof/tool_probe.py:163,846,1010` + `compproof/harness.py:164` (run comp-tools whose stdout can
  carry repo bytes). **AWS/terraform JSON readers (low, latent):** the remaining ~17.
- ⛔ **DIRECTION, NOT A SWEEP WARRANT:** per the estate's own surface-not-chase default, the 33-site
  census is SURFACED here for the owning lane; only `state_scan.py:68` is in this remedy's scope. A
  sibling gets fixed when its lane touches it or its owner so routes -- 32 unforced edits in push week
  is the wrong trade. (INFERRED judgment, stated as recommendation.)

### J2.4 REMEDY (smallest; BUILD LADDER rung 6 -- one line)

1. `state_scan.py:68`: `subprocess.run(["git", *args], cwd=_WS, capture_output=True, text=True,
   encoding="utf-8", errors="replace")` -- the comp_missions pattern. `errors="replace"` is
   load-bearing: commit bytes are not guaranteed valid UTF-8 either (the specimen's `0x90` may be a
   cp1252-authored artifact); `replace` makes the read TOTAL -- a mangled character in one commit body
   costs one BM25 token, never the corpus. git's own storage is encoding-agnostic; UTF-8 is git's
   default commit-encoding convention, so `utf-8 + replace` is the maximum-fidelity total read.
   (`i18n.commitEncoding` is unset in this repo -- checked -- so no re-encoding subtlety applies.)
2. **Regression control (the self-test is the home -- it already plants records):** extend
   `--self-test` to plant a synthetic commit whose body carries a non-UTF-8/non-cp1252 byte (e.g.
   `\x90`) in a temp repo (or feed `load_commits`' parser a planted raw chunk) and require the corpus
   read to COMPLETE and carry the commit; verdict line becomes 4/4. This makes the control
   window-independent -- specimen `389d604c08` will scroll out of the 400-commit window; a planted
   byte cannot.
3. **Mutant (per the controls doctrine):** with the fix reverted, the planted-byte leg must CRASH --
   run once at land time, recorded in the fixing TO's proof instance (`controls.mutant`).

### J2.5 OWNER (suggested)

**0.8.0_AE_CloudComp / DS~B** per the launch block's own line (comp-tool lane, `.owned-paths`
`org/modules/graph/**`). One-line fix + self-test leg: small enough to ride any existing comp-tool TO
at that seat; COO routes.

### J2.6 ACCEPTANCE-THAT-FAILS-IF-WRONG

- **A1:** default env (no PYTHONUTF8/PYTHONIOENCODING), `python .tools/comp-state` on a corpus
  containing specimen `389d604c08` (or the planted leg) -> completes rc=0, report renders, the
  specimen's commit present in the corpus count. Fails if the fix is cosmetic or landed on the wrong
  call site.
- **A2 (mutant):** fix reverted -> planted-byte self-test leg crashes (AttributeError at `:77`).
  A "fix" that passes A1 with A2 also passing didn't change the read path.
- **A3 (self-test):** `--self-test` 4/4 including the encoding leg; exit 2 on any miss (existing
  contract).
- **A4 (no behavior drift):** `PYTHONUTF8=1` run before vs default-env run after: identical record
  verdict counts on the same HEAD (the fix must change decoding, not scoring).

### J2.7 SEQUENCING

**Before 08-19 EOD** -- ahead of the P1-close reconciliation reads and every "did the record keep up
with the push" question this week. Smallest item in this spec; no reason to wait.

---

## J3 -- ARCHETYPE CONFORMANCE IS CHECKED BY PEOPLE: spec for the nine-atom runner

### J3.1 EXISTS-TODAY

- **The law:** pattern spec SS2 (nine atoms, each with its measured mdpf violation) + SS3 (atom-8 in
  full, with a mechanical per-field test already worded: *"name the endpoint field it traces to, or
  name its exception-list entry"*) @a9c159f134, ratified @d272021791. The ratified exception set
  (5 members incl. the 49F TWR-from-components grant) is IN the spec -- the atom-8 oracle's allowlist
  already exists as prose.
- **Partial instruments, per atom, already built:** `d00_served_shape_census.py` + `d00_census_out.json`
  @2417f7a366 (family x schema census, fe/estate/producers legs -- the served-field universe atom 8
  needs); `fit_harness.py` (read-only GET/LIST, refuses platinum writes -- parity bar SS6; the
  run-and-read form the runner must copy); `c03_twr_lineage.py` (the 49F TWR lineage leg, exception
  member 5); `predeclared_divergences_49f.json` (the declared-exception form, field-path globs).
- **The consumer shape:** every P4/P5 TO already carries proof-of-spec criterion rows with
  `method: command` + `invocation` + `output_evidence` -- a runner row embeds directly; no contract
  change needed.
- **What does NOT exist:** any executable that renders an atom verdict. Zero hits for an
  atom-conformance runner in `.tools/`/`org/modules/graph/` (comp-find sweep this session; the only
  "atom" tooling is the atom_decomp METHOD corpus, which is a decomposition instrument, not a
  conformance checker).

### J3.2 GAP + the per-atom checkability enumeration (the deliverable the block asks for)

Verdict enum (Rule-24 clean): **CONFORMS / VIOLATES / NOT-CHECKABLE-BY-THIS-RUNNER** -- one axis (this
runner's verdict), one grain (atom x product x firm), MECE, and NOT-CHECKABLE is an honest value never
rendered as CONFORMS. `NOT-CHECKABLE` rows carry a `why` (the missing instrument or declaration), the
UNCOMPUTABLE-split convention transposed.

| atom | mechanically checkable TODAY? | what the runner invokes (v1) | what stays NOT-CHECKABLE (named) |
|---|---|---|---|
| 1 one-product-root grammar | **YES** | S3 list under `portal/gold/{product}/{scope}/` -> every key matches `{canonical\|dimensions}/{table}/date={D}/...` or a declared `_`-plane prefix; denominator = keys listed | -- |
| 2 `_code/` one deploy target | PARTIAL | existence of `_code/` + deploy-map entries resolve INTO it (source-map/deploy-map read) | "runners pull ONLY here" needs a code-read census of pull sites -- v2, and per Rule 4 the map pairs, it does not byte-compare |
| 3 manifests on every gold write | **YES** | per `{table}/date={D}` partition, a `_manifests/{data-as-of}/*.json` exists; denominator = partitions (49F today: 526) | manifest CONTENT truthfulness (a manifest is a producer self-report -- NEVER#: verify against served state where it matters) |
| 4 intermediates inside the root | PARTIAL | `_feeds/`/`_staging/` prefixes exist under the product root where the product declares intermediates | detecting a FOREIGN-homed intermediate requires classifying arbitrary estate keys as "this product's" -- unbounded; v2 at best |
| 5 schedule floor / one producer / one runtime | PARTIAL -- **the floor half is YES** | EventBridge read: the leg's rule exists with `ScheduleExpression != None` (the NEVER#4 defect rendered mechanical; paginated per the retrieval law, denominator printed) | one-producer-per-key = principal census (post-P4 it holds BY CONSTRUCTION; pre-P4 needs IAM+code census -- comp-iam is DESIRED-only and fails green, Rule 22a); one-runtime = v2 |
| 6 config never in code store | PARTIAL | static scan of the product's runner sources for data reads resolving into `_code/` (the measured violator shape: `build_portal_gold_accrual.py:110,136`) | dynamic/indirect path construction -- the msys_argv/comp-iam lesson: an AST miss is silence, so the scan reports its own coverage denominator |
| 7 serve only via publisher + spelling law | PARTIAL -- **the spelling half is YES** | gold keys use `_`, platinum keys `-` (regex predicate per layer, both spellings DECLARED, guarded-set law); denominator = keys per layer | "only via publisher" = platinum writer census (same instrument gap as atom 5's producer half) |
| 8 raw-from-endpoint | **YES for DECLARATION COVERAGE** | every served field in the d00 census schema for the family appears in (lineage declaration ∪ ratified exception set); a field in neither = **VIOLATES (ILLEGITIMATELY-DERIVED per SS3)**; denominators = fields per family | the TRUTH of a declared mapping (that field X really traces to endpoint Y) is a human/CVO read -- the runner checks coverage, never veracity |
| 9 provenance columns | **YES** | parquet schema read (pyarrow `read_schema`, no data load) on every intermediate table: `source_pipeline` + `_ingested_at` present; denominator = tables | -- |

**Rule-24(iv) state-coherence declaration (required by the law, so stated):** the NOT-CHECKABLE
residue does NOT move with one remedy. Atoms 2/5/7's residue shares one missing instrument (a
producer/writer census -- code+IAM read); atom 8's residue is a DECLARATION artifact (per-family
lineage map, below); atoms 4/6's residue is static-analysis depth. Building the runner delivers the
5 YES cells and structurally cannot deliver the rest -- **a "build the runner" plan covers 5 of 9 on
its own axis, and this paragraph is the required naming of which values do not move.**

**The one NEW artifact atom 8 needs (smallest form):** a per-family lineage declaration --
`{served_field: endpoint_field | exception_id}` JSON, sibling to `predeclared_divergences_49f.json`,
authored by the emitting lane (DS~B) as each P4 family emits. The runner then checks coverage
mechanically. Without it, atom 8 renders NOT-CHECKABLE (honest), not CONFORMS.

### J3.3 COST-MEASURED

- Today each proof row cites atoms by hand; the pattern spec's own SS2 table records a measured
  violation for 6 of 9 atoms at mdpf decomp vintage -- found by HUMAN reads.
- Atom 5's violation class has the estate's sharpest price tag: the no-schedule-floor defect froze
  the client-facing Model Portfolios product for SIX DAYS with fresh inputs unused (CLAUDE.md NEVER#4
  record, mdpf-daily-refresh-trigger). The runner's atom-5 leg renders that class a one-command read.
- The plan binds INF then COT as parameters of the same shape "endpoint-by-endpoint" (push plan SS3
  closing line): without a runner the hand-check surface is 3 firms x 9 atoms x every phase event,
  during the highest-tempo week the program has had. 49F today (CTO handoff SS3, live facts): canonical
  root exists (4 tables + 5 dims, 526 partitions) but **no scheduled writer** -- i.e., atom 5 currently
  VIOLATES for 49F and flips at P2; the runner is the instrument that records that flip as evidence
  rather than prose.

### J3.4 REMEDY (smallest; BUILD LADDER rung 7 with rung-2 parts -- a new runner, assembled from existing instruments)

`comp-atomcheck --product {advi|mdpf} --firm {49financial|inflection|cottonwood} [--atom N]`
(name illustrative; the building lane names it per manifest convention):

- **Output:** one row per atom-in-scope: `{atom, scope, verdict, evidence, denominator, why?}` --
  table + `--json`. A proof instance embeds a row verbatim as `output_evidence` with
  `method: command`; the row IS what the block asks each instance to invoke per atom.
- **v1 scope = the 5 YES cells** (atoms 1, 3, 5-floor, 7-spelling, 8-coverage, 9); every other cell
  prints NOT-CHECKABLE-BY-THIS-RUNNER + why. **Never a monitor** (run-and-read, no schedule, no
  standing comparator -- the fit_harness form, parity bar SS6); read-only by construction (GET/LIST +
  `aws events` describe/list; refuses writes).
- Provenance header (vintage of every read) + paginated-listing discipline (denominator beside every
  count -- the `--no-paginate` law).
- Registered comp-tool (comp-which routable); inputs: d00 census for the field universe, the ratified
  exception set (transcribed once from SS3 into a small JSON the spec's ratifier blesses -- the
  exception SET is ratified law, its machine form is new), the per-family lineage declarations as they
  land.

### J3.5 OWNER (suggested)

**0.8.0_AE_CloudComp** (runner -- comp-tool lane) + **DS~B** (per-family lineage declarations, landing
with each P4-EMIT family; P4E rows already make DS~B the family emitter). CVO consumes verdicts in the
parity/cert chain. COO staffs + sequences.

### J3.6 ACCEPTANCE-THAT-FAILS-IF-WRONG

- **A1 (known-state reproduction):** run on 49F TODAY (pre-P2): atom 5 floor leg = **VIOLATES** (no
  scheduled writer -- the handoff-measured fact); atom 1 = CONFORMS over the 526-partition root
  (denominator printed); atom 3 = the true manifest/partition ratio. After P2 lands (row 2's first
  unattended cycle), the SAME invocation flips atom 5 to CONFORMS. A runner that reads CONFORMS today
  is reading the wrong plane.
- **A2 (mutant, grammar):** a planted key violating the grammar under the product root (e.g. a `.json`
  under `gold/.../date={D}/`) -> atom 1 VIOLATES naming the key. Silence = FAIL.
- **A3 (mutant, atom 8):** a planted served field absent from lineage ∪ exceptions -> VIOLATES
  (ILLEGITIMATELY-DERIVED); and with NO lineage declaration for a family, the family renders
  NOT-CHECKABLE, **never CONFORMS** (the block's constraint, exercised).
- **A4 (enum honesty):** for every atom outside v1 scope the output carries
  NOT-CHECKABLE-BY-THIS-RUNNER + why; grep proves no unimplemented atom ever prints CONFORMS.

### J3.7 SEQUENCING

Usable by **49F P4 emit (08-20)** -- P4E proof rows embed atom rows for the emitted families; REQUIRED
before **INF binds at P2-open** (the spec's first customer, per the block). v1 is a 1-2 day build at
the owning lane (INFERRED estimate; the parts exist).

---

## J4 -- P4 ACCEPTANCE IS A RENDERED + BEHAVIORAL READ PER KEY: the oracle-set spec

### J4.1 EXISTS-TODAY

- **The precedent, in full:** MDPF_EVR.FE-2.PROMOTE ledger
  `org/critical_paths/change_management/20260815T211100Z_portal_prod_promote_MDPF_EVR_FE2.md`
  @00e12cb15a, AC-P3 section: rendered read on the DEPLOYED PROD bundle -- and the measured lesson that
  the pixel read was **NON-DISCRIMINATING** (mutant fixture rendered pixel-identical: 60 of 3,378,240
  px, the animated dot), because `ModelPortfolios.tsx:884-889 @449a6a0e` empties the distinguishing
  state at Global. The read that DISCRIMINATED was **behavioral** (console capture: real data 0 warns;
  unknown-string mutant `reconstructed_zzz` -> exactly 1 warn) plus a **bundle-content read** (served
  chunk carries `reconstructed(` x1, absent at v2.1.161, positive control `interpolated_estimate` x13).
  Three oracle kinds, one lesson: **enumerate which kind discriminates per surface BEFORE flip day.**
- **The TO chain already invokes the pattern by name** (all issued 2026-08-18T16:05Z, COO):
  - `0.4.0_DE_.../OPAL_ADVIPOINTERS.P4-REPOINT-49F...md` -- P4R-1 read-surface enumeration (key ->
    config/router/component), P4R-2 tolerant read with LOUD mismatch, P4R-3 flip-per-key + rendered
    read on DEV, P4R-4 named-deltas-never-blended.
  - `0.4.0_DT_.../OPAL_ADVIPOINTERS.P4-PROMOTE-49F...md` -- P4X-4: `portal/scripts/ui-smoke.mjs`
    (fs-verified present, 8,550 B) on the AdvisorIntelligence route, "screenshot READ + behavioral
    assertions pass", named as the row-4c close evidence.
  - `3.0.0_SA_CVO/.../OPAL_ADVIPOINTERS.P4-PINS-CERT-49F...md` -- the pin/cert legs are FULLY SPEC'D:
    same-content-date precondition, FRESH-vintage pin per key incl. the $122.5M Schwab-canonical
    authority class @745ca6d78f, vintage-stated rows, Rule-14e cert per key at flip consuming pin +
    never-widen disclosure + CTO/COO determination, post-flip re-base ~0 as its own recorded act,
    DELTA=0 keys certed without hold.
- **The key universe:** P4E-1 (DS~B + CVO joint) freezes THE key list as ONE committed artifact -- the
  denominator every leg cites. The d00 census fe-leg (24 FE-read families; 16 matched live; 8
  REACHABILITY findings) is the enumeration source.
- **The cert evidence form:** parity bar SS5 @0d72d36f48 -- criterion-id grammar
  `{firm}-OVERLAY-{surface}-{check}`, mandatory `-MUTANT-CATCHES` row (absence = INVALID instance),
  date-framing stated per row.

### J4.2 GAP

**"Behavioral assertions pass" has no per-key content.** No artifact says, for each key on the frozen
list: (a) which portal surface renders it; (b) the discriminating positive -- what value/label MUST
change when THIS key's flip lands (and its expected magnitude class from the pin, e.g. the $122.5M
class where it lands vs DELTA=0 keys where NOTHING must move); (c) the invariants -- what MUST NOT
change; (d) the negative control -- the mutant this key's read must CATCH, chosen per the FE-2 lesson
by oracle KIND (pixel / behavioral-console / bundle-content), because for some keys the pixel read
will be structurally non-discriminating and only the enumeration can say so BEFORE 08-22.

### J4.3 COST-MEASURED

FE-2's non-discrimination was discovered MID-promote and cost a premise correction inside a live
acceptance row (the DT log records it: "Reported AC-P3 as PASS with the premise correction inside the
row"). That was ONE surface with a settled TO. P4 is ~15 keys x an 08-22 flip day x three seats
consuming the same reads (DE flip evidence, DT close evidence, CVO cert input). Unenumerated, each
non-discriminating pixel read is discovered per key, on flip day, with the CVO cert BLOCKED behind
each discovery -- or worse, NOT discovered, and a flip is accepted on a read that could not have said
otherwise (the instrument-that-cannot-fail class, Rule 22b's exact shape).

### J4.4 REMEDY (smallest; BUILD LADDER rungs 1-2 -- NO new tool, one committed artifact + criterion wording)

**ONE artifact: `P4_FLIP_ORACLES_49F.json` (name illustrative), committed BEFORE the pins (08-21),
joint-authored, referenced by P4R-3 / P4X-4 / the CVO cert rows.** One row per frozen-list key:

```
{ key,                        # from the P4E-1 frozen list, verbatim
  fe_surface,                 # route + component (from DE's P4R-1 enumeration -- the same read, recorded once)
  read_exercised: yes|no,     # the d00 reachability finding per key; a key nobody reads is DISPOSED in writing (P4R-1 law), its row says so
  oracle_kind: pixel|behavioral|bundle|combination,   # chosen per key, FE-2 taxonomy
  must_change,                # the discriminating positive: field/label + expected class (pinned-delta class per CVO pin, or "DELTA=0: nothing")
  must_not_change,            # named invariants (route-move vs content-refresh separation -- P4R-4's law, made per-key)
  mutant,                     # the planted wrongness this key's read MUST catch (unknown-shape fixture / wrong-vintage fixture / legacy-bytes fixture)
  discriminates_0v1: HOW }    # one sentence: why this oracle can tell flipped from not-flipped (the FE-2 question, pre-answered)
```

- **DELTA=0 keys get oracles too** -- theirs assert NOTHING changed but the read path (the never-widen
  posture made mechanical); a DELTA=0 key whose oracle would also pass pre-flip must carry a
  bundle/behavioral discriminator (e.g. the network read now resolves `platinum/advi/...`), because
  "nothing changed AND I can't tell if it flipped" is not acceptance.
- **Two-phase-pin re-base as the recorded act:** the post-flip re-base (~0) row cites the same key's
  oracle row -- pin says what the DELTA was, oracle says the portal SHOWS the post-flip truth; the CVO
  cert consumes both. No change to the CVO TO needed -- its 49F-CERT-PERKEY row already consumes "(i)
  the pre-flip pin"; the oracle row becomes a named input beside it (COO folds the reference).
- **CVO cert shape (confirming, not inventing -- it exists):** per key, the Rule-14e cert = proof
  instance rows per the parity-bar SS5 grammar (`49F-P4FLIP-{key}-{check}` transposition), mandatory
  `-MUTANT-CATCHES`, vintages + content-date framing stated, grounded on CVO's OWN reads
  (49F-CERT-INPUT-INDEPENDENT). This spec adds ONE required row kind: `-ORACLE-DISCRIMINATES` -- the
  key's oracle row exercised on the deployed bundle, mutant caught.
- **COO's fold (the block's closing instruction):** P4R-3 and P4X-4 gain a clause -- "per the key's
  row in P4_FLIP_ORACLES_49F.json @<vintage>" -- so the criterion sets stay stable and the per-key
  content lives in one home. No TO re-issuance required (INFERRED: a criterion-referenced artifact
  vintage is COO's call to fold; flagged, not assumed).

### J4.5 OWNER (suggested; the block names them)

**DE** authors fe_surface/read_exercised/must_not_change (it IS their P4R-1 read, recorded once) ·
**CVO** authors must_change/mutant/discriminates (the pin owner knows each key's delta class) ·
**COO** folds the references into the P4 TOs · **DT** executes P4X-4 against it · cert stays CVO
(Rule 14e). CRO drafted the schema; CRO does not staff it.

### J4.6 ACCEPTANCE-THAT-FAILS-IF-WRONG

- **A1 (coverage):** one row per key on the frozen P4E-1 list, both directions (missing key / extra
  key = FAIL) -- proof-of-spec-check's coverage mode pattern, run positionally against the list.
- **A2 (discrimination, the FE-2 test):** per key, the oracle must FAIL against the PRE-flip serve and
  PASS against the post-flip serve (or for DELTA=0 keys: the read-path discriminator alone flips).
  Any key whose oracle passes BOTH sides is non-discriminating = the row is wrong -- this is checkable
  on 08-21, BEFORE flip day, against the legacy serve + the platinum twin.
- **A3 (mutant):** each key's named mutant, planted as a fixture, must be CAUGHT by that key's read
  (console warn / shape refusal / bundle absence). A mutant nobody ran = `-MUTANT-CATCHES` absent =
  INVALID per the parity bar's own rule.
- **A4 (pixel honesty):** any key claiming `oracle_kind: pixel` alone must cite why its pixel read
  discriminates (what visible value moves); FE-2 proved the default assumption false -- an unjustified
  pixel-only row FAILS review.

### J4.7 SEQUENCING

Artifact committed **by 08-21** (with the pins; CVO needs the delta classes anyway) -> P4R-3/P4X-4
fold same day -> flip day 08-22 executes against it. The A2 discrimination check runs 08-21 against
both serves -- the one day both sides exist and nothing has flipped.

---

## SURPRISE CHANNEL (banked to COO, one line each, no action taken)

1. `.tools/audit-archive-invoker.py` (startup A.2 run, this session) flagged
   `org/jq-ban-override-audit.log` as an audit-log-shaped file not in MANIFEST -- its own FINDINGS.md
   routing fired; owner 0.7.0_AE_CloudOps.
2. d00 census reconciliation carries 8 FE-read families with NO live instance (REACHABILITY) -- known
   to the census (@2417f7a366); relevant to P4E-1 freezing and P4R-1 disposal rows; DS~B/CVO already
   own that read.

## NON-GOALS HONORED / WHAT THIS SPEC DELIBERATELY DOES NOT DO

No gate is proposed anywhere above (the runners/boards are instruments assignees INVOKE; nothing
blocks a commit or an apply). No monitor/alarm/SNS (every instrument is run-and-read). No shadow
channel or comparator (J4's A2 uses the two serves that ALREADY both exist pre-flip -- no standing
process). No production code was written; the J1 mini-read and J2 reproduction were ad-hoc QA reads,
artifacts discarded. No TO was issued; owners above are SUGGESTIONS for COO. No ratified law is
re-opened -- J3 transcribes the ratified exception set, it does not amend it; J4 confirms the CVO TO's
cert shape rather than redefining it.

-- 4.0.0_SA_CRO~A, 2026-08-18. Draft delivered ahead of the 2026-08-19 ~1800Z date.

---

## CORRECTION (2026-08-18 ~1910Z, CTO-caught at J1 execution @9adb18c7c0; RE-VERIFIED by this author before recording)

**Two measurements above are true of their RETRIEVAL, not of the substrate -- my own J1.3 class
(three grains on one axis / the domain silently redefined), caught in my own numbers at build:**

1. **J1.1's "44 instances (45 files)" was a PREFIX-glob count.** `PROOF_OF_SPEC*.json` misses the
   suffix-named form `{TO_ID}_PROOF_OF_SPEC[~lane].json` -- **20 instances dropped, including the two
   newest and most load-bearing** (`OPAL_ADVIPOINTERS.P1-CLOSE-49F_PROOF_OF_SPEC~A.json`,
   `3.0.0_SA_CVO/.../OPAL_ADVIPOINTERS.P1-SWEEP-49F_PROOF_OF_SPEC.json`). **True substrate
   2026-08-18: 65 files / 64 instances / 0 malformed** (re-verified: substring find = 65; prefix
   find = 45). The sharpest fact: `MDPF_EVR.FE-2.PROMOTE_PROOF_OF_SPEC.json` appears BY NAME in this
   spec's own J4.1 -- the counterexample to J1's glob was inside the same document and neither the
   author nor the ratifier connected them. The as-built board globs SUBSTRING and prints both
   denominators (CTO's execution); A1's "44 of 45" reads as the record of the glob's frame, not an
   acceptance value.
2. **J1.6 A4 / J1.4(1) said "the 5 P1_B* instances"; the P1_B* set measures 4** (to_ids
   P1-B1..B4-*, re-verified). The mini-read's UNPARSED count was 5; only 4 of those are P1_B* --
   two different counts conflated into one sentence. The A4 rule itself (UNPARSED rendered, never
   absorbed) stands and was exercised at build.

Neither correction changes any remedy, owner, or acceptance RULE -- both change COUNTS, and both
are exactly the class this spec's J1 exists to retire: a typed number true of something other than
the thing asked. Recorded here so the numbers carry their frame at the surface a reader reads.
