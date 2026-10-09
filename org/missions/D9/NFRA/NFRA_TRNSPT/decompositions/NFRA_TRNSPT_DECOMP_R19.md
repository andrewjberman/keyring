# NFRA_TRNSPT decomposition -- ROUND 19 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msgs 2938 and 2946, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 8 @c592051597 and 8.1 @3cbbddbe24
(enrichment list, six items; W1-S8 first, as ARMED).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-s-19` | (1) W1-S8: `read_meeting.py` and `research_read.py` call ONE shared holdout filter; a held-out row is never printed | FWD-5, FWD-8 | dell2 worker | LOCAL | worker-light | -- |
| `TR-w-19` | (2) W1-S7: a Teams-silver re-wipe tool (dry-run names every key) + (2b) wipe-on-landing in `parse_silver.py`, planted-token test; the served re-wipe follows under a pair | FWD-5, C-TIERS | dell2 worker | LOCAL | worker | -- |
| `TR-r-19` | (3) FWD-2: the Research Graph 403 read by name for the permission it lacks | FWD-2 | ISSUER (read-only) | SERVED | -- | -- |
| `TR-e-19` | (4) FWD-4: a listing snapshot stored per pull, so the "expired" cause is reachable on demand | FWD-4 | dell2 worker | LOCAL | worker | -- |
| `TR-i-19` | (5) FWD-6: market-update intake, one file kept byte-exact, a re-saved copy recognised | FWD-6 | dell2 worker | LOCAL | worker | -- |
| `TR-q-19` | (6) FWD-9: one read-only question across meetings, mail updates and commentary, by a named reader | FWD-9 | dell2 worker | LOCAL | worker | -- |

**Chains.** Five independent worker chains, one per build cell (slots ~1..~5); TR-r-19 is the issuer's read. Fan-out 5 of 5, cap 8.
FWD-5's reader role follows TR-w-19's served re-wipe AND wipe-on-landing (ADDENDUM 8.1: no reader on teams/transcripts/* until both ship).

**Issuer rulings.** (1) Every build cell is LOCAL: fakes and synthetic fixtures only, no AWS, no content. (2) W1-S8 stays ARMED until TR-s-19 is
merged: `read_meeting.py` is NOT run against Research silver by any seat or worker. (3) Any new S3 address is `lib/opal_naming.py address()` output;
a builder refusal is a row, never a typed key.

## Rule 24 record

Domain: ADDENDUM 8's six enrichment items. 1 = TR-s-19; 2 (+ 8.1's 2b) = TR-w-19; 3 = TR-r-19; 4 = TR-e-19; 5 = TR-i-19; 6 = TR-q-19. Remainder:
FWD-5's reader role (sequenced after item 2 by the CTO), FWD-1/3 (ride the Teams pull, TO-APPLY-p18), FWD-8 (TO-APPLY-a18 at the laptop).

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py` at base box/dell2 6ab360052a: s8, w7, e4, i6, q9 all FAIL
(absent).
