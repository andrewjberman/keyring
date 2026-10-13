# Never-widen half (COO half SIGNED, CTO half owed): MDPF_HEALGAP round 5, drain act HG-t-18 -- the ASTN FT re-attempt's code onto the scraper and the orchestrator, which also restores the morning brief's send

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-13 ~18:1xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Ruling this applies:** the CTO's round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @c36a37275f section 2 (D1-W14-S3, "the FT leg gets the project's own
same-day re-attempt") and section 3 item 1; msgs 4962 and 4966. **Order:** `MDPF_HEALGAP.TO-HG-t18`, worker `0.9.0_WK_MDPF_HEALGAP~15`, merged by
`.tools/safe-merge.sh` as `d5ef37258a` (LOCAL on `box/dell1`; code commit `1eaea051c4`, row commit `52035870ac`, proof commit `f4a40bf3da`).
**Status:** nothing applied. The act waits on your half. No schedule resource is in this act (it waits on the astn registry row, msg 4966).

## 0. Read this first: the act restores a send that has not happened

Reading the deployed code to count writers, the issuer found that the 3 AM brief is not being SENT (surprise row `MDPF_HEALGAP-D1-S17`, `43c9fd2cab`).

- `ssm list-commands` on `i-059405dfefcb4b44a`, read 2026-10-13T18:00Z: 31 commands, one per day 2026-09-13..2026-10-13, 31 of 31 `Failed`.
- The two newest (2026-10-13 `a536d8e5`, 2026-10-12 `cbb1e737`) read in full: stdout shows the digest built and `OK: code deployed to /opt/astn-wsjft`; stderr ends
  `botocore.exceptions.ParamValidationError ... Destination.ToAddresses[0], value: ['austin@opalinvest.com', 'andrew@opalinvest.com'], type: list`. The call fails
  client-side, so no SES request was made on those two days. The other 29 were read for Status only.
- Cause: the S3 code prefix `s3://opal-313476888478-lambda-artifacts/ec2/astn-wsjft/code/` (which `deploy.sh` pulls over `/opt/astn-wsjft` at every run) holds
  `scripts/send_ses.py` from 2026-06-25T00:42Z, which wraps `config.SES_TO` in a list, beside `scripts/config.py` from 2026-06-29T18:24Z, where `SES_TO` is a list.
  The repo's `send_ses.py` handles the list (`isinstance` guard, lines 11-15). Downloaded S3 copies byte-compared with `git archive fe216d8d06 tools/astn_wsjft`:
  18 files identical, 4 differ (`ARCHITECTURE.md`, `scripts/analyze.py`, `scripts/run.py`, `scripts/send_ses.py`), 3 only in S3 (old tests), 2 only in the repo (pyc).
- Why nobody saw it: the digest and email objects are persisted before the send, so the absence guard (digest content) reads healthy, and the orchestrator's
  `_alert` publishes "run FAILED" to `astn-wsjft-alerts`, which has 0 subscriptions (read 2026-10-13T18:02Z; the 2026-07-13 CloudOps record
  `20260713T0744Z_astn-orchestrator-selfkill-contentguard` says the subscription drifted out when Andrew unsubscribed 07-01 and that re-creating it is Andrew-gated).
  The orchestrator's own comment (`lambda_function.py` near line 209) reads rc=1 as "works, digest landed"; these two reads refute that for those days.
- Not read: the history before 2026-09-13, and the box's `ASTN_SES_TO` environment (the recipients below are the code default).

**Consequence for this act:** the upload below moves `send_ses.py` (needed for the refill's own send) and `run.py`, so the next 3 AM run (2026-10-14 03:00 ET,
07:00Z) is the first to run the repo's code and the first in the retained window to send. A served output moves from not-sent to sent, to the two recipients
the code names. SES state read 2026-10-13T18:05Z: sending enabled, production access, `austin@opalinvest.com` and `andrew@opalinvest.com` identities verified
(`Success`), sender domain `opalinvest.dev` verified (`morningbrief@opalinvest.dev` is under it), 50,000 / 24 h quota, 1 sent in the last 24 h.

## 1. The act (order matters)

0. Open the ledger entry first: `.tools/deploy_ledger.py open` with legs L1 upload, L2 Lambda, L3 driven arm, L4 organic arm, each with its proof.
1. **Record the before state:** S3 object `VersionId`s of the three keys below (read 2026-10-13T18:07Z: `run.py` `Q_QNScU1TrQhR6Mw53kMvv_66h9j9UZX`, `send_ses.py`
   `nEU5l.gGBk1n1ed2XVDr4IA1BHmyjnIv`, `store.py` `BSLHzwdNU4aMB4pjfdj.arP0qSBhmeKv`; bucket versioning Enabled), the Lambda `CodeSha256`
   `gXzCrCaEvIPd8M7z1FtGJQ33hYrxq8g/h4Ud2obIpL0=` (LastModified 2026-07-13T07:48:22Z), and `astn-wsjft-3am-run` read ENABLED `cron(0 3 * * ? *)` America/New_York,
   input `{"mode":"run"}`.
2. **Upload exactly three keys** from `git archive` of the merge pin (never the shared worktree), each with `--checksum-algorithm SHA256`, then read the
   checksum back: `scripts/run.py`, `scripts/store.py`, `scripts/send_ses.py` under `ec2/astn-wsjft/code/`. NOT uploaded: `scripts/analyze.py` (a one-line
   removal of the constant `faithful_verified: True`, commit `8dad740440`; drift left in place, named below), `ARCHITECTURE.md`, anything under
   `configs/`, `fetch_ft.js`, `package.json`. No key is deleted.
3. **Lambda:** `.tools/safe-apply.sh` in `infra/aws/terraform/astn-pipeline`, `-target=aws_lambda_function.orchestrator` only (the 2026-07-13 precedent; an
   untargeted apply is refused: it would re-create the unsubscribed SNS subscription and email Andrew). **Two preconditions the plan read found today**, section 2.
4. **Driven arm:** invoke the Lambda once with `{"mode":"ft_reattempt","dry_run":true}`. It starts the scraper, runs `deploy.sh`, runs
   `python3 run.py --ft-reattempt --dry-run`, stops the box. Today's digest has no FT failure (read 2026-10-13: 12 in, 1 out, `warnings: []`), so the line read
   is `ASTN_FT_REATTEMPT SKIP-COMPLETE 2026-10-13: today's digest carries no FT fetch failure`, rc 0: it proves the new code is on the box, imports, and the
   mode reaches `run.py`. It sends and writes nothing.
5. **Organic arms (read, not driven):** (a) the 2026-10-14 03:00 ET run, read at about 07:20Z: `get-command-invocation` for that day's command should read
   Success, rc 0, with `SES sent <MessageId> -> ['austin@opalinvest.com', 'andrew@opalinvest.com']`; (b) the first FT-failed day after a schedule exists runs the
   refill's positive arm (nothing on demand can drive it: `_run_date()` has no override and a failed day's digest is a record this act must not write).

## 2. What changes, and what does not

- **Changes (S3, 3 keys):** `run.py` (adds `ft_reattempt`, its helpers and the `--ft-reattempt` / `--dry-run` switch; ALSO moves the 2026-08-06 CTO-ruled
  validate-before-persist: a run with 0 surviving articles no longer writes `digest.json`; the absence guard reads an absent object as a miss and alerts as it
  did for an empty one), `store.py` (adds `try_load_digest`; drops one unused `import re`, row D1-W15-S1), `send_ses.py` (the list fix).
- **Changes (Lambda):** one attribute, `source_code_hash`, `gXzC...` to `RcBxw9W48ZOwoj+5+Uvi1nb4L6VrexgsBFXh9vPmjUU=` (plan read 2026-10-13T18:06Z at HEAD
  `b78d4ffe91`); the new mode `ft_reattempt` and the event key `dry_run`. The `run` command line is byte-identical (the gate pins it).
- **Precondition 1, provider lock:** `infra/aws/terraform/astn-pipeline/.terraform.lock.hcl` pins `hashicorp/archive` 2.8.0, which the registry now reports
  "no longer available", so `terraform init` fails from a clean checkout (read twice). With the archive block removed from the lock, `init` selected 2.8.1 and
  the plan ran (rc 0). The lock refresh is a 2-line change (`version = "2.8.0"` to `"2.8.1"` and its hashes), committed before the apply and named in the ledger.
- **Precondition 2, a second change enters by dependency:** the Lambda's environment reads `aws_instance.astn.id`, so the targeted plan also reads
  `aws_instance.astn ... user_data` `751e88e4...` to `07717eec...`, in place. Computed: the state value equals the sha1 of the heredoc in `instance.tf` with
  CRLF endings and the new value equals the same text with LF; the committed file is LF (0 CR bytes), so a LF checkout always plans this. No functional change:
  user-data runs once at first boot. The instance is `stopped` (read 2026-10-13T18:07Z) between runs. Ask of your half: accept this one in-place attribute change
  as part of the act, or direct the apply from a CRLF tree (which would put CRLF bytes into the Lambda's zip). The plan must read EXACTLY these 2 changes and
  0 added, 0 destroyed; any other line refuses the act.
- **Unchanged:** the schedule `astn-wsjft-3am-run`; both roles and every grant (no IAM change: section 4); the SES identities; the SNS topic and its
  0 subscriptions; the `run` and `absence_check` modes; `analyze.py` and `ARCHITECTURE.md` on S3 (the remaining 2 of the 4 differing files).

## 3. Branches, each read from the producer's own rule (`run.py` lines 138-213, never predicted from an input's shape)

| day | 3 AM run | refill invoked (driven today; scheduled later) | served effect |
|---|---|---|---|
| A, FT fine | digest, no `FT fetch failed` warning; ONE brief sent to 2 recipients | `SKIP-COMPLETE`, nothing fetched or sent; the box starts, runs `deploy.sh` and stops (cost ~$0.08, minutes) | the brief, once |
| B, FT failed, other sources gave output | WSJ-only digest with the warning; brief sent without FT | fetches FT once; window = hours since 07:00Z of the newest earlier day whose digest has output and no FT failure (12 h when none, 7 days at most); keeps only articles no known digest carried (by `sha256(url)[:16]`); persists `digest/<date>-ftsup`, sends ONE `FT supplement` email to the same 2 recipients | one extra email, new FT items only |
| C, FT still dead at the refill | as B | the fetch raises: SSM Failed, nothing sent, alert to the 0-subscriber topic | unchanged from B; loud only in the log |
| D, no usable digest | run exits 2 (0 articles) | `NO-PRIOR-DIGEST`, nothing sent | the 4 AM absence guard owns it |
| E, refill already sent | n/a | `SKIP-COMPLETE` on the `-ftsup` digest | no second supplement |
| F, `dry_run` | n/a | everything but persist and send; the FT fetch is not persisted | none |

**Named residuals.** (1) A previously dropped FT article is re-analysed inside the window (the dedupe compares what was SENT) and can surface as new. (2) The
refill's schedule must sit after the 3 AM run's worst case (900 s Lambda, 600 s SSM): it is chosen when the resource is cut. (3) `analyze.py` and
`ARCHITECTURE.md` stay behind the repo; a later deploy moves them. (4) The 4 AM absence guard still reads a digest object, so it cannot see a failed SEND:
the failure class that hid for 31 days is not guarded by this act; building any alert or monitor is Andrew's word and is not proposed here.

## 4. Writers and readers (read live 2026-10-13T17:49Z)

**Writers of `digest/<date>-ftsup/digest.json` and `email/<date>-ftsup/digest.html` in `opal-data-astn`, N = 1.**
- By GRANT: role `astn-wsjft-scraper-role`, inline policy `astn-wsjft-scraper` (7 statements; the one with `s3:PutObject` is `WriteAndReadArticleStore`, Resource
  `opal-data-astn/*`), plus the managed `AmazonSSMManagedInstanceCore`. Role `astn-wsjft-orchestrator-role` (8 statements) holds no `PutObject`.
- By BUCKET POLICY: none (`NoSuchBucketPolicy`, read).
- By SOURCE: `store.put_digest` / `store.put_email` called from `run.py` lines 204/206 (new) and 266/270 (existing). Not enumerated: identity policies of
  other principals holding a broad `s3:*` on the bucket.
- The code prefix `ec2/astn-wsjft/code/`: written by this act's upload only (role `astn-wsjft-scraper-role` can read it, `PullHarnessArtifact`).

**Senders:** `ses:SendEmail` on the scraper role, condition `ses:FromAddress` `*@opalinvest.dev`. Recipients: code default `austin@opalinvest.com,andrew@opalinvest.com`
(`config.py` lines 44-45); the box's `ASTN_SES_TO` not read.

**Readers of `digest/`, N = 2 runtime:** the orchestrator's absence guard (exact key `digest/{date}/digest.json`, `lambda_function.py` line 122; a `-ftsup` key
cannot collide with it) and `run.py`'s own `try_load_digest`. `comp-find 'opal-data-astn' --band SURFACED` read 2026-10-13: 14 non-log files; the first-party
code and Terraform among them are `iam.tf`, `main.tf`, `router_iam.tf` (a deny-write fence list, no read) and the two proof scripts
`infra/aws/ec2/astn-wsjft/run_wsj_proof.py` and `wsj_test.sh` (named, NOT read). Not read: any reader outside the repo (the portal tree was not searched for the
bucket name beyond that band).

## 5. Rollback (per key)

- **S3 keys:** copy the recorded prior `VersionId` back over each key (`run.py`, `store.py`, `send_ses.py`); read the object back against the recorded checksum.
  Rolling `send_ses.py` back re-creates the failing send; roll the three together or not at all.
- **Lambda:** re-apply the file at the parent of the HG-t-18 merge (its `CodeSha256` `gXzC...` is the target); read `CodeSha256` back.
- **Instance user-data:** re-apply from the CRLF text (state value `751e88e4...`).
- **A supplement email already sent** cannot be recalled; the refill sends at most one per day (the `-ftsup` digest is its done-marker).
- **The lock refresh:** revert the 2-line commit.

## 6. Acceptance

1. `get-object-attributes` of the three keys read the uploaded checksums; the `deploy.sh` pull on the next run prints `OK: code deployed`.
2. Lambda `CodeSha256` read back equals the plan's `RcBxw9W4...`; the targeted plan after the apply reads `No changes`.
3. The driven `ft_reattempt` dry run reads SSM Success rc 0 and the `SKIP-COMPLETE` line above; the box reads `stopped` afterwards.
4. The 2026-10-14 03:00 ET run reads Success rc 0 with the `SES sent` line (organic arm 5a), or the act is rolled back and the row reopened.

**Merge pin and code reads:** the issuer re-ran both criteria in the worker's tree (`GATE-OK` 13 arms, `GATE-OK` 7 arms), validated the instance (`VALID`),
and byte-compared the worker's files with the reference patches applied on a clean worktree at `fe216d8d06`: `run.py` and the orchestrator IDENTICAL,
`store.py` differs by the one removed unused import (the commit gate's F401; row D1-W15-S1).
