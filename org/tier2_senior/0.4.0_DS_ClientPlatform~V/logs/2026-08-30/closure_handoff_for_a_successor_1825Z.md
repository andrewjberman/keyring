# 0.4.0_DS_ClientPlatform~V — CLOSURE HANDOFF, written 2026-08-30 18:25Z for a successor who was not here

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE

Written under the Andrew-direct edict of 18:2xZ (*"a clean context reset and alignment check would
be beneficial for these continued works"*). **This closes a CONTEXT, not the work.** Nothing below
is cancelled, complete-by-default, or narrowed. The companion log for this window is
`session_close_0920-1815Z.md` @`7a62439475`; that one is written for this fabric, **this one is
written for a reader with zero prior context** and wins where the two differ in plainness.

---

## 0. WHO THIS SEAT IS, IN PLAIN TERMS

`0.4.0_DS_ClientPlatform~V` is a Data Science (DS) lane worker on the `~V` sub-lane. Its base
serial is `0.4.0_DS_ClientPlatform`. Its issuer (the seat that assigns and accepts its work) is
`2.0.0_SA_COO`; the per-apply gate that authorises deploys is `1.0.0_SA_CTO`; the grader that
scores proofs is `3.0.0_SA_CVO`; the integrator that runs push windows is `0.0.0_AB_MSTR`.

**Its home directory is `org/tier2_senior/0.4.0_DS_ClientPlatform~V/`.** Deliverables (proof
instances, records, templates) live in `deliverables/`, logs in `logs/{date}/`.

**Its inbox is NESTED at `org/mcp/inbox/0.4.0_DS_ClientPlatform/~V/`** — base directory, then a
`~V` subdirectory. ⛔ The flat path `org/mcp/inbox/0.4.0_DS_ClientPlatform~V/` **does not exist**
and lists identically to an empty inbox. The issuer nearly filed a false delivery-gap on exactly
that today. A zero from the wrong path is out-of-corpus, not absence.

---

## 1. THE VOCABULARY A SUCCESSOR NEEDS (nothing below assumes it)

| term | what it actually is |
|---|---|
| **INF-ONEWRITER** | A project cell asking: the AWS Lambda function `inf-silver-chain` and an EC2-hosted dispatch script BOTH wrote the same S3 keys daily. Goal: redeploy the Lambda onto current code, then retire the second writer so ONE writer remains. **Closed CORRECT today.** |
| **`inf-silver-chain`** | An AWS Lambda that builds "silver"-layer parquet tables daily at ~11:18Z into `s3://opal-data-inf/silver/api_dims/{key}/snapshot_date={D}/data.parquet`, for keys `performance`, `billing`, `tax_unrealized`, `tax_realized` (plus 3 stages that fail for non-code reasons). |
| **the second writer** | `orion-gold-dispatch.sh` running on EC2, which pulled current code at run time and overwrote the Lambda's output ~37 minutes later each day. **Its billing leg was retired 2026-08-30 14:03:13Z.** |
| **arm A / arm B** | The two halves of the acceptance test for that redeploy. **Arm A:** the Lambda's write is value-equal to the SAME-DAY object the second writer left. **Arm B:** the Lambda's new write differs from its own last pre-deploy output in exactly the expected columns. |
| **PB-1** | One acceptance criterion on a proof face named `MDPF_PROVENANCE.T-B`. It asks that a scheduled 13:30Z run of the `mdpf-gold-lambda` function reads a prior-day self-carry AND that the executing bytes contain no read of a retired S3 prefix. **Scored PASS today.** |
| **R7 / card (6)** | A yes/no question carried to Andrew: delete the dormant `json/mdpf/{firm}` S3 prefix. He approved it with a gate. **Executed today.** |
| **V-4** | A post-close obligation on the proof face `OPAL_ADVIPOINTERS.P2F-MARKER-DS`: verify that a "day complete" marker JSON actually gets written by the deployed converter. **NOT YET DUE.** |
| **a "face"** | A JSON proof-of-spec instance in `deliverables/`, one row per acceptance criterion, validated by `.tools/proof-of-spec-check.py`. |
| **a "fire"** | A scheduled (cron/EventBridge) execution of a pipeline. Acceptance reads are timed to fires. |

---

## 2. DONE — closed and verified, with the pin and the instrument

| what | pin | instrument that proved it |
|---|---|---|
| **`layer_dependencies` declared** on `infra/aws/lambda/inf-pipeline/inf-silver-chain/BUILD_MANIFEST.json` — the field that let the build's import-closure check pass | `6ab4c76a0f` | An `ast` import census over the packaged `.py` files: 22 top-level modules = 13 stdlib + 5 local + 4 third-party; `boto3`/`botocore` are runtime-provided so only `pandas`/`pyarrow` are the layer's. Refusal EXERCISED: rc=1 with the field removed, rc=0 with it, tree restored by digest. |
| **Pre-redeploy baseline** of the four served keys | `bc42f4d35b` | Both writers' versions compared per key. **Finding: the code drift reached the OUTPUT on only ONE key (`billing`) of four**; the other three were value-equal cell-for-cell even under the stale code. |
| **Two-arm exercised read** — the redeploy's acceptance | `e88205d404` | Arm A 4 of 4 value-equal (billing 15,487 cells); arm B's column delta exactly as pre-registered. **Cell closed at CORRECT.** |
| **`OPAL_ADVIPOINTERS.P2F-MARKER-DS` face repaired** from INVALID to VALID | `c7e1199b79` | `.tools/proof-of-spec-check.py` at checker vintage `3948c766a7`, rc=0 read UNPIPED. |
| **PB-1 scored PASS** | `924d560a32` | Deployed package DOWNLOADED and bound by `base64(sha256(zip)) == CodeSha256`; 0 code reads of `json/mdpf` in 3,046 lines. |
| **Acceptance template** made durable, then amended | `5dbb7c7795`, `865648b24b` | Adopted by the gate as the per-leg acceptance carrier for a follow-on cell. |
| **`json/mdpf/{firm}` DELETED** — 8 objects, both buckets | `f35367d264` | Four-plane consumer census re-run in the same stretch, then 8 deletes by exact key, rc=0 on all 8. Ledger in `org/critical_paths/change_management/20260830T1742Z_json-mdpf-firm-delete_andrew-card-6.md`. |

**PUSH STATE, MEASURED** (`git ls-remote` + `git branch -r --contains`, read 2026-08-30T18:25:18Z;
origin/CLOUD = `89edf8efc1`): **all eight work commits above are ON ORIGIN.** The companion session
log `7a62439475` is **LOCAL** and rides the next window.

---

## 3. IN FLIGHT — and exactly where it stops if nobody touches it

**Nothing is mid-execution at this seat.** No partial write, no open transaction, no half-applied
change. Every artifact listed in section 2 is committed and complete.

The one thing with an unfinished shape is the **acceptance template's future use**: the follow-on
cell `OPAL_ADVIPOINTERS.INF-REDEPLOY` cites it, but that cell closed with **zero deploy legs
left** — seven of its eight functions became record-corrections (no deploy, no fire), and only leg
**D2** (`inf-etf-ownership-daily`) remains, and it is OPTIONAL. **If nobody touches this, nothing
degrades**: the template sits committed and cited; no deadline passes.

---

## 4. OWED BY THIS SEAT — what another seat is waiting on

**Nothing.** No seat is blocked on `0.4.0_DS_ClientPlatform~V` as of 18:25Z. Every message
addressed to this lane is acknowledged (delivery ledger read directly, not inferred from an empty
inbox directory), and every request received today has been answered or executed.

---

## 5. CLOCK/EVENT-GATED — the fires, what they prove, what failure looks like

### (a) Post-retirement read — **tomorrow (2026-08-31) ~11:18Z**

- **What fires:** `inf-silver-chain`'s daily scheduled run — the FIRST one after the second writer's
  billing leg was retired at 14:03:13Z today.
- **What to read:** `aws s3api list-object-versions --bucket opal-data-inf --prefix
  silver/api_dims/billing/snapshot_date=2026-08-31/data.parquet`
- **What it proves:** exactly ONE version on the key, LastModified inside the Lambda's own run
  window, content equal to today's certified write. That is the one-writer end state.
- **What FAILURE looks like:** TWO versions (the retired writer still ran — a real finding, and the
  retirement did not take), or ZERO (the Lambda did not run or did not write).
- ⛔ **Single-writer now prints as the INTENDED END STATE, not a finding**, because the retirement
  IS on the record. Before today it would have been a finding. The read takes retirement state as
  an explicit input for exactly this reason.

### (b) V-4 — **Monday 2026-08-31's first CONVERTING run**

- **What it checks:** that a marker JSON appears at
  `s3://opal-data-assets/schwab/08335338/meta/complete/date={D}.json` carrying
  `declared_source == "schwab_schemas.SPECS @ 5c7b2a9a6b"`.
- **Current state, and why an empty prefix is NOT a defect:** that prefix holds **0 objects**. The
  producer code IS deployed (2026-08-30T03:37:41Z). The first post-deploy run (12:17:50Z today)
  was a Sunday sweep that converted **ZERO partitions** — `partitions=[]` in its own run manifest —
  so the marker builder had nothing to build from and emitted none BY CONSTRUCTION. **2026-08-30
  was a Sunday; the last trading day was Friday 08-28 and the newest bronze partition is
  `20260828`.** Resolve the trading calendar before calling this stale.
- **What is STILL UNKNOWN:** whether the marker's write-and-verify path works in production. A run
  with no markers to write exercises no write. Monday's first CONVERTING run is the first
  opportunity.

### (c) D2 (`inf-etf-ownership-daily`), ~15:00Z — **only if that optional leg is instantiated**

- Carries an ImportError trap as a gate: the current source requires two modules the deployed
  single-member package lacks, so a redeploy shipping the old member set breaks a currently healthy
  function. The leg's build must assert the member set BEFORE the apply.

---

## 6. ⛔ WHAT IS UNVERIFIED, UNCERTAIN, OR RESTING ON ONE INSTRUMENT

A closure log that reads uniformly clean is the one to distrust. These are this seat's:

1. **The marker write path (V-4) is UNEXERCISED in production.** Everything known about it is
   source-plane. Nothing has yet demonstrated the S3 put-and-verify works when there is something
   to write.
2. **The attribution of the second writer is INFERRED, not measured.** Throughout this cell the
   ~11:5xZ daily overwrite has been attributed to `orion-gold-dispatch.sh` on EC2. That is
   consistent with the timestamps and with the current-code schema, and with nothing else measured
   — **but that runner's own log was never read.** It is labelled INFERRED on the baseline face and
   should stay labelled.
3. **PB-1's "run succeeds" scope was read one of two possible ways.** Read as the self-carry read it
   is met; read as the whole cycle it is not clean (that run ends `12/16 objects built,
   errors=['global']`). The issuer ruled the first reading. **The `global`-scope failure is a
   STANDING condition** — identical on 08-29 and 08-30 — **and it has no named owner.** It is a
   live open question, not a closed one.
4. **`fee_amount` differs in 120 cells** between the stale 08-29 billing object and the post-deploy
   08-30 one. It is REPORTED and UNSCORED, because the period-varying column class could not be
   tested against an object that predates the period columns. Not shown benign; shown untestable on
   that pair.
5. **The date-invariance column classification rests on ONE date pair** (08-28 vs 08-29). Five
   columns read invariant there only because both dates sat inside one billing period; they move at
   a period boundary. Do not bank that table as a definition.
6. **Three failing stages in `inf-silver-chain` are unowned**: `household` and `activity` fail on
   `NoSuchKey` (an absent upstream object) and `accounts_v2` on an absent local rep_map JSON, every
   day, on both measured days. None is code-vintage, none moved on the redeploy, and none has an
   owner named anywhere this seat has seen.
7. **Deliveries to this lane can read SENT-never-EMITTED while having been read.** Two messages
   today were in that state, one of them a directive. Some message files arrive with **no
   `**Msg-ID:**` header at all**, which makes them un-ackable at the moment of reading. **Do not
   infer an id from another seat's subject line** — this lane did that once and 6 of 7 ids were
   wrong. Read the delivery ledger with `get_delivery_state` instead of trusting an empty inbox.

---

## 7. FOUR INSTRUMENT FAILURES FROM TODAY THAT A SUCCESSOR WILL MEET AGAIN

1. **Local time wearing a `Z` suffix.** `ls --time-style=+%Y-%m-%dT%H:%M:%SZ` and
   `git log --date=format:'...Z'` both render LOCAL time. Only `--date=format-local:` honours
   `TZ=UTC`. This shipped once today in a committed citation and produced a figure 4 hours off.
2. **ETag / byte equality as a content oracle on parquet.** Parquet is not byte-deterministic;
   ETag said DIFFERENT on 4 of 4 keys where 3 were value-identical. Compare SCHEMA then VALUES,
   order-insensitively.
3. **A pin that resolves but does not carry the change.** A commit-ish can be valid while its
   content is one amendment behind, and nothing compares the two. The checker gained an
   `introduces:` field today for exactly this.
4. **A broken parser printing a value shaped like a finding.** A flattened JSON capture reported
   "0 delete markers created by this act" moments after 8 deletes returned rc=0. The contradiction
   with something directly observed is what caught it — nothing else would have.

---

## 8. NEXT STEPS

1. **[0.4.0_DS_ClientPlatform~V]** the post-retirement read at the ~11:18Z fire (section 5a).
2. **[0.4.0_DS_ClientPlatform~V]** V-4 at the first CONVERTING run (section 5b).
3. **[0.4.0_DS_ClientPlatform~V]** D2's fire if that optional leg is instantiated (section 5c).
4. **[2.0.0_SA_COO]** the `global`-scope owner question (section 6.3) is unowned and open.
5. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** the IAM grants in `infra/aws/terraform/mdpf-pipeline/iam.tf`
   and the publisher's `json/mdpf/*` write-prefix declaration survive today's delete and were
   carried as a SEPARATE follow-on act. **They have no word and no cell.**
