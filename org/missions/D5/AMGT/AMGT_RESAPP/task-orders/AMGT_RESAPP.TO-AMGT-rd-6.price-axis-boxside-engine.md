# AMGT_RESAPP.TO-AMGT-rd-6 -- THE PRICE AXIS ENGINE: a 30-day price ranking in the BOX-SIDE puller shape on the BLOOMBERG TERMINAL box, never a Lambda calling Bloomberg

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-6. THE PRICE AXIS ENGINE, BOX-SIDE. The price ranking reads Bloomberg historical/intraday and
therefore runs in the BOX-SIDE PULLER SHAPE -- the ETF-daily-pull shape -- and NOT as a Lambda calling
Bloomberg. 30-day window, matching chatter; Andrew unified both axes to 30. Writes PRE-COMPUTED per-ticker
rows into `opal-amgt-security-metrics`.

READ THE HOST CAREFULLY, BECAUSE THIS IS WHERE THE CELL CAN GO WRONG SILENTLY. "BOX-SIDE" HERE MEANS THE
BLOOMBERG TERMINAL BOX -- the machine whose loopback-only DAPI at 127.0.0.1:8194 is the only place
Bloomberg data can be pulled. It does NOT mean the new harvester EC2 box that `AMGT-rd-3` stands up: that
box hosts the four ARTICLE harvesters and has no Bloomberg terminal on it. Two different machines, two
different concerns. The decomposition carried the wrong edge here at v0.6 and it was corrected at v0.6.1
before issuance precisely so this order would not send you to the wrong host.

WHY A LAMBDA CANNOT DO THIS: the DAPI is loopback-only. A Lambda has no route to it. That is the same seam
`AMGT-s-2` exists to cross and it is not re-opened here -- you run where the terminal is.

WHAT TO PRODUCE, under integrations/bloomberg/ + lib/research/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE ENGINE  computing the price axis per ticker over a 30-day window in the box-side puller shape,
      reading Bloomberg historical/intraday through the existing terminal path rather than a new one.

  (b) THE WRITE  PRE-COMPUTED ranked rows into `opal-amgt-security-metrics` under the key schema
      `AMGT-rd-2` landed, so the Lead Panel reads without re-deriving.

  (c) THE HOST RECORD  a deliverable naming the host the engine runs on and the existing box-side pull it
      follows, so a reader can see the shape was copied from a live precedent rather than invented.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-2` (the metrics store) ONLY.** It does NOT depend on `AMGT-rd-3`: the harvester box
is not this engine's host. Worked in slot ~2's queue after `AMGT-rd-2` lands; independent of `AMGT-rd-5`
and `AMGT-rd-7`.

## BOUNDS

```
BLOCK THE HOST IS THE BLOOMBERG TERMINAL BOX, NOT THE NEW HARVESTER BOX. Do not deploy this engine onto
  AMGT-rd-3's EC2 instance; it has no terminal and the pull will fail or, worse, silently return nothing.
BLOCK NOT A LAMBDA CALLING BLOOMBERG. The DAPI is loopback-only. A Lambda has no route to it.
BLOCK 30-DAY WINDOW, matching chatter. Andrew unified both axes to 30. Do not pick a different window.
BLOCK PRE-COMPUTED ONLY -- write ranking OUTPUTS; never leave the ranking to render time.
BLOCK BLOOMBERG SIGN-IN IS NOT YOURS. The two-attempt sign-in budget belongs to `0.0.3_BG_BBGTerminal`.
  Credentials reach a process ONLY through `bbg_credentials.py --` and are never written anywhere. If the
  terminal is signed out, that is a BLOCKING row and a stop, not a sign-in attempt by you.
BLOCK READ `integrations/bloomberg/READ_HERE.md` FIRST -- Bloomberg, any scenario. Never mint
  `data/bloomberg/`; the derived layer is current-day-only.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER on the output. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
WARN Bound every invocation under `timeout 120`. A live Bloomberg pull may exceed that -- exercise it in
  the cell and assert on the PERSISTED result, not on the pull itself.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD s.3b C-PRICE-RANKING-BOXSIDE (Andrew-direct 2026-09-11 ~12:1xZ): "the price axis reads Bloomberg
    historical/intraday and therefore runs in the BOX-SIDE puller shape (the ETF-daily-pull shape), NOT a
    Lambda calling Bloomberg. 30-day window, matching chatter (Andrew unified both to 30)."
DECOMPOSITION v0.6.1 s.13g (this cell's own correction, made BEFORE issuance): v0.6 wrongly gave this cell
    a dependency on AMGT-rd-3, conflating "box-side" with "the box this round builds". The ETF-daily-pull
    shape runs on the BLOOMBERG TERMINAL box against loopback DAPI. The edge was removed and the fan-out
    re-measured. Stated here because the wrong edge would have mis-scoped this very order's <paths>.
AMGT-s-1 (LANDED, round 1): the model block pulls ~20 line items x 10 fiscal years + ~25 header scalars
    from DAPI 127.0.0.1:8194 by a BOX-SIDE job, raw vendor bytes landing before derivation. That is the
    live precedent for the shape; read it rather than inventing a second one.
comp-schedule --drift (at the cut): C3 = 12 standing NEVER clauses including the no-monitor moratorium.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/
lib/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-6.price-axis-boxside-engine.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W2-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-6"><invocation>timeout 110 python -m pytest lib/research integrations/bloomberg/research/tests -q -k "price" 2>&amp;1 | tail -3</invocation><expect>a summary line with a passed count and no "failed" -- including a test pinning the window to 30 DAYS, matching chatter. A suite that does not pin the window is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-6"><invocation>timeout 110 .tools/aws dynamodb scan --table-name opal-amgt-security-metrics --max-items 12 --output text 2>&amp;1 | tail -10</invocation><expect>pre-computed PRICE-axis rows present alongside whatever chatter rows exist -- each carrying a ticker and a price-axis score. An empty table, or a table carrying only chatter rows, means this engine never wrote and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-6"><invocation>timeout 110 comp-find "8194|blpapi|localhost|127.0.0.1" lib/research integrations/bloomberg --limit 20 2>&amp;1 | tail -12</invocation><expect>a printed denominator showing the price engine reaching Bloomberg through the LOOPBACK DAPI path (127.0.0.1:8194 / blpapi), i.e. box-side. A denominator of 0 hits across 0 files is OUT-OF-CORPUS and is NOT met. Evidence that the engine instead calls Bloomberg from a Lambda, or targets the harvester EC2 box, is the defect this criterion exists to catch and is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-6" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the 30-day window is pinned and matches chatter.
- **AC2** (mechanical, LIVE plane): real pre-computed price rows landed.
- **AC3** (mechanical, denominator-bearing): the engine genuinely runs box-side against loopback DAPI.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): does the engine run on the BLOOMBERG TERMINAL box in the established ETF-daily-pull shape -- not on the new harvester EC2 box and not as a Lambda -- and did it follow the LIVE precedent (`AMGT-s-1`'s box-side job) rather than inventing a second path to the same data?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b `C-PRICE-RANKING-BOXSIDE`, ANDREW-DIRECT 2026-09-11 ~12:1xZ -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13 + 13g, AMGT-rd-6) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN B, slot ~2. Depends on `AMGT-rd-2` ONLY. Independent of `AMGT-rd-5` and `AMGT-rd-7`.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-6` row, as corrected at 13g.
> **NOTE (2.0.0_SA_COO~ZZZ).** This is the cell whose edge I got wrong at v0.6 and corrected at v0.6.1 before any order was cut. The correction is carried INTO the worker face rather than left in the decomposition, because the failure mode is a worker deploying to the wrong host and finding no terminal there -- which looks like a broken engine rather than a wrong address.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C3 = 12 standing NEVER clauses incl. the no-monitor moratorium. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) across 96 mapped role(s); box-side compute, and the metrics write rides a role. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, 51 GRANTED-BROAD excluded not cleared.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8, incl. 13g's correction of THIS cell's edge). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- writes this project's own table; no shared served artifact moves.
</preflight>
**Preflight disposition:** a box-side producer against a landed store, whose sharpest hazard is HOST CONFUSION -- carried as an explicit bound, a mechanical denominator criterion and the judgment criterion.
