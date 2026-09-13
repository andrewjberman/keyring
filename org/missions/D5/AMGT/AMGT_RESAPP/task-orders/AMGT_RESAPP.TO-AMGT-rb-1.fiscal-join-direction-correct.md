# AMGT_RESAPP.TO-AMGT-rb-1 -- THE FISCAL JOIN, DIRECTION-CORRECT: _nearest_price returns UNRESOLVED when no on-or-before price exists, never a FUTURE price at a small absolute gap; a price_date is never after its period_end

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 2b, FWD-1/FWD-3; fixes AMGT-r-1 / finding C-S15 FAIL)

```
AMGT-rb-1. THE FISCAL JOIN, DIRECTION-CORRECT. AMGT-r-1's fye_join.py passed the fiscal-alignment sample
(30 rows), but the CVO's control found a bounded source defect (C-S15): `_nearest_price` falls back to the
nearest point in EITHER direction when the series has nothing on-or-before the period_end, and `gap_days`
uses `abs`. So a period_end 2025-12-31 with only a 2026-01-02 price returns that FUTURE price at gap_days
2 and passes the under-45-day check -- a price from AFTER the period end, which is not yet the market's
reaction to that period's results and is exactly what C-FISCAL-YEAR-JOIN's "as of that period end" forbids.
ALL 30 live served rows have ZERO such violations at this vintage -- a BOUNDED source defect, not a fourth
live failure -- but the join can silently accept a future price for a future input.

WHAT TO PRODUCE, under integrations/bloomberg/research/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE FIX  in `_nearest_price` (integrations/bloomberg/research/fye_join.py): return UNRESOLVED (None)
      when NO price exists on or before period_end -- drop the either-direction future fallback entirely.
      A resolved row's price_date is NEVER after its period_end; keep `gap_days` non-negative and computed
      as (period_end - price_date).days (which is >= 0 once the direction holds), never a hidden absolute
      clamp over a future price. fiscal_period_join carries the UNRESOLVED (price None, price_date None,
      gap_days None) through unchanged, exactly as it already does when no price row exists at all.

  (b) THE FUTURE-ONLY NEGATIVE CONTROL, in tests/test_fye_join.py  a test that MUST distinguish the fix:
      period_end 2025-12-31 with ONLY a 2026-01-02 price returns UNRESOLVED (price None), NEVER a resolved
      row at gap_days 2. The OLD code returned the future price at gap 2; the fix returns UNRESOLVED. Plus
      a DIRECTION ASSERTION: for every RESOLVED row, price_date <= period_end.

  (c) PRESERVE THE PASSING SAMPLE  the 3 landed securities (SAP GY, BA US, BABA US) still resolve with
      max gap under 45 days and every price_date on or before its period_end -- 0 of 30 rows was affected
      by the defect, so the served sample and its exact pins do not move.
```

## DEPENDENCIES

**NONE** for rb-1 itself. (AMGT-rb-2, the consumer integration, DEPENDS ON this cell and is queued to the
same worker slot -- it runs after rb-1 lands.) Reads AMGT-r-1's landed fye_join.py, derive_fye_fixed.py,
check_join_fye.py and the served model_block_fye blocks (all at HEAD).

## BOUNDS

```
BLOCK C-FISCAL-YEAR-JOIN / DIRECTION: a resolved price_date is NEVER after its period_end; no price from
  after the period end is ever paired. UNRESOLVED is the correct answer when nothing is on-or-before.
BLOCK PRESERVE THE PASSING SAMPLE: the 3-security sample's gaps and pins do not change (0 of 30 affected);
  the fix only changes behaviour when the series has NOTHING on-or-before the period end.
BLOCK C-S8 (correction-note): fiscal period end is read from the fundamentals ROW-DATE already on the
  record, NEVER a mapped FISCAL_YEAR_END reference field (that field is BAD_FLD for this coverage).
BLOCK NO NEW UNIQUE SECURITY (F2/G-24): re-use the landed securities; a fourth is a widening (AC3).
BLOCK NO new vendor call: reads LANDED data and the landed served block; integrations/bloomberg/READ_HERE.md
  binds if any re-read is needed -- health first, NEVER a sign-in.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @b3acbcf3dd (C-S15, BLOCKING): "period_end 2025-12-31 plus only price_date 2026-01-02 returns
    price 100, gap_days 2. fye_join._nearest_price falls back to the nearest point in either direction;
    gap_days uses abs, so the under-45-days mechanical check accepts this direction violation. All 30 actual
    landed rows have zero such violations at this vintage. Return unresolved when no on-or-before price
    exists; add a future-only negative control and a direction assertion. Preserve the passing three-security
    sample and its exact pins."
L10 round-2 analysis @c48576bf85 s.3: "a bounded source defect, not evidence of a fourth live security
    failure." C-S8: name the measured row-date carrier, do not imply a mapped FISCAL_YEAR_END field.
AMGT-r-1 (landed): fye_join._nearest_price (the either-direction fallback + abs gap); fiscal_period_join
    already carries None-price rows through; test_fye_join.py is the difference arm; check_join_fye.py reads
    the served block; pull_log.json records the securities.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rb-1.fiscal-join-direction-correct.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/` (where AMGT-r-1's check_join_fye.py and
pull_log.json live). A path missing from that block is a path you are REFUSED on. Refuse a criterion you
cannot satisfy as written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W1-S<k>` continuing your prior
sequence -- your next is `AMGT_RESAPP-Z-W1-S6`, project AMGT_RESAPP, fabric site-z) and STOP on that
criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rb-1"><invocation>python -m pytest integrations/bloomberg/research/tests/test_fye_join.py -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- AMGT-r-1's tests still pass PLUS (1) a FUTURE-ONLY negative control: period_end 2025-12-31 with only a 2026-01-02 price returns UNRESOLVED (price None), never a resolved row at gap 2; and (2) a DIRECTION assertion: every resolved row's price_date <= period_end. A test that still accepts the future price, or omits the direction assertion, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rb-1"><invocation>python -c "import importlib.util as u,datetime as dt; s=u.spec_from_file_location('fj','integrations/bloomberg/research/fye_join.py'); m=u.module_from_spec(s); s.loader.exec_module(m); pe=dt.date(2025,12,31); fut=m._nearest_price([(dt.date(2026,1,2),100.0)], pe); ob=m._nearest_price([(dt.date(2025,12,30),99.0),(dt.date(2026,1,2),100.0)], pe); print('future_only_resolves_to', fut, '| on_or_before_picks', (ob[0].isoformat() if ob else None), '| on_or_before_not_after', (ob is None or ob[0] <= pe))"</invocation><expect>"future_only_resolves_to None" (a future-only series is UNRESOLVED, never clamped to the future price) AND "on_or_before_picks 2025-12-30" AND "on_or_before_not_after True" -- when an on-or-before price exists it is chosen and is never after the period end. A non-None future_only result is the C-S15 defect and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rb-1"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json')); print('unique securities requested', len(set(l['securities'])))"</invocation><expect>"unique securities requested" of 3 or fewer -- NEGATIVE: the direction fix and its control added no new unique security (F2/G-24)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rb-1" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): the future-only negative control and the direction assertion are in the test suite and pass on the fix.
- **AC2** (mechanical, difference arm): `_nearest_price` returns None for a future-only series and picks the on-or-before price otherwise, never after the period end -- the exact C-S15 defect cannot recur.
- **AC3** (mechanical, NEGATIVE): no new security.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): is UNRESOLVED the right answer when no on-or-before price exists (never a hidden future clamp), and is the direction assertion sound and complete? This is the C-S15 regrade.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.4 + L6 round 2b) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-2 analysis @c48576bf85 (answering CVO slug REMEDIATION_v2 @b3acbcf3dd, finding C-S15) -> L5 recut decomposition v0.4 @192c198231 (section 11, AMGT-rb-1) -> this round-2b issuance.
**Chain:** round 2b, the FIRST of a two-cell chain (AMGT-rb-1 -> AMGT-rb-2), both on integrations/bloomberg/research/, one worker slot (~1). rb-2 is handed to this worker after rb-1 lands.
**Provenance:** decomposition v0.4 section 11a's AMGT-rb-1 row; the defect is C-S15 (r-1 future-price direction) per the CVO evidence @b3acbcf3dd and analysis s.3.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-2 analysis @c48576bf85 is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move (the passing sample and its pins do not move).
</preflight>
**Preflight disposition:** a source-logic + test correction to a landed module against landed data; no new gate/IAM/adversary/vendor plane; the authority is the L10 round-2 analysis.
