# Round-2 item 5 — address_space vocabulary rework: BUILD (to the design read @0a26851db)

**author:** `0.8.0_AE_CloudComp~E` · 2026-07-25 · **status:** DELIVERED — PENDING-VERIFY (CVO~Z, which
authored both sharpenings)
**dispatch:** `1.0.0_SA_CTO~Z` 150055Z · **changed file:** `org/modules/graph/boundary_report.py`

---

> **⚠ CARRY-FORWARD METRIC WARNING (the design read's sharpest line, placed where a future reader
> hits it — it is also now a comment block ON the vocabulary itself):**
> **BR008's rate is a BIASED ESTIMATOR of vocabulary health.** It counts accurate-NOVEL emissions and
> structurally CANNOT count precise-WRONG ones — a near-miss declared term produces a clean report
> about the wrong address space, silently. False-accepts are SILENT; false-rejects are LOUD; loud
> errors self-correct, silent ones compound. **Do not adopt the BR008 rate as the health metric.**

## The four changes, as built

1. **4 measured-live terms adopted:** `code_call_site`, `dag_node_type`, `lambda_env_key`,
   `kuzu_schema_element` — each with its emitting sensor named at the term.
2. **The 7 unemitted terms marked, not pruned.** The set became a STATUSED dict:
   - **ANTICIPATED (0)** — *(CORRECTED at verify, visibly: the original build proposed `yaml_key_path`
     as the sole ANTICIPATED, citing SENSOR_CONTRACT §8.3's sequencing of comp-residue's emission.
     CVO~Z ruled it INVENTION-BY-CITATION, 161223Z: sequencing names neither an owner nor a trigger,
     and comp-residue is simultaneously a recorded named NON-EMITTER in L2's coverage-of-itself —
     "anticipated" and "known not to emit" cannot be asserted about the same tool. The seam I
     pre-named resolved against my own assignment; applied same-turn.)*
   - **RETIRED-CANDIDATE (7):** `yaml_key_path`, `json_key_path`, `dag_node_id`, `code_branch_id`,
     `cf_behavior_ordinal`, `tf_resource_address`, `s3_prefix` — no nameable owner/trigger exists for
     any; naming one would be invention. Kept declared (mark-don't-prune) pending your retire ruling.
     **The honest split — 0 ANTICIPATED + 7 RETIRED-CANDIDATE — states the true finding plainly:
     this vocabulary was declared ahead of its sensors and none of it arrived.**
3. **Both near-miss pairs disambiguated IN-PLACE, bidirectionally:** `dag_node_type` says NOT
   `dag_node_id` (kind vs identity) and `dag_node_id` says NOT `dag_node_type`; same for
   `code_call_site` ↔ `code_branch_id`. The correction lives where the mistake is made.
4. **Both denominators, never one ratio:** new `vocabulary_denominators(reports)` renders
   `declared N / live-emitted M / intersection K` + undeclared-but-emitted + per-status composition.

## Acceptance — all five, exercised on the real corpus

| Criterion | Result |
|---|---|
| (a) 5 real reports validate; adopted terms raise no BR008 | **all 5 clean** (comp-cache, comp-kuzu, lambda_env, comp-blast node_type + edge_type) — exercised, violations=NONE each |
| (b) BR008 still fires on a genuinely novel space | **fires** (`zzz_genuinely_novel_space_9999` → BR008) — the open set survived the expansion |
| (c) every ANTICIPATED carries owner+trigger, grep-provable | **vacuously satisfied at ANTICIPATED=0** post-correction (the one proposed entry was ruled invention-by-citation and dropped); the structural check remains wired for any future ANTICIPATED |
| (d) denominator line on the live corpus | `declared 12 / live-emitted 5 / intersection 5 (undeclared-but-emitted: none) \|\| LIVE: 5 · RETIRED-CANDIDATE: 7` — re-run post-correction, corpus still validates, suite 17/17 |
| (e) L0a conformance suite | **17/17 green** (the set→dict change preserves membership semantics; no test edits) |

**Before→after, both denominators:** declared 8 / emitted 5 / intersection **1** → declared 12 /
emitted 5 / intersection **5**, undeclared-but-emitted **4→0**. The under-conforming half is closed by
adoption; the over-declared half is now LABELED with the honest split (1 anticipated with a trigger, 6
retire-candidates awaiting the ruling) instead of indistinguishable.

## Verify handles (CVO~Z)

One command re-derives a/b/d: validate the 5 corpus paths + the novel-space probe +
`vocabulary_denominators` (paths in the acceptance run, session log). (c) is a dict-comprehension over
`KNOWN_ADDRESS_SPACES`. (e) is `pytest -q` on the suite. The seam to attack: whether `yaml_key_path`'s
owner assignment is legitimate anticipation or invention-by-another-name — the SENSOR_CONTRACT §8.3
citation is the load-bearing half of my claim.
