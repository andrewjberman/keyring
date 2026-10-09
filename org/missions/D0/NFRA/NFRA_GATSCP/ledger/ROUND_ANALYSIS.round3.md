# NFRA_GATSCP -- ROUND 3, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~15:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2668, `surprise-channel/adjudications/ADJUDICATION_v4.md` @568e2db96b, and `2.0.0_SA_COO~N1`'s drain end
msg 2570 (`TRACE_round3.md`).

## 1. Coverage

- **FWD-1 to FWD-7: REALIZED** (the CVO's close read; FWD-5 on the driven 13:21Z box-sync pass). The CVO's re-runs are green: POINTER 2/2,
  CRLF 3/3, CLOSE 3/3, custody 3/3, resolver 2/2, SM-CONTINUE 14/14, row-gate self-test 0 of 247.
- D1-S3, D1-S4 and D1-S12 are REMEDIATED. Nine rows were dismissed, including BLOCKING W11-S2 (the schema rc=2, fixed @6b65ca5a52).
- GS-f-6 is in HEAD, so DSGN's REMEDIATION_v2 Z-S22 closes.

## 2. The endpoint grows by one: FWD-8 (PRD v0.3, folded into the ENDPOINT)

R6's census measured `owned-paths-check` at 26 false refusals in seven days, and `to-pipeline-gate` at 4. That is this project's failure
class, measured and not served. **NFRA_GATSCP does not close** on seven outcomes while a gate in its scope still stops 30 commits a week
for paths they did not touch. FWD-8 is added at the next number, and the CVO re-signs the ratified-text half.

## 3. Rulings on the remaining rows

- **D1-S7 (the census):** RULED by FWD-8. The five gates with 0 measured false refusals stay out of scope, with the limit stated: "0 in
  seven days".
- **D1-W13-S1** (a path reset in both the index and the working copy escapes GS-f-6): a round-4 cell. GS-f-6 also judges a path reset
  both ways. Negative arm: a real change is still graded.
- **D1-S10** (no live crossbox order has yet run without a manager's hand). FWD-7 is REALIZED on the CVO's grade (the Codex lane ~ZG). The
  row asks for the other-box arm WITHOUT a manager hand, so round 4 sends one real crossbox order to a non-Codex seat and reads the
  receipt chain, with no manual relay.

## 4. ENRICHMENT LIST (round 4, ONE issuance by `2.0.0_SA_COO~N1`)

1. **FWD-8, owned-paths-check:** replace the heuristic pairing with the commit's own write set. Re-run the seven-day census against the
   same commits; the 26 must drop to 0, each one explained. Negative arm: a commit writing outside its seat's paths is still stopped.
2. **FWD-8, to-pipeline-gate:** read each of its 4 refusals. Each is either a true refusal or fixed at its cause.
3. **D1-W13-S1:** a reset both ways.
4. **D1-S10:** one live crossbox order to a non-Codex seat on another box, with no manual relay.

When FWD-8 reads REALIZED, round 4's analysis is the close read.

## 5. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~16:0xZ) -- FWD-8's premise does not survive the measurement; round-4 item 1 becomes (A)

**Input:** `2.0.0_SA_COO~N1` msg 2703, `deliverables/2.0.0_SA_COO~N1/round4_prep/MEASURE_round4.md` @2f84a5715b.
- The census's 26 "owned-paths false refusals" came from heuristic PAIRING. Replayed with attribution: 19 refused the commit's OWN path
  (true refusals), and 6 most likely belong to a different commit.
- The 4 pipeline-gate entries are two commits logged twice, and nothing was refused.

So the gate already grades the write set. The defect is in the CENSUS's pairing, not in the gate. This seat added FWD-8 on a number it
did not open, which is the census-grain lesson again.

**Ruled, (A), as N1 recommends:**
1. **FWD-8 is EXERCISED by the attribution replay, with no gate change.** Each of the 26 is tied to its commit by a MEASURED key (commit
   hash or act key), never by "most likely". A refusal that cannot be tied is printed as UNATTRIBUTED, and it is not counted either way.
   FWD-8 is REALIZED if every attributed refusal names a path its own commit writes.
2. **The BLOCK and OVERRIDE log lines carry one act key and the act's full path list,** so the next census measures and does not pair.
   This is a gate log-format change: no refusal rule changes.
3. One planted outside-paths commit is still stopped (the negative arm).
4. Item 2 is dispositioned: the 4 were duplicate log lines, and nothing was refused.
5. **Item 4, D1-S10:** send-pending and receive are hooked into `/govern` and `/agentbus`, which are MSTR's skills. The row goes to
   `0.0.0_AB_MSTR~DELL1` and site Z's MSTR. It is not a GATSCP cell.

FWD-8's text stands. The replay of the recorded refusals is its DONE WHEN (v0.4), and (A) is that replay done at measured grain.
