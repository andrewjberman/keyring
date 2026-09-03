# Deploy Completion Record
**Date opened:** 2026-09-03T17:23:36.385576+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-17R-28 -- BUILD opal-security-evidence (project CMK, versioned, private, SecureTransport-only policy) + ALIGN opal-data-security as the log destination (read-only, zero changes expected). The LOGGING limb is HELD by row Z-S49, whose disarm is the issuer's
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | s3_evidence.tf committed on SITEZ under 0.7.0_AE_CloudOps~S; UNSCOPED baseline quoted BEFORE the edit | commit hash + the baseline verdict |  | OPEN |
| L2 | activation | safe-apply of opsec -- 5 to add, 0 to change, 0 to destroy, all five the new bucket and its configurations -- ROLLBACK: destroy of the EMPTY new bucket and nothing else; NEVER a change to the log destination | apply output + the enumerated changed-resource list |  | OPEN |
| L3 | verify | S17R-AC1 -- every C-8 property on opal-security-evidence on the APPLIED plane: PAB 4 of 4, encryption aws:kms on the project key 64f25291 with BucketKeyEnabled true (and NOT AES256, NOT the AWS-managed key), versioning Enabled, policy = the SecureTransport deny with a censused ZERO Service principals | pasted reads with denominators |  | OPEN |
| L4 | verify | S17R-AC2 -- versioning leaves the original: a fixture under cases/ written and overwritten yields 2 versions, both readable with DIFFERENT bodies, head-object reads aws:kms on the project key, then both versions deleted and the listing empty | pasted reads + empty listing |  | OPEN |
| L5 | verify | S28-AC1 + S28-AC2 -- the log destination reads exactly as C-16 states it (private, AES256 and NOT the project key, versioning, the non-TLS deny, the two per-prefix service grants with both conditions, the waf-logs lifecycle), its plan wants ZERO changes, delivery is still running, and the evidence prefixes stay EMPTY on both sides -- nothing moved | pasted reads + the 0-change plan |  | OPEN |
| L6 | verify | S17R28-AC3 -- UNSCOPED re-plan 0-diff after the apply; nothing else rode; push state MEASURED by ls-remote + is-ancestor | plan + ls-remote |  | OPEN |

## Log

- 20260903T172336Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
