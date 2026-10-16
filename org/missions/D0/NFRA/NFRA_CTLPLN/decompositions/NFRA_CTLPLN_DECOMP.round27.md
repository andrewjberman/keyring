# NFRA_CTLPLN decomposition -- round 27: FWD-18 on site Z, FWD-19's lane-wait clause, FWD-11's drill, and the measured short act of every ADVANCED FWD (issuer 2.0.0_SA_COO~C; cut 2026-10-16)

**Status: ISSUED in one issuance. FROZEN at the cut.** (A cell cut later in the round, once its dependency clears, is an AMENDMENT of this document stating its gate limb, as in rounds 22, 24, 25 and 26.)

**Input.** `ledger/ROUND_ANALYSIS.round26.md` (1.0.0_SA_CTO) @82ec4bb123 sections 2-3 and msg 109600; the CVO's `ADJUDICATION_v30.md` @80d253d41f; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND26.md` @1d136f5200. **PRD:** v0.31. **Coverage entering the round (CTO table):** REALIZED 1, 3, 5, 15, 16, 17, 24, 28 (8); ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14, 18, 19, 21, 22, 23, 25, 27 (16); PARKED 9; MOVED 13, 20, 26; denominator 28. **Cadence:** `/canonical-drive` 30m.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-aq-1` | **FWD-18, site Z, laptop half.** Send the already-released, already-checked `tabulate` pack (4 files, `$HOME/tdrop/out/intake-20261016-tabulate`) to site Z by Taildrop, once each, record it, and extend the journey test with `--taildrop-sitez`. No new fetch, no re-release. | FWD-18 | SERVED (one file set sent to one box; as `CT-ao-2`) | `0.9.0_WK_NFRA_CTLPLN~129` |

## Driven by the issuer in this round (not cells)

1. **FWD-18, site Z, receiving half.** After `CT-aq-1`'s Taildrop: one crossbox call to `1.0.0_SA_CTO~Z`: collect the files, run `intake_receive.py` `verify`, `prove` and `install --target <a scratch folder that is not its own TARGET>`, commit the receipts with their pip logs on `box/sitez`, then (as dell1 did) run one read of the installed package from that scratch target only. The scratch delete is Andrew's word (recursive delete). The issuer reads the committed files from `origin/box/sitez`.
2. **FWD-19, the lane-wait clause.** One laptop lane (this seat) is deliberately put in a waiting state on a package: it files an intake request for a package absent from `requirements.txt` for one stated piece of work and does NOT decide it; it records the wait in the one decision list (`open-calls.py add`, kind `act`, naming the lane, the package and the piece of work); the issuer then reads the three places that must agree: the intake status verb (REQUESTED), the decision list (`open-calls.py list` shows the call) and the lane's own broker summary (WAITING), while the lane keeps working elsewhere (its commits during the wait). The CTO's decision closes the wait either way: APPROVED (the piece proceeds through the route) or REFUSED (the lane loses that one piece of work, as the clause says).
3. **FWD-11, the drill.** A crossbox call to one box's CTO to name (a) a lane whose round is in flight, (b) the time at which the process carrying that round is restarted, and (c) the record the round's state is read from before and after (the published branch and the ledger, per C-RESTART). After the restart the round is shown to finish without work redone or lost, from committed files. Not Andrew's word: if the box's CTO reads his hold of 2026-10-14 ~20:49Z ("Dell1 Restart is being held til later ...") as still binding for any seat restart on that box, the answer says so and the issuer takes it to `0.0.0_AB_MSTR` for Andrew; the issuer does not read the hold wider or narrower. The organic case (an unplanned restart) is the negative arm. A whole-box reboot is not asked.
4. **The measured short act of the 12 other ADVANCED FWDs** (2, 4, 6, 7, 8, 10, 12, 21, 22, 23, 25, 27): the issuer reads each PRD DONE WHEN and states the one act short and whether a seat or Andrew holds it (round-26 ruling 3). A packet section, not a cell.

## FWD-14 (no cell)

Waits on Andrew's sitting (`c9a4`, `b87f`; the Security-log read joins `b87f`). FWD-9 PARKED. The dell1 scratch delete is the CTO's to put to Andrew (round-26 ruling 1).

## Carried with an OWNER and the CONDITION that un-parks each

As in the round-24, 25 and 26 decompositions: `W8-S7`, `S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3` (before 2027-12-01), `S9125` (dell1, before 2026-12-31), `S9119`, `S9128`, `W121-S3`/`S4`.

## Rule 24

**Domain:** the CTO's round-26 section 3 enrichment list (5 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** `CT-aq-1` writes the sitez record and the journey test only; the three issuer-driven items write deliverables and crossbox files. **State coherence:** nothing in this round deploys, pushes or calls AWS; the one network act is a Taildrop to a box already on the tailnet.

## Dependency chains and fan-out

Five chains: (1) FWD-18: `CT-aq-1`, then the site Z call; (2) FWD-19: the issuer's own request, decision-list entry and three reads, then the CTO's decision; (3) FWD-11: the box CTO names the lane and time, then the restart and the read-back; (4) the measured read of the 12 FWDs; (5) FWD-14 (Andrew's sitting). `fanout: 1 of 5 chains, cap 8, reason: chain 1 is the only chain with a worker cell and no unmet dependency; chains 2-4 are the issuer's own acts or wait on a box CTO's naming, chain 5 on Andrew's sitting`
