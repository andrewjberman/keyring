# AMGT_RESAPP -- ROUND 1 ANALYSIS (L10, 1.0.0_SA_CTO~Z)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

| | |
|---|---|
| **Answers** | the L10 slug `surface-channel/remediations/REMEDIATION_v1.md` @`b8f0b21938` from `3.0.0_SA_CVO~Z` (msg 21185), stamps L8.r1/L9.r1/L10.r1 |
| **Graded against** | each FWD's `DONE WHEN` STATE LINE in the PRD ENDPOINT, NOT the surface manifest's COVERED claim |
| **Routes to** | `2.0.0_SA_COO~Z` (the round-2 recut) · Andrew (the gates in s.4) · `0.0.0_AB_MSTR~Z` (the register) |

---

## 1. THE VERDICT: 0 of 14 REALIZED. A STRONG BUILD ROUND THAT CLOSES NO OUTCOME -- AND THAT IS THE HONEST GRADE.

The build is real and largely sound: **16 of 16 orders terminal, each with a VALID proof instance; 24
channel items, 0 undispositioned; 16 of 16 judgment criteria graded (13 PASS / 2 FAIL / 1
NOT_EVALUATED).** The CVO's compile and adjudication are not in question. This is not a weak round.

⛔ **BUT 13 OF 14 FWDs CARRY AN `EXERCISED` BAR, AND `EXERCISED` MEANS AN ANALYST HAS ACTUALLY USED A
SERVED SURFACE -- WHICH CANNOT HAVE HAPPENED, BECAUSE THE SURFACES ARE NOT SERVED.** Every `.tsx` waits
on Andrew's DESIGN_SPEC approval (C-DESIGN-SPEC-FIRST), and the approval block measured EMPTY at the
drain-end (COO~ZZZ, msg 21137 item 4). No analyst can open a page that does not serve. So the
`EXERCISED` bars are systematically UNMET -- not because the work is bad, but because the outcome the
work SERVES has not been exercised. This is the same discipline as the OPSEC round-3 read: **grade the
DONE WHEN state line, never the fact that a cell was built.** A cell that builds the model block does
not make FWD-1 (an analyst read a pack) true.

**FWD-9 is the one `APPLIED` bar, and it is still NOT_REALIZED**: "the marking is in place beside the
evidence on the page" needs the page, and the page waits on the same design-spec gate.

**This round does NOT close.** It is graded, settled, and routed to round 2 -- it is not flag-closed.

---

## 2. THE GRADE, PER FWD (all NOT_REALIZED; the reason distinguishes the surface gate from a defect on top of it)

| FWD | bar | cell | verdict | why not REALIZED |
|---|---|---|---|---|
| FWD-1 | EXERCISED | S1 | NOT_REALIZED | surface unserved; **and W1-S2**: the fiscal-year join marries non-December filers' fundamentals to prices ~9mo later (a served-correctness defect, not a render) |
| FWD-2 | EXERCISED | S2 | NOT_REALIZED | surface unserved (no uncovered name pulled + read on a page) |
| FWD-3 | EXERCISED | S3, S11 | NOT_REALIZED | surface unserved; W1-S2 also touches basis/vintage |
| FWD-4 | EXERCISED | S4, s-b4 | NOT_REALIZED | surface unserved; **s-4 AC7 NOT_EVALUATED** -- its bar needs SA raw landed, which had 0 at grade time and 18 objects/3 tickers since (04:02Z): a round-2 RE-RUN of an exercisable criterion, not a defect |
| FWD-5 | EXERCISED | S5 | NOT_REALIZED | surface unserved (Adam has not forwarded a printed pack) |
| FWD-6 | EXERCISED | S6 | NOT_REALIZED | surface unserved (no analyst compared two versions) |
| FWD-7 | EXERCISED | S7 | NOT_REALIZED | surface unserved (Adam has not used the freshness view) |
| FWD-8 | EXERCISED | S8 | NOT_REALIZED | surface unserved; **s-12 coverage owed**: the identity layer is 32 MEASURED/32 distinct after W7-S3's remediation, but 57 UNRESOLVED residual remains (coverage, not a regression from a 48 that held 16 falsehoods) |
| FWD-9 | APPLIED | S9 | NOT_REALIZED | the marking's home (.tsx) waits on the design-spec gate; APPLIED "beside the evidence on the page" needs the page. Also a per-use word for the drafting model is pending (s-9) |
| FWD-10 | EXERCISED | S10, S11 | NOT_REALIZED | surface unserved; **s-10 AC6 FAIL** -- '12345 [PROVISIONAL]' skims as "a number, fine": the held-back rule is in the DATA and absent in the READING, so an unchecked figure ships looking checked. Remedy scoped in SPEC_SECTION_checkface.md (a colour/icon marker) -- land it BEFORE the .tsx serves PROVISIONAL figures |
| FWD-11 | EXERCISED | S13 | NOT_REALIZED | surface unserved; S13 is `measure, then build` on an unexercised catalogue; a Bright Data social per-use word is pending (s-13) |
| FWD-12 | EXERCISED | S14 | NOT_REALIZED | surface unserved (no single input re-run demonstrated on a page) |
| FWD-13 | EXERCISED | S12 | NOT_REALIZED | surface unserved; the identity DATA layer is partly exercised (W7-S3 disarmed at the artifact) but "checked on a name more than one business uses, on the page, found not mixed" needs the page; the 57 unresolved (s-12) also bears here |
| FWD-14 | EXERCISED | S15 | NOT_REALIZED | surface unserved; **s-15 AC6 FAIL** -- the official-vs-impostor test is a bare OR of three unequal checks, so an impostor beats the weakest (a copied "official account of <domain>" bio admits on check 3 alone). Remedy: require check (3) to CO-OCCUR with (1) or (2). **And the two lists' owners are UNASSIGNED (C-NO-CONTACT)**, so nothing is told when a list rots |

---

## 3. COVERAGE READ (the CTO's L10 obligation): EVERY FWD HAS A CELL. NO PRD ADDENDUM.

Walking the 14 outcomes against the surface manifest S1-S15 (+ s-b4 for FWD-4's SA half): **every FWD
is served by at least one cell; 0 outcomes are UNCOVERED.** So there is no `/endpoint --forward` F0
re-entry and no PRD addendum owed on coverage grounds -- the ENDPOINT is complete and the round's gap
is EXERCISE, not a missing outcome. (S12, the identity layer, is the root four surfaces depend on; the
CVO and COO both treat it correctly as prior-to-S4/S8/S13.)

---

## 4. WHAT ROUND 2 NEEDS -- AND THE ANDREW GATES THAT SIT ABOVE IT

⭐ **THE TRUE CRITICAL PATH IS ANDREW'S DESIGN-SPEC APPROVAL.** Until DESIGN_SPEC.md is approved
(C-DESIGN-SPEC-FIRST), NO `.tsx` serves, so NO surface FWD can reach its EXERCISED bar however good the
build. This is the one gate that moves 12 of 14 outcomes at once. It is expressly qualified here as the
essential wait Rule 27 permits -- a UI that serves before its design is approved is the failure
C-DESIGN-SPEC-FIRST exists to prevent -- but it is a wait, and it is Andrew's to lift.

**AT ANDREW (the round's surfaced decisions, all gating REALIZED):**
1. **DESIGN_SPEC approval** -- unblocks every surface FWD. The pivot.
2. **Social vendor per-use word** (one Bright Data trigger, s-13) -- FWD-11.
3. **Drafting-model per-use word** (s-9) -- FWD-9.
4. **Peer-universe quota** (s-8's classification) -- FWD-8.
5. **List owners** (the publisher allowlist + the company-to-social map, s-15, C-NO-CONTACT) -- FWD-14.

**AT `2.0.0_SA_COO~Z` (the round-2 recut, ONE issuance -- the mechanical work that does not wait on the
design spec):**
- **s-10 checkface marker** (FWD-10) -- land the colour/icon before PROVISIONAL figures serve.
- **s-15 impostor AND-clause** (FWD-14) -- require check (3) to co-occur with (1) or (2); the OR is the defect.
- **s-4 SA re-run** (FWD-4) -- SA raw has landed; re-exercise the criterion (not a re-write).
- **s-12 identity coverage** (FWD-8, FWD-13) -- resolve the 57 UNRESOLVED; the folder-name fallback for
  the SAP-GY-style placeholder is an identity-layer design question, not a mid-cell edit.
- **W1-S2 fiscal-year join** (FWD-1, FWD-3) -- a served-correctness fix with a control on a NON-December
  filer; the join always succeeds and a December-heavy sample cannot see it.
- The surface EXERCISE of every FWD, once the design spec is approved and the .tsx serve.

⛔ **DO NOT RE-CUT s-b4's fetcher** (W9-S2 is disarmed by the completed re-run; its world-fact stands),
and do not read the 57-unresolved identity residual as a regression from the 48 that held 16 falsehoods.

---

## 5. OWNED BY THIS SEAT (carried, not gating the round)

- **The grades schema `criterion` pattern** (`^[A-Za-z0-9]+-AC[0-9]+$`, compound-only) contradicts its
  own description on a project whose orders carry bare ids (`AC6`). The CVO minted deterministic
  compound values (`AMGTs12-AC6`) and disclosed it; **the fix is mine as schema owner** -- the pattern
  should admit the instance's own string, or the description should stop promising it. Not this round's.
- **Rail/gate-owner items** surfaced as investigation rows: `S2` (a per-file check answering a set
  question -- instrument grain), `W2-S4` (a bare comp-tool on a branch answers from the MAIN checkout
  and reported 0 for a route that exists -- rail-wide, recurs on every branch that adds a route). These
  are the same class as tonight's other rail findings; owned, on no round-2 critical path.
- **The criterion-cannot-discriminate rows** (W7-S1, W2-S2, W3-S4 always-fail; W7-S5 jointly
  unsatisfiable with the lane gate; W3-S2 the proof-of-spec filename, twice in one round) are cut
  defects the CVO named; they are decomposition-quality feedback for the recut, not FWD gaps.

**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` pushes.
