**archetype:** IMPLEMENT

# Session Log -- ADVI_DEMOV1.006 Phase 1 Design: Path B Structured-PII-Tagging-at-Build-Time

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-24
**Branch:** CLOUD
**Session start:** 2026-05-24T21:52Z (MSTR INITIAL-CHARTER `20260524T215233Z`, CY-0088 SS-0002 §7 step 14 / LD-0050 / SPAWN-WITH-DIRECTION pattern)
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_DEMOV1.006.dsc-leak-detection-mechanism-class-change.md` (re-routed `~C` -> `~D` per commit `9b5543054` per LD-0030 attempt-13-SUCCESS sequencing + LD-0021 staging)
**Tier-0 law state:** `tier0_commit_hash: 1a515b769` (CONSTITUTION v1.2 + STAKES_MATRIX v1.4 + DIRECTIVES v1.10)
**Phase:** 1 of 5 -- DESIGN (this commit). Phases 2-5 = implementation, FN-1 fixture, transform re-run, R5 + RAVC2.

---

## Objective

Author the Path B primitive design + AC5 defense-in-depth call + FN-1 fixture skeleton as the first Phase-1 artifact for ADVI_DEMOV1.006. This is the design-doc commit that gates the Phase-2 implementation; no `data/demo/scripts/transform/*.py` edits land in this commit.

---

## Provenance chain understood

D-001 v1.7 (sovereign-pending-backstop) -> LD-0026 generalized backstop framework (Andrew 2026-05-24T01:40Z) -> LD-0029 architectural-fork surface (2026-05-24T02:35Z) -> Andrew sovereign direct-route "Ask CVO" 02:45Z -> CVO CORROBORATE Path B verify-channel GREEN at MECHANICAL/NOVEL/META verdict `293649cc0` (file `org/tier1_exec/3.0.0_SA_CVO/logs/2026-05-24/spot_check_0353Z_LD0029_path_b_verdict.md`) -> MSTR LD-0030 ratification + materialization charter `b58751842` (supersedes LD-0029) -> COO TO author + GO `bde6ae3bd` (originally `<issued_to>~C</issued_to>`) -> attempt-13 SUCCESS empirical anchor `dbf170b32` -> `_embeds_real` guard achieves R5 PASS `leak_count=0/22,260` (DS~C close-out `469df551f`, CVO CORROBORATE AC5 `95e2b366e`) -> per LD-0030 attempt-13-SUCCESS sequencing, Path B becomes durable follow-on (NOT supersession) -> COO TO reassignment commit `9b5543054` re-routes to DS~D.

## Iteration-history baseline (substring-scan ceiling)

12-attempt substring-scan iteration enumerating collision-classes, each fix addressing one failure mode but allowing the next to surface. Within-class structural shift `_embeds_real` at `dbf170b32` (attempt-13) achieved R5 PASS — the strongest available within the current mechanism class. CVO META layer 3 (verbatim from `293649cc0`):

> "the substring-scan primitive is *checking after the fact* for fragments that should never have been allowed IN. Structured-PII-tagging-at-pseudonymizer-build-time is *preventing by construction* — knowing all real names upfront (DS factory already pre-seeds in attempt-10) means the pseudonymizer can structurally guarantee no overlap, eliminating the entire 'did a fake accidentally embed a real name' failure class."

Path B is the mechanism-class-change that delivers prevent-by-construction.

---

## Design framing: Path B as construction-time corpus-bind (extension of CVO 2D-coverage pattern)

CVO's AC5 verdict (`95e2b366e`, file `org/tier1_exec/3.0.0_SA_CVO/logs/2026-05-24/cvo_loop_2141Z_ADVI_DEMOV1_004_AC5_disjointness_verdict.md`) banked a 2D-coverage pattern as the load-bearing insight (FN-2):

> "Substring-scan binds the haystack (would-be-leaks against value-cells of all S3 objects). Set-disjointness binds the namespace (corpus-completeness against namespace-key-cells of pseudonymized dict-structures). Together: 2D coverage on PII leakage by leak-class."

**Path B is the CONSTRUCTION-TIME extension of the corpus-bind half** — same architectural direction (corpus-bind), shifted from VERIFICATION-TIME (AC5 method, applied to dict-keys after generation) to CONSTRUCTION-TIME (the candidate pool itself is structurally disjoint before generation).

Map of the architectural surface:

| Bind direction | Verification-time (post-hoc) | Construction-time (Path B) |
|---|---|---|
| **Haystack-bind** (value-cells) | `pii_leak_scan.py` substring scan against TARGET bucket | `_embeds_real` runtime guard at generation (attempt-13 within-class ceiling) -- becomes ZERO-FIRE safety net under Path B |
| **Corpus-bind** (namespace/key-cells) | AC5 Identity #5 set-disjointness on `nna.quarterly[*].by_adv.keys()` | **Path B**: candidate pool filtered upfront against real-fragment index -- structurally disjoint by construction |

Under Path B:
- The construction-time corpus-bind is the PRIMARY mechanism (prevent by construction)
- The verification-time corpus-bind (AC5 method) becomes a CONSTRUCTIVE-INVARIANT VERIFIER (confirms the bind holds end-to-end)
- The verification-time haystack-bind (substring scan in `pii_leak_scan.py`) becomes a VERIFY-NOT-DETECT step (zero by construction)
- The runtime haystack-bind (`_embeds_real` at generation) becomes a DEFENSE-IN-DEPTH SAFETY NET for any fragment class not covered by the structured index (the FN-3 common-name false-negative bound CVO surfaced; the iteratively-grown leaker-set protection layer)

The pattern's deeper insight (CVO FN-2 + COO §2 of ACK `20260524T22xxxxZ`): both Path B and the AC5 method are instances of CORPUS-BIND. Path B is the strongest expression of CVO's 2D-coverage framing in the SAME direction (corpus, not haystack), but at the EARLIEST possible time (construction, not verification).

---

## RealFragmentIndex -- 4 fragment classes

Built once at factory pre-seed time (the existing call site `demo_transform.py:327-332` where `factory._used_person.update(nms)` + `factory._real_names.update(nms)` already enumerates the real-name universe). The index is a precomputed lookup structure, not a substring scan:

```python
@dataclass
class RealFragmentIndex:
    full_names: frozenset[str]            # ATTEMPT-9 anchor; exact-match class
    name_tokens: frozenset[str]           # ATTEMPT-10/austin_thompson; token-level class
    couple_components: frozenset[str]     # ATTEMPT-11/Sullivan,Dan-in-Sullivan,Danielle; substring class
    surname_cohorts: frozendict[str, frozenset[str]]  # ATTEMPT-12/Powell+Winslow+Clarke; surname -> first-name set
```

### Class derivations (from existing `_real_names` set)

1. **`full_names`** — every real full name as currently held in `_real_names` (preserved verbatim). Catches: exact-match leak (a fake equal to a real). Existing primitive; not new.

2. **`name_tokens`** — for every real name `r`, split on whitespace + `,` + `&` + ` and ` and add each token to the set. Catches: fake "Austin Hawthorne" where "Austin" is a real first-name token. Empirically validates: attempt-9 `austin_thompson` slug-collision class.

3. **`couple_components`** — for every real couple name (containing ` & ` or ` and `), split into the two component names `c1`/`c2` and add each. ALSO for every "Last, First" component, add the prefix substrings ("Last,", "Last, F", "Last, Fi", ... up to len(component)) so a fake "Sullivan, Danielle" structurally excludes against the real "Sullivan, Dan" component. Catches: attempt-10 prefix-substring class (the `_embeds_real` motivating example). Implementation: a sorted-tuple lookup keyed by surname + first-name-prefix length, NOT a Python `in` substring scan.

4. **`surname_cohorts`** — for every real surname `s` appearing in 2+ real names, record `s -> {first_names_with_that_surname}`. Catches: attempt-11 Powell/Winslow/Clarke shared-surname couple-component class. At generation time, when assembling a fake couple with surname `s`, the structured check rejects any fake first-name in the cohort.

### Index build cost

O(|real_names|) one-time at factory pre-seed; ~3,000 names × ~4 tokens = ~12,000 token insertions. Memory: ~1MB. Trivial vs the 22,260-object transform runtime (~12h wall).

---

## Candidate-pool filtering at factory init

At factory pre-seed (or first-generation-call gated by `factory._real_names` non-emptiness), filter the static fake pools:

```python
# In FakeIdentityFactory.__init__ or seal_real_names():
self._FIRST_NAMES_FILTERED = tuple(n for n in _FIRST_NAMES if n not in self._idx.name_tokens)
self._LAST_NAMES_FILTERED  = tuple(n for n in _LAST_NAMES  if n not in self._idx.name_tokens)
self._FIRM_LEAD_FILTERED   = tuple(n for n in _FIRM_LEAD   if n not in self._idx.firm_tokens)
self._FIRM_TAIL_FILTERED   = tuple(n for n in _FIRM_TAIL   if n not in self._idx.firm_tokens)
```

Result: a curated pool where no individual token can produce a token-level leak by construction. The fake "Austin Hawthorne" cannot be generated because "Austin" was filtered out of `_FIRST_NAMES_FILTERED` upfront.

Existing pool sizes (149 first / 96 last / 12 firm-lead / 6 firm-tail) vs 49F's ~3,000 names: empirically very few tokens overlap (most real names are uncommon enough). Expected pool reduction < 5% per class. The bucket arithmetic in `_bucket()` still works against the filtered tuples.

If a filtered pool reduces below the entity count after intersection (rare but possible), the `_person_name` probe loop already raises `RuntimeError("name pool exhausted")` — same fail-loud failure mode. The Phase-2 implementation will surface a clear error if the filter is too aggressive (e.g. "first-name pool 149 -> 7 after filter; insufficient for 168 advisors"); the FN-1 fixture explicitly tests pool-adequacy.

---

## Structured generation-time check (replaces `_embeds_real` substring scan)

Current implementation at `data/demo/scripts/transform/fake_identities.py:134-138`:

```python
def _embeds_real(self, cand: str) -> bool:
    return any(r in cand for r in self._real_names if r and r != cand)
```

O(|real_names|) per candidate, substring scan. This is the attempt-13 within-class ceiling.

Path B replacement (structured lookup, O(1)-per-class):

```python
def _is_structurally_disjoint(self, cand: str, cand_tokens: tuple[str, ...]) -> bool:
    """O(1)-per-class membership against the precomputed RealFragmentIndex.
    Returns False (reject) if cand violates any class; True (accept) if disjoint."""
    if cand in self._idx.full_names:
        return False
    if any(t in self._idx.name_tokens for t in cand_tokens):
        return False
    # couple-components: prefix-substring lookup via surname+prefix-length sorted-tuple structure
    if self._idx.has_couple_component_collision(cand):
        return False
    if self._idx.has_surname_cohort_collision(cand_tokens):
        return False
    return True
```

The check is O(1) per class with the precomputed structures (set membership + dict lookup), NOT O(|real_names|) substring scan. Crucially, the pool was already filtered upfront, so this check should rarely fire — it catches the residual classes the pool-filter cannot fully cover (e.g. token combinations producing a real couple-component when concatenated).

---

## AC5 defense-in-depth call: KEEP `_embeds_real` as zero-fire safety net

**Choice:** KEEP `_embeds_real` substring scan as a tail-end safety net AFTER the structured-disjointness check.

**Rationale:**

1. **CVO META 3 ("prevent by construction beats check after the fact") is satisfied by the structured check being PRIMARY.** The substring scan is no longer the mechanism; it is the safety net.

2. **CVO FN-3 (common-name collision false-negative bound) explicitly motivates retention.** The retained substring scan covers any unknown fragment class not yet in the structured index — the same iteratively-grown discipline as FN-1.

3. **Zero-fire expectation = correctness verification.** If the structured-disjointness check is correct, `_embeds_real` should NEVER fire (zero substring rejections). A non-zero count from `_embeds_real` would signal a structural-index gap that needs an additional fragment class added — the natural feedback loop for iterative fragment-class discovery.

4. **Deletion would tighten coupling between fragment-index correctness and end-to-end leak protection.** Retention preserves option-value at trivial runtime cost (the substring scan is now only invoked on candidates the structured check already passed; expected rejection rate near zero).

5. **Aligns with COO §3 of ACK `20260524T22xxxxZ` recommendation:** "more conservative + iteratively-grown-fixture-friendly call ... documenting the retention rationale in session log is exactly the right discipline."

**Future deletion path:** if `_embeds_real` is observed to fire zero times across N successive transform runs covering varied real-name corpora, the substring scan can be deleted with a "proven-redundant by construction" rationale + the disjointness-completeness proof folded into the FN-1 fixture.

**ALSO deleted:** the 4096-probe loops in `client_name` and `zid` become 256-probe loops or smaller — under structured generation, collision rate drops dramatically (the pool-filter removes most collision sources). Phase-2 implementation will calibrate probe counts empirically.

---

## FN-1 regression-test fixture design (Phase-3 deliverable; sketch here)

**Path:** `data/demo/scripts/transform/test_path_b_disjointness.py`

**Structure:** standalone-callable pytest module + invocation point at `demo_transform.py` `main()` pre-`--apply` (the gate fires before any S3 write).

**Test cases (initial set, iteratively-grown per CVO FN-1):**

| Case ID | Real fragment | Leak class | Path B assertion |
|---|---|---|---|
| FN1-09a | `Austin Thompson` (real advisor) | Token-level (attempt-9) | `RealFragmentIndex.name_tokens` contains `"Austin"` AND `"Thompson"`; pool-filter removes both from `_FIRST_NAMES_FILTERED`/`_LAST_NAMES_FILTERED`; no fake can be generated containing either as a token |
| FN1-10a | `Sullivan, Dan` (real couple-component) | Prefix-substring (attempt-10) | `RealFragmentIndex.couple_components` includes `"Sullivan, Dan"`; structured check rejects fake `"Sullivan, Danielle"` |
| FN1-10b | `sam_owens` slug (real advisor slug) | Couple-component prefix | Structured check rejects any fake whose slug contains `"sam_owens"` as a token-level prefix |
| FN1-11a | `Powell, Craig & Powell, Valerie` (real couple) | Shared-surname cohort | `RealFragmentIndex.surname_cohorts["Powell"]` contains `{"Craig","Valerie"}`; structured check rejects any fake couple `"Powell, Craig & Powell, Valerie"` regardless of independent generation |
| FN1-11b | `Winslow, Fiona & Clarke, Julia` | Component embedding (real solo "Clarke, Julia") | Structured check rejects fake couple if either component matches a real solo client name |
| FN1-12 | Iteratively-grown set per `c61d4da6e` attempt-12 HARD ERROR diagnostic | Whatever attempt-12 surfaced | Structural rejection without runtime substring scan |
| FN1-13 | Iteratively-grown set per `dbf170b32` attempt-13 `_embeds_real` catches | Whatever attempt-13 caught | Structural rejection via the new index; `_embeds_real` should not need to fire |
| FN1-pool-adequacy | (synthetic) | Pool exhaustion | After filtering against a worst-case real corpus, filtered pool sizes >= entity counts (149 first >= 168 advisors fails... but `_LAST_NAMES_FILTERED` x `_FIRST_NAMES_FILTERED` x probe-salt space remains adequate) |

**Acceptance:** all cases pass against the Path B primitive. Each case asserts `factory.generate(real_X)` produces fake `Y` where the structured check `_is_structurally_disjoint(Y, ...)` returns True AND the original real fragment is not structurally present in Y. The fixture is iteratively-grown — any future leak surfaces adds a new case + an additional fragment class if needed.

**Invocation point:** pre-`--apply` gate in `demo_transform.py main()` (fail-loud if fixture fails); also standalone via `python -m pytest data/demo/scripts/transform/test_path_b_disjointness.py`.

---

## Compiler tools mandate -- Phase 1 satisfaction (per TO §`<compiler_tools_mandate>` Phase 1)

| Phase | Mandate | Action | Output |
|---|---|---|---|
| 1 (before write/design) | Read CVO LD-0029 verdict + LD-0030 ledger + iteration history commits | Read `org/tier1_exec/3.0.0_SA_CVO/logs/2026-05-24/spot_check_0353Z_LD0029_path_b_verdict.md` in full; read `org/tier0/ledger/LD-0030.md` + `LD-0021.md`; read commits `9e02fc35d` (couple-component), `defcab3cb` (shared-surname), `dbf170b32` (`_embeds_real`), `c61d4da6e` (attempt-12 HARD ERROR), `95e2b366e` (CVO AC5 verdict) | All five sources cited above; Path B primitive design grounded in CVO reasoning + iteration history's known-leaker set + 2D-coverage pattern. |

**Compiler-tools-log row** appended by `.tools/safe-commit.sh` post-commit (auto-appended via `.comp-graph/.agent_context` SERIAL=0.4.0_DS_ClientPlatform~D TO_ID=ADVI_DEMOV1.006). No `.py` edits in this commit; no `comp-validate` or `comp-pipescript` run (no script to validate yet). Phase-2 implementation commit will run `ds-commit-gate.sh` per CLAUDE.md Rule 14.

---

## Files Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-24/session_dsd_advi_demov1_006_phase1_path_b_design.md` | NEW — this design doc (Phase-1 deliverable; commit gates Phase-2 implementation). |

---

## Decisions Made

1. **Path B framed as CONSTRUCTION-TIME corpus-bind extension of CVO's 2D-coverage pattern.** The architectural direction (corpus-bind, prevent-by-construction) matches CVO's framing exactly; Path B shifts the timing from verification (AC5 method) to construction (filtered pool + structured generation check). This framing closes the conceptual adjacency COO surfaced in ACK §2 and may close CVO's banking decision (both AC5 method and Path B become instances of the same load-bearing 2D-coverage / corpus-bind doctrine).

2. **4 fragment classes (`full_names` / `name_tokens` / `couple_components` / `surname_cohorts`) cover attempts 8-13 leak history empirically.** Iteratively-grown per CVO FN-1; future leak surfaces adds a class if not already covered.

3. **Candidate-pool filtering at factory init (not at generation-time).** The pool itself is structurally disjoint upfront; the generation-time structured check is the secondary guarantee. This is the EARLIEST possible enforcement point — CVO META 3 "preventing by construction" satisfied.

4. **`_embeds_real` substring scan RETAINED as defense-in-depth safety net (AC5 design call).** Rationale: CVO FN-3 false-negative bound + iteratively-grown fragment-class discipline + zero-fire expectation = correctness verification feedback loop. COO §3 of ACK explicitly endorsed this call as conservative + iteratively-grown-fixture-friendly. Future deletion possible if proven-redundant across N runs.

5. **4096-probe loops reduced to 256 in Phase-2 implementation.** Pool-filter dramatically reduces collision rate; oversized probe counts become deadweight. Empirical calibration in Phase-2.

6. **FN-1 fixture initial set covers attempts 9-13 + pool-adequacy synthetic case.** 8 initial cases, iteratively-grown per CVO FN-1 doctrine.

7. **Phase-2 implementation commit will NOT touch `pii_leak_scan.py`.** That scanner remains the closure gate (per CTO ruling R5); Path B's structural guarantee makes it verify-not-detect, but no scanner-code changes needed.

---

## Blockers

None. ~D enumerated in `.owned-paths.yaml` POD4 / POD4_OR_AE / POD4_OR_EXEC / ANY_POD / ANY_POD_OR_EXEC per COO ACK §1; structurally clean to commit `data/demo/scripts/transform/**` + session logs in Phase 2 onward.

---

## Next Steps

| Recipient | Item |
|---|---|
| 2.0.0_SA_COO | MCP surfacing this design-doc commit hash + path (per `feedback_surface_phase_artifacts_during_execution`); commit IS the Phase-1 artifact |
| Self (next turn) | Phase 2 -- implement `RealFragmentIndex` + pool-filter + structured generation check in `data/demo/scripts/transform/fake_identities.py`; run `.tools/ds-commit-gate.sh`; commit via `.tools/safe-commit.sh` |
| Self (Phase 3) | FN-1 fixture at `data/demo/scripts/transform/test_path_b_disjointness.py`; integrate as pre-`--apply` gate in `demo_transform.py main()` |
| Self (Phase 4) | `.tools/safe-deploy.sh` cycle (push -> S3 upload to `s3://opal-313476888478-lambda-artifacts/demov1/` -> comp-pipescript deployed MATCH -> SSM dispatch demo-transform-runner against `i-03343a6072834f77d`) |
| Self (Phase 5) | R5 PII scan verify-not-detect (`leak_count=0` by construction); RAVC2-Request to COO + CC CVO + CC AE~C citing all 7 ACs + FN-1 fixture path + R5 scan exit code + this design-doc commit hash |
| 3.0.0_SA_CVO | (No direct ask; the design-doc's framing of Path B as construction-time corpus-bind extension of FN-2 2D-coverage pattern may close the LD-0030 banking-decision loop they flagged in `95e2b366e` §7) |
| 0.7.0_AE_CloudOps~C | (No direct ask; existing `demo-transform-runner` IAM + ephemeral t3.large from TO-5 suffices unless Phase-2 surfaces a different infra class) |

ETA for Phase-2 implementation commit: ~2h from this commit timestamp. Will MCP commit hash + comp-validate results to COO as each lands.

-- 0.4.0_DS_ClientPlatform~D (DS~D), Phase 1 of 5, tier0_commit_hash: 1a515b769
