# /self-drive NFRA_OPSEC202609 -- ticks 13-16 (2026-09-03 ~16:4xZ-18:2xZ), 1.0.0_SA_CTO~Z

state: ARMED | cron 30635e1e (:13/:43) | carrier org/XXX.md Step 1b-F CTO row | paired: solo | last log: tick 12 @b869fbc8de
scope: NFRA_OPSEC202609 (D12, site-z) -> 1 project (1 of 13 live directives) | device SITEZ | completion: NOT DONE

## Calls and verdicts

Zero calls pitched across all four ticks. Zero new verdicts. **Two SELF-CORRECTIONS by `3.0.0_SA_CVO~Z` of its own
tick-6 verdict**, both caught by a worker's mandated pre-write re-read, both landed here:

1. **AMEND D's split was wrong by one in each direction** -- 39 = 21 non-OPTIONS + 18 OPTIONS, not 20 + 19, and the
   fallback denominator is 21. **Load-bearing:** a worker taking the fallback at 20 attaches the authorizer to 20
   methods, prints 20 of 20, PASSES, and leaves one real data method open -- the outcome FWD-1 and FWD-2 exist to
   prevent, produced by a criterion that reads as satisfied. Landed as ledger **correction row 5** (append-only,
   citing row 3) plus the project row's phase @bd12c75664.
2. **AMEND C's bar contradicted itself** -- "0 to add" beside a clause mandating a deployment that cannot be imported
   and must therefore be added. The CVO's root: it transplanted the Z-S14 bar from a pure-import cell to an adoption
   that necessarily creates a resource, without re-checking the premise.

**This seat re-measured the split independently before landing it** rather than accepting the correcting seat's
number: `get-resources --embed methods`, no `position` key so one complete read, 38 resources / 20 method-bearing /
39 methods / NONE on 39 of 39, per-verb OPTIONS 18, GET 12, POST 7, PUT 2. Agrees with the worker and the CVO.

**And this seat's own exposure on it, stated:** row 3 recorded the wrong figure verbatim, and this seat validated
that verdict's grounding at three pins without measuring the split it asserted. The pins covered C-10's scope, the
cell's denominator and the DESIRED plane. None was the OPTIONS partition. **A grounding check that reads every pin
an author offers still misses the number the author never pinned.**

## Driver acts

| act | vintage |
|---|---|
| ledger correction row 5 + phase, on the CVO's self-correction, re-measured first | @bd12c75664 |
| `org/XXX.md` Step 1b-F promoted to a heading -- it was the one subsection of Step 1b in bold, so a heading probe reported it ABSENT and a worker concluded the only stated source of truth on loop authorization does not exist | @3bde8d1bac |
| Andrew-direct record: "iron out these kinds of issues" -- six friction instances, each with cost, fix and holder | @73e8c0259a |
| Z-S50 disarm: the sanctioned fixture's header claimed to be "the ONE structured home" and that the memory corpus points there; both false. Header now names the second home inside the portal submodule, why a superproject search cannot see it, and the MFA measurement | @60bdb15654 |
| **PRD v0.11 -- C-16 OVERSTATED the log destination's controls** | @d9e5b3dc00 |

## The one that matters: C-16 asserted controls that do not exist

`0.7.0_AE_CloudOps~S`, running the OP-s-28 ALIGN limb, found that C-16 describes both service grants as "each scoped
to its own prefix with SourceAccount + SourceArn". **Measured on the applied plane: of four asserted condition slots,
ONE is present.** The CloudFront grant carries `aws:SourceAccount` and no `SourceArn`; the ALB grant carries
**neither**, its only condition being `s3:x-amz-acl`. So that grant is **not account-scoped at all** -- a
confused-deputy exposure on a bucket that receives log deliveries. Both grants carry `s3:x-amz-acl`, which v0.10
never mentioned: an under-statement beside the over-statement. The prefixes and the non-TLS deny ARE as claimed.

**The gap is NAMED, not NORMALISED.** Correcting the text to match a weaker world would retire the requirement by
describing it away. C-16 now states the three statements as they read AND says the shortfall is a shortfall; the
correct end state stays C-15's form, and hardening is WORK on row Z-S57 with the issuer, because it touches a policy
under live delivery and needs its own delivery-continuity evidence.

**Why nothing else caught it:** the declaration agrees with the world, so the align's plan is legitimately 0 changes
and the STOP-on-any-plan-line correctly does not fire. Nothing in the pipeline compares either plane against the
CONSTRAINT that authorised them. That needs a seat reading the constraint beside the artifact, which is what an align
limb is for. **Sixth referent in this document asserted from a reading rather than a measurement; fourth caught by a
worker at its pre-write read.**

## Andrew asked two questions and both were answered with measurement

**"Why are Tier-2 agents troubleshooting instead of following the flow?"** They are not. They filed 20 of 56 rows and
11 of 12 blocking ones -- the row mechanism, used as designed. The specs were written from readings, not
measurements, and L7 is the first live contact after L1's brief, so every unmeasured referent surfaces in the
worker's hands at the last possible moment.

**"Where are the breaks?"** Measured over 401 message deliveries dated today: **1.0.0_SA_CTO~Z 115, 2.0.0_SA_COO~Z
92, 0.0.0_AB_MSTR~Z 92, 3.0.0_SA_CVO~Z 59, both workers combined 42.** Eighty-nine percent is senior seats talking to
each other, and this seat is the single largest source. Four named breaks: a row creates a Tier-1 obligation rather
than resolving in place, so 56 rows produced 400 messages; a worker's queue is one deep, so a blocking row is a
line-stop with nowhere to move; senior seats use messages where the law already says row-or-log; and error correction
compounds at roughly five artifacts per error, with senior seats originating most of them.

**Ticks 15 and 16 sent ZERO messages.** The C-16 amendment shipped with no broadcast -- row Z-S57 is the carrier and
already names both this seat and the issuer.

## Scope state

| measure | value |
|---|---|
| cells | 28: 6 COMPLETE, 2 APPLIED/round-1-done, 2 IN-FLIGHT, 3 HELD, 15 OPEN |
| task orders / valid proof instances | 9 / 7 |
| rows | 61, ARMED 22 |
| open deploy ledgers | 1 (the S17R-28 logging limb) |

`2.0.0_SA_COO~Z` accepted TO-OP-S-2 at 17:20Z and flipped five cells at v0.1.8. It also measured this seat's
OP-s-5/OP-s-8 observation and found they split: OP-s-5 was lag and is flipped; **OP-s-8 is deliberate, and the open
limb is now MEASURED open** -- three identity tables sit on the AWS-managed default key, not the project CMK. That
alignment has not happened and everyone assumed it had.

Completion test: **NOT DONE** -- 1 of 1 REACHABLE, 0 complete. RESERVED cards at Andrew on this scope: **none**.

## Compiler Tools

- the split: `get-resources --embed methods --limit 500` with a pagination control, per-verb census as a second cut
- C-16: `get-bucket-policy`, three statements read whole for Sid / Resource / Condition
- v0.11 graded through the conformance limb's real entry point with its ran-discriminator present
- the traffic census: every `20260903T*.md` under the inbox tree, sender parsed from the filename, denominator printed
- push state: LOCAL
