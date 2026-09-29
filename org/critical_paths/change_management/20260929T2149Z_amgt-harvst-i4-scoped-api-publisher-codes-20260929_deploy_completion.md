# Deploy Completion Record
**Date opened:** 2026-09-29T21:49:29.128653+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST round 19 HVST-i-4: redeploy opal-amgt-scoped-api so /timeline and /timeline/day serve publishers_covered and publishers_covered_codes. ONE artifact write + ONE safe-apply moving the scoped API's code only -- no IAM, no route, no layer, no runtime/memory/timeout change, no S3 delete. Under the never-widen pair COO @0abf041dfa (AMENDMENT 1: i-4 runs ALONE) / CTO @053e4ae20f, with the closure ruling @3a354b0720 (continuation.py ships INERT). Base re-verified live by this seat at the open: CodeSha256 lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=, artifact VersionId 61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U (40097441 B) latest -- equal to what both halves signed, so the halves travel (CTO condition 4)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | build-only closure diff + budget + continuation re-confirm | closure diff shows EXACTLY the 3 source files the halves name (harvest/publication_gold.py, harvest/timeline_api.py, corpus/continuation.py) plus the a-2-pinned wheels, anything else a STOP; new unzipped total printed and under 262144000 B; continuation.py re-confirmed equal to CLOUD HEAD with no request-path caller (CTO condition 1) |  | OPEN |
| A1 | activation | artifact upload + ONE safe-apply | prior VersionId 61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U recorded as the rollback target; plan printed and showing the scoped API's code and nothing else; apply confirmation; post-apply CodeSha256 |  | OPEN |
| V1 | verify | AC1 + AC2 | both read 'RESULT: PASS (0 failure(s))' with their TRUE exit codes taken without a pipe; any failure is the ROLLBACK to 61Fb7L90 the same session |  | OPEN |

## Log

- 20260929T214929Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
