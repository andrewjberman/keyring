# ont-cse-version-current grep_absent -> version_pin migration (python_constant mode) — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z arch-gated dispatch 20260725T093651Z (from CVO~Z LD-0318 finding; off-main-fabric
group, no XML TO)
**Status:** COMPLETE
**Cycle wall:** ~09:37Z dispatch → ~09:52Z committed

---

## Objective

Migrate the `ont-cse-version-current` parity unit off its CHECK-DEFECTIVE `grep_absent` (frozen literal
"cse_schema @0.4" — blind past the one drift it was written for) onto `version_pin`, which requires a
second addressing mode: the version source is a PYTHON MODULE CONSTANT (`cse_schema.py SCHEMA_VERSION`),
not a YAML path. Design as a declared mode, AST-read, never import, fail-closed on unevaluable.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `system_parity.py` | `--worktree` (baseline, pre-edit) | PASS rc=0 | baseline captured FIRST: ontology 80% (4/5), ont-cse PASS via grep_absent, ont-rulebank FAIL-by-design, engineering 100% |
| `commit-gate` | on edited `system_parity.py` | PASS | py_compile + AST + ruff py39 clean |
| battery harness | direct `_version_pin` calls, `_VINTAGE="worktree"`, 7 cases | 7/7 | mutant FAIL + live-positive PASS + 4 fail-closed ASSUMPTIONs + fixture-positive + yaml_path regression (byte-identical FAIL detail) |
| `system_parity.py` | `--worktree` (post-edit full) | PASS rc=0 | ontology 80% (4/5) unchanged shape; migrated unit PASS with DERIVED head |
| `system_parity.py` | `--domain engineering` (HEAD vintage, old contract) | PASS rc=0 | variable-isolation control: eng-currentstate FAIL reproduces on the OLD contract — exogenous (HEAD advance + comp-system TTL), not my change |
| `comp_system.py` | `--check` (direct) | rc=0* | reports BLOCKED-ON-PEER-LANDING on uncommitted `types-index/ClientDirectoryEntry.fields.yaml` — correctly refusing to launder unlanded peer work; surfaced, not chased |

**What worked:** capturing the full baseline BEFORE any edit made the engineering 100%→80% flip
immediately visible as an anomaly, and the which-side-is-the-variable control (HEAD-vintage run of the
old contract) attributed it to comp-system's HEAD-advance/TTL staleness in one command — the exact
discipline CVO~Z's correction this morning named (~D's same-file-loaded-twice model).

**What failed:** nothing this cycle.

**Gap found:** the dispatch said "both existing version_pin units"; the contract carries exactly ONE
(`ont-rulebank-version-current`). Denominator stated in the memo rather than silently complied with.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. Read `_version_pin` + the contract unit + `cse_schema.py:42` + owned-paths (infra/system/** =
   ANY_EXEC_OR_AE → my lane commits directly; the dispatch's exec-locked on-disk-only branch does not bind).
2. Extended `_version_pin` with declared `source_kind: yaml_path | python_constant` in the file's own
   idiom (docstring reasons, ASSUMPTION-on-unevaluable everywhere, last-wins module semantics evaluating
   only the last matching assignment, AnnAssign supported, no import, no regex).
3. Replaced the unit's check in `scope_contract.json` in the same change (grep_absent REMOVED — no
   duplicate record).
4. Ran the 7-case acceptance battery + full regression + the exogenous-flip isolation.
5. Authored `VERSION_PIN_PYCONST_MIGRATION_C.md` + 4 fixtures to the census dir (on disk, CTO~Z tree);
   committed the two infra/system files + this log under my lane.

## Decisions Made

| Decision | Rationale |
|---|---|
| Declared `source_kind`, defaulting to `yaml_path` | never inferred from content; default preserves the existing unit's behavior byte-identically |
| Evaluate only the LAST matching assignment | python module semantics — the check cannot diverge from what an importer would observe; earlier shadowed assignments irrelevant |
| Commit myself rather than on-disk-only | infra/system/** is ANY_EXEC_OR_AE (owned-paths:1385) — the dispatch's exec-lock condition was checked and does not apply |
| eng-currentstate flip accepted as exogenous only after a HEAD-vintage control | a regression claim without isolating the variable is the class CVO~Z's correction named this morning |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/system/system_parity.py` | `source_kind` addressing mode in `_version_pin` (+ `import ast`) | This session, this lane |
| `infra/system/scope_contract.json` | ont-cse-version-current check replaced grep_absent→version_pin | This session, this lane |
| `.../NFRA_TOOLUNIFY_CENSUS/VERSION_PIN_PYCONST_MIGRATION_C.md` + `fixtures_version_pin_pyconst/` (5 files) | New — memo + re-run fixtures | No — CTO~Z tree, on disk |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None. (comp-system BLOCKED-ON-PEER-LANDING is surfaced for its owner, not a blocker for this change.)

## Current State

Migration delivered + committed. The unit now derives its expectation from the source at run time — the
next SCHEMA_VERSION bump makes it FAIL until 06 catches up, which is the entire point. CVO~Z attack
surface (fail-closed preservation) explicitly mapped in the memo §3. Reported to CTO~Z + CVO~Z this turn.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Attack the fail-closed property per the dispatch (memo §3 lists the surfaces +
   fixtures).
2. **[1.0.0_SA_CTO~Z]** Independent re-run if desired (the commit is revertible); memo + fixtures await
   your tree's commit.
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.

---

## ADDENDUM (same session, ~09:49–09:55Z): CVO~Z verify + float-lossiness hardening (CTO~Z follow-on)

CVO~Z VERIFIED @9efe8da91 (8 cases, real AST path via a `_read` monkeypatch — its scratch fixtures were
invisible to the default HEAD vintage, a method note worth keeping): fail-closed preserved everywhere;
all 3 of my named edges accurate including the 2 unexercised (TYPE_CHECKING → ASSUMPTION; shadowing →
last-wins matches importer semantics, now on the record as a case). **One edge neither of us named:
float versions render LOSSY** (`1.10` → `"1.1"` — a correct `@1.10` doc would FAIL; an `@1.1` doc would
PASS against intended `1.10`). Never fail-open, not live (source is a string).

CTO~Z FOLLOW-ON (20260725T094941Z) dispatched the hardening CVO~Z had offered as my call — I was mid-way
through the identical build off the verify note when it arrived; designs matched (require STRING literal,
ASSUMPTION on non-string; require-over-normalize since normalization guesses intent, ASSUMPTION
discloses). Detail names type + value per the follow-on's example.

**Hardening battery 6/6** (worktree vintage, same harness): (1) float `1.10` fixture → ASSUMPTION naming
`float 1.1`, not PASS/FAIL; (2) live string positive → PASS unchanged; (3) tuple `(0, 5)` → **ASSUMPTION
(my stated call, was FAIL-with-visible-rendering pre-hardening)**: a misconfigured pin's FAIL detail
("/system is behind the source") would misattribute a check defect as a representation gap — ASSUMPTION
with the type+value named is the honest verdict; (4) the 0.6-vs-@0.5 next-bump mutant still FAILs;
plus regressions: computed-non-literal ASSUMPTION unchanged, yaml_path default byte-identical.
commit-gate clean. New fixtures `cse_schema_fixture_float_110.py` + `cse_schema_fixture_tuple.py` added
to the census fixtures dir. Committed this session (see below); CVO~Z verifies per the same loop.
