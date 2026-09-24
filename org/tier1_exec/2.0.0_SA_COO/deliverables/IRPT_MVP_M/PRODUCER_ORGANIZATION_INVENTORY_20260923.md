# Producer ownership and Opal organization source inventory

Authority: CTO messages `20260923T140502Z`, `140537Z`, and `141018Z`; completion
`CONTRACT.md` and `LOCAL_LIVE_PARTNER_SCOPE_20260923.md`. This is read-only
follow-through to audit `9cc02ebff709055342fd22031cbe87f397bddc39`, with no transfer
of reviewer PASS and no implementation or operational GO.

Source baseline: **`bfa05759101ae36fa4d8d9fb16d548e3001ab06f`**.
[The source receipt inventory](PRODUCER_ORGANIZATION_INVENTORY_20260923.json)
pins 25 files by Git blob, SHA256 and last-changing commit, with Python definition
line numbers. Owner statements below distinguish semantic responsibility from
a permissive path gate; they do not appoint or activate a worker.

## Producers, owners and bounded repair scopes

### Stale directory dates: all three firms

Actual producer: `data/assets/scripts/gold/investor_reporting/directory_runner.py`,
`run_firm`, `SOURCE_SETS`, `select_business_date`, `land`.
`land` writes the dated artifact and `investor-reporting/directory/latest.json`.
Its source sets are:

| Firm | Required source frontier |
|---|---|
| 49financial | Firm Gold `dim_account`, `dim_relationship`, `dim_identity_crosswalk`; relationship manifest supplies completion metadata. Optional BD xref and portfolio-group inputs are separate. |
| inflection | Silver `accounts_v2`, `representatives`, `household_rep_mapping`; intersection of available partition dates. |
| cottonwood | Silver `fact_allocations`; available partition dates. |

Runtime orchestration: `infra/aws/lambda/investor-reporting/directory/refresh.py`,
`lambda_handler` and `SsmBuildDispatcher`, plus Terraform
`infra/aws/terraform/investor-reporting/directory/schedule.tf` and
`principal_49f.tf`. Current executable code dispatches via SSM when configured;
the old module-header description of unwired builds is not proof that the current
deployment is unwired. Terraform declares weekday 09:00 America/New_York refresh;
that is desired configuration, not evidence that the current schedule fired.

**Owners:** DS/`0.4.0_DS_ClientPlatform` owns data computation under workspace
Rule 13; AE/CloudOps owns compute, source-role and schedule plumbing. P is the
current sole IRPT directory/runtime integrator under the narrow exception;
coordinate any data-builder repair with its semantic owner. No source claim is
inferred from the broad `data/**: ANY` file permission.

**Repair scope:** first connect the exact `_refresh` manifest and pending SSM
command/build outcome to the September 17 pointer, installed bundle and each
required source frontier. Distinguish missed/held schedule, failed dispatch,
unreadable source, missing completion and a genuinely old common frontier. Then
repair the specific cause and validate publication before proposing one bounded
refresh. This inventory did not read those live run records or invoke a build;
the old directory date alone cannot select the cause. No schedule activation is
authorized by this proposal.

### Inflection absent ownership map

The bounded committed search over **166 non-test Python files under `data/inf/`**
finds no `ownership_map` writer. This is checked-in corpus absence, not a claim
about every external job. There is an existing maintained attribution producer:
`data/inf/scripts/gold/INF_C_07.advisor_attribution.py`, authored by
`0.4.0_DS_ClientPlatform`, produces `gold/views/account_team.parquet`,
`relationship_team.parquet` and `rel_architect_lookup.parquet`. Its contract is
one `advisor_key` per account, with `household_id`; it explicitly rejects the
assumption of BD's five-role schema. Advisor-of-record source/hold restrictions
in that file remain applicable.

**Owner and repair scope:** DS/ClientPlatform must establish the exact current,
accepted advisor-of-record population, its relationship grain and correspondence
to canonical directory IDs, then add a narrow schema-1 ownership emitter and
same-firm landing/receipt path if no other authoritative producer is identified.
AE owns scheduling/deploy plumbing; P consumes the declared output. Do not run
BD/COT's five-role writer against INF, infer advisors from display names, or
grant all accounts merely to replace the missing object. Required evidence:
input completion/version, advisor/account/relationship denominators, exact ID
join controls, no-grant versus invalid-input distinction, and publication/read
receipts before describing the missing map as repaired.

### Cottonwood empty ownership map

Writer: `data/cot/scripts/gold/D_00.portal_aggregates.py`,
`build_advisor_ownership_artifact` / `_build_advisor_ownership_map`, called from
`main` and saved through `platinum_advisor_ownership_key(FIRM_ID)`.
Input producer: `data/cot/scripts/gold/C_07.advisor_attribution.py`,
`gold/views/account_team.parquet`; owner is DS/`0.4.0_DS_ClientPlatform` by its
header and Rule 13. AE owns chain dispatch. COT is a separate firm; no BD mirror.

**Concrete source risk:** a failed account-team load is caught and replaced by
an accounts-dimension frame containing only account, relationship and architect.
The ownership function requires five role columns. Missing columns return `{}`,
and `main` can still publish a fresh schema-1 empty ownership object.
An actually empty or all-sentinel attribution population can also produce `{}`.
The live empty object from the preceding audit does not distinguish these cases.

**Evidence needed before causal attribution:** the exact publishing run/code pin,
its failed/successful `ACCOUNT_TEAM` read and exception, input object version and
column/row/role counts, and the same run's destination version/hash matching the
audited empty map. Logs alone without output binding are insufficient.
**Repair scope:** preserve genuinely empty grants, but prevent unreadable,
malformed or missing required role inputs from overwriting a valid map as empty;
make refusal/outcome explicit, retain the last accepted version and test both
the failed-input and genuine-empty cases. Do not infer advisor assignments from
the fallback architect column without source-owner authority.

### 49F account and relationship seam

Existing served-shape writer candidate:
`data/black_diamond/scripts/gold/D_00.portal_aggregates.py`, consuming
`ACCOUNT_TEAM`, emitting its raw account and relationship IDs. A distinct
canonical-spine emitter already exists:
`data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`. Its docstring
explicitly distinguishes the served BD IDs from its Schwab account / canonical
relationship / account-singleton IDs. This is not a drop-in equivalent writer.
The live object's deployed writer/code pin was not established by this inventory.

The current serving bridge is `_ids/ids.py:projection_for_firm` plus
`_ids/data/custodian_key_seam.json`. The latter is a bundled historical worker
snapshot, attributed to `0.9.0_WK_IRPT_BCKEND~1 / TO-IB-rte-6`, sourced from
September 16 `blackdiamond/49f/silver/dim_account_xref`. The maintained xref
producer is `data/assets/scripts/silver/bd49f_dim_conversion.py`, authored by
DS/ClientPlatform. Its `resolve_bridge` keeps unresolved rows in-band; its own
accepted-dimension branch filters unresolved mappings. The bundled seam is not
evidence of a continuously maintained serving crosswalk. No maintained seam
refresh generator was located in the inspected production paths.

**Owners:** DS/ClientPlatform owns raw attribution/xref meaning; P owns the
temporary IRPT `_ids` integration. CTO must settle an actual source migration
or newly authoritative crosswalk, rather than treating reconciliation metadata
as an entitlement authority. The existing bundle metadata itself calls the xref
best-effort reconciliation and retains that decision boundary.

**Repair scope:** preserve the full audit denominators (6,564 raw accounts;
287 bad bundled targets; 69 entire advisor calls refused; zero of 3,105 projected
relationships matched). Validate mapping status, non-null target, uniqueness,
source date and exact raw key space before a new bundle can be admitted. Invalid
targets require explicit refusal/coverage; filtering them must not silently turn
the current all-or-nothing grant call into a successful partial grant. Establish
authoritative relationship correspondence separately. If canonical D08 is chosen,
prove both-plane equivalence and migrate every edge/IRPT consumer together;
do not silently change the raw grammar or invent a fuzzy/name join.

## Opal organization: existing record, current adoption/reader gap

`users/configs/opal-capital.json` contains a real checked-in descriptor:
`firmId=opal-capital`, `firmName=Opal Capital`, `configType=user-defaults`,
`configVersion=v1`, created/updated February 17, 2026. The DynamoDB key is
`opal-users-v2`, `PK=FIRM#opal-capital`, `SK=CONFIG#defaults`.

A **read-only, strongly consistent exact-key GetItem at 14:11:46 UTC** returned
that same eight-field metadata projection, HTTP 200. No PROFILE, user list,
security settings or permission defaults were fetched. Receipt:
[OPAL_ORGANIZATION_STORAGE_20260923.json](OPAL_ORGANIZATION_STORAGE_20260923.json).
Projection SHA256 is
`7cf0b38b85f49588bef4a8e4d2d783f3625074cc0bd751c7812ef45e966ed767`.
`configVersion=v1` and `updatedAt` are mutable attributes, not an immutable
upstream version. Existence and operator readability do not establish current
reporting-source authority or an execution-role grant.

The located reader, `users/scripts/create_user.py:get_org_defaults`, is explicitly
**DEPRECATED -- DO NOT USE**, including the CONFIG#defaults approach, under the
May 28 Andrew/CTO migration. It also substitutes the firm token when `firmName`
is missing, which cannot be inherited as report-source semantics. It was not
imported or invoked. Canonical `create_user_v2.py` names `0.7.0_AE_CloudOps` as
sole provisioning owner but exposes no organization display reader. The README's
advertised view/update-config tools and organization-config docs are absent.
The source search inventory records the exact bounded corpus and matches.

The five-row client/test/demo registry has no `opal-capital` row. Current
`maintained_sources._firm_projection` additionally requires `kind=client`;
inserting a home organization into that enumeration would change unrelated firm
and scope semantics. Current user/partner SDK readers identify the actor and
advisor, not an admitted Opal organization descriptor. **The gap is maintained
source adoption and a reader, not absence of all records.**

## Minimal proposal for owner adjudication; not implemented

1. **Source authority:** ask CloudOps (`0.7.0_AE_CloudOps`, canonical provisioning
   owner) and CTO to explicitly adopt only the existing Opal record's organization
   identity/display projection for reporting, with a maintenance owner and update
   contract. Do not revive deprecated user-default provisioning, introduce a new
   tenant, or infer reporting authority from an old file. If that record cannot
   be adopted, the smallest alternative is an owner-issued organization-only
   descriptor with the same home identity and explicit revision; no invented
   display default is used while it is unavailable.
2. **Reader:** a new narrow canonical reader beside `canonical_profile_reads.py`,
   integrated by current owner P, takes a server-verified actor-home identity.
   Read only the fixed organization key using GetItem/consistent read. Require
   exact PK/SK/firmId, admitted config type/version and a nonempty string display
   name; absent, malformed, wrong-home and unreadable are distinct refusals.
   Project only firmId, firmName, configType/configVersion and update provenance.
   Never return user defaults, role templates, security fields or contact data.
3. **Actor versus report tenant:** bind actor home to the actual canonical active
   user PROFILE and verified subject. P's selected tenant and accepted selection
   remain a separate report-data authorization. An Opal actor selecting 49F still
   prepares on behalf of its verified Opal home organization; a partner actor
   never acquires Opal organization identity by selecting Global, sending a
   browser field or carrying a Dev-like string. Mixed actor/profile/selected-set
   identities refuse. No report tenant is renamed to solve the home lookup.
4. **Provenance and retention:** retain the exact permitted source projection,
   canonical source locator, content digest and explicit immutable-version
   absence with the accepted request composition. Recheck actor/input access and
   relevant projection stability during preparation. Retries/reopening reuse
   the frozen accepted projection; a later source correction creates a new
   composition revision. P owns canonical descriptor wire spelling; Y consumes
   that descriptor rather than building an alternate organization field.
5. **Packaging/read permission:** stage the agreed reader and tests in only the
   actual composition preparer package. P must identify its exact execution role
   and existing grant before proposing a delta. If absent, propose only GetItem
   on `opal-users-v2`, constrained to the admitted organization partition where
   supported; enforce the exact sort key and field projection in the reader.
   No scan, write, table creation or partner-table widening. Do not claim IAM can
   independently enforce a sort-key boundary without proving the policy shape.
   This inventory grants no packaging upload, IAM apply or deployment.
6. **Required negative tests:** missing/malformed name or config; wrong PK/SK/home;
   inactive/mismatched actor PROFILE; spoofed browser organization/selected tenant;
   missing current access or revoked selected set; denied read; changed projection
   during preparation; unrelated/default/security fields excluded; partner actor
   cannot borrow Opal identity; Opal-home/partner-report positive remains separate;
   reload/retry preserves the retained original. Run actual SDK/Entry/consumer
   boundaries with pinned fixtures, then independently review the exact package.

Only M evidence paths changed. No producer, deprecated reader, fallback join or
shared application code was run or edited; the sole new live action was the
projected read-only organization GetItem described above. No cloud writes,
deployments or push. Push state LOCAL; prior observed origin CLOUD remains
`365ab567ba1250a6a3569df38cb75d12fe2e8d0e` pending the final handoff measurement.
