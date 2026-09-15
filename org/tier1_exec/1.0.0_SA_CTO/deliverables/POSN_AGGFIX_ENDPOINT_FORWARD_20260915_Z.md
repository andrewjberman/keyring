# POSN_AGGFIX -- ENDPOINT (step 2, /endpoint --forward)

**Author:** `1.0.0_SA_CTO~Z` (spine L2). **Date:** 2026-09-15.
**Status:** EMITTED, NOT CONFIRMED. The spine makes Andrew's word on each DONE WHEN line the confirmation (L2 "Tool").
**Amended 2026-09-15 ~17:1xZ, before confirmation, ids unchanged:** FWD-2 and FWD-7 name advisors as well as clients;
FWD-4 and FWD-6 carry dependencies the L1 brief measured. Findings from `4.0.0_SA_CRO~Z` msg 23175, re-read by this
seat at the portal (origin/PROD `edf85ce503` `portal-proxy.ts:1418-1426`: the model route is "internal + advisor
only" and "blocks client tier") and at ruling 5's own text.
**NOT YET LANDED IN A PRD.** No PRD exists. The block below belongs verbatim under the section title
`## ENDPOINT (step 2, /endpoint --forward)` in `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` at L4.
**Authority:** Andrew-direct ~16:2xZ, record `ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md` (this folder).

**Input (the brief, by Andrew's designation):**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md` @ `2033ff3ea6`
(origin/CLOUD, and on SITEZ byte-identical since `1e268c164e`; blob `0765b9af1f`; 13372 bytes; authored by
`4.0.0_SA_CRO`, dated 2026-09-15; no `generated` line).
**L1 brief in an admitted shape:** `docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md` @ `1e268c164e`
(blob `8a527c8aa0`, 27655 bytes, by `4.0.0_SA_CRO~Z`). Its outcomes O1-O7 map onto FWD-1..FWD-8 and re-open nothing.
Every `:n` below is a line of that blob, read with `git show 2033ff3ea6:<path> | cat -n`.

---

## The endpoint

```
ENDPOINT -- POSN_AGGFIX (emitted 2026-09-15; awaiting Andrew's DONE WHEN word)

  FWD-1  Opal staff can view the whole firm's aggregate book on the Positioning page
         DONE WHEN  EXERCISED -- an Opal user has opened Positioning, chosen the
                    aggregate, and read both the composition picture and the
                    holdings table for it
         ACCEPT     An Opal staff member opens Positioning, picks the aggregate,
                    and both the composition chart and the holdings table show
                    the whole firm's positions.
         SOURCE     :27 "restore the UI for Opal users only"; :21 "Both panels you
                    named read the same selected book"; :129 Phase 1 step 3

  FWD-2  Nobody outside Opal sees the aggregate on the page
         DONE WHEN  EXERCISED -- the page has been opened as an advisor and as a
                    client, each including a viewer whose browser remembers the
                    aggregate as its last choice, and no aggregate choice appeared
                    for either
         ACCEPT     An advisor or a client looking for the aggregate cannot find
                    it, and one whose browser remembered it lands on an ordinary
                    model instead.
         SOURCE     :27; :126-128 "Gate it by viewer ... a mode-level flag would
                    show AGG to clients again"; :133-135 remembered selection;
                    brief O3 "An advisor or a client never finds the aggregate"
         AMENDED    before confirmation: the advisor arm added (brief finding 1)

  FWD-3  Each aggregate holding shows how the models share it, marked as firm-wide
         DONE WHEN  EXERCISED -- an Opal user has read the per-model split on
                    aggregate holdings, on the page as it looks today
         ACCEPT     For any aggregate holding, an Opal user can read how much of it
                    each model accounts for; the split is plainly marked as the
                    whole firm rather than any advisor's own book, and it is easy
                    to read on the page's current look.
         SOURCE     :49-50 the Model Breakdown group; :131-132 "Label it as
                    Opal-wide, not advisor exposure"; :86-89 "The columns need
                    re-authoring in current tokens, not a revert"

  FWD-4  The aggregate uses the firm's current model mix
         DONE WHEN  EXERCISED -- the aggregate's model mix has been compared with the
                    firm's most recent assets-by-model figures, and they agree
         ACCEPT     The share each model carries in the aggregate matches the firm's
                    latest assets by model, not a mix left over from months ago.
         SOURCE     :22-23 "A straight revert would restore a stale number"; :74-76;
                    :147-148 Phase 2 step 1; D1 :167
         DEPENDS    D1 = "Together" (the CRO's rec). On "Phase 1 alone" this outcome
                    is not promised, the endpoint must say the mix is stale, and the
                    aggregate comes back on the old portfolio file that Andrew's
                    2026-09-09 ruling 5 treated as no longer needed (brief F9,
                    finding 3).

  FWD-5  The aggregate says which day's figures its model mix comes from
         DONE WHEN  EXERCISED -- an Opal user has read the date shown with the
                    aggregate and checked it against the figures it uses
         ACCEPT     An Opal user can see on the page which day's figures the
                    aggregate's mix is built from, and that day is correct.
         SOURCE     :150-151 "so the UI can print the date instead of implying
                    freshness"; D1 :167 "nothing in today's data could label its date"

  FWD-6  Every Opal model's money counts in the aggregate
         DONE WHEN  EXERCISED -- the aggregate's inputs have been read: the blended
                    models count through the models they are split between, and
                    the per-model figures have been reconciled to the firm total
         ACCEPT     No Opal model is left out of the aggregate. The blended models
                    count through the models they split into, and any gap between
                    the per-model figures and the firm's own total is explained,
                    never silently dropped.
         SOURCE     :23-24 "still drops the two 50/50 Opal Blend models"; :77-79;
                    :109-111 "Reconcile before relying"; :149; D2 :168
         DEPENDS    D2 = "Fold them in" (the CRO's rec). On "exclude with a note" the
                    ACCEPT becomes: the page says plainly which models are left out.
                    ALSO: explaining the gap depends on the owner of the firm's
                    assets-by-model figures, which this project relies on and does
                    not own; the gap is already in that owner's source (brief F4,
                    finding 2). If Andrew prefers a bar this project alone can
                    meet, the last clause becomes "is shown plainly as not yet
                    explained". Not changed here, because that choice narrows the
                    outcome.

  FWD-7  The aggregate figures are not sent to clients at all
         DONE WHEN  EXERCISED -- what an advisor's and a client's signed-in
                    sessions receive has been read and neither carries the
                    aggregate, while an Opal session still receives it
         ACCEPT     Looking at what an advisor's or a client's browser is given
                    shows nothing about the firm-wide model mix or the firm total,
                    while Opal staff still get the aggregate and the page still
                    works for them.
         SOURCE     :82-85 "A UI gate makes AGG Opal-only on screen, not in the
                    data"; :158-160 Phase 3; D3 :169; brief O7
         AMENDED    before confirmation: the advisor arm added. The plan's Phase 3
                    precedent refuses clients only, so a design copied from it
                    would fail this line (brief finding 1)
         DEPENDS    D3 = "Move it" (the CRO's rec). On "leave it", this outcome is
                    retired before landing and the endpoint says, in one line, that
                    clients' sessions keep receiving the firm-wide mix and total.

  FWD-8  What clients and advisors already see on Positioning does not change
         DONE WHEN  EXERCISED -- each of the five model views has been compared
                    before and after the change, and they match
         ACCEPT     A client or advisor viewing any of the five models sees the same
                    holdings and weights after the change as before it.
         SOURCE     :153-154 "the five model books must be byte-unchanged, checked
                    by comparing before and after"; :126-128
```

**D4 (default book for Opal users, `:170`)** adds an outcome only if Andrew picks the aggregate. It would read
"An Opal user who opens Positioning starts on the aggregate" and would take the next unused id at that time. No id is
reserved for it now.

**No outcome above is a wait.** Each is proven by opening the page as a named kind of viewer, or by reading and
comparing figures that already exist. None names a date or an event nobody controls.

## Out of scope (from the brief, `:176-182`)

- The aggregate on Attribution and Factor Tilts.
- The AGG bond-fund ticker, which shares the string.
- A per-advisor aggregate.

## What Andrew is asked, in order

1. **Confirm or change each DONE WHEN line**, FWD-1 to FWD-8. This is the spine's L2 confirmation.
2. **Answer D1, D2 and D3** (`:167-169`). FWD-4, FWD-6 and FWD-7 are written on the CRO's recommendation for each,
   and each carries the line it becomes under the other answer.
3. **Answer D4** (`:170`), which only adds an outcome.
4. **The process question** (`:172-174`): the plan asks whether he wants the 2026-08-24 exemption or the full flow.
   `0.0.0_AB_MSTR` is reported to be asking him now (msg 23163). This endpoint assumes the full flow, because he named
   `/endpoint --forward`.

## Carried to L4, not decided here

- **`brief_ref` RESOLVED ~17:0xZ.** `4.0.0_SA_CRO~Z` landed `docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md`
  @ `1e268c164e`, an admitted L1 shape on SITEZ, and carried the plan onto SITEZ byte-identical. Read back by this
  seat: both paths in SITEZ HEAD, the plan's blob equal to origin/CLOUD's.
- **The CRO's measurements are the CRO's.** This phase re-derived none of them: the served file's aggregate block, the
  July-dated weight file, the seven-model current file and its unexplained gap. L4 cites them at their vintage, and
  the decomposition re-measures anything a cell relies on. The L1 brief re-locates the plan's producer and portal
  line numbers to SITEZ HEAD and origin/PROD, so L4 cites the brief's locations, not the plan's.

## Provenance

```
GROUNDED ON: the plan @2033ff3ea6 (read whole, 13372 bytes, line-numbered for citations);
             Andrew-direct relay msg 23156; the ~W scope relay msg 23163 (for what is being asked of Andrew)
NOT READ:    the task-order register, the project row, any PRD (none exists), portal source, the served files,
             the producer source -- Phase 0 reads the brief and nothing else, by the skill's F1 rule
```
