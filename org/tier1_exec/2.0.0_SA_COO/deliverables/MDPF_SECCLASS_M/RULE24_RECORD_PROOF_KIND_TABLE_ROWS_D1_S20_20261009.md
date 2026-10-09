# Rule-24 record -- a `proof_of_spec` artifact kind for rows written to a DynamoDB table (row MDPF_SECCLASS-D1-S20)

**Author:** `2.0.0_SA_COO~M1`, dell1, 2026-10-09 ~09:4xZ. **Rules:** the laptop `1.0.0_SA_CTO` (routed by `1.0.0_SA_CTO~DELL1` msg 2168).
**Schema adopted:** `org/standards/PROOF_OF_SPEC.schema.json` `artifacts_produced/items/kind` (enum at :140-151). **Resolver:**
`.tools/proof-of-spec-check.py` :402 and :417, where `s3_object` is the only kind that skips the git `(commit, path)` resolution.

## The proposal

1. Add one enum member, **`ddb_rows`**: rows a DEPLOY-genre act wrote to a DynamoDB table. `path_or_key` is
   `dynamodb://<region>/<table>`, plus the key list or the set file that names the keys. `commit_or_etag` is the snapshot
   file or the read-back record, never a git pin.
2. In the resolver, treat `ddb_rows` like `s3_object`: count it, then skip git resolution. Truth is held by the order's own
   read-back criterion, exactly as for S3.

A second member, `lambda_function`, has more de-facto use than this one (see the census). It is named under postulate (i)
and **not** proposed here: one value per proposal, and the ruling seat decides whether to widen.

## The census (denominators printed)

Every `*.proof_of_spec.json` under `org/`, read 2026-10-09 on box/dell1: **2,750 instances, 0 unparsed, 13,515 artifact rows.**

| kind | rows | in the enum |
|---|---|---|
| script | 3,879 | yes |
| doc | 3,595 | yes |
| test | 2,481 | yes |
| config_data | 1,659 | yes |
| frontend_component | 1,059 | yes |
| s3_object | 424 | yes |
| terraform | 344 | yes |
| iam | 55 | yes |
| schedule | 9 | yes |
| **lambda_function** | **5** | **no** (AMGT_RESAPP, 0.7.0_AE_CloudOps~A, 5 redeploy orders) |
| **file** | **2** | **no** (AMGT_RESAPP) |
| **iam_inline_policy** | **2** | **no** (ETFS_RIVALS TO-RIV-iam-1) |
| **record** | **1** | **no** (AMGT_RESAPP TO-AMGT-am-7, a management-objects write) |

- **Instances whose text names a DynamoDB write surface** (`dynamodb`, `put_item`, `batch_write` or `etf-classifications`): 233 of
  2,750. That is an upper bound on orders that touch a table; it is not a count of table-write products.
- **Word-boundary token census** of the proposed name and five near forms (`table_rows`, `ddb_rows`, `dynamodb_rows`, `table_row`,
  `ddb_item`, `dynamodb_item`) over `.tools/**/*.py`, `org/standards/**/*.json` and `docs/**/*.md` (1,545 files): **0 hits each.** No
  collision, and no existing reader keys on the name.

## The four postulates

**(i) MECE over a declared domain.**
- **Domain:** the products an L7 act can leave behind, on any substrate the fabric writes.
- **Hunted by subtraction from the census above, not by a forward list.** 10 rows (4 kinds) already sit outside the enum. The
  subtraction finds the domain WIDER than this row claims. Every off-enum member names a non-git cloud product:
  - a Lambda deployment;
  - an inline IAM policy (covered by `iam`; a mis-declaration);
  - a generic file (`config_data` or `doc` fits; a mis-declaration);
  - a written record set (`record`, the same class as this proposal).
- **Uncovered after this proposal:** `lambda_function`, which is named above and left to the ruling seat. With `ddb_rows`, the
  enum covers both cloud data substrates this project writes (S3 objects and table rows).

**(ii) Same grain.** `ddb_rows` sits at the same grain as `s3_object`: one substrate's written product, keyed by the substrate's own
address. It is not a grain coarser than its siblings (it is not "cloud state"), nor finer (it is not "one etf-classifications row").

**(iii) Intent coherence.** The enum's one axis is *what substrate holds the product, and so how the checker resolves it*. The new
member answers that axis and no other. Its one intent is to let a table-write order declare its true substrate and still validate.

**(iv) State coherence.** These values one remedy does NOT move:
- the 9 existing members, and the 13,505 rows declared under them;
- the 10 off-enum rows already in the tree (their own re-declaration is a separate act by their issuers);
- the artifact-coverage heuristic, which stays scoped to `script` and `s3_object`;
- `lambda_function`'s status.

The remedy moves one schema enum and one resolver branch.

## What the precedent did (the cost of no member)

`0.7.0_AE_CloudOps~SC1` closed `MDPF_SECCLASS.TO-SC-e71b` (15 rows of `etf-classifications`) by pinning the seed source as
`config_data` and stating the real product in `deploy_evidence`. The record is honest but its kind is a stand-in. Every later
row-write order (SC-e-83's one-row write is next) repeats that stand-in until the enum has a member.
