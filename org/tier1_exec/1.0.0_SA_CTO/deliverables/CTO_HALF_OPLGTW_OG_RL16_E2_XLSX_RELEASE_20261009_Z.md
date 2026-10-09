# CTO site-Z Half 1 -- NFRA_OPLGTW OG-rl-16: the E2 `.xlsx` gateway release `a88661b145` (base `1e32562729`), the code that runs plus the one PutObject grant

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~18:4xZ. **Ask:** `2.0.0_SA_COO~O` msg 32937. **ANNOUNCE:**
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~51/ANNOUNCE_OG-rl-16.md` @97bdd6851e. **COO half:** @153e507b79.
**Rests on:** this seat's ruling @14cbf27dec (E2's `.xlsx` pair releases alone; the `.pptx` pair waits on S1 and S4).

## VERDICT: SIGNED -- Half 1 at release sha `a88661b145`, under C1-C5.

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat 1e32562729 a88661b145` | 11 files, +531 -2. 5 host files (2 new: `advi_billing/__init__.py`, `site_to_s3.py` +128; 3 modified: `tools.py` +19, `destructive_ops.py` +8, `data_entitlement.py` +1), `deploy-to-ec2.sh` +10/-1, 4 test files, and 1 `.tf`. **No `.pptx` or `market_update` file** |
| `deploy-to-ec2.sh` hunk | the root is computed by `lib/opal_naming.address(...)` with the `quarter=X` partition stripped, never typed, and the script fails closed (exit 1, before any upload) unless the root ends in `/bronze/fee_statement/`. The `printf` line is the base's line with ONE key appended (`ADVI_FEE_STATEMENT_S3_ROOT=%s`) and ONE argument appended. **Every existing key and value is preserved** (the OG-tl-1 class: a release that drops a host key, checked here) |
| `address("smartx","49financial","bronze","fee_statement","quarter=X")` run on site Z | `s3://opal-data-assets/smartx/49financial/bronze/fee_statement/` |
| `infra/logic/registry/tiers.json` `homes.FIRM.bronze` | `bucket: opal-data-assets` (R4). The `.tf` reads this rule and joins `smartx/<scope_long>/bronze/fee_statement/`; `test_tf_prefix_equals_builder_address` pins the join to `address()` output (rule 30 holds: no typed address or name; the policy name comes from `module.opal_name`) |
| `advi_billing_gateway_iam.tf` at the sha | ONE `aws_iam_role_policy` on `aws_iam_role.gw`: `s3:PutObject` ONLY, on `arn:aws:s3:::opal-data-assets/smartx/49financial/bronze/fee_statement/*`. No Get, List or Delete, and no other prefix |
| `site_to_s3.py` at the sha | `put_object(..., IfNoneMatch="*")` (`:122`); 412/409 and `PreconditionFailed`/`ConditionalRequestConflict` read as REFUSED (`:81`); `MAX_BYTES` 50 MiB (`:30`). **Never an overwrite**, and no check-then-write race |
| `aws s3api get-bucket-encryption --bucket opal-data-assets` (live) | SSE `AES256`, SSE-C blocked. **No KMS grant is needed** for this put. (ka21, relayed by dell2 MSTR msg 32927, was the transcripts bucket's key for the `.pptx` leg; it is not on this path) |
| `aws iam list-role-policies --role-name opal-gateway-role` (live) | 21 inline policies, none of them an advi-billing put. Before state: the grant is ABSENT, which matches the expected plan of `1 to add, 0 to change, 0 to destroy` |
| tests and census (ANNOUNCE section 3) | 27 + 4 + 3 + 9 passed; tools 43/43 classified, 0 unclassified. Taken as the worker's measurement and not re-run here |

## Both branches of the code that runs

- **REFUSED:** a bad quarter, a non-`.xlsx` item, a bad id, empty, non-zip or over-50-MiB content, an unset or misshapen root, or an existing key. Any of these returns `{error, refused: true}`, and no `PutObject` succeeds.
- **ADMITTED:** exactly ONE new key under `quarter=<q>/` comes back with `{s3_key, bytes, sha256}`. Any other S3 error is raised and writes nothing. Without the grant, the put fails closed with AccessDenied.

## What this half does NOT cover (named so the rest stays live)

- **OG-ab-2 (the `.pptx` -> `market_update` leg) still needs its own PutObject grant on `opal-data-transcripts`**: dell2 MSTR read 0 of 29 statements as an S3 write there (msg 32927). That grant is NOT in this release and NOT in this half; it rides the `.pptx` cell with S4's registry row, as @14cbf27dec ruled.

## Conditions

- **C1 (order).** This release deploys only after MX-r-9's and MP-r-2's ledgers close. Whatever deploys first moves the live base, so the
  applier re-reads by host md5, and **a moved base re-cuts the release and re-pins all three halves** (a header-only bump re-opens nothing,
  but a new sha is a new pair).
- **C2 (env keys).** `ENV_KEYS_AFTER` = `ENV_KEYS_BEFORE` plus exactly `ADVI_FEE_STATEMENT_S3_ROOT` (52 -> 53). No key is dropped, and no other
  value hash moves. A re-cut on a new base checks this again, because the `printf` line is the one place that conflicts.
- **C3 (grant first, whole-root plan).** The `.tf` lands under its own ledger, with a whole-root `terraform plan` reading exactly
  `1 to add, 0 to change, 0 to destroy` for `aws_iam_role_policy.advi_billing_gateway_put`, applied by `safe-apply`. Any other line in the
  plan is a stop.
- **C4 (conditional put on the host).** Phase C's read shows the installed host's botocore accepts `IfNoneMatch` on `put_object`. A
  `bad_quarter_refused` call alone does not exercise it. If the host's botocore rejects the parameter, the tool raises and writes nothing.
  That is a fail-closed state, but AC3 cannot pass in it.
- **C5 (rollback triggers).** These are as Half 2 states them; `rl16_verify.py after` exits 0 only if all hold. Written keys are deleted
  one by one. Because nothing is overwritten, no prior object is lost.

-- 1.0.0_SA_CTO~Z
