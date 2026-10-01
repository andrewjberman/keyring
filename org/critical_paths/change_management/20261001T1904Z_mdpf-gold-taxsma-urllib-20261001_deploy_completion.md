# Deploy Completion Record
**Date opened:** 2026-10-01T19:04:06.456409+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T190933Z
**Deploy:** MDPF_TAXSMA fix inside the activation: mdpf-gold-lambda from pin 335430e793 (CodeSha256 9YL45zw0.., S3 version J34f45wQHVHOaZUAvogvIKJJRxjaWCzd) to pin 0f1a67e196 (zip sha256 c0a7e04c.., expected wKfgTBeq..): the Gateway call on the standard library (the activation's first dry run failed: no httpx in the runtime); Tax ENABLED; halves CTO @1b43d6f201 (+@5f39857797), COO @07d269eb28
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the built zip uploaded | downloaded back, sha256 c0a7e04c17aaeb20a21fc308f97b6d6119b2b546a7ad8f8e701c639501a6688a equal; prior version recorded | Uploaded 19:06Z: VersionId 5uNyXSXz9cl2d9weCs5CWwUGyCi3va2A; downloaded back by that VersionId: sha256 c0a7e04c17aaeb20a21fc308f97b6d6119b2b546a7ad8f8e701c639501a6688a = the built zip (pin 0f1a67e196, urllib present, no httpx import) = the metadata. Prior version J34f45wQHVHOaZUAvogvIKJJRxjaWCzd is the rollback target. | CLOSED 20261001T190932Z |
| P1 | verify | saved plan of mdpf-pipeline | 0/1/0: code, hash and MDPF_GOLD_COMMIT only; the four TAXSMA_ keys unchanged | Saved plan 19:06Z: 0/1/0 = aws_lambda_function.mdpf_gold: s3_object_version J34f.. to 5uNy.., source_code_hash f582f8e7.. to c0a7e04c.., MDPF_GOLD_COMMIT 335430e793 to 0f1a67e196; the four TAXSMA_ keys unchanged. | CLOSED 20261001T190932Z |
| D1 | activation | safe-apply | CodeSha256 wKfgTBeq6yCiH8MI+XttYRmytUanrY+OcBxjlQGmaIo=; re-plan No changes | safe-apply complete 19:07:14Z, 0/1/0. CodeSha256 wKfgTBeq6yCiH8MI+XttYRmytUanrY+OcBxjlQGmaIo= = base64 of the zip sha256; Active; Successful; re-plan No changes. | CLOSED 20261001T190932Z |

## Log

- 20261001T190406Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
- 20261001T190932Z LEG U1 closed: Uploaded 19:06Z: VersionId 5uNyXSXz9cl2d9weCs5CWwUGyCi3va2A; downloaded back by that VersionId: sha256 c0a7e04c17aaeb20a
- 20261001T190932Z LEG P1 closed: Saved plan 19:06Z: 0/1/0 = aws_lambda_function.mdpf_gold: s3_object_version J34f.. to 5uNy.., source_code_hash f582f8e7.
- 20261001T190932Z LEG D1 closed: safe-apply complete 19:07:14Z, 0/1/0. CodeSha256 wKfgTBeq6yCiH8MI+XttYRmytUanrY+OcBxjlQGmaIo= = base64 of the zip sha256
- 20261001T190933Z CLOSED -- all 3 legs proven
