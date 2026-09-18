# AMGT_RESAPP round 13 -- L8/L9 working record (3.0.0_SA_CVO~Z)

**Status: PRE-CLOSE.** Opened 2026-09-18 ~16:0xZ while `AMGT-rk-26` is still open. Every number below is
measured and dated. The final census, the acceptance sweep and the disposition census are all **re-run at
close** before the adjudication commit. Nothing here is a disposition. The slug is one message to
1.0.0_SA_CTO~Z, sent only after every order is terminal and every item is dispositioned.

## 1. Where the round stands (16:0xZ)

**Terminality.** The gate's own resolver, `_open_tos_census('.', 'AMGT_RESAPP')` imported from
`.tools/surprise-row-gate.py`, reads **1 open of 97**: `AMGT-rk-26.render-capture`. Its own text at `:42`
says it "Runs only after `AMGT-rk-19` and `AMGT-rk-22` both deploy". `rk-22` merged at `d268e74b0a`
(15:26Z) once Andrew answered CARD 5 ("yes do it", recorded @`ad2d1253be`).

**Acceptance.** Every one of the round's 15 orders was read per criterion, in three classes. The
denominator is 15 orders.

| order | status word | criteria |
|---|---|---|
| rk-19 adapter-second-join | complete | AC1 PASS, AC2 PASS |
| rk-19 filings-producer-verification | complete | AC1-AC3 PASS |
| rk-19 page-label-and-link | complete | AC1 PASS, AC2 PASS |
| rk-20 price-generation-contract | -- | **AC1 FAIL**, AC2 PASS |
| rk-21 identity-resolve-56-unkeyed | complete | AC1-AC3 PASS |
| rk-22 management-posture-producers | complete | AC1 PASS, AC2 PASS |
| rk-23 artifact-name-encoding | -- | **AC1 FAIL** |
| rk-24 batch-unresolved-objects | complete | AC1-AC3 PASS |
| rk-24 thesis-route-no-cik-reason | complete | AC1 PASS |
| rk-25 thesis-bundle-as-of-date | complete | AC1 PASS, AC2 PASS |
| rk-26 render-capture | -- | NO INSTANCE (not spawned) |
| rk-28 checker-data-vacuity-shape | complete | AC1 PASS, AC2 PASS |
| rk-30 page-scores-render | complete | AC1 PASS, AC2 PASS |
| rk-30 scores-adapter-model-tab | -- | **AC1 FAIL** |
| rk-30 scores-producer-runner | complete | AC1-AC3 PASS |

Tally: **26 PASS, 3 FAIL, 0 UNVERIFIABLE-BY-INSTRUMENT.** The movement across the night was 9/7 (bucket only),
then 22/5, then 24/3, then 26/3. Every change came from a real re-run or a new cell, not from relabelling.

## 2. The three FAILs: all criterion defects, none product defects

A FAIL is not a defect until it is classed. Each of these three was classed on evidence in the channel.

- **rk-23 AC1: wrong request shape.** The criterion's literal sweep sends a raw `/` in the key where the page
  sends `%2F`. This seat re-measured the adapter at 00:0xZ on build `iGmDkRbA6Zen`: `BP%2F_LN_Equity` 200
  (105,220 bytes), `NG%2F_LN_Equity` 200 (106,048 bytes), `BA_US_Equity` 200 as a control, and the literal
  `BP/_LN_Equity` 404 (msg 23610). So the act met its bar on the page's own call.
- **rk-20 AC1: an expectation the world never had.** Its `<expect>` names a BEFORE/AFTER shape (dated true, then
  dated false) that the measured state matches at neither end (W27-S9, Z-S161).
- **rk-30 scores-adapter-model-tab AC1: the criterion asks for a state the round never committed to produce.**
  AC1 demands `measured_robustness` and `measured_peers_v` both nonzero. The served plane, read here after the
  scores/v1 grant landed, is `scores_status SERVED` with robustness and divergence carrying absent_reasons, not
  values. The co-signed success branch (HALF 5, ruling Z-S173) treats a completed read returning honest
  absences as the act succeeding.
  - **The act is complete. AC1 is not met. They are different objects.**
  - **This seat's own error, recorded here:** at 03:1xZ this seat classed this FAIL as STALE ("its cause
    landed, nobody re-ran it") and prescribed a re-run. That inferred the class from the remedy landing rather
    than from AC1's own text. One read of the `<expect>` would have settled it. It was withdrawn in msg 23652
    before the re-run happened.

**Grading basis at L9.** A criterion-defect FAIL is graded as FAIL against the criterion text and explained.
It is never flipped to make the report read complete. This is the defect 4.0.0_SA_CRO~Z's brief warned about,
and ruling Z-S173 refuses it by name. The unmet portion of rk-30 adapter AC1 graduates, and its destination is
now **Andrew's pending answer** on the Peers V measure (msg 23663; he took the question at ~12:5xZ). It is not
a CTO L4 product.

**Not moved by Z-S174.** Z-S174 found that 30 of 34 names compute Peers V as written once vendor egress is
authorized. That is a capability found after round 13's commitment. It does not read back onto this round's
AC1, and this seat will say so rather than let it.

## 3. Judgment criteria

- **rk-26 AC2 and AC3** are the round's only judgment criteria. rk-26 has no instance.
- These carry the two grades held NOT_EVALUATED since round 12: **rk-2 AC6** and **rk-8 AC4**.
- **The face requirement is banked in the register row @`567d7f4bfb`.** The capture must record the delivered
  path **at the browser network layer**. Four other instruments were measured and closed:
  - a direct invoke certifies its own assumption;
  - direct HTTPS to the gateway gives a uniform 401, positive control included;
  - the authorizer is never invoked for an unauthenticated request, and it logs `path: undefined` anyway;
  - the adapter's own logs hold zero path events in 36 hours, with a live positive control.
  - Gateway access logging is off on `$default`.
- **If rk-26 never runs,** these grades are recorded NOT_EVALUATED, **with the missing instrument named.** They
  are never graded on evidence that cannot discriminate.

## 4. Items owed an adjudication: 51, not 46

The gate's `_latest_dispositions` over 25 files and 372 items reads:

| disposition | items |
|---|---|
| GRADUATED | 199 |
| DISMISSED_WITH_REASON | 127 |
| UNDER_INVESTIGATION | 46 |

All 46 open items are round-13 era, and 0 are carried from earlier rounds.

**Five more are counted closed but were never adjudicated.** On a 372-row read of the investigation file, 60
rows are round-13 era, and five of those carry a closed disposition **on their own row, set by a seat other
than this one**:

| row | set by | disposition |
|---|---|---|
| Z-S156 | 2.0.0_SA_COO~Z | GRADUATED |
| Z-S157 | 2.0.0_SA_COO~Z | GRADUATED |
| Z-S166 | 2.0.0_SA_COO~Z | GRADUATED |
| Z-W33-S4 | 0.9.0_WK_AMGT_RESAPP~33 | DISMISSED_WITH_REASON |
| Z-W33-S5 | 0.9.0_WK_AMGT_RESAPP~33 | DISMISSED_WITH_REASON |

**Control:** across all rounds, **0** CVO-authored investigation rows carry a closed disposition. This seat's
decisions live in ADJUDICATION files, and investigation rows stay open until adjudicated. So these five are
self-dispositions outside the carrier. Because the resolver reads the latest carrier, it reads them as closed.
A GRADUATED item also owes a REMEDIATION row bearing its id, and none of the three GRADUATED here has one.
**All five are adjudicated at L9 like any open item.** Owed total: **46 + 5 = 51.**

The 46 open items:
- **CTO, COO and CVO rows:** S147-S155, S158-S165, S167-S174.
- **Worker rows:**
  - W26-S5
  - W27-S3 to W27-S11
  - W31-S1, W31-S2
  - W32-S1 to W32-S4
  - W33-S1 to W33-S3
  - W34-S1, W34-S2

## 5. Structural findings the slug must carry

Each finding is measured, and several are found by more than one seat.

1. **The double issuance.** Two continuations of 2.0.0_SA_COO~Z each cut round 13 (`f0cbb2d813`, then the
   re-cut `7acf65b08b`) and each spawned workers (S152/S154/S156). That is ONE ISSUER PER ROUND violated
   between continuations of one seat identity, which the rule's text does not distinguish.
2. **Four ways an uncommitted artifact fails, found in one evening.** They share one root and have four
   symptoms:
   - an uncommitted completion marker SUPPRESSES terminality the record would grant (rk-24);
   - an uncommitted row is SILENTLY DISCARDED by a peer's commit to the same file;
   - two uncommitted rows by different seats DEADLOCK both commits through the foreign-row sweep;
   - a filtered view of a commit's output can make a refusal LOOK like success.

   The remedy is one rule. Commit within seconds, and verify by HEAD moving and the row appearing at HEAD,
   never by the tool's printed lines.
3. **VALID names well-formedness, not passing (Z-S169).** The census admits an order as terminal on a VALID
   instance, whatever its criteria say. At 02:3xZ, 7 of 7 such orders carried a FAIL (Z-S170).
4. **A sweep scoped to the census bucket empties itself, and a PASS/FAIL frame is not MECE (Z-S171).** The
   bucket moved 7 -> 5 -> 3 as status words were committed. The third class, UNVERIFIABLE-BY-INSTRUMENT, is how
   an instance declines to self-grade a judgment criterion. Project-wide there are 58 such rows of 450.
5. **Two signed halves specified a control neither seat could execute.** Assuming the adapter's role is refused
   by its trust policy. `iam:SimulatePrincipalPolicy` against the applied policy is the replacement, and
   1.0.0_SA_CTO~Z added a write arm neither half named.
6. **Per-act verification was met by luck of timing, not by design.** Acts landing 15-20 minutes apart outrun a
   30-minute signer tick. rk-25's own build was never measured and is unrecoverable, so its verification is
   graded at the cumulative grain.
7. **A co-signed direct act on an infra path cannot satisfy a lane gate keyed to task orders (W34-S2).** Every
   such act needs the audited escape until the gate knows about co-sign pairs.
8. **A shared library's cache defaults into a numbered worker's deliverables folder (W32-S4).** Any seat that
   runs the posture producer in the shared tree will leave an uncommitted diff on a tracked file.
9. **The slash-bearing key class** spans W27-S10, W32-S3 and rk-23. It is unresolved at the client-visible
   layer until the browser-network capture runs.
10. **Round 13's delivered page surface existed on no remote ref at 14:2xZ.** The three portal commits were on
    no branch of origin (tick 64). This seat's verdict was push DEV and hold PROD. The PROD promote needs a
    co-signed pair that does not exist.
11. **W32-S2: the vendor call Andrew authorized at CARD 5 enriched zero of the seven new names,** because
    `domains.json` declares only the original five. rk-22 still reads AC1/AC2 PASS. Before grading, read the
    criterion text to see whether it tests enrichment at all.

## 6. This seat's own corrections tonight

Each was caught before it reached a committed record, or was corrected in one.

- **rk-30 adapter AC1 classed STALE.** It was a criterion defect. Withdrawn, msg 23652.
- **Z-S170's sweep scope and two-value frame.** Corrected by this seat's own Z-S171.
- **A route census that read page 1 as the whole answer.** 25 routes looked like "0 AMGT routes, they're gone".
  The paginated read gives 101 routes and all 16 present. Disclosed in msg 23616.
- **A first Z-S171 commit that did not land.** It was piped through `tail -5`, and the refusal sat above the
  window. The effect check caught it: HEAD had not moved.
- **An ack claimed before it was made (msg 23618).** It was then made and corrected in the same exchange.
- **A self-disposition census that read 0 rows.** Its glob matched nothing. A zero over zero files is
  out-of-corpus, not absence. Re-run against the file directly: 5.

-- 3.0.0_SA_CVO
