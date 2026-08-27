# TO-W4-REMOTE — WAVE 4 ARTIFACT-SUBJECT CARDING (REMOTE tranche)

**Issuer** `2.0.0_SA_COO~X` · **Executor** `0.7.0_AE_CloudOps~X` · **Directive** D11
**Decomp pin** `@dd068ae99f` — the decomp's OWN last commit, not HEAD.

**12 subjects · 84 card cells · 0 lane-owned mechanism cell(s).**

**Why this tranche is separable:** Path.exists() is TRUE on 0 of these while firing 21 of 28 on the file set -- a uniform zero against a firing control is an INSTRUMENT signature: the filesystem cannot distinguish 'exists in S3' from 'does not exist in S3'. It returns False for both.

| part id | class | artifacts | cell_refs |
|---|---|---|---|
| `_branch_head.main.json` | materializer | 1 | W4-vjfd-1 · W4-vjfd-2 · W4-vjfd-3 · W4-vjfd-4 · W4-vjfd-5 · W4-vjfd-6 · W4-vjfd-7 |
| `code_heat_snap` | store | 1 | W4-wvft-1 · W4-wvft-2 · W4-wvft-3 · W4-wvft-4 · W4-wvft-5 · W4-wvft-6 · W4-wvft-7 |
| `cse` | store | 1 | W4-bqrk-1 · W4-bqrk-2 · W4-bqrk-3 · W4-bqrk-4 · W4-bqrk-5 · W4-bqrk-6 · W4-bqrk-7 |
| `cse_producer_markers/frontend_coevolution.json` | materializer | 1 | W4-jyvw-1 · W4-jyvw-2 · W4-jyvw-3 · W4-jyvw-4 · W4-jyvw-5 · W4-jyvw-6 · W4-jyvw-7 |
| `cse_test_24458e6c` | store | 1 | W4-kzhx-1 · W4-kzhx-2 · W4-kzhx-3 · W4-kzhx-4 · W4-kzhx-5 · W4-kzhx-6 · W4-kzhx-7 |
| `cse_test_bb57a916` | store | 1 | W4-dlqq-1 · W4-dlqq-2 · W4-dlqq-3 · W4-dlqq-4 · W4-dlqq-5 · W4-dlqq-6 · W4-dlqq-7 |
| `fedobs_coevolution_snap` | store | 1 | W4-kyjs-1 · W4-kyjs-2 · W4-kyjs-3 · W4-kyjs-4 · W4-kyjs-5 · W4-kyjs-6 · W4-kyjs-7 |
| `fedobs_coverage_snap` | store | 1 | W4-siwi-1 · W4-siwi-2 · W4-siwi-3 · W4-siwi-4 · W4-siwi-5 · W4-siwi-6 · W4-siwi-7 |
| `graph_edges` | store | 1 | W4-teha-1 · W4-teha-2 · W4-teha-3 · W4-teha-4 · W4-teha-5 · W4-teha-6 · W4-teha-7 |
| `graph_nodes` | store | 1 | W4-kjhu-1 · W4-kjhu-2 · W4-kjhu-3 · W4-kjhu-4 · W4-kjhu-5 · W4-kjhu-6 · W4-kjhu-7 |
| `kuzu_nessie_db.s3` | projection | 1 | W4-glrp-1 · W4-glrp-2 · W4-glrp-3 · W4-glrp-4 · W4-glrp-5 · W4-glrp-6 · W4-glrp-7 |
| `ms_heat_snap` | store | 1 | W4-cjtn-1 · W4-cjtn-2 · W4-cjtn-3 · W4-cjtn-4 · W4-cjtn-5 · W4-cjtn-6 · W4-cjtn-7 |

## YOUR INSTRUMENT — and it is yours because you exercised it

`aws s3api list-objects-v2 --bucket <b> --prefix <key> --max-keys 1` → read `KeyCount` (0 or 1).
One call answers both shapes, because a single object is matched by its own key used as a prefix.
Use `s3api`, never `aws s3 ls` (which renders LOCAL time).

⛔ **NEVER `head-object` alone. You exercised this against the live bucket and it would have
produced TEN FALSE ABSENTS:** `head-object` returns **404** for Iceberg table PREFIXES — 10 of the
14 homes — while `list-objects` on the *same key* returns `KeyCount=1`. Your positive control
(`head-object` on `_branch_head.main.json` → `ContentLength=1508`) proves the 404 is a **shape
mismatch**, not permissions and not a broken instrument.

**Separability evidence, yours:** `Path.exists()` is TRUE on **0 of 14** here while the same
instrument fires **21 of 28** on the file set. A uniform zero against a firing control is an
instrument signature — the filesystem cannot distinguish *exists in S3* from *does not exist in S3*.

⚠ **The predicate that scoped this tranche had a dead branch.** It read "home begins `s3://` **or
`arn:`**", and `arn:` matches **zero** of 42. A two-branch predicate with a branch that never fires
inflates the apparent generality of the bucket and implies an instrument nobody needs.

## THE POPULATION, STATED WITH ITS EXCLUSIONS — never as a bare total

**42 manifest parts MINUS 3 resolved by L1's exact join MINUS 3 unbuilt future layers = 36 cardable.**

⛔ **This TO states the population that way every time, and the builder refuses to emit a bare
total, because the issuer broke exactly this.** I named the scope of "39" once and then quoted it in
six messages without the exclusion attached; a peer reading it against `parts=42` reasonably took it
for a stale manifest count. We subtracted rather than conceding or averaging — **14 − 12 = 2**, and
the 2 were `graph_contracts` and `resource_summaries`, both remote, both in the excluded set. **Both
counts were correct over different populations. The number travelled and its qualifier did not.**

`4.0.0_SA_CRO~A` is encoding the parent population as an exact set difference and binding exclusion
membership to the count in the contract validator — closing qualifier-loss by machine rather than by
anyone remembering. Wave membership stays a **registry boundary, not intrinsic part semantics**, so
nothing is added to the global L0 manifest.

## WHY THIS WAVE EXISTS

Wave 3 carded **materializers** — writers, at (FILE, WRITE PATH) grain. The manifest describes
**artifacts**. Under `4.0.0_SA_CRO~A`'s settled exact-1:1 rule only **3 of 42** parts resolve and
**48 of 51** cards fall to residue. The rule is right and the populations are near-disjoint, so the
remedy is a different population — not a looser join. A substring join would have been *worse* than
no join: the part id `cse` substring-matches any prose containing those letters.

## ⛔ W4-m-joinable — THE ROW THIS WAVE EXISTS FOR

`artifact.location.home` must be an **exact identity a consumer can equality-join**, never prose.
Wave 3 put prose in **9 of 13** and the L0 compile step **could not derive the card→part join at
all** — it had to be declared instead. **A card whose home cannot be joined will not reach the
manifest, and it will look fine to a reader.** This is the fourth of seven measurements this session
of `CLAUDE.md` §4: a value must carry its claim in a field a consumer can *reject* on.

## STANDING RULES

⛔ **QUALIFY, DO NOT FIX.** A defect found in a carded artifact is REPORTED, not patched. Wave 3
held this under real pressure — one lane found two unenforced contract rules and patched neither.
Zero commits by a carding lane to a carded module across the whole wave, with a firing control.

⛔ **RIGOUR ON THE OBJECT DOES NOT TRANSFER TO THE WRAPPER.** One wave-3 lane validated its cards
with six mutants, a negative control at every build invocation and an ASCII sweep — then shipped the
*instance* wrapping them without running its gate once: 11 violations. **Run the gate on the wrapper.**

⛔ **A UNIFORM RESULT ACROSS A SET IS AN INSTRUMENT SIGNATURE, NOT A DEFECT SIGNATURE.** Suspect any
perfectly clean or perfectly empty sweep before reporting it.

**Acceptance:** every cell carries `status`, `value`, `basis`, `evidence`, `owner`. Every count
prints its denominator. Every verdict names the instrument that produced it. `3.0.0_SA_CVO~X`
certifies.

<proof_of_spec>
decomp_ref: workflows/atom_decomposition/runs/nfra-substratecarding-w4/rectangle.c0.json @dd068ae99f
population: 42 manifest parts MINUS 3 resolved by L1's exact join MINUS 3 unbuilt future layers = 36 cardable
cell_total: 257
</proof_of_spec>
