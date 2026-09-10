# CRO Ratification — PREQ-04 normalization `136531a` and `$02check` repairs

Recorded by: `1.0.0_SA_CTO~Y`

Ratifying seat: `4.0.0_SA_CRO~Y`, personally verified by Andrew in the current session

Received: `2026-09-09T23:45:23Z`

Source inbox message:
`20260909T234523Z_4.0.0_SA_CRO_Y_CRO_PASS__136531a_normalization_and_02ch.md`

## Disposition

**PASS — zero blocking amendments** on exact docs commit
`136531afc6cffb24cb2d931c351e45015ec3e310` and the two local `$02check`
temporal repairs.

CRO ratification receipt:

- commit: `169d042001622015e5a4b1299675a67aa7253003`;
- path: `plan/integration_proposals/CROY_RATIFICATION_PREQ04_NORMALIZATION_136531A_02CHECK_20260909.md`;
- bytes: `7364`;
- SHA256: `5d4fc3e54c5880da6f42250d40edc8a7d9dc15a8df069e0034fa0c373ddd96ea`.

## Independently reproduced evidence

- Source and normalized hashes and ancestry match.
- Against verified generation 236, all 33 previous typed-index rows are a
  byte-exact prefix and one 447-byte PASS row was appended; the prior AMEND
  remains present.
- Only the typed index and manifest changed among the 172 archived Fabric
  entries.
- Fabric generation 237 reproduces at chain head
  `37054306989b3f8e66bf3eb4317eab14282c170f9a8b56a1b6f0f63eb339c6b0`.
- Fabric verifier negative suite: `61/61`.
- Snapshot refusal suite: `4/4`.
- ASCII/scope suite: `13/13`.
- `$02check` regression suite: `22/22`; CRO independent temporal controls:
  `15/15`.
- Product `scratchpad_tmp/main` is clean at
  `c71e7300080c80bf3f9a44c1f3d094c3485e58ca`.
- Phase 2 remains `DONE`; the latest bounded Phase 3 cut remains certified;
  no Phase 3 aggregate exit is claimed.

Critical qualification: docs commit `136531a` carries forward older committed
Fabric state because its Git parent predates the verified shared Fabric state.
The append-only generation-236-to-237 comparison above is the authoritative
bounded-delta evidence. The helper repairs are accepted at SHA256
`05E0BA387C0ACC39BEA0CEF346FC31D6A526FF2D21BBC7041013079D21F14F28`
and regression-file SHA256
`2ECFD10A88D70026DB3F56367F915F8DDE24422C3870C304ACE99F53D8386BB4`;
they are not claimed to be part of docs commit `136531a`.

## Preserved boundary and next motion

The next bounded motion is to prepare the next exact local
prerequisite/evidence boundary under existing authority. No missing pin or
project selection is inferred. `CANDIDATE / NON-EXECUTABLE / NO GO /
UNSUPPLIED_NO_PROJECT_SELECTED` remains in force, together with every AWS,
execution, deployment, and push hold.
