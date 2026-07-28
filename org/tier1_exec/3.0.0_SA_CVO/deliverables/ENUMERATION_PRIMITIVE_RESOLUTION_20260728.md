# ENUMERATION-PRIMITIVE RESOLUTION — 93 of 93, and the two primitives my own classifier was blind to

    author:  3.0.0_SA_CVO
    task:    Andrew-direct 2026-07-28 — *"resolve the 57 unresolved enumeration primitives"*
    result:  **57 UNRESOLVED -> 0.** 93 of 93 comp-* tools classified.
    method:  automated resolver (85) + direct inspection of the residual 8

---

## §1 Result

| | count |
|---|---|
| comp-* executables (DENOMINATOR, live count) | **93** |
| resolved by the automated resolver | **85 (91%)** |
| resolved by inspection | **8** |
| **UNRESOLVED** | **0** |

**Primitive distribution** (a tool may carry more than one):

    REGISTRY   66      GIT        29      FS-WALK    19      SQL/TRINO  10
    GRAPH-DB   34      AWS-API    24      AST        12      SUBPROC     3
    + SIMULATE  5      + FS-GLOB   1      (both discovered during the residual pass -- §3)

## §2 What fixed the 57 — three wrapper shapes, not one

My earlier pass resolved only 35/92 because it followed a single delegation shape. The resolver now
follows three:
1. **Python** `_ENGINE = os.path.join(...)` + `runpy.run_path`
2. **Bash** `python "$WORKSPACE/org/modules/.../engine.py" "$@"` — the majority shape, and the one
   that caused the original 57
3. **Sibling** `exec python "$(dirname $0)/comp_x.py"` — delegation to another file **inside `.tools/`**,
   which shape (2)'s `org/modules/` path regex could never match (`comp-missions`, `comp-tagauthz`)

Plus one hop of transitive resolution (engine → engine). **69 of 93 tools delegate to a resolvable
engine**; the rest are self-contained.

## §3 THE RESIDUAL 8 — and the finding is not the count

| tool | primitive | note |
|---|---|---|
| `comp-denytest.py` | **SIMULATE** | `iam simulate-principal-policy` |
| `comp-firmsep-sweep.py` | **SIMULATE** | the PROVE-THE-UNIVERSE tool |
| `comp-glob` | **FS-GLOB** | `fnmatch` ×6 — distinct from `os.walk` |
| `comp-missions` | **REGISTRY** | via sibling `comp_missions.py` — reads `MISSIONS.md`, yaml, json |
| `comp-tagauthz` | **TF-PARSE + REGISTRY** | via sibling — `terraform` ×7, `json.load` ×5 |
| `comp-imgread` | **BINARY-READ** | PIL. **Not an estate enumerator at all** |
| `comp-to` | **NONE — correctly** | a WRITER (sets session TO context). Enumerates nothing |
| `comp-v5-composite-test.sh` | **TEST-HARNESS** | not an estate tool |

**So the true denominator for estate-scanning tools is 90, not 93** — `comp-to`, `comp-imgread` and
the test harness are legitimately non-enumerating. **"No primitive" and "not an enumerator" are
different verdicts and must not be collapsed**; only the first is a gap.

## §4 THE ACTUAL FINDING — my classifier had no `SIMULATE` primitive, and that is Pattern B

**`SIMULATE` — enumerate by exercising every candidate against the live plane — is PATTERN B in the
library I wrote four hours earlier** (`@a3dac97be` §3-B), where I called it *"the closest thing to
proving a set is complete."* **My classifier did not contain it.**

**Five tools use it:** `comp-denytest`, `comp-firmsep-sweep`, `comp-which`, `comp-whoread`,
`comp-deadgrant`.

>> **AND THE DANGEROUS HALF IS NOT THE THREE THAT CAME BACK UNRESOLVED. It is `comp-which` and
>> `comp-whoread` and `comp-deadgrant`, which RESOLVED on other primitives — so they read as
>> fully classified while their strongest enumeration mechanism was invisible to me.**
>> **An unresolved tool announces itself. An UNDER-classified one reads as complete.** That is the
>> type-2 error, inside the instrument built to find type-2 errors, for the third time today. <<

**The generalisable rule, and it is the reason this matters beyond my script:** a classifier's
primitive list IS its coverage universe. Mine was derived from the tools I had read (Pattern A —
derive from a static sample), and it therefore missed the primitive used by the tools I had not read.
**A coverage instrument needs its own coverage declared, or it silently under-reports exactly the
population it did not sample.**

## §5 What this hands the register

- **INFRA.TOOLS field 3 (`BUILT`, positive enumeration): the primitive census is now COMPLETE at
  93/93** — a fact MSTR can carry with an anchor rather than an `UNASSESSED`.
- **The §4 blind-spot table in `@a3dac97be` gains two rows** (`SIMULATE`, `FS-GLOB`) and one column
  distinction (`NONE — correctly` vs `unresolved`).
- The per-tool rows are persisted as JSON so the `excludes:` field can be populated **mechanically
  from the primitive**, per the recommendation — not by hand.

## §6 Limits

- **Classification is by SOURCE PATTERN, not by execution.** A tool whose primitive is reached only
  on a rare code path may be mis-binned. The verdicts are `DECLARED-from-source`, **not exercised** —
  except `comp-heat`, `comp-clobber` and `comp-coverage-check`, which I ran.
- **Multi-primitive tools are counted in every bucket they match**; the distribution sums above 93 by
  design.
- **The primitive list is now 10 entries and is still not provably exhaustive** — §4 is the proof
  that a missing entry is silent. An 11th primitive would fail exactly the same way.

— 3.0.0_SA_CVO
