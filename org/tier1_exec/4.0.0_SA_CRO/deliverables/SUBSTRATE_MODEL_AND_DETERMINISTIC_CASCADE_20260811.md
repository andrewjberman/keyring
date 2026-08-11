# THE SUBSTRATE MODEL [APPROVED -- Andrew-direct GO 2026-08-11: "Plan approved, get started"] + THE DETERMINISTIC->INFERENTIAL->USER CASCADE (Andrew-direct 2026-08-11)

**Author:** `4.0.0_SA_CRO~B`. Andrew-direct architecture for complete, deterministic-first C3 coverage,
refreshed daily via the Kimi SVP.

## 1. THE SUBSTRATE (`layer`) -- FOUR, deterministic, and MOSTLY ALREADY RULED
**Ruling:** `layer = aws | portal | codebase | ms`.
- **aws** = cloud resources (deterministic from node_type / ARN).
- **portal** = the portal REPO (deterministic from file path -> its git root).
- **codebase** = the ajb_workspace REPO (deterministic from file path -> its git root). *(Andrew's name
  "codebase"; the prior ruling called it `ajb_workspace`.)*
- **ms** = Microsoft / content (deterministic from source).

**This is NOT a new decision -- it is finishing one Andrew already made.** ESTATE_AXIS_AND_SEAM_GRAIN_DESIGN
(Andrew 2026-07-20): **`semctl` DROPS** -- *"a REDUNDANT relabel -- NODE_TYPE_LAYER derives it purely from
node_type ({C2Motif,C3System} -> semctl), zero info beyond type."* **`pipeline` DROPPED** 2026-06-26
(*"empty placeholder", 0 nodes*), and its value map already says **`pipeline -> ajb_workspace`**. So
Andrew's dislike of `semctl`/`pipeline` matches rulings on the books; they are RESIDUE not yet fully
purged from the production derive (`derive_runner.py:1759` still relabels C2/C3 -> semctl). **The
substrate axis becomes PURELY physical/deterministic (which cloud/repo/content), and functional
categories -- `pipeline`, `object-data`, `identity`... -- move OFF it onto the DOMAIN axis where they
belong (Rule-24: one grain per axis).**

## 2. THE CASCADE -- deterministic (90%+) -> inferential (<=9%) -> user-described (<=1%)
The construction is a three-stage filter, and the two ontology layers STOP at different stages:

| stage | budget | what it does | mechanism |
|---|---|---|---|
| **DETERMINISTIC** | **>=90%** | substrate assignment + anchor-node overlapping-domain-cover + domain -- pure graph structure / paths / ARNs | `c3_cover.py` (anchor-node, 1,255 today) + provenance-derived substrate |
| **INFERENTIAL** | **<=9%** | anchor the residue determinism can't place (unanchored instances, single-motif domains) to the nearest structure/domain | Potion/model2vec + BM25 (the estate's own semantic axes), null-gated |
| **USER-DESCRIBED** | **<=1%** | NAME the deterministic+inferential structure-clusters into business verticals | a naming act, CVO-verified |

- **C3.i (deterministic structures) STOPS AT INFERENTIAL.** No human input. C3.i = the anchor-node cover
  (deterministic) + inferential gap-fill. It is *what the estate structurally IS*.
- **C3.ii (semantic verticals) GOES ALL THE WAY through USER-DESCRIBED.** C3.ii = clusters of C3.i
  structures, NAMED by the human (<=1%). It is *what the business says it is*.

## 3. THE EFFORT MATH (measured today, and the target)
- Deterministic anchoring today: **5,035 of 6,138 instances anchored (82%)**; 1,103 unanchored (18%);
  617 single-motif domains unpromoted. **82% is short of the 90%+ target** -- so the FIRST work is
  making DETERMINISM do more: extend the anchor catalog (add the missing anchor types, incl. the CODE
  substrates -- files/modules/components as anchors for portal + codebase, which today are UNCOVERED --
  all 1,255 are `substrate_side: BACKEND`). Every anchor type added moves work from inferential/user back
  to deterministic, which is the direction Andrew wants.
- Then inference (<=9%) places the true residue; then <=1% user naming yields C3.ii.
- **This INVERTS today's state:** the current 14 structures / 28 verticals were ~all user-drawn. The
  target is determinism carrying 90%+, user carrying <=1% (naming only).

## 4. WHY THIS IS THE RIGHT SHAPE
It makes "how many structures / verticals, and are they covered" a DERIVED, daily, mostly-deterministic
answer instead of a legislated aggregation that drifts (the 29-vs-28, the 4-vs-14-vs-1255 confusion all
came from legislation standing in for construction). Determinism cannot be argued with; inference is
bounded and null-gated; user input is a thin naming layer that cannot silently expand.

## 5. PATH
1. **Purge `semctl`/`pipeline` residue** from the derive; substrate axis = pure {aws, portal, codebase,
   ms}, deterministic; move functional categories to the DOMAIN axis.
2. **Extend the anchor catalog to the CODE substrates** (portal + codebase) so the cover runs over both
   repos, not AWS-backend only -- the two-repo deterministic barrier, made real.
3. **Drive deterministic anchoring 82% -> 90%+** (catalog completeness), measure the residual.
4. **Wire the inferential (<=9%) gap-fill** (Potion/BM25, null-gated) -- C3.i complete.
5. **Thin user-naming (<=1%)** over the structure-clusters -> C3.ii.
6. **All of it daily in the Kimi SVP**, so the coverage denominator is same-day and self-correcting.
*(CRO measures + recommends; CVO owns the derive; CTO gates.)*

## 6. RULINGS FOLDED (Andrew-direct ~17:5xZ: "All approved as recommended, (a), (a)")
- **90/9/1 binds ESTATE-WIDE; per-substrate splits DECLARED** -- ms's larger inferential share is
  legitimate-when-declared, never force-fit (ceilings-are-honesty-floors ratified as the binding reading).
- **ms motif run = PROCEED-ONCE-CLEAN** -- when the pre-run checklist verifies (housekeeping landed
  @9b4d484132), no further word needed; step-0/step-2 sequencing + CTO gate + the co-change
  revive-or-declared-UNAVAILABLE gate remain in front.
- The four extension DOMAIN NAMES ratified (see step-0 spec).
