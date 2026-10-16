# IRPT_ANLREQ round 32, workstream ~G (ENGINE) -- decomposition: the irpt-status Lambda package for the failure-code release, built

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** C-HOP-FAILURE (PRD v0.21), CTO msgs 8907 and 8971. Round 30 merged the reader (`AR-g-111`, `766ec706ee`); round 31 re-pinned the two staged rows of `irpt-status` (`AR-g-113`, merged `28734e0985`). The issuer's trial build of the tooling commit `90b69dcb12`: `irpt-status`, 49 members, delta against the r33 build exactly `durable_job.py`, `owned_status.py`, `status.py`, CodeSha256 `+TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A=`, verifier `ar_g115_checks.py` OK.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The build is a cell of its own, like `AR-g-103`:** BUILD ONLY at the fixed pin `90b69dcb12cdfedc786966ab33d034bf14229396` (the tooling commit, which carries every merged source change), twice, byte-identical; the verifier recomputes everything and requires the CodeSha256 to equal the issuer's own trial build.
- **The baseline is the r33 build pin `927337a741`,** not the map's `last_deployed_commit` for `irpt-status` (a later test-only commit AQ2's map record wrote), because the live package is the r33 build.
- **Release shape:** this build, then the resident r35 (the hop_failure writers: its own build cell and tooling), then ONE packet (CTO decides whether the commentary role's grant, `~T2`'s, rides in it), `irpt-status` applied first, then the resident, so the reader exists before any writer writes.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-115` | the `irpt-status` zip in a stage folder outside the repo and the record `R35L_BUILD.json` | the worker's folder, the order, the channel file | WORLD (floor of an infrastructure path; nothing deployed, no AWS call) |

## Edges and chains

- ONE chain. Depends on `AR-g-111` and `AR-g-113` (merged). Feeds the r35 packet.

## Four-postulate record

(i) Domain: one Lambda package of 49 members. (ii) One pin, one baseline, one verifier. (iii) One intent. (iv) What this cut does NOT move: any deployed byte, the Terraform root, the resident.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 255).
