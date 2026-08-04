# RCG execution gating -- D-0001 items 3 + 5 discharged, sweep gate built and exercised

**archetype:** MIXED (IMPLEMENT + DIAGNOSE + COORDINATE)
**Serial:** `1.0.0_SA_CTO~B` (RCG execution-coordination seat, spawned Andrew-direct per RCG `R-0021`)
**Window:** 2026-08-04 00:45Z - 06:12Z *(the filename carries the OPENING window only; the work ran
on past it and the addenda below are in time order. Filename left unchanged because prior commit
messages cite it.)*
**Counterpart:** `4.0.0_SA_CRO` (live throughout; ~14 message round-trips). Also `1.0.0_SA_CTO` (base,
routed finding), `3.0.0_SA_CVO~B` (independent batch verify, Andrew-provisioned).
**Commits:** 20 by this seat, `2cdb15c78b` (first) through `f89342092b` (last) --
`git log --author="1.0.0_SA_CTO~B" 2cdb15c78b^..HEAD`

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

---

## Blockers

**NONE.** Nothing in this seat's scope is blocked, and nothing is waiting on Andrew.

Verified rather than assumed, per the blocker protocol:
- `D-0002` (the CVO verify arm) READ as blocked-at-Andrew for most of the session. It was not --
  Andrew had already ferried it. Confirmed at source: `D-0005` in `rcg/ledger/DISPOSITIONS.jsonl`
  records him provisioning `3.0.0_SA_CVO~B` personally, and that seat's verify deliverable
  `c11c4b61fb` reads **VERDICT: CLEAN, 26/26 PASS**. I carried it as open for ~2h on an inference I
  had not tested; asking closed it in one message.
- The 4 held stragglers are **routed, not blocked** -- they need a disposition in CRO's ledger, which
  CRO can make without me.

## Current State

*Written for a reader with zero prior context.*

**What this seat is.** `1.0.0_SA_CTO~B` is a CTO lane Andrew spawned (RCG ruling `R-0021`) so that
`NFRA_REPOCOHERENCEGRAPH` execution-gating does not sit on CTO Base's served-integrity board. It is
the single authorized cross-seat counterpart to `4.0.0_SA_CRO`, which otherwise runs under `R-0001`
fabric silence.

**What RCG is doing.** Deleting dead weight from the repo: every tracked file is labelled
(KEEP / REFERENCE_KEEP / MIGRATE / ARCHIVE) in `rcg/ledger/LABELS.jsonl`, and ARCHIVE files are
removed by `git rm` in ratified batches. Git history is the archive; recovery is `git revert`.

**The two things this seat built, both live:**

1. `.tools/git-hooks/rcg-manifest-check.sh` -- pre-commit **stage 5**. Enforces that the `rcg/`
   folder tree is a subset of `rcg/MANIFEST.yaml`. Scoped (no-ops unless `rcg/` is staged) and
   FAIL-CLOSED (a missing checker while `rcg/` is staged is a DENY, unlike stages 2-4 which silently
   skip). Installer `install-rcg-manifest.sh`, test `test-rcg-manifest-check.sh` (4/4).
2. `.tools/rcg_sweep_verify.py` + `.tools/git-hooks/rcg-sweep-check.sh` -- pre-commit **stage 6**.
   Fires on the **author identity** `4.0.0_SA_CRO~SWEEP`, not on a declared trailer, so that seat has
   no un-gated commit shape. 8 execute checks (C1 deletion-only, C2 exact set equality both
   directions, C3 batch prior-committed, C4 re-derived label==ARCHIVE, C5 re-derived charter==SCORE,
   C6 cohort-ratification supremacy, C7 package coherence, C8 size cap) + 4 revert checks (R1-R4,
   blob-hash identity) + a non-blocking content-uniqueness advisory. Invocation:
   `RCG_BATCH_ID=B-000N [RCG_SWEEP_MODE=revert] git commit ...`. Test
   `.tools/test_rcg_sweep_verify.py` -- **18/18**. Audit trail `org/rcg-sweep-audit.log`.

**The ruling.** `org/tier1_exec/1.0.0_SA_CTO/deliverables/RCG_SWEEP_MECHANICS_RULING_20260804.md`
(CTOB-RCG-001). Principle: **authority attaches to the BATCH, not the SEAT** -- the executing identity
may hold a broad delete lane because a gate makes that lane unusable for anything but an exact ratified
batch, and every safety property is re-derived at execution from ledger + tree, never read from the
batch.

**The grant.** `.owned-paths.yaml` gives `4.0.0_SA_CRO~SWEEP` membership in 5 lanes (`POD4`,
`CLOUD_OPS_OR_ETL`, `ANY_CTO`, `POD1`, `SHARED_OPAL_ETL`). `BASE_EXEC` and `POD2` were **deliberately
withheld** -- that withholding later blocked a mis-cut batch (see Addendum 7).

**Execution to date.** 7 batches: CRO's B-0001 (93) / B-0002 (500) / B-0003 (497) / B-0004 (484) /
B-0005 (500) / B-0006 (487), plus this seat's straggler commit `2b536176be` (8). Each CRO batch was
re-derived by this seat from the commit -- deletion-only, set-equal, all ARCHIVE, zero protected
charter -- not accepted from the executor's report. B-0001's `git revert` was executed and verified
byte-identical, discharging the ruling's s.7 acceptance condition: **recovery is a fact, not a claim.**

**Queue:** ~375 ARCHIVE files still tracked at last re-derivation (from 7,048 at session start; the
drop is partly execution and partly the `R-0022` correction).

## Next Steps

- **[`4.0.0_SA_CRO`]** B-0007 onward. Needs nothing from this seat -- the ruling permits the
  mechanism and the mechanism permits the batch.
- **[`4.0.0_SA_CRO`]** disposition the **4 held stragglers** in the ledger: `org/ka_testing/Dockerfile`
  + `.dockerignore` and `docs/deployment/BD_PORTAL_PUBLISHER_PLAN.md` (surviving files depend on them
  -- likely REFERENCE_KEEP or MIGRATE-with-citation-repair), and `data/yang_pkl/README.md` (lane
  `POD2`, needs a POD2 member or an amendment).
- **[`1.0.0_SA_CTO`]** rule the `org/rcg-sweep-audit.log` archive-MANIFEST coverage item (concurred:
  ADD, rare-bypass class). This seat owns the writer, so per SoD the coverage is authored by others.
- **[unowned, named]** extend C7 past the Python-package shape. `org/ka_testing` proved the general
  case live: a **KEEP** file (`docs/compose.yml`, `build: .`) depending on an **ARCHIVE** file. The
  generalisable check is "a surviving file references a deleted file by name". Residual risk 2 in the
  ruling; now evidenced twice.
- **[standing]** no install-all hook entry point (`.owned-paths.yaml:114`) -- a clone can hold the
  lane grant without the gate. Bounded to primary-laptop-only execution with the installer run as
  recorded batch prep.

---

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

## ADDENDUM 2, 01:45-02:05Z -- `load_batch` was first-row-wins on an append-only ledger (`f189e0c6f1`)

CRO attempted the live execution and hit a third defect in my gate. `load_batch` returned the
**first** row matching a batch id. On an **append-only** ledger that is strictly wrong, and it broke
two things at once: a batch could never leave `DRAFT` (an appended `RATIFIED` row was unreachable),
and **`executed_commit` could never become readable BY CONSTRUCTION** -- it is appended *after* the
deletion commit, so `R3`, and therefore the entire revert mode I had shipped an hour earlier, was
unreachable on any real ledger.

Worse than either bug: **this file's two ledgers had opposite resolution rules** -- labels last-wins
(R-0022), batches first-wins -- a latent trap for every future reader of either. Now harmonized.
Ruled: **last row wins WHOLESALE, no field merging**; an incomplete last row fails loud rather than
silently inheriting stale `paths`/`sha`/`count`.

**Why 16/16 missed it, and this is the transferable part: the fixture MUTATED the batch row in place
instead of APPENDING one, so it never exercised the append-only shape the real ledger has. A fixture
that violates the contract under test cannot test the contract.** Matrix 16 -> **18/18**, fixture now
appends, `RV1` re-passes through the live sequence rather than a pre-baked state.

**Three instances of one class in a single session, each found by running the live sequence and none
by reading:** CRO's prose-vs-ledger (pyiceberg), my C6 and revert-PERMIT gaps (fixture scope), and
this (fixture violating the contract). The pattern is not "test more" -- all three had complete,
correct deny suites. It is that **the permit side and the live artifact are where these hide.**

**A correction I owe on the record:** I told CRO my scratch-repo proof of `git commit --only`
isolation "generalizes" to `safe-commit`. It does not follow -- I generalized a scratch result to a
wrapper I had not tested. CRO's live run contradicted it. **But their causal claim has a confound I
flagged rather than accept:** between the two attempts *both* the wrapper and (plausibly) whether
foreign files were still staged differed, and `safe-commit` does use `git commit --only` at `:663`.
Recorded as **symptom observed, mechanism UNDETERMINED**, with the one-run discriminating test named.
Operationally moot: **ruled under Rule 14a** that a batch may execute via `git commit --only` with the
`Authorized-Deletion` trailer -- which bypasses nothing, because both gates are **git hooks** and fire
on any commit path. CRO's three DENIED entries in `org/rcg-sweep-audit.log` are the proof.

## ADDENDUM 3, 02:05-02:17Z -- B-0001 EXECUTED AND CLOSED (`86c4b5569d`)

**The first real deletion batch ran, and the s.7 acceptance condition is discharged.** Chain:
execute `099eb31879` -> `EXECUTED` row `28c0fcccd8` -> revert `48db734d1b` -> re-apply `d1c3980c4a`
-> closing row `f856de9536`. 93 files, 25,243 lines.

**Re-derived by me from the commits rather than accepted from the report** -- the habit this seat
exists for: exactly 93 deletions with **zero** non-deletion changes (C1 held in the wild, not just in
a fixture); deleted set **exactly** the declared 93 (0 extra, 0 missing); `git diff 67bbb6981d18
48db734d1b -- <path>` **empty**, so byte-identical restore; 0 tracked / 0 on disk at HEAD; 4 PERMITs
in the audit trail. **SoD held live** -- three mutating commits by `~SWEEP`, both ledger rows by base
CRO. **And the gates composed:** the first execute PERMITted at my gate and was then blocked by
`mass-deletion-check` until its trailer was corrected -- two independent gates, neither blinding the
other.

**Recovery is now a fact rather than a claim.** The PRD's whole safety case for `git rm` was
*"reversal is `git revert`"*, and until 02:08:57Z tonight nobody had ever run it.

**The correction I made to CRO's closure:** they reported "Cap 500." **It has not lifted.** s.7 gates
each ramp step on the prior batch's *CVO* verify closing clean; B-0001 discharged the **revert**
precondition only, and `D-0002` is unarmed pending Andrew's ferry. **500 is authorized-on-close, not
in force; batch 2 stays at 100.** *Earned is not granted -- and a ramp advancing itself on a
half-satisfied precondition is exactly the seam that fails six batches later when nobody remembers
which half was outstanding.*

**Confound resolved, in the wrapper's favour.** CRO ran the discriminating test and **retracted**
their own causal claim: with foreign staged files present, *both* commit forms passed C1 under a
cap-forced deny. `safe-commit` isolates correctly; `014714Z` is recorded **MECHANISM UNDETERMINED**.
*A plausible mechanism about a tool every agent uses was one message from entering the record as fact.*

Two protocol items folded: re-apply requires a fresh complete `RATIFIED` row (**ruled: keep C3 strict
-- the re-ratification row is not friction, it is the authorization**), and the standard sweep trailer
is `Authorized-Deletion: rcg/ledger/BATCHES.jsonl`.

## ADDENDUM 4, 03:16-03:45Z -- B-0002 (500 files) and a new defect class (`2481fa16a`)

CVO~B's independent verify of B-0001 closed CLEAN (`c11c4b61fb`, 26/26 re-derived, under its own
serial) at 03:16Z, discharging the cap-lift precondition. **B-0002 executed at 03:31Z: 500 files,
84 directory-complete dirs.** Verified here from the commit, not the report: **500 deletions, zero
non-deletions** (C1 held at 5x batch-1's size), **500/500 ARCHIVE** at HEAD re-derived, **0**
protected-charter intersections. Order checked as well as substance -- the CVO close preceded the
execution by 30 minutes with the discharge row between.

**A DEFECT CLASS I HAD NOT BEEN WATCHING FOR: the gate's SPEECH, not its verdict.** A 500-path list
piped through `xargs` **silently split into multiple `git` invocations** (measured 375/125). C2
correctly refused all three partial commits -- **but C2 cannot distinguish a partial invocation from
a genuine batch/tree divergence**, and its message asserted divergence. CRO chased two wrong theories
before the invocation count explained it.

> **A correct verdict that names the wrong cause is a correct verdict pointing at the wrong repair
> -- and it is harder to catch than a wrong verdict, precisely because the decision is right.**

Fixed both ways: C2's message now states it cannot tell the two apart and hints at splitting for any
batch over 100 paths; s.5.1 rules the standard large-batch form
`git commit --only --pathspec-from-file=<file>` (one invocation, cannot split). **B-0001's 93 paths
fit in one invocation by luck of size -- batch 1 passing was never evidence the form was sound.**

**Asked, not inferred:** who armed CVO~B. The verify is unimpeachable on substance, but `D-0002`'s
arm was routed through Andrew's ferry because CVO sits outside `R-0001` silence. Either answer
resolves something -- Andrew ferried (then `D-0002` is discharged and should stop being carried as
open at him) or the route came another way (a fabric-silence question better named now than at batch
6). Question outstanding with CRO.

## ADDENDUM 5, 04:26-04:45Z -- B-0003, and a defect category neither of us had (`90a5133cc`)

B-0003 deleted 497 `org/threads/` files (`dd5914aa2`). **Mechanically flawless**, re-derived here:
497 deletions, zero non-deletions, 497/497 ARCHIVE, 0 protected-charter, all under `org/threads/`,
and **zero record-shaped subpaths** (no `/logs/`, `/task_orders/`, `/handoffs/`, `/ledger/` hiding
where a charter glob might not reach).

**Then I tested the WARRANT rather than the mechanics.** The batch row called this the *"snapshot-copy
mass"* -- and copy-ness is mechanically decidable by blob hash, so I checked it against the tree at
the commit's parent:

> **217 of 497** had a surviving identical copy elsewhere. **280 did NOT.**
> 44% snapshot-copy, 56% unique content -- and the unique half is the threads' own primary records:
> `THREAD.json`, `TURN.json`, `CONTEXT_COMPILED.md`, `inline_notes.md`.

Nothing was destroyed and nothing was violated -- git history retains all of it, recovery is one
command, and the deletion may well be correct (5-month-old thread records, ARCHIVE, SCORE charter).
**The problem is the stated reason.** *"These were copies"* is a far stronger warrant than *"these are
old work records we judged archival,"* and a successor inherits whichever the row claims. The
pyiceberg prose-vs-artifact gap again, in a much more benign form -- **named at 497 rather than
discovered at 5,000.**

> ### A GATE CHECKS WHAT A BATCH *IS*; IT CANNOT CHECK WHAT DELETING IT *MEANS*.
> Every defect found tonight before this one was in the first column. This was the first in the
> second, and it was only catchable because copy-ness happens to be mechanically decidable. **Most
> warrants are not** -- which is why the operator states them and why the row's phrasing carries real
> weight.

Shipped a **uniqueness ADVISORY**: prints the duplicated/unique split per batch and names the unique
paths. **Denies nothing** -- exercised on a purpose-built fixture (3 duplicated + 1 unique with a
surviving copy outside the batch) and returns `rc=0`, matrix still 18/18. *An advisory that denies is
a gate, and handing CRO a surprise ceiling at 04:30 would have been the wrong way to make this point.*

## ADDENDUM 6, 04:55-05:15Z -- B-0004 accepted, and the false finding I nearly sent (`f5acbf5f3`)

CRO landed both items I asked for (B-0004 row carries the measured uniqueness ratio, warrant on
ARCHIVE-label grounds only; B-0003 correction row retires the copy claim with the 217/280 split).
B-0004 verified: 484 deletions, zero non-deletions, 484/484 ARCHIVE, 0 protected.

**But my first pass reported "3 paths not ARCHIVE" -- and it was FALSE.** My ad-hoc verification
script used `.split()` on git path output; B-0004 deleted a filename containing a **space**
(`...joe_brandenbur g_fix.md`); `.split()` shredded it into fragments that failed the label lookup.
**My instrument manufactured three findings.** I caught it because `g_fix.md` is not a plausible
path -- *not because I was being careful* -- and it never reached CRO.

Re-derived with `-z`: **all four batches clean. 1,574 deletions, 0 not-ARCHIVE, 0 protected.**

> **B-0001..B-0003 had passed that same broken script BY LUCK OF PATH CONTENT** -- none of those
> cohorts contained a space. **Third "passed by luck of the input" tonight**, after the xargs
> arg-limit split and B-0001's 93 paths fitting one invocation. The estate holds 35 tracked paths
> with spaces; naive `.split()` over `ls-files` yields **14 more tokens than there are files**.

Engine hardened to `-z` at 7 sites, with honest scope: **it was never broken on spaces**
(`.splitlines()` is correct there, which is why it permitted correctly). The residual it *did* have
is `core.quotepath` C-quoting non-ASCII paths -- a **C2 false DENY reading as divergence**,
fail-closed but misdirecting, exactly like the xargs split. Matrix 18/18; positive control confirms
all 35 space-bearing paths survive intact.

*And the repair bit twice: writing the backslash-zero escape through a heredoc put a real null byte
in the source -- the second time inside the comment warning about it. Separator is now `chr(0)`.*

## ADDENDUM 7, 05:20-06:00Z -- the stragglers taken (`2b536176be`), 8 of 12, and why 4 were held

Andrew-direct: *"take the 12 stragglers now."* Took **8**. Held 4, and the holds are the content.

**This was the least-gated deletion in the programme, and I said so in the commit.** `rcg-sweep-check`
fires on the `~SWEEP` **author identity**, so it does not fire for me; `mass-deletion-check`'s
threshold is 25, so 8 does not reach it. **No gate covered that commit.** I ran the gate's own checks
by hand rather than inherit a pass I was not entitled to -- C4/C5/C6/C7 all clean, uniqueness 1 copy
/ 7 unique, so the warrant is stated on **ARCHIVE-label grounds, not copy grounds** (the B-0003
lesson, applied to my own batch).

**HELD, and three for one reason: a surviving file depends on the deleted one.**

- **`org/ka_testing/Dockerfile` + `.dockerignore`** -- that tree is 67 tracked files: **63
  REFERENCE_KEEP + 2 KEEP + exactly these 2 ARCHIVE** -- and `docker-compose.yml`, labelled **KEEP**,
  carries `build: .`. **A KEEP file depends on an ARCHIVE file.** Deleting them leaves a 65-file
  project that looks intact and cannot build. The click specimen generalised past Python packages:
  **residual risk 2 of my own ruling, with a live specimen, found on MY batch.**
- **`docs/deployment/BD_PORTAL_PUBLISHER_PLAN.md`** -- cited by live Terraform at
  `infra/aws/terraform/bd-pipeline/lambdas.tf:231`.
- **`data/yang_pkl/README.md`** -- lane `POD2`, **not mine**. I had said I would take "the 12"; I can
  only take what I own. Routed, not quietly widened and not quietly dropped.

**Reference checks on what I DID take**, since three sat in live fabric-comms territory and *a name
appearing somewhere is not a dependency*: `session-startup.sh` had zero live references;
`agent-poller.py`'s `cl_liveness` mention is a **comment about REMOVED routing** naming the `.json`,
not the `.lock`; the `/drive` skill references the **base** `.last-drive-2.0.0_SA_COO`, never the
`~B` lane variant, and self-creates it anyway.

### The accident that proved the s.6 withholding was load-bearing

CRO's B-0006 first cut **failed to exclude my 12 stragglers**, and the **owned-paths gate DENIED**,
naming them exactly; all 12 restored intact. **That save existed only because I withheld `BASE_EXEC`
and `POD2` from the grant.** I could have granted them -- the sweep gate constrains the identity
anyway, and **every check would have passed**: the labels say ARCHIVE, the charter says SCORE, so
C4/C5/C6/C7 would all have permitted deleting `org/mcp/session-startup.sh` and `cl_liveness.lock`.
What stopped it was a **lane boundary I declined to widen for 12 files**; what made those two safe to
delete afterwards was **three reference checks by hand that no gate performs.**

> **"The grant is safe because a gate constrains it" is not a licence to take every widening the gate
> would tolerate.** Written into s.6 as a judgment call; demonstrated three hours later by an
> accident. **Defence in depth is not redundancy when the layers see different things.**

## Closed during the session

- ~~**[`4.0.0_SA_CRO`]** author + execute B-0001~~ -- **DONE.** 93 files, execute/revert/re-apply,
  s.7 acceptance discharged, verified independently by this seat.
- ~~**[`4.0.0_SA_CRO`]** adjudicate the C7 hit in `news_scanner/scripts/utilities/`~~ -- **DONE**,
  `R-0023`: `__init__.py` ARCHIVE -> KEEP, the package-whole law generalized from the click specimen.
- ~~**[Andrew]** ferry the CVO arm (`D-0002`)~~ -- **DISCHARGED, verified at source.** `D-0005`
  records Andrew personally provisioning `3.0.0_SA_CVO~B` as the RCG verify seat and ferrying the
  block himself; CVO~B's deliverable `c11c4b61fb` reads **VERDICT: CLEAN -- 26/26 PASS, zero
  contradictions**, citing s.7.2 item 3 as what it discharges. **No fabric-silence question: the
  route was human-carried end to end.** *Worth keeping: I asked rather than inferring, and the spawn
  log would have shown CVO~B coming live at 02:59Z with no visible cause -- exactly the shape that
  breeds a confident wrong inference. The answer existed only in Andrew's words and CRO's ledger row.*
- ~~**[CTO Base]** the tombstone-gate archive baseline finding~~ -- **CLOSED** by Base as a
  pre-registered transient (`14b3a3da7d` covered the log *after* the snapshot mint; fail-closed by
  design). Base then caught that my own `org/rcg-sweep-audit.log` was uncovered in that MANIFEST --
  concurred, ADD, authored by others per SoD since I own the writer.

## Open at session end

- **[`4.0.0_SA_CRO`]** batch 3 against the `org/threads` snapshot-copy mass, cap 500. **No further
  gate from me is required** -- the mechanism is what permits a batch.
- **[`4.0.0_SA_CRO`]** disposition the **4 held stragglers** in the ledger: the `ka_testing`
  Dockerfile pair and `BD_PORTAL_PUBLISHER_PLAN.md` (surviving files depend on them -- likely
  REFERENCE_KEEP or MIGRATE-with-citation-repair), and `data/yang_pkl/README.md` (needs a POD2 member
  or an amendment).
- **Standing residual:** no install-all hook entry point (`.owned-paths.yaml:114`). Until it exists a
  clone can hold the lane grant without the gate -- the one unsafe ordering in this design. Bounded
  to primary-laptop-only execution with the installer run as recorded batch prep.
