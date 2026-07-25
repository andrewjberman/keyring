# CVO~Z — SYSPARITY cycle-34: `ont-cse-version-current`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: CLEAN — passes for a TRUE reason, and mutant-proven sensitive

Picked as the sibling of cycle-27's `ont-rulebank-version-current`, which **fails with a false
explanation**. Question: does the one that PASSES pass for a real reason?

### Values

| | |
|---|---|
| live `SCHEMA_VERSION` (`cse_schema.py:42`) | **`"0.5"`** — a **string** literal, so the float-lossy hazard (`1.10 → 1.1`) does not apply |
| assertion sites under `infra/system` (harness exclusions applied) | **3** — matches the harness's reported 3 exactly |
| values at those sites | `0.5`, `0.5`, `0.5` — **all current** |
| required file carries `cse_schema @0.5` | **yes** (`06_current_state.json`) |

Sites: `06_current_state.json`, `06_current_state.md`, `07_maturity.md`.

### Sensitivity — EXERCISED, positive control and mutant

```
POSITIVE CONTROL (source 0.5)   -> PASS
MUTANT (source bumped to 0.6)   -> FAIL
  "head is 0.6 but 'cse_schema @0.6' appears in NONE of 1 required representation file(s);
   3 of 3 enumerated assertion site(s) STALE"
```

**The check reddens when the source moves, and its failure message is ACCURATE AND QUANTIFIED** — it
names the required file *and* the enumerated sites. **Direct contrast with the sibling at cycle-27**,
whose failure message asserts *"/system is behind the source"* when 8 of 8 sites were current. Same check
family; one explains its failure correctly, one does not.

### Positive finding: the harness is vintage-pinned to HEAD by design

`system_parity.py:65` — `_VINTAGE = "head"`, and `_read` uses `git show HEAD:<path>` so **the read is
reproducible across agents** rather than depending on whose worktree is dirty. My first two mutants were
structurally unreadable *because of this*, which is the guard working, not a defect. Exercising the
predicate required explicitly switching to `worktree` vintage.

### Disclosed blind spot, already in the desc

Sensitivity is **BORROWED from source bump discipline**: an ADD without a version bump is not detected.
Stated by the unit itself; not a new finding.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| independent site enumeration | 3 sites, all `0.5` — matches harness |
| `_version_pin` positive control | PASS |
| `_version_pin` mutant (worktree vintage) | **FAIL**, message accurate and quantified |

**Three failed mutant attempts before one worked, all one root cause: I did not read `_read`'s vintage
semantics.** Attempt 1 used an absolute temp path; attempt 2 a workspace-relative path; both returned
`ASSUMPTION — version source unreadable`, because the harness reads **committed** content and my mutant
was never committed. **Every failure was fail-closed (`ASSUMPTION`, never `PASS`), so no wrong verdict was
ever produced** — and the fix was to read `system_parity.py:83-92` instead of guessing a fourth time.
Scratch file removed; `.comp-graph/` clean.
