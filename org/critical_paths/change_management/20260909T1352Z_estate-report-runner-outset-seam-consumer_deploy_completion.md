# DEPLOY COMPLETION LEDGER -- estate-report-runner OUTSET SEAM CONSUMER (NFRA_OUTSET.TO-OS-s-19)

**Opened:** 2026-09-09T13:52Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `6dbb1e6a3a`)
**Status:** **CLOSED 2026-09-09T13:56Z** -- all four legs verified, content diff identical, the
comparator proven able to fail
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-19.the-deploy-of-the-served-runner.md`
(cell `OS-s-19`, outcome_refs FWD-2 / FWD-4 / FWD-7; issuance `37b2a19129`, face amended `cb43d05200`)

⛔ **This entry is opened BEFORE the upload and is committed in that state, so "opened first" is a
fact in git history rather than a claim in prose.** It is closed in a second commit after the legs
are verified.

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`, carrying the repo
file at HEAD. No Terraform change: no env var added, schedule untouched, instance untouched, IAM
untouched by this act (the seam grant landed separately under `TO-OS-s-18` at `54ccbdb47d`).

**WHY THIS DEPLOY EXISTS.** Round 1 of NFRA_OUTSET landed 17 of 17 task orders, every criterion
passed, and the estate still reads a runner dated **2026-08-25**. The CTO's round-1 analysis
`a0500abe18` names the cause: the PRD costed a publishing step and assigned it to an acceptance limb
rather than a manifest row, so the upload belonged to no cell. This is that upload, placed.

## EVERY CONSUMER OF THE KEY THIS ACT MOVES

The NEVER-2 rule requires an image-class act to name every task family that pulls what it moves.
Censused rather than recalled: `comp-find 'code/estate_report_runner\.py'` -> **154 hits across
152,096 files scanned**, banded HEAD 3 / SURFACED 41 / CONFIG 32 / TEST 2 / DOC 76.

| Consumer | How it consumes | Effect of this act |
|---|---|---|
| `estate-report.service` on `i-0512bd3cbaf602b7f` | `ExecStartPre=/usr/bin/aws s3 cp s3://.../code/estate_report_runner.py` (`instance.tf:215`) -- pulls the key at **every** service start | **The only functional consumer.** Picks up the new bytes at its next start. |

**AND THE THINGS THAT DO NOT CONSUME IT, checked so the count means something:**
`estate-report-orchestrator` holds exactly one environment variable, `ESTATE_INSTANCE_ID`
(`get-function-configuration`, LastModified 2026-08-06T21:46:42Z) -- it starts the instance and never
reads the code key. Every remaining hit is documentation, an audit log, a message archive, or this
session's own scratch copies. **ONE task family, not a shared tag: no `:latest`-class fan-out exists
here, so the NFRA_CLDGRPH-S31 hazard of one image act re-pointing several families does not apply.**

## THE WINDOW -- stated plainly, as the face requires

The report runs on EventBridge Scheduler `estate-report-0900et`, **ENABLED**,
`cron(0 9 * * ? *)` `America/New_York`, target the orchestrator Lambda.

- Today's run: instance launched **13:00:45Z**, self-stopped **13:11:04Z** (`StateTransitionReason`
  "User initiated (2026-09-09 13:11:04 GMT)"). Duration about 10 min 19 s.
- This upload is performed after 13:52Z, with the instance **stopped**.
- Next scheduled fire: **2026-09-10 13:00Z** (09:00 ET).

⛔ **THE UPLOAD LANDS OUTSIDE THE WINDOW, and outside it in the safe direction.** The service pulls
the key at ExecStartPre, which for today already happened at ~13:00:50Z, so today's run cannot be
affected even in principle; and the next pull is ~21 hours away, so no run is mid-flight against a
changing key. First live exercise is the 2026-09-10 13:00Z fire.

## PRE-STATE, measured live before the upload

| | value |
|---|---|
| Served object | **125,857 B**, ETag `58113db66bf3819f3515333d55fd5877`, LastModified **2026-08-25T05:36:35Z**, VersionId `bvnr1MynPuJ8Asn3u6Tgo9LPd5CrL5OO` |
| Served sha256 | `0f2afd2ee6b1e2f9...` (2,333 LF lines, 0 CRLF) |
| HEAD file | **159,687 B**, sha256 `88096c625bf70c3f...`, md5 `e75c59a35457535ca0d339c9f59589f5` (2,860 LF lines, 0 CRLF) |

**THE BYTES UPLOADED ARE `git show HEAD:<path>`, NOT THE WORKTREE COPY** -- and the two were compared
rather than assumed equal, because a worktree hash on an autocrlf box hashes the CHECKOUT and not the
record. Measured: worktree and HEAD are byte-identical here (same length, same sha256, 0 CRLF on
both), so the distinction costs nothing today. It is stated because the next file may differ.

## OPEN/RED ENTRIES FOUND, AND THE ARTIFACT MEASURED BEFORE ACTING ON THEM

An entry a device left OPEN proves only that THAT device saw no completion, and re-executing an
overtaken promote is a REWIND. So the ledger was read before this act rather than after.

- `org/critical_paths/.open_deploys/` holds **6** named entries: 4 OPEN (ADVI_INSURE x2,
  NFRA_OPSEC x2) and 2 HELD-SOVEREIGN-GATED (D12 SMS, FRESHGUARD). A scoped census of that directory
  for `estate.report|estate_report_runner|opal-estate-report` returns **4 hits across 7 files**, and
  **all four are inside `.unindexed_red_state.json`**, which is a path-to-timestamp index and not an
  open deploy. **Denominator 6 of 6 entries read; ZERO name this key.**
- The four index rows point at two ledger files, both of which were **opened and closed on
  2026-08-05** (`corpus-delivery` CLOSED 16:45Z; `budget-inversion` CLOSED 23:12:53Z). Two of the
  four rows carry the **other device's** path prefix (`C:\Users\Opal Bloomberg\...`) -- exactly the
  "a device left it open" shape -- and the artifact measurement settles it: the served object's
  vintage is 2026-08-25, three weeks LATER than both, so neither is an unfinished promote of this
  key. **Nothing is half-landed and nothing here is a rewind.**

## Legs

1. [x] `s3api put-object` HEAD bytes -> `s3://opal-estate-report/code/estate_report_runner.py`.
       Instance state read **immediately before** the call: `stopped`. Started 13:53:20Z, returned
       13:53:22Z. New `VersionId GQny85Je837UhagoFc0FY8eoJzcB1RFy`, SSE AES256.
2. [x] `head-object` verify: ContentLength **159,687 == 159,687**; ETag
       `e75c59a35457535ca0d339c9f59589f5` **== HEAD md5** `e75c59a35457535ca0d339c9f59589f5`;
       LastModified 2026-09-09T13:53:22Z.
3. [x] **CONTENT diff, which is the leg that actually decides** (Rule 22a: deployed bytes are diffed
       against the BUILD INPUT, never by filename -- running-bytes-older-than-built passes every
       other rung). Re-downloaded the object and compared sha256 against `git show HEAD:<path>`:
       **`88096c625bf70c3f...` == `88096c625bf70c3f...`, 159,687 B both.**
       **NEGATIVE CONTROL, because a comparison that cannot fail is not a comparison:** one bit
       flipped at offset 100 of a copy, length unchanged -> the same comparator reports MISMATCH. So
       leg 3's match is a measurement and not a constant.
4. [x] `O19-AC1` battery green at the amended path: **6 of 6 arms PASSED, 0 NOT-EVALUATED**,
       `SERVED MATCHES HEAD`, rc 0 captured unpiped; second grain `pytest -q` -> 1 passed; two
       same-input repeats with an IDENTICAL verdict set.

## Post-state

| | value |
|---|---|
| Served object | **159,687 B**, ETag `e75c59a35457535ca0d339c9f59589f5`, LastModified **2026-09-09T13:53:22Z**, VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy` |
| Identical to | `git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py`, sha256 `88096c625bf70c3f...` |

**THE TOKEN CENSUS, WITH A POSITIVE CONTROL PER TOKEN** (`W1-S27`: a census of four tokens is four
detectors, not one). Five LIVE tokens -- non-zero at HEAD, so their counts carry information --
`_outset_read` 4, `OUTSET_ANSWER_STATE_TO_STATUS` 3, `ESTATE_OUTSET_SEAM_PREFIX` 5, `_outset_trace`
3, `render_trace` 2, each now equal in the served bytes; **before this deploy every one of them was
0 in the served object.** One INERT token, `rerun_recipe`, carried deliberately as a sealed control
because row `S14` measured it at zero on BOTH sides -- the battery classifies it INERT and REFUSES
it as evidence rather than counting a meaningless zero. Same-program positive control `_stratum(`
reads 16 on both sides.

## Close condition -- MET

All four legs checked and the post-state measured. First live exercise is the next scheduled 09:00 ET
fire at **2026-09-10 13:00Z**, which is left untouched -- **no watcher, monitor or freshness checker
is armed against it** (standing moratorium; the scheduled fire is the acceptance, not an ad-hoc run).

⛔ **WHAT THIS DEPLOY DOES NOT DO, stated so the close is not read as more than it is.** The served
runner now carries the OS-s-10 seam consumer, and the consumer will still return
`INSTRUMENT_UNAVAILABLE` on the next fire, because `ESTATE_OUTSET_SEAM_PREFIX` is set nowhere in
Terraform (row `NFRA_OUTSET-S16`). This deploy closes the gap between HEAD and the served artifact.
It does not turn the seam on, and no criterion on this order claims it does.

## Rollback

S3 versioning is on. The prior object is `VersionId bvnr1MynPuJ8Asn3u6Tgo9LPd5CrL5OO`
(125,857 B, 2026-08-25T05:36:35Z); restoring it is a single `copy-object` from that version, in
session, with no Terraform involvement. Recorded here before the act, so the rollback path is known
without reconstructing it under pressure.
