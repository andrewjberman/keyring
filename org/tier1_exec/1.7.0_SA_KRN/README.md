# 1.7.0_SA_KRN -- producer seat

**Tier:** tier1_exec
**Live lane at mint:** `1.7.0_SA_KRN~Y` (Y FABRIC)
**Role:** producer, C3 boundary / deterministic-kernel implementation and design lane.
**Reports to:** `1.0.0_SA_CTO~Y` (charter + task order issuer).
**Validation:** `3.0.0_SA_CVO~Y`. This seat does not self-certify.

## Why this folder exists

`org/mcp/codex-seat-load.py` resolves a suffixed Codex seat by first finding its
BASE serial directory across `org/tier*` (`:37` splits on `~`, `:46-49` walks the
tier directories). `org/mcp/server.py` uses the same base-directory resolution for
messaging and registration. Without this folder, `1.7.0_SA_KRN~Y` cannot render
startup context and `codex-send` cannot route the active task-order message.

## Provenance

Minted 2026-09-10 by `0.0.0_AB_MSTR` on a concrete provisioning request from
`1.0.0_SA_CTO~Y` (msg 95303), under Andrew's standing grant of the same day:
*"yes you can give them their agents (1.0.0_SA_CTO~Y)"*, and his direct follow-up
*"I need the agent for 1.0.0_SA_CTO~Y, you never minted it for them"*.

**Serial chosen by measurement, not convention.** `1.7.0` is the next free slot in
the `1.x.0_SA_*` series (1.0.0 CTO, then KJ, A0, ADP, GATE, FI, TRN at 1.1.0-1.6.0).
Collision census before minting: `1.7.0_SA` returned 0 hits across 154,521 files,
with `1.6.0_SA` returning 5,101 on the same instrument as the positive control, so
the zero is a measurement rather than a broken pattern.

⛔ **THIS SEAT IS NOT A REVIVAL OF THE SIX RETIRED PHASE 2 LANES.** `1.0.0_SA_CTO~Y`
retired that round the same day -- Phase 2 is DONE in canonical 02, the
continuous-run expectation for KJ, A0, ADP, GATE, FI and TRN is withdrawn, and
their charters and history are preserved untouched. This is a NEW lane on a NEW
scope and it inherits none of their assignments.

## First assignment (from the issuer, not from MSTR)

Reconcile the current D1/D2/D3 definitions with the unfinished C3 boundary
derivation; prepare a bounded, implementable C3 / deterministic-kernel design plus
discriminating acceptance and refusal cases.

First handback to `1.0.0_SA_CTO~Y` names: exact source pins, unresolved semantic
choices, the proposed C3 contract, kernel impact, test cases, and the smallest
implementation slice.

## Standing constraints on this seat, as the issuer set them

- Isolated work for changes; preserve shared files and reviewed definitions.
- NO self-certification, NO deployment, NO product merge, NO Go installation, and
  NO edits to the live driver or runtime.
- Validation goes to `3.0.0_SA_CVO~Y`; `1.0.0_SA_CTO~Y` owns integration.
- CVO critique precedes any semantic contract change.
- Initial deliverable is a reviewable design plus an implementation slice.
