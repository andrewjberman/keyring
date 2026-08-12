---
name: integrate
description: Reconcile the two fabrics' branches (CLOUD <-> SITEZ) so each can read the other's work -- the MSTR-to-MSTR cross-device merge protocol. Measures true divergence and the OVERLAP SET (the only thing that can conflict), computes conflicts without touching a working tree, agrees ONE resolution across both fabrics rather than two, merges (NEVER rebases), and verifies from the remote. Use when both fabrics are quiet, before a device reboot or a long dark window, when a citation from one fabric does not resolve on the other, or when either MSTR asks to integrate. Parity is maintained "to the extent convenient/relevant" (Andrew) -- the fabrics deliberately work separate projects, so a healthy overlap is ~1% and a LARGE overlap is itself the finding.
---

# /integrate — the cross-fabric reconcile (CLOUD <-> SITEZ)

**Who runs it:** `0.0.0_AB_MSTR` (laptop) and `0.0.0_AB_MSTR~Z` (site Z), together. Both halves
are MSTR acts because both are shared-branch pushes (LD-0367/LD-0368: only the two MSTRs push a
shared branch). A lane agent invoking this stops at Step 0 and routes to its MSTR.

**What it is for (Andrew, 2026-08-12):** *"we do want to maintain parity to the extent that is
convenient/relevant. I try to make sure that the fabrics always work on separate projects so
there is zero or very little overlap to make this easy to manage."* **Parity is a convenience
goal, not an invariant** — this is not a merge-to-one-trunk. Each fabric keeps its own branch as
its working trunk; integrating means **each side can READ the other at a known head**.

**FIRST MEASURED RUN (2026-08-12, the one this skill is written from):** base 34h old, CLOUD +387
/ SITEZ +438, 900 files touched, **overlap 7 files (0.78%)**, of which 2 auto-merged and 5 needed
a human. That is the shape to expect when the separate-projects discipline is holding.

---

## Step 0 — Identity + quiet check

- Confirm you are an MSTR serial. If not, STOP and route to yours.
- **Both fabrics should be QUIET** (no seat mid-commit). Not a hard gate — a reconcile during
  live work just means more churn arrives after you measure — but the cheapest run is a quiet one.
- Confirm the bus is armed (`/agentbus status`): this protocol is a two-party exchange, and the
  bus is the only live channel between devices.

## Step 1 — ⛔ VERIFY YOUR OWN CLONE IS COMPLETE (do this BEFORE measuring anything)

```bash
test -f .git/shallow && echo "SHALLOW -- $(wc -l < .git/shallow) cut point(s)" || echo "complete"
```

**A SHALLOW CLONE SILENTLY FALSIFIES EVERY NUMBER IN STEP 2.** Measured on the first run:
a shallow laptop clone reported **no common ancestor** (`git merge-base` rc=1), **24,201 vs 370**
commits apart, and **23,804 overlapping files**. The true figures were 387 / 438 / **7**. The
grafted boundary commit reads as a parentless ROOT (`rev-list --max-parents=0` returns it) while
`git cat-file -p <that commit>` plainly shows a parent your object store does not have.

**Fix before proceeding, and re-check:**
```bash
git fetch --unshallow origin        # or: git fetch --deepen=<n> if unshallow is too heavy
test -f .git/shallow || echo "now complete"
```
**BOTH SIDES RUN THIS.** The trap is symmetric — a shallow *peer* reports their truncation as
your divergence, and neither of you can see it from your own box.

> This step is first because the failure is silent and confident: rc=1 from `merge-base` looks
> exactly like "unrelated histories," and the counts look exactly like a real divergence.

## Step 2 — Measure the divergence and, above all, THE OVERLAP SET

```bash
git fetch origin
BASE=$(git merge-base origin/CLOUD origin/SITEZ)
echo "base $BASE  $(git log -1 --format='%cI %an' $BASE)"
git rev-list --count origin/SITEZ..origin/CLOUD    # CLOUD ahead
git rev-list --count origin/CLOUD..origin/SITEZ    # SITEZ ahead

git log --name-only --format= $BASE..origin/CLOUD | sort -u | grep -v '^$' > /tmp/a.txt
git log --name-only --format= $BASE..origin/SITEZ | sort -u | grep -v '^$' > /tmp/b.txt
comm -12 /tmp/a.txt /tmp/b.txt          # <-- THE OVERLAP SET
```

**The overlap set is the whole job.** Everything outside it merges by construction — two fabrics
adding different files cannot conflict. **Print its COUNT beside the touched totals** (e.g.
"7 of 900 = 0.78%") so the number carries its own frame.

**READ THE SIZE AS A SIGNAL:**
| overlap | meaning |
|---|---|
| ~0–2% | the separate-projects discipline is holding; reconcile is mechanical |
| 5–15% | the fabrics have started working the same surfaces — worth naming to Andrew, since it is HIS premise that keeps this cheap |
| >15% | **stop and surface it.** Something is being worked twice; that is a coordination finding, not a merge problem, and merging it silently hides the duplication |

**Expect the overlap to be SHARED-SURFACE files** — the ones both fabrics legitimately edit:
`CLAUDE.md`, `.owned-paths.yaml`, `docs/doctrine/*`, `org/ref/*` protocols, the ATOM_DECOMP
package, registry/index files. A *project* file in the overlap is the surprise worth reading.

## Step 3 — Compute the conflicts WITHOUT touching a working tree

```bash
git merge-tree --write-tree --name-only origin/CLOUD origin/SITEZ
```
rc=0 clean, rc=1 conflicts. Output lists conflicted paths, then the auto-merge/CONFLICT lines.

**Why not a trial `git merge`:** the working tree usually holds live lane state (on the first run:
17 modified tracked files, 125 untracked). `merge-tree` is a pure computation — it cannot strand
you mid-merge, and it needs no `--abort`.

**Classify each conflict before resolving:**
- **CONTENT on a shared-law file** (CLAUDE.md, doctrine, protocols) — usually **both sides ADDED
  rules blind to each other**, so the resolution is a **UNION, not a pick**. Only where both
  edited the *same row* is there a real adjudication, and **that belongs to the law owner
  (CTO/CTO~Z), not to MSTR.**
- **ADD/ADD on the same path** — often a **NAMESPACE COLLISION**, not a content dispute: two
  fabrics independently created the same filename (e.g. a per-fabric drive log). **Keep both,
  disambiguated per fabric.** Deleting either destroys a real record.
- **CONTENT on a code/schema artifact** — auto-merge is **not** semantic correctness. Route the
  merged result to that artifact's steward for a read even when git reports clean.

## Step 4 — Agree ONE resolution, then order the merges

**Exchange over the bus before either side merges.** Each MSTR sends: their Step-1 clone status,
their Step-2 counts + overlap set, their Step-3 conflict list, a per-file resolution proposal, and
**anything on their branch NOT ready to travel** (in-flight, superseded, fabric-local by design).

**ORDER: whoever merges FIRST resolves; the other merges the RESULT.** The point is **one
resolution, not two** — if both sides resolve the same five files independently, the resolutions
themselves diverge and the next reconcile inherits a worse conflict. Direction is negotiable
(smaller delta first is a reasonable default); *singleness* of the resolution is not.

⛔ **MERGE, NEVER REBASE** — `git merge`, no `--rebase`, no exceptions. Rewriting shared history
across two fabrics is NEVER#7 and a non-conflicting rebase result is luck, not correctness.

⛔ **NEVER resolve another fabric's law text unilaterally.** Union what composes; route genuine
same-row collisions to the law owners with both versions quoted.

## Step 5 — Execute your half

```bash
git fetch origin
git merge origin/SITEZ            # (or origin/CLOUD from the site-Z side)
# resolve ONLY the overlap set, per the agreed resolutions
git push origin CLOUD             # your own branch; the deploy gate may sweep for minutes
```
- The pre-push safe-deploy gate verifies deploy-scope scripts against S3 — **a slow push is the
  gate working, not a hang.** Run it backgrounded and read the result.
- **Push carries every lane's committed work, not just yours** — that is the LD-0367 rationale.
  Enumerate the payload (`git log --format='%an' origin/CLOUD..HEAD | sort | uniq -c`) so you can
  say what you carried.

## Step 6 — Verify from the REMOTE, and hand the peer a head they can check

```bash
git ls-remote origin refs/heads/CLOUD          # the oracle
git rev-parse HEAD                              # must match
git ls-tree origin/CLOUD <a file the peer needs>   # blob-verify what they asked for
```
**Send the peer the landed HEAD and the blob hash of anything load-bearing.** Measured on the
first run: a citation sent before the integrator leg ran did not resolve on the peer's fabric and
was correctly recorded as UNDISCHARGED — **a path is not a citation until it is on the remote.**
The peer verifies against the remote, never against your report.

## Step 7 — Close

- Post-merge, ask each affected steward to read their artifact (auto-merged ≠ semantically right).
- Record the run: base, both counts, overlap size + set, resolutions taken, both landed heads.
- **Ledger it** (MSTR commits touching non-record paths need an `LD-NNNN`).
- If the overlap exceeded the Step-2 band, **surface it to Andrew** — it is his separate-projects
  premise that keeps this cheap, and its erosion is a fact he would want early.

---

## Invocation forms

| form | behavior |
|---|---|
| `/integrate` | full protocol, Steps 0-7, coordinated with the peer MSTR |
| `/integrate status` | Steps 1-3 only: clone check, divergence, overlap set, conflict dry-run. Changes nothing, sends nothing. The read to run before deciding whether a reconcile is even worth it |
| `/integrate execute` | Steps 5-6 only — **only after a peer-agreed resolution exists.** Never the first call |

## Discipline notes

- **Parity is convenience, not an invariant.** If a reconcile is expensive, that expense is
  information: the fabrics have started overlapping. Say so rather than absorbing it.
- **Never assume the peer fabric is alive.** Seats die with a device and nothing respawns them; a
  quiet bus is wind-down, not fault. If the peer cannot answer, do NOT resolve their law files
  alone — merge what composes, leave the contested set, and say what you left.
- **Both directions are separate acts.** "SITEZ->CLOUD landed" says nothing about CLOUD->SITEZ.
  Report each with its own landed head.
- **The overlap set is the deliverable of Step 2**, not the commit counts. Counts tell you how
  much happened; the overlap tells you how much can *hurt*.
