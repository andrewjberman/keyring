# RCG SWEEP MECHANICS -- CTO RULING

**Ruling id:** CTOB-RCG-001
**Ruled by:** `1.0.0_SA_CTO~B` (RCG execution-coordination seat, spawned Andrew-direct per RCG `R-0021`)
**Date:** 2026-08-04
**Discharges:** `NFRA_REPOCOHERENCEGRAPH` ferry item `D-0001` item 5, ferried to this seat via `D-0004`
**Authority basis:** `R-0021` (Andrew spawned this seat as the CTO-side counterpart for execution gating);
PRD `docs/architecture/NFRA_REPOCOHERENCEGRAPH_PRD.md` s.13
**Blocks/unblocks:** the ARCHIVE execution queue -- 2,945 files as re-derived at `R-0022`

---

## 1. The ask

> *"RULING NEEDED before first executed sweep: mechanics for ratified ARCHIVE batches that delete
> files across foreign owned-paths lanes (proposal: scoped audited sweep-executor authorization keyed
> to ledger-cited batches)."* -- `D-0001` item 5

## 2. The problem, stated mechanically

Two live gates stand between a ratified batch and the tree, and **both are correct**:

| Gate | Where | Why it fires on a sweep |
|---|---|---|
| `owned-paths-check.sh` | pre-commit stage 2 | `4.0.0_SA_CRO` owns `rcg/**` and nothing else. A batch deleting `infra/`, `org/`, `data/`, `docs/` is out-of-lane on every path. |
| `mass-deletion-check.sh` | commit-msg | BLOCK mode since 2026-07-11, threshold 25 deleted tracked files. Verified live this session: `--mode` reports `effective mode: block`. |

Neither is a bug to be worked around. The `mass-deletion` gate already carries the governing doctrine,
ruled by this seat's own base lineage on 2026-07-09:

> **"A mass deletion of tracked files is LEGAL. An UNATTRIBUTED one is not."**
> *The discriminator is ATTRIBUTION, not COUNT.*

**This ruling does not replace that doctrine. It supplies the missing half of it: what attribution has
to MEAN when the deletion is 2,945 files wide and crosses every lane in the estate.**

## 3. Options rejected, and why

**(a) Grant CRO a broad write lane.** Rejected. `owned-paths` cannot distinguish a delete from a
write, so "broad enough to sweep" is identically "broad enough to rewrite the estate." It converts a
single-writer operator seat into the widest lane in the fabric to solve a deletion problem.

**(b) Per-batch audited override** (`GIT_COMMIT_AUTHOR_OVERRIDE`, `FORCE_DELETE=1`). Rejected, and
this is the important rejection. Both bypasses exist and both are audited, so this *looks* compliant.
But CLAUDE.md Rule 21 already names the failure: **a repeat override for one intent is a coverage
gap -- build the tool.** An override used once per batch across a multi-week sweep is not an override;
it is the gate being off, with a logfile describing how often.

**(c) Trailer-keyed authorization only** -- i.e. lean on the existing `Authorized-Deletion:` trailer.
Rejected as *insufficient*, not wrong. The existing gate accepts any trailer that RESOLVES: an
`LD-####`-shaped id, or a path to a file that exists. It never checks that the cited authority
authorizes **these** paths. At 25 files that is proportionate. At 2,945 it means a batch could cite a
real ledger and delete an arbitrary set. **Attribution that does not bind to content is a citation,
not a control.**

## 4. THE RULING

> ### AUTHORITY ATTACHES TO THE BATCH, NOT TO THE SEAT.
>
> A sweep deletion is legitimate because a **ratified, pre-committed, content-bound batch** says those
> exact paths go -- never because of who is holding the keyboard. Therefore the authorization is keyed
> to the batch, and the executing identity is constrained, by a gate, to doing nothing except
> executing batches exactly.

Three consequences follow, and they are the whole design:

1. **The executing identity may be granted a broad delete lane, because a gate makes that lane
   unusable for anything but an exact ratified batch.** The grant is safe *by construction*, not by
   the grantee's care.
2. **The gate keys on the AUTHOR IDENTITY, not on the trailer.** A gate that fires only when you
   declare a sweep is evaded by not declaring one. Firing on identity means every commit that
   identity ever makes is checked, so there is no un-gated shape available to it.
3. **Every safety property is RE-DERIVED at execution time from the ledger and the tree -- never
   read from the batch file.** The batch says *which paths*; it is never trusted about *whether they
   may go*. A proposal authored by the executing seat cannot also be the evidence that the proposal
   is safe.

### 4.1 Why clause 3 is not paranoia -- it was falsified on day one

This ruling's own gating pass found it. The delegated labeling round (`R-0020`) marked **4,103 files
under `infra/aws/lambda/layers/pyiceberg-nessie-deps/` as ARCHIVE at HIGH confidence** -- inside a
subtree Andrew had *explicitly ratified as KEEP* at `R-0019` ("infra/aws/lambda SPLIT -- layers/ +
v2_portal/ KEEP"). Ratified cohort verdict, contradicted at file grain, silently, because a batch is
built from file labels and nobody re-read the cohort ruling.

The specimen, inside one vendored package (`.../python/click/`):

```
ARCHIVE  __init__.py     <- the package entry point
ARCHIVE  core.py
KEEP     decorators.py, termui.py, formatting.py, _termui_impl.py, _textwrap.py, _winconsole.py
```

Executing that deletes `click`'s entry point while keeping six of its modules: **not a disposition
anyone would defend, and not a judgment call -- structurally incoherent.** The residue is worse than
either extreme; 65 orphans that make the tree look present while it cannot import. And the tree is
build-load-bearing (`infra/aws/terraform/shared-infra/layers.tf:9` builds layers from these manifests).

Corrected by CRO at `R-0022` (4,103 rows ARCHIVE -> MIGRATE), and CRO's own sweep then found **three
more contradiction sites** of the inverse shape (46 subtrees checked, 4 fired). ARCHIVE queue fell
**7,048 -> 2,945**.

**Two of this ruling's checks (`C4`, `C6`) exist because of that finding, and one (`C7`) is named
after its specimen.** They are not hypothetical hardening.

## 5. MECHANISM -- `rcg-sweep-check`

A pre-commit gate, `.tools/git-hooks/rcg-sweep-check.sh`, wired by a tracked idempotent installer.

**Trigger:** `GIT_AUTHOR_NAME` resolves to the sweep-executor identity. Unconditional for that
identity -- there is no opt-in and no trailer to forget.

**Verdict:** rc 0 = permit · **any** other condition = DENY. There is no warn mode and no
cannot-evaluate pass: if the gate cannot establish a property, that is a DENY.

| # | Check | Rationale |
|---|---|---|
| **C1** | **DELETION-ONLY.** Every staged change is `D`. Zero `A/M/C/R/T`. | The single check that makes a broad lane safe. A sweep that can add or modify a file is not a sweep. Note `R` is excluded deliberately: a rename is a *move*, which is the MIGRATE path, not this one. |
| **C2** | **EXACT SET EQUALITY** with the batch path list, **both directions**, denominator printed. Missing-from-commit and extra-in-commit are both DENY. | "Subset" is not good enough in either direction: a superset deletes unratified files, a subset means the batch and the tree have silently diverged. |
| **C3** | **BATCH IS PRIOR-COMMITTED** -- present at `HEAD`, unmodified in this commit. | SoD. The executor may not author its own authorization in the same act, and a prior commit is a reviewable one. |
| **C4** | **RE-DERIVED LABEL** = `ARCHIVE` for every path, resolved from `LABELS.jsonl` **at HEAD** under last-row-per-path (the resolution semantics defined at `R-0022`). | Never trusted from the batch. This is the check that catches a batch built from a stale vintage. |
| **C5** | **RE-DERIVED CHARTER** handling = `SCORE` for every path. Any `PROTECT` / `APPEND_ONLY` / `EXCLUDE` is a DENY. | The protected-class fence, re-asserted at the last reversible moment rather than inherited from the proposal. |
| **C6** | **COHORT-RATIFICATION SUPREMACY.** No path may sit under a subtree carrying an `andrew_ratification`-sourced verdict that contradicts `ARCHIVE`. | **The pyiceberg check.** An explicit Andrew ratification outranks a delegated file label wherever they overlap -- `R-0020` reserves exactly this ("Andrew retains override on everything"). Mechanised so it is not a thing anyone has to remember. |
| **C7** | **PACKAGE COHERENCE.** DENY if the batch deletes an `__init__.py` from a directory retaining surviving tracked `.py` files. Partial-directory deletions are reported with counts. | **The click check.** Cheap, exact, no heuristics -- and it catches the precise defect that was queued for execution tonight. |
| **C8** | **SIZE CAP.** Batch <= the ramp cap in force (s.7). | Blast-radius bound while the chain is young. |

**Where it sits:** pre-commit, not commit-msg. Its sibling `mass-deletion-check` is commit-msg
*because it must read the trailer*; this gate reads the index and the ledger, both available earlier,
and pre-commit is upstream of `owned-paths` in the same invocation. `mass-deletion-check` continues to
apply unchanged -- batches still carry `Authorized-Deletion: <batch id>`, so the estate-wide deletion
audit trail stays complete and one gate does not blind the other.

### 5.1 The batch artifact -- contract only

`rcg/**` is CRO's single-writer lane and I do not write it. This ruling therefore specifies the
**contract**, and CRO owns the layout:

- An **append-only** batch record carrying, per batch: `id`, `status` (`RATIFIED` before execution),
  the **full explicit path list** (no globs -- a glob re-expands at execution against a different
  tree), a `sha256` over the sorted path list, the `count`, and the citing `ruling` id.
- Batch files are listed in `rcg/MANIFEST.yaml` (a prefix entry is fine) so the item-3 gate keeps the
  folder clean as batches accumulate.
- **No glob, ever.** The whole design rests on the path set being fixed at ratification time.

**COMMIT FORM FOR LARGE BATCHES -- `git commit --only --pathspec-from-file=<file>`.** Added
2026-08-04 after it cost a live diagnosis on B-0002: a 500-path list piped through `xargs` **silently
splits into several `git` invocations** past the arg limit (measured: a 375/125 split). The gate
correctly refused all three partial commits on C2 -- but **it cannot distinguish a partial invocation
from a genuine batch/tree divergence**, so a correct verdict pointed at the wrong repair for two
rounds. `--pathspec-from-file` is a single invocation and cannot split. B-0001's 93 paths fit in one
invocation *by luck of size*, which is why batch 1 never surfaced it. C2's deny message now carries
the hint for any batch over 100 paths.

## 6. The grant, and separation of duties

The sweep-executor identity is **`4.0.0_SA_CRO~SWEEP`**.

> **AMENDED 2026-08-04, same session, against my own text.** This section first said the grant is
> *"one narrow lane."* **It is not, and I only found that by measuring instead of asserting.**
> `owned-paths` resolves a lane **per path**, and a sweep spans every root -- so there is no single
> lane to grant. Measured against the live 2,945-path queue: the queue touches **10 distinct lanes**,
> of which **1,796 paths (61%) were already reachable** by that identity and needed no grant at all.
> Seven lanes denied. *A ruling that specified a mechanism it had not measured would have sent the
> executor to an audited override on first contact -- the exact outcome s.3(b) rejects.*

**Granted: 5 lane memberships** -- `POD4` (778 paths), `CLOUD_OPS_OR_ETL` (160), `ANY_CTO` (130),
`POD1` (41), `SHARED_OPAL_ETL` (28). Each carries an inline marker naming this ruling.

**NOT granted, deliberately: `BASE_EXEC` (11 paths) and `POD2` (1).** Widening the fabric's most
sensitive lane -- 3 members -- to reach 12 files, 6 of them deployment markdown, is a bad trade, and
"the grant is safe because a gate constrains it" is not a licence to take every widening the gate
would tolerate. **Those 12 execute under the ORDINARY path instead**: an exec seat already holding
`BASE_EXEC` deletes them in a normal attributed commit (`Authorized-Deletion:` trailer, the 2026-07-09
doctrine, unchanged). The sweep identity never touches `BASE_EXEC`. Net reach: **2,933 of 2,945.**

**CONTROL RUN, because a grant is exactly the kind of change that quietly does more than it says.**
After the amendment, re-measured: `4.0.0_SA_CRO~SWEEP` reaches 2,933; **`4.0.0_SA_CRO` (base) is
UNCHANGED at 1,796.** The suffix-to-base auto-permit in `owned-paths-validate.py:125-160` runs
suffix -> base only, so granting a lane to `~SWEEP` cannot widen the base seat -- now confirmed
empirically, not merely read. Negative controls held: `CLAUDE.md` DENY for both identities,
`org/tier0/ledger/**` DENY, and an unrelated seat's access was untouched.

**One honest asymmetry to know about:** `owned-paths` permits `~SWEEP` on `docs/doctrine/**` (it
falls in a granted lane), while check **C5** denies it (PROTECT charter). The lane is more permissive
than the gate there. That is defense in depth working in the intended direction -- the *gate* is the
binding constraint, and the lane never needed to be the tight one -- but it should be read as
deliberate rather than discovered later and mistaken for a hole.

| Role | Held by | Note |
|---|---|---|
| Designs + rules the mechanics | `1.0.0_SA_CTO~B` | this document |
| **Commits the grant (grantor)** | `1.0.0_SA_CTO~B` | `.owned-paths.yaml` is `ANY_EXEC_OR_AE`; follows the `@56ef220877` precedent where base CTO granted CRO's `rcg/**` lane |
| Executes batches (grantee) | `4.0.0_SA_CRO` | **grantee-only** -- authors no part of its own authorization, per its own standing posture |
| Independent per-batch verify | `3.0.0_SA_CVO` | RCG `D-0002`, dormant until the first executed batch; **Andrew ferries the arm** (CVO is outside R-0001 fabric silence) |
| Sovereign | Andrew | override on any label, any batch, at any time |

**The grantee never commits any part of its own authorization.** That is why the broad lane is
tolerable: the seat that benefits from it did not write it, and cannot use it for anything the gate
does not permit.

## 7. Ramp, and the acceptance condition that is not negotiable

**Batch 1** is the declared `archive/` directories cohort (~400 files post-`R-0022`), **capped at 100
files for the first execution.** Then:

> ### THE REVERT MUST BE EXERCISED ON BATCH 1 BEFORE BATCH 2 IS AUTHORED.
> Execute -> verify the deletion -> **`git revert` the batch commit** -> verify every file is
> restored byte-identical -> re-apply. Only then does the cap lift.

### 7.1 The restore leg had no legal author -- AMENDED 2026-08-04, same session

**A defect in this ruling as first written, found by `4.0.0_SA_CRO` reading the gate's source before
executing and declining to work around it.** A revert of a deletion batch is **additions**, which
**C1 denies** -- and the sweep identity is the **only** identity that can reach those paths, because
granting it the delete lanes in s.6 is what made it so.

> Measured on B-0001 (93 paths, lane `POD4`): `4.0.0_SA_CRO~SWEEP` **93/93**;
> `1.0.0_SA_CTO~B`, base CTO, MSTR, COO all **0/93**.

**So the recovery path was structurally unauthorable from the moment the grant landed: the one seat
able to restore was the one seat forbidden to.** Nobody would have found that by reading -- the deny
suite was complete *and correct*. It is the **PERMIT side of the revert leg that was never driven**,
and a revert-mode deny suite was vacuously complete because nothing could legally permit a restore at
all. Precisely the lesson C6 had already taught this session, recurring one layer up.

**Fix: a REVERT mode, safe the same way C2 is -- it cannot introduce content.**

| # | Check |
|---|---|
| **R1** | **ADDITION-ONLY.** Zero `D/M/R/T`. |
| **R2** | **EXACT SET EQUALITY** with the batch list, both directions. A partial restore leaves the tree in neither state. |
| **R3** | The batch's **`executed_commit`** is recorded (a separate commit, after execution). Absent, there is nothing to restore *from* -- `CANNOT EVALUATE`. |
| **R4** | **CONTENT IDENTITY.** Every staged blob is **hash-identical** to the blob at the parent of `executed_commit`. **You may restore exactly what was deleted, and nothing else.** |

Invocation: `RCG_SWEEP_MODE=revert RCG_BATCH_ID=B-0001 git commit ...`

The PRD's entire safety argument for `git rm` over move-to-`archive/` is *"reversal is `git revert` /
`git checkout <sha> -- path`."* **That reversal has never been run.** A recovery path that has never
been executed is not a recovery path -- it is a belief about one, and this estate has a standing rule
that a passing assertion never mutated has never been tested. It costs one commit to convert the
belief into a fact, and it is the cheapest control in this document.

Ramp after a clean batch-1 including the revert exercise: 100 -> 500 -> uncapped, each step gated on
the prior batch's CVO verify closing clean.

### 7.2 B-0001 CLOSED 2026-08-04 ~02:12Z -- the acceptance condition is DISCHARGED

The full chain ran and was **independently re-derived by this seat from the commits, not accepted from
the executor's report**: execute `099eb31879` (exactly 93 deletions, **zero** non-deletion changes --
C1 held in the wild) -> `EXECUTED` row `28c0fcccd8` -> **revert `48db734d1b`** -> re-apply
`d1c3980c4a` -> closing row `f856de9536`. Re-derived here: deleted set **exactly equal** to the
batch's declared 93 (0 extra, 0 missing); `git diff 67bbb6981d18 48db734d1b -- <path>` **empty**, so
the restore was byte-identical; 0 tracked and 0 on disk at HEAD after re-apply. Gate audit carries
four PERMITs (`execute`/`execute`/`revert`/`execute`).

**SoD held in practice, not just on paper:** all three mutating commits authored by
`4.0.0_SA_CRO~SWEEP`; both ledger rows by base `4.0.0_SA_CRO`. **And the gates composed:** the first
execute PERMITted here and was then blocked by `mass-deletion-check` until its attribution trailer was
corrected -- two independent gates, each doing its own job, neither blinding the other.

> **RECOVERY IS NOW A FACT RATHER THAN A CLAIM.** The PRD's safety case for `git rm` -- *"reversal is
> `git revert`"* -- has been executed end-to-end and verified byte-identical. That is what s.7 was for.

**Three protocol items folded from the live run:**

1. **RE-APPLY REQUIRES A FRESH COMPLETE `RATIFIED` ROW.** Under last-row-wins the re-apply leg
   correctly C3-denied on `status=EXECUTED`. **Ruled: keep C3 strict; do NOT add a re-execution-
   permitting status.** Re-applying a deletion *after* a revert is a genuine authorization decision,
   and the re-ratification row is not friction -- **it IS the authorization.** Widening a status
   vocabulary to auto-permit re-execution would trade an explicit act for convenience in the one gate
   that must not have any.
2. **STANDARD SWEEP TRAILER: `Authorized-Deletion: rcg/ledger/BATCHES.jsonl`.** The existing gate
   accepts an `LD-####` id or an existing file path; the batch ledger is the semantically exact
   referent -- the attribution *is* the batch record.
3. **THE CAP HAS NOT LIFTED YET.** The ramp reads *"each step gated on the prior batch's CVO verify
   closing clean."* Batch 1 discharged the **revert** precondition; the **CVO** precondition is
   outstanding because `D-0002` is unarmed pending Andrew's ferry. So 500 is **authorized-on-close,
   not in force.** Batch 2 stays at 100 until CVO's B-0001 verify closes clean. *Earned is not
   granted, and this is exactly the seam where a ramp quietly advances itself.*

**One confound resolved, in the wrapper's favour.** CRO's live claim that `safe-commit`'s hook view is
full-index was **retracted after running the discriminating test**: with foreign staged files present,
**both** commit forms passed C1 under a cap-forced deny. `safe-commit` isolates correctly (`:663`),
and the 014714Z C1 deny's mechanism is recorded **UNDETERMINED** rather than attributed. *A plausible
mechanism about a core tool was one message away from entering the record as fact.*

## 8. Scope -- what this ruling does NOT authorize

- **`MIGRATE` never executes here.** 5,715 files post-`R-0022`, dominated by vendored-dependency trees
  whose parent functions are live. That is the layer-refactor queue with citation repair, a different
  mechanism with a different gate.
- **`CONTESTED` never executes.**
- **No `git rm -r` on a directory.** Explicit path lists only (s.5.1).
- **History is never rewritten.** `git revert` forward, never `rebase`/`filter-branch` -- CLAUDE.md
  NEVER#7 is untouched by this ruling.
- **This does not lift `R-0001` fabric silence** for any seat other than the counterpart relationship
  `R-0021` established.

## 9. Residual risks, stated rather than closed

1. **`C4`/`C6` read the ledger at `HEAD`, and the ledger's authority is a delegated round.** The gate
   enforces internal consistency between ratification and execution; it cannot tell you a delegated
   label was *substantively* right. That is what `R-0020` traded away deliberately and what Andrew's
   standing override and the CVO per-batch verify exist to catch.
2. **`C7` catches the Python-package shape only.** The general "partially gutted tree" class is
   reported, not denied. A vendored JS/`node_modules` or a data tree with an index file has the same
   failure mode and no equivalent check. Named, not solved.
3. **The gate is one more un-installed-by-default hook.** The single install-all entry point remains
   the real, named, unbuilt item recorded at `.owned-paths.yaml:114`. Until it exists, a fresh clone
   or a second device has the lane grant but not the gate that constrains it -- **which is the one
   ordering in this design that is unsafe.** Mitigation until then: batches execute **only** on the
   primary laptop, and the installer must be run and its output observed as part of batch prep.

## 10. Verification of this ruling's own claims

Every number here was re-derived by this seat from committed artifacts, not carried from a summary:
ARCHIVE 7,048 (pre-`R-0022`) counted from `rcg/ledger/LABELS.jsonl`; 7,048/7,048 confirmed still
tracked against `git ls-files`; 7,048/7,048 confirmed under `SCORE` charters by running
`rcg/charters.yaml` matching directly; the `R-0019`/`R-0020` contradiction confirmed at source in
`rcg/rulings/RULINGS.jsonl`; `mass-deletion-check` BLOCK mode confirmed by running its own `--mode`
self-check surface. The hand-off's `7,031` figure was **stale by 17** -- benign in itself, and the
reason **`C2` re-derives the count instead of trusting a number anyone typed.**

---

*Sweep execution is authorized subject to every condition above. Until `rcg-sweep-check` is
implemented, installed, and exercised on both its deny and permit paths, no batch executes -- the
ruling permits the mechanism, and the mechanism is what permits a batch.*
