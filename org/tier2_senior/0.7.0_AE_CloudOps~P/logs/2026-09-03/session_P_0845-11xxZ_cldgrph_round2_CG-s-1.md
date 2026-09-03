# Session log -- `0.7.0_AE_CloudOps~P` -- 2026-09-03 08:45Z - 11:3xZ (ROUND 2)

**Seat:** `0.7.0_AE_CloudOps~P` · **Fabric:** laptop · **Directive:** D0 · **Project:** `NFRA_CLDGRPH`
**TO:** `NFRA_CLDGRPH.TO-CG-B-1` (cell `CG-s-1`, ROUND 2 / STAGE 1) · **Issuer:** `2.0.0_SA_COO~A` · **GO:** 93401
**Archetype:** build + deploy · **Pause:** account-wide usage limit 09:38Z-11:0xZ (issuer 93509; nothing owed)

## Current state

**TO-CG-B-1 is COMPLETE.** The marker write is now a queue message. Proof instance **VALID rc=0**, 6/6 criteria PASS,
deploy ledger **CLOSED** with all 4 legs proven.

The wiring, live: an S3 `ObjectCreated:*` notification on `warehouse/_branch_head.main.json` feeds a new SQS queue
with a DLQ, and a new two-service-trust role holds queue-consume on it. Exercised on **two real producer stamps**.

| | |
|---|---|
| queue | `arn:aws:sqs:us-east-1:313476888478:opal-globgrph-projection-events` |
| DLQ | `arn:aws:sqs:us-east-1:313476888478:opal-globgrph-projection-events-dlq` |
| role | `arn:aws:iam::313476888478:role/opal-globgrph-projection-worker` |

## The turn that mattered

`terraform plan` came back **`8 to add, 2 to change, 0 to destroy`** when the face expected adds-only. My six were
exactly right; **four were foreign** — three Glue partition changes and
`aws_sns_topic_subscription.critical_surface_alerts_email`, an **email subscription to `andrew@opalinvest.com`**.

**I stopped**, which the face names as its own STOP condition. Then `comp-find 'critical_surface_alerts_email'` turned
an unexplained plan line into a documented one: `ZGATES_PREFLIGHT_VERIFIED_20260714.md:37` — *"THE EXCLUSION (must NOT
land)"* — plus a 2026-07-14 CVO P1 flag and a 2026-06-22 precedent for a `-target` apply in this same tree. A bare
apply would have emailed a real person and landed another cell's work.

**These were not peer worktree edits.** `git status` on the tree returned exactly one line — my own untracked file.
They are **committed Terraform never applied**, one of them since **2026-06-17**. That is Rule 22a's DESIRED ≠ APPLIED
axis in the concrete, and it is a standing trap for every seat that applies here.

Filed **`NFRA_CLDGRPH-S13`** BLOCKING and routed to the issuer in the same turn with a recommendation I did **not**
self-execute — an apply is outward-facing and hard to reverse. The issuer adopted it (93430) and amended the face
(`@e23ac771bf`). Then: `-target` on the six → `6 to add, 0 to change, 0 to destroy` → **`Apply complete! Resources: 6
added, 0 changed, 0 destroyed.`**

Verification was **unscoped and by address list**, never a `-target` re-plan (Rule 22's scoped-check specimen): the
whole-module plan returns **exactly** the four known foreign addresses and **none** of my six — a control that fails
both ways. Corroborated on SNS itself: **no email subscription to Andrew exists.**

## Findings worth carrying

1. **The `hosts`-style trap of this cell: `depends_on` the queue policy.** S3 validates queue reachability at
   notification-create time, so without it the apply fails.
2. **A second message shape arrives on this queue.** AWS's one-off `s3:TestEvent` has **no `Records` key**. My own
   first parser crashed on it — carried into B1-AC5 so CG-s-2's consumer does not.
3. **No `versionId` in the events** (bucket versioning Andrew-locked OFF), so object identity is `eTag` + `sequencer`.
4. **The queue reading 0 later was discriminated, not assumed** — the marker's `LastModified` (09:42:42Z) showed the
   producer had been quiet ~88 min and the 3600s retention had expired the message. Quiet producer, not a broken rule.

## ⛔ My own error, disclosed

**I redrove three messages to the DLQ myself.** Collecting bodies, I called `receive-message` **four times**; every
receive increments `ApproximateReceiveCount` *even at `--visibility-timeout 0`*, which I had used precisely to leave
them visible, and `maxReceiveCount` is 3. Benign (no consumer exists; nothing deleted; DLQ self-clears in 24h) and it
does not implicate the wiring — it incidentally exercises the redrive policy. **I did not purge the DLQ**: that would
destroy the evidence. Disclosed in the deliverable (D.3), in B1-AC4's `status_reason`, and in the ledger's L4 proof.

⭐ It is also a real handoff finding: at 30s visibility and `maxReceiveCount 3`, **a worker slower than 30s will DLQ
its own message** — concrete evidence for why CG-s-2 must set the timeout from CG-s-10's number.

## Compiler Tools

| tool | result |
|---|---|
| `aws s3api get-bucket-notification-configuration` (live, ×2 + 2 controls) | BEFORE empty **proven** by a positive control (1486 B elsewhere) and a negative control (rc 255 `NoSuchBucket`); AFTER exactly one rule |
| `comp-read item2b.tf` | surfaced the `:18` retention qualifier I had to mirror |
| `comp-read iam.tf --enumerate assume_role_policy` | 3 hits — the tree keeps `ecs_assume` and `lambda_assume` **separate**, so the two-service trust needed a new document |
| `comp-read main.tf --enumerate locals\|...` | gave `local.account_id`; `local.vpc_cidr = 172.31.0.0/16` independently corroborated round 1's CG-s-11 finding |
| **`comp-find 'critical_surface_alerts_email'`** | **the decisive read** — turned an unexplained plan line into a documented Andrew exclusion with an established handling convention |
| `comp-iam gaps` (before) | delta = 4 lines, all parser denominators; gap totals unchanged; new role adds zero gaps |
| `comp-iam refresh-census` + APPLIED read | 216 → 217 roles; APPLIED matches DESIRED exactly |
| `terraform` init/validate/fmt/plan ×4 | validate Success; fmt clean; module-wide STOP; targeted 6/0/0; unscoped re-plan identical across two runs 90 min apart |
| `.tools/safe-apply.sh` | HALT gate blocked on 2 messages, **both read** (the second stood the first down), then `HALT_ACK=1`; 6 added |
| `.tools/deploy_ledger.py` | `hold` correctly refused while an apply leg was open — left OPEN/RED rather than force-closed with a false proof; then 4/4 legs closed, entry CLOSED |
| `proof-of-spec-check.py` | **VALID rc=0**, 6/6, surprises 1/1 resolving to S13 |

## Next

1. **[`2.0.0_SA_COO~A`]** CG-s-2 (the worker) and CG-s-4/CG-s-5 on these ARNs; the visibility timeout is CG-s-2's.
2. **[`0.7.0_AE_CloudOps` base / `0.8.0_AE_CloudComp`]** their own ~2.5-month unapplied drift in this tree — carried on
   S13 for the L8 seat to route, **not** resolved here.
3. **[`3.0.0_SA_CVO~A`]** L8/L9 on the channel.
