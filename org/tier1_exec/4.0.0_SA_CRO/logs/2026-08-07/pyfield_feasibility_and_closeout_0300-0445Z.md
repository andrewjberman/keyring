# 4.0.0_SA_CRO -- NFRA_PYFIELD feasibility measured (and my own headline corrected 3x down), charter breaches closed, everything routed (2026-08-07 03:00Z -> 04:45Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** SCRIBE, COORDINATE

## Window

03:00Z -> 04:45Z. Prior log: `script_io_s_layer_dissolved_and_layer_anatomy_0100-0300Z.md`.
Continuation of the Andrew-direct Script I/O engagement with `3.0.0_SA_CVO~C` + `1.0.0_SA_CTO~D`,
CRO driving. **The S-layer was already dissolved when this window opened**; this window is the
residue: feasibility for the build it left behind, plus closing my own charter gaps.

## What happened

**1. `1.0.0_SA_CTO~D` shipped `NFRA_PYFIELD_PRD` v0.1 and held it to the standard that killed the
S-layer** -- §7 Q1 is *"should this be built at all,"* their own recommendation is **DEFER**, and they
**deliberately registered no project** (registering implies active work; a "do not build" would force
closing a project that never started).

**2. Q2 spike run, because they wrote it should PRECEDE the build.** Flow-local (binding-side)
inference reaches **24.3%** on the gold trees. **Then I formed a hypothesis and refuted it**: seeing
`df` unresolved 100x I assumed the missing mass was FUNCTION PARAMETERS -- which would have been
decisive, since inter-procedural inference is a far more expensive build. Measured: **9.4%, not 90%.
A more alarming conclusion was available and the evidence did not support it.**

**3. The real Q2 answer is that the bar CANNOT be set** -- the unresolved mass is largely dicts and
JSON records that were never columns, so 24.3% is a true statement about SUBSCRIPTS and a meaningless
one about COLUMNS. **No column denominator exists.** This *strengthened* DEFER for a reason neither
of us had: not "the mechanism is weak" but **"we cannot state what success would look like."**

**4. CTO~D found a second discriminator I had not tested** -- USAGE-side (a pandas-only method called
on the subscript *result*), which fires precisely where binding-side is blind. Measured the 2x2:
**largely independent** (overlap 34.6%), union **41.1%** vs 27.6% binding-alone, **+13.5 pts
net-new**. And it partially answered the denominator question -- usage-side hits are *evidence of
column-ness*, so they floor the column population.

**5. THEN I SENSITIVITY-TESTED MY OWN MARKER SET AND THE HEADLINE COLLAPSED.** I had flagged the set
as hand-chosen and untested, then let it stand in someone else's PRD. Tested:
**12 strict markers -> +3.8 pts · 36 (mine) -> +13.5 · 48 wide -> +14.5.**
**My published number was 3.5x the conservative reading**, and the "floor" claim I was proudest of
fell from >=23.1% to >=8.1%. Sent as a CORRECTION-SEND-FAST while their v0.2 was hardening;
recommended they carry the RANGE and use **+3.8** if one number must carry a decision.

**6. Charter breaches closed, both found by testing my own claims rather than by review:**
- **§4 (register + in-band IDs):** I had raised a discoverability gap against CVO's ontology index
  while **my own `RECON_REGISTER.md` listed none of the five artifacts I had produced** (measured 0/5).
  `RCN-0006` appended with its lateness stamped in-band; then the five in-band `Recon ID:` tags
  discharged (0/5 -> 5/5).
- **§8 (preserve the tooling):** five probes producing **every number in CTO~D's PRD** existed only in
  a reapable scratchpad -- while I twice told them to *"re-derive before the PRD rests on it."*
  Preserved to `scripts/pyfield_probes/`.

**7. Andrew ruled the held-out fence** (relayed via CVO~C, recorded VERBATIM): *"its just an obvious
thing and dont need more noise about it."* **The fence is NOT discharged** -- he rejected EXPANDING
it. §8.1 closed.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python`/`ast` (5 probes) | binding-side, base-name, parameter, 2x2, 3-point sensitivity | **CAUGHT-OWN-DEFECT x2** | refuted my own parameter hypothesis; then falsified my own +13.5 headline |
| `ruff` (via commit-gate) | blocked the probe preservation on 44 cosmetic findings | **GATE WORKED** | forced byte-identical -> **behaviourally identical, PROVEN by re-run** |
| `git ls-tree` | verify probes in HEAD | PASS | after a **malformed** `--stat --name-only` check returned a false 0 |
| `comp-which` | discoverability test on the anatomy file | **COVERAGE GAP FOUND** | self-reported *"THE CATALOG DOES NOT COVER IT"* -- routed to the tool lane |
| `comp-kuzu` | (prior window) the measurement that dissolved the S-layer | PASS | not re-run this window |
| `safe-commit.sh` | 8 commits, all `-F` | PASS | one heredoc parse failure caught and re-done via Write |

**What worked:** testing my own claims instead of asserting them. **Every finding this window came
from checking something I had already said** -- the parameter hypothesis, the marker set, the register,
the tooling, the "referenceable" claim.
**What failed:** three instrument-shaped errors in one window, all mine, all caught -- a `sed` on a
multi-line literal that errored into a `grep` and **read as an empty result**; a `--stat --name-only`
check that suppressed itself and **reported a successful commit as failed**; and a denominator quoted
from one probe under another probe's name (4896 vs 4897).
**Gap found:** `comp-which` has **no curated rule** for ladder field-shape questions; per Rule 21 a
comp-tool coverage gap is a DEFECT. Routed, not adopted.

## MCP traffic

**OUT:** CTO~D x5 (feasibility, Q2 spike, two-axis, sensitivity correction, DDL answer to ~B);
CTO~B x1; CVO x2 (index gap, C3.i close); `0.7.0_AE_CloudOps` x1 (DDL divergence -- **deposited, not
delivered**: no channel push, they were offline).
**IN:** CTO~D x6 · CTO~B x2 · CVO x3 · CVO~C x3 · AE x2.

## Blockers

**None at me.** **Q1 is at Andrew and it gates everything downstream** -- build a Python field-grain
extractor with no named consumer and no statable acceptance bar, or defer. **CTO~D recommends DEFER;
I concur.** Also at Andrew: placement of artifacts into `projects/ATOM_DECOMP/` (lane `TIER0_MSTR`).

## Current State (zero-context handoff)

- **The S-layer stays DISSOLVED.** Nothing this window reopened it; the residue is a build question.
- **`NFRA_PYFIELD` PRD is CTO~D's**, v0.2, no project registered by design, DEFER recommended.
- **Every figure I published is now bounded in writing**: subscript != column; marker-sensitivity
  +3.8 to +14.5; four non-held-out trees only; `bd`/`cot`/`mdpf`/assets-monolith UNSWEPT; probes are
  **measurements, not instruments** -- no tests, not on the rail, not registered.
- **My desk is clear of owed items.** Register current, tags discharged, tooling preserved, anatomy
  indexed and corrected, disposition closed with the fence ruling folded.
- **Andrew's loop stop-condition is NOT self-assessed as met** -- the *question* is closed and
  exercised, the *capability* is unbuilt and now gated on his Q1. **atom_decomp is NOT self-authorized.**
- **`/loop` 10m still armed** -- cron `57624188`. Not stood down; that is an operator act.
