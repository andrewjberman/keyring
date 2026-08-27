# TO-W4-BRACE — WAVE 4 ARTIFACT-SUBJECT CARDING (BRACE tranche)

**Issuer** `2.0.0_SA_COO~X` · **Executor** `0.8.0_AE_CloudComp~Y` · **Directive** D11
**Decomp pin** `@4ec2452a02` — the FACE's own last commit. Not HEAD, and not the rectangle, which lanes write values into.

**3 subjects · 21 card cells · 0 lane-owned mechanism cell(s).**

**Why this tranche is separable:** one part id denotes a SET. Ruled by the map's owner as ONE part carrying a DECLARED CARDINALITY and an ENUMERATED member list -- not expanded into N parts (that fabricates measurement at 14x, since not one member was measured individually) and not known_unsearched (these are known, located and finitely enumerable; that bucket is for unbounded runtime input). Members ENUMERATED rather than counted is what makes it falsifiable.

| part id | class | artifacts | cell_refs |
|---|---|---|---|
| `.comp-graph/platinum.CACHE_SET` | store | x5 | W4-lgbr-1 · W4-lgbr-2 · W4-lgbr-3 · W4-lgbr-4 · W4-lgbr-5 · W4-lgbr-6 · W4-lgbr-7 |
| `_build_manifest.json.SET` | output_artifact | x3 | W4-dncq-1 · W4-dncq-2 · W4-dncq-3 · W4-dncq-4 · W4-dncq-5 · W4-dncq-6 · W4-dncq-7 |
| `kuzu_nessie_db.rebuild.tmp.SET` | output_artifact | 1 | W4-vikb-1 · W4-vikb-2 · W4-vikb-3 · W4-vikb-4 · W4-vikb-5 · W4-vikb-6 · W4-vikb-7 |

**Members:**

- `.comp-graph/platinum.CACHE_SET` → `.comp-graph/platinum.dag.bd.cache` · `.comp-graph/platinum.dag.cot.cache` · `.comp-graph/platinum.dag.inf.cache` · `.comp-graph/platinum.dataflows.cache` · `.comp-graph/platinum.routing.cache`
- `_build_manifest.json.SET` → `infra/aws/globgrph/kuzu_nessie_db._build_manifest.json` · `infra/aws/globgrph/kuzu_db._build_manifest.json` · `infra/aws/globgrph/kuzu_stitch_db._build_manifest.json`
- `kuzu_nessie_db.rebuild.tmp.SET` → **NOT ENUMERABLE** — declared pattern `infra/aws/globgrph/kuzu_nessie_db.rebuild.tmp.<pid>.<monotonic_ns>.<counter> with an optional .wal sibling`; instances are runtime-named and no expansion of a template yields them

## YOUR SUBJECTS ARE FAMILIES, NOT FILES

Ruled by the map owner: **ONE part carrying a DECLARED CARDINALITY and an ENUMERATED member list**
for the two stable families — and **NOT for the third.**

- **NOT expanded into N parts** — each would need vintage, basis, evidence and owner, and **not one
  member was measured individually.** That fabricates measurement, which is Rule 28's own failure
  committed by the compile step.
- **NOT `known_unsearched`** for the stable families — that disposition was earned by an
  unbounded-runtime-input home where no stable identity can exist.

⛔ **The transient family IS NOT ENUMERABLE.** Proven at source: `_canonical.py:288` generates names
from `os.getpid()`, `time.monotonic_ns()` and a process counter, and `:292` `_gc_stale_tmps` actively
reaps them. **Six members were declared and zero existed; four existed and none were declared.
Overlap zero.** It carries a DECLARED PATTERN with `population_status: transient`, never a member
list — a fictional enumeration is worse than an honest pattern.

⛔ **USE A NESTED-GROUP EXPANDER.** A two-group pattern is 3 × 2 = **6, not 3**. Three seats reported
the fan-out as 11 — the issuer, a validation carrying it forward, and the map owner's first pass —
**because all three wrote the same single-group parser shape.**

## THE POPULATION, STATED WITH ITS EXCLUSIONS — never as a bare total

**42 manifest parts MINUS 3 resolved by L1's exact join MINUS 3 unbuilt future layers = 36 cardable.**

⛔ **The builder refuses to emit a bare total, because the issuer broke exactly this.** I named the
scope of "39" once and then quoted it in six messages without the exclusion attached; a peer reading
it against `parts=42` reasonably took it for a stale manifest count. We subtracted rather than
conceding — **14 − 12 = 2**, and the 2 were `graph_contracts` and `resource_summaries`, both remote,
both in the excluded set. **Both counts were correct over different populations.**

## WHY THIS WAVE EXISTS

Wave 3 carded **materializers** — writers, at (FILE, WRITE PATH) grain. The manifest describes
**artifacts**. Under the settled exact-1:1 rule only **3 of 42** parts resolve and **48 of 51** cards
fall to residue. The populations are near-disjoint, so the remedy is a different population — not a
looser join. A substring join would be *worse* than no join: the part id `cse` substring-matches any
prose containing those letters.

## ⛔ W4-m-joinable — THE ROW THIS WAVE EXISTS FOR

`artifact.location.home` must be an **exact identity a consumer can equality-join**, never prose.
Wave 3 put prose in **9 of 13** and the L0 compile step **could not derive the card→part join at
all**. **A card whose home cannot be joined will not reach the manifest, and it will look fine to a
reader.**

## ⛔ THE RECTANGLE IS NO LONGER A WRITE SURFACE

Ruled `@60404dcb80`. **Write ONLY `cells.<serial>.json` in your own deliverable directory.** The
rectangle is REGENERATED from those files by the issuer and carries `authority: DERIVED`. Three lanes
writing one file is a designed-in race and it already fired: a commit of mine moved **91 cells when I
intended 7**, putting 84 of another lane's delivered work under a message that never mentions it. The
merge REFUSES a lane writing a cell the rectangle seats elsewhere, and refuses the whole run rather
than dropping the row.

## STANDING RULES

⛔ **QUALIFY, DO NOT FIX.** A defect found in a carded artifact is REPORTED, not patched.

⛔ **RIGOUR ON THE OBJECT DOES NOT TRANSFER TO THE WRAPPER.** One wave-3 lane validated its cards
with six mutants and an ASCII sweep, then shipped the *instance* wrapping them without running its
gate once: 11 violations. **Run the gate on the wrapper.**

⛔ **A UNIFORM RESULT ACROSS A SET IS AN INSTRUMENT SIGNATURE.** Suspect any perfectly clean sweep.

⛔ **A CONTROL HAS ITS OWN SUBJECT.** This wave's brace control asserted a six-member expansion,
which tested that the expander *expands* and never that the expansion *denotes anything real*. Six
declared members, zero existed.

**Acceptance:** every cell carries `status`, `value`, `basis`, `evidence`, `owner`. Every count
prints its denominator. Every verdict names the instrument that produced it. `3.0.0_SA_CVO~X`
certifies at card level for wave 4.

<proof_of_spec>
population: 42 manifest parts MINUS 3 resolved by L1's exact join MINUS 3 unbuilt future layers = 36 cardable
cell_total: 257
</proof_of_spec>

<decomp_ref>
workflows/atom_decomposition/runs/nfra-substratecarding-w4/DECOMP.md
vintage_commit: 4ec2452a02
<owned_cells>
W4-dncq-1 W4-dncq-2 W4-dncq-3 W4-dncq-4 W4-dncq-5 W4-dncq-6 W4-dncq-7 W4-lgbr-1 W4-lgbr-2 W4-lgbr-3 W4-lgbr-4 W4-lgbr-5 W4-lgbr-6 W4-lgbr-7 W4-vikb-1 W4-vikb-2 W4-vikb-3 W4-vikb-4 W4-vikb-5 W4-vikb-6 W4-vikb-7
</owned_cells>
</decomp_ref>
