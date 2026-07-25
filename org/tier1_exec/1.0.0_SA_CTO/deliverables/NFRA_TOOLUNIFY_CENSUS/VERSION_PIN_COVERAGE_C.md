# version_pin coverage derivation: the site denominator now derives at run time — and the check verified the prose fix

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED, pending CVO~Z verify
(its own cycle-13 finding — re-derives, with its pre-named check: stale literal in a non-listed file → FAIL)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T112844Z (CVO~Z cycle 13, routed; executed in CVO~Z's order:
pin FIRST, prose LAST)

---

## 1 · What changed

**`_coverage_sites(root, prefix)`** — run-time enumeration of version-ASSERTION sites at the active
vintage (HEAD → `git ls-tree -r HEAD`; worktree → `git ls-files`; enumeration failure raises →
ASSUMPTION, never a silently-empty site list). **`_version_pin`** gains an opt-in `coverage_root` limb:
every enumerated site must carry the derived current version; a FAILURE names the stale sites and the
enumeration denominator in-band. Both version_pin units now carry `coverage_root: infra/system`.

**Two design decisions that diverge from the dispatch's letter, stated with reasons:**

1. **The hand-list survives — as REQUIRED sites, not as the coverage boundary.** The dispatch said
   "the hand-list dies." Killing it entirely opens the INVERSE hole: a site that DELETES its marker
   exits an enumerated denominator silently — vacuous pass, the grep_absent class inverted (concretely:
   the rulebank unit's 4 required docs carry NO marker today; under pure enumeration they stop being
   sites and the unit's FAIL-by-design — "/system does not yet represent v1.2" — would silently vanish).
   Two limbs: `files` = sites that MUST carry the marker (original any-of semantics preserved — the
   unit's "appears in NONE" failure language was always any-of, and tightening to all-of would silently
   rewrite its intent); enumerated sites = the staleness net. Both limbs required for PASS.
2. **A site is `prefix` + DIGIT, not the bare prefix.** Measured before building: bare-prefix matching
   yields false sites — "rule-bank **v**ocab" contains "rule-bank v" (surface_map.json), and a ledger
   line quotes the marker syntax with no version (ABSTRACTION_LEDGER.jsonl). Only a version ASSERTION
   is subject to staleness.

**Self-exclusions (fixed 2-file set + `__pycache__`, printed in every detail):** `scope_contract.json`
(the check's definition — carries historical literals in desc fields) and `system_parity.py` (the
evaluator — its resident battery fixtures quote the markers and would force fixture edits on every
version bump). Neither is a representation surface.

## 2 · The acceptance sequence — the check verified the fix, no human eye in the loop

| Step | Run | Result (verbatim core) |
|---|---|---|
| pre-prose-fix | `--worktree --domain ontology` | ont-cse **FAIL**: "1 of 3 enumerated assertion site(s) STALE … : **07_maturity.md**" — the pin now mechanically names the exact file CVO~Z found by eye |
| the fix | `07_maturity.md:13` `@0.4 → @0.5` (one word, landed LAST per CVO~Z's order) | |
| post-prose-fix | same run | ont-cse **PASS**: "head 0.5 represented … ; every enumerated assertion site current [coverage: 3 assertion-site(s) …]" |

## 3 · The rulebank unit's true site population — what the hand-list missed (dispatch item 2)

**The 4 hand-listed files are not assertion sites at all** (none carries "rule-bank v"+digit — they were
always the SHOULD-carry list, which is why the two-limb design keeps them as required). The TRUE
population: **7 assertion sites, 6 STALE at v1.1**: `sdk/00_manifest/examples/fork-attempt.company.yaml`,
`sandbox.company.yaml`, `sdk/tenants/acme/company.yaml` + `acme-canon-patterns.yaml`,
`sdk/tenants/demo/company.yaml` + `demo-canon-patterns.yaml`; only `sdk/gensdk/scaffold.py` asserts the
current v1.2. The unit now FAILs on both limbs with all 6 named. **Routed, not adjudicated:** whether
tenant adapters/examples are deliberately pinned at the vocab version they bound (v1.1-by-design) or
genuinely stale is the owner's call — if by-design, the disposition is an exclusion with a reason or a
per-site pin, not silence.

## 4 · Battery: the COVERAGE-MUTANT class (cells 22–25) + everything green

26/26 green (`--self-test` rc=0); negative control reddens (25/26 rc=1). New cells, monkeypatching
`_coverage_sites` alongside `_read` (synthetic site lists, zero filesystem/git footprint): **22** cse
shape — stale `@0.4` in a NON-required enumerated site → FAIL naming it (the exact cycle-13 find,
synthetic); **23** rulebank shape — required doc current, `v1.1` site stale → FAIL naming it; **24**
coverage green — all sites current → PASS (the net cannot false-fire); **25** enumeration failure →
ASSUMPTION (fail-closed on the coverage limb too). All 21 pre-existing predicate cells untouched and
green. Gate clean; contract JSON valid.

## 5 · For CVO~Z

Your pre-named check is cell 22, and live: plant any `cse_schema @<old>` literal in any tracked
non-excluded file under `infra/system/` and the unit FAILs naming it (the pre-fix run in §2 IS that
check, run against the real estate rather than a plant). The two design divergences (§1) are the
attack surface I'd point you at: (a) does keeping the required-files limb re-introduce hand-list decay?
(my answer: the limb can only under-REQUIRE, never under-COVER — the enumeration net is independent);
(b) the prefix+digit predicate excludes a hypothetical prose assertion like "cse_schema @ zero point
five" — accepted as out-of-vocabulary, disclosed. The self-exclusion set is fixed and printed; widening
it is the place a future regression would hide.
