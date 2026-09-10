# ROUND 6 ANALYSIS -- NFRA_CLDGRPH

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-10 ~04:0xZ
**On the slug:** `surprise-channel/adjudications/ADJUDICATION_v1.md` + `org/modules/graph/grain_baseline.json`
@`32114f8e9b` (`3.0.0_SA_CVO`, msg 94957; 61 adjudication rows, 245 investigation items)
**Completion report:** `2.0.0_SA_COO~A` `ledger/COMPLETION_REPORT.round6.json`, FINAL packet
`ledger/L8_PACKET.round6.final.md` @`aec7dc8cfd`, sha256 `6b9c09744d366feb` (re-hashed at the CVO)
**Graded against:** PRD **v0.14**

---

## 1. The coverage read

**11 of 11 orders terminal and drained. 0 of 245 investigation items undispositioned**, by `comp-surprise`'s
own census at the CVO, 0 defects, 0 malformed rows, no duplicate ids. Ten orders flipped complete;
`TO-CG-F-11` drained OPEN on `F11-AC3` alone, which is exactly what this seat ruled at 94872 it should drain
on. **Every endpoint outcome is served by a cell and no outcome went unserved**, so there is no PRD addendum
this round -- the answer is this analysis.

## 2. What round 6 actually did, in the endpoint's own terms

The stitch JOIN was built, served, and then **made honest**. That last clause is the round, and it took four
cycles to reach.

| the claim | measured, and by whom |
|---|---|
| the four provisional stitch types are gone from the served vocabulary | 0 of 4, unified at the PRODUCER, with `PORTAL_BUNDLE` present as the positive control a stitch-free graph would fail |
| the stitch-v1 stamp is retired on BOTH its writers | `STITCH_V1_STAMPED_SERVED` 0, from 1,771 at the round's start; whole-graph node diff over 27,665 nodes each side reads exactly `{'-vocabulary': 1}`, 0 added, removed or re-typed |
| the per-machine copy is gone, not merely unused | archived, verified by S3-computed checksum, deleted, tombstoned; the loader removed |
| the boundary edges are facts, not a cross-product of guesses | 955 emitted -> 137; per-key `{5: 191}` -> `{1: 137}`; 0 edges contradicted by their own source node; **54 no-bucket keys COUNTED, not guessed** |
| the identity census resolves | 1,330 of 1,380 resolved, LOST 0 of 1,790 |
| `comp-debt` answers from the served graph, `comp-aws` is deprecated and unrouted | rc 0 reading the unified names |

**The grain baseline is SIGNED** (`C-S59`), the round's one outstanding act, executed inside the slug's own
commit: nine entries, 0 pending fields, verified by re-reading the committed blob rather than the writer's
report.

## 3. The instrument, which is why I accept the sign

The CVO did not certify the baseline from the producer's report. It read the estate's **served** CloudNode
table through the projection service: the five canonical classes at their exact magnitudes and the four
retired names returning **zero rows -- an empty result set, not a null count** -- over 27,665 nodes.

Three properties of that read are what make it a signature rather than an assertion:

1. **The vintage names a SCHEDULED fire.** The served projection at 03:31:02Z was built from
   stitch-codebuild 03:01:17Z, manifest sha256 `5361815924ce7afd` -- cycle 4's zip consumed by the 03:00Z
   **rule-initiated** nightly. That is a better vintage than the packet asked for, and it is the first
   scheduled success in a slot that had failed **67 of 67 times**.
2. **The discrimination a single read cannot supply.** The five magnitudes held UNCHANGED across three
   successive served vintages (01:27:30Z, 02:28:23Z, 03:31:02Z) while the graph around them visibly moved --
   the stamp went 1 to 0 between the first two, the boundary edges went 764 over 191 keys to 135 over 135
   keys between the second and third. **They held while things changed, rather than holding because nothing
   was rebuilt**, which is the only version of stability worth signing.
3. **The signature states what it does NOT certify:** not the `STORED_IN` endpoints, not any class outside
   the nine, not the artifact's internal counts. `C-S59` supersedes `C-S53`, whose numbers came from a
   scratch-tree run and differed by 3 scripts and 13 S3 keys -- and saying so is the reason I trust the rest.

## 4. The four-cycle reading -- the round's real product

`F11-AC6` PASSES, and it is the strongest judgment record this project has produced. Its finding:

> **Every remaining failure was a SECOND WRITER or a SECOND COPY of something the first fix had already
> handled correctly.**

The map retired the stamp and the deployed image still wrote it. The image stopped and the producer carried
the stamped node forward out of the snapshot the derive archives. The producer stopped fanning the edges five
ways and last night's 955 arrived inside that same snapshot. **One mechanism: this producer's input contains
its own output.** So a retirement takes effect only when the carry-forward is handled too, and each plane
hides the next.

Three of four cycles were spent discovering a writer the previous cycle's fix had *revealed*, not repairing
the same defect twice. **No code read could have found it; only the served graph could.** This is the
shared-dependency limb of Rule 22 arriving from a direction the rule does not yet name -- not a defect beneath
a set of members, but a defect in a producer's own FEEDBACK PATH, where each fix is what makes the next one
visible.

And the single most valuable line in the round is a worker **disowning its own gate's numbers**: the relayed
magnitudes 332 / 2,428 / 588 / 24 / 188 are ADMITTED counts, a different quantity from `per_class`, and
Component at 24 against 201 would have read 8.46x and refused the very publish the gate existed to allow. A
worker telling its own gate that the gate is measuring the wrong quantity is what a judgment criterion is for.

## 5. The grades

Seven REALIZED, one NOT_REALIZED. **No grade moved on the v0.13 -> v0.14 re-pointing**, and the COO~A and the
CVO both said so independently before I read it: FWD-2, FWD-4 and FWD-8 had their `DONE WHEN` re-pointed at
on-demand READS of history that already exists, ids KEPT, and *a re-pointing that makes an outcome provable
today cannot make it less proven than it was*.

**FWD-7 stays NOT_REALIZED at `state_observed: APPLIED`, and TWO of its three remaining limbs closed tonight:**

| limb, as round 5 named it | round 6 |
|---|---|
| (i) no second, older copy anyone could still be reading from | **CLOSED** -- the per-machine store archived with an S3-computed checksum, deleted, tombstoned, loader gone |
| (iii) the cloud stitch producer had never produced (67 of 67 failed) | **CLOSED** -- the 03:00Z rule-initiated nightly succeeded and its artifact is what the baseline is signed on |
| (ii) the PERSON half -- two people on different machines asking the same question at the same moment | **OPEN, and it is the whole of what remains** |

**That last limb is an ACT, not a wait, and it is worth being precise about under this night's L2 law.** It is
not proven by patience: it is proven the moment a site-Z seat asks D-8's fixed question beside this one. What
gates it is a *named human decision* -- Andrew's allocation of a site-Z seat (his word at ~17:3xZ, row S22 of
v0.6) -- and, practically, the push he holds: local is 303 commits ahead of `origin/CLOUD` @`c6bcb7b12b`, so
site Z cannot yet read what this round built. **A gate on one named person's one decision is not the
indeterminate wait the law forbids; it is the expressly-qualified exception the law provides for, and this
paragraph is that qualification.**

## 6. What round 7 inherits -- four items, each with an owner

1. **The bucket-identity seam** (`W2-S68`, `W2-S70`, `S102`) -- `F11-AC3` measured-and-failing at 135 of 137,
   all landing on `S3_BUCKET_POLICY`. Round 7's, with its own image act and its own never-widen sign.
   **I adopt the CVO's warning as a binding condition on the cut: the class census must count FACTS PER KEY,
   not edges, or it will re-measure the fan-out and call it identity.** That is the same wrong-quantity error
   the F11-AC6 worker caught in its own gate, one round downstream.
2. **The SMS page path** (`W2-S72`, `S104`) -- RESERVED FOR ANDREW, hold in force, nothing unsubscribed and
   nothing edited. The hold rests on the standing egress law ("all egress off Opal infrastructure" is
   excluded from agent autonomy), **not** on a widening of his `aj@` word, and the CVO concurred with that
   grounding specifically.
3. **The producer's self-consuming cycle** -- at its engine owner. Section 4 is its statement of the problem.
4. **The archive carry-forward substrate card** (`W2-S61`, `W2-S69`, `W2-S71`, `S103`) -- **a row PER CARRIER**,
   because the same question got three different correct answers on nodes, props and edges, each found
   separately, three cells apart. Rule 28 says every row carries its owner because remedies do not move
   together; this is that rule earning its keep.

Also carried: the portal layer's vintage moved twice inside one round with nothing declaring it. The CVO
classes that as the same family as an unsigned baseline, and I agree -- it is a vintage nobody can cite.

## 7. The round's lesson, and what it cost

**A producer that reads back its own output is silently idempotent under a fixed emission and silently WRONG
under a shrinking one** -- which is exactly what a nightly with stable counts cannot surface. Every one of
this round's four cycles is that sentence.

Two of tonight's three spine edits were paid for by this round's own mistakes (v3.9's worker-death clause,
and NEVER-1's writer census after `W2-S67`), which is the cheapest way that ever happens. `dep_stage` stays
**EXECUTING**: seven of eight outcomes hold, and the eighth is one allocation away.

## Push state
LOCAL. `origin/CLOUD` @`c6bcb7b12b` (`ls-remote`, this seat 03:22Z; the CVO's own read at 03:5xZ agrees).
Local 303 ahead. **Nothing in this round is readable at site Z until Andrew's push word**, which is also what
FWD-7's last limb waits on.
