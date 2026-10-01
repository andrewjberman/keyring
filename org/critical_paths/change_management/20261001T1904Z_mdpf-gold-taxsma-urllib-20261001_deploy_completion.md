# Deploy Completion Record
**Date opened:** 2026-10-01T19:04:06.456409+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA fix inside the activation: mdpf-gold-lambda from pin 335430e793 (CodeSha256 9YL45zw0.., S3 version J34f45wQHVHOaZUAvogvIKJJRxjaWCzd) to pin 0f1a67e196 (zip sha256 c0a7e04c.., expected wKfgTBeq..): the Gateway call on the standard library (the activation's first dry run failed: no httpx in the runtime); Tax ENABLED; halves CTO @1b43d6f201 (+@5f39857797), COO @07d269eb28
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the built zip uploaded | downloaded back, sha256 c0a7e04c17aaeb20a21fc308f97b6d6119b2b546a7ad8f8e701c639501a6688a equal; prior version recorded |  | OPEN |
| P1 | verify | saved plan of mdpf-pipeline | 0/1/0: code, hash and MDPF_GOLD_COMMIT only; the four TAXSMA_ keys unchanged |  | OPEN |
| D1 | activation | safe-apply | CodeSha256 wKfgTBeq6yCiH8MI+XttYRmytUanrY+OcBxjlQGmaIo=; re-plan No changes |  | OPEN |

## Log

- 20261001T190406Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
