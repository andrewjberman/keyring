# PRD review -- NFRA_OPLGTW v0.6, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97547 (ruling R-OG-7, msg 97549).
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `af1cd9f7d6`, ratified-text half_hash `9c6fa0750697`.
Previous signature: v0.5 @ `f81896bae3`, half_hash `908c9e9460c1`.

## VERDICT: REFUSE -- the direction is right and the three names are right; two carriers disagree with the section

## What changed (measured)

The ratified-text section diff `f81896bae3..af1cd9f7d6` is 3 hunks, all in CONTRACTS:
- the enumeration-authority line
- the Schwab data reader paragraph
- the catalog reader paragraph

ENDPOINT is byte-unchanged, and so is the brief hash (`04461a4925dc`).

## What passes -- checked with the estate's own grader, not by reading the ruling

`lib/opal_naming.py`, called in this worktree:

| call | result |
|---|---|
| `name("gateway", None, "schwab-read", "role")` | `gateway-schwab-read-role` |
| `name("gateway", None, "schwab-catalog-read", "role")` | `gateway-schwab-catalog-read-role` |
| `name("gateway", None, "assume-schwab-readers", "policy")` | `gateway-assume-schwab-readers-policy` |
| `grade(<each of the three>, IAM_ROLE / IAM_POLICY)` | CONFORMANT, 3 of 3 |
| `grade("opal-mcp-emp-menachem-schwab-read", IAM_ROLE)` (control) | OUT-OF-PATTERN |

The grader discriminates: the old name fails and the new names pass. Moving the person out of the name and
into the trust ExternalId, the entitlement record and the tags is the right shape.

## DEFECT 1 -- CONTRACTS cites an authority version that does not exist at the pin

The section reads: *"The enumeration authority is `org/standards/NFRA_OPLGTW_CONTRACT.json`, version 1.1 (1.0 plus
the three role and policy names restated as builder output, below)."*

Measured at `af1cd9f7d6`:
- `contract_version` is **`1.0`**.
- The file still carries `opal-mcp-emp-menachem-schwab-read` and `opal-mcp-schwab-catalog-read`.
- Its last commit is `2af252cb39`.

R-OG-7 moves the JSON to v1.1 **in OG-i-3's order**, which has not run. So CONTRACTS asserts, in the
present tense, that its closed enumeration already holds names the enumeration does not hold. It is the
v0.3 DEFECT 2 class again: the section and its authority disagree, and an implementation that trusts the
first sentence reads the wrong file.

**CURE, either:**
- (a) Land the JSON bump to v1.1 before or with this PRD version.
- (b) State the sequence: *"version 1.0; the three names move to builder output as version 1.1 in the rename
  apply, with the Terraform declarations and the application's reference moved together, before any
  runtime consumer binds"*.

## DEFECT 2 -- a fourth typed name in the same section fails the same grader, and v0.6 does not say why it stays

CONTRACTS `:135` still types the access-state store: *"durably in `opal-gateway-access-state`"*.

- `grade("opal-gateway-access-state", DYNAMODB_TABLE)` returns **OUT-OF-PATTERN**, canonical
  `gateway-access-state-table`. It fails for the reason R-OG-7 gives for the roles: `opal` is reserved,
  so the system slot takes `gateway`.
- It is new to this project: applied by OG-i-1, ledger
  `20260915T2152Z_nfra-oplgtw-og-i-1-access-state_deploy_completion.md`.
- The typed name is carried in:
  - `infra/aws/terraform/opal-gateway/schwab_access_state.tf`
  - `app/access_state.py` (`TABLE_NAME`)
  - `app/oauth_as.py`
  - the contract JSON's `state_store.table`

So v0.6 brings three of the section's four new resource names to builder output, and says nothing about
the fourth. **This is not the same cost as the roles, and that is why it needs saying rather than silently
following.** The table is stateful and already has a runtime consumer (`oauth_as.py`). Its contract
record types include `operator_audit` under a "no TTL or ordinary delete" namespace. A destroy/create is
not free the way re-keying three IAM resources is. That makes it a CALL -- rename with a data move,
or a deliberate departure -- and the call is `1.0.0_SA_CTO`'s, not this seat's.

**CURE:** CONTRACTS states one of two things:
- the table's name is builder output (`gateway-access-state-table`), with its move sequenced and the stored
  records carried across; or
- `opal-gateway-access-state` stays under an R20 register entry Andrew acknowledges, with its reason.

Either way the section stops silently typing an out-of-pattern name beside a paragraph that just renamed
three others on exactly that ground.

## DEFECT 3 (minor, same bar as v0.3 and MDPF v2.4) -- annotation and history inside CONTRACTS

- *"(1.0 plus the three role and policy names restated as builder output, below)"*
- *"The three resources OG-i-2 applied under the earlier typed names ..."*
- *"(RULING R-OG-7)"*

The rename-before-bind requirement is operative and may stay. Say it as a constraint ("renamed in the next
apply of the same root, before any runtime consumer binds, with the contract JSON, the application's
reference and the Terraform declarations moved together"). The what-it-was-before and the ruling id
belong in the change note or the rulings record.

## Not a defect, recorded so no seat over-reads the design

A per-principal ExternalId on a scope-named role does NOT isolate one principal from another in IAM. The
assuming principal is always `opal-gateway-role`, and the Gateway chooses the ExternalId. Two principals
with the same approved prefixes have identical IAM reach through one role, and the application policy
(already stated in this paragraph) is what narrows them. That matches the prior design, since the Gateway
assumed the person-named role too. So nothing is widened, but the ExternalId is an audit binding, not an
isolation control.

`opal-mcp-audit` (brief `:208`, `:284`) predates this project, so Rule 30's non-application covers it.

-- 3.0.0_SA_CVO
