# ADVI_COTBKF round 42 -- L9 grade

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~15:0xZ. Packet `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_42_DRAIN_END_20261009.md @0dd3bad9eb (msg 3540)`. Row D2-S68.

| criterion | verdict | evidence |
|---|---|---|
| CB42ap1-AC2: exactly one registry file, read from the writer's own directory, with no fallback path; absent is never the own firm; the removed check was unreachable | MET | The diff f30ad987a6..1111ec9b9b sets `REGISTRY_FILE = 'scopes.json'`, read at `Path(__file__).resolve().parent`. It removes the `opal_naming` and repo-registry search, and a missing or bad file returns `(None, reason)`, so nothing falls back. The absent rule is unchanged from round 40. The removed check filtered on `t1_transaction_observed`, which the writer never emits. Both served `code/gold/` keys equal the repo bytes (this seat's read: 3ac0a502..., 13947f7f...) |

**Note:** repo-file inputs resolve their pipeline tree from `Path(__file__).parents[3]`, which is the repo root only when the script runs from the
repo. From `code/gold/` it resolves elsewhere and stamps `absent`: safe, but NOT-CLEAN for those inputs.
