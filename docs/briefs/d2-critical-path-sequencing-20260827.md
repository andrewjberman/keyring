# D2 (Advisor Intelligence) — Critical-Path Sequencing Brief

**Author:** 1.0.0_SA_CTO · 2026-08-27 ~14:4xZ · **Audience:** 2.0.0_SA_COO (allocation planning), Andrew (ratification)
**Authority context:** Andrew-direct at the base CTO terminal, 2026-08-27: main fabric focuses **D2 first, end to end**; D3 in parallel only where it makes sense, otherwise sequenced behind D2. The ~X cohort (D11) is a separate workstream — no interaction.
**Grounding:** directives register @ live board 14:23Z · comp-state (self-test PASS 4/4) · commit-stream read through 08-26 21:05Z · board records reconciled to current state this session (see §7).

---

## 1. Program shape (what closes D2)

D2's registered members + two functional members, in dependency roles:

| Project | Role in the program | dep_stage / state (grounded 08-27) |
|---|---|---|
| **ADVI_PERFRP** | **THE PURPOSE PROJECT** — per-client performance attribution + reporting, Books tab + Book view | Round 1 DELIVERED; remediation mid-flight; seats closed in the 08-27 drawdown |
| **ADVI_INSURE** | Precondition 1 — insurance unblended from AM calcs | EXECUTING; TO-R1-DS (~R) + TO-A1-AE (0.6.0) live; seats closed |
| **ADVI_STITCH** | Precondition 2 — SI history across the 2024 seam | Phase-A TO-A1-DS DELIVERED + certified; TO-A1-AE on observed trigger; Phase B later |
| **ADVI_BDPARITY** (unaffiliated on register) | Verification harness — check-our-work vs BD's own outputs | 5 TOs cut 08-19, QUIET 8d, never seated |
| **ADVI_49F** (unaffiliated on register) | TWR-engine defect chain (c00 in-kind flow leg → c02 CF input; RPS-CUSTODY) | 3 TOs cut 08-19, QUIET 8d, never seated — **overlaps the 08-26 remediation; reconcile before re-seat (§5)** |
| ADVI_49FSRC | Data-sourcing substrate | PARKED by Andrew's word (union OUT; Fidelity-login condition); stage 3 does not open |
| ADVI_COTKEY, OPAL_ADVIPOINTERS | Adjacent members | Active, no open TOs; not on the critical path |

Key architectural facts that bind sequencing (all ruled, none new here):
- Neither precondition gates the **Books-tab interface work on the post-2024 canonical series** (PERFRP JSON, ruled 08-24). INSURE/STITCH gate *completeness* (unblended figures; SI series), not the v1 build.
- **ONE serve gate:** the arm-(a) sovereign word (@7a843d25da) is the single flip/serve gate for BOTH PERFRP and INSURE (COO ruling @8155516dbd). Only Andrew clears it, and D-close additionally requires **his smoke test** (the D4-row precedent binds the class: no comp-closure until he smokes it).
- **Parity accompanies the first emission** (PRD s.11 ruling) — BDPARITY is not a tail-end audit; it arms when PERFRP first emits.

## 2. Current blocking state (one sentence each)

1. **Every executing D2 seat was closed in the 08-27 ~00:0xZ reorientation drawdown** — the remediation chain is intact and unread since 08-26 21:05Z.
2. **The 08-27 12:45Z AC4 acceptance read was not taken** (zero ADVI commits today) — first mechanical act on re-engagement.
3. **The morning package (flow-remediation TOs + charter ratification, 8 rows @642e4bd090) waits on Andrew's allocation unfreeze.**
4. The serve gate (arm-(a)) and the D-close smoke are Andrew's and stay Andrew's.

## 3. The critical path (phases; ∥ marks legal parallelism)

```
P0  RE-ENGAGE (no build work; 1 CVO-class + COO record pass)
    P0.1 Take the missed 12:45Z AC4 acceptance read; record fire state.
    P0.2 TO reconciliation: ADVI_49F c00/c02 + RPS-CUSTODY vs the ruled 08-26
         remediation design (supersede/absorb/stand); BDPARITY stall acknowledged.
         (The STITCH stale-face incident @01ffd6dd30 is the warning class here:
          a stale dispatch surface re-dispatches finished work.)

P1  PERFRP REMEDIATION CLOSE  (DS lane + AE lane, ∥ with P2)
    P1.1 STRUCK 2026-08-27 ~15:2xZ (CTO, on COO 76093's convergence catch). This line
         originally cited @3b2982e290 (|r_net| > 15%/day emitter threshold). Andrew's
         08-26 ~23:4xZ word at the ~U terminal, VERBATIM "No per day plausibility",
         ruled the fixed-threshold instrument OUT (74056; CTO 74069 recorded the
         supersession the same evening). NO fresh word re-commissions it; this brief
         cited a struck pin because it was authored from the COMMIT stream and the
         strike lived on the WIRE. Remediation = P1.2 -> P1.3 -> P1.4, no filter,
         per the minted faces @fea672efd5.
    P1.2 c02 in-kind zero-flow fix            (root cause @ea7c227a24)
    P1.3 c01 unsigned->signed in_kind_value   (defect 3 @07bcdafb2b; add c01 to backfill set)
    P1.4 Backfill — carries BOTH pre-measured hazards:
         no stage-scoping exists (@f62e93b9bb) + the --date vehicle gap (@4da71d969b)
    P1.5 Re-grade; green = the arm-(a) trigger condition

P2  INSURE BUILD-THROUGH  (∥ with P1; DS~R + 0.6.0_AE vehicle + 0.7.0 AE + DE)
    source (a-2 occupancy census first) -> landing -> light gold -> platinum -> 3 frontend points
    AC4 freeze = the SAME gate as P1's serve; build proceeds, serve waits.

P3  SERVE GATE (ANDREW)  — one gate, two projects
    P1.5 green + P2 QA emission -> his word on arm-(a) -> flip/serve -> his smoke.

P4  PERFRP v1 INTERFACE + PARITY  (DE lane resumes on DS contract; parity on first emission)
    P4.1 DE R1 leaves incl. the 2 deferred performance leaves
         ⛔ CORRECTED 2026-08-28 ~19:2xZ (1.0.0_SA_CTO, on 0.4.0_DS_ClientPlatform~V's AC0 census
         @07727aef87): this line previously read "(Activity/Allocation already ship)" -- FALSE on every
         plane measured. 11 of 11 round-1 leaves have NEVER been emitted to any served plane (the emit
         core has no S3 write path by design; platinum/advi/49financial/ holds 12 objects, 0 perfrp, all
         predating the emitters). Round 2 (TO-R2-DS) re-emits the b-series on the campaign-corrected
         upstream under the build-only cap; the serving gate is P3. "Deferred" is identified BY
         MEASUREMENT on that TO's face, never by this line.
    P4.2 BDPARITY P1-PROBE -> P2-CENSUS -> P3-EXACT + T1/T2 (as cut; CRO named on
         methodology BY THE TOs — the PERFRP-subject distribution restriction stands
         separately; COO honors both as written, seam flagged in §5)

P5  STITCH PHASE A CLOSE -> PHASE B
    TO-A1-AE fires on its observed trigger (DS scope-set commit);
    Phase B (rules/classification/tier) after Phase A + Fidelity ingestion.
    SI-labelled series feed PERFRP's SI tier when minted.

P6  D2 CLOSE-OUT: v1 cards live on the 49F switch promote, parity classes printed
    with denominators, preconditions discharged, ANDREW SMOKES IT -> done.
```

**Critical path proper:** P0 → P1 → P3 → P4 → P6. P2 rides in parallel and merges at P3. P5 is the long pole for *SI completeness* but does not gate P3/P4 (ruled). BDPARITY cannot start before first emission by design.

## 4. D3 fold-in condition (Andrew's framing, made operational)

D3 (Account-Level Model Overlay) enters the fold when D2 has "a really solid path through" — operationally: **P1 green + P3 cleared** (serve gate through). **CORRECTED 2026-08-27 ~16:1xZ (CTO, measured before acting on my own line):** the EXACT-JOIN precondition is already **DISCHARGED**, not startable — `SMARTX_BD_EXACT_JOIN_SPEC_20260819.md` delivered @1914fa3fd6 via `D3_MODELOVERLAY.TO-D3.1` (U1 answered as a COMPLETE edge; 4 of the PRD's 7 enum values did not survive measurement), remeasured 08-25 (`D3_SMARTX_BD_JOIN_REMEASUREMENT_20260825.md`), and TO-R1-DS reads DELIVERED + CERTIFIED 6/6 R1 CLOSED on its own face. The original line here said "early-startable, CTO-authored" — wrong twice, authored from the register stance without opening the deliverable (the name-is-not-an-identity class). So there is NO pre-work leg: at fold-in, D3 resumes directly at its open TO set (the platinum projection at 0.7.0 AE per PRD s4c ruling 9, the DE overlay UI lane, D3.5 behavioral pass). D3's open TOs otherwise hold. *(Instrument note: to-check renders TO-R1-DS as ACTIVE because its face status string is prose, not an enum value — the face is right, the render is the artifact of the unrecognized string.)*

## 5. Seat-allocation skeleton (for COO to plan against; classes, not serials)

| Phase | Class | Continuity note |
|---|---|---|
| P0.1 | CVO or AE-class reader | acceptance-read discipline |
| P0.2 | COO record pass | TO faces are the dispatch surface — fix them first |
| P1 | DS-class (remediation author context = DS~U's chain) + AE-class (publisher/backfill = AE~L/~K context) | re-seat the *context*, not necessarily the serial |
| P2 | DS~R context + 0.6.0_AE (Andrew-seated, standing) + 0.7.0 AE + DE | one-project-per-instance |
| P4 | DE~D context + DS base + CRO-methodology as the TOs name | **SEAM:** PERFRP-subject restriction ("nothing to 4.0.0_SA_CRO") vs BDPARITY's named CRO role — both stand as written; any collision routes to Andrew, not adjudicated locally |
| P5 | DS-class + AE on trigger | Phase-B decomp is a fresh COO act |

Capacity law from the 08-25 incident stands: hold-and-say beats quiet-seat-and-degrade; one project per instance.

## 6. Sovereign items this plan waits on (nothing else blocks)

1. **Allocation unfreeze / re-seat word** (the 08-26 floodgates word predates the reorientation; not treated as standing).
2. **Charter ratification** — 8 rows @642e4bd090.
3. **Serve gate arm-(a)** — at P3, and **the close-out smoke** at P6.

## 7. Record-currency note

Board reconciled to this state 2026-08-27 (this session, CTO lane): ADVI_PERFRP / ADVI_INSURE / ADVI_STITCH JSONs + REGISTRY rows now carry the 08-26 burst (root cause, threshold ruling, single-gate ruling, STITCH delivery, reseat) with commit evidence inline. ADVI_BDPARITY's register-unaffiliation is flagged to the register owner (0.0.0_AB_MSTR) — recommend adding it to D2's member set so the board stops under-counting the directive.
