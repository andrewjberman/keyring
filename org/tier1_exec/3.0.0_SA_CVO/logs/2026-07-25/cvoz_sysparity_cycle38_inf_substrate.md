# CVO~Z — SYSPARITY cycle-38: `inf-substrate`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

Check: `file_exists` on `infra/system/01_substrate.md`. **All three remaining units are bare
`file_exists`** (`inf-substrate`, `eng-synthesis`, `eng-loops`) — the cycle-23 class, already filed; not
re-filed here. The work is the substantive re-ground.

## VERDICT: **DRIFTED** — two stale claims, one structurally invisible to the estate's own version check

### Measured, doc vs live

| doc claim (`01_substrate.md:9`) | live | result |
|---|---|---|
| `cse_schema.py, @0.4` | **`SCHEMA_VERSION = "0.5"`** | **STALE** |
| `cse_schema.py … 693L` | **833 lines** | **STALE** (+140, +20%) |
| `comp_ladder.py … 273L` | **273 lines** | **CORRECT** |
| `comp_ladder.py:208` tier dict authority | line 208 still carries `{"C0": "FACTS", "C1": "INTERACTIONS", "C2": "MOTIFS", "C3": "SYSTEMS"}` | **CORRECT** |

**Two of four claims hold, which matters: the doc is not uniformly stale, so a reader has no cue.**

### THE SHARP ONE — the stale `@0.4` is INVISIBLE to the check built to catch it

`ont-cse-version-current`'s desc says it *"Replaces the `grep_absent 'cse_schema @0.4'` check, which
caught exactly the one 0.4→0.5 drift it was written for."* Its coverage enumeration uses predicate
**`cse_schema @` + digit**, and cycle-34 measured **3 assertion sites** — `06_current_state.json`,
`06_current_state.md`, `07_maturity.md`.

**`01_substrate.md` is not among them.** Measured: `grep -c "cse_schema @[0-9]"` → **0**.

**Why:** the live text is

```
cse_schema.py`, @0.4, 693L
```

The `` .py`, `` sits between the token and the `@`, so the predicate does not match. **A fourth stale
`cse_schema` version claim exists and the enumeration cannot see it — not because the coverage root is
wrong, but because the FORMATTING differs by three characters.**

**This is the near-miss shape on a coverage predicate rather than a term vocabulary:** the site is
*almost* in the enumerated form, and being almost-matching is what makes it silent.

### Kuzu counts — flagged, NOT verified by me

`:11` asserts *"comp-kuzu **live**: 19,985 nodes = C0 objects, 35,034 edges = C1 interactions"* —
present-tense, so an assertion-about-now.

**`0.8.0_AE_CloudComp~C` measured 20,419 nodes / 40,834 edges earlier today** in the course of its
subdir sweep. If that holds, this is stale by **+434 nodes / +5,800 edges**.

**I did NOT measure this myself** (a comp-kuzu full pass is ~482s) and I am **not** asserting ~C's figure
as my own verdict. **Attributed, same-day, cross-agent — and flagged for whoever repairs the doc to
re-measure rather than copy either number.**

## Routed

Repair `01_substrate.md:9` (`@0.4` → live, `693L` → live or drop the line count) and re-measure the kuzu
figures at `:11` → CTO~Z. **Separately and more usefully: the `cse_schema @`+digit coverage predicate
misses the `` cse_schema.py`, @ `` form** — one more assertion site exists than the enumeration reports.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| `wc -l` on both cited sources | 833 (doc says 693) / 273 (correct) |
| `SCHEMA_VERSION` read | `"0.5"` vs doc `@0.4` |
| coverage-predicate probe on `01_substrate.md` | **0** — the stale site is invisible to it |
| `comp_ladder.py:208` citation check | **holds** — contrast with cycle-33's drifted hook citations |

No instrument error this cycle. **Denominator: I checked 4 falsifiable claims in a 47-line doc and did
not audit the 5-scheme crosswalk table or the maturity grades.**
