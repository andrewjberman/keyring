# CTO ROUND ANALYSIS -- NFRA_TRNSPT round 12 (FWD-10 AI investment commentary thread)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-08 ~22:5xZ | **Input:** `2.0.0_SA_COO~T2` msg 1838; packet
`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R12_CLOSE.md` @21eec739ed. The CVO's slug is not yet in; this analysis
is written on the COO packet and is revised if the slug differs.

## The one decision asked: is C-WIPE-GATE recorded passed?

**RULING: YES. C-WIPE-GATE is PASSED at current code.**
- `NFRA_TRNSPT.TO-TR-w1` is `complete`, with its proof VALID (d15a6e9951, 2026-09-30). TR1-w1-AC1 is the planted-token test that the
  PRD's C-WIPE-GATE names.
- The wipe changed after that: round 11's allowlist (256c5a4386). So this seat re-ran the gate at HEAD 49c04cd4b2:
  `python -m pytest data/transcripts/scripts/tests/test_wipe_planted.py -q -p no:cacheprovider`. Result: **13 passed**.
- Its result is "the planted classes were removed". That is not "no PII remains" (PRD C-WIPE-GATE).

**What this unlocks:** the first real Kimi K3 call, under Andrew's 2026-09-30 word (PRD C-KIMI). The input is the abstract fields only.
Any second use of the vendor needs his word for that use.
- **Measured state:** gold holds 0 objects, so the first draft is the no-precedent draft.
- **Not decided here:** gold body text sent as precedent waits on gold existing. When it does, the gate is re-run at that HEAD.

## Enrichment list (round 13)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | D2-S6: the drafter emits `generated_at`, matching ~V2's ticket contract | the H6 contract test passes; the trace reaches H6 without a dead letter |
| E2 | The first real Kimi call: one no-precedent draft from abstract fields | one call, logged by request id with no prompt body; the draft lands as a ticket DRAFT that only Opal can see |
| E3 | The journey trace re-run H2 to H6, with the gate real (not simulated) | every hop reads OK, or names the one hop that breaks |

H1 (the analysis report's READY event, from ~P2) and H5 (the ticket service route, ~V2's FWD-6 workstream) stay stubbed until their
owners land them.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~23:0xZ) -- round 13 drain-end (`~T2` msg 1862, `R13_CLOSE.md` @ab11f097f3) and the D2-S7 ruling

**Measured, from the packet:** E1 to E3 are met on the stub. One Kimi K3 call was made on synthetic inputs and returned a no-precedent
DRAFT of 3,908 characters with no planted identity. D2-S6 (`generated_at`) is fixed. **Andrew's 2026-09-30 word for the first call is
now spent:** every further call needs his word per use (PRD C-KIMI).

**D2-S7 RULING: household is NOT required on a ticket the `svc-commentary` principal creates.** It is not sourced either.
- **Why:**
  - C-KIMI limits the commentary path to abstract fields with no client identity, and the household is client identity. Giving the drafter
    a household source would widen what it holds for no reader's benefit.
  - The `analysis_request` definition's `household` question (`lambda_function.py:86`, `required: True`) is the human form's question
    (FWD-1).
- **The rule:** a type's `required` set is evaluated per creating principal. The `svc-commentary` create requires `report_request_id`,
  `draft_commentary`, `generated_at` and the firm, and nothing else. Anyone opening the ticket reaches the household through
  `report_request_id`, by IRPT's firm-fenced read.
- **Owner:** `2.0.0_SA_COO~V2` (C-TYPE: data, not code), one cell in its F10 workstream.
- **Order with the F10-d-1 deploy:** leg D (CTO half @a4ccfb4439) may ship first, because the widening is unreachable until leg M. Leg M
  (the mint) waits for this fix to be live, or real reports dead-letter on the first call.
- **Direction:** under C-PACKAGE (TCKT_VNEXT ADDENDUM 2) the commentary lands on the REQUESTING ticket, which already carries the household
  from the human form. The separate svc-commentary ticket is the interim path.

**Act only Andrew can do (cited):** a standing word for one Kimi call per Analysis Request in this workflow. Citation: PRD C-KIMI ("any
other use of a vendor call carries his word per use") and CLAUDE.md "NEVER call an external vendor API without Andrew's explicit per-use
word". Without it, the automated workflow stops at the commentary step on every request.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-08 ~23:3xZ) -- FWD-7 graded REALIZED (`~T2` msg 1946)

**Read by this seat on the served log** (`/aws/lambda/outlook-global-transcripts-pull-lambda`, filter `window_days`, since 23:29Z):
`MAIL-PULL-FIRE run=20261008T233013Z window_days=7 listed=12 admitted=0 landed=0 skipped_known=0 list_refusals=0 silver_rows=0 held_out=0`.
This is the scheduled fire, not an ad-hoc one. The C3 ledger closed @7b234d0031.

**FWD-7: REALIZED**, by round 4's test ("REALIZED when L5 closes").
- `admitted=0` of 12 listed is the admission filter's own verdict on tonight's mail. It is not an outage, and it is not graded here.
- The mail_pull hold lift is MSTR's act, and ~T2 has told it.

-- 1.0.0_SA_CTO~DELL2
