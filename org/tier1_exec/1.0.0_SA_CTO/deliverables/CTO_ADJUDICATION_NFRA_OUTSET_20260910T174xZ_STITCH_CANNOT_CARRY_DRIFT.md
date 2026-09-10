# CTO ADJUDICATION — `NFRA_OUTSET` — "CONTINUOUSLY STITCHED" RESOLVED. THE STITCH **CANNOT** CARRY THE DRIFT MEASURE, AND ANDREW SUPPLIED THE REASON HIMSELF.

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-10 ~17:4xZ · **Class:** an L4 design ruling on Andrew's
returned question, unblocking `2.0.0_SA_COO`, whose registered summary read *"gated on his stitching answer."*

---

## THE QUESTION, VERBATIM AND ENTIRE

> 3) Explain what you mean by plain english here? If we already have a stitch mechanism ride that,
> although I thought you were talking about "uncommitted" material, of which the stitch should be for
> commits.

**Two things in one sentence: a request for an explanation, a CONDITIONAL GRANT, and — carried inside the
aside — a FACT CLAIM about what the drift measure measures.** I answered the fact claim first, because a
conditional whose premise is unmeasured is not answerable.

---

## 1. WHAT "PLAIN ENGLISH" MEANT, SINCE HE ASKED DIRECTLY

I offered him two readings of his own phrase *"continuously stitched"*. **"Ride the stitch mechanism"** =
the drift publish becomes a leg of the estate's existing stitch machinery, firing when that machinery
fires. **"Plain English"** = *"stitched"* carries no technical referent at all and he simply means
**seamless / always-current**, in which case the implementation is an ordinary short repeating timer on
the device and the word "stitch" points at nothing in the codebase. That is the whole of the distinction.
It was a fork about WHOSE CLOCK the measure runs on, and nothing more.

## 2. HIS ASIDE IS CORRECT ON BOTH HALVES, AND IT IS THE RULING

⛔ **HALF ONE — THE DRIFT MEASURE IS EXACTLY "UNCOMMITTED" MATERIAL, AND HE IS THE ONE WHO DEFINED IT SO.**
`org/modules/heatmap/object_freshness.py:84-93` @`9554733409`, the function's own name and docstring:

> `def uncommitted_writes(root, now_ts)` — *"WRITES NOT CONNECTED TO A GIT COMMIT -- the working-tree
> drift signal (**Andrew-direct 2026-06-25**): local filesystem edits / new files that exist on disk but
> are not in any commit. This is the LOCAL->GIT layer. Two classes, from `git status --porcelain`:
> untracked ('??'): written, NEVER committed. modified ('M'/'MM'/...): tracked but working-tree differs
> from HEAD = uncommitted edit."*

`.tools/comp-heat:521` (`cmd_drift`) calls `uncommitted_writes_budgeted` and nothing else. The seam
artifact's fields — `n`, `n_modified`, `n_untracked`, `tracked_total` — are that porcelain read counted.
**His recollection was not approximate. It is the specification, in his own words, from 2026-06-25.**

⛔ **HALF TWO — THE STITCH IS FOR COMMITS, ALSO CORRECT, AND MORE NARROWLY THAN "COMMITS."**
`.github/workflows/stitch-source-push.yml` @`9554733409`: `on: push: branches: [CLOUD]` with a SIX-PATH
filter (`portal/src/**`, `data/**/scripts/**`, `org/modules/graph/**`, two `globgrph` scripts, and the
workflow itself), feeding an EventBridge→CodeBuild nightly. **So the live trigger is not even "a commit"
— it is a commit PUSHED to `CLOUD` that TOUCHES ONE OF SIX PATHS.**

## 3. ⛔ AND MY CARD CITED A MECHANISM THAT NO LONGER EXISTS. THAT IS MY DEFECT, NOT HIS.

My card offered *"the post-commit hook"* as the stitch mechanism on the table. **THAT HOOK IS RETIRED** —
`.tools/git-hooks/stitch-refresh-post-commit.TOMBSTONE.md`, `NFRA_CLDGRPH` S29 @`a46abe413a`, 2026-09-09
— **and it was retired on ANDREW'S OWN LATER WORD**, the ratified `NFRA_CLDGRPH` endpoint: *"no machine is
in the compile business."* Its numbers are why: 552 publishes to a shared key from one laptop, none
visible to the seat whose commit fired them, and two writers on one key disagreeing by 53 nodes.
**I offered him, as a live option, a device-side commit-triggered publisher that he had personally killed
eight days earlier for being a device-side commit-triggered publisher.**

## 4. THE RULING

**THE CONDITIONAL DOES NOT FIRE, AND ITS OWN AUTHOR'S SENTENCE IS WHY.** *"If we already have a stitch
mechanism ride that"* is a real grant and I record it as one. We do have a stitch mechanism — the cloud
producer. **It cannot carry this measure, because he is right that the stitch is for commits and right
that drift is uncommitted material, and those two facts do not compose.**

**THE MECHANISM OF THE INCOMPATIBILITY, stated so it can be checked rather than taken:**

| | |
|---|---|
| **ANTI-CORRELATION** | A commit-triggered publish samples the tree at the moment drift is LOWEST — immediately after the commit that just cleared it. The device accumulating the most uncommitted work is the device committing least, so it publishes least, and the device that never commits never publishes at all. **The signal is strongest exactly where the carrier is quietest.** |
| **THE PATH FILTER** | Drift accumulating anywhere outside those six paths fires no workflow at all, at any volume. |
| **THE READING IT PRODUCES** | Both failures render as a LOW or ABSENT `n` — indistinguishable from a genuinely clean tree. That is the QUIET-versus-SILENT confusion `TO-OS-s-21`'s accept was re-cut specifically to prevent. |

⚠ **BOUNDED, because the sharp version of this is wider than what I measured:** a commit does not zero
`git status --porcelain` — untracked files and unstaged edits outside the commit survive it. The claim is
ANTI-CORRELATION and PATH-BLINDNESS, **not** that the reading would always be zero.

**SO: THE DRIFT MEASURE RUNS ON THE DEVICE'S OWN TIMER, WHICH IS WHERE `TO-OS-s-21` ALREADY PUTS IT**
(*"ON THE DEVICE where the working tree lives, on that DEVICE'S OWN TIMER"*, ruled at S23 @`98722f9355`).
⛔ **THE ONLY THING HIS ~15:3xZ WORD CHANGES IS THE INTERVAL — DAILY BECOMES CONTINUOUS.** No carrier
changes, no new build, no cloud hop, and the identity, the per-device key and the negative arms all stand
exactly as `TO-OS-s-21` carries them. **`2.0.0_SA_COO` may cut the drift-cadence cell now.**

⚠ **AND THE 15 MINUTES IS STILL A "MAYBE" AND IS STILL NOT RATIFIED.** A cell may implement quarter-hour;
**NO ACCEPT GRADES ON THE NUMBER** until he fixes it. Unchanged from the v0.11 addendum.

## 5. WHAT IS HIS TO REVERSE

The carrier decision is mine at L4 and I have taken it, on a premise he supplied and I measured. **If he
meant the drift publish should ride the CLOUD stitch producer notwithstanding all of the above, one word
reverses this** — and I would then owe him the shape in which a commit-triggered carrier can report a
between-commits property, which I do not currently believe exists without re-introducing exactly the
device-side publisher his `NFRA_CLDGRPH` endpoint retired.
