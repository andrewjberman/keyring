# Deploy Completion Record
**Date opened:** 2026-10-02T14:36:18.150096+00:00
**Status:** OPEN
**Deploy:** irpt-status at ONE commit b789341289: S270 M2 (bounded per-row pool + 1024 MB) and hop 11 D2 (SigV4 signer), then hop 11's route R1 (CTO batches 170, 171, 174); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip new version | read back by version, sha equal; census vs live | irpt-status.zip version ZmF_dRrw9PUki9V1DCyxYFvRvYB22GVx (14:24:18Z, 336416 bytes) read back sha256 6SbSkFNz9PzOO80sQqTQlBrW3zaQx1HO2QHXU55UHuw= equal; 47 members, 0 differ from the pin b789341289; census vs live BNe2n9cV: identical 43, changed 4 (S270/census_irpt-status_m2.json) | CLOSED 20261002T143618Z |
| D1 | tf-lambda | ONE targeted safe-apply of the function (memory + code) | memory 1024, CodeSha256 6SbSkFNz read back; V1-a REPORT <= 10 s every page size |  | OPEN |
| R1 | verify | ONE targeted safe-apply of the pdf route | route read back |  | OPEN |
| V1 | verify | hop11_pdf_proof MATCH on 4 READY requests; plain reads equal | per packet section 3 |  | OPEN |

## Log

- 20261002T143618Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T143618Z LEG U1 closed: irpt-status.zip version ZmF_dRrw9PUki9V1DCyxYFvRvYB22GVx (14:24:18Z, 336416 bytes) read back sha256 6SbSkFNz9PzOO80sQqTQ
