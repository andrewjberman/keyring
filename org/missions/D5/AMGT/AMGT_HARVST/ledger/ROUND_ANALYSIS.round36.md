# AMGT_HARVST -- ROUND 36 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~06:5xZ

**Input:** CVO~Z slug msg 28258, `surprise-channel/adjudications/ADJUDICATION_v47.md` @1c42dfcd6e (L10 precondition MET:
6 of 6 terminal, 5 complete, ai-2 cancelled on ruling 28235). Drain-end packet `round36/ROUND36_DRAIN_END_PACKET.md`
@a21c2553e9. **Round 36 is CLOSED.**

## 1. WHAT THE ROUND DELIVERED

- **Gold #4 is served before 13:00Z** (ruling 28084 met). Article mentions: 14,375 rows (sa 10,802, bbg 2,298, wsj 785, ft 449,
  barrons 41). Chatter daily: 58,300 rows. Both were read from S3 by CVO~Z and equal the packet.
- **The bbg outbox is drained:** 829 of 830 rows in silver.
  - ai-5 replaced one silver append per row with one per source, plus local isolation of bad rows (@6a0a2ebc79). It cleared
    244 due rows in about 2 min.
  - Z-S57, Z-S58, Z-W91-S19 and Z-C-S57 are disarmed and re-read.
- **FWD-11 limb 2a is graded on ruling 28245:**
  - bbg is MET: 9 non-void, 9 passed, on CVO~Z's true-band re-derivation.
  - wsj, ft and sa are MET-BY-ABSENCE over monitored traffic.
  - barrons is NOT_EVALUATED, because none of its requests fall in a monitor window.
- **FWD-11 is NOT REALIZED.** Three limbs hold it: ft limb (1), sign-in longevity; barrons limb 2a; and limb 2b on wsj, barrons,
  ft and sa, where no challenge has been sampled.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **The grader anchors each band on the challenge's presentation as the run records it.** bbg emits `challenge_presented` from its path; until it does, the grader anchors on the HTTP 403 that precedes each pass. `requests` is counted inside the monitor windows only. | v47 s.2(a), s.5: right on bbg by approximation, wrong on barrons by construction |
| 2 | **The load monitor runs again now and stays up for the life of FWD-11.** It was stop-filed at the 04:0xZ wind-down. Every challenge since 04:03Z is unmonitored and VOID. | v47 s.5 |
| 3 | **barrons is exercised under the monitor.** One scheduled barrons collection runs inside a monitor window. | barrons 2a NOT_EVALUATED |
| 4 | **Limb 2b stays open until a publisher presents a challenge in normal collection.** No cell provokes a challenge on purpose. | 2b is "a real challenge, really solved"; manufacturing one is not this round's to design |
| 5 | **ft limb (1):** the enrichment item from ruling 28235. One 2h run from a sign-in Andrew solves by hand while present, proving the keep-alive fires once per page load. It waits on his presence, and no solver vendor is used. | ai-2 cancelled |
| 6 | **Packet item 5.3, the one stranded bbg article** (`TD7VMGKGCTIZ00`, SilverRowError, 1 of 830): the issuer records the error text on the row. A cell repairs it only if the cause would recur on new rows. | 0.12%, now isolated by ai-5 |
| 7 | **Z-W90-S11 (a sparse cone that cannot run the collector suite):** the issuer fixes its own worktree recipe as an issuer amendment (rule 27). No cell. | graduated v47 |

## 3. THE ENRICHMENT LIST -- round 37, `2.0.0_SA_COO~H`, ONE issuance

| # | cell | criteria shape (at most three, mechanical) |
|---|---|---|
| 1 | grader: presentation anchor + windowed requests (ruling 1) | re-grading round 36's windows reproduces bbg 9 non-void, 9 passed; barrons reads NOT_EVALUATED (0 windowed requests), not MET-BY-ABSENCE; a planted presentation 3 min before its pass, with input inside the band, reads VOID |
| 2 | the load monitor back up (ruling 2) | its window file opens at the restart, and its log grows across two reads 10 min apart |
| 3 | a monitored barrons run (ruling 3) | at least 1 barrons request inside a monitor window; the grader's barrons verdict is MET or MET-BY-ABSENCE on monitored traffic |
| 4 | the ft keep-alive run (ruling 5), waiting on Andrew's hand-solved sign-in | the run record carries one keep-alive event per page load over 120 min, and the session holds |

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **The hand-solved ft sign-in for cell 4** (his own hand on the hCaptcha. A solver is a vendor use no word of his names, and
   ruling 28235 does not spend the 04:57Z egress word on one).

**HARVST is never HELD-AT-STOP** (Andrew: "we do not accept any defeat").

## ADDENDUM 2026-10-02 ~07:3xZ -- ruling 8, on CVO~Z msg 28274 (ADJUDICATION_v48 @ac88fdaf80, row Z-C-S60)

A clean, unassisted bbg press-and-hold FAILED at 06:59:52Z inside the restarted monitor window, which held 0 hardware events
(run `20261002T065754Z-bbg-4f3bfa12bd`). The window grade now reads bbg 10 non-void, 9 passed. Section 1's "bbg MET" held on
round 36's windows only. No DOM capture exists, so the cause (solver, server refusal or rate) is unread.

| # | ruling | why |
|---|---|---|
| 8a | **Limb 2a is graded PER RUN**, as the PRD's DONE WHEN reads it ("one unattended run ... meets each publisher's live challenge and passes it"). A publisher's 2a is MET by a run inside a monitor window in which every challenge presented is non-void and is passed by the collector. A bounded in-run retry counts, and each attempt is recorded as its own challenge. A failed run elsewhere in the window does not void a passing run. It is a robustness finding, and the grader prints every publisher's window pass rate (non-void passed / non-void presented) beside the verdict. | 28245 graded the window, and one failure would then fail the limb forever. The PRD's grain is the run. |
| 8b | **Round 37 gains a cell: failure capture plus one bounded retry on the bbg path.** On a challenge failure the collector writes a capture bundle (DOM snapshot, screenshot, the HTTP status and response headers of the challenge exchange) before it gives up. It then makes one retry after a 60-120 s backoff, recorded as a second challenge event. | The 06:59:52Z failure cannot be classified without a capture. A retry is the robustness half of "robust auth". |
| 8c | **Run `20261002T065754Z-bbg-4f3bfa12bd` stays UNCLASSIFIED** until a capture exists. It is not graded as solver failure, refusal or rate. | No artifact holds its cause. |

Round-37 cell 5 (`2.0.0_SA_COO~H`, the same ONE issuance, or an issuer amendment if round 37 is already cut). Criteria:
- a planted challenge failure writes a capture bundle with all three parts;
- the retry writes a second challenge event 60-120 s later;
- the grader prints per-run verdicts and the window pass rate for each publisher.

**Ruling 8d (07:3xZ, on CVO~Z msg RE 28279, PRD :244-251): the run's grain.**
- **FWD-11's acceptance grain is ONE composite run under ONE run record.** It covers all five publishers, each meeting its live
  challenge with no human hand, plus a session made deliberately stale and renewed without Andrew, in the same run. The record
  names each publisher's challenge, path and session source, as :244-251 reads.
- **The per-publisher job runs (`runs/<stamp>-<pub>-*.json`) are limb evidence:** they grade each publisher's readiness (2a per
  run, pass rate beside it). They are never the acceptance.
- The composite run is a cell of its own, cut once every publisher's limbs pass on job runs. Its orchestration writes the one
  record.
- CVO~Z grades round 37 on the job-run grain as limb evidence. FWD-11 stays NOT REALIZED until the composite run.
