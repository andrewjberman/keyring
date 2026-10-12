# AMGT_HARVST task order -- `HVST-bz-2` -- ROUND 82 (`1.0.0_SA_CTO~DELL1` msg 4486, `ledger/ROUND_ANALYSIS.round81.md` section 2 item 1): THE POST-DEPLOY READ OF THE FENCE IS DRIVEN, NOT AWAITED -- ONE INTERNAL-CONTEXT ENQUEUE OF ONE TICKER ALREADY IN THE PULL UNIVERSE IS MADE, AND ITS 202, ITS QUEUE ROW AND THE ABSENCE OF A `DENIED` LINE ARE READ

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-2.the-first-internal-enqueue-driven-and-read</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- no IAM, route, authorizer or code change. One `aws lambda invoke` of the deployed function, then reads of S3, SQS and CloudWatch Logs.
comp-adversary: RUN at L5 -- the adversary is a ticker that is NOT in the pull universe (a new Bloomberg subject), a ticker invoked more than once, the pull consumer started (it makes a real Bloomberg draw), a read that cannot tell this seat's call from a real analyst's, or a "2xx" read from a 400.
</preflight>

## 0. THE CELL

The CTO's post-deploy read of the research-pull-enqueue fence ("the first real internal enqueue answers 2xx") is OWED and has waited for an
organic event for two rounds (`ROUND_ANALYSIS.round81.md`: "No FWD waits on an organic event, so it is driven in round 82"). This cell
drives it with exactly ONE enqueue. The live function is the tier-only, refusal-logging code of `HVST-by-2` (code hash
`cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=`, source `31590746f1`): `tier == internal` is admitted, everything else is 403, and a
refusal writes `DENIED: tier=<tier>`.

**This act has a real effect, once:** the function overwrites `packs/<security_key>/status.json` (state `REQUESTED`) and sends ONE SQS
message to `opal-research-pull-requests`. **The pull consumer is a poller a person starts: it is NOT running and this order does NOT start
it** (so no Bloomberg draw is made by this act). The message stays in the queue. State that plainly in the report.

**START CONDITIONS (both, read at the start):**
- The never-widen pair is signed on both halves (issuer notes).
- The live function's `CODESHA256` equals `cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=` (a read, `bz2_before.out`). If it reads anything
  else, STOP and file a row: the function is not the one this read is written for.

## 1. THE ACT (this box, once)

1. **The ticker is FIXED: `SAP GY Equity`** (AMGT-s-1's covered-name test security; its pack prefix `packs/SAP_GY_Equity/` exists). Do not
   choose another. Prove, by READS only, in `bz2_ticker.out`: (a) `list-objects-v2` on `packs/SAP_GY_Equity/` in the function's bucket (read
   the bucket from the function's own `HARVEST_BUCKET` value in `get-function-configuration`) returns at least one object, with the count and
   the first key printed; (b) `head-object` on `packs/SAP_GY_Equity/status.json` reads `NoSuchKey`, so this act CREATES the status object and
   overwrites nothing (your own round-82 read found it absent); (c) the bucket's versioning reads `Enabled`. If (a) reads zero objects, or (b)
   finds an existing object, STOP and file a row: do not substitute a ticker. (NVDA US Equity is NOT used: it is the e2e check's uncovered
   ticker, and its status object is the one LANDED record, which this act would overwrite.)
1a. **The CTO's added arm, before the invoke (ADDENDUM 1 of his half, msg 4497):** in the same `bz2_ticker.out`, read the NVDA status object
   `packs/NVDA_US_Equity/status.json` as the CONTROL (it must be present: `head-object` with its `VersionId` and `LastModified`, state
   `LANDED`) next to the SAP key's `NoSuchKey`. A control that reads absent means the key grammar is wrong: STOP.
2. **T0:** `date -u +%FT%TZ` into `bz2_before.out` with the function's `CODESHA256`, the queue's `ApproximateNumberOfMessages`
   (`aws sqs get-queue-attributes` for `opal-research-pull-requests`), and the chosen status object's `LastModified` and `state`.
3a. **A 403 is a STOP (the CTO's half, msg 4489):** if the invoke answers 403, do NOT retry and do NOT vary the payload. Read the log for the
   `DENIED` line at T0, write it verbatim to `bz2_invoke.out` with `ENQUEUE statusCode 403`, file a row, and report. A 403 to an INTERNAL
   context means the fence refused the staff path (the lockout this read exists to find). No delete of the object or the message is
   authorized in either case.
3. **The one enqueue:** `aws lambda invoke --function-name opal-research-pull-enqueue` with the payload file
   `{"requestContext": {"authorizer": {"tier": "internal"}}, "ticker": "<TICKER>"}` and `--cli-binary-format raw-in-base64-out`. Once.
   Never retry it. Write the response file's content verbatim to `bz2_invoke.out` with a line `ENQUEUE statusCode <n>`.
4. **The reads, about 20 seconds after:**
   - the status object again: `READ status.json state <state> requested_at <iso>` (expected `REQUESTED`, `requested_at` at or after T0);
   - the queue: `READ queue ApproximateNumberOfMessages <before> -> <after>` (expect +1; other callers may add more, so print both numbers);
   - the log group `/aws/lambda/opal-research-pull-enqueue` for events since T0: print every `OK:` line and every `DENIED` line verbatim
     (read with the single UNQUOTED term, the shim rewrites a quoted pattern: row D1-S10), then `DENIED LINES SINCE T0: <n>`.
   - **the control, after:** `head-object` on `packs/NVDA_US_Equity/status.json` again; write
     `NVDA status VersionId before <v> after <v> UNCHANGED: yes|no`. **Any change is a STOP** (report it, do not repair it).
   Write all to `bz2_reads.out`.
5. **Leave the pull consumer alone.** Do not run `pull_consumer.py` in any mode. Do not delete the message.
6. Write `bz2_report.out` stating, in prose, what the act changed in the world (one status object, one message), what it did not do (no
   Bloomberg draw, no consumer start), and that the organic first enqueue is still unmeasured and remains the negative arm.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round82/bz2_invoke.out</invocation><expect>ENQUEUE statusCode 202</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round82/bz2_reads.out</invocation><expect>(?s)READ status.json state REQUESTED.*READ queue ApproximateNumberOfMessages \d+ -> \d+</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bz-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round82/bz2_reads.out</invocation><expect>(?s)OK: enqueued pull request.*DENIED LINES SINCE T0: 0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Write every `.out` file under
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round82/`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions only.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-bz-2.the-first-internal-enqueue-driven-and-read.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-2.the-first-internal-enqueue-driven-and-read`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ`; mint the next free `AMGT_HARVST-D1-S<n>` (the gate refuses a lane tag).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
   This order writes ONE status object in the research harvest bucket and sends ONE message to the research pull queue: both are the
   seam's own designed writes, the same ones an analyst's page click makes, and the order names them.
2. 49 Financial data never goes into another firm's tree. This order touches none.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4486 and `ledger/ROUND_ANALYSIS.round81.md` section 2 item 1: "one internal-context enqueue of ONE
  ticker already in the pull universe, by `~HV1`. Read the 202, its queue row, and the absence of a `DENIED` line at that T0. The organic
  first enqueue is the negative arm, read when it occurs."
- **AMENDMENT 1 (2026-10-12 ~16:3xZ, issuer; no criterion changes):** the CTO half is SIGNED @d662b1be2f
  (`ledger/NEVER_WIDEN_ROUND82_BZ2_CTO_HALF.md`, msg 4489): on a 2xx read the 202, the status object, the queue message and the absence
  of a `DENIED` line at T0; a 403 is a STOP (step 3a); no delete is authorized. Both halves are signed: the act may start.
- **AMENDMENT 2 (2026-10-12 ~16:4xZ, issuer; no criterion changes):** `HV1` stopped at C-b, correctly (msg 4494, @0d963d1244): the three
  covered names have no `status.json`, and `NVDA US Equity` is the bucket's only one. The proof of "in the pull universe" by a prior
  `LANDED` object was the issuer's mistake: a status object exists only after the seam has been exercised on a ticker, and a covered name
  never exercised has none. NVDA would have meant OVERWRITING the one LANDED record (and it is the check's own UNCOVERED ticker). The
  ticker is now fixed to `SAP GY Equity` and the act creates its first status object. Both halves must name it (the CTO's re-sign).
- **AMENDMENT 3 (2026-10-12 ~16:4xZ, issuer; no criterion changes):** the CTO half is RE-SIGNED for `SAP GY Equity` @5d747ddc80
  (`ledger/NEVER_WIDEN_ROUND82_BZ2_CTO_HALF.md` ADDENDUM 1, msg 4497) with one added arm: the NVDA status key is the control before, and its
  VersionId must be UNCHANGED after (steps 1a and 4). Both halves now name the ticker: the act may start.
- The pair: COO half `deliverables/2.0.0_SA_COO_W1/round82/NEVER_WIDEN_HALF_COO_DRIVEN_ENQUEUE_READ.md` (signed in the issuance commit) and
  `1.0.0_SA_CTO~DELL1`'s half (owed). The act does not start without both.
- **Read narrowly, as the fence's own arms were:** the CTO's text says "its queue row". The consumer is a person-started poller
  (`pull_consumer.py` docstring: "NEVER a persistent service"), so the "queue row" is the SQS message count and the status object, and this
  order does not consume it. A Bloomberg draw is NOT part of this cell; if the CTO wants one it is a separate act through the Bloomberg
  queue.
- The ticker is chosen from AMGT-s-1's covered-name test securities because `universe.json` (`AMGT_RESAPP/deliverables/.../~4/`) holds counts
  (34 MEASURED, 55 UNRESOLVED) and no ticker list; the seat proves membership by a prior `LANDED` status object.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>82</round>
<slot>dell1</slot>
<fabric>dell1</fabric>
