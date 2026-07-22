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
| `comp-aws` | `derive --class iam` | RESOLVED | I ran `--classes` (plural) -- wrong flag, not a broken tool. See the CORRECTION section. |

**What worked:** comp-kuzu's structured `snapshot_ts`/`source` fields made the four-clock finding
measurable rather than arguable. comp-iam's own new provenance header caught its own generator's
first bug (fail-closed degraded honestly instead of writing an empty census).
**What failed:** `comp-aws derive --classes iam` was rejected, so the accept-side control was proven
on a touched copy instead. SUPERSEDED -- the flag is `--class`; see the CORRECTION section.
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

---

# ADDENDUM — CVO verify-on-land: 4 P1s closed, both not-reached items closed

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT

Window ~15:40Z -> ~20:10Z, continuing this log. Andrew released the CVO handoff explicitly
("Yes, hand off the CVO verify") — a **SCOPED** release of his no-Tier-1-contact instruction, read
narrowly: it authorised the CVO loop, not a general channel re-open.

## Commits (3, pushed)

| Commit | What |
|---|---|
| `2901f1fc9` | handoff record + the scoped-release amendment |
| `72fda2aa5` | all 4 CVO P1s fixed, mutant-locked |
| `996fcad53` | both CVO not-reached items closed |

## Handoff design decision

**I gave CVO the METHOD and withheld my artifact.** His §9 commits him to verifying "against a fresh
census"; had I sent mine, he would have been checking my artifact with my tool. He regenerated his own
and landed at 205 — same as mine — so the population is **REPRODUCED, not accepted**.
*A verifier handed the builder's evidence is checking arithmetic, not truth.*

## CVO verdict (@da7478839): BROKEN@MECHANICAL + BROKEN@DECLARATIVE, SEMANTIC PASS. 4 P1, 0 P0.

**F1 — the headline, and I had logged it as a curiosity.** A future-dated census read `FRESH`;
pushing the date *forward* made it read *fresher*, so any stale census became authoritative via a
one-field edit. His framing is why it is P1, and it is now in the source verbatim:

> **A CONTROL WHOSE BYPASS IS CHEAPER THAN ITS OVERRIDE CHANNELS BEHAVIOUR TOWARD THE BYPASS.**

`--allow-stale-census` is audited and stamps the verdict non-authoritative; editing `generated_utc`
is silent. The gate refused a census that *cannot* date itself and accepted one whose date is
*impossible* — the same epistemic state, opposite verdicts. My verdict set had no cell for
"impossible". FIX: a `FUTURE` verdict past a 0.25h clock-skew tolerance (minutes of skew are real,
hours are not — a blanket future-refusal trades a false-accept for a false-refuse).

**F2** — `live --census` applied no vintage gate at all; two census-overlay surfaces, one gated. Fixed
by DISQUALIFYING THE LIMB rather than refusing the report: the graph is `live`'s primary source and
stays trustworthy. **CVO falsified his own harm hypothesis here** — he expected suppression, found
none, because the 111-role census happens to contain the 12 roles in question. *"The coincidence that
saved it is not a design property."* The real defect was the denominator: a stale run printed
"graph 193 vs census 111", reading as the graph OVER-enumerating by 82 when against a live 205 it
UNDER-enumerates by 12.

**F3 (DECLARATIVE)** — my docstring claimed future-dating was "flagged by the caller's provenance
line". It was not: `[FRESH]`, no marker, while the undated case got a loud `!!`. The marker existed
and was simply not applied. *Visible-to-a-careful-reader is not a flag and not a control*, and a
record describing a safeguard one strength above the code is worse than no record.

**F4 (DECLARATIVE)** — `live` carried the detector disclaimer; `reconcile` did not, while saying
"granted live" and evaluating no Deny/boundary/condition/SCP. **I back-fitted the guard to the surface
I had just built and left it off the older, more-quoted one** — so the surface people actually use
kept the defect.

## Two defects I introduced INSIDE the fix and caught pre-commit

The F1 refusal initially reported a FUTURE census as *"is STALE (older than the 24h TTL)"*, and the F2
disqualified path then printed *"UNAVAILABLE (no --census)"* when one WAS supplied and rejected.
**Committing the misreporting defect inside the fix for the misreporting defect would have been its
own finding.** Disclosed to CVO rather than left as a quiet save; he verified both actually correct in
the landed code.

## CVO's upward correction — I was UNDERclaiming

I said the Plane-3 hazard was "absent because unbuilt". He verified `cmd_simulate` untouched (every
hunk a pure insertion, none inside `:537-745`) **and corrected me upward**: the pre-existing
`cmd_simulate` already enforces `ResourceArns=[arn]` one-per-call (`:597`), separate positive-control
invocations (`:620,656`), and a self-test asserting `len(ResourceArns)==1` (`:698`). The Rule-22a
guard EXISTS and is TEST-ENFORCED. A wrong statement about the estate in the safe direction is still
wrong.

## Both not-reached items — closed on evidence (996fcad53)

CVO left the D4 scope-exclusion and the `_provenance.py:405` contradiction explicitly NOT-REACHED
("never clean") and was blocked from scheduling under Andrew's hold. Both mine; both closed.

**D4 suppression — adversarially checked, then made self-falsifying.** T1 (the falsifier:
service-linked roles Terraform declares) = 0; T2/T3 (path-vs-name disagreement, either direction) = 0.
The rule is sound. **But "0 today" is a data-dependent result, not a property of the rule** — it holds
only while nothing we govern lives under `/aws-service-role/`. So the falsifier is now a STANDING
CONTROL whose failure text says *narrow the rule, do not silence the test*. And I confirmed the
control is **discriminating rather than decorative** by injecting `AWSServiceRoleForECS` into a TF set
and checking the predicate fires — a falsifier that cannot detect its own condition is the
instrument-that-cannot-fail class.

**`_provenance.py:405` "runs hourly" — RESOLVED, and wrong in the direction that matters.** No
`schedule_expression` exists for the incremental updater anywhere; the SQS ESM is its only trigger.
Measured 114 invocations/24h = ~4.75/hour, ~5x the documented rate. That clause supports the
docstring's own erasure hazard, so the hazard fires ~5x more often than the record claims — and **a
frequency error that understates a hazard is the direction that gets it deprioritised.** The live
updater log carries `MARKER_CAS_DISABLED -- table_metadata is REPLACED, not merged`: that hazard,
firing now.

## Compiler Tools (addendum window)

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-iam` | `reconcile` / `live --census` / `census-self-test` against FUTURE + undated + stale + fresh mutant censuses | PASS + correct REFUSALs | the F1/F2 exercise; accept side still computes (graph 193 vs census 205) |
| `commit-gate` | every commit | PASS | blocked once on a real E401 in my own patch |
| `pytest` | `test_iam_census_vintage.py` | 10/10 | +4 regression locks, +1 standing falsifier |

**What worked:** the mutant discipline — deleting the `FUTURE` branch failed 4 of 9 tests, so the new
locks are load-bearing rather than decorative.
**What failed:** nothing new. (`comp-aws derive` since RESOLVED -- see the CORRECTION section.)
**Gap found:** none new this window; the three from the main log stand.

## Current State (supersedes the section above where they differ)

- All 4 CVO P1s FIXED and mutant-locked; RAVC CLOSED by CVO @e8dd46725, re-verified against **his**
  mutant files with the F1 boundary probed directly (+15min FRESH, +16min FUTURE).
- CVO recorded the F2 fix as **BROADER than his finding** — I gated the whole verdict class
  (`NO_VINTAGE`/`STALE`/`FUTURE` each disqualify and each say which), not just the two cases reported.
- Suite 10/10. Working tree clean of my work. 13 commits this session.
- **No longer builder-verified only** — independently verified by CVO, twice, against artifacts I did
  not produce.

## Next Steps

- **[Andrew]** nothing outstanding on comp-iam; the two items CVO could not reach are closed.
- **[0.8.0_AE_CloudComp]** ~~the correct `comp-aws derive` invocation~~ RESOLVED (`--class`, see the
  CORRECTION section). Still open: whether zero `source=incremental` IAM rows is correct or
  a derivation gap — the D4 oracle now reports NO ATTRIBUTABLE GAPS, consistent with "no IAM role
  mutated", but settling it still needs one known IAM mutation to correlate.
- **[unowned]** the live `MARKER_CAS_DISABLED` warning is a real production hazard in the globgrph
  writer path, now with a corrected (5x higher) frequency. Not mine to fix; recorded twice.

---

# CORRECTION — the `comp-aws derive` invocation is RESOLVED (supersedes 4 records in this log)

**archetype:** DIAGNOSE

Andrew asked whether I had suggested a fix for the failing `comp-aws derive` invocation. **I had not.**
I flagged it four times across this log, two commit messages and the compiler-tools log — every time as
*"the correct invocation was NOT determined"* — and never spent the one command it took to determine it.
He was half-right to remember it: the flag was real and repeated; the suggestion never existed.

**THE FIX IS `--class`, SINGULAR.** I was passing `--classes iam`. `comp-aws derive --help` states the
argument plainly:

```
usage: comp-aws derive [-h] [--class CLS] [--out OUT] [--resource RESOURCE]
```

Exercised, read-only, output to scratchpad so no shared surface moved:

```
comp-aws derive --class iam --out <path>
counts: {"live": 193, "tf_declared": 172, "live_declared": 174, "live_no_declared": 19,
         "declared_no_live": 0, "untyped": 0}     nodes: 193
```

## What this changes, and what it does not

- The Jul-14 artifact read `live 183 / tf_declared 162 / live_declared 164 / live_no_declared 19`.
  A fresh derive reads `193 / 172 / 174 / 19` — the population grew by 10 and the drift count is
  UNCHANGED at 19. So the eight-day-old snapshot was under-enumerating but not mis-classifying.
- The fresh derive's 193 matches kuzu's 193 exactly, which is the expected agreement (both exclude the
  12 AWS service-linked roles that the live census's 205 includes). Two independent reads agreeing on
  the governable population is a real cross-check, not a coincidence.
- **`comp-iam live`'s conclusions are unaffected.** It reads the graph, not this artifact, and the
  derive-JSON path is a declared fallback.

## The part worth keeping

**A one-command answer sat behind a `--help` I never ran, and I recorded "not determined" four times
instead.** Repetition made it look investigated. Writing an unknown down carefully — with its
denominator, in the right sections, in the commit body — is not the same as resolving it, and the
care in the recording is exactly what made it feel handled.

Nothing about it was hard. It was undetermined because I never looked.

Also worth noting, because it is good instrument behaviour: the tool printed an unprompted
**NOT PUBLISHED** notice explaining that a local derive does not refresh comp-kuzu's canonical
Nessie-sourced surface, naming the two commands that would, and warning that bare `comp-aws snapshot`
does NOT refresh it either. That is a tool refusing to let a local run be mistaken for a published one
— the same class of honesty this session has been building into comp-iam.

## Records superseded by this correction

- the Compiler Tools table above (`comp-aws | derive --classes iam | FAIL`) — flag was wrong, not the tool
- "What failed" in the main body, and the addendum's repeat of it
- the addendum's Next Steps item — now closed
- `org/compiler-tools-log.md` — corrected in the same commit

Commit messages `c6434108d`, `4a09baa49` and `996fcad53` carry the stale claim and are immutable;
this correction is the propagating record.
