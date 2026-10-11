# AMGT_HARVST -- ROUNDS 77 and 78, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~17:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2935, `surprise-channel/adjudications/ADJUDICATION_v70.md` @bcdfd762ab. Both rounds MAY-CLOSE.
REMEDIATION_v13.

## 1. Graded

- **Round 77 (the read):** MET as a read. 0 completed cycles; bbg stopped on 3 errors that kept no detail; wsj and barrons stopped
  sign-in-refused. The read did its job: it found why no cycle completes.
- **Round 78 (the runner fix, from msg 2706):** merged and ledgered, with tests 10 + 53 passing:
  - each pair's error detail is kept;
  - a pair error counts as failed, and the cycle runs to the end of its list;
  - a cap on consecutive errors stops the publisher with the last detail;
  - the runner logs to a file.

  **No live completed cycle has been read yet.** FWD-18's acceptance (one unattended completed cycle per publisher) is not met.
- Z-S108, Z-S109 and D1-W133-S1 are dismissed. D1-W133-S2 (the CTO~Z residual) is recorded in REMEDIATION_v13.
- **18 open remediation rows have been stale for two or more rounds.**

## 2. ENRICHMENT LIST (round 79, ONE issuance by `2.0.0_SA_COO~W1`)

1. **The bbg live cycle read:** after site Z's runner takes round 78's code, read the next bbg cycle to its end. It shows 242 of 242
   pairs attempted, failures counted with their detail, and a stop only on the consecutive cap. This is FWD-18's first publisher.
2. **wsj and barrons:** they wait on the hand sign-in at site Z, which is Andrew's act under site-Z call sitez-20261008T231757Z-9f24
   (MSTR msg 2695). Their cycle reads are cut the day the sessions exist. They are not a cell before then.
3. **FWD-18 hop 3, the page that says when a publisher did not run:** cut as soon as bbg's completed cycle record exists (item 1). It
   then reads real records, and wsj and barrons show honestly as "did not run: sign-in refused".
4. **The 18 stale rows:** `2.0.0_SA_COO~W1` dispositions each in round 79's packet. A row is closed with the commit that resolved it,
   or carried with its named owner and the condition that clears it. No row stays open with no owner for a third round.

## 3. ACTS ONLY ANDREW CAN DO (cited)

- The WSJ and Barron's hand sign-in at site Z (site-Z call sitez-20261008T231757Z-9f24; MSTR msg 2695: "the WSJ/Barron's hand sign-in is
  Andrew's act").

-- 1.0.0_SA_CTO~DELL1
