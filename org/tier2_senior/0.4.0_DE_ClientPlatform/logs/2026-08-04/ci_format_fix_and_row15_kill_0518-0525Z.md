# CI ack-format fix + kill-list row 15 — 0518-0525Z

**archetype:** IMPLEMENT

## What happened

**1. Surface-check gate RED on 7d544d27 (DT 051928Z, CI run 30880062845).** Mechanism
DT-grounded and exercised both ways: my ack was real and audited but the commit-message line
read 'SURFACE_ACK justification:' where the CI parser requires the literal 'SURFACE_ACK:'
prefix — a format seam, not an authorization gap. Fix exactly as DT proposed: empty commit
`0576ef22` restating the full authorization chain in canonical format, pre-verified against
the CI's own sed before reporting. CTO 052138Z: instance correct, class fix (auto-append with
the CI sed as self-check, my incident as the required failing fixture) already ratified +
routed to DT in parallel. Promote resumes on DT's gate-run verification post-push.

**2. Kill-list row 15 (~F 051830Z, COO dead-consumer GO 042634Z, DE-lane).** Portal DEV
`d32f5a52`: `getMdpfAggregateAUATimeSeries` KILLED at both layers (portal-proxy root +
aum.ts wrapper) — route measured 403 on a nonexistent post-flip key (~F @297db6f6bf), zero
callers (my @b48634789a sweep); the never-built `/aum/aggregate-mdpf` dependency note died
with it; all four falsified /json/-rewrite comment blocks (F4) corrected to deployed
router-v6 truth; firmId enumerations updated to the 4-scope canonical set. Executed
same-hour ("whenever your pod next touches" + drive imperative + context already loaded).
SEV1 acked in BOTH grammars (env var + literal CI line — the seam lesson applied same-hour),
audited, self-checked against the CI parser in the commit command itself.

## Compiler Tools

| Tool | Result |
|---|---|
| tsc -b | clean both commits |
| provenance-guard | OK |
| eslint (touched files) | no errors |
| comp-surface-check (pre-commit) | SEV1 block-with-ack on d32f5a52 — acked (dead-code/comments-only justification, GO chain cited), audited |
| CI parser self-check (`sed -n 's/^[[:space:]]*SURFACE_ACK:...'`) | run in-command on both commits — extracts non-empty (the fixture-grade lesson from 0576ef22 applied forward) |

## State

Portal DEV local: `7d544d27` (canonical map + T2/T3) → `0576ef22` (ack format) →
`d32f5a52` (row 15). MSTR pushes; DT verifies the gate run; promote sequencing at CTO/MSTR.
Working tree: ModelPortfolios.tsx dirty with EXACTLY the held T1 blocks (patch banked).
Seat gates unchanged: Andrew T1 word · DS served-meta ping · emitter landing · promote call.
