# 3.0.0_SA_CVO~DELL2 on dell2 -- session log, 2026-10-14 11:30Z to 12:55Z

**archetype:** VALIDATE

Event-driven; no cron (`org/ref/LIVE_ARMS.md` has no row for this seat). The watcher was armed at load and re-armed at each expiry.
At load: 4 inbox messages from 2026-10-08 were acked, all superseded (TCKT_VNEXT ratified-text half SIGNED at v0.4; IRPT_ANLREQ
registered 2026-10-09).

## Done, with commits (LOCAL on box/dell2; origin read before each slug)

| item | result | commit |
|---|---|---|
| NFRA_TRNSPT round 24 L8/L10 | No new rows. D2-S22 had been graduated ARMED in REMEDIATION_v10 and no remediation row ever disarmed it, so comp-surprise kept reading armed=1. Row D2-C-S1 (`disarms` D2-S22) lands the disarm; armed now 0. Own live read: 3 of 3 functions on xC1GDXXp. Battery re-run OK | 9738102262 |
| IRPT_DASHBD round 104 L8/L9/L10 | DB104-1-J1 FAIL: figures called 'needs more history' are printed elsewhere in the same report; an account note contradicts its table; slot names and an absent disclosure page print as client lines. Orientation met; AC1..5 PASS re-run; 9 dismissed | fe2d7b779b |
| IRPT_ANLREQ round 39 ZD L8/L9/L10 | AR309/310/311-y-AC2J PASS. Builds re-run; live digests unchanged at 12:13Z; host scripts' guard lines equal to release 28; 9 dismissed; W123-S1 ARMED held with AQ2 | 8347e4a1cc |
| IRPT_BCKEND round 192 ~P L8/L10 | 6 of 6 PASS re-run; release not ready (Inflection pin; Cottonwood one trading day behind T-1); the 10-09 fire died at ~310 s of 3600 s; 9 dismissed | b956283de1 |
| TCKT_VNEXT round 16 L10 (corrected packet) | CW2-OK on own live re-run; both check fixes sound. Card 1 completed by Andrew 2026-10-13T18:17Z, crawl identity in 0 of 3 events; asked the CTO whether TR-dp-24's precondition still holds | none (slug by message) |

## Compiler Tools

- `comp-surprise --project <CODE> [--armed|--json]`: worked. It pinned the NFRA_TRNSPT armed=1 to a REMEDIATION_v10 row that no later
  remediation row had disarmed. Gap: an adjudication dismissal never clears an ARMED read on a graduated row, and the CVO compiles before
  this one assumed it did.
- `.tools/round-close-check.py`: worked. Gap: untagged seat-folder orders are counted in every round, so "8 of 8" (NFRA_TRNSPT r24) is
  1 round order plus 7 older ones, and IRPT_ANLREQ r39 reads REFUSED on three older orders' proofs.
- `.tools/surprise-row-gate.py` (via safe-commit): refused `NFRA_TRNSPT-C-S21` with fabric dell2, because a dell2 row must carry the D2
  coordinate. Fixed by using the schema's `-D2-C-S<n>` form. Earlier dell2 CVO rows passed only by declaring `fabric: laptop`.
- The comp-rail denied four calls (census piped to a filter; recursive grep); each RUN NEXT line was correct.

## Open

- TR-dp-24 (NFRA_TRNSPT) against card 1's completed state: the CTO's.
- IRPT_ANLREQ channel: 212 open and 33 ARMED rows from earlier rounds, not re-graded this session.

## Addendum, 2026-10-14 12:55Z to 16:00Z

**archetype:** VALIDATE

| item | result | commit |
|---|---|---|
| UB-20261014T123908Z-151e (NFRA_OPSWKF) | SIGNED the CTO's fold: HOLD to ~2026-10-27 on Andrew's 10-13 word, existing drive-mode carrier | 74bfac0568 |
| NFRA_OPSWKF round 1 close L8/L10 | 7 dismissed (4 BLOCKING resolved on own reads 13:11Z: SES read, simulate and get-resource-policy held, trade_request tests 4 passed, FWD-10 graded); 5 graduate OPEN as the resume list; open 0, armed 0 | 66c31ff70b |
| IRPT_BCKEND round 193 ~P | release stopped at its own digest gate; 6 dismissed incl. ARMED W374-S1 on Andrew's record; new row D2-S172 (AC3 check diffs base..HEAD); the issuer's re-grade commit also removed both declared_exclusions | 9ed92c6795 |
| IRPT_DASHBD round 105 | DB105-2-J1 FAIL (p.7 household Net Gain 'needs more history' while p.4 prints it; allocation-chart reasons; the latter missed by this seat in round 104); 13 dismissed | c196c507a8 |
| IRPT_BCKEND round 194 ~P | packet v2 not signable as is (live producer matches no commit); re-grade verified 3 of 86 leaves; 3 dismissed | 24b7c00c79 |
| IRPT_DASHBD round 106 | DB106-2-J1 FAIL on two lines (p.5 pointer to an account page; p.6 household-allocation clause); 6 dismissed | 61b56ab8a9 |
| IRPT_ANLREQ PRD v0.6 | ratified-text REFUSED: CONTRACTS C-FIRM still bound the old partner-advisor filer | 57cea3c90c, stamp e17a2daaf9 |
| IRPT_ANLREQ PRD v0.7 | SIGNED on the one-row fix | ab69bc85c4, stamp 4490e36e3e |
| IRPT_DASHBD round 107 | DB107-1-J1 PASS (pages 2, 4, 5, 6 read); 3 dismissed | 879e7badcb |
| IRPT_ANLREQ PRD v0.9 | SIGNED (one YCharts data call per request, prices only); PRD ADMITTED; YCharts-before-yfinance ordering put to Andrew's list | a2a34a5659, stamp adffe99ed7 |

Compiler tools: `comp-surprise` (armed reads before and after each compile), `round-close-check` (two instrument conflicts named: untagged orders; the judgment-row proof conflict W156-S8), JSON leaf diffs of issuer re-grade commits (caught an unstated deletion at 7dae6e5467; confirmed a clean one at 7b46d4a24d). One ack sent to a wrong message id (7720, a no-op); 7719 acked after.

## Addendum, 2026-10-14 16:00Z to 21:45Z

**archetype:** VALIDATE

| item | result | commit |
|---|---|---|
| IRPT_ANLREQ PRD v0.10 | ratified-text REFUSED: C-PACKAGER still said the branded PDF is a later enrichment | 2af2238cdb, stamp d86b7fee43 |
| IRPT_ANLREQ PRD v0.11 | SIGNED on the C-PACKAGER fix; PRD ADMITTED | 5d3cf206aa, stamp 473bba9b5f |
| IRPT_DASHBD round 108 | no judgment; 2 of 2 PASS; Orion client-grain fork to the CTO; 6 dismissed | 963438b352 |
| IRPT_BCKEND round 195 ~P | confirmed the pin's bundle closure lacked opal_unidentified.py (Cottonwood mint would crash); 4 dismissed | 0ebbceaca0 |
| Andrew's 17:3xZ priorities relay | flagged the NFRA_OPSWKF HOLD against the Oct 24 Ticket Center date; the CTO ruled OPSWKF stays on HOLD, trade scope to TCKT_VNEXT | none (message) |
| IRPT_DASHBD round 109 | DB109-2-J1 FAIL on the first Inflection render (4 counts: household since-inception benchmark under the account window; gain/loss ending value; false 'needs more history'; two reasons) | d6fee3fc43 |
| TCKT_VNEXT PRD v0.5 | ratified-text REFUSED: no CONTRACTS rows for the two new types or the staff firm choice | 6d7a6309e8, stamp 060c5ab228 |
| TCKT_VNEXT PRD v0.6 | SIGNED on four CONTRACTS rows; PRD ADMITTED | a75b63ea56, stamp b281a87ffc |
| IRPT_DASHBD round 110 | DB110-3-J1 FAIL on the account labels only; all round-109 counts fixed; since-inception benchmarks recomputed from the served series and equal; 22 dismissed | 28b72ca20d |
| IRPT_BCKEND round 196 ~P | new pin b1d354cfc9 verified (+opal_unidentified.py, 2 lines); 232 of 236 attributed; 4-node STOP held; 13 dismissed | a25a244747 |

Compiler tools: `prd-signoff.py` (sign/refuse/status), `comp-surprise` armed and open reads, `round-close-check`, the project's own `model_series_windows` reader for an independent recompute, `git merge-base`/`diff --stat` on pins. Two process slips: surfaced_at stamps ran ahead of the real clock (10 min at 17:15Z, corrected before commit; 8 min at 21:20Z, committed, since the channel is append-only); safe-commit refused twice during other seats' merges, waited out.
