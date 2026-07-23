# NFRA_MSBEFF Case Study 1 — the MDPF arc: what each defect needed, which tool should have supplied it, what actually happened

**Method (PRD §2 Phase 2):** for each defect in the MDPF_3FIRMS RF ledger (§2.5, the arc's ground
truth), reconstruct: the QUESTION an agent needed answered · the TOOL that should have answered it ·
WHAT ACTUALLY HAPPENED (from telemetry + the postmortem + carrier docs) · the M/S/B layer verdict.
Telemetry base: comp-tool-runs.jsonl 07-14→23 (the arc's hot window) — **665 MDPF-tagged runs, of
which 560 are auto-gate fires; ~105 chosen tool runs across 8 agents on the estate's #1 project.**

## The per-RF grid

| RF | The question that needed answering | Tool that should have answered | What actually happened | Layer verdict |
|---|---|---|---|---|
| RF-1 PUBLISH_MAP no-Cottonwood | "Which structures hardcode the firm set?" | comp-constants (multifirm lane) | `PUBLISH_MAP` was **never registered** as a constant, so the tool had no denominator to check it against; found by human census 07-22. Blindness even if registered: wrong axis (drift-not-completeness) until item 7 | **S** (registration coverage) + M (axis) |
| RF-2 freshness one-firm dict | "Does the freshness gate evaluate ALL firms?" | comp-freshness | The gate evaluates what its own config names — *a completeness signal whose denominator is its own configuration* (doctrine `f9f6a4c72`). Nothing asked whether the config was complete over the world until the P1 registry gate | **M** (instrument design) |
| RF-3 six fold sites, four null-poison | "Where does global composition fold per-firm data, and does each site survive a no-history firm?" | comp-blast/comp-grep enumerate sites; NO tool evaluates null semantics | Caught by CVO **STOP-BEFORE-BUILD** — human verification, not instrumentation. Enumeration was tool-feasible; the semantic evaluation legitimately is not | **S** (site-enumeration query unnatural to phrase) / judgment beyond tool scope |
| RF-5 orchestration fixed at 2 firms | same as RF-1 | comp-constants | same class as RF-1: unregistered structure, wrong axis | **S** + M |
| RF-6 audit markers from config | "Do the audit controls derive their denominator from the world?" | none existed | Controls 1–4 passed green on a cycle missing a firm; Control-5 (synthetic firm) invented in response | **M** (instrument design; now doctrine) |
| RF-7 49F counts from a legacy SERVED artifact | "Does any gold/silver producer read from a served artifact?" | none existed — zero coverage class | Discovered by manual trace during the revamp; PSTMRT item 9 (layer-grammar gate) is the remediation | **M** (missing instrument, now building) |
| RF-9 converter committed-not-deployed (later corrected: WAS deployed) | "Are the live bytes the committed bytes?" | comp-pipescript deployed — but its coverage is gold-script trees, NOT the vendored converter lambdas; monolith lambdas entered the graph only at item-5 @`fe19d46ff` (07-22) | Resolved by 0.6.2's **manual live-ZIP byte read** (correct per Rule 22a, but manual). The doc-of-record carried the stale claim until then — 5th doc-of-record fix that night | **M** (coverage boundary) + the LD-0334 record class |
| RF-10 IAM claim stale at authoring | "Is this policy APPLIED, not just declared?" | comp-iam — structurally DESIRED-plane (documented Rule 22a limitation); live `get-role-policy` is the real oracle | The PRD was authored mid-apply carrying pre-apply state; corrected by a live-primitive read ~40min later | **M** (known instrument limit) + B (the read wasn't habitual at authoring time) |
| RF-14 vendor template dims unselected 4 months | "What does the vendor OFFER vs what do we SELECT?" | `dump_enriched_templates.py` — **existed, gate-clean, never run** | The purest trigger-layer exhibit: capability present, nothing made it fire. Item 8 (comp-vendor, scheduled diff) is the remediation | **B** (trigger absent) |
| RF-15 REVAMP had no REGISTRY row | "Do the records match the estate?" | comp-state (the BM25 drift linter, built for exactly this) | **comp-state: 0 runs in the entire jsonl era.** The drift sat until a manual grep at supersession | **B** (tool exists, not in anyone's flow) |

## Cross-cut findings

**CS1-1 (BEHAVIORAL-TRIGGER, the widest gap):** three independent shapes of *capability present,
nothing fires it* — comp-state 0 runs while a registry drift sat (RF-15); dump_enriched_templates
never run across 4 months of an empty column (RF-14); ~105 chosen tool runs total on the #1
project's hottest 9 days. This is the postmortem's trigger-layer finding, now MEASURED. The
remediations in flight (P3 doctrine, item-8 scheduled diff, the P1 commit-time gate) all share one
design property: **they move the tool from "available" to "fires at a moment of work."** The
next-wave candidates from this case study: comp-state on a closeout-class trigger (project
supersession/close = auto drift sweep), and pipescript-deployed on a deploy-completion trigger.

**CS1-2 (SEMANTIC-REGISTRATION):** the arc's tools mostly answered correctly *about what they were
told to watch* — the failures were denominators: unregistered constants (RF-1/5), a one-firm config
(RF-2), a graph that didn't cover monolith lambdas until 07-22 (RF-9). The semantic layer's real
weakness is not routing to the wrong tool; it is that **what a tool covers is invisible at query
time** — an agent asking a covered-sounding question gets a confident answer about a smaller world
(the coverage-denominator problem, in Andrew's "truly understanding state and dependencies" terms).
Candidate remediation: every tool answer carries its coverage statement (the mdpf-preflip-check /
item-7 denominator-printing convention, generalized as a standard — would route via the main-CTO
carve).

**CS1-3 (MECHANICAL-VINTAGE):** two arc defects were vintage-class (RF-10 DESIRED-vs-APPLIED; the
doc-of-record staleness family LD-0334) — consistent with this week's three same-class catches
(M2, census surfaces, verdict set). Mechanically the tools run; the recurring mechanical hazard is
*answering from the wrong vintage and not saying so*. comp-kuzu's provenance header is the good
pattern (praised in the NL corpus); most tools have no equivalent.

**CS1-4 (RAIL OVERRIDES = the demand signal for missing tools):** 597 DENYs (rising: 175 June →
421 July) split infra_grep 259 / aws_freshness 178 / aws_iam_inspect 85 / comp_which 38 /
deploy_verify 17 / route 15 / dynamodb 4. The 187 override reasons read as LEGITIMATE work the
comp surface doesn't cover: served-key EXISTENCE enumeration ("which artifacts exist per firm"),
earliest-partition/backfill-ceiling discovery, TF mechanism reads, and Rule-22a isolated positive
controls. Per CLAUDE.md's own rule (*a repeat override for one intent = a coverage gap → build the
tool*), the two repeat-intents are: (1) a **key/partition enumeration primitive** (most
aws_freshness overrides are not freshness questions at all), and (2) a **TF mechanism-read shape**
that comp-aws/comp-iam don't serve (259 infra_grep denials). These are Phase-3 build candidates
with measured demand attached.

## Inputs consumed
RF ledger (MDPF_3FIRMS_PRD §2.5 @ v1.17) · MDPF_POSTMORTEM_20260722 @`c75862249` ·
comp-tool-runs.jsonl joins (this doc's numbers) · rail log (17,409 lines / 597 DENY / 187
override-markers, estate-wide — per-case attribution deferred to the fanout results) · the NL
corpus extract (@`b8bf323ff`; the 10-agent structured fanout is running and will refine CS1-1/2
frequencies with per-quote provenance).
