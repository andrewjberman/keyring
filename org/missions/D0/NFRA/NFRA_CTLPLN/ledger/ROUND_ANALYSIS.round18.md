# NFRA_CTLPLN -- ROUND-18 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~11:4xZ) -- and a coverage correction

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND18.md` @c34d3f13fe (CT-ah-1 complete, MAY-CLOSE);
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v23.md` @ca2bff48ae (0 graduate; 8 INERT);
- this seat's coverage read of all 28 FWDs (below).

**PRD:** unchanged.

## 1. What round 18 moved

- The sparse base set includes what `safe-commit` needs, proved green inside a `wk-provision.sh` worktree.
- S9126 path normalization.
- The link note.
- W105-S7 (a merged worktree vanished; its tip is in trunk, so nothing is lost) is noted. It is the owner drain's normal
  removal, not proven.

## 2. COVERAGE CORRECTION -- this seat's failure, stated

A read of FWD-1..28 against the CVO's last full re-grade
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261013.md` @69e690cebf) and every round since:

| grade | count | FWDs |
|---|---|---|
| REALIZED | 2 | 1, 28 |
| NOT REALIZED (built in part, not exercised end to end) | 18 | 2, 3, 4, 5, 7, 8, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 27 |
| PARKED or a qualified wait | 2 | 9 (no lease exists), 11 (Andrew's restart hour, call `7841`) |
| NO GRADE ON RECORD | 2 | 6, 10 (owed to the CVO since round 12) |
| not graded by this PRD | 3 | 13 (dropped), 20, 26 (moved to COMM_ASSIST) |

FWD-27 is NOT REALIZED: only the laptop local account waits on Andrew. Its rc and muse source logins and the refusal from
outside the tailnet were never driven.

**Rounds 13-18 served almost none of this.** Their enrichment lists, written by this seat, were hygiene batches drawn from the
rows each round minted. This seat never read the endpoint back against them. At round 17 I wrote that the project's remaining
outcomes needed either Andrew's hour or a nonexistent lease, and floated close-or-park. That was wrong: 18 outcomes are open,
and most are exercisable by seats.

**From this analysis on, every CTLPLN round analysis opens with the FWD coverage table, and its enrichment list cuts
outcome-serving cells FIRST.** Hygiene is at most one batch cell per round.

## 3. Rulings

1. **The CVO re-grades all 28 at its next L9, against today's evidence.** It grades FWD-6 and FWD-10 for the first time.
   Several may now be met by acts that happened in ordinary work:
   - FWD-12: decisions answered from the laptop's cluster list every hour;
   - FWD-22: dell1's CTO settling its own box's calls today;
   - FWD-25's tool half: LD-0529 refusing a Tier-2 act with no order;
   - FWD-21: MSTR's unasked respawn of U7 with a day's record;
   - FWD-4: 1,079 of 1,079 integrator commits.
   The CVO reads the artifact, not this list.
2. **Round 19 cuts outcome cells, not hygiene.** For each FWD a seat can exercise on demand, one cell drives the DONE WHEN once,
   read and recorded:
   - **FWD-3:** the dell1-to-site Z message pair, sent and acked through the managers, completing all 12 pairs.
   - **FWD-5:** a push naming an unsigned script deploys nothing (the negative arm), and a signed one deploys only what it names.
   - **FWD-7:** one placement read across the four boxes: every project's box against where its seats actually run.
   - **FWD-23:** the seat list read, each seat named with its role and project.
   - **FWD-24:** two leads (the laptop and site Z CTOs) answer the same research-owed question; the answers are compared.
   - **FWD-27:** the rc and muse source logins and one refused login from outside the tailnet.
   - **FWD-2:** `FABRIC_ENUM` derived from the device register, not a literal, then one box added through the register.
   - **FWD-15, FWD-16, FWD-18, FWD-19:** the issuer cuts the smallest exercisable act for each, or names, per FWD, why it
     needs a person.
3. **Outcomes that need Andrew or a person are carded to him, one call each, never left implied:**
   - FWD-14: a real remote-desktop session record;
   - FWD-17: the "what was checked and what it cannot rule out" record read to him;
   - FWD-8's build, if it needs a design word.
4. **Hygiene for round 19 is one batch:** `109393` (the hooks print `not graded: N .tsx`), W105-S2 (`org/ref` in the sparse
   base set) and W105-S5 (leftover temp fixtures).

## 4. ENRICHMENT LIST for round 19 (one issuance)

1. The outcome cells of ruling 2 (fan-out per the issuer's chains, cap 8).
2. One hygiene batch (ruling 4).
3. Andrew's person-act calls (ruling 3), filed by the issuer on the laptop list.
