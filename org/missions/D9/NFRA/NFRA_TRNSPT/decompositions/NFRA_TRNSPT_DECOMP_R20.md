# NFRA_TRNSPT decomposition -- ROUND 20 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 3012, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 10 @200cbac519: "(1) the W1-S7 re-wipe under a pair:
every key with its prior version, the planted-token test on the rewritten bytes; (2) FWD-4, FWD-6 and FWD-9 exercised once each, read recorded, so I
can grade; (3) the transport cell once NFRA_OPLGTW answers."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-w-20` | (1) the re-wipe of the 30 existing Teams silver keys (3 series; research_meeting excluded, already wiped) under a pair; the issuer's read-back re-wipe sweep | FWD-5, C-TIERS | ISSUER (served; `0.7.0_AE_CloudOps~DELL2` runs) | SERVED | -- | the CTO half |
| `TR-x-20` | (2) live read-only wiring so FWD-4 and FWD-9 can be exercised on real stored bytes: S3 readers for `query/securities_across.py` (counts only) and a `completeness` CLI that asks about ONE meeting and prints its cause | FWD-4, FWD-9 | dell2 worker | LOCAL | worker | -- |
| `TR-f-20` | (2) the exercises: FWD-4 asked about one missing meeting, FWD-9's question run once for 2026Q3, each read recorded (counts and causes only) | FWD-4, FWD-9 | ISSUER (read-only, a named reader) | SERVED | -- | TR-x-20 |
| `TR-d-20` | (2) FWD-6: one real market-update deck placed with `updates/intake.py --apply` and read back byte-exact | FWD-6 | ISSUER (served) | SERVED | -- | a deck file, which no seat can fetch (the gateway returns a hint, not bytes, for an Office file; R18 coverage FWD-6) -- queued for Andrew |
| `TR-t-20` | (3) the Teams gateway transport (CTO ADDENDUM 9) | FWD-1, FWD-2, FWD-3 | dell2 worker | LOCAL | -- | NFRA_OPLGTW's bearer name + route contract (asked via MSTR 09:20Z); NOT cut this issuance |

**Chains.** A = TR-x-20 -> TR-f-20 (worker slot ~1, then the issuer). TR-w-20 and TR-d-20 are the issuer's served acts. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.** (1) The re-wipe's blast radius is the 30 keys of the three Teams meeting series; `research_meeting` is excluded because its silver was
written wiped by `research_fold.py` and carries the graded Apple state. (2) Exercises print counts and causes only, never transcript, email or client
text. (3) TR-t-20 is named here and cut by amendment the tick the owner's contract arrives.

## Rule 24 record

Domain: ADDENDUM 10's three items. (1) = TR-w-20; (2) = TR-x-20 + TR-f-20 (FWD-4, FWD-9) and TR-d-20 (FWD-6); (3) = TR-t-20. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R20_CHECKS/r20_checks.py` at base: x20 FAIL (absent).
