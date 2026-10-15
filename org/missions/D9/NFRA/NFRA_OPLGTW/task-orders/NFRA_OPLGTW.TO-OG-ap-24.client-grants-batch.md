# NFRA_OPLGTW task order -- `OG-ap-24` -- APPLY (grants): the vendor read roles of the G2 client adapters, as ONE batch (PRD v3.12, CTO msg 34552)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-24</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-24</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: six vendor read roles (five NEW, one EXTENDED) and two policies on existing roles; every statement is `s3:GetObject` and a prefix-confined `s3:ListBucket` (or the existing news and  actions), no `*` resource, no Put or Delete. The role set is `G2_ROLES.json`'s `new_or_extended_roles` (the CRO's census measured the live account); this cell regenerates it from the MERGED adapter modules and the catalog rows.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's GO (msg 34552, PRD v3.12 @532d1e68bb: "re-issue the IAM and grant cells to ~ZS in parallel with code on ~Z"; Andrew-direct ~19:2xZ "We have usage, run it now") on the G2 plan of PRD v3.1 Rulings 1-5 and v3.2.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-24` (decomposition addendum R3-T.73, workstream GRANTS-BATCH, FWD-22)

The G2 client adapters (`OG-cl-1..6`, built and merged) read client data from `opal-data-assets/<vendor>/<firm>/silver/` (and, for 49F Black Diamond, the live `opal-data-bd/silver/`). **Client data NEVER reads through `gateway-global-internal-reader-role`** (PRD v3.2): each vendor has its own role, assumed only by the gateway's instance role, prefix-conditioned to that vendor's own key segments. The code reads each role's ARN from an environment variable named in `app/client_role.py` (read that file: it is the table vendor -> variable name; the `.env` names are the CODE release's, `OG-ap-23`, not this order's).
You are the SECOND applier: IAM and Terraform here, in parallel with the code release on `0.7.0_AE_CloudOps~Z`. The host stays one deploy at a time; this order never deploys.

### PHASE A (files, plan, ask; NO apply IN ANY FORM, a negative check is a plan and its output is KEPT)

1. **Read the live state first.** `get-role` and `get-role-policy` for `gateway-blackdiamond-read-role` and `gateway-schwab-read-role`, and list the roles named `gateway-*-read-role`. Print the denominator. Write `W/GR_BEFORE.json` = `{"read_at": "<iso>", "roles_present": [...], "bd_policy_sha256_16": "<sha>"}`.
2. **Write the generator** `W/gr_grant_gen.py`: it reads (a) the merged adapter modules `app/client_adapter_*.py` and finds, by AST, every `(vendor, segment, layer, table)` they pass to `ctx.prefix(...)` (a name bound to a constant is resolved; a call the AST cannot resolve is printed and is a STOP), (b) the DATA_CATALOG rows (`app/refs/DATA_CATALOG.yaml`) to turn each into the `bucket` and key prefix, and (c) `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/G2_ROLES.json` for the role names and the fence kinds. It prints, per role, the exact `s3:GetObject` ARNs and the `s3:ListBucket` `s3:prefix` values. A table the adapters read with NO catalog row is listed as a GAP (the catalog release `NFRA_MCPINDEX` adds the Schwab `dim_*` rows; do not invent a key). `--check` regenerates and diffs against the committed `.tf`: exit 0 only when equal in both directions.
3. **Write the Terraform** `infra/aws/terraform/opal-gateway/client_vendor_roles_iam.tf`: ONE role per vendor (`gateway-blackdiamond-read-role` EXTENDED with the `opal-data-assets/blackdiamond/49f/silver/` tables in addition to its existing `opal-data-bd` statement, which stays byte-for-byte; NEW `gateway-cot-blackdiamond-read-role`, `gateway-inf-orion-read-role`, `gateway-inf-eclipse-read-role`, `gateway-cot-commonwealth-read-role`, `gateway-smartx-read-role`; `gateway-schwab-read-role` stays as it is: read its policy and state in the ask that it already covers the `dim_*` and `fact_*` Schwab prefixes, or name the gap). Names come from `lib/opal_naming.py` (`name()`), written as literals the naming limb can grade; new legacy-form prefixes go through the `legacy_addresses.json` registry route (commit the rows FIRST, on their own, then the `.tf` with ONE file under `org/missions/D9/NFRA/NFRA_OPLGTW/`; the CTO's naming clause admits the name only, never the access). Trust: each new role is assumable ONLY by the gateway instance role (copy the trust block of `gateway-schwab-read-role`'s Terraform; read it, never hand-type a principal). Actions exactly `s3:GetObject` and `s3:ListBucket`; ListBucket confined by `s3:prefix` to the vendor's own key segments; no `*` resource, no bucket-wide object ARN, no Put, no Delete.
4. (WITHDRAWN by A1) The person-roles Terraform (the news policy on the internal reader and the  policy) stays in `OG-ap-21`, which is NOT superseded: it goes to release first, on the live ref after MX-r-14, so the person reader reaches `NFRA_MCPORTAL` tonight. Do not write or touch `news_read_internal_iam.tf`, `harvest_published__iam.tf` or `news_read_iam.tf`.
5. **The plan**, targeted, `-lock=false`, no `-out`, no apply: it must read `N to add, M to change, 0 to destroy`, with N and M stated from the files: 5 roles + their policies and the BD extension as ONE change. Save it as `W/GR_PLAN.txt` and keep the output of every negative check. Any other change is a STOP.
6. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-24.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file; (2) the `widening`, stated plainly, ONE block per role: who gains what, on which prefixes, for which firm; SmartX's role reads objects that hold FOUR firms (IAM cannot fence them; the code filters rows on the roster, with a two-firm negative arm: say it); the Commonwealth role reads a CLOSED delivery; the 49F role also reads the live `opal-data-bd` silver; (3) the `tools` that use each role (the five `client_*` tools route by vendor); (4) the `order` of acts (the grants applied ONE role at a time, each read back from IAM, BEFORE the code deploy `OG-ap-23`); (5) `both branches` (a refused call reads zero; an admitted call reads one capped partition); (6) the `rollback` per role (delete the new role and its policy; the BD extension removed from the statement or the prior document restored, its sha256 in `GR_BEFORE.json`; the  policy destroyed targeted); (7) the `triggers`; (8) the GAPS (tables without a catalog row). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed)

7. Ledger `nfra-oplgtw-grants-ap24`, entry AND sentinel first. Apply the roles ONE at a time through `safe-apply`, targeted, each read back from IAM (`get-role`, `get-role-policy`); on a trigger failing, destroy what this ask added and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/GR_APPLIED.json` = `{"roles": {"<role>": {"state": "live", "policy_sha256_16": "<sha>"}, ...}, "_policy_live": true}`, commit, run AC2, report once.

## 2. BOUNDS

- IAM and Terraform of the named roles and policies only. No object or item is written to or deleted from any bucket or table; no deploy; no catalog edit.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form (including `-auto-approve`, a `-target` apply or an `apply` inside a conditional or a pipe: a negative check is `plan`-only and its output is kept); print a role's credentials, an account number or an object's content.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/client_vendor_roles_iam.tf
infra/aws/terraform/opal-gateway/harvest_published__iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ap24.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-24"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap24.AC1.sh; echo "exit=$?"</invocation><expect>(?s)generator --check exit 0 \(want 0\); roles in the .tf [5-9] \(want at least 5\); wildcard resource 0 \(want 0\); put or delete in actions 0 \(want 0\); trust principals other than the gateway role 0 \(want 0\); plan: [0-9]+ to add, [0-9]+ to change, 0 to destroy.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-24"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap24.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; roles live in IAM 6 of 6;  policy live yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the grant `.tf` equals what the generator derives from the merged adapters, five role resources in the new .tf (the sixth, the Black Diamond role, is extended in `blackdiamond_reader_iam.tf`), no wildcard, no Put or Delete, trust only the gateway role, and the plan reads no destroy. `AC2` (Phase B): the roles are live in IAM, each read back, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-24.client-grants-batch.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream GRANTS-BATCH (decomposition addendum R3-T.73). PRD v3.12 @532d1e68bb; CTO msg 34552: ask each grant as soon as its plan reads, he signs on receipt; client data off the global internal reader; done by 10-16 ~22:00Z. `OG-ap-21`'s Terraform (steps 1-2, `9b3660631b`) moves here; `OG-ap-21` is superseded by this order plus the code batch `OG-ap-23`.
- The seat: `0.7.0_AE_CloudOps~ZS` (idle; the second applier, so grants run beside the code release on `~Z`). The GO for Phase A is the issuer's message citing this order, sent when `OG-cl-1` (the core and the role client) is merged, because the adapters are the generator's input.
- Pre-cut: ap24.AC1 and ap24.AC2 base FAIL as expected (the `.tf`, the generator and the ledger are absent).

- A1 (issuer, 2026-10-15 ~20:2xZ): `NFRA_MCPINDEX` MX-r-14 went live at `c4c106aea1` (19:50Z) and `OG-ap-21` (the person reader and its Terraform) is going to release on it NOW, ahead of the batch, so `NFRA_MCPORTAL` is unblocked tonight. Therefore the person-roles Terraform stays in `OG-ap-21` and is WITHDRAWN from this order (item 4); this order is the six vendor roles only. `OG-ap-21` is not superseded; `OG-ap-22` is, by the code batch. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-15 ~23:4xZ, `0.7.0_AE_CloudOps~ZS` msg 34610, `PHASE_A_FINDINGS.md`): TWO RULINGS. (1) THE BD EXTENSION IS AN EDIT, NOT A SECOND POLICY: the live `gateway-blackdiamond-read-policy` carries explicit Denies outside `opal-data-bd/silver/fees/*`, and an explicit Deny beats any Allow, so the `opal-data-assets/blackdiamond/49f/silver/` read is added by editing `bd_read_policy` in `infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf`, which is now in `<paths>`. The edit widens the `NotResource` of the two Deny statements and the Allow by that ONE prefix and nothing else (no new bucket, no `*`); the plan shows it as `1 to change`. The ask states it as a change to a LIVE role's policy, with the before sha (`4893211d4408180a`) and the rollback (re-apply the before policy). (2) THE NEW .tf HOLDS FIVE ROLE RESOURCES: `aws_iam_role.bd_read` is declared in `blackdiamond_reader_iam.tf`, so a sixth declaration would be a duplicate address. AC1 wants 5 `aws_iam_role` resources in `client_vendor_roles_iam.tf`; the six-roles count is read at AC2 in IAM (6 of 6, unchanged). Schwab: the grant stays at the 12 `dim_*` prefixes the adapter reads (OG-cl-1 reads `dim_*` and substitutes no `fact_*`); the absent `fact_*` coverage is a NAMED GAP in the ask (catalog rows MX-c-23, release MX-r-15), not coverage. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-15 ~23:4xZ, `0.7.0_AE_CloudOps~ZS` msg 34612, supersedes item (1) of A2): THE BLACK DIAMOND ROLE IS KEYED BY FIRM. `client_core` derives the vendor role key from the prefix's first segment, so both BD firms (49financial and cottonwood) would read through one `BLACKDIAMOND_READER_ROLE_ARN`: IAM could not fence the firms apart. RULED (option b): the code keys the BD role by firm (cell `OG-ch-1`: env `BLACKDIAMOND49F_READER_ROLE_ARN` and `BLACKDIAMONDCOTTONWOOD_READER_ROLE_ARN`; every other vendor keeps its vendor key), ahead of `OG-ap-23`. The live `gateway-blackdiamond-read-policy` is NOT edited and the live BD role is NOT widened; `blackdiamond_reader_iam.tf` stays in `<paths>` only for a Cottonwood delta the issuer rules separately. The new `client_vendor_roles_iam.tf` holds one role per role key the generator derives from the merged adapters (a `blackdiamond49f` role is new). For the Cottonwood key the live role is reused ONLY if the generator proves its policy covers the prefixes that adapter reads; otherwise the delta is asked of the issuer, one ask. AC1 reads `roles >= 5` in the new `.tf`; `gr_grant_gen.py --check` (the `.tf` equals what the generator derives from the merged adapters) is the equality. Schwab stays at the `dim_*` prefixes its adapter reads; the absent `fact_*` coverage is a NAMED GAP in the ask (MX-c-23, MX-r-15). Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>GRANTS-BATCH</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
