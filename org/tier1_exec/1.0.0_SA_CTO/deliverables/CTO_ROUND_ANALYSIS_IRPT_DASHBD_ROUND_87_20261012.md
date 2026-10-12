# CTO ROUND-87 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-86 L10 slug (2026-10-12 ~17:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2 (relaunched under fc10 addendum 1 @843970c375). **Answers:**
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v51.md` @3959c6611f (3.0.0_SA_CVO msg 6473): 1 row
dismissed (D2-S19, the acceptance read that passed and was acted on), nothing graduates, ARMED 0. **Prior:** the round-86 analysis
@976ca0db4d. **No PRD addendum.**

## 1. What round 86 did

DB-b-164 applied R45 REFRESH 4 under its signed pair (COO half @598347202e, CTO half @e969a090cc): `irpt-49f-reporting-gold-lambda`
moved oNgy4rnr -> i2r7CbVr at 13:58:42Z, MemorySize 3008, plan 0/1/0, targeted re-plan clean. One dry run: 349 s of 765, 1,372 MB
of 2,556.8, 0 objects written (positive control: 13 objects from the Monday fire seen by the same call).

## 2. Measured by this seat

The CTO half's after-read, EXERCISED, is `CTO_DELL2_RELAUNCH_THREE_ASKS_READ_AND_RULED_20261012.md` section 3: live digest, memory,
artifact version and metadata equal to the apply record; the build commit and the four pins are ancestors of origin CLOUD (7 of 7)
and two pinned files hash equal at pin and at CLOUD. The CVO read the same digest at 17:35Z. Nothing else was re-measured.

## 3. ENRICHMENT LIST for round 87

Nothing is cut now. The order stays as round 86 fixed it:

1. **Ledger leg L5** (2.0.0_SA_COO~D2): the scheduled call site read at the 2026-10-13 11:41Z fire (memory on the call site, the
   three added keys, `method_version` 2, six-key thresholds). The ledger entry
   `org/critical_paths/.open_deploys/irpt-dashbd-r45-refresh4-20261012.json` closes on that read, or the kept version
   `qh361rTWYO2VtgsirsJXq6kiqJEVBDpZ` is restored the same session.
2. **Then the thresholds-file swap's pair**, signed only after item 1 reads clean. This wait is the signed pair's own condition:
   the call-site keys are written only by the scheduled event, and a driven invoke with that event would write served output
   outside a pair. It is one scheduled fire, under 24 hours away.

The tie-out against Black Diamond stays unworked until Andrew's two answers (round 86 section 4); no read by a seat decides it.

## 4. Acts only Andrew can do

The other system's written statement of its flow timing (now open-calls act on dell2's list). **Correction (~20:5xZ):** the
tolerance FWD-8 is graded on is NOT open: 0.35pp was ruled 2026-10-09 (`CTO_RULING_IRPT_DASHBD_FWD8_TOLERANCE_035PP_20261009.md`,
call `dell2-20261009T140136Z-2f53` CLOSED); the round-86 analysis listed it as Andrew's in error, and this file repeated it.

## 5. What this analysis did not measure

The dry run's figures and the Monday fire's are the issuer's and the CVO's reads.

-- 1.0.0_SA_CTO~DELL2
