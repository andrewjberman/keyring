# COO never-widen half -- NFRA_CTLPLN: the Dell group reads four named vendor secrets (one apply of the Dell identity root)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~22:5xZ. **Read at:** trunk `3f19f5c377`; the cell merged @22c49c71e2 (CT-a-1 AMENDMENT 5).
Root `infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half for this same act. **Authority:**
`1.0.0_SA_CTO` msg 106535: "Measure which vendor secrets the Dells' placed projects need, and send one half request granting the
Dell group read of exactly those", on Andrew's word as recorded
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md`
item 4): "Vendor egress does not count as raw internet access; those are protected channels. The Dell Boxes have vendor egress
as needed." This seat read that record and did not hear the word itself.

## The act

One `safe-apply` of the root, untargeted, at the laptop, from a commit that contains `22c49c71e2`.

## The plan, MEASURED

`terraform plan -lock=false -detailed-exitcode` on the laptop, 2026-10-07 ~22:5xZ, read-only, exit 2:

```
  # aws_iam_group_policy_attachment.dell_agent_vendor_secrets[0] will be created
  # aws_iam_policy.dell_agent_vendor_secrets[0] will be created
Plan: 2 to add, 0 to change, 0 to destroy.
```

One statement, `ReadNamedVendorSecrets`: Allow `secretsmanager:GetSecretValue` on exactly four full ARNs, no wildcard:
`astn/brightdata/residential-proxy`, `astn/kimi/api-key`, `openai-api-key`, `ycharts/login/credentials`. Terraform builds it from
the census file under `tests/` (the form the CTO ruled for the routes Deny), so no policy file holds a name.

**Writers of the property (what the two Dell users may do): N = 9 documents after the act**, the eight read at the earlier
applies plus this one. The Dell group then carries 6 managed policies (limit 10).

## Blast radius

Two IAM objects. The act changes what the two Dell users may READ and nothing else; no other principal changes.

**What both Dell users gain (the widening):** the VALUE of four secrets. Today the group can read no secret's value. Each is a
credential for an outside service: a model provider's key (Kimi), a second model provider's key (OpenAI), the firm's sign-in at
a market-data vendor (YCharts), and a proxy provider's credential (Bright Data). A box that holds the value can call that vendor
as the firm, from anywhere, until the key is rotated: detaching the policy later does not un-read a key.

**How the four were chosen, and what was left out:** by NAME ONLY (no secret value was read by any seat). 114 secrets exist, all
in one region of 17 listed. 15 projects are placed on a Dell by their own project rows. Their code references 40 secrets. A
secret is in the grant only when it is a vendor credential AND a program of a Dell-placed project reads it by name: 4. 13 are
not vendor credentials (signing keys, internal bearer tokens, seeds). 23 are UNSURE and NOT granted: vendor keys no program
reads, client-firm or tenant logins, captured session bundles, the firm's own directory app credential, and three bundles with
no description. They are listed in the plan note for a person to rule.
**Limits of that measurement, stated:** 74 call sites name no literal secret (the name is built at run time), 22 of them in
files a Dell project's orders cover: a secret reached only that way is unseen. Four placed projects have no task-order paths
yet and so join nothing.

**Three things this half names so they are not read as covered:**
1. **The OpenAI key and the standing whitelist.** The census found the standing vendor whitelist scopes OpenAI to one project
   (ETFS_RIVALS), while four programs of MDPF_SECCLASS, a dell1 project, read `openai-api-key` (row `NFRA_CTLPLN-W14-S8`).
   This grant lets a Dell READ that key. It does not decide whether MDPF_SECCLASS may call that vendor; his word of 18:3xZ says
   "as needed" for the Dell boxes and does not name vendors. The CTO weighs whether that key stays in the grant.
2. **Writes are untouched.** Both Dell users can already WRITE any secret's value (`secretsmanager:PutSecretValue` on `*` in the
   create policy; the simulator reads it allowed with and without this document). This act neither grants nor removes that.
3. **Where the readers run.** Several of the programs that read these keys run on a pipeline host or a function, under that
   host's own role, not from a Dell. The grant is for the runs a Dell seat makes itself.

**Evidence, issuer's own re-runs in the worker's tree:**
`POLICY-SIM ... ssm_ok=9/9 routes_ok=5/5 vendor_ok=19/19 all_ok=True` (both Dells allowed on the four; refused on a not-vendor
secret, an UNSURE secret, an unrelated secret and a vendor name with a wrong suffix; without the new document the same four
read refused); `VENDOR-SECRETS secrets=114 referenced=114 dell_projects=15 placement_inferred=False vendor=4 not_vendor=13 unsure=23 granted=4 ok=True`;
each resource entry matches exactly one listed secret; all four are under the account's default key, so no key policy is
touched; proof VALID.

## Expected outcome, BOTH branches

- **A:** the applier's plan reads exactly the two creations above, the statement naming exactly those four ARNs with the one
  action -> apply.
- **B:** any other line or count, a fifth ARN, a wildcard, another action -> apply NOTHING and report.

## Rollback

Detach and delete the policy (remove the pair and `safe-apply`, or detach in the console the same window). A key a Dell has
already read stays read: the only full rollback of a read is rotating that key at its vendor.

## Conditions

1. The plan shape of branch A, read immediately before the apply.
2. `tests/derive_vendor_secrets.py --from-file tests/vendor_secrets_census.json` and `tests/simulate_policy.py` read `ok=True`
   and `vendor_ok=19/19` immediately before the plan.
3. A NEVER-2 ledger entry opened and closed, naming the four secrets by name (never a value).
4. Read-back LIVE by the simulator against the ATTACHED policies: both Dell users allowed `GetSecretValue` on each of the four;
   refused on one not-vendor secret and one UNSURE secret, each named; a re-plan reads no changes. The applier reads NO secret
   value.
5. The exercised read is a Dell's own, by another route: one Dell program that uses one of the four runs and reaches its
   vendor. Until then the grant is APPLIED, not EXERCISED.
6. A fifth secret is a new census class and a new plan, never an edit under this half.

**SIGNED** -- `2.0.0_SA_COO~C`
