# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain T (tools). One co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_T_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; the worker reads BOTH before its first live act and STOPS with a
BLOCKING row if either is absent or lacks the `AMGT-rk-61` section. `rk-55`..`rk-60` write tools, tests and skill text;
none moves served output (`rk-59`'s Terraform edit is a plan-time expression change with an IDENTICAL value when the zip
is present, NO apply named; a plan diff on the function is recorded as pre-existing drift, never applied) and none is
co-signed.

## `AMGT-rk-61` -- the router is slash-indifferent on the security arm; redeploy (R14-T7; W27-S10, FWD-13) -- the LAST cell in the adapter single-writer queue

**THE ACT.** ONE redeploy of `opal-amgt-scoped-api` from THIS worktree's bytes, cut from HEAD after `AMGT-rk-53` drains
(so the artifact also carries `rk-53`'s `generation_fields` / `_ranking_reason` change -- the chain L half names it):
`build-and-upload-scoped-amgt.sh` -> artifact `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
(a new VersionId), ONE targeted `safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this` (0 destroy; a non-zero
destroy is a STOP), under a change-management entry opened BEFORE the build with its sentinel COMMITTED.

**BLAST RADIUS -- what the act MAY touch, and nothing else.** The code of ONE function, `opal-amgt-scoped-api`: the
`handler()` security arm (`scoped_amgt.py:3315-3324`) becomes `len(rest) >= 3`, `leaf = rest[-1]`, `requested =
unquote("/".join(rest[1:-1]))`, so a security key carrying a slash (`BP/_LN_Equity`, `NG/_LN_Equity`, row W32-S3) resolves
the same whether it arrives encoded or raw. NOT touched: the route table and the gateway route set (the HTTP API routes
are single-segment `{security_key}` with no `{proxy+}` -- `scoped-amgt-api.tf:286-308` -- so a literal slash never reaches
the Lambda through the gateway; indifference is proven IN-PROCESS and by DIRECT INVOKE, and the route set is deliberately
left alone because a `{proxy+}` route would change precedence and the authorizer surface, a wider radius no half signs);
the function's environment, layers, timeout (29), memory (512); the role policy; any other function; any pool object.

**WRITER CENSUS: N = 1 writer of the artifact key** (`build-and-upload-scoped-amgt.sh` + the targeted apply; never
`update-function-code`) **and N = 1 writer of the function's code** (the same apply). The ADAPTER SINGLE-WRITER QUEUE
guarantees no other round-14 cell holds adapter bytes in flight: this cell is the LAST of six (`rk-43` -> `rk-45` ->
`rk-53` -> `rk-61` -> `rk-36` -> `rk-37`; `rk-36`/`rk-37` come after it by the M chain's own edges), and its pre-build
`git log <merge-base>..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` MUST print nothing or the worker STOPS.

**EXPECTED OUTCOME, both branches (read from the new arm as the order inlines it, section 1).** The 13-route census: 13 of
13 `200` pre AND post, `LOST=[] GAINED=[]`. The six slash pairs by direct invoke (encoded and raw for each of three keys,
`BP/_LN_Equity` and `NG/_LN_Equity` among them): each pair returns EQUAL payloads post-act (pre-act the raw form 404s --
that is the defect, recorded as the baseline); a key with no slash returns byte-equal payloads pre and post. `rk-53`'s
`empty_reason` key appears in the rankings payload post-act (a key gained; no figure moves -- the chain L half). If the
targeted apply refuses (non-zero destroy, plan drift on a resource outside the target, a stale-bytes print): NOTHING is
applied, the criterion FAILS naming the refusal, the artifact upload is rolled back by the mechanism below.

**PER-KEY ROLLBACK, from the live pre-act state THIS worker measures FRESH.** Pre-act: `get-function-configuration`
`CodeSha256` and the artifact's current `VersionId` (`list-object-versions`, IsLatest true), plus `get-bucket-versioning`
reading `Enabled` (MEASURED by the issuer 2026-09-18 ~22:4xZ; re-measured into the entry), all recorded BEFORE the build.
Rollback = restore the pre-act bytes as the CURRENT version -- `s3api copy-object` from the pre-act VersionId onto the same
key -- then the SAME targeted `safe-apply`; `get-function-configuration` must print the pre-act `CodeSha256` again. The
module (`infra/aws/terraform/modules/yang-lambda/main.tf:17-20`, `:38`) resolves the CURRENT artifact version and is NEVER
edited (CTO msg 23830). No pool key moves, so no data rollback.

**NOT COVERED:** any route-table or gateway change; a `{proxy+}` route; a second redeploy; any IAM change; any pool
write; a deploy from bytes behind the shared branch.

**Sequencing:** `rk-61` after `rk-53` (adapter queue) AND after `rk-59` (the harvest-root Terraform plan hits W34-S1 unless
`rk-59`'s `fileexists()` expression has landed; the order carries the `build_zip.py` fallback if not).

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.
