---
name: integrate
description: Reconcile the two fabrics' branches (CLOUD <-> SITEZ) -- the MSTR-to-MSTR cross-device merge: measure true divergence and the overlap set, compute conflicts without touching a worktree, agree one resolution, merge (never rebase), verify from the remote. Bare `/integrate` = assess-only; `/integrate merge` = your own leg; `/integrate parity` = drive both legs to PARITY or LEG-OUTSTANDING (a single leg is never reported as parity). Runs at MSTR launch as the joint parity assessment and absorbs `/git-pull once`; also when a citation from one fabric does not resolve on the other.
---

# /integrate — the cross-fabric reconcile (CLOUD <-> SITEZ)

**Who runs it:** `0.0.0_AB_MSTR` (laptop) and `0.0.0_AB_MSTR~Z` (site Z), together. Both halves
are MSTR acts because both are shared-branch pushes (LD-0367/LD-0368: only the two MSTRs push a
shared branch). A lane agent invoking this stops at Step 0 and routes to its MSTR.

**What it is for (Andrew, 2026-08-12):** *"we do want to maintain parity to the extent that is
convenient/relevant. I try to make sure that the fabrics always work on separate projects so
there is zero or very little overlap to make this easy to manage."* ⛔⛔ **REDEFINED BY ANDREW 2026-08-27 ~23:2xZ, AND IT RETIRES THE FIXED-POINT AS A GOAL.
VERBATIM:**
> *"parity is foundationally never going to happen unless work is stopped, which is not happening,
> the gist of it is that i want both fabrics to be updated with each others work, the big reason for
> this right now is that i need to run a /daily-sprint with the full render but i dont want to do it
> until we have all the info in from sitez."*

>> **THE OBJECTIVE IS MUTUAL UPDATEDNESS ON A PRACTICAL CADENCE, NOT A FIXED POINT.** Both
   `is-ancestor` reads returning YES means the refs are EQUAL, and **two live fabrics cannot hold that
   for longer than it takes someone to commit.** Driving for it means asking a working fabric to stop
   working. <<

⛔ **SO: NEVER ASK A FABRIC TO HOLD PUSHES TO MANUFACTURE A BOTH-YES READ.** The stationary-head
coordination step is legal ONLY when a real consumer needs a frozen state and someone has ASKED for
it; it is not the mode's default terminus. *(Offered and DECLINED on the 08-27 run: "not needed under
the redefined objective; keep your seats committing.")*

⭐ **ASK WHAT THE INTEGRATION IS FOR, AND MEASURE THAT INSTEAD.** The 08-27 driver was
ONE-DIRECTIONAL — the laptop needed everything of site Z's for a `/daily-sprint`. **The satisfying
read was `is-ancestor(SITEZ -> CLOUD) = YES` alone**; the other direction was irrelevant to the need
and would have cost a push-hold to obtain. **A one-directional need has a one-directional test.**
⛔ **`LEG-OUTSTANDING` still means what it said — one YES and one NO — but it is a STATE DESCRIPTION,
not a defect, and it must not be reported as a failure or drive further legs on its own.**

**Parity is a convenience
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

## Step 1b — ⛔ IS YOUR OWN BRANCH REF CURRENT? (the same failure, one layer over)

```bash
git fetch origin
B=$(git rev-parse --abbrev-ref HEAD)
echo "$B: behind $(git rev-list --count HEAD..origin/$B), ahead $(git rev-list --count origin/$B..HEAD)"
git merge --ff-only origin/$B      # fast-forward ONLY; never a rebase, never a messy auto-merge
```

**A PARITY ASSESSMENT COMPUTED FROM A STALE LOCAL REF IS WRONG THE SAME WAY A SHALLOW CLONE IS
WRONG** — both produce confident, well-formed divergence numbers off an incomplete graph. Step 1
closes that for *history depth*; this closes it for *branch currency*. Do both in one breath.

**This is where the old `/git-pull once` launch step LIVES NOW — it is not replaced, it is
ABSORBED**, as the act that makes the assessment trustworthy. That framing is load-bearing: an
integrator who skips it does not "miss a nicety," they get **wrong numbers**, which is the only
kind of enforcement that holds.

> **SEVERITY IS ASYMMETRIC BY DEVICE — the step is identical, what it BUYS is not** (Andrew-direct
> intent, 2026-07-30). On a **NON-PRIMARY device (site Z / any `~Z` seat) this is THE SYNC
> GUARANTEE and a failed or skipped one is a REAL FINDING** — that machine is downstream of a tree
> that commits and pushes continuously, so a stale HEAD there silently poisons every evidence read.
> **FAIL LOUD there.** On the **PRIMARY laptop** it is incidental hygiene ("we are effectively
> source"), so a deferral past live uncommitted seat-work is consistent with intent — **WARN, do
> not fail.** ⚠ **A laptop pull-deferral is NOT precedent for a site-Z one.**

**WHY THIS STEP EXISTS AT ALL — a measured instance, site Z, 2026-08-12 ~1320Z.** `/git-pull once`
ran per the launcher and printed `596254785b..91e1854258  CLOUD -> origin/CLOUD` **on screen**. The
seat then ff'd its own branch, saw 0 behind, and moved on — **never looking at CLOUD.** The other
fabric had advanced ~34 hours and the startup was *structurally incapable* of noticing, because the
act performed was **same-branch currency** and the question that mattered was **cross-branch
parity**. The information was on the screen and the procedure had no slot for it. That session then
spent four hours discovering the divergence by hand. **This is Andrew's "not just blindly running
git pull," and it is not hypothetical.**

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

### ⛔ FIRST, FOR EVERY CONFLICTED FILE: GET THE PER-SIDE HUNK RANGES. DO NOT READ THE CONFLICT HUNK.

```bash
git diff --unified=0 $BASE origin/CLOUD -- <file> | grep '^@@'   # BASE-side ranges, CLOUD
git diff --unified=0 $BASE origin/SITEZ -- <file> | grep '^@@'   # BASE-side ranges, SITEZ
```
| the two BASE-side range sets are… | verdict |
|---|---|
| **disjoint** | **MECHANICAL UNION.** Both sides edited different rows; git conflicted on ADJACENCY alone. No law owner, no adjudication. |
| **overlapping** | read the content, *then* classify with the table below |

**A CONFLICT HUNK SHOWS THE WHOLE CONTESTED REGION FROM BOTH SIDES, INCLUDING LINES NEITHER SIDE
TOUCHED.** So it answers *"what region is contested"* — it **never** answers *"which rows did each
side change."* Those are different questions and the hunk is well-formed output to the wrong one.

**This is a DESIGNED-domain mismatch, not carelessness: no amount of reading the hunk more
carefully fixes it** (Rules 22/22a class — the remedy is knowing the instrument's domain and
corroborating outside it, never a closer read). **And it does not fail loudly — it produces a
plausible escalation to a law owner who is not needed, which on a quiet fabric is an unbounded
delay.**

*Measured 2026-08-12, and recorded as `0.0.0_AB_MSTR~Z`'s catch against its own analysis: rules 22
and 22a appeared on both sides of the `=======` in CLAUDE.md, read as "both fabrics edited rules
22/22a," and a law-owner hold was raised on it. The `--unified=0` ranges were CLOUD {27,40,49,+58}
vs SITEZ {48,77} — **zero shared rows.** The whole conflict was 48 sitting next to 49. Hold
withdrawn; the file took a mechanical union.*

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

### ⛔ IDENTICAL **NONZERO-COUNT** BASE-SIDE RANGES = ONE DEFECT CORRECTED TWICE. **PICK, NEVER UNION.**

⛔⛔ **READ THE COUNT BEFORE YOU READ THE POSITION. THIS HEADING SAID ONLY "IDENTICAL" UNTIL
2026-09-16 AND ON A ZERO-COUNT RANGE THAT RULE DELETES ONE FABRIC'S ROWS.** A `--unified=0` header
carries BOTH: `-41,3` consumes three base rows, `-463,0` consumes **none**. Identical POSITION with a
**ZERO** count is not two renderings of one sentence — it is a **PURE APPEND COLLISION**, two fabrics
inserting DIFFERENT content at the same point, neither having touched a base row. **PICK there is not
a choice between two edits of one region; it is a silent DELETION of whichever side loses**, and it
leaves no conflict, no error and no diff to review.

```
-N,0  (ZERO count)     -> APPEND COLLISION      -> MECHANICAL UNION, keep both sides' rows
-N,M  (M >= 1)         -> same rows replaced    -> PICK one whole, per the rest of this section
```

**Found by `0.0.0_AB_MSTR~Z` on the 2026-09-15/16 assessment, against its own live conflict set:
`org/XXX.md -463,0` on both sides, where the two fabrics had each appended a DIFFERENT Step 1b-F
loop-authorization row. PICK would have dropped one — and Step 1b-F is the ONLY source of truth for
live loop arming, so the failure mode is a fabric that reads clean and arms nothing.** ⚠ The peer
found it; `0.0.0_AB_MSTR` (laptop) re-derived the MECHANISM on a throwaway two-branch repo rather
than taking the finding on report, with both arms: identical `-3,0` on each side, PICK dropped the
other side's row; the NEGATIVE control, identical `-2,1`, was a genuine same-row replacement where
PICK is right. **The instance is the peer's, the mechanism is independently measured, and the two
arms are what separate the cases.** COST: read the `,N` you already printed in Step 3. NON-APPLICATION:
disjoint ranges (already union) and any range pair where either count is nonzero.

The classification table above splits conflicts into *disjoint ranges -> mechanical union* and
*overlapping -> read the content*. **There is a third case it did not name, and the union default
produces VISIBLE GARBAGE on it.** When both sides' `--unified=0` BASE-side ranges are not merely
overlapping but **IDENTICAL — and NONZERO-count, per the block above** — the two fabrics did not add
rules blind to each other; **they independently CORRECTED THE SAME SENTENCE.** Union stacks two
corrections of one defect.

**And it usually needs NO law-owner adjudication**, which the bullet above would otherwise send it
to: there is no disagreement about substance, only two renderings. **Read both, pick the better one
whole, discard the other, and say which you took.** Escalate only if the two texts actually disagree.

*Measured 2026-08-27, CLOUD<->SITEZ: `org/XXX.md` (line 336 both sides) and
`.claude/skills/watcher/SKILL.md` ((43,3) both sides) — both fabrics had independently corrected
the same false orphan-watcher mechanism within hours. Overlap 5 of 1254 = 0.40%. Resolution was one
line long ("take CLOUD wholesale") and needed no owner.*

### ⛔⛔ AFTER PICKING A WINNER, AUDIT THE **LOSING** RENDERING FOR CONTENT — THIS STEP IS MANDATORY AND NOTHING ELSE IN THIS PROTOCOL ASKS FOR IT

**A WHOLESALE TAKE-ONE-SIDE RESOLUTION SILENTLY DISCARDS WHATEVER ONLY THE OTHER SIDE KNEW, AND
NOBODY IS ASSIGNED TO LOOK FOR IT — BECAUSE THE QUESTION FEELS SETTLED THE MOMENT A WINNER IS
NAMED.** Every incentive points the wrong way: the side that conceded has moved on, and the side
that won has no reason to read the text it beat. **The loss is silent by construction** — a
discarded rendering leaves no conflict, no error, and no diff to review.

**Do this, and do it AFTER conceding, not instead of conceding:** diff the two renderings for
CONCEPTS, not wording — `grep -c` a handful of distinctive phrases from the losing side against
the winner. Anything present only in the loser is either (a) genuinely redundant, or (b) **content
the winner is about to lose.** Route (b) as a one-paragraph fold-in, never as a competing text.

**AUDIT THE LOSER FOR CONTENT; DO NOT DEFEND IT FOR PREFERENCE.** The distinction is the whole
discipline: you already conceded, so this is not re-litigation — if the only thing you find is
that you liked your phrasing better, you have found nothing, and say so.

*Measured on the same 2026-08-27 reconcile, and it caught a live defect in the text both fabrics had
just agreed was canonical: the winning rendering's NEW paragraph (`PARENT_CHECK=0` at `$PPID <= 1`)
composed with TWO OLD untouched paragraphs ("every healthy wrapper is `ppid=1`") into the false
conclusion that the self-exit never fires — contradicting the winner's own measurement three
paragraphs above, and failing toward "I am orphan-capable, the banner instruction is theatre." The
losing rendering carried the separation that dissolves it: `ppid=1` is the **OUTSIDE** `ps` view of
the WRAPPER; a CHILD reading its own `$PPID` gets a real pid. Demonstrated in ONE process tree
(wrapper 515411 `ppid=1`; child 515417 `ppid=515411`; banner `parent-tied: pid 515411`), corroborated
at three seats with zero 1s. Fixed @a12b8173fc.*

⛔ **THE GENERAL FORM, which is why this sits in the protocol and not in a postmortem: WHEN YOU
CORRECT A MECHANISM, RE-READ EVERY OTHER PARAGRAPH THAT MENTIONS ITS VARIABLES. YOUR DIFF IS NOT
YOUR BLAST RADIUS, AND THE UNIT UNDER TEST IS THE DOCUMENT, NOT THE EDIT.** A correction can be
LOCALLY TRUE AND GLOBALLY WRONG: neither paragraph is wrong alone, the defect exists only in their
composition, it is CREATED BY THE FIX, and it is invisible to the author because the author only
diffs what they wrote.

#### ⛔ WHAT TRIGGERS THAT AUDIT: **DISCLOSE A VINTAGE MOVE. IT IS NOT COURTESY.**

The step above says to audit the loser. It does not, on its own, say what makes you *go back* — and
**nothing re-opens a settled question by itself.** Once a resolution is agreed, both sides close the
files and move on; that is the correct behaviour and it is exactly why the discarded content stays
lost.

**THEREFORE, A HARD OBLIGATION ON THE SIDE THAT MOVES FIRST: if you commit to your side of a
contested file AFTER the peer's assessment was taken, SAY SO, unprompted, naming the vintage their
verdict was measured at and the one it now faces.** Frame it as *re-based, not invalidated* when the
substance is unchanged. The peer then re-verifies at the new vintage — and **the content audit rides
along with the re-verification, which is the only reason it happens at all.**

*Measured 2026-08-27: `0.0.0_AB_MSTR` disclosed a post-assessment commit as routine bookkeeping,
expecting nothing from it. That disclosure sent `0.0.0_AB_MSTR~Z` back to files it had already
conceded and closed; the re-verification carried the content audit; the audit found a false
conclusion in text both fabrics had just agreed to canonize. **THE VALUE WAS NOT IN THE CONTENT OF
THE DISCLOSURE — IT WAS IN THE RE-OPENING.** Neither seat intended the thing that mattered, and the
record does not assign it to one: the audit found the defect, the disclosure caused the audit.*

⛔ **AND DO NOT LET A VERDICT-AT-A-PASSED-VINTAGE BE DISCOVERED LATER.** A peer's "take yours
wholesale" was measured against a specific ref. Silence after you move it is not neutral — it leaves
a live verdict pointing at a vintage that no longer exists, and the peer has no signal that anything
changed. This is the same class as a stale citation, one layer up: **the claim is fine, the thing it
was measured against moved.**

*Both findings authored by `0.0.0_AB_MSTR~Z` and `0.0.0_AB_MSTR` jointly on the 2026-08-27
reconcile; the second was surfaced by the losing side auditing its own rendering after conceding,
and the audit itself was caused by the peer's unprompted vintage disclosure.
Records: LD-0465 + AMENDMENT 2 (CLOUD), @a12b8173fc.*

## Step 5 — Execute your half

```bash
git fetch origin
git merge origin/SITEZ            # (or origin/CLOUD from the site-Z side)
# resolve ONLY the overlap set, per the agreed resolutions
git push origin CLOUD             # your own branch; the deploy gate may sweep for minutes
```
### ⛔⛔ THE SECOND LEG'S PUSH IS A **DEPLOY EVENT**. IT WRITES LIVE PRODUCTION S3.

**MEASURED 2026-08-12 on the first completed reconcile — nobody predicted this, either side.** Site
Z's CLOUD→SITEZ push carried files under `data/*/scripts/**` new *to their branch*; the pre-push
`safe-deploy` gate did exactly its job and **deployed them**, reporting *"all files deployed and
verified."*

**THE MEASURED NUMBER IS 28 OBJECTS, of a 396-object denominator** — re-derived independently at
both seats and agreeing exactly:

| tree | written | denominator |
|---|---|---|
| `opal-data-inf/code/gold/` | **24** | 170 |
| `opal-data-inf/code/silver/` | **3** | 22 |
| `opal-data-bd/code/gold/` | **1** | 179 |
| `opal-data-bd/code/silver/` | 0 | 25 |
| **total** | **28** | **396** |

**ATTRIBUTION CONTROL (this is what makes 28 caused-by rather than merely concurrent-with):** every
object written to those trees on 2026-08-12 landed between **16:55:09 and 16:56:19 GMT** — writes
outside the push window that day: **ZERO**. The window and the whole day return the same set, so
nothing else is mixed in. Spot-confirmed in explicit UTC via `head-object`:
`code/silver/build_billing_dim.py` **16:56:18 GMT**, `code/gold/INF_D_02.advisor_client_detail.py`
**16:55:45 GMT** — ~90 seconds before the leg-2 report.

> ### ⛔ THE MERGE-DIFF COUNT IS NOT THE DEPLOY COUNT. It is the CEILING.
> The first report of this finding said **"~100 files deployed."** That was the count of files under
> `data/*/scripts/**` **in the merge diff** — the **exposure ceiling**. The gate deploys a **NARROWER
> SET** than the merge carries, and the true figure was **28**. *Two different denominators, and the
> first was labelled with the second's meaning.*
>
> ### ⛔⛔ AND THE REASON IT IS NARROWER IS **NOT** "IT DEPLOYS WHAT DIFFERS." THAT SENTENCE WAS IN
> THIS SKILL AND IT IS FALSE AT SOURCE — corrected 2026-08-21 after it produced a wrong prediction
> that was broadcast to four seats and a peer fabric.
> **`safe_deploy_core.py:548` runs `aws s3 cp` UNCONDITIONALLY**, then head-objects and compares
> ETag to the local md5 at `:565`. **That is a POST-WRITE VERIFY, NOT A PRE-WRITE SKIP.** There is no
> S3 comparison anywhere before the upload. **Every deploy-scope file in the change set is REWRITTEN,
> even when its bytes are already identical.** The narrowing is a **DEPLOY-SCOPE filter** — `:351`
> and `:389`, `if not norm.endswith(".py")` — nothing more.
> ⛔ **AND `MATCH` IN THE GATE'S OUTPUT MEANS "UPLOADED AND VERIFIED," NOT "SKIPPED BECAUSE
> IDENTICAL."** The word invites exactly the wrong reading, which is how the false sentence survived.
> **Measured end-to-end on the 2026-08-21 leg-2 run:** 8 cot files in the merge diff, **6 written**
> (all `.py`), 2 skipped (`account_attributes.json`, `gold_validate_config.yaml` — non-`.py`).
> `cot_bronze_ingest.py` LastModified moved **18:06:50Z -> 01:04:18Z with an UNCHANGED ETag**
> (`a1d81b96...`), and `account_attributes.json` stayed at **18:06:01Z**. Identical bytes, new object.
> **THEREFORE, THE TWO THINGS AN INTEGRATOR MUST NOT SAY:** (1) never predict a leg is "inert"
> because local bytes already match S3 — **byte-parity does not prevent the write, it only makes the
> write invisible in the content**; the honest claim is *"the write will land CLOUD's own content, so
> nothing can be DISPLACED"*, which is a claim about WHAT lands, not about WHETHER anything lands.
> (2) never let a downstream seat pin an S3 `LastModified` as a drift detector across a merge —
> **a rewrite-with-identical-bytes moves the timestamp and moves no hash**, so a timestamp-based
> detector fires falsely and a hash-based one is blind to the rewrite. Tell affected owners which
> of the two they are holding. *(Both errors were mine on the 08-21 run; the second reached
> `0.6.2_AE_PartnerETL`, who had pinned timestamps for a next-morning acceptance.)*
> **SHARPER FORM, `1.0.0_SA_CTO` on the same run — the two detectors have OPPOSITE blind spots and
> neither is simply better:** `sha256` sees a content change and is blind to an identical-bytes
> rewrite; `LastModified` sees any write **but cannot tell a rewrite from a real change.** So
> *"LastModified moved"* is **not a stronger signal — it is a DIFFERENT QUESTION**, and for the only
> question an acceptance asks (*did the executed bytes change?*) **the hash detector's blindness is
> the CORRECT blindness.** ⛔ **THEREFORE THE TRAP: a verifier holding BOTH limbs and alarming on
> disagreement FIRES FALSELY ON THE HEALTHY CASE — after any merge-triggered deploy leg,
> `hash-same + timestamp-moved` is the NORMAL state, not an anomaly.** Drop the timestamp limb or
> re-pin it; do not treat the pair as corroboration.
> **So the pre-push enumeration below is the right instrument and must be read as a CEILING — never
> reported as a deploy manifest.** (Self-corrected by `0.0.0_AB_MSTR~Z`, who measured it rather than
> leaving it as an unverified number of their own.)

> ### ⛔ TWO RETRIEVAL TRAPS THAT NEARLY BROKE THIS MEASUREMENT — both produced clean-looking, WRONG answers
> **1. A GUESSED PREFIX RETURNS EMPTY, AND EMPTY IS BYTE-IDENTICAL TO A REAL ABSENCE.** The first
> probe used `s3://opal-data-inf/code/scripts/silver/` — the real prefix is `code/silver/`
> (`safe_deploy_core.py:82-84` `CODE_TREES`). Taken at face value it would have **REFUTED A TRUE
> FINDING with a confident negative.** *Re-derive the prefix from SOURCE; print the denominator; a
> zero from a path you guessed is UNRESOLVED, not absent.*
> **2. `aws s3 ls` WITHOUT `--recursive` COUNTS A DIFFERENT DOMAIN THAN THE CLAIM.** The second probe
> read inf gold as **"2 of 110"** — top-level objects only, silently excluding `runners_inf/` and
> `lib/`, where most of the deploy landed. The truth was **24 of 170**. The output was well-formed
> and carried no hint it had answered a narrower question. **Always `--recursive` for a
> prefix-scoped count.**
> **And prefer `head-object` over `s3 ls` for any timestamp you will compare:** `s3 ls` prints
> LOCAL time, `head-object` prints explicit UTC. When the entire conclusion is a timestamp
> comparison, do not leave a timezone inference in the chain.

**THIS IS NOT A FAULT — the S3 artifacts now match the merged tree, which is correct. THE DEFECT IS
THAT IT IS INVISIBLE IN THE PROTOCOL.** The integrator believes they are reconciling *git* and does
not realise they are shipping *code*.

**BEFORE THE SECOND LEG'S PUSH, ENUMERATE YOUR EXPOSURE CEILING** (not your deploy manifest — see above):
```bash
git diff --name-only HEAD@{1} HEAD -- 'data/*/scripts/**' | tee /tmp/willdeploy.txt | wc -l
```

⛔ **AND THE CEILING EXPIRES. MEASURE IT AGAINST THE RANGE YOU ARE ACTUALLY PUSHING, IN THE SAME
BREATH AS THE PUSH — on a live fabric a lane lands deploy-scope code between your measurement and
your `git push`, and the stale ceiling reads CLEAN.**

≫ A ceiling is a claim about a RANGE, and `HEAD` is not a range endpoint you control while other
   seats hold the same checkout. The enumeration above is correct for a merge leg (where `HEAD@{1}`
   pins the pre-merge state); **for an ordinary integrator push the range is `origin/<branch>..HEAD`,
   and it is only valid for as long as HEAD does not move.** ≪

```bash
B=$(git rev-parse --abbrev-ref HEAD)
git diff --name-only origin/$B..HEAD -- 'data/*/scripts/**' | wc -l   # re-read IMMEDIATELY before pushing
```

*Measured 2026-08-27, `0.0.0_AB_MSTR~Z`, on its own push: the ceiling was enumerated at 0 deploy-scope
files and was TRUE when measured. `0.4.0_DS_ClientPlatform~Q` landed three `data/mdpf/scripts/gold/`
files in the interval, and the push **deployed two of them** (the third, a `.json`, fell outside the
deploy-scope `.py` filter). Fabric rate at the time: 18 commits in 30 minutes. The deploy was correct
and lane-legitimate — **the defect was that the integrator announced a zero and shipped a two**, which
is the same false-clean an integrator would carry into a report.*

**SO: a ceiling older than your push is a FLOOR, not a ceiling.** Either re-read it immediately
before the push, or state it as measured-at-`<hash>` and re-derive what actually shipped from
`git log <old-remote-head>..<new-remote-head>` afterwards — which is the honest form when the fabric
is too hot to freeze.
**AFTER the push, if you need the ACTUAL deploy count, measure it at S3** — recursive, with the
denominator, windowed to your push, plus the outside-the-window control that makes it attributable:
```bash
aws s3 ls s3://<bucket>/code/<layer>/ --recursive | grep -c '^<YYYY-MM-DD>'   # vs total = denominator
```
**⛔ THE SHARP EDGE: if the two fabrics hold DIFFERENT content for the same script, the second push
silently rewrites S3 with its merged view.** The first leg is usually inert (its files already
deployed from that fabric); **the second leg is where the shipping happens**, and it happens to
whichever fabric merges second — an operational asymmetry the merge ORDER decision (Step 4) never
mentioned it was making. **Weigh that when choosing the order**, and say out loud which fabric is
taking the deploy.

- The pre-push safe-deploy gate verifies deploy-scope scripts against S3 — **a slow push is the
  gate working, not a hang.** Run it backgrounded and read the result.
- ⛔ **A PUSH TIMEOUT TELLS YOU NOTHING ABOUT WHETHER IT LANDED.** Measured same run: >2 min, first
  attempt timed out, the ref had landed anyway. **Never retry blind — `git ls-remote origin
  refs/heads/<branch>` is the oracle.** A blind retry after a successful-but-timed-out push is how
  you turn a completed deploy into a confusing second one.
- ⛔ **NEVER `git stash` to clear a dirty tree for the merge** — prohibited on this shared tree, and
  **stash is the reflex**, which is why it is named here. Back the files up in full (patch + copies)
  and leave open work IN-TREE. *(Site Z found 16 modified files pre-merge, 10 colliding; all 16 were
  backed up before anything was touched, and 9 cleared as machine churn — timestamp bumps on
  `.open_deploys` entries the peer had since closed.)*
- ⛔ **THE MERGE WINDOW IS A SHARED-INDEX HAZARD: ANNOUNCE IT OPEN, AND INSPECT THE INDEX BEFORE
  CONCLUDING.** On one shared worktree, a lane running `safe-commit` while your `MERGE_HEAD` exists
  **stages its files into YOUR merge index, silently** — the lane's commit is then refused loud
  ("cannot do a partial commit during a merge"), but the staging has already happened, so the
  refusal lands on the WRONG seat while the sweep hazard sits with the integrator. **Measured
  THREE times in one night (2026-08-20):** CVO's staged log swept into @a206dfba9c under the
  integrator's subject; AE's staged TrueShares work swept the same way; 0.8.0's comp-adversary
  work staged mid-merge and self-rescued (`git reset HEAD -- <own files>`) minutes before the
  commit. This is the CLAUDE.md @6d14f2d15 "test subject" class, structural to
  LANES-COMMIT-INTEGRATORS-PUSH on one tree. **Therefore, both halves mandatory:** (a) BEFORE
  `git merge` — one-line broadcast to live seats: *"MERGE WINDOW OPEN — hold safe-commits until my
  close"* (and a matching CLOSE line after); (b) BEFORE the merge-conclusion commit — run
  `git diff --cached --stat`, and any path outside your resolution set gets `git reset HEAD -- <path>`
  and a note to its owner. **A gate candidate rides with this (CTO to route): safe-commit refusing
  to STAGE — not just to commit — while `.git/MERGE_HEAD` exists.**
  ⛔ **(a) AND (b) ARE NOT TWO CONTROLS — (b) IS THE CONTROL AND (a) IS COURTESY. Do not let the
  pair read as redundancy.** (a) is a SEAT-COOPERATION protocol and therefore carries a REACH
  DEPENDENCY: it protects only seats that are registered, live, and reading. (b) is MECHANICAL and
  holds whether or not any seat read anything. **Measured on the 2026-08-21 0051Z leg-1 run: the
  hold broadcast reached 9 of 11 seats; the 2 that came back QUEUED (no live broker session) were
  `4.0.0_SA_CRO~A` and `~B` — the two seats that had committed most recently (00:44Z, 00:47Z). THE
  REACH GAP WAS ANTI-CORRELATED WITH NEED**, the orphan-watcher shape again: the seats a hold most
  needs to reach are the ones least able to receive it (Codex lanes commit without holding a broker
  registration). *Framing owed to `0.6.2_AE_PartnerETL`, same run: "you ran a real control and a
  decorative one, and the decorative one is the one that failed — the intuitive fix (make the
  broadcast more reliable) improves the decorative half, while the load-bearing half is already
  sound and could simply be made the DECLARED mechanism."* **So: send (a), never COUNT it. Never
  report N-of-M delivery as coverage. If (b) is skipped, the merge was unprotected no matter how
  many seats acked.** Corollary measured the same run: a zero-conflict `git merge` AUTO-COMMITS, so
  `MERGE_HEAD` may never be observable — a peer's `test -f .git/MERGE_HEAD` returning absent is
  **byte-identical between not-yet-started and already-finished** and must not be read as either
  (CTO declined to guess it mid-act, correctly). The CLOSE frame is the only signal that discharges
  the hold.
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

## Step 6b — ⛔ NUDGE THE PEER, AND A QUEUED MESSAGE IS NOT A NUDGE

**Andrew-direct 2026-08-12:** *"did you nudge them? that needs to be part of the skill."* — asked
after site Z landed its leg, sent one SQS message, and reported parity as "one fast-forward away."

**PARITY IS NOT DONE WHEN YOUR LEG IS DONE. Leg 2 requires the PEER to act**, and everything about
this protocol up to here is things *you* can do alone. This step is the one that isn't.

**THE FAILURE THIS CLOSES: an SQS send is fire-and-forget.** If no consumer is armed on the peer
device, the message is **STORED, NOT READ** — indefinitely, silently, with a successful-looking
`MessageId` returned to you. You will believe you asked and they will never have been asked.

**MEASURE REACHABILITY BEFORE TRUSTING THE SEND — and know what each signal cannot say:**
```bash
bash .tools/agentbus-sqs.sh peek <peer-device>   # consumes nothing
```
| reading | what it means |
|---|---|
| `ApproximateNumberOfMessages` > 0 | your mail is **sitting unread** — the peer consumer is down |
| `= 0` | **NOT proof of delivery.** Consistent with read, and with in-flight, and with drained |
| `NotVisible` | an **instantaneous in-flight gauge, not a cumulative receipt** — `recv --keep` releases messages back, so it reads 0 for received-and-released. Never use it as a delivery oracle |
| **an agent-side ACK** | **the only sound oracle** (Rule 22b). Check the timestamp of the peer's last one |

⛔ **THE NUDGE GOES OVER THE AGENTBUS. DO NOT REACH FOR A SECOND CHANNEL.**
**Andrew-direct 2026-08-12, VERBATIM: *"no you should write them via agentbus"*** — said after site
Z, finding the peer unACKed for ~4h, escalated onto the `org/mcp/agentbus-trunk/` git transport and
pushed an envelope to the peer's branch. **That was the wrong instinct and the reason is a standing
rule, not a preference: a backup channel is a BACKDOOR EXTRA PATH**, and extra paths are vetoed —
*"we do not do all these extra paths, these things never ever get decommissioned and they become
debt."* The trunk is a **superseded git-transport MVP** ("to de-risk the real build", per its own
README); SQS is the **delivery tier**. Building a parallel route around a quiet consumer is the
shadow-channel anti-pattern wearing an operational excuse.

**A QUEUED BUS MESSAGE IS NOT A LOST ONE.** SQS here is FIFO with **14-day retention** and
exactly-once delivery: an unconsumed nudge is **waiting**, not dropped, and it lands the moment the
peer arms a consumer. So the correct handling of an unreachable peer is:

1. **Send it on the bus, once, with everything they need to act** (below).
2. **Record leg 2 as OUTSTANDING** — in your report and to Andrew. An unACKed nudge is a *known*
   open item, which is a completely different thing from a silent one.
3. **Do not re-send, do not build a route around it, do not chase silence.** A quiet bus is
   wind-down, not fault.

*Note the asymmetry that makes this safe: you are not waiting on the peer for anything you can do
yourself. Your leg is landed and pushed; theirs is a fast-forward whenever they return.*

**Nudge content is the peer's ACTION, not your status:** their exact commands, the payload size and
authors, the conflict count, the exposure ceiling, and an explicit *verify-do-not-trust-this-message*.
Say plainly if it is not urgent — a nudge that manufactures false urgency gets discounted next time.

## Step 7 — Close

- **PARITY IS A TWO-LEG CLAIM. Verify BOTH from the remote before saying "at parity":**
  `is-ancestor(origin/CLOUD, origin/SITEZ)` **and** `is-ancestor(origin/SITEZ, origin/CLOUD)`.
  One rc=0 is *your* leg, not parity. Report each leg with its own landed head and name the
  outstanding one as OUTSTANDING.
- ⚠ **THE SKILL ITSELF CAN BE STALE — Step 1b CHECKS THE LOCAL REF, NOT THE LOCAL SKILL.**
  Measured 2026-08-12: site Z ran the full protocol on a bare `/integrate` (assess-only under
  Andrew's ruling) because its copy still carried the retired table, and **the reconcile's own
  merge is what imported the corrected skill.** A fabric can run this protocol under rules the
  other fabric already retired, and nothing in Steps 0–6 detects it. After leg 1, re-read the
  invocation table before acting on it.
- Post-merge, ask each affected steward to read their artifact (auto-merged ≠ semantically right).
- Record the run: base, both counts, overlap size + set, resolutions taken, both landed heads.
- **Ledger it** (MSTR commits touching non-record paths need an `LD-NNNN`).
- If the overlap exceeded the Step-2 band, **surface it to Andrew** — it is his separate-projects
  premise that keeps this cheap, and its erosion is a fact he would want early.

---

## Step 8 — `/integrate parity`: DRIVE BOTH LEGS TO A MEASURED TERMINAL STATE

**Andrew-direct 2026-08-27, VERBATIM:** *"i want a function that explicitly is an instruction to work
with the other fabric and bring both devices to parity with remote."*

⛔ **`merge` AND `parity` ARE MATERIALLY DIFFERENT AND THE DIFFERENCE IS WHO CAN FINISH THEM.**

| | `/integrate merge` | `/integrate parity` |
|---|---|---|
| scope | **MY leg** | **the joint objective** |
| terminates when | my push lands | **BOTH `is-ancestor` checks pass, read FROM THE REMOTE** |
| can I finish it alone? | **yes** | **NO — the second leg belongs to a party I cannot command** |
| silent about | the other direction | nothing |

**MEASURED THE DAY THIS WAS COMMISSIONED:** site Z ran `merge`, leg 1 landed clean at `@5edabd600a`,
and **the fabrics were still not at parity six hours later** — because leg 2 belongs to the laptop and
`merge` has no slot for a second party. *A mode that terminates on its own success cannot deliver an
objective that requires someone else's.*

### The procedure

1. **MEASURE BOTH DIRECTIONS FIRST.** This decides what the run even is:
   ```bash
   git fetch origin
   git merge-base --is-ancestor origin/CLOUD origin/SITEZ   # leg 1: CLOUD in SITEZ?
   git merge-base --is-ancestor origin/SITEZ origin/CLOUD   # leg 2: SITEZ in CLOUD?
   ```
   Both rc=0 — **ALREADY AT PARITY. Report and stop.** Do not merge to prove it.
2. **RUN MY OUTSTANDING LEG** via Steps 0—7 (merge window, index control, per-hunk resolution, push,
   remote verify). If my leg is already in, skip.
3. **COORDINATE THE PEER'S LEG.** Send them, in one message: the measured both-direction state, what
   their leg carries (commit count + per-author breakdown), **their deploy ceiling — the second pusher
   ships**, every resolution already agreed, and any per-hunk trap. Ask them to name their count when
   they run it. ⛔ **The nudge goes over the agentbus — never a second channel** (Step 6b).
4. **RE-MEASURE FROM THE REMOTE.** Never from their push receipt, never from their report.
5. **REPORT THE TERMINAL STATE, WHICH IS ONE OF TWO — AND BOTH ARE LEGITIMATE ENDS OF THE RUN.**

### ⛔ The two terminal states, and the second is NOT a failure

```
PARITY        both is-ancestor checks pass, read from the remote. Name both heads.
LEG-OUTSTANDING   my leg landed @<hash>; peer leg asked at <ts>, MessageId <id>, unACKed.
```
**`LEG-OUTSTANDING` IS A SUCCESSFUL RUN OF THIS MODE.** The peer may be mid-wave, drawn down, or
asleep; their gate is theirs. **What the mode buys is that the outstanding leg is a NAMED, DATED,
ADDRESSED open item instead of a silent one.** Do not loop, do not chase, do not re-send, and **do
not build a route around a quiet consumer** — a queued bus message is waiting, not lost (14d FIFO
retention).

⛔⛔ **NEVER REPORT A SINGLE LEG AS PARITY.** *"I merged"* and *"we are at parity"* are
different claims with different truth conditions, and the first is the one you can verify alone —
which is exactly why it gets substituted. **Measured 2026-08-27: leg 1 was reported as the pull being
"done" and the sovereign made placement decisions for hours believing this fabric had material it did
not have.** The report was true and the impression was false.

### ⛔ PARITY IS A FIXED-POINT, NOT A LEG COUNT — the convergence step

**This section shipped without this step and was wrong within three hours.** The procedure above
counts legs: run mine, coordinate theirs, done. **TWO CORRECTLY-EXECUTED LEGS DO NOT IMPLY PARITY**,
because each leg is measured against a ref the other fabric is still advancing.

**`0.0.0_AB_MSTR` (laptop), 2026-08-27, landed as theirs:**

> **PARITY IS A FIXED-POINT, NOT A LEG COUNT: after both legs, re-measure both `is-ancestor` from the
> remote; if either reads NO, the state is LEG-OUTSTANDING (name whose), and the final convergence
> requires ONE side to hold pushes while the other runs its leg against the stationary head — a
> parity claim is legal only in the same breath as the two YES reads it cites.**

**MEASURED THE DAY BOTH HALVES OF THIS MODE WERE WRITTEN.** Site Z ran leg 1 (`@5edabd600a`); the
laptop ran leg 2 (`@9fc70e31a1`, zero conflicts, the leg-1 per-hunk resolution having removed every
contested hunk). **Both legs succeeded. Both `is-ancestor` checks then read NO** — site Z was short 24
laptop commits, the laptop short 5 site-Z commits, every one of them landed *while the legs ran*.
**No error, no conflict, nobody at fault, and no instrument reported anything wrong.**

**So the terminating act is not a merge — it is a HOLD.** One side declares a push hold, the other
merges against a head that is not moving, and parity is measured in that window. Without a hold, two
live fabrics can ping-pong indefinitely with every leg correct.

⛔ **AND THE HOLD IS ON *PUSHES*, NOT ON WORK.** Seats keep committing; their commits ride the
next push after parity is measured. A hold that stops seats working to achieve a bookkeeping state
has inverted the cost — and it is the shape most likely to be reached for, because "freeze
everything" feels safer than "freeze one ref".

⭐ **AND THE MODE'S REAL PRODUCT IS THE ASK, NOT THE MERGE.** Anyone can run their own leg; the
thing that was missing was a named act whose *definition of done* includes the other device. If you
finish your leg and say nothing to the peer, you have run `merge` and mislabelled it.

## Invocation forms

| form | behavior |
|---|---|
| **`/integrate`** | **ASSESSMENT — THE DEFAULT.** Steps 0→4: clone check, **local-ref currency (1b)**, divergence, overlap set, conflict dry-run + per-file classification, report. **Merges nothing, pushes nothing, resolves nothing.** May send the peer its findings. |
| **`/integrate merge`** | **ASSESS AND PROCEED.** The full protocol, Steps 0→7 — everything the assessment does, then the peer-agreed resolution, the merge, the push, and remote verification. |
| **`/integrate parity`** | **DRIVE BOTH LEGS.** Step 8. Measures both directions, runs MY outstanding leg via 0—7, COORDINATES the peer's, re-measures from the remote, and terminates in exactly one of two named states: **PARITY** (both `is-ancestor` pass) or **LEG-OUTSTANDING** (mine landed, theirs asked-and-named). **The only form whose definition of done includes the other device.** Never reports one leg as parity. |
| `/integrate status` | Alias of the default assessment, minus the peer send. Changes nothing, sends nothing. |
| `/integrate execute` | Steps 5-6 only — **only after a peer-agreed resolution already exists.** Never the first call. |

> **ANDREW-DIRECT, 2026-08-12, laptop terminal, VERBATIM:** *"something I want to bring in to the
> mstr launch script is not just blindly running git pull, its better to run /integrate as a joint
> fabric parity assessment and this parity can either be just an assessment (default), or it can be
> /integrate merge, which is assess and proceed the merge."*
>
> ⚠ **THIS INVERTED THE PRIOR DEFAULT.** Bare `/integrate` used to run Steps 0-7 **including the
> merge and the push**; it is now **assess-only**, and the merge requires the explicit `merge`
> argument. An agent working from a cached memory of the old default will expect a reconcile to
> have happened when only a report was produced — **the assessment says so explicitly in its own
> closing line, so the state is never inferred.**
>
> **ASSESS-AS-DEFAULT IS THE SAFE DIRECTION FOR A LAUNCH STEP:** a startup that silently merged two
> fabrics would be a shared-branch write nobody asked for, on a device that may have just woken with
> stale context. Reading is always safe to do at load; writing is not.

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
