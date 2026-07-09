# PII / firm-sep incident-#9 tail — FILED-SOVEREIGN-DEPRIORITIZED

**Author:** 2.0.0_SA_COO | **Date:** 2026-07-09 | **Status:** CLOSED-AS-FILED (not remediated)
**Supersedes the operative status of:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_PII_schwab-reidentification-key-exposure-class-brief-20260709.md` (`810973b19`)

## Why this file exists

The PII class had **no project code, no PRD, no TO, and no completion gate** — it executed as loose
incident work off an inbox thread (CTO's finding, and the reason it expanded to fill the attention it was
given). This file is that missing close condition.

It also closes a **durable-artifact hazard**: brief `810973b19` still reads *"legs 1-3: CTO-GO'd,
UNAPPLIED"* and still cites MSTR's **retracted** Tier-0 hold as live provenance. The sovereign kill order
exists only in MCP traffic. A successor agent reading that brief cold on startup gets *"GO'd — go apply
it."* That is exactly how `0.5.0_AE_OpalETL` started its 2026-07-09 session. Anyone reading the brief must
read this file with it.

## The sovereign ruling

Andrew, 2026-07-09, via MSTR at the source (`20260709T182954Z`), verbatim:

> "Stop legs 1-3 too. Pull 0.5.0 fully onto NFRA_TERRAFORM. The exposure stays open and bounded by
> route-absence until we choose to reopen it."

Preceded by, to CTO: *"this is not a priority"* (re: the schwab PII bucket).

This ruling **overturned** CTO's judgment ("stopping a live security remediation mid-flight is worse than
finishing it"), MSTR's concurrence, and COO's re-scope. The sovereign owns the risk appetite. The execs
owned the accuracy of the briefing; that part held. **Do not re-litigate it. Do not "helpfully" resume it.**

## Disposition

| Item | State |
|---|---|
| Legs 1-3 (partners wildcard narrow; opal-news `AmazonS3ReadOnlyAccess` detach; class-level prefix separation) | **KILLED.** Never applied. Zero mutations. |
| Leg 4 (destructive on PII) | **BLOCKED-SOVEREIGN.** Unchanged. |
| Estate-bucket sweep (14 of 17 `opal-data-*`) | **FILED, not driven.** |
| CTO Q4 (S3 data events on schwab/cot) | **FILED, not driven.** No selector widened. |
| CTO 5b (cot object reads forensically unlogged estate-wide) | **FILED, not driven.** Real, not urgent. |

## The accepted open exposure — stated plainly so the tracker is honest

`0.5.0` confirmed on live at ~18:2xZ, grounded (`get-role-policy`, not `comp-iam` DESIRED):

```
partners-lambda-role : ReadPartnerBuckets Resource = opal-data-*, opal-data-*/*   (still wildcard)
opal-news-lambda-role: attached = ..., AmazonS3ReadOnlyAccess, AmazonDynamoDBFullAccess  (still attached)
```

Both unsanctioned reaches into `opal-data-schwab/03_mappings/` — the Schwab **re-identification key**, which
sits in one bucket alongside both the raw client PII (`01_raw/`) and the anonymized output (`02_anonymized/`)
— remain **ALLOWED today**. CTO independently re-verified this on live AWS rather than accepting the
producer's self-report.

**The exposure is bounded by ROUTE-ABSENCE, not by IAM.** `opal-partners-data` never names a bucket; it
resolves `FIRM#{id}.s3Bucket` from `opal-users-v2`, and no firm record maps to `opal-data-schwab`. So no
route can serve from it *today*. A new firm record, or any code path that names the bucket directly, removes
the bound. **Bounded is not closed.** This is recorded as an **OPEN, ACCEPTED** risk — not a closed item.

## Close condition (this tail is CLOSED)

**CLOSED-AS-FILED, 2026-07-09.** The tail closes on the sovereign deprioritization itself, not on
remediation. Nothing further is owed. The earlier COO-authored close condition ("closes when legs 1-3 are
applied + exercised + CTO's diff gate passes") is **VOID** — `0.5.0` correctly flagged that legs 1-3 will
now never be applied, so as written the tail could never close.

## Standing fence — survives the kill order and every future priority shift

`opal-data-schwab/03_mappings/`: **no read, no move, no delete, no re-key, no lifecycle.** Fabric-law
(MSTR-ratified) until **Andrew personally** lifts it. Reading the re-identification key to characterize it
*is* the exposure, performed.

## To reopen

Requires an explicit Andrew decision. The remediation design survives intact in `810973b19` and in
`0.5.0`'s session log; nothing needs re-deriving. Note that the IAM root cause — attachments invisible to
Terraform `plan`/`drift` — is being closed on its own merits under **NFRA_TERRAFORM TO-1/TO-2**, which is
where `0.5.0` was redirected. A future TERRAFORM coverage pass will surface these same two grants as
over-broad in its normal batch order.

## Lessons banked (they outlived the incident)

- **"A 0-result is a claim about my query, not about the world."** (`0.5.0`) A lowercase `pk` scan of
  `opal-users-v2` returned 0 records; trusting it would have narrowed the partner grant to nothing and
  broken the API for all 6 firms. The live keys are `PK`/`SK`, source-confirmed at
  `opal-partners-data/lambda_function.py:300-312`.
- **A belt that enumerates resources covers only the resources you thought of.** The belt missed
  `AmazonS3ReadOnlyAccess` because it enumerated three bucket names literally. The sweep then repeated the
  error at the bucket layer; the CloudTrail selectors repeat it again at the audit layer (2 of 17 buckets).
  Same defect, three layers. **Enumerate the actual universe from the account.**
- **A control that cannot see must not report "clean."** An absent CloudTrail selector answers "nothing
  found" to every question ever asked of it. Cousin to CVO's GCONTR value-check reporting `CLEAN` on an
  injected violation it was structurally blind to (fixed to read `UNDISCRIMINATING`).
- **A relay can authorize a stand-down or a reversible act; it cannot authorize a deletion.** (MSTR)
