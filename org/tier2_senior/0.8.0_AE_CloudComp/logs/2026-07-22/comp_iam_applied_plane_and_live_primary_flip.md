# comp-iam: APPLIED plane built, then FLIPPED to live-primary — and the graph freshness headers were measuring the wrong clock

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Window 2026-07-22 ~14:17Z -> ~15:40Z, continuing from `ee59efb15` (which closed at 11:34Z). Serial
`0.8.0_AE_CloudComp`. Andrew-direct throughout; working directly for him under his standing
instruction *"You are my agent not theirs. Do not talk to tier 1 agents unless I say so."*

## Commits (8, all pushed)

| Commit | What |
|---|---|
| `804fe34da` | Andrew-direct RECORD (verbatim) + located the CVO brief; PRD confirmed ABSENT |
| `c490ee017` | APPLIED plane increment 1 — vintage-stamped census + fail-closed vintage gate |
| `840ad1e67` | census aws-executable resolver fix; generator EXERCISED live (205 roles) |
| `1ff543927` | grounding for the live-primary flip |
| `ae8e03597` | LIVE-PRIMARY plane + the four-clock freshness finding |
| `93a31c299` | workflow topology + design D1-D6 |
| `c6434108d` | D1/D3/D5 implemented |
| `4a09baa49` | D2/D4 implemented |

## What was asked and what happened

Andrew assigned the comp-iam APPLIED plane and asked me to find CVO's brief to CTO. Found it
(`COMP_IAM_APPLIED_PLANE_DESIGN_BRIEF_20260720.md`); **verified PRD-ABSENT rather than inheriting his
"I don't think so"** — nothing under `docs/architecture/`, `docs/briefs/` or `org/projects/`, no
registered project. It sat two days and surfaced only because he remembered it. *Durable is not
reachable.*

Built the census + fail-closed vintage gate (CVO §9's load-bearing item, not the generator). Then he
proposed flipping the tool to key off live state instead of Terraform. I **tested the hypothesis
rather than agreeing**: right in effect, wrong in dominant cause. Then he asked me to establish the
provenance of the freshness headers, suspecting they mislead. **They do**, and the mechanism is
precise. Then D1-D5, then D2/D4.

## Findings that changed the work

**1. The unjoinable class is a CATEGORY ERROR, not a parser gap.** comp-iam joins DESIRED->APPLIED on
exact `RoleName`. Terraform source is a TEMPLATE — identities resolve at apply time — so `iam_cli`
holds a role literally named `opal-assets-silver-${each.key}-role`: one template row that can never
equal the six real roles it produces. No amount of better parsing fixes it. This is a stronger
argument for the flip than the one proposed.

**2. FOUR CLOCKS, and the header showed the wrong one.**

| Clock | Measures | Age |
|---|---|---|
| `built:` | local kuzu DB assembled | 2.2h |
| `graph_nodes: last-write` | the nessie TABLE write | 4.5h |
| `snapshot_ts` on rows | **when the estate was OBSERVED** | **17.1h** |
| derive JSON mtime | untracked local scratch | 201h |

14,708 full-derive nodes at 02:00:31Z; **TWO** incremental nodes at 14:37Z set the table clock. The
header printed `last-write 4.5h (< 6h cadence)` = PASS. Against the cohort it names: 17.1h > 6h =
FAIL. **A last-write timestamp is a property of the container, not the contents** — and it is
monotonic the wrong way, since a finer-grained incremental updater refreshes the table clock more
often while covering the same corpus.

**3. The pipe is ALIVE and yielding nothing — a third state I had not enumerated.** I wrote that the
2-node cohort was ambiguous between *quiescent* and *dead*. Measured: `invocations=114 errors=0
sqs_sent=2492 queue_depth=0 dlq_depth=0`, logs `processed_arns=0 nodes_written=0`. Neither. The
inference I would have drawn ("dead, escalate") manufactures a false outage. This is exactly why D3
said measure the pipe rather than infer from node counts.

**4. The reconciliation oracle closed the open question.** `CreateDate` separates the producers'
obligations. Result: **NO ATTRIBUTABLE GAPS — zero incremental misses**; all 12 gaps are
`AWSServiceRoleFor*` scope exclusions, not defects.

## Errors I made and corrected (all self-caught)

1. **"28 roles have no Terraform" — RETRACTED.** A literal substring scan cannot find an identifier
   Terraform CONSTRUCTS (`name = "opal-assets-silver-${each.key}-role"`; 102 interpolated `name =`
   assignments exist). **kuzu was right; I was wrong.** Absence of a literal match read as absence.
2. **Lifted comp-tagauthz's CALL and left its RESOLVER behind** — bare `aws` argv, `WinError 2`. The
   part that made it work was one function up from the part I copied.
3. **`cmd | head` captured head's exit code**, not comp-iam's — the documented pipeline-rc trap.
4. **My own permission script returned a false DENY** — `permitted_agents: "*"` is a wildcard STRING
   and I ran list-membership on it.
5. **Labelled `ms`/`semctl` "event-driven"** in D2's first cut, from "not in my cadence table". They
   now read `cadence UNDECLARED — NOT judged`.
6. **The oracle's first result called 12 scope exclusions "MISSES"** — would have cried wolf 12x per
   run forever. Miss = obligation unmet; exclusion = no obligation existed.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-iam` | `refresh-census` / `live` / `reconcile` / `census-self-test` | PASS + real REFUSALs | built these surfaces; generator exercised live (205 roles); gate refuses the undated 06-03 census rc=3 |
| `comp-kuzu` | node/kind/source/snapshot_ts cross-tabs | PASS | the instrument that **falsified my grep** and supplied the four-clock evidence |
| `comp-grep` | sovereign/comp-iam caller sweeps | PARTIAL | correct on literals; **structurally blind to interpolated identifiers** — the root of error #1 |
| `commit-gate` | every commit | PASS | caught 2 ruff violations in my own patches (E401 x2) |
| `comp-aws` | `derive --classes iam` | FAIL | `unrecognized arguments`; correct invocation NOT determined |

**What worked:** comp-kuzu's structured `snapshot_ts`/`source` fields made the four-clock finding
measurable rather than arguable. comp-iam's own new provenance header caught its own generator's
first bug (fail-closed degraded honestly instead of writing an empty census).
**What failed:** `comp-aws derive --classes iam` is rejected — the derive artifact could not be
refreshed, so the accept-side control was proven on a touched copy instead, stated as such.
**Gap found:** `comp-grep` cannot match a constructed identifier, and its clean 0 is indistinguishable
from absence without a positive control — the same class Andrew recorded this morning for git-ref
search. My retraction of the "28 roles" claim is a live instance.

## Blockers

**None on this work.** Two standing items unchanged and NOT worked this window:
- predicate-split wave: built, 90/90 green, unstaged at fingerprint `1673ceac9c2bd70f`, blocked on the
  owned-paths ANY_EXEC authorship refusal — CTO's to clear.
- 6 undiagnosed CI reds + the CRO `liveness.json` item — both post-wave in CTO's sequencing.

## Current State

- `comp-iam` has THREE planes: DESIRED (TF, unchanged) · APPLIED-inventory (`refresh-census`, `live`)
  · APPLIED-decision (`simulate`, untouched). Detector/oracle tier separation intact — `live` states
  in its own output that it evaluates no Deny/boundary/condition/SCP.
- `comp-iam live` is graph-primary, keyed on `snapshot_ts`, with `--pipe` liveness, a census
  population cross-check, and the D4 oracle. Fails closed on a stale/undated source.
- `_provenance.py` emits cohort vintage alongside (not instead of) the table-write lines, which now
  say what they are.
- NEW: `comp_iam_census.py`, `comp_iam_live.py`, `tests/test_iam_census_vintage.py` (5/5),
  `census-self-test` (17/17).
- The live census is deliberately NOT committed — a 24h-TTL artifact in git becomes the stale undated
  artifact that caused this defect.
- **BUILDER-VERIFIED ONLY.** CVO reserved verify-on-land (his §9) and I cannot hand it over under the
  no-Tier-1 instruction. On a tool whose defect class is FAILING GREEN this is the weakest posture
  available; naming it rather than letting 5/5 stand in for independent verification.

## Next Steps

- **[Andrew]** whether to release the CVO verify-on-land handoff, and whether D6 (the
  service-linked denominator question) should be settled or left stated.
- **[0.8.0_AE_CloudComp]** open items if continued: the correct `comp-aws derive` invocation;
  whether zero `source=incremental` IAM rows is correct or a derivation gap (settling it needs one
  known IAM mutation to correlate — not run against production for instrumentation); the doc-vs-TF
  drift at `_provenance.py:405` ("runs hourly" vs SQS event-driven); and the live
  `MARKER_CAS_DISABLED` warning in the updater log, which is the exact hazard `_provenance.py:402-409`
  documents, firing now.
