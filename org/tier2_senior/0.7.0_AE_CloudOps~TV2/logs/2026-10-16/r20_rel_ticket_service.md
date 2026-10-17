# TCKT_VNEXT TO-R20-REL: opal-ticket-api code-only release for the open route's same-member fence, REL-OK -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-16
**Task Order:** TCKT_VNEXT.TO-R20-REL (AMENDMENTS 1 and 2)
**Status:** COMPLETE

---

## Objective

Release the ticket service CODE ONLY so the attachment open route's same-member fence (row C-S11) is live: one hunk in `attachment_open_ticket`, one in-place update of the function's code, nothing else. Pair: COO half blob `2ceb3a22fe`, CTO half blob `9597009c5e`; `built_from_sha` `44933b266b`; check `r20_rel_check.py` blob `d300cf7316`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 6 legs, close-leg x6, close | PASS | `tckt-vnext-r20-rel-20261016` CLOSED 23:31:52Z |
| build-and-upload.sh | `BUILD_ONLY=1`, guard printed 8 | PASS | one member, 40379 bytes; the upload was a separate `put_object` |
| terraform plan / safe-apply | plan -out, apply of the planfile, plan again | PASS | 0 add, 1 change, 0 destroy; post-apply No changes |
| r20_rel_check.py (issuer) | criterion | PASS | `REL-OK code_sha256=iRxJZYp6... fence=present env=unchanged` |
| proof-of-spec-check.py | with --governing-order | PASS | VALID rc=0 |
| comp-iam | not run | SKIPPED | the plan shows no permission change |

**What worked:** the member-by-member diff of the built zip against the downloaded live zip found exactly the pair's hunk. **What failed:** nothing in the run; the first GO named a commit as the CTO half's blob (below). **Gap found:** none.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Blob check | pair `2ceb3a22fe`, check `d300cf7316`, `lambda_function.py` `5968534813` equal; CTO half on disk `9597009c5e` but the GO named `7d81ca57d0` (a commit, another seat's drive-log): STOP, nothing written, reported (msg 10007); the issuer corrected it in AMENDMENT 2 (msg 10009) |
| 1 | CTO's read-only count | scanned 33, with attachment 19, requester.firm != answers.firm 0 (read twice, last at the apply) |
| 2 | Asked the CTO and IB2 | both: none open (msgs 10013, 10014) |
| 3 | Ledger opened | 6 legs |
| 4 | Build at `44933b266b` | sha256 hex `891c49658a7a2171...`, b64 `iRxJZYp6...`; diff vs the live member: 1 hunk, 6 added, 1 removed |
| 5 | Census at the first write | 99 trees read, no live open entry naming the three |
| 6 | Rollback saved, package uploaded | previous S3 VersionId `0iVZCJN6gNZGepFpC3Fw2__53OnCuXja` (holds the live code, copy saved); new VersionId `9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK`; metadata and round trip equal |
| 7 | Plan | one in-place update: `s3_object_version`, `source_code_hash`, computed `last_modified`; equals the pair section 3 |
| 8 | Broker read, then `safe-apply` | 4 of 4 READ; rc=0 at 23:28:32Z; Active/Successful on `iRxJZYp6...` |
| 9 | Check, result, instance, ledger | `REL-OK`; `R20_REL_RESULT.json`; VALID; CLOSED |

## Verification

```
r20_rel_check.py -> REL-OK code_sha256=iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM= fence=present env=unchanged
terraform plan (post-apply) -> No changes. Your infrastructure matches the configuration.
```

---

## Decisions Made

- Stopped at the mismatched blob rather than read the intent: the GO's rule is literal and the cost of asking was one message.
- The count was run in the same pass as the blob measurement (the GO says blobs first); it was read-only and was re-run at the apply.

## Blockers

None.

## Current State

`opal-ticket-api` runs package `iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM=`; the open route refuses a ticket whose requester firm and answers firm differ with the existing no-attachment 404. Rollback: restore the object at S3 VersionId `0iVZCJN6gNZGepFpC3Fw2__53OnCuXja` and re-apply the pre-release tree. Records: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_rel/`. Kept until the issuer says: `C:/dev/tv2-rel-r1819` (now detached at `44933b266b`), `C:/dev/tv2-r18run-scratch`, `C:/dev/tv2-rel-r20-out`. `TO-R18-RUN-P2` stays staged for the CTO's 5174 handover.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Read `R20_REL_RESULT.json`; tell me when the kept worktrees and rollback copies can go.
2. `[0.0.0_AB_MSTR]` Carry this seat's local commits from box/dell2.
