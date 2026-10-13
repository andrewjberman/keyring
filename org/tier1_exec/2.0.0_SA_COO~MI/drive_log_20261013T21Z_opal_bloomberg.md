# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX round 10: MX-c-8 drained, two ARMED rows disarmed, MX-r-11 A1 -- 2026-10-13 20:2xZ-21:4xZ (host opal_bloomberg)

**archetype:** DRIVE FORWARD (L7 drain + RULE)

## Ticks and events

| time | act |
|---|---|
| 20:2xZ | msg 33732, 1.0.0_SA_CTO~Z: Andrew's call 8 widens the harvest bucket to all 24 prefixes (list v4). Round 10 drains AS CUT on v3; row Z-S105 (INERT) carries the widening to the round-10 analysis |
| 20:3xZ | msg 33743 (Andrew-direct relay, /keep-driving): `/canonical-drive NFRA_MCPINDEX` armed hourly at :17 (job b21e4e7a). The LIVE_ARMS row reached CLOUD @81ef5aa2db (msg 33756). The lane deletes the loop when the project re-parks |
| 21:2xZ | Worker ~33 reported MX-c-8: AC1-AC3 PASS, proof VALID, e4d01b489f. Drained by safe-merge @212f2370a3 (32 paths, 0 dropped, 0 foreign). Re-run at the merged index: 3 of 3 PASS |
| 21:3xZ | ARMED rows ruled. Z-S106 rules Z-W33-S3 INERT: the duplicated `entity` reaches no app reader. Z-S107 rules Z-W33-S4 INERT: 7 base failures are carried as known |
| 21:3xZ | msg 33788 (MSTR~Z GC ask): C:/tmp/mx-dep-r10 LANDED and superseded (both shipped blobs equal trunk at MX-r-10's close). Answer: tag the tip on origin, then remove |
| 21:4xZ | MX-r-11 A1 @543b25a015. r11.AC3 was unsatisfiable as cut (the issuer's defect): every (a) depth reads absent. It is re-cut, its planted arms are exercised, and the live run reads PASS. PHASE A is held to MP-z-5's ledger close (MP-z-5 pending @81e079ba4b) |

Tick row: `NFRA_MCPINDEX | L7 | 10 | TOs 1/2 | cells 2/2 | thread none | drained c-8, A1 on r-11; r-11 waits on the gateway slot`.

## Measured

- Partition at the deployed commit 185dc04888: N=67, a=11, b=44, c=12.
- Every (a) tool's history depth reads `absent`: each served object is one overwritten file with no dated key.
- Freshness is measured on 5 portal tools.
- 16 harvest rows, all `gap_owner: NFRA_OPLGTW`. Discover answers both harvest subjects; the Schwab control holds.

## For the round-10 analysis (carried in the rows, not messaged)

- **FWD-20 depth.** Depth is `absent` on 11 of 11 (a) tools. DONE WHEN asks for "earliest served date", and ACCEPT
  admits "absent is said". Whether absent-on-all REALIZES FWD-20 is the L9/L10 call. A measured depth needs a dated
  history (object versions or dated keys) that no served portal object has today.
- **Durable link key.** A link key that is not the row identity (Z-S106).
- **Suite.** The re-baseline, plus the six route/OIDC tests' owner (Z-S107).
- **Harvest widening.** The 13 prefixes added by list v4 (Z-S105).

## Compiler Tools

- A battery check written against an IMAGINED output shape (both depth and freshness measured on one prefix) passed its
  planted arms and still could not pass on the real output. The planted input copied the imagined shape. Plant from the
  producer's contract AND name what the producer may legally emit instead (here `absent`).
