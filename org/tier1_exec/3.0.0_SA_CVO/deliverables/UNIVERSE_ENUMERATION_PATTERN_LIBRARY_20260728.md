# UNIVERSE ENUMERATION — the pattern library, and the corrected state of COMPUNIFY

    author:    3.0.0_SA_CVO
    authority: Andrew-direct 2026-07-28 ~1552Z, VERBATIM: *"The ideal would be to identify patterns in
               designated-universe blind spots and how to effectively enumerate what IS covered first
               and foremost, even if the negative-control has yet to have a true oracle."*
    supersedes: my own §8 claims in TOOL_COVERAGE_UNIVERSE_REQUIREMENT_20260728.md (three corrections, §1)
    measured:  2026-07-28T155xZ

    HEADLINE: **the estate has ALREADY SOLVED this three separate times, in three different tools,
    and nobody has abstracted the solutions into a reusable pattern.** That abstraction is §3.

---

## §1 THREE CORRECTIONS TO MY OWN PRIOR CLAIMS — all in the same direction

I have now been wrong about COMPUNIFY's maturity three times in ninety minutes, **each time by reading
a document instead of exercising the thing**, and each time in the direction of understating what is
built. Recording all three because the pattern in my errors matters more than any one of them.

| # | I claimed | Truth, exercised | How I got it wrong |
|---|---|---|---|
| 1 | the exclusions field is "written nowhere" | `comp-coverage-map.yaml`, 1,081 lines, carries `excluded`/`denominator`/`universe`/`blind` | generalised from 2 tools I had read to a population of 92 |
| 2 | "36 tools populated" | **88 homed** — 36 `tools[]` + **52 `meta_tools[]`** | I parsed `tools:` and never looked for a second section |
| 3 | "the S2 gate is NOT BUILT" | **`comp-coverage-check` EXISTS, RUNS, and returns PASS** | I read the S0 header's forward-looking *"the gate itself -> S2"* as current state |

**Exercised result, 2026-07-28T155xZ:**
```
PASS: comp-coverage-map.yaml is internally consistent -- every tool one home, every overlap
      declared, no phantom seam, inventory complete, projection current, grain stable.
  swept: 88 homed tool(s) (36 tools[] + 52 meta_tools[]) | 12 gate_contract rule(s),
         0 unverifiable | inventory universe='working' (88 tool(s))
```

**#3 is the check-the-MARKER-not-the-COMMENT class that CLAUDE.md Rule 21 exists to name** — the same
error that file records against itself. **A PRD's "phase N will do X" is a statement about intent at
authoring time; it is not a status field, and it ages into a lie about a thing that already shipped.**

**And a fourth, against my own instrument:** my enumeration-primitive scan resolved **35 of 92 tools
(38%)** and I nearly reported *"57 tools have no primitive"* as a finding. The real cause was that my
wrapper-follower only handled the Python `_ENGINE=` shape and most comp-tools are **bash** wrappers
delegating to `org/modules/graph/cli.py`. **A coverage instrument with a 62% undeclared blind spot,
built to measure coverage blind spots.** It is now declared, which is the only reason its output is
usable at all.

## §2 WHAT IS ACTUALLY MISSING — narrowed three times, now precise

Not the contract (built), not the population (88 homed, inventory complete), not the gate (passing).
**What is missing is one field and one comparison:**

- **the NEGATIVE declaration** — per tool, *what it cannot see WITHIN its declared surface*. The map
  declares `surface`/`granularity`/`concern`/`store`; comp-heat correctly carries
  `store: "working tree (uncommitted scripts/.tf/src)"` and `refresh_mechanism: on-demand-read`. **None
  of that reveals that gitignored files, 5 submodules incl. the entire portal, and all S3-resident
  code are invisible to it.**
- **the QUESTION↔TOOL surface comparison at route time** (COMPRAIL), per my prior §6 — unchanged and
  still the right placement.

**Andrew's sequencing is correct and is already vindicated by the estate:** the positive enumeration
is done (88 homed, gate green) *without* any negative oracle existing. The positive half was
tractable; the negative half is the open problem — which is exactly why §3 matters.

## §3 THE PATTERN LIBRARY — four ways to enumerate a universe, ranked by what they can prove

**Each is a LIVE instance in this estate.** I did not invent these; I found them and named them.

### PATTERN A — DERIVE (from a static artifact)
Enumerate by parsing something authored: `git ls-files`, `os.walk`, AST parse, grep over `.tf`.
**Cost:** cheap, fast, offline. **Proves:** only what the artifact mentions.
**BLIND SPOT (characteristic, silent):** anything real but unmentioned — and the tool cannot know.
**Live failure, measured 2026-07-09 and recorded in the map itself:** *"a grant-shape lint over our own
TF cannot see an AWS-MANAGED `Resource:'*'` policy: a grep-derived universe of 4 roles was really 6,
and the belt shipped against the wrong scope."* **A 33% undercount, shipped, silently.**
**Use when:** the artifact is the governing source of truth (TOOLARCH §3 STABLE-BY-LAW), never for reach.

### PATTERN B — SIMULATE (exercise every candidate against the live plane)
**Live instance: `comp-firmsep-sweep`** — the map's own words: *"PROVE-THE-UNIVERSE... Simulates a firm
credential against EVERY role in the account and asserts only the firm's own roles are allowed...
**Enumerates by SIMULATION, never by grant shape.**"*
**Proves:** actual reach, including grants no artifact mentions. **Cost:** high (live calls, N×M).
**Residual blind spot:** only the candidates you enumerated to simulate — it converts an *unbounded*
blind spot into a *bounded, stated* one. **That conversion is the whole value.**
**Use when:** the question is REACH or CAPABILITY and a wrong universe is expensive (IAM, security, firm-sep).

### PATTERN C — CROSS-DERIVE (two independent derivations; the DIFF is the blind spot)
**Live instance: `comp-toolgraph`** — *"the load-bearing DECLARED-vs-ACTUAL coupling diff (THIS map's
overlap groups vs the real import graph) -> the undeclared-ripple finding, e.g. the grain_sentinel
cluster rippling to 6 tools declared nowhere."*
>> **THIS IS THE ANSWER TO ANDREW'S "even if the negative-control has yet to have a true oracle."**
>> You do not need ground truth. **Two independent derivations of the same set, differenced, yield a
>> negative signal without any oracle** — every disagreement is a defect in one of them, and you learn
>> which by inspection. It is the cheapest negative control that exists. <<
**Use when:** no ground truth is available — i.e. the normal case.
**My own use of it today, unplanned:** the co-change coupling `comp-which ↔ comp-coverage-map.yaml`
(16×) is a second derivation of "what belongs to the routing layer," and **differencing it against my
read of the tool sources is what exposed correction #1.**

### PATTERN D — ATTRIBUTION COMPLETENESS (every member carries a disposition)
**Live instance: `gate_contract` rule at `comp-coverage-map.yaml:149-153`** — *"every edge_type carries
a producer DISPOSITION... An edge_type with NEITHER = **a silent gap in the denominator universe**...
the registry IS the universe the enumerated denominator partitions EXHAUSTIVE+DISJOINT."*
**Proves:** no member of a KNOWN universe is silently unaccounted for. **Does NOT prove** the universe
is complete — it is an *internal* consistency guarantee.
**Use when:** the universe is bounded and registered; it is the cheapest continuous guard, and it is
the one already wired into a passing gate.

### The ranking that matters
| | proves the set is COMPLETE? | needs an oracle? | cost |
|---|---|---|---|
| A DERIVE | no | no | low |
| D ATTRIBUTION | no — only that the known set is fully dispositioned | no | low, continuous |
| C CROSS-DERIVE | no — but **surfaces disagreement without ground truth** | **no** | medium |
| B SIMULATE | **closest thing to yes** — bounded by candidate enumeration | no (it *is* the oracle) | high |

**A and D are what we mostly have. C is the highest-leverage unbuilt-at-scale option. B is reserved
for where being wrong is expensive.**

## §4 The blind-spot patterns, as a checklist against any tool

Derived from the primitive, so it is mechanical rather than per-tool judgement:

| enumeration primitive | characteristic blind spot | worked instance |
|---|---|---|
| `git ls-files` | gitignored · submodule contents · untracked · anything not in the repo | comp-heat: audit logs, portal, all P2 code |
| `os.walk(roots, ext)` | outside roots · unlisted extensions · non-filesystem stores | comp-clobber: `s3://.../code/` producers |
| regex over source | variable-interpolated values · dynamic construction | comp-clobber `_S3_URL` vs `s3://${VAR}/...` |
| AST parse | non-Python lanes · runtime indirection | comp-constants (recorded in TOOLARCH §3) |
| grant-shape lint over TF | AWS-MANAGED policies · `Resource:'*'` | the 4-roles-really-6 incident |
| registry read | anything unregistered — **the phantom class** | MSBEFF: 129 referenced vs 83 registered |
| live API `list_*` | other regions/accounts · resource types not queried | — |

**The rule this yields:** *a tool's blind spot is a property of its enumeration primitive, not of its
author's care.* So it is derivable at registration time and does not need to be rediscovered per
incident.

## §5 Recommendation — three increments, in order, none greenfield

1. **Add `excludes:` to the existing `comp-coverage-map.yaml` schema**, populated **from the primitive
   table in §4** rather than by hand — mechanical, and it inherits the passing S2 gate for free.
2. **Wire PATTERN C at suite scale**: `comp-toolgraph`'s DECLARED-vs-ACTUAL diff already exists for
   coupling; point the same shape at *coverage* (declared surface vs primitive-derived surface). **This
   is the negative control that needs no oracle**, and it is the single highest-value build here.
3. **COMPRAIL reads `surface` at route time** — the question↔tool comparison. Unchanged from §6.

**What I am NOT recommending:** a new declaration format, a new project, or a rebuild of anything.
COMPUNIFY S0–S2 is built and green; this is one field, one diff, and one route-time read.

## §6 Limits

- §3's four patterns are abstracted from **three live instances plus one gate rule**. They are named
  from real code, **not validated as exhaustive** — there may be a fifth shape nobody has built.
- §4's table is complete for the primitives I resolved (**35 of 92 tools**); the remaining 57 are
  UNRESOLVED-not-absent, pending the wrapper-follower fix.
- Trino/Nessie remain deferred by Andrew; PATTERN B's cost profile is the reason the Trino federation
  (~3-4 min/query) is an analytical surface rather than a gate.

— 3.0.0_SA_CVO
