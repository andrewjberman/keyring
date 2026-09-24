# AMGT_RESAPP ROUND 38 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-24 ~17:0xZ
**Input:** `2.0.0_SA_COO~Z`'s drain-end packet, msg 25631, `DRAIN_END_PACKET.md` @`e51fd80d4e` (read to EOF).
**L7 state, RE-MEASURED not adopted:** 7 of 7 `rm-*` orders terminal on the LAST `<status>` tag of each
face (orders APPEND their flips; each face carries exactly one tag, so there is no stale-first-tag risk);
21 acceptance criteria; **0 carrying `judgment="true"`**, with that attribute's 258 uses elsewhere in this
project's orders as the positive control.

---

## 1. L8 -- THE CHANNEL COMPILE (the round's new rows, and no others)

Denominator **12**, exactly the packet's s.4 list. Disposition read from `_latest_dispositions()`
(`.tools/surprise-row-gate.py:433`) -- the resolver the L10 requirement itself reads, which folds this
seat's `adjudicates` lists -- and **not** from the rows' own frozen `hazard_standing`, whose census method
R-78's author retracted this tick. Project-wide before this adjudication: 597 ids, GRADUATED 273,
DISMISSED_WITH_REASON 306, UNDER_INVESTIGATION 18.

| row | class | resolver before | disposition here |
|---|---|---|---|
| `W140-S1` | OBSERVATION | DISMISSED_WITH_REASON | terminal already |
| `Z-S250` | OBSERVATION | GRADUATED | terminal already (carrier for `W140-S2`) |
| `Z-S254` | BLOCKING | GRADUATED | terminal already |
| `Z-S257` | OBSERVATION | GRADUATED | terminal already (carrier for `W144-S1`) |
| `Z-S258` | OBSERVATION | GRADUATED | terminal already (carrier for `Z-S253`/`-S254`/`-S256`) |
| `W140-S2` | OBSERVATION | UNDER_INVESTIGATION | **GRADUATED** -- `Z-S250`, verified at the artifact |
| `W144-S1` | OBSERVATION | UNDER_INVESTIGATION | **GRADUATED** -- `Z-S257`, verified + confirmed in the grid |
| `W141-S1` | OBSERVATION | UNDER_INVESTIGATION | **GRADUATED** -- INERT, additive flag already applied |
| `Z-S253` | BLOCKING | UNDER_INVESTIGATION | **GRADUATED** -- `Z-S258`, by execution |
| `Z-S256` | BLOCKING | UNDER_INVESTIGATION | **GRADUATED** -- `Z-S258`, by execution |
| `Z-S251` | OBSERVATION | UNDER_INVESTIGATION | **CARRIED OPEN** -- round-39 cell, the issuer's |
| `Z-S255` | OBSERVATION | UNDER_INVESTIGATION | **CARRIED OPEN** -- estate-wide exposure, unremedied |

**12 = 5 terminal + 5 graduated here + 2 carried open.** `Z-S265` is new, filed during this L9, and is
carried for round 39.

⚠ **On the carriers' FORM, because it cost this seat a wrong read.** All three carriers recorded their
disarms in **prose**, and two name their targets in **short form** (`-Z-S254`, `-Z-S256`). A full-id match
misses those, and this seat's first pass reported them as uncited -- that read was wrong. `adjudicates` is
the CVO's L9 field (gate limb A-1 refuses it on a worker's row), so this adjudication is where it is written.

## 2. L9 -- THE ADJUDICATION

**No judgment criteria exist this round**, so the L9 grade is the render read `C-RENDER-IS-THE-ORACLE`
requires. `thesis.png` and `peers.png` at `contract-check-after-rm-2/` were READ AS IMAGES by this seat.

**Every mechanical claim in the packet holds**, measured at the terminal baseline (six states, scope=main,
portal DEV `5e339ffd`):

- `bandContainersTopLevel` **1** on all six
- weights **{400, 700} only** on all six -- C1 clean, the 300 and 600 residues **CLOSED**
- **no 8px radius** on any state -- C11 clean, the strip radii **CLOSED**
- `clippedTextBlocks 0`, `shadows 0`, `lowContrastChars 0`, `fonts {Lato}` on all six
- residue: `sizes[10]` on **thesis** (21 chars) and **model** (21 chars), and nowhere else

**The re-keyed band instrument is SOUND**, verified at the bytes rather than taken on report -- this seat's
round-37 error was to reason about this very metric from its NAME. The JSON now **prints its own
coordinates**: `_bandRef rgb(25,38,67)` (`--bg-band` via `--layer-body`) and `_headerRef rgb(10,23,51)`
(the `#0A1733` title strip), counted in **separate fields**. thesis reads band 1 / strip 1, peers band 1 /
strip 0, list band 1 / strip 2 -- and the peers render **confirms strip 0 visually**. An instrument that
records the coordinate it resolves is the right remedy for the class: the next reader can audit the
identity without opening the component.

### The finding the round could not have seen

**`Z-S265`: the Peers tab renders `P/E (trailing)` and `P/E (NTM)` 100x too small, on 12 of 12 members.**

Implied EPS computed from the render alone (price and P/E, same image) falls outside a plausible
0.50-200 band for **12 of 12** as shown, and for **0 of 12** at x100. `lib/research/peers/csc.py:88-89`
states the relation as *"RECIPROCAL: P/E = 1 / ey"* -- arithmetically correct only where `ey` is a
FRACTION -- and that reciprocal has **no locatable implementation**: `comp-find` over `portal/src` +
`lib/research/peers` returns 16 hits across 1043 files, page 1 of 1, with the DEF band holding only
`MEMBER_FIELD_FOR_CODE` and no arithmetic. Every other hit is a relation string, a comment, or a fixture
echoing the relation string.

**Why it survived 38 rounds:** dividing every member by 100 **preserves the ordering** and destroys only
the magnitude, so the table stays internally consistent and ranks members correctly. `rk-14`'s label
discipline governs a column's HORIZON, never its UNITS.

**Not claimed:** which of three faults it is (a reciprocal taken on a percent, a missing x100, or a
mislabelled earnings-yield column). The value is not raw `ey` under either convention, so something
transforms it and this seat did not find that code. **Not a round-38 regression** -- no cell touched the
peers table, and no claim is made about when it entered.

### Two bounds this verdict carries

1. **PLANE.** Every render graded this round is a LOCAL vite render; rounds 37/38 are not deployed. **An
   L9 verdict on this packet is a verdict on the local render and says nothing about the served page.**
2. **The round's authority is not in the record.** `contract-check-after-rm-2/` -- the terminal baseline
   every claim above rests on -- has **19 files on disk and 0 tracked at HEAD**, while
   `contract-check-after-rm-1/` has **18 of 18** tracked as the control proving the path and the
   convention both work. On a shared tree worked by many seats, that evidence exists only as untracked
   working-tree files. Committing it is the issuer's and is one act.

### Two false starts of this seat's own

Recorded because an L9 that hides its instrument failures is worth less than one that does not.

1. `comp-find --name 'contract-check*'` returned a **MEASURED ZERO over 707,108 raw files** for a
   directory that plainly exists and is tracked -- `--name` matches FILE names and the target is a
   DIRECTORY. One step from reporting *"the graded renders do not exist"* against the packet; caught by
   the named-object read (`ls` + `git ls-tree`).
2. The page subtitle appeared to read *"Universe discoveery"* on the downsampled thesis capture; the
   source reads *"Universe discovery"*. **The render oracle has a GRAIN** -- it settles layout, banding,
   clipping and contrast; the SOURCE settles spelling.

## 3. L10 PRECONDITION -- three clauses, measured

1. **Every task order terminal** -- 7 of 7, last-tag read. **MET**
2. **Every channel row dispositioned** -- the 12 above, on the consumer's resolver. **MET**
3. **Every judgment criterion graded** -- none exist, proven against a live positive control. **MET
   VACUOUSLY, and stated as vacuous rather than as graded.**

Ten rows from rounds before this one remain `UNDER_INVESTIGATION` on the resolver. They are prior rounds'
L9 business, not this round's L8 input, and they are named here rather than folded into this round's count.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S416",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-24T17:05:00Z",
    "one_line": "L9 round 38: every mechanical claim in the packet VERIFIED at the terminal baseline and the re-keyed band instrument confirmed SOUND at the bytes -- and, reading the render as the oracle on a round that carried NO judgment criteria, the Peers tab's P/E columns are wrong by 100x on 12 of 12 members (Z-S265), which no criterion in this round could have seen.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": ["AMGT_RESAPP-W140-S2", "AMGT_RESAPP-W144-S1", "AMGT_RESAPP-W141-S1", "AMGT_RESAPP-Z-S253", "AMGT_RESAPP-Z-S256"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, NOT ADOPTED. 7 of 7 rm-* orders terminal, read as the LAST <status> tag in each face (orders APPEND their flips); each face carries exactly ONE tag, so there is no stale-first-tag risk. 21 acceptance criteria across the seven faces.",
        "L10 CLAUSE 3 VERIFIED WITH A POSITIVE CONTROL, because an absence read is worthless without one. ZERO of the 21 criteria carry judgment=\"true\"; the attribute is alive and used 258 times across this project's other task orders, so the absence is REAL and not a token this seat failed to find. The packet's word 'mechanical' is not an encoding -- the file convention is the ATTRIBUTE'S ABSENCE, and grepping for 'mechanical' returns 0 on all seven faces.",
        "THE DISPOSITION WAS READ FROM THE CONSUMER'S INSTRUMENT, not from the rows' own frozen fields. _latest_dispositions('.','AMGT_RESAPP') at .tools/surprise-row-gate.py:433 -- the resolver the L10 requirement actually reads, which FOLDS this seat's adjudicates lists -- returns 597 ids: GRADUATED 273, DISMISSED_WITH_REASON 306, UNDER_INVESTIGATION 18. Of the packet's 12 L8 rows, 5 already read terminal and 7 read open. R-78's ARMED-minus-substring census is RETRACTED by its own author and was not used.",
        "THE FIVE GRADUATED HERE WERE VERIFIED AT THE RESOLVING ARTIFACT, never at the citation. Z-S250 disarms W140-S2 (the issuer read the census in the worker's tree after rm-1's AC3 && chain was found). Z-S257 disarms W144-S1 (PanelFooter's flex-shrink-0 dropped, min-w-0 on both wrappers, clippedTextBlocks 0 in BOTH scopes at 5e339ffd -- confirmed independently in the six-state grid). Z-S258 disarms Z-S253 and Z-S256 BY EXECUTION: artifact VersionId ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe -> 9z.fsHGW7ZN2Qf2yU_rsnv0wiL7uKqRS (807904 -> 844437 bytes), apply 0/1/0 with replan 'No changes', and gen_harvest_prefixes.py --check rc=0 after the issuer regenerated the module at 19a22f2f51. W141-S1 is INERT with its additive flag already applied.",
        "ON THE CARRIERS' FORM, because it cost this seat a wrong read: all three recorded their disarms in PROSE, and two name their targets in SHORT FORM (-Z-S254, -Z-S256), which a full-id match misses. This seat's first pass reported those two as uncited and that read was WRONG. adjudicates is the CVO's L9 field and this row is where it is written.",
        "C-RENDER-IS-THE-ORACLE HONOURED: thesis.png and peers.png at contract-check-after-rm-2/ (portal DEV 5e339ffd) were READ AS IMAGES by this seat, not inferred from JSON. THE SIX-STATE GRID at that baseline, scope=main, DENOMINATOR 6: bandContainersTopLevel 1 on all six; weights {400,700} ONLY on all six (C1 clean -- the 300 and 600 residues are CLOSED); no 8px radius on any state (C11 clean -- the strip radii CLOSED); clippedTextBlocks 0, shadows 0, lowContrastChars 0, fonts {Lato} on all six. RESIDUE: sizes[10] on thesis (21 chars) and model (21 chars) and nowhere else -- exactly as the packet states.",
        "THE RE-KEYED BAND INSTRUMENT IS SOUND, VERIFIED AT THE BYTES AND NOT TAKEN ON REPORT -- this seat's round-37 error was to reason about this metric from its NAME. The JSON now PRINTS ITS OWN COORDINATES: _bandRef rgb(25,38,67) = --bg-band via --layer-body, _headerRef rgb(10,23,51) = the #0A1733 title strip, counted in SEPARATE fields. thesis reads band 1 / strip 1, peers band 1 / strip 0, list band 1 / strip 2 -- and the peers render CONFIRMS strip 0 visually. An instrument that records the coordinate it resolves is the correct remedy for the class, because the next reader can audit the identity without opening the component.",
        "THE FINDING NO CRITERION COULD SEE -- Z-S265: the Peers tab renders P/E (trailing) and P/E (NTM) 100x too small on 12 of 12 members. Implied EPS from the render alone is outside a plausible 0.50-200 band for 12 of 12 as shown and 0 of 12 at x100. csc.py:88-89 states 'RECIPROCAL: P/E = 1 / ey', correct only where ey is a FRACTION, and that reciprocal has no locatable implementation (16 hits over 1043 files, page 1 of 1, DEF band holding only MEMBER_FIELD_FOR_CODE). Dividing every member by 100 PRESERVES THE ORDERING and destroys only the magnitude, which is why a table that ranks correctly survived 38 rounds.",
        "TWO FALSE STARTS OF THIS SEAT'S OWN, RECORDED BECAUSE AN L9 THAT HIDES ITS INSTRUMENT FAILURES IS WORTH LESS. (1) comp-find --name 'contract-check*' returned a MEASURED ZERO over 707108 raw files for a directory that plainly exists and is tracked -- --name matches FILE names and the target is a DIRECTORY. One step from reporting 'the graded renders do not exist' against the packet; caught by the named-object read. (2) The page subtitle appeared to read 'Universe discoveery' on the downsampled thesis capture; the source reads 'Universe discovery'. THE RENDER ORACLE HAS A GRAIN -- it settles layout, banding, clipping and contrast; the SOURCE settles spelling."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @e51fd80d4e asserts seven of seven orders terminal, every row dispositioned, NO judgment criteria on any face, and a terminal baseline at contract-check-after-rm-2/ reading main-scope PASS on every graded column for every state except sizes [10] on thesis and model.",
    "world_is": "Every one of those claims is TRUE as measured here, independently, at the artifacts rather than from the packet's summary. The packet is accurate on its own subject. What it does not claim, and what this L9 adds, is a verdict on the CONTENT the page renders -- and there the Peers comparison table shows a valuation multiple 100x smaller than the column that names it.",
    "notes": "TWO ROWS ARE DELIBERATELY CARRIED OPEN AND ARE NOT ADJUDICATED HERE: Z-S251 (the 13-site prose class asserting the retired --bg-band identity) is a ROUND-39 cell with the issuer as disarm owner and nothing this round remedied it; Z-S255 (portal is an embedded repo with zero active hooks) is an EXPOSURE whose remedy is estate-wide and outside every AMGT boundary, so graduating it here would assert a fix nobody made. Z-S265 is new, filed during this L9, and is carried open for round 39. AND THE ROUND'S OWN AUTHORITY IS NOT IN THE RECORD: contract-check-after-rm-2/ -- the terminal baseline every claim above rests on -- has 19 files on disk and ZERO tracked at HEAD, while contract-check-after-rm-1/ has 18 of 18 tracked as the positive control proving the path and the convention both work. On a box whose shared tree is worked by many seats, the evidence for the round's headline exists only as untracked working-tree files. Committing it is the issuer's, is one act, and is named here rather than assumed."
  }
]
```
