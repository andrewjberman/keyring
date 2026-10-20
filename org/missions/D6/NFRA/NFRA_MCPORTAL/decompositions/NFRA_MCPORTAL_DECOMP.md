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
| `MP-t-2` | FWD-1 | `infra/logic/registry/systems.json` (the `mcportal` row), `infra/aws/lambda/mcportal/<the builder name>/**` (the writer), `infra/aws/lambda/ci/lambda-source-map.json` (its row), `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`, the writer's tests | `ops/schwab_entitlement_admin.py`, `app/access_state.py`, `app/data_entitlement.py`, `app/identity.py`, `schwab_access_state.tf` |
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

---

# ROUND 2 -- THE ENRICHMENT CUT (L5, v2)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v2",
 "step": 5,
 "round": 2,
 "input": "org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round1.md@667f442b8a (section 4, E1-E6)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@87b310f4c2",
 "author": "2.0.0_SA_COO~O",
 "cells": 6,
 "chains": 3,
 "join_cells": 2,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~O`. **Input:** the CTO's round-1 analysis @667f442b8a, section 4, cut in ONE issuance. Round 1
(sections 1-9 above) stays frozen as its own record.

## R2.1 THE CELLS -- 6

| Cell | From | Builds | Write surface | Risk |
|---|---|---|---|---|
| `MP-b-1` | E2 (R-1, R-3) | the grant writer's STAGED BUILD: `build_package.py` stages `lambda_function.py` plus the import closure of `app.access_state` and `ops.schwab_entitlement_admin`, copied from the gateway tree at the same commit; the package root resolved from the package itself (no `parents[N]`); the Terraform archive built over the staged directory; a layer SPEC for PyJWT + cryptography (a `lambda-layer-map.json` row and a pinned `requirements.txt`, built later by MP-a-1) | `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/**`, `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`, `infra/aws/lambda/ci/lambda-layer-map.json`, `infra/aws/lambda/layers/mcportal-grant-writer-deps/requirements.txt` | WORLD (infra floor) |
| `MP-b-2` | R-2, R-4 (writer side) | the owner key: `MCPORTAL_OWNER_KEY_CLAIM` in `oid`/`sub` plus `MCPORTAL_OWNER_KEY`; freshness on `iat` when present, else on `exp`; a header with neither owner claim refuses. The writer's own record: one item per WRITTEN or REFUSED outcome in `mcportal-grant-changes-table` (name() output). Terraform: that table, the writer's PutItem-only grant on it, and the gateway role's read-only grant | `lambda_function.py`, its `tests/`, `mcportal_grant_writer.tf` | WORLD (infra floor) |
| `MP-g-1` | E1 capture, E6 read | the owner gate logs the verified header's claim KEYS once per process, with only the `oid`/`sub`/`iat` values (the owner's own identifiers) printed; `GET /api/admin/whoami` returns them to the owner; `GET /api/admin/changes` with no parameters reads the writer's table across principals, newest first | `app/owner_gate.py`, `app/admin_api.py`, `app/admin_grants.py`, `app/config.py`, `tests/test_admin_round2.py` | WORLD (infra floor) |
| `MP-p-1` | E5 (R-5), E6 client | the typed client refuses a non-JSON response by content type with a plain reason; Recent Changes asks for every principal | `mcportal/src/api/admin.ts`, `mcportal/src/pages/recent-changes/**`, `mcportal/src/api/*.test.ts` | LOCAL |
| `MP-d-1` | E4 | the NARROW gateway release: cut at the deployed `f1f0fc6780`, plus ONLY NFRA_MCPORTAL's gateway commits (MP-t-1 `98ad7e253f`, MP-t-4 `17b7e01c0f`, MP-g-1's); the dashboard bundle built from `mcportal`; the host `.env` gains `DASHBOARD_OWNER_EMAILS`, `GRANT_WRITER_FUNCTION_NAME=mcportal-grant-writer-lambda` and `MCPORTAL_CHANGES_TABLE=mcportal-grant-changes-table` (both fail closed until MP-a-1 lands) | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-a-1` | E3 (R-2 branch pick) | the writer's APPLY: read the gateway's claim-keys line (after G-HDR), pick R-2's branch and set the owner key from it; build the layer from its pinned requirements (after G-PYPI); `safe-apply` the writer, its table and both grants; a live refusal run | apply only; ledger paths | WORLD |

## R2.2 DEPENDENCY EDGES AND CHAINS

```
chain A   MP-b-1 --> MP-b-2 --> MP-a-1     one slot: b-1 and b-2 both edit lambda_function.py
chain B   MP-g-1 --> MP-d-1                d-1 releases g-1's commits
chain C   MP-p-1 --> MP-d-1                d-1 builds the bundle p-1 changes
joins     MP-d-1 (B + C); MP-a-1 (A + d-1 + G-HDR [+ G-C4 on an absent-claim branch] + G-PYPI)
```

**Fan-out:** `N = 3 of M = 3 chains, cap 8; root cells: 3 (MP-b-1, MP-g-1, MP-p-1)`. Slots: `~1` b-1, then b-2, then
a-1; `~2` g-1, then d-1; `~3` p-1.

## R2.3 PLACEMENT AND ISSUER RULINGS

- **E1's measurement is not a read of the deployed gateway.** No route at `f1f0fc6780` records a verified header's
  claims, and a packet capture on the box would sweep up colleagues' bearer tokens. So E1 splits:
  - the CAPTURE is built (MP-g-1) and released (MP-d-1);
  - the MEASUREMENT is one ALB-authenticated request by Andrew (G-HDR);
  - the branch PICK is MP-a-1's first step.
- **R-2's two branches are both built in MP-b-2 and selected by configuration,** so no cell waits on the measurement to
  be written.
- **The layer is specified in MP-b-1 and built in MP-a-1.** Its pinned manylinux wheels come from PyPI through the
  estate's layer precedent (`lambda-layer-map.json`, `irpt-common`). That is egress off Opal infrastructure, held on
  Andrew's word (G-PYPI). MP-b-1's in-zip proofs need no wheel: the refusal it runs returns before any JWT decode, and
  the local interpreter supplies PyJWT for the import.
- **Rows carried into round 2:** C-S10 (R-2), W3-S3 (R-3), W2-S1 (R-4), C-S11 (R-5). W1-S1 is the CTO's own act (R-6),
  and it binds no cell.

## R2.4 GATES AND THE CLOSE RUN

- **G-HDR:** after MP-d-1 is live, Andrew opens the dashboard once in his own browser. Holder: Andrew. It produces the
  claim-keys line MP-a-1 reads.
- **G-C4 (conditional):** if the line shows `oid` or `iat` absent, the CTO's C4 wording addendum is signed by
  `3.0.0_SA_CVO~O` before MP-a-1's apply (R-2).
- **G-PYPI:** Andrew's word for the one pinned-wheel fetch that builds the writer's layer. Holder: Andrew.
- **G-COLLEAGUE:** Andrew names the colleague whose grant the close run narrows and widens back. Holder: Andrew.
- **The close run (the COO's one real run):**
  - FWD-1 LIVE: Andrew narrows the named colleague's grant from the dashboard;
  - the colleague's next MCP call is answered within the new limit;
  - it is widened back, and both writes show in Recent Changes;
  - A1n's negative arms, run LIVE: a second signed-in Opal account is refused on the dashboard, and `/sprint` still
    serves.

## R2.5 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The claim keys, the owner key's value and the release census are measured by their cells.
2. The remaining pages (FWD-3, 5-9, 11-13) and S6 are subtracted, per the analysis's section 4.

# ROUND 3 -- THE ENRICHMENT CUT (L5, v3)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v3",
 "step": 5,
 "round": 3,
 "input": "org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round2.md@33ca99c40e (section 5, E1-E5)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@963fff9f5a (v0.3, ratified-text half re-signed @24ef97a3b7)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 5,
 "chains": 3,
 "join_cells": 1,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MP`, the project's one COO since the ~19:5xZ placement. **Input:** the CTO's round-2 analysis
@33ca99c40e, section 5, cut in ONE issuance. Rounds 1 and 2 above stay frozen as their own records.

## R3.1 E1 IS DONE BEFORE THE CUT (the issuer's act, R-7)

E1 was read by the issuer @c8b42c8913 (`deliverables/2.0.0_SA_COO~MP/round3/E1_G-HDR_READ.md`): 1
`OWNER-HEADER-CLAIMS` line in 552671 journal lines across 4 boots, keys
`email,exp,family_name,given_name,iss,name,picture,sub`. That picks the `sub` branch, and because `oid` and `iat` are
both absent, it triggers G-C4. G-C4 is now signed: the CTO's addendum is v0.3 @963fff9f5a and the CVO re-signed it
@24ef97a3b7. The line is printed only AFTER `is_owner` (`app/owner_gate.py:113-118`), and the access log shows `GET /
200` at 14:59:58Z, so Andrew's admission (A2's third arm) is MEASURED by E1, and no cell re-runs it. E1 is not a cell.

## R3.2 THE CELLS -- 5

| Cell | From | Builds / runs | Write surface | Risk |
|---|---|---|---|---|
| `MP-b-3` | row Z-S10 (CTO ruling msg 26207) + row Z-S12 | the writer's record: `who` on a WRITTEN item carries the claim NAME and the email only, never the owner-key value (`lambda_function.py:189`, `:266`); a test proving no WRITTEN item holds the configured value on either branch; the stale expectation at `tests/test_grant_writer.py:141` (it predates NFRA_OPLGTW's `email_deny` record @3e936f77bd) brought to the record set `activate` writes at HEAD | `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`, its `tests/` | WORLD (infra floor; it goes live through MP-a-2's apply) |
| `MP-a-2` | E2 (the re-cut of MP-a-1, plus R-9) | the writer's APPLY on the `sub` branch: `MCPORTAL_OWNER_KEY_CLAIM=sub`, key = Andrew's own `whoami` `sub` (from the issuer's spawn note, never committed); the layer built from its pinned requirements (G-PYPI given); `safe-apply` targeted to `mcportal_grant_writer.tf`; NEVER-2 ledger slug `nfra-mcportal-r3-writer-apply`; the live no-header refusal; R-9's source-map note replaced | `infra/aws/lambda/layers/mcportal-grant-writer-deps/`, `infra/aws/lambda/ci/lambda-source-map.json`, ledger paths | WORLD |
| `MP-f-1` | E3 (R-8, row Z-W2-S3) | the batch cell: a gateway test fixture that points `AUDIT_PATH` at a temp file for the whole session; `app/config.py`'s default is untouched | `infra/aws/ec2/opal-gateway/tests/conftest.py` | WORLD (infra floor) |
| `MP-v-1` | E4 (A2, FWD-2) | FWD-2's live arms: one signed-in Opal account that is not Andrew's (`Opal Bloomberg`, named here) requests `/` and each of the 5 admin handlers once (6 of 6 expect 403) and `/sprint` (expect 200); graded on the gateway's own access log | its deliverables only | WORLD |
| `MP-c-1` | E5 (A1 + A1n, the FWD-1 close run) | after Andrew's sitting (narrow one colleague's grant from the Entitlements tab, the colleague asks, widen back, the colleague asks again): reads both writes in the writer's table, runs A1n's two live-reachable arms, commits the redacted exchange; carries the round's JUDGMENT criterion | its deliverables only | WORLD |

## R3.3 DEPENDENCY EDGES AND CHAINS

```
chain A   MP-b-3 --> MP-a-2 --> MP-c-1     a-2 applies the package b-3 changed; c-1 grades writes the applied writer makes
chain B   MP-f-1                no edge
chain C   MP-v-1                no edge (reads the live gateway only)
joins     MP-c-1 (A + G-CLOSE)
```

**Fan-out:** `N = 3 of M = 3 chains, cap 8`. Slots: `~1` b-3, then a-2, then c-1; `~3` v-1; `~4` f-1 (`~2` is skipped because
round 2's `wk-NFRA_MCPORTAL-2` worktree at `C:/tmp/mp-2` still carries uncommitted gitlink moves and is not reaped
here).

## R3.4 GATES (spawn preconditions; none of them holds another chain)

- **MP-b-3** has no gate and spawns at the issuance. It was added at the cut, before any issuance, on the CTO's Z-S10
  ruling (msg 26207: "cut it ahead of MP-c-1").

- **G-SUB (MP-a-2):** Andrew's own `sub` from `https://mcp.opalinvest.dev/api/admin/whoami` (runbook Part D step 7),
  given to the issuer off-repo. Holder: Andrew. G-HDR, G-C4 and G-PYPI are satisfied.
- **G-2ND (MP-v-1):** a person at the box signs in as `Opal Bloomberg` in the headed Edge window the worker opens
  (Entra MFA is a human act). Holder: Andrew. If nobody can, the arm is ONE card to Andrew, and nothing else in this
  cell runs without a session.
- **G-CLOSE (MP-c-1):** MP-a-2 has drained, and Andrew's sitting is done: he names the colleague, narrows their data
  grant from the Entitlements tab, the colleague asks one real MCP question, Andrew widens the grant back, and the
  colleague asks again. The exchanges are handed to the issuer, who writes `c1_run.json` (window, principal hash,
  off-repo raw path) before the spawn. Holder: Andrew.

## R3.5 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The owner key's value, the layer's versions and every live read are measured by their cells.
2. The full gateway suite is not a criterion. On this box it collects 212 tests with 13 collection errors (`moto` is
   not installed, and installing it is vendor egress), and the run exceeded 300 s. It is the issuer's drain check.
3. A1n's arms (ii), a valid non-owner header, and (iii), an owner header past `exp`, need an ALB-signed header no seat
   can mint. They stand on MP-b-2's in-package tests, as a fixture, per the diet's clause (b).
4. Subtracted, per the analysis's section 5: C6 (round 4), FWD-3 and 5-13 and FWD-4's A4, and Z-W2-S6 (CloudOps).

# ROUND 4 -- THE CONTROL-PLANE THREAD (L5, v4)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v4",
 "step": 5,
 "round": 4,
 "input": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@cecf26d2c9 (v0.5 addendum, FWD-14..19, C11-C16; ratified-text half signed @8de5b2dc76 by 3.0.0_SA_CVO~Z)",
 "author": "2.0.0_SA_COO~MP",
 "thread": "FWD-14",
 "cells": 5,
 "chains": 2,
 "join_cells": 2,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MP`, re-seated 2026-10-08 ~21:0xZ. **Input:** the CTO's v0.5 addendum, which is the CTO's answer
under rule 27 L10 (an FWD that no cell served). Its **Order** paragraph sets this round: FWD-14 end to end first. FWD-15 to
FWD-19 are later enrichment rounds on the same page and two more pages. Rounds 1 to 3 above stay frozen as their own records.

## R4.0 THE ISSUER'S RE-READ OF ROUND 3 (the addendum's "re-read before any cut")

- `MP-c-1` (G-CLOSE) stays staged in round 3. Andrew held Alyssa's close run until gateway r29 is live (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_200xZ_OPLGTW_THREE_CALLS_RECS_APPROVED_ROUND32_FWD10_13_ALYSSA_HOLD.md`).
  That is an essential wait, qualified with Andrew's word. It spawns from its staging file when r29 is live and the
  sitting is set.
- `MP-v-1` (G-2ND) stays staged in round 3. There is no Andrew word on it. It is a human sign-in act.
- Round 3 therefore stays open beside round 4. Its L10 follows its last terminal order. Neither round holds the other: no
  round-4 cell reads a round-3 write, and the two write surfaces are disjoint (round 3: the grant writer and its
  deliverables; round 4: the cells below).

## R4.1 THE DOMAIN, BY SUBTRACTION

FWD-14's ACCEPT has three clauses: (i) every figure carries its age; (ii) a box that is not reporting reads "not
reporting", never zero; (iii) the counts match the activity store for the same window. The journey has five hops:
1. the store (`s3://opal-313476888478-globgrph/fabric/activity/v1/`, live, writer `.tools/fabric-activity.py`);
2. the gateway's read permission on it;
3. an owner-gated admin handler that reads and aggregates;
4. the page that renders it;
5. the release that serves 3 and 4, and Andrew's look.

Hop 1 exists and is not this project's (C11). Each of hops 2 to 5 is one cell. The look is the close run. Subtracted:
- site Z's activity hook. It is a precondition of a four-box read, placed with `0.0.0_AB_MSTR~Z` by C12. Until it lands,
  the page shows site Z as "not reporting", which is clause (ii) working.
- the git-state columns (FWD-16) and overlap (FWD-15). These are enrichments.

## R4.2 THE CELLS -- 5

| Cell | Serves | Builds / runs | Write surface | Risk |
|---|---|---|---|---|
| `MP-x-1` | FWD-14 hop 3 | `GET /api/admin/fabric/boxes?hours=N` behind `owner_only`, per the contract in R4.3, plus its roster file and tests | `infra/aws/ec2/opal-gateway/app/admin_fabric.py` (new), `app/admin_api.py` (one route line), `app/refs/fabric_boxes.json` (new), `infra/aws/ec2/opal-gateway/tests/test_admin_fabric.py` (new) | WORLD (infra floor; live only through MP-x-4) |
| `MP-x-2` | FWD-14 hop 4 | the Control Plane page in `mcportal`: the sidebar entry, the API client call, the view, its tests | mcportal `src/pages/control-plane/*` (new), `src/shell/pages.ts`, `src/shell/sidebar.test.ts`, `src/api/admin.ts`, `src/api/admin.test.ts` | WORLD (live only through MP-x-4) |
| `MP-x-3` | FWD-14 hop 2 | the gateway role's read grant on the activity prefix, in the form the CTO rules on row Z-S18; `safe-apply`, targeted; NEVER-2 ledger; read-back by `simulate-principal-policy` (one positive and two negative arms) | `infra/aws/terraform/opal-gateway/mcportal_fabric_read.tf` (new), `graph-read.tf` comment only if the ruling says so, ledger paths | WORLD |
| `MP-x-4` | FWD-14 hop 5 | the gateway release that ships MP-x-1 and the MP-x-2 bundle: `EC2_MANIFEST.json` `mcportal_commit` moves to MP-x-2's commit; deploy on the live base with the stale-base guard; read-back: `/api/admin/fabric/boxes` returns 200 with real boxes, `/` serves the new bundle | `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-x-5` | FWD-14 DONE WHEN | the close run: Andrew opens the page and names one box's projects for the afternoon. The worker reads the same window from the store with `fabric-activity.py boxes`/`who` and grades A14. Carries the round's JUDGMENT criterion (graded at L9) | its deliverables only | WORLD |

## R4.3 THE CONTRACT BETWEEN MP-x-1 AND MP-x-2 (fixed here so the two chains run in parallel)

`GET /api/admin/fabric/boxes?hours=N`. N is an integer from 1 to 24; the default is 6; out of range returns 400. The
response is JSON:

```
{ "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"},
  "read_at": "<ISO Z>",
  "records_scanned": <int>,
  "records_skipped": <int>,
  "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/",
  "boxes": [ { "box": "<roster name>",
               "status": "reporting" | "not reporting",
               "commits": <int>,
               "seats": ["<serial>", ...],
               "projects": [ {"code": "<CODE>", "commits": <int>, "last": "<ISO Z>"} ],
               "last_commit": {"when": "<ISO Z>", "sha": "<12>", "seat": "<serial>", "subject": "<text>"} | null,
               "claims": ["measured" | "inferred" | "absent", ...] } ],
  "unrostered": [ "<box name seen in records but not on the roster>", ... ] }
```

- **Roster.** The boxes are the `devices[].name` values of `org/devices/DEVICES.json`, copied into
  `app/refs/fabric_boxes.json`, because the gateway host carries `app/` and not `org/`. A test asserts the two lists are
  equal, so the copy cannot drift silently. Every roster box appears in `boxes`. A box with no record in the window has
  `status` "not reporting", `commits` 0 and `last_commit` null. That is the one place a 0 may appear, and it is labelled.
- **Reading.** Records are deduplicated by `sha`, preferring `box_claim` measured, the same rule as `fabric-activity.py`
  `fetch()`. They are filtered by `when` against the window. The keys listed are `dt=<day>/` for each UTC day the window
  touches.
- **Load.** The gateway runs as one worker on a t4g.nano, so every S3 call runs off the event loop (Starlette
  `run_in_threadpool`). Bodies are cached in-process by key, bounded, because each record is write-once and its body is
  a function of its key. Thread fan-out is capped at 8.
- **Failure.** An unreadable store (AccessDenied, a timeout, a parse failure on a listing) returns 503 with
  `{"error": "store unreadable", "reason": "<class: message>"}` and never an empty `boxes` list. One unparseable record is
  skipped and counted in `records_skipped`. Before MP-x-3 is applied, the live handler returns that 503, which is the
  failure arm working.

## R4.4 DEPENDENCY EDGES AND CHAINS

```
chain A   MP-x-1 --> MP-x-4 --> MP-x-5     the release ships x-1; the close run reads the released page
chain B   MP-x-2 --> MP-x-4                the release ships x-2's bundle
joins     MP-x-4 (A + B + MP-x-3 applied + G-REL)    MP-x-5 (x-4 drained + G-SEE)
MP-x-3    no code edge; gated on G-R3; it must be APPLIED before MP-x-4's read-back can pass
```

**Fan-out:** `N = 2 of M = 2 chains, cap 8`. The slots start at the issuance: `~5` takes MP-x-1, then MP-x-4, then
MP-x-5; `~6` takes MP-x-2. MP-x-3 takes slot `~7` when G-R3 is ruled. The issuance cuts the two ungated cells. MP-x-3,
MP-x-4 and MP-x-5 are cut into this round by issuer amendment when their gates land, because MP-x-3's criteria depend on
the form of the G-R3 ruling. The decomposition does not change.

## R4.5 GATES (spawn preconditions, each an act a named holder can take)

- **G-R3 (MP-x-3):** a ruling on row NFRA_MCPORTAL-Z-S18 (C11's grant against the gateway's no-globgrph-grant control,
  `graph-read.tf:4-8`). R3 is NFRA_CLDGRPH's control, and NFRA_CLDGRPH belongs to the laptop fabric. `1.0.0_SA_CTO~O`
  routed it cross-fabric through `0.0.0_AB_MSTR~Z` to the laptop MSTR with rec (a) (msg 32021, ~21:33Z). Holder: the
  laptop NFRA_CLDGRPH owner, via the laptop MSTR. This cell stays parked until that ruling lands.
- **G-REL (MP-x-4):** the gateway's release lane is clear. NFRA_OPLGTW's r29 is the next release (Andrew's ~20:0xZ word
  holds G-CLOSE until it is live). MP-x-4 deploys on the live base after r29 drains, or rides r29 if `2.0.0_SA_COO~O`
  takes it. The issuer asks `2.0.0_SA_COO~O` once MP-x-1 and MP-x-2 have drained. Holder: `2.0.0_SA_COO~O`.
- **G-SEE (MP-x-5):** Andrew opens `https://mcp.opalinvest.dev/control-plane` once and says one box's projects. Holder:
  Andrew.

## R4.6 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The store's live record count, the handler's latency on the nano, and the bundle size are measured
   by their cells.
2. FWD-14's "four-box read" needs site Z's activity hook (C12, `0.0.0_AB_MSTR~Z`). The thread closes on the boxes that
   report, with site Z shown "not reporting" if the hook has not landed. That is ACCEPT clause (ii), not a gap.
3. The Control Plane sidebar entry goes LAST, after Infosec, so that Andrew's verbatim sidebar order from the 2026-09-17
   brief (asserted by `src/shell/sidebar.test.ts`) stands unchanged with one entry appended. The position is the issuer's
   placement, and Andrew may move it.
4. FWD-15 to FWD-19, C13 to C16, the open-calls read (C11's second prefix) and the git-state columns are subtracted and
   belong to later rounds.

# ROUND 5 -- FWD-14 GOES LIVE (L5, v5)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v5",
 "step": 5,
 "round": 5,
 "input": "org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.round4.md@460bc0af2f (section 5, E1-E3 + the two re-cuts)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@cecf26d2c9 (v0.5, ratified-text half signed @8de5b2dc76)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 5,
 "chains": 3,
 "join_cells": 1,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MP`. **Input:** the CTO's rounds 3-4 analysis @460bc0af2f, section 5, cut in ONE issuance. Every
cell of the rectangle is issued here, gated cells STAGED on their gates (row Z-S19: a round's cells are cut in its one
issuance or not in that round).

## R5.1 THE CELLS -- 5

| Cell | From | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-x-3` | E1, R-12 | the gateway role's read grant under ruling (a): GetObject on `fabric/activity/v1/*` and `fabric/open-calls/v1/*`, ListBucket conditioned on those two; `graph-read.tf` R3 text carve-out; `safe-apply`; NEVER-2 ledger; simulation read-back with a refused third prefix | `0.7.0_AE_CloudOps~MP` | `infra/aws/terraform/opal-gateway/mcportal_fabric_read.tf`, `graph-read.tf` (comments), ledger paths | WORLD |
| `MP-x-4` | E2, R-13 | the NARROW gateway release on the live base after NFRA_OPLGTW r29: MP-x-1's gateway commit plus mcportal `d60b4e0`; the on-host cold `_compute(6)` at most 30 s (else cache or narrow the default window first); NEVER-2 ledger; manifest record | `0.7.0_AE_CloudOps~MP` | `infra/aws/ec2/EC2_MANIFEST.json`, `app/admin_fabric.py` only if R-13's load condition forces a change, ledger paths | WORLD |
| `MP-x-5` | E3, R-14 | the close run: the issuer cards Andrew ONCE; he opens the page and names one box's projects; the worker records the window and his words, reads the store for that minute, and carries the round's JUDGMENT criterion | worker `~5` | its deliverables only | WORLD |
| `MP-c-2` | R-15 | MP-c-1, the FWD-1 close run, re-cut UNCHANGED (same checks `round3/checks/c1.AC*`) | worker `~1` | its deliverables only | WORLD |
| `MP-v-2` | R-15 | MP-v-1, FWD-2's live arms, re-cut; one change: the route census is 6 and the walk adds `GET /api/admin/fabric/boxes` (MP-x-1's route; checks `round5/checks/v2.AC*`) | worker `~3` | its deliverables only | WORLD |

## R5.2 DEPENDENCY EDGES AND CHAINS

```
chain A   MP-x-3 --> MP-x-4 --> MP-x-5      the release's AC3 reads the live store through x-3's grant; the close run reads the released page
chain B   MP-c-2                            G-CLOSE (r29 live + Andrew's sitting with Alyssa)
chain C   MP-v-2                            G-2ND + MP-x-4 drained (its walk includes the new route)
joins     MP-x-4 (x-3 applied + G-REL: NFRA_OPLGTW r29 drained by 2.0.0_SA_COO~O)
```

**Fan-out:** `N = 1 of M = 3 chains, cap 8` at the issuance (chain A's head, MP-x-3).

**Applier lane:** `0.7.0_AE_CloudOps~MP`, a FRESH lane for this project. Msg 32061 moves site Z's applies onto a site-Z
CloudOps seat, and `~Z` is refused by rule 27's one-project-per-Tier-2-seat check (it holds three other projects). Chains B and C start when their gates
land; MP-x-4 and MP-x-5 follow within chain A.

## R5.3 GATES

- **MP-x-3:** none. Starts at the issuance.
- **G-REL (MP-x-4):** MP-x-3 drained, and NFRA_OPLGTW r29 drained by `2.0.0_SA_COO~O`. The issuer asks `2.0.0_SA_COO~O` once
  for r29's drain. Holder: `2.0.0_SA_COO~O`.
- **G-SEE (MP-x-5):** MP-x-4 drained; the issuer cards Andrew ONCE (R-14). Holder: Andrew.
- **G-CLOSE (MP-c-2):** r29 live and Andrew's sitting with Alyssa done; the issuer writes `c1_run.json`. Holder: Andrew.
- **G-2ND (MP-v-2):** MP-x-4 drained and a person signs in as `Opal Bloomberg` in the worker's headed Edge window. Holder:
  Andrew (one card).

## R5.4 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. r29's base commit, the host's cold-read time and the bundle size are measured by MP-x-4.
2. FWD-15 to FWD-19 are subtracted (analysis section 5): FWD-15 to FWD-17 are cut the round after FWD-14 grades REALIZED.
3. Z-S14 belongs to NFRA_OPLGTW (R-17). The round-1 ARMED rows C-S8, C-S10 and W3-S3 are this issuer's by transfer (R-18),
   and W3-S2 is re-read at this cut; those are row acts, not cells.

# WORKSTREAM CP2, ROUND 1 -- FWD-15, FWD-16, FWD-17 ON THE CONTROL PLANE (L5, v6)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v6",
 "step": 5,
 "workstream": "CP2",
 "round": 1,
 "input": "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round6/R6_DECOMP_DRAFT.md@54c2fd91b6 (Q1-Q3 RULED (a), 1.0.0_SA_CTO~O msg 32404) + the producers @5bf8350baa (4.0.0_SA_CRO, read back from S3 on all four boxes 2026-10-09 07:28Z)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@cecf26d2c9 (v0.5: FWD-15..17, C11, C13, C14, A15..A17; ratified-text half signed @8de5b2dc76)",
 "authority": "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ANDREW_DIRECT_20261009_060xZ_CP2_WORKSTREAM_APPROVED_START_POST_REBOOT.md",
 "author": "2.0.0_SA_COO~MP",
 "cells": 7,
 "chains": 5,
 "join_cells": 2,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MP`, re-instantiated after the site Z reboot. **Authority:** Andrew approved this seat's ask at
~06:0xZ 2026-10-09: FWD-15 to FWD-17 issue NOW as a second workstream, `CP2`, while round 5 waits on NFRA_OPLGTW r29 and his
gates ("i approve your ask, you can start there when you are reinstantiated"). That word overrides the round-4 analysis's
sequencing line ("FWD-15 to FWD-17 are cut the round after FWD-14 grades REALIZED"). It does not override the release order:
CP2's release follows MP-x-4. Every order carries `<workstream>CP2</workstream>` beside `<round>1</round>`, so the
one-issuance limb keys CP2 apart from round 5 (`to-pipeline-gate.py` GATE (x), row IRPT_BCKEND-S179). Rounds 1 to 5 above
stay frozen.

## CP2.0 WHY THE CELLS ARE GATEWAY-SIDE ONLY (the ruling)

The gateway host holds no git, no checkout and no box's working tree. Its fabric data is the S3 read MP-x-3 granted (LIVE):
`fabric/activity/v1/` and `fabric/open-calls/v1/`. `1.0.0_SA_CTO~O` ruled (a) on Q1-Q3 (msg 32404). The three producers
are other owners' and are LIVE on all four boxes (read 2026-10-09 07:28Z):

| FWD | producer (writer) | S3 key | schema |
|---|---|---|---|
| 15 | `.tools/open-calls-scan.py` every pass | `fabric/open-calls/v1/box=<B>/open_deploys.json` | `open-deploys/1` |
| 16 | `.tools/fabric-gitstate.py` from `box-sync.sh` | `fabric/activity/v1/gitstate/box=<B>/<stamp>.json` + `latest.json` | `fabric-gitstate/1` |
| 17 | `.tools/open-calls.py` (list), `.tools/open-calls-scan.py` (applies requests) | `fabric/open-calls/v1/box=<B>/open_calls.json`; requests `.../requests/<id>.json`; results `.../request_results/<id>.json` | `open-calls/1`; `open-calls-close-request/1`; `open-calls-close-result/1` |

So this project builds three read handlers, one write of a close REQUEST, the page panels, the one PutObject grant, the
release and the close run. The producers are not cells. A box with no record reads "absent" or "not recorded".

## CP2.1 THE CELLS -- 7

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-o-1` | FWD-15, C13, A15 | `app/refs/overlap_rules.json` (kinds and the deploy rule, versioned) + `GET /fabric/overlap` per CP2.3-O + tests (planted Terraform-with-open-deploy rated above planted shared log; the real capture) | worker `~8` | `app/admin_fabric_overlap.py`, `app/refs/overlap_rules.json`, `tests/test_admin_fabric_overlap.py` (all new) | WORLD (live only through MP-r-2) |
| `MP-s-1` | FWD-16, C14, A16 | `GET /fabric/gitstate` per CP2.3-G + tests | worker `~9` | `app/admin_fabric_gitstate.py`, `tests/test_admin_fabric_gitstate.py` (new) | WORLD (via MP-r-2) |
| `MP-k-1` | FWD-17, C11, A17 | `GET /fabric/calls` + `POST /fabric/calls/close` (writes ONE request object) per CP2.3-K + tests | worker `~10` | `app/admin_fabric_calls.py`, `tests/test_admin_fabric_calls.py` (new) | WORLD (via MP-r-2) |
| `MP-p-2` | FWD-15..17 on the page (S14, S15) | mcportal: Overlap and Git state panels on Control Plane; the Open Calls page with the close form; client functions; tests | worker `~11` | mcportal `src/pages/control-plane/*`, `src/pages/open-calls/*` (new), `src/api/admin.ts`, `src/api/admin.test.ts`, `src/App.tsx`, `src/shell/pages.ts`, `src/shell/sidebar.test.ts` | WORLD (via MP-r-2) |
| `MP-k-2` | FWD-17 hop (the write grant) | `gateway-mcportal-close-request-write-policy`: `s3:PutObject` on `fabric/open-calls/v1/box=*/requests/*` ONLY; never-widen pair (CTO `1.0.0_SA_CTO~O` + COO `2.0.0_SA_COO~MP`) signed against the applier's ASK before the apply; `safe-apply`; NEVER-2; simulation read-back | `0.7.0_AE_CloudOps~MP` | `infra/aws/terraform/opal-gateway/mcportal_close_request_write.tf` (new), ledger paths | WORLD |
| `MP-r-2` | FWD-15..17 live | the gateway release on MP-x-4's live base: the three handlers + the merge-time route lines + the MP-p-2 bundle; NEVER-2; manifest; on-host read-back | `0.7.0_AE_CloudOps~MP` | `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-q-1` | FWD-15..17 DONE WHEN | the close run: Andrew reads one real overlap and one box's git state on the page and closes ONE real call with his ruling; the worker reads the store for each and the close's RESULT object back; carries the workstream's JUDGMENT criterion | worker `~12` | its deliverables only | WORLD |

**The hookup belongs to no cell** (report 2 C10). `app/admin_api.py` gets four route lines at the merge, in ONE issuer
commit: `/fabric/overlap` GET, `/fabric/gitstate` GET, `/fabric/calls` GET, `/fabric/calls/close` POST. Each handler cell
exports its handler and names its line in its report.

## CP2.2 SHARED READ CODE

`app/admin_fabric.py` (MP-x-1, drained) already holds `BUCKET`, `_s3_client()`, `_roster()`, `_list_keys()`,
`_read_records()`, `_cache_put()` and the `run_in_threadpool` + 503 discipline. The three handler cells IMPORT these and
never edit `admin_fabric.py`. A cell that needs a variant writes it in its own module.

## CP2.3 THE CONTRACTS (fixed here so the four build chains run in parallel)

Every route sits under `/api/admin` behind `owner_gate.owner_only`. A store failure that is not a plain absence answers
**503** `{"error": "store unreadable", "reason": "<ExceptionClass: message>"}` and never a 200 with an empty list. A
missing object (`NoSuchKey` / 404) is an ABSENCE and is labelled, never a zero.

### CP2.3-O `GET /api/admin/fabric/overlap?hours=N` (FWD-15)

N is an integer from 1 to 24, default 6; anything else is 400.
```
{ "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"},
  "read_at": "<ISO Z>", "records_scanned": <int>, "records_skipped": <int>,
  "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/",
  "rules": {"file": "app/refs/overlap_rules.json", "version": "<string>"},
  "deploys": [ {"box": "<roster name>", "status": "read" | "absent", "published_at": "<ISO Z>" | null, "open": <int> | null} ],
  "overlaps": [ { "surface": "<surface key>", "cls": "INFRA" | "CODE" | "REGISTRY" | "TOOL" | "RECORD" | "APPEND",
                  "boxes": [ {"box": "<name>", "commits": <int>, "seats": ["<serial>"], "last": "<ISO Z>"} ],
                  "last": "<ISO Z>",
                  "deploys_open": [ {"box": "<name>", "slug": "<slug>", "status": "<status>", "opened_at": "<ISO>"} ],
                  "rating": <int>, "label": "<text>" } ] }
```
- **Records:** the window's activity records, read and deduplicated exactly as MP-x-1 does (by `sha`, the measured claim
  wins; `when` at or after the start).
- **An overlap** is a surface `key` (from each record's `surfaces[]`) touched by two or more distinct ROSTER boxes in the
  window. Every class is listed, APPEND and RECORD included, because A15 rates a shared log BELOW a Terraform surface and
  must show both.
- **The rule file** `app/refs/overlap_rules.json` holds:
  - `version`;
  - `kinds`: per class, its `rank` and its `label`. The order is INFRA ("Terraform") > CODE > REGISTRY > TOOL > RECORD >
    APPEND ("shared log"): PRD C13's order, with the activity writer's two extra classes below it;
  - `deploy_uplift`: an integer larger than the whole kind range;
  - `deploy_open_statuses`: `["OPEN", "HELD-SOVEREIGN-GATED"]`, the two statuses the producer emits for a sentinel still
    on disk;
  - `names`: per surface-key prefix, the needle templates that say an open-deploy entry NAMES that surface. For example,
    `"tf:": ["infra/aws/terraform/{name}/"]` and `"lambda-src:": ["infra/aws/lambda/{name}/"]`, where `{name}` is the key
    after its prefix.
- **Naming:** an entry names a surface when a needle is a substring of the entry's `title`, `entry_path` or any leg
  `target`. A prefix with no `names` row is never deploy-matched and is rated by kind alone.
- **Rating:** `rating = kinds[cls].rank + (deploy_uplift if deploys_open else 0)`. `label` is the kind label, plus
  " -- deploy open" when uplifted.
- **Order:** `overlaps` sorts by rating descending, then box count descending, then `last` descending.
- **`deploys`:** one row per roster box, from `fabric/open-calls/v1/box=<B>/open_deploys.json`. NoSuchKey gives `"absent"`
  and `open` null. A read gives `"read"`, `published_at`, and `open` = the count of entries whose status is in
  `deploy_open_statuses`.

### CP2.3-G `GET /api/admin/fabric/gitstate` (FWD-16)

```
{ "read_at": "<ISO Z>", "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/",
  "trunk": {"head": "<12>" | null, "first_seen": "<ISO Z>" | null, "claim": "inferred", "basis": "<text>"},
  "boxes": [ { "box": "<roster name>", "status": "recorded" | "not recorded", "at": "<ISO Z>" | null,
               "box_branch": "<text>" | null, "box_head": "<12>" | null, "origin_box_head": "<12>" | null,
               "trunk_head": "<12>" | null, "unpushed": <int> | null, "pushed_not_on_trunk": <int> | null,
               "behind_trunk": <int> | null,
               "state": "committed, not pushed" | "pushed, not on trunk" | "on trunk" | "not recorded",
               "unread": ["<text>"],
               "last_pass": {"mode": "<text>", "rc": <int>, "note": "<text>", "serial": "<text>"} | null,
               "integration_refused": {"at": "<ISO Z>", "note": "<text>"} | "not recorded" } ] }
```
- **Source:** `boxes` has one row per roster box, from `gitstate/box=<B>/latest.json`. NoSuchKey gives
  `status` "not recorded", `state` "not recorded", and every other field null (`unread` empty).
- **`state`:**
  - `unpushed.count > 0` -> "committed, not pushed";
  - else `pushed_not_on_trunk.count > 0` -> "pushed, not on trunk";
  - else a null head or count (the producer names an unreadable ref null) -> "not recorded";
  - else "on trunk".
- **Field mapping:** `unpushed` and `pushed_not_on_trunk` carry the record's `.count`. Shas are cut to 12 characters.
- **`trunk`:**
  - `head` is the `trunk_head` of the newest `latest.json`, by `at`.
  - `first_seen` is the earliest `at` among that box family's history records (`gitstate/box=<B>/<stamp>.json`, every
    box, the last 48 hours by key stamp) that carry that head.
  - `claim` is always "inferred". `basis` says so: the first record seen carrying the head, not the push time, which C14
    says has no home yet.
- **`integration_refused`:** the newest history record of that box whose `pass.mode` is "integrate" and whose
  `pass.rc` is not 0. If there is none, the literal "not recorded".

### CP2.3-K `GET /api/admin/fabric/calls?state=open|all` and `POST /api/admin/fabric/calls/close` (FWD-17)

GET (default `state=open`; any other value is 400):
```
{ "read_at": "<ISO Z>", "source": "s3://opal-313476888478-globgrph/fabric/open-calls/v1/",
  "boxes": [ {"box": "<roster name>", "status": "published" | "absent", "written_at": "<ISO Z>" | null,
              "written_by": "<serial>" | null, "scanned_at": "<ISO Z>" | null, "open": <int> | null} ],
  "calls": [ {"box": "<name>", "id": "<id>", "project": "<CODE>", "subject": "<text>", "asked_by": "<serial>",
              "opened_at": "<ISO Z>", "state": "<OPEN|CLOSED|...>", "source": "<path>",
              "request": {"id": "<rid>", "state": "PENDING" | "APPLIED" | "REFUSED", "requested_at": "<ISO Z>",
                          "detail": "<text>" | null} | null } ] }
```
- **Boxes:** one row per roster box, from `box=<B>/open_calls.json` (`rows[]`) and `box=<B>/scan.json` (`scanned_at`).
  An absent `open_calls.json` gives `"absent"`, `open` null, and no calls.
- **Calls:** `state=open` keeps rows whose `state` is "OPEN". `calls` sorts by `opened_at`, oldest first.
- **Requests:** list `box=<B>/requests/` and read each request. Its result is `request_results/<id>.json`; NoSuchKey
  means PENDING. The NEWEST request per `call_id` attaches to its call.

POST, JSON body `{"box": "<roster name>", "call_id": "<id>", "ruling": "<text>"}`:
- **Validation:**
  - a box not on the roster -> 400;
  - an empty `ruling` (after strip) or one over 4000 characters -> 400;
  - a `call_id` that is not an OPEN row of that box's `open_calls.json`, read NOW -> 409 `{"error": "call not open on
    that box"}`, and the same 409 when the list is absent.
- **The write:** ONE `put_object` to `fabric/open-calls/v1/box=<B>/requests/<rid>.json`, `ContentType`
  `application/json`.
  - `rid` = `<YYYYMMDDTHHMMSSZ>-<8 hex>` (the scan's `^[A-Za-z0-9._-]{1,80}$`).
  - The body is `{"schema": "open-calls-close-request/1", "id": rid, "call_id", "ruling" (stripped, otherwise verbatim),
    "ruled_by": "andrew", "requested_at", "requested_by": "andrew", "owner": request.state.owner_email}`.
- **Answer:** 202 `{"request_id": rid, "key": "<key>", "state": "PENDING"}`. A failed put -> 503
  `{"error": "request not written", "reason": ...}`.
- **Bound:** this is the gateway's ONLY write to the bucket. The box's scan applies it through `open-calls.py close
  --ruled-by andrew` and writes the result. The page never edits a list (C11).

## CP2.4 THE PAGE (MP-p-2, against CP2.3)

- **Control Plane** (`/control-plane`, MP-x-2's page) gains two panels below the boxes table: **Overlap** (rated rows,
  the deploy-open ones marked, each with its boxes and age; the `deploys` row per box, "absent" where absent) and **Git
  state** (one row per box: state, heads, counts, age; "not recorded" verbatim; the trunk head with "first seen" and its
  claim). Both re-fetch on MP-x-2's 60 s refresh.
- **Open Calls** (`/open-calls`, new, sidebar entry after Control Plane): every call with box, project, asking seat and
  age; an absent box reads "absent", never an empty list; a Close form per OPEN call (a ruling text box and a Close
  button) that POSTs CP2.3-K and then shows the request as PENDING, later APPLIED or REFUSED with its detail.

## CP2.5 DEPENDENCY EDGES AND CHAINS

```
chain O   MP-o-1 --\
chain G   MP-s-1 ---+--> MP-r-2 --> MP-q-1     the release ships every handler and the bundle; the close run reads the live page
chain K   MP-k-1 ---+
chain P   MP-p-2 --/
chain W   MP-k-2 --/                           the close's write needs the grant APPLIED before MP-r-2's read-back can POST
joins     MP-r-2 (o-1, g-1, k-1, p-2 drained + routes hooked up + k-2 applied + G-REL2)    MP-q-1 (r-2 drained + G-SEE2)
```

**Fan-out:** `N = 4 of M = 5 chains, cap 8` at the issuance: workers `~8` (MP-o-1), `~9` (MP-s-1), `~10` (MP-k-1) and `~11`
(MP-p-2). Chain W is the applier seat `0.7.0_AE_CloudOps~MP`, which gets its GO by message because it is a seat, not a
worker. MP-r-2 and MP-q-1 are issued STAGED (row Z-S19: a round's cells are cut in its one issuance).

## CP2.6 GATES

- **MP-o-1, MP-s-1, MP-k-1, MP-p-2:** none. They start at the issuance.
- **MP-k-2:** none to start the build and the ASK. The apply waits on the never-widen pair signed against the ASK at its
  commit: CTO half `1.0.0_SA_CTO~O` and COO half `2.0.0_SA_COO~MP`. This is the CTO's ruling on Q3 (msg 32404).
- **G-REL2 (MP-r-2):**
  - MP-x-4 (round 5) is drained and live;
  - the four build cells are drained, and the issuer's route hookup has landed;
  - MP-k-2 is applied.

  Holder: the issuer. MP-x-4's own gate is G-REL, NFRA_OPLGTW r29 live.
- **G-SEE2 (MP-q-1):** MP-r-2 is drained. The issuer cards Andrew ONCE. He reads one overlap, reads one box's git state,
  and closes one real OPEN call with his ruling. Holder: Andrew.

## CP2.7 RULE 24 RECORD (the three new value sets)

- **`state` (CP2.3-G)** is over the domain "a roster box's latest gitstate record, or its absence":
  - MECE by construction: absent -> "not recorded"; then unpushed > 0; then pushed-not-on-trunk > 0; then a null field ->
    "not recorded"; then "on trunk".
  - Same grain: one box at one record.
  - One axis: where the box's newest commit sits.
  - State coherence: re-running box-sync moves a box out of "committed, not pushed"; integration moves it out of
    "pushed, not on trunk". Neither remedy moves a "not recorded" box, which needs the producer.
- **`status` "read" | "absent" and "published" | "absent"** are over "the per-box object exists". They are MECE (a read
  either returns the object or NoSuchKey; any other failure is the 503 arm, outside the set).
- **The overlap classes** are the producer's six (`fabric-activity.py` `CLS_RANK`), adopted unchanged. They are not a
  new enum.
- **Token census:** none of `not recorded`, `absent`, `PENDING`, `APPLIED` or `REFUSED` is new to the estate. Each is
  the PRD's or the producer's own word.

## CP2.8 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The real overlap count, the gitstate history size and the open-call count are read by the cells,
   from the capture and from the live store at MP-r-2.
2. **The capture:** the seam fixture is a VERBATIM capture of the live store,
   `deliverables/2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json`. It holds 944 objects: every
   `open-calls/v1` object, every `gitstate` object, and the activity records stamped 04:00Z-07:59Z on 2026-10-09. It is
   a fixture of REAL shapes, not live evidence. Live evidence is MP-r-2's read-back and MP-q-1.
3. **Not measured:** that the producer's `trunk_head` agrees across boxes at one instant. Each box fetches on its own
   clock. The page shows each box's own trunk head and age, and the `trunk` row is "inferred".
4. **Out of scope:** push and fetch EVENTS (C14's "no readable home") stay "not recorded" beyond what the gitstate record
   carries. Giving them a home is `4.0.0_SA_CRO~A`'s GitOps work.
5. **Subtracted:** FWD-18 and FWD-19 go to the next workstream round.

## CP2.9 AMENDMENT 1 (issuer, before any spawn): the git-state cell is `MP-s-1`

The issuance cut the git-state cell as `MP-g-1`. That id is round 2's claims-capture cell (R2.1, order
`NFRA_MCPORTAL.TO-MP-g-1.claims-capture-and-history.md`, `<to_id>NFRA_MCPORTAL.TO-MP-g-1</to_id>`, complete). Two cells
under one id is the two-allocators-one-sequence class: a rollup resolves the id to whichever it reads last. The CP2
cell is renamed `MP-s-1` here and in its order. The ORDER FILE keeps its path
(`NFRA_MCPORTAL.TO-MP-g-1.fabric-gitstate-handler.md`), because a renamed file is a newly-added order and GATE (x)
refuses a second issuance into CP2 round 1. The order now answers to `<to_id>NFRA_MCPORTAL.TO-MP-s-1</to_id>` and to
its filename stem (`proof-of-spec-check.py:758`). The checks keep their file names `g1.AC*.sh`.

## CP2.10 AMENDMENT 2 (issuer, while MP-r-2 is staged): the route hookup is MP-r-2's step 0

CP2.1 placed the four `app/admin_api.py` route lines with the issuer, at the merge. The owned-paths gate refused the
issuer's hookup commit: that file is lane CLOUD_OPS_OR_ETL, and the COO lane holds no grant on `infra/aws/`. The lines move
into MP-r-2 as its step 0, and its assignee `0.7.0_AE_CloudOps~MP` holds that lane. Measured by the issuer on the
drained tree, uncommitted: routes 4 of 4, and every admin and fabric test file 58 passed. G-REL2's "routes hooked
up" clause is now satisfied inside MP-r-2, not before it.

## C17 ADDENDUM CELL (PRD v0.6 @fc09ade4ea, issuer 2.0.0_SA_COO~MP, 2026-10-12): the bounded git-state read

**Input.** PRD v0.6 addendum C17 (`1.0.0_SA_CTO~Z`, msg 33458 ruling msg 33456) on row Z-S38. The live Git state cold
read was 25.1 s against R-13's 30 s bar; the issuer's dry run of n1.AC3 read 22.8 s and 2,771 body fetches on the served
code. One cell, cut by the addendum path (spine L10 -> L6, "new cells for an addendum"). The frozen rounds and the CP2
decomposition above are untouched. Its orders carry `<workstream>C17</workstream>` beside `<round>1</round>`, so GATE (x)
keys this issuance apart from CP2 round 1.

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-n-1` | FWD-16 under R-13 (C17) | the bounded read in `app/admin_fabric_gitstate.py` per C17 (windowed listing by `StartAfter`; `integration_refused` stops at the first `integrate` pass of either outcome; `first_seen` stops early per box) + its tests; then the gateway release on the live ref under a never-widen pair (CTO `1.0.0_SA_CTO~Z` + COO `2.0.0_SA_COO~MP`), NEVER-2, manifest, on-host read-back | `0.7.0_AE_CloudOps~MP` (holds the opal-gateway lane) | `app/admin_fabric_gitstate.py`, `tests/test_admin_fabric_gitstate.py`, `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths, its deliverables | WORLD |

**Chain:** one cell, no edge into or out of CP2. **Fan-out:** 0 workers; the assignee is a seat and takes its GO by
message. **Gate:** none to build. The deploy waits on the never-widen pair signed against the assignee's ASK, and on the
gateway queue (one release in flight at a time).

**Checks** (`deliverables/2.0.0_SA_COO~MP/c17/checks/`), dry-run by the issuer 2026-10-12 ~08:5xZ:

| Check | HEAD (negative control) | the issuer's scratch C17 sketch (positive control) |
|---|---|---|
| n1.AC1: 1x vs 10x history, equal get_object counts | FAIL: 242 vs 2,402 | PASS: 98 vs 98 |
| n1.AC2: superseded refusal "not recorded"; live refusal {at, note} | FAIL: the superseded refusal is shown | PASS |
| n1.AC3: served cold _compute, body fetches printed, <= 10 s | FAIL: 22.8 s, 2,771 fetches | not runnable before the release |

**Does not claim:** the 10 s bar holds for every future history size inside the window. The window still grows with the
producers' write rate, roughly 840 to 1,200 records a day across 4 boxes, so about 2,000 in 48 h. AC3 measures it once,
on the served release.

# WORKSTREAM GW, ROUND 1 -- FWD-20: THE GATEWAY BREAKDOWN, AND THE DEEP-LINK FIX (L5, v7)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v7",
 "step": 5,
 "workstream": "GW",
 "round": 1,
 "input": "PRD v0.7 addendum (FWD-20) @cdb5ff66b1, ratified-text half signed @3318b66cd0; 1.0.0_SA_CTO~Z msgs 33511, 33519 (the deep-link ruling, row Z-S41 @4160a7a9db), 33592",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@cdb5ff66b1 (v0.7: FWD-20; C2, C4, C15, C16 apply unchanged)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 6,
 "chains": 4,
 "join_cells": 2,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MP`, re-seated 2026-10-13. **Authority:** the v0.7 addendum makes FWD-20 the FIRST outcome cut
(Andrew-direct ~20:5xZ 2026-10-12, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`). It
is cut ahead of every other open order; the four staged close runs (MP-x-5, MP-q-1, MP-v-2, MP-c-2) do not gate it. The
deep-link cell rides this issuance on the CTO's ruling (msg 33519). Every order carries `<workstream>GW</workstream>`
beside `<round>1</round>`, so GATE (x) keys this issuance apart from CP2 and C17. Every section above stays frozen.

## GW.0 WHAT IS MEASURED BEFORE THE CUT (issuer, 2026-10-13 ~09:3xZ)

1. **The map exists as code, not as a page** (`4.0.0_SA_CRO` census
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/GATEWAY_CHANNEL_MAP_20261008.md`, read whole). The sources C15 names are all
   in the gateway app: the integration specs (`app/integrations/*/integration.py`, `IntegrationSpec` in
   `app/integrations/base.py:56`), the registry (`app/integrations/registry.py`: `_ACTIVE_BY_TOOL`,
   `classification_for_tool`, `catalog_ref_for_tool`), the tool class table (`app/data_entitlement.py` `classify`,
   `TOOL_CLASSES`, `DATA_GRANT_TOOLS`), `app/destructive_ops.py` (`classify`, `write_class`), the Graph scope map
   (`app/graph_scope_map.py`), the catalog (`app/refs/DATA_CATALOG.yaml`, rows carrying `read_tool`), and the live server's
   registered tool list (`app/tools.py:99`, `mcp`).
2. **Who may call what is decided by a chain, not by one store.** Per call, in order: the kill switch and the blocklist
   (`app/blocklist.py`); `data_entitlement.tool_denial` (a profiled principal is confined to its grant on the data-grant
   family only); `identity_scope.check(email, tool)` (a scoped identity is confined to its allowlist); the tier
   (`tier.resolve_tier`) through `guard.enforce` and `entitlements.is_entitled` on a write class, and
   `guard.enforce_min_tier` on an integration's `min_tier`. So "who is entitled to a channel today" is a function of the
   env rosters (`MASTER_ADMIN_EMAILS`/`_PRINCIPALS`, `WRITE_CAPABLE_EMAILS`/`_PRINCIPALS`), the scope allowlist, the
   blocklist, and the grant store.
3. **The grant store cannot be listed by the gateway today.** `opal-gateway-role` holds `dynamodb:GetItem` only on
   `gateway-access-state-table` (`infra/aws/terraform/opal-gateway/schwab_access_state.tf:88-113`). The writer's changes
   table (which the gateway may Scan) holds 1 row and names none of the store's principals. Measured by the issuer
   (keys only, values redacted): the table holds 1,453 rows; POLICY partition 17 rows over 5 keys: ONE real principal
   (`principal_profile` + 4 `data_entitlement` revisions + 4 `operator_audit`), three `probe-og-i1-*` test keys, and one
   `EMAILDENY` row. So listing "who holds a grant" needs ONE new read action: `dynamodb:Scan` on that table, cell MP-z-4.
4. **The deep-link defect** (row Z-S41): the served `server.py` routes the bundle only at `/` and `/assets/{path}`; the
   bundle's `BrowserRouter` routes `/mcp-server`, `/mcp-server/recent-changes`, `/control-plane`, `/open-calls` and the
   placeholder pages (mcportal `bc37107` `src/App.tsx:21-30`, `src/shell/pages.ts`), so a direct load 404s.
5. **Live ref:** gateway `185dc04888` (EC2_MANIFEST `services.opal-gateway`), mcportal `bc37107`. The trunk carries other
   projects' unreleased gateway changes, so the release (MP-z-5) cuts on the LIVE ref at its act, as MP-n-1 did.

## GW.1 THE CELLS -- 6

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-z-1` | FWD-20 (all three parts), C15, C16 | `GET /api/admin/gateway/breakdown` per GW.3, generated in-process from the gateway's own definitions and decision chain; the grant-store read per GW.3 holders | worker `~13` | `app/admin_gateway_breakdown.py`, `tests/test_admin_gateway_breakdown.py` (both new) | WORLD (live only through MP-z-5) |
| `MP-z-2` | FWD-20 on the page (S16) + the route list for MP-z-3 | mcportal: the Gateway page `/gateway` (sidebar after Open Calls), its client function and tests; `public/routes.json` per GW.4 with a test that it equals the app's routes | worker `~14` | mcportal `src/pages/gateway/**` (new), `src/api/admin.ts`, `src/api/admin.test.ts`, `src/App.tsx`, `src/shell/pages.ts`, `src/shell/sidebar.test.ts`, `public/routes.json` (new) | WORLD (via MP-z-5) |
| `MP-z-3` | Z-S41 (deep links) | in `app/server.py`: one owner-gated handler serving `index.html` for each path in the bundle's `routes.json` (GW.4); an unknown path still 404s; tests | worker `~15` | `app/server.py`, `tests/test_dashboard_deep_links.py` (new) | WORLD (via MP-z-5) |
| `MP-z-4` | FWD-20 part 3 hop (the list read) | `gateway-access-state-principal-scan-policy`: `dynamodb:Scan` on `gateway-access-state-table` ONLY; never-widen pair (CTO `1.0.0_SA_CTO~Z` + COO `2.0.0_SA_COO~MP`) signed against the applier's ASK before the apply; `safe-apply`; NEVER-2; simulation read-back | `0.7.0_AE_CloudOps~MP` | `infra/aws/terraform/opal-gateway/access_state_principal_scan.tf` (new), ledger paths | WORLD |
| `MP-z-5` | FWD-20 + Z-S41 live | the gateway release on the LIVE ref: MP-z-1's module + its route line in `app/admin_api.py` (step 0, the CP2.10 precedent) + MP-z-3's `server.py` change + the MP-z-2 bundle; never-widen pair; NEVER-2; manifest; on-host read-back | `0.7.0_AE_CloudOps~MP` | `infra/aws/ec2/opal-gateway/app/admin_api.py`, `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-z-6` | FWD-20 DONE WHEN | the close run: Andrew reads the page (G-SEE3); the worker checks ONE channel's tool list against the deployed code and ONE person's entitlements against the grant store, and opens `/control-plane` by direct load; carries the JUDGMENT criterion | worker `~16` | its deliverables only | WORLD |

**The hookup belongs to no cell** (report 2 C10): the `app/admin_api.py` route line
`Route("/gateway/breakdown", admin_gateway_breakdown.breakdown, methods=["GET"])` plus its import is MP-z-5's step 0, as
CP2.10 ruled (the file is lane CLOUD_OPS_OR_ETL).

## GW.2 READ-ONLY SURFACES (no cell edits them)

`app/admin_api.py` (except MP-z-5 step 0), `app/owner_gate.py`, `app/admin_grants.py`, `app/access_state.py`,
`app/data_entitlement.py`, `app/tier.py`, `app/guard.py`, `app/entitlements.py`, `app/identity_scope.py`,
`app/blocklist.py`, `app/destructive_ops.py`, `app/graph_scope_map.py`, `app/integrations/**`, `app/tools.py`,
`app/refs/DATA_CATALOG.yaml`, `app/config.py`. C16's ratings file does not exist yet (FWD-19 is not cut); MP-z-1 reads
`app/refs/channel_ratings.json` IF PRESENT and creates nothing.

## GW.3 THE CONTRACT -- `GET /api/admin/gateway/breakdown` (fixed here so MP-z-1 and MP-z-2 run in parallel)

Behind `owner_gate.owner_only`. The body, exactly:

```
{ "read_at": "<ISO Z>",
  "kill_switch": true | false,
  "channels": [
    { "id": "m365" | "<integration spec id>",
      "name": "Microsoft 365" | "<spec.display_name>",
      "kind": "native" | "integration",
      "auth": "delegated" | "<spec.auth_kind value>",
      "min_tier": "<spec.min_tier>" | "per tool",
      "rating": {"value": "<R0..R4>" | "unrated", "reason": "<text>" | null},
      "tools": [ { "name": "<tool>",
                   "access": "read" | "write",
                   "write_class": "<destructive_ops.write_class>" | null,
                   "data_class": "<data_entitlement.classify>" | "unclassified",
                   "graph_scopes": ["<scope>"] | null,
                   "indexes": ["<catalog id>"] } ],
      "indexes": ["<catalog id>"],
      "holders": [ { "who": "<email or display>", "how": "<basis>", "tools": ["<tool>"] } ],
      "holders_basis": "<one line>" } ],
  "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
```

- **Channels** = every tool on the live server (`mcp`'s registered list, UNFILTERED by principal), each placed in exactly
  one channel: a tool an active integration owns (`registry._ACTIVE_BY_TOOL`) goes to that integration's channel; every
  other tool goes to `m365` (native). No hand-kept list. A tool `data_entitlement.classify` does not know reads
  `data_class: "unclassified"`.
- **Indexes** of a tool: `registry.catalog_ref_for_tool(tool)` when not None, plus the id of every catalog row whose
  `read_tool` equals the tool; a channel's `indexes` is the sorted union over its tools. None reads `[]` and the page
  prints "none".
- **Rating**: from `app/refs/channel_ratings.json` (`{"channels": {"<id>": {"value", "reason"}}}`) when the file and the
  channel's entry exist; otherwise `{"value": "unrated", "reason": null}`. Never a default level.
- **Holders**: computed by CALLING the gateway's own chain (GW.0 item 2), never a re-typed rule. Candidates: every
  address in `MASTER_ADMIN_EMAILS` and `WRITE_CAPABLE_EMAILS`, every scoped identity `identity_scope` knows (seed +
  overlay), every principal with a `principal_profile` in the grant store (MP-z-4's Scan, projected to `pk`/`sk`, then
  each read through the EXISTING `data_entitlement.current_access`), and ONE population row, `who`: "every signed-in Opal
  Microsoft user", evaluated as an unprofiled, unscoped, unblocked address at tier `read_only`. A candidate holds a tool
  when none of the chain's checks denies it; a holder row lists only the channel's tools it holds; a candidate holding
  none of a channel's tools is not listed there. A blocklisted candidate holds nothing. With the kill switch on, every
  channel's `holders` is `[]` and `holders_basis` says so. A channel with no holder has `holders: []` and the page prints
  "no one".
- **`grant_store`**: a Scan refused or failing gives `status: "unreadable"` with the reason, and the holders rows that
  depend on it are omitted with `holders_basis` naming the gap. It is never a 200 that reads as "no grants".

## GW.4 THE ROUTE LIST -- `routes.json` (fixed here so MP-z-2 and MP-z-3 run in parallel)

mcportal ships `public/routes.json` (Vite copies it to the bundle root): `{"version": 1, "paths": ["/", ...]}`, every
path the app's `<Routes>` serves, `/gateway` included, sorted. A mcportal test fails if it differs from the paths in
`src/App.tsx` and `src/shell/pages.ts`. The gateway reads `<DASHBOARD_BUNDLE_DIR>/routes.json` at request time and serves
`index.html` behind the owner gate for an EXACT path in `paths`; every other path answers 404 as today; a missing or
unreadable `routes.json` serves `/` only (fail closed); `/assets/{path}`, `/api/admin`, `/mcp` and every other existing
route keep their endpoint.

## GW.5 DEPENDENCY EDGES AND CHAINS

```
chain B   MP-z-1 --\
chain P   MP-z-2 ---+--> MP-z-5 --> MP-z-6     the release ships the handler, the deep-link route and the bundle
chain D   MP-z-3 ---+
chain W   MP-z-4 --/                           holders need the Scan grant applied before the release's read-back
joins     MP-z-5 (z-1, z-2, z-3 drained + z-4 applied + G-REL3)    MP-z-6 (z-5 drained + G-SEE3)
```

**Fan-out:** `N = 3 of M = 4 chains, cap 8`: workers `~13` (MP-z-1), `~14` (MP-z-2), `~15` (MP-z-3). Chain W is the
applier seat `0.7.0_AE_CloudOps~MP`; it takes its GO by message because it is a seat, not a worker. MP-z-5 and MP-z-6 are
issued STAGED (row Z-S19).

## GW.6 GATES

- **MP-z-1, MP-z-2, MP-z-3:** none. They start at the issuance.
- **MP-z-4:** none to build the policy and write the ASK. The apply waits on the never-widen pair signed against the ASK.
- **G-REL3 (MP-z-5):** the three build cells drained; MP-z-4 applied; the gateway queue free (one release in flight at
  a time; NFRA_OPLGTW's `2.0.0_SA_COO~O` holds the other releases); the never-widen pair signed against the release ASK.
  Holder: the issuer.
- **G-SEE3 (MP-z-6):** MP-z-5 drained. The issuer cards Andrew ONCE: open `https://mcp.opalinvest.dev/gateway` and read
  it. Holder: Andrew.

## GW.7 RULE 24 RECORD (the new value sets)

- **`kind`** {native, integration} over "a tool on the live server": MECE by construction (an active integration owns
  it, or it is native); one axis (who registered it).
- **`access`** {read, write}: write iff `destructive_ops.write_class(tool)` is not None; MECE over the classified set; a
  tool `destructive_ops` cannot classify is fail-closed there and reads as that module says.
- **`rating.value`**: C16's R0..R4 plus "unrated" (the PRD's own token).
- **`grant_store.status`** {read, unreadable}: a Scan returns or it does not.
- **Token census:** "unrated", "unclassified", "no one", "read", "write" are the PRD's or the code's own words; none is new.

## GW.8 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The live channel count, tool count and holder rows are read by MP-z-1's tests against the real
   registry and by MP-z-5's on-host read.
2. **REST route families** (OTP, mail, Teams, `/ms/*`, `/graph/*`) are not channels under GW.3: FWD-20's ACCEPT names
   MCP channels, tools and indexes. They stay on the CRO census until a later round adds them.
3. **Ratings** stay "unrated" everywhere until FWD-19 lands C16's file.
4. **The population row** stands for every tenant user who can sign in; the page cannot name them, and says so.

# WORKSTREAM C17, ROUND 2 -- THE INTEGRATE POINTER (E1) AND THE MANIFEST HELPER (E2) (L5, v8)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v8",
 "step": 5,
 "workstream": "C17",
 "round": 2,
 "input": "ledger/ROUND_ANALYSIS.c17-round1.md @53231d51ee (1.0.0_SA_CTO~Z), ENRICHMENT LIST E1 + E2; E1 consent by 4.0.0_SA_CRO~Z, five conditions, org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CONSENT_NFRA_MCPORTAL_C17_E1_LAST_INTEGRATE_POINTER_20261013.md @b5ce7b2966 (msg 33630)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@cdb5ff66b1 (C17 unchanged; FWD-16)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 4,
 "chains": 3,
 "join_cells": 1,
 "frozen": true
}
```

**The recut, from the analysis's enrichment list, one cell per item, with E1 split by write set.** E1 has two writers on
two surfaces, the producer `.tools/fabric-gitstate.py` (`4.0.0_SA_CRO`'s, consent above) and the gateway reader
`app/admin_fabric_gitstate.py`, so it is two parallel cells against one fixed object (C17R2.2), plus the release. E2 is
one cell; the analysis allowed a LOCAL direct act, but the L6 gate floors an `infra/` path at WORLD, so it is cut as a
build order. Every order carries `<workstream>C17</workstream>` beside `<round>2</round>`.

## C17R2.1 THE CELLS -- 4

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-n-2` | E1, gateway side (C17, FWD-16) | `_refused` reads ONE object per box, `.../gitstate/box=<B>/last_integrate.json`; the window scan in `_refused` is REMOVED; `first_seen` keeps its early stop; tests | worker `~17` | `app/admin_fabric_gitstate.py`, `tests/test_admin_fabric_gitstate.py` | WORLD (live only through MP-n-4) |
| `MP-n-3` | E1, producer side | `.tools/fabric-gitstate.py` writes the pointer on an `integrate` pass only, under the CRO's five conditions; tests | worker `~18` | `.tools/fabric-gitstate.py`, `.tools/tests/test_fabric_gitstate_pointer.py` (new) | WORLD (it reaches every box through box-sync) |
| `MP-n-4` | E1 live (C17 criterion 3) | the gateway release on the LIVE ref, carrying MP-n-2's two files only; never-widen pair; NEVER-2; manifest; on-host cold read at or under 5 s | `0.7.0_AE_CloudOps~MQ` | `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-n-5` | E2 | the `safe-ec2-deploy.sh` manifest helper copies the old `deployed_commit` into `previous_deployed_commit` when the commit changes; an equal commit moves nothing; two test arms | worker `~19` | `infra/aws/ec2/safe-ec2-deploy.sh`, `.tools/tests/test_safe_ec2_deploy_manifest.py` | WORLD (the L6 gate's floor for an `infra/` path; the analysis said LOCAL and DIRECT ACT) |

## C17R2.2 THE OBJECT (fixed here so MP-n-2 and MP-n-3 run in parallel)

`s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/box=<B>/last_integrate.json`, written by the producer's
existing `put()` client and `PREFIX`, body ASCII JSON with exactly these keys:
`{"at": "<the pass record's own 'at', YYYY-MM-DDTHH:MM:SSZ>", "rc": <int, box-sync's --rc>, "note": "<the pass note, at most 200 chars>"}`.
- **Reader:** absent (NoSuchKey/404) -> `integration_refused` "not recorded", basis "no integrate pass recorded since the
  pointer began 2026-10-13"; `rc != 0` -> `{at, note}`; `rc == 0` -> "not recorded" (the newest integrate passed). Any
  other read failure is the existing 503 arm.
- **Writer:** the CRO's conditions, verbatim in the consent record: (1) integrate passes only; (2) same `PREFIX` and
  `box=<B>`; (3) `rc` is the pass's rc and `at` the pass record's `now`; (4) a failed pointer put is reported on the LAST
  line as `pointer=no:<ExceptionName>` beside `put=`, the two existing keys are still attempted, and nothing else fails;
  (5) a later GitOps home folds the pointer in (not this round).

## C17R2.3 DEPENDENCY EDGES AND CHAINS

```
chain G   MP-n-2 --> MP-n-4        the release ships the reader
chain W   MP-n-3                   the producer reaches each box by git; no deploy act
chain H   MP-n-5                   closes at its own drain
```

**Fan-out:** `N = 3 of M = 3 chains, cap 8`: workers `~17` (MP-n-2), `~18` (MP-n-3), `~19` (MP-n-5). MP-n-4 is issued
STAGED to the applier seat.

## C17R2.4 GATES

- **MP-n-2, MP-n-3, MP-n-5:** none.
- **G-REL4 (MP-n-4):** MP-n-2 drained; the gateway queue free. That means after NFRA_MCPORTAL's own MP-z-5 release (GW)
  and any NFRA_OPLGTW release `2.0.0_SA_COO~O` holds. The never-widen pair is signed against the release ASK. Holder:
  the issuer.

## C17R2.5 WHAT THIS CUT DOES NOT CLAIM

1. Until a box runs an `integrate` pass under the new producer, the gateway reads that box "not recorded". The window
   scan that read older refusals is removed by design, and the basis line says so.
2. The 5 s bar is measured once, on the served release (MP-n-4). `first_seen` still walks the window and is not bounded
   further here.
3. Condition (5), the GitOps fold, is not cut; it rides `4.0.0_SA_CRO~A`'s home if that lands.

# WORKSTREAM PC, ROUND 1 -- FWD-21 READ (F1), THE THREE-STATE REFUSAL (G1), FWD-22'S READ (U1) (L5, v9)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v9",
 "step": 5,
 "workstream": "PC",
 "round": 1,
 "input": "ledger/ROUND_ANALYSIS.c17-round2.md @d0dd3f0964 (1.0.0_SA_CTO~Z), NEXT ROUND G1 + F1 + F2 + U1; PRD v0.8 ADMITTED (ratified-text half signed by 3.0.0_SA_CVO~Z, msg 33949); C18 gateway side ruled to NFRA_OPLGTW C-PERSON (msgs 33955, 33959)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@7da54894cf (v0.8: FWD-21, FWD-22, C18; C2, C4, C15 apply unchanged)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 6,
 "chains": 4,
 "join_cells": 2,
 "frozen": true
}
```

**The recut, from the analysis's NEXT ROUND table, by write set.**
- **G1** has two writers in two repositories: the gateway's `_refused` and the mcportal Git state panel. The gateway half
  is `MP-pc-1`. The panel half joins `MP-pc-3`, because both mcportal halves write `src/api/admin.ts`, and two cells may
  not own one file.
- **F1** is the gateway handler (`MP-pc-2`) and the page (`MP-pc-3`), built in parallel against PC.3.
- **U1** is a read (`MP-pc-4`).
- **The release (`MP-pc-5`) and the close run (`MP-pc-6`) are issued STAGED.** F1 and G1 are not served until a release
  ships them, and the release carries Z-W2-S8's rollback-time measurement (analysis ruling 2).
- **F2 is NOT cut this round.** `1.0.0_SA_CTO~Z` msg 33955: "F1 (read only) proceeds; F2 (write) waits on that reader"
  (NFRA_OPLGTW C-PERSON, cut by `2.0.0_SA_COO~O` after r30 and the tier fix). PC.7 fixes the record's shape now, so that
  OPLGTW's reader and F2's writer are cut against one object.
- Every order carries `<workstream>PC</workstream>` beside `<round>1</round>`.

## PC.0 WHAT IS MEASURED BEFORE THE CUT (issuer, 2026-10-14 ~03:1xZ)

1. **Live:** gateway `b0c75d24f1` (MP-n-4), mcportal `0e02a1f` (origin DEV; ls-remote read). The gitstate handler serves
   `integration_refused` as the string "not recorded", or as `{at, note}` for rc != 0. rc == 0 reads "not recorded".
   That is Z-C-S31's defect: laptop's pointer reads rc 0 at 02:37:22Z.
2. **The page** (`src/pages/control-plane/GitStatePanelView.tsx`) prints the string, or `refused <clock>: <note>` for any
   object. So a new object shape without a page change would print "refused" for a clean pass.
3. **The per-call chain** (research read): the `/mcp` middleware runs `blocklist.enforce(email)` (`app/server.py:171-172`).
   `_PolicyGuardedMCP.call_tool` runs `data_entitlement.tool_denial` (`app/tools.py:73-75`). Then `tools._run` (`:133-169`)
   and `integrations/base.py` (`:144-163`) run tier, `tool_denial`, `identity_scope.check` and `guard`.
   `admin_gateway_breakdown._admits` (`:136-170`) mirrors that chain. Holders are built inline in `_compute`'s
   `evaluate()` (`:265-336`). There is no exported per-person function.
4. **Depth and cadence:** `app/refs/DATA_CATALOG.yaml` `tool_index` (`:1359`) rows carry `history_depth` and `freshness`,
   each with a `claim`. No row carries a poll cadence. NFRA_OPLGTW FWD-20 (cadence read live from the AWS schedule) is
   not served yet.
5. **There is no per-person stop on the tool-call path today.** `email_deny` is read only at `/login`, `/sprint*` and
   the consent redeem. A grant-writer `revoke` stops a profiled principal's tools through `decide`. FWD-21's stop is F2's,
   via PC.7.

## PC.1 THE CELLS -- 6

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-pc-1` | G1, gateway half (Z-C-S31, FWD-16) | `_refused` returns three states per PC.2; a per-box `integration_refused_basis` naming the state that applies; tests | worker `~20` | `app/admin_fabric_gitstate.py`, `tests/test_admin_fabric_gitstate.py` | WORLD (live only through MP-pc-5) |
| `MP-pc-2` | FWD-21 read (F1), handler | `GET /api/admin/people` per PC.3, built from the breakdown's own `_admits` chain and the same candidate sources; depth and freshness from `tool_index`; cadence "absent" with its reason; tests | worker `~21` | `app/admin_people.py` (new), `tests/test_admin_people.py` (new) | WORLD (via MP-pc-5) |
| `MP-pc-3` | FWD-21 read on the page (F1) + G1 panel half | mcportal: the People page `/people` (sidebar after Gateway), its client function, `routes.json` entry; the Git state panel prints the three PC.2 states; tests | worker `~22` | mcportal `src/pages/people/**` (new), `src/pages/control-plane/GitStatePanelView.tsx`, `src/pages/control-plane/control-plane.test.tsx`, `src/api/admin.ts`, `src/api/admin.test.ts`, `src/App.tsx`, `src/shell/pages.ts`, `src/shell/sidebar.test.ts`, `public/routes.json` | WORLD (via MP-pc-5) |
| `MP-pc-4` | FWD-22's first cell (U1) | a READ: where Claude Code or the account exposes the signed-in account and the 5-hour and weekly limits, per source, with claims; no build; never a credential value | worker `~23` | its deliverables only | LOCAL |
| `MP-pc-5` | F1 + G1 live | the gateway release on the LIVE ref: MP-pc-1, MP-pc-2, the route line (step 0), the MP-pc-3 bundle; never-widen pair; NEVER-2; manifest; Z-W2-S8 rollback time measured; `infra/logic/registry` in the sparse list (the five recipe rows) | `0.7.0_AE_CloudOps~MQ` | `infra/aws/ec2/opal-gateway/app/admin_api.py`, `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths | WORLD |
| `MP-pc-6` | FWD-21 DONE WHEN, read half + G1 close | the close run: one real person's served view checked against the stores; one channel's per-person tools against the breakdown; the served gitstate reads `no` for a box whose pointer rc is 0 and "not recorded" for a box with no pointer | worker `~24` | its deliverables only | WORLD |

**The hookup belongs to no cell** (report 2 C10). `Route("/people", admin_people.people, methods=["GET"])` plus its
import in `app/admin_api.py` is MP-pc-5's step 0, as CP2.10 ruled.

## PC.2 THE THREE STATES -- `integration_refused` (fixed here so MP-pc-1 and MP-pc-3 run in parallel)

Per box, from the ONE pointer object `box=<B>/last_integrate.json` (C17R2.2, unchanged):

| pointer | `integration_refused` | `integration_refused_basis` |
|---|---|---|
| present, rc != 0 | `{"refused": true, "at": "<at>", "note": "<note>"}` | "refused: the box's newest integrate pass, read from its last_integrate.json pointer, failed with rc <rc>." |
| present, rc == 0 | `{"refused": false, "at": "<at>"}` | "no: the box's newest integrate pass, read from its last_integrate.json pointer, succeeded." |
| absent (404) | `"not recorded"` | "not recorded: no integrate pass has been recorded for this box since the pointer began on 2026-10-13." |

The page prints, in the Git state panel's "Integration refused" cell:
- `refused <clock(at)>: <note>` for `refused: true`;
- `no (<clock(at)>)` for `refused: false`;
- `not recorded` for the string.

A read failure other than absent stays the module's 503 arm. One get per box, unchanged (C17).

## PC.3 THE CONTRACT -- `GET /api/admin/people` (fixed here so MP-pc-2 and MP-pc-3 run in parallel)

Behind `owner_gate.owner_only`. The body, exactly:

```
{ "read_at": "<ISO Z>",
  "kill_switch": true | false,
  "people": [
    { "who": "<email or display>",
      "kind": "person" | "population",
      "how": "<basis, as the breakdown's holder rows phrase it; '; '-joined when several>",
      "tier": "<tier.resolve_tier value>" | "unresolved",
      "channels": [
        { "id": "<channel id>", "name": "<channel name>",
          "tools": [ { "name": "<tool>",
                       "history_depth": {"claim": "measured" | "inferred" | "absent", "value": <as catalogued> | null, "reason": "<text>" | null},
                       "freshness":     {"claim": "measured" | "inferred" | "absent", "value": <as catalogued> | null, "reason": "<text>" | null},
                       "cadence":       {"claim": "absent", "value": null, "reason": "no poll-cadence source is served yet (NFRA_OPLGTW FWD-20)"} } ] } ] } ],
  "people_basis": "<one line: the candidate sources, and any gap>",
  "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
```

- **People** = every candidate the breakdown evaluates (GW.3 holders: `MASTER_ADMIN_EMAILS`, `WRITE_CAPABLE_EMAILS`, every
  scoped identity `identity_scope` knows, every principal with a `principal_profile`, and the population row). A person
  appears whether or not it holds a tool. A person holding nothing has `channels: []`, and the page prints "holds
  nothing". `opalbloomberg@opalinvest.com` is listed like any other person whenever a source names it. Order: Andrew
  (`MASTER_ADMIN_EMAILS`) first, then by `who`; the population row last.
- **What a person holds** = exactly the tools the breakdown's holders say it holds. It is computed by the SAME
  `_admits` chain, imported from `app/admin_gateway_breakdown.py` and never re-typed. A channel appears under a person
  only when the person holds at least one of its tools, and only those tools are listed.
- **Depth and freshness:** the `tool_index` row whose tool is this tool supplies `history_depth` and `freshness` as
  catalogued, with each `claim` carried through. A tool with no `tool_index` row reads `{"claim": "absent", "value":
  null, "reason": "no tool_index row"}`. Never blank and never a default.
- **Cadence:** `{"claim": "absent", ...}` for every tool, with the reason above, until NFRA_OPLGTW FWD-20 is served.
- **Kill switch on:** every person's `channels` is `[]`, and `people_basis` says so.
- **`grant_store`:** as GW.3. A failed Scan omits the profiled principals and `people_basis` names the gap; it never
  reads as "no grants".
- **Writes:** none. F1 is read only.

## PC.4 DEPENDENCY EDGES AND CHAINS

```
chain G   MP-pc-1 --\
chain H   MP-pc-2 ---+--> MP-pc-5 --> MP-pc-6     the release ships G1, the handler, the route and the bundle
chain P   MP-pc-3 --/
chain U   MP-pc-4                                  closes at its own drain
joins     MP-pc-5 (pc-1, pc-2, pc-3 drained + G-REL5)    MP-pc-6 (pc-5 drained)
```

**Fan-out:** `N = 4 of M = 4 chains, cap 8`: workers `~20` (MP-pc-1), `~21` (MP-pc-2), `~22` (MP-pc-3), `~23` (MP-pc-4).
MP-pc-5 goes to the applier seat `0.7.0_AE_CloudOps~MQ` (same project, so the seating rule admits it). MP-pc-6's slot
is `~24`. Both are issued STAGED.

## PC.5 GATES

- **MP-pc-1 to MP-pc-4:** none. They start at the issuance.
- **G-REL5 (MP-pc-5):** MP-pc-1, MP-pc-2 and MP-pc-3 drained; the gateway queue free, which today means after NFRA_OPLGTW
  r30, the tier-admission fix and OG-mg-1 (analysis section 3); the never-widen pair signed against the release ASK.
  Holder: the issuer.
- **MP-pc-6:** MP-pc-5 drained. There is no Andrew gate: FWD-21's read half is graded on the host, and Andrew's own look
  rides the MC Portal sitting (call 21d9) when it happens.

## PC.6 RULE 24 RECORD (the new value sets)

- **`integration_refused`** {refused, no, not recorded} over "a box's pointer read": the pointer is absent, or present
  with rc == 0, or present with rc != 0. That is MECE, on one axis (the newest integrate pass's outcome), and "not
  recorded" is the existing token.
- **`kind`** {person, population}: the population row is the breakdown's one non-addressable candidate; every other
  candidate is a person.
- **`claim`** {measured, inferred, absent}: the estate's own reserved words (CLAUDE.md A VALUE MUST CARRY ITS CLAIM).
  "held" is not used: no figure here is held.
- **Token census:** "holds nothing", "no", "not recorded", "absent" and "unresolved" are the code's or the PRD's own words,
  plus the one new page phrase "holds nothing".

## PC.7 THE PER-PERSON RECORD -- F2's object, fixed now for NFRA_OPLGTW C-PERSON's reader (NOT cut this round)

C18 makes MC Portal the writer and NFRA_OPLGTW C-PERSON the reader, so both are cut against this one object:
- **Key:** `pk` `POLICY#<tid>#<oid>` (the principal's existing partition, `access_state.policy_key`), `sk` and record type
  `person_access`. The record type is added to `access_state.POLICY_RECORD_TYPES` by the reader's cell, the module's
  owner.
- **Body:**
  - `revision`: an int, conditional on the prior value (the grant writer's existing optimistic check);
  - `stopped`: a bool;
  - `channels_off`: a list of channel ids;
  - `tools_off`: a list of tool names;
  - `tools_on`: a list of tool names, each one the floor lists for some principal (C-PERSON);
  - `updated_at` and `updated_by`.
- **Reader rule (C-PERSON):** no record means the floor governs exactly as today. With a record, in order:
  1. `stopped` denies every tool.
  2. A tool in `tools_off`, or whose channel is in `channels_off`, is denied.
  3. A tool in `tools_on` is admitted past the identity-scope and tier floor, but only if the deployed gateway serves it
     and the floor lists it for some principal.
  4. The Opal-users-only gate, C2 and tier admission are evaluated first. A record never admits a non-Opal principal.
- **Writer (F2, a later round):** the grant writer gains the action `set_person_access` with before/after in the change
  history (FWD-4).
- **Rollback per change:** re-write the before.
- **Rollback of the mechanism:** delete the record kind.

## PC.8 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The people count, holder sets and depth claims are read by MP-pc-2's tests against the real
   registry, and by MP-pc-5's on-host read.
2. **FWD-21 is not REALIZED by this round.** Its DONE WHEN needs the test-principal writes (F2), which wait on
   NFRA_OPLGTW C-PERSON. This round serves the read half.
3. **FWD-22 is not built.** U1 is a read that names where the limits are exposed; the build is cut from its findings.
4. Cadence reads "absent" everywhere until NFRA_OPLGTW FWD-20 is served.

---

# WORKSTREAM PC, ROUND 2 -- THE OPERATOR-ROLE READ (R1), THE PER-PERSON WRITE (F2), THE USAGE SOURCE ON SITE Z (U2) (L5, v10)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v10",
 "step": 5,
 "workstream": "PC",
 "round": 2,
 "input": "ledger/ROUND_ANALYSIS.pc-round1.md @771fadb53b (1.0.0_SA_CTO~Z, msg 34162), NEXT ROUND R1 + F2 + U2; L8 adjudications/ADJUDICATION_v5.Z.md; PRD v0.8 unchanged",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@7da54894cf (v0.8: FWD-21, FWD-22, C18; C2, C4, C15 apply unchanged)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 8,
 "chains": 5,
 "join_cells": 2,
 "frozen": true
}
```

**The recut, from the analysis's NEXT ROUND table, by write set.**
- **R1** is one read (`MP-pd-1`): Z-W24-S2's limit, closed by a seat.
- **F2** crosses three write sets, so it is three build cells plus a release and a close run. The grant writer (`MP-pd-2`, the
  Lambda source), the gateway handler (`MP-pd-3`) and the People page (`MP-pd-4`) are built in parallel against PD.2 and PD.3.
  Two cells may not own one file, so `MP-pd-3` is the only cell that edits `app/admin_people.py` this round.
- **U2** is a script (`MP-pd-5`, LOCAL, changes no setting) and then its enablement (`MP-pd-6`, WORLD, STAGED): the analysis
  asks that the first act be to SEE one live `rate_limits` payload on this box, and only then that anything be written.
  Enabling changes every site Z seat's Claude Code settings, so it is its own order with the blast radius and rollback named.
- **The release (`MP-pd-7`) and the close run (`MP-pd-8`) are issued STAGED** (gates in PD.6).
- Every order carries `<workstream>PC</workstream>` beside `<round>2</round>`.

## PD.0 WHAT IS MEASURED BEFORE THE CUT (issuer, 2026-10-14 ~18:0xZ)

1. **Live:** gateway `bacec95ccd` (MP-pc-5), mcportal `17dcbb2` (origin DEV `ls-remote`). The grant writer Lambda
   (`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`) takes the actions `narrow`, `widen`, `revoke`
   and `register_tenant`. `register_tenant` is the precedent for a record kind added by a branch in `_decide`.
2. **A new record kind needs the module's own tuple.** `app/access_state.py` `POLICY_RECORD_TYPES` is the closed set
   `("principal_profile", "data_entitlement", "operator_audit", "email_deny", "tenant_firm")`, and `_as_key`/`_expected_type`
   refuse a key whose record type is not in it. `person_access` is not in it. NFRA_OPLGTW's draft OG-cp-1 (not yet issued,
   `2.0.0_SA_COO~O`'s `DRAFT_NOT_ISSUED_TO-OG-cp-1_person_record_reader.md`) adds it, with the contract copies.
3. **The writer's tests use the RELEASED gateway code.** `tests/conftest.py` stages the Lambda's import closure from
   `EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` with `build_package.py` and puts that directory first on
   `sys.path`. So the writer sees the `access_state` of the live gateway release, never the working tree. Two consequences:
   (a) the writer's tests must plant the record type into the staged module's tuple to test a write; (b) the Lambda that
   accepts `person_access` for real can only be built AFTER OG-cp-1 is RELEASED (live). That is the gate on `MP-pd-7`.
4. **Base: the lambda suite reads 24 passed, 0 failed** (measured 18:0xZ in `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda`).
5. **The operator role can be assumed by this box's identity** (`sts assume-role` on `opal-gateway-access-admin` returned an
   assumed-role ARN; its trust policy admits any principal of the account except `opal-gateway-role`). So R1 can read the
   grant store under the operator role, which Z-W24-S2 said the close run did not.
6. **`ops/schwab_entitlement_admin.py` has no read/show subcommand** (its subparsers are activate, revoke, deny-backfill;
   row Z-W24-S1). A read under the operator role is a raw `GetItem`/`Scan` on `gateway-access-state-table` with the assumed
   credentials, the way `MP-pc-6` read it under the instance role.
7. **U1 (the finding):** the account is readable without a credential (`~/.claude.json` `.oauthAccount`); the 5-hour and
   weekly remaining are not, except through the status-line command's stdin member `rate_limits` (INFERRED from the binary,
   never seen). No `statusLine` is configured on site Z's `~/.claude/settings.json`.
8. **The People rows have no principal id today.** `GET /api/admin/people` rows carry `who` (an email or display), not
   `tid`/`oid`. The grant store and the new record are keyed by `tid`/`oid`. A person known only by email cannot be written
   until a row carries a principal key (PD.3).

## PD.1 THE CELLS -- 8

| Cell | Serves | Builds / runs | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-pd-1` | R1 (Z-W24-S2) | the operator-role read: the grant store read under `opal-gateway-access-admin`, each profiled principal's data-grant tools, compared with the served `/people` view per person per tool, denominators printed | worker `~25` | its deliverables only | SERVED |
| `MP-pd-2` | F2, the writer | the action `set_person_access` in the grant writer Lambda per PD.2: refusals before any store call, optimistic revision, `operator_audit` in the same transaction, the change record with before and after; tests | worker `~26` | `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`, `.../tests/test_person_access.py` (new) | WORLD (live only through MP-pd-7) |
| `MP-pd-3` | F2, the gateway handler | `POST` and `GET /api/admin/people/{tid}/{oid}/access` per PD.3, owner-gated, the POST through `admin_grants.invoke_grant_writer`; the People rows gain `principal`; tests | worker `~27` | `app/admin_people_access.py` (new), `app/admin_people.py`, `tests/test_admin_people_access.py` (new), `tests/test_admin_people.py` | WORLD (via MP-pd-7) |
| `MP-pd-4` | F2, the page | mcportal: on the People page, per row with a principal: channel and tool switches, stop and restore, the person's change history; the client functions; tests | worker `~28` | mcportal `src/pages/people/**`, `src/api/admin.ts`, `src/api/admin.test.ts` | WORLD (via MP-pd-7) |
| `MP-pd-5` | U2, the script | `.tools/claude-usage-statusline.py`: the status-line command that writes the PD.4 snapshot; synthetic-payload tests; it changes NO setting | worker-light `~29` | `.tools/claude-usage-statusline.py` (new), `.tools/tests/test_claude_usage_statusline.py` (new) | LOCAL |
| `MP-pd-6` | U2, enable and SEE a live payload | writes the one `statusLine` key into this box's Claude Code user settings, sees one live `rate_limits` payload (or records that the member is absent), names the blast radius, proves the rollback on a copy | worker `~29` (same queue as pd-5) | its deliverables, plus the one settings key | WORLD |
| `MP-pd-7` | F2 live | the F2 release: the Lambda code apply through `safe-apply` (rebuilt from the then-live gateway release that knows `person_access`) and the gateway release of MP-pd-3, the route lines (step 0), the MP-pd-4 bundle; never-widen pair; NEVER-2 | `0.7.0_AE_CloudOps~MQ` | `infra/aws/ec2/opal-gateway/app/admin_api.py`, `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths, `infra/aws/lambda/mcportal/**` for the build record only | WORLD |
| `MP-pd-8` | FWD-21 DONE WHEN, the write half | the close run after Andrew's sitting: on the test principal, a channel and a tool switched off and back on, and the person stopped and restored, each read back from the grant store and from the change history; the effect on that person's next gateway call | worker `~30` | its deliverables only | WORLD |

**The hookup belongs to no cell** (report 2 C10). The two `Route(...)` lines for `admin_people_access` and their import in
`app/admin_api.py` are MP-pd-7's step 0, as CP2.10 and PC.1 ruled.

## PD.2 THE PER-PERSON RECORD -- the aligned object (supersedes PC.7's field names)

PC.7 fixed `channels_off`, `tools_off` and `tools_on`. NFRA_OPLGTW's OG-cp-1 draft, aligned with this seat in the
2026-10-14 exchange, fixes the names below, and they are the ones used from here. Mapping: `tools_off` is `tools_deny`,
`channels_off` is `channels_deny`, `tools_on` is `tools_allow`, and `channels_allow` is new.

- **Key:** pk `POLICY#<tid>#<oid>`, sk `person_access`, record type `person_access` (`access_state.policy_key(tid, oid,
  "person_access")`): one record per person, no revision part.
- **Body:** `status` (`active` | `revoked`), `revision` (int >= 1), `stopped` (bool), `tools_allow`, `tools_deny` (sorted
  unique lists of tool names), `channels_allow`, `channels_deny` (sorted unique lists of channel ids), `updated_at` (ISO
  Z), `updated_by` (the first 16 hex characters of the sha256 of the approver string the writer already uses, which is
  the verified email or the claim name, never the owner key).
- **The writer's event:** `{"action": "set_person_access", "tid", "oid", "change": {...}, "expect_revision": <int> | null,
  "owner_header"}`, where `change` holds any of `stopped` (bool), `status`, and the four lists. A key absent from `change`
  keeps its prior value; a key present REPLACES it. `expect_revision` is `null` for a first write (the put must find the
  item absent) and the prior `revision` otherwise (the put must find exactly that revision).
- **The writer's answers:** `{"verdict": "WRITTEN", "reason": null, "detail": "", "result": {"tid", "oid", "revision": n,
  "record": {the body}}}` or `{"verdict": "REFUSED", "reason": R, "detail": ...}` where R is one of the four header reasons,
  `OWNER-CONFIG-MISSING`, `BAD-TID`, `BAD-PERSON-ACCESS` (shape), `RECORD-KIND-NOT-LIVE` (the staged `access_state` does
  not know `person_access` yet), or `STALE-REVISION`.
- **Revoking the record** is `change: {"status": "revoked"}`: it writes revision + 1 with status `revoked` (a tombstone,
  never a delete), which returns the floor to the person (OG-cp-1's reader treats a non-active record as no record).
- **Rollback per change:** re-write the before, from the change history's `before`, through the same writer.
- **Rollback of the mechanism:** revoke the record, or delete the record kind; the floor governs exactly as today.
- **Writes are Andrew-only** (C2, laptop CTO ruling @f469cb665f): the writer's header check is unchanged and runs first.

## PD.3 THE CONTRACTS (fixed here so MP-pd-3 and MP-pd-4 run in parallel)

All behind `owner_gate.owner_only`, same origin.

**`GET /api/admin/people`** (existing, edited by MP-pd-3 only): each row gains `"principal": {"tid": "<guid>", "oid":
"<guid>"} | null`. The value is non-null exactly for a row built from a principal with a `principal_profile` in the grant
store (those rows already come from the store's Scan, which carries `tid` and `oid`); every other row is `null`. Nothing
else in the body moves.

**`GET /api/admin/people/{tid}/{oid}/access`** answers 200 with
`{"tid", "oid", "record_kind": "live" | "not live", "record": {the PD.2 body} | null, "read_at": "<ISO Z>"}`. It reads the
record with one strong `access_state` get. If the module refuses the key because it does not know `person_access`, the
answer is `record_kind: "not live"` and `record: null`, never a 500. A read failure other than that is the module's 503
arm. A `tid` or `oid` that is not a GUID is 400.

**`POST /api/admin/people/{tid}/{oid}/access`** takes `{"change": {...}, "expect_revision": <int> | null}`, validates the
shape (`change` keys limited to `stopped`, `status`, `tools_allow`, `tools_deny`, `channels_allow`, `channels_deny`; lists
of at most 64 non-empty strings of at most 128 characters; `stopped` a bool; `status` `active` or `revoked`; at least one
key), reads the verified `x-amzn-oidc-data` header as `admin_grants` does, and calls `admin_grants.invoke_grant_writer(
"set_person_access", tid, oid, change_with_expect_revision, owner_header)`, relaying the verdict. A bad shape is 400 before
any invoke.

**The page** (MP-pd-4): controls render only for a People row whose `principal` is non-null; a row with `principal: null`
reads "no principal id: cannot be changed from here yet" and shows no control. The page loads a person's `access` on
selection, shows `record_kind: "not live"` as "per-person control is not live yet", and after a change re-reads the record
and the person's history. The history is the existing `GET /api/admin/changes?tid=&oid=` list (FWD-4), filtered by the
page to `action` `set_person_access`.

## PD.4 THE USAGE SNAPSHOT -- U2's object (fixed here so MP-pd-5 and MP-pd-6 agree)

The status-line command writes ONE file, `usage_snapshot.json`, in the directory named by `CLAUDE_CONFIG_DIR` when that is
set and `~/.claude` otherwise (so one file per login on a box):
`{"schema": 1, "written_at": "<ISO Z>", "rate_limits_claim": "measured" | "absent", "reason": "<text>" | null, "five_hour":
{"used_percentage": <num>, "remaining_percentage": <num>, "resets_at": <as the payload gives it>} | null, "seven_day": {same} |
null, "account": {"email", "plan", "organization"} | null, "account_claim": "measured" | "absent"}`.
- `remaining_percentage` = 100 - `used_percentage`. The command computes it from the payload and invents nothing.
- The account comes from `~/.claude.json` `.oauthAccount` (`emailAddress`, `organizationType`, `organizationName`) and
  nothing else. It never opens `~/.claude/.credentials.json` and never prints or writes a token.
- A payload with no `rate_limits` member writes `rate_limits_claim: "absent"` with the reason, UNLESS a snapshot already
  holds `rate_limits_claim: "measured"`, which is then left as it is: its own `written_at` is its age. An absent payload
  never replaces a measured snapshot.
- The command prints one short line (`5h <used>% wk <used>%`, or `usage n/a`), always exits 0, writes atomically (temp file
  then replace), and on any error prints nothing and leaves the previous file.

## PD.5 DEPENDENCY EDGES AND CHAINS

```
chain R   MP-pd-1
chain W   MP-pd-2 --\
chain H   MP-pd-3 ---+--> MP-pd-7 --> MP-pd-8       the release ships F2; the close run follows Andrew's sitting
chain P   MP-pd-4 --/
chain U   MP-pd-5 --> MP-pd-6                        one queue, one worker
joins     MP-pd-7 (pd-2, pd-3, pd-4 drained + G-REL7)    MP-pd-8 (pd-7 drained + G-WRITE)
```

**Fan-out:** `N = 5 of M = 5 chains, cap 8`: workers `~25` (MP-pd-1), `~26` (MP-pd-2), `~27` (MP-pd-3), `~28` (MP-pd-4), `~29`
(MP-pd-5, then MP-pd-6 on the same queue). MP-pd-7 goes to the applier seat `0.7.0_AE_CloudOps~MQ`. MP-pd-6, MP-pd-7 and MP-pd-8
are issued STAGED (MP-pd-8's slot is `~30`).

## PD.6 GATES

- **MP-pd-1 to MP-pd-5:** none. They start at the issuance.
- **G-ENABLE (MP-pd-6):** MP-pd-5 drained, and the issuer has read the script and its tests at HEAD. Holder: the issuer. The
  blast radius is every site Z Claude Code session on this Windows profile (the status line runs in each and shows one
  line); the rollback is removing the one `statusLine` key. Both are named in the order and in the pre-act record, and the
  rollback is proven on a copy of the settings file before the live write.
- **G-REL7 (MP-pd-7):** MP-pd-2, MP-pd-3 and MP-pd-4 drained; NFRA_OPLGTW's OG-cp-1 RELEASED (the live gateway's
  `access_state` knows `person_access`, which is what `build_package.py` stages from); the gateway queue free; the
  never-widen pair signed against the release ASK. Holder: the issuer.
- **G-WRITE (MP-pd-8):** MP-pd-7 drained and OG-cp-1 live; a test principal named by the issuer; Andrew's sitting on the
  People page (the writer verifies an ALB-signed owner header, which no seat can produce), with the window and his words on
  the issuer line. The sitting is queued as a call when G-REL7 holds, not before.

## PD.7 RULE 24 RECORD (the new value sets)

- **`person_access.status`** {active, revoked}: a record is in force or it is a tombstone. MECE on one axis (the record's
  standing); the tokens are NFRA_OPLGTW's.
- **`record_kind`** {live, not live}: the deployed `access_state` knows the type, or it does not.
- **`rate_limits_claim` and `account_claim`** {measured, absent}: the estate's own reserved words (CLAUDE.md A VALUE MUST
  CARRY ITS CLAIM). "inferred" is not used in the snapshot: a figure either came from the payload or it is absent.
- **Token census:** "not live", "absent", "measured", "stopped", "revoked" and "no principal id" are the code's or this
  document's own words, plus the page phrase "per-person control is not live yet".

## PD.8 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The writer's behaviour is proven against a fake store with the record type planted; the real store
   accepts `person_access` only after OG-cp-1 is released and the Lambda is rebuilt from it (PD.0 item 3).
2. **FWD-21 is not REALIZED by this round.** Its DONE WHEN needs the test-principal writes read back and honoured on a real
   call (MP-pd-8), which wait on MP-pd-7, OG-cp-1 live, and Andrew's sitting.
3. **FWD-22 is not REALIZED by this round, and the panel is not built.** The status-line snapshot is a file on ONE box. The
   control-plane page is served from AWS and cannot read it. The transport (the per-box producer carrying the snapshot, the
   gateway handler passing it through, the panel printing it) is the NEXT round's enrichment, and the analysis's "the panel
   reads it" is read here as that later hop. The issuer rules this scope inside this decomposition and states it to the CTO.
4. The other three boxes are other fabrics. U2 carries to them only as a cross-box direction after site Z is proven.
5. A person known only by email has no principal key, so no control (PD.0 item 8). Closing that is a later cell.
6. The refusal branch (rc != 0) of the three-state git read stays unexercised, as the analysis ruled.

---

# WORKSTREAM PE, ROUND 1 -- THE /GATEWAY VIEW GROUPED BY SOURCE, NO MICROSOFT 365 DEFAULT (L5, v11)

```json
{
 "project": "NFRA_MCPORTAL",
 "decomp_version": "v11",
 "step": 5,
 "workstream": "PE",
 "round": 1,
 "input": "Andrew-direct 2026-10-15 ~16:3xZ at the 2.0.0_SA_COO~MP terminal (record deliverables/ANDREW_DIRECT_20261015_16xxZ_GATEWAY_VIEW_OWNERSHIP_HUMAN_UI_IS_MCPORTAL.md @5025c60ba1); 2.0.0_SA_COO~O msgs 34496 and 34503 (the finding and the corrected split); 2.0.0_SA_COO~MI msg 34513 (the declaration field and carrier MX-c-21)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md@7da54894cf (v0.8: FWD-20 ACCEPT and C15 apply unchanged; no ENDPOINT or CONTRACT change)",
 "author": "2.0.0_SA_COO~MP",
 "cells": 2,
 "chains": 2,
 "join_cells": 0,
 "frozen": true
}
```

**A defect in the delivered FWD-20 page, and it is MCPORTAL's.** `GET /api/admin/gateway/breakdown` (MP-z-1, my cell) puts every tool that has no
integration spec in a group named "Microsoft 365" (`app/admin_gateway_breakdown.py`, the `else` branch of the tools-to-channels loop, and the forced
`M365_ID` channel). That files the harvest, etfs, news and portal tools under the wrong source, so the page tells a human something false. Andrew's rule
(relayed by 2.0.0_SA_COO~O, msg 34496): the human-facing view is MCPORTAL's, and a fault there is MCPORTAL's.

## PE.0 WHAT IS MEASURED BEFORE THE CUT (issuer, 2026-10-15 ~16:5xZ)

1. The page is not the cause. `GatewayView.tsx` keys each section on `channel.id` (`key`, `data-channel`) and prints `channel.name`; it renders what the
   handler sends. The wrong group is made server-side, in the handler.
2. The catalog does NOT yet say which bucket a tool reads. `DATA_CATALOG.yaml` `tool_index` rows carry `tool`, `definition`, `member`, `owner`, `read_tool`,
   `links`, `index`, `history_depth`, `freshness`; none carries a bucket, and only 11 of 99 rows carry `links`. Bucket names appear only inside dataset
   descriptions (`opal-data-harvest` 78 mentions). So the declaration must be added by NFRA_MCPINDEX (2.0.0_SA_COO~MI msg 34513: field `source_group` on each
   `tool_index` row, carrier cell MX-c-21, cut after MX-r-14 closes; MX-r-14 ships the catalog around 19:00Z).
3. The Microsoft 365 truth is already in the code: `graph_scope_map.TOOL_GRAPH_SCOPES` lists exactly the tools that call Microsoft Graph.
4. Base: the gateway admin suite (`tests/test_admin*.py tests/test_owner_gate.py`) reads 93 passed, 0 failed; `bun test src` at mcportal `f7760a6` reads 51 pass,
   0 fail.
5. The ratings file (`channel_ratings.json`, C16) is keyed by channel id, owned by the project's CTO. A new group id reads "unrated" until a row is added; that
   is the designed reading, not a defect.

## PE.1 THE CELLS -- 2

| Cell | Serves | Builds | Assignee | Write surface | Risk |
|---|---|---|---|---|---|
| `MP-pe-1` | FWD-20 page correctness, handler half | the breakdown groups each tool per PE.2, with no Microsoft 365 default; tests | worker `~31` | `app/admin_gateway_breakdown.py`, `tests/test_admin_gateway_breakdown.py`, `tests/test_admin_people.py` (only assertions that pin a channel id or kind the contract changes) | WORLD (live only through a gateway release) |
| `MP-pe-2` | FWD-20 page readability, view half | the Gateway page shows a summary table of groups, labels each group's kind, shows the grouping basis, counts a tool once; tests | worker `~32` | mcportal `src/pages/gateway/**`, `src/api/admin.ts`, `src/api/admin.test.ts` | WORLD (via a gateway release) |

**The release is NOT a cell here.** 2.0.0_SA_COO~O ships the gateway release of each side (msg 34503): MI's catalog (MX-c-21) and these two cells' commits.
The handler commit and the mcportal bundle commit are handed to 2.0.0_SA_COO~O with their hashes when drained; the never-widen pair and the NEVER-2 ledger are
the releasing seat's act as ever. The mcportal commits reach origin DEV by 0.0.0_AB_MSTR~Z, the only pusher.

## PE.2 THE CONTRACT -- `GET /api/admin/gateway/breakdown`, changed fields only (fixed here so MP-pe-1 and MP-pe-2 run in parallel)

**Grouping, per tool, the first rule that holds:**
1. The tool has an integration spec (`registry._ACTIVE_BY_TOOL`): its integration channel, as today (kind `integration`). A declaration never moves a tool out of
   its integration channel: the integration carries real auth and tier facts. (Whether integration tools should ALSO be regrouped by bucket is Andrew's call,
   open at PE.6 item 3.)
2. Else the tool's `tool_index` row carries `source_group`: an object `{id, name, kind}` or a list of such objects, `kind` equal to `"bucket"`, `id` and `name`
   non-empty strings. The tool joins ONE group per element: `id` = the element's id (the bucket name, e.g. `opal-data-harvest`), `name` = its name, `kind` =
   `"bucket"`, `auth` = `"per tool"`, `min_tier` = `"per tool"`. A tool with several elements is listed in each of those groups.
3. Else the tool is in `graph_scope_map.TOOL_GRAPH_SCOPES`: the existing Microsoft 365 group (`id` `m365`, `kind` `native`, unchanged), and ONLY such tools.
4. Else the tool joins the group `{id: "undeclared", name: "No source declared", kind: "undeclared", auth: "per tool", min_tier: "per tool"}`. It is created only
   when at least one tool lands in it. A tool is never placed in Microsoft 365 by default.
5. A `source_group` that is not an object or list of objects with a string `id`, `name` and `kind` "bucket" is treated as not declared (rule 3 or 4 then applies).

**New and changed body fields:**
- `channels[].kind` takes the values `integration`, `native`, `bucket`, `undeclared`.
- `grouping_basis` (new, a string at the top level): one sentence stating rules 1 to 4 in this order, and the count of tools that fell to the undeclared group,
  ending `N tool(s) declare no source.` (N may be 0).
- `channels` order: all `bucket` groups sorted by id; then `integration` groups by id; then `native` (`m365`); then `undeclared`.
- The forced Microsoft 365 channel (`chans.setdefault(M365_ID, ...)`) stays as today. Every other field of a channel (`tools[]`, `indexes`, `holders`,
  `holders_basis`, `rating`) keeps its meaning; `rating` reads `unrated` for a group id with no row in the ratings file.
- Holders are computed from each group's tool list by the existing chain; a tool listed in two groups appears in both groups' holder rows.

**The view (MP-pe-2)** shows, in this order: the existing title and refresh control; the header line with the number of groups and the number of DISTINCT tool
names (a tool in two groups counts once); the `grouping_basis` line; a summary table (Group, Kind, Tools, Holders) with one row per channel in the
response order, whose Group cell is a link to that group's section (`#gateway-<channel id>`); then the sections as today, each with its kind written in words
(`AWS bucket`, `Integration`, `Built in (Microsoft Graph)`, `No source declared`). A group of kind `undeclared` is marked as a gap in the existing red warning
text style (no new colour).

## PE.3 DEPENDENCY EDGES AND CHAINS

```
chain H   MP-pe-1   (handler: needs no other cell; works with zero declarations)
chain V   MP-pe-2   (view: built against PE.2; no edge to MP-pe-1 beyond the contract)
```
`N = 2 of M = 2 chains, cap 8`: workers `~31` (MP-pe-1) and `~32` (MP-pe-2). No joins.

## PE.4 GATES

None on the cells: they start at the issuance. The REAL grouping shows only after MI's MX-c-21 ships declarations in a gateway release; until then the
page shows the Microsoft 365 group shrunk to its true graph tools and a "No source declared" group holding the rest, which is honest and already an improvement.
Holder of the release gate: 2.0.0_SA_COO~O.

## PE.5 RULE 24 RECORD (the new value set)

- **`channels[].kind`** {integration, native, bucket, undeclared} over "how the tool's group was decided": by spec, by graph scope, by a declared bucket, or by
  nothing. MECE on one axis (the rule that placed the tool); `undeclared` is the explicit gap, never a default level.
- Token census: `bucket`, `undeclared`, `No source declared`, `AWS bucket`, `Built in (Microsoft Graph)` are new; `integration` and `native` are the code's own.

## PE.6 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. Whether the live page reads right is looked at on the running page after a release, by Andrew's eyes or a screenshot.
2. The bucket groups appear only when MI declares them (MX-c-21). This cut makes the page honest without them and ready for them.
3. **Open for Andrew: should integration channels (Schwab, Black Diamond, YCharts and the rest) also be regrouped by bucket?** Rule 1 keeps them as their
   own integration groups because they carry auth and tier facts a bucket group cannot. One word from him changes rule 1.
4. Ratings for the new group ids are the CTO's data file (C16); until rows exist they read `unrated`.

## PE.7 AMENDMENT 1 (issuer, while MP-pe-1 is open and MP-pe-2 is being amended; 2026-10-15 ~18:3xZ)

Appended, not rewritten: PE.0 to PE.2 stand as the record of what was believed at the cut. Three corrections, each found by a worker or by looking at the rendered page.

1. **PE.0 item 3 was wrong.** It said `graph_scope_map.TOOL_GRAPH_SCOPES` "lists exactly the tools that call Microsoft Graph". It does not: its header says it is the consent-scope map for SCOPED identities, one entry per tool any scoped identity may call, and "an allowlisted tool with NO entry contributes nothing". Measured by worker `~31` and re-measured by the issuer on the repository's own registry (86 tools, no integration enabled): 11 tools have an entry; at least eight tools that plainly use Microsoft Graph (`send_email`, `create_draft`, `reply_email`, `upload_text_to_site`, `save_email_attachment_to_site`, `copy_site_file_to_s3`, `list_calendar`, `find_online_meeting`) have none. The map is a PARTIAL signal. No hand-kept Microsoft 365 list is introduced (FWD-20 ACCEPT: "none from a hand-kept list").
2. **PE.2 rule 2 gains a second kind.** A `source_group` element may carry `kind` equal to `graph` as well as `bucket`. A tool whose declaration has an element of kind `graph` joins the existing Microsoft 365 group (`id` `m365`, `kind` `native`, `auth` `delegated`, `min_tier` `per tool`), whatever the element's `id` and `name`. Rule 5 (malformed means not declared) reads "`kind` equal to `bucket` or `graph`". Rule 3 stays, stated as what it is: tools with a known Graph scope join Microsoft 365 when no declaration places them. Until NFRA_MCPINDEX's carrier MX-c-21 declares the remaining Microsoft tools, they read "No source declared": truthful, not yet pretty. The ask to MX-c-21 is sent to `2.0.0_SA_COO~MI` with the eight names above as the start of its census.
3. **The People view had its own copy of the placement rule** (`app/admin_people.py` lines 87 to 97, built at MP-pc-2): every tool with no spec went to `m365`. It made the People view disagree with the regrouped breakdown, and the seam test `test_person_holdings_equal_breakdown_holders` caught it. The rule is made ONE function in `app/admin_gateway_breakdown.py`, called by both the breakdown and the People view. `app/admin_people.py` joins `MP-pe-1`'s write surface for that and nothing else.

**What changes in the orders.** `MP-pe-1` gets Amendment 1 (the three items above, two new tests, `admin_people.py` in its paths, the AC1 wording). `MP-pe-2` is unaffected by this amendment (its own Amendment 1 is about readability). The checks: `pe1.AC1.sh` gains two named tests; `pe1.AC2.sh` is unchanged.


---

# v12 -- WORKSTREAM PF (PE continued): `/gateway` segmented by CONTRACT C-GROUP (2026-10-15 ~20:1xZ, 2.0.0_SA_COO~MP)

Source: PRD v0.9 @532d1e68bb (addendum "the gateway finish by EOD Fri 2026-10-16"), CTO GO msg 34553, Andrew's words carried in the PRD (verbatim there):
"...making sure everything is extremely legible, clean, and well-designed, using the opalinvest.com website design fixtures, as well as making sure that everything is
readable by human eyes and not wrapped or squished on text and segments. The most important thing is really that each displayed tool segment is very clearly
segmented, i recommend this being by bucket, and in the case of opal-data-assets, by client/vendor pairs."
The hold on workstream PE is lifted by that word; PD stays held. Done by 2026-10-16 ~22:00Z. Serves FWD-22 (CONTRACTS side). ENDPOINT unchanged.

## PF.0 WHAT IS MEASURED

1. MP-pe-2 (drained, mcportal DEV 2fdfb607d7) renders one section per `channels[]` entry, a summary table, plain kind words. A bucket group exists only for a tool whose
   `tool_index` row carries `source_group` (MX-c-21, in MCPINDEX round 18, not yet released). Today the live page shows m365 plus "No source declared".
2. CONTRACT C-GROUP (MCPINDEX PRD v0.17 section C-GROUP) fixes the segmentation key: `bucket` on every row (its value IS `source_group.id`); `vendor` and `firm` on every
   opal-data-assets and opal-data-bd row. Vendor values: schwab, blackdiamond, orion, eclipse, smartx, commonwealth, gateway (Tax SMA), market. Firm values: 49financial,
   cottonwood, inflection, multi (one object mixes firms), none (market data), unresolved (neither source resolved it; never guessed). No other grouping field exists.
3. MP-pe-1 (worker ~31, branch `wk-NFRA_MCPORTAL-pe-31`) is the handler cell and holds the same file (`admin_gateway_breakdown.py`). It reported at 7abfb91b46 with
   two blocking rows (Z-W31-S3 the seam test pins the old default for `send_email`; Z-W31-S4 the AC1 expect form); both are the issuer's and are ruled in PF.5.

## PF.1 CELL `MP-pf-1` -- the breakdown segments an assets/bd bucket by (vendor, firm)  (handler; chain H, runs on worker ~31's queue AFTER MP-pe-1 closes)

Reads, never re-derives: for each tool the handler already places by PE.2 rules 1 to 5.

1. When a tool joins a group of kind `bucket` whose `id` is `opal-data-assets` or `opal-data-bd`, read two more string fields from the tool's `tool_index` row (the same
   row `source_group` comes from): `vendor` and `firm`. A field that is missing, not a string, or empty reads as the literal `unresolved`. The handler does NOT
   validate the values against the C-GROUP lists (a new value is an addendum to the contract, never a local rejection).
2. That channel gains `segments`: a list of `{"vendor": <str>, "firm": <str>, "tools": [<tool name>, ...]}`, one entry per distinct (vendor, firm) pair among the channel's tools,
   each tool name listed once in its pair, `tools` sorted by name. A tool in two buckets is placed per bucket by its own element; its vendor and firm are the row's.
3. ORDER of `segments`: by `vendor` ascending, and inside a vendor the named firms ascending, then `multi`, then `none`, then `unresolved`. A vendor `unresolved` sorts last.
4. A channel that is not one of those two buckets carries NO `segments` key (absent, not empty). A bucket channel in those two with no tools in it does not exist (as today).
5. `grouping_basis` gains nothing. `channels[].tools[]`, `indexes`, `holders`, `holders_basis`, `rating` keep their meaning. The People view is unchanged (it lists channels, not segments).

Tests, in `infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py`, by these names (a test plants `tool_index` rows through the file's existing helper):
- `test_assets_bucket_splits_into_vendor_firm_segments`
- `test_multi_none_and_unresolved_firms_are_own_segments`
- `test_missing_vendor_or_firm_reads_unresolved`
- `test_bucket_without_vendor_firm_fields_has_no_segments`
- `test_segments_order_named_firms_before_multi_none_unresolved`
- `test_tool_in_two_buckets_is_segmented_only_where_it_is_assets_or_bd`

## PF.2 CELL `MP-pf-2` -- the Gateway page shows each bucket as a clear segment and each assets/bd (vendor, firm) as a sub-segment  (view; chain V, a new worker ~33)

Contract the page is built against (fixed): `GatewayChannel` gains an optional `segments?: {vendor: string; firm: string; tools: string[]}[]` (MP-pf-1 fills it; absent
means none). The page keeps working with the response of today. It builds against a checked-in fixture (`gateway.cgroup.fixture.ts`, a `GatewayBreakdown` of: opal-data-harvest
(no segments), opal-data-assets with Schwab/49financial, Schwab/cottonwood, Black Diamond/cottonwood, SmartX/multi, Commonwealth/cottonwood, Market/none and one
unresolved/unresolved segment, opal-data-bd with Black Diamond/49financial, one integration, m365, undeclared) and switches to the live catalog with no code change.

What a reader sees (words are fixed so a test can pin them):
- Vendor words: schwab `Schwab`; blackdiamond `Black Diamond`; orion `Orion`; eclipse `Eclipse`; smartx `SmartX`; commonwealth `Commonwealth`; gateway `Tax SMA`; market
  `Market data`; any other value is shown as given; `unresolved` reads `Vendor not resolved`.
- Firm words: 49financial `49 Financial`; cottonwood `Cottonwood`; inflection `Inflection`; multi `Several firms`; none `No firm`; unresolved `Firm not resolved`; any other value as given.
- A segment heading reads `<vendor words> / <firm words>` (for example `Schwab / 49 Financial`); a segment of `multi`, `none` or `unresolved` firm shows ONE line under the heading saying
  why (`One object mixes firms; the tools filter rows by firm.` / `Not a client source.` / `The catalog did not resolve a firm for these tools; a gap, not a firm.` -- the last in
  the existing `gateway-gap` red).
- A bucket with `segments` shows, inside its section, one sub-section per segment with `id="gateway-<bucket>--<vendor>--<firm>"` (`data-segment`), its tool count in the heading line,
  and its own tools table (the bucket's tool rows whose names are in the segment). A bucket with no `segments` renders as it does today.
- The summary table lists the bucket row as today and, under each segmented bucket, one indented row per segment (Group cell a link to the sub-section, Kind `Segment`, Tools = the
  segment's count, Holders blank).
- NOT SQUISHED, NOT WRAPPED: every tools table sits in a container `gateway-scroll` with `overflow-x: auto`, tool and index names are `white-space: nowrap`, and the page itself never scrolls
  sideways at 390 px width; a segment heading never wraps mid-word (`overflow-wrap: normal`, the heading may wrap between words only). Colour and type are the existing tokens
  only (portal/DESIGN.md at `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, read-only): light canvas, white hairline panels, navy ink `#163372`, one band per page; no new colour, no new font.

Tests, in `src/pages/gateway/gateway.test.tsx` by these names (the file's `renderToStaticMarkup` way), using the checked-in fixture:
- `a segmented bucket renders one sub-section per vendor and firm`
- `a segment heading reads vendor words slash firm words`
- `multi none and unresolved firms are labelled segments with their reason`
- `the summary table lists each segment under its bucket with a link`
- `a bucket with no segments renders as before`
- `every tools table sits in a scroll container`

## PF.3 EDGES AND CHAINS

```
chain H   MP-pe-1 (open) -> MP-pf-1    (same file, one worker's queue: ~31)
chain V   MP-pf-2                       (no edge to H beyond the contract; builds on the fixture)
```
`N = 2 of M = 2 chains, cap 8` (workers ~31 continued and ~33 new). No join; the live `segments` field arrives with the gateway release by 2.0.0_SA_COO~O, which batches MP-pf-1
with MP-pe-1 (one release). The catalog fields arrive with MCPINDEX's first C-GROUP catalog release.

## PF.4 CRITERIA

- MP-pf-1: AC1 the six named tests; AC2 the admin suite bound (0 failed, no seam failure, 102 or more passed); no third.
- MP-pf-2: AC1 the six named tests plus `bun test src` 0 failed; AC2 a judgment criterion (`judgment="true"`): legibility at 1280 px and 390 px, graded by the CVO or Andrew from the issuer's screenshots.
  The ISSUER's one real run at close: render the fixture at both widths with headless Edge, one screenshot per segment (every bucket and every sub-segment), look at each, and measure
  `document.documentElement.scrollWidth <= innerWidth` at 390 px. That run is mine, not a worker criterion.

## PF.5 RULINGS ON WORKER ~31's ROWS (issuer, inside this decomposition; gate limb: none graded a modification, `<placeholders>` is NONE)

- **Z-W31-S3:** the seam test asserts the old default, `("m365","send_email")`. `send_email` calls Microsoft Graph but has no `TOOL_GRAPH_SCOPES` entry, so by PE.7 rule 3 it is undeclared
  until MX-c-21 declares it (kind `graph`). The assertion is the stale half: it changes to say BOSS holds `send_email` and the population does not, under whatever group id the breakdown gives it.
- **Z-W31-S4:** the AC1 expect form is the issuer's: the script prints three lines. The expect becomes one pattern a checker can match: `named tests PASSED 10 of 10.*RESULT: PASS.*exit=0`; the same for AC2.

## PF.6 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. Whether the live page reads right is looked at on the rendered fixture by me and on the live catalog after the first C-GROUP release, then by Andrew's sitting (21d9).
2. The segments exist on the live page only after (a) MCPINDEX's C-GROUP catalog release and (b) the gateway release carrying MP-pe-1 and MP-pf-1. Until then the page shows what it shows today.
3. The vendor and firm WORDS are the issuer's spelling of the C-GROUP values for a human; they are display only and change no value.
4. The open question for Andrew from PE.6 item 3 (regroup integration channels by bucket) is unchanged.

## PF.7 AMENDMENT 1 (issuer, 2026-10-15 ~22:0xZ, after reading NFRA_MCPINDEX TO-MX-c-21 lines 28 to 37 and the CTO's ruling msg 34591)

Appended, not rewritten. Three facts that PF.0 to PF.2 did not have:
1. **`source_group.kind` takes a THIRD value, `store`.** MX-c-21 item 3 writes `kind` `bucket` for an `opal-data-` bucket, `graph` for the Microsoft tools and `store` for any other source (the YCharts tools, the Kuzu graph tools, a tool that reads only gateway
   state, DynamoDB), with `source_group.name` the bucket word title-cased. PE.2 rule 5 (written before MX-c-21 existed) treats any kind other than `bucket` and `graph` as a malformed declaration, so every `store` tool would read as "No source declared"
   although it IS declared. That is the issuer's fault; it would have shown a false gap on the live page. Ruling: rule 2 accepts a third kind `store`; the tool joins a group `{id: <source_group.id>, name: <source_group.name>, kind: "store", auth: "per tool", min_tier: "per tool"}`;
   `channels[].kind` gains `store`; the channel order becomes bucket, store, integration, native, undeclared. The page says `Data store` for it (not `AWS bucket`, not a gap).
   Rule 24 record: `kind` {integration, native, bucket, store, undeclared} stays one axis (how the tool's group was decided: by spec, by graph scope, by a declared S3 bucket, by a declared other store, or by nothing); `store` is declared, so it is never a gap.
   Token census: `store` is new in this field; in the catalog it appears only as `source_group.kind` (MX-c-21 item 3).
2. **`vendor` and `firm` are on catalog ROWS only, not on `tool_index` entries** (MX-c-21 items 2 and 3). I asked the CTO (msg 34589).
3. **RULED by the CTO (msg 34591, C-GROUP item 2 amended @5ba12d1de5): the tool-level pair is a LIST, `serves`.** Each assets/bd `tool_index` entry carries `serves`, the distinct (vendor, firm) pairs of the catalog rows naming it as `read_tool`, written by MX-c-21 and never typed;
   /gateway lists a tool under EVERY pair in its `serves`. This replaces PF.1 rules 1 and 2 (one `vendor` and one `firm` field per tool). The shape the handler reads, stated here because the contract names no element form: a list of objects `{"vendor": <str>, "firm": <str>}`.
   Until MX-c-21 writes it, every assets tool reads the pair (`unresolved`, `unresolved`), which the page shows honestly as `Vendor not resolved / Firm not resolved`.

New cells (PF ROUND 2, because the issuance gate allows one issuance per workstream round; round 1 stays open until its two orders and Amendment 2 drain): `MP-pf-3` (handler: `store` and `serves`, chain H on worker ~31's queue) and Amendment 2 to `MP-pf-2` (the words `Data store`, the type, the fixture with a store channel and a tool serving two pairs, two tests).


# v13 -- WORKSTREAM PF, ROUND 3: the served /gateway read, the scroll cue, the principal-set read (2026-10-16 ~03:3xZ, 2.0.0_SA_COO~MP)

Source: the CTO's round-2 analysis `org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.pf-round2.md` @bfe9f3549c (msg 34676), on the CVO's slug msg 34672
(`surprise-channel/adjudications/ADJUDICATION_v6.Z.md` @9ffddae434: Z-C-S38 grade, Z-C-S40 and Z-C-S41 graduated). PRD v0.9 unchanged. ENDPOINT unchanged.
Ruling 1 of that analysis binds this round: a /gateway outcome is REALIZED only when the live page, read at mcp.opalinvest.dev/gateway, shows the segments at a
measured `mcportal_commit` and `deployed_commit`. A merged display cell is not a live one.

## PF3.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~03:2xZ)

1. The handler already keys on the `tool_index` block only: `_declared_source_groups` and `_segment_fields_for` read `doc["tool_index"]` and nothing else
   (`admin_gateway_breakdown.py:127-201`). Run over the REAL repo catalog (`_pf4_realcat.py`): `tool_index_rows=99 firm_keys_outside_tool_index=273 pairs_from_tool_index=0
   pairs_returned=0 extra_pairs=0`. So ruling 3's trap exists in the real catalog (273 owning-firm `firm:` keys) and the handler does not fall into it; what is missing is the
   PLANTED negative arm that keeps it so.
2. The served host today (EC2_MANIFEST `opal-gateway`): `deployed_commit` d577e0e7297b, `mcportal_commit` 17dcbb286; the served `_compute` lists m365 with 76 tools and no
   segments. The PF handler (54a75d46ba) and page (421f8fb) are not deployed. The release path is MCPINDEX `TO-MX-r-15` (C-GROUP keys in the host catalog), then `OG-ap-23`
   (`2.0.0_SA_COO~O`, the handler and the bundle), then this round's served read.
3. The People check (Z-C-S40) compares the principals the host-role Scan returns (`_scan_principals`, `principal_profile` rows) with themselves. The CTO's source for a second plane is the grant
   writer's OWN table, `mcportal-grant-changes-table` (env `MCPORTAL_CHANGES_TABLE`, host `.env`). MEASURED over SSM at ~03:2xZ (`_r2_probe.py`, command a9f00f73): the grant store holds
   1 principal (digest b43a6e7dd649); the changes table holds 1 item, a `REFUSED` attempt (`NO-OWNER-HEADER`, 2026-09-29) by a PLACEHOLDER principal (digest 5e6f088b53db), and no grant.
   The two sets DIFFER. The grant writer is not the only writer today (the real grant was written another way), so its history is not an independent enumeration of who holds a grant.
   `admin_grants.read_changes_table` reads ONE Scan page and does not follow `LastEvaluatedKey`; the probe follows it.

## PF3.1 CELL `MP-pf-4` (S1) -- the segment compute reads `tool_index` only, shown by a planted arm and by the real catalog; the served arm is the issuer's  (handler tests; chain H)

Risk SERVED as the CTO classed the cell (the order carries WORLD: the L6 gate floors any `infra/` path at WORLD). A worker builds and proves what runs offline; the SERVED arm needs a deploy that is not this order's, so it is NOT a worker criterion (a criterion no worker can pass is a defect at the cut).

1. Two tests in `infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py`, by these names:
   - `test_channel_row_firm_key_never_makes_a_segment`: a catalog with a `tool_index` row that declares a bucket (`opal-data-assets`) and NO `serves`, plus a channel-artifact row whose
     `read_tool` is that tool and a silver row, each carrying `firm: cottonwood`, yields ONE segment, the pair (`unresolved`, `unresolved`), and no segment named `cottonwood`;
   - `test_tool_index_serves_pair_makes_a_segment`: the same catalog with `serves: [{vendor: schwab, firm: cottonwood}]` on the `tool_index` row yields the segment (`schwab`, `cottonwood`)
     (the positive arm, so the first is not vacuous: the planted owning-firm rows are present in both).
2. The handler is changed only if a test shows a defect (it should not: PF3.0 item 1). A defect is fixed in `admin_gateway_breakdown.py` and named in the report.
3. THE SEAM: the real-catalog probe `_pf4_realcat.py` reads `extra_pairs=0` with `firm_keys_outside_tool_index` at least 1 (a bound; passes at the base).
4. THE SERVED ARM (issuer, at close, once `OG-ap-23` reads deployed): `pf4.served.sh` reads `deployed_commit` and `mcportal_commit`, then the SERVED `_compute` over SSM, and prints the
   denominator (channels, tools, segments per bucket). Then the live page at 1280 and 390 px, screenshots graded by the CVO (judgment, at L9). Until then S1 is NOT REALIZED.

## PF3.2 CELL `MP-pf-5` (S2) -- a table that scrolls inside its box shows a cue at 390 px  (view; chain V)

Risk LOCAL. The CVO's grade Z-C-S38 bound: at 390 px a cut table column shows no scroll cue (the Kind, Tools and Holders columns of the summary table, and Data class and Indexes of a tools
table, are off the right edge with nothing to say so). The cue is CSS only (no script, no timer): on every `.gateway-scroll`, a fade or edge on the side that has more to scroll to, using
the existing tokens, one test. The issuer's one real run then re-renders the fixture at 390 px and looks.

## PF3.3 CELL `MP-pf-6` (R2) -- the host-role scan's principal set and the grant writer's change-history set, both read, both denominators printed  (probe and comparator; chain R)

Risk SERVED (one read-only SSM command on the gateway host). It builds a comparator with planted arms and records ONE real read; it does not assert equality (PF3.0 item 3: the sets differ today, and
that is the finding the CVO's Z-C-S40 asked to see). The cell does NOT widen what the writer or the store may do: it reads.

1. `r2_principal_sets.py` in the worker's deliverables dir: `compare(scan_set, history_set)` returns `{scan_n, history_n, only_scan_n, only_history_n, equal, vacuous}`; `vacuous` is true when
   BOTH sets are empty (equal is then false: an empty equals an empty proves nothing). A CLI mode turns the probe's `R2 {json}` line into the run file `r2_run.json`.
2. `test_r2_principal_sets.py` with four named tests (planted arms): equal sets; a principal in the scan only; a principal in the history only; two empty sets.
3. The one real read: the worker runs the issuer's `pf6.run.sh` (SSM, read-only) and writes `r2_run.json` from its output.
4. The verdict `equal` is a JUDGMENT for the CVO (criterion AC3): does the grant writer's change history serve as an independent enumeration of who holds a grant, and if not, what source does?

## PF3.4 EDGES AND CHAINS

```
chain H   MP-pf-4        (handler tests; no edge)
chain V   MP-pf-5        (the mcportal page; no edge)
chain R   MP-pf-6        (the principal-set read; no edge)
```
`N = 3 of M = 3 chains, cap 8` (workers ~34, ~35, ~36). Write sets are disjoint: MP-pf-4 writes the gateway breakdown test file (and its handler only on a found defect); MP-pf-5 writes
`mcportal/src/pages/gateway/`; MP-pf-6 writes only its own deliverables dir. No shared-file hookup is needed. The served arm of MP-pf-4 waits on `OG-ap-23`; nothing else waits.

## PF3.5 RULINGS (issuer, inside this decomposition; gate limb: none graded a modification, `<placeholders>` is NONE)

- **The worker status flip.** The order file is outside every worker's `<paths>`, so a worker cannot flip `<status>` (rows Z-W26-S2, Z-W28-S4, Z-W29-S3, Z-W31-S8). Every face of this round says
  "do not flip this order's `<status>`; the issuer does". The clause in `.claude/agents/worker.md` line 73 is not edited here (a standing agent definition is outside this lane); the face overrides it.
- **Carried fact (CTO ruling 6):** `opal-gateway-access-admin` has no `dynamodb:Query` or `Scan` on `gateway-access-state-table`. No cell of this round assumes either under that role; MP-pf-6 reads under the
  host instance role over SSM, and says so.

## PF3.6 WHAT THIS CUT DOES NOT CLAIM

1. No served segment. The live page shows segments only after `TO-MX-r-15` and `OG-ap-23`; the served arm is run then, by me, and is graded by the CVO.
2. R2 does not close Z-C-S40: it measures the second plane and finds it is not independent. A source that is (the writer made the only writer, or another enumeration) is the CTO's to name.
3. S2's cue is judged by my look at 390 px, not by a test; the test pins the rule, not the reading.


# v14 -- WORKSTREAM PF, ROUND 4: the People view's principal set against a raw read under a different credential (2026-10-16 ~04:0xZ, 2.0.0_SA_COO~MP)

Source: the CTO's PF round-3 analysis `org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.pf-round3.md` @0a775f4f7b (msg 34710), on the CVO's slug msg 34708 (`ADJUDICATION_v7.Z.md` @3cae7d7992). PRD v0.9 unchanged. ENDPOINT unchanged.
That analysis WITHDRAWS round-2 ruling 4 (the premise "the grant writer is the only writer" was never measured, and MP-pf-6 measured it false) and names the independent source for Z-C-S40: a raw full read of the table under a different credential, outside the page's code path.

## PF4.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~04:0xZ)

1. This box's AWS identity (what the workers' `.tools/aws` shim resolves to) is the IAM user `Andrew_Berman`, not the gateway host role. `iam simulate-principal-policy` for it on `gateway-access-state-table` reads `dynamodb:Scan` allowed and `DescribeTable` allowed. The negative control is NOT a nonexistent action (this user allows `NoSuchAction99` too): it is the same `Scan` for the operator role `opal-gateway-access-admin`, which reads `implicitDeny` (it matches row Z-W25-S1's measured AccessDenied), so the simulator discriminates.
2. The table holds 1,669 items (3 `--no-paginate` pages of 945, 483 and 241, no filter). The raw grant-bearing set (distinct (tid, oid) of `POLICY#<tid>#<oid>` items of record type `principal_profile`, `data_entitlement` or `person_access`) is 1 principal, digest b43a6e7dd649; the same 9 POLICY items hold no other principal (`audit_only_principals` 0). The page set (`_scan_principals` under the host role over SSM) is 1 principal, the same digest. EQUAL today.
3. The sanctioned writer of `POLICY#` records is `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py` (the operator role only; it writes a profile and its grant together, DELETES NOTHING, and appends an `operator_audit` row for every change). So the analysis's live plant ("write a planted grant item through the one sanctioned writer, then confirm both sets show it, and that removing it removes it from both") cannot be done as written: the audit rows would keep a planted principal in any raw read for good, and a profile plus grant written together can never be the "page misses a holder" case the arm exists for.

## PF4.1 CELL `MP-pf-7` (R3) -- the raw read, the comparison, and the planted principal both ways  (chain R3; risk SERVED, read-only)

A worker reads and records; the instruments are the issuer's (`pf7.run.sh`, `_r3_page_probe.py`). Built by the worker in its deliverables dir:
1. `r3_principal_sets.py`: `compare(page_set, raw_set)` returns `{page_n, raw_n, only_page_n, only_raw_n, equal, vacuous}` (`vacuous` when both are empty; `equal` only when both differences are 0 and not vacuous); a command line turns the output of `pf7.run.sh` into `r3_run.json`, exits 3 and writes no run file when the SIM line says Scan is not allowed.
2. `test_r3_principal_sets.py`: five named tests, the planted principal checked BOTH ways (in the raw set only = the page misses a holder; in the page set only), the empty case, and the STOP branch.
3. The one real read: `pf7.run.sh`, read-only, three reads (SIM, RAW, PAGE), recorded as `r3_read.txt` (digests and counts only) and `r3_run.json`.

## PF4.2 EDGES, CHAINS, AND WHAT DEPARTS FROM THE ANALYSIS

```
chain R3   MP-pf-7   (no edge; the S1 served arm of MP-pf-4 still waits on MX-r-15 and OG-ap-23)
```
`N = 1 of M = 1 chains, cap 8`. Departures, ruled by the issuer inside this decomposition and reported to the CTO in the L10 slug:
- **The executor is a worker subagent (`~37`), not the `0.7.0_AE_CloudOps~Z` seat.** The property the analysis needs is "a different credential, outside the page's code path": the worker's read runs under the IAM user above with no app import, which is that. A seat adds a message round and a dependency for the same credential on this box. Whether CloudOps~Z's own shell resolves to a different identity than the IAM user is NOT measured here.
- **No live plant** (PF4.0 item 3). The both-ways arm is planted in the comparator (offline) and graded by AC1. The control that the raw read can see a holder the page misses is the comparator's own `only_raw_n` arm; a live arm would add a permanent audit row to the production store.
- **Checks anchor to their own root** (the analysis's template fix): `_root.sh` now derives the worktree root from its own file's location, not the shell's cwd; proven by running `pf7.run.sh` from `/c/Users`.

## PF4.3 WHAT THIS CUT DOES NOT CLAIM

1. It is one read at one instant: equal today is not equal after F2 adds a principal. Re-run it then (a measurement, not a monitor).
2. The raw set is the principals holding a profile, a data grant or a person-access record. A principal holding only an `operator_audit` row is counted separately (`audit_only_principals`, 0 today) and is not a holder.
3. `RUNTIME#` principals (OAuth families and catalog snapshots, 1,650 items) are sessions, not grants, and are outside both sets.

## PF4.4 CARRIED CRITERION FOR THE NEXT RUN OF THE COMPARATOR (CTO PF round-4 analysis @a49b708852, ruling 1; no cell is cut now)

The re-run owed when F2 adds a principal (`pf7.run.sh` and `r3_principal_sets.py`, MP-pf-7) carries ONE added criterion: the raw side prints the table's TOTAL POLICY items and each EXCLUDED class with its count and its reason, beside the grant-bearing set. Today those are: 3 probe principals (`POLICY#probe-*`, not GUIDs), 1 EMAILDENY digest (`POLICY#EMAILDENY#<digest>`), and the operator_audit-only principals (0). The nine POLICY items MP-pf-7 printed were a post-filter count shown beside the table's 1,669 denominator; the re-run prints the pre-filter count.
Status of the rest: Z-C-S40 REALIZED for today (CTO). S1 (MP-pf-4, the served /gateway read) stays issued behind OG-ap-23 (after OG-ng-2) and MX-r-15. The probe residue Z-S160 is NFRA_OPLGTW's; Z-S63 stays ARMED on 0.0.0_AB_MSTR~Z.

# v15 -- WORKSTREAM PF, ROUND 5: the Indexes paragraph scrolls inside its own box (2026-10-16 ~11:2xZ, 2.0.0_SA_COO~MP)

Source: row `NFRA_MCPORTAL-Z-S64` (BLOCKING, the issuer's, filed at the S1 served run) and the CTO's ruling msg 34947: "CUT NOW -- one LOCAL mcportal cell". PRD v0.9 unchanged; ENDPOINT unchanged.

## PF5.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~11:2xZ)

The SERVED breakdown body (read over SSM at 10:59:30Z, deployed 0cb4a87bcb, mcportal 090b9cdc85) rendered through the real GatewayView and CSS in a real browser at a true 390 px: `documentElement.scrollWidth` 561 against 390. Cause: `p.gateway-indexes`, a channel's comma-joined index names, holds an unbroken name of about 65 characters (`opal_data_assets_silver_commonwealth_cottonwood_account_day_value`) wider than its 328 px column; six sections overflow. 1280 px is unaffected. The MP-pf-2 fixture carries short names (`idx-positions`), which is why its tests and the first render passed.
The check (`pf8.AC2.sh`) plants that real-length name in every channel's and tool's index list itself, so the worker's own fixture cannot make it pass, and measures at 390 and 1280 in a real browser (Edge via playwright-core, viewport emulation): at the base it reads `scrollWidth=557`, 16 offenders (FAIL as expected), with the short-name control and the 1280 px read ok.

## PF5.1 CELL `MP-pf-8` -- the Indexes paragraph scrolls inside its own box  (view; one chain; LOCAL)

1. `mcportal/src/pages/gateway/gateway.css`: `.gateway-indexes` takes `overflow-x: auto` (the paragraph keeps wrapping between names; a single name wider than the box scrolls inside it). If `pf8.AC2.sh` still reads a page wider than 390 px after that, its output names the next offending element; give it the same treatment inside the same directory and name each in the report.
2. `gateway.cgroup.fixture.ts`: the `opal-data-assets` channel's `indexes` and one of its tools' `indexes` gain the real-length name above, so the checked-in fixture exercises it.
3. ONE test in `gateway.test.tsx`: `an index list holding an unbroken real-length name scrolls inside its own box` (the `.gateway-indexes` rule holds `overflow-x: auto`; the fixture holds a name of 60 or more characters with no space).
Criteria: AC1 the named test and `bun test src` 72 or more pass; AC2 the 390 px and 1280 px measurement. No third.

## PF5.2 WHAT THIS CUT DOES NOT CLAIM

The 390 px measurement is on the checked-in fixture plus a planted long name, not on the live page: the live look is Andrew's (call 21d9), and S1 item (iii) is graded by the CVO on the served body after this lands and reaches the host. The fix reaches the host only with the next mcportal bundle release (a new `mcportal_commit` in EC2_MANIFEST); nothing here deploys it.

# v16 -- WORKSTREAM PF, ROUND 6: the bundle-only release of the Gateway page fix (2026-10-16 ~12:3xZ, 2.0.0_SA_COO~MP)

Source: the CTO's ruling msg 34980 (b): "cut the bundle-only release now; Andrew is at site Z today and can sit any time ... MP-pc-5 shape, two halves, applier CloudOps~Z ... mcportal c66ca82952 only, with no gateway code. Graded on the served page at 390 px (scrollWidth 390) and at 1280. I sign my half on receipt. ~O's round-38 release then carries the same bundle with no delta." Row Z-S64 is the finding; MP-pf-8 (merged @e15f6538f8) is the fix; origin mcportal DEV reads c66ca82952 (MSTR~Z, ls-remote ~12:0xZ). PRD v0.9 unchanged.

## PF6.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~12:2xZ)

1. Live: EC2_MANIFEST `services.opal-gateway` `deployed_commit` 1bc2df0b13 (MX-r-15 v2), `mcportal_commit` 090b9cdc85. No opal-gateway release is open in the ledger (MX-r-15 v3 is next to open; one release in flight at a time).
2. The deploy builds the bundle from the manifest's `mcportal_commit` in a detached mcportal worktree and ships `dist/` as `dashboard/` beside `app/` (`deploy-to-ec2.sh` lines 62-93 and 237-254).
3. A local build of an mcportal commit equals the host's bytes: the host's `dashboard/index.html`, `routes.json` and both current assets were read over SSM (read-only, `ls` and `sha256sum`) and are byte-identical (sha256) to a local `bun run build` of 090b9cdc85. The host also keeps 12 asset files (older bundles accumulate), so the live bundle is whichever `index.html` names.
4. The expected bundle of c66ca82952 (local build): `index.html` sha256 5a6e2eeef8ec...; `assets/index-BRnJX9Mi.css` 120ae5bbd491...; `assets/index-DbObnWYp.js` 52466cffc886... (the JS content is unchanged: only its name moved); `routes.json` e6d4a9ac3ce7... (unchanged). The full hashes are in `pf9.AC2.sh`.

## PF6.1 CELL `MP-pf-9` -- the bundle-only release  (WORLD; applier `0.7.0_AE_CloudOps~Z`; staged until the GO)

One swap of the dashboard bundle on the gateway host: `EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` becomes c66ca82952c01575968d16cc736cdabe36606572 and nothing else in the gateway tree moves (census EMPTY). Never touched: the MCP tool surface, IAM, any store. Rollback: the previous pin (090b9cdc85) through the same deploy. Criteria: AC1 the ledger, the manifest pin and the empty gateway census; AC2 the host's deployed bytes equal the build of c66ca82952, /health 200, the owner gate still 401/403. The 390 px and 1280 px grade is the issuer's real run after the release (the served body through the fixed page, measured).

## PF6.2 EDGES AND WHAT THIS CUT DOES NOT CLAIM

Gate G-REL9 (the issuer holds it): both never-widen halves signed at HEAD AND no opal-gateway release open. `~O`'s round-38 release then carries the same pin with no delta (the CTO's note). It does not claim the page is judged legible: that is S1 item (iii), the CVO's, after the release and MX-r-15's last catalog. The served look is Andrew's (call 21d9).

## PF6.3 SEATING (issuer, ~12:4xZ) -- a departure from the CTO's named applier, and why

The CTO's ruling named `0.7.0_AE_CloudOps~Z` as the applier. `0.7.0_AE_CloudOps~Z` holds NFRA_OPLGTW work, and the seating rule (Andrew-direct 2026-08-24 ~19:29Z, enforced by `.tools/to-decomp-ref-lint.py`'s seating check, announce mode) is ONE PROJECT PER TIER-2 SEAT INSTANCE: the commit gate printed `REFUSED ... FIX: address this TO to a FRESH LANE`. MCPORTAL's own releases have used their own CloudOps lanes (~MP, ~MQ). So `MP-pf-9` is addressed to `0.7.0_AE_CloudOps~MQ`, the lane that applied MP-pc-5 and MP-n-4 and has only ever held NFRA_MCPORTAL orders (same project, so it passes the seating rule), re-seated by the issuer. The order, its checks and its paths follow (`deliverables/0.7.0_AE_CloudOps~MQ/`). The cost: one seat spawn, minutes. Reported to the CTO with the GO-PREP.

# v17 -- WORKSTREAM PF, ROUND 7: six gateway tests repaired against the landed catalog (2026-10-16 ~13:2xZ, 2.0.0_SA_COO~MP)

Source: row `NFRA_MCPORTAL-Z-S67` (filed by `0.7.0_AE_CloudOps~MQ` at the MP-pf-9 prep, step 1) and the issuer's A1 to MP-pf-9 (`66a4be01d8`), which named the six and said their repair is a cell, not the release. PRD v0.9 unchanged; ENDPOINT unchanged.

## PF7.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~13:0xZ)

1. At `box/sitez` HEAD the admin suite (`tests/test_admin*.py tests/test_owner_gate.py`) reads 6 failed, 110 passed. Nothing else fails. The six: `test_admin_gateway_breakdown.py::test_every_live_tool_in_exactly_one_channel` and `::test_real_server_tool_inventory`; `test_admin_people.py::test_people_lists_every_candidate_even_holding_nothing`, `::test_cadence_reads_absent_with_reason`, `::test_real_server_people_inventory`, `::test_people_principal_never_leaks_into_other_fields`.
2. Cause (read in the two files): the landed `DATA_CATALOG.yaml` declares a source group for every live tool. `bd.CATALOG_YAML` defaults to that real file. The breakdown `world` fixture patches no catalog at all, and the people `world` fixture patches only `ap.CATALOG_YAML` (a copy taken at import) and leaves `bd.CATALOG_YAML` real, while the placement rule lives in `bd`. So planted-tool tests now place `list_calendar` and `send_email` in `m365` (not `undeclared`), and the two real-inventory tests pin a channel list (`['m365']`, `{"m365","undeclared"} | specs`) that the real catalog no longer yields.
3. The gateway code is correct as landed (MP-pf-3 and MX-r-15 graded it); only these tests are stale.

## PF7.1 CELL `MP-pf-10` -- repair the six stale tests  (tests only; one chain; worker-light; risk WORLD only because the path floor for infra/ says so)

1. `test_admin_gateway_breakdown.py`: the two planted-tool and real-inventory tests stop depending on the real catalog's contents. `test_every_live_tool_in_exactly_one_channel` plants `tool_index: []` (the file's own `_plant_catalog`) before it plants tools, so its old expectation of an `undeclared` channel is true again. `test_real_server_tool_inventory` asserts invariants derived from the real catalog through `bd._group_ids_for_tools(live)`: every live tool appears exactly once in the body, the set of channel ids equals the union of the group ids of the live tools (plus nothing invented), channel ids are unique, and an integration channel holds only its own tools; the pinned `want=['m365']` list and the pinned count of 5 channels go.
2. `test_admin_people.py`: the `world` fixture points `bd.CATALOG_YAML` at the same empty catalog it already gives `ap.CATALOG_YAML`, which restores the first, second and fourth failing tests to their old expectations. `test_real_server_people_inventory` runs against the REAL catalog (both `bd.CATALOG_YAML` and `ap.CATALOG_YAML` set to the real file path, recorded by the fixture before it patches) and asserts `allowed_channels` as the union of the group ids `bd._group_ids_for_tools(registered)` yields plus the integration spec ids, not `{"m365","undeclared"} | specs`.
3. No file outside the two test files changes. If a test needs an app change to pass, the worker files a BLOCKING row and stops.
Criteria: AC1 the six named tests PASSED and each file 0 failed; AC2 the whole admin suite 0 failed (the existing bound, `pf3.AC2.sh`); AC3 only the two test files changed under `infra/`.

## PF7.2 EDGES AND WHAT THIS CUT DOES NOT CLAIM

No edge to MP-pf-9: the release is bundle-only and excused these six at A1; this cell lands on the trunk after the release's close and is not part of it. The five `FileNotFoundError` tests named in the release ASK are sparse-tree artifacts of the release tree, not stale tests (they pass at HEAD), and are not in this cell. It does not claim the real-inventory tests guard the catalog's content: they guard the placement rule's invariants, which is what they were for.

## PF6.4 WHAT THE RELEASE TAUGHT THE NEXT RELEASE ORDER (issuer, ~14:2xZ, at the close of MP-pf-9; rows Z-S68, Z-S69, Z-S72)

1. The sparse list for a gateway release tree adds `/data/mdpf/config/` (`deploy-to-ec2.sh` stages `data/mdpf/config/partner_roster.json` into the artifact; without it the act is refused before any upload).
2. A release tree cut on an older trunk cannot run the tree-local naming gate: commits there run the TRUNK's `.tools/safe-commit.sh` from inside the tree.
3. A release branch is cut on the live-base lineage and does NOT merge to `box/sitez` (MP-pf-9: 24 conflicting gateway paths). The record of a release lands through a LANDING branch cut from `box/sitez` HEAD carrying only the release's three artifacts (the `opal-gateway` block of `EC2_MANIFEST.json`, the completion entry, the pre-act record), committed by the APPLIER under its own lane (the issuer's lane may not commit `EC2_MANIFEST.json` or the applier's folder), then drained by the issuer. The release branch is kept: the manifest's `deployed_commit` names its commit.
4. The manifest's `file_checksums` are taken from the trunk, not from a release tree cut earlier: a release that moves no gateway file leaves the files of the live base deployed (MP-pf-9: the release block's md5 values mismatched the files at `38fe44d5cb`; the trunk's matched 10 of 10).

# v18 -- WORKSTREAM PF, ROUND 8: the Indexes box shows the same scroll cue as a tools table (2026-10-16 ~14:3xZ, 2.0.0_SA_COO~MP)

Source: the CTO's round analysis `ledger/ROUND_ANALYSIS.pf-s1.md` @b6efe81187 (update ~14:2xZ, after the CVO's v10 read: S1 item (iii) MET, bounded): "Enrichment, cut in the next mcportal batch, LOCAL: `.gateway-indexes` gets the same scroll cue as `.gateway-scroll`, so a card's Indexes box shows it scrolls ... graded on the fixture's ~65-character name." PRD v0.9 unchanged; ENDPOINT unchanged.

## PF8.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~14:3xZ)

At mcportal c66ca82952 (origin DEV, live on the host): `.gateway-indexes { overflow-x: auto; }` is the whole rule (gateway.css), so a name wider than the box scrolls with nothing to say so. `.gateway-scroll` carries the cue: four `linear-gradient` layers, `background-position`, `background-repeat`, `background-size`, and `background-attachment: local, local, scroll, scroll`. In a real browser at 390 px with a 65-character name in every index list, 7 of 7 `p.gateway-indexes` scroll and 0 of 7 carry a cue (`pf11.AC2.sh` base: FAIL). The page itself still fits (`pf8.AC2.sh` base: 390 of 390, 1280 of 1280, 0 offenders: the bound). `bun test src` reads 72 pass, 0 fail.

## PF8.1 CELL `MP-pf-11` -- the Indexes box shows the scroll cue  (view; one chain; LOCAL)

1. `mcportal/src/pages/gateway/gateway.css`: the `.gateway-indexes` rule carries the same cue declarations as `.gateway-scroll` (the four gradient layers, position, repeat, size, attachment), by sharing them (a selector list) or repeating them; `overflow-x: auto` stays, and the paragraph keeps wrapping between names. The existing tests `a scroll box shows a cue that more columns lie off the edge` and `an index list holding an unbroken real-length name scrolls inside its own box` keep their names and pass; the white end covers must match the paragraph's own background so no patch shows.
2. ONE test in `gateway.test.tsx`: `an index list carries the same scroll cue as a tools table` (the rule block or blocks selecting `.gateway-indexes` hold a `background-image` with `linear-gradient(` and a `background-attachment` naming `local` and `scroll`).
Criteria: AC1 the named test and `bun test src` 73 or more pass; AC2 the cue read in a real browser at 390 px; AC3 the bound: the page still does not scroll sideways (`pf8.AC2.sh`).

## PF8.2 WHAT THIS CUT DOES NOT CLAIM

The cue is graded on the fixture's planted 65-character name, never imaged on real data (the real index names carry Schwab master numbers). The look at it on the served page is Andrew's (call 21d9). Like MP-pf-8 it reaches the host only with the next mcportal bundle release (a new `mcportal_commit` in EC2_MANIFEST); nothing here deploys it.


# v19 -- WORKSTREAM GWZ, ROUND 1: a /gateway segment table lists only its own indexes, and one line explains the Schwab master that Black Diamond reports (2026-10-19 ~19:5xZ, 2.0.0_SA_COO~MP)

Source: the CTO's round analysis `ledger/ROUND_ANALYSIS.z-round1.md` @11c572fef9 (answering the CVO's slug, msg 36090, `adjudications/ADJUDICATION_v11.Z.md`: MP-z-6 AC2 NOT MET -- Andrew sees Black Diamond indexes on Schwab tools) and the routing ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_GATEWAY_ASSETS_AUDIT_DEFECT_ROUTING_20261019_Z.md` @473f5177a8 (defect P1, class `display`). PRD v0.9 unchanged; ENDPOINT unchanged.

## GWZ1.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~19:5xZ)

At mcportal 59e802a (origin DEV): `SegmentSection` in `src/pages/gateway/GatewayView.tsx` renders `ToolRow`, and `ToolRow` prints `listOrNone(tool.indexes)` unchanged, so a tool that serves several (vendor, firm) pairs lists ALL its indexes under EVERY segment. The breakdown payload carries `tool.indexes: string[]` and no pair per index (`GatewayTool` in `src/api/admin.ts`), so the page cannot filter today. The CRO's audit (@216dfc8144, section 1, item 1) counts it: `client_get_holdings` lists 13 indexes under "Schwab / 49 Financial": 6 Schwab, 2 Black Diamond, 2 Commonwealth, 1 Orion, 2 SmartX.

## GWZ1.1 THE INTERFACE (issuer's contract, sent to 2.0.0_SA_COO~O; the issuer amends it if NFRA_OPLGTW's round 47 lands a different shape)

Each tool object in the breakdown may carry `index_pairs: [{ "index": <name>, "vendor": <segment vendor key>, "firm": <segment firm key> }, ...]`, one entry per (index, pair) the index serves, in the server's own order. The keys are the same strings a `segments[]` entry carries. The page's rule, in a segment section: show the tool's `index` names whose entry matches that segment's vendor and firm, each once, in the order sent; show `none` if there are none. If a tool has NO `index_pairs` key (an older payload), the page keeps listing `tool.indexes` unchanged. An EMPTY `index_pairs` means the tool has no index for any pair: every segment shows `none` for it.

## GWZ1.2 CELL `MP-z-7` -- one line of context on the Schwab master that Black Diamond reports  (view; one chain; LOCAL)

`GatewayView.tsx` states once, near the top of the page and not per segment, the line `Schwab master 08335338 is the one Black Diamond reports.` (the CTO's words; the master number already appears in the real index names on the page). ONE test in `gateway.test.tsx`, by the name `the page states once that Schwab master 08335338 is the one Black Diamond reports`. Criteria: AC1 the named test and `bun test src` 74 or more pass, 0 fail.

## GWZ1.3 CELL `MP-z-8` -- a segment table lists only the indexes of its own (vendor, firm)  (view; same chain as MP-z-7, queued after it; LOCAL)

`src/api/admin.ts` gains the `index_pairs` field of GWZ1.1 on `GatewayTool` (optional); `SegmentSection`/`ToolRow` apply the rule of GWZ1.1. FIVE tests in `gateway.test.tsx`, by name: `a segment table lists only the indexes whose vendor and firm are that segment's`; `a tool serving two pairs shows each pair its own indexes`; `a tool with no index_pairs keeps listing its indexes unchanged`; `a tool with an empty index_pairs lists none under any segment`; `the audit case: client_get_holdings shows 6 of its 13 indexes under Schwab / 49 Financial` (synthetic index names, the audit's counts 6/2/2/1/2). Criteria: AC1 the five named tests and `bun test src` 79 or more pass, 0 fail.

## GWZ1.4 EDGES AND WHAT THIS CUT DOES NOT CLAIM

- MP-z-7 and MP-z-8 write the same files (`GatewayView.tsx`, `gateway.test.tsx`), so they are ONE chain, ONE worker (slot ~41), z-7 first. The fan-out is 1 of 1 chains.
- The seam probe against the real neighbour is NOT possible: the breakdown handler is owner-gated and `2.0.0_SA_COO~O` has not yet landed `index_pairs` (NFRA_OPLGTW round 47). Both cells are graded on fixtures. That is stated, not a gap hidden.
- NEITHER cell reaches the host: the page change rides the next mcportal bundle release (a new `mcportal_commit` in `EC2_MANIFEST.json`), a separate release cell cut when the bundle is ready, and the handler's `index_pairs` must be live for the served page to filter. The CVO's re-grade of MP-z-6 AC2 (all indexes under every segment belong to it; MCPINDEX's routing table reads 0 `MISROUTED (display)` for `/gateway`) is on the served page after that release. Andrew's read is welcome evidence, never the gate.
- Not claimed: that the `index_pairs` shape above is `2.0.0_SA_COO~O`'s final shape.


## GWZ1.5 AMENDMENT 1 (issuer, 2026-10-19 ~21:0xZ): how the page reaches the host

Measured: the host runs gateway `6d1b5dcb64` (deployed 2026-10-19 16:35:59Z, OG-ap-50) with `mcportal_commit` 59e802a (EC2_MANIFEST.json); mcportal origin DEV reads 21ad404 (MSTR~Z push, msg 36108); no gateway release is open in `.open_deploys/`. A bundle-only release like `MP-pf-9` (one `mcportal_commit` pin in a release tree, the applier's ledger, a rollback proof, two never-widen halves) is possible today.

Ruling: NO separate bundle release. MP-z-8's filter is a no-op until `2.0.0_SA_COO~O`'s `index_pairs` field is live (an absent key leaves the lists unchanged), and the CVO's re-grade of MP-z-6 AC2 needs both halves on the served page, so a release now would put up only the context line and cost one applier cycle that the later gateway release repeats. The page rides the gateway release that carries `index_pairs`: that release's tree also moves `services.opal-gateway.mcportal_commit` to 21ad404 (the one-line pin `MP-pf-9` made), and its census must then name exactly that manifest line beside the handler files. The ask is with `2.0.0_SA_COO~O`. If that release is far off or Andrew asks for the context line sooner, the issuer cuts a `MP-pf-9`-shaped bundle-only cell then. This is a sequencing choice inside this decomposition; the release itself stays `~O`'s order and `0.7.0_AE_CloudOps~NFRA1`'s act.


# v20 -- WORKSTREAM OGW, ROUND 1: /opalgateway, the per-person access page -- the thread first: see a person, subtract, restore, stop, audit (2026-10-20 ~18:0xZ, 2.0.0_SA_COO~MP)

Source: PRD v0.10 (text 9b4bbcfbb9; ratified-text half SIGNED by `3.0.0_SA_CVO~Z` @314290bab3, `prd-signoff` ADMITTED), FWD-23 to FWD-29, Andrew-direct @790786dcfc, the CRO's brief `docs/briefs/mcportal-entitlement-add-subtract-brief-20261020.md` @542fb0983f (findings F1-F8). The CTO's cut instruction (file ferry 17:50Z, broker down): "cut the round from the cured text, thread first: subtract and restore for one person, with FWD-29", and the CVO's note: a test that the writer REFUSES a WIDENING confirm from a non-owner master_admin principal. The earlier PD hold (CTO msg 34212 / OG-cp-1 and Andrew's sitting) does not bar this round: the CTO's cut instruction names these surfaces and I read it as lifting the hold for them; MP-pd-1..6 stand as built.

## OGW1.0 WHAT IS MEASURED BEFORE THE CUT (issuer, ~18:0xZ)

- mcportal DEV `21ad404`: `src/pages/people/` already holds `PersonAccessView.tsx` (channel and tool switches, stop/restore, the person's history), `PersonAccessPanel.tsx` (reads the record and history, posts one change, re-reads) and `personAccess.ts`; `PAGES` in `src/shell/pages.ts` has 12 entries, People last; `public/routes.json` lists 13 paths; there is no `/opalgateway`. `PeoplePerson` carries `tier` and `principal {tid, oid}`; `PersonChange` carries action, when, who, verdict, before, after.
- Writer `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`: `_set_person_access` exists (source since f40bf7dded5); the DEPLOYED build has none (CRO F4). Tests at base: 35 pass, 1 FAIL. The failing test `test_person_access_refused_when_record_kind_not_live` expects the staged live closure NOT to know `person_access`; the live gateway (13917ef993) now does (OG-cp-1 landed), so the test is stale, not the writer.
- The writer accepts only the verified owner's header (`_verify_owner_header`), so a non-owner principal is already refused before any store call; no writer path asks for a WIDENING confirm.
- Gateway side (NFRA_OPLGTW, `2.0.0_SA_COO~O`): the mount of `admin_people_access.routes` is `OG-mp-1`, in batch17; FWD-29's single admission rule is theirs.

## OGW1.1 CELL `MP-zo-1` -- the /opalgateway page: pick a person, see their reach, subtract, restore, stop (page chain; LOCAL; FWD-23, 24, 25, 27)

A new route `/opalgateway` (label `Opal Gateway`), appended last in `PAGES` after People, listed in `public/routes.json`, registered in `App.tsx`. It reads `GET /api/admin/people` (the same loader as People) and lists each person with a principal; the picked person's section shows tier, how, and the channels and tools exactly as the people data lists them (the gateway's own admission chain, never a retyped rule), and hosts the EXISTING `PersonAccessPanel` for that person (its switches subtract and restore; its button stops and restores). LAST-ADMIN GUARD (FWD-27): when the picked person's tier is `master_admin` and no other listed person has tier `master_admin`, the stop control is disabled with the text `This is the last master admin; the page will not stop it.` and no request is sent. The People page gains a link per person into `/opalgateway`. Fixture tests only (the served handler is owner-gated and the mount is `OG-mp-1`).

## OGW1.2 CELL `MP-zo-2` -- the audit list on /opalgateway (page chain, after MP-zo-1; LOCAL; FWD-28)

A section on `/opalgateway` listing every access change for every person, newest first, from `GET /api/admin/changes` (the writer's own table): when, who, action, verdict, and the before and after. An entry with no `who`, `when` or `action` is shown with the label `unattributed`, never with an owner label (the negative arm of FWD-28).

## OGW1.3 CELL `MP-zo-3` -- the writer: a WIDENING needs the verified owner's confirm; the stale test repaired (writer chain; risk WORLD by the path floor only, nothing deploys; FWD-26 writer side, CVO note)

In `_set_person_access`: a change that ADDS an entry to `tools_allow` or `channels_allow` (against the prior record) is a WIDENING; it needs `widening_confirm: true` in the event, else REFUSED `WIDEN-NO-CONFIRM` after the one strong read of the prior record and before any write (amended after worker ~43's row Z-W43-S1: a widening is defined against the prior record, so it cannot be refused with zero store calls); with it, and the verified owner header, it is WRITTEN and the record and audit item carry `widening_signoff {confirmed_by, at}`. Subtract, restore, stop and restore-person are not widenings and need no confirm. A non-owner principal (a master_admin that is not the owner) is refused by the header check before any store call: a test proves it for a widening confirm. The stale test is repaired in place (it monkeypatches `POLICY_RECORD_TYPES` without `person_access`, so it tests the writer's refusal, not the live closure's vintage). The three-halves path for non-owner widenings is NOT built: any non-owner widening stays refused (`NEEDS-HALVES` is a later cell with FWD-26's add, after NFRA_OPLGTW round 48).

## OGW1.4 EDGES, SEQUENCE AND WHAT THIS CUT DOES NOT CLAIM

- Two chains by write set: the page chain (`MP-zo-1` then `MP-zo-2`, mcportal) and the writer chain (`MP-zo-3`, the Lambda directory). `fanout: 2 of 2 chains, cap 8`.
- Not cut now (staged or later): `MP-pd-7` is re-scoped to Act A only, the writer deploy through Terraform, after `MP-zo-3` drains (the gateway mount is `OG-mp-1`, not this seat's); the page reaches the host in a bundle release that pins the mcportal commit (rides NFRA_OPLGTW's batch, as GWZ1.5); the close run (FWD-24, 25, 29 driven on a test principal, then one call through the served gateway) is cut when the mount, the writer deploy and the bundle are live, and supersedes `MP-pd-8`.
- Deferred, stated: FWD-26 add and the WIDENING label wait on NFRA_OPLGTW round 48; `portal_channels` in the writer's change shape (CRO F7) lives in the gateway's `ScopeChange`, which the Lambda stages from the live gateway release, so it is a NFRA_OPLGTW cell, not a writer-only edit; the last-admin guard counts `master_admin` tiers in the people list and cannot see other people's stopped flags (conservative: a listed master_admin counts as active).
- Nothing here is graded against the served gateway: both page cells and the writer cell prove on fixtures and fakes; the served proof is the close run.
