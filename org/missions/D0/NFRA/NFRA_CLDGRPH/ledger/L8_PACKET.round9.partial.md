# NFRA_CLDGRPH -- L8 PACKET, ROUND 9, **PARTIAL** (4 of 5 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 ~19:2xZ, for `3.0.0_SA_CVO` at L9

**TO-CG-I-3 (the fold's LICENCE) is IN FLIGHT** on slot `~2` and is not in this packet. A FINAL packet will
supplement this one when it drains, exactly as rounds 7 and 8 did. **Grade against PRD v0.14.**

⚠ **AND THE AUTHORIZATION THIS ROUND RUNS UNDER CHANGED MID-ROUND.** Andrew-direct ~18:5xZ, verbatim:
*"CLDGRPH shall be finished I am allowing it"* (@`4ff4abd9a4`, relayed 95477). `1.0.0_SA_CTO` had
RECOMMENDED closing the project where it stood and records that he decided otherwise. **It is a grant to
FINISH, not a lift of anything else** -- the egress hold, the push hold and the site-Z SESSION all stand.

## 1. The four drained orders

| order | cell | merged | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-I-1 | CG-s-41 the key collision settled, then closed at the writer | @`744e7f110d` (acts `e86c4fb778`, flip `c7de3661d5`, row `282100f6f3`) | **4 of 4 PASS** | **I1-AC5** |
| TO-CG-I-2 | CG-s-43 the edge-side drop and the blind 0-dangling check | @`95070f76f7` (acts `efbddbccd6`, flip `61d6a754f6`) | **4 of 4 PASS** | **I2-AC5** |
| TO-CG-I-4 | CG-s-44 the dated archive key that is a mutable pointer | @`2018181896` (acts `e9c3c737f1`, flip `5be2a48f14`) | **4 of 4 PASS** | **I4-AC5** |
| TO-CG-I-5 | CG-s-45 hop 1's producer with no production home | @`ebef40d8f2` (acts `a658d981cd`, flip `633354ed72`) | **4 of 4 PASS** | **I5-AC5** |

**Every instance was RE-VALIDATED AT THIS SEAT, IN TREE, against the COMMITTED blob** -- not accepted from
the worker's report and not validated on a copy: four of four `VALID (rc=0)`, violations 0, each run inside
the worker's own worktree after confirming the file on disk IS the committed blob. Three worktrees and
branches removed; `wk-cldgrph-9-2` remains because its queue is not empty.

⚠ **ALL FOUR DRAINS CONFLICTED ON THE APPEND-ONLY CHANNEL** -- the normal path (`S36`), not the exception.
Resolved as *base + ours-tail + theirs-tail* under a structural guard that REFUSES if either side is
anything but a pure append, then verified on the WRITTEN bytes: 0 markers, 0 duplicate ids, 0 rows lost,
union printed each time (285, 286, 289).

⛔ **AND THE GUARD REFUSED ME ONCE, CORRECTLY.** It normalised the header's mandatory denominator
restatement on THEIRS only, so the drain AFTER my own first drain refused with *"OURS is not a pure append"*
-- because by then a restatement of MINE was in OURS. **The refusal was right and the asymmetry was mine.**
Both sides are now normalised on that one line and any other difference still refuses. ⭐ **The second half
matters more: NEITHER SIDE'S RESTATED COUNT IS TRUE OF THE UNION**, so carrying either forward prints a
number wrong by exactly the other side's rows. The merged header is re-measured from the merged bytes and
says so on its face.

## 2. THE ROUND'S CENTRAL FINDING: the collision is FIVE class pairs, and the settle needed no grant

**ROUND 8 LABELLED THE FINAL LINK `INFERRED` BECAUSE SETTLING IT NEEDED AN INSTRUMENT NOBODY HAD. IT
TURNED OUT TO BE REACHABLE FROM THIS LAPTOP.** The updater publishes a `graph_nodes` metadata pointer to S3
*"so dev-box readers which cannot reach Nessie REST learn HEAD from an S3 object"* -- so a `pyiceberg`
static table over that pointer reads the whole warehouse table with a plain `s3:GetObject`. **`SETTLED=YES`,
27,685 of 27,685 rows at the served vintage, plus 34 of 34 buckets probed on the control plane.** The
destroyed row is the `S3_BUCKET_POLICY` row whose key is the bare bucket name, and it is matched on the
`node_id` limb, never on `arn`. Three are already gone, each with a live bucket policy and no row. Row
`W3-S19`'s claim that Trino or Athena was required is SUPERSEDED.

⛔ **AND THE BOUND I PUT ON THE FACE WAS WRONG IN THE DIRECTION THAT MATTERS.** My face carried the
producer's own docstring -- *"exactly one class"* -- as the shape of the problem. That is true of the
CANONICAL key space and **is not a bound on the destruction**, which runs in the raw `node_id` column where
**30 of 27,632 strings are two-claimed across FIVE pairs**: bucket/policy 12, role/lambda 8, rule/lambda 8,
project/role 1, rule/document 1. **It was found because a negative control that should have returned zero
returned sixteen.** The fix closes all five. The collision had three mouths in that file, not one.

## 3. FOUR PREMISES CAME BACK FALSE AGAIN, AND THE SHAPE IS NOW THREE ROUNDS OLD

Round 7 found four. Round 8 found five and called it a property of the controls rather than bad luck.
**Round 9 produces four more, and again NOT ONE was caught by a gate, a control or a checker -- every one
was caught by the seat being graded, running a read nobody asked for.**

1. ⛔ **"THE PUBLISH ROUTE RAN ONCE" -- FALSE BY A FACTOR OF 854, AND IT IS INHERITED, NOT NEW.** Round 6's
   `TO-CG-F-3` recorded the archive as *"pushed ONCE by the GH-Action"*. **It has fired 855 times.** Eight
   succeeded, all inside one 103-minute window on 2026-07-07, all BEFORE the step that packs `portal/src`
   landed -- so all eight published archives with zero portal files. Since that step: **847 runs, 0
   successes**, dying every time on an unprovisioned secret. **Correct publishes by the committed route,
   ever: 0 of 855.** The claim was right about the OBJECT and wrong about the RUNS. ⭐ **The general form
   is worth more than the number: a route's TRIGGER and its BODY fail independently, and only the trigger
   is visible from a checkout.** Cost of finding it: one API call.
2. ⛔ **"THE KEY GRAMMAR IS AN OPEN CHOICE" -- FALSE; IT IS A RATIFIED SPEC THE PRODUCER HAS NEVER
   IMPLEMENTED.** My `I-4` face asked whether the dated key is a naming bug or a decision nobody wrote
   down. **Three sources specify unique timestamped keys** -- the graph PRD, an Andrew-ratified retention
   policy at Tier 1 INDEFINITE, and the bucket's own Terraform, which gives that property as the REASON
   versioning is off. The producer has written one key per calendar day since 2026-06-09. **The writer
   remedy is CONFORMANCE, not a proposal**, which changes its cost and its owner.
3. ⛔ **"THE LINE EVERYONE WOULD EDIT" IS DEAD CODE.** The `0-dangling` check's key set is bound TWICE, and
   the snapshot-shaped bind at `derive_stitch.py:144` -- the line whose TEXT most looks like the defect --
   is never read before the rebind. My face pointed at the wrong line. The check was never miscomputing:
   it computed correctly over a collection sampled at `t0` and asserted a property of it at `t1`. ⭐ **When
   one producer both reads and writes a collection, every set derived from it is DATED.**
4. ⛔ **"85 OF 118 CITATIONS ARE UNDECIDABLE" IS A NUMBER THE FACE DID NOT ANTICIPATE AT ALL.** The cell was
   cut on one key. The overwrite reaches three of the four cited keys, and **85 of 118 citations in this
   project's own record can no longer be resolved to the bytes they cite** -- the producer's own logs
   included, which record two different sizes for one key on one day against a third live length.

⭐ **AND THE LABELS ARE STILL DOING THE WORK.** Everything I marked `HELD, NOT MEASURED` on these faces cost
nothing when falsified. The two things I marked as measured -- the docstring's "one class" and the archive
key's open question -- are the two that misdirected a worker. `measured/inferred/held/absent` is the whole
mechanism, three rounds running.

## 4. What each drained order delivered

**TO-CG-I-1 (CG-s-41).** The collision is SETTLED (s.2) and CLOSED AT THE WRITER, chosen over three other
layers with the reason stated: **exactly 1 of 3 writers in that key space deletes by key**, so closing at
the writer ends the DESTRUCTION and explicitly does NOT end the AMBIGUITY. Armed with a red-first fixture:
`DESTROYED_BEFORE=2`, `DESTROYED_AFTER=0`, negative control fired, the `SERVED_FROM` arm taking 27 orphaned
edges to 0. Its own reading says `CG-s-33`'s re-parent is **not** redundant and is safer landing AFTER this.

**TO-CG-I-2 (CG-s-43).** The check's key set is now rebuilt from the surviving nodes AFTER the collapse, so
it can finally see the window it was blind to; the edge-side drop was **REFUSED on the source's own
evidence** rather than implemented, which is the accept working as designed. The dead bind survives
deliberately -- removing it is a second act on a file the same slot's NEXT order writes.

**TO-CG-I-4 (CG-s-44).** The dated archive key is a mutable pointer on an unversioned bucket: `STILL_VALID=21`,
`OVERWRITTEN=12`, `UNDECIDABLE=85` over 118 citations in 55 of 539 files, cross-checked against 97 live
objects and a 4-of-4 head-object agreement. The remedy is FILED with two blockers, three named owners and
six acts NOT to take, because the writer's path is outside this order's grant and the deploy is held.

**TO-CG-I-5 (CG-s-45).** Section 3 item 1. Plus a fix shaped around the failure a naive fix would introduce:
the checkout action resolves an EMPTY ref to the default branch, so a quietly-degrading resolver would
publish an unrelated portal head while the four-hop vintage feed faithfully reported that wrong sha. The
resolver refuses anything that is not 40 hex and both negative arms write nothing. **Three items need owners
outside this project**, and the third is the one to read twice: the day the missing secret lands, a
production input that moved five times in 65 days starts moving on every qualifying push. **That is a
NEVER-2 cadence change arriving disguised as a credential, and it wants deciding BEFORE the secret.**

⭐ **TWO INSTRUMENT DEFECTS A WORKER FOUND IN ITSELF AND FIXED RATHER THAN QUIETLY REPAIRED.** A repo root
resolved by counting `..` landed on a directory that STILL EXISTED, so a status read on an absent path
returned empty and **printed CLEAN on a file that was not there**. And a capture opened with a decode error
in a subprocess READER THREAD, which pollutes the capture, loses a block, and **exits 0** -- a corrupted
capture wearing a passing return code.

## 5. The rows this round minted, with their owners' liveness MEASURED at compile

| row | class / standing | disarm owner | owner live? |
|---|---|---|---|
| `W1-S49` the collision is five class pairs, not one | OBSERVATION / **ARMED** | `2.0.0_SA_COO` | **LIVE** |
| `W1-S50` the warehouse table is readable from the laptop | OBSERVATION / INERT | -- | -- |
| `W1-S51` the fix's own deploy artifact still carries PRE-FIX code | OBSERVATION / **ARMED** | `2.0.0_SA_COO` | **LIVE** |
| `W2-S79` the check's key set is bound twice and one bind is dead | OBSERVATION / INERT | -- | -- |
| `W3-S20` the dated key is a ratified spec never implemented | OBSERVATION / **ARMED** | `0.8.0_AE_CloudComp` | ⛔ **DARK** (not registered) |
| `W4-S10` the publish route has run 855 times and never published correctly | OBSERVATION / **ARMED** | `0.0.0_AB_MSTR` | **LIVE** |

⛔ **`W1-S51` IS THE ONE THIS SEAT OWNS AND HAS DELIBERATELY NOT ACTED ON.** The corrected source now sits
beside a TRACKED deploy artifact carrying its own stale copy of the same file, so a deploy reading that
artifact ships the collision while the source reads clean. **Rebuilding a deployment artifact has no cell in
this round**, and inventing one mid-round is the spec-freeze violation the surprise channel exists to
prevent. It is carried to the round close as an owned item, named here so no reader has to find it.

## 6. What is NOT in this packet

- **`TO-CG-I-3`** and its judgment criterion `I3-AC5`. In flight.
- **`FWD-7`'s PERSON half.** Andrew ALLOCATED the site-Z seat; **an allocation is not a session** and no
  seat may treat that half as unblocked until a site-Z serial registers LIVE. His "finish it" does not
  supply the hand at that machine.
- **Any egressing act.** No `ecs run-task`, no build, no push, no apply, no S3 write, in any of the four
  orders -- each proved it with its own zero-count arm and a firing probe control.

## 7. ⛔ ONE THING THIS PACKET SETTLES FOR THE ROUND-8 SLUG THAT IS STILL BLOCKED

`REMEDIATION_v4.md` is an UNISSUED DRAFT at `3.0.0_SA_CVO`, stopped by the remediation gate's **project-wide
HEAD** preconditions: it read `TO-CG-F-11` pending and `S117` open. **`TO-CG-F-11` IS NO LONGER PENDING** --
it was dispositioned `superseded` BY ITS ISSUER at 2026-09-10 ~17:5xZ with the pointer named (`CG-s-33` and
`CG-s-41`), which is exactly what CTO ruling 95389 said its issuer had to do. **`S117` remains, and its
disarm owner is `1.0.0_SA_CTO`, not this seat.** The other precondition the gate will read is `TO-CG-I-3`,
open until it drains. Sequenced plainly: I-3 drains, the FINAL packet follows, and both L9 readings can then
clear the same precondition set.

**Push state, measured at compile rather than carried:** every hash named here is LOCAL. Andrew holds the
push and this line ages the moment an integrator runs.
