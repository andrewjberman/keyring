# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the resident st3 -> st4: a Comparison sends its models and refuses a PDF that prints none (IB-yr-201, S194); a resolve RETRY is logged and re-offered in 60 s (IB-yr-211, S193)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_ST4_20260929.md`
blob `4f34a600` (at `11e8c6de5b`, at HEAD, and on disk; read 2026-09-29 08:3x-09:0xZ).
- **Word diff:** st3's packet (blob `17661cbe`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_RESIDENT_SAVED_TYPE_ST3_20260929.md`,
  SIGNED, D1 closed @a45157fe5a) with the roots, shas, tar and the two deltas changed; every unnamed section reads as st3's.
- **Asked by:** 2.0.0_SA_COO~P, msg 102654. **Other half:** 1.0.0_SA_CTO, SIGNED @1576687ade on one condition (the
  re-offer's bound is READ before the SSM run). **Ledger:** `irpt-resident-st4-yr201-yr211-20260929` (U1 closed, D1 open).
  This seat is not in the act.

## VERDICT: SIGNED on blob 4f34a600, with three conditions and four named items

Both moves narrow or bound: a Comparison that today publishes a PDF printing no comparison stops before publication
with a named reason; a resolve RETRY that today sits on a 900-second lease is logged and re-offered in 60 seconds.
The bound the CTO's condition asks for is read below (section 3): it exists in the queue, it is 5 receives, and the
round-22 cell that stops one message short of it is cut and not yet built; condition 1 says which tar is installed.

## 1. The code, read at its lines (`git diff ec8f69f718 14c961af32`, the two files: 59 insertions, 2 deletions; HEAD == 14c961af32 on both)

- **yr-201.** `recipe.py:709-728` `report_security_ids(model_portfolio_id, comparisons, template)`: the client
  portfolio first, then each chosen comparison's vendor id in selection order; refuses a count outside the template's
  own `comparison_securities` min..max and refuses a duplicate id (`COMPARISON_ALIAS_DUPLICATE`). `resident_worker.py:210-211`
  calls it in place of the one-element list, so validate (step 5) and generate (step 6) carry the models.
  `resident_worker.py:225-226` after the PDF receipt check: `missing_comparisons(data, prepared["comparisons"])` ->
  `WorkerAttention("COMPARISON_NOT_PRINTED")` before any artifact is persisted. `missing_comparisons()` (:267-287)
  extracts the PDF text with pdfplumber (a local import, as the comment says) and searches each comparison's whole
  name at word boundaries. An account with no comparisons never enters the check.
- **yr-211.** `resident_worker.py:413` `RESOLVE_RETRY_VISIBILITY_S = 60`; `poll_once` (:434-441) prints
  `IRPT_RESIDENT_RESOLVE state=<state> code=<code>` for every `resolve_upload` message and, on RETRY, sets that
  message's visibility to 60 s; READY/ATTENTION delete as before; nothing else in the loop moves.
- **Unchanged, read:** the st3 saved-type refusal (:207-209), the printed-type check, certification, publication; no
  Lambda, IAM, queue, schema or Terraform member.

## 2. The artifact, read here on its own bytes

- **Tar** `ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz` S3 version `jK0FFkzC` (08:11:26Z)
  hashes to `7d10152cd8...` (730,824 bytes); st3's `vDS2rcSq` to `26769a3790...`. **226 file members each** (the
  packet's "266" is a typo; `SHA256SUMS` lists 225 = the members minus itself), nothing added or removed. Four members
  differ: `ycharts/generate/recipe.py` (4fde9ac9 -> **b2fbd720**), `ycharts/generate/resident_worker.py` (95f79dad ->
  **0b67be2a**), `reports/resident_bindings.json`, `SHA256SUMS`. The two `.py` members hash equal to the repo at
  `14c961af32` and at HEAD.
- **Install script** `resident_host_install_st4_20260929.sh` (sha `7423a589`) diffed against st3's: only the ledger
  comment, NEW/OLD roots, KEY, the three WANT shas, the two error strings and the receipt's ledger change; the
  10-member check, factory pre-check, empty-queue stop, 30-second Traceback watch and the rollback to st3 are st3's.
- **Tests on these bytes (this seat's runs, HEAD == the tar's two members):** `ycharts/generate/tests/` **290 passed,
  30 skipped, 32 subtests** (85 s); ~Y's `R19_CHECKS/test_r19_y1_pregen_static.py` (the st3 rule, regression) and
  `R20_CHECKS/test_r20_y1_comparison.py` + `test_r20_y2_resolve_retry.py` (the two cells) **9 passed**; ~Y's
  `R22_CHECKS/test_r22_y1_resolve_bounded.py` **2 failed, 1 passed** -- the two failures are the round-22 base
  (`RESOLVE_MAX_RECEIVES` absent; no `ApproximateReceiveCount` asked), which is the point of section 3.

## 3. The bound, read (the CTO's condition): the queue dead-letters on the 5th receive

- **Live** `irpt-generation` (`resident_bindings.json` `queue_url`): `RedrivePolicy {"deadLetterTargetArn": ...irpt-generation-dlq,
  "maxReceiveCount": 5}`, `VisibilityTimeout 900`, `MessageRetentionPeriod 345600`; declared at
  `infra/aws/terraform/investor-reporting/core/sqs.tf:40-42` ("a message that fails five handlers is a poison"). The
  DLQ holds **1 message today** (retention 14 days), unrelated to this act.
- **What happens at it, read from the code:** a `resolve_upload` that keeps answering RETRY is received five times --
  under st3 that is 5 x 900 s (about 75 minutes of patience); under st4 it is **5 x 60 s (about 5 minutes)** -- and
  then SQS moves the message to the DLQ. The worker writes nothing: the NORMALIZATION row stays RESOLVING. The
  recovery is the client's own poll: `intake/uploads.py _answer` re-dispatches a RESOLVING row whose `dispatched_at`
  is older than `REDRIVE_SECONDS` = 960 s (`upload_resolution.py:24`), which sends a fresh message. So the vendor is
  re-read at most 5 times per message and at most once per 60 s; a stuck upload costs 5 reads per 16-minute cycle for
  as long as the client keeps polling, and one DLQ message per cycle. Bounded per message and per cycle; not "the job
  ends ATTENTION".
- **Round 22:** `TO-IB-yr-221` (@52e63f09ee, worker ~73, `resident_worker.py` only) adds `RESOLVE_MAX_RECEIVES = 4`,
  asks SQS for `ApproximateReceiveCount`, and at the 4th receive deletes the message by name
  (`IRPT_RESIDENT_RESOLVE state=GAVE_UP code=RESOLVE_RETRY_EXHAUSTED`), the row still RESOLVING for the 960 s redrive.
  Its order says served code moves only through ~P's st4 REBUILD. Tar `jK0FFkzC` does not carry it.

## 4. Blast radius, read from the producer's own rule

- **One writer** of a job's outcome, `ResidentGenerationWorker`.
- **Comparison / Multi-Comp (moves):** before, a Comparison generated with `["P:<id>"]` alone and a PDF printing no
  comparison published READY (window 21 Y1, S194); after, the models are sent and a PDF whose text lacks a chosen
  comparison's name stops ATTENTION `COMPARISON_NOT_PRINTED` before persistence. The check is by printed NAME: a
  vendor PDF that names the comparison differently from the selection's `name` refuses a good report (fail-closed,
  never fail-open).
- **resolve_upload RETRY (moves):** the 900 s lease becomes a 60 s re-offer with a log line; the 5-receive bound and
  the 960 s client redrive are unchanged infrastructure.
- **Unchanged:** Overview, the st3 rule, every non-Analysis path, generate/status/export Lambdas, IAM, queues,
  schemas. A job resumed from an st3 checkpoint reads the new code at its next step.
- **Rollback per key:** the st3 root stays on the host; the receipt is copied aside before the write; the script rolls
  back on rc != 0, an inactive unit, no poll, or a Traceback within 30 s.

## Conditions

1. **The tar installed is named by S3 version in the ledger with ~Y's R22 check run on ITS bytes and the result
   recorded before the SSM run.** If it is the rebuilt tar carrying IB-yr-221, the check reads 3 passed and the bound
   is 4 receives then GAVE_UP by name. If it is `jK0FFkzC` as built, the check reads 2 failed and the ledger names the
   bound as section 3 reads it (5 receives, DLQ, the 960 s client redrive) and reads the DLQ's message count before and
   after the first Analysis window. Either is signed; an install whose bound is not written down is not.
2. **~Y's four gates PASS on the built tar are in the ledger before step 4** (this seat's st3 condition, carried), and
   the install's own read-back (root `fe64236bbb-st4`, recipe `b2fbd720`, worker `0b67be2a`, polls, 0 Tracebacks) is
   the D1 proof, never the SSM rc alone.
3. **The first Analysis window after st4 records, per body, the `IRPT_RESIDENT_RESOLVE` line(s) and any
   `COMPARISON_NOT_PRINTED` stop as the named terminal states they are**, so the two fixes are read live rather than
   assumed from the tests.

## Named items (not refusal grounds)

1. The name-based PDF check is the only oracle for "the comparison was printed"; a vendor rename of a model refuses a
   good report. Fail-closed is the right side, and the refusal names itself.
2. `report_security_ids` takes the template's `comparison_securities` bounds, so a template with `max` 0 refuses any
   comparison by name rather than silently dropping it.
3. The DLQ holds 1 message from before this act; no consumer of the DLQ exists (none is asked for).
4. Under st4 without yr-221, a resolve that never succeeds cycles every 16 minutes while the page polls; the vendor
   cost is 5 reads per cycle, not unbounded, and the walk windows are the only Analysis traffic today.

## What this half signs against

- Packet blob `4f34a600`; commits f287444013 and 14c961af32; ledger `irpt-resident-st4-yr201-yr211-20260929`.
- Tar `7d10152cd8` (S3 `jK0FFkzC`) with its 226-member census against st3 `26769a3790`; install script `7423a589`.
- The bound in section 3 as read live at 08:4xZ; the blast radius in section 4; the three conditions.
