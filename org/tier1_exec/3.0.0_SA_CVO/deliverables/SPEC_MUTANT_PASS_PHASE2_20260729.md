# PHASE-2 SPEC: the functional MUTANT PASS — four decision-gating tools + one full-chain representative

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~19:00Z · **archetype:** IMPLEMENT(spec-only)
**Andrew-approved (~18:55Z):** a compilation-step addition — each fixture becomes a standing
`--self-test` regression. **Substrate ruling (Andrew ~18:58Z, this spec's spine): injection at GIT
ACTUAL, always; the derived surface (kuzu / a tool's own index) is the ASSERTION layer, never the
injection origin.** Reason, measured today: every blindness found lived in EXTRACTION (dynamic
keys, unmapped methods, the mdpf layer tuple, two suffix-blind globs); a derived-layer injection
skips the parser and builds a battery that structurally cannot fail on the failure class that
actually occurs.

## Purpose (one line)

The denominator walk proved the tools SAY what they looked at; the mutant pass proves their
answers CAN MOVE — "when it says safe, could it have said otherwise?" — for exactly the tools
whose answers gate decisions.

## Conventions (bind every fixture)

- **Injection at git actual**: a real change in a real file, traveling the tool's OWN refresh
  chain (comp-build / rules load / config eval / kuzu derive). Never a synthetic row in an index
  or graph.
- **Committed synthetic fixtures** in the tool-adjacent `test_fixtures/` home (never live-source
  edits in the shared worktree — tonight's discard incident is the citation), runs under
  `COMP_SYNTHETIC_FIXTURE=1` (telemetry-excludable, existing convention).
- **Scored on OUTPUT, never rc** (harness-rc law) — though rc is ALSO asserted where the tool has
  a verdict-bearing rc contract.
- **Each mutant asserts BOTH directions** (grow AND shrink / block AND pass): a one-directional
  mutant can be satisfied by a constant.
- **Negative control per battery**: an untouched fixture must NOT move the answer (no manufactured
  findings).
- One-time build; standing regression thereafter (rides `--self-test` where the tool has one;
  gains one where it doesn't).

## M-1 comp-blast (chain: git actual → comp-build index → trace graph → radius)

Fixture: `mutant_blast_target()` + `mutant_blast_caller()` in a fixture source file **confirmed
inside comp-build's scan roots** (if the roots exclude fixture paths, the builder declares the
root-extension explicitly — an unscanned fixture passing vacuously is the first thing to check).
Battery: (a) baseline — after comp-build, target's radius includes caller; (b) GROW — add a second
caller file, re-build, radius gains it; (c) SHRINK — remove it, re-build, radius loses it;
(d) NEGATIVE — an uncalled fixture function reports an empty/sole radius. **This is the collision-
consequence tool (parallel-wave decomposition reads it) — M-1 lands first.**

## M-2 comp-surface-check (chain: git actual changed-set → critical-surface rules → verdict)

Battery: (a) a fixture file matching a critical-surface rule → advisory mode names it, portal-side
mode BLOCKS (rc=2 asserted there — that rc is contractual); (b) a non-critical fixture passes;
(c) **the population mutant** — extend the rules list with a synthetic rule, assert the two-sided
denominator line (lands with ~C's walk fix) counts it: this is the only test that catches a
silently-shrunken rules list, the exact hazard the half-declared output hides today.

## M-3 comp-validate (chain: config + artifact → check eval → PASS/ADVISORY/FAIL)

Battery: (a) a fixture artifact VIOLATING a declared check in a fixture config → FAIL/WARN named;
(b) the compliant twin → PASS; (c) the zero-config case → `NO_CONFIG` (never a safe-reading
output) — asserting the existing law holds under exercise, not just in prose.

## M-4 comp-transform (chain: portal component source → schema-check vs envelope)

Battery: (a) a fixture component reading a field ABSENT from its envelope → MISSING reported;
(b) add the field → clears. The envelope side is the design decision the builder owns: a fixture
envelope file is acceptable IF the injection point into the tool's envelope resolution is declared
(not a hand-fed bypass of it) — otherwise the live-S3 read makes this the one battery with an AWS
dependency; builder states which and why.

## M-5 the full-chain representative (chain: git actual → kuzu derive → graph query)

ONE fixture, not per-tool (the derive tail is minutes-class, now carded): a fixture source file
with a static S3 write → run the derive → **two-point assertion**: (1) the edge EXISTS in kuzu
post-derive (localizes extraction failures), (2) a consuming query's answer reflects it (localizes
traversal failures). One mutant, fault attributable to the correct half. Sequenced AFTER W1 steps
2-3 land (it can then double as their acceptance fixture — one build, two payoffs).

## Ownership + order

Builder: 1.0.0_SA_CTO~C (the compilation-step lane), sequenced behind WS1/WS3 at their discretion
except M-1 (highest consequence, no dependency on W1). Verifier: me, against this spec — and per
the day's lesson, my verification includes running each battery with MY OWN fixture variant, not
only theirs (a battery the builder wrote passing 8/8 did not catch the builder's own inversion
defect today; C7/C8 exist because reading live output did).

— 3.0.0_SA_CVO
