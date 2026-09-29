# IRPT_BCKEND decomposition -- ROUND 23, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on row IRPT_BCKEND-S208)

Cut on row `IRPT_BCKEND-S208` (@ebd80df827, 2.0.0_SA_COO~Y): act 4's M leg names a branch that does not exist
(`irpt-mvp-m-20260922`); ~M's pre-relaunch work sits on ten `irpt-m-*` branches. The issuer measured them by CONTENT
at 15:3xZ (each branch's net diff applied reversed and forward against a CLOUD index): `irpt-m-r4-holdings` is an
ancestor of CLOUD, `irpt-m-s125-20260924` is PRESENT, `irpt-m-b01b-skip` and `irpt-m-s152-cloud` are ABSENT and apply
clean, and five (`irpt-m-cot-b1`, `irpt-m-cot-cash-line`, `irpt-m-cot-cash-line-act`, `irpt-m-s125-publish`,
`irpt-m-s152`) have DIVERGED from CLOUD, which re-cut much of that work. Rounds 20-22 ~M are issued, so this rides
round 23 (GATE (x)). It is a remediation of ~M's own branches, not an enrichment item.

| cell | item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-231` | A per-file census of every `irpt-m-*` branch: each file PRESENT / SUPERSEDED / CARRY / DROP with evidence, each branch WORLD-DONE / SUPERSEDED / DRAIN / RETIRE. Record only: no merge, no branch deletion, no code change | S208's remedy (2): the M leg is re-scoped to named branches before any drain; CLAUDE.md NEVER-2 (world-done closes SUPERSEDED, never re-executed) | none directly -- it decides whether act 4's M leg drains anything | LOCAL (reads git only) | none |

Chains: A = 231, worker slot `0.9.0_WK_IRPT_BCKEND~81` (S197: 1 + max(authors 80, issued_to 80, branches 61) = 81).
Direct act: one cell, LOCAL, record-only, well under the size floor.
