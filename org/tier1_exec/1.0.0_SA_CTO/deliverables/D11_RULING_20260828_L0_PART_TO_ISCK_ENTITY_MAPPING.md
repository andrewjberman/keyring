# DESIGN-LANE RULING — the L0 manifest part → ISCK entity join (WP-3b, 2026-08-28 15:1xZ)

**Finding:** `0.4.0_DT_ClientPlatform~X` 78074 (WP-3b unit 1 @6176b7d4ae): the translator, run against the pinned
population (the emitted L0 manifest `graph_object_manifest.json` @2feca185e7, 42 parts), **translated 0 / ERRORED 42**
with ONE distinct missing-field set — `entity_class`, `plane`, `entity_grain`, `identity_scope`, `identity_policy` absent on
42 of 42. The manifest's vocabulary (part_class · home · authority_role · temporal_claim · lineage · generation ·
population_status · vintage · basis · evidence · owner · grain · key · failure_mode · member_set) contains none of the
ISCK entity contract's five identity fields. **Two schemas that were never joined** — not a data-quality shortfall.
Upheld by `3.0.0_SA_CVO~X` 150659Z (one uniform declaration gap, not 42 defects; owner remedy preferred: the emitter
declares the five fields per part with cited vocab).

**What DT~X refused, correctly:** mapping `part_class → entity_class` ("both end in class") — a green run that would have
admitted 42 entities, passed every gate, produced a real snapshot digest and a positive control returning 42, and asserted
something false about the estate.

## THE RULING (form (a) + (b): ruled ONCE here; lands as DATA the emitter carries and the translator reads)

The mapping is `org/standards/isck/ledger/translation/L0_PART_IDENTITY_MAPPING.json` (v0; NOT a bundle member; the
contract `v0.3-candidate+27` does not move). Every value it yields carries **basis `held`** with that file @commit as the
evidence — never `measured`. Summary of the rules, each cited to a registry or a declaration rather than minted:

| field | value | source |
|---|---|---|
| `entity_class` | **`part`** (uniform) | ISCK vocab `entity_classes.json` carries `part` for exactly this; the manifest's `part_class` is a graph-object taxonomy and travels on the binding's native-key context, not on `entity_class` |
| `entity_grain` | **`part`** (uniform) | the L0 registry's own grain; L1's per-plane grains belong to the parts' MEMBERS, which the slice does not admit |
| `identity_scope` | **`logical`** (uniform) | contract enum; a registry part is a logical object, its instances are `surface_version`s / `materialization_run`s |
| `plane` | by `home_space`: `repo_path→file`, `s3_uri→arn_resource`, `iceberg_table→arn_resource`, `none→unplaced` | L1's canonical grain declaration @16cd74c870 (FOUR planes: symbol, file, arn_resource, chain_motif); a part's plane is its home's plane; a homeless part fits no L1 plane and is NOT forced into one |
| `identity_policy` | by `home_space`: `repo_path→git_history_v0`, `s3_uri→provider_key_v0`, `iceberg_table→provider_key_v0`, `none→held_for_adjudication` | ISCK vocab `identity_policies.json` (8 registered; none minted here) |

**The one new token — `unplaced` — and its four-postulate record (Rule 24):** axis = the plane a part is comparable within;
grain = one manifest part; intent = one (which L1 plane, or none); MECE over the declared domain = L1's four planes + the
member "no plane" (a homeless part) — `unplaced` closes the population honestly; state coherence = `unplaced → <plane>` is a
DECLARATION act (a later home or a declared bridge), never a re-read; word-boundary token census at ruling time over
`org/standards` + `docs/doctrine` + the two D11 PRDs: **0 hits** — no collision. `plane` is a free string in the contract,
so no contract byte moves.

**Denominators at ruling time** (working-tree copy of the pinned manifest, 42 parts, compiled 2026-08-27T11:27:48Z
@e48a7466ba; the translator RE-DERIVES these at run time and prints its own line — these are not the number):

| part_class × home_space | parts | → plane / policy |
|---|---|---|
| store × s3_uri | 11 | arn_resource / provider_key_v0 |
| store × repo_path | 10 | file / git_history_v0 |
| output_artifact × repo_path | 6 | file / git_history_v0 |
| projection × repo_path | 5 | file / git_history_v0 |
| materializer × none | 3 | **unplaced / held_for_adjudication** |
| materializer × s3_uri | 2 | arn_resource / provider_key_v0 |
| spec_artifact × repo_path | 2 | file / git_history_v0 |
| materializer × repo_path | 2 | file / git_history_v0 |
| projection × s3_uri | 1 | arn_resource / provider_key_v0 |
| **TOTAL** | **42** | **39 placed (25 file, 14 arn_resource) · 3 held_for_adjudication · 0 forced** |

## WHAT MOVES, BY SEAT

- **`0.4.0_DT_ClientPlatform~X` (TO-WP3b, unit 2):** the translator reads the mapping file (its digest printed), yields the five
  fields with `basis: held` + evidence = the file @commit, and prints per part: part id, part_class, home_space, the five
  values, the mapping digest. A part under `held_for_adjudication` is ADMITTED (the contract's own policy) and counted in the
  admitted denominator with its policy named. Expected shape, from the table above and re-derived by the run: admitted 42
  (39 placed + 3 held) / refused 0 / errored 0 — **the run's line governs.** AC4/AC5 become reachable on N>0.
- **The (b) half — the L0 manifest carries the join as a RECEIVER:** `L0_GRAPH_SUBSTRATE_MANIFEST.schema.json` gains an
  `identity` receiver on `part` (claim_status declared/unknown; the five fields; basis/evidence/owner; the same
  null-under-unknown semantics as the `key` receiver), landed by this seat as the next commit; the L0 EMITTER (DT~X's,
  under a later TO) populates it FROM this mapping so the manifest itself says what the translator currently derives, and
  the translator then reads the manifest, never a side table. Until the emitter lands, the translator's mapping read is the
  bridge; both print the same values or that is a finding.
- **`3.0.0_SA_CVO~X`:** the replay subject is the translator's printed per-part line against this file's digest.
- **Contestable:** every value is a claim a `contest_event` can target; a KILL of a row is a finding against the mapping
  routed to the design lane and moves `mapping_version`.

Push state: LOCAL at writing (origin/CLOUD @98a25b3112).
