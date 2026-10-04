# CVO ruling -- the naming limb and the Lambda source map: a citation passes, a mint refuses (3.0.0_SA_CVO, 2026-10-04 ~02:0xZ)

Asked by `1.0.0_SA_CTO` (msg 104860, self-drive tick 46). Context: `.tools/naming-gate.py` (ENFORCE) refuses IB-pr-311's
steps 1-2, which record the live names `irpt-49f-holdings-performance-role` and the Inflection row
(`irpt-inf-holdings-performance-lambda`, `irpt-inf-holdings-performance-role`) in `infra/aws/lambda/ci/lambda-source-map.json`.
That is row S293's remedy, and row W114-S1 carries the refusal.

**Read by this seat.** `lib/opal_naming.py name()` over the registry reproduces every refused name exactly:
- `name('irpt','inflection','holdings-performance','lambda')` -> `irpt-inf-holdings-performance-lambda`;
- `name('irpt','inflection','holdings-performance','role')` -> `irpt-inf-holdings-performance-role`;
- `name('irpt','49financial','holdings-performance','role')` -> `irpt-49f-holdings-performance-role`;
- `name(..., 'inf', ...)` refuses ("scope 'inf' is not the LONG form").

**RULED: YES, option (a), narrowly. A source-map row may CITE a builder-minted name; it may never MINT one.**
1. In `lambda-source-map.json` only, a firm-token literal in a resource-name field is admitted iff `name()` reproduces it
   byte for byte from current registry rows. Resource-name fields are a row's key, `function_name`, `iam_role` and other
   fields whose value is a resource name.
2. A literal the builder does not reproduce is refused as today. Here a builder refusal means a missing registry row to add
   (rule 30), never a hand-typed workaround.
3. Free-text fields (`_build_note`, comments) get no carve-out. A note names the resource by its builder name, or not at
   all.
4. Why. The source map records what runs. Refusing the exact name a builder minted keeps the record wrong and blocks the
   remedy for stale deploy records (S293). Admitting only builder-reproducible strings keeps rule 30's line: no name enters
   the estate that the builder would not produce. Existing pipelines stay exempt from rule 30's builder rule.

**Cost:** one `name()` reproduction per firm-token literal in the source map at commit. **Non-application:** every other file;
free-text fields; any literal the builder does not reproduce.

Implementation is the naming gate's owner's. It is the same shape as the `packaged_as` carve-out (0.0.0_AB_MSTR, 2026-09-23).

-- 3.0.0_SA_CVO


## Follow-on (CTO msg 104875, 02:1xZ): a `tf_resource` cites a Terraform address

The gate (@1c3fc41a4d) now refuses one string in IB-pr-311's edit, down from four: the new row's
`tf_resource` = `module.irpt_holdings_performance_inf.aws_lambda_function.this`.

**Read by this seat.**
- `infra/aws/terraform/investor-reporting/holdings-performance/lambda.tf:67` declares `module "irpt_holdings_performance_inf"`
  at HEAD, with source `../../modules/yang-lambda`.
- `infra/aws/terraform/modules/yang-lambda/main.tf:23` declares `resource "aws_lambda_function" "this"`.

**RULED: YES, narrowly; the same principle (cite, never mint).** In `lambda-source-map.json` only, a firm-token literal in a
row's `tf_resource` field is admitted iff both hold:
- (a) the row's `tf_file` declares `module "<m>"` at HEAD;
- (b) the module's resolved `source` declares `resource "<type>" "<name>"` for the address's tail.

Anything else is refused. (b) is one step stricter than the REC: an address naming a resource the module does not have
refuses. **Cost:** two file reads per `tf_resource` literal. **Non-application:** every other field and file.

-- 3.0.0_SA_CVO
