# AMGT_HARVST -- ROUND 8 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~02:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~O` (file 20260928T023026Z): `adjudications/ADJUDICATION_v16.md` and
`remediations/REMEDIATION_v2.md` @`fd93bed742`. Round 8 closed on its ISSUED half by this seat's ruling
(20260928T022141Z): a card at Andrew is not an order.

**Round 8 is CLOSED. The project is NOT closed: no FWD grades REALIZED.** Recut owner: `2.0.0_SA_COO~Y`.

## 1. WHAT ROUND 8 DID

| item (round-7 list) | outcome |
|---|---|
| 1 repair cell `w-1` | complete; Z-W9-S1 listings half and Z-S27 read remedied at HEAD by the CVO; **the 3 red tests are STILL RED** (Z-W21-S2: 3 failed / 306 passed on the CVO's re-run) |
| 2 capture `w-2` | CARDED at Andrew (vendor word) -- not issued |
| 3 timeline build `w-3` | complete |
| 4 ft/barrons `w-4`, 5 bbg `w-5` | CARDED at Andrew -- not issued |
| 6 the 16 backlog rows | **not re-measured on the record -- carried a SECOND time** |
| (route) Z-W11-S1 | REMEDIATED by this seat @`454fc37e30`, measured on a sparse cone (27 -> 0 orphans) |

## 2. MY MISS, STATED FIRST: L9 WAS VACUOUS AGAIN, AND THE ROUND-7 ANALYSIS CAUSED IT

The round-7 analysis required "at least one judgment criterion" and named the capture cell -- a WORLD cell
that cannot issue without Andrew's per-use word. The only judgment criterion therefore sat on a card, and L9
graded nothing (C-S24). **Corrected rule, binding on every recut from here: the round's judgment criterion
sits on a cell that can issue without a pending Andrew word.** A second judgment criterion on a WORLD cell
is welcome; it never replaces the first.

## 3. FINDINGS THE RECUT MUST ANSWER

1. ~~**The repair cell did not repair.** The 3 red tests were its reason for existing and they still fail.
   Either its criterion did not require them green (a cut defect) or it did and graded green on something
   else. **The recut reads `w-1`'s order and instance and says which, before cutting a second repair.**~~

   **SUPERSEDED (2.0.0_SA_COO~Y, 20260928T0242Z, measured @`9a5d538d35`) -- both horns were wrong.** `w-1`
   was cut for Z-W9-S1 (AC1) and that repair LANDED, with a negative control. The red suite was AC2, a
   REGRESSION BASELINE requiring disclosure with every failure named -- exactly what this seat's round-7
   analysis asked for -- and 0 assertions were altered. **And it is TWO tests, not three** (one test
   SUBFAILS twice). A second repair is still needed; its diagnosis is
   `deliverables/2.0.0_SA_COO_Y/WHY_THE_RED_TESTS_ARE_STILL_RED_20260928.md`, including an UNGUARDED
   `.json()` at `publishers.py:672` that a completed test double would hide. **Round 9 cell 1 carries that
   guard as its own criterion, so a green suite cannot imply it.**
2. **A barrons test alternates between two failure faces across identical runs** (COO~Y's two-run finding).
   A test that fails differently on identical input is not a regression baseline. Quarantine it with the
   reason stated, then diagnose it inside `w-4`'s scope.
3. **Item 6 is carried twice.** It is the issuer's act, not a worker's; the round-9 issuance commit states
   the 16 rows re-measured or states why not.
4. **Three remedies read at HEAD, clocks not flipped** (Z-W9-S1 listings half, Z-S27, Z-W11-S1): REMEDIATION_v1
   rows still read OPEN because the table carries no flip verb. **Recorded here as REMEDIATED on the CVO's
   HEAD read (Z-W11-S1 also on this seat's own measurement);** ~~the disarm owner writes the evidence rows.~~
   **CORRECTED: REMEDIATION rows are the CVO's to write (CLAUDE.md section 2; `.tools/surprise-row-gate.py`
   splits it: the disarm owner acts and files evidence, `3.0.0_SA_CVO` writes the clock).**

## 4. FWD GRADES -- all nine NOT REALIZED

`w-3` built the timeline surface, but FWD-5/FWD-6 are graded on an analyst EXERCISING it, which no cell did.
Nothing else in round 8 reached a DONE WHEN population. Unchanged from round 7 otherwise.

## 5. THE ENRICHMENT LIST -- round 9, in order

| # | cell | note |
|---|---|---|
| 1 | **Second repair, from COO~Y's diagnosis** (finding 1): the 2 red tests + the `publishers.py:672` `.json()` guard + quarantine of the flaky barrons test (finding 2) | LOCAL. Criteria: the guard exists (a non-JSON body raises `AuthExpired`, shown directly, not via the suite); the suite's failed count is ZERO or each remaining failure is quarantined with a named reason |
| 2 | **Timeline EXERCISE (LOCAL) carrying the round's JUDGMENT criterion**: open the validation security's timeline, pick a day, read the articles strongest first -- are the events shown the real coverage bursts? | FWD-5/FWD-6. This is the issuable cell the corrected rule requires |
| 3 | The three cards `w-2`, `w-4`, `w-5` | unchanged, at Andrew; each fires only on his live per-use word. `w-2` keeps its own judgment criterion |
| 4 | Item 6, the 16 rows | the ISSUER's act, stated in the issuance commit |

No serp or social cell (Andrew 2026-09-27, @`a89b7619ca`). Fan-out: `1` and `2` are independent and LOCAL;
the cards serialise on the vendor ledger and session vault when they fire.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not read `w-1`'s instance itself (finding 1 is the recut's first act). It grants no vendor word. It
adds no outcome and re-opens no L4-R half: a recut input, not a PRD addendum.

## Compiler Tools

The CVO's slug and ADJUDICATION_v16 read, not re-derived; the round's terminality taken from this seat's own
recorded ruling; Z-W11-S1's remedy cited from this seat's measured commit rather than asserted.
