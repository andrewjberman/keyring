# Deploy Completion Record
**Date opened:** 2026-10-17T15:28:41.312956+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-s-6 DEPLOY (TO ADHOC.canon-r11-global-axis-deploy, GO msg 7623, risk WORLD): mdpf-gold-lambda package built from code commit 128fce3524a820c3c912a5f1e28ab149a68c5024 (child of deployed pin d2f734fbac) with MDPF_GOLD_COMMIT stamp; D4-ref (no-write invoke of the CURRENT function, bodies returned) BEFORE, D2 (build_package --pin, upload, one .tf value in infra/aws/terraform/mdpf-pipeline/gold-lambda.tf, ONE targeted safe-apply), D4-new AFTER; issuer grades D4-PASS or D4-STOP; emitter opal-assets-daily-emitter and publisher NOT touched; no code/ key (D1) moves. Rollback: MDPF_GOLD_COMMIT back to d2f734fbac, package back to the VersionId read in the before print, CodeSha256 back to fAXZ4gdLPspZepxmR9J8l3BfJROkppYOyf3qC2dAd40=, targeted safe-apply. D2 and D4-new finish by 2026-10-18T12:44Z.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 21.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | preconditions: GO 7623 after both halves signed, pair sha256, pin ancestry and content, clock, sentinel scan, one-change-per-fire, SMArtX partitions | printed reads |  | OPEN |
| L1 | verify | before print: whole-tree equality, CodeSha256/env/package VersionId, 16 latest-date served objects, 514 staged keys, control key, stores, workbook counts, emitter, schedule input | before-print json under deliverables/canon_s6/ |  | OPEN |
| L2 | verify | D4-ref: ONE invoke of the CURRENT function, schedule input plus qa_local plus qa_return_bodies, saved to C:/dev/_deploy_artifacts/canon_s6/d4_ref_response.json | status, errors {global}, 12 bodies, size and sha256 |  | OPEN |
| L3 | activation | D2: build_package --pin 128fce3524, package read before upload, upload, the one .tf value, ONE targeted safe-apply on mdpf-gold-lambda, read back | MDPF_GOLD_COMMIT == pin == manifest commit, CodeSha256 differs from fAXZ4gdLPsp |  | OPEN |
| L4 | verify | D4-new: same invoke on the new function, d4_new_response.json, then the same 16/514/control/stores reads | status green, errors empty, a4_objects_built 16, 16 bodies, reads unchanged, sha256 printed |  | OPEN |
| L5 | verify | issuer D4-PASS or D4-STOP against the pair section 3 (STOP: section 4 rollback read back) | the issuer's message |  | OPEN |
| L6 | verify | emitter CodeSha256 GLQf6kv4 unchanged; whole-tree equality after print attached; DIFFER names stated as known | after print and compare |  | OPEN |
| L7 | git | ledger, deliverables, the one .tf value and logs committed | commit hash with push state |  | OPEN |

## Log

- 20261017T152841Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 8 leg(s)
