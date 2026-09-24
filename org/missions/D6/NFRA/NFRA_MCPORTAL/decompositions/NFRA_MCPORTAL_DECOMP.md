# NFRA_MCPORTAL -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD

```json
{
 "project": "NFRA_MCPORTAL",
 "directive": "D6",
 "macro": "NFRA",
 "fabric": "site-z",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@87b310f4c2",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO~O (current)", "brief": "SIGNED (auto) CRO-authored brief"},
 "author": "2.0.0_SA_COO~O",
 "round": 1,
 "rectangle": "the FWD-1 thread's hops (PRD v0.2 Canonical handoff steps 1-5)",
 "cells": 7,
 "chains": 3,
 "join_cells": 1,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~O`. **Input:** PRD v0.2 @`87b310f4c2`, ADMITTED by `prd-signoff.py status`. **Frozen at the cut.**
A cell that looks wrong mid-round is a surprise row, never an edit.

**Rulings reaching every cell:**
- Only Andrew uses the dashboard, checked SERVER-SIDE on every page and every write (C2). `/sprint` stays open to any
  signed-in Opal account.
- The gateway can never grant itself access: grant writes go through a separate writer that verifies Andrew itself (C4).
- Every write is audited and revertible (C5).
- Read when opened, never an alert (C8).
- Every new resource name is `lib/opal_naming.py name()` output. A builder refusal is a missing registry row to add,
  never a hand-typed name (Rule 30).
- Round 1 is built on the gateway's CURRENT path, `infra/aws/ec2/opal-gateway/` (handoff; NFRA_OPALAI's G-MOVE carries
  it later).
- No push by any worker (G-PUSH is `0.0.0_AB_MSTR~Z` on Andrew's word). No vendor call.

**Cross-project sequencing with NFRA_OPALAI round 1 (one issuer holds both):**
- (a) `MP-w-1` writes `.gitmodules`, which `OA-w-1` also writes, so `MP-w-1` spawns only after `OA-w-1` has merged
  and its nested provisioning exists.
- (b) The gateway cells here (`MP-t-1`, `MP-t-4`) touch no file `OA-t-5` writes (`app/tools.py`,
  `app/data_entitlement.py`). But `OA-t-6` deploys the gateway at HEAD and REFUSES to ship another project's
  unreleased change, so this round's gateway merges are held until `OA-t-6`'s deploy entry is CLOSED.
- (c) `MP-t-6` edits `deploy-to-ec2.sh` after `OA-t-6` has used it.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  handoff steps (v0.2 "Canonical handoff") ................................................ 5
    1 repo + shell (S1, G-REPO)   2 owner gate + serving (S2, S3)   3 grant writer + A1n (S4)
    4 Entitlements tab over the DATA grant + audit rows (S5, S7 minimum)   5 one live change followed (A1)
  minus step 5: the COO's ONE REAL RUN at close, not a cell ................................ -1
  step 3 split by act: build (LOCAL-shaped code, WORLD floor) / apply (WORLD) .............. +1
  step 4 split by repo: gateway handlers / mcportal pages ................................... +1
  plus the deploy that makes steps 2 and 4 live on the served host ......................... +1
  -----------------------------------------------------------------------------------------------
  CELLS IN ROUND 1 ................................................................................ 7
```

**The unscoped control.** Read from the 15-row manifest: S1 -> MP-w-1; S2 + S3 -> MP-t-1 (+ MP-t-6 live); S4 ->
MP-t-2 + MP-t-3; S5 -> MP-t-4 + MP-t-5; S7 (the minimum FWD-1's history needs) -> MP-t-4 + MP-t-5. **Outside round 1 by
the handoff's own words:** S6 (G-OPLGTW), S8-S15 (the enrichment rounds, in Andrew's page order), and the rest of S7
(revert of every kind). Read from the acceptance matrix: A1 and A1n are this round's; A2 is partly served (the gate
is built and its negative arm is exercised in tests; the second signed-in account is the close run's); A3-A13 are
enrichment. **G-REPO is SATISFIED:** `Opal-Capital/mcportal` exists, private, `DEV` = `PROD` = `fa1ff9693b` (README
only), measured by `git ls-remote` at the cut and reported by `0.0.0_AB_MSTR~Z` (created 2026-09-24T21:25Z).

**Status vocabulary:** `MEASURED` (evidence in hand at the cut, instrument named), `DECLARED` (the PRD or a ruling
asserts it; not independently measured here), `NOT-EVALUATED`, or `N/A`.

---

## 2. THE RECTANGLE -- 7 cells

Measured on site Z at CLOUD HEAD, 2026-09-24 ~22:1xZ, unless stated.

| cell | hop | what is built | current state | existing work carried | risk |
|---|---|---|---|---|---|
| `MP-w-1` | 1: S1 | `.gitmodules` maps `mcportal` (`https://github.com/Opal-Capital/mcportal.git`, branch `DEV`) with the gitlink at `fa1ff9693b`; in the nested repo, a React + Vite + TypeScript + bun scaffold whose shell's sidebar lists the pages in the brief's order, on `portal/DESIGN.md`'s law; `bun run build` emits a static bundle | `MEASURED`: remote is a README only; no `mcportal` path in the parent | the portal's toolchain and design law (`portal/DESIGN.md`) | LOCAL |
| `MP-t-1` | 2: S2 + S3 | `app/owner_gate.py` (new): a dashboard-owner list of its OWN (config `DASHBOARD_OWNER_EMAILS`, Andrew's address only; the gateway refuses to boot if it holds any other entry; NOT `MASTER_ADMIN_EMAILS`), exact-matched against the identity from the ALB-signed `x-amzn-oidc-data` header verified by the existing `_alb_oidc_identity` (`app/identity.py:50-62`), on every `/` page request and every `/api/admin/*` handler; `app/admin_api.py` (new): the admin router, first route `GET /api/admin/whoami`; `server.py`: the static bundle mounted at `/` and the admin router, with `/sprint` and every existing route untouched | `MEASURED`: `/` is unrouted; the ALB default action sends every non-bypassed path through Microsoft sign-in (`alb.tf:210`, "the future GUI path"); `/sprint` has its own handlers (`server.py:866-869`) | `identity.py` `_alb_oidc_identity`, `GuardMiddleware` | WORLD (floor: gateway code under `infra/`) |
| `MP-t-2` | 3: S4 build | the grant-writer function: a `mcportal` row in `infra/logic/registry/systems.json` so `name('mcportal', None, 'grant-writer', 'lambda')` resolves; its source under `infra/aws/lambda/` (per the lambda source map); it carries the operator CLI's path (`ops/schwab_entitlement_admin.py` `prepare`/`activate`/`revoke`, whose writes land with an `operator_audit` in ONE transaction); it verifies `x-amzn-oidc-data` ITSELF against the regional ELB key, exact-matches Andrew's Entra oid from its OWN config, refuses a header older than a short window, and refuses before any store call; its Terraform (function, execution role scoped to the `POLICY#` partition like `opal-gateway-access-admin`, and ONE `lambda:InvokeFunction` grant for the gateway role) | `MEASURED`: `name()` refuses `mcportal` ("not a systems.json key"); the operator role's trust `ArnNotEquals aws:PrincipalArn = gateway role` (`schwab_access_state.tf:125-133`) and the runtime write guard (`access_state.py:14-16`) stand | `schwab_entitlement_admin.py`, `access_state.operator_transact`, `data_entitlement.operator_audit_op` | WORLD (floor) |
| `MP-t-3` | 3: S4 apply | `safe-apply` of `MP-t-2`'s Terraform under a C10 ledger entry (blast radius: one function, one role, one invoke grant); then the LIVE negative arms (A1n): the writer invoked with no owner header, with a non-owner header, and with a stale header, each refused before any store call; and `sts:AssumeRole` from the gateway role on the operator role simulated DENIED | `NOT-EVALUATED`: Andrew's Entra oid (the writer's owner config) is read by the cell from an existing record, or its absence is a BLOCKING row routed to Andrew | the existing trust condition and `LeadingKeys` guard | WORLD |
| `MP-t-4` | 4: S5 + S7 backend | `app/admin_grants.py` (new): `GET /api/admin/grants/{tid}/{oid}` (profile + active data grant, read through the existing store), `POST .../narrow` and `.../widen` (invoke the writer with the request's forwarded owner header; the gateway itself writes nothing), `GET /api/admin/changes` (the writer's audit records, newest first, before and after) | `N/A` (new) | the store's read path, `data_entitlement` scope dimensions | WORLD (floor) |
| `MP-t-5` | 4: S5 + S7 pages | in `mcportal`: the MCP Server -> Entitlements tab (pick a person, show their data grant, narrow or widen it through the admin API) and Recent Changes (newest first, before and after), against a typed API client | `N/A` (new) | the portal's grant vocabulary and design law | LOCAL |
| `MP-t-6` | 2+4 live | the gateway deploy that also ships the `mcportal` bundle: `deploy-to-ec2.sh` builds `mcportal` at its pinned commit and adds the bundle to the artifact; `EC2_MANIFEST.json` records the `mcportal` commit beside the workspace commit (C3); NEVER-2 entry; the live reads of health, the bundle's `index.html` md5 over SSM, and the boot owner-list check | `NOT-EVALUATED`: the deployed commit at the time (after `OA-t-6`) | `deploy-to-ec2.sh`, `safe-ec2-deploy.sh` | WORLD |

**Load-bearing `DECLARED` / `NOT-EVALUATED` rows, stated:** (a) the runtime role's READ of `POLICY#` records for
`GET /api/admin/grants` is DECLARED by the store's design (writes are guarded, reads are not named as refused); MP-t-4
measures it. (b) Andrew's Entra oid source is NOT-EVALUATED (MP-t-3). (c) The brief's sidebar order is read by MP-w-1
from the brief at its pin.

---

## 3. THE CELLS -- 7 (round 1)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1: prefix `MP`, axis `t` = thread hop, `w` = wiring.

| cell | serves | writes | reads (never writes) |
|---|---|---|---|
| `MP-w-1` | FWD-3 (shell) | `.gitmodules`, `mcportal` (gitlink), `mcportal/**` (nested) | `portal/DESIGN.md`, the brief at `8d1f5c362b` |
| `MP-t-1` | FWD-2 | `infra/aws/ec2/opal-gateway/app/owner_gate.py`, `.../app/admin_api.py`, `.../app/server.py`, `.../app/config.py`, `.../tests/test_owner_gate.py` | `app/identity.py`, `app/sprint_view.py`, `app/tier.py` |
| `MP-t-2` | FWD-1 | `infra/logic/registry/systems.json` (the `mcportal` row), `infra/aws/lambda/<name>/**` (the writer), `infra/aws/lambda/ci/lambda-source-map.json` (its row), `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`, the writer's tests | `ops/schwab_entitlement_admin.py`, `app/access_state.py`, `app/data_entitlement.py`, `app/identity.py`, `schwab_access_state.tf` |
| `MP-t-3` | FWD-1 (A1n) | `org/critical_paths/change_management/<entry>.md`, `org/critical_paths/.open_deploys/<slug>.json`, the applied plane (WORLD) | `mcportal_grant_writer.tf` |
| `MP-t-4` | FWD-1 | `infra/aws/ec2/opal-gateway/app/admin_grants.py`, `.../tests/test_admin_grants.py` | `app/access_state.py`, `app/data_entitlement.py`, `app/admin_api.py` |
| `MP-t-5` | FWD-1, FWD-4 (min) | `mcportal/src/pages/mcp-server/entitlements/**`, `mcportal/src/pages/recent-changes/**`, `mcportal/src/api/admin.ts` | the admin API's route shapes (fixed below) |
| `MP-t-6` | FWD-1, FWD-2 (live) | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, `infra/aws/ec2/EC2_MANIFEST.json`, the ledger entry + sentinel, the served host (WORLD) | `safe-ec2-deploy.sh` |

**Fixed names across cells:** the routes `GET /api/admin/whoami`, `GET /api/admin/grants/{tid}/{oid}`,
`POST /api/admin/grants/{tid}/{oid}/narrow`, `POST /api/admin/grants/{tid}/{oid}/widen`, `GET /api/admin/changes`; the
config key `DASHBOARD_OWNER_EMAILS`; the nested repo path `mcportal/`; the bundle dir `mcportal/dist/`.
**Hookups (belong to no cell; the issuer adds them at the merge):** `MP-t-4`'s router registration line in
`app/admin_api.py`, and `MP-t-5`'s route entries in the shell's router file.

---

## 4. PLACEMENT AXIS

**Every cell executes on SITE Z.** Served by `0.9.0_WK_NFRA_MCPORTAL~<n>`. The mcportal cells get a nested
`mcportal` worktree through `wk-provision.sh --nested mcportal=<ref>` (OA-w-1's generalisation), after MP-w-1 has
merged and the main tree's `mcportal` is initialised.

---

## 5. DEPENDENCY EDGES AND CHAINS

```
  chain A   MP-w-1 --> MP-t-5                 the repo, then the pages in it
  chain B   MP-t-1 --> MP-t-4                 the gate and router, then the grant handlers behind them
  chain C   MP-t-2 --> MP-t-3                 the writer built, then applied (A1n live)
  JOIN      {MP-t-5, MP-t-4, MP-t-3} --> MP-t-6   the deploy ships the gateway handlers and the bundle once all three land
```

**CHAINS: M = 3** (A, B and C are pairwise disjoint in write set), plus the join cell. Following the NFRA_OPALAI v1 and
DSGN_IRPTV1 v2 precedent, chains are counted without the join. **Fan-out:** `N = 3 of M = 3 chains, cap 8; join_cells: 1
(MP-t-6)`. At the cut, spawn `~2` (MP-t-1, then MP-t-4) and `~3` (MP-t-2, then MP-t-3). Spawn `~1` (MP-w-1, then MP-t-5)
once OA-w-1 has merged (sequencing (a)). Spawn `~4` (MP-t-6) when A, B and C have drained and `OA-t-6` is closed.

---

## 6. BATTERY DISPOSITION (a thread round)

- **`comp-adversary` -- DECLARED-NOT-APPLICABLE:** thread round.
- **`comp-schedule` -- DECLARED-NOT-APPLICABLE:** thread round. No cell arms a cron, alarm, monitor or cadence; the
  nightly rollups are enrichment.
- **`comp-iam` -- RUN, because the thread touches IAM (MP-t-2/MP-t-3), and its instrument is the cell's own:** MP-t-3's
  live arm simulates `sts:AssumeRole` from the gateway role on the operator role and requires DENIED. It also reads the
  gateway role's new grant back as `lambda:InvokeFunction` on exactly one function ARN. Blindness stated: this lens
  sees the two roles and the one function, not the rest of the account.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE.** Five handoff steps, minus the close run, plus three splits by act or repo, gives seven cells. This is
falsified against the 15-row manifest and the 14-row acceptance matrix (section 1). No file has two writers; the hookups
belong to no cell.

**(ii) SAME GRAIN.** Each cell is one hop adapter, graded by its built behaviour, a seam probe against its real
neighbour where reachable (the naming builder, the live store, the live IAM plane, the served host), and at most one
further check.

**(iii) INTENT COHERENCE.** One axis: Andrew narrows one colleague's data grant from his own dashboard and the
colleague's next answer obeys it. Out of scope: every other page, the tier move (S6), user management, cost, and infosec.

**(iv) STATE COHERENCE -- what each remedy does NOT move.**
- `MP-w-1` adds a repo mapping; it does NOT move portal or opal_ai.
- `MP-t-1` adds a gate on `/` and `/api/admin/*`. It does NOT move `/sprint`, `/mcp`, the OAuth paths or any
  existing route's guard, and `MASTER_ADMIN_EMAILS` is untouched.
- `MP-t-2` builds and names. It creates no resource.
- `MP-t-3` creates one function, one role and one invoke grant. It does NOT move the operator role's trust condition,
  the `LeadingKeys` guard or the operator CLI.
- `MP-t-4` adds handlers. The gateway writes no grant itself.
- `MP-t-5` adds pages. It serves nothing until deployed.
- `MP-t-6` ships. It does NOT change Terraform, the host or its role.

---

## 8. GATES AND THE CLOSE RUN

- **G-REPO: SATISFIED** (section 1).
- **G-PUSH:** `mcportal` DEV/PROD pushes. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's word. The bundle ships from the pinned
  commit; the push records it on the remote.
- **G-LEDGER:** MP-t-3's and MP-t-6's entries, each the acting worker's own.
- **G-OWNER-OID (only if MP-t-3 cannot find it):** Andrew's Entra object id for the writer's owner config. Holder: Andrew.
- **The close run (A1 + A2's live arm):** Andrew, signed in at `mcp.opalinvest.dev`, narrows one colleague's data grant.
  The colleague's next MCP call answers within the new limit, and widening it back works the same way. Both changes
  show in Recent Changes, and a second signed-in Opal account is refused on the dashboard while `/sprint` still serves
  it. Artifact: `deliverables/2.0.0_SA_COO~O/round1/`.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. No cell has been exercised; every target state is a specification.
2. Andrew's Entra oid, the runtime role's POLICY read and the deployed commit at MP-t-6's time are measured by their
   cells.
3. Revert of every write kind (A4), the Home verdict (A3) and every other page are enrichment.
4. The `mcportal` DEV/PROD push and the gitlink bump that names it are the close run's, under G-PUSH.
