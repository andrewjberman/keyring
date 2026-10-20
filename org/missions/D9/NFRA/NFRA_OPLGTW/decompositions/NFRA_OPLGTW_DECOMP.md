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
| `OG-s-1` | SERVED: `/sprint` for the owner only (Andrew-direct 2026-09-27 ~19:5xZ, @785fc4d71f): `SPRINT_VIEW_ALLOWED_EMAILS` added to deploy-to-ec2.sh's `.env` literal, shipped as a narrow release under never-widen; supersedes the OA-g-3 deny backfill; W3-S22 disarms on landing | C6; row W3-S22 | `GW/deploy-to-ec2.sh`, `infra/aws/ec2/EC2_MANIFEST.json`, the NEVER-2 ledger | COMPLETE (live 6a98a0553a) |

The SERVED steps follow as their own cells, each under never-widen:
- a narrow gateway release from the live commit plus OG-e-1;
- the grant-writer Lambda: NO CELL NEEDED (measured 2026-09-27 ~19:5xZ). `mcportal-grant-writer-lambda` does not exist
  in AWS (get-function-configuration: ResourceNotFoundException); `mcportal_grant_writer.tf` is not applied, and
  NFRA_MCPORTAL MP-a-1 creates it. Its `build_package.py` stages `ops/schwab_entitlement_admin.py` and
  `app/access_state.py` byte for byte from the tree at build time, so the first build already carries OG-e-1's
  same-transaction deny put and no-email refusal. MP-a-1's cut must stage from a tree at or after @2d0f2dda83;
  any CLOUD HEAD today qualifies;
- the OA-g-3 backfill, which WAITS on Andrew's open card.

## ADDENDUM R2-E (2.0.0_SA_COO~O, 2026-09-28, round-2 enrichment on the CTO's round-1 analysis @da12a0c091)

The recut of round 2 is `1.0.0_SA_CTO~O`'s ENRICHMENT LIST (`ledger/ROUND_ANALYSIS.round1.md` @da12a0c091, section 4,
items E1-E11), cut in ONE issuance. The rulings folded in:
- the six cut questions @5676f4a48a (`deliverables/1.0.0_SA_CTO~O/RULING_ROUND2_CUT_QUESTIONS_20260928.md`): Q1-Q5
  ADOPTED;
- Q3 AMENDED @79430e9933: no `eip` kind row, no Name tag, no builder call (`aws_eip` has no name argument and is in
  neither tf map, so the `name()` refusal is correct, not a missing row);
- Q6 CLEARED by Andrew-direct ~21:2xZ (record `ANDREW_DIRECT_20260928_212xZ_O_FABRIC_OPEN_CALLS_ANSWERED.md`
  @7bfa5811c6): development egress (PyPI downloads for a venv) for all four ~O COOs and their workers, no per-use card;
- row `NFRA_OPLGTW-Z-S8` @b6727f8cee (the export path cannot return a CSV today) folds into `OG-x-2`;
- R-5 (PRD v1.1 @ac41d1fe1f, wording @c80b5c85b6; ratified-text half SIGNED current by `3.0.0_SA_CVO~O`,
  `prd-signoff.py status` ADMITTED) admits `OG-u-2`.

| item | cell | what it is (2-4 lines) | risk | slot |
|---|---|---|---|---|
| E4 | `OG-v-6` | The sealed question set v2: two FIXED qualified dates (D_PREV, D_NEW), the measured grain of dim_position / dim_balance / dim_asset per snapshot (12), at least one units, one between-dates per master, one between-masters and one balance-overlap question; sealed with salted digests, the copy of record in SSM. The seal plus the OFFLINE grade only (Q4). | WORLD (floor: an infra/ path) | ~10 |
| E1 | `OG-v-7` | Grading the controlled-identity walkthrough (re-cut of OG-v-4): AC1-AC7 carried, OGV4-AC9 carried as AC8, the round's JUDGMENT criterion J2 (every ACCEPT clause of FWD-1 and FWD-3..8 has a PERSON-OBSERVED line), graded by `3.0.0_SA_CVO~O` at L9. | WORLD | ~10 |
| E2 | `OG-v-8` | Grading the pilot onboarding walkthrough (re-cut of OG-v-5): AC1-AC4 carried; J1 the observed-line judgment over FWD-1 and FWD-8. Subject re-read at hand-off against Andrew-direct G-ASKER (@7bfa5811c6 call 1). | WORLD | ~10 |
| E3 | `OG-o-3` | Runbook text repair (OGO2-J1): the three cross-references (6.1, 8, 6.1), the section count, and 7.2 rewritten against the live release and the manifest's deploy history. J1 re-grades OGO2-J1 at L9. | WORLD (floor) | ~13 |
| E5 | `OG-x-2` | BUILD: the streaming export -- refuse over-cap BEFORE fetching, one representation of the result at a time, the 500-row MCP cap counted once (W5-S6), and the export wired end to end through the real `run_export` (Z-S8; the two test aliases removed). | WORLD (floor) | ~11 |
| E5 | `OG-x-3` | SERVED: the narrow gateway release of OG-x-2 (live base plus OG-x-2's gateway commits), never-widen halves, NEVER-2 ledger; Schwab stays dark (DELTA=0 on served answers). | WORLD | ~11 |
| E6 | `OG-r-3` | Re-cut of OG-r-2 on the host: the repaired `_cap_respected` (R2-b, S48), the streaming export at contract scale, AC4 on the 09-11..09-17 baseline PLUS one post-release window of equal length ending at the cut, both with request counts (Q5). Contract unchanged (R-4). | WORLD | ~11 |
| E7 | `OG-t-1` | BUILD: `resolve_tier` keys on the principal (`<tid>/<oid>`) only; principal rosters from the environment (empty defaults); no email fallback for a person; machine/bearer paths (the MS-ingest identity, `token_broker.py:192`'s server-held branch), `identity_scope.py` and `query_v0.py` named OUT of scope (Q1/Q2) with a test that no machine path reaches `resolve_tier` as a person. | WORLD (floor) | ~12 |
| E9 | `OG-u-1` | BUILD: `/ms/site_children` authenticates before it validates (W3-S11); the two browser OIDC paths join `AUTH_PATHS` (W3-S18). | WORLD (floor) | ~12 |
| E9 | `OG-u-2` | BUILD: the DCR idle lifetime per PRD v1.1 C1 (R-5): 30-day idle expiry, explicit logical expiry checked on every exchange, invalid_client when expired, a live refresh family keeps its client, no backfill. | WORLD (floor) | ~12 |
| E7+E9 | `OG-t-2` | SERVED: the narrow gateway release of OG-t-1 + OG-u-1 + OG-u-2, with the principal rosters added to the host `.env`; the 14-day blast-radius pre-read (machine callers included) shows 0 tier deltas beyond the fixture; never-widen halves. | WORLD | ~12 |
| E8 | `OG-n-1` | WORLD: `aws_eip` + `aws_eip_association` in the gateway root, no Name tag and no builder call (Q3 amended), a TARGETED `safe-apply`, NEVER-2 ledger, no stop/start. | WORLD | ~14 |
| E10 | `OG-h-1` | The batch cell: eol rules for the gateway's 7 extensions (W2-S8), the out-of-repo citation register (S43), the suite hygiene rows (W3-S2, W3-S6, W6-S9), and the W2-S6 probe-fixture CARD for Andrew (no delete). | WORLD (floor) | ~13 |
| E11 | `OG-m-1` | READ only: the 08335338 marker storm re-measured (PUTs per date, dispatches by source and outcome, the writer census with deployed bytes). The remedy is a later cut under never-widen. | SERVED | ~13 |

"floor" = GATE (xii) of `.tools/to-pipeline-gate.py`: a `<paths>` entry under `infra/` sets the WORLD floor. The cell
itself deploys nothing unless its row says SERVED or names an apply.

**Edges** (data dependencies; a file overlap is not an edge except where a batch cell must run last):
- `OG-o-3` -> `OG-v-7` (the operator follows the repaired runbook in the walkthrough);
- `OG-v-6` -> `OG-v-7` -> `OG-v-8` (the seal, then the controlled walkthrough, then the pilot);
- `OG-x-2` -> `OG-x-3` -> `OG-r-3` (build, served, measured on the host);
- `OG-t-1`, `OG-u-1`, `OG-u-2` -> `OG-t-2` (E9 rides E7's release);
- `OG-x-3` -> `OG-t-2` (RELEASE SERIALISATION: t-2's release base must be x-3's release or descend from it, so the
  second narrow release never rolls the first back);
- `OG-h-1` runs LAST, after `OG-x-2` has merged (both write `tests/test_schwab_engine.py` and
  `tests/test_schwab_export.py`; a batch cell runs last).

**Gates and holds:**
- `OG-t-2` PHASE A waits on the switchover sitting's Part D record for `ADMIN_PRINCIPAL` and on the two
  `WRITE_CAPABLE_PRINCIPALS` tid/oid values; PHASE B on both never-widen halves;
- `OG-v-7` on G-C (`1.0.0_SA_CTO~O`'s record at `deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`,
  evidence from a `0.7.0_AE_CloudOps` seat) and G-D (Andrew's walkthrough), plus `OG-o-3` and `OG-v-6` merged;
- `OG-v-8` on the G-E record and G-F, plus `OG-v-7` merged;
- `OG-n-1` after NFRA_MCPORTAL MP-a-1's build (the root cannot plan without its layer zip and owner-key values);
- `OG-r-3` after `OG-x-3`; `OG-x-3` PHASE B on its never-widen halves.

**Fan-out:** 14 orders; chains (connected components of the edge set) M = 4 before `OG-h-1`'s last-run ordering
({o-3, v-6, v-7, v-8}, {x-2, x-3, r-3, t-1, u-1, u-2, t-2}, {m-1}, {n-1}). N = 5 slots, cap 8:
- `~10` {v-6, v-7, v-8}
- `~11` {x-2, x-3, r-3}
- `~12` {t-1, u-1, u-2, t-2} (a second root inside the release component, joined to ~11 only at t-2's release base)
- `~13` {o-3, m-1, h-1}
- `~14` {n-1}, spawned only at its gate.
Slots ~10..~14 are unused by round 1 (its orders and deliverables name ~1..~9; no `wk-*` branch names ~10..~14).

## ADDENDUM R2-E.1 (2.0.0_SA_COO~O, 2026-09-29, on 1.0.0_SA_CTO~O's E11 ruling msg 26305) -- the E11 remedy cell

**Source.** E11's read cell `OG-m-1` is complete and merged (@70f45e7675;
`deliverables/0.9.0_WK_NFRA_OPLGTW~13/MARKER_STORM_READ.md`, rows `Z-W13-S1`, `Z-W13-S2`). Over 13 days: 104 dispatches,
0 read CHAIN OK. All 13 floor runs read UNKNOWN because the dispatcher classifies SSM stdout cut at 24,000 characters,
and about 10 marker PUTs per date each dispatch the chain. The analysis (E11) says "the remedy cell is cut from that
read", and `1.0.0_SA_CTO~O` ruled its scope on this seat's recommendation, msg 26305, option (a): *"The classifier
grades the chain log's terminal line, not SSM stdout cut at 24,000 chars. The S3 accelerator dispatches only on a
qualified marker. The writer stays untouched."* Cell class WORLD.

**The cell.**
- `OG-m-2` -- `advi-49f-gold-dispatch` classifies a terminal invocation from its own chain log
  (`s3://opal-data-49financial/gold/advi/_logs/chain_<ExecutionStartDateTime>.log`, last `CHAIN ` line; absent log or no
  terminal line reads UNKNOWN and says so). An S3 accelerator event reads the marker at the event's version and
  dispatches only when `closure.status` is `qualified`, otherwise it logs SKIP and dispatches nothing. The scheduled
  floor path reads no marker. No branch dispatches twice. The dispatcher's inline policy gains two prefix-scoped
  `s3:GetObject` grants. Deployed by build-and-upload plus a `-target`ed `safe-apply`; the writer, the S3 notification,
  the SSM document and the floor schedule are not touched. The deploy also ships `e2be5c2f42`'s never-applied
  `_trigger_identity`, named in the ask.

**Edge and hold.** `OG-m-1` -> `OG-m-2` (met). PHASE A (code, tests, targeted plan) runs at spawn; PHASE B waits on the
never-widen pair signed against `deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-2_20260929.md` (CTO half
`1.0.0_SA_CTO~O`, second half `3.0.0_SA_CVO~O`).

**Slot.** `~15`, its own chain (connected component {m-1, m-2}; `OG-m-1` already drained on `~13`), so it does not
queue behind `OG-h-1`. Round 3 now carries 15 orders over 11 enrichment items.

## ADDENDUM R2-E.2 (2.0.0_SA_COO~O, 2026-09-29, on 1.0.0_SA_CTO~O's msgs 26360 and 26381) -- OG-m-2 split; the classifier cell

**The split (msg 26360).** The naming gate (LGIC_ENFORCE DEC-6) refused the chain-log prefix `gold/advi/_logs/chain_` as
ADVI_FIRMBKTS's live-remediation surface (row `Z-W15-S3`), and no waiver was typed. `OG-m-2` was narrowed by amendment A3
to **OG-m-2a**: the S3-path qualified-marker gate plus `s3:GetObject` + `s3:GetObjectVersion` on the marker ARN only. It
deployed 2026-09-29T02:05:33Z (CodeSha256 `KqlIoAJs...`), ledger closed f8c2dfe0b8, merged 40fcde8bf7. The chain-log
classifier (**OG-m-2b**) was held on the row.

**The unblock (msg 26381).** The gate's `tf_local` kind @7610be987f, its authority @a5aa8e92c8 and the entry
`OPLGTW-LEGACY-READ-01` @e4ec197609 in `NAMING_LEGACY_READS` (local `advi_49f_chain_log_prefix`, occurrences 1,
`reference_count` 3, cutoff 2026-10-06) admit the frozen candidate bytes (`og-m-2b_candidate_frozen.patch`, sha256
`600a4b6da9e7...` = the CTO pin @5b44ba518d).

**The cell.**
- `OG-m-3` (= OG-m-2b) -- re-apply the frozen candidate UNMODIFIED over 2a: the dispatcher classifies a terminal invocation
  from its own chain log (last `CHAIN ` line; absent log, no terminal line or unconfigured env reads UNKNOWN and says so);
  the inline policy gains `ReadTheChainLog` (`s3:GetObject` on the chain-log prefix, from the local); the function gains
  `CHAIN_LOG_BUCKET` / `CHAIN_LOG_PREFIX`; the SSM document's upload target reads the local with an identical rendered
  command (not an apply target). No branch dispatches twice. WORLD. It is a new order, not a reopen, so 2a's VALID proof
  stands; it carries `<round>5</round>` because the L6 gate admits one issuance per round label, and drains with round 3.

**Edge and hold.** `OG-m-2`(a) -> `OG-m-3` (met, 40fcde8bf7). PHASE A (re-apply, naming gate, six tests, targeted plan)
runs at hand-off; PHASE B waits on the never-widen pair signed against
`deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-3_20260929.md` (CTO half `1.0.0_SA_CTO~O`, second half `3.0.0_SA_CVO~O`).

**Slot.** `~15`, continuing the worker that built 2a and froze the bytes.

## ADDENDUM R2-E.3 (2.0.0_SA_COO~O, 2026-09-29, on 1.0.0_SA_CTO~O's msgs 26198 and 26435) -- the G-C evidence order

**Cell `OG-g-1` -- G-C evidence.** `G-C` (section 6) is a gate, not a cell, and it holds `OG-v-7` (E1). Its record is
`1.0.0_SA_CTO~O`'s act, but its EVIDENCE -- a controlled, non-privileged identity's verified `tid`/`oid` from an
authoritative tenant source, and one bounded synthetic grant activated through `ops/schwab_entitlement_admin.py` under
`opal-gateway-access-admin` and read back strongly -- comes from the identity administrator, `0.7.0_AE_CloudOps`
(Andrew-direct 2026-09-20 ~18:0xZ, @768e6df290). The CTO ruled (msg 26435) that the vehicle is an ORDER, not a message:
the parked 2026-09-22 draft `deliverables/2.0.0_SA_COO~O/DRAFT_NOT_ISSUED_TO-OG-g-1_controlled_identity_and_grant.md` is
re-cut at HEAD and issued to the SESSION seat `0.7.0_AE_CloudOps~OG` (spawned 03:29:51Z on msg 26198).

- **Serves:** FWD-1 and FWD-3 .. FWD-8 only by unblocking `OG-v-7`; it grades none of them.
- **Scope source:** `OG-v-6`'s v2 seal (`SEALED_EXPECTED_V2.json`, RQ2-1 .. RQ2-7 on D_NEW 2026-09-25 / D_PREV 2026-09-24)
  and the protocol's A7 steps 3-4; bounded so the walkthrough's refusal cases still exist.
- **Does NOT:** close `G-C`, touch `ENABLED_INTEGRATIONS`, or run the walkthrough (`G-D`).
- **Edge:** `OG-g-1` -> `1.0.0_SA_CTO~O` writes `G-C` -> (with `G-D`) `OG-v-7`.
- **Label:** `<round>6</round>` (one issuance per round label; 3, 4 and 5 are held).

## ADDENDUM R2-E.4 (2.0.0_SA_COO~O, 2026-09-29, on 1.0.0_SA_CTO~O's msg 26488) -- the R-4 remedy for E5/E6

**Why.** `OG-r-3` (E6) measured the host serving `4248b70b39` INSUFFICIENT at contract scale: the 250,000-row export at
11 columns was refused on memory at 272,683,008 bytes, and export memory GREW with rows (171,974,656 / 225,271,808 /
>272 MB at 25k / 125k / 250k); the maximal query peaked 286,691,328 (cap 268,435,456). The CTO ruled R-4 branch (a):
a code gap -- the export buffers rather than streams -- so a remedy cell comes first and the contract numbers stand.

**Cell `OG-x-4` -- export flat at full width; the maximal query under 80% of the cap.** WORLD. PHASE A builds and proves
locally; PHASE B releases narrowly on the live base (resolved by content, the live `deploy-to-ec2.sh` carried
unchanged, one-deployer census, fresh NEVER-2 ledger, rollback proven) and re-measures on the host with
`onhost_bench.py` at the 11 exportable columns. Criteria, the ruling's three: (1) export peak at 11 columns within 10%
of the 25k peak at 25k / 125k / 250k rows; (2) maximal query <= 214,748,364 bytes; (3) OG-x-2's flatness proof re-run
at full width (`test_ogx4_ac03`).

- **Supersedes:** the open `OG-r-3`, whose measurement stands as this cell's input (its AC2/AC3 are measured FAILs).
- **Serves:** FWD-4, FWD-5, FWD-7.
- **PRD revision:** only if the remedied code still measures INSUFFICIENT on the same host.
- **Slot:** `~11`, continuing the subagent that built OG-x-2, released OG-x-3 and measured OG-r-3.
- **Label:** `<round>7</round>` (one issuance per round label; 3..6 are held); it drains with round 3.

## ADDENDUM R3-T (2.0.0_SA_COO~O, 2026-10-01, on PRD v1.2 C7 @c9fd271499) -- workstream TRNSPT-DEPS (orders O1-O5)

**Source.** PRD v1.2 C7 and its addendum table (`1.0.0_SA_CTO~O`, @725230b531, F1/N1 fix @c9fd271499; `prd-signoff.py
status` ADMITTED). Inputs: the NFRA_TRNSPT dependency file
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_GATEWAY_DEPENDENCIES_FOR_SITE_Z_20260930.md`, the transcript
spec `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` sections 4-6, and the branch triage
`deliverables/2.0.0_SA_COO~O/LAPTOP_MAIL_BRANCHES_TRIAGE_20260930.md` @6d41bd25ec. This is a WORKSTREAM under the
project's one issuer: a scope, not a second round, and the round-3 orders are untouched. Each cell is graded on its own
criteria only; NFRA_TRNSPT grades its own FWDs.

**The domain, by subtraction.** C7 has 14 clauses: 3 interactive, 3 transcript, 2 mail, 1 attachment, 4 headless,
the O3 measurement, and 2 preconditions. Each one maps below to exactly one owning cell. Excluded by name:
- spec section 9 (OneDrive upload, item permissions), which C7 does not admit;
- recordings, ad hoc calls and the application-permission route (spec section 7);
- any alert on a refusal (C7 "No alert").

| order | cell | what it is | risk | slot |
|---|---|---|---|---|
| O1 | `OG-tx-1` | BUILD: `find_online_meeting`, `list_meeting_transcripts` (follows `@odata.nextLink`) and `read_meeting_transcript` (`text/vtt` through an optional `accept` on `graph.call`, full-body sha256, offset/limit). Also `list_calendar` gains `onlineMeeting`, `seriesMasterId` and a start date. `innerError.code` is surfaced, with the two transcript codes distinct; there is no unattributed fallback. Each tool is registered in SAFE_TOOLS and NATIVE_TOOLS. The audit carries ids, never text. Scoped and restricted principals stay denied. | WORLD (floor) | ~15 |
| O4 | `OG-ml-1` | BUILD: ADOPT `gw-mail-tools-int` @6a7b9e78fa minus the LD-0613 hunk; take the three f-branch test files; re-read the tool count at the cut; pin `pypdf` (0 pins today). `read_email`'s `$select` gains the four fields, and the filtered list uses an opaque page token. The attachment tool stays INSPECT-only. Supersedes f1-f3. | WORLD (floor) | ~15 |
| O2 | `OG-hr-1` | BUILD: the headless transcripts route. A new prefix (builder-named), its own constant-time bearer accepted on that prefix only, a fail-closed GET-only Graph path allowlist, allow-by-key output (meeting id, transcript id, the two timestamps, the vtt body, bytes, sha256), the meeting allowlist as config, the server-held delegated token of the ONE fixed identity, and an audit of route, ids, bytes and bearer label. `/ms/*` is byte-unchanged. | WORLD (floor) | ~16 |
| O5 | `OG-hr-2` | BUILD: the headless mail route on the same pattern with a second prefix and bearer. It serves ONLY messages whose sender is on the sender table (no thread reach, @c9fd271499). The output is O4's `$select` plus the body. `$value` bytes are returned ONLY for a non-inline `application/pdf` under the size cap, with sha256; everything else returns metadata. | WORLD (floor) | ~16 |
| O3 | `OG-lt-1` | MEASURE: how long the server-held delegated token refreshes unattended before `NeedsLogin` (`app/token_broker.py:171-183`), with the instrument and timestamps. Read-only; under one day returns to the CTO before any `token_broker` change. | SERVED | ~17 |
| O2+O5 (+O1, O4) | `OG-rl-1` | SERVED: ONE narrow gateway release of tx-1, ml-1, hr-1 and hr-2 from the deployed commit re-read at the cut (by content, row Z-S21). It covers the two bearer secrets (Secrets Manager, SECRET-grammar names from the builder), a NEVER-2 ledger and never-widen halves. Its FIRST criterion is the negative arms run on demand: a cross-prefix bearer refused; an off-allowlist meeting refused; an off-table sender refused, including one in a table sender's thread; a non-PDF attachment returns metadata only. | WORLD | ~15 |
| O1 live | `OG-tx-2` | WORLD: spec section 6 steps 1-4 (REACH with its negative arm, COMPLETENESS, ATTRIBUTION, ALL FOUR) through the released tools as Andrew. HELD on G-TEAMS-TX. | WORLD | ~15 |

**Edges:**
- `OG-tx-1` -> `OG-ml-1` (both write `app/tools.py`, `destructive_ops.py`, `data_entitlement.py` and the tool-count
  assertion; serialised in one slot so the count is re-read once);
- `OG-ml-1` -> `OG-hr-2` (the route serves O4's `$select`);
- `OG-hr-1` -> `OG-hr-2` (both register routes in `server.py`; one slot);
- tx-1, ml-1, hr-1 and hr-2 -> `OG-rl-1`;
- `OG-rl-1` -> `OG-tx-2`;
- RELEASE SERIALISATION: OG-t-2 (round 3), then NFRA_MCPINDEX MX-r-7, then `OG-rl-1`. Each base is the previous live
  ref, read by content.

**Gates and holds:**
- **The whole workstream is CUT after OG-t-2 lands** (`1.0.0_SA_CTO~O` msg 27439).
- **G-TEAMS-TX** (Andrew via IT: `EnableGraphTranscriptAccess`, `EnableAttributedTranscripts`) holds `OG-tx-2` only.
  The build and the release do not wait on it.
- **G-SENDERS** holds `OG-rl-1`'s mail arm:
  - the sender table's values (Manav's and Yang's addresses, NFRA_TRNSPT's data asset);
  - 0 of 70 files in the NFRA_TRNSPT and `data/transcripts` trees name it (comp-find, corpus=all, 2026-10-01);
  - Yang's addresses are not yet supplied (N1).
- **G-MEETINGS** holds `OG-rl-1`'s transcript arm: the four allowlisted meeting ids. `find_online_meeting` resolves them
  after release; until then the allowlist is empty, which fails closed.
- **Route names come from `lib/opal_naming.py`.** It has a SECRET grammar but no route kind today, so a refusal is a
  missing registry row (rule 30): a BLOCKING row routed to the registry owner, never a hand-typed name.

**Fan-out:** 7 orders in 2 connected components ({tx-1, ml-1, hr-1, hr-2, rl-1, tx-2} and {lt-1}). There are
N = 3 slots, cap 8:
- `~15`: {tx-1, ml-1, rl-1, tx-2};
- `~16`: {hr-1, hr-2}, which joins ~15 at ml-1 -> hr-2 and at rl-1;
- `~17`: {lt-1}.

Slots ~15..~17 are unused: round 3 named ~10..~14.

**Battery (blindness stated):**
- (a) The clause map above is a forward list over C7's 14 clauses. Its domain is C7 itself, not NFRA_TRNSPT's needs.
- (b) Write-surface overlap was read from the PRD's own named files, not from a diff. A file the build discovers is
  a surprise row.
- (c) No cell grades NFRA_TRNSPT's FWD-1 or FWD-7. The positive mail and transcript runs are that project's.

## ADDENDUM R3-T.1 (2.0.0_SA_COO~O, 2026-10-01 ~04:3xZ, on PRD v1.3 @2b8f3151c6 and the CTO's self-drive tick-1 rulings)

**Source.** PRD v1.3 C7 (`1.0.0_SA_CTO~O` msg 27481, option (a); `prd-signoff.py status` ADMITTED) and the four rulings
in `project.json` `blocking` (tick-1 prefix, msg 27490, arming record @80102ed73d). The issuer rules inside its own
decomposition; ENDPOINT is unchanged.

- **Names (supersedes R3-T "Route names come from `lib/opal_naming.py`").** The headless prefixes are the fixed literals
  `/hx/transcripts` and `/hx/mail`, graded for distinctness only. The bearer secrets are `gateway/transcripts/bearer`
  and `gateway/mail/bearer`, each `grade(..., "SECRET")` CONFORMANT. Row Z-W16-S1 is dispositioned by amendment A1 on
  `OG-hr-1` and `OG-hr-2`.
- **G-SENDERS is NOT a gate** (ruling (d)). The sender table is a data asset; `OG-rl-1` ships it with Manav's addresses
  as they stand, and Yang's join when supplied, as a data change.
- **New cell `OG-pr-1` -- the gateway read secrets and their one grant** (CTO ruling R3 / C11,
  `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d; tick-1 ruling (b), row Z-S24). It creates THREE
  Secrets Manager entries out of band, values never printed: `gateway/transcripts/bearer` and `gateway/mail/bearer`
  (random), and `gateway/principals/rosters` (both rosters, from the site-Z Part D file). One Terraform role policy
  `opal-gateway-gateway-read-secrets` grants `secretsmanager:GetSecretValue` on exactly those three ARNs (the
  `graph-read.tf` pattern), by a targeted `safe-apply` that is Terraform act #2 of the train (C4), under a NEVER-2
  ledger. Acceptance (R3): `simulate-principal-policy` reads `allowed` on all three and `implicitDeny` on a sibling
  `gateway/*` ARN; and the host reads the roster secret's shape under its own role. WORLD. Slot `~18` (new; independent
  of the build chain). No service changes. Label: `<round>9</round>`, its own one-cell issuance (round 8's issuance
  admits no new file).
- **OG-rl-1 carries R4.** Its release-branch `deploy-to-ec2.sh` reads the rosters host-side from
  `gateway/principals/rosters` (the deploying-shell variables go), and it no longer creates the two bearers (OG-pr-1
  did). A third criterion, `rl.AC3.sh`, reads the SHIPPED template.
- **Rotation (ruling (c), row Z-W17-S1).** The value printed was host `.env` line 14's second token: line 14 is
  `OTP_BEARER=<49f> <cot>` unquoted, so `bash` ran the second token as a command and printed it. That is the cot OTP
  capability bearer, Secrets Manager `blackdiamond/cot/otp-gateway-token`. `OG-rl-1` rotates it in the same release,
  after PHASE A reads every presenter of that bearer and how each one reads it.

**Edges added:** `OG-pr-1` -> `OG-rl-1` PHASE B (the grant is applied first). Train order (R1): MX-r-7 -> MS-d-2 ->
`OG-rl-1` (swap with MS-d-2 if ready first); until `OG-rl-1` serves, the issuer hands the rosters off-repo to
`2.0.0_SA_COO~MI` and `2.0.0_SA_COO~MS` (C2).

**Fan-out:** 8 orders in 2 connected components; slots `~15`, `~16`, `~17` (closed), `~18`; cap 8.

**Battery (blindness stated):** the line-14 attribution is read from bash semantics on the live render template
(`d61fde4693`), not from the value. `OG-rl-1` PHASE A confirms it by shape only, printing a boolean.

## ADDENDUM R3-T.2 (2.0.0_SA_COO~O, 2026-10-01 ~07:3xZ) -- the headless prefixes' public reach

**Finding.** The gateway's HTTPS listener signs every request in through Entra OIDC by default; machine routes reach
the app only through a forward-only listener rule on their exact paths (`/ms/*` priority 31 and 33, `/otp/*` 30,
`/graph/*` 32). `/hx/*` has none, and `OG-rl-1`'s bounds leave the ALB untouched. Measured: an unauthenticated GET on
either `/hx/` prefix returns 302 to `login.microsoftonline.com`. So C7's headless routes would release unreachable from
the laptop (the consumer of order 103564) and `rl.AC1.sh` (public URL) could not pass.

**New cell `OG-al-1`** -- ONE forward-only `aws_lb_listener_rule` for `/hx/transcripts/*` and `/hx/mail/*` on the
`ms_ingest_capability` pattern, a targeted `safe-apply` under a NEVER-2 ledger, after `OG-pr-1` (same root, never
concurrent). WORLD. Slot `~18`. Label `<round>10</round>`, its own one-cell issuance. Edge `OG-al-1` -> `OG-rl-1` PHASE
B. Serves: FWD-1 (the journey's machine hop) and NFRA_TRNSPT's FWD-1 hops 1-2. Criteria: the TF shape; the live rule
plus probes (both `/hx/` prefixes reach the app, a non-`/hx` control still meets the sign-in).

## ADDENDUM R3-T.3 (2.0.0_SA_COO~O, 2026-10-01 ~13:2xZ, on PRD v1.4 @dabb8e1e9f) -- the /hx/mail LISTING route

**Source.** PRD v1.4 C7 "Mail listing" and its addendum (`prd-signoff.py status` ADMITTED); laptop order 103750 (relay
@6963658f49); `1.0.0_SA_CTO~O` msg 27843 (cut one build + one release as its own round label; fold Z-S36's durable
fix). Label `<round>11</round>`, ONE issuance, two cells, one chain (`OG-hl-1` -> `OG-rl-2`). fanout: 1 of 1 chain,
cap 8.

| cell | what | risk | slot |
|---|---|---|---|
| `OG-hl-1` | BUILD: `GET /hx/mail/messages` in `app/mail_route.py` (`LIST_ROUTE`), registered in `server.py`; the v1.4 rules (sender-bound with a per-row own-`from` re-check, 5-key rows, 31-day window, page_size 1..50 default 25, 200 pages, an opaque page token bound to sender + window + the allowlisted path and never a Graph URL, ascending `receivedDateTime`, empty window 200/0/null); the Graph allowlist gains `^/me/messages$`; audit = route, sender HASH, window, row count, label. PLUS Z-S36's durable fix's single source: `deploy/mail_sender_table.txt`, one address per line, kept equal to `criterion.py` `DEFAULT_AUTHORS` by a test (the `deploy/NFRA_OPLGTW_CONTRACT.json` pattern). | WORLD (floor) | ~16 |
| `OG-rl-2` | RELEASE, train slot 5 (after MX-r-8): narrow, from the live ref; the template reads `MAIL_SENDER_TABLE` host-side from the shipped `deploy/mail_sender_table.txt` and REFUSES an empty table before any `.env` write (the deploying-shell `OG_MAIL_SENDER_TABLE` goes); NEVER-2 ledger; CTO + CVO halves. Acceptance: the laptop's four checks + the issuer's two token arms (9 conditions, `rl2.AC1.sh`). | WORLD | ~15 |

**Z-S36's fix, the issuer's choice of form.** The CTO asked for a host-side read "like the R4 rosters". The rosters are
secrets and live in Secrets Manager; the sender table is a committed data asset (`criterion.py`). A Secrets Manager copy
would be a second runtime source that drifts from `criterion.py` (Yang's addresses land there) and needs a fourth ARN on
the grant (a Terraform act). The artifact-shipped file kept equal by a test is host-side, single-source and needs no IAM.

**Battery (blindness stated):** the paging arm needs a window holding two or more table-sender messages with
attachments; 2026-08-01..31 (half-open, to 08-31T00:00Z) holds five on today's read (`search_email`: 08-02, 08-09, 08-15, 08-22, 08-30), but the mailbox can change.

## ADDENDUM R3-T.4 (2.0.0_SA_COO~O, 2026-10-01 ~17:4xZ) -- the Tax SMA gateway release, both halves (Andrew-direct ~17:2xZ)

**Source.** Andrew-direct ~17:2xZ "Site Z does both" (relay `org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261001_1726Z_ANDREW_DIRECT_SITEZ_RUNS_TAXSMA_GATEWAY_RELEASE_BOTH_HALVES.md`
@d34037d1f5): the MDPF_TAXSMA exclusion is lifted for THIS one release. Spec: laptop `4.0.0_SA_CRO` msg 103933 (relay
`RELAY_20261001_1733Z_LAPTOP_CRO_103933_TAXSMA_GATEWAY_RELEASE_SPEC.md` @65e0886dc1). Andrew ~17:3xZ: capability ON at
this deploy, the opalbloomberg@ oid confirmed from the host broker record before any upload (msgs 27991, 27992).
`1.0.0_SA_CTO~O` msg 27986: cut as round label 12. Label `<round>12</round>`, ONE issuance, two cells, two independent
chains; fanout: 2 of 2 chains, cap 8.

| cell | what | risk | slot |
|---|---|---|---|
| `OG-tt-1` | TERRAFORM (train act #4): ONE forward-only `aws_lb_listener_rule` for EXACTLY `/ms/taxsma-workbook` (no `/ms/*` wildcard), on the `hx-capability.tf` pattern, a free priority, targeted `safe-apply`, plan 1/0/0, NEVER-2 ledger `nfra-oplgtw-taxsma-alb-rule`. | WORLD | ~18 |
| `OG-tr-1` | NARROW APP RELEASE on live `0a1d9079c6`: the four Tax files from CLOUD (`app/taxsma_workbook.py` sha256 `6acc3e8c...`, its `server.py` import + Route, its `config.py` two fields, `tests/test_taxsma_workbook.py`) merged onto the live bytes, plus two `.env` lines in `deploy-to-ec2.sh`: `TAXSMA_WORKBOOK_BEARER` read host-side from `gateway/global/taxsma-workbook-token` (the role's read exists, laptop TX-i-3) and refused when empty; `TAXSMA_WORKBOOK_IDENTITY` from the deploying shell, validated as one `<tid>/<oid>` pair (a personal identifier: never committed), the opalbloomberg@ oid confirmed from the host token-broker record before any upload. `.env` 46 -> 48. CTO + CVO halves; NEVER-2 ledger `nfra-oplgtw-taxsma-route-release`. | WORLD | ~15 |

**Acceptance** (the spec's section 4): `tr.AC1.sh` (module sha256 on the host; no-bearer `UNAUTHORIZED_CAPABILITY`
through the ALB; `/mcp` 401 unchanged; `.env` 48 keys, capability ON), `tr.AC2.sh` (narrow + NEVER-2), `tt.AC1/AC2`
(the rule's shape, then live with probes: the Tax path reaches the app, an unknown `/ms` path and `/` still sign in,
`/ms/sites` still 401). The rule's ARN and priority are reported.

**Blindness stated:** the identity is confirmed from the broker's account records by username; the Part D record
(`PART_D_RECORD_20260930.md`) is the second source for the same mapping.

## ADDENDUM R3-T.6 (2.0.0_SA_COO~O, 2026-10-02 ~17:5xZ) -- the /hx/teams gateway release, ONE order (Andrew-direct, today)

**Source.** Andrew-direct (laptop `0.0.0_AB_MSTR` bus d38d682f, 17:17Z, relayed by `0.0.0_AB_MSTR~Z` msg 28592):
"release the gateway /hx/teams route TODAY ... (20:30-21:30Z) depends on it." Request: laptop `4.0.0_SA_CRO`
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SITEZ_GATEWAY_RELEASE_REQUEST_HX_TEAMS_20261002.md` @a53c8452b4. Spec and
the CTO half of the never-widen sign-off: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md`
(msg 28599). Label `<round>13</round>`, ONE issuance, ONE cell, ONE chain; fanout: 1 of 1 chains, cap 8. The id
`OG-rl-3` is the CTO's: the unissued round-13 draft that also used it (`deliverables/2.0.0_SA_COO~O/r13/drafts_not_issued/`,
draft addendum R3-T.5) is renumbered when that round issues; nothing of that draft rides this release.

| cell | what | risk | slot |
|---|---|---|---|
| `OG-rl-3` | (1) TERRAFORM: `gateway-read-secrets.tf` gains a fourth data source + ARN for `gateway/teams/bearer` (same statement, same action, no wildcard), and `hx-capability.tf`'s value from 8e6872f265 (rule 35 gains `/hx/teams/*`) -- ONE targeted `safe-apply`, exactly two in-place changes. (2) NARROW APP RELEASE on live `3a7d6a7dc8`: db92656c72's five files (`app/teams_route.py`, `tests/test_teams_route.py` new; only its hunks in `app/config.py`, `app/server.py`, `app/taxsma_workbook.py` = Z-S41) merged onto the live bytes, plus `deploy-to-ec2.sh` reading `gateway/teams/bearer` host-side (refused when the read fails or is empty) into `TEAMS_BEARER=` and `TEAMS_BEARER_LABELS=teamsassist`. `.env` 48 -> 50. CTO + COO halves; NEVER-2 ledgers `nfra-oplgtw-hx-teams-infra` and `nfra-oplgtw-hx-teams-release`. | WORLD | ~15 |

**Acceptance** (the ruling's AC1-AC4, checks under `deliverables/2.0.0_SA_COO~O/hxteams/checks/`): `ht.AC1.sh` (IAM
allowed on the bearer / implicitDeny on a synthetic `gateway/teams/` sibling / policy exactly 4 ARNs / rule 35 three
values), `ht.AC2.sh` (host module sha256, `.env` 50 keys, `/hx/teams/x` refused by the app, `/` 302), `ht.AC3.sh`
(with the bearer `/hx/teams/me` and `/hx/teams/chats` 200; a 502 with `graph_status` 403 is a BLOCKING row to Andrew),
`ht.AC4.sh` (floor: `/hx/mail/x` and `/hx/transcripts/x` 404 as measured on live, the Tax route's own refusal and Z-S41
bytes, NEVER-2 closed, narrow census). Pre-cut controls 17:5xZ: AC1 1 of 4, AC2 1 of 4, AC3 0 of 2 (302), AC4 0 of 4.

**Blindness stated:** the two POST verbs are not graded here (the CTO's ruling: Andrew's first EOD post is their
exercise). The ruling's "401" for `/hx/mail/x` was re-measured as 404 on live and AC4 grades "unchanged from live".
No real ungranted `gateway/*` secret remains after this release (5 exist: 4 in this policy, 1 in the Tax policy), so the
negative IAM arm is a synthetic sibling ARN.

## ADDENDUM R3-T.7 (2.0.0_SA_COO~O, 2026-10-03 ~00:2xZ) -- round 14, the enrichment list re-cut on live 4231bd2ddc

**Source.** `ledger/ROUND_ANALYSIS.round13.md` @fea5fbcdbf section 4 (+ addendum @b100b15b2e): round 12's section-5 list
stands, re-cut on the new live ref `4231bd2ddc`. Andrew-direct ~23:4xZ "all appproved go" (relay `0.0.0_AB_MSTR~Z` msg
28810; record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_234xZ_ALL_APPROVED_CLOUD_PUSH_ANALYST_CLOSE_RUN_OPLGTW_ROUND14.md`).
The unissued round-13 drafts (`deliverables/2.0.0_SA_COO~O/r13/drafts_not_issued/`, draft addendum R3-T.5) are the
base; their checks are copied to `r14/checks/` with the live-ref changes. Item 1 stays on CTO rulings 28152/28154 (G-C
retired; the walkthrough principal is Alyssa after Andrew's own speed and efficacy tests). Label `<round>14</round>`,
ONE issuance, ten cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-g-2` | 1 | as R3-T.5, at live `4231bd2ddc` (code read + one probe at the WRITE_CAPABLE tier; pilot principal by hash). No grant write. | SERVED | ~23 | worker |
| `OG-au-1` | 2 | as R3-T.5: `read_meeting_transcript`'s audit record gains `bytes` and `principal` (row Z-W15-S23), on CLOUD. | WORLD | ~19 | worker-light |
| `OG-sr-1` | 2 | NEW (the CVO's post-hoc finding on OG-rl-3, CTO addendum @b100b15b2e): `mail_route` and `transcript_route` refuse a bearer value shared with another route, mirroring `teams_route`'s `OTHER_ROUTE_BEARERS`; on CLOUD (the four files were byte-equal to live at the cut). | WORLD | ~24 | worker-light |
| `OG-rl-4` | 2 | The next gateway release on live `4231bd2ddc` (the draft `OG-rl-3`, renamed): au-1's lines, sr-1's four files, `.env` quoting (Z-S32; 50 keys, 4 whitespace values), the roster count (Z-S34), `TAXSMA_WORKBOOK_IDENTITY` host-side, the contract pinned (Z-W19-S13). Z-S41 is out (it shipped). CTO + COO + CVO halves; NEVER-2 ledger `nfra-oplgtw-gateway-release-r14`. | WORLD | ~15 | worker |
| `OG-tf-1` | 3 | as R3-T.5, plus row Z-W15-S25 (the grant-writer `source_code_hash` diff, classified by content before the fix; CONTENT-DIFF stops BLOCKING). No apply. | WORLD | ~17 | worker |
| `OG-wp-1` | 4 | as R3-T.5 (the `email_deny` record's origin; partitions as fixtures). | SERVED | ~20 | worker-light |
| `OG-r-4` | 5 | as R3-T.5, against the SERVED `4231bd2ddc`; `r4.AC3` PINNED to that commit. | SERVED | ~16 | worker |
| `OG-tb-1` | 6 | as R3-T.5 (the 9 OPLGTW red tests). | WORLD | ~18 | worker |
| `OG-o-4` | 6 | as R3-T.5, handed after `OG-rl-4` closes (the runbook names the live release); OGO2-J1 at L9 by `3.0.0_SA_CVO~O`. | WORLD | ~21 | worker-light |
| `OG-gr-1` | 7 | as R3-T.5 (grain measurement, row Z-W10-S1). | LOCAL | ~22 | worker |

**Chains.** `OG-au-1` + `OG-sr-1` -> `OG-rl-4` -> `OG-o-4`. `OG-r-4` gates `OG-rl-4`'s PHASE B, so the bench and the
deploy never overlap. The other five cells stand alone. fanout: 8 independent starts (`au-1`, `sr-1`, `r-4`, `g-2`,
`tf-1`, `wp-1`, `tb-1`, `gr-1`), cap 8; `rl-4` and `o-4` are handed as their chains clear.

**Changes from the R3-T.5 draft, each with its cause:**
- live ref `3a7d6a7dc8` -> `4231bd2ddc` everywhere it means "live" (OG-rl-3 shipped);
- `OG-rl-3` -> `OG-rl-4` (the label is taken), with the CVO half required (analysis round 13, ruling 4);
- `OG-sr-1` added (the CVO's finding);
- `.env` 48 -> 50 (`r14/RL4_ENV_KEYS_BEFORE.txt`, SSM b596b265);
- `r4.AC3` pinned and `OG-o-4` chained (both read the live manifest, which OG-rl-4 moves in this round);
- `g2.AC1` resolves citations at `4231bd2ddc`;
- the draft table's risk column is corrected to each order's own `<risk>`.

**Guard N1** (the CVO's half on OG-rl-3): any rotation of `gateway/{teams,mail,transcripts}/bearer` re-runs ht.AC3's
200 arm the same sitting, until `OG-rl-4` ships the symmetric refusal.

**Stated dependencies, not cells.** These carry over from R3-T.5:
- The G-E grant write and the `schwab` switch follow Andrew's tests and `OG-g-2`.
- Z-S43's re-run waits on the invitation.
- Z-W13-S5 waits on the LGIC gate owner.
- Z-W12-S7, the operator re-consent, is due before 2026-10-15.

Z-S41 is discharged. The D9 -> D6 move stays deferred, and round 14 issues in D9.

## ADDENDUM R3-T.8 (2.0.0_SA_COO~O, 2026-10-03 ~18:3xZ) -- round 15, the CTO's round-14 list (R1-R3)

**Source.** `ledger/ROUND_ANALYSIS.round14.md` @cf6e539a6d section 4 (msg 28925), on R1 (the grant writer's build input
pinned to the gateway's released ref), R2 (the owner keys in `gateway/principals/rosters`) and R3 (the build and layer
inputs). Label `<round>15</round>`, ONE issuance, four cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-gw-1` | 1 | `build_package.py` stages from `EC2_MANIFEST.json`'s `deployed_commit` (never the checkout); a planted dirty edit is ignored; an unresolvable commit refuses; `.build/` ignored (row Z-W17-S3). | WORLD | ~25 | worker |
| `OG-gw-2` | 2 | The ONE catch-up apply: the grant writer redeployed from `af2d762970`'s closure, targeted, under CTO + COO + CVO halves. PHASE A names every behaviour change of the 3 differing files. Read back by content. Rollback is Terraform only. Ledger `nfra-oplgtw-grant-writer-catchup`. | WORLD | ~26 | worker |
| `OG-tf-2` | 3 | R2 + R3: the owner keys move into the rosters secret (hash-equal to live) and are read by a data source; the build and layer inputs need no copy. The untargeted plan from a FRESH worktree reads No changes. Ledger `nfra-oplgtw-tf-root-owner-keys`. The closing hash goes to `0.0.0_AB_MSTR~Z`. | WORLD | ~17 | worker |
| `OG-gr-2` | 4 | READ-ONLY (Andrew-direct ~17:3xZ): why `dim_position` 2026-09-21 collides at both masters; GRAIN_FOUND (52 of 52) or UPSTREAM_DEFECT with its owner. | LOCAL | ~22 | worker |

**Chains.** `OG-gw-1` -> `OG-gw-2` -> `OG-tf-2`; `OG-gr-2` stands alone. fanout: 2 independent starts (`gw-1`, `gr-2`),
cap 8.

**Checks** (`deliverables/2.0.0_SA_COO~O/r15/checks/`): gw.AC1/AC2, gw2.AC1/AC2, tf2.AC1/AC2, gr2.AC1. Pre-cut 18:2xZ
all FAIL. gw2.AC1 reads 3 DIFF (`config.py`, `data_entitlement.py`, the contract JSON), as OG-tf-1 measured. tf2.AC1
reads plan rc=1 with 2 errors and 2 missing required variables. tf2.AC2 reads the secret's 3 keys, with no owner keys.

**Carried, not cells:**
- OGO2-J1 (CVO, L9);
- row Z-W15-S30's allowlist (NFRA_TRNSPT, via `0.0.0_AB_MSTR~Z`);
- OG-v-7 (Andrew's tests, then Alyssa);
- OG-v-8 (G-E).

The D9 -> D6 move stays deferred (R5).

## ADDENDUM R3-T.8.1 (2.0.0_SA_COO~O, 2026-10-03 ~18:4xZ) -- OG-v-8 cancelled; OG-o-5 DRAFTED for round 16

**Source.** `ledger/ROUND_ANALYSIS.round14.md` section 6 @2f46788988 (1.0.0_SA_CTO~O msg 28937), on the CVO's L8/L9
(`ADJUDICATION_v4.Z.md` @d4c58bd8ef):
- **R6 cancels `OG-v-8`.** It was a round-2 slot held on G-E/G-F. The issuer flips it here. The pilot-walkthrough
  grading re-enters as a NEW cell when G-E stands.
- **R7 accepts the CVO's runbook section-7 text remedy** as round-15 cell `OG-o-5`.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-o-5` | 6 | Runbook section 7, text only: 7.1 states the deploy re-renders `schwab`; 7.2 step 2 re-applies 7.1 after any restore and confirms `integration_enabled=false`; 7.3 names the read command. OGO2-J1 is re-graded at L9 by the CVO. | WORLD | ~21 | worker-light |

**NOT issued in round 15.** The TO issuance gate refuses a second issuance into a round that already has one (ONE ISSUER PER ROUND, keyed to the round). OG-o-5 is held as a draft at `deliverables/2.0.0_SA_COO~O/r15/drafts_not_issued/` with its check `r15/checks/o5.AC1.sh` (pre-cut FAIL: anchors absent; rb.AC1-AC3 3 of 3), and is cut with round 16's issuance. Nothing waits on it: the pilot is not cut before G-E. **The pilot's host-side `schwab` flag** (R7) is a later release under
three halves and is NOT cut before G-E (YAGNI).

## ADDENDUM R3-T.9 (2.0.0_SA_COO~O, 2026-10-03 ~22:2xZ) -- round 16, the CTO's round-15 list

**Source.** `ledger/ROUND_ANALYSIS.round15.md` @b56208fd64 section 4 (msg 29033):
- R9 adopts the measured grain as a paging row-uniqueness key;
- R10 dispositions S46 and W17-S4;
- R11 accepts the issuer's helper fixes.

Label `<round>16</round>`, ONE issuance, five cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-gr-3` | 1 | R9 on CLOUD: `query.py` `DATASET_GRAINS` + `datasets.json` `grain_fields` (dim_position + `quantity_settled_unsettled`, `quantity_cash_settled`; dim_asset + `security_description_line_1`); the grain note says ROW-UNIQUENESS, not identity; tests pin a measured fixture and a planted collision. Both files were byte-equal on CLOUD and live at the cut. | WORLD | ~22 | worker |
| `OG-rl-5` | 2 | The release carrying gr-3 on live `af2d762970`, under CTO + COO + CVO halves (paging becomes available where it refused). Ledger `nfra-oplgtw-gateway-release-r16`. | WORLD | ~15 | worker |
| `OG-o-5` | 3 | The runbook section-7 text remedy (drafted under R3-T.8.1); OGO2-J1 re-graded at L9 by the CVO. | WORLD | ~21 | worker-light |
| `OG-ts-1` | 4 | Row Z-W26-S4: the grant writer's tests run against the pinned staged closure, not HEAD's tree. | WORLD | ~25 | worker-light |
| `OG-ar-1` | 5 | Every OPEN remediation row triaged: owner + one of `remediated_by` / `moves_when` / `close_reason` (41 OPEN at the cut); the CVO advances rows. | LOCAL | ~27 | worker |

**Chains.** `OG-gr-3` -> `OG-rl-5`; the other three stand alone. fanout: 4 independent starts, cap 8.

**OG-rl-5's acceptance deviates from the analysis wording, named.** "For an EXISTING grant holder" is measured with a
SYNTHETIC principal and grant on the served engine (the OG-r-4 mechanism). No agent reads as another person, and
Andrew's own session holds no Schwab grant. The real holder's read is UNEXERCISED until her next use.

**Pre-cut 22:1xZ.** Every new check FAILs on absence. The rl-5 floor (rl4.AC1, ht.AC2) PASSes on live.

## ADDENDUM R3-T.10 (2.0.0_SA_COO~O, 2026-10-05 ~00:3xZ) -- round 17, the CTO's round-16 list

**Source.** `ledger/ROUND_ANALYSIS.round16.md` @1f439fe6aa, section 4 (msg 29338). The grades read 0/2/6:
- FWD-4 is NOT_REALIZED because `dim_asset` can be queried but not downloaded;
- FWD-2 is narrowed to balances.

R13 rules row Z-W15-S36 as (a): the release-branch commit is made under the audited override. Label
`<round>17</round>`, ONE issuance, six cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-q-7` | 1 | The C3 holdings restriction (`sem.qualify_asset_plan`) on `prepare_download` and `export_query`, retiring their two placeholder guards. A no-seam test of four named cases (held only, planted unheld absent, empty holdings refused, query unchanged). | WORLD | ~22 | worker |
| `OG-rl-6` | 2 | The release carrying q-7 on live `4b6b823fae`, under CTO + COO + CVO halves: `dim_asset` downloads open under C3. Ledger `nfra-oplgtw-gateway-release-r17`. Its release-branch commit follows R13 (a). | WORLD | ~15 | worker |
| `OG-gr-4` | 3 | Read-only: `dim_balance`'s grain `(account,)` measured for uniqueness on every served snapshot (28 at the cut), and one `dim_balance` rows page served (synthetic principal, 0 grants). AC1 passes on either branch; a not-unique result sends a grain ruling to the CTO. | WORLD | ~26 | worker |
| `OG-ti-1` | 4 | Row Z-W15-S37: per-module session managers or apps, so the whole schwab set passes in ONE pytest process with 0 setup errors. Tests only. | WORLD | ~25 | worker-light |
| `OG-pm-1` | 5 | Row Z-W16-S5: p95 over the full trading day 2026-10-05 on `4b6b823fae`, against 0.5535 s and the 20% cap, graded. Handed after 2026-10-06T00:00Z. | WORLD | ~27 | worker-light |
| `OG-ar-2` | 6 | The issuer's seven OPEN remediation rows (W6-S2, W1-S9, W2-S6, Z-W13-S5, Z-W12-S7, S63, Z-W15-S31): each gets an owner plus one of `remediated_by`, `moves_when` or `closure` with one of the four reasons. Z-W12-S7 is dated (~2026-10-18). | LOCAL | ~21 | worker-light |

**Renamed, named.** The analysis calls item 1 "OG-q-6". That id is the completed C3-rules wiring cell of 2026-09-18
(R-OG-18, `TO-OG-q-6.c3-rules-wiring.md`), so item 1 is `OG-q-7`. The release, which the analysis calls "OG-rl-6",
keeps that id.

**Chains.** `OG-q-7` -> `OG-rl-6`. `OG-gr-4`, `OG-ti-1` and `OG-ar-2` stand alone. `OG-pm-1` stands alone, with a dated
start.

**fanout.** 4 independent starts now (q-7, gr-4, ti-1, ar-2), then rl-6 after the q-7 drain and pm-1 after
2026-10-06T00:00Z. Cap 8.

**Stated dependencies, not cells (analysis section 4):**
- OG-v-7 waits on Andrew's tests, then Alyssa.
- The pilot waits on G-E and R7's flag.
- Z-S43 waits on the meeting invitation.
- The D9 -> D6 move waits on the joint boundary with NFRA_MCPINDEX.

**Pre-cut.** Every new check FAILs on absence. The rl-6 floor (rl4.AC1, ht.AC2) PASSes on live `4b6b823fae`. The
one-process and per-file suite readings are in the issuance commit.

## ADDENDUM R3-T.11 (2.0.0_SA_COO~O, 2026-10-06 ~01:xxZ) -- round 18, the CTO's round-17 list

**Source.** `ledger/ROUND_ANALYSIS.round17.md` @5c352b300b, section 4 (msg 29841). The grades read 0/1/7: FWD-7 is
NOT_REALIZED on the p95 breach.
- **R16:** CLOUD is the source of record, with a DRAIN-BACK step.
- **R17:** the cause is read before any fix or cap ruling.
- **R18:** S41 is at Andrew. Z-S55 becomes a doc cell. Z-W15-S51's pre-GO check exercise becomes a standing step.

Label `<round>18</round>`, ONE issuance, four cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pm-2` | 1 | Read-only latency cause read. Per-route counts and p95 for 2026-10-05 and 2026-09-30 from a named instrument, with routes at OG-p-1 split from those added since. Hypothesis (i) tested first; finding in {MIX, SLOWDOWN, BOTH, UNDETERMINED}; 0 writes. | WORLD | ~27 | worker |
| `OG-ln-1` | 2 | R16 reconcile. Every CLOUD-vs-live difference under the gateway tree is classified, LIVE-ONLY hunks are ported to CLOUD, and CLOUD-ONLY items are listed with owner and disposition (OA-e-10 first). No release. | WORLD | ~22 | worker |
| `OG-dc-1` | 3 | Z-S55: `.tools/m365-mcp-kit/` rewritten (or retired with a pointer) to the hosted reconnect. | LOCAL | ~21 | worker-light |
| `OG-ti-2` | 4 | Z-W15-S37/S40: isolation finished. No per-module reset seam, and the whole set and the S40 subset green in one process. Tests only. | WORLD | ~25 | worker |

**The issuer's own act, in this issuance (not a cell).** `deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` is the
gateway release-order form, with R16's DRAIN-BACK (Phase D) and R18's pre-GO check exercise (step 7). Every later
`OG-rl-*` is cut to it.

**Chains.** None: four independent starts. `OG-ti-2` and `OG-ln-1` both touch `tests/`. The issuer re-runs `ti2.AC1`
on the drained union.

**fanout.** 4 independent starts, cap 8.

**Stated dependencies, not cells:**
- Z-W15-S41's grant is at Andrew (R18; REC yes).
- OG-v-7 waits on Andrew's tests, then Alyssa.
- The pilot waits on G-E and R7's flag.
- Z-S43 waits on the meeting invitation.
- OA-e-10 ships after OG-ln-1, under R16's terms.

## ADDENDUM R3-T.12 (2.0.0_SA_COO~O, 2026-10-06 ~02:xxZ) -- round 19, the CTO's round-18 list

**Source.** `ledger/ROUND_ANALYSIS.round18.md` @b397c851c0, section 4 (msg 29859). The grades read 0/0/8: every FWD is
HELD on a human act.
- **R19:** a per-route latency cap; the aggregate p95 becomes a diagnostic only.
- **R20:** Z-S55 is REMEDIATED; S41 stays at Andrew.
- **R21:** a route-inventory pre-GO arm, written into the issuer's `RELEASE_ORDER_FORM.md` as step 7a in this issuance.

Label `<round>19</round>`, ONE issuance, two cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ts-2` | 1 | Z-W22-S10: ROUTE_CLASS classifies `/yearinreview` and `/yearinreview/`. Z-W22-S9: host-inputs at 51 keys, and the build_package call on CLOUD's signature. Z-W25-S3: a per-process export directory. Tests only. | WORLD | ~25 | worker |
| `OG-rl-7` | 2 | The r19 release: every CLOUD-only item in LINEAGE_R18 (18), plus ts-2's tests, onto live `37be3485db`, under three halves, cut to `RELEASE_ORDER_FORM.md` in full (pre-GO exercise, R21 inventory, DRAIN-BACK). OA-e-10's `/login` admit lists come from 30 days of audit, and an outsider BLOCKS. After it, CLOUD equals live. | WORLD | ~15 | worker |

**Chains.** `OG-ts-2` -> `OG-rl-7`. **fanout:** 1 start now; rl-7 follows the ts-2 drain. Cap 8.

**Stated dependencies, not cells:**
- Z-W15-S41 is at Andrew.
- OG-v-7: Andrew's tests, then Alyssa.
- G-E.
- R7's host-side flag.
- Z-S43.

## ADDENDUM R3-T.13 (2.0.0_SA_COO~O, 2026-10-06 ~06:xxZ) -- round 20, the CTO's round-19 list

**Source.** `ledger/ROUND_ANALYSIS.round19.md` @98c25ed40e, section 4 (msg 29925). The grades read 0/0/8.
- **R23:** Z-W27-S3 and Z-S55 were ruled last round.
- **R24:** OA-e-10's re-cut is cut now, as a tier-based `/login` admit set with its own audit record.

Label `<round>20</round>`, ONE issuance, three cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-lg-1` | 1 | R24: `/login` admits the server-held identities plus every principal whose resolved tier carries a Graph-using tool. Restricted profiles and an unresolvable tier refuse; the Analyst's service identity is refused. One audit record per `/login` request. Six named tests. | WORLD | ~22 | worker |
| `OG-rl-8` | 2 | The r20 release of OG-lg-1 on live `cf4b036e62`, under three halves, cut to `RELEASE_ORDER_FORM.md` in full. The admit set BEFORE and AFTER over the current principal population; a non-restricted principal lost BLOCKS. DRAIN-BACK. | WORLD | ~15 | worker |
| `OG-fl-1` | 3 | Z-W15-S58: `test_ogx2_ac01` made deterministic, with its cause named. 20 of 20 own-process runs. | WORLD | ~26 | worker |

**Chains.** `OG-lg-1` -> `OG-rl-8`; `OG-fl-1` stands alone. **fanout:** 2 starts now, cap 8.

**Stated dependencies, not cells:**
- Z-W15-S41 is at Andrew.
- OG-v-7.
- G-E.
- R7's flag.
- Z-S43.

## ADDENDUM R3-T.14 (2.0.0_SA_COO~O, 2026-10-06 ~09:xxZ) -- round 21, the CTO's round-20 list (then PARK)

**Source.** `ledger/ROUND_ANALYSIS.round20.md` @36886eb1d9, section 4 (msg 29977). The grades read 0/0/8.

**R26:**
- Z-S57 stays open (R20's REMEDIATED rested on a README-only read).
- Z-W15-S64 (b): the raw lake prefix is the `/login` instrument.
- Z-W15-S65: `file_checksums` becomes `{}`, with a note.

Label `<round>21</round>`, ONE issuance, three LOCAL cells, no release.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-dc-2` | 1 | Z-S57: `.tools/m365-mcp-kit/` holds `README.md` only (`.mcp.json` and 3 Lokka skills removed). | LOCAL | ~21 | worker-light |
| `OG-mf-1` | 2 | Z-W15-S65: the opal-gateway row's `file_checksums` is `{}`, plus `_checksums_note`. | WORLD | ~26 | worker-light |
| `OG-o-6` | 3 | Z-W15-S64: the runbook section 5 names the raw lake prefix and the `gw_login` fields. The runbook is listed CLOUD_ONLY in LINEAGE_R18 (R16), because it does not ship to the host. | WORLD | ~22 | worker-light |

**Chains.** None. **fanout:** 3 starts, cap 8.

**After round 21: PARK.** NFRA_OPLGTW owes no engineering cell to any FWD. No round 22 is cut unless a slug, a human act
or a ruling creates one. The project waits on:
- Z-W15-S41 (Andrew);
- OG-v-7 (Andrew's tests, then Alyssa);
- G-E;
- R7's flag;
- Z-S43.

R25.3 is carried to NFRA_OPALAI.

## ADDENDUM R3-T.15 (2.0.0_SA_COO~O, 2026-10-06 ~18:4xZ) -- round 22, R28 un-park event 1 (Z-W15-S41 YES)

**Source.** Andrew-direct ~18:1xZ, "Yes go ahead", to the COO~O `/open-calls` card. Record
`org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261006_181xZ_S41_DOWNLOAD_FILTERED_GRANT_YES.md` @ca460bf9fe.
R28 (`ledger/ROUND_ANALYSIS.round21.md:32`): on a yes, one grant cell with a post-act read of a real C3 download.

Label `<round>22</round>`, ONE issuance, one WORLD cell, no release.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ga-1` | 1 | Write `download_filtered` onto the one in-force dim_asset grant (one new revision, operations only), then run one on-host dim_asset download as the real holder. | WORLD | ~28 | worker |

**Chains.** None. **fanout:** 1 start, cap 8.

**NEVER-1: does not apply.** The write set is one principal's `POLICY#` partition, a literal key list the actor controls,
and Andrew worded the exact widening. The change-management ledger is kept.

**After round 22.** FWD-4 becomes exercisable. Its acceptance stays OG-v-7 (the holder's own walk). The remaining park
conditions (OG-v-7, G-E, R7, Z-S43) stand.

## ADDENDUM R3-T.16 (2.0.0_SA_COO~O, 2026-10-06 ~20:0xZ) -- round 23, the CTO's round-22 list (R29-R31)

**Source.** `ledger/ROUND_ANALYSIS.round22.md` @a28c065593, section 4 (msg 30253). R29: a blank or null cusip never
qualifies a `dim_asset` row. R31: no grant revert in the meantime.

Label `<round>23</round>`, ONE issuance, two cells in one chain.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-q-8` | 1 | `integration.py:341` drops None and blank-after-strip from `position_cusips`, plus `tests/test_schwab_q8_blank_cusip.py` (query and download: 0 blank rows; whitespace; all-blank refused). | WORLD | ~22 | worker-light |
| `OG-rl-9` | 2 | Releases q-8 on live `2c27f3a795` under CTO + COO + CVO halves. Served output narrows: the blank-cusip key leaves both dim_asset paths. Post-release read: ga1.AC2 UNAMENDED, plus the query path and no duplicates. | WORLD | ~28 | worker |

**Chains.** `OG-q-8` -> `OG-rl-9` (the release is handed after q-8 drains). **fanout:** 1 start, cap 8.

**After round 23.** If rl-9 passes, FWD-3 returns to HELD on OG-v-7, and FWD-4's approved-information half stands for
the holder. The un-park events left are OG-v-7, G-E and R7's flag.

## ADDENDUM R3-T.17 (2.0.0_SA_COO~O, 2026-10-06 ~23:2xZ) -- round 23, one HOTFIX cell on CTO R32

**Source.** `1.0.0_SA_CTO~O` msg 30413 (R32), inside the fabric hold's carve-out (`0.0.0_AB_MSTR~Z` msgs 30408, 30411).
The gateway's `opal_data_refresh_upload` fails `portal login 403`, because it logs in at the raw API Gateway host and
the auth Lambda's origin gate refuses it. That blocks the integrate.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-rl-10` | 1 | The r24 hotfix release on live `2c27f3a795`: `opal_portal/integration.py` logs in through `PORTAL_FRONT_DOOR`, and the raw host leaves the `hosts` tuple. Nothing else ships. Post-deploy read: the installed code's own login is accepted. | WORLD | ~28 | worker |

**Chains.** `OG-rl-10` runs BEFORE the held `OG-rl-9`, which re-cuts on the new live. **fanout:** 1 start, cap 8.

## ADDENDUM R3-T.18 (2.0.0_SA_COO~O, 2026-10-07 ~03:0xZ) -- round 24, the CTO's round-23 list (R33, R35) plus OA-f-14's release

**Source.** `ledger/ROUND_ANALYSIS.round23.md` @c8a3b2911e, section 4 (msg 30512). For the release's second part:
`2.0.0_SA_COO~AI`'s release request (OA-f-14 on CLOUD @af10f7d42b) and the CTO's msg 30365 (the pre-GO host read).

Label `<round>24</round>`, ONE issuance, three cells.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-up-1` | 1 | R33: `opal_data_refresh_upload` returns right after `/trigger`; a new read-only `opal_data_refresh_status`; an idempotent re-send; the two caller texts; the 01:26Z execution read. | WORLD | ~29 | worker |
| `OG-hg-1` | 2 | R35 cell 1: the halt gate reads a worker's order from the shared root and reads the LAST status tag, with a four-case fixture. | LOCAL | ~30 | worker |
| `OG-rl-11` | 3 | The r25 release on live `7d65a28db0` under CTO + COO + CVO halves: OG-up-1, plus NFRA_OPALAI OA-f-14 (the scoped identity's consent narrows 17 -> 8 or 9). Pre-GO: the three host identity keys are read. | WORLD | ~28 | worker |

**Chains.** `OG-up-1` -> `OG-rl-11`. `OG-hg-1` stands alone. **fanout:** 2 starts, cap 8.

**No cell (form edits, the issuer's):** R35 part 2 (the deploy identity and who commits the manifest), Z-W28-S9 (a
per-run host scratch name) and Z-W28-S2 (operator-command output).

**After round 24.** The project parks again on OG-v-7, G-E and R7's flag (R28).

## ADDENDUM R3-T.19 (2.0.0_SA_COO~O, 2026-10-07 ~04:3xZ) -- round 25, the concierge's status-tool row (Andrew-direct)

**Source.** Andrew-direct 2026-10-07 ~04:1xZ, "rec approved", at the `1.0.0_SA_CTO~O` terminal. Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_041xZ_CONCIERGE_MAY_CALL_DATA_REFRESH_STATUS_TOOL_YES.md`
@4403ac63df. Routed by the CTO's msg 30555: one cell, shipped in the release AFTER r25, under three halves.

Label `<round>25</round>`, ONE issuance, two cells in one chain.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-al-2` | 1 | ONE row in `identity_tool_allowlist.txt`: the scoped concierge identity may call `opal_data_refresh_status`, unqualified, with its authorization above it; plus a four-test file. | WORLD | ~29 | worker-light |
| `OG-rl-12` | 2 | The r26 release on live r25 (`240ac2fe5a`) under CTO + COO + CVO halves. Served output widens by that one tool for that one identity. | WORLD | ~28 | worker |

**Chains.** `OG-al-2` -> `OG-rl-12`. **fanout:** 1 start, cap 8.

**Ordering against round 24.** `OG-al-2` is BUILT now and held on its worker branch. It drains to CLOUD only after r25
(`OG-rl-11`) closes, because `rl11.AC1`'s drain-back arm reads CLOUD against live.

## ADDENDUM R3-T.20 (2.0.0_SA_COO~O, 2026-10-07 ~05:2xZ) -- round 25, workstream SEND-DEDUPE-R36 (CTO R36)

**Source.** `1.0.0_SA_CTO~O` msg 30594 (R36), on the evidence in `0.0.0_AB_MSTR~Z` msg 30592: three pulls of
`model 20261005 v1.pkl` at one size, 17,919,590 bytes, with different content.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-up-2` | 1 | The re-send signature becomes (name, size, content hash) per file, the hash read from the drive item already resolved. An unreadable hash does not dedupe: the send fires. | WORLD | ~29 | worker-light |

**Chains.** `OG-al-2` (complete) -> `OG-up-2` -> `OG-rl-12`. Release r26 now carries three things: the status-tool row
for the concierge, the execution-id shape check (Z-S65) and this cell. **fanout:** 1 start, cap 8.

## ADDENDUM R3-T.21 (2.0.0_SA_COO~O, 2026-10-07 ~10:5xZ) -- round 26, the two cells of the round-24 analysis

**Source.** `ledger/ROUND_ANALYSIS.round24.md` @0e813364da (`1.0.0_SA_CTO~Z`, msg 30794), section 4. Its item 1 (r26 as
re-cut) is `OG-rl-12` amendment A3 @c38d69aa3d, already issued in round 25. Its item 4 (the re-consent read) is done:
`deliverables/2.0.0_SA_COO~O/R37_STEP1_RECONSENT_READ_20261007.md` @2e96271d1f.

Label `<round>26</round>`, ONE issuance, two build cells; the release that ships them is cut when r26 closes.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-au-2` | 1 | `rivalfunds_view`'s `day`, `route` and `fund` join the audit args allowlist and each 200 answer passes its size. Any other arg stays dropped. Row Z-S64. | WORLD | ~31 | worker-light |
| `OG-sd-1` | 2 | The status tool's `displayed_date` reads the served manifest's own date key. Row Z-W28-S13. | WORLD | ~32 | worker-light |
| `OG-rl-13` | 3 | The r27 release carrying both, with the status tool exercised once through its wrapper with a real principal. NOT cut in this issuance: it is cut when `OG-rl-12` is terminal, on the live sha r26 leaves. | WORLD | -- | worker |

**Chains.** `OG-au-2` -> `OG-rl-13`; `OG-sd-1` -> `OG-rl-13`. The two build cells write disjoint files and run at once.
**fanout:** 2 starts, cap 8.

**Ordering against round 25.** Both cells are BUILT now and HELD on their worker branches. They drain to CLOUD only after
r26 (`OG-rl-12`) closes, because the release set is every live..CLOUD gateway difference.

## ADDENDUM R3-T.22 (2.0.0_SA_COO~O, 2026-10-07 ~15:0xZ) -- round 27, the r27 release of the two round-26 cells

**Source.** `ledger/ROUND_ANALYSIS.round24.md` @0e813364da section 4, items 2 and 3 ("for the release after r26"), and
addendum R3-T.21's third row. r26 (`OG-rl-12`) is terminal: `feddb37244` live since 2026-10-07T14:03:49Z.

Label `<round>27</round>`, ONE issuance, one cell.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-rl-13` | 1 | The r27 release on live r26 (`feddb37244`) under CTO + COO + CVO halves: the rivalfunds audit args (OG-au-2) and the status tool's date key (OG-sd-1), with the status tool exercised once through its dispatch wrapper as the scoped concierge. | WORLD | ~28 | worker |

**Chains.** `OG-au-2` (complete) -> `OG-rl-13`; `OG-sd-1` (complete) -> `OG-rl-13`. **fanout:** 1 start, cap 8.

**After round 27.** The project parks again on OG-v-7, G-E and R7's flag (R28), with two items open at the issuer:
the hash read at the first real send (CTO half on r26, C1) and row Z-W28-S17's disposition.

## ADDENDUM R3-T.23 (2.0.0_SA_COO~O, 2026-10-07 ~17:5xZ) -- round 28, the deploy's install step cannot fetch

**Source.** `1.0.0_SA_CTO~Z` msg 31231, the ruling on row `NFRA_OPLGTW-Z-W28-S24` after the issuer's read
`deliverables/2.0.0_SA_COO~O/S24_BUN_INSTALL_SOURCE_READ_20261007.md` @8c05d986a1. r27 (`OG-rl-13`) is terminal:
`510c8cfed2` live since 2026-10-07T16:57:30Z.

Label `<round>28</round>`, ONE issuance, one cell.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bi-1` | 1 | `deploy-to-ec2.sh`'s dashboard install fails on a bun cache miss and never fetches: a pre-check of every lockfile entry against the cache, one guarded sequence with the install, a negative control on a copy of the cache. Row Z-W28-S24. | WORLD | ~33 | worker-light |

**Chains.** `OG-bi-1` alone. **fanout:** 1 start, cap 8.

**The hold.** No gateway deploy runs from site Z until this cell is complete and drained (CTO msgs 31228 and 31231).

## ADDENDUM R3-T.24 (2.0.0_SA_COO~O, 2026-10-07 ~18:0xZ) -- round 28 recut, the host step no longer upgrades pip

**Source.** `1.0.0_SA_CTO~Z` msg 31243, answering the issuer's msg 31240 on lines 302-303 of `deploy-to-ec2.sh` (found by
`0.0.0_AB_MSTR~Z`'s install-line census @543bee5743).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bi-2` | 2 | Delete `pip install --upgrade pip` from the deploy script's host step; the `-r requirements.txt` line stays unchanged until Andrew answers whether the gateway host is a "box". | WORLD | ~33 | worker-light |

**Chains.** `OG-bi-1` -> `OG-bi-2` (one file, one worktree, in turn). **fanout:** 1 start, cap 8.

**The hold** lifts when both cells are complete and drained. **Standing term:** until Andrew answers, a gateway release
whose diff touches `requirements.txt` goes to `1.0.0_SA_CTO~Z` before its never-widen pair.

## ADDENDUM R3-T.25 (2.0.0_SA_COO~O, 2026-10-07 ~18:3xZ) -- round 28, workstream LAKE-KEY-R43

**Source.** R43 of `ledger/ROUND_ANALYSIS.round27.md` @028a074f26 (`1.0.0_SA_CTO~Z` msg 31248), row `NFRA_OPLGTW-Z-W28-S26`.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-lk-1` | 3 | The audit lake's key builder never writes an empty time part: read the one object that has it, name the writer, fix the stamp at the writer. | WORLD | ~34 | worker-light |

**Chains.** `OG-lk-1` alone; disjoint from `OG-bi-1` -> `OG-bi-2`. **fanout:** 1 start, cap 8.

**Round 28's other two items are the issuer's own acts, not cells:** the release form's edits (R41, R42, R44; done
@532b2e1c5e) and the read of the first rivalfunds record on the audit lake (R36's acceptance).

## ADDENDUM R3-T.26 (2.0.0_SA_COO~O, 2026-10-07 ~18:5xZ) -- round 29, the pre-check's completeness and the r28 release

**Source.** `ledger/ROUND_ANALYSIS.round27.md` ADDENDUM 1 @f6fd7281cf (`1.0.0_SA_CTO~Z` msg 31259): R45, R46 and the
round-29 list. Round 28 is terminal: OG-bi-1, OG-bi-2, OG-lk-1 complete and drained @5133f144fb.

Label `<round>29</round>`, ONE issuance, two cells in one chain.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bi-3` | 1 | The bun cache pre-check tests that each entry is COMPLETE; negative control: a directory that exists and is empty. Also the read-only answer to whether a frozen install contacts the registry, if a read decides it without a fetch. R46. | WORLD | ~33 | worker-light |
| `OG-rl-14` | 2 | The r28 release on live r27 (`510c8cfed2`) under CTO + COO + CVO halves: the audit-lake key stamp (OG-lk-1), deployed by the changed script, with R45's control (0 bun cache entries touched since the deploy began). | WORLD | ~28 | worker |

**Chains.** `OG-bi-3` -> `OG-rl-14`. **fanout:** 1 start, cap 8.

**The round's other item is the issuer's own read, not a cell:** the first rivalfunds record on the audit lake
(R36's acceptance). `OG-rl-14`'s post-deploy read takes it again.

## ADDENDUM R3-T.27 (2.0.0_SA_COO~O, 2026-10-07 ~20:3xZ) -- round 29, workstream GUARD-RIG-S27

**Source.** Row `NFRA_OPLGTW-Z-W28-S27`, filed by `OG-rl-14`'s Phase A: `tests/test_deploy_base_guard.py` reads 6 passed on
live and 3 passed, 3 failed on the r28 release tree, because its rig's dashboard stub carries no lockfile and the
pre-check stops the script.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bi-4` | 3 | The base-guard test rig carries a lockfile and a stub cache of complete entries; two tests added, one a negative control (a cache miss stops the script before the upload). | WORLD | ~33 | worker-light |

**Chains.** `OG-bi-4` -> `OG-rl-14` (the release commit is re-cut to carry it). **fanout:** 1 start, cap 8.

## ADDENDUM R3-T.28 (2.0.0_SA_COO~O, 2026-10-07 ~22:5xZ) -- round 30, the deploy drains before it restarts

**Source.** `1.0.0_SA_CTO~Z` msg 31444 (the round-29 analysis by message, on `3.0.0_SA_CVO~Z` slug msg 31443), remedy 1 of
row `NFRA_OPLGTW-Z-S67`. Round 29 is terminal: r28 `aa75078e1b` live since 2026-10-07T21:49:10Z.

Label `<round>30</round>`, ONE issuance, one cell.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-dr-1` | 1 | The deploy stops the service gracefully and waits for requests in flight before it restarts; the revocation of row Z-S67 is reproduced offline as the negative control. No token rule changes. | WORLD | ~35 | worker |

**Chains.** `OG-dr-1` alone; the release that ships it is cut after it drains. **fanout:** 1 start, cap 8.

**Not cut:** a grace window for the previous token generation (research at `4.0.0_SA_CRO~Z`, then the CTO's ruling).
**Standing:** the release form's 12-hour bar before the 07:00 America/New_York send, until the drain is shown.

## ADDENDUM R3-T.29 (2.0.0_SA_COO~O, 2026-10-08) -- round 31, the mail route by sender DOMAIN (PRD v1.9)

**Source.** PRD v1.9 @b736f07a28, the C7 addendum (v1.8 @29b7392bc9, refused at L4-R and cured by v1.9; `1.0.0_SA_CTO~Z` msgs 31849,
31850, 31875); ratified-text half signed as a file by `3.0.0_SA_CVO~Z` @d77caa1548 (relay msg 31894), on CTO ruling msg 31856. The request is the laptop's, cross-fabric (CLAUDE.md rule 32).
Round 30's one order, `OG-dr-1`, is built and not drained on the CTO's ruling msg 31464.

Label `<round>31</round>`, ONE issuance, one build cell; the release that ships it is cut when the cell drains.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-md-1` | 1 | `mail_route.py` admits a message by its sender's own DOMAIN from a configured table (whole, case-insensitive), and the listing takes exactly one of `sender` or `sender_domain`, the domain judged in the gateway on each row. The domain file ships EMPTY. | WORLD | ~36 | worker |
| `OG-rl-15` | 2 | The r29 release carrying it, under CTO + COO + CVO halves that name the domain table's entries. NOT cut in this issuance. | WORLD | -- | worker |

**Chains.** `OG-md-1` -> `OG-rl-15`. **fanout:** 1 start, cap 8.

## ADDENDUM R3-T.30 (2.0.0_SA_COO~O, 2026-10-08 ~21:5xZ) -- round 32, the round-31 analysis list with section 4a (PRD v2.0)

**Source.** `ledger/ROUND_ANALYSIS.round31.md` section 4 @e43ee663be and section 4a @8ca3947b86 (`1.0.0_SA_CTO~O` msgs
31971, 32018); PRD v2.0 ADMITTED, both L4-R halves signed (ratified-text `3.0.0_SA_CVO~Z` @5924aaedbe, brief
`4.0.0_SA_CRO~Z` @d91440b591). Andrew-direct ~21:2xZ "asap" on the 13 months and the Tax SMA master (@6233bae5de).
Round 31 is terminal: OG-md-1 drained @a2c6b9cc65; OG-dr-1 closed undrained (R51).

Label `<round>32</round>`, ONE issuance, eight cells in six chains.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-sf-1` | 1 | `opal_asker_query` into `SAFE_TOOLS`; the census of every `@mcp.tool` in tools.py against the three sets; the test through `_run` (R54). | WORLD | ~37 | worker-light |
| `OG-rf-1` | 2 | Refresh rotation and code redemption answer once their transaction is sent; a deadline before the send answers 503 with nothing consumed (R50, PRD v2.0 item 6). | WORLD | ~38 | worker |
| `OG-en-1` | 3 | One `-Mode enumerate` run for 08403355 beside 08335338 over the same window, from a box-side temp copy only; outside both pull windows. | WORLD | ~39 | worker |
| `OG-tm-1` | 7 | On g5-1's "same shape": the puller, schedule (30+ minutes apart), box grant, silver conversion and the gateway reader roles carry 08403355; one QA day lands, converts and qualifies. Phase A plan + never-widen ask, Phase B after CTO+COO halves. | WORLD | ~39 | worker |
| `OG-sc-1` | 4 | The exact column lists of `fact_acc`, `fact_uln`, `fact_ult`, `fact_rld`, `fact_rly`, `fact_rty`, `fact_trn`, both masters, newest partition, from the parquet footer only (no statistics). | SERVED | ~40 | worker-light |
| `OG-cc-1` | 5 (+4's marker clause) | The 13-month closure census per master with the gateway's own record-level qualification; oldest/newest qualified record. | SERVED | ~41 | worker |
| `OG-bf-1` | 8b | The producer's completion-record backfill over the census's missing dates (OG-c-2's replay path), the 49F accelerator's effect planned per branch. Phase A plan + never-widen ask, Phase B after CTO+COO halves. | WORLD | ~41 | worker |
| `OG-cm-1` | 8a | The gateway's `calendar_months` (1-13) grant window, exactly one of days/months, month-end clamped; caps unchanged; the contract file and its deploy copy. | WORLD | ~42 | worker |
| `OG-rl-15` | 6 | The r29 release (R55): OG-md-1, OG-sf-1, OG-rf-1, and (proposed to the CTO) OG-cm-1 with the 13-month grants for Andrew's and Alyssa's principals and tm-1's contract hookup. NOT cut in this issuance: after its build cells drain, and after the `opal-gateway-bbg` move and Andrew's sign-in. | WORLD | -- | worker |

**Chains.** `OG-en-1` -> `OG-tm-1` (slot ~39); `OG-cc-1` -> `OG-bf-1` (slot ~41); `OG-sf-1`, `OG-rf-1`, `OG-cm-1` ->
`OG-rl-15`; `OG-sc-1` alone (feeds round 33). **fanout:** 6 of 6 chains, cap 8.

**Issuer rulings inside the decomposition.**
- Item 8 splits into 8a (`OG-cm-1`, the grant mode the 13-month reach needs; the gateway has no per-grant window today)
  and 8b (`OG-bf-1`, the records).
- Item 4's marker clause is read by `OG-cc-1` with item 5's instrument, never measured twice.
- `OG-cm-1` owns `org/standards/NFRA_OPLGTW_CONTRACT.json` this round; `OG-tm-1`'s contract lines are a merge hookup.
- PRD v2.0 item 5(b) "placed with an AE lane": placed in the issuer's L7 slot ~39 under CTO+COO halves, the puller's
  owner `0.6.2_AE_PartnerETL` named in the ask.
- `OG-en-1`'s spawn waits for 23:05Z 2026-10-08 (the box-wide SDD session lock and the 22:15Z pull's deadline).
- **OG-rl-15's scope, RULED** (`1.0.0_SA_CTO~O` msg 32087, 2026-10-08 ~22:4xZ, on the issuer's ask 32086): r29 carries
  OG-md-1, OG-sf-1, OG-rf-1 AND OG-cm-1, plus the 13-month grant write for Andrew's and Alyssa's principals. Conditions:
  OG-cm-1 drains before the r29 cut; the grant write is a never-widen act whose blast radius is the reach field of exactly
  those two principals' grants, set to 13 calendar months, no other field or principal, rollback = the prior reach per
  key, CTO+COO halves before it; until OG-bf-1 lands a date without a qualified record answers unavailable; R55's other
  terms stand (the 12-hour window before the 07:00 ET send).
- **OG-rl-15 CUT as workstream RELEASE-R29** (2026-10-09 ~01:2xZ, slot ~43, worker; the round-32 issuance at HEAD admits a second order only under its own workstream, gate (x)) after its four build cells drained, on `1.0.0_SA_CTO~O` msg
  32184 (R55's sign-in precondition MET, Andrew ~00:4xZ @6938d82aad). Phase A by the worker; Phase B's deploy by
  `0.7.0_AE_CloudOps~Z` (msg 32057) under an apply order cut after the CTO + COO + CVO halves; Phase C (post-deploy
  read, the 13-month grant write, drain-back) by the worker. Deploy window 11:00Z-23:00Z (R55/R49).
- **OG-bf-1 A1** (@8f0b2e4660): Phase B signed for 08242234 only (W); Phase C builds the CTO-ruled Y leg (the 49F
  dispatcher skips a non-T-1 record); Phase D writes 08335338 after Y. **OG-tm-1 A1/A2** (@f49624438b, @3998bbe5a7):
  slm-only difference proceeds (CTO 32147); the data/assets/scripts/silver mirror (row S4) before Leg C; both halves
  signed (COO @3998bbe5a7, CTO @4149c01c23).
- **OG-ap-1 CUT as workstream APPLY-TM1** (2026-10-09 ~01:4xZ, issued to `0.7.0_AE_CloudOps~Z`): OG-tm-1's Phase B legs
  C, B, A and the gateway roles, by `-target` only, under the signed pair (COO @3998bbe5a7, CTO @4149c01c23), after row
  S4's mirror drained @b831326e39. The QA pull stays with worker ~39.
- **OG-ap-2 CUT as workstream APPLY-Y** (2026-10-09 ~02:0xZ, issued to `0.7.0_AE_CloudOps~Z`): OG-bf-1's leg Y, the 49F
  dispatcher date gate, under the signed pair (COO @9e406fcb00, CTO @094786bd2a); source-map entry first, code-only
  plan, Arm 1 on demand, Arm 2 organic.
- **OG-tg-1 CUT as workstream GATE-R30** (2026-10-09 ~04:0xZ, slot ~44): sender identity (UPN, tenant) on Teams reads for
  every caller; the Opal-users-only gate on the Bloomberg concierge's Teams reads and sends; the concierge unscoped (seed
  + two overlay rows removed) -- Andrew ~03:2xZ/~03:3xZ, PRD v2.3 item 4; held out of r29 (A6), ships in r30.

## ADDENDUM R3-T.31 (2.0.0_SA_COO~O, 2026-10-09 ~04:4xZ) -- round 33, workstream ENTITLE-R33 (ahead of the analysis)

**Source.** `1.0.0_SA_CTO~O` ruling msg 32383: a profile confines only the data-grant tool family; "unprofiled = full"
refused; Andrew gets a v2.2-width profile with 13 months, and the Bloomberg concierge mirrors it in r30. "Cut it as a
round-33 cell with tests."

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pf-1` | -- | `decide()` confines a profiled principal only on the five schwab_* tools and the Black Diamond data tools; unprofiled still denied data; Alyssa's data reach unchanged. | WORLD | ~45 | worker |

**fanout:** 1 start, cap 8. r30 carries OG-pf-1 and OG-tg-1 plus the two grant writes (Andrew's profile; the mirror).
- **OG-da-1 CUT as workstream DATA-REFRESH-ADMIT** (2026-10-09 ~05:3xZ, issued to `0.7.0_AE_CloudOps~Z`, CTO~Z ruling
  32354): the data_refresh admission fails closed (Dev or Opal-internal; empty/null and no-authorizer refused). Measured at
  the cut: the live function already differs from HEAD; Phase A names that drift before any deploy.

## ADDENDUM R3-T.32 (2.0.0_SA_COO~O, 2026-10-09 ~07:4xZ) -- round 33, workstream TAXSMA-HISTORY (ahead of the analysis)

**Source.** Andrew-direct 2026-10-09 ~06:3xZ at the 2.0.0_SA_COO~O terminal (record
`org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261009_063xZ_08403355_BACKFILL_SAME_SHAPE.md` @98c4e6a47f):
a FULL history backfill for 08403355 through bronze, silver and the completion record, the same path as 08242234 /
08335338. Serves FWD-13. The schedule half is OG-tm-1 (applied by OG-ap-1).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bh-1` | -- | Phase A: census of the source's earliest served date (enumerate only) + the never-widen ask; Phase B after both halves: the backfill over the same path, every served date QUALIFIED or named unavailable. | WORLD | ~46 | worker |

**fanout:** 1 start, cap 8. The 49F-accelerator question for 08403355 stays with Andrew; not in this cell.

## ADDENDUM R3-T.33 (2.0.0_SA_COO~O, 2026-10-09 ~08:0xZ) -- round 32, workstream APPLY-R29

**Source.** OG-rl-15 Phase B: the three never-widen halves on the r29 ANNOUNCE @368e48e533 are at HEAD (CTO~O @d3f04813df,
COO~O @40b39ad88d, CVO~Z @c348b51df9). Site Z's applier deploys (msg 32057).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-3` | 6 | Create gateway/mail/commassist-bearer; apply the one policy line (98501422dc) under its own ledger; deploy r29 91811b648a under ledger nfra-oplgtw-gateway-release-r29 per ANNOUNCE Half 2. | WORLD | ~AE | worker |

**fanout:** 1 start, cap 8. OG-rl-15 Phase C (served read + Alyssa's 13-month grant) follows the applier's report.

## ADDENDUM R3-T.34 (2.0.0_SA_COO~O, 2026-10-09 ~10:2xZ) -- round 33, workstream ADVI-E2

**Source.** `1.0.0_SA_CTO~Z` ruling msg 32663: NFRA_OPLGTW TAKES dell2 ADVI_BILLING packet E2 (copy_site_file_to_s3,
@9828e7761f), released after r29 and NFRA_MCPINDEX MX-r-9 under its own never-widen pair.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ab-1` | -- | Cherry-pick E2's registration code (e8290dd5fe, code paths only); build the required carry (destructive_ops + data_entitlement entries, the deploy printf env line from address()); tests. No release. | WORLD | ~47 | worker |

**fanout:** 1 start, cap 8. The E2 release cell is cut after MX-r-9 lands.

## ADDENDUM R3-T.35 (2.0.0_SA_COO~O, 2026-10-09 ~11:3xZ) -- round 33, workstream TRNSPT-ALLOWLIST

**Source.** `1.0.0_SA_CTO~Z` ruling @261e2c42a0 (msg 32708): the 4 NFRA_TRNSPT meetings onto the gateway's
TRANSCRIPT_MEETING_ALLOWLIST, read from dell2's meeting_allowlist.json, an env-only release under its own three halves.
Host queue (msg 32713, one release in flight at a time): r29 -> MP-x-4 -> OG-tl-1 -> MX-r-9 -> E2 -> metadata route.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-tl-1` | -- | Phase A: release candidate on the live ref, deploy-to-ec2.sh reads the 4 ids from the json; the never-widen ask naming them. Phase C: the served read after the applier's deploy. | WORLD | ~48 | worker |

**fanout:** 1 start, cap 8.

## ADDENDUM R3-T.36 (2.0.0_SA_COO~O, 2026-10-09 ~13:0xZ) -- round 33, workstream APPLY-TL1

**Source.** OG-tl-1's three halves at HEAD (CTO~Z @033a840b3b, COO~O @167b7b8f1a, CVO~Z @b73aa5a7d9). Applied by
`0.7.0_AE_CloudOps~Z` after MP-x-4 in the host queue.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-4` | -- | Re-cut the allowlist hunk on the live ref, deploy under its ledger, read back env keys and value hashes. | WORLD | ~AE | worker |

**fanout:** 1 start (staged until MP-x-4's ledger closes), cap 8.

## ADDENDUM R3-T.37 (2.0.0_SA_COO~O, 2026-10-09 ~13:2xZ) -- round 33, workstream ADVI-E2-PPTX

**Source.** `1.0.0_SA_CTO~Z` ruling @4e2f00c9fa (msg 32768): generalise copy_site_file_to_s3 for dell2 FWD-6 (.pptx ->
market_update), built on OG-ab-1, released WITH E2 under one pair naming both admitted pairs.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ab-2` | -- | Two admitted (extension, destination) pairs in one table, roots from address(); the deploy env line; the grant if needed (unapplied); tests. No release. | WORLD | ~49 | worker |

**fanout:** 1 start, cap 8.

## ADDENDUM R3-T.38 (2.0.0_SA_COO~O, 2026-10-09 ~15:4xZ) -- round 33, workstream RPS-PIN

**Source.** Both OG-bh-1 halves' AMENDMENT 1 (CTO @f77e32d7c3, COO @eea4aebe10), row Z-W46-S3: six 08403355 dates carry
28 RPS section-1 columns the converter's pin does not know; they are held, and a pin-extension cell re-runs them.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pn-1` | -- | Measure the 28 columns, extend the pin explicitly (guard not loosened), tests, the never-widen ask; then (by continuation) the applier's deploy and the re-run of only the held dates. | WORLD | ~50 | worker |

**fanout:** 1 start, cap 8.

## ADDENDUM R3-T.39 (2.0.0_SA_COO~O, 2026-10-09 ~17:0xZ) -- round 33, workstream E2-RELEASE

**Source.** CTO~Z msg 32663 (TAKE E2) and @14cbf27dec (the .xlsx pair releases ALONE). Host free after MP-x-4
(16:27Z); MX-r-9 next, then this release.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-rl-16` | -- | Phase A: release on the live ref carrying E2's .xlsx pair only (not OG-ab-2's .pptx), the ANNOUNCE for three halves. Phase C: the served read after the applier deploys. | WORLD | ~51 | worker |

**fanout:** 1 start, cap 8. The applier's order is cut after the halves and MX-r-9's ledger close.

## ADDENDUM R3-T.40 (2.0.0_SA_COO~O, 2026-10-09 ~19:4xZ) -- round 33, workstream APPLY-PN1

**Source.** OG-pn-1's pair (COO @d41a3068cd, CTO @d66a0fb956; C1 met @b3e481b261). Applied by `0.7.0_AE_CloudOps~Z`.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-5` | -- | Deploy the converter's D-tag routing (one Lambda, Terraform), then re-run ONLY the six held 08403355 dates; all 758 qualify. | WORLD | ~AE | worker |

**fanout:** 1 start, cap 8.

## ADDENDUM R3-T.41 (2.0.0_SA_COO~O, 2026-10-10 ~23:4xZ) -- round 33, workstream APPLY-E2

**Source.** OG-rl-16's three halves (CTO @5e258448d2, COO @153e507b79, CVO @9b6003cd3b), cut at MP-r-2's close (COO~MP msg
33064; live ref 2a5966dfbd). Applied by `0.7.0_AE_CloudOps~Z`. B1 (re-cut + plan read) now; B2 (policy, then deploy) on the
issuer's GO after the three halves re-pin at the re-cut sha (CTO C1).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-6` | -- | Re-cut E2's three commits on 2a5966dfbd and prove the patch-ids equal; then the one PutObject policy and the gateway deploy under their own ledgers. | WORLD | ~AE | worker |

**fanout:** 1 start, cap 8.

## ADDENDUM R3-T.42 (2.0.0_SA_COO~O, 2026-10-11 ~15:3xZ) -- round 34, ONE issuance

**Source.** `1.0.0_SA_CTO~Z`'s round-33 analysis `ledger/ROUND_ANALYSIS.round33.md` @2672b8d28a section 3: round-32's
E1-E5 plus E6-E8. Also the gateway queue's CT-i-11 release, which the laptop CTO consented to under XB-b98e @de13ed0e00,
with Addendum 1 @4f285abe22.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-db-1` | E6 | Drain OG-tl-1's allowlist deploy hunk back onto trunk's deploy-to-ec2.sh (row Z-S85). FIRST. | WORLD | ~54 | worker-light |
| `OG-br-1` | E4 | Batch repair: runbook 7.2 to the live ref (Z-S88); manifest checksums from the served release (Z-S84); the dispatcher _build_note (S70); the SI2 puller's lock release and range print (W39-S1/S2); the failing-test baseline read (W45-S4, W47-S2). | WORLD | ~54 | worker-light |
| `OG-mu-1` | E1 | The .pptx market_update writer: intake's content-addressed key (W49-S3) and one builder-fed PutObject grant (W49-S4). Phase A plus the ask. | WORLD | ~55 | worker |
| `OG-gw-1` | E2 | Rebuild mcportal-grant-writer from the live release (W42-S1, the opal-gateway half of W39-S5). Phase A: build, targeted plan, ask. | WORLD | ~56 | worker |
| `OG-wr-1` | E5 | Prime the 13-month window once per master; measure the warm read on the served gateway (W43-S7, ruling (d)). | WORLD | ~56 | worker |
| `OG-dq-1` | E7 | READ ONLY: name the actor that drained opal-assets-silver-dlq, and read its current messages (Z-S77). | SERVED | ~57 | worker |
| `OG-bd-1` | E8 | Census the callers of blackdiamond_list_fees; deny it to unprofiled principals only if the census is clean (W45-S2, ruling @135719d313). | WORLD | ~57 | worker |
| `OG-ap-7` | queue | APPLY: NFRA_CTLPLN CT-i-11's /hx/teams/* routes, re-cut on live c3af8687e4. B1 re-cut and ask; B2 deploy on GO. | WORLD | ~AE | applier |

**E3 is not cut.** Its restart-free route to the lost answer (W35-S1) is OG-rf-1's R50 send-gate (@41b0c7903b): the
token grants answer once their consuming transaction is sent. It has been live since r29 and is in c3af8687e4
(`_within_send_budget` x3). The issuer's citing row disarms W35-S1.

**Chains: 7 independent cells plus 1 applier.** Slots queue by write set and kind: ~54 runs db-1 then br-1, ~56 runs
gw-1 then wr-1, ~57 runs dq-1 then bd-1.
**fanout:** 4 of 7 chains, cap 8. Reason: Andrew-direct 2026-10-10 slower pacing for the usage limit (relay msg 33086).

## ADDENDUM R3-T.43 (2.0.0_SA_COO~O, 2026-10-11 ~19:1xZ) -- round 34, workstream APPLY-R34

**Source.** Round 34's signed Phase A cells: OG-mu-1 (COO @34bf3d67a4, CTO @e0ca80f880) and OG-gw-1 (COO @88926383b1, CTO
@bef54b9b62). Applied by `0.7.0_AE_CloudOps~Z`, after OG-ap-7's ledger, one act at a time.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-8` | E1 apply | The market_update PutObject grant: -target, -var from address(), plan 1/0/0 then 0/0/0 at rc=0, live read-back. | WORLD | ~AE | applier |
| `OG-ap-9` | E2 apply | Rebuild mcportal-grant-writer from live c3af8687e4: -target, -var, plan 0/1/0 then 0/0/0 at rc=0; session-free read-back (CodeSha256 plus the deployed parse_scope taking 13 months, with the prior package refusing it). | WORLD | ~AE | applier |

**fanout:** 1 of 1 chains (ap-8 then ap-9 on one applier), cap 8.

## ADDENDUM R3-T.44 (2.0.0_SA_COO~O, 2026-10-11 ~23:2xZ) -- round 35, ONE issuance

**Source.** `1.0.0_SA_CTO~Z`'s round-34 analysis `ledger/ROUND_ANALYSIS.round34.md` @026a983b34 section 3. E4 (the OG-bd-1
re-cut) is NOT cut: it is conditional on Andrew's admission answer (row Z-W57-S2, ARMED, held on him) and will issue as its
own workstream when the answer lands.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-fd-1` | E1 | Each silver sweep drains only its own family's DLQ messages; others are returned (visibility 0); unattributed messages are never deleted (Z-S91). Phase A: source, tests, ask. | LOCAL | ~58 | worker |
| `OG-ap-10` | E2 | APPLY: the .pptx -> market_update gateway release (OG-ab-2 + OG-mu-1 hunks) re-cut on live 28ba9532b6, stating the key form (Z-W55-S2). B1 re-cut and ask; B2 deploy on GO. | WORLD | ~AE | applier |
| `OG-tb-1` | E3 | READ: who reads gateway/teams/bearer (90-day CloudTrail, positively controlled), the group's grant statement, then the narrowing ask (Z-S92). | SERVED | ~59 | worker |

**fanout:** 2 of 3 chains plus 1 applier, cap 8. Reason: Andrew-direct 2026-10-10 pacing.

## ADDENDUM R3-T.45 (2.0.0_SA_COO~O, 2026-10-12 ~00:5xZ) -- round 35, workstream APPLY-R35

**Source.** OG-fd-1's pair (COO @824ec17c4d, CTO @aafc1640e8): schwab ONLY today. etf, blackdiamond, orion and eclipse each
wait for their own pair naming their drift's owner.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-11` | E1 apply (schwab) | Read the live record shape first; deploy the per-family drain to opal-assets-silver-schwab by Terraform (pin moved); grade it on the scheduled 12:15Z sweep with two planted synthetic records. The ledger states the partial roll-out. | WORLD | ~AE | applier |

**fanout:** 1 of 1, cap 8.

## ADDENDUM R3-T.46 (2.0.0_SA_COO~O, 2026-10-12 ~13:1xZ) -- round 35, workstream APPLY-R35-G

**Source.** Row Z-S97: OG-ap-11 AC2 FAILED on the real 12:15Z sweep, because the schwab role lacks
`sqs:ChangeMessageVisibility` on the DLQ. Pair: COO @031aec9026, CTO @2a3205e69d.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-12` | Z-S97 fix | Add `sqs:ChangeMessageVisibility` to `opal-assets-silver-dlq-access` (1 queue, 7 roles), with simulate DENY before and ALLOW after. The schwab converter runs the OG-ap-11 build. Grade on the next scheduled 12:15Z sweep, with the same two synthetics. | WORLD | ~AE | applier |

**fanout:** 1 of 1, cap 8.

## ADDENDUM R3-T.47 (2.0.0_SA_COO~O, 2026-10-12 ~13:3xZ) -- round 35, workstream APPLY-R35-T

**Source.** OG-tb-1's pair (COO @f9cb4c5dca, CTO @fa2892a777). The hold was lifted by `1.0.0_SA_CTO~Z` msg 33492: the
laptop CTO ruled sitez-ffaf YES (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_CLUSTER_TICK1_RULINGS_20261012.md`
section A row 1).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-13` | E3 apply | Re-class `gateway/teams/bearer` to OTHER at the census source, regenerate the census, then targeted apply of `aws_iam_policy.dell_agent_platform_secrets` (31 -> 30 ARNs). Read back by simulate: bearer implicitDeny, a kept ARN allowed. | WORLD | ~AE | applier |

**fanout:** 1 of 1, cap 8.

## ADDENDUM R3-T.48 (2.0.0_SA_COO~O, 2026-10-13 ~15:2xZ) -- round 36, ONE issuance

**Source.** `1.0.0_SA_CTO~Z`'s round-35 analysis `ledger/ROUND_ANALYSIS.round35.md` @682d1ced78, section 3 (E1-E4). Every
WORLD cell's release or deploy is a later apply order under its own never-widen pair; these cells build and ask.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bd-2` | E1 | `decide()` denies `blackdiamond_list_fees` to unprofiled principals, with master_admin admitted by tier and no profile written. The unlinked caller fc9aed2e22 stays denied. Tests, plus the release ask. | WORLD | ~60 | worker |
| `OG-fd-2` | E2 | `run_sweep` persists its drain dict into backfill-status (Z-S100), plus a per-family package-drift census with each drift's owner and the per-family release ask (Z-S91). | WORLD | ~61 | worker |
| `OG-rd-1` | E3 | READ the cause of every 502 on `/hx/teams/channels/.../messages` (Z-S95), with a positive control. No fix. | SERVED | ~62 | worker-light |
| `OG-sh-1` | E4 | The gateway `list_shared_folder(url)` tool (Graph `/shares/u!<b64>/driveItem/children`, READ, classified), plus the one 2026-09-29 request-log read for the 06-01 meeting (dell2-54ae point 3), plus the release ask. | WORLD | ~63 | worker |

**Chains.** bd-2 and sh-1 write the same files (`data_entitlement.py`, `server.py`, the two suites), so they are ONE
queue: sh-1 is spawned from HEAD after bd-2 drains. fd-2 and rd-1 are independent.

**fanout:** 3 of 3 chains now (bd-2 then sh-1; fd-2; rd-1), cap 8.

## ADDENDUM R3-T.49 (2.0.0_SA_COO~O, 2026-10-13 ~21:0xZ) -- round 37, ONE issuance

**Source.** `1.0.0_SA_CTO~Z`'s round-36 analysis `ledger/ROUND_ANALYSIS.round36.md` @713305ee56, section 3 (R1-R5); ruling
`ledger/CTO_RULING_R37_ONE_RELEASE_PF1_TG1_BD2_SH1_20261013.md` @8f236865cc (row Z-S101); PRD v2.8 @ecdab3c7d0 (FWD-20; FWD-21 V1 admits by identity, CTO msg 33764; v2.8 adds the research-only arm and the identity-store census, msg 33775),
ADMITTED before this issuance (LIMB 6). Cut-template rules carried from round 36: a build cell whose release is deferred
names the release order it rides; an APPLY order's preflight runs comp-iam on every API call the new code makes.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-14` | R1 | APPLY: the r30 gateway release (OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1), re-cut on the live ref after NFRA_MCPORTAL MP-z-5's ledger closes; only the six cell commits' hunks; served read of each cell. | WORLD | ~AE | worker |
| `OG-ap-15` | R2 | APPLY: the per-family DLQ drain releases (OG-fd-1 + OG-fd-2) for schwab, etf, orion, eclipse, blackdiamond; built off trunk, each family signed alone (schwab's drain-ahead-of-lanes disclosed, blackdiamond's held modules named), graded on its next scheduled sweep. | WORLD | ~AE | worker |
| `OG-cd-1` | R3 | `app/family_depth.py` `read()`: per-family schedule (live EventBridge), last sweep and depth (backfill-status + earliest silver partition), every value claimed; read-only; its read-grant file and ask. Rides release `OG-ap-16` (cut after OG-ap-14's ledger closes). | WORLD | ~65 | worker |
| `OG-hv-1` | R4 | Gateway `harvest_list` / `harvest_read` (READ, SAFE): Opal principals on the 24 prefixes of list v4 @7e0da2dfee, non-Opal and off-list refused before any S3 call; the asset-manager principal census; the ask. Rides `OG-hv-2`. | WORLD | ~64 | worker |
| `OG-hv-2` | R4 | APPLY: one builder-named read policy on the 24 harvest prefixes, then OG-hv-1's gateway release on the live ref, then the served read; the real asset manager's call is owed (judgment, CVO). | WORLD | ~AE | worker |
| `OG-gd-1` | R5 | READ: each FWD-1..8 PROOF split into arms; every instrument-runnable arm run against live state with its claim; the rest recorded as owed acts; no grade word (the CTO grades at the round-37 analysis). | SERVED | ~66 | worker |

**Chains (edges are data or queue dependencies).**
- Gateway queue, one release at a time: MP-z-5 (NFRA_MCPORTAL) -> `OG-ap-14` -> `OG-hv-2` -> `OG-ap-16` (next round).
  NFRA_MCPINDEX MX-r-11 and MCPORTAL MP-n-4 interleave by their issuers' asks.
- `OG-hv-1` -> `OG-hv-2` (hv-2 releases hv-1's code).
- `OG-ap-14` and `OG-ap-15` share the applier `0.7.0_AE_CloudOps~Z`, as ONE queue: ap-15 Phase A runs first, while
  ap-14 waits on MP-z-5.
- `OG-cd-1` and `OG-gd-1` are independent.

**fanout:** 4 of 4 chains (applier ~Z: ap-15 / ap-14 / hv-2; hv-1; cd-1; gd-1), cap 8.

**R3-T.49 A1 (2.0.0_SA_COO~O, 2026-10-14 ~00:5xZ) -- one cell added mid-round, on 1.0.0_SA_CTO~Z's ruling msg 33850.**
The positive arm on r30 needs the grant writes that R3-T.31 kept separate ("r30 carries OG-pf-1 and OG-tg-1 plus the two
grant writes (Andrew's profile; the mirror)"). The issuer adds the one cell inside its own decomposition.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-mg-1` | R1+ (CTO msg 33850) | APPLY: Andrew's v2.2-width restricted profile with 13 months (ruling 32383), and the Bloomberg principal as its exact mirror (PRD v2.3 item 1), through the one writer (`ops/schwab_entitlement_admin.py` under `opal-gateway-access-admin`); Phase B after OG-ap-14's ledger closes; AC3 (judgment) is the BG seat's re-exercise of the 8 tools. | WORLD | ~AE | worker |

**Chain:** `OG-ap-14` -> `OG-mg-1` Phase B (Phase A, read only, may run now). Applier queue for `0.7.0_AE_CloudOps~Z`:
OG-ap-15 graded on the sweeps; OG-ap-14 B1 now; OG-mg-1 Phase A now; then OG-ap-14 B2 at 11:00Z+; OG-mg-1 B; OG-hv-2.

**R3-T.49 A2 (2.0.0_SA_COO~O, 2026-10-14 ~02:5xZ) -- one cell, on 1.0.0_SA_CTO~Z's ruling msg 33941 (route (a)).** The
COO refused OG-mg-1's halves because profiling Andrew would end his master_admin tier admission to
`blackdiamond_list_fees` (r30's `decide()` admits by tier only on the no-profile branch).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-bd-3` | R1+ (CTO msg 33941) | `decide()` admits a `TIER_ADMITTED_TOOLS` member for master_admin on the profiled branch too (any profile state); `tool_denial`/`visible_tools` read the tier for restricted callers; 3 offline tests; OG-bd-2's tests unchanged. Its release is a gateway apply order cut when it drains. | WORLD | ~67 | worker-light |

**Chain:** OG-bd-3 -> its release (after OG-ap-14's ledger) -> OG-mg-1 Phase B (halves re-signed on that base).

**R3-T.49 A3 (2.0.0_SA_COO~O, 2026-10-14 ~03:2xZ) -- OG-bd-3's release (CTO ruling msg 33941: r30, then this, then OG-mg-1 B).**

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-17` | R1+ | APPLY: OG-bd-3 (`fffac3b499` + `486b643b97`) on the live ref after OG-ap-14's ledger closes; the served read checks the four tier arms. | WORLD | ~AE | worker |

**Gateway queue now:** (MX-r-12 if closed by 10:00Z) -> OG-ap-14 (r30) -> OG-ap-17 (bd-3) -> OG-hv-2 -> OG-ap-16 (cd-1, next round) -> the C-PERSON reader's release.

**R3-T.49 A4 (2.0.0_SA_COO~O, 2026-10-14 ~12:1xZ) -- Andrew-direct "accelerate this use case".** Queue is now OG-hv-2 -> OG-ap-17 -> MX-r-13
(OG-ap-17 re-cuts on hv-2's live release). R3-T.50 below then places OG-ap-18 between OG-hv-2 and OG-ap-17.

## ADDENDUM R3-T.50 (2.0.0_SA_COO~O, 2026-10-14 ~13:2xZ) -- round 37, workstream G1-TYPED (FWD-22, PRD v3.0 @7878037d98)

**Source.** `1.0.0_SA_CTO~Z` msg 34077: Andrew-direct ~12:4xZ, the gateway is live with the census tables by Friday 2026-10-16,
harvest first ("I would prioritize that as number one"). The G1 enrichment list is PRD v3.0's addendum; the contracts are
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md` @0d7c29b3c5 section 3 (the tool
registry). **THE CUT IS HELD until `prd-signoff.py status NFRA_OPLGTW` reads ADMITTED** (both halves are STALE at v3.0; owed by
`3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~Z`, both asked). Only the plan is written here.

**Seam.** All ten tools admit through `harvest_read.admit()` and write its audit row; each answers with `as_of`,
`source_keys[]`, a denominator and `absent_reason`, projected to 50 KB. `harvest_describe_dataset` is NOT built (the catalog
serves it); `publication-links/v1/` and `publications/v1/` are not tool targets. Hookups (the `tools.py` registrations and
the `data_entitlement.py` family rows for the new names) belong to no cell: the issuer adds them at the merge, in one commit.

| cell | what | writes (new files only) | risk | slot | class |
|---|---|---|---|---|---|
| `OG-gt-0` | the typed-tool base: the envelope (`as_of`, `source_keys`, denominator, `absent_reason`), the 50 KB projection, the newest-part read over `harvest_read`'s capped client, one admit-and-audit wrapper; offline tests with a fake client | `app/harvest_typed.py`, `tests/test_og_gt0.py` | WORLD | ~71 | worker |
| `OG-gt-1` | `harvest_resolve_security`, `harvest_security_coverage` (crosswalk/universe/identity; one ListObjectsV2 per keyed prefix) | `app/harvest_identity.py`, `tests/test_og_gt1.py` | WORLD | ~72 | worker |
| `OG-gt-2` | `harvest_get_chatter`, `harvest_search_articles`, `harvest_get_article` (gold chatter and mentions joined to publisher silver) | `app/harvest_press.py`, `tests/test_og_gt2.py` | WORLD | ~73 | worker |
| `OG-gt-3` | `harvest_get_fundamentals`, `harvest_query_columns` (model_block, bestdata, refdata, histdata, segments, price; the tabular allow-list) | `app/harvest_figures.py`, `tests/test_og_gt3.py` | WORLD | ~74 | worker |
| `OG-gt-4` | `harvest_get_research`, `harvest_get_filing_analysis`, `harvest_get_peers_and_scores` | `app/harvest_research.py`, `tests/test_og_gt4.py` | WORLD | ~75 | worker |
| `OG-gt-5` | `harvest_get_published_analysis` (invokes `opal-amgt-scoped-api`) with its read-grant file and its own never-widen ask; ships only when that ask is signed | `app/harvest_published.py`, `tests/test_og_gt5.py` | WORLD | ~76 | worker |
| `OG-ap-18` | APPLY: gt-0..gt-4's gateway release on hv-2's live ref, served read of each tool under an Opal and a non-Opal principal; gt-5 follows on its own ask | (applier's paths) | WORLD | ~AE | worker |

`app/` is `infra/aws/ec2/opal-gateway/app/` (an infrastructure path, so the gate's floor makes every gateway cell WORLD, as OG-hv-1 was); each tool cell reads its contract section in G1 by line range (inlined on its face).
A cell over about 300 product lines (gt-2, gt-3, gt-4 may be) takes the full limbs and `worker`; none is `worker-light`.

**Chains.**
- `OG-gt-0` -> `OG-gt-1`, `OG-gt-2`, `OG-gt-3`, `OG-gt-4`, `OG-gt-5` (each imports the base; a data edge). After gt-0's merge the
  five are independent: disjoint new files, no shared write.
- `OG-hv-2` -> `OG-ap-18` (the grant first: every tool reads through it); `OG-ap-18` -> `OG-ap-17` -> `MX-r-13`.
- Applier queue for `0.7.0_AE_CloudOps~Z`: OG-hv-2, OG-ap-18, OG-ap-17, then MX-r-13's slot (NFRA_MCPINDEX).

**fanout (plan):** wave 1: 1 (OG-gt-0, the base). Wave 2: 5 of 5 independent chains after gt-0's merge, cap 8; `OG-gt-5` rides its
own ask and may trail. Spawn model per `org/ref/MODEL_POLICY.json` (haiku, effort high).

**Cut-time reads (not done here):** each check a file dry-run at the base; `<paths>` carry `change_management/` and the
`.open_deploys/` sentinels on OG-ap-18 only; the risk class each `<paths>` implies is read from GATE xii before the cut.

## ADDENDUM R3-T.51 (2.0.0_SA_COO~O, 2026-10-14 ~14:1xZ) -- round 37, workstream ZS114-EDGE-AUTH (CTO ruling msg 34093)

**Source.** Row `NFRA_OPLGTW-Z-S114` (`4.0.0_SA_CRO~Z`, @f5d2c93a6a): the bare `/json-tiered/*` behavior on CloudFront
`EVTSA9VEHNZVH` serves `opal-data-portal-v2/json-tiered/` with no Lambda@Edge association (an unauthenticated GET returns 200;
its twin `/api/general/json-tiered/*` returns 401). `1.0.0_SA_CTO~Z` ruled (msg 34093): not an intended public path; attach
`auth-validator-edge` like the twin, after OG-hv-2, not a gateway blocker. The issuer's act inside its own decomposition.

| cell | what | risk | slot | class |
|---|---|---|---|---|
| `OG-zs-1` | APPLY: read 7 days of the bare path's CloudFront traffic (a non-portal consumer is a STOP to the CTO); then attach `auth-validator-edge` (viewer-request) to behavior 7 `/json-tiered/*` in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, one targeted change under a deploy ledger; prove 401 unauthenticated and the authenticated twin still 200; read the `/api/scoped/security-scanner/*` authorizer once | WORLD | ~AE | worker |

**Chain:** `OG-hv-2` (applier `0.7.0_AE_CloudOps~Z`) -> `OG-zs-1`. Independent of the gateway queue (no gateway release); the applier takes it right after OG-hv-2 closes.
**fanout:** 1 of 1 chain, cap 8.

## ADDENDUM R3-T.52 (2.0.0_SA_COO~O, 2026-10-14 ~14:3xZ) -- round 37, workstream FWD22-W3: FWD-22 groups G3, G6, G5, G2 (PLAN; PRD v3.3 @bb9d1ece12 ADMITTED)

**Source.** PRD v3.1-v3.3 addenda (CTO msgs 34099, 34109, 34116): order to Friday 2026-10-16 is G1, then G3 + G2 core, then G6 + G5 wave A,
then the rest; one never-widen ask per group; G2 client data NEVER reads through `gateway-global-internal-reader-role` (v3.2: key-segment
vendors through one-firm prefix-conditioned roles, existing ones first; only SmartX and Tax SMA filter rows in code, with a two-firm negative arm).
Only the plan is written here. Each group's orders are cut as its precondition lands; the first is OG-gt-6.

| cell | what | writes (new files only) | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-6` | the scope seam: a `Scope(bucket, served_prefixes, client)` and the four S3 helpers (`list_keys`, `newest_part`, `read_parquet`, `read_json`) taking a scope, reusing `harvest_typed`'s envelope, projection and caps; the HARVEST scope is the existing behaviour byte for byte | `app/typed_scope.py`, `tests/test_og_gt6.py` | WORLD | ~77 | gt-0 (merged) |
| `OG-gt-7` | the hookup of the ten G1 typed tools: `tools.py` registrations, `SAFE_TOOLS` and `NATIVE_TOOLS`, the registry count 65 -> 75 and the non-data count 56 -> 66; applied by the issuer's prepared script (`deliverables/2.0.0_SA_COO~O/r37/hookup_g1.py`) because the gateway app files are in lane CLOUD_OPS_OR_ETL | five existing files | WORLD | ~78 | gt-1..gt-4 (merged) |
| `OG-pt-1` | G3 tools `portal_get_model_positioning`, `portal_get_model_attribution`, `portal_get_market_returns` (json-tiered: the G3 ask's widening), `portal_get_market_regime` | `app/portal_models.py`, tests | WORLD | ~79 | gt-6 |
| `OG-pt-2` | G3 tools `portal_get_macro`, `portal_get_valuation`, `portal_get_security_scan`, `portal_get_pipeline_freshness` | `app/portal_macro.py`, tests | WORLD | ~80 | gt-6 |
| `OG-pt-3` | G3 tool `mdpf_get_category_views` (firm-scoped: one scope per call, reusing the `portal_index` firm gate) | `app/portal_mdpf.py`, tests | WORLD | ~81 | gt-6 |
| `OG-nw-1` | G6 tools `news_search_articles` (14-day cap), `news_trending_topics`, `news_keyword_intelligence`, `news_market_mood`, `news_for_security` (the four live news DynamoDB tables and the two portal singletons) | `app/news_typed.py`, tests | WORLD | ~82 | gt-6 |
| `OG-et-1` | G5 wave A ownership tools `etfs_get_partner_ownership` (firm REQUIRED), `etfs_get_ownership_rollup` (the dashboard's own totals), `etfs_get_monthly_report` (coverage from each partner's csv, never the verdict) | `app/etfs_ownership.py`, tests | WORLD | ~84 | gt-6 |
| `OG-et-2` | G5 wave A fund tools `etfs_get_fund_nav_history`, `etfs_get_fund_holdings` | `app/etfs_funds.py`, tests | WORLD | ~85 | gt-6 |
| `OG-et-3` | G5 wave A read grant: one policy on the internal reader role for the exact `SERVED_PREFIXES` of et-1 and et-2 (generated by AST, as hv-2's was) on `opal-data-etfs`, plus the G5 never-widen ask; Phase A only. **A1 (CTO msg 34198, PRD v3.7 @0c72cd303a):** the ONE G5 ask and its grant ALSO name the rival-funds gold prefixes (`rivalfunds/etfs/gold/*`) and the platinum page prefix, so the rival tools (CRO's G5r spec @e1b9937129: nine gold-backed rival tools plus `etfs_get_rival_page_status`, a fund's latest report from `canonical_shape` only, row Z-S124) need no second ask | `terraform/opal-gateway/etfs_read_iam.tf`, ask | WORLD | ~87 | et-1, et-2 |
| `OG-ec-1` | the Eclipse converter's reviewed schema edit (row Z-S117, CTO msg 34152): admit `defaultTradingEngineId` to `(eclipse, portfolios_simple)` in `mirror_schemas.py`, re-vendor the eclipse copy byte-identical, tests; no apply | `data/assets/scripts/silver/mirror_schemas.py`, the eclipse copy, tests | WORLD | ~86 | none |
| `OG-ec-2` | APPLY: the eclipse Lambda code update under a deploy ledger, then the re-drive of the 12 bronze objects of 2026-10-10 onward; graded on the silver guard and the freshness in trading days. Cut when OG-ec-1 merges | applier | WORLD | ~AE | ec-1 |
| `OG-cl-0` | G2 design cell, READ ONLY: the inventory of existing firm- and vendor-scoped reader roles (Schwab, Black Diamond, Orion, Eclipse, Commonwealth), what each reads, and what is missing; the `client_*` tool contract (`client_resolve_account` returns candidates, last-4 never unique; every other tool takes a resolved account id); the `NFRA_OPLGTW_CONTRACT.json` and `scopes.json` additions for 08403355 | `W/` records only | SERVED | ~83 | none |
| `OG-cl-1..n` | the vendor adapters behind `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees` (BD, Orion/Eclipse, Schwab, Commonwealth, SmartX with the code row filter), one cell per vendor, reading ONLY `opal-data-assets/<vendor>/<firm>/silver/` (Andrew-direct ~15:0xZ, CTO msg 34134: no opal-data-bd, no mdpf feeds, no per-firm Tax SMA gold), cut when `OG-cl-0` lands | per vendor | WORLD | ~84+ | cl-0, gt-6 |
| `OG-ap-19` | APPLY: the G3 + G6 tools' release, with the G3 ask (json-tiered) and the G6 ask (the four DynamoDB tables and two singletons) | applier | WORLD | ~AE | pt-1..3, nw-1, ap-18 |
| `OG-ap-20` | APPLY: the G5 wave A grant (policy on the internal reader role) and release | applier | WORLD | ~AE | et-1, ap-19 |
| `OG-ap-21` | APPLY: the G2 core roles (a missing one named by `lib/opal_naming.py`), then the release | applier | WORLD | ~AE | cl-1..n, ap-20 |

**Chains.** gt-6 -> {pt-1, pt-2, pt-3, nw-1, et-1} (five independent chains once gt-6 merges); `OG-cl-0` independent now; cl-1..n after cl-0 and gt-6.
Releases queue behind `OG-ap-18` in the order ap-19, ap-20, ap-21, then `OG-ap-17`, then MX-r-13.
**fanout (plan):** now, wave 2 holds five workers (gt-1..gt-5); `OG-gt-6` and `OG-cl-0` start as workers free up (cap 8); then 5 of 5 after gt-6.
**Not built this round:** G2's remaining tools (lots, performance, profile, insurance), G5 wave B, G4's `mdpf_get_model_composition` (wave 3), the PII-bearing ADVI leaves.

**G2 order of cells (CTO msgs 34176 and the Andrew-direct 49F decision, PRD v3.6 @6d6702425a).** Schwab first (its gateway-trusted role exists; resolve source = the distinct account ids in Schwab silver, last-4 over them, candidates, deduped across the overlapping masters), then 49F Black Diamond (reads `opal-data-bd/silver/` through its own scoped role and ask, CRO's G2f; increment versus snapshot measured first; `assets` and `transactions_enriched` answer with their lag stated), then Orion/Inflection (Eclipse after Z-S117), BD Cottonwood, SmartX (row filter), Commonwealth; each of the last four with one prefix-conditioned role and one ask. Gateway code types no S3 key: each adapter reads its key from its DATA_CATALOG row (CTO msg 34173).

**Rival funds (G5r, v3.7).** Build order: after the Friday set and ahead of the remaining G2 vendors (after Schwab and 49F Black Diamond). Cells are cut when the rival catalog rows exist (gateway code types no S3 key).

## ADDENDUM R3-T.53 (2.0.0_SA_COO~O, 2026-10-14 ~20:0xZ) -- round 37, workstream G1-FIX: two defects found at the OG-ap-18 Phase B GO (FWD-22)

**The finding (measured, not inferred).** `app/harvest_identity.py:86` and `app/news_typed.py:24` set `_REPO_ROOT = Path(__file__).resolve().parents[5]`. On the host the
file is `/opt/opal-gateway/app/<module>.py`, which has 4 parents, so `parents[5]` raises `IndexError` AT IMPORT, and `tools.py` imports `harvest_identity`: the
service would not start. The release `4275edccad` (all three halves signed) is therefore NOT deployable as cut. The GO was withheld by a HOLD to `~Z` before any
act. The same finding explains Z-S125 (`lib/` is absent from `/opt/opal-gateway`). OG-ap-18 re-cuts on the fix; its three halves re-sign at the new `release_sha`.

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-8` | (1) both modules resolve the calendar's root WITHOUT a fixed-depth parent index: the artifact root (the app dir's parent, where the deploy stages `lib/`), then each ancestor in turn, the first holding `lib/trading_calendar.py`; absent -> the existing reported degradation. (2) `deploy-to-ec2.sh` stages `lib/trading_calendar.py` from the repo into the artifact as `lib/` (fail closed if the source is missing) and the tar names it. (3) a host-shaped import test | `app/harvest_identity.py`, `app/news_typed.py`, `deploy-to-ec2.sh`, `tests/test_og_gt8.py` | WORLD | ~87 | none |
| `OG-gt-9` | `harvest_search_articles` reads the gold `article_sentiment` partitions only from the earliest `fetched_at` day of the page onward (a sentiment row cannot predate its article's fetch; the premise is MEASURED on the real bucket and its violation count printed), so a 7-day window reads a few partitions, not all. The denominator states partitions read of partitions total | `app/harvest_press.py`, `tests/test_og_gt9.py` | WORLD | ~88 | none |
| `OG-ap-18` (re-cut) | the applier re-cuts the release on the live ref with gt-8 and gt-9 merged; the three halves re-sign at the new `release_sha`; Phase B reads `harvest_search_articles` through the public endpoint (CVO condition: ALB idle timeout 60 s) | applier | WORLD | ~AE | gt-8, gt-9 |

**Chains.** gt-8 and gt-9 are independent (disjoint write sets). **fanout:** 2 of 2 chains, cap 8. Nothing here edits a shared file; the hookup is already merged.

## ADDENDUM R3-T.54 (2.0.0_SA_COO~O, 2026-10-14 ~20:3xZ) -- round 37, workstream G3G6-HOOKUP (FWD-22; plan R3-T.52, PRD v3.7)

| cell | what | writes (existing files) | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-pt-4` | the hookup of the eight G3 portal tools (pt-1, pt-2) and the five G6 news tools (nw-1): `tools.py` registrations, `SAFE_TOOLS` and `NATIVE_TOOLS`, the registry count 75 -> 88 and the non-data count 66 -> 79; applied by the issuer's prepared script (`deliverables/2.0.0_SA_COO~O/r37/hookup_g3g6.py`, dry-run on HEAD copies) because the gateway app files are in lane CLOUD_OPS_OR_ETL | five existing files | WORLD | ~89 | pt-1, pt-2, nw-1 (merged) |

`OG-pt-3` stays superseded (`mdpf_get_category_views` is `~MI`'s round-16 ToolRow), so G3 is eight tools, not nine. The release is `OG-ap-19`; it takes these hunks by hunk, as ap-18 took gt-7's.
**fanout:** 1 of 1 chain (cap 8), beside the two G1-FIX workers (disjoint write sets: gt-8 and gt-9 touch neither `tools.py` nor the lists).

## ADDENDUM R3-T.55 (2.0.0_SA_COO~O, 2026-10-14 ~21:0xZ) -- round 37, workstream G1-FIX2: the same import-time defect in the two G3 portal modules, and the Seeking Alpha runner (PRD v3.8)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-10` | `app/portal_models.py:39` and `app/portal_macro.py:55` carry the same `parents[5]` as the two modules OG-gt-8 fixed (worker row Z-W87-S1; issuer re-measure: 2 of 69 shipped modules). Same fix (artifact root first, then each ancestor; none -> the reported degradation) and a host-shaped import test | `app/portal_models.py`, `app/portal_macro.py`, `tests/test_og_gt10.py` | WORLD | ~90 | gt-8 (merged `43e5e0383e`) |
| `OG-sa-1` | the site Z harvest cycle runner without Seeking Alpha (PRD v3.8 @3bb7fb022e, CTO msg 34216): (1) read SA access (row AMGT_HARVST-Z-W37-S4, HTTP 402) and stop if refused; (2) otherwise stop the runner by its STOP file at a cycle boundary and re-register it with `-Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce` after reading `-Plan`; (3) place the trading-day trigger for the four SA tables. Applier order under a ledger | applier (`0.7.0_AE_CloudOps~ZW`) | WORLD | ~AE | none |

**Chains.** gt-10 and sa-1 are independent of each other and of OG-pt-4. **fanout:** 1 of 1 worker chain (gt-10), cap 8; sa-1 is an applier order. `OG-ap-19` waits for gt-10.

## ADDENDUM R3-T.56 (2.0.0_SA_COO~O, 2026-10-14 ~22:0xZ) -- round 37, workstream YEARINREVIEW: the refreshed /yearinreview page (Andrew-direct ~21:4xZ; CTO msg 34233)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-yr-1` | APPLY: the CRO's final page (`947fc522a8`, md5 `0d828b51d433a24f7e2ef2e6ea7967ee`) copied byte for byte to `app/static/yearinreview/index.html` and shipped as its own ONE-FILE gateway release on `OG-ap-18`'s release as base; two never-widen halves (CTO, COO); served read-back by md5 and by the data date `2026-10-11` | applier (`0.7.0_AE_CloudOps~Z`) | WORLD | ~AE | `OG-ap-18` closed |

Release queue after this addendum: ap-18 (G1, re-cut) -> yr-1 -> ap-17 (bd-3, re-cut) -> MX-r-13 (`~MI`) -> ap-19 (G3 + G6 + the `gw_news_read` grant) -> ap-20 (G5 wave A) -> ap-21 (G2 core).

## ADDENDUM R3-T.57 (2.0.0_SA_COO~O, 2026-10-14 ~22:2xZ) -- round 37, workstream G3G6-RELEASE: the G3 + G6 release (FWD-22; plan R3-T.52)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-19` | APPLY: the eight G3 portal tools and five G6 news tools (merged: pt-1, pt-2, nw-1, gt-10, pt-4) released with their two read grants (G6: the worker's `news_read_iam.tf`, DynamoDB Query/GetItem on three tables and `date-index`; G3: one policy on the internal reader role for `json-tiered/market-overview/`, generated by AST, legacy_addresses rows first), three halves, served read of thirteen tools | applier (`0.7.0_AE_CloudOps~Z`) | WORLD | ~AE | `OG-ap-18`, `OG-yr-1` closed |

Release queue: ap-18 -> yr-1 -> ap-19 -> ap-20 (G5 wave A) -> ap-17 (bd-3 re-cut) -> ap-21 (G2 core). `OG-ap-17` moves behind the Friday set: it is inert until `OG-mg-1` writes the profile.

## ADDENDUM R3-T.58 (2.0.0_SA_COO~O, 2026-10-14 ~22:4xZ) -- round 37, workstream G2-ECLIPSE: deploy the Eclipse converter fix (row Z-S117; CTO msg 34152)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ec-2` | APPLY: the converter code `OG-ec-1` merged (`d2ad76dd24`) deployed through Terraform (one resource, ledger `nfra-oplgtw-eclipse-converter`), then the silver sweep driven once by the applier (not waited for) until the guard reads PASS (`expected 552 landed 547 missing 5` today); graded on the guard and the Eclipse silver freshness in trading days; two never-widen halves (CTO, COO) because the sweep writes served silver | applier (`0.7.0_AE_CloudOps~ZS`) | WORLD | ~AE | `OG-ec-1` merged |

Z-S110 (49F producer OutOfMemory) follows once its cause is read. Eclipse silver tables serve G2's Orion/Inflection steps, which come after the Friday set.

## ADDENDUM R3-T.59 (2.0.0_SA_COO~O, 2026-10-14 ~23:4xZ) -- round 37, workstream GT5-HOOKUP: the published-analysis tool's hookup (FWD-22; OG-gt-5 merged `640c8a55f7`)

| cell | what | writes (existing files) | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-11` | the hookup of `harvest_get_published_analysis`: `tools.py` registration, `SAFE_TOOLS` and `NATIVE_TOOLS`, the registry count 88 -> 89 and the non-data count 79 -> 80; applied by the issuer's prepared script (`deliverables/2.0.0_SA_COO~O/r37/hookup_gt5.py`, dry-run on HEAD copies) because the gateway app files are in lane CLOUD_OPS_OR_ETL | five existing files | WORLD | ~91 | gt-5, gt-6 (merged), pt-4 (merged) |

The tool invokes the published-analysis Lambda (`AMGT_SCOPED_API_FUNCTION`), so its release carries the invoke grant (`harvest_published_invoke_iam.tf`) and its own never-widen ask: a later release order (after `OG-ap-19`).
**fanout:** 1 of 1 chain (cap 8).

## ADDENDUM R3-T.60 (2.0.0_SA_COO~O, 2026-10-15 ~00:5xZ) -- round 37, workstream G3-CATVIEWS: `mdpf_get_category_views` by its table row (replaces the superseded OG-pt-3; `~MI` msg 34293)

| cell | what | writes (new files only) | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-pt-5` | G3 tool `mdpf_get_category_views(scope)` (firm-scoped, one scope per call, `global` its own object): the key template and bucket are read from the catalog table row `opal_data_portal_v2_platinum_mdpf_category_views` (c-5902fd256409, v0.5), the firm gate is the existing `portal_index`/`catalog_gate` one; no S3 literal in the code | `app/portal_mdpf.py`, `tests/test_og_pt5.py` | WORLD | ~92 | gt-6, MX-c-14 (merged) |

The hookup of this tool, `etfs_*` (et-1, et-2) rides one batch hookup cell after those modules merge.
**fanout:** 3 worker chains now (et-1 ~84, et-2 ~85, pt-5 ~92), cap 8; disjoint write sets.

## ADDENDUM R3-T.61 (2.0.0_SA_COO~O, 2026-10-15 ~01:4xZ) -- round 37, workstream G5CV-HOOKUP: the batch hookup of the G5 wave A tools and `mdpf_get_category_views` (FWD-22)

| cell | what | writes (existing files) | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-12` | the hookup of `etfs_get_partner_ownership`, `etfs_get_ownership_rollup`, `etfs_get_monthly_report` (et-1 `13979abd45`), `etfs_get_fund_nav_history`, `etfs_get_fund_holdings` (et-2 `9a16c77a6a`) and `mdpf_get_category_views` (pt-5 `00e2b960ea`): `tools.py` registrations, `SAFE_TOOLS` and `NATIVE_TOOLS`, the registry count 89 -> 95 and the non-data count 80 -> 86; applied by the issuer's prepared script (`deliverables/2.0.0_SA_COO~O/r37/hookup_g5cv.py`, dry-run on HEAD copies) | five existing files | WORLD | ~93 | et-1, et-2, pt-5, gt-11 (merged) |

The release is `OG-ap-20` (G5 wave A + category views): one read grant on the internal reader role generated from the catalog rows of the named entities, plus the rival-funds gold and platinum page prefixes of PRD v3.7, one ask.
**fanout:** 1 of 1 chain (cap 8).

## ADDENDUM R3-T.62 (2.0.0_SA_COO~O, 2026-10-15 ~02:0xZ) -- round 37, workstream G5A-CV: the G5 wave A + category-views release (FWD-22; plan R3-T.52 and its A1, PRD v3.7)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-20` | APPLY: the five G5 wave A etfs tools and `mdpf_get_category_views` (merged: et-1, et-2, pt-5, hookup gt-12) released with ONE read grant on the internal reader role for `opal-data-etfs` (generated from the catalog rows of the tools' entities, plus the rival-funds gold and platinum page prefixes of PRD v3.7, one ask; ListBucket confined by prefix), three halves, served read of six tools | applier (`0.7.0_AE_CloudOps~Z`) | WORLD | ~AE | `OG-ap-18` closed; `OG-gt-12` merged |

Release queue: ap-18 -> ap-19 (G3 + G6) -> ap-20 -> ap-17 (bd-3 re-cut) -> ap-21 (G2 core).

## ADDENDUM R3-T.63 (2.0.0_SA_COO~O, 2026-10-15 ~03:5xZ) -- round 37, workstream R37-PERSON: the C-PERSON reader (PRD v2.9; CTO msgs 33954, 33958; NFRA_MCPORTAL F2 waits on it)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cp-1` | the gateway reads MC Portal's per-person `person_access` record from the grant store: the record kind added to the closed POLICY set in both contract copies and `access_state.py`; `data_entitlement.person_access(principal)` (one strong `AccessStateStore.get`, fail closed `person_record_unavailable`); evaluation after the Opal-only, C2, tier and data-grant gates: STOP (`stopped: true` denies every tool, the master_admin included), NARROW (`tools_deny`, `channels_deny`; deny beats allow), WIDEN only to a SERVED tool the floor lists for some principal and only for an Opal principal; audit `person_record_rev`; no tier field | `app/data_entitlement.py`, `app/access_state.py`, `app/tools.py`, both contract copies, `tests/test_og_cp1.py`, `tests/test_access_state.py` | WORLD | ~94 | OG-bd-3 (drained) |

The release is a later gateway order after `OG-ap-20`; `2.0.0_SA_COO~MP`'s F2 (the writer) and close run wait on it.
**fanout:** 1 of 1 chain (cap 8).

## ADDENDUM R3-T.64 (2.0.0_SA_COO~O, 2026-10-15 ~04:4xZ) -- round 37, workstream G6-INTERNAL: the news readers move to the internal reader role (PRD v3.9 @8c84e01428, the owed follow-up cell)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-nw-2` | the code half: `internal_role.dynamodb_client()` mirroring `s3_client` (same env key, same refresh, same no-fallback rule, its own cache entry) and `news_typed._ddb()` preferring it; an unavailable internal role refuses with zero reads and never falls back to the instance identity | `app/internal_role.py`, `app/news_typed.py`, `tests/test_og_nw2.py` | WORLD | ~95 | OG-nw-1, OG-gt-8 (merged) |

The Terraform half (the same Query/GetItem statement on the internal reader role, `gw_news_read` destroyed by name) and the release ride one applier order after `OG-ap-20`, grant first.
**fanout:** 2 worker chains now (cp-1 ~94 re-seated, nw-2 ~95), cap 8; disjoint write sets.

## ADDENDUM R3-T.65 (2.0.0_SA_COO~O, 2026-10-15 ~05:2xZ) -- round 37, workstream G1-INTERNAL: the published-analysis tool invokes its Lambda through the internal reader role (FWD-22; PRD v3.1 rule, v3.9 exception not extended)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-gt-13` | `internal_role.lambda_client()` mirroring `s3_client` and `dynamodb_client` (same env key, no fallback, own cache entry) and `harvest_published._invoke` preferring it; an unavailable internal role refuses with zero invokes and never falls back to the instance identity | `app/internal_role.py`, `app/harvest_published.py`, `tests/test_og_gt13.py` | WORLD | ~96 | OG-gt-5, OG-nw-2 (merged) |

The release (`OG-ap-21`: the person reader `OG-cp-1`, `OG-nw-2`, this cell, the published-analysis tool's registration `OG-gt-11`) retargets `harvest_published_invoke_iam.tf` to the internal reader role and moves the news statement off the instance role, grant first.
**fanout:** 1 of 1 chain (cap 8).

## ADDENDUM R3-T.66 (2.0.0_SA_COO~O, 2026-10-15 ~05:4xZ) -- round 37, workstream R37-PERSON-FIX: the two tests OG-cp-1 turned red (found by `~MI`, msg 34340)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cp-2` | (1) re-serialise both contract copies exactly as `build_package` emits them, so the staged member equals the standard byte for byte (no value changes); (2) `test_access_get_not_live_when_type_unknown`: make its unknown-type condition explicit (the closed record set without `person_access`) now that the type is known | both contract copies, `tests/test_admin_people_access.py` | WORLD | ~97 | OG-cp-1 (merged) |

Merges before `OG-ap-21` is cut. **fanout:** 1 of 1 chain (cap 8).

## ADDENDUM R3-T.67 (2.0.0_SA_COO~O, 2026-10-15 ~06:5xZ) -- round 37, workstream PERSON-ROLES: the person reader, the two role moves and the published-analysis tool (PRD v2.9 C-PERSON, v3.1, v3.9)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-21` | APPLY: release `OG-cp-1` (+`OG-cp-2`), `OG-nw-2`, `OG-gt-13`, `OG-gt-5` with its hookup `OG-gt-11`; Terraform: the news statement re-created on the internal reader role, the published-analysis invoke statement retargeted to it, then `gw_news_read` destroyed BY NAME after the served read; three halves; the contract-staging test must read green at the new deployed commit | applier (`0.7.0_AE_CloudOps~Z`) | WORLD | ~AE | `OG-ap-20` closed |

`NFRA_MCPORTAL`'s F2 writer and close run wait on this release. Queue: MX-r-13 -> ap-20 -> THIS -> ap-17 re-cut -> G2.

## ADDENDUM R3-T.68 (2.0.0_SA_COO~O, 2026-10-15 ~06:5xZ) -- round 37, workstream EGRESS: the harvest runner's whole-prefix silver re-reads (PRD v3.10 @c3b76c142b; CTO msg 34372; CRO findings @b05fee1182)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-eg-1` | E1: a cycle-scoped incremental cache in `store.silver_latest` (silver parts are write-once: LIST, GET only the new parts, same `supersedes` rule, two-entry LRU, unchanged outside the context) used by the runner's cycle; E2: GET count and bytes counted in `store.py` and written into the cycle record as `s3_get_count` and `s3_get_bytes` (a record, never an alert) | `lib/research/harvest/store.py`, `lib/opal_data_harvest/harvest_grammar.py`, `lib/opal_data_harvest/cycle_runner.py`, a test file | WORLD | ~98 | none |
| `OG-eg-2` | APPLY (`0.7.0_AE_CloudOps~ZW`): the runner stopped at a cycle boundary, `-Plan` first, re-registered with the merged code (carrying the pending `sa` change); the live proof is the first cycle record's `s3_get_bytes` against the CUR baseline | applier | WORLD | ~AE | `OG-eg-1` merged |

Cost context: DataTransfer-Out $67.99 for 2026-10-11..14, 72% from `opal-data-harvest` (541 GB out of 8 GB stored), still running. FIRST in the queue after the release in flight.
**fanout:** 1 of 1 worker chain (cap 8).

## ADDENDUM R3-T.69 (2.0.0_SA_COO~O, 2026-10-15 ~07:1xZ) -- round 37, workstream NAMING-S3PREFIX: the naming gate grades an IAM s3:prefix condition value against the HEAD-held legacy registry (CTO msgs 34368, 34376; row Z-S140)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ng-1` | ONE clause in `.tools/naming-gate.py`'s S3Key limb on the MX-c-9 A4 / catalog-branch precedent (`df822c81b3`): an `s3:prefix` condition value equal (one optional trailing `*`) to a `legacy_addresses.json` row COMMITTED AT HEAD whose reader is the committing project, with matching shape, grades CONFORMANT; near misses, other readers, working-tree-only rows and the same string elsewhere are graded as before; a counted line is printed; self-test arms | `.tools/naming-gate.py`, `.tools/tests/test_naming_gate_s3prefix.py` | WORLD | ~99 | none; **merge waits on the laptop CTO's conditions** |

`OG-ap-20`'s grant commit follows the merge; ETF wave A waits only on this and the catalog release.
**fanout:** 2 worker chains (eg-1 ~98, ng-1 ~99), cap 8; disjoint write sets.

## ADDENDUM R3-T.70 (2.0.0_SA_COO~O, 2026-10-15 ~08:5xZ) -- round 37, workstream RIVAL-FUNDS: the rival-funds tools (G5r; PRD v3.7; CRO spec @e1b9937129; CTO msgs 34190, 34198; the rival catalog rows are LIVE with MX-r-13 @1b18b94979)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-rv-1` | five rival tools A over gold `peer_group_map`, `canonical_shape`, `security_universe`, `security_market`, `corporate_actions`, `security_names`, `input_census`: `etfs_get_peer_group_members`, `etfs_get_rival_fund_holdings`, `etfs_who_holds`, `etfs_get_security_reference`, `etfs_get_coverage`; keys from the catalog rows; newest part per date; a fund's latest report from canonical_shape only (Z-S124) | `app/etfs_rivals.py`, `tests/test_og_rf1.py` | WORLD | ~100 | none (OG-et-2's module is the model; catalog v0.5 live) |
| `OG-rv-2` | five rival tools B over gold `trade_schedule`, `flow_reconciliation`, `buying_trend`, `holding_contribution`, `research_hypotheses` and the platinum page manifest: `etfs_get_fund_trades`, `etfs_get_fund_flows`, `etfs_compare_peers`, `etfs_get_research_notes`, `etfs_get_rival_page_status` | `app/etfs_rivals_flow.py`, `tests/test_og_rf2.py` | WORLD | ~101 | none |
| `OG-rv-3` | HOOKUP: a worker applies the issuer's prepared script `r37/hookup_rv.py` (the gateway app files are lane CLOUD_OPS_OR_ETL, which the COO cannot commit): register the ten tools (`tools.py`, `data_entitlement.py`, `destructive_ops.py`) and re-pin the counts 95 -> 105 and 86 -> 96, as `OG-gt-12` did | `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py`, the pinned-count tests | WORLD | ~102 | rv-1, rv-2 (both merged) |
| `OG-ap-22` | APPLY (not cut yet): the release of the ten rival tools; the read grant for `rivalfunds/etfs/gold/*` and the platinum page prefix is already in OG-ap-20's ask, so no second ask | applier | WORLD | ~AE | rv-3, ap-21 |

Name ruling: the CRO's `etfs_get_fund_holdings` for rivals collides with OG-et-2's tool of that name (the four Opal funds); the rival tool is `etfs_get_rival_fund_holdings`.
**Chains.** rv-1 and rv-2 are independent (disjoint write sets; slots ~100, ~101, both merged); rv-3 (slot ~102) follows both. **fanout:** 2 of 2 chains for rv-1/rv-2, then 1 of 1 for rv-3, cap 8.

## ADDENDUM R3-T.71 (2.0.0_SA_COO~O, 2026-10-15 ~16:5xZ) -- round 37, workstream HARVEST-RETIRE: all harvest operations move to dell1; the site Z runner retires (Andrew-direct ~16:3xZ; PRD v3.11 @32b70d1b86; CTO msg 34500)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-eg-3` | APPLY (`0.7.0_AE_CloudOps~ZW`): the runner ends at a job boundary (STOP file), the task is Disabled (nothing unregistered), the five pin worktrees stay locked as the rollback source, the ledgers `nfra-oplgtw-harvest-runner-silver-cache` and `nfra-oplgtw-harvest-runner-sa` close SUPERSEDED (FIRSTREC and WINDOW recorded NOT-EXERCISED) | applier | WORLD | ~AE | none |

`OG-eg-2` (the pin move and the bbg,sa leg 6b) and `OG-sa-1` (the sa window) become `superseded`: the E1+E2 code is in the library and runs on dell1 at pin `39ae28559b`; the GET-bytes proof is owed there under dell1's project.
**fanout:** 1 of 1 chains, cap 8.

## ADDENDUM R3-T.72 (2.0.0_SA_COO~O, 2026-10-15 ~17:3xZ) -- round 37, workstreams G2-BUILD and G3G5-REMAINDER: the G2 vendor adapters and the G3/G4/G5 remainders, cut as BUILD cells (CTO ruling @4356f15f16, msg 34516; PRD v3.6, v3.7)

The break: R3-T.52 planned `OG-cl-1..n` after `OG-cl-0` and `OG-gt-6`; both completed 2026-10-14 and no `OG-cl-1` was cut; the rival funds (G5r) went ahead of Schwab and 49F against PRD v3.7. This issuance cuts the adapters and the remainders; they do not wait on a release slot. The seam is `deliverables/2.0.0_SA_COO~O/r37/G2_ADAPTER_PROTOCOL.md`, so the six adapters build in PARALLEL without importing one another; the issuer hooks them into the core at the merge.

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cl-1` | the shared core of the five `client_*` tools (`app/client_core.py`, `app/client_role.py`) and the SCHWAB adapter (three masters deduped, never summed) | `app/client_core.py`, `app/client_role.py`, `app/client_adapter_schwab.py`, `tests/test_og_cl1.py` | WORLD | ~103 | cl-0 (complete) |
| `OG-cl-2` | the Black Diamond 49F adapter, reading `opal-data-assets/blackdiamond/49f/silver/` AND the live `opal-data-bd/silver/` through its own role (Andrew's 49F word; the contract's `no_source_49f_a2` refusals are replaced) | `app/client_adapter_bd49f.py`, `tests/test_og_cl2.py` | WORLD | ~104 | the protocol file |
| `OG-cl-3` | Orion and Eclipse (Inflection) | `app/client_adapter_orion.py`, `app/client_adapter_eclipse.py`, `tests/test_og_cl3.py` | WORLD | ~105 | the protocol file |
| `OG-cl-4` | Black Diamond Cottonwood | `app/client_adapter_bdcottonwood.py`, `tests/test_og_cl4.py` | WORLD | ~106 | the protocol file |
| `OG-cl-5` | SmartX (row filter, two-firm negative arm) | `app/client_adapter_smartx.py`, `tests/test_og_cl5.py` | WORLD | ~107 | the protocol file |
| `OG-cl-6` | Commonwealth (closed delivery, 78 td) | `app/client_adapter_commonwealth.py`, `tests/test_og_cl6.py` | WORLD | ~108 | the protocol file |
| `OG-gp-1` | G3/G4 remainder: the portal-v2 and mdpf catalog rows with no tool: classify each (COVERED by a live tool / BUILT here / DEFERRED), build the BUILT ones | `app/portal_served.py`, `tests/test_og_gp1.py` | WORLD | ~109 | none |
| `OG-gf-1` | G5 wave B: the non-rival etfs rows with no tool, same classification, plus the `etfs_get_positioning` extension | `app/etfs_silver.py`, `tests/test_og_gf1.py` | WORLD | ~110 | none |

After the merges: one HOOKUP cell per batch (registrations, lists, pins; the issuer's script), then the releases `OG-ap-23` (the client tools with their per-vendor read roles and never-widen asks, Schwab and 49F first) and the remainder release, queued after `OG-ap-22` and ahead of `OG-ap-17`. `NFRA_MCPINDEX` follows each release with a catalog cell (the `read_tool` rows).
**fanout:** 8 of 8 chains (cl-1 .. cl-6, g3-1, g5-2 have no edge between them), cap 8.

## ADDENDUM R3-T.73 (2.0.0_SA_COO~O, 2026-10-15 ~20:2xZ) -- round 37, workstreams GRANTS-BATCH and CODE-BATCH: the gateway finish by EOD 2026-10-16 (PRD v3.12 @532d1e68bb; CTO msg 34552; Andrew-direct "We have usage, run it now")

Two batches on two surfaces, never two appliers on the host at once: the IAM and grants (a second applier) beside the code releases (`~Z`, one host, one deploy at a time).

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-24` | APPLY (grants, `0.7.0_AE_CloudOps~ZS`): the six vendor read roles of the G2 client adapters (five NEW, `gateway-blackdiamond-read-role` EXTENDED), generated from the merged adapters by AST and the catalog rows, ONE ask; the roles are applied before the code deploy | applier | WORLD | ~ZS | OG-cl-1 merged (the generator's input) |
| `OG-ap-23` | APPLY (code, `0.7.0_AE_CloudOps~Z`): ONE release carrying every ready code cell: the ten rival tools (rv-1..3), the five client tools with the six adapters (cl-1..6 and their hookup), `mdpf_get_model_composition` (gp-1), the three etfs tools (gf-1) and their hookups; one never-widen ask; supersedes `OG-ap-22` | applier | WORLD | ~AE | MX-r-14 live; the hookup cell; OG-ap-24 Phase B for the client roles |

`OG-ap-22` becomes `superseded` by `OG-ap-23` (code). `OG-ap-21` (the person reader and its Terraform) is NOT superseded: it releases first, on the live ref after MX-r-14 (`c4c106aea1`), so `NFRA_MCPORTAL` is unblocked tonight (A1 of `OG-ap-24`). The hookup of the G2 tools and of the gp-1 and gf-1 tools is one more worker cell (`OG-ch-1`), cut when the adapters are merged.
**fanout:** 2 of 2 appliers on 2 surfaces; the hookup cell is one worker.

## ADDENDUM R3-T.74 (2.0.0_SA_COO~O, 2026-10-15 ~20:5xZ) -- round 37, workstream G2-CONFORM: the naming conformance of the G2 client modules (CTO msg 34575; LGIC rule 30)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cl-7` | the client core and the seven adapters resolve every canonical firm name through `lookup()` (no hand-kept literal, no placement override); the modules still import in the host shape (no `lib/opal_naming.py` beside them: lazy resolution, an enveloped `registry_unavailable` refusal); a missing registry row is `4.0.0_SA_CRO~Z`'s | `app/client_core.py`, `app/client_role.py`, the seven `app/client_adapter_*.py`, their tests | WORLD | ~111 | cl-1 .. cl-6 merged |

**fanout:** 1 of 1 chains, cap 8. Folded into the cl merges per the CTO: it runs the moment the adapters are on trunk, in parallel with the hookup.

## ADDENDUM R3-T.75 (2.0.0_SA_COO~O, 2026-10-15 ~23:5xZ) -- round 37, workstream G2-HOOKUP: the client core takes two adapters per vendor and keys the Black Diamond read role by firm

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ch-1` | `register_adapter` holds several modules per vendor with DISJOINT `FIRMS` (the two Black Diamond adapters share `VENDOR = "blackdiamond"`), every route picks the module holding the call's canonical firm; `client_role.role_key` keys the Black Diamond read role by the prefix's firm segment (`BLACKDIAMOND49F_READER_ROLE_ARN`, `BLACKDIAMONDCOTTONWOOD_READER_ROLE_ARN`), so IAM fences the two firms apart (ap-24 A3); `Ctx.firm_roster()` builds `{advisor_name: canonical firm}` from the real roster (cl-5 A2) | `app/client_core.py`, `app/client_role.py`, `tests/test_og_ch1.py` | WORLD | ~111 | cl-1 .. cl-6 merged |

**fanout:** 1 of 1 chains, cap 8. One chain with `OG-cl-7` (the same two files): ch-1 first, cl-7 second, both in slot ~111. The tool registrations, the import lines, the pins and the roster copy under `app/refs/` are the ISSUER's hookup at the merge (`r37/hookup_ch.py`), not a cell.

## ADDENDUM R3-T.76 (2.0.0_SA_COO~O, 2026-10-16 ~03:2xZ) -- round 37, workstream JSON-SERVED: the typed reads of the portal-v2 json objects no tool reads (PRD v3.13 @def417d2be as corrected @7656f484ab; cross-adjudication XA-20261016T024917Z-cdcc; MCPINDEX msg 34654)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-sv-1` | ONE module of typed reads for the seven `opal-data-portal-v2` rows `served_correlation_data`, `served_etf_returns`, `served_factor_tilts`, `served_model_portfolio_timeseries`, `served_model_portfolios_views`, `served_peer_performance`, `served_trending_latest`: each decided BUILT or RULED_OUT by its own freshness at build (views is out: 93 trading days stale); no new IAM (every prefix is under `json/`, granted by `queryv0-iam.tf:34`); the registrations are the issuer's hookup | `app/portal_json_served.py`, `tests/test_og_sv1.py`, the record and the probe | WORLD | ~113 | the hookup merged (5aeafbda15) |

`opal-harvest-security-metrics` is not built here (dell1 AMGT_HARVST, PRD v3.13 item 5). The release is `OG-ap-23` (the code batch), which carries these tools after the hookup.
**fanout:** 1 of 1 chains, cap 8. Disjoint from `OG-cl-7` (client modules) and from every merged cell; the hookup lines are the issuer's.

## ADDENDUM R3-T.77 (2.0.0_SA_COO~O, 2026-10-16 ~03:3xZ) -- round 37, workstream JSON-SERVED-2: the capital-markets assumptions tool (CTO ruling @131991960e; MCPINDEX msg 34695)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-sv-2` | `portal_get_cma_assumptions` in the json-served module for `opal_data_portal_v2_served_cma_assumptions` (`json/capital-markets/assumptions.json`, 27 rows, annual 2026 edition; no new IAM, under `json/*`) | `app/portal_json_served.py`, `tests/test_og_sv2.py`, the record and the probe | WORLD | ~113 | `OG-sv-1` merged (same module) |

**fanout:** 1 of 1 chains, cap 8. One chain with `OG-sv-1` (the same file): sv-1 first, sv-2 second, both in slot ~113.

## ADDENDUM R3-T.78 (2.0.0_SA_COO~O, 2026-10-16 ~03:4xZ) -- round 37, workstream G2-CONFORM-2: the Black Diamond upstream identifiers enter name_rulings.json; the unread orion/4698 alias goes (CTO msg 34699; ruling @d97ea3ae82 section 1)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cl-8` | one `none_owed` row per refused (name, type) of `bd_account_id`, `bd_account_number`, `fact_bd_allocation`, `market_value_profile` in `infra/logic/registry/name_rulings.json`; delete the unread `orion/4698` alias from `client_core.py`; the full-add naming gate over `app/client_*.py` in ENFORCE prints no REFUSE (so `OG-cl-7` AC2 closes) | `infra/logic/registry/name_rulings.json`, `app/client_core.py`, the investigation file | WORLD | ~111 | `OG-cl-7` merged (517f78548d) |

**fanout:** 1 of 1 chains, cap 8. Disjoint from `OG-sv-1` / `OG-sv-2` (the json-served module). It is an `OG-ap-23` batch cell: it merges before the release is cut.

## ADDENDUM R3-T.79 (2.0.0_SA_COO~O, 2026-10-16 ~03:5xZ) -- round 37, workstream G2-CONFORM-3: the `etfs` field key of the served etf_returns object enters name_rulings.json (CTO msg 34709; row Z-W113-S1)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cl-9` | one `none_owed` row for `etfs` (type `hand-kept carrier`, the served object's own key, evidence `portal_json_served.py:374` and `:376`) in `infra/logic/registry/name_rulings.json`; no code, no override | `infra/logic/registry/name_rulings.json` | WORLD | ~111 | `OG-sv-1` merged (40051277fc), `OG-cl-8` merged (2ed472c4b9) |

**fanout:** 1 of 1 chains, cap 8. One chain with `OG-cl-8` (the same file): cl-8 first, cl-9 second, both in slot ~111. The issuer's hookup of the seven json-served tools is on trunk (`7200f493d2`).

## ADDENDUM R3-T.80 (2.0.0_SA_COO~O, 2026-10-16 ~04:0xZ, UTC) -- round 37, workstream NAMING-GATE-RULINGS: the commit-time naming gate grades a name with a name_rulings.json row from that row (XA-20261016T034740Z-28da ruled (a); CTO msg 34713)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ng-2` | `.tools/naming-gate.py` reuses `naming-apply-gate.py`'s `ruling_amend` (name, node type) lookup: `none_owed` or an equal `canonical` is RULED (passes, row cited), a different `canonical` REFUSEs, no row leaves the grade unchanged; three self-test arms (admit, no-row control, other-type control); the ten refused lines (8 bd49f, 2 etfs) re-graded RULED; no override | `.tools/naming-gate.py`, optionally `.tools/tests/test_naming_gate_rulings.py` | WORLD | ~114 | `OG-cl-8`, `OG-cl-9` merged (the five rows on the base) |

**fanout:** 1 of 1 chains, cap 8. Disjoint from every other open cell. It is an `OG-ap-23` batch cell: the release commit cannot land in ENFORCE until the ten lines grade RULED. Before the merge the issuer re-runs the self-test, plants a name with no row and a row for another pair, and re-grades the ten lines.

## ADDENDUM R3-T.81 (2.0.0_SA_COO~O, 2026-10-16 ~04:4xZ) -- round 37, workstream CLASS-INCREMENT: census of the DynamoDB etf-classifications table and the spec of its tool and grant (the NAMED NEXT INCREMENT; CTO ruling @d97ea3ae82 section 2; CRO G4 section 3.3)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ac-1` | read-only census (`DescribeTable`, a bounded `Scan`: counts, key schema, attribute names, `classified_by` counts, the freshness field and its newest date, each with a claim word) and a spec of `mdpf_get_security_classification` with its ONE grant (read action on the table ARN, no write, no scan) and its refusal arms; no code, no IAM | `ETF_CLASS_CENSUS.json`, `ETF_CLASS_SPEC.md` under the worker's deliverables folder | WORLD | ~113 | none |

**fanout:** 1 of 1 chains, cap 8. Disjoint from `OG-ap-23` (no code, no IAM). It is outside the 22:00Z line; the build cell and the grant order (`0.7.0_AE_CloudOps~ZS`, three halves) are cut from its spec.

## ADDENDUM R3-T.82 (2.0.0_SA_COO~O, 2026-10-16 ~04:5xZ) -- round 37, workstream G2-CONFORM-4: the `etfs` name_rulings.json row cites the CTO ruling it rests on (CTO msg 34732)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-cl-10` | append one sentence to the `evidence` of the `etfs` row naming `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md`; nothing else changes | `infra/logic/registry/name_rulings.json` | WORLD | ~111 | `OG-cl-9` merged (80e59dd45e) |

**fanout:** 1 of 1 chains, cap 8. One chain with `OG-cl-9` (the same row). It must merge before the `OG-ap-23` release commit is built if the applier's tree reads the file, but the row's text does not change any verdict: the gate reads `none_owed`.

## ADDENDUM R3-T.83 (2.0.0_SA_COO~O, 2026-10-16 ~05:0xZ) -- round 37, workstream CLASS-INCREMENT-2: the tool and the grant for the DynamoDB etf-classifications table (the NAMED NEXT INCREMENT; built on OG-ac-1's census and spec, merged a69cf430b1)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ac-2` | `mdpf_get_security_classification(ticker, as_of="latest")` in a new module: ONE `get_item` by `ticker` on `etf-classifications`, never scan/query/batch/write; refusals before any read; the common envelope with `as_of` from `last_updated`; offline tests (6) and a probe on the real table with the box's own credentials | `app/mdpf_classification.py`, `tests/test_og_ac2.py`, the probe | WORLD | ~113 | `OG-ac-1` merged |
| `OG-ap-25` | APPLY (grant, `0.7.0_AE_CloudOps~ZS`): ONE policy on the gateway role, `dynamodb:GetItem` on the table ARN, nothing else; ask for three halves | `infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf`, the ledger | WORLD | ~AE | `OG-ac-1` merged |

After both: the issuer's hookup (one tool, registry 121 to 122), then the code release (a second release after `OG-ap-23`, applier `0.7.0_AE_CloudOps~Z`) and the catalog's `read_tool` row (`NFRA_MCPINDEX`).
**fanout:** 2 of 2 chains, cap 8 (the tool and the grant share no file and no edge until the release). Outside the 22:00Z line by the CTO ruling @d97ea3ae82 section 2; parallel with `OG-ap-23` (disjoint).

## ADDENDUM R3-T.84 (2.0.0_SA_COO~O, 2026-10-16 ~05:0xZ) -- round 37, workstream ROUND-CLOSE-HYGIENE: three proof instances the round-close check calls PROOF-BAD (read-only `round-close-check.py --round 37`, 04:55Z)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-rc-1` | rename `OG-gf-1`'s proof instance to its order's slug; re-run `OG-cl-7`'s and `OG-cl-8`'s mechanical criteria at the current trunk and record the TRUE AC2 result in their instances (the naming gate now reads `name_rulings.json`); the round-close check lists none of the three | three proof-instance paths | LOCAL | ~111 | `OG-ng-2`, `OG-cl-9`, `OG-cl-10` merged |

The other round-close findings are not this cell's: five judgment criteria (`OG-ap-14/18/19/20/hv-2` AC3) are ungraded (the CVO's L9), and `OG-ap-14` and `OG-hv-2` carry no AC3 acceptance row in their instances (the applier `~Z`/`~ZS` files its row or the CVO grades).
**fanout:** 1 of 1 chains, cap 8. Disjoint from every open cell.

## ADDENDUM R3-T.85 (2.0.0_SA_COO~O, 2026-10-16 ~05:4xZ) -- round 37, workstream NAMING-RELEASE-CLEAN: three lines the commit-time naming gate still refuses in the OG-ap-23 release modules (applier's row NFRA_OPLGTW-Z-S161, msg 34745)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ng-3` | `portal_served.py` types `Scope("mdpf", ...)` twice: derive the label from the bucket as `typed_scope.py` does (no `mdpf` row: a row is global, not per file); one `none_owed` row for `bloomberg_profile` (INSTANCE_PROFILE, an internal audit label at `etfs_silver.py:313`); the full-add gate over all 17 release modules prints no REFUSE | `app/portal_served.py`, one assertion at most in `tests/test_og_gp1.py`, one row in `name_rulings.json` | WORLD | ~111 | `OG-ng-2` merged; `OG-ac-2` hookup merged (the module list includes `mdpf_classification.py`) |

The other 20 + 72 + 1 lines of row Z-S161 are not code cells: the roster and registry copies leave the release commit (the deploy script stages them at bundle time, `OG-ap-23` amendment A2), and the 72 + 1 `scopes.json` / `opal-data-bd` lines were an environment effect of the sparse release tree (`infra/aws/globgrph` missing from its cone), told to `~Z`. `OG-ap-23` now also takes `app/mdpf_classification.py` (the `OG-ac-2` tool; its grant `OG-ap-25` is live before the deploy).
**fanout:** 1 of 1 chains, cap 8. Disjoint from every other open cell. It is an `OG-ap-23` batch cell: the Phase A re-GO names a new `trunk_sha` after its merge.

## ADDENDUM R3-T.86 (2.0.0_SA_COO~O, 2026-10-16 ~06:3xZ) -- round 37, workstream CLASS-INCREMENT-3: the etf-classifications read grant moves to the internal reader role (OG-ap-23 Phase A, gap 2, `~Z` msg 34753)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-26` | APPLY (grant move, `0.7.0_AE_CloudOps~ZS`): the one `dynamodb:GetItem` policy of `OG-ap-25` re-points from `opal-gateway-role` to `gateway-global-internal-reader-role` (a one-for-one replacement, plan `1 to add, 0 to change, 1 to destroy`); the tool reads as the internal reader role, and OG-ap-21 had moved Opal-internal reads OFF the instance role; ask for three halves | `infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf`, the ledger | WORLD | ~AE | `OG-ap-25` complete |

The error is the issuer's (my `OG-ac-2` order preferred the internal reader's client; my `OG-ap-25` order named the instance role). `OG-ap-23` Phase B now waits on `ap26.AC2` PASS. The same Phase A also measured gap 1 (the deploy script writes none of the six vendor reader env keys, so the client tools would stay on the instance role and the CVO's C1/C2 could not be shown); `OG-ap-23` amendment A3 adds the six keys to its deploy hunk.
**fanout:** 1 of 1 chains, cap 8. Disjoint from every worker cell; the release re-cut (A3) runs in parallel on `~Z`.

## ADDENDUM R3-T.87 (2.0.0_SA_COO~O, 2026-10-16 ~07:1xZ) -- round 37, workstream CLIENT-ADMISSION: the five client_* tools are the data-grant class, master_admin only (PRD v3.14 @f2b066d9ad; PRD v3.1 Ruling 2; CVO refusal of the OG-ap-23 half, row Z-S162, relayed by CTO msg 34796)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ad-1` | `client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees` leave `NATIVE_TOOLS` for a new `CLIENT_TOOLS` set that is classified, in `DATA_GRANT_TOOLS` AND in `TIER_ADMITTED_TOOLS` (the model: `blackdiamond_list_fees`); five named tests; the family pin 113 to 108 | `app/data_entitlement.py`, `tests/test_og_ad1.py`, the pin numbers in `tests/test_data_entitlement_family.py` | WORLD | ~113 | none |

The error is the issuer's: my hookups placed the five tools in `NATIVE_TOOLS` by the default pattern, and I signed the COO half of `OG-ap-23` without reading Ruling 2. `OG-ap-23` is re-cut once more on the merged trunk (the CTO's tar-line fix, A5, rides the same re-cut) and its served read gains the negative arm (A6).
**fanout:** 1 of 1 chains, cap 8. Gates the `OG-ap-23` re-cut; the ruling_ref cells and the muse cell stay behind it.

## ADDENDUM R3-T.88 (2.0.0_SA_COO~O, 2026-10-16 ~08:4xZ) -- round 37, workstream RELEASE-GAP-GRANTS: the internal reader role gets the read of the four prefixes the OG-ap-23 served read found denied (applier row Z-S164; CTO ruling msg 34853)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ap-27` | APPLY (grant, `0.7.0_AE_CloudOps~ZS`): two read-only policies on `gateway-global-internal-reader-role` -- `s3:GetObject` and prefix-confined `s3:ListBucket` on `opal-data-etfs` `bbg/`, `snapshots/`, `mdpf/etfs/gold/new_securities/` and `opal-data-mdpf` `mdpf/feeds/model_composition/`, derived from the committed catalog rows (plan `2 to add, 0 to change, 0 to destroy`); ask for three halves, the firm-scoped model-composition row stated plainly | `infra/aws/terraform/opal-gateway/gateway_release_gap_read_iam.tf`, the ledger | WORLD | ~AE | none (re-GO of `OG-ap-23` depends on it) |

The gap is the issuer's: the `OG-ap-23` preflight declared no IAM change and its condition C5 assumed the four tools read prefixes the internal reader already held. C5 fired correctly (rolled back to `d577e0e729`). After `ap27.AC2` PASS the SAME release `3d5c9c8bf1` is re-deployed (CTO: the code halves stand); fallback at 18:00Z is a 23-tool re-cut.
**fanout:** 1 of 1 chains, cap 8. Disjoint from every worker cell; the ruling_ref cells and the muse cell stay behind the `OG-ap-23` close.

## ADDENDUM R3-T.89 (2.0.0_SA_COO~O, 2026-10-16 ~09:4xZ) -- round 37, workstream RULING-REF: every name_rulings.json row carries a resolvable `ruling_ref` (CTO ruling @8b9adcbd8d section 3 cell 1; CVO verdict 6495)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-rr-1` | add `ruling_ref` (`<path>@<commit>`, resolving by `git cat-file -e`) to each of the 136 `name_rulings.json` rows whose ruling record is in the repository; list the rest by `(name, type)` in `W/RULING_REF_UNRESOLVED.json` for the CRO; change no other field | `infra/logic/registry/name_rulings.json` | WORLD | ~115 | `OG-ap-23` closed (done 20261016T092154Z) |

Held since ~07:0xZ so the file did not move under the release commit. `OG-rr-2` (the gate refuses an unresolved `ruling_ref`) follows this cell's merge.
**fanout:** 1 of 1 chains, cap 8. Disjoint from every other open cell; the muse cell stays behind the 22:00Z finish.

## ADDENDUM R3-T.90 (2.0.0_SA_COO~O, 2026-10-16 ~10:2xZ) -- round 37, workstream RULING-REF-GATE: the commit-time naming gate checks `ruling_ref` (CTO ruling @8b9adcbd8d section 3 cell 2, scoped by CTO msg 34906)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-rr-2` | `.tools/naming-gate.py` refuses (a) a present `ruling_ref` that does not resolve (`git cat-file -e <commit>:<path>`) and (b) a `name_rulings.json` row added by the graded commit with no resolving `ruling_ref`; the 111 legacy rows keep today's grade; four self-test arms; full-add re-grade of the 17 release modules moves 0 names | `.tools/naming-gate.py`, `.tools/tests/test_naming_gate_rulings.py` | WORLD | ~116 | `OG-rr-1` merged (ecd2aad5d0) |

The 111 legacy rows are not refused: the CTO ruled (msg 34906) that backfill stays open on the CRO's list rather than moving 111 grades.
**fanout:** 1 of 1 chains, cap 8. Disjoint from every other open cell.

## ADDENDUM R3-T.91 (2.0.0_SA_COO~O, 2026-10-16 ~10:4xZ) -- round 37, workstream ANSWER-BODIES: one projected answer body per named marker, for the CVO's grade of the AC3 judgment criteria of OG-ap-18, ap-19, ap-20, ap-21 and ap-23 (CVO v29 @7f1ada5f4e; CTO relay msg 34905)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-ev-1` | APPLY-SIDE READ (`0.7.0_AE_CloudOps~Z`): re-run the served harnesses against the installed code (live `3d5c9c8bf1`) read-only and write `W/ANSWER_BODIES.json`: one projected answer body per marker the CVO named (ap-18 x3, ap-19 x3, ap-20 x3, ap-21 x3, ap-23 x4), accounts masked, no secrets or names | `deliverables/0.7.0_AE_CloudOps~Z/ANSWER_BODIES.json` | SERVED | ~AE | `OG-ap-23` closed (done) |

The grade is the CVO's judgment on the bodies; the cell only supplies them. `OG-ap-14` and `OG-hv-2` AC3 are NOT MET on acts other seats owe (`OG-mg-1` then the BBGTerminal re-exercise; Andrew's stand-in read and the asset manager's call): no cell here serves them.
**fanout:** 1 of 1 chains, cap 8. Disjoint from every other open cell (`OG-rr-2` runs in parallel on worker `~116`).

## ADDENDUM R3-T.92 (2.0.0_SA_COO~O, 2026-10-16 ~10:5xZ) -- round 37, workstream RULING-REF-CRO: apply the CRO's 110 ruling_refs to the legacy name_rulings.json rows (CRO file msg 34909; CTO msg 34913)

| cell | what | writes | risk | slot | depends on |
|---|---|---|---|---|---|
| `OG-rr-3` | set the CRO's `ruling_ref` string (verbatim, verified by `git cat-file -e`) on the 110 registry rows the CRO file rules; `opal-data-ycharts` (CRO: NOT RULED, the open R21 question) stays without one; change nothing else | `infra/logic/registry/name_rulings.json` | WORLD | ~117 | `OG-rr-1` merged (ecd2aad5d0); the CRO file (done) |

Sequence (CTO msg 34913): this backfill merges first, then `OG-rr-2`'s drain (its worker `~116` builds the gate check in parallel; its AC2 is the full-add re-grade, 0 moved).
**fanout:** 2 of 2 chains, cap 8. `OG-rr-3` writes `name_rulings.json`; `OG-rr-2` writes `.tools/naming-gate.py`: disjoint write sets, one ordering edge at the drain.

## ADDENDUM R3-T.93 (2.0.0_SA_COO~O, 2026-10-16 ~11:4xZ) -- round 38, ONE issuance, workstream ENRICH-R38

**Source.** `1.0.0_SA_CTO~Z`'s round-37 analysis `ledger/ROUND_ANALYSIS.round37.md` @afa8003488 section 3 (E1 to E8), answering the CVO's slug (ADJUDICATION_v31.Z.md). Round 37 is MAY-CLOSE with 7 of 7 judgment criteria graded. Plus one remediation found at the `OG-ng-3` A1 re-seat (`OG-ts-1`).

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-mg-1` (existing) | E1 | Phase B: R1 and R2 writes (all three halves signed 11:1xZ; GO sent 11:15Z; `~Z` reported both written 11:30Z) | SERVED | ~Z | applier |
| (seat act) | E2 | after E1: `0.0.3_BG_BBGTerminal` re-exercises the 8 tools, per tool; DENIED = BLOCKING row naming its gate. Not a task order: the L6 gate refuses an order issued to a Tier-0 seat, so it is a message citing `OG-mg-1` | SERVED | BBGTerminal | seat |
| (COO act) | E3 | the FWD-21 stand-in read: one covered name's pack and chatter through THIS session's gateway MCP (Andrew's own work Claude as the stand-in principal); recorded in the COO deliverables; waits on the MCP reconnecting (429 rate-limited) | SERVED | ~O | COO |
| `OG-en-4` | E4 | client holdings state `weight_unit` and `currency` (+ `currency_basis`) per row, from each adapter's source; test on each adapter's real row | WORLD | ~118 | worker |
| `OG-en-5` | E5 | a `coverage_floor` beside an empty news answer ("no articles in window W, newest article at T") | WORLD | ~119 | worker |
| `OG-en-6` | E6 | harvest chatter states `trading_days_behind_t1` | WORLD | ~120 | worker |
| `OG-en-7` | E7 | the 49F SmartX served read counts candidates whose advisor maps to another firm, with the denominator (expected 0) | SERVED | ~AE | applier |
| `OG-en-8` | E8 | the muse-only narrowed OAuth client (M365 mail and Teams read and send plus `whoami`), inert until `MUSE_CLIENT_ID` is configured | WORLD | ~121 | worker |
| `OG-ts-1` | remediation | the OG-gp-1 and OG-gf-1 classification pins follow the MCPINDEX v2 catalog (two tests red at HEAD; 18 of 32 classified rows absent from the catalog) | WORLD | ~122 | worker |

**Not cells (the CTO's rulings):** the named asset manager's driven call (a person's act, on site Z's open list); Alyssa's `download_filtered` (Z-S173, Andrew's, act row bd68); `OG-rr-2` and the 110-row backfill (already issued and merged in round 37, not recut).
**Release (not yet cut):** E4, E5, E6 and E8 ride ONE batched gateway release (WORLD: the applier cell, the narrowing never-widen ask for E8, the `MUSE_CLIENT_ID` configuration act and the muse served arm); cut after the four builds merge. `OG-ts-1` and `OG-en-7` do not ride it.
**Risk class:** the L6 gate floors any order whose `<paths>` name a gateway infrastructure path at WORLD (spine v3.19 L6); the five worker cells are WORLD by that floor though none deploys.
**fanout:** 5 of 5 worker chains plus 1 applier read, cap 8. Disjoint write sets: `client_*` (`en-4`), `news_typed.py` (`en-5`), `harvest_press.py` (`en-6`), entitlement code (`en-8`), two test files (`ts-1`).

## ADDENDUM R3-T.94 (2.0.0_SA_COO~O, 2026-10-16 ~12:5xZ) -- round 38, workstream ENRICH-R38-B: E9 and E10 added to the round-38 rectangle

**Source.** `1.0.0_SA_CTO~Z`'s update to the round-37 analysis @9dbe9546bc ("add E9 (Z-S175)": a missing key answers not-found, a denied one 403) and the CTO's finding msg 34991 (the gateway's per-identity 429 cuts off the site Z seats; the audit holds no 429 row). A second workstream because the L6 gate keys one issuer to a round and workstream.

| cell | item | what | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-9` | E9 | `gateway_query_catalog`: a key that does not resolve answers 404 (400 if malformed) in words, never `guard_denied`; an entitled-denied key keeps 403; a test of both arms | WORLD | ~123 | worker |
| `OG-en-10` | E10 | the per-identity 429 writes one audit row (limit, window, `count_in_window`, retry), bursts folded, an audit failure never changes the answer; no limit value changes | WORLD | ~124 | worker |

Both are WORLD by the L6 floor (a gateway infrastructure path) though neither deploys; both ride the batched gateway release with E4, E5, E6 and E8. Whether the identity limit is raised, or the site Z seats get distinct identities, is decided after the first 429 audit rows exist.
**fanout:** 2 of 2 chains, cap 8. Disjoint write sets (catalog gate and portal-index tool; ratelimit, server guard, audit).

## ADDENDUM R3-T.95 (2.0.0_SA_COO~O, 2026-10-16 ~13:5xZ) -- round 38, workstream ENRICH-R38-C: the served source of the 49F Black Diamond adapter (CTO msg 35014)

**Source.** The CTO asks that the 49F Black Diamond adapter on `opal-data-bd` (PRD v3.6, Andrew-direct 2026-10-14; G2 item 2) be cut "if not cut". It is already built and live: `OG-cl-2` (complete, merged) wrote `app/client_adapter_bd49f.py` over the live `opal-data-bd/silver/` tables through its own scoped role, `OG-ap-24` (applied) extended `gateway-blackdiamond-read-role`, and both are live in `3d5c9c8bf1`. The CTO's reading that, live, it reads the `opal-data-assets` copy is not contradicted or confirmed by any served record (the OG-ap-23 served read holds no 49F reading). One measuring cell:

| cell | what | risk | slot | class |
|---|---|---|---|---|
| `OG-en-11` | READ (`0.7.0_AE_CloudOps~Z`): the four 49F Black Diamond client tools through the installed code for firm `49financial`; per tool the bucket class of the first source key (`opal-data-bd`, `opal-data-assets`, other, none), the partition date, the role session if readable; a BLOCKING row naming tool, bucket and the cause read from the code path if any tool reads other than `opal-data-bd` | SERVED | ~AE | applier |

**fanout:** 1 of 1 chains, cap 8. A code cell follows only if the measurement shows a different bucket.

## ADDENDUM R3-T.96 (2.0.0_SA_COO~O, 2026-10-16 ~14:0xZ) -- round 38, workstream ENRICH-R38-D: the 49F Black Diamond live tables (CTO rulings @ed33f552ae, @8b2865e461, @96ea4ac3da; rows Z-S292, Z-S293)

**Source.** `OG-en-11`'s served read (BD49F_SERVED.json): the four 49F BD client tools answer `no_catalog_row` and read nothing. The CTO's rulings: the catalog gets four NEW live rows (`opal-data-bd`, `silver/<t>/`, an `address` field, `read_tool`; NFRA_MCPINDEX's half); the code resolves a row by its `address` and reads the row's real prefix in its own bucket (a); the live tables route to a DEDICATED read role (never-widen, three halves), `gateway-49f-blackdiamond-read-role` keeping its Deny; one batched release. MI's measurement (msg 35037): the live files are FLAT dated files (`silver/fees/2026-10-14.parquet`), not `date=YYYY-MM-DD/` folders, so the partition logic must accept both.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-12` | CODE: `Ctx` resolves a row by `address` and reads the real prefix in the row's bucket; `role_key` sends `-live` to `blackdiamond49flive` (env `BLACKDIAMOND49FLIVE_READER_ROLE_ARN`, refuses closed when unset, never a fallback); the partition logic accepts the flat `<date>.parquet` form beside `date=<d>/` | `app/client_core.py`, `app/client_role.py`, the 49F adapter only if needed, tests | WORLD | ~125 | worker |
| `OG-ap-29` | GRANT: ONE new role and ONE policy, read-only on exactly `opal-data-bd/silver/{unrealized,transactions,allocations,fees}/`, trust only the instance role; ask for three halves; applied BEFORE the release | `blackdiamond_live_reader_iam.tf`, the ledger | WORLD | ~ZS | applier |
| (MI's half) | four NEW catalog rows with `address`, `read_tool`, measured freshness; the 8 legacy rows re-bucketed and still OUT | `DATA_CATALOG.yaml` | -- | MI | seat |
| (release) | the ONE batched gateway release: E4, E5, E6, E8, E9, E10 and `OG-en-12`, the catalog edit, the `BLACKDIAMOND49FLIVE_READER_ROLE_ARN` env key in the deploy hunk, `mcportal_commit` `c66ca82952`; then the `OG-en-11` re-run closes Z-S292 | -- | WORLD | ~Z | applier |

**fanout:** 1 of 1 worker chain plus 1 applier, cap 8 (the release cell is cut after the builds, the role and the catalog half are in).

## ADDENDUM R3-T.97 (2.0.0_SA_COO~O, 2026-10-16 ~15:2xZ) -- round 38, workstream ENRICH-R38-E: the ONE batched gateway release (CTO rulings @ed33f552ae, @8b2865e461, @96ea4ac3da, msgs 35000 and 35074)

**Source.** The round-38 builds are merged and each named test passes in the main tree: `OG-en-4`, `OG-en-5`, `OG-en-6`, `OG-en-8`, `OG-en-9`, `OG-en-10`, `OG-en-12`, `OG-ts-1`. The dedicated 49F live role is applied (`OG-ap-29`, ledger CLOSED, `ap29.AC2` PASS). MI's catalog half (`NFRA_MCPINDEX.TO-MX-c-26`) is the one input still outstanding. The CTO ruled (msg 35074) that `NFRA_MCPORTAL.TO-MP-pf-11` (the Indexes box scroll cue) rides this release: `mcportal_commit` moves to `59e802a`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-28` | APPLY: ONE code-only release on the live ref: the named orders' files, the catalog edit, the seventh reader key (`BLACKDIAMOND49FLIVE_READER_ROLE_ARN`, one deploy hunk on the live ref's script), `mcportal_commit` `59e802a`; Phase A re-cut and ask for three halves, Phase B on the GO; then the served read of seven arms | the release tree, `EC2_MANIFEST.json`, the ledger, `W/` | WORLD | ~AE (`~Z`) | applier |

**fanout:** 1 of 1 chains, cap 8 (the release is one act; the builds and the grant it carries are done).

**Where the release is held.** Phase A waits for MI's four live catalog rows on trunk and for origin mcportal DEV to hold `59e802a` (it does). The `OG-en-11` re-run (served 49F reads from `opal-data-bd`) follows the close and answers rows Z-S292 and Z-S293.

## ADDENDUM R3-T.98 (2.0.0_SA_COO~O, 2026-10-16 ~19:2xZ) -- round 39, workstream ENRICH-R39-E5: the round-38 analysis (CTO msg 35210, `ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e); E5 first, alone

**Source.** The CTO's round-38 analysis (the L10 answer to the CVO's slug, msg 35209): round 38 reads MAY-CLOSE, `OG-ap-28` is live (`bf9d23b518`), Z-S292 REMEDIATED, `OG-ap-28` AC3 MET on data dates and firm separation, PARTIAL on units (only holdings carry them). The ENRICHMENT LIST of round 39 is E1 to E6 (below). CTO ruling `@e511fa0194` and the CRO's cause note: `OG-mg-1` Phase B (11:22Z) made the two Opal owner principals restricted, C2 wrote their `email_deny` records, and the email-only browser routes refuse the owners. The defect is the issuer's (row Z-S312).

| cell | content | risk | this issuance |
|---|---|---|---|
| E1 | the 13-month transactions and fees window is answered from ONE daily partition; measure increment vs snapshot on the live tables, then span the partitions or say so; a test plants two partitions | SERVED | follows (ENRICH-R39-B) |
| E2 | `weight_unit` and `currency` on the allocation, transactions and fees answers, from the adapter's source | LOCAL, next release | follows |
| E3 | numbers, not 24-decimal strings or scientific notation; `as_of` from `partition_date` | LOCAL, next release | follows |
| E4 | the email-deny route-class guard (shape a): a restricted profile is refused only on routes that serve restricted data; Alyssa stays refused on today's four routes; a restricted master_admin passes | LOCAL, next release | follows |
| **`OG-ap-30` = E5** | the two-key `email_deny` removal (andrew@ and opalbloomberg@; alyssa@ untouched), three halves, applier `0.7.0_AE_CloudOps~NFRA1`, NOW, not batched | WORLD | **this commit** |
| E6 | `NFRA_MCPINDEX.TO-MX-c-24` (R20-3), named in the next release's ask | SERVED | follows |

**fanout:** 1 of 1 chains, cap 8 (E5 is one applier act). E1 to E4 and E6 are cut in the immediate follow-up issuance under workstream ENRICH-R39-B, because E5 must not wait on their gate dry-runs.

**Pre-checks.** `ap30.AC1`/`AC2` dry-run at the base (FAIL) and on real shapes (PASS arms and controls) before the cut; the live table read: all three `email_deny` records active, count 3.

## ADDENDUM R3-T.99 (2.0.0_SA_COO~O, 2026-10-16 ~19:3xZ) -- round 39, workstream ENRICH-R39-B: E1 to E4 of the round-38 analysis (CTO msg 35210), the rest of the issuance after E5 (R3-T.98)

**Source.** The CTO's round-38 analysis (`ledger/ROUND_ANALYSIS.round38.md` @faa77bd49e) and the CVO's v35 reading of the six live 49F bodies (`ADJUDICATION_v35.Z.md`): AC3 of `OG-ap-28` PARTIAL on units and on the window. This addendum cuts the cells R3-T.98 left for "the follow-up issuance". E6 (`NFRA_MCPINDEX.TO-MX-c-24`) is a take-list item named in the next release's ask, not a cell.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-2` (E1 measure, E2 scale) | MEASURE the live 49F `transactions` and `fees` partitions (increment, snapshot or mixed, by the median consecutive-pair key overlap) and the live `allocations` weight scale (fraction or percent, by per-account sums near 1 or near 100); counts only, no client value printed or committed | `W/E1_PARTITION_MEASURE.json` | SERVED | `~NFRA1` | applier |
| `OG-en-13` (E2 + E3) | `weight_unit` on allocation rows, `currency`/`currency_basis` on transactions and fees rows, figures as JSON numbers at 6 decimals (weights) and 2 (money) with no exponent text, `as_of` from `partition_date`, duplicate profile rows removed | `app/client_adapter_bd49f.py`, tests | WORLD | `~126` | worker |
| `OG-en-15` (E1 code) | transactions and fees read every partition in the window up to a cap of 60 when the measure says `increment` or `mixed`, the newest only when `snapshot`; `partitions_in_window`, `partitions_read`, `window_partial` true only when the cap bites | `app/client_adapter_bd49f.py`, tests | WORLD | `~126` | worker |
| `OG-en-14` (E4) | the email-deny guard takes a route class: a master_admin passes the four internal browser routes, a denied non-admin stays refused (CTO shape a) | `app/data_entitlement.py`, `app/server.py`, tests | WORLD | `~127` | worker |

**Edges.** `OG-ev-2` precedes `OG-en-13` (the allocation weight scale) and `OG-en-15` (the measured partition semantics). `OG-en-13` precedes `OG-en-15` (same file, one worker queue `~126`). `OG-en-14` is independent (`~127`). Spawn: `OG-en-14` now; `OG-en-13` and `OG-en-15` when `E1_PARTITION_MEASURE.json` exists.

**fanout:** 2 of 3 chains, cap 8 (chain 1: `OG-en-13` then `OG-en-15` on `~126`; chain 2: `OG-en-14` on `~127`; chain 3: `OG-ev-2`, the applier's measurement, a seat act). All four orders ride the next batched gateway release, which also takes `MX-c-24` (named in its ask, CTO R20-3) and carries NFRA_MCPINDEX's R20-1 precondition (the catalog regeneration keeps `address`).

**Pre-checks.** Every check dry-run at the base (FAIL as expected): the three named-test files absent, the write bound at 0 files touched, `ev2.AC1` with no record; `ev2.AC1` PASS arms and four control arms FAIL on a synthetic record.

## ADDENDUM R3-T.100 (2.0.0_SA_COO~O, 2026-10-16 ~20:3xZ) -- round 39, workstream ENRICH-R39-R: a repair cell found at the drain

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-16` | tests only: `tests/test_og_en14.py` sets its own `MOCK_GRAPH` before the first import of `app.config`, so `test_ogen14_ac03` passes in the full-suite order (after `test_og_en4.py` and `test_og_en12.py`), not only alone | `tests/test_og_en14.py` | WORLD (gateway path floor) | `~128` | worker |

**fanout:** 1 of 1 chains, cap 8. Source: the issuer's drain re-run of the merged `OG-en-14`, `OG-en-13` and `OG-en-15` (merges `6510ce187f`, `592d79f192`): `test_ogen14_ac03` red in the forward order, green alone and in reverse.

## ADDENDUM R3-T.101 (2.0.0_SA_COO~O, 2026-10-16 ~20:5xZ) -- round 39, workstream ENRICH-R39-C: the second batched gateway release

**Source.** The round-39 builds are merged and each named test passes in the main tree: `OG-en-13` and `OG-en-15` (`592d79f192`), `OG-en-14` (`6510ce187f`), the repair `OG-en-16` (`19db3a905b`; the 40 touched tests together pass in both orders), and `NFRA_MCPINDEX.TO-MX-c-24` (complete @8a01e0b554, CTO R20-3: named in this release's ask).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-31` | APPLY: ONE code-only release on the live ref `bf9d23b518`: the named orders' files, no Terraform, no IAM, no env key, no deploy-script or manifest change; Phase A re-cut and ask for three halves, Phase B on the GO; then the served read of five arms (E1 window, E2 unit and currency, E3 numbers and `as_of`, E4 owner exemption, E6 discover echo) | the release tree, the ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (the release is one act; the builds are done).

**Held, not in this release.** NFRA_MCPINDEX R20-1 (`gen_silver_rows` keeps `address`) gates any catalog regeneration, and this release changes no catalog. The 429 limit choice (OG-en-10 audit rows) is not made here. Allocation `weight_unit` ships `null` with `not_established` (row Z-S313); the question carries to round 40.

## ADDENDUM R3-T.102 (2.0.0_SA_COO~O, 2026-10-16 ~23:0xZ) -- round 40, workstream ENRICH-R40-W1: the 49F window (CTO ruling @0a15d90223; CVO v37)

**Source.** CVO v37 (msg 35285): `OG-ap-31` live, the owner guard condition MET, `OG-ap-28` AC3 MET, `OG-ap-31` AC3 PARTIAL (a 13-month request reads the newest 60 of 334 transaction and 60 of 395 fee partitions, about two months, and `window_partial` says so). The CTO's round-40 ruling W1: measure first on the host, then a concurrent full read if the p95 is inside the request budget, else a continuation cursor; never a silent truncation, never a monthly source (a new pipeline, rule 30 / R19), never narrowing up front. `round-close-check.py --round 39`: MAY-CLOSE (7 orders, 7 complete, `OG-ap-31` AC3 graded).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-3` | MEASURE the full 13-month read of `transactions` (~334 files) and `fees` (~395) on the host through the installed adapter's read path at concurrency 16, 5 runs each: p50, p95, bytes; verdict `inside` if the worst p95 is 30 s or less (half the 60 s ALB idle timeout, the issuer's reading), else `outside` | `W/WINDOW_MEASURE.json` | SERVED | `~NFRA1` | applier |
| `OG-en-17` | CODE: the branch the verdict names: `concurrent` (cap 400, `ThreadPoolExecutor(16)`) or `cursor` (60-partition pages, `next_cursor` = the day before the oldest partition read, passed back as `to_date`); never a silent truncation | `app/client_adapter_bd49f.py`, tests | WORLD | `~129` | worker |

**Edge.** `OG-ev-3` precedes `OG-en-17` (the verdict). **fanout:** 1 of 2 chains started, cap 8 (the measure now; the worker is spawned on its verdict). The change rides the next batched gateway release together with MI's re-emitted catalog (frozen blob `3d47a95791` is stale after `MX-c-24`'s six lines, MI row Z-S136) and `NFRA_MCPINDEX` R20-1.

**Carried, not cells.** The allocation weight scale (Z-S313), the roster for the browser exemption (Z-S322/Z-S325), the 429 limit choice (Z-S177: no 429 rows yet), the owner's browser run for `OG-ap-30`.

## ADDENDUM R3-T.103 (2.0.0_SA_COO~O, 2026-10-17 ~00:0xZ) -- round 40, workstream ENRICH-R40-C: the third batched gateway release

**Source.** `OG-ev-3` closed (the host measurement reads OUTSIDE: transactions one full-window run of 239.9 s, fees p95 147.2 s, threshold 30 s), so `OG-en-17` took the cursor branch and is merged (`4ebc1e781b`; AC1 3 of 3 in the main tree; the round-39/40 test set passes in both orders). `NFRA_MCPINDEX`'s re-emitted catalog (blob `2cbe275d03`, MI's half v2 signed) is on trunk.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-32` | APPLY: ONE code-only release on the live ref `4be300110e`: `OG-en-17` and the catalog taken whole at MI's blob; the two release-tree cures of `Z-S324` as steps; Phase A re-cut and ask for three halves, Phase B on the GO; then the served read of four arms (cursor first page, cursor chain to the window start, newest first, catalog on the host) with the host memory recorded | the release tree, the ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (the release is one act; the builds are done). **Held.** The allocation weight unit (`Z-S313`), the browser-exemption roster (`Z-S322`, `Z-S325`), the 429 limit choice (`Z-S177`: no 429 rows yet), the per-partition prefix listing (`Z-S328`, a `client_core` cell).

## ADDENDUM R3-T.104 (2.0.0_SA_COO~O, 2026-10-17 ~00:2xZ) -- round 40, workstream ENRICH-R40-R: repair of `OG-en-17` before the third release

**Source.** `OG-ap-32` Phase A (`0.7.0_AE_CloudOps~NFRA1`, msg 35302) measured the merged cursor build on the host: a page of 60 partitions holds all of its rows at once (+470 to +550 MB, one page 55 to 59 percent of host memory, two overlapping pages 85 to 100 percent, no swap) and the transactions rate (about 0.72 s per file) puts a first page near 43 s against the 30 s budget. The defect is the issuer's (`OG-en-17`'s cell text kept the full partition lists and set the page at 60); the halves were stopped and release `11031f278d` is superseded.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-18` | REPAIR: each pool task fences and keeps only the requested account's rows (returning the partition row count and the fence exclusions), `PAGE_PARTITIONS` 60 to 30, a process-wide `BoundedSemaphore(1)` around the windowed read with a 15 s wait and a `window_read_busy` answer; tests `test_og_en18.py` | `app/client_adapter_bd49f.py`, `tests/test_og_en18.py`, existing window tests to follow the new truth | WORLD (gateway path floor) | `~130` | worker |

**fanout:** 1 of 1 chains, cap 8 (one file, one cell). `OG-ap-32` gains Amendment A1 (page 30, the semaphore, a new Phase A on the merged `trunk_sha`); the amendment is a wording change to an order with no halves asked, so no gate limb graded it. **Held.** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328` as before.

## ADDENDUM R3-T.105 (2.0.0_SA_COO~O, 2026-10-17 ~02:2xZ) -- round 40, workstream ENRICH-R40-L: landing the AMGT_HARVST release on trunk

**Source.** Row `Z-S336` (BLOCKING, ruled `Z-S337`): `0.7.0_AE_CloudOps~SC1` deployed `319c9413a2` (`AMGT_HARVST` `HVST-cc-7`) from the release line `rel-amgt-harvst-cc7b`, never merged to trunk. The CTO's ruling (msg 35311): `~NFRA1` resolves the landing AFTER `OG-ap-32` Phase B closes, in its own worktree, on a small order the COO cuts; `0.0.0_AB_MSTR~Z` carries the merge to origin after.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-33` | APPLY (repository only): merge `319c9413a2` on the `box/sitez` head; gateway conflicted paths to the bytes live after `OG-ap-32`; the manifest `opal-gateway` block as trunk has it; the six mcportal entries keep both sides; the billing IAM Terraform file keeps both sides only if disjoint and additive, else STOP; a STOP if a resolution would drop an undeployed trunk change | the 18 conflicted paths, `W/` | WORLD (gateway and Terraform path floors) | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (one merge, after `OG-ap-32` closes). Dependency: the `OG-ap-32` ledger CLOSED. **Held.** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`.

## ADDENDUM R3-T.106 (2.0.0_SA_COO~O, 2026-10-17 ~02:5xZ) -- round 40, workstream ENRICH-R40-M: the cursor release rolled back; memory retention and page order

**Source.** `OG-ap-32` Phase B (`0.7.0_AE_CloudOps~NFRA1`, msg 35318): release `b124377b41` deployed 01:53Z; the paging read-back showed host memory 27.8 percent before, 52.4, 58.3, 64.5, 73.3 after pages 1 to 4, peak 87.1 (trigger 85); rolled back at once to `d3ae88be46`; ledger CLOSED; `ap32.AC2` FAIL, arms 1 of 4. Rows `Z-S338` (BLOCKING, ARMED: memory not returned between pages, about 110 to 165 MB per page, cause not isolated) and `Z-S339` (the rows of one page are not ordered by trade date). The OG-en-18 design bound the memory IN a page, not ACROSS pages.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-4` | MEASURE on the host: six variants of the three-page chain in fresh processes (as released; plus gc and the pyarrow pool release; plus `malloc_trim`; `MALLOC_ARENA_MAX=2`; the system pool; 4 workers) with RSS and host percent per page; the flattening variant by a stated rule | `W/` | SERVED | `~AE` (`~NFRA1`) | applier |
| `OG-en-19` | order each window page by trade date, newest first, with a stable sort; tests | `app/client_adapter_bd49f.py`, `tests/test_og_en19.py`, window tests | WORLD (gateway path floor) | `~131` | worker |

**fanout:** 2 of 2 chains, cap 8 (the measure and the sort share no file). `OG-en-20` (the memory repair on the measured variant) and the next release (`OG-ap-34`) are cut on the `OG-ev-4` answer and the `OG-en-19` merge; `OG-ap-33` (landing the HVST line) stays staged until a release is live, because trunk's adapter and catalog are AHEAD of the host. **Held.** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`.

## ADDENDUM R3-T.107 (2.0.0_SA_COO~O, 2026-10-17 ~02:5xZ) -- round 40, workstream ENRICH-R40-N: the memory repair, on the measured cause

**Source.** `OG-ev-4` closed (`~NFRA1`, msg 35320, commit `0b03c0dc57`, `ev4.AC1` PASS): median RSS growth per page, three pages, fresh processes, the release app `b124377b41`: as released 135.9 MB; plus gc and the pyarrow pool release 146.8; plus `malloc_trim` 110.7; `MALLOC_ARENA_MAX=2` 26.7; the system pool 104.5; 4 read workers 42.4; wall time within 20 percent in every variant; flattening variant by the 20 MB rule: none (the lowest is D). Supported cause: glibc per-thread arenas under a new 16-thread pool per page. Row `Z-S342`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-20` | cap the arenas in code (`mallopt(M_ARENA_MAX, 2)` once at import, never raising where libc is absent) and `READ_WORKERS` 16 to 8; tests `test_og_en20.py` | `app/client_adapter_bd49f.py`, `tests/test_og_en20.py`, window tests | WORLD (gateway path floor) | `~132` | worker |

**fanout:** 1 of 1 chains, cap 8 (the file is shared with `OG-en-19`; this cell is spawned when `OG-en-19` is merged). The next release `OG-ap-34` carries `OG-en-17`, `OG-en-18`, `OG-en-19`, `OG-en-20` and the catalog; its Phase A runs the three-page chain on the candidate code on the host and STOPS above 20 MB per page. **Held.** `OG-ap-33`, `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`.

## ADDENDUM R3-T.108 (2.0.0_SA_COO~O, 2026-10-17 ~03:1xZ) -- round 40, workstream ENRICH-R40-G: enforce Andrew's no-download word on alyssa's grant

**Source.** The CTO's ruling on open call `sitez-20261016T111519Z-bd68` (`CTO_RULING_OPLGTW_BD68_ALYSSA_DOWNLOADS_ENFORCE_HIS_WORD_20261017_Z.md` @aed4469fa6, laptop CTO 02:52Z, msg 35321): her live grant holds `download_filtered` (row `Z-S173`, `OG-mg-1` section 3) against Andrew's word of 2026-10-08, "no downloads needed yet"; enforce it with a one-key narrowing under three never-widen halves, usage counts to the CTO first, no seat contacting her or her firm.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-35` | APPLY: before-record and usage counts (counts only); one-key candidate (`operations` minus `download_filtered`) through the admin module's `prepare`; ask for three halves; Phase B on the GO: ledger, `activate` under `opal-gateway-access-admin`, read-back through the installed code (her download refused, one other operation answers), after-record | the grant record (one revision), the ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (one grant write; it shares no file or host with the release work). **Held.** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`.

## ADDENDUM R3-T.109 (2.0.0_SA_COO~O, 2026-10-17 ~03:3xZ) -- round 40, workstream ENRICH-R40-P: the fourth batched gateway release, with a memory gate

**Source.** `OG-en-19` merged (`983095f7af`) and `OG-en-20` merged (`d9364e3e9c`; AC1 2 of 2 and AC3 33 of 33 in both orders, this seat's run), on top of `OG-en-17` and `OG-en-18`. `OG-ap-32` was rolled back at its Phase B (memory 87.1 percent); the host runs the rollback tree `d3ae88be46`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-34` | APPLY: ONE code-only release on the live ref: the code of `OG-en-17` to `OG-en-20` and MI's catalog blob `2cbe275d03`; Phase A re-cut and a MEMORY GATE (the candidate code's four-page chain in a fresh process on the host: median RSS growth 20 MB per page or less, first page 45 s or less, else STOP with no ask); ask for three halves; Phase B on the GO; served read of five arms (cursor first page, chain to the window start, newest first within a page, cursor by partition, memory flat and returned) | the release tree, the ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (the release is one act; the builds are done). Staged behind `OG-ap-35` Phase A (same applier). **Held.** `OG-ap-33` (waits for this release live), `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`.

## ADDENDUM R3-T.110 (2.0.0_SA_COO~O, 2026-10-17 ~07:5xZ) -- round 40, workstream ENRICH-R40-Q: re-landing OG-db-1's preflight on the live deploy script

**Source.** `OG-ap-33` Phase A stopped (row `Z-S356`): the real three-way of the HVST line against trunk has 8 overlapping blocks, 5 of them one move of `harvest_get_published_analysis` (`tools.py`, `destructive_ops.py`: trunk's order, live holds no line trunk lacks) and 3 real overlaps in `deploy-to-ec2.sh` (`OG-db-1`'s preflight vs the live release's `OG-ap-23` staging, the `.env` printf and the tar block). CTO decisions 35436 and 35438: the move is accepted in trunk's order (each name imported, registered and allowlisted exactly once); `deploy-to-ec2.sh` takes the LIVE blob whole; `test_og_en13.py` and `legacy_addresses.json` take trunk's side; the `OG-db-1` preflight is re-landed by a separate cell cut in the same issuance as the `OG-ap-33` amendment; `Z-S356` stays open until it lands.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-db-2` | insert the `OG-db-1` PREFLIGHT block (as trunk carries it at `33fb4d9708`, 17 lines) into the live `deploy-to-ec2.sh` before the `OG-tl-1` allowlist block, nothing else changed; the check runs only the extracted block, never the script | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` | WORLD (gateway path floor) | `~133` | worker |

**fanout:** 1 of 1 chains, cap 8 (a one-file edit that must start from the `OG-ap-33` merge). **Held.** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`, `Z-S328`, `Z-S354`.

## ADDENDUM R3-T.111 (2.0.0_SA_COO~O, 2026-10-17 ~09:4xZ) -- ROUND 41, workstream ENRICH-R41: the enrichment list of the CTO's round-40 analysis, cut in ONE issuance

**Source.** `ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c (the CTO's answer to this seat's slug 35454): no FWD went unserved by a cell; the round-41 enrichment list is four items, thread-breaking first. Each build order carries at most three mechanical criteria.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-21` | item 1 (FIRST, thread-breaking, row Z-S353): `client_get_transactions` and `client_get_fees` run in a worker thread (`anyio.to_thread.run_sync`), so `/health` and every route answer during a 22 to 34 s page and the one-read gate contends in the service | `app/tools.py`, `tests/test_og_en21.py`, window tests | WORLD (gateway path floor) | `~134` | worker |
| `OG-en-22` | item 2 (row Z-S328): `Ctx.partition_keys(prefix)` lists the served prefix ONCE and `read_rows(..., key=...)` skips the per-partition listing; the adapter indexes once per call; a ctx without `partition_keys` runs as before | `app/client_core.py`, `app/client_adapter_bd49f.py`, `tests/test_og_en22.py`, window tests | WORLD | `~135` | worker |
| `OG-db-3` | item 3 (row Z-S354): `deploy-to-ec2.sh` writes the release sha to `/opt/opal-gateway/.deployed_commit` after the extract and before the restart | `deploy-to-ec2.sh`, `tests/test_og_db3.py` | WORLD | `~136` | worker |
| `OG-ev-5` | item 4 (row Z-S355): a READ-ONLY trace of the near-empty fees stretch: is the SOURCE thin there or the ACCOUNT; verdict by a 25 percent rule from counts; no tool change in this round | `W/` | SERVED | `~AE` (`~NFRA1`) | applier |

**fanout:** 4 of 4 chains, cap 8: the write sets are disjoint (`tools.py`; `client_core.py` plus the adapter; `deploy-to-ec2.sh`; a read-only trace). The batched release that carries items 1 to 3 (`OG-ap-36`, with its own never-widen, its Phase A page-wall measurement before and after item 2, a health probe during a page chain, and a marker read on the host) is cut after the three builds merge. **Carried, no cell** (the CTO's list): `Z-S313`, `Z-S177`, `Z-S322`/`Z-S325` (cut only with a named principal list), `Z-S338` (the organic case, never an impersonated call), `Z-W94-S2` (producer: dell2 `IRPT_BCKEND` IB-hm-5; the reader grant is the laptop CTO's).

## ADDENDUM R3-T.112 (2.0.0_SA_COO~O, 2026-10-17 ~10:5xZ) -- ROUND 41, workstream ENRICH-R41-P: the fifth batched gateway release (items 1 to 3), cut on the real merged diff

**Source.** `OG-en-21`, `OG-en-22`, `OG-db-3` (and `OG-db-2`) are merged on trunk (`1d3234ae24`, `a866c7c78c`, `8d2241ef81`). The design note `DRAFT_NOT_ISSUED_TO-OG-ap-36_round41_batched_release.md` waited for the real diff; the real diff of trunk against the live ref `9d5b712557` holds four files this release takes (`app/tools.py`: `OG-en-21` plus the position move of `harvest_get_published_analysis` that `OG-ap-33` landed on trunk; `app/client_core.py` and `app/client_adapter_bd49f.py`: `OG-en-22`; `deploy-to-ec2.sh`: `OG-db-2` preflight and `OG-db-3` marker) and three new test files, and other seats' files (`destructive_ops.py`, `family_depth.py`, the partner roster, `silver_families.json`, other tests) that belong to no order of this release and stay out. Items 1 to 3 of the CTO's round-40 analysis ship in a batched release under their own never-widen.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-36` | the release: Phase A re-cut on the live ref with the take list above (each file byte-equal to trunk's blob), the memory gate and plateau test on the host, the first-page wall of the live code and of the candidate on the same window (candidate shorter), pages equal live row for row, `/health` under 1 s during a page, the ask for three halves; Phase B on the three halves' GO: deploy, the host marker equals the release sha, eight served arms, the 30-minute read-back with the `/mcp` window-call count stated | `W/`, the ledger, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (the release is one act on one host; the builds are done). Staged: the GO for Phase A is the issuer's message citing this order and naming `trunk_sha`. **Not in this release (the check counts them at 0):** `destructive_ops.py`, the harvest files, the catalog, `EC2_MANIFEST.json` (the deploy wrapper writes it at the close), Terraform, the registry files unless the naming gate needs a prelude. **Carried, no cell:** `Z-S313`, `Z-S322`/`Z-S325`, `Z-S177`, `Z-W94-S2`; `Z-S338` is re-read on this release's deploy.

## ADDENDUM R3-T.113 (2.0.0_SA_COO~O, 2026-10-17 ~11:3xZ) -- ROUND 41, workstream ENRICH-R41-Q: the repair of the OG-ap-36 Phase A stop (row Z-S370)

**Source.** `OG-ap-36` Phase A stopped on two host measurements (msg 35467, row `Z-S370`, `MEM_GATE_OG-ap-36.json`): (e) with the page off the event loop by `OG-en-21` the loop is still starved 1 to 3.9 s at a time (limit 1 s; the live code held it 29.8 s), and (a) the four-page chain grows 27.7 MB per page at the median (limit 20; the live code 18.3 in the same run, a median of three sawtooth differences). Passing: the plateau (+34.5 MB), the first page (20.8 s against 29.7 s live) and row-for-row equality. The cause the issuer reads in the code, INFERRED and to be measured by the applier's re-run: `typed_scope.read_parquet` converts the WHOLE partition (`to_pylist`, `json.dumps`, `json.loads`: three GIL-holding passes over every account's rows) and `_read_partitions` filters to the one account afterwards (`client_adapter_bd49f.py:341-348`).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-23` | `Ctx.read_account_rows(...)` applies the 49F fence and the account test IN ARROW and converts only the account's rows; returns the same `(kept, total, excluded)` the old path derives (the two denominators kept exactly); the adapter uses it when the ctx has it; a non-string id column takes the old path | `app/client_core.py`, `app/client_adapter_bd49f.py`, `tests/test_og_en23.py`, window tests | WORLD (gateway path floor) | `~137` | worker |

**fanout:** 1 of 1 chains, cap 8 (one repair; it edits the two files of `OG-en-22`, so it cannot run beside another cell). **Amendment A1 to `OG-ap-36` (same commit):** Phase A is RE-RUN after `OG-en-23` merges, on the new `trunk_sha` (the take list gains `tests/test_og_en23.py`; `client_core.py` and the adapter are already in it); the criteria stay (the 1 s health limit and the 20 MB median growth are NOT relaxed); to remove the noise the first run showed (a median of THREE differences, one chain per code), the memory chain is SIX pages (a median of five) and the live code's chain is read the same way in the same run. **Not changed:** the 1 s limit, the 20 MB limit, the plateau test, the equality test. **Held:** `Z-S313`, `Z-S322`, `Z-S325`, `Z-S177`.

## ADDENDUM R3-T.114 (2.0.0_SA_COO~O, 2026-10-17 ~13:3xZ) -- ROUND 41, workstream ENRICH-R41-R: keep the adapter's absent_reason (row Z-S372, the CVO's row Z-S373)

**Source.** The `OG-ap-36` Phase A addendum (msg 35482, row `Z-S372`) read the CTO's CT1: under a 0.5 s gate wait the second concurrent call is refused with empty rows and `absent_reason` null, so `window_read_busy` is not surfaced. Cause read in the code: `client_core._answer` sets `"absent_reason": meta["_absent_reason"]`, which is None for the 49F adapter (its `_absent` writes `absent_reason` without an underscore), overwriting the adapter's code. The CVO's row `Z-S373`: the same line nulls the five `no_partition_at_as_of` refusals of the live release. CTO decisions 35485, 35489, 35492: cut the mapping now, general, on trunk, with a test per case; re-run proportionately (the window tests and CT1; no memory gate; a fresh ask; the halves re-sign).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-24` | `_answer` keeps the adapter's `absent_reason` whenever `_absent_reason` is None (one line); tests: a refused second call carries `window_read_busy` (transactions and fees), the line changes nothing else, and each of the five tools' `no_partition_at_as_of` read carries that reason | `app/client_core.py`, `tests/test_og_en24.py`, window tests | WORLD (gateway path floor) | `~138` | worker |

**fanout:** 1 of 1 chains, cap 8 (one line and its tests; the release waits on it). **Amendment A3 to `OG-ap-36` (same commit):** the release takes `client_core.py` and `tests/test_og_en24.py` from the new trunk (nine files), `measured_release_sha` carries the memory record's release, `ap36.AC1` checks the delta, CT1 is repeated, the ask is re-drafted, the halves re-sign. **Not changed:** every limit.

## ADDENDUM R3-T.115 (2.0.0_SA_COO~O, 2026-10-17 ~15:4xZ) -- ROUND 41, workstream ENRICH-R41-S: land dell1's gateway release 1753c741d9 on the sitez trunk (CTO decision 35516)

**Source.** dell1 `2.0.0_SA_COO~W1` deployed `1753c741d9` (`AMGT_HARVST` `HVST-cd-2`: `harvest_research.py` and one test, disjoint from `OG-ap-36`) at 15:01Z; ledger CLOSED 15:08:06Z; the host owner's order swap (CTO 35508) put it ahead of `OG-ap-36`. CTO 35516: landing it on sitez's lineage is an order cut for `~NFRA1`, as for `319c`; its one conflict, `client_adapter_bd49f.py`, is lineage only (trunk's side taken). Measured at the cut: the two released files are already byte-equal on trunk; the manifest commit `25699bc8e5` is already an ancestor of `box/sitez` (the box pass took CLOUD @b86bda10ec); the merge-tree of trunk and `1753c741d9` has one conflicted path.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-37` | merge dell1's release commit into a branch on `box/sitez` with trunk's side on `client_adapter_bd49f.py`; no gateway, Terraform or other byte changes; the manifest block still names `1753c741d9` (previous `9d5b712557`) | the merge commit, `W/ap37_landing.json`, ledger folders | WORLD (gateway path floor) | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (a repository merge; it moves the trunk head, so it runs after the `OG-ap-36` re-cut report). Not on the `OG-ap-36` critical path. **Not changed:** every limit.

## ADDENDUM R3-T.116 (2.0.0_SA_COO~O, 2026-10-17 ~18:0xZ) -- ROUND 41, workstream ENRICH-R41-T: the repair of the ARMED hazard Z-S375 (CTO decision 35541)

**Source.** `OG-ap-36` Phase B (msg 35538): the applier's unguarded 27-tool harness took the 1.8 GB host out of memory at 17:21Z through `etfs_compare_peers` (byte-equal on both refs; not this release's widening): the gateway was killed once (back in 3 s) and eight system daemons (restored; `chronyd` unsynchronised until it polls). Row `Z-S375` ARMED (disarm owner this seat); any caller can still trigger it. CTO decision 35541: the served read grades 26 of 27 with the row open; no probe on the live host; this seat cuts the fix cells now: bound `etfs_compare_peers`'s memory or refuse above a size, proven in a fresh process, plus a `MemoryMax` on the gateway unit; each ships under its own never-widen. Cause (code reading, INFERRED, the host measures it in the release's Phase A under a hard guard): `typed_scope.read_parquet` converts a whole table to Python after only a COMPRESSED-size cap, and `_peer_section` reads the gold peer tables unfiltered and filters in Python (the class `OG-en-23` fixed for the 49F window).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-25` | `typed_scope.read_parquet` refuses a FILTERED table over an in-memory cap before any Python conversion (protects every typed reader); `etfs_compare_peers` reads its peer tables with Arrow filters and takes the available values from an Arrow `unique`; identical answers for valid inputs; a fresh-process test holds the heap bound on the call that ran away | `app/typed_scope.py`, `app/etfs_rivals_flow.py`, `tests/test_og_en25.py`, peer and window tests | WORLD (gateway path floor) | `~139` | worker |
| `OG-un-1` | `deploy/opal-gateway.service` gains `MemoryHigh=1200M`, `MemoryMax=1400M`, `OOMScoreAdjust=300` and nothing else changes; the deploy already installs the unit and restarts it | `deploy/opal-gateway.service`, `tests/test_og_un1.py` | WORLD | `~140` | worker |

**fanout:** 2 of 2 chains, cap 8 (the write sets are disjoint: Python and tests; a unit file and its test). **Not in this issuance:** their release (a later order with its own never-widen), the owner of `etfs_rivals_flow` (the hazard is routed by this cell, not left to it), other whole-table readers beyond the new central cap.

## ADDENDUM R3-T.117 (2.0.0_SA_COO~O, 2026-10-17 ~19:3xZ) -- ROUND 41, workstream ENRICH-R41-V: the release of the Z-S375 repair (OG-en-25 and OG-un-1)

**Source.** `OG-en-25` (typed Parquet in-memory cap, `etfs_compare_peers` Arrow filters; drained `a197c3fc38`) and `OG-un-1` (memory cap on the gateway unit; drained `a6788723f3`) are merged and verified (ruling rows `Z-S376`, `Z-S377`). The ARMED hazard `Z-S375` (any caller can take the 1.8 GB host out of memory through `etfs_compare_peers`) is repaired only when they are LIVE and measured on the host UNDER A HARD GUARD (the applier's unguarded harness caused the 17:21Z OOM). CTO decision 35541: each ships under its own never-widen.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-38` | the sixth batched release (five files: `typed_scope.py`, `etfs_rivals_flow.py`, `deploy/opal-gateway.service`, two tests) on the live ref `efcc8ae19f`: Phase A on the host under the guard (the call that ran away bounded, a valid pair, the 49F chain unchanged, the unit acceptable to systemd), the ask for three halves, Phase B (deploy, the 27-tool read 27 of 27 under the guard, the unit limits live, the clock and failed units read BEFORE the ledger closes) | `W/`, the ledger, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (one release on one host; the builds are merged). Staged behind `OG-ap-37` (the same applier; a repository merge) and its GO naming `trunk_sha`. One ask carrying both changes, each stated with its own widening (a reading of the CTO's "each under its own never-widen", named to the CTO). **Held:** `Z-S338` (organic window call), `Z-S177`, `Z-W94-S2`, `Z-S313`, `Z-S322`/`Z-S325`.

## ADDENDUM R3-T.118 (2.0.0_SA_COO~O, 2026-10-17 ~20:3xZ) -- ROUND 41, workstream ENRICH-R41-W: the repair of the OG-ap-38 Phase A stop (row Z-S380)

**Source.** `OG-ap-38` Phase A STOPPED on measurement (a) (applier msg 35555, row `Z-S380`): under the hard guard the candidate `etfs_compare_peers` raised MemoryError inside `pyarrow.parquet.read_table` at a 724 MB peak (limit 700; the live code 927 MB). Cause the issuer reads in the code (INFERRED; the applier's re-run measures it): `typed_scope.read_parquet` reads the WHOLE object before it filters, with no column projection for the peer tables, and the `OG-en-25` in-memory cap runs after that read; the peer tables' lineage column `input_manifest` (up to about 100 KB a row, replaced in the answer by its byte count) is the bulk. Also measured: pyarrow cannot start its thread pools under `RLIMIT_AS`, so the chain needs a cgroup guard.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-26` | a filtered `read_parquet` STREAMS by batch (`iter_batches`, 2048 rows, one thread) and keeps only matched rows; an unfiltered read is refused from the file metadata BEFORE it reads; a new `length_columns` returns the lineage column's byte count for the matched rows without loading its values; `distinct_values` streams; `etfs_compare_peers`'s answer is identical | `app/typed_scope.py`, `app/etfs_rivals_flow.py`, `tests/test_og_en26.py`, peer and window tests | WORLD (gateway path floor) | `~141` | worker |

**fanout:** 1 of 1 chains, cap 8 (it edits the two files of `OG-en-25`; the release waits on it). **Amendment A1 to `OG-ap-38` (same commit):** the guard may be a cgroup limit (`systemd-run --scope -p MemoryMax=1400M -p OOMScoreAdjust=1000`) as well as the address-space cap; Phase A is RE-RUN on the new `trunk_sha`; the limits are NOT relaxed. **Held:** `Z-S375` (ARMED until `OG-ap-38` is live and measured), `Z-S338`, `Z-S177`, `Z-W94-S2`.

## ADDENDUM R3-T.119 (2.0.0_SA_COO~O, 2026-10-18 ~01:0xZ) -- ROUND 42, workstream ENRICH-R42-A: the CTO's round-41 analysis (`ledger/ROUND_ANALYSIS.round41.md`, msgs 35583 and 35584)

**Source.** The round-41 analysis cuts three items and, after the CRO's research, rules the through-the-service probe (slug item 8) as option A: (1) the window page size chosen from a measured sweep; (2) `test_ogdb3_ac03` reads the worktree; (3) the `absent_reason` codes documented; and cells 4 and 5, a read-only SSRF audit of the outbound call sites and the loopback probe listener. `Z-S375` disarms on `etfs_compare_peers` answering THROUGH the listener (service heap and `NRestarts` printed); `Z-S338` closes on a full window chain through it with the service heap flat.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-6` | the window page size measured on the host at 30, 60 and 120 partitions, three fresh guarded runs each, graded by a rule fixed before any run (page time under 15 s, median growth 20 MB or less, host peak under 75, the same rows over the newest 120 partitions); `W/PAGE_SWEEP.json` names `chosen_partitions` | `W/` | WORLD (gateway code on the host) | `~AE` (`~NFRA1`) | applier |
| `OG-en-29` | `PAGE_PARTITIONS` set to the chosen size, the tests that pin 30 followed, two new tests (a full page at the new size; the same rows at 30 and at the new size) | `app/client_adapter_bd49f.py`, window tests | WORLD (gateway path floor) | `~144` | worker |
| `OG-en-27` | `test_ogdb3_ac03` reads the worktree, not git history, so it passes in a release tree | `tests/test_og_db3.py` | WORLD (gateway path floor) | `~142` | worker |
| `OG-en-28` | the `absent_reason` codes (the adapter's and the core's refusals a client tool can return) documented in the `client_*` docstrings, one line each; no line moves in `tools.py` (the catalog cites it by line) | `app/tools.py` (docstring lines), `W/ABSENT_CODES.json` | WORLD (gateway path floor) | `~143` | worker |
| `OG-sec-1` | a read-only audit of the 18 outbound-HTTP call sites in `identity.py`, `graph.py`, `ycharts/client.py`, `globgrph/integration.py`, `opal_portal/integration.py` for a caller-controlled target; any `yes` is a STOP on `OG-pr-1` | `W/` | LOCAL | `~145` | worker |
| `OG-pr-1` | the loopback probe listener: a second listener inside the same process on `127.0.0.1`, off by default, armed by an SSM lease of 60 minutes or less that expires closed, exactly two tools for one fixed probe principal and the test account, the audit label `probe:<order>`, a `SIGUSR2` heap line; one arm/call/expiry test | `app/probe_listener.py`, `app/server.py` (lifespan hookup), `tests/test_og_pr1.py` | WORLD (gateway path floor) | `~146` | worker || `OG-ap-39` | the seventh batched release (the page size, the db3 test, the codes documented) under its own never-widen: Phase A five fresh chain runs at the new size by the rule stated before them, the 27-tool read live against candidate; Phase B the 27 of 27 under the guard, the clock read before the ledger closes, `NRestarts` 0 | `W/`, the ledger, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |
| `OG-ap-40` | the eighth batched release (the listener) under its own never-widen: the arming, `etfs_compare_peers` and a window chain through the listener with the service heap read before and after, the disarm and an expired lease refused; staged behind `OG-sec-1` CLEAN and `OG-pr-1` | `W/`, the ledger, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 3 of 4 chains, cap 8 (the chain heads are `OG-en-27`, `OG-en-28`, `OG-sec-1` and `OG-ev-6`; spawn now: `OG-en-27`, `OG-en-28`, `OG-sec-1`; `OG-ev-6` is the applier's, on a GO naming `trunk_sha`; `OG-en-29` follows `OG-ev-6`, `OG-pr-1` follows `OG-sec-1` CLEAN; `OG-ap-39` joins the first three, `OG-ap-40` the last). **Held:** `Z-S375`, `Z-S338` (disarm only through the listener), `Z-S177`, `Z-W94-S2`, `Z-S313`, `Z-S322`/`Z-S325`, `Z-S369`. Slug item 6 (`safe-merge.sh --lineage-only`) is `0.0.0_AB_MSTR`'s tool; no gateway cell.

**R3-T.119 amendment A3 (2.0.0_SA_COO~O, round 42, ~03:0xZ, no CTO ruling needed: the issuer amends its own decomposition's order).** `OG-ev-6` (the sweep) chose 30 partitions per page, so `OG-en-29` is SUPERSEDED (nothing to build) and `OG-ap-39` carries two files (`app/tools.py`, `tests/test_og_db3.py`). `OG-pr-1` was re-seated as `~147` for a repair found in the issuer's review (the lease read blocking the shared event loop). Gate limb: none graded (a modified order that declares no placeholder change).

**R3-T.119 amendment A4 (2.0.0_SA_COO~O, round 42, ~03:3xZ, workstream ENRICH-R42-B): a repair cell `OG-pr-2`.** The issuer's review of the merged probe listener (`OG-pr-1`, built by `~146`, lease read repaired by `~147`) found two defects in `app/probe_listener.py`: the audit write runs inline on the shared event loop (worker row `Z-W147-S1`) and a refusal is answered before the request body is read (a flaky connection reset in `test_ogpr1_ac02`). `OG-pr-2` repairs both with two new tests; worker `~148`; `OG-pr-1` is closed as superseded by it (the status gate graded the old proof instances against the amended criteria: row `Z-W147-S2`). `OG-ap-40` stays staged behind `OG-pr-2`. Gate limb: the new tree order is graded by `to-pipeline-gate`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pr-2` | the probe listener's audit write goes through the threadpool; every refusal reads the request body first (bounded at 65536 bytes); tests `ac07` (40 refused calls answer cleanly, twice) and `ac08` (the audit write is off the loop) | `app/probe_listener.py`, `tests/test_og_pr1.py` | WORLD (gateway path floor) | `~148` | worker |

**fanout:** 1 of 1 chains, cap 8 (one repair on the merged state).

**R3-T.119 amendment A5 (2.0.0_SA_COO~O, round 42, ~04:0xZ, workstream ENRICH-R42-C): a repair cell `OG-pr-3`.** The second repair worker's row `Z-W148-S1`: the body-first read of `OG-pr-2` buffers the whole request body (`await request.body()`) before its 65536-byte check, so the check bounds the answer and not the read; the listener runs unarmed and shares the gateway heap. `OG-pr-3` streams the body with a byte count (and refuses a declared `Content-Length` over the cap unread), with tests `ac09` (the read is bounded) and `ac10` (a body at the limit is served, one byte over refused); worker `~149`; spawn after `OG-pr-2` has drained. `OG-ap-40` waits on it. Gate limb: the new tree order is graded by `to-pipeline-gate`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pr-3` | the probe listener streams the request body with a byte count, stops reading past 65536 and refuses a declared over-length body unread | `app/probe_listener.py`, `tests/test_og_pr1.py` | WORLD (gateway path floor) | `~149` | worker |

**fanout:** 1 of 1 chains, cap 8 (one repair on the state `OG-pr-2` leaves).

**R3-T.119 amendment A6 (2.0.0_SA_COO~O, round 42, ~04:3xZ, workstream ENRICH-R42-D): a wording cell `OG-en-30`.** The CVO's half for `OG-ap-39` (SIGNED at ask `942adaf1e59e`) carries row `Z-S385`: the `client_get_fees` note written by `OG-en-28` tells a calling model that an empty fee list is "a true zero ... report zero" while the source's completeness for the window is unmeasured (`Z-S355`/`Z-S368`/`Z-S369`). The issuer rules it before the release rather than after: `OG-en-30` rewords the note to say what was measured (no fee row in the source; no total established) and audits the eleven other notes for the same class; docstring text only, line count held at 1896; worker `~150`. `OG-ap-39` is re-cut after it drains (amendment A4 of that order). Gate limb: the new tree order is graded by `to-pipeline-gate`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-en-30` | the `no_fee_rows_in_window` note says "no fee row in the source; no total established" instead of "a true zero, report zero"; the other eleven notes audited for claims the code does not establish | `app/tools.py` (docstring text) | WORLD (gateway path floor) | `~150` | worker |

**fanout:** 1 of 1 chains, cap 8 (one wording cell; the release `OG-ap-39` re-cut waits on it).

**R3-T.119 amendment A7 (2.0.0_SA_COO~O, round 42, ~05:5xZ, workstream ENRICH-R42-E): a lineage cell `OG-ap-41`.** dell1's CTO (its msg 7926, via `0.0.0_AB_MSTR~Z` msgs 35629/35630) rules that site Z lands its gateway release commits `efcc8ae19f` (`OG-ap-36` A4) and `d077cef043` (`OG-ap-38` A1) on its own lineage first and resolves its own conflicts (`app/tools.py`, `tests/test_og_db3.py`, as MSTR measured), then dell1's `cg-3` (`4257a2aa42`) merges on top; the CTO (msg 35632) adds that `OG-ap-39`'s release commit is taken by the same cell after its Phase B, and the criterion that `app/` be AST-equal to the live release plus trunk's own changes, listed, with the window tests passing. `OG-ap-41` is the repository merge for `~NFRA1` (the shape of `OG-ap-37`): trunk's side on every conflicted gateway path, no gateway byte changed, `ap41.AC1` to `AC4`. Part 2 (the `OG-ap-39` release commit) follows its Phase B as an amendment. Gate limb: the new tree order is graded by `to-pipeline-gate`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-41` | merge `d077cef043` (which carries `efcc8ae19f`) onto the `box/sitez` head in the applier's worktree, trunk's side on the two conflicted gateway paths, the manifest block untouched; the record lists trunk's own changes against the live release | `W/`, the merge on a landing branch (drained by the issuer) | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (a repository merge; independent of `OG-ap-39`, whose release is cut on its own branch).

## ADDENDUM R3-T.120 (2.0.0_SA_COO~O, 2026-10-18 ~12:3xZ) -- ROUND 43, workstream ENRICH-R43-A: the CTO's round-42 analysis (`ledger/ROUND_ANALYSIS.round42.md` @664109af96, msg 35681), cut in ONE issuance

**Source.** The round-42 analysis (endpoint unchanged; round 43 hardens the instrument that made the through-the-service read, and lands trunk) cuts nine cells. Standing condition for every round-43 release: the base is the live ref at the GO (`6575999df5`, dell1's harvest release deployed 2026-10-18 10:52:49Z, parent `3b94a83e05`), each release carries dell1's four harvest files unchanged with their blobs named in the ask, and the ask's diff lists every path that differs from live and takes only its own. No arming happens until the firm pin ships.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pr-4` | the probe lease carries `firm`; a mismatched `firm` is refused 403 `probe_firm_refused` BEFORE the tool runs; a lease without `firm` is malformed; tests `ac11`, `ac12` | `app/probe_listener.py`, `tests/test_og_pr1.py` | WORLD (gateway path floor) | `~151` | worker |
| `OG-en-31` | `test_ogpr1_ac13`: every refusal within the bound has pulled the WHOLE request body before `http.response.start` (the property the connection reset depends on, asserted at the ASGI boundary); a mutant check (`en31.AC3.sh`) shows it fails when a refusal precedes the read | `tests/test_og_pr1.py` | WORLD (gateway path floor) | `~151` (second order, after `OG-pr-4`) | worker |
| `OG-sec-2` | `graph.call` refuses an absolute URL whose scheme is not https, whose host is not exactly `graph.microsoft.com`, with user-info or a port other than 443, before any client is built; tests `ac01`, `ac02` | `app/graph.py`, `tests/test_og_sec2.py` | WORLD (gateway path floor) | `~152` | worker |
| `OG-sec-3` | the SSRF audit completed over SIX modules with `PyJWKClient(` added (21 sites, not 20: `token_broker.py:307` is outside the five modules of round 42); any `yes` is a STOP | `W/` | LOCAL | `~153` | worker |
| `OG-ev-8` | read-only table of the 81 inline audit-write sites (the slug's 82 under a different pattern): on the event loop or not, calls over 7 days (or ABSENT with its reason), timeout; the repair is a round-44 decision | `W/` | LOCAL | `~154` | worker |
| `OG-ev-9` | read-only trace of the per-identity limiter (`Z-S177`): limit and window as read from `config.py`, keying, `Retry-After`, the identities hitting it in 24 hours by hash (or ABSENT), the reconnect arithmetic, a recommendation; no change | `W/` | LOCAL | `~155` | worker |
| `OG-ap-42` | the ninth batched release (`OG-pr-4`, `OG-en-31`, `OG-sec-2`; four files) on the live ref read on the host, under its own never-widen; Phase A on the host under the hard guard, Phase B unarmed only (`armings` 0) | `W/`, the ledger `batch10`, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |
| `OG-ev-7` | the peers call measured in the running service under ONE 25-minute lease that pins the firm: three calls (heap signal on, on, off) and one fresh-process call, verdict by a rule fixed before the run (`COLD`, `SLOW_IN_SERVICE`, `SIGNAL_COST`, `INCONCLUSIVE`); its own three-half ask; staged behind `OG-ap-42` CLOSED | `W/` | WORLD | `~AE` (`~NFRA1`) | applier |
| `OG-ap-43` | the merge of the newest live release (`6575999df5` today; it carries `3b94a83e05`) onto the `box/sitez` head in the shape of `OG-ap-41`: trunk's side on conflicts except dell1's own harvest paths (dell1's blob); `ap43.AC3` lists every path that differs from live, each marked site-Z-own or dell1-own | `W/`, the merge on a landing branch (drained by the issuer) | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 5 workers of 6 chains, cap 8 (workers `~151` to `~155`; the chain heads are `OG-pr-4` (then `OG-en-31`, then `OG-ap-42` and `OG-ev-7`), `OG-sec-2`, `OG-sec-3`, `OG-ev-8`, `OG-ev-9` and the landing `OG-ap-43`, which is the applier's). Spawn now: `OG-pr-4`, `OG-sec-2`, `OG-sec-3`, `OG-ev-8`, `OG-ev-9`; `OG-en-31` follows `OG-pr-4` on the same slot (same file); `OG-ap-42` joins `OG-pr-4`/`OG-en-31`, `OG-sec-2` and `OG-sec-3`; `OG-ev-7` follows `OG-ap-42` CLOSED; `OG-ap-43` waits on a GO naming `trunk_base_sha`, `dell_sha` and the manifest commit.

**Readings disclosed to the CTO (each can be corrected before the asks).** (1) "the listener refuses any call whose account does not resolve to that firm": read as the call's `firm` argument equalling the lease's firm, because the account reference carries no firm. (2) "plus the login host the token flow already uses" (Graph pin): not applied inside `graph.call`, which never calls the login host. (3) The SSRF denominator is 21 over the six modules, not 20 over five: `PyJWKClient(` also matches `token_broker.py:307`. (4) The audit-write sites count 81 under `\baudit\.[A-Za-z_]+\(|\b_emit\(` (the slug said 82). (5) On a conflict in the landing, dell1's own harvest paths take DELL1's side. (6) The measured set of trunk's own changes against live `6575999df5` is `admin_people_access.py`, `destructive_ops.py`, `family_depth.py` (a synthetic merge at the cut; `ap43.AC3` lists the real ones at the GO).

**Held / carried.** `Z-S177` (traced by `OG-ev-9`), `Z-W94-S2`, `Z-S313`, `Z-S322`/`Z-S325` (as the analysis). `Z-S375` and `Z-S338` are ruled disarmed in my row `Z-S388`; the CVO writes the DISARMED remediation rows. Slug item 6 (the proof-instance gate: grade only the newest instance of an order?) is `0.0.0_AB_MSTR`'s gate, routed by the CTO; slug item 9 stays with the laptop CTO's fees probe (`Z-S368`/`Z-S369`).

**R3-T.120 amendment A1 (2.0.0_SA_COO~O, round 43, ~17:4xZ, workstreams ENRICH-R43-B and ENRICH-R43-C): two cells for the access-log regression `Z-S395` (CTO ruling, msg 35769).** `~NFRA1` measured (its msgs 35766 and 35767) that since the `OG-ap-40` deploy the gateway service's own `POST /mcp` access lines are absent from the journal (157 to 171 per 30 minutes before, 0 after) while the audit lake shows traffic continuing: `probe_listener.make_server` builds a `uvicorn.Config`, whose constructor configures the PROCESS-WIDE `uvicorn` loggers (the default `LOGGING_CONFIG`, the levels of `uvicorn.error`/`uvicorn.access`/`uvicorn.asgi` set to the Config's `warning`, and for `access_log=False` the `uvicorn.access` handlers emptied and `propagate` off). The CTO ruled: cut a repair cell in round 43, ship it in a batched release under its own never-widen, ahead of `OG-ev-7`. The mid-round spec stays frozen except for this ruled surprise row; the issuer cuts it as two new workstreams (the gate allows one issuance per workstream).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-pr-5` | `make_server` snapshots the four process-wide `uvicorn` loggers (level, handlers, propagate, disabled, filters) before building its Config and restores them in a `finally` (also when the constructor raises); the listener's own `access_log=False` stays; tests `ogpr5_ac01` to `ac03` | `app/probe_listener.py`, `tests/test_og_pr5.py` | WORLD (gateway path floor) | `~156` | worker |
| `OG-ap-44` | the tenth batched release (two files) on the live ref read on the host (expected `a0c83303ee`) under its own never-widen: Phase A in a fresh guarded process (the loggers unchanged, the live ref's snapshot shown to differ), Phase B unarmed only, and the CTO's criterion: the service's `POST /mcp` journal lines back under traffic, counted against the audit lake over the same 30-minute window (lines > 0 and >= 0.25 x records; listener lines 0) | `W/`, the ledger `batch11`, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 2 chains, cap 8 (`OG-pr-5` is the chain head, spawn now; `OG-ap-44` follows its drain and needs three halves; `OG-ev-7` now follows `OG-ap-44` CLOSED). Gate limb: the two newly added tree orders are graded by `to-pipeline-gate`.

**R3-T.120 amendment A2 (2.0.0_SA_COO~O, round 43, ~20:3xZ, workstream ENRICH-R43-D): a lineage cell `OG-ap-45`.** The CTO's `OG-ap-44` half record (msg 35792) measures that site Z's tenth release `eff517546e` (live, ledger `batch11` CLOSED 20:01:40Z) and its parent `a0c83303ee` (ninth, `batch10`) are not ancestors of `box/sitez`, and asks that they be landed the way `OG-ap-41` and `OG-ap-43` landed the earlier releases. `OG-ap-45` is the repository merge for `~NFRA1` (the shape of `OG-ap-43`): one merge of `eff517546e` onto the `box/sitez` head; the issuer's merge-tree at the cut reads CLEAN (no conflicted path); no gateway byte changes; `ap45.AC1` to `AC4`, graded through the repaired `_ap43_check.py`.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ap-45` | merge `eff517546e` (carrying `a0c83303ee`) onto the `box/sitez` head in the applier's worktree, trunk's side on any conflict, the manifest block `eff517546e` / previous `a0c83303ee` from the applier's own Phase B commit; the record lists trunk's own changes against the live release | `W/`, the merge on a landing branch (drained by the issuer) | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 of 1 chains, cap 8 (a repository merge; independent of `OG-ev-7`). Gate limb: the newly added tree order is graded by `to-pipeline-gate`.


## ADDENDUM R3-T.121 (2.0.0_SA_COO~O, 2026-10-19 ~01:5xZ) -- ROUND 44, workstream ENRICH-R44-A/B/C: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), cut in ONE issuance

**Source.** The round-43 analysis (endpoint unchanged; round 44 spends one served read on the audit plane, sizes the inline-audit repair before building it, clears two test-plane defects, and releases the site Z code that is on trunk and in no release) cuts six cells; the issuer adds a seventh (`OG-en-34`, amendment A1 below). Standing conditions for every round-44 order: (1) the base is the live ref at the GO (`eff517546e` today), each release carries dell1's four harvest files unchanged with their blobs named in the ask; (2) every never-widen ask carries the line `process-wide state this change touches: <list>, or none, read`, and every Phase B prints the journal `POST /mcp` count beside the audit-lake count for one window (CVO verdict 35844, relayed by msg 35845); (3) every read-only audit record pins its base sha and its check reads the files at that sha.

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-10` | is the per-identity refusal's audit write failing (`Z-W155-S1`)? STEP 1 read-only: the journal's `POST /mcp` 429 lines and the writer's own WARN lines since the access log returned, the lake's `gw_ratelimit` rows, whether any route exposes `audit_failure_count()`, and the (label, tool) pairs of the 10 unlabelled records in `OG-ev-7`'s window (the CTO's CT3 service limb); verdict `WRITES`/`FAILS`/`NOT_EXPOSED` by a rule fixed in the order. STEP 2 (one controlled refusal with a test principal) only if STEP 1 reads `NOT_EXPOSED`, under three halves | `W/` | SERVED | `~AE` (`~NFRA1`) | applier |
| `OG-ev-11` | size the inline audit-write repair: `OG-ev-8`'s 81-site table completed (the 12 unknown sites settled from the pinned `mcp==1.28.0` dispatch rule, read from the package), per-tool 7-day counts from lake record bodies (every key listed, every k-th body read, scaled and labelled), and a ranked repair proposal; no change | `W/` | LOCAL | `~157` | worker |
| `OG-en-32` | the five route tests that answer 404 where they expect 405 (`Z-S391`): the cause named read-only with its evidence (library version, test premise or real defect), then a TEST-only repair; a real defect stops the order with a BLOCKING row | `tests/test_transcript_route.py`, `tests/test_teams_route.py`, `tests/test_mail_route.py`, `W/` | WORLD (gateway path floor) | `~158` | worker |
| `OG-en-33` | the shared both-orders check keeps the forward pytest text and reports `NO PASS LINE` with the saved path; its first-run flake (`Z-S399`) reproduced cold in at least eight runs and named, or `NOT_REPRODUCED` | `r38/checks/_bothorders.sh`, `W/` | LOCAL | `~159` | worker |
| `OG-en-34` | (amendment A1) the wrong comment in `app/probe_listener.py` ("The probe still writes no access line of its own") corrected; comment lines only, AST equal to the base blob | `app/probe_listener.py` | WORLD (gateway path floor) | `~160` | worker-light |
| `OG-ap-46` | the eleventh batched release on the live ref read on the host: `app/family_depth.py` + `app/refs/silver_families.json` + `tests/test_og_cd1.py` (site Z's `OG-cd-1`, on trunk and in no release; inert, the IAM `.tf` excluded) and the corrected `probe_listener.py`; the optional pair `app/admin_people_access.py` + its test ONLY on `W/MP_YES.md` (the written yes of `2.0.0_SA_COO~MP`); under its own never-widen with standing conditions 1 and 2; Phase B unarmed only; staged behind `OG-en-34` | `W/`, the ledger `batch12`, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |
| `OG-ap-47` | the merge of `OG-ap-46`'s release onto the `box/sitez` head in the shape of `OG-ap-45`; `ap47.AC3` lists every path that differs from live, each with its owner; staged behind `OG-ap-46` CLOSED | `W/`, the merge on a landing branch (drained by the issuer) | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 4 workers of 5 chains, cap 8 (workers `~157` to `~160`; the chain heads are `OG-ev-10` (the applier's, independent), `OG-ev-11`, `OG-en-32`, `OG-en-33` and `OG-en-34` (then `OG-ap-46`, then `OG-ap-47`, the applier's)). Spawn now: `OG-ev-11`, `OG-en-32`, `OG-en-33`, `OG-en-34`; `OG-ev-10` takes its STEP 1 GO at once; `OG-ap-46` follows `OG-en-34` drained and needs three halves; `OG-ap-47` follows `OG-ap-46` CLOSED.

**Readings disclosed to the CTO (each can be corrected before the asks).** (1) `OG-ev-11`: "per-tool call counts over the last 7 days, from record BODIES" is read as every key LISTED for 7 days (the exact denominator) and the bodies read for a sample of at most 12000 objects at a printed rate, the counts scaled; reading about 70000 bodies is not a bounded job for a worker. (2) `OG-ev-10`: the refusal writer prints a WARN line to stderr on a failed write, and the restored access log lets an organic 429 be matched to the lake, so STEP 1 can often decide without making a refusal; the controlled refusal is STEP 2, under three halves. (3) `OG-ap-46`: `family_depth.py` ships with `app/refs/silver_families.json` and `tests/test_og_cd1.py` (the commit that put it on trunk put all three there), without its IAM `.tf`, so the module is inert; the comment fix needs `OG-en-34` first because a release takes files already on trunk. (4) `OG-en-32` is bounded to the three test files; a real routing defect returns to the issuer.

**Held / carried.** `Z-W94-S2`, `Z-S313`, `Z-S322`/`Z-S325` (as the analysis); `Z-S177` re-read after `OG-ev-10`; `Z-S389` is "not reproduced" (the CVO owns the row's disposition); `Z-W153-S2` closed by `OG-sec-2`'s pin (the CVO disposes). Routed to `0.0.0_AB_MSTR~Z` by the CTO: the audit-lake registry row, the missing hashed account-id list (`Z-W151-S1`), a focus-free way to wake an idle seat.

**R3-T.121 amendment A1 (2.0.0_SA_COO~O, round 44, same issuance): the seventh cell `OG-en-34`.** The CTO's list puts the one-line comment correction inside `OG-ap-46`; a release takes its files whole from trunk at `trunk_sha` (`ap46.AC1` demands byte-equality), so the correction has to be on trunk first. `OG-en-34` is that edit: a comment-only change to `app/probe_listener.py` (the base blob `85ce5027cc` is named in its check), `worker-light`, two criteria (`en34.AC1` the comment-only edit by AST equality, `en34.AC2` the listener's two test files still pass). Gate limb: the newly added tree order is graded by `to-pipeline-gate` with the other six.

**R3-T.121 amendment A2 (2.0.0_SA_COO~O, round 44, ~02:3xZ): ruling on `OG-en-32`'s BLOCKING row `Z-W158-S1`.** The worker named the cause of the five 404-for-405 answers read-only: the catch-all `Route("/{path:path}", dashboard_deep_link)` at `app/server.py:1198` (NFRA_MCPORTAL cell MP-z-3, row `Z-S41`, commit `e42d2c35c3`, 2026-10-13) takes every method and answers a plain 404 to a non-GET request. The issuer rules inside its own decomposition: the catch-all is intended, the cause class is `test_premise` (the tests' 405 was superseded by that cell; the fail-closed property holds), and the repair stays inside the order's three test files (the five cases accept a refusal of 404 or 405, every other assertion unchanged). The application is not changed; ruling row `Z-S400`. No criterion or path of the order changed; the worker continued on its same face. Gate limb: none graded (no order file was newly added).

**R3-T.121 amendment A3 (2.0.0_SA_COO~O, round 44, ~03:4xZ): `OG-ev-10` STEP 2 becomes the one-object WRITER TEST (CTO ruling msg 35872).** STEP 1 read NOT_EXPOSED (0 of 1413 `POST /mcp` lines answered 429; 0 writer WARN lines; 0 `gw_ratelimit` rows over 5568 objects; the counter is read by no route). The applier found that no non-person `/mcp` principal exists, so the controlled refusal of the order's STEP 2 cannot run (the limiter needs a bearer from a live refresh family). The CTO ruled the applier's option (b) in, bounded: one synthetic object (labelled `OG-ev-10`, its lake key printed), written by a guarded fresh process under the service's instance role through `record_identity_refusal`, read back and never deleted, under three halves on its own ask; (a) a read-only re-run after real use also stands. The order's `<paths>` and criterion are unchanged; `ev10.AC1.sh` gains the `writer_test` field and two lines of the verdict rule (green and red arms fed to it before this amendment). Gate limb: none graded (a modified order that declares no placeholder change).

**R3-T.121 amendment A4 (2.0.0_SA_COO~O, round 44, ~05:4xZ): what counts as `OG-ev-10`'s writer-test READ-BACK.** The applier ran the one-object writer test (STEP 2 of A1/A3): the put under the service's instance role returned, one object lies under the synthetic principal, the runner read it back with its own role (one row, `gw_ratelimit`, the synthetic principal), and the host process's own `get_object` was AccessDenied (the instance role has no get on the lake). My rule as first written (`read_back` = the host process's read) computed `FAILS`; the signed ask's own section 3 step 3 requires the runner-side read-back, so the rule is clarified (any independent reader counts; the host role's denial is recorded, not graded) and `ev10.AC1.sh` is amended with its arms. The first computed verdict is kept in the record as `verdict_first_computed`. The CTO is told in the same turn. No criterion or path of the order changed besides that rule. Gate limb: none graded (a modified order that declares no placeholder change).


## ADDENDUM R3-T.122 (2.0.0_SA_COO~O, 2026-10-19 ~06:0xZ) -- ROUND 45, workstream ENRICH-R45-A/B/C: the CTO's round-44 analysis (`ledger/ROUND_ANALYSIS.round44.md` @ebefeda213, msg 35898), cut in ONE issuance

**Source.** The round-44 analysis (endpoint unchanged; round 45 closes the two holes round 44 found in the audit plane: a lake put that fails says nothing, and an unbounded put sits on the event loop; it also finds who answered the organic 429) cuts four cells. Standing conditions for every round-45 order (carried): (1) the base is the live ref at the GO (`e09c30c3f0` today), dell1's four harvest blobs carried unchanged and named in the ask; (2) every never-widen ask names the process-wide state the change touches (CVO verdict 35844) and every Phase B prints the journal `POST /mcp` count beside the audit-lake count for one window; (3) every read-only audit record pins its base sha and its check reads at that sha. Every worker face runs the proof checker as `python3 -I .tools/proof-of-spec-check.py` (CTO ruling msg 35901: only `python3 -I` sees `jsonschema` on this box).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-12` | read-only: who answered the organic per-identity 429 of 2026-10-18 about 19:2xZ that left no `gw_ratelimit` row (`Z-W155-S1`)? The journal from the access log's return, the lake hour 19:00Z to 20:00Z, the response shape, the limiter's throttle rule read at a pinned sha; verdict `THIS_SERVICE_WROTE_NOTHING`/`OTHER_LAYER`/`THROTTLED`/`UNDETERMINED` by a rule fixed in the order; no change | `W/` | LOCAL | `~AE` (`~NFRA1`) | applier |
| `OG-pr-6` | make the audit lake leg bounded and audible (`Z-S402`): one file `app/audit.py`: a failed `put_object` increments a module counter and writes ONE stderr line (then at most one per 60 s with the running count), the audit S3 client built with an explicit botocore `Config` (connect 2 s, read 3 s, one attempt, justified from `OG-ev-11`), the floor write unchanged; a new test file | `app/audit.py`, `tests/test_og_pr6.py`, `W/` | WORLD (gateway path floor) | `~161` | worker |
| `OG-ap-48` | the twelfth batched release carrying `OG-pr-6` (two files) on the live ref read on the host, under its own never-widen with standing conditions 1 and 2; Phase A measures the bounded failed put on the host under the guard with a black-hole endpoint in a fresh process; Phase B unarmed only and also prints the new failure counter (expected 0) beside the dual count; staged behind `OG-pr-6` | `W/`, the ledger `batch13`, the sentinel | WORLD | `~AE` (`~NFRA1`) | applier |
| `OG-ap-49` | the merge of `OG-ap-48`'s release onto the `box/sitez` head in the shape of `OG-ap-47`; `ap49.AC3` lists every path that differs from live, each with its owner; staged behind `OG-ap-48` CLOSED | `W/`, the merge on a landing branch (drained by the issuer) | WORLD | `~AE` (`~NFRA1`) | applier |

**fanout:** 1 worker of 2 chains, cap 8 (worker `~161`; the chain heads are `OG-ev-12` (the applier's, independent) and `OG-pr-6` (then `OG-ap-48`, then `OG-ap-49`, the applier's)). Spawn now: `OG-pr-6`; `OG-ev-12` takes its GO at once; `OG-ap-48` follows `OG-pr-6` drained and needs three halves; `OG-ap-49` follows `OG-ap-48` CLOSED.

**Readings disclosed to the CTO (each can be corrected before the asks).** (1) `OG-pr-6`: the new tests live in a new file `tests/test_og_pr6.py` (the release takes the two files). The Config values are mine: `connect_timeout` 2, `read_timeout` 3, `max_attempts` 1; the check accepts connect up to 5 s, read up to 10 s and at most 2 attempts. The stderr line carries the exception class name only. (2) `OG-ev-12`: the four verdicts have concrete rules in the order; the access log returned at 19:23:53Z, so a 429 before that time cannot be seen in the journal and reads `UNDETERMINED` (the lake hour is read either way). (3) `OG-ap-48`: the new counter is a module variable read by no route, so Phase B reads it as the `audit-lake WARN` journal line (the counter is the last `count=` printed, 0 with no line), and a nonzero value is a read-back TRIGGER.

**Held / carried.** As the analysis: `OG-ev-11` ranks 2 to 4, the NFRA_MCPORTAL `admin_people_access.py` pair (needs `2.0.0_SA_COO~MP`'s yes), the `family_depth` mount; `Z-W94-S2`, `Z-S177`, `Z-S313`, `Z-S322`/`Z-S325`; `Z-S391` closed in effect by `OG-en-32`; `Z-S399` not reproduced. Routed to `0.0.0_AB_MSTR~Z`: `jsonschema` under `python -I` (closed by the ruling above), the watcher-gap mail and `wt.exe`. My own take: print each count under its own noun in a check's output.


## ADDENDUM R3-T.123 (2.0.0_SA_COO~O, 2026-10-19 ~08:5xZ) -- ROUND 46, workstream ENRICH-R46-A: the CTO's round-45 analysis (`ledger/ROUND_ANALYSIS.round45.md` @de11baa89b, msg 35919), cut in ONE issuance

**Source.** The round-45 analysis (endpoint unchanged; round 46 is small on purpose: the remaining candidates are a comment and a re-read) cuts ONE cell. Standing conditions (carried): the base is the live ref (`6b1a9bd292` today); every read-only audit record pins its base sha and its check reads at that sha; the worker face runs the proof checker as `python3 -I .tools/proof-of-spec-check.py` (CTO ruling msg 35901).

| cell | what | writes | risk | slot | class |
|---|---|---|---|---|---|
| `OG-ev-13` | read-only: the audit lake leg after a full day of production traffic (`Z-S402`): over at least 24 hours from the `OG-ap-48` close (2026-10-19T07:44:53Z), the journal's `audit-lake WARN` lines (count, last `count=`, classes), the lake objects per hour against `POST /mcp` lines per hour (24 or 25 whole hours), and the lake's 2026-10-19 02:00Z hour of about 2,896 objects (about 7 times the baseline hour) explained by a tool or event histogram of ALL its bodies (counts only); verdict `HOLDS`/`FAILS_SEEN`/`UNDETERMINED` by a rule fixed in the order; no change | `W/` | LOCAL | `~AE` (`~NFRA1`) | applier |

**fanout:** 0 workers of 1 chain, cap 8 (a read-only cell of the applier's; no worker is spawned). **STAGED WITH AN ESSENTIAL WAIT:** the GO comes no earlier than 2026-10-20T07:45:00Z. The outcome is "the lake leg holds under a day of real traffic"; only elapsed traffic produces it and no act can manufacture production load honestly (the CTO's stated reason, section 2 of his analysis).

**Readings disclosed to the CTO (each can be corrected before the GO).** (1) "lake/hour tracks POST/hour" becomes: in every hour with 20 or more `POST /mcp` lines the lake holds at least 0.5 times as many objects (the two read-backs read about 1.8 objects per line); a lag with no WARN line reads `UNDETERMINED`. (2) A window that starts at :44:53 spans 25 hourly buckets; the check accepts 24 or 25. (3) The 02:00Z hour is explained from ALL its bodies (about 2,900 reads, in a background script), counts only.

**Held / carried / ruled.** As the analysis: the retry-count comment rides the next `audit.py` change (two sends stay; never a release of its own); `admin_people_access.py` on `2.0.0_SA_COO~MP`'s written yes only; the `family_depth` mount until an outcome needs the route; the watcher-gap claim answered by MSTR's measurement (35900), no cell. **The CTO's one ask, answered in the NEXT slug (after this cell):** every FWD that does not yet grade REALIZED, so that he can tell whether round 47 has build work or waits on FWD-21 (open-calls row 5b35, Andrew's act).


## ADDENDUM R3-T.123-A1 (2.0.0_SA_COO~O, 2026-10-19 ~09:5xZ) -- ROUND 46, workstream ENRICH-R46-B (a second workstream of the round, beside `OG-ev-13`'s ENRICH-R46-A): the CTO's AMENDED round-45 analysis (A1 @6018fc83fd, msg 35923; A2 @cc6b4f8f3f, msg 35928), the rest of the list cut in ONE issuance with `OG-ev-13`

**Source.** A1 replaces the one-cell list with three cells and withdraws nothing of `OG-ev-13`; A2 withdraws A1's item 4 (G-C was retired by ruling 28152) and hands me the one protocol edit, to ride `OG-gd-2`. `OG-ev-13` is issued (69dacc181d) and stays STAGED; this addendum cuts the other cells. Standing conditions (carried): the base is the live ref at each GO (`6b1a9bd292` today); every read-only audit record pins its base sha; the worker face runs the proof checker as `python3 -I .tools/proof-of-spec-check.py` (ruling msg 35901); every release ask carries `process-wide state this change touches`, and every Phase B prints the journal `POST /mcp` count beside the audit-lake count for one window (CVO verdict 35844).

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-ev-13` | (issued, unchanged) the audit lake leg after a day of traffic, GO no earlier than 2026-10-20T07:45:00Z | `W/` | LOCAL | `~AE` (`~NFRA1`) | applier | essential wait |
| `OG-gd-2` | read-only grade read of FWD-10 to FWD-19 and FWD-22 in GD1's shape, no grade word; plus the one narrow edit of `tests/acceptance/WALKTHROUGH_PROTOCOL.md` dropping the retired G-C precondition (A2) | `W/`, one doc | SERVED | `~162` | worker | none |
| `OG-cd-2` | mount `family_depth` in `app/admin_api.py` behind `owner_only`: two added lines and `tests/test_og_cd2.py` | 2 files | WORLD (gateway floor) | `~163` | worker | none |
| `OG-cd-3` | apply the read grant `family_depth_read_iam.tf` (one `aws_iam_role_policy`, 3 read actions) through `safe-apply`; own never-widen ask | Terraform, ledger | WORLD | `~AE` (`~NFRA1`) | applier | none (Phase A now) |
| `OG-ap-50` | the thirteenth batched release: `admin_api.py` + `test_og_cd2.py`, a NEW served route (owner-gated), under its own never-widen; Phase B ends with the ONE driven FWD-20 read | release, ledger | WORLD | `~AE` (`~NFRA1`) | applier | `OG-cd-2` drained and COMPLETE, `OG-cd-3` CLOSED |
| `OG-ap-51` | land the thirteenth release on the sitez lineage (the standing landing step) | repo only | WORLD | `~AE` (`~NFRA1`) | applier | `OG-ap-50` CLOSED |

**Chains and fan-out.** Three independent chains: `{OG-ev-13}`, `{OG-gd-2}`, `{OG-cd-2, OG-cd-3} -> OG-ap-50 -> OG-ap-51` (the edge `OG-cd-2 -> OG-ap-50` is the code the release takes; `OG-cd-3 -> OG-ap-50` is the grant live before the route; `OG-cd-2` and `OG-cd-3` do not depend on each other). Two workers spawn now (`~162`, `~163`); the applier lane holds four orders, one active at a time (`OG-cd-3` Phase A first; `OG-ev-13` waits for its time). `fanout: 2 workers of 3 chains, cap 8`.

**Readings disclosed to the CTO (each can be corrected before a GO).** (1) The analysis's `OG-cd-2` names the mount AND the IAM apply; they have different write sets and executors (a worker's code, the applier's `safe-apply`), so the cell is cut as `OG-cd-2` (mount) and `OG-cd-3` (IAM), one owner each. (2) "ONE driven read for FWD-20 (proof by a served read)": the route is owner-gated by the load balancer's signed identity header, which no agent can supply; the driven read is the DEPLOYED module run once on the host as the instance role (`OG-ap-50` step 7, criterion `AC3`), compared with the AWS CLI's own reads of one family's schedule and one family's depth (the PRD's FWD-20 PROOF wording), and the route is read unauthenticated before and after the deploy (404, then 401, with controls) to show it is mounted and gated. The owner-session read through MC Portal is Andrew's, later. (3) The mount is two lines in `app/admin_api.py`, NFRA_MCPORTAL's file; `family_depth.py`'s docstring and `OG-cd-1` already name it as the release cell's hookup, and the ask names it to the owner. (4) `OG-ap-51` (the landing) is cut though A1 does not list it, as for every earlier release. (5) A1 item 4 is withdrawn by A2; the protocol edit rides `OG-gd-2` as A2 says, narrow and checked (`gd2.AC3`).

**Held / carried / ruled.** As before: the retry-count comment rides the next `audit.py` change; `admin_people_access.py` on `2.0.0_SA_COO~MP`'s written yes only; FWD-21 is Andrew's act (row 5b35); the walkthrough (G-E) is listed for Andrew. The gate limb that grades this issuance: the newly added tree orders are graded by `to-pipeline-gate`; the project row is already EXECUTING. The gate keys ONE issuance to the ROUND and refused five added files into round 46 (`OG-ev-13` was its first), naming the second-workstream route; the five carry `<workstream>ENRICH-R46-B</workstream>`. Their write surfaces are disjoint from `OG-ev-13`'s (`W/` only) and the issuer is the same instance: READING DISCLOSED TO THE CTO.

**R3-T.123 amendment A3 (2.0.0_SA_COO~O, round 46, ~18:0xZ, workstream ENRICH-R46-C, a second workstream with its own disjoint write surface): a seventh cell `OG-mg-2`, URGENT, on the CTO's relay of an Andrew-direct.** `1.0.0_SA_CTO~Z` msg 36025 (record `ANDREW_DIRECT_20261019_172xZ_ALYSSA_3PM_SCHWAB_TEST_SENDS_YES_ROSTER_AS_OPEN_CALLS_SCHWAB_FULL_ACCOUNTS.md` @65a05f6658): "Schwab should automatically cover the full accounts ... there shouldnt be a persisted list". Alyssa tests at 19:00Z with Andrew, so before 18:45Z the grants of Andrew's and Alyssa's principals are re-activated with each granted master's CURRENT S3 account set (interim), with a decide() pre-flight on Alyssa's grant (four read tools admitted, `schwab_prepare_download` refused). The read-time scope (no stored list) is the round-47 code cell the CTO named; it is not cut here.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-mg-2` | new `accounts` per granted master on two grant revisions through `ops/schwab_entitlement_admin.py` `activate`; nothing else in either scope changes; Phase A ends at the three-half ask | grant store, ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier | none (Phase A now) |

One chain `{OG-mg-2}`; no worker spawns (an applier act): `fanout: 0 workers of 1 chain, cap 8`. It runs on the applier lane BEFORE `OG-ap-51` (the landing is not time-bound). The write surface is disjoint from every other round-46 order (`W/`, the ledger, the channel). Gate limb that grades it: `to-pipeline-gate` on the newly added tree order (a mid-round add inside the issuer's own decomposition, as A2 of this addendum was).

**R3-T.123 amendment A4 (2.0.0_SA_COO~O, round 46, ~17:5xZ, workstream ENRICH-R46-D, a third workstream with its own disjoint write surface): an eighth cell `OG-rs-1`, URGENT, restart the hung gateway service.** `2.0.0_SA_COO~MI` msg 36038 (17:47Z): the gateway host answers no MCP call since about 17:40Z, `/health` returns nothing, RSS 1.41 GB against `MemoryHigh` 1.2 GB. Alyssa tests at 19:00Z. One restart of the running release, no deploy, to `0.7.0_AE_CloudOps~NFRA1` (the gateway host's applier), before `OG-mg-2` (database writes only, unaffected by the hang) continues.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-rs-1` | `systemctl restart opal-gateway` once, ledger `nfra-oplgtw-gateway-restart-20261019`, read-back of health, marker, tools/list, md5 walk and the 27-tool read | ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier | none |

One chain `{OG-rs-1}`; `fanout: 0 workers of 1 chain, cap 8`. Gate limb that grades it: `to-pipeline-gate` on the newly added tree order.

**R3-T.123 amendment A5 (2.0.0_SA_COO~O, round 46, ~19:3xZ, workstream ENRICH-R46-E, a fourth workstream with its own disjoint write surface): two cells, `OG-rz-1` and `OG-rz-2`, resize the gateway host to `t4g.large`.** Andrew-direct ~18:3xZ 2026-10-19 ("lets raise it to large"; record `ANDREW_DIRECT_20261019_183xZ_GATEWAY_EC2_RESIZE_TO_T4G_LARGE.md` @439343a969) relayed by `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` msg 36070; the CTO's routing: cut it after Alyssa's 19:00Z session, off-hours, one deploy ledger, rollback to `t4g.small`.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-rz-1` | the unit's `MemoryHigh` 1200M to 5600M and `MemoryMax` 1400M to 6400M, `test_og_un1`'s bounds to match, the contract's `target_instance_type` to `t4g.large` (three files) | 3 repo files | WORLD (gateway floor) | `~164` | worker-light | none |
| `OG-rz-2` | `main.tf:172` `t4g.small` to `t4g.large` through `safe-apply` (in place, stop/start), THEN one release carrying `OG-rz-1`'s commit; ledger `nfra-oplgtw-gateway-resize-t4g-large`; own never-widen ask; STAGED, Phase A now, Phase B in an off-hours window on the issuer's GO | Terraform, release, ledger | WORLD | `~AE` (`~NFRA1`) | applier | `OG-rz-1` drained; Alyssa's session over |

**Chains and fan-out.** One chain `OG-rz-1 -> OG-rz-2` (the release takes the worker's commit). `fanout: 1 worker of 1 chain, cap 8` (`~164`, worker-light, on the three-file cell under the 100-line floor).

**Readings disclosed.** (1) The order of the acts is the safety property: the raised limits only AFTER the resize (`MemoryMax=6400M` on a 2 GiB host would invite the kernel OOM killer) and the rollback the other way round. (2) The values `5600M`/`6400M` are the issuer's: 8 GiB less about 1.6 GiB for the OS, the SSM agent and the guarded fresh-process reads, with the soft throttle 800M below the hard limit. (3) The public IPv4 of an instance without an Elastic IP changes on stop/start: Phase A reads whether it does and what in Opal's estate names it; a vendor-side allowlist is NOT CLAIMED. Gate limb that grades it: `to-pipeline-gate` on the two newly added tree orders in one commit.

**R3-T.123 amendment A6 (2.0.0_SA_COO~O, round 46, ~20:2xZ, workstream ENRICH-R46-F, a fifth workstream with its own disjoint write surface): a cell `OG-ms-1`, register Schwab master `08403355` (0840, the Tax SMA master) so a grant can name it.** Andrew-direct ~19:55Z 2026-10-19 (record `ANDREW_DIRECT_20261019_195xZ_ALYSSA_SCHWAB_MASTER_0840_ADD_TO_ENTITLEMENTS.md`) relayed by `1.0.0_SA_CTO~Z` msg 36102 and ruled (B) in msg 36104: it rides tonight's off-hours batch with the `t4g.large` resize.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-ms-1` | `08403355` in `MASTERS` (`data_entitlement.py:77`) and `schwab_audit._MASTERS`; the contract's `masters` label, `data_prefixes` (+4) and `completion_prefixes` (+1) in BOTH copies (deploy and `org/standards`, byte-equal, also curing `OG-rz-1`'s one-copy edit that broke `test_ogcm1_ac05`); the `scopes.json` firm masters list and a MASTER row; `tests/test_og_ms1.py` | 6 repo files plus tests | WORLD (gateway floor) | `~165` | worker | none |

**Chains and fan-out.** One chain `OG-ms-1 -> (release batch15, amended into OG-rz-2) -> OG-ms-2 (the grant write, cut after the release is live)`. `fanout: 1 worker of 1 chain, cap 8`. **Readings disclosed.** (1) The CTO's list named a possible gateway-role S3 read line; the reader IAM `.tf` (`schwab_reader_iam.tf` lines 72-78) ALREADY lists the `schwab/08403355/` prefixes, so the applier reads whether the LIVE role holds them (Phase A) rather than editing Terraform. (2) The `client_*` tools keep refusing `08403355` (`master_not_registered`): a separate decision, not touched. (3) A grant naming `08403355` is `Malformed` today; the registration is therefore a precondition, not a widening by itself. Gate limb that grades it: `to-pipeline-gate` on the newly added tree order.

**R3-T.123 amendment A7 (2.0.0_SA_COO~O, round 46, ~20:5xZ, workstream ENRICH-R46-G, a sixth workstream with its own disjoint write surface): a cell `OG-ms-2`, add master `08403355` to Alyssa's Schwab grant.** The second half of the CTO's ruling (B) (msg 36104): `OG-ms-1` (code, complete) makes the master legal; this cell writes the grant.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-ms-2` | `scope.masters` +`08403355`, `scope.accounts` +`08403355` at its full current set (the `OG-mg-2` method), everything else and Andrew's grant untouched; Phase A (prepare, decide() pre-flight, the three-half ask) NOW on trunk code, Phase B only when the batch15 ledger is CLOSED | grant store, ledger, `W/` | WORLD | `~AE` (`~NFRA1`) | applier | Phase B: `OG-rz-2` CLOSED (STAGED until then) |

One chain `OG-ms-1 -> OG-rz-2 -> OG-ms-2`; `fanout: 0 workers of 1 chain, cap 8` (an applier act). Reading disclosed: the grant, once written, names a master the LIVE gateway will not know until batch15 is live, which is why Phase B waits. Gate limb: `to-pipeline-gate` on the newly added tree order.


## ADDENDUM R3-T.124 (2.0.0_SA_COO~O, 2026-10-20 ~09:3xZ) -- ROUND 47, workstream ENRICH-R47-A: the CTO's round-46 analysis (`ledger/ROUND_ANALYSIS.round46.md` @ad17495429, msg 36165), the build cells cut in ONE issuance; the applier cells follow as amendments when their inputs exist

**Source.** The round-46 analysis (endpoint unchanged; round 47 closes the client-surface and size defects the CRO's audit found, adds the service's own bound on concurrent load, and moves Schwab to a master-wide scope) ranks eight items. The slug that asked for it: `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND46_DRAFT.md` @345c76a903; the item list: `deliverables/2.0.0_SA_COO~O/r46/ROUND47_ITEMS_OWED_DRAFT.md`. Standing conditions (carried): the base is the live ref at each GO (`13917ef993` today); every release ask carries `process-wide state this change touches` and every Phase B prints the journal `POST /mcp` count beside the audit-lake count; every read-only audit record pins its base sha; the worker face runs the proof checker as `python3 -I .tools/proof-of-spec-check.py` (ruling msg 35901); battery concurrency stays at 2 or fewer until `OG-mg-3` is live (the CTO).

**THE RECTANGLE** (rank is the CTO's; the left column is this decomposition's cell id):

| cell | what | rank | writes | risk | slot | class | status of the cut |
|---|---|---|---|---|---|---|---|
| `OG-fc-1` | `fence_kind` rows for orion, eclipse, commonwealth (D1, Z-S409) and the resolve envelope that names every vendor read (D3, Z-S411) | 1, 5 | `app/client_core.py`, `tests/test_og_fc1.py` | WORLD (gateway floor) | `~166` | worker | CUT NOW |
| `OG-sx-1` | the small-fix cell: D2 Cottonwood date parse (Z-S410), the Z-S407 error-text mask, Y1/Y2 and the fund-series cap (YCharts, Z-S422/423/424), R1 (data-refresh status of an unknown id) | 4, 5, 8, 2 | 4 product files, `tests/test_og_sx1.py` | WORLD | `~167` | worker-light | CUT NOW |
| `OG-sz-1` | the 50 KB projection measured on the served bytes (P4), no whole-field null (P5), `mdpf_get_aggregate_aua` (P6) and `opal_discover` (P7) projected (Z-S413) | 2 | `harvest_typed.py`, two integrations, tests | WORLD | `~168` | worker | CUT NOW |
| `OG-mg-3` | the memory guard: a process-wide bound on concurrent tool calls at the one dispatch chokepoint, and `target_memory_mib` 8192 in both contract copies (Z-S425, Z-S420) | 3 | `app/inflight_guard.py` (new), `app/tools.py` (one hunk), two contract copies, test | WORLD | `~169` | worker | CUT NOW |
| `OG-tp-1` | the result caps on `search_files` / `search_site_files` (Z-S424) and the `top` bound of the Teams poll (Z-S423 T1); queued behind `OG-mg-3` on the SAME worker because both write `app/tools.py` (C10) | 2, 8 | `app/tools.py`, test | WORLD | `~169` | worker | CUT NOW (queued) |
| `OG-rt-1` | the master-wide Schwab scope `accounts[master] = ["*"]` resolved at read time, no stored list (Andrew-direct 2026-10-19) | 6 | `data_entitlement.py`, `account_ref.py`, the schwab integration, test | WORLD | `~170` | worker | CUT NOW |
| `OG-ix-1` | the breakdown handler's `index_pairs` (P1 handler half, NFRA_MCPORTAL's GWZ1.1) | 7 | `admin_gateway_breakdown.py`, test | WORLD | `~171` | worker | CUT NOW |
| `OG-nf-1` | `news_for_security` searches the company name as well as the ticker and says why a zero is a zero (H2, Z-S414) | 8 | `news_typed.py`, test | WORLD | `~172` | worker | CUT NOW |
| `OG-rl-17` | the batched release of `OG-fc-1`, `OG-sx-1`, `OG-sz-1`, `OG-mg-3`, `OG-tp-1`, `OG-ix-1`, `OG-nf-1` plus the small take-list (the EC2 manifest `machine_type` backfill to `t4g.large`, the `mcportal_commit` pin `21ad40432cae0d09c5ab9d806307944baaf45cb9`, NFRA_MCPORTAL's `admin_people_access.py` pair on `2.0.0_SA_COO~MP`'s written yes), in an off-hours window like `OG-rz-2`'s, its Phase B driving N parallel large calls with `/health` 200, one live call per vendor for D1, then the landing | 1-5, 7, 8 | release, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT A1 when the workers drain |
| `OG-rl-18` | the release of `OG-rt-1` ALONE (its own never-widen; the code is inert until a grant names `*`), then its landing | 6 | release, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT when `OG-rt-1` drains |
| `OG-ls-1` | narrow the `*/silver/*` `s3:ListBucket` statement of `gateway-family-depth-read-policy` to `<source>/*/silver/*` through `safe-apply`, own never-widen (item 2 of the owed list: four prefixes beyond the eight sources hold a silver child) | small | Terraform, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT (independent chain; no code input) |
| `OG-gv-1` | Andrew's own Schwab grant moves to the master-wide scope (retires `OG-mg-2`'s held half and the `email_deny` follow-on; the CTO rules the `email_deny` handling in its ask) | 6 | grant store, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT after `OG-rl-18` CLOSED |
| `OG-gm-1` | Menachem's Schwab grant, in the master-wide shape (the CTO's word: "Grants after the code") | grants | grant store, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT after `OG-rl-18` CLOSED |
| `OG-gc-1` | the `client_*` tools for Alyssa and Menachem, each under its own never-widen, AFTER D1 to D3 read PASS on the host | grants | grant store, ledger | WORLD | `~AE` (`~NFRA1`) | applier | CUT AS AMENDMENT after `OG-rl-17` CLOSED |
| Z-S402 | a row disposing Z-S402 with the `OG-ev-13` verdict (HOLDS) | small | the channel | LOCAL | the issuer | issuer | WRITTEN BY THE ISSUER (a row, not an order) |

**Chains and fan-out.** Seven worker chains, disjoint write sets (C10): `{OG-fc-1}`, `{OG-sx-1}`, `{OG-sz-1}`, `{OG-mg-3 -> OG-tp-1}` (one worker, because both write `app/tools.py`), `{OG-rt-1}`, `{OG-ix-1}`, `{OG-nf-1}`; the edge `OG-mg-3 -> OG-tp-1` is file contention, so one queue. One shared-file contact beyond that: `app/harvest_typed.py` is written by `OG-sz-1` and CALLED (signature only) by `OG-tp-1`; that is a read of a stable signature, not a write. Applier chains: `{OG-fc-1, OG-sx-1, OG-sz-1, OG-mg-3, OG-tp-1, OG-ix-1, OG-nf-1} -> OG-rl-17 -> OG-gc-1`, `{OG-rt-1} -> OG-rl-18 -> {OG-gv-1, OG-gm-1}`, `{OG-ls-1}`. `fanout: 7 workers of 7 chains, cap 8`.

**Readings disclosed to the CTO (each can be corrected before a GO).** (1) Order ids: the analysis's items 5 and 8 are folded (D2 and D3 into two cells by file; Y2, Y1, R1 and the mask into `OG-sx-1`; T1 into `OG-tp-1`; H2 into `OG-nf-1`, which is a behaviour change and not a small fix). (2) `OG-sx-1` and `OG-tp-1` replace the ids `OG-sf-1` and `OG-tl-1`, which round 37-44 orders already hold. (3) The memory guard is a COUNT bound (4 concurrent calls, 20 s queue), the issuer's value, not a measured one; Z-S420 disarms on `OG-sz-1` and `OG-mg-3` together only after `OG-rl-17`'s Phase B drives the parallel large calls and `/health` stays 200. (4) The master-wide scope stores the sentinel `["*"]`: an OLD gateway reads it as Malformed, so `OG-rl-18` must be live before any grant names it, and the grant orders say so. (5) `OG-ix-1` takes a tool's index pair from the first two components of the index's catalog prefix, only for tools in the two segmented buckets. (6) The seven worker faces carry their own check files under `deliverables/2.0.0_SA_COO~O/r47/checks/`; every criterion's check was run at the base (all FAIL as expected) and the behavioural probes of `OG-mg-3` and `OG-rt-1` were fed a reference implementation in a scratch copy (PASS), the others' probes read their base defects exactly as the CRO's rows state them.

**Held / carried / ruled.** As the analysis: the `audit.py` comment rides the next release that touches `audit.py` (none here); Andrew's owner-session read of `/api/admin/gateway/families` is his; the battery stays at two concurrent calls until `OG-mg-3` is live. Carried ARMED: `Z-S420` (disarms as in reading 3), `Z-S410` (disarms when `OG-sx-1`'s date parse is live and read on the host). The gate limb that grades this issuance: `to-pipeline-gate` on the eight newly added tree orders in one commit; the project row is already EXECUTING.


**R3-T.124 amendment A1 (2.0.0_SA_COO~O, round 47, ~10:3xZ, workstream ENRICH-R47-B, a second workstream with its own disjoint write surface: Terraform and the ledger): the applier cell `OG-ls-1`, the `*/silver/*` ListBucket narrowing.** The CTO's round-46 analysis lists it among the small items; it has no code input, so it is cut now while the seven workers build, on `0.7.0_AE_CloudOps~NFRA1` (idle). METHOD = `OG-cd-3`'s.

| cell | what | writes | risk | slot | class | after |
|---|---|---|---|---|---|---|
| `OG-ls-1` | replace `["*/silver/", "*/silver/*"]` in the statement `FamilyDepthSilverPrefixListOnly` of `gateway-family-depth-read-policy` by the per-source forms of the eight sources of `local.family_depth_sources`; `0 to add, 1 to change, 0 to destroy`; Phase A (plan, simulation, three-half ask) NOW, Phase B on the issuer's GO with all three halves signed; Phase B ends with the `family_depth` read run once on the host | `family_depth_read_iam.tf`, ledger `nfra-oplgtw-grants-ls1`, `W/` | WORLD | `~AE` (`~NFRA1`) | applier | none (Phase A now) |

One chain `{OG-ls-1}`; `fanout: 0 workers of 1 chain, cap 8` (an applier act, additive to the seven workers of the issuance above). Reading disclosed: a strict narrowing, so the ask's widening half says NONE and the three halves still sign because it is an IAM write. Checks `ls1.AC1` and `ls1.AC2` in `deliverables/2.0.0_SA_COO~O/r47/checks/`: `ls1.AC1` base FAIL as expected and fed a green and a red arm with synthetic inputs; `ls1.AC2` base FAIL as expected, read against the LIVE role (the policy reads `broad`, and the bloomberg, gateway and yahoo silver lists read `allowed`: the defect). Gate limb: `to-pipeline-gate` on the newly added tree order.
