# RCG execution gating -- D-0001 items 3 + 5 discharged, sweep gate built and exercised

**archetype:** MIXED (IMPLEMENT + DIAGNOSE + COORDINATE)
**Serial:** `1.0.0_SA_CTO~B` (RCG execution-coordination seat, spawned Andrew-direct per RCG `R-0021`)
**Window:** 2026-08-04 00:45Z - 01:30Z
**Counterpart:** `4.0.0_SA_CRO` (live throughout; 4 message round-trips)
**Commits:** `2cdb15c78b` · `0fb3be24a3` · `5d8b576299` · `b308fa7132`

---

## Mandate

Andrew spawned this lane as a **separate CTO seat** so CTO Base stays on the served-integrity board.
RCG work lives here. The RCG ledger already named the seat before I registered: `R-0021` +
`D-0004` ferried the two `D-0001` items CTO had held back for the RCG drive start:

- **item 3** -- wire `rcg/bin/manifest_check.py` into the commit-gate chain
- **item 5** -- rule the mechanics for ratified ARCHIVE batches deleting across foreign
  `owned-paths` lanes

Execution of the ARCHIVE map was parked on item 5. The hand-off text block Andrew was to carry never
arrived; I reconstructed the mandate at source from the ledger rather than waiting, and said so.

## What landed

| Commit | Item |
|---|---|
| `2cdb15c78b` | item 3 -- `rcg-manifest-check.sh` (pre-commit stage 5) + tracked installer + tracked test |
| `0fb3be24a3` | item 5 -- ruling **CTOB-RCG-001** |
| `5d8b576299` | `rcg-sweep-check` -- the ruling's mechanism (8-check engine, wrapper, installer, 11-case matrix) |
| `b308fa7132` | the sweep-executor grant (5 lanes) + a ruling amendment against my own text |

**Ruling in one line: AUTHORITY ATTACHES TO THE BATCH, NOT TO THE SEAT.** The executing identity may
hold a broad delete lane precisely because a gate makes that lane unusable for anything but an exact
ratified batch; the gate keys on **author identity**, not a trailer, so no un-gated commit shape
exists for that seat; and every safety property is **re-derived at execution** from ledger + tree,
never read from the batch.

## The finding that justified the seat

Gating pass, before authorizing anything: the delegated labeling round (`R-0020`) had marked **4,103
files under `infra/aws/lambda/layers/pyiceberg-nessie-deps/` as ARCHIVE at HIGH confidence** -- inside
a subtree Andrew **explicitly ratified KEEP** at `R-0019`. Three independent proofs: the ruling
contradiction; a mid-package split (`click/__init__.py` and `core.py` ARCHIVE while `decorators.py`,
`termui.py` +4 KEEP -- structurally incoherent, not a judgment call); and the tree being
build-load-bearing (`infra/aws/terraform/shared-infra/layers.tf:9`).

**The sharpest part was not the contradiction but the gap it sat in:** CRO's own hand-off described
that tree as MIGRATE ("never batch-deleted") while the executable ledger had 4,103 of its files as
ARCHIVE. Mental model protected, artifact queued for deletion, and a batch is built from the artifact.
That is the entire argument for a second seat reading the ledger instead of the summary.

CRO verified and corrected at `R-0022`, then swept and found **3 more contradiction sites** of the
inverse shape (46 subtrees checked, 4 fired). **ARCHIVE queue 7,048 -> 2,945.**

## Errors I made, and what caught each

1. **My test harness reported FAIL against a correct gate.** `grep` parsed the expected substring
   `DENY [not-in-manifest]` as a character class ("Invalid range end"). The harness's own pattern
   failed and I nearly read it as the subject failing -- CLAUDE.md's *put the control on the
   RETRIEVAL, not the pattern*, in miniature. Fixed with `grep -F`, reason commented in the test.
2. **My C6 was wrong in a way only a PERMIT control could see.** First written to walk every
   *ancestor* directory of an andrew-ratified path, so one ratified file at the top of a tree marked
   the whole tree ratified -- a single KEEP under `data/` denied every path beneath it. Against the
   live ledger: **all 870 `data/` archives denied.** *A deny-only suite would have scored it 10/10.*
   The gate was failing loud but wrong, and only driving it to PERMIT a legitimate batch exposed it.
   Now scoped to the immediate directory; subtree-level supremacy needs a **declared** cohort list in
   the ledger, not an inference in my code.
3. **My own ruling asserted a mechanism I had not measured** -- s.6 said the grant was "one narrow
   lane." `owned-paths` resolves a lane *per path*; a sweep spans every root. Measured: 10 lanes
   touched, **1,796 paths (61%) already reachable**, 7 denied. Amended in `b308fa7132`. Left
   unmeasured it would have sent the executor to an audited override on first contact -- the exact
   outcome the ruling's own s.3(b) rejects.
4. **The commit gate blocked me** on E702 in my own engine. Fixed, re-ran the matrix (a lint fix is
   still a code change), re-committed.

## Evidence

- item 3: 4/4 including both mutants; composed hook run end-to-end on a throwaway index **reaches
  stage 5 and denies**; installer idempotent. Not exercised: the append-only tamper path (it compares
  the working copy of CRO's live ledgers, which were being appended to) -- recorded, not omitted.
- sweep gate: 11/11 fixture cases, every check driven to fire by a real mutant, plus 3 trigger cases
  (ordinary author -> rc=0 zero output; sweep identity without `RCG_BATCH_ID` -> DENY; nonexistent
  batch -> CANNOT EVALUATE -> DENY).
- grant control: after granting, `4.0.0_SA_CRO~SWEEP` reaches 2,933/2,945 while base `4.0.0_SA_CRO`
  is **measured unchanged at 1,796** -- the suffix->base auto-permit runs one way only, confirmed
  empirically rather than only read. `CLAUDE.md` and `org/tier0/ledger/**` DENY for both.
- **Nothing was accepted on its authoring commit.** The deny paths are proven by the matrices; the
  authoring commits exercise only the no-op path.

## Dry-run against the live queue

C5 protected-charter violations **0** · C6 cohort contradictions **0** (R-0022's correction was
complete on this criterion) · C7 **1 live hit**: `tools/news_scanner/scripts/utilities/` would lose
`__init__.py` while 6 `.py` siblings survive, and `backfill_clean_summaries.py:19` imports
`from utilities.text_cleaner`. Second instance of the click class, found by the gate on its first
real-data run, before any batch was cut. Routed to CRO.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-which "how do I grep the repo"` | PASS | startup A.3 exercise -- forwarder RAN (banner), not merely resolved. PATH 94/94 bare. |
| `comp-surface-check` (via safe-commit) | OK x4 | 3-7 files screened vs 6 surfaces each commit; no critical surface touched |
| `comp-pulse diff` (risk-reflex) | CLEAN x4 | denominators printed: 3, 1, 5, 2 files vs 1,662 danger nodes |
| `commit-gate.sh` | **BLOCKED then PASS** | caught E702 x4 in `rcg_sweep_verify.py`. The gate fired on its own author -- worth the record |
| `owned-paths-check` | **BLOCKED then PASS** | correctly denied `org/rcg-sweep-audit.log` as UNDEFINED; fixed with a `GOVERNANCE_AUDIT` path rule + `.gitignore` un-ignore, mirroring its four 2026-07-16 siblings |
| `owned-paths-validate.py` | PASS | 54 lanes, 224 path rules, all refs resolve (run before and after the grant) |
| `audit-archive-invoker` | rc=1, 1 finding | `org/tombstone-gate-audit.log` baseline missing from the 2026-08-03T143634Z archive -- **routed to CTO Base, predates this seat** |
| `mass-deletion-check --mode` | measured | `effective mode: block`, threshold 25 -- the live constraint item 5 had to design around |
| raw `grep`/`git` | used | ledger/charter arithmetic and lane-reachability measurement; no comp-tool models label-vs-charter-vs-lane intersection, which is the whole question |

## ADDENDUM 01:30-01:45Z -- the restore leg had no legal author (`e3a07f97f4`)

**A defect in my own ruling, found by CRO reading the gate's source before executing.** s.7 makes an
exercised `git revert` the acceptance condition. A revert of a deletion batch is **additions**, which
**C1 denies** -- and the sweep identity is the only one that can reach those paths, *because granting
it the delete lanes in s.6 is what made it so.* Measured on B-0001: `~SWEEP` **93/93**; `~B`, base
CTO, MSTR, COO **0/93 each**.

**The recovery path was structurally unauthorable from the moment my grant landed: the one seat able
to restore was the one seat I forbade.** Invisible to reading, because the deny suite was complete
*and correct* -- the revert deny-suite was **vacuously** complete, since nothing could legally permit
a restore at all. **My own C6 lesson, recurring one layer up, four hours later, in my own code.**

Fixed with a REVERT mode that cannot introduce content (R1 addition-only · R2 set equality both
directions · R3 `executed_commit` recorded · **R4 blob-hash identity** to the pre-deletion tree).
Matrix 11 -> **16/16**. The new cases caught **two more bugs in my own code**, both of which would
have shipped and both of which would have bitten CRO mid-exercise:

1. **R4 compared `git diff --raw`'s abbreviated sha to `git rev-parse`'s full 40-char sha** -- so a
   *perfect* restore was denied as tampered on every path. `--abbrev=40` is now load-bearing and
   commented as such.
2. **RV5 returned rc=3 while printing "SWEEP DENIED"** -- right code, wrong story; told an operator
   they were denied when the gate could not evaluate.

**Also settled by exercise rather than reading** (CRO's open question on commit form): `git commit
--only -- <pathspec>` isolates the pre-commit hook's index view to *exactly* the pathspec. Proven in
a scratch repo with a foreign staged modification deliberately present -- the hook saw only the 2
batch deletions; the foreign file stayed uncommitted. Batches ride **true `git rm` + the ordinary
safe-commit pathspec form**; neither workaround CRO offered is needed.

**Routed-finding loop closed both ways:** CTO Base closed the tombstone-gate finding as a
*pre-registered transient* (`14b3a3da7d` added the log to the archive MANIFEST *after* the snapshot
mint -- fail-closed by design, not a defect), and in the same pass caught that **my own
`org/rcg-sweep-audit.log` is UNCOVERED in that MANIFEST**. I did the owned-paths and `.gitignore`
halves tonight and missed the archive half. Concurred: ADD, rare-bypass class (~10-30 lines across
the entire sweep programme, single writer, gated on one identity). I am the writer's author, so
coverage is authored by others -- SoD.

## Open at session end

- **[`4.0.0_SA_CRO`]** author B-0001 DRAFT->RATIFIED. Verified for them: the proposed cohort
  `data/black_diamond/archive/gold/client_detail/` is **93 files, directory-complete, zero survivors,
  no `__init__.py`, 93/93 reachable** -- take all 93 rather than "first 100 sorted"; directory-complete
  beats a mid-directory cut. Then the **revert exercise** before batch 2 exists.
- **[`4.0.0_SA_CRO`]** adjudicate the C7 hit in `news_scanner/scripts/utilities/`.
- **[Andrew]** ferry the CVO arm (`D-0002`) -- CVO sits outside `R-0001` fabric silence, so neither
  CRO nor I can arm it. The one step neither seat can take.
- **[me]** the 12 `BASE_EXEC`/`POD2` stragglers -- I take that leg under ordinary attribution rather
  than widen a 3-member lane; not in any batch.
- **[CTO Base]** the tombstone-gate archive baseline finding.
- **Standing residual:** no install-all hook entry point (`.owned-paths.yaml:114`). Until it exists a
  clone can hold the lane grant without the gate -- the one unsafe ordering in this design. Bounded
  to primary-laptop-only execution with the installer run as recorded batch prep.
