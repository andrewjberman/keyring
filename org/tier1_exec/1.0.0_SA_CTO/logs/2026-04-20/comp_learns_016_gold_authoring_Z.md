# 1.0.0_SA_CTO~Z — COMP_LEARNS.016 httpx Gold Authoring

**Date:** 2026-04-20 (Mon)
**Lane:** ~Z
**Scope:** COMP_LEARNS.016 httpx gold authoring (imports_gold + ab_questions + ab_answer_key + target_version + GOLD_SURVEY) + PRD v4 + v4.1 + TO .016 v4 + v4.1 amendments + inline bench stubs (validator + cache)
**Parallel COO:** 2.0.0_SA_COO~Z

---

## 1. Session boot

- Registered `1.0.0_SA_CTO~Z` (PID 29004).
- Inbox-watch launched via Bash `run_in_background:true`.
- Ground-truth reconciliation scoped to COMP_LEARNS per Andrew's ~Z-only directive.
- COMP_LEARNS state at start: Phase 2 — wave `.011-.021` staged on base `0.4.0_DS` lane; COO~B v3 sweep unfinished on 4/11; operator + validator never run.

## 2. COO~Z boot + dispatch bundle

COO~Z registered, did full A→D dispatch prep in one pass:

- **A. v3 sweep**: .015 `9270837f` (RC/Exp split + cached-answer regime + temp-0 JudgeBackend). .016/.017/.021 `ecac2684` (gold pool split + E2E RC paths + mutation byte-identical determinism). Both sweeps executed against my 2026-04-16 13:59Z checklist preserved in ~B handoff log.
- **B. Resolve forks**: `5091974e` — operator.py schema normalization (active, deferred both accepted); `.005` flipped to `deferred` with PRD §2 row 6 citation. `ffa43e25` — evidence blocks backfilled on .001/.003/.004/.006 to clear `COMPLETED_WORK_WITHOUT_EVIDENCE` fork.
- **C. Project JSON**: `8d10456f` — coo_lane ~B → ~Z + phase refreshed.
- **D. Operator + validator smoke**: 0 forks, dep-graph confirms `.011` is zero-in-edge root; I signed off the graph at 17:55Z.

Then Andrew flagged out-of-lane dispatch (COO~Z fired GO to `0.4.0_DS_ClientPlatform~A` on .011 + scoped question to AE 0.7 on LibCST). I owned the co-miss (my "Fire the GO" directive was the violation root). COO~Z retracted both MCPs, reverted .011 to `staged`, shipped hand-off doc `org/projects/COMP_LEARNS_DISPATCH_BUNDLE.md` (`931ee1e4`) for base-lane resumption. In-lane discipline for remainder of session: author, sweep, plan, doc-update only; no cross-lane dispatch.

## 3. PRD v4 + v4.1 — R1/R3 layer separation on gold dimension coverage

### Phase 1 compiler mandate finding

`.016` Phase 1 step 3 surfaced dimension coverage gap on httpx:
- Initial grep (unescaped `from .*\*` pattern): reported 4/6 natural coverage (absent: `resolution=dynamic`, `binding=unresolved`).
- **Self-correction after star-import re-grep:** correct pattern `^\s*from\s+[^\s]+\s+import\s+\*` returned 16 star imports. Actual coverage: 5/6 (absent: `resolution=dynamic` only).

### Amendment rationale

The v3 TO required all 6 dimension values in gold OR pivot-target / synthetic-extend. My read of the R-defenses:
- **R3 (subtype explosion)** — defended by `.011` attribute validator + per-subtype synthetic fixture tests (`.013`'s `test_synthetic_3_file` covers all 6 values mechanically). Target-independent.
- **R1 (benchmark dishonesty)** — defended by authentic real-world gold reflecting what the target actually exhibits. Forcing 6/6 on a pinned target invites synthetic pollution and dilutes the real-world property.

The two defenses live at different layers. Gold does R1, not R3.

### Commits

| Commit | Summary |
|---|---|
| `28999f01` | PRD v4 — §4.5 + §6.3 amended; R1/R3 separation explicit; GOLD_SURVEY.md attestation format documented with worked example. |
| `087ac4ba` | TO `.016` AC #3/#4 + Phase 1 step 3 `<if_mismatch>` softened from "STOP, pivot" to "document in GOLD_SURVEY.md". Path correction `_repo/httpx/` (was `/httpx/httpx/`). Status flipped `staged` → `pending`. |
| `885c8dc3` | PRD v4.1 fact correction — 4/6 → 5/6 after star-import re-grep. `binding=unresolved` example removed from §6.3 example block. COO~Z polish item 1 absorbed ("lives in `.013`" → "lives in the relevant per-subtype synthetic fixture, e.g. for `imports`, `.013`'s test_synthetic_3_file"). |
| `3ba83810` | TO `.016` v4.1 AC correction — AC #3 adds `binding=unresolved` as observed value (16 star imports); AC #4 narrows absent-values to just `resolution=dynamic`. |

COO~Z ACCEPTANCE FLEX +1 on record (MCP 20260420T181300Z and 20260420T182500Z).

## 4. Gold authoring (5 files + inline bench stubs)

### Files shipped

| Path | Purpose | Size |
|---|---|---|
| `comp/targets/httpx/gold/imports_gold.jsonl` | 85 internal httpx→httpx import edges with dimensional tags | 85 records |
| `comp/targets/httpx/gold/ab_questions.yaml` | 24 questions (19 ratchet — 4 adversarial; 5 exploratory) | 24 entries |
| `comp/targets/httpx/gold/ab_answer_key.yaml` | typed answer key — 19 deterministic, 5 open_ended rubrics | 24 entries |
| `comp/targets/httpx/gold/target_version.txt` | SHA-256 cache-invalidation seal over gold + source | `909ea79f63e9c016e457693b01eb1d1bdc8a7f60fb6fdb9430235e0810e39f0b` |
| `comp/targets/httpx/gold/GOLD_SURVEY.md` | authoring-process doc + gold-before-code attestation + "Dimension Values Not Observed" section (per PRD v4.1 §6.3) | — |
| `comp/bench/__init__.py` + `ab_answer_key_validator.py` + `cache.py` | inline bench stubs (removed on `.015` landing per TO `<cross_domain_coordination>`) | — |

### Gold statistics

- 85 edges, 21/23 source files emit ≥1 edge (`__version__.py` + `_status_codes.py` zero-out).
- `resolution`: 85 static. `guard`: 79 unconditional + 6 conditional. `binding`: 69 resolved + 16 unresolved.
- Top fan-in: `httpx._types` (11 incoming unconditional — adversarial q18 target).
- Top fan-out: `httpx._client` (12 unconditional).

### Absent value attestation (PRD v4.1 §6.3)

`resolution=dynamic` documented in `GOLD_SURVEY.md` "Dimension Values Not Observed" with reproducible grep:
```
$ grep -rnE "importlib|__import__" comp/targets/httpx/_repo/httpx/
(0 matches)
```
R3 defense for this value lives in `.013 test_synthetic_3_file` (per PRD §4.5).

### AC verification (Phase 2 + Phase 3)

| AC | Expected | Observed | Status |
|---|---|---|---|
| #1 | public API importable from package root | N/A (.011 not shipped; imports resolve via inline bench stubs) | DEFERRED to post-.011 (per TO `<cross_domain_coordination>`) |
| #2 | record count matches GOLD_SURVEY | 85 = 85 | PASS |
| #3 | observed dimension values ≥2 each | static=85 / unconditional=79 / conditional=6 / resolved=69 / unresolved=16 | PASS |
| #4 | target-absent values documented | `resolution=dynamic` attestation present | PASS |
| #5 | 15-30 questions (ratchet 12-22 incl. adv 3-5; exploratory 3-8) | 24 total (19 ratchet incl. 4 adv; 5 exploratory) | PASS |
| #6 | answer_type on every entry; ratchet entries typed correctly | 24/24 typed; 19 ratchet all `enumerable`/`set_membership`/`numeric` | PASS |
| #7 | validator passes on ratchet-pool discipline | `VALIDATOR_PASS` | PASS |
| #8 | stored target_version matches recomputed | hash equal | PASS |
| #9 | GOLD_SURVEY documents authoring process | file written with 6 sections | PASS |
| #10 | gold-before-code attestation sentence | `grep -l "Gold was authored without running"` hits GOLD_SURVEY.md | PASS |
| #11 | session log with Compiler Tools | this file §6 | PASS |
| #12 | MCP COMPLETE to COO~Z | pending next tool call | PENDING |

## 5. Scope decisions (gold-authoring)

- **Module granularity, not symbol granularity** — one edge per `(source_module, target_module)` pair regardless of imported-symbol count.
- **External imports out of scope** — first-pass gold is internal httpx→httpx only. Follow-up gold extension for `imports_external_gold.jsonl` can land as a later TO once the internal ratchet is stable.
- **TYPE_CHECKING counts as an edge** — tagged `guard=conditional`, not omitted.
- **Star imports = `binding=unresolved`** — per PRD §4.5 normative example.
- **Self-imports excluded** — `import httpx` inside `_transports/default.py` TYPE_CHECKING block is a self-reference with no structural signal.

## 6. Compiler Tools

| Date | Agent | TO | Tool | Command | Result | Note |
|---|---|---|---|---|---|---|
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 1 step 1 | `ls comp/targets/httpx/_repo/httpx/` | PASS | 17 .py files + 1 subpackage |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 1 step 2 | `find comp/targets/httpx/_repo/httpx -name "*.py" \| wc -l` | PASS | 23 .py files (matches SURFACE_INVENTORY.md) |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 1 step 3 (v3) | `grep -rn "TYPE_CHECKING\|importlib" comp/targets/httpx/_repo/httpx/` | TARGET-ABSENT | 12 TYPE_CHECKING hits; 0 importlib/__import__. `resolution=dynamic` flagged absent → ACCEPTANCE FLEX MCP to COO~Z for PRD v4 amendment. |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 1 step 3 (re-run) | `grep -rnE '^\s*from\s+[^\s]+\s+import\s+\*' comp/targets/httpx/_repo/httpx/` | CORRECTION | 16 star imports (11 in __init__.py; 5 in _transports/__init__.py). `binding=unresolved` observed — corrected earlier wrong claim. PRD v4 → v4.1. |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 1 | `jq -r '.attributes \| keys[]' comp/targets/httpx/gold/imports_gold.jsonl \| sort -u` | PASS | `binding`, `guard`, `resolution` — all 3 dimensions on every record |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 2 | `for d in resolution guard binding; do ... \| sort \| uniq -c; done` | PASS | 5/6 observed values ≥2 each; 1 absent value (resolution=dynamic) documented per v4.1 §6.3 |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 3 | python yaml-loader count (Q_total/ratchet/exploratory/A/match) | PASS | Q_total:24 ratchet:19 exploratory:5 adversarial:4 A:24 match:True |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 4 | `from comp.bench.ab_answer_key_validator import validate; validate(...)` | PASS | `VALIDATOR_PASS` — no `RatchetPoolOpenEndedRejected` raise |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 5 | `compute_target_version` vs stored | PASS | both = `909ea79f63e9c016e457693b01eb1d1bdc8a7f60fb6fdb9430235e0810e39f0b` |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 2 step 6 | `grep -l "Gold was authored without running" GOLD_SURVEY.md` | PASS | attestation sentence present |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 3 step 1 | `comp.bench.structural.load_gold` | SKIPPED | `.015`'s `bench.structural` not yet shipped; inline stub in `comp/bench/` provides validator+cache only. |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | Phase 3 step 2 | `comp.bench.ab_answer_key_validator + load_ab_questions` | PARTIAL | validator validates via inline stub; `load_ab_questions` available in stub; ratchet-pool question IDs enumerate to {q01..q19}. |

## 7. Meta-process observations (ADHC_ROUTER Phase 2 candidates)

- **Unescaped-glob grep silently returns 0.** My first Phase 1 star-import grep was `from .*\*` (shell-mangled). Self-caught during gold authoring when `__init__.py` star-import lines jumped out on file enumeration. Would have been caught sooner by mechanized grep-command-in-TO format instead of author-written-prose. Candidate: TO Phase 1 `<run>` blocks should be shell-quoted exactly to avoid transcription drift.
- **PRD-text worked examples as separate artifact.** The v4 §6.3 example block initially included `binding=unresolved` as an absent-value example that was factually wrong by the time v4.1 correction shipped. A pattern where worked examples live as concrete target-pointers (e.g., link into `comp/targets/httpx/gold/GOLD_SURVEY.md`) rather than PRD-inline text would prevent v4-style drift. Not urgent; park.
- **Inline bench stubs in-target.** Shipping `comp/bench/__init__.py` + `ab_answer_key_validator.py` + `cache.py` unblocked `.016` pre-`.015`. Clean swap path documented in each stub's docstring. Pattern candidate for future "ship-when-dep-pending" TOs with explicit removal marker.

## 8. Next steps

- MCP COMPLETE to COO~Z with commit hashes + AC table + target_version hash + pool-breakdown.
- Park remaining polish items from COO~Z v4 approval (PRD `should halt` → `MUST halt` normativity hardening + gold-survey-checker owner question) for a session-end polish commit if time.
- Base COO lane (non-~Z) inherits: PRD v4.1 + TO `.016` v4.1 + gold + inline stubs. `.016` complete; dispatch-bundle doc `931ee1e4` is the entry point for resuming the `.011`-`.021` wave.
