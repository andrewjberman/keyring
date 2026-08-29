# NFRA_SUBSTRATECARDING -- RULE-28 COVERAGE CENSUS (the zero-graduation denominator)

**Seat** `1.0.0_SA_CTO~Y` -- **for** `2.0.0_SA_COO~X` (issuer; owner of the graduation act) -- cc `1.0.0_SA_CTO~X` (design lane), `3.0.0_SA_CVO~X` (certifier)
**Handed** by the issuer 80827 under the split 1.0.0_SA_CTO~X proposed (80816) on Andrew's 03:45Z word at this terminal.
**Written** 2026-08-29 05:3xZ. **Card population pin** = the settled v3.1 pin `cf66984cfc` (the receipt `D11_V31_SETTLED_RECEIPT_cf66984cfc.md`). **Manifest pin** = worktree `graph_object_manifest.json` (as_of compiled 2026-08-27T07:10:00Z @e48a7466ba, 42 parts).

## 0. WHAT THIS IS AND IS NOT

A MEASUREMENT: the Rule-28 subject population enumerated on four declared axes, each with its denominator printed, joined against the cards at the settled pin, the uncarded remainder LISTED. **No card is written. No remediation. No verdict on `status`** -- the graduation flip is the issuer's act on what this returns (80827 (2)), and this census would rather refuse to close the project than be shaped to.

Method: population files read at the pin (`git show cf66984cfc:<path>` for every card; the tree list `git ls-tree -r cf66984cfc` for the file census); joins by exact `subject_id`/`location.home` after slug normalisation, then by long-token containment (>= 10-12 chars) -- every containment match was eyeballed and one false match (below, sec 2) was removed by hand. Instrument: python at this seat, scratchpad `census_b_*.json`.

## 1. THE CARD POPULATION AT `cf66984cfc` -- what "the 72" actually is

| carrier | count | note |
|---|---|---|
| JSON files under `org/tier2_senior/*/deliverables/D11_CARDS*/` | **81** | the tree list |
| of which schema_version **3.1** cards | **72** | == the receipt's 72 exactly; `trust.key.key_expression` present 72/72, non-null 71/72; verdict.standing QUALIFIED 60 / UNSOUND 10 / INCOMPLETE 2 |
| of which schema_version **1** cards | **8** | the PRD sec-2 wave-1 subjects (C0, C1, C2, C3.i-as-built, D1, D2, D3, comp-similar) -- the receipt's "not-v3 8" |
| of which a CELLS carrier, not a card | **1** | `0.8.0_AE_CloudComp/deliverables/D11_CARDS_W4/W4-FILE.cells.json` (148 cells / 22 subjects) |
| cells carriers OUTSIDE the D11_CARDS dirs | 4 | `0.7.0_AE_CloudOps/deliverables/cells.0.7.0_AE_CloudOps~X.json` @a5fffa2bb7 (84 cells / 12 subjects, 75 MEASURED / 6 ABSENT / 3 INFERRED; `key_expression` absent from the file) -- ancestor of cf66984cfc and on origin; plus `workflows/.../nfra-substratecarding-w4/cells.{0.8.0_AE_CloudComp~X, ~Y, 2.0.0_SA_COO~X}.json` |

>> **The 72 is the v3.1 CARD-FILE population. It is not the carded-subject population.** Wave 4's REMOTE tranche (12 subjects, CVO VERIFIED PASS at TO level) lives only in a cells carrier, and KEYFILL's glob (`org/**/D11_CARDS_W*/*.json` + schema_version) could not see it -- so those 12 subjects were never asked for a `key_expression`. <<

## 2. AXIS P2 -- THE L0 GRAPH-OBJECT MANIFEST (42 parts; the fabric's own registry of stores / materializers / projections / outputs / specs)

```
  42 manifest parts
  = 31 with a v3.1 (or v1) CARD FILE at cf66984cfc
  +  7 carded ONLY in the REMOTE cells carrier (no card file, no key_expression)
  +  1 cut in wave 4 (7 cell ids in the W4 DECOMP) with NO card located at this seat   <- kuzu_nessie_db.rebuild.tmp.SET
  +  3 UNBUILT BY CONSTRUCTION (PRD sec 10.2: not debt)                                <- affinity_matrix, identity_and_succession, similarity_network_fusion
  = 42
```
The 7 cells-only: `code_heat_snap`, `cse` (THE PRODUCTION CSE STORE), `cse_test_24458e6c`, `cse_test_bb57a916`, `fedobs_coevolution_snap`, `fedobs_coverage_snap`, `ms_heat_snap` -- all warehouse stores, all in TO-W4-REMOTE's subject table. (The other 5 REMOTE subjects -- `_branch_head.main.json`, `cse_producer_markers/frontend_coevolution.json`, `graph_edges`, `graph_nodes`, `kuzu_nessie_db.s3` -- ALSO carry a W2/W3 card file, so they are double-carded across two carriers.)
*Instrument note: a first containment join matched `kuzu_nessie_db.rebuild.tmp.SET` to a `kuzu_nessie_db` card and printed 32 carded; the match was false (no card's subject_id or home contains "rebuild"). Corrected to 31 + 1. Wave 4's own population statement was "42 - 3 L1-resolved - 3 unbuilt = 36 cardable"; 35 of those 36 have a carrier somewhere, 1 has none located.*

## 3. AXIS P3 -- THE WRITER POPULATION (the materializers the manifest itself names in `generation.materializer`; Andrew's 0015Z test: "resolvable crucial dependencies for materializers")

Resolvable generator paths named by the manifest: **32** (regex over the 42 parts' materializer strings for repo paths / comp-tool names). Carded (any card file, any wave): **13**. **UNCARDED: 19**, listed:

| generator (as the manifest names it) | writes (manifest parts) | resolves to |
|---|---|---|
| `infra/aws/globgrph/_canonical.py` | kuzu_nessie_db.rebuild.tmp.SET | file, tracked |
| `infra/aws/globgrph/_provenance.py` | _build_manifest.json.SET | file, tracked |
| `infra/aws/globgrph/code_heat_emit.py` | code_heat_snap | file, tracked |
| `infra/aws/globgrph/cse_emit_agent.py` | cse | file, tracked |
| `infra/aws/globgrph/cse_emit_deploy.py` | cse | file, tracked |
| `infra/aws/globgrph/cse_emit_graphhead.py` | cse | file, tracked |
| `infra/aws/globgrph/cse_emit_promote.py` | cse | file, tracked |
| `infra/aws/globgrph/cse_producers_nightly.py` | cse | file, tracked |
| `infra/aws/globgrph/derive_stitch.py` | stitch_graph.json (THE WRITER of view 2's source) | file, tracked |
| `infra/aws/globgrph/emit_fedobs_snap.py` | fedobs_coverage_snap | file, tracked |
| `infra/aws/globgrph/extract_portal_stitch.py` | stitch_graph.json | file, tracked |
| `infra/aws/globgrph/kuzu_incremental_refresh.py` | kuzu_nessie_db.fallback.jsonl, kuzu_nessie_db.local | file, tracked |
| `infra/aws/globgrph/kuzu_nessie_load.py` | kuzu_nessie_db.local, kuzu_nessie_db.s3 (THE canonical projection loader) | file, tracked |
| `infra/aws/globgrph/ms_cloud_extract.py` | ms_heat_snap | file, tracked |
| `org/modules/graph/gen-estate-resolver.py` | estate-coverage-resolver.json | file, tracked |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MOTIF_c2c3_materialize_spec.py` | motif_c2c3_materialize.json (the C2 class-spec materializer) | file, tracked |
| `comp-trace` (graph build) | .comp-graph/graph.json | `.tools/comp-trace`, tool family |
| `comp-iam` (managed-policy resolution) | .comp-graph/managed_policy_actions_cache.json | `.tools/comp-iam`, tool family |
| `comp-platinum` (per-firm cache build) | .comp-graph/platinum.CACHE_SET | `.tools/comp-platinum`, tool family |

The 13 carded: `cse_emit_frontend_coevolution.py` (W3, 2 paths), `cse_store.py` (W3, 2 paths), `derive_runner.py` (W3, 2 paths), `kuzu_load.py`, `kuzu_stitch_load.py`, `resource_summaries_store.py`, `snap_store.py` (W3 + W4 WRITER), `incremental_updater/lambda_function.py` (W3, 2 paths), `comp_aws_cli.py` (W3), `nerves_resolve.py` (W4), `c2_individuate.py` + `c3_cover.py` (W2), `NFRA_MOTIF_P1_canonical_ab_catalog.py` (W2).
*Grain note (wave 3's own lesson): the carded writers are at (FILE, WRITE PATH) grain; the 19 above are counted at file grain and each may split into more than one write path when carded -- 19 is a FLOOR on the uncarded writer count, not a ceiling.*

## 4. AXIS P4 -- WAVE 2's OWN DERIVED LIST (44 subjects harvested from wave-1 cards' q1/q4; `subjects.json`)

44 = **37 carded** + **7 uncarded**. The 7, classified under Andrew's 0015Z test (verbatim: *"not to hit random phrases and concepts, it was to hit the actual things that are resolvable crucial dependencies for materializers and ontological functions"*):

| subject | resolves to an artifact? | class |
|---|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MOTIF_c2c3_materialize_spec.py` | YES | RESOLVABLE, UNCARDED (also P3 row) |
| D1's EdgeKind semantic | no -- a value enum inside a rail block | fragment (CCY declined it under the ruling, `W2-iarh`) |
| D3's delivery_cadence obligation | no -- an enum member inside a rail block | fragment (`W2-jlsi`) |
| live graph node types: Field, Prop, S3Key, S3_BUCKET, DYNAMODB_TABLE | partly -- a population, not a file | borderline (`W2-ifqm`, not written) |
| live graph edge types: FLOWS_TO, READS_FIELD, ... | partly | borderline -- NOTE `W2-kwjy d1_bound_live_graph_edge_types` IS carded; this row is the wave-2 string that did not slug-match it; counted UNCARDED here to stay on the instrument, but a reader should treat it as carded |
| live AWS estate | no -- a plane | phrase |
| repo source tree | no -- a plane | phrase |

## 5. AXIS P1 -- THE PRD sec-2 WAVE-1 RUNGS AND RAILS (8)

8 of 8 carded -- **all at schema_version 1, none at v3.1.** The foundational eight (C0, C1, C2, C3.i-as-built, D1, D2, D3, comp-similar) are outside the 72-card v3.1 population, were never re-stamped, and carry no `trust.key.key_expression` (the field does not exist in v1). A vintage gap, not an absence.

## 6. THE REMAINDER, LISTED (what the issuer asked for)

```
  NO CARD ANYWHERE, RESOLVABLE (the true uncarded remainder) ........ 20
      19 writers (sec 3)  +  kuzu_nessie_db.rebuild.tmp.SET (sec 2)
  CARDED IN A CARRIER THE v3.1 CENSUS DOES NOT READ (cells-only) ...... 7   (sec 2; 12 REMOTE subjects, 5 of them double-carded)
  CARDED AT v1 ONLY (vintage gap) ..................................... 8   (sec 5)
  UNBUILT BY CONSTRUCTION, correctly absent ........................... 3   (sec 2)
  FRAGMENTS / PHRASES, excluded under the 0015Z test, with reason ..... 6   (sec 4; one of them is in fact carded under a slug)
```
Denominators used, so nobody re-derives them: cards 81 files (72 + 8 + 1); manifest 42; writers 32; wave-2 derived 44; wave-1 8.

## 7. WHAT THIS CENSUS DOES NOT COVER (stated, not implied)

- Generators named ONLY inside cards' `methodology.composes` / `location.projection_of` / `co_resident_stores` prose and NOT in the manifest -- 189 distinct strings, of which 143 match neither a card nor a manifest part; **they are the wave-2 harvest class Andrew cut, and are NOT counted here as remainder.** They are in scratchpad `census_b_join.json` for anyone who wants the list; most are phrases, some are real (e.g. `org/modules/graph/derive_stitch.py`, `org/modules/graph/extract_pipeline.py`, `graph_cache.py`, `kuzu_cli.py`, `platinum_cli.py`, `cse_schema.py`, `debris_adapters.py`). A materializer-first walk (start at each of the 32 writers, enumerate what it READS) would bound that set properly; that walk is not this census.
- Write-path multiplicity of the 19 uncarded writers (sec 3 note).
- Whether any carded subject's card is CURRENT (as_of spans 2026-08-26T22:17Z .. 2026-08-27T08:23Z over the 72; the manifest is 07:10Z 08-27) -- vintage coherence across the wave is a separate check.

## 8. COMPILER TOOLS

| tool | invocation | result |
|---|---|---|
| `git ls-tree -r cf66984cfc` | D11_CARDS* file census | 81 files |
| `git show cf66984cfc:<path>` x81 | every card read at the pin | 72 v3.1 / 8 v1 / 1 cells |
| python join (slug + containment) | 4 axes | numbers above; one false containment match caught and removed |
| `git merge-base --is-ancestor` | a5fffa2bb7 vs cf66984cfc, ebd767e803 | YES, YES |
| comp-find (earlier, corpus=all) | NFRA_SUBSTRATECARDING 1,221 hits / 126,159 files | orientation only; counts of what was written |
