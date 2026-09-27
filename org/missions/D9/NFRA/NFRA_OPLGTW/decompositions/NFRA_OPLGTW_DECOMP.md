# NFRA_OPLGTW -- DECOMPOSITION (L5) -- round 1 -- v1

```json
{
 "project": "NFRA_OPLGTW",
 "directive": "D9",
 "macro": "NFRA",
 "fabric": "laptop",
 "round": 1,
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@f0aa50dbc0",
 "prd_version": "v0.2",
 "prd_half_hashes": {"ratified-text": "908c9e9460c1cdbb3cf4fa111d5946461c1dfc074963022b3b5e43d6c00233f9 SIGNED 3.0.0_SA_CVO, current", "brief": "04461a4925dc40dcbe06c85962f6cd200dd819bacdf1a6c2251885281c798dc1 SIGNED 4.0.0_SA_CRO, current"},
 "contract_ref": "org/standards/NFRA_OPLGTW_CONTRACT.json@f0aa50dbc0 (version 1.0)",
 "ground_truth_ref": "workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/rectangle.final.certified.json@bc3f6698a82ebc658ab87df913d99fcd64522341",
 "author": "2.0.0_SA_COO~O",
 "cells": 28,
 "edges": 45,
 "chains_maximal_paths": 64,
 "components": 1,
 "cell_id_shape": "OG-<axis>-<n> (DECOMP_CELL_ID_CONVENTION shape 1)",
 "worker_serial": "0.9.0_WK_NFRA_OPLGTW~<slot>",
 "cut_head": "f5a6d57e4a",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~O`, seated by `0.0.0_AB_MSTR` (msg 96971) on Andrew-direct ~07:5xZ 2026-09-15, VERBATIM:
*"If laptop has capacity let's get mdpf_Taxsma going; then nfra_opalgt or whatever the mcp hook up new nfra project was,
then IPRT_BCKND if the lgic work is in proper position and we can address backend canonically now"* (record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_075xZ_LAPTOP_CAPACITY_ORDER_TAXSMA_THEN_OPLGTW_THEN_IRPT_BCKEND.md`,
LD-0567 @`4524cc2466`). One project, this seat. L5 is the COO's; no seat certifies this before L6.

**Input, graded before use.** `python .tools/prd-signoff.py status NFRA_OPLGTW` at 08:1xZ: v0.2 @`f0aa50dbc0` ADMITTED,
both halves SIGNED and current. `.tools/receiving-check.py` on the PRD: **ACCEPT** (`prd-manifest`: manifest, ENDPOINT,
header, outcome cards and header/section agreement present). The L4 closeout (`prd/L4_CLOSEOUT.md`) hands L5 the
certified documentary rectangle and says the COO *"must assign the named probes before using any deployment claim as
fact"*. Section 2 is that assignment, 24 of 24.
**Sequence:** `sequence-check --project NFRA_OPLGTW` reads UNPLACED, so D9's own rules govern. The box is at 3 of 3 COO
lanes, this seat counted.
**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`).

**What binds every cell, from the PRD.** Activation is `DESIGN_ONLY_NOT_A_GRANT`: the proposed profile is not an
entitlement, and no cell activates a real employee's grant. The feature flag defaults off and new grants default pending.
Unknown deployment facts are measured before they are used: no cell asserts a deployed state it did not read back. No
source data is written, deleted or rewritten, and no bucket policy is broadened.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  SURFACE MANIFEST rows (PRD s. SURFACE MANIFEST; contract surface_ids) ........ 10   S1 .. S10
  minus rows excluded, read-only or delivered at L4 ............................  -0
  ---------------------------------------------------------------------------
  SURFACES THIS ROUND'S CELLS SERVE ............................................ 10   (each has >= 1 cell, s.3)
```

**Falsifier 1: the component manifest, which is the physical grain under the ten surfaces.**
`workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/component_manifest.yaml` declares **15 units on 9 planes**.
Units a cell writes or measures: 15 of 15. The Gateway process is served by the S1/S2/S3/S5/S6/S7/S8 cells; the two
producer scripts by `OG-c-1` and `OG-c-2`; the six silver prefixes and two completion prefixes by `OG-c-2`, `OG-k-1`,
`OG-i-2` and `OG-v-3` (read only); the two reader roles by `OG-i-2`; the state table by `OG-i-1`; the ALB routes by
`OG-p-1` and `OG-i-3`; the audit sink by `OG-o-1`; the entitlement administration by `OG-z-2`; the support/withdrawal act
by `OG-o-2`, `OG-v-4` and `OG-v-5`; the acceptance set by `OG-v-1` .. `OG-v-5`.

**Falsifier 2: every path the PRD cites.** `comp-adversary compose` on the PRD (read-vintage `@de5ebb73c7`,
2026-09-15T08:18:54Z) found 7 cited repo paths: 6 stable, 1 GONE. The GONE one is `org/rfc/rfc9700.html`, which is the
tool parsing the external RFC URL in C1 as a repo path. It is not a defect.

**Falsifier 3: the new AWS names against the live plane.** `comp-find --corpus aws
'opal-gateway-access-state|opal-mcp-schwab-catalog-read|opal-mcp-emp-menachem'` reads **0 hits over 2,530 nodes**
(graph vintage 2026-09-15 08:19:46 UTC). That is a measured zero over the classes the graph models: the three resources
are new. `OG-p-1` re-reads each one by its own Describe/Get call.

**Falsifier 4: who reads what the producer cell changes.** `comp-find 'meta/complete' --files --all` finds 361 hits
across 172,084 files. The first-party SURFACED set is 4 files: `data/assets/scripts/silver/conversion_manifest.py`, its
**vendored copy** `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py`,
`infra/aws/terraform/opal-assets/advi_49f_floor.tf` and `infra/aws/terraform/opal-assets/silver.tf`.
**`silver.tf:756-759` is a live consumer:** the S3 notification `advi-49f-silver-complete-accelerator` fires on
`s3:ObjectCreated:*` under `schwab/08335338/meta/complete/`. Any marker written for that master starts the 49F gold
dispatcher. `OG-c-1` and `OG-c-2` carry it (s.3, s.6 G-B).

**Status vocabulary.** Evidence columns take four values, and NOT-EVALUATED is one of them, so non-evaluation is never
encoded as a verdict:

| value | meaning |
|---|---|
| `MEASURED` | evidence in hand at the cut, instrument named |
| `DECLARED` | the PRD, contract or rectangle asserts it; not re-measured here |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply |

Cell status takes `OPEN`, `HELD` (a named gate stands, s.6) or `DONE`. At v1: 25 OPEN, 3 HELD.

---

## 2. THE 24 BOUNDARY QUESTIONS, EACH ASSIGNED

The certified rectangle's `unverified_boundary` cells name 24 questions (S1-auth 6, S2-authorization 4, S3-data 3,
S4-query 3, S5-download 3, S6-operations 5). Assigned 24 of 24. None becomes an expected value about the world before
its cell reads it.

| # | question (short form) | cells that answer it |
|---|---|---|
| 1 | deployed bytes/config and the real OAuth transports carry the callback and browser identity | `OG-p-1`, `OG-r-1`, `OG-v-4` |
| 2 | Menachem's verified tid/oid, carried end to end | gate G-E, `OG-v-5` |
| 3 | atomic refresh, replay, restart, concurrency within the auth budgets | `OG-a-1`, `OG-v-2`, `OG-v-4` |
| 4 | the workspace owner adds or reuses the connector without replacing shared settings | `OG-o-2`, `OG-v-4` |
| 5 | the member connects, enables and completes A20 | `OG-v-5` |
| 6 | logout, reconnect, expiry, restart and legacy migration | `OG-a-2`, `OG-v-2`, `OG-r-1`, `OG-v-4` |
| 7 | effective grants, dedicated trust, no Gateway-credential fallback | `OG-i-2`, `OG-k-1`, `OG-v-4` |
| 8 | the fail-closed profile guards every entry point | `OG-z-1`, `OG-v-2`, `OG-v-4` |
| 9 | the approved scope, and invalid profile states fail closed | `OG-z-2`, gate G-E, `OG-v-4` |
| 10 | prompt-like file content stays inert (A12) | `OG-q-2`, `OG-v-1`, `OG-v-2`, `OG-v-4` |
| 11 | a producer certificate that proves a complete dataset and binds versions | `OG-c-1`, `OG-c-2`, `OG-k-1` |
| 12 | the self-contained record works through a metadata-only role | `OG-c-1`, `OG-i-2`, `OG-k-1`, `OG-c-2` |
| 13 | date alignment, units, balance overlaps, key uniqueness | `OG-q-3`, `OG-v-3` |
| 14 | assumed-role credentials, with policy checked before credentials | `OG-k-1`, `OG-z-1` |
| 15 | decimals, serialized budgets, cancellation and isolation under host limits | `OG-q-1`, `OG-q-2`, `OG-r-2` |
| 16 | aggregates, exports and hidden-field inference | `OG-q-2`, `OG-q-3`, `OG-x-1`, `OG-v-1`, `OG-v-2` |
| 17 | one principal across MCP OAuth and browser SSO; copied, expired, stale and revoked tickets | `OG-a-3`, `OG-x-1`, `OG-v-2`, `OG-v-4` |
| 18 | export parity, source binding, original-file permission, lifecycle, session trust | `OG-x-1`, `OG-v-2` |
| 19 | headroom, revocation at download start, cancellation, caps, integrity, ALB idle | `OG-i-3`, `OG-r-2`, `OG-v-4` |
| 20 | dedicated data/metadata trust and IAM ceilings under live controls | `OG-i-2` |
| 21 | deployed bytes and dependencies match, and capacity is adequate | `OG-p-1`, `OG-i-4`, `OG-r-1`, `OG-r-2` |
| 22 | enablement, audit, state and rollback preserve users and enforce revocation | `OG-o-1`, `OG-r-1`, `OG-o-2`, `OG-v-4` |
| 23 | the runbook is executable at its named moments | `OG-o-2`, `OG-v-4`, `OG-v-5` |
| 24 | the actual Claude connection meets the network/front-door clauses | `OG-i-3`, `OG-v-4` |

---

## 3. THE CELLS -- 33 (28 at v1; `OG-i-5` added 2026-09-16 on ruling R-OG-8; `OG-q-4` added 2026-09-17 on ruling R-OG-13; `OG-q-5` added 2026-09-17 on ruling R-OG-17; `OG-q-6` added 2026-09-18 on ruling R-OG-18; `OG-z-4` added 2026-09-18 on ruling R-OG-20)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `OG`. Axes: `p` parity and baseline, `i` AWS
infrastructure (Terraform, one state), `d` durable state, `a` authentication, `z` authorization, `c` completion closure,
`k` catalog, `o` audit and operations, `q` query, `x` export, `v` validation, `r` release.

Paths below are relative to the repo root. `GW` = `infra/aws/ec2/opal-gateway`. `TFGW` = `infra/aws/terraform/opal-gateway`.
Every cell also writes `deliverables/0.9.0_WK_NFRA_OPLGTW~<slot>/` under the project, and may append to the
investigation file. A cell that can deploy also writes `org/critical_paths/change_management/` and its
`org/critical_paths/.open_deploys/<slug>.json` sentinel.

Each acceptance line is **one criterion**. `J` marks a judgment criterion: no verdict at L7, graded by `3.0.0_SA_CVO` at
L9. A criterion asserting a control states what must DIFFER when the control is engaged, and proves that against the
same harness with it disengaged (spine L6). Those are marked "(difference)".

### S9 -- baseline, infrastructure, release

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-p-1` | deployed parity and the pre-change baseline, read only | FWD-7, FWD-8; inputs to `OG-q-1`, `OG-i-4`, `OG-r-1`, `OG-c-2` | deliverables only | OPEN |
| `OG-i-1` | the `opal-gateway-access-state` table and its two grants | FWD-1, 3, 4, 6, 7 | `TFGW/schwab_access_state.tf` (new) | OPEN |
| `OG-i-2` | the Schwab data-plane identities: two reader roles, the Gateway's assume statement, the alias-key secret | FWD-3 | `TFGW/schwab_reader_iam.tf` (new) | OPEN |
| `OG-i-5` | the access-state table renamed to the builder's name, its records carried across under proof (added 2026-09-16 on ruling R-OG-8) | FWD-1, 3, 4, 6, 7 | `TFGW/schwab_access_state.tf`, `GW/app/access_state.py`, `GW/app/oauth_as.py`, the contract JSON | OPEN |
| `OG-i-3` | the ALB's explicit browser paths for the download page and its OIDC callback | FWD-1, 4, 7 | `TFGW/alb.tf` | OPEN |
| `OG-i-4` | the pilot host: t4g.nano to t4g.small | FWD-7 | `TFGW/main.tf` (`aws_instance.gw` `instance_type` only) | HELD (G-A) |
| `OG-r-1` | the first release: the integrated build, the OAuth cutover, the Schwab flag off | FWD-1, 7, 8 | `infra/aws/ec2/EC2_MANIFEST.json` (the deploy record) | OPEN |
| `OG-r-2` | on-host capacity and existing-workflow regression on the candidate | FWD-5, 7, 8 | `GW/tests/acceptance/onhost_bench.py` (new) | OPEN |

**`OG-p-1` acceptance**
- the running Gateway's per-file source digests, read on the host by SSM, are compared file by file with the tree at `EC2_MANIFEST.json`'s `deployed_commit`; mismatches listed, denominator printed
- the host's instance type, architecture, process and worker count, Python version and installed package versions are read on the host
- the ALB's listener rules, priorities, default browser OIDC action, WAF association and `idle_timeout` are read back live, each with its resource ARN and UTC time
- `opal-data-assets` versioning, default encryption, the four public-access-block flags and the policy status are read back live
- `opal-gateway-role`'s trust and every inline and attached policy are read back live
- `GetRole` on `opal-mcp-emp-menachem-schwab-read` and on `opal-mcp-schwab-catalog-read` each return NoSuchEntity
- `DescribeTable` on `opal-gateway-access-state` returns ResourceNotFound
- the `meta/complete/` object count, newest key and schema field per master are printed
- the bucket's notification configuration is read live, and every `ObjectCreated` consumer whose prefix covers `schwab/*/meta/complete/` is listed
- the Gateway's peak RSS over a stated window is recorded with its instrument named
- the existing-user baseline records p95 latency per representative tool from the audit record over a stated window, with its sample count printed
- the OAuth client inventory lists every `client_id` the audit record shows over a stated window, with counts, and states that clients are process-local
- every AWS call in the cell's command log is a read verb (Describe, Get, List, Head)

**`OG-i-1` acceptance**
- the plan creates only the table, the runtime grant and the operator role and policy, with zero changes or destroys to existing resources
- the apply runs through `safe-apply` under a ledger entry whose OPEN sentinel is committed before the act
- the ledger entry is closed and committed before the reads below
- `describe-table` reads SSE enabled, point-in-time recovery enabled, PAY_PER_REQUEST billing, the TTL attribute set and the designed key schema
- the runtime grant allows `GetItem`, `PutItem`, `UpdateItem` and `DeleteItem` on exactly the table ARN, with every write action conditioned on `dynamodb:LeadingKeys` matching `RUNTIME#*`, and no table-admin action. **`DeleteItem` was added and the prohibition on it STRUCK AS TO `RUNTIME#` on 2026-09-18 by `1.0.0_SA_CTO` ruling R-OG-21 (@`157b426b2d`), Andrew-approved directly ~16:1xZ**, after the prohibition was measured to be the cause of a ten-hour login outage: `app/oauth_as.py:649` (the pending-authorization consume at `/callback`) and `:772` (burning a code on a failed verifier) both call a CONDITIONAL delete, and both delete an EXPIRING record, which is what the contract's `RUNTIME` clause affirmatively admits ("runtime conditional writes and expiring records"). The contract needed no amendment; only this line and `OGI1-AC5` did. **THE PROHIBITION STANDS UNCHANGED FOR `POLICY#` (line below) AND FOR TABLE-ADMIN ACTIONS**, and the `LeadingKeys` confinement is what keeps the two apart. **AND THE OLD WORDING NAMED A PERMISSION THAT DOES NOT EXIST:** there is no `dynamodb:TransactWriteItems` IAM action at all -- a transaction is authorized PER ITEM against `PutItem`/`UpdateItem` (`probes/og_i1.py:33`, and the TF's own comment at `schwab_access_state.tf:21`) -- so "allows ... TransactWrite" was not an over-grant on paper but a CATEGORY ERROR, and a later cell relying on it would have been relying on something no policy can grant.
- the operator principal is separate, may conditionally update `POLICY#` records and append `operator_audit` in one transaction, and holds no DeleteItem on `POLICY#` and no table-admin action
- (difference) from the Gateway host, an isolated runtime-principal write to a `POLICY#` key is AccessDenied, while the same write to a `RUNTIME#` key succeeds in the same harness (A13)
- two concurrent operator revisions of one isolated `POLICY#` record yield exactly one success and one ConditionalCheckFailed (A13)
- a probe `POLICY#` record carries no TTL attribute

**`OG-i-5` acceptance** (added 2026-09-16 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-8, msg 97553, PRD v0.7 @79a1fd4a47. It is a cell added mid-round on the L4 owner's ruling, not a re-decomposition. Edges: `OG-i-2 -> OG-i-5` (state), `OG-i-5 -> OG-i-3` (state), `OG-i-5 -> OG-r-1`. Slot ~1, before `OG-i-3`.)
- the table's new name is printed from `lib/opal_naming.py` and equals the ruled value
- the apply runs through `safe-apply` under a ledger entry whose OPEN sentinel is committed before the act
- the first apply's plan creates exactly the new table, repoints only the runtime grant and the operator policy to it, and destroys nothing
- `describe-table` on the new table reads SSE enabled, point-in-time recovery enabled, PAY_PER_REQUEST billing, the TTL attribute and the designed key schema
- (discriminating) the item count of the old and new tables is equal, both printed
- every copied item, the operator-audit namespace included, is equal item by item on both sides, the denominator printed
- no application, Terraform or contract reference to the old table name remains outside the project's historical records, by an unscoped count with its denominator
- `tests/test_access_state.py`, `tests/test_oauth_durable.py` and `tests/test_principal_cutover.py` pass, one process per module
- (difference) from the Gateway host, a runtime-principal write to a `POLICY#` key of the new table is AccessDenied, while the same write to a `RUNTIME#` key succeeds (A13)
- the old table is removed only after the equality criteria are recorded, by a second apply whose plan destroys only the old table
- the ledger entry is closed and committed before the final reads, and a fresh plan of the root reads 0 changes

**`OG-i-2` acceptance**
- the plan creates exactly two roles with their policies, one statement on `opal-gateway-role` allowing `sts:AssumeRole` on exactly those two ARNs with each one's dedicated ExternalId, and the alias-key secret with the Gateway's read grant on it
- the plan shows zero changes to `TFGW/taxsma_gateway_iam.tf`'s resources, to `opal-gateway-assume-emp-roles` and to the `opal-mcp-emp-alyssa-*` roles
- the data role allows GetObject and GetObjectVersion on the six data prefixes and ListBucket conditioned on those prefix forms, with explicit denies outside them (`meta/*` included) and no write action
- the catalog role allows GetObject and GetObjectVersion on the two completion prefixes and ListBucket conditioned on them, with explicit denies outside them
- each role trusts only `opal-gateway-role`, with its own ExternalId
- (difference) from the Gateway host, assuming each new role with the Tax SMA ExternalId fails, while assuming it with its dedicated ExternalId succeeds
- from the Gateway host, the data role's GetObject on a silver object of a listed prefix succeeds
- from the Gateway host, the data role's GetObject on a `meta/complete/` key is denied
- from the Gateway host, the data role's GetObject on a key outside the six prefixes is denied
- from the Gateway host, the data role's PutObject on a key under a listed prefix is denied
- from the Gateway host, the data role's ListBucket outside its prefix forms is denied
- from the Gateway host, assuming any role from a data-role session is denied
- from the Gateway host, the catalog role's GetObject on a `meta/complete/` key succeeds
- from the Gateway host, the catalog role's GetObject on a silver key is denied
- the source bucket policy's hash before the apply equals its hash after
- policy-simulation results and live exercised results are recorded in separate, labelled sections

**`OG-i-3` acceptance**
- the plan changes only listener rules for the exact download and OIDC-callback paths `OG-a-3` and `OG-x-1` name, and leaves the default action unchanged
- the apply runs through `safe-apply` under a ledger entry opened and committed before the act and closed before the reads
- every pre-existing rule reads back byte-equal to `OG-p-1`'s baseline
- (difference) an unauthenticated GET to an unrelated path still redirects to the ALB login, while the same request to an explicit path reaches the application (status and Location header recorded)
- the `idle_timeout` is read back with its ARN and UTC time
- the WAF association equals `OG-p-1`'s baseline

**`OG-i-4` acceptance**
- the ledger entry cites the Andrew-direct record authorizing this stop and start of the Gateway instance, by path@commit
- the plan changes only `instance_type` on `aws_instance.gw` and does not replace the instance
- the apply runs through `safe-apply` under a ledger entry opened and committed before the act and closed before the reads
- the instance reads t4g.small, arm64, running
- after the restart, the Gateway's systemd unit is active and an unauthenticated `/mcp` returns 401 with the resource challenge
- the existing-user baseline is re-taken on the new host with `OG-p-1`'s instrument and window rule

**`OG-r-1` acceptance**
- the ledger entry is opened and its sentinel committed before the deploy
- the deploy runs through `infra/aws/ec2/safe-ec2-deploy.sh` with the Schwab feature flag off
- no principal profile is active in the state store after the deploy
- on the host, every deployed file's digest equals the build input's, file by file, denominator printed
- an unauthenticated `/mcp` returns 401 with the advertised resource challenge (asserted, not printed)
- the discovery metadata advertises exactly the resource, issuer, endpoints, scope and S256 behaviour the running configuration enforces
- on the host, the registry loaded with the live configuration enumerates zero Schwab tools
- the ledger entry is closed and committed before the grading reads
- the Gateway's error count over the first stated window after the deploy does not exceed `OG-p-1`'s baseline for the same window length
- the previous release artifact is recorded and restorable by the runbook's rollback section

**`OG-r-2` acceptance**
- the benchmark runs on the candidate host (after `OG-i-4`) against the released build, with synthetic principal contexts in process and no bearer token minted
- the maximal and concurrent Unicode query fixtures each stay within 256 MiB resident memory per job
- the maximal and concurrent Unicode query fixtures each finish within 30 seconds or return BUSY or LIMIT_EXCEEDED as designed
- a 50 MiB CSV fixture is generated within the export deadline and its temporary files are gone afterwards
- the existing peak RSS on the new host and the admission reserve computed from it are recorded
- (difference) the existing-workflow p95 after, against `OG-p-1`'s before, regresses by no more than 20 percent with zero failures, workload, sample counts and windows printed
- the ALB `idle_timeout` is read immediately before the test, with ARN and UTC time, and exceeds the 30-second preparation deadline
- the record carries a capacity verdict, SUFFICIENT or INSUFFICIENT, and an INSUFFICIENT one carries its measurements for a PRD revision
- `J`: the benchmark's workload is representative of the pilot's declared use

### S3 -- durable state

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-d-1` | the access-state adapter: key namespaces, strong reads, conditional writes, logical expiry | FWD-1, 3, 4, 6, 7 | `GW/app/access_state.py` (new), `GW/tests/test_access_state.py` (new) | OPEN |

**`OG-d-1` acceptance**
- every read is strongly consistent
- every write is conditional, and every multi-item change is one transaction
- keys use the `POLICY#<tid>#<oid>` and `RUNTIME#<kind>#...` namespaces
- (difference) the runtime write API refuses a `POLICY#` key before any AWS call, and accepts the same call on a `RUNTIME#` key
- (difference) an expired-but-present record reads as absent, and the same record unexpired reads as present
- an unavailable or malformed store returns DEPENDENCY_UNAVAILABLE and never a default or stateless fallback
- the tests run against an emulator that implements ConditionExpression and transaction semantics, named with its version

### S1 -- identity and OAuth

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-a-1` | durable OAuth: registration, redirects, resource binding, one-use codes, refresh families | FWD-1, 3, 7 | `GW/app/oauth_as.py`, `GW/app/server.py`, `GW/tests/test_oauth_durable.py` (new) | OPEN |
| `OG-a-2` | the immutable principal, the legacy cutover and the challenge semantics | FWD-1, 3, 7 | `GW/app/token_broker.py`, `GW/app/context.py`, `GW/app/identity.py`, `GW/app/oauth_as.py`, `GW/app/server.py`, `GW/app/revocation.py`, `GW/tests/test_principal_cutover.py` (new) | OPEN |
| `OG-a-3` | the download browser's own OIDC login | FWD-4 | `GW/app/browser_oidc.py` (new), `GW/app/server.py`, `GW/tests/test_browser_oidc.py` (new) | OPEN |

**`OG-a-1` acceptance**
- registration (JSON) accepts exactly `https://claude.ai/api/mcp/auth_callback` and registered loopback redirects with RFC 8252 port handling
- registration refuses an arbitrary hosted redirect
- (difference) code redemption without the issued `client_id` is refused, and the same redemption with it succeeds
- authorization with an unregistered `client_id` is refused
- a requested resource other than the advertised one is refused at authorize and at token exchange
- PKCE S256 is required and `plain` is refused
- a second redemption of one authorization code returns invalid_grant
- a refresh rotates the family's generation by one conditional transaction
- reuse of a consumed refresh token revokes the family, so the newest token then fails too
- N concurrent refreshes of one token yield exactly one success, and every loser gets invalid_grant with no second valid successor
- a refresh never returns a broader scope than the family's, and a narrower requested scope is recorded
- access tokens last 15 minutes and refresh families 30 days absolute and 7 days idle, with logical expiry enforced while records are present
- (difference) a restart between authorize and callback resumes the bound transaction or returns an explicit restart-login error, and never guesses an identity
- client registrations survive a process restart
- (difference) with the state store failing, new and refresh exchanges fail closed, and with it healthy they succeed
- the advertised metadata equals the enforced configuration field by field
- token exchange is form encoded
- under the harness load, discovery, registration and token responses stay under 10 seconds and refresh under 30 seconds of server time
- the whole `GW/tests/` suite passes, count printed

**`OG-a-2` acceptance**
- the signed access token and the request context carry the validated Entra `tid` and `oid` and a token-version claim, and email is display metadata only
- authentication completes without Graph mail or file scopes
- a Graph-using tool still acquires its delegated Graph token in the harness
- every protected MCP and REST route rejects an access token lacking the new token-version and principal claims while its `exp` is still valid, over all route declarations, denominator printed
- a legacy refresh token returns invalid_grant
- (difference) an access token of a revoked family is rejected, and one of a live family is accepted
- a caller-supplied email, identity header, role or tenant never becomes the authorization identity
- a principal with the same email and a different `oid` is denied (A3)
- a token from an unauthorized tenant is rejected
- (difference) a missing or invalid credential returns 401 with the resource challenge, while a valid token lacking a scope returns 403 insufficient_scope
- a denied data entitlement returns a terminal tool error and never a 401 or an OAuth escalation

**`OG-a-3` acceptance**
- the Gateway-owned OIDC callback and download paths are listed exactly, for `OG-i-3`
- a mismatched state or nonce is refused
- an ID token with a wrong signature, issuer or audience is each refused
- the session cookie is Secure, HttpOnly and SameSite, scoped to the download paths
- the same user fixture yields the same `tid`/`oid` principal through this login as through MCP OAuth
- the cell's code neither imports nor calls `identity.py`'s ALB email helper
- the route table differs from the one before only by the new paths

### S2 -- authorization

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-z-4` | the guard denial's MCP envelope: a refused call is flagged as an error to the CONSUMER, not only in its body (added 2026-09-18 on ruling R-OG-20) | FWD-3, 5 | `GW/app/tools.py`, `GW/tests/test_schwab_denial_envelope.py` (new) | OPEN |

**`OG-z-4` acceptance** (added 2026-09-18 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-20, msg 97775 @bb15319584, closing call 18 on row `NFRA_OPLGTW-W5-S18`. Found because `OG-q-5`'s half-one fix UNMASKED it behind an assertion that had been failing first. Edges: `OG-z-1 -> OG-z-4`, `OG-q-5 -> OG-z-4`, `OG-z-4 -> OG-v-2` (its last re-hand). Slot ~6.)
- a guard-denied tool call returns the MCP error flag TRUE and its contract error code, graded live through the real app
- a permitted call in the same harness still returns the error flag FALSE
- (mutant control) removing the flag-setting line fails the first criterion
- the class docstring's claim that a denial is "a terminal tool error" is true of the code, or the docstring is corrected to what the code does
- **R-OG-20's bar, stated as the cell's reason:** a criterion about a REFUSAL grades the signal the CONSUMER reads, never only the text the producer wrote

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-z-1` | the persistent policy model and its guard on discovery, dispatch and every REST route | FWD-3, 6, 7 | `GW/app/data_entitlement.py` (new), `GW/app/identity_scope.py`, `GW/app/tools.py`, `GW/app/integrations/base.py`, `GW/app/integrations/registry.py`, `GW/app/server.py`, `GW/app/query_v0.py`, `GW/tests/test_data_entitlement_guard.py` (new) | OPEN |
| `OG-z-2` | the operator's entitlement administration command | FWD-6, 8 | `GW/ops/schwab_entitlement_admin.py` (new), `GW/tests/test_entitlement_admin.py` (new) | OPEN |
| `OG-z-3` | the keyed account alias | FWD-2, 3 | `GW/app/account_ref.py` (new), `GW/tests/test_account_ref.py` (new) | OPEN |

**`OG-z-1` acceptance**
- profile and grant records are keyed by `tid`/`oid`, carry status pending, active or revoked and a revision, and a revoked record is a tombstone
- every request strongly reads the current profile and grant
- (difference) with the store unavailable or a record malformed, restricted access is denied, and with the store healthy it is served
- an unknown user sees no Schwab tool in discovery and a direct Schwab call fails
- a newly registered, unclassified tool is denied to the restricted profile
- the restricted profile's discovery lists only its allowed tools
- every other native and integration tool is denied to the restricted profile before any credential fetch, over all tools, denominator printed
- `/teams/poll`, `/query/v0` and every other non-MCP route are denied to the restricted profile before any credential or data read, over all route declarations, denominator printed
- a restricted principal with an `opalinvest.com` email is denied on `/query/v0`
- scope is enforced separately on master, dataset, account IDs, dates, columns and operations
- (difference) every existing identity-scope entry and an unlisted internal user keep exactly their current tool set, before against after
- removing an overlay row does not reopen the unlisted path for a restricted profile

**`OG-z-2` acceptance**
- a candidate with an empty or unknown identity is refused
- a candidate with an unapproved account or field is refused
- a candidate with a malformed date is refused
- the command prints the exact scope diff before activation
- (difference) activation against a stale revision is refused, and against the current revision succeeds
- one transaction writes the `POLICY#` record and its `operator_audit` with approver, timestamp and source authorization reference
- revocation writes a tombstone and deletes nothing
- no registered MCP tool writes a `POLICY#` record, over all tools, denominator printed
- the command runs under an operator AWS identity and refuses to run under the runtime role

**`OG-z-3` acceptance**
- `account_ref` is a versioned keyed HMAC over master and account ID, with its key read from the secret `OG-i-2` provisions
- one account ID in two masters yields two different references (A5)
- a reference outside the current authorized account set returns ENTITLEMENT_DENIED without revealing whether the account exists
- a raw account ID appears in no log or audit line the harness captures
- a reference under a retired key version is handled by the stated rule

### S4 -- completion closure

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-c-1` | the producer's extended completion contract, built and tested, not deployed | FWD-2, 5, 8 | `data/assets/scripts/silver/conversion_manifest.py`, `data/assets/scripts/silver/schwab_runtime.py`, `data/assets/scripts/silver/tests/test_conversion_manifest.py` | OPEN |
| `OG-c-2` | the producer deploy, then a controlled replay that qualifies one date per master | FWD-2, 5, 8 | `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/{conversion_manifest.py,schwab_runtime.py,BUILD_MANIFEST.json}`, `infra/aws/terraform/opal-assets/silver.tf` (`silver_build_commit.schwab` only) | OPEN (replay HELD on G-B) |

**`OG-c-1` acceptance**
- the completion object gains a schema version, master and date, run identity, expected source partitions, explicit non-applicable and empty dispositions, the expected table set, successful and failed outputs, counts, and every silver object's key with its VersionId
- every legacy field keeps its name and meaning, by a golden test on a legacy fixture
- the complete fixture yields a qualified closure
- a partial event yields incomplete
- a failed sibling yields incomplete
- an idempotent existing output yields its stated disposition
- an overwrite yields its stated disposition
- concurrent completion yields exactly one qualified closure
- a typed empty day yields its explicit empty disposition
- an unexplained empty day, an inconsistent grain and an ambiguous inventory each yield incomplete
- the closure validator, given only the completion object, decides without reading another prefix
- the `data/assets/scripts/silver/tests/` suite passes, count printed
- every reader of `meta/complete` found by an unscoped repo read (denominator printed; `silver.tf:756-759` and `advi_49f_floor.tf` included) is listed with what it reads, and none reads a field this cell removes or renames
- `J`: the diff composes the marker only and rewrites no silver value

**`OG-c-2` acceptance**
- the vendored files are byte-equal to `data/assets/scripts/silver/` at `OG-c-1`'s merged commit
- `silver.tf`'s `silver_build_commit.schwab` names that commit
- the plan changes only `opal-assets-silver-schwab` and shows zero rows for the other five families
- the deploy runs through this Lambda's estate deploy path under a ledger entry opened and committed before the act
- the deployed `CodeSha256` equals the built zip's hash
- the never-widen sign-off of gate G-B is at HEAD before the replay, cited by path@commit
- the controlled replay writes one qualified closure record per master for one stated business date
- each replayed record validates against `OG-c-1`'s schema
- every VersionId a replayed record lists HEAD-matches the live object
- (difference) the VersionIds of every silver object for the replayed dates are identical before and after the replay
- the bucket settings read back equal to `OG-p-1`'s baseline

### S5 -- catalog

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-k-1` | the authorized catalog and the assumed-role credential adapter | FWD-2, 3, 5 | `GW/app/integrations/schwab/catalog.py` (new), `GW/app/integrations/schwab/aws_roles.py` (new), `GW/app/integrations/base.py`, `GW/tests/test_schwab_catalog.py` (new) | OPEN |

**`OG-k-1` acceptance**
- the assumed-role adapter is a new AuthKind, and calls STS with the role's dedicated ExternalId
- the data-policy check precedes every credential fetch, by a call-order assertion
- (difference) with the adapter failing, no S3 client is built from ambient or instance credentials, and with it healthy the role session is used
- closure validation uses the catalog role only and data HEADs use the data role only
- every named silver object is HEADed by its VersionId
- a null, unversioned, changed or unavailable object yields incomplete or unavailable, one fixture each
- a marker naming another bucket, master or dataset is rejected
- the catalog snapshot persisted under `RUNTIME#` carries the closure version, table, master, date, VersionIds, sizes, schema fingerprint, row counts, validation result and opaque file IDs
- a second write of one snapshot key is refused
- (difference) a legacy marker yields unavailable, and the qualified fixture for the same date yields a snapshot
- the rolling window is the latest qualified business date plus the previous 29 calendar days, per master and dataset
- fixed-date mode takes an enumerated date set
- the response returns the available dates and the latest qualified date
- no date is filled from another master or dataset
- staleness is reported as days since the qualified business date, with the observation time

### S8 -- audit and operations

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-o-1` | the acknowledged Schwab audit entry point | FWD-6, 8 | `GW/app/schwab_audit.py` (new), `GW/tests/test_schwab_audit.py` (new) | OPEN |
| `OG-o-2` | the operator runbook and its status summary | FWD-6, 8 | `GW/runbooks/SCHWAB_PILOT_RUNBOOK.md` (new), `GW/ops/schwab_status.py` (new) | OPEN |

**`OG-o-1` acceptance**
- the entry point awaits a successful PutObject under `opal-mcp-audit` `audit/schwab/` and returns its receipt before any data release, by a call-order assertion
- (difference) with the sink failing, a new data release returns DEPENDENCY_UNAVAILABLE and no data, and with it healthy the data is released
- the event types are exactly release_authorized, delivery_finished, denied, cancelled, failed and operator_revision
- release_authorized and delivery_finished record planned and delivered counts separately
- a fixture record holds no raw account ID, customer value, prompt, OAuth credential, cookie, ticket secret or complete URL
- (difference) with the sink failing, an unrelated legacy authentication still succeeds
- the prefix sits inside the Gateway's existing grant (`TFGW/audit-lake.tf:186-187`, `audit/*`), so no IAM change is made

**`OG-o-2` acceptance**
- the runbook carries onboarding, connector add or reuse, member connection, troubleshooting, audit read, grant change and revocation, rollback and disclosure sections
- every command the runbook names exists at HEAD
- troubleshooting distinguishes authentication failure, terminal entitlement denial and data unavailability
- the rollback section disables the integration and keeps the restricted-profile denial and the revocation shim
- the rollback section forbids restoring a binary that reopens the email-only path or accepts legacy refresh tokens
- the rollback section preserves source objects and ingesters and carries the source-bucket readbacks
- the disclosure states the chat-environment and retention exposure, that commercial training defaults do not mean zero transfer, and that delivered data cannot be recalled
- the runbook names its readers and their consuming moments
- the status summary prints health, closure and error summaries with no customer value
- `J`: an operator can execute each section at its named moment without other context

### S6 -- query

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-q-1` | the bounded execution engine | FWD-5, 7 | `GW/app/integrations/schwab/engine.py` (new), `GW/requirements.txt`, `GW/tests/test_schwab_engine.py` (new) | OPEN |
| `OG-q-2` | the five tools, request validation, the response envelope, cursors | FWD-2, 3, 5 | `GW/app/integrations/schwab/integration.py` (new), `GW/app/integrations/schwab/query.py` (new), `GW/app/integrations/schwab/envelope.py` (new), `GW/app/integrations/schwab/cursor.py` (new), `GW/app/integrations/registry.py`, `GW/tests/test_schwab_query.py` (new) | OPEN |
| `OG-q-3` | snapshot and metric semantics | FWD-2, 5 | `GW/app/integrations/schwab/semantics.py` (new), `GW/app/integrations/schwab/datasets.json` (new), `GW/tests/test_schwab_semantics.py` (new) | OPEN |
| `OG-q-4` | the semantics checks wired into the live query path (added 2026-09-17 on ruling R-OG-13) | FWD-2, 5 | `GW/app/integrations/schwab/query.py`, `GW/app/integrations/schwab/integration.py`, `GW/tests/test_schwab_wiring.py` (new) | OPEN |
| `OG-q-5` | the dim_asset partial-account restriction wired on the live path, and a CENSUS of every C3 rule against its call path (added 2026-09-17 on ruling R-OG-17) | FWD-2, 5 | `GW/app/integrations/schwab/query.py`, `GW/app/integrations/schwab/catalog.py`, `GW/tests/test_schwab_asset_policy.py` (new) | OPEN |
| `OG-q-6` | the FOUR remaining NOT-ENFORCED C3 rules the census found, wired on the live path under ONE mutant (added 2026-09-18 on ruling R-OG-18) | FWD-2, 5 | `GW/app/integrations/schwab/query.py`, `GW/tests/test_schwab_c3_rules.py` (new) | OPEN |

**`OG-q-1` acceptance**
- each job runs in a child process outside the event loop
- (difference) the event loop's latency probe stays responsive while a job runs, against the same probe with a blocking in-loop job
- a job over 256 MiB resident memory is killed and returns LIMIT_EXCEEDED
- a job over 30 seconds is killed and returns no partial total
- a second concurrent job for one principal returns BUSY
- a third concurrent job globally returns BUSY, with no queue
- admission reserves `OG-p-1`'s measured existing peak RSS (value cited) times 1.25 plus 128 MiB, and insufficient headroom returns BUSY
- a request over 12 source objects or 64 MiB compressed, policy dependencies included, returns LIMIT_EXCEEDED with a narrowing suggestion
- DuckDB runs with external access, extension loading and remote files disabled, each setting asserted
- no caller-supplied string reaches the generated SQL, by a fuzz corpus
- temporary files are gone after success, failure, cancellation and startup cleanup
- cancelling the awaiting request terminates the child process
- the pinned PyArrow and DuckDB wheels resolve for linux aarch64 on the host's Python
- `mcp==1.28.0` is unchanged

**`OG-q-2` acceptance**
- exactly the contract's five tools are registered
- an unknown enum value or an extra property is refused
- a request carries exactly one of rows mode or aggregate mode
- a field reference outside the grant, in columns, filters, groups, sorts or aggregates, is refused without revealing the field (A6)
- filter values match their measured types, `is_null` takes no value, and `in` takes at most 100 values
- more than 20 filters, 10 group fields, 10 aggregates or 10 order fields is refused
- an aggregate declares function, field and alias, and a duplicate or shadowing alias is refused
- no expression, SQL fragment, regex, path, code or URL is accepted, by a fuzz corpus
- (difference) a cache warmed under a broader grant is not served to the narrower grant, and the same request under the broader grant is (A6)
- after revocation, a warmed cache entry is denied
- cache, cursor and ticket keys bind principal, revision, master, dataset, dates, projection and source versions
- the envelope carries master ID and label, business date, dataset, opaque source references, scope summary and revision, matched count, returned count, truncation, completeness and available-date and staleness metadata
- decimals are strings with their schema scale and unit
- aggregate totals cover the whole authorized match set before pagination
- an incompletely scanned aggregate returns an error
- the whole serialized result stays within 500 rows, 100,000 codepoints and 131,072 UTF-8 bytes, counting every block, measured before emission (A18)
- metadata alone over the cap returns an error
- a cursor is authenticated, lives 5 minutes and binds identity, revision, query and snapshots
- an edited cursor and an expired cursor are each refused
- rows tie-break deterministically on a validated unique grain, and a dataset without one refuses paging
- (difference) a revision change during a job discards the result, and an unchanged revision releases it
- prompt-like text inside data comes back as data and invokes no tool, widens no filter and changes no grant (A12)
- every tool call writes its audit event through `OG-o-1` before release

**`OG-q-6` acceptance** (added 2026-09-18 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-18, msg 97749 @d6466d7697, closing call 17 on rows `NFRA_OPLGTW-W5-S14`..`W5-S17`. A cell added mid-round on the L4 owner's ruling, not a re-decomposition. Edges: `OG-q-4 -> OG-q-6`, `OG-q-5 -> OG-q-6`, `OG-q-6 -> OG-v-2` (its last re-hand). Slot ~5. ONE cell for all four because they share one call site, one harness and one mutant -- and the ruling made that premise FALSIFIABLE BY THE CELL: the mutant must fail ALL FOUR, and fewer than four is the finding, not an anomaly.)
- R20: a grouping that drops master or date identity is refused on the live path, the refusal's contract code printed
- R22: a total built by adding DIFFERENT balance fields is refused on the live path, while a named field's sum across approved accounts still succeeds
- R24: a duplicate or conflicting source grain returns unavailable rather than a silently de-duplicated answer
- R25: the dataset description carries sign and null semantics for every authorized field, denominator printed
- (ONE mutant control, and the one-cell premise rests on it) removing the SHARED call site fails ALL FOUR criteria above; fewer than four FAILS this criterion and the cell splits on that evidence
- (closing) the C3 census is re-read and its NOT-ENFORCED count falls to 0, WITH ITS DENOMINATOR RE-PRINTED at re-read time rather than inherited from the 29 measured at the earlier vintage

**`OG-q-5` acceptance** (added 2026-09-17 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-17, msg 97682 @70570f36b9, on row `NFRA_OPLGTW-W6-S8`, which `OG-v-2`'s integrated harness measured. A cell added mid-round on the L4 owner's ruling, not a re-decomposition. Edges: `OG-q-2 -> OG-q-5`, `OG-q-3 -> OG-q-5`, `OG-q-5 -> OG-v-2` (its last re-hand). Slot ~5, after `OG-q-4`.)
- under a partial-account grant, `dim_asset` returns only the CUSIPs the authorized accounts hold on that master and date, graded through the real app
- a CUSIP held ONLY by an unauthorized account is ABSENT from that same response
- (mutant control) with the restriction's call site removed in a scratch copy, both criteria above FAIL
- (the census R-OG-17 adds, because this is the third instance of one root cause) every rule PRD C3 states is enumerated with its denominator PRINTED, and each is marked enforced-on-the-call-path or NOT, measured through the app rather than read off the PRD
- the neighbouring query, semantics, wiring and acceptance modules still pass, one pytest process per module

**`OG-q-4` acceptance** (added 2026-09-17 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-13, msg 97629 @9798d9dda5, closing call 13 on row `NFRA_OPLGTW-W6-S6`. A cell added mid-round on the L4 owner's ruling, not a re-decomposition. Cause: `OG-q-3`'s criteria exercised `semantics.py` in isolation and named no call site, so 14 of 14 passed over a module nothing imports; `OG-q-2`'s query path predates it. Edges: `OG-q-2 -> OG-q-4`, `OG-q-3 -> OG-q-4`, `OG-q-4 -> OG-v-2` (re-hand). Slot ~5. Every criterion here is graded on the LIVE path through the real app and carries a mutant control, per R-OG-13's standing bar.)
- a nonadditive field's SUM through the registered `schwab_query` tool is refused, with the refusal's contract error code printed
- a quantity SUM not grouped by `cusip` and `l_s` through the same tool is refused
- a legal named-balance SUM through the same tool still succeeds and returns its total
- (mutant control) with the call site removed in a scratch copy, the two refusal criteria FAIL and the legal SUM still passes
- `OG-q-2`'s and `OG-q-3`'s own test modules still pass, one pytest process per module

**`OG-q-3` acceptance**
- grouping never drops master or date identity
- a sum across dates is refused
- a both-master question returns separate results and no combined total
- a date comparison uses separately authorized snapshots and an exact decimal delta
- a named balance field's sum across approved accounts is allowed
- a cash or AUA total built from different balance fields is refused
- a quantity sum without grouping by `cusip` and `l_s` is refused
- a price aggregation is refused
- a duplicate or conflicting grain returns unavailable and never deduplicates
- every field's description carries grain, type, unit, sign and null semantics, each with its source
- under a partial-account grant, `dim_asset` returns only CUSIPs the authorized accounts hold on the same master and date, by a qualified position snapshot
- those position objects count toward the object, byte and deadline limits
- an unqualified position snapshot denies the asset read
- an unsupported or unverified metric is refused

### S7 -- export

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-x-1` | the authenticated, filtered CSV download | FWD-4, 6, 7 | `GW/app/integrations/schwab/export.py` (new), `GW/app/download_routes.py` (new), `GW/app/static/schwab_download/` (new), `GW/app/server.py`, `GW/tests/test_schwab_export.py` (new) | OPEN |

**`OG-x-1` acceptance**
- `schwab_prepare_download` returns only a Gateway HTTPS URL with the ticket in its fragment, and never a presigned S3 URL
- the ticket record holds a hashed ID, `tid`/`oid`, the grant revision, source versions, the normalized query and projection, creation and a 300-second expiry, and single-use state
- logical expiry is checked before TTL deletion
- the page script removes the fragment from history and exchanges it in an Origin-checked, CSRF-protected POST body
- the ticket never appears in a request path, query string, redirect URL or referrer, by request capture
- when login is needed, only a hashed pending ticket bound to the browser session is retained through `OG-a-3`'s login
- a synthetic ticket appears in no application log line
- the page carries a restrictive Content-Security-Policy
- the page shows master, date, file scope and field definitions, and a Download CSV control
- identity and the current grant are checked, then the ticket is consumed atomically at download start
- (difference) a ticket copied to another principal fails, and the same ticket for its own principal succeeds (A10)
- an expired ticket fails
- a replayed ticket fails
- a ticket whose grant revision changed fails
- a ticket whose grant was revoked fails
- a consumed ticket that fails midstream requires a new preparation
- the CSV applies the query's projection, filter and decimal rules, by parity with the same request through `schwab_query`
- the CSV is generated and validated completely before the response starts
- the response is reauthorized, then streamed without buffering on the event loop
- an export over 250,000 rows or 50 MiB fails and asks for a narrower scope, and is never truncated
- formula prefixes in text cells are escaped, leading whitespace and control characters included
- numeric values stay numeric strings with correct sign and precision, and headers carry units where needed
- the response has a safe filename, attachment disposition, `Cache-Control: no-store` and a referrer policy
- one ticket yields one artifact, and a second download attempt fails
- an original Parquet or bronze request fails for every profile, and no route serves an original (A11)
- local export files are gone after success, failure, cancellation and startup cleanup
- no token and no data value appears in an access log line

### S10 -- acceptance

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-v-1` | independent acceptance expectations and the walkthrough protocol | FWD-1 .. 8 | `GW/tests/acceptance/fixtures/` (new), `GW/tests/acceptance/expected/` (new), `GW/tests/acceptance/A_ROWS.json` (new), `GW/tests/acceptance/WALKTHROUGH_PROTOCOL.md` (new) | OPEN |
| `OG-v-2` | the local integrated acceptance run, before any production deploy | FWD-2 .. 7 | `GW/tests/acceptance/test_local_acceptance.py` (new) | OPEN |
| `OG-v-3` | real-data expected answers, sealed by hash | FWD-2 | deliverables only (`SEALED_EXPECTED.json`; values held outside the repo) | OPEN |
| `OG-v-4` | grading the controlled-identity walkthrough | FWD-1, 3 .. 8 | deliverables only | HELD (G-C, G-D) |
| `OG-v-5` | grading the pilot onboarding walkthrough | FWD-1, 8 | deliverables only | HELD (G-E, G-F) |

**`OG-v-1` acceptance**
- the A-row census is exactly A1 .. A20, 20 of 20, each with its expected result, its instrument and whether a machine or a person operates it
- the synthetic fixtures carry two masters sharing one numeric account ID
- the synthetic fixtures carry overlapping balance fields, nulls, signs, decimal edge values and a duplicate grain
- the synthetic fixtures carry prompt-like text in a security description and formula-like text
- the synthetic closure fixtures carry missing, partial, failed and stale variants and an unversioned object
- expected answers are computed by an instrument independent of the query engine, named, with no import from `GW/app/integrations/schwab/`
- for each person-operated A-row, the protocol lists the steps, the expected observation, and the sanitized evidence to record: tool, UTC time, public connector URL, server correlation, and an `ofid_` reference if Claude supplies one
- the protocol lists the chosen real-data questions `OG-v-3` answers: at least one per master, one comparison between masters as separate snapshots, one comparison between dates
- no fixture holds customer data

**`OG-v-2` acceptance**
- the integrated application runs locally against the emulated state store and the fixture objects
- each machine-operated A-row of `OG-v-1`'s census is run against its expectation and reported PASS or FAIL, denominator printed
- (difference) a legacy refresh token returns invalid_grant, and a freshly registered loopback client connects and survives a restart (A2, machine half)
- the whole `GW/tests/` suite passes, count printed

**`OG-v-3` acceptance**
- each chosen question's expected answer is computed from qualified VersionIds (after `OG-c-2`) by an instrument independent of the engine, named
- only a salted hash of each expected answer and the VersionIds used are committed
- no customer value appears in any committed file of the cell, by a scan
- the location outside the repo that holds the values, and its retention, are stated
- `J`: the questions exercise date alignment, units and balance-field overlap on real snapshots (question 13, s.2)

**`OG-v-4` acceptance**
- every person-operated A-row of `OG-v-1`'s protocol has a recorded observation in the walkthrough record, denominator printed
- every recorded server correlation resolves to a sanitized audit record carrying the expected decision
- no audit record the walkthrough produced holds a disallowed field
- the source-bucket readbacks after grant change, revocation and rollback equal `OG-p-1`'s baseline
- the actual answers to the chosen real-data questions hash-match `OG-v-3`'s sealed expectations
- `J`: each walkthrough step's observation matches the protocol's expected observation
- `J`: the record meets the ACCEPT clauses of FWD-3, FWD-4, FWD-5, FWD-6, FWD-7 and FWD-8

**`OG-v-5` acceptance**
- Menachem's profile is active at the revision the identity and data administrator approved, by `OG-z-2`'s audit record
- the active scope equals the administrator's approved account, date and field grant
- the pilot record covers A1 (connect, expiry, refresh, reconnect, logout) and A20 (owner and member support walkthrough)
- every recorded server correlation resolves to a sanitized audit record
- `J`: the record meets FWD-1's ACCEPT clause

### Coverage, run not asserted

**Outcomes, 8 of 8** (the PRD header's `endpoint_outcomes`):

| FWD | cells |
|---|---|
| FWD-1 | `OG-i-1`, `OG-i-3`, `OG-d-1`, `OG-a-1`, `OG-a-2`, `OG-r-1`, `OG-v-4`, `OG-v-5` |
| FWD-2 | `OG-c-1`, `OG-c-2`, `OG-k-1`, `OG-z-3`, `OG-q-2`, `OG-q-3`, `OG-v-1`, `OG-v-2`, `OG-v-3`, `OG-v-4` |
| FWD-3 | `OG-i-1`, `OG-i-2`, `OG-d-1`, `OG-a-1`, `OG-a-2`, `OG-z-1`, `OG-z-3`, `OG-k-1`, `OG-q-2`, `OG-v-2`, `OG-v-4` |
| FWD-4 | `OG-i-1`, `OG-i-3`, `OG-d-1`, `OG-a-3`, `OG-x-1`, `OG-v-2`, `OG-v-4` |
| FWD-5 | `OG-c-1`, `OG-c-2`, `OG-k-1`, `OG-q-1`, `OG-q-2`, `OG-q-3`, `OG-r-2`, `OG-v-2`, `OG-v-4` |
| FWD-6 | `OG-i-1`, `OG-d-1`, `OG-z-1`, `OG-z-2`, `OG-o-1`, `OG-o-2`, `OG-x-1`, `OG-v-4` |
| FWD-7 | `OG-p-1`, `OG-i-1`, `OG-i-3`, `OG-i-4`, `OG-d-1`, `OG-a-1`, `OG-a-2`, `OG-z-1`, `OG-q-1`, `OG-x-1`, `OG-r-1`, `OG-r-2`, `OG-v-2`, `OG-v-4` |
| FWD-8 | `OG-p-1`, `OG-c-1`, `OG-c-2`, `OG-z-2`, `OG-o-1`, `OG-o-2`, `OG-r-1`, `OG-r-2`, `OG-v-4`, `OG-v-5` |

**Surfaces, 10 of 10:** S1 `OG-a-1` `OG-a-2` `OG-a-3` · S2 `OG-z-1` `OG-z-2` `OG-z-3` · S3 `OG-i-1` `OG-d-1` ·
S4 `OG-c-1` `OG-c-2` · S5 `OG-k-1` · S6 `OG-q-1` `OG-q-2` `OG-q-3` · S7 `OG-x-1` · S8 `OG-o-1` `OG-o-2` ·
S9 `OG-p-1` `OG-i-2` `OG-i-3` `OG-i-4` `OG-r-1` `OG-r-2` · S10 `OG-v-1` .. `OG-v-5`.

**Acceptance rows, 20 of 20** (contract `acceptance_ids`). Each row names the cells that build it and, last, where it is
proved:

| A | built by | proved in |
|---|---|---|
| A1 | `OG-a-1`, `OG-a-2` | `OG-v-4`, `OG-v-5` (person-operated) |
| A2 | `OG-a-1`, `OG-a-2`, `OG-r-1` | `OG-v-2` (machine half), `OG-v-4` (a registered Code client reconnects) |
| A3 | `OG-a-2`, `OG-z-1` | `OG-v-2`, `OG-v-4` |
| A4 | `OG-z-1` | `OG-v-2`, `OG-v-4` |
| A5 | `OG-z-3`, `OG-q-2`, `OG-x-1` | `OG-v-2` |
| A6 | `OG-z-1`, `OG-q-2`, `OG-x-1` | `OG-v-2`, `OG-v-4` |
| A7 | `OG-q-2`, `OG-x-1`, `OG-v-3` | `OG-v-4` |
| A8 | `OG-q-3` | `OG-v-2` |
| A9 | `OG-c-1`, `OG-k-1` | `OG-v-2` |
| A10 | `OG-x-1` | `OG-v-2`, `OG-v-4` |
| A11 | `OG-z-1`, `OG-x-1` | `OG-v-2`, `OG-v-4` |
| A12 | `OG-q-2` | `OG-v-2`, `OG-v-4` (through actual Claude) |
| A13 | `OG-i-1`, `OG-i-2` | `OG-i-1`, `OG-i-2` (live arms) |
| A14 | `OG-q-1`, `OG-o-1` | `OG-v-2`, `OG-r-2` |
| A15 | `OG-z-2`, `OG-o-2`, `OG-p-1` | `OG-v-4` |
| A16 | `OG-i-3` | `OG-v-4` (person-operated) |
| A17 | `OG-a-1` | `OG-v-2`, `OG-v-4` |
| A18 | `OG-q-2` | `OG-v-2` |
| A19 | `OG-a-1`, `OG-q-1`, `OG-x-1`, `OG-i-3` | `OG-r-2`, `OG-v-4` (through the ALB) |
| A20 | `OG-o-2` | `OG-v-4`, `OG-v-5` |

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D9 is placed LAPTOP, and the row's `fabric_ruling` carries it. The AWS acts reach
account 313476888478 (us-east-1) from this laptop, and the on-host probes run through SSM on the Gateway instance.
**No cell is owned by a seat**; every cell is served by a worker at L7 (`0.9.0_WK_NFRA_OPLGTW~<n>`). The one possible
exception is `OG-c-2`'s deploy, which is a rule-13 act on `data/*/scripts/silver/` code: if the estate's guard on that
path refuses a worker serial, the worker files a BLOCKING row and the issuer seats a DS lane for that order alone, as the
estate has done before.

**Person-operated acts are not cells.** The walkthroughs need a person at a work browser, signing in through Entra and
using Claude itself. That is egress off Opal infrastructure, which no worker takes. They sit between cells as gates G-D
and G-F (s.6), and worker cells grade their records.

---

## 5. DEPENDENCY EDGES, CHAINS, AND THE FAN-OUT THIS SUPPORTS

Edges are keyed to **observed completion**: `A -> B` means B's acceptance cannot be evaluated until A's artifact is at
HEAD (or, for an apply, live and read back). Four edges are **state-collision** edges rather than data edges: the
`opal-gateway` Terraform root is one state, so `OG-i-1`, `OG-i-2`, `OG-i-3` and `OG-i-4` apply in that order and never
from two worktrees.

```
  baseline and infrastructure
    OG-p-1 -> OG-q-1        OG-p-1 -> OG-i-4        OG-p-1 -> OG-r-1
    OG-i-1 -> OG-i-2 (state)   OG-i-2 -> OG-i-3 (state)   OG-i-3 -> OG-i-4 (state)
    OG-x-1 -> OG-i-3        OG-i-1 -> OG-r-1        OG-i-2 -> OG-r-1        OG-i-4 -> OG-r-2
  state, identity, policy
    OG-d-1 -> OG-a-1        OG-d-1 -> OG-z-1        OG-d-1 -> OG-k-1        OG-d-1 -> OG-x-1
    OG-a-1 -> OG-a-2        OG-a-2 -> OG-a-3        OG-a-2 -> OG-z-1        OG-a-3 -> OG-x-1
    OG-z-1 -> OG-z-2        OG-z-1 -> OG-z-3        OG-z-1 -> OG-k-1        OG-z-1 -> OG-q-2
    OG-z-3 -> OG-q-2
  data, query, export
    OG-c-1 -> OG-c-2        OG-c-1 -> OG-k-1        OG-c-1 -> OG-v-1        OG-k-1 -> OG-q-2
    OG-o-1 -> OG-q-2        OG-o-1 -> OG-x-1        OG-q-1 -> OG-q-2        OG-q-2 -> OG-q-3
    OG-q-3 -> OG-x-1        OG-z-2 -> OG-o-2        OG-x-1 -> OG-o-2
  acceptance and release
    OG-v-1 -> OG-v-2        OG-x-1 -> OG-v-2        OG-z-2 -> OG-v-2        OG-v-2 -> OG-r-1
    OG-r-1 -> OG-r-2        OG-c-2 -> OG-v-3        OG-r-2 -> OG-v-4        OG-o-2 -> OG-v-4
    OG-i-3 -> OG-v-4        OG-v-3 -> OG-v-4        OG-v-4 -> OG-v-5
```

**The chain read, computed from the 45 edges by a script (not chosen):**

```
  cells 28, edges 45, acyclic: yes (Kahn order covers 28 of 28)
  heads (no incoming edge) = 5 :  OG-p-1 OG-i-1 OG-d-1 OG-c-1 OG-o-1
  leaves (no outgoing edge) = 1 :  OG-v-5
  edge-connected components = 1
  M, maximal head-to-leaf paths = 64
  longest dependency path = 13 cells :
    OG-d-1 -> OG-a-1 -> OG-a-2 -> OG-z-1 -> OG-z-3 -> OG-q-2 -> OG-q-3 -> OG-x-1 -> OG-i-3 -> OG-i-4 -> OG-r-2 -> OG-v-4 -> OG-v-5
  width by earliest level:  L0 5 | L1 5 | L2 2 | L3 2 | L4 3 | L5 1 | L6 1 | L7 1 | L8 3 | L9 2 | L10 1 | L11 1 | L12 1
```

**THE BINDING FACTS.** (a) The project is **narrow and deep**: one component, five heads, a thirteen-cell critical path,
and nowhere wider than five. The useful fan-out is therefore the level width, not M. (b) The spine is **authentication
before authorization before data**, because each layer's criteria read the one below: the principal (`OG-a-2`) keys the
guard (`OG-z-1`), and the guard keys the catalog, the query and the export. (c) Two long waits sit outside any worker:
`OG-i-4` waits on Andrew's word to stop the instance (G-A), and `OG-v-4`/`OG-v-5` wait on person-operated walkthroughs
(G-C .. G-F).

### The distinct-worker constraint

| cell | must not share a worker with | why |
|---|---|---|
| `OG-v-1` | `OG-k-1`, `OG-q-1`, `OG-q-2`, `OG-q-3`, `OG-x-1` | the PRD: *"The test author must construct independent expected fixtures rather than calculate expectations with the query under test."* |
| `OG-v-2` | every cell that writes `GW/app/` | the run that grades the integrated build is not its author's |
| `OG-v-3` | `OG-q-1`, `OG-q-2`, `OG-q-3` | real-data expectations are computed apart from the engine they will grade |

The constraint binds on context, never on the slot number: a cold start is a fresh context.

### A slotting that satisfies every constraint above (L6's to choose and defend)

| slot | queue, in dependency order | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` infrastructure (the one Terraform state holder) | `OG-i-1` -> `OG-i-2` -> `OG-i-3` -> `OG-i-4` | `OG-i-3` after `OG-x-1` merges; `OG-i-4` after G-A |
| `~2` baseline and release | `OG-p-1` -> `OG-r-1` -> `OG-r-2` | `OG-r-1` after `OG-v-2`, `OG-i-1`, `OG-i-2` and notice N-1; `OG-r-2` after `OG-i-4` |
| `~3` identity and policy | `OG-d-1` -> `OG-a-1` -> `OG-a-2` -> `OG-a-3` -> `OG-z-1` -> `OG-z-3` -> `OG-z-2` | none |
| `~4` producer | `OG-c-1` -> `OG-c-2` | the replay after G-B |
| `~5` query and export | `OG-o-1` -> `OG-q-1` -> `OG-k-1` -> `OG-q-2` -> `OG-q-3` -> `OG-x-1` -> `OG-o-2` | `OG-q-1` after `OG-p-1`; `OG-k-1` after `OG-z-1` and `OG-c-1`; `OG-q-2` after `OG-z-3`; `OG-x-1` after `OG-a-3`; `OG-o-2` after `OG-z-2` |
| `~6` independent acceptance | `OG-v-1` -> `OG-v-2` -> `OG-v-3` -> `OG-v-4` -> `OG-v-5` | `OG-v-1` after `OG-c-1`; `OG-v-2` after `OG-x-1` and `OG-z-2`; `OG-v-3` after `OG-c-2`; `OG-v-4` after `OG-r-2`, `OG-o-2`, `OG-i-3`, G-C, G-D; `OG-v-5` after G-E, G-F |

**The fan-out this supports: 6 workers over M = 64 maximal paths, cap 8**, with 5 spawned at issuance (`~1` .. `~5`, one
head each) and `~6` when `OG-c-1` drains. Each hand-off is a fresh worktree from HEAD at hand-off time. Disk: a checkout
measured 179 MB against 18 GB free at the cut, so disk does not bind the fan-out.

---

## 6. GATES AND NOTICES -- the promises this project creates

None is an approval gate this seat invented. Each is either standing law or the PRD's own runtime input, and its
carrier is named.

| id | what must exist | carrier of the rule | owner | cells it holds |
|---|---|---|---|---|
| **G-A** | Andrew's word, recorded, authorizing the stop and start of the Gateway instance for the resize | CLAUDE.md Agent Autonomy: stopping EC2 needs human confirmation | Andrew; recorded by the seat he tells | `OG-i-4` |
| **G-B** | the never-widen sign-off (CTO and COO) for the marker replay, naming its write set, the count of writers of `meta/complete/`, and every `ObjectCreated` consumer, the 49F accelerator on `schwab/08335338/meta/complete/` (`silver.tf:756-759`) included | CLAUDE.md HARD STOPS, never move served output without the sign-off; its writer-census clause | `1.0.0_SA_CTO` and `2.0.0_SA_COO~O` | `OG-c-2` (the replay step) |
| **G-C** | a controlled identity: its verified `tid`/`oid` and an approved synthetic grant, recorded | PRD s. Scope: *"An authorized identity/data administrator must verify the immutable identity and approve a concrete account/date/field grant"* | `1.0.0_SA_CTO` (the rectangle's closing owner; re-assigned from `1.0.0_SA_CTO~A` by ruling 98451 @`a0e4748ac2` -- the DELIVERABLE PATH still reads `1.0.0_SA_CTO~A/`, pinned by the seal, row S54), **the identity administrator supplying the evidence = `0.7.0_AE_CloudOps`** (ANDREW-DIRECT 2026-09-20 ~18:0xZ, VERBATIM *"0.7.0_AE_CloudOps is the admin. Should be the default admin for all testing tasks of cloud projects/workflows/resources."*; record `org/tier1_exec/2.0.0_SA_COO/ANDREW_DIRECT_20260920_180xZ_O_IDENTITY_ADMIN_IS_CLOUDOPS_DEFAULT_FOR_CLOUD_TESTING.md` @`768e6df290`. ⛔ This ASSIGNS the role the PRD named and never assigned -- R-OG-26's measured blocker. It does NOT change the closing owner and does NOT move the path. The standing half of his sentence is recorded as HIS and is not carried by this decomposition beyond this project) | `OG-v-4` |
| **G-D** | the controlled walkthrough record at HEAD, following `OG-v-1`'s protocol | the act itself; a person at a work browser | the operator (the PRD's assigned CloudOps operator role) | `OG-v-4` |
| **G-E** | Menachem's verified `tid`/`oid`, the administrator's approved concrete grant, and its activation through `OG-z-2` by an authorized operator | PRD s. Scope and C2 | `1.0.0_SA_CTO` (re-assigned from `1.0.0_SA_CTO~A` by ruling 98451 @`a0e4748ac2`; path unchanged, row S54); **the approving administrator = `0.7.0_AE_CloudOps`** (same Andrew-direct 2026-09-20 ~18:0xZ as G-C); activation by an authorized operator | `OG-v-5` |
| **G-F** | the pilot walkthrough record (owner and member) at HEAD | the act itself | Menachem, the workspace owner, the operator | `OG-v-5` |
| **N-1** | a notice, **not a gate**: before `OG-r-1` is spawned, this seat sends `0.0.0_AB_MSTR` and `1.0.0_SA_CTO` `OG-p-1`'s client inventory, because the cutover makes every existing client reconnect once | PRD C1: *"Cutover rejects them with invalid_grant ... and tells existing users to reconnect once"* | `2.0.0_SA_COO~O` | none (it precedes a spawn) |

---

## 7. THE BATTERY -- run at L5, each lens with its blindness stated

| lens | disposition | result | what it does NOT cover |
|---|---|---|---|
| `comp-adversary` | RUN | `compose` on the PRD, read-vintage `@de5ebb73c7` 2026-09-15T08:18:54Z: 4 of 4 cited commits VERIFIED; 7 cited paths, 6 stable, 1 GONE (the external RFC URL parsed as a repo path); 611 uncited siblings, 12 digested, all postdating the PRD and all other projects' files | `T11: decomposition neighborhood NOT RESOLVED` (the PRD carries no `<decomp_ref>`), so the siblings are filesystem adjacency, not this decomposition's chain. Re-run against a task order at L7 resolves T11 |
| `comp-schedule` | RUN, APPLICABLE | self-test: the first run was killed at 120 s (rc=124) and a re-run read **PASS 6/6**. The view at `--budget 540` scanned 5 of 5 carriers (C1 230, C2 8, C3 12, C4 21, C5 334): **27 gates armed, none naming NFRA_OPLGTW, the Gateway or any surface here.** Five moratoria bind cells: never-widen (`OG-c-2`), no half-landed deploy (`OG-i-1` .. `OG-i-4`, `OG-c-2`, `OG-r-1`), no new monitor or alarm (`OG-o-1`, `OG-o-2`), safe-apply only (`OG-i-*`, `OG-c-2`), no vendor egress without Andrew's word (the person-operated gates) | C4 and C5 are NOT-DECIDABLE prose carriers: 136 project `blocking` fields are a reading list, not gates. The gates this project creates are s.6, registered here |
| `comp-iam` | RUN | `comp-iam service opal-gateway` (DESIRED plane, 473 `.tf` files): role `opal-gateway-role`, 3 operations traced, **all UNRESOLVABLE-RESOURCE** (`s3:PutObject` in `audit.py:48`, `secretsmanager:GetSecretValue` in `integrations/base.py:204`, `s3:GetObject` in `query_v0.py:101`); 27 policy blocks NOT ATTACHED; 2 deny statements unparsed | Terraform only; blind to deny (it cannot answer "is this denied?"). This project adds `sts:AssumeRole` twice, DynamoDB actions, `GetObjectVersion` through assumed roles and a secret read, none of which exist yet. The APPLIED and EXERCISED planes are the live arms of `OG-i-1` and `OG-i-2`; each cell that adds an operation re-runs the lens and records it in its instance |
| `comp-blast` | RUN | on the Gateway instance (L4's run, cited: 47 of 47 traversal, graph 2026-09-14 12:13:53: 2 tables, 17 policies, 5 roles, 2 Lambdas among its downstream, the two existing `opal-mcp-emp-alyssa-*` roles included); on the ALB (this seat's run, graph 2026-09-15 08:34:46): **1 downstream node**, `opal-gateway-alb-sg` | extracted edges only, a LOWER BOUND; dynamic consumers are not counted. The two graphs are one day apart and neither sees the new resources |
| `comp-routes` | DECLARED-NOT-APPLICABLE | L4's `comp-routes trace /mcp` resolved the portal's CloudFront catch-all, not this ALB | it models the portal's CloudFront path only; the Gateway front door is read live by `OG-p-1` and `OG-i-3` |
| `comp-cache` | DECLARED-NOT-APPLICABLE | it analyzes React Query cache keys under `portal/src` | no cell touches the portal. The Gateway's own caches are `OG-q-2`'s criteria |

**Beyond the core:** `comp-find --corpus aws` (s.1 falsifier 3) and the unscoped `meta/complete` census (s.1 falsifier
4) are measurements at this cut. No other lens of the admitted catalogue is claimed.

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6

1. **No egress off Opal infrastructure.** No worker calls Claude, an Anthropic endpoint, an interactive Entra sign-in or
   any vendor API. Those arms are person-operated (s.4).
2. **No bearer token is minted outside the OAuth flow.** No token, cookie, ticket secret, raw account ID or customer
   value enters repository evidence; server correlations are recorded sanitized.
3. **Deploy discipline.** A world-changing act opens its change-management entry and commits the OPEN sentinel before
   the act, then closes and commits the entry before the reads that grade it (spine L7). Terraform through `safe-apply`
   only, never `-target`; the Gateway through `infra/aws/ec2/safe-ec2-deploy.sh` only; no `aws lambda
   update-function-code`.
4. **One Terraform state, one slot.** `OG-i-1` .. `OG-i-4` apply the `opal-gateway` root in order and never from two
   worktrees.
5. **No served output moves without G-B.**
6. **No new monitor, alarm, SNS or notification path** (standing moratorium). Audit classifications only.
7. **No source mutation.** No write, delete or rewrite of a bronze or silver object, no bucket-policy broadening, no KMS
   grant unless the measured encryption mode requires one (then a row).
8. **The Tax SMA role contract, its ExternalId and the `opal-mcp-emp-alyssa-*` roles are untouched.**
9. **The feature flag stays off and profiles stay pending** except where G-C and G-E record otherwise.
10. **The spec is frozen, and the face instructs refusal.** A criterion that cannot be satisfied as written is REFUSED
    and reported with its measurement, never repaired, widened or met by another route. Anything off-spec is a row.
11. **Every invocation terminates** (`timeout 120`, or the tool's own budget).
12. **Commits go through `.tools/safe-commit.sh` under the worker's serial; every `.py` edit passes
    `.tools/commit-gate.sh`.**
13. **`mcp==1.28.0` is not raised.**
14. **No portal or DEV push and no portal gitlink move** (the portal promote freeze, 13:00Z today).
15. **Unknown deployment facts are measured, never presumed.** A cell asserts no deployed state it did not read back.

---

## 9. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is s.1's subtraction: 10 manifest rows, every one served, with four
falsifiers run before use (the 15 physical units, every cited path, the live plane, the marker readers). Exhaustive: 10 of
10 surfaces, 8 of 8 outcomes, 20 of 20 acceptance rows and 24 of 24 boundary questions (s.2, s.3). Mutually exclusive on
write surfaces except where the edges order them: the shared files (`GW/app/server.py`, `GW/app/oauth_as.py`,
`GW/app/integrations/base.py`, `GW/app/integrations/registry.py`) are written by cells joined by a dependency path, so no
two of their writers run at once.

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one record: one module with its tests, one apply, one
measurement, or one grading. The person-operated walkthroughs are a different grain (a person's act) and are gates, not
cells.

**(iii) INTENT COHERENCE.** One axis: **deliver the PRD's first release so every FWD bar has its deliberate proof.** No
cell widens scope: no original-file download, no source mutation, no new portal, no managed Enterprise Auth, no private
tunnel, no cross-master aggregation, no enrichment join.

**(iv) STATE COHERENCE, and what each remedy does NOT move:**
- `OG-i-1` creates the table and moves **no grant or profile record**.
- `OG-i-2` creates two roles and moves **neither the Tax SMA contract nor any existing employee role, nor the bucket policy**.
- `OG-c-1` changes the producer's code and **deploys nothing**; `OG-c-2` changes markers and **no silver value**.
- `OG-z-2` builds the command and **activates no real grant** (G-E is separate).
- `OG-r-1` releases the build and **enables no Schwab tool and activates no profile**.
- `OG-i-4` changes the host and **no code**.
- `OG-v-1` .. `OG-v-5` move **no production code**; a failing acceptance row is a row for the round-N analysis.

---

## 10. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, stated so it can be argued with, and revertible at the round-N analysis.

1. **S1 is three cells on one chain** (`OG-a-1` -> `OG-a-2` -> `OG-a-3`), because all three write `oauth_as.py` or
   `server.py`.
2. **A local integrated acceptance cell (`OG-v-2`) precedes any production deploy.** It is the PRD's *"test the migration
   before cutover"*, made a dependency edge.
3. **The OAuth cutover rides the first release (`OG-r-1`).** The PRD forbids a binary that accepts legacy refresh tokens,
   so the cutover cannot sit behind the Schwab flag. Notice N-1 precedes the spawn.
4. **Person-operated walkthroughs are gates between cells** (G-D, G-F), graded by worker cells, with the judgment
   criteria at L9.
5. **Real-data expectations are sealed by hash** (`OG-v-3`), with the values held outside the repo, because the PRD
   forbids customer data in repository evidence.
6. **The producer deploy and its replay are one cell (`OG-c-2`), with the replay held on G-B**, because a replay for
   08335338 starts the 49F gold dispatcher.
7. **The host resize is its own cell (`OG-i-4`), held on G-A.**
8. **The Schwab audit prefix is `audit/schwab/`**, inside the Gateway's existing `audit/*` grant, so no audit IAM change is
   made.
9. **The entitlement administration is a repository command (`GW/ops/`)**, never an MCP tool, per C2.
10. **The alias key is provisioned with the reader roles (`OG-i-2`)**, as one change to the Schwab data plane's AWS
    identities.

---

## 11. FINDINGS AND CARRIES, for the CTO's L10 read

1. **The cutover's reconnect cost falls on this estate's own agents.** Every client of `mcp.opalinvest.dev`, including
   every agent seat's `opal-gateway` MCP connection, must redo OAuth in a browser once after `OG-r-1`. The PRD closes the
   rule but not the moment. N-1 hands the moment to `0.0.0_AB_MSTR`, who is at Andrew's terminal.
2. **The PRD names roles, not people, for eight acceptance rows.** A1, A2 (its human half), A7, A12 (through Claude), A16,
   A19 (through the ALB), A20 and the FWD-6 repeats need a person with a work browser. G-C through G-F carry them, and
   who performs each is an open staffing fact, owned by `1.0.0_SA_CTO` (re-assigned from `1.0.0_SA_CTO~A`,
   which is not seated, by ruling 98451 @`a0e4748ac2`).
3. **The 49F accelerator is a second consumer of the marker the producer cell changes** (`silver.tf:756-759`). FWD-8's
   *"existing source data and collection continue unchanged"* holds only if that consumer tolerates the extended record.
   `OG-c-1` proves the legacy fields unchanged, and G-B puts the accelerator inside the sign-off.
4. **The data reader role is named per employee, while the controlled identity's reads also pass through it.** Per C6,
   the application policy is the narrower control. Recorded, not a defect.
5. **The new data role's name matches the Gateway's existing wildcard assume grant** (`opal-gateway-assume-emp-roles` over
   `opal-mcp-emp-*`, keyed on the Tax SMA ExternalId). `OG-i-2`'s difference arm proves the Tax SMA ExternalId cannot
   assume it.
6. **`comp-schedule`'s self-test needed more than 120 s on this box** (rc=124, then PASS 6/6). A seat that bounds it at
   120 s reads a dead instrument.
7. **Estimate, as the PRD asks the COO to re-derive it.** The machine critical path is 13 cells. At an inferred 1 to 3
   worker-hours per cell, that is roughly 1.5 to 3 days of serial work, plus the gated waits (G-A, G-C .. G-F), whose
   timing no seat controls. Basis INFERRED, not measured; no delivery date is committed.

---

## 12. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **No cell has been exercised.** Every target state is a specification.
2. **The Gateway's OAuth client inventory is not a durable registry.** Clients are process-local today; `OG-p-1` reads
   what the audit record shows.
3. **The live contents of `meta/complete/` were not read at the cut.** `OG-p-1` counts them.
4. **Whether the rule-13 guard admits a worker on the vendored Lambda tree is NOT-EVALUATED.** `OG-c-2` measures it.
5. **The chain count and the constraint table are readings.** M = 64 follows from the 45 edges this document declares; a
   missing edge would show as false width.
6. **The emulator for DynamoDB conditional semantics is not chosen here.** `OG-d-1` names it; the build ladder applies.

## ADDENDUM R2-k (2.0.0_SA_COO~O, 2026-09-27, on the re-seat @6fba157e76) -- the email-keyed deny cell (row W3-S22)

Ruled: CTO ruling 97251 (row S17) placed W3-S22 in round 2's email-keyed authorization cell. `1.0.0_SA_CTO~O` re-affirmed
it @244cd0d80f and ruled the five design calls @2ae58221ab (`deliverables/1.0.0_SA_CTO~O/RULING_R2-k_FIVE_CALLS_20260927.md`;
contract v1.3 adds `email_deny`; PRD v1.0 C2 and C6 each gain one clause). The design is
`deliverables/2.0.0_SA_COO~O/R2-k_EMAIL_DENY_CELL_DESIGN_20260927.md` @500aac7e4d. Ordered before `OG-v-4`/`OG-v-5`
(the 09-18 ruling), which stay HELD behind it.

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `OG-e-1` | BUILD: the hashed-email deny record, its guard on `/login` + `/sprint*` + legacy `/callback`, the writer's same-transaction put, and `deny-backfill` | C2, C6 (PRD v1.0 @2ae58221ab); row W3-S22 | `GW/app/access_state.py`, `GW/app/data_entitlement.py`, `GW/app/server.py`, `GW/app/token_broker.py`, `GW/ops/schwab_entitlement_admin.py`, `GW/tests/test_email_deny.py` (new), `GW/tests/test_owner_gate.py` | COMPLETE @ed13cfee26 |
| `OG-e-2` | SERVED: the narrow gateway release of OG-e-1 (live commit + OG-e-1's two gateway commits), under never-widen | C2, C6; row W3-S22 | `infra/aws/ec2/EC2_MANIFEST.json`, the NEVER-2 ledger | COMPLETE @bc66889185 (live fe94911257) |

The SERVED steps follow as their own cells, each under never-widen:
- a narrow gateway release from the live commit plus OG-e-1;
- the grant-writer Lambda: NO CELL NEEDED (measured 2026-09-27 ~19:5xZ). `mcportal-grant-writer-lambda` does not exist
  in AWS (get-function-configuration: ResourceNotFoundException); `mcportal_grant_writer.tf` is not applied, and
  NFRA_MCPORTAL MP-a-1 creates it. Its `build_package.py` stages `ops/schwab_entitlement_admin.py` and
  `app/access_state.py` byte for byte from the tree at build time, so the first build already carries OG-e-1's
  same-transaction deny put and no-email refusal. MP-a-1's cut must stage from a tree at or after @2d0f2dda83;
  any CLOUD HEAD today qualifies;
- the OA-g-3 backfill, which WAITS on Andrew's open card.
