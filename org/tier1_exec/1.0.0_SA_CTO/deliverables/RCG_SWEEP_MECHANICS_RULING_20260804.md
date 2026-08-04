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

## 6. The grant, and separation of duties

`.owned-paths.yaml` gains **one** narrow lane for the sweep-executor identity, described as
gate-conditional and pointing at this ruling.

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

The PRD's entire safety argument for `git rm` over move-to-`archive/` is *"reversal is `git revert` /
`git checkout <sha> -- path`."* **That reversal has never been run.** A recovery path that has never
been executed is not a recovery path -- it is a belief about one, and this estate has a standing rule
that a passing assertion never mutated has never been tested. It costs one commit to convert the
belief into a fact, and it is the cheapest control in this document.

Ramp after a clean batch-1 including the revert exercise: 100 -> 500 -> uncapped, each step gated on
the prior batch's CVO verify closing clean.

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
