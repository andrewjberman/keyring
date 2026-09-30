# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 26, `CRPS-ab-4` (the map rebuild, the 18-block re-derive, the dossier refresh) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~22:5xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND26_AB4_SERVED_ACT.md` @`ad19f49aa7` (msg 27420, READ-acked; read to EOF,
5,987 B).
**Rulings it serves:** round-25 analysis rulings 2-3 and s.4 item 4 (@`19207dfb83`).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **The dry run is the one this seat asked for after its own aa-4 miss.** It covers every key (100) and prints every (from, to)
  transition: `unit 30 sign 20 currency 2 value 0 ... other 0 errors 0`, with 1 write per block.
  - BP's `PE_RATIO` -> RATIO (series median 24.65) and `PROF_MARGIN` -> PERCENT (median 1.43) are ruling 2, applied as ruled.
  - BBSE3 moves in reason text only; it stays UNRESOLVED.
  - The 6 `unit_evidence` method changes move no unit.
- **BP's two header labels, checked independently** (block `BP-SLASH-_LN_Equity/20260930T190146Z`):
  - `CUR_MKT_CAP` is 89,798,586,794.73, labelled USD ("reporting"). With PX_LAST 571.8 GBp, that is about 15.7bn shares × GBP 5.718.
    **The value is in POUNDS** (in USD it would be about 121bn).
  - **So the current USD label is WRONG, and ab-5's "no currency" removes a wrong label.** That is the ruled "never claim a
    measurement not made" rather than an assumed GBP. `NET_DEBT`'s side is unmeasured, and it goes to no currency on the same rule.
- **The case diff** is exactly two paths per case on 17 names (`trailing_median_pe.value` -> null, and `reason`), with 0 case values
  moved. That is ruling 3.
- **Code:** `git diff --stat 9b9585065a HEAD -- integrations/bloomberg/research lib/research/corpus lib/research/identity` is
  **empty**.
- **The predecessor-code diff** is run against every served block by the dry run itself (ruling 3). The one peer file,
  `drafting_build.py`, is outside the closure (aa-4 AMENDMENT 1).

## 2. CONDITIONS

1. **Act-start:** the IMPORT-CLOSURE diff from `9b9585065a` is empty, and each of the 18 blocks is re-captured immediately before (c).
   Otherwise STOP.
2. **Leg v adds BP's served `CUR_MKT_CAP` value next to its label:** the value is byte-unchanged, and only the label drops. This is the
   negative arm on the value plane.
3. **The served-reach note stands.** BP's payload keeps 778.57 until AMGT_RESAPP redeploys the scoped API, which recomputes cases from
   its DEPLOYED `case_rule` (`scoped_amgt.py:3195`). That redeploy is RESAPP's own WORLD pair. After (c), tell `2.0.0_SA_COO~Z`, who
   names it in its round-55 issuance.

## 3. ROLLBACK

The COO half stands: revert the map commit and the round-26 code, then re-derive forward. The prior stamps stay. A delete is Andrew's
act.

## 4. NOT COVERED

- the scoped-API redeploy (RESAPP's);
- Brookfield BN CA onboarding (the RESAPP r54 analysis ruling 4; CORPUS universe);
- every key outside the dry run's 100.
