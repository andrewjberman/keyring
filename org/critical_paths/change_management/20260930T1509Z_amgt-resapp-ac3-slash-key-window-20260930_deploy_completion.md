# Deploy Completion Record
**Date opened:** 2026-09-30T15:09:06.658908+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 53 AMGT-ac-3 -- THE SLASH-KEY WINDOW: leg (a) COPY the 40 raw-slash objects to their encoded keys (raw KEPT), THEN leg (b) redeploy opal-amgt-scoped-api at pin cd70547173 (CORPUS z-4 slash-safe readers, HARVST q-5 publishers_found_codes, ac-4 docstring). Halves: COO @bae8e66201, CTO @02eb2c5f9f.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B0 | verify | act-start gate (4 CTO clauses) + pre-act captures incl. --what save | base equal, content diff exactly 8, 40/40 raw sha256 equal, 40/40 destinations ABSENT; ac3-pre body capture written |  | OPEN |
| CP | activation | leg (a): 40 CopyObject raw->encoded, raw KEPT, no delete | AC1 ac_3_copies.py reads objects 40, raw kept and encoded byte-equal 40, exit=0 -- BEFORE leg (b) starts (limb 5) |  | OPEN |
| A1 | activation | leg (b): artifact upload + ONE safe-apply (code only) | prior+new VersionId, local b64 == S3 metadata == post-apply CodeSha256, plan read in full, 0-diff re-plan |  | OPEN |
| V1 | verify | AC2/AC3/AC4 on the SERVED route + never-widen limbs 6 and 7 | three criteria YES exit=0 and no limb fired |  | OPEN |

## Log

- 20260930T150906Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
