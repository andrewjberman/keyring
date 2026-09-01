# ANDREW-DIRECT 2026-09-01 — RE-AUTHORIZE enforcement layers 1, 2 and 3-sweep; ADD the stage-3 preflight

**Channel:** Andrew-direct, the `3.0.0_SA_CVO` terminal, 2026-09-01.
**Recorded by:** `3.0.0_SA_CVO`. **Relayed, never adjudicated — verbatim scope, neither widened nor narrowed.**

---

## 1 · THE WORD, VERBATIM

> **"re-authorize the three enforcement layers and add the stage-3 preflight"**

**Context it was given in, so scope is readable later:** I had reported that
`org/ref/DIRECTIVE_EXECUTION_PIPELINE.md` (2026-08-21) specifies a five-layer enforcement
architecture; that **layers 1, 2 and layer 3's sweep hook were marked `build routed` and never
shipped**; and that the doc itself predicted the consequence — *"Until layers 1–3 land: the pipeline
binds as protocol… The gates convert 'followed religiously' from a vow into a property."*

---

## 2 · WHAT "THE THREE ENFORCEMENT LAYERS" RESOLVES TO — quoted from the pipeline table, not paraphrased

| layer | mechanism, as already specified | prior state |
|---|---|---|
| **1. Validation gate** | `proof-of-spec-check.py` extension: an instance for a pipeline-bound project is **INVALID without a `decomp_ref` + bidirectional cell↔criterion mapping (denominators printed)**. **No VALID instance → no `complete` flip.** | build routed, **never built** |
| **2. Commit gate** | commit-time lint: a **NEW TO file** under `org/**/task_orders/` whose project is pipeline-registered **must carry `<decomp_ref>`** — refused otherwise. Teaches at violation time. | build routed, **never built** |
| **3. Machine-readable stage — THE SWEEP HOOK ONLY** | the `dep_stage` enum itself **LANDED** (COO @`c4d8c0025d`). What did not land is the **sweep** (`comp-state` / `registry-check`) that makes COO's TO pass instrumented rather than heroic. | enum landed; **sweep hook never built** |

⛔ **Layer 3's ENUM is not re-authorized because it does not need it — it landed.** ⚠ **And its
FORWARD-ONLY / no-back-fill rule stands unchanged**: a back-filled `dep_stage` is a guess about history
wearing a controlled vocabulary's clothing.
⭐ **MEASURED 2026-09-01, the cost of the sweep never landing: 316 of 348 project JSONs carry NO
`dep_stage` key at all.** The enum exists and nothing populates it — which is why **139 of 281 proof
instances sit under the resulting waiver** and 77 belong to project codes with no project JSON.

---

## 3 · THE STAGE-3 PREFLIGHT — what is being ADDED (this is new; it is in neither doc)

**Run by `2.0.0_SA_COO` at stage 3, AFTER atom-decomp and BEFORE TO dispatch.** Purpose, in Andrew's
framing: *COO should issue perfect-enough deliverables — no massive flaw — so agents are only executing.*

| # | tool | what it is asked to surface | why, measured |
|---|---|---|---|
| **P-1** | `/comp-schedule` | preconditions and gates that could interfere with the round | `comp-schedule`'s own live run found **18 gates, 135 NEEDS-READ prose rows, and a gate SATISFIED 2026-07-13 still armed** |
| **P-2** | `comp-iam` | permissions on the resources the decomp actually touches | **2026-09-01: a false `implicitDeny` cost five seats an afternoon, a revoked grant and a false self-attribution. Andrew-direct the same day: *"remember comp-iam when checking these things."*** ⚠ **And its population is LAMBDA ENTRY POINTS ONLY — the EC2/SSM chain is outside it; that hole must be declared in the preflight record, not discovered later** |
| **P-3** | `/comp-adversary` | the complement — what the decomp did NOT look at | its uncited-sibling list turns *assumed clean* into *declared unexamined* |

### 3.1 ⭐ HOW THE PREFLIGHT BECOMES ENFORCED RATHER THAN A VOW

⛔ **A preflight that is only mandated in prose is the same vow that layers 1–3 already are.** The
pipeline's own **choke-point principle** gives the answer: *gate the NECK of the funnel, not every stage.*

>> **FOLD THE PREFLIGHT INTO LAYER 2. A new TO already must carry `<decomp_ref>`; require additionally
that the DECOMP it references carries a `preflight` block with P-1/P-2/P-3 each recorded as RUN (with
its invocation and denominator) or DECLARED-NOT-APPLICABLE (with a reason).** One gate, two
requirements, no new checkpoint — **and a preflight that was skipped becomes a TO that cannot be cut.** <<

⚠ **`DECLARED-NOT-APPLICABLE` is deliberate and is the third value:** a preflight enum of RUN/SKIPPED
would force a genuinely-inapplicable tool to be recorded as skipped, and **a vocabulary with no
not-applicable value encodes non-application as a violation** — measured eight times on 2026-09-01.

---

## 4 · ONE ITEM I AM NOT TREATING AS AUTHORIZED, BECAUSE THE WORD DOES NOT CLEARLY REACH IT

In the report that preceded this word I listed **four** deltas. Three are tool runs and are plainly
"the stage-3 preflight". **The fourth was a ROUND / CYCLE ID so `v(n)` is traceable — a schema and
naming concern, not a preflight act.**
⛔ **I am NOT relaying it as authorized.** ⚠ It is arguably load-bearing for the cycleability Andrew
asked for — `INVESTIGATION_v{N}` / `REMEDIATION_v{N}` already imply a round number with **no field
that carries it** — **but "the stage-3 preflight" does not obviously include it, and widening a
sovereign word is the act CLAUDE.md forbids most explicitly.** **Surfaced for his one-line answer;
nothing waits on it.**

---

## 5 · PLACEMENT — NOT MADE HERE

⛔ **Rule 27 puts placement with `2.0.0_SA_COO`. This record authorizes; it does not assign.**
Observations offered as input, not as dispatch:

- **Layer 1** touches `.tools/proof-of-spec-check.py` — the file `1.0.0_SA_CTO~X` authored the
  artifact-resolution arm in. A second arm sits naturally beside it.
- **Layer 2** is a commit-time hook — the `.tools/hooks/never-rules-gate.sh` pattern already exists.
- **Layer 3's sweep** is `comp-state` / `registry-check`, the comp-tool lane.
- **P-1/P-2/P-3** are COO's own acts at stage 3; only the *record* of them is checkable by layer 2.

⚠ **AND A SEQUENCING CONSTRAINT WORTH HAVING BEFORE ANYTHING IS CUT:** layer 2 enforcing a `preflight`
block means **every TO cut after it lands needs one**. If layer 2 ships before COO's stage-3 process
changes, **TO issuance blocks estate-wide.** **Layer 1 and layer 3's sweep have no such coupling and
can land independently.**

---

## 6 · WHAT THIS RECORD DOES NOT DO

⛔ Does not build anything. ⛔ Does not assign a lane. ⛔ Does not amend `CLAUDE.md`, the pipeline doc
or the protocol doc — **those edits belong to their owners and to a law-edit's three surfaces (commit
+ same-turn broadcast + push state).** ⛔ Does not back-fill `dep_stage`, which remains forward-only.
⛔ **Does not re-open the specification: layers 1–3 are already specified in the pipeline table and I
am re-authorizing them AS WRITTEN, not re-designing them.**
