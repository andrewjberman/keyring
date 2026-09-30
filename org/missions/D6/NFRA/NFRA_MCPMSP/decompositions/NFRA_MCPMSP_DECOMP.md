# NFRA_MCPMSP -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD

```json
{
 "project": "NFRA_MCPMSP",
 "directive": "D6",
 "macro": "NFRA",
 "fabric": "site-z",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md@c2f5d5a071",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO~O (current by ENDPOINT hash; v0.2-v0.3 wording under proportionate sign-off)", "brief": "SIGNED (auto) CRO-authored brief"},
 "author": "2.0.0_SA_COO~MS",
 "round": 1,
 "rectangle": "the FWD-1 thread's hops (PRD Canonical handoff hops 0-5)",
 "cells": 10,
 "chains": 4,
 "join_cells": 1,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MS`. **Input:** PRD v0.3 @`c2f5d5a071` (C5 v0.2-v0.3, C2 v0.3; NFRA_MCPORTAL v0.4 C4 addendum at the same commit), ADMITTED by `prd-signoff.py status`. **Frozen at the
cut.** A cell that looks wrong mid-round is a surprise row, never an edit.

**Rulings reaching every cell:**
- ONE gateway, extended in place at `infra/aws/ec2/opal-gateway/` (C1). No second server, no fork.
- A firm asker's fetch runs under that firm's role, assumed per request (C5 v0.2: the firm bucket AND the firm's key
  prefixes in `opal-data-portal-v2`, other firms denied). Round 1's gateway zero-read covers `opal-data-inf` and
  `opal-data-cot` only; its `opal-data-portal-v2` read for opal-internal askers stays (C5 v0.3, CTO msg 26956).
- The tenant registry is `POLICY#TENANT#<tid>` in `gateway-access-state-table`, inside the existing `POLICY#`
  LeadingKeys guard (precedent `POLICY#EMAILDENY#<sha>`, `app/access_state.py:62`); record type `tenant_firm` in
  `org/standards/NFRA_OPLGTW_CONTRACT.json`. The gateway only READS it; the one writer is the MCPORTAL grant writer's
  `register_tenant` op (MCPORTAL v0.4 C4 addendum, CTO msg 26956).
- Every refusal is logged in the gateway's existing audit record; the message text is never stored (C4).
- Every new name is `lib/opal_naming.py` output. Measured at the cut: `name('gateway','inflection','firm-reader','role')`
  = `gateway-inf-firm-reader-role`; `address('gateway','inflection','bronze','msp_runs',<date>)` =
  `s3://opal-data-assets/gateway/inflection/bronze/msp_runs/<date>`. Both resolve with no registry row.
- Read when opened, never an alert (C10). No push by any worker (G-PUSH). No vendor call.

**Cross-project sequencing (PRD "Sequencing against siblings"; measured at the cut):**
- (a) `MS-t-3` writes `opal_ai/opal/runtime/{launcher,launch-gate}.ps1` and `provision/*.ps1`, which NFRA_OPALAI's
  `OA-t-3` round-2 order (status `pending`) also writes. `MS-t-3` spawns only after that order is terminal.
- (b) `MS-w-1` writes `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/**`, NFRA_MCPORTAL's writer. Its open
  orders on that surface: `MP-a-2` complete; `MP-c-1` and `MP-v-1` staged and deliverables-only. No overlap at the cut.
  The N1 addendum (MCPORTAL v0.4) grants those paths to this cell for the `register_tenant` op alone.
- (c) `MS-t-1` writes `app/asker_scope.py`, `app/audit.py`, `app/config.py`, `app/tenant_registry.py` (new),
  `app/firm_role.py` (new). No non-terminal sibling order names those files at the cut. The open gateway writers
  (NFRA_MCPINDEX `app/integrations/**`, `app/data_entitlement.py`, `app/access_state.py`; NFRA_OPLGTW
  `ops/`, `tests/acceptance/`) are disjoint.
- (d) `MS-d-1` releases the gateway. It spawns only when no other project's gateway deploy entry is open, and it ships
  a NARROW release (the deployed commit plus NFRA_MCPMSP's gateway commits only: MS-t-1 and MS-t-5), per the MCPORTAL MP-d-1 precedent.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  handoff hops (PRD "Canonical handoff") ......................................................... 6
    0 federated-chat probe (S1, A0)     1 tenant registry + router + refusal-log minimum (S2, S4)
    2 Inflection firm role + gateway zero read (S5, A1n)     3 advisor pilot grant via MCPORTAL writer (S6)
    4 supervised pilot session under its own account + run-record minimum (S8, S9)     5 one live question (A1)
  minus hop 5: the COO's ONE REAL RUN at close, not a cell ............................................ -1
  minus hop 0: the ISSUER's probe act before the cut (worker has no Teams reader), not a cell ....... -1
  hop 2 split by act: build / apply ..................................................................... +1
  hop 3 split by act: writer op build / apply ........................................................... +1
  hop 3 plus the gateway admin handler that carries Andrew's approval to the op (the view is FWD-4's) ...... +1
  hop 4 split: harness files / run-record shipper / account provisioning on the box .................... +2
  plus the gateway release that makes hop 1 live on the served host .................................... +1
  -----------------------------------------------------------------------------------------------------------
  CELLS IN ROUND 1 ........................................................................................ 10
```

(Hop 1's code, and the audit-allowlist gap row NFRA_OPALAI-Z-W2-S2 the PRD sends to L5, are one cell: both land in
the gateway's asker path and are graded by one test run. 6 - 1 - 1 + 1 + 1 + 1 + 2 + 1 = 10.)

**The unscoped control.** Read from the 14-row manifest: S1 -> the issuer's probe; S2 + S4 (minimum) -> MS-t-1; S5 ->
MS-t-2 + MS-a-1; S6 -> MS-w-1 + MS-t-5 + MS-a-2 (the grant, through the existing `widen`, and the approval itself are Andrew's acts at
the close); S8 -> MS-t-3 + MS-a-3; S9
(minimum) -> MS-t-4. **Outside round 1 by the handoff's own words:** S3 in full (the domain half of the sender gate
and the agent-side no-reply, FWD-3), S4's listing and approval view (FWD-4; mcportal surface, CVO~O N2), S7 (keys,
FWD-8), S10-S14. Read from the acceptance matrix: A0, A1 and A1n are this round's; A2-A11 are enrichment.

**Status vocabulary:** `MEASURED` (evidence in hand at the cut, instrument named), `DECLARED` (the PRD or a ruling
asserts it; not independently measured here), `NOT-EVALUATED`, or `N/A`.

---

## 2. THE RECTANGLE -- 10 cells

Measured on site Z at CLOUD HEAD, 2026-09-30 ~06:1xZ, unless stated.

| cell | hop | what is built | current state | existing work carried | risk |
|---|---|---|---|---|---|
| `MS-t-1` | 1: S2 + S4 min | `app/tenant_registry.py` (new): `firm_of(tid)` reads `POLICY#TENANT#<tid>` through the existing store (strong read, fail closed; an absent row is `None`, an unreadable store raises); `app/asker_scope.py`: `resolve_asker_class` returns `("opal-internal","")` for Opal's tenant, `("firm", <firm>)` for a registered tenant, and refuses an unregistered one `asker_tenant_denied`, now writing ONE refusal entry (ts, tid, oid, display name, chat id, reason code; never the text); a firm asker's fetch goes through `app/firm_role.py` (new): `fetch_capped(firm, key)` assumes `FIRM_ROLE_ARNS[firm]` (config, empty by default = refuse), caches the credentials until expiry, enforces query_v0's byte cap, and never falls back to the gateway identity; `app/audit.py`: `_ARGS_ALLOWLIST` gains `opal_asker_query` (`asker_oid`, `key`, `verdict`, `bytes`) and the refusal entry's fields (row NFRA_OPALAI-Z-W2-S2); `app/config.py`: `FIRM_ROLE_ARNS` | `MEASURED`: `asker_scope.py:226-233` returns opal-internal or None, "no tenant-to-firm registry"; `query_v0.py:58` fetches `opal-data-portal-v2` with the gateway identity; `audit.py` allowlist is fail-closed for an undeclared tool | `access_state` store, `catalog_gate` rule 5 (firm scope by key segment), `query_v0._fetch_capped` cap | WORLD (floor: gateway code under `infra/`) |
| `MS-t-2` | 2: S5 build | `infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf` (new): role `gateway-inf-firm-reader-role` (name() output), trust = the gateway instance role only; allow `s3:GetObject` on `opal-data-inf/*` and `opal-data-portal-v2/platinum/mdpf/inflection/*`; explicit Deny on `opal-data-cot`, `opal-data-bd`, `opal-data-49financial` and on `opal-data-portal-v2` outside the Inflection prefix; the gateway role gains `sts:AssumeRole` on exactly that one ARN | `MEASURED`: no firm role exists in the tree; `name()` resolves the role name with no registry row | the cross-firm rule's two shapes (CLAUDE.md NEVER) | WORLD (floor) |
| `MS-a-1` | 2: S5 apply | `safe-apply` of `MS-t-2` targeted to `mcpmsp_firm_roles.tf`, under a C12 ledger entry (blast radius: one role, one trust, one AssumeRole grant); the LIVE arms by `iam simulate-principal-policy`: Inflection role reads its prefix ALLOWED, reads `opal-data-cot/*` DENIED, reads `opal-data-portal-v2/platinum/mdpf/cottonwood/*` DENIED; gateway role `sts:AssumeRole` on the one ARN ALLOWED; gateway role reads of `opal-data-inf/*` and `opal-data-cot/*` DENIED (A1n v0.3) | `NOT-EVALUATED`: the gateway role's live reach on `opal-data-inf`/`opal-data-cot` (read by the cell; if either reads ALLOWED today, the remedy is a Deny in `mcpmsp_firm_roles.tf` plus a row, never an edit of another file) | the existing gateway role | WORLD |
| `MS-w-1` | 3: S6 build | in the MCPORTAL grant writer, the op `register_tenant {tid, firm}` (MCPORTAL v0.4 C4 addendum): owner-verified exactly as narrow and widen; writes the `tenant_firm` record at `POLICY#TENANT#<tid>` with a condition (absent, or already the same firm); refused before any store call unless `firm` is in the writer's `LIVE_FIRMS` config (empty by default: C11) and is one of `inflection`, `cottonwood`; a row already naming another firm refuses; one record item per outcome in the writer's changes table | `MEASURED`: the writer's actions are `narrow|widen|revoke` (`lambda_function.py`, BAD-ACTION refusal otherwise); the store's namespaces are `POLICY#<tid>#<oid>`, `RUNTIME#...` and the `EMAILDENY` precedent | the writer's owner verification and changes table | WORLD (floor) |
| `MS-t-5` | 3: S6 caller | `app/admin_tenants.py` (new): `POST /api/admin/tenants/{tid}` with body `{firm}`, behind the existing owner gate, invokes the writer's `register_tenant` with the request's forwarded owner header on `admin_grants.invoke_grant_writer`'s pattern; the gateway writes nothing itself | `MEASURED`: `admin_grants.py:137-175` invokes the writer for narrow/widen and relays its verdict | `owner_gate`, `admin_grants.invoke_grant_writer` | WORLD (floor) |
| `MS-a-2` | 3: S6 apply | the writer's package build and `safe-apply` targeted to `mcportal_grant_writer.tf` under a ledger entry; the live refusal: the new op with `LIVE_FIRMS` empty refuses before any store write | `NOT-EVALUATED`: the writer's deployed package hash at the time | MP-a-2's apply path | WORLD |
| `MS-t-3` | 4: S8 files | in `opal_ai`: an `account_name` config key read by `provision-account.ps1`, `verify-boundary.ps1`, `launcher.ps1` and `launch-gate.ps1` (default `Opal_Agent`; behaviour unchanged when absent); `opal/runtime-msp/` (new): `CLAUDE.md` (the partner Analyst: answers only through `opal_asker_query`, states the data's date, sends nothing on a refusal), `.claude/settings.json` (the same fence), `mcp.json.example` (ONE server, the gateway, signed in as the Opal Analyst user), `provision/runtime.msp.config.example.json` (`account_name` `Opal_MSP`) | `MEASURED`: the four scripts hard-code `$AccountName = 'Opal_Agent'` (opal_ai DEV @fd8ab8a57f) | NFRA_OPALAI's harness (C8: reused, not re-owned) | LOCAL. HELD on sequencing (a) |
| `MS-t-4` | 4: S9 min | `opal_ai/opal/runtime-msp/record/ship-run.py` (new), run by the OPERATOR: for one run window it collects the `Opal_MSP` session transcript and the gateway audit rows for that window and calling identity, tags them `{firm, advisor_oid, run_id}`, and writes them under the `address()` output above; dry run by default, `--write` to put | `N/A` (new) | the audit lake (`audit.py` `AUDIT_S3_BUCKET`) | LOCAL (its criteria run on fixtures) |
| `MS-a-3` | 4: S8 live | on the site-Z box, in an elevated session: `provision-account.ps1 -Config <msp config>` creates `Opal_MSP`; `verify-boundary.ps1` AS `Opal_MSP`: the workspace probe read DENIED, the state dir writable; `launch-gate.ps1` AS `Opal_MSP` prints `GATE: PASS` against the opal_ai PROD checkout | `NOT-EVALUATED`: an elevated session on the box (G-ADMIN) | OA-t-2's scripts | WORLD (a device account) |
| `MS-d-1` | 1 live | the NARROW gateway release: the deployed commit plus NFRA_MCPMSP's gateway commits only; the host `.env` gains `FIRM_ROLE_ARNS={"inflection": <MS-a-1's ARN>}`; NEVER-2 entry naming every task family the tag moves; post-act reads: health, `opal_asker_query` listed, the boot log shows `FIRM_ROLE_ARNS` with one key | `NOT-EVALUATED`: the deployed commit at the time | `safe-ec2-deploy.sh`, `EC2_MANIFEST.json` | WORLD |

**Load-bearing `DECLARED` / `NOT-EVALUATED` rows, stated:** (a) catalog_gate rule 5 admits `("firm","inflection")` on
`platinum/mdpf/inflection/*` by key segment: DECLARED from `catalog_gate.py:98-120`; MS-t-1's test measures it. (b) The
calling identity in the pilot is the Opal Analyst user (G-USER), an `opalinvest.com` address, so `query_v0._principal`
reads it opal-internal (`query_v0.py:82-92`) and the second gate passes: DECLARED until G-USER exists. (c) The gateway
role's live reach on the firm buckets: NOT-EVALUATED (MS-a-1).

---

## 3. THE CELLS -- 10 (round 1)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1: prefix `MS`; axis `t` = thread build, `a` = apply or live
act, `w` = the MCPORTAL writer, `d` = deploy.

| cell | serves | writes | reads (never writes) |
|---|---|---|---|
| `MS-t-1` | FWD-1, FWD-2, FWD-3 (min) | `infra/aws/ec2/opal-gateway/app/tenant_registry.py`, `.../app/firm_role.py`, `.../app/asker_scope.py`, `.../app/audit.py`, `.../app/config.py`, `.../tests/test_mcpmsp_asker_firm.py` | `app/access_state.py`, `app/data_entitlement.py`, `app/query_v0.py`, `app/graphql_plumbing/catalog_gate.py`, `app/context.py` |
| `MS-t-2` | FWD-1, FWD-2 | `infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf` | the gateway role's Terraform, `lib/opal_naming.py` |
| `MS-a-1` | FWD-1 (A1n) | `org/critical_paths/change_management/<entry>.md`, `org/critical_paths/.open_deploys/<slug>.json`, the applied IAM plane (WORLD), its deliverables | `mcpmsp_firm_roles.tf` |
| `MS-w-1` | FWD-1, FWD-4 (min) | `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`, its `tests/` | `app/access_state.py`, `app/data_entitlement.py`, `org/standards/NFRA_OPLGTW_CONTRACT.json` |
| `MS-t-5` | FWD-1, FWD-4 (min) | `infra/aws/ec2/opal-gateway/app/admin_tenants.py`, `.../tests/test_admin_tenants.py` | `app/admin_grants.py`, `app/owner_gate.py`, `app/admin_api.py` |
| `MS-a-2` | FWD-1 | ledger paths, the applied writer (WORLD), its deliverables | `mcportal_grant_writer.tf`, the writer package |
| `MS-t-3` | FWD-1, FWD-9 (base) | `opal_ai/opal/runtime/launcher.ps1`, `.../launch-gate.ps1`, `.../provision/provision-account.ps1`, `.../provision/verify-boundary.ps1`, `opal_ai/opal/runtime-msp/**` except `record/` | `opal_ai/opal/agent/**` |
| `MS-t-4` | FWD-5 (min) | `opal_ai/opal/runtime-msp/record/**` | `app/audit.py` (the lake key shape) |
| `MS-a-3` | FWD-1 | the box's local account plane (WORLD), its deliverables | the opal_ai PROD checkout |
| `MS-d-1` | FWD-1 (live) | `infra/aws/ec2/EC2_MANIFEST.json`, ledger paths, the served host (WORLD) | `safe-ec2-deploy.sh`, `deploy-to-ec2.sh` |

**Fixed names across cells:** the key `POLICY#TENANT#<tid>` (sk per `access_state.policy_key` convention, set by
MS-w-1 and read by MS-t-1 from one constant each side); the config keys `FIRM_ROLE_ARNS` (gateway) and `LIVE_FIRMS`
(writer); the role `gateway-inf-firm-reader-role`; the account `Opal_MSP`; the refusal reason code
`asker_tenant_denied`; the record prefix `gateway/<firm>/bronze/msp_runs/`.
**Hookups (belong to no cell; the issuer adds them at the merge):** `MS-t-5`'s router registration line in
`app/admin_api.py`.

---

## 4. PLACEMENT AXIS

**Every cell executes on SITE Z.** Served by `0.9.0_WK_NFRA_MCPMSP~<n>`. The opal_ai cells get a nested `opal_ai`
worktree through `wk-provision.sh --nested opal_ai=<DEV ref>`. `MS-a-3` needs an elevated session on this box
(G-ADMIN).

---

## 5. DEPENDENCY EDGES AND CHAINS

```
  chain A   MS-t-1                          the gateway's asker path
  chain B   MS-t-2 --> MS-a-1               the role built, then applied (A1n live)
  chain C   MS-w-1 --> MS-t-5, MS-a-2       the op built; then its gateway caller, and its apply
  chain D   MS-t-3 --> MS-t-4 --> MS-a-3    harness files, the shipper beside them (same nested repo), then the account
  JOIN      {MS-t-1, MS-t-5, MS-a-1} --> MS-d-1   the release ships the asker path, the tenants route and the role's ARN
```

**CHAINS: M = 4**, pairwise disjoint in write set, plus the join cell (chains counted without the join, per the
NFRA_MCPORTAL v1 precedent). **Fan-out:** `N = 4 of M = 4 chains, cap 8; join_cells: 1 (MS-d-1)`. At the cut, spawn `~1`
(MS-t-1, then MS-d-1 at the join) and `~2` (MS-t-2, then MS-a-1). Spawn `~3` (MS-w-1, then MS-t-5, then MS-a-2) at the
cut (the N1 addendum landed @c2f5d5a071). Spawn `~4` (MS-t-3, then MS-t-4, then MS-a-3) when OA-t-3's round-2 order is terminal.

---

## 6. BATTERY DISPOSITION (a thread round)

- **`comp-adversary` -- DECLARED-NOT-APPLICABLE:** thread round; the lens runs on the enrichment round that touches its
  surface.
- **`comp-schedule` -- DECLARED-NOT-APPLICABLE:** thread round. No cell arms a cron, alarm, monitor or cadence; the
  daily page and sample are enrichment (FWD-6, FWD-7).
- **`comp-iam` -- RUN, because the thread touches IAM (MS-t-2/MS-a-1), and its instrument is the cell's own:**
  MS-a-1's simulations of the Inflection role (own prefix ALLOWED, other firm's bucket and prefix DENIED) and of the
  gateway role (one AssumeRole ALLOWED, the ruled firm reads DENIED). Blindness stated: this lens sees the two roles
  and the named resources, not the rest of the account, and the writer's own role (MS-a-2) is unchanged by this
  round.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE.** Six hops, minus the close run and the issuer's probe, plus four splits by act or repo, the approval's
gateway caller and one release, gives ten cells, falsified against the 14-row manifest and the 12-row acceptance matrix (section 1). No file has two
writers: MS-t-3 and MS-t-4 share the `opal_ai/opal/runtime-msp/` tree but split it at `record/`, and they are one slot.

**(ii) SAME GRAIN.** Each cell is one hop adapter, graded by its built behaviour, a seam probe against its real
neighbour where reachable (the naming builder, the live IAM plane, the writer, the box's account plane, the served
host), and at most one further check.

**(iii) INTENT COHERENCE.** One axis: a named Inflection advisor asks in a one-to-one Teams chat and is answered from
Inflection's own figures, read under Inflection's role. Out of scope: Cottonwood, the domain half of the sender gate,
the onboarding view, replay beyond the minimum, keys, the daily page and sample, production.

**(iv) STATE COHERENCE -- what each remedy does NOT move.**
- `MS-t-1` adds the firm branch. It does NOT move an Opal-tenant asker's path, query_v0's own principal, any grant, or
  the gateway identity's reads for opal-internal askers.
- `MS-t-2` builds and names. It creates no resource.
- `MS-a-1` creates one role, one trust and one AssumeRole grant. It does NOT move the gateway role's existing reads
  beyond the `opal-data-inf`/`opal-data-cot` Deny A1n v0.3 names.
- `MS-w-1` adds one op. It does NOT move narrow, widen, revoke, the owner key or any existing record.
- `MS-t-5` adds one owner-gated route. It does NOT move any existing route or guard.
- `MS-a-2` ships the writer. `LIVE_FIRMS` stays empty, so no tenant row can be written until G-FIRM.
- `MS-t-3` adds a config key whose absence keeps `Opal_Agent` exactly as it is.
- `MS-t-4` writes nothing without `--write`.
- `MS-a-3` creates one local account. It does NOT touch `Opal_Agent` or its credential.
- `MS-d-1` ships. It does NOT change Terraform, the host or its role.

---

## 8. GATES AND THE CLOSE RUN

- **HOP 0 -- the issuer's probe (A0), not a cell.** With an outside test account (G-OUTSIDE), one one-to-one chat to an
  Opal user; the issuer reads it through the gateway's Teams reader and records the sender's `tenantId` and `id`, and
  whether the chat's member list carries the outside sender's email (the input FWD-3's domain check will need).
  Artifact: `deliverables/2.0.0_SA_COO~MS/round1/A0_PROBE.md`. If the reader cannot see the chat, the finding goes to
  `1.0.0_SA_CTO~O` before `~4` spawns (the harness is the only cell that builds on the channel).
- **G-OUTSIDE:** Andrew's word for an outside test account and one message from it. Holder: Andrew.
- **G-N1, G-A1N:** SATISFIED (CTO msg 26956; PRD v0.3 and MCPORTAL v0.4 @c2f5d5a071).
- **G-ADMIN:** an elevated PowerShell session on the site-Z box for MS-a-3. Holder: Andrew.
- **G-USER, G-IT-INF, G-ADVISOR, G-FIRM:** PRD gates, external acts. Holder: Andrew (with Opal IT and Inflection's IT).
- **G-PUSH:** opal_ai DEV -> PROD (the launcher checks out PROD) and every shared-branch push. Holder:
  `0.0.0_AB_MSTR~Z`, on Andrew's word.
- **G-LEDGER:** MS-a-1's, MS-a-2's and MS-d-1's entries, each the acting worker's own.
- **The close run (A1 + A1n's live arm 4):** after G-USER, G-IT-INF, G-ADVISOR and G-FIRM: `LIVE_FIRMS` gains
  `inflection`; Andrew registers Inflection's tenant (`POST /api/admin/tenants/{tid}` from his signed-in dashboard
  session; the approval view itself is FWD-4's) and grants the named advisor through the Entitlements tab's `widen`; the advisor asks one real question in a one-to-one chat with the Opal Analyst user; the supervised
  `Opal_MSP` session answers from `platinum/mdpf/inflection/`, stating the data's date, matching the portal for the
  same item; the gateway's audit shows the fetch under `gateway-inf-firm-reader-role`; MS-t-4 ships the run; and the
  G-OUTSIDE account's next message (an unregistered tenant) is refused with one refusal entry. Artifact:
  `deliverables/2.0.0_SA_COO~MS/round1/`.

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. No cell has been exercised; every target state is a specification.
2. A0 is not measured; the pilot channel's viability rests on it.
3. An `opalinvest.com` asker who writes to the Opal Analyst user is still served at their own grant through the
   existing opal-internal branch; C3's "Opal staff take the refusal path in the pilot" is the FWD-3 enrichment's
   (sender gate in full), not this round's.
4. The gateway identity's reads of firm prefixes in `opal-data-portal-v2` for opal-internal askers are unchanged (C5
   v0.3's named residual); their removal is an enrichment behind an internal reader role and never-widen sign-off.
5. Cottonwood, the domain gate, the onboarding view, keys and caps, the daily page and sample, and production are
   enrichment.

---

# ROUND 2 -- THE ENRICHMENT CUT (L5, v2)

```json
{
 "project": "NFRA_MCPMSP",
 "decomp_version": "v2",
 "step": 5,
 "round": 2,
 "input": "org/missions/D6/NFRA/NFRA_MCPMSP/ledger/ROUND_ANALYSIS.round1.md@5e2ff94c28 (section 4, E1-E5)",
 "prd_ref": "org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md@7ecc812be5 (v0.4; ratified-text SIGNED current)",
 "author": "2.0.0_SA_COO~MS",
 "cells": 13,
 "chains": 6,
 "join_cells": 3,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~MS`. **Input:** the CTO's round-1 analysis @5e2ff94c28, section 4, cut in ONE issuance; two CTO
rulings at the cut: msg 27414 (E1's Deny: option (a) -- MCPMSP owns the internal role, NFRA_MCPINDEX routes its own two
readers; the Deny cell is HELD until every gateway-identity reader of `opal-data-portal-v2` is routed) and msg 27416
(`MSP_CALLING_IDENTITIES`, empty by default, scopes the pilot refusal to the MSP calling identity; the account is
Andrew's -- gate G-MSPID). Round 1 (sections 1-9 above) stays frozen as its own record.

## R2.1 GROUND TRUTH MEASURED AT THE CUT (site Z, CLOUD, 2026-09-30 ~22:3xZ)

- The gateway runs `42c52ed4d9` (EC2_MANIFEST @3a67e6fcf2; NFRA_MCPINDEX MX-r-6). Every round-2 release is NARROW from
  the deployed commit re-read at its own spawn.
- The gateway identity reads `opal-data-portal-v2` through: `app/query_v0.py:58` (`_fetch_capped`, also the
  opal-internal asker fetch), `app/integrations/portal_index/integration.py:273-275` and
  `app/integrations/opal_discover/integration.py:228` (default boto3 client; NFRA_MCPINDEX's paths). The grant is
  `infra/aws/terraform/opal-gateway/queryv0-iam.tf` (`gw_queryv0_portal_read`: `json/*`, `platinum/*`), plus
  `daily-reports-iam.tf` (`daily-reports/*`).
- Builder names (no registry row needed): `gateway-global-internal-reader-role`, `gateway-global-internal-reader-policy`,
  `gateway-global-internal-assume-policy`, `gateway-firm-deny-policy`.
- The gateway test fixture that writes audit to a temp file (`tests/conftest.py`, MP-f-1 @31b9d1975e) is on CLOUD but in
  NO deployed commit (`093fc247c6`, `4ce7946426`, `42c52ed4d9` all lack `_AUDIT_FILE`), so a narrow release tree's suites
  dirty the tracked `audit.jsonl` (R-5). The parent `mcportal` gitlink is `fa1ff9693b` (README only) while the manifest's
  `mcportal_commit` is `a3bff71ffa` (R-4).
- Sibling orders open on overlapping gateway paths at the cut: NFRA_MCPINDEX MX-t-10, MX-t-12 (`tests/test_portal_index.py`),
  MX-t-13 (`tests/test_blackdiamond.py`, `tests/test_entitlement_admin.py`). No round-2 cell writes those files;
  none writes `deploy-to-ec2.sh` but MS-r-1 and MS-d-2 (one slot).
- `Opal_Agent`'s Claude is signed into the gateway as `opalbloomberg@opalinvest.com` (G-ACCT step 6); the operator launch
  recipe that gives a typeable window is `.NET Process.Start` from a Medium-integrity shell
  (`C:\Users\Opal Bloomberg\.opal_runtime\G-ACCT_STEP6_RESULT_20260930.md`).

## R2.2 THE CELLS -- 13

| cell | from | builds / runs | write surface | risk |
|---|---|---|---|---|
| `MS-c-1` | E1 | the reader census: every S3 read the gateway identity makes of `opal-data-portal-v2` (code call sites with bucket/prefix; the live policies on `opal-gateway-role`), printed with its denominator; and the DELTA question set: a fixed list of firm-scoped catalog keys whose served bytes (sha256) are captured on the host today, through the existing path, as E1-z's baseline | its deliverables only | WORLD (reads the served host over SSM) |
| `MS-e1-t` | E1 | `infra/aws/terraform/opal-gateway/mcpmsp_internal_reader.tf`: the internal reader role (module `opal_name`, scope `global`), its policy = today's `gw_queryv0_portal_read` resources on the builder bucket, trust = the gateway role, the gateway's one AssumeRole policy; and `mcpmsp_gateway_firm_deny.tf`: an explicit Deny for `opal-gateway-role` on the firm-segment keys the census names (written now, applied only by MS-e1-z) | the two `.tf` files | WORLD (floor) |
| `MS-e1-a` | E1 | targeted `safe-apply` of the internal role, its policy and the gateway's AssumeRole policy ONLY (never the Deny file's resources); live simulate: internal role reads a firm key and a global key ALLOWED; gateway AssumeRole on it ALLOWED | ledger paths | WORLD |
| `MS-e1-g` | E1 | `app/internal_role.py` (new): the opal-internal S3 client assumed from env `INTERNAL_READER_ROLE_ARN` (unset = today's client, so a release before the role exists moves nothing); `query_v0._fetch_capped` reads through it; tests | `app/internal_role.py`, `app/query_v0.py`, `tests/test_mcpmsp_internal_role.py` | WORLD (floor) |
| `MS-e1-z` | E1 | the Deny: HELD. Spawns only when (i) the census at its own cut prints every gateway-identity reader of `opal-data-portal-v2` routed (first criterion, with its denominator -- CTO 27414), (ii) the never-widen pair (CTO half + COO half) names the blast radius, (iii) MS-d-2 is live. Applies `mcpmsp_gateway_firm_deny.tf`; DELTA=0 on MS-c-1's question set after vs before; one JUDGMENT criterion (Rule J): `3.0.0_SA_CVO~O` grades the internal Analyst's and `/query/v0`'s served figures, dates and coverage unchanged | ledger paths | WORLD |
| `MS-e2-g` | E2 | `app/sender_gate.py` (new) + `asker_scope.py`: the sender's address from the chat's member list (the member whose `userId` is the sender oid), Andrew's four allowed domains, the domain must match the tenant's registered firm (`opalinvest.com` = Opal's tenant), guest-form (`#EXT#`) refused, `opalinvest.com`/`49financial.com` senders refused `asker_pilot_scope` ONLY when the calling identity is in `MSP_CALLING_IDENTITIES` (env, empty default); the refusal entry gains `sender_email`, `sender_domain` (C4, no text); `audit.py` allowlist; tests | `app/sender_gate.py`, `app/asker_scope.py`, `app/audit.py`, `tests/test_mcpmsp_sender_gate.py` | WORLD (floor) |
| `MS-e2-h` | E2 | the agent-side gate in `opal_ai/opal/runtime-msp/`: a PreToolUse hook on every send-message tool that allows a send only when the session transcript's most recent `opal_asker_query` for that chat returned a served answer (no `asker_scope_denied`); registered in `runtime-msp/.claude/settings.json`; fixture tests | `opal_ai/opal/runtime-msp/hooks/**`, `opal_ai/opal/runtime-msp/.claude/settings.json` | LOCAL |
| `MS-e2-v` | E2 | the live arm: gates G-MSPID and MS-d-2 live and MS-e4-r's session; Andrew sends one Teams message from `opalinvest.com` to the MSP calling identity; the session calls `opal_asker_query`; no reply; one refusal entry (`asker_pilot_scope`, sender email/domain, no text) found in the audit record; one JUDGMENT criterion (Rule J): the CVO judges from the entry and the absent reply that the refusal came from the gate | its deliverables only | WORLD |
| `MS-e3-g` | E3 | `app/admin_refusals.py` (new), owner-gated: `GET /api/admin/refusals` lists `asker_sender_refusal` entries (host audit + the audit lake), newest first, C4 fields; `POST /api/admin/refusals/approve` carries one approval to the writer -- `register_tenant` when the tid has no tenant row, then `widen` for the advisor -- relaying verdicts; the gateway writes nothing; tests | `app/admin_refusals.py`, `tests/test_admin_refusals.py` | WORLD (floor) |
| `MS-e4-r` | E4 | one replayable run: gates G-MSPID and G-MSPCL (Claude installed and signed in under `Opal_MSP`, Andrew's act) and a checkout of opal_ai DEV at `C:\opal_runtime_msp\opal_ai`; Andrew starts the supervised session with the operator recipe and asks one question; the worker ships it with `ship-run.py --write` (transcript as exported by the operator) | its deliverables only (S3 writes under the builder address) | WORLD |
| `MS-e4-x` | E4 | a second seat reconstructs the run from the record ALONE (the builder address's three objects): what was asked, what was looked up, allowed/refused, answered | its deliverables only | LOCAL |
| `MS-r-1` | E5 | batch repair: R-4 -- `deploy-to-ec2.sh` builds the dashboard from a detached checkout of the manifest's `mcportal_commit` when the workspace `mcportal` is not a real checkout; R-5 -- `tests/run_release_suites.sh` (new) runs named gateway suites with `AUDIT_PATH` pointed at a temp file | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, `infra/aws/ec2/opal-gateway/tests/run_release_suites.sh` | WORLD (floor) |
| `MS-d-2` | release | the NARROW release (join of MS-e1-g, MS-e1-a, MS-e2-g, MS-e3-g, MS-r-1): deployed commit re-read + this project's commits; item 0 the `admin_refusals` hookup in `admin_api.py`; `.env` gains `INTERNAL_READER_ROLE_ARN` and `MSP_CALLING_IDENTITIES` (G-MSPID's value, or empty); suites via `run_release_suites.sh`; MCP tool list unchanged | `app/admin_api.py` (hookup), `deploy-to-ec2.sh` (the two `.env` lines), `EC2_MANIFEST.json`, ledger paths | WORLD |

**Fixed names:** `INTERNAL_READER_ROLE_ARN`, `MSP_CALLING_IDENTITIES` (env), refusal code `asker_pilot_scope`, refusal
fields `sender_email`/`sender_domain`, routes `GET /api/admin/refusals` and `POST /api/admin/refusals/approve`,
`tests/run_release_suites.sh`. **Hookups:** `admin_refusals` in `admin_api.py` -- carried by MS-d-2's item 0 (the issuer
cannot write `infra/aws/**`, measured at round 1).

## R2.3 DEPENDENCY EDGES AND CHAINS

```
chain A   MS-c-1 --> MS-e1-t --> MS-e1-a           the census names the Deny keys; the role is applied from the tf
chain B   MS-e1-g                                  the query_v0 route
chain C   MS-e2-g                                  the gateway sender gate
chain D   MS-e3-g                                  the refusal routes
chain E   MS-r-1 --> MS-d-2 --> MS-e1-z (HELD)     the tooling, the release, then the Deny
chain F   MS-e2-h --> MS-e4-r --> MS-e4-x          the agent gate, the run, the replay
joins     MS-d-2 (A + B + C + D + E); MS-e1-z (d-2 + readers routed + never-widen pair); MS-e2-v (d-2 + e4-r + G-MSPID)
```

**Fan-out:** `N = 6 of M = 6 chains, cap 8; join_cells: 3 (MS-d-2, MS-e1-z, MS-e2-v)`.

## R2.4 BATTERY

- `comp-iam` -- RUN (MS-e1-a simulations; MS-e1-z's reader census + simulate on the gateway role). Blindness: the named
  roles and keys only.
- `comp-adversary` -- RUN at MS-e1-z (the census is its adversary read: any unrouted reader blocks the Deny).
- `comp-schedule` -- DECLARED-NOT-APPLICABLE: no cron, alarm or cadence.

## R2.5 RULE 24 RECORD

(i) MECE: E1-E5 = 5 items -> E1 census/tf/apply/route/Deny (5), E2 gateway/agent/live (3), E3 routes (1), E4 run/replay
(2), E5 repair (1), + the release join (1) = 13; the analysis's "NOT in round 2" list is subtracted whole. (ii) Same
grain: one adapter or one act per cell. (iii) One intent: the pilot's controls tighten -- the gateway reads no firm data
on its own identity, the sender gate is complete, a refusal is queue-able, one run is replayable. (iv) What each does NOT
move: MS-e1-g moves nothing until `INTERNAL_READER_ROLE_ARN` is set; MS-e1-a creates a role and grant, no Deny; MS-e2-g
moves no Opal-staff serving unless the calling identity is listed; MS-e3-g writes nothing itself; MS-r-1 changes no
served byte; MS-d-2 changes no Terraform.

## R2.6 GATES

- **G-MSPID** (MS-e2-v, MS-e4-r; MS-d-2 ships the value if given): the MSP calling identity -- G-USER now, or an existing
  non-person account, not Andrew's, not opalbloomberg@, not Alyssa's. Holder: Andrew (CTO 27416 asks; forwarded record).
- **G-MSPCL** (MS-e4-r): Claude installed and signed in under `Opal_MSP`, and the gateway sign-in as G-MSPID (an MFA act).
  Holder: Andrew, with the operator launch recipe.
- **G-NW-E1** (MS-e1-z): the never-widen pair (CTO half, COO half) naming the Deny's blast radius. Holders:
  `1.0.0_SA_CTO~O`, `2.0.0_SA_COO~MS`.
- **G-RDR** (MS-e1-z): NFRA_MCPINDEX has routed `portal_index` and `opal_discover` through the internal role (CTO 27414;
  MCPINDEX's first round after MX-t-10/t-12). Holder: `2.0.0_SA_COO~MI`.

## R2.7 WHAT THIS CUT DOES NOT CLAIM

1. No cell has run. The Deny's key set comes from MS-c-1's census; the MSP identity from Andrew.
2. Subtracted per the analysis: FWD-2/Cottonwood, FWD-6/7, FWD-8 (G-KEY), FWD-9..11, R-1 (parked), R-2 (laptop gate
   owner), R-3 (NFRA_MCPORTAL), the launcher fix (NFRA_OPALAI), and A1 (PARKED, v0.4).
