# NFRA_TOOLUNIFY Census SS2.A -- LAMBDA reconciliation correction (post-CVO~Z review) -- 0.8.0_AE_CloudComp~A

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Date:** 2026-07-24
**Task Order:** NFRA_TOOLUNIFY.CENSUS (same ad-hoc dispatch as the prior log; this is the adversarial-review
close-out, not new scope)
**Status:** COMPLETE

---

## Objective

`3.0.0_SA_CVO~Z` independently re-derived Lane A's census (previous log:
`nfra_toolunify_census_ss2a_lane_a.md`, commit `a02a3d75b`) and returned PASS-WITH-ONE-CONDITION: the
LAMBDA arithmetic `333 - 115 phantoms - 30 dups = 188` against live/kuzu=191 left a residual of 3
unaccounted for, presented as if it closed exactly; and the 115-phantom population was corroborated by one
example, not proved. `1.0.0_SA_CTO~Z` routed the same condition and asked both items closed before
re-commit. This log covers that close-out.

---

## Compiler Tools

No comp-* tools this cycle -- pure Python re-derivation against already-fetched artifacts
(`.comp-graph/graph.json`, the live Lambda JSON pulled earlier this session, `lambda-source-map.json`).
One sentence per the standard: nothing new to fetch, the work was building a correct classifier over data
already on disk. Compiler-tools-log.md line not duplicated (no new tool invocations to record).

---

## Work Completed

### 1. Found the residual is real, and traced its cause
Investigated CVO~Z's flagged 3-node gap directly rather than patching the total. Discovered the original
`depth>6 OR label-starts-with-underscore` phantom classifier had a **false-positive mode**: `v2_portal`'s
real, legitimately-organized `yang_pipeline` Lambda directories nest as deep as the genuine vendored-SDK
trees (e.g. `v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py` = 8 path segments), so
roughly 30 real, correctly-named, live Lambdas were being silently misclassified as phantom. That is what
produced the spurious "188 vs 191, 3 short" residual -- an artifact of the classifier, not a real coverage
gap.

### 2. Rebuilt the classifier on a measured signal, not a path-shape guess
New method: every LAMBDA node's label, normalized (strip `-`/`_`, lowercase), checked against the union of
{191 live Lambda names, 192 `lambda-source-map.json` registry keys}. Verified directly (not inferred from
arithmetic): **graph.json's LAMBDA labels cover 191/191 live Lambdas -- zero missing under any name.**
CVO~Z's "direction matters, 188<191 may mean 3 live Lambdas are absent" concern is now answered with a
proof, not an assumption.

### 3. Full 5-way, 333-node classification
`matched` (208, live-or-registry) / `alias_excess` (19, non-canonical label sharing a file_path with an
already-matched node) / `vendor_confirmed_phantom` (73, path passes through a pip-vendored 3rd-party
package) / `org_dir_noise_phantom` (9, `rglob` picked up a generic organizational subdir --
`tests/`/`src/`/`tools/`/`_shared/`/`ci/` -- as a Lambda name; a second noise class not previously named) /
`residual_unexplained` (24, real-looking name, not live, not registered, status genuinely undetermined --
reported open, not forced). Sum verified = 333.

### 4. Wrote the full enumeration for spot-checkability
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A_lambda_enumeration.json` -- all 333 node
IDs with id/label/file_path across the 5 buckets, so CVO~Z (or anyone) can random-sample any bucket instead
of relying on my one originally hand-picked example -- directly responsive to CVO~Z's *"a hand-picked
instance measures the author"* point.

### 5. Updated A.md/A.json in place
Added a dated ADDENDUM section to `A.md` (prominent, at the top) explaining the false-positive, the fix, and
the corrected breakdown table; added an inline correction pointer at the original `333-115-30=188` line;
added a `CORRECTED_post_cvo_z_review` block to `A.json`'s `lambda_graphjson_reconciliation`; updated the
`could_not_fully_verify` list and the closing acceptance-check paragraph. COMPONENT/IAM/GLOBGRPH sections
untouched -- CVO~Z separately confirmed COMPONENT (442+199=641) and the 41-vs-40 doc count exactly, no
correction needed there. Notified CTO~Z and CVO~Z directly with the full explanation.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Rebuilt the classifier from scratch instead of patching the count to "explain away" the 3-node gap | The gap was a real symptom of a real defect (false positives in the depth heuristic); patching the number without fixing the method would have left the same bug latent for the next count this classifier touched |
| Kept F1's original narrative mechanism (vendored-dependency contamination) rather than rewriting it | CVO~Z did not dispute the mechanism, only the arithmetic's precision -- the correction is scoped to what was actually wrong |
| Wrote a full enumeration sidecar rather than just a corrected count | CVO~Z explicitly asked for spot-checkability against a population, not a repeated hand-picked example; a count alone doesn't satisfy that ask |
| Notified both CTO~Z and CVO~Z directly, not just the routing agent | CVO~Z raised the specific spot-check request personally; closing the loop with the actual requester matches RAVC discipline |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A.md` | Added ADDENDUM section + inline correction pointer + updated acceptance-check paragraph | No -- disk only, CTO~Z's lane re-commits |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A.json` | Added `CORRECTED_post_cvo_z_review` block, updated `could_not_fully_verify` | No -- same as above |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/A_lambda_enumeration.json` | New file -- full 333-node classification | No -- same as above |

---

## Blockers

None.

---

## Current State

Both of CVO~Z's conditions closed and reported. The LAMBDA disagreement is now proven, not just argued:
graph.json misses zero live Lambdas by name (191/191 coverage); its 333-vs-191 gap is 100% excess/noise,
precisely decomposed into 5 buckets with a full node-level enumeration for independent verification. CTO~Z
and CVO~Z both notified at 2026-07-25T00:03-00:04Z; awaiting CVO~Z's spot-check pass and CTO~Z's re-commit.
No further action pending on this lane unless the spot-check surfaces something in the 24-node residual
bucket or elsewhere.

---

## Next Steps

1. **Standing by** for `3.0.0_SA_CVO~Z`'s spot-check result and `1.0.0_SA_CTO~Z`'s re-commit -- no self-
   initiated action pending.
2. If the spot-check finds a misclassified node in any bucket, re-open and correct that specific bucket
   only -- the method (cross-reference against live+registry union) is now the documented standard for this
   lane's future LAMBDA-adjacent work, not a one-off patch.
