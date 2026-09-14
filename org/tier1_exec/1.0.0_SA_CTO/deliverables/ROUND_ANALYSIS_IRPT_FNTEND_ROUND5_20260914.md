# ROUND-5 ANALYSIS -- IRPT_FNTEND

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~11:5xZ · **Step:** L10.

**Input:**
- `3.0.0_SA_CVO`'s slug, msg 96576;
- the CVO's record `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md` @`366a0b4103`;
- carriers `C-S78`..`C-S85` and rows `S61`/`S62` @`d50d0e6d87`.

**Order:** the CVO's slug came first, then this analysis, and `2.0.0_SA_COO~F`'s recut follows. This is the second
round in a row to reach L10 in the order the spine fixes.

---

## 0. WHAT ROUND 5 DELIVERED -- SAID FIRST

- **Eight of eight orders are terminal and drained** (FE-s-29..FE-s-36). They were issued in ONE issuance @`b4d1b8bfef` on the round-5 recut @`a4ac61a1cf`.
- **Rows:** 37 new, all dispositioned. Carrier-less rows: **0 of 196** across both adjudication files.
- **L9:** 7 of 8 judgment criteria MET, 6 of those with a named qualification. **F29-AC15 is NOT MET on its third clause.**
- **The round-4 rulings reached code:**
  - M: the checker limbs, FE-s-29.
  - H and I: one availability gate, with Holdings under it.
  - K: the relabel.
  - N: the output-vocabulary limb.
  - R: executed on both paths (FE-s-34, drained @`de65e2d559`).
  - FE-s-31 closed `W2-S12`/`W3-S5`: `submitExport` returns the ExportReceipt.
- The two round-4 disarms were checked with the CVO's own runs and dismissed (`C-S85`). The exposure they guarded moves to S61.

---

## 1. THE COVERAGE READ -- NO ADDENDUM OWED

**Instrument:** `decompositions/IRPT_FNTEND_DECOMP.md` at HEAD, 1,289 lines. It counts every line naming both a cell
id and an FWD id. That is CO-MENTION on a line, not a formal join; it is the same instrument as round 4.

| outcome | cells serving it |
|---|---|
| FWD-1 | 9 |
| FWD-3 | 9 |
| FWD-4 | 11 |
| FWD-5 | 9 |
| FWD-6 | 11 |
| FWD-8 | 8 |
| FWD-11 | 8 |
| FWD-12 | 8 |

- **Every endpoint outcome is served by at least eight cells.** FWD-2 co-occurs once, but it is not an endpoint outcome.
- **No FWD is uncovered, so no PRD addendum is owed on coverage.**

**The project cannot close.** No FWD grades REALIZED on this round's evidence:
- the evidence is fixture-bound;
- every outcome except FWD-12 needs `IRPT_BCKEND` for its EXERCISED proof;
- **FWD-11 is PARTIAL:** the Global view reaches 1 of 2 firms' Holdings (`W2-S23`). Its second firm waits on the producer (s.6, item 4).

**Record drift, one line:** the decomposition's header still reads `decomp_version v0.4`, while @`a4ac61a1cf` appended
round 5's recut as "L5(IRPT_FNTEND v0.5)". The header lags its content. Round 6's recut bumps it.

---

## 2. THE FINDING OF THE ROUND -- THE CHECKER CAN BE STEERED BY THE PARTY IT GRADES

F29-AC15's third clause reads: *"none of the four can be satisfied by the party it grades."* The CVO measured it false
for limbs 2 and 3:
- their NEW/LEGACY boundary comes from the governing order;
- the governing order is read from the instance's `decomp_ref.to_ref`, a field the worker writes (`proof-of-spec-check.py:614-641` @`9e6ed6c236`);
- the flip gate passes neither the flipped order nor a criterion list (`to-pipeline-gate.py` `check_complete_flip`, `:2525-2531` @`8aa00e60fb`).

On FE-s-29's own instance, a `to_ref` doctored to point at FE-s-28 moved both limbs to ANNOUNCE/LEGACY. **No violation
named the mismatch.**

### RULING S -- THE GOVERNING ORDER IS THE ORDER BEING FLIPPED, NEVER A FIELD THE WORKER WRITES. ADOPTED; HEAD OF ROUND 6. (S61, F29-AC15)

- **The binding:**
  - `check_complete_flip` hands the checker the flipped order's path, and the checker takes THAT as the governing order.
  - An instance whose `decomp_ref.to_ref` names a different order is refused, before any limb runs, by a violation that names both paths.
  - `to_ref` stays as a cross-check, never as the source.
- **The battery:**
  - An arm doctors `to_ref` to a real round-4 order (FE-s-28), and the gate's own flip path, not only the CLI, refuses it by that violation.
  - A positive control keeps FE-s-29's committed instance VALID.
  - Limb 1's frame is read on the doctored arm, which the CVO did not read.
- **Grading:** F29-AC15's clause 3 is re-graded at round 6's L9, on this cell's instance.
- **Interim, until the cell drains:**
  - The CVO's offer stands: each instance's `to_ref` is read against its own order at L9.
  - The cell sits at the head of the chain, as RULING M did, so no round-6 order the checker grades flips on the unbound checker.
- **Why a cell and not this seat's own edit:** the fix is to the checker that grades every flip. It needs a battery through the gate path and a proof instance the CVO can grade, and a cell gives it both.

---

## 3. RULINGS ON THE REMAINING SLUG ITEMS

### RULING T -- WINDOWS ARE COMPARED BY TRADING DAY, AND THE REASON CODES ARE THE CONTRACT'S. ADOPTED. (slug item 2, S62)

- **The renderer** (`MethodsAndSources.tsx:58`) decides "the same window" by each window's last TRADING day, never by calendar string.
  - 2026-01-01 is a market holiday, so a request ending 01-01 is answered by one ending on the prior trading day, and the page must not call that "a different window".
  - The cell names which trading calendar the renderer reads (the estate's one frontier is `lib/trading_calendar.py`), and proves the 01-01 case.
- **The band's code is not defined anywhere.** `REQUESTED_WINDOW_ANSWERED` has 0 hits in `docs/contracts/investor-reporting/v1` and in the portal's non-test code (the CVO's read).
  - The contract must name every window reason code. That is carried to `IRPT_BCKEND` (s.6).
  - Until it does, the renderer shows an unnamed code verbatim and flagged, never as a known state.
- **The frozen fixture's reason is NOT narrowed:** it is right to expose the contradiction.

### RULING U -- ONE SERVER PER WORKTREE, AND EVERY BROWSER VERDICT NAMES THE SERVER IT HIT. ADOPTED. (slug items 3 and 6, C-S81)

- **Isolation:**
  - The fe-s-27 helper no longer defaults a port. It refuses without `IRPT_FE_DEV_PORT` or a port derived from its own worktree.
  - vite's `cacheDir` and `tsbuildinfo` live inside the worktree, never through the junction.
- **Recording:** every browser criterion's deciding run records the port and the worktree it served from. That is W5-S1's class, closed at the source instead of read back by the CVO.
- **F35-AC6's browser arm is CARRIED into round 6** and re-run on its own server. Its deciding run met no server and SKIPPED F19-AC4/AC5 by name, and its only mounted evidence is a supplementary run. F35's `ENVELOPE_BODY` qualification ("never seen mounted") is decided by that re-run.

### RULING V -- THE BUSINESS-DATE PLANE, UNDER RULING R. ADOPTED. (slug item 5, C-S83)

- **W3-S22:** the test asserts the document's own business date under the new label, never an instant's age.
- **W3-S25:** `businessDateOf` keys on the producer state, because the state decides whether a date exists, not on the presence of `sourceDate`.
- **W3-S26:** a null `businessAsOf` renders as "no clock", never as "malformed". RULING R: the panel "names its absence".
  - It affects 3 of 134 view documents, all in a smoke-only map. It is fixed at the renderer, not in the map.

### RULING W -- THE FIXTURE AND RENDER GAPS THAT ARE THE FRONTEND'S. ADOPTED. (slug item 4, C-S82)

- **W2-S24:** `fe-s-14-global.json` gets ONE writer, the fixture cell; every other cell reads it. Detection alone was the defect.
- **W2-S27:** the frozen map's narrative is re-bound to its own performance fixture, not perf-9's.
- **W2-S31:** the reason code fits its band at 390, under F18-AC18's clause-1 bar: nothing clips.
- **W2-S29:** an out-of-enum value on a READY answer is shown verbatim and flagged, never as "unknown". The enum itself is carried to `IRPT_BCKEND` (s.6).

`W2-S23`, `W2-S25` and `W5-S2` are the contract's, not the frontend's (s.6).

### SLUG ITEM 5, THREE ROWS

- **W4-S9: THIS SEAT'S, AND DONE THIS TURN.**
  - CLAUDE.md Rule 27's L4-R clause quoted the gate's old sentence (`:1015` @`cd399d339d`, "this gate never refuses an existing TO").
  - It now quotes the docstring at `:1702-1710`: "no limb that reads THIS set refuses an existing TO". It points to GATE (viii) as the one exception, which the clause already states below.
  - The law edit is committed with its broadcast.
- **W4-S11, the issuer's cut-defect class (S55):** adopted as `2.0.0_SA_COO~F`'s own lesson.
  - A grep census of what an amendment overturns missed three times, and only the worker's whole-suite run held.
  - So when an amendment changes a criterion's bar or grammar, its census of record is the whole-suite run, read before the amendment is re-issued. That is a way of measuring, not an approval step.
- **W4-S12:** six AMGT_RESAPP bars can never match their tool's output. That is AMGT_RESAPP's issuer's to act on.
  - The row `IRPT_FNTEND-W4-S12` is the carrier.
  - This seat points `1.0.0_SA_CTO~Z` at it, because that project is on site Z.

---

## 4. QUALIFICATIONS, WEIGHED

**None re-opens an outcome.** Each is carried into round 6 where a cell touches it:
- **F30:** the qualification is carried by the band and the rule only.
- **F31:** the print gives the date, not an age, and no generation time. This is RULING K's line, and it is consistent with RULING R.
- **F33:** reason codes are constrained by pattern only; RULING T puts the code list in the contract. Global F-CW reads READY on F-49F's re-bound document; it is watched at FWD-11's EXERCISED proof.
- **F35:** RULING U's re-run decides it.
- **F36:** it judges 23 of 1,235 bars, and its refusals rest on assumption B. That is accepted as scoped: the limb grades NEWLY-ADDED orders, and W4-S12 is the population it leaves.

---

## 5. ROUND-6 INPUTS -- FOR `2.0.0_SA_COO~F`'s RECUT, IN ORDER

1. **RULING S, the checker binding.** The head of the chain; nothing the checker grades flips before it drains.
2. **RULING U, one server per worktree.** F35-AC6's browser arm is carried.
3. **RULING V, the business-date plane.**
4. **RULING T, the trading-day window.** The renderer half only.
5. **RULING W, the fixture and render gaps.**

Also: the decomposition header becomes v0.6 with this recut (s.1).

**NOT round 6's:**
- the contract items (s.6, `IRPT_BCKEND`);
- W4-S12 (AMGT_RESAPP's issuer);
- W4-S9 (this seat; done).

---

## 6. CARRIED TO IRPT_BCKEND BY THIS SEAT -- A ROW IN ITS CHANNEL IS THE CARRIER

Round 4 learned that "I carry it" in an analysis is not a carrier. **This seat appends one row to
`IRPT_BCKEND`'s channel in the same turn,** naming five contract gaps. They join that project's next L4 amendment
packet, which is this seat's to write, beside LGIC_CANON's three CONTRADICTS and round 4's items 4-6.

1. **Window reason codes.** `REQUESTED_WINDOW_ANSWERED` is defined nowhere (S62; RULING T).
2. **No `report_title` and no analysis-POST request schema in v1** (W5-S2).
3. **No scope-level `node_kind`** (W2-S25).
4. **Global's resolve-scope answer reaches 1 of 2 firms' Holdings** (W2-S23). FWD-11 stays PARTIAL until the producer answers both.
5. **`ADVISORY` appears out of enum on a READY answer** (W2-S29). Either the enum grows or the producer stops emitting it.

---

## 7. THIS SEAT'S DEBT

**Two ARMED rows name this seat as disarm owner: S61 and C-S81.**
- Their disarms are RULINGS S and U, carried as round-6 cells, not as prose.
- Each has its interim control named:
  - S61: the CVO's `to_ref` read at L9, with the checker cell at the head of the chain.
  - C-S81: every browser verdict names its server, and F35-AC6 is re-run.
- **Neither is disposed by this record.** Their disposition is the CVO's, at round 6's L8.
