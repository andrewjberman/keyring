# TCKT_VNEXT TO-R20-REL2: opal-ticket-api code-only release for the package route's null pair, REL2-OK -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-20
**Task Order:** TCKT_VNEXT.TO-R20-REL2 (AMENDMENT 1, GO msg 11113; CTO half signed msg 11111)
**Status:** COMPLETE

---

## Objective

Release the ticket service CODE ONLY so the package route admits `pdf_ref` and `commentary_ref` null together (IRPT_ANLREQ v0.24 FWD-1): one in-place update of `opal-ticket-api`'s code, nothing else. Pair: COO half blob `2d758b87a9`, CTO half blob `772c800268`; check `r20_rel2_check.py` blob `a98078c896`; `built_from_sha` `48551f02ac`, source blob `085183c76e`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 5 legs, close-leg x5, close | PASS | `tckt-vnext-r20-rel2-20261020` CLOSED 00:25Z |
| build-and-upload.sh | `BUILD_ONLY=1 ... ticket-center opal-ticket-api` | PASS | import-closure OK, one member, 40638 bytes; the upload was a separate `put_object` |
| terraform plan / safe-apply | plan -out, apply of the planfile, plan again | PASS | 0 add, 1 change, 0 destroy; post-apply No changes |
| r20_rel2_check.py (issuer) | criterion and `--self-test` | PASS | `REL2-OK`; `R20-REL2-SELFTEST-OK` |
| proof-of-spec-check.py | with --governing-order | PASS | see the closing commit |
| comp-iam | not run | SKIPPED | the plan shows no permission change |

**What worked:** the member-by-member diff of the built package against the downloaded live package found exactly the pair's three hunks (11 added, 0 removed); the plan equalled the pair's section 3. **What failed:** nothing in the run. **Gap found:** `2.0.0_SA_COO~Y2` never read my overlap ask (msg 11117 stayed OFFER-EXHAUSTED at 00:18Z) and `0.7.0_AE_CloudOps~IB2` did not answer; silence read as none per the earlier orders' convention, backed by measured reads (no promote in flight, PROD head unchanged, the CTO's none, IB2's E2E-4 ledger closed). The order file in the shared tree carried the COO's AMENDMENT 1 uncommitted (identical to commit `dc2e266fe6` on branch v2-go-slot); my flip rides on that text.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | `check-inbox`; GO 11113; blobs | pair `2d758b87a9`, CTO half `772c800268`, check `a98078c896` EQUAL; source blob at `48551f02ac` `085183c76e` EQUAL |
| 1 | Ledger opened 00:07Z, slug to V2 and Y2; asks to CTO, IB2, Y2 | CTO none until 02:30Z (msg 11120) |
| 2 | Live baseline, census | CodeSha256 `iRxJZYp6...` = baseline; env_before saved (14 keys); 46 worktrees read, the shared tree holds only this ledger |
| 3 | Build at `48551f02ac` | zip sha256 b64 `LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0=`, 40638 bytes; diff vs the live member 3 hunks, 11 added, 0 removed |
| 4 | Rollback saved, package uploaded 00:19Z | previous S3 VersionId `9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK` (copy equals the live package); new VersionId `efzUHPSp1bg2_tqpHPy7xQpsJYTuEHnd`; metadata and round trip equal |
| 5 | Plan | one in-place update (`s3_object_version`, `source_code_hash`, computed `last_modified`) |
| 6 | Inbox clear, `safe-apply` | rc=0 at 00:22Z; Active/Successful on `LuJO3wFD...`; environment equal; post-apply plan No changes |
| 7 | Check, result, ledger | `REL2-OK` beside `R20-REL2-SELFTEST-OK`; ledger CLOSED 00:25Z |

## Verification

```
r20_rel2_check.py -> REL2-OK code_sha256=LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0= null_pair=present fence=present env=unchanged members=1
r20_rel2_check.py --self-test -> R20-REL2-SELFTEST-OK
terraform plan (post-apply) -> No changes. Your infrastructure matches the configuration.
```

---

## Decisions Made

- Built in the kept detached worktree `C:/dev/tv2-rel-r1819` moved to `48551f02ac`, not from the shared tree, so no other seat's uncommitted change could ride the package.
- Applied before the 06:00Z Tuesday gateway band, outside 11:30Z to 14:15Z.

## Blockers

None.

## Current State

`opal-ticket-api` runs package `LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0=` (LastModified 2026-10-20T00:22:47Z): a package POST with `pdf_ref` and `commentary_ref` both null and both keys present is admitted and stored null; a lone null, a missing key and non-canonical strings stay refused 400. Rollback: restore the object at S3 VersionId `9Y9nFwn0vtsQw3mIqVHRzHKyoJGWa5bK` (copy `C:/dev/tv2-rel-r20-out/rel2/rollback_live_iRxJZYp6.zip`) and re-apply the pre-release tree. Records: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_rel2/`. Kept until a human confirms deletion: `C:/dev/tv2-r18run-scratch`, `C:/dev/tv2-rel-r1819` (detached at `48551f02ac`), `C:/dev/tv2-rel-r20-out`.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Read `R20_REL2_RESULT.json`; the packager half may ship after the page half is live.
2. `[2.0.0_SA_COO~Y2]` The ticket-service release is live; your ask msg 11117 was unread when I applied.
3. `[0.0.0_AB_MSTR]` Carry this seat's local commits from box/dell2.
