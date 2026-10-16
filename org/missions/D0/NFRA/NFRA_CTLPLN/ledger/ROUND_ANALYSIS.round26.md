# NFRA_CTLPLN -- ROUND-26 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~04:5xZ)

**On:**
- the issuer's L8 packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND26.md` @1d136f5200;
- the CVO's L10 slug `ADJUDICATION_v30.md` @80d253d41f (msg 109599).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage

| grade | count | FWDs |
|---|---|---|
| REALIZED | 8 | 1, 3, 5, 15, 16, 17, 24, 28 |
| ADVANCED | 16 | 2, 4, 6, 7, 8, 10, 11, 12, 14, 18, 19, 21, 22, 23, 25, 27 |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

**FWD-15 REALIZED (C-S86).** dell1's lane imported tabulate only from the scratch target and printed the table (`e5f033b15c`).
This seat read the committed output:
- `tabulate.__file__` is under `SCRATCH_TARGET`, version 0.9.0;
- both receipts show `received_sha256` `024ca478df22`.

The CVO reproduced the table byte for byte. The package journey, FWD-15 to FWD-17, is closed.

## 2. Rulings

1. **dell1's scratch delete is put to Andrew now.** No grade depends on the folders any longer (v30). REC: delete `SCRATCH2` and
   `SCRATCH_TARGET`. A recursive delete is his confirmation (CLAUDE.md Agent Autonomy); if he declines, the leftover is
   recorded as harmless.
2. **My round-23 enrichment list was wrong.** It said "every other open FWD is a person's act, a qualified wait or PARKED", but
   the CVO's C-S80 (v28) names three FWDs that each stop one SEAT-reachable act short:
   - **FWD-18:** stopped and installed on dell1; the install on site Z has not been run.
   - **FWD-19:** the DONE WHEN is exercised; the clause about a lane waiting in the decision list is unread.
   - **FWD-11:** dell1 restarted with its one candidate uninterrupted, but no round has been shown in flight across a
     restart and then finished.
3. **The rest of the ADVANCED list is to be MEASURED, not asserted.** The issuer reads the PRD's DONE WHEN for each of the 12
   ADVANCED FWDs not named here (2, 4, 6, 7, 8, 10, 12, 21, 22, 23, 25, 27). It states for each the one act that is short, and
   whether a seat or Andrew holds it. That read is a packet section, not a cell.

## 3. ENRICHMENT LIST for round 27 (one issuance)

1. **FWD-18:** run the install on site Z, as on dell1. It is a cross-box act through `0.0.0_AB_MSTR`.
2. **FWD-19:** read the lane-wait clause against the decision list, with one lane deliberately put in a waiting state.
3. **FWD-11:** a deliberate drill. With a round in flight on one box (dell1 or whichever box the issuer chooses), the process
   carrying it is restarted at a time that box's CTO names, and the round is then shown to finish.
   - The organic case (an unplanned restart) is the negative arm.
   - A whole-box reboot is not required unless the PRD's text demands it. If it does, that box's MSTR does it on its CTO's word.
4. The packet section of ruling 3.
5. FWD-14: Andrew's sitting (`c9a4`, `b87f`).
