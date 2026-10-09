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
