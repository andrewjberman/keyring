# ROUND-8 ANALYSIS -- IRPT_FNTEND

**Seat:** 1.0.0_SA_CTO. **Stamp:** 2026-09-15 ~10:5xZ.

**Inputs:**
- 3.0.0_SA_CVO's slug, msg 97041: record `IRPT_FNTEND_ROUND8_L8_L9_20260915.md` @`29f54c47c7`, carriers C-S99..C-S108,
  `REMEDIATION_v5.md` @`db4e444efb`.
- 2.0.0_SA_COO~F's packet, msg 96994, and its 97021 (cells A and B, written to be cut without that seat).
- The promote record for portal candidate 9adad7ce (1.0.0_SA_CTO~A's `PREPARATION.md` @`323e1fdd75`), for the lint inventory.

**Round 8 delivered:**
- 4 of 4 orders drained; 49 of 49 at HEAD.
- All 4 judgment criteria graded PASS, each with a named qualification.
- 19 new rows: 10 graduated, 9 dismissed with reason. The standing census reads 0 missing; 0 of 246 rows lack a carrier.
- The Investor Reporting portal gate holds at DEV 10c2f07d and at the promote candidate 9adad7ce.

**The project still cannot close.** Its closing proofs need IRPT_BCKEND, as rounds 6 and 7 said.

## Rulings on the eight open rows, and on two qualifications

1. **S66 -- the backend admin wall. PUT TO ANDREW, with a recommendation. Nothing changes until he answers.**
   - The fact (3.0.0_SA_CVO, source read): the portal is the only admin wall. `_scope/resolve.py:186-187` resolves any
     role=admin caller with a verified firm as FIRM_OPERATIONS, so a partner firm's admin calling the API directly would be
     served its own firm's data. No PRD or FWD names a backend wall; R8.9 lists it as not moved.
   - No route serves yet: IRPT_BCKEND B15 builds them, and IRPT_BCKEND sits in stage 3 behind Platform Logic. So nothing is
     exposed today.
   - The question is whether Andrew's condition 2, "no clients are allowed to see that", binds the DATA or only the PAGE.
     Read plainly it binds the data. But a backend wall widens IRPT_BCKEND's scope on his word, so it is his call, not
     inferred here.
   - REC: yes. Before any IRPT_BCKEND route serves, the backend refuses a caller who is not role admin AND firm
     opal-capital. It lands as an IRPT_BCKEND FWD at its next PRD revision.
   - The design question that FWD must answer first: the resolver's own comment says "the injected header set cannot
     separate an Opal-platform admin from a partner-firm admin". So the wall needs an identity signal the header set does
     not carry today.
2. **W3-S37 -- the reason travels with the explicit unknown, wherever the adapter supplies it.**
   - This is round 7's W3-S35 rule applied to the path the grant excluded: a status member with no state takes
     wireEnvelope's reasonless default.
   - `adaptStatusEnvelope` supplies `NO_STATUS_REASON` when the status member states no state. The document's own reason
     still comes first (amendment 1, 96947). Cell D.
3. **W3-S38 -- a stated state wins, wherever the response states it.**
   - For status-summary and status-job, the data IS a status document, and it states PARTIAL at the top level. That is
     the response's stated state. The adapter lifts it, with its reason, into the carried availability, and supplies no
     `NO_STATUS_REASON`.
   - The cell's first act is the read 3.0.0_SA_CVO did not make: which production components render those two
     operations' availability or top-level state. Cell E.
4. **W3-S41 -- fixed by this seat in `.tools/proof-of-spec-check.py`, the COUNT-BAR limb.**
   - A digit directly after a letter or an underscore ends an identifier (`F47-AC2 PROBLEMS`); it is not a count.
   - ANSI escapes now read as a space, not as nothing. Without that, the new rule would hide a real count an escape glued
     to a word (`pass\x1b[0m4 fail`).
   - Self-test arms: Y2 (an id's trailing digit, 0 violations) and Y3 (a glued count, 1 violation). The commit is named in
     this seat's send.
5. **W4-S19 -- RULING W reaches Holdings: a classification the producer does not assert reads "withheld".**
   - Both PRDs' CONTRACTS line reads: "Both only when authoritative; an unknown value is an explicit unknown state, never
     false and never Client" (`IRPT_BCKEND_PRD.md:153`, `IRPT_FNTEND_PRD.md:123`). So "unknown" is a value the producer
     ASSERTS. A partition the panel declines to assert is not that value, and printing it as "unknown" makes it
     indistinguishable from one.
   - `tabs/holdings/slices.ts:100-102` renders every partition of a non-authoritative classification as "withheld".
   - "Render every partition above as unknown" is the portal's OWN comment (`contracts/index.ts:708`), not ratified text.
     So this is a cell, not an L4 amendment. That comment and `slices.ts`'s header (:21-25) change with the code.
     `SliceTable`'s `data-classification-authoritative` marker stays.
   - Before the edit, a WHOLE-SUITE run finds every test that asserts "unknown" for a non-authoritative classification.
     A grep cannot see what a test asserts through a helper. Cell F.
6. **S68 -- cell A, as 2.0.0_SA_COO~F wrote it in 97021.** `gen-wire.ts` normalizes CRLF to LF before hashing, and every
   wire header citing a source sha256 is regenerated. Discriminator: `fe-s-25/generator.test.ts` green on an untouched
   checkout at BOTH line endings.
7. **W2-S35 and W4-S20 -- 2.0.0_SA_COO~F's rows, one cell (G).**
   - The fe-s-14 control is re-pointed to the re-pointed test's own git form (committed trees), over a known pair where
     `firmAccess.ts` GAINED 3 entries, so it can return an answer the test would refuse.
   - `fixtures/index.ts:77`'s `proves` prose reads "renders as withheld".
8. **The lint inventory at the promote candidate -- the three IRPT errors, cell C.**
   - `fe-s-5/alias-probe.test.ts:16:20` (no-constant-binary-expression); `fe-s-19/pre-envelope.test.ts:43:28` (unused
     PERFORMANCE_KEY); `export/ExportButton.tsx:246:5` (react-hooks/immutability).
   - ExportButton's code is runtime-correct: the effect hides a DOM node and restores it on cleanup. The remedy moves the
     hide and restore into `useExportAnchor`, where the node is obtained.
   - **ADDENDUM 12:3xZ (0.0.0_AB_MSTR 97061): the two SentimentGauge errors fold into this cell.**
     - They are `src/components/market-performance/SentimentGauge.tsx:6:10` and `:6:22`, unused PanelEmpty and PanelError
       imports from DSGN_REBRND's a65b939a and a7c4fa4f.
     - DSGN_REBRND has no live seat, so they could not be routed there.
     - The fix is two import deletions. Cell C's `<paths>` names the file explicitly, and the order states it is
       DSGN_REBRND's file, carried under this ruling.
     - One cell then clears all five lint errors, and portal DEV CI can read green for the first time since 09-11.
9. **F49-AC8's carried-hunks arm, cell B, as 2.0.0_SA_COO~F wrote it.** If c29a8b86 is an ancestor of HEAD, its 2 unrelated
   hunks are expected; if not, they must be absent. Green at 9adad7ce AND at 10c2f07d.
10. **F46-AC8 qualification (3) -- the cap stands.** A committed cost above 20000 ms has no legal timeout under the 60000 cap.
    Such a test is split or its cost cut; it never gets a timeout above the cap. This is a rule for any later timeout cell,
    not a cell now.

## Round 9 -- ONE issuance of seven small cells

| Cell | Rows | What moves |
|---|---|---|
| A | S68 | `gen-wire.ts` hashes LF-normalized text; wire headers regenerated |
| B | F49-AC8 | the carried-hunks arm keyed to ancestry |
| C | lint | the three IRPT lint errors above |
| D | W3-S37 | `adaptStatusEnvelope` supplies the reason for a status member with no state |
| E | W3-S38 | a status document's own state is the response's state |
| F | W4-S19 | Holdings' non-authoritative partitions read "withheld" |
| G | W2-S35, W4-S20 | the fe-s-14 control re-pointed; the fixture prose corrected |

- Every cell is test-side or render text. No contract field moves, and no served behaviour except the words D, E and F
  change on screen.
- The build goes on a portal branch from the promoted head. The DEV push waits for the freeze release.
- The seat: 2.0.0_SA_COO~F holds IRPT_FNTEND through round 8 and then frees (Andrew's approved rec (b)). Round 9's issuance
  is the next COO's, seated by 0.0.0_AB_MSTR. The cell text here and in 97021 is complete enough to cut from cold.

**At Andrew:** item 1 (S66), the backend admin wall.
