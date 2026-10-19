# Deploy Completion Record
**Date opened:** 2026-10-19T15:45:40.825690+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-s-7 DEPLOY (TO ADHOC.canon-r11-global-axis-keep-deploy, GO msg 8335, risk WORLD): mdpf-gold-lambda package built from code commit 3d3d5ed5b91069a68b77d2d26b1ca37ae6a8fd8a (grandchild of deployed pin 128fce3524) with MDPF_GOLD_COMMIT stamp; D4-ref (no-write invoke of the CURRENT function, bodies returned) BEFORE, D2 (build_package --pin, upload, one .tf value in infra/aws/terraform/mdpf-pipeline/gold-lambda.tf, ONE targeted safe-apply), D4-new AFTER; issuer grades D4-PASS or D4-STOP; emitter opal-assets-daily-emitter and publisher NOT touched; no code/ key (D1) moves. Rollback: MDPF_GOLD_COMMIT back to 128fce3524a820c3c912a5f1e28ab149a68c5024, package back to the VersionId read in the before print, CodeSha256 back to whMJ8Ei9g0ZUDFEUxSaEQAViS0kokkxt9CS+vlD7SGI=, targeted safe-apply. D2 and D4-new finish by 2026-10-20T12:44Z.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 21.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions: GO 8335 after both halves signed, pair sha256, pin ancestry and content, clock, sentinel scan, one-change-per-fire | printed reads |  | OPEN |
| L1 | verify | before print: whole-tree equality, CodeSha256/env/package VersionId, 16 latest-date served objects, staged keys, control key, stores, workbook counts, emitter, schedule input | before-print json under deliverables/canon_s7/ |  | OPEN |
| L2 | verify | D4-ref: ONE invoke of the CURRENT function, schedule input plus qa_local plus qa_return_bodies, saved to C:/dev/_deploy_artifacts/canon_s7/d4_ref_response.json | status, errors, bodies, size and sha256 |  | OPEN |
| L3 | activation | D2: build_package --pin 3d3d5ed5b9, package read before upload, upload, the one .tf value, ONE targeted safe-apply on mdpf-gold-lambda, read back | MDPF_GOLD_COMMIT == pin == manifest commit, CodeSha256 differs from whMJ8Ei9 |  | OPEN |
| L4 | verify | D4-new: same invoke on the new function, d4_new_response.json, then the same 16/staged/control/stores reads | status green, errors empty, a4_objects_built 16, 16 bodies, reads unchanged, sha256 printed |  | OPEN |
| L5 | verify | issuer D4-PASS or D4-STOP against the pair section 2 (STOP: rollback read back) | the issuer's message |  | OPEN |
| L6 | verify | emitter CodeSha256 GLQf6kv4 unchanged; whole-tree equality after print attached; DIFFER names stated as known | after print and compare |  | OPEN |
| L7 | git | ledger, deliverables, the one .tf value and logs committed | commit hash with push state |  | OPEN |

## Log

- 20261019T154540Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 8 leg(s)
