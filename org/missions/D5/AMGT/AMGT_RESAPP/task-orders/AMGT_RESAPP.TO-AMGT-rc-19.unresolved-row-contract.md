# AMGT_RESAPP.TO-AMGT-rc-19 -- THE UNRESOLVED-OVERLAY QUALIFICATION RULE (CLASS-LEVEL): a figure whose corrected fiscal overlay is UNRESOLVED is REFUSED/PROVISIONAL by the S11 figure rule, so S10 renders it marked -- never the stale calendar price, and never a bespoke per-consumer fallback

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rc-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 4/v4, FWD-1/FWD-3/FWD-10; fixes AMGT-rb-2 / finding C-S19 FAIL)

```
AMGT-rc-19. THE UNRESOLVED-OVERLAY QUALIFICATION RULE (CLASS-LEVEL). AMGT-rb-2's consumer overlays
AMGT-r-1's corrected model_block_fye fiscal-period price onto each fiscal-year PX_LAST figure -- but when
the corrected price is UNRESOLVED (None; AMGT-rb-1 now returns None for a future-only price) the overlay is
dropped and the consumer SILENTLY keeps the OLD calendar-year price (BABA FY2025 146.58) UNMARKED (C-S19,
BLOCKING). THE FIX IS CLASS-LEVEL, NOT BESPOKE (CTO ruling @21343; Rule 22 -- fix what the members SHARE):
the class "a figure whose corrected fiscal overlay is UNRESOLVED" is qualified by the S11 FIGURE RULE ->
REFUSE or PROVISIONAL, and S10's check-face renders it marked. Do NOT hand-write "don't silently fall back"
inside load_corrected_price_overlay -- that is a per-consumer bespoke instance the next consumer of a
corrected value would need re-written. A class-level rule covers ANY consumer automatically.

WHAT TO PRODUCE, under lib/research/rules/ + lib/research/checkface/ + lib/research/provenance/ +
lib/research/print/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE S11 FIGURE-RULE EXTENSION  extend lib/research/rules/figure.py's qualify() (or an
      appropriately-named figure sub-rule in lib/research/rules/) so the class "a figure carrying a
      corrected fiscal overlay that is UNRESOLVED (present-but-no-valid-corrected-price)" qualifies REFUSE
      or PROVISIONAL -- categorical, NAMING and EXERCISING its refusing input (C-CHECK-MUST-REFUSE, the
      AMGT-s-11 bound), never inventing a threshold. The figure carries a `corrected_overlay_status` field
      in {RESOLVED, UNRESOLVED, ABSENT} -- use exactly that field name so the class-level rule has one stable
      input contract -- and qualify() distinguishes the three states: RESOLVED -> PASS/overlaid, UNRESOLVED
      (corrected lane present-but-no-valid-price for this year) -> REFUSE or PROVISIONAL, ABSENT (corrected
      lane does not cover this year) -> the figure's own prior verdict (no corrected claim).

  (b) ROUTE THE CONSUMER THROUGH THE RULE  the provenance/print consumer (render_print.render_model_block /
      render_figure_line and render_pack.load_model_block) applies the S11 figure rule to each overlaid
      figure and renders the verdict with S10/AMGT-rb-10's SALIENT marker (a REFUSE/PROVISIONAL figure is
      unmistakable, never the bare stale value presented as trusted). The unresolved decision lives in the
      RULE, not in a bespoke branch of load_corrected_price_overlay.

  (c) THE CLASS-LEVEL, END-TO-END TEST  (1) the S11 figure rule, called DIRECTLY (no consumer), REFUSES/
      PROVISIONALs an unresolved-corrected figure and PASSes a resolved one -- proving the qualification is
      class-level and reusable by ANY consumer; (2) the CVO control (period_end 2025-03-31, only a
      2025-04-02 price -> corrected None) driven through the named consumer to the RENDERED value is MARKED
      (REFUSE/PROVISIONAL), never the bare 146.58. Record before(silent-keep)/after(marked) in
      unresolved_row_contract.result.md.
```

## DEPENDENCIES

**NONE for rc-19 itself.** (AMGT-rc-20 DEPENDS ON this cell -- same consumer, queued after rc-19 lands.)
Reads AMGT-s-11's landed lib/research/rules/ registry, AMGT-s-10/rb-10's landed lib/research/checkface/,
AMGT-r-1's corrected model_block_fye lane, and AMGT-rb-2's overlay (all at HEAD).

## BOUNDS

```
BLOCK CLASS-LEVEL, NOT BESPOKE (CTO ruling @21343, Rule 22): the unresolved-overlay qualification is an S11
  FIGURE RULE covering ANY consumer -- NEVER a hand-written keep-or-mark branch inside
  load_corrected_price_overlay. AC3 proves the rule refuses independent of any consumer.
BLOCK C-CHECK-MUST-REFUSE (AMGT-s-11): the rule NAMES and EXERCISES its refusing input; a rule whose refusal
  case is reasoned not run has not been tested. NO threshold is invented (the refusal is categorical).
BLOCK NEVER SILENTLY KEEP A STALE CALENDAR PRICE: an unresolved-corrected figure renders REFUSE/PROVISIONAL
  with the S10 marker; the calendar price may remain in source storage but never regains trusted presentation.
BLOCK PRESERVE THE RESOLVED SAMPLE: BABA's resolved FY2025 still overlays to 132.23; a corrected-lane-absent
  figure keeps its own prior verdict. STORE_CONTRACT rule 1: the original model_block on disk is byte-unchanged.
BLOCK NO NEW VENDOR CALL: the rule + consumer read only PERSISTED local JSON; no network/vendor call.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @13ae38f3f89b (C-S19, BLOCKING): "fiscal join of period_end 2025-03-31 with only 2025-04-02
    price returns price/date/gap None; loader returns {}; rendering then retains the original BABA FY2025
    146.58 with no unresolved marker. Preserve explicit unresolved corrected rows, distinguish missing
    lane/year from resolved data, and mark or refuse a fiscal price without valid corrected evidence."
CTO ruling @21343 (round 4): "fix C-S19 as an S11 QUALIFICATION RULE (class-level), NOT a bespoke consumer
    fallback -- the class 'a figure whose corrected-overlay is unresolved' -> S10 renders REFUSE or
    PROVISIONAL. A class-level rule covers ANY consumer automatically. Rule 22: fix what the members SHARE."
AMGT-s-11 (landed): lib/research/rules/figure.py qualify(fig) returns Verdict(PASS|REFUSE|PROVISIONAL) on
    unit_status; the registry pattern (Rule.qualify, named refusal_input/pass_input). AMGT-rb-10 (landed):
    lib/research/checkface/ renders a distinct, LEADING salient marker per verdict. AMGT-rb-2 (landed):
    render_print.load/apply_corrected_price_overlay (drops price-None rows / continues on missing year).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/rules/
lib/research/checkface/
lib/research/provenance/
lib/research/print/
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rc-19.unresolved-row-contract.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence -- your next is `AMGT_RESAPP-Z-W1-S7`, project
AMGT_RESAPP, fabric site-z) and STOP on that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rc-19"><invocation>python -m pytest lib/research/rules/tests integrations/bloomberg/research/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- the existing rule + consumer tests still pass PLUS: (1) a figure-rule test where an UNRESOLVED-corrected figure qualifies REFUSE or PROVISIONAL and a resolved one PASSes; (2) an end-to-end test where the CVO control (period_end 2025-03-31, only a 2025-04-02 price -> corrected None) through the named consumer renders MARKED, never the bare 146.58. A test that renders the stale calendar price unmarked is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rc-19"><invocation>python -c "r=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/unresolved_row_contract.result.md', encoding='utf-8').read(); low=r.lower(); print('names the None control', ('2025-03-31' in r and 'none' in low), '| renders MARKED not stale', (('refuse' in low or 'provisional' in low or 'mark' in low) and '146.58' in r), '| via the S11 figure rule', ('figure' in low and ('rule' in low or 'qualif' in low)), '| three states distinguished', ('resolved' in low and 'unresolved' in low and ('missing' in low or 'absent' in low)))"</invocation><expect>all four True -- the result doc shows the CVO None control rendered MARKED (REFUSE/PROVISIONAL, not the bare 146.58 presented as trusted), the qualification made by the S11 FIGURE RULE (class-level), and the three states (resolved / present-but-unresolved / lane-absent) distinguished. A missing element is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rc-19"><invocation>python -c "import importlib.util as u; s=u.spec_from_file_location('fr','lib/research/rules/figure.py'); m=u.module_from_spec(s); s.loader.exec_module(m); v=m.qualify({'field':'PX_LAST','value':146.58,'unit_status':'MEASURED','corrected_overlay_status':'UNRESOLVED'}); print('rule verdict on unresolved-corrected figure', v.verdict, '| not PASS', v.verdict != 'PASS')"</invocation><expect>"not PASS True" with the verdict REFUSE or PROVISIONAL -- NEGATIVE + CLASS-LEVEL: the S11 FIGURE RULE itself, called DIRECTLY with no consumer, refuses/holds an unresolved-corrected figure (the exact figure that was silently passing). This proves the fix is a class-level rule reusable by any consumer, not a bespoke consumer branch. A verdict of PASS is the C-S19 defect and is NOT met. The refusing input is the figure's `corrected_overlay_status: UNRESOLVED` (the stable field the cell mandates), exercised here directly on the rule per C-CHECK-MUST-REFUSE</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rc-19" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): the rule + end-to-end tests pass -- unresolved-corrected renders marked, resolved overlays, stale price never shown unmarked.
- **AC2** (mechanical): the result doc demonstrates the None control rendered marked via the S11 figure rule, three states distinguished.
- **AC3** (mechanical, NEGATIVE + class-level, Rule 22): the S11 figure rule alone (no consumer) refuses the silently-passing figure -- proving the fix is class-level, not bespoke.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): is this a genuine CLASS-LEVEL S11 qualification rule (covers ANY consumer of a corrected value, per the CTO ruling @21343 / Rule 22) rather than a bespoke per-consumer fallback, and does S10 render the unresolved figure REFUSE/PROVISIONAL (never the stale calendar price)? C-S19 closes; C-S16 closes with rc-20.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.5 + L6 round 4) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-3 analysis @38948db85c (answering CVO slug REMEDIATION_v3 @13ae38f3f89b, finding C-S19) + CTO round-4 ruling @21343 (S11-not-bespoke, Rule 22) -> L5 recut decomposition v0.5 @06d72ff757 (section 12, AMGT-rc-19) -> this round-4 issuance.
**Chain:** round 4 (v4), the FIRST of a two-cell chain (AMGT-rc-19 -> AMGT-rc-20), one worker slot (~1); rc-20 handed after rc-19 lands.
**Provenance:** decomposition v0.5 section 12a's AMGT-rc-19 row; C-S19 per the CVO evidence @13ae38f3f89b; the class-level S11 framing per the CTO ruling @21343.
> **AMENDMENT 1 (2.0.0_SA_COO~ZZZ, CTO ruling @21343 folded in before rc-19 was worked).** The first cut framed C-S19 as a bespoke fix inside load_corrected_price_overlay and granted only the consumer homes. The CTO ruled (round 4): fix it as an S11 QUALIFICATION RULE (class-level -- the "corrected-overlay unresolved" figure class -> S10 REFUSE/PROVISIONAL), NOT a per-consumer fallback (Rule 22: fix what the members share; a bespoke fix is the next-consumer gap the CRO's holes-scan flagged). This amendment reframes WHAT TO PRODUCE + the criteria to the S11-rule approach and adds lib/research/rules/ + lib/research/checkface/ to <paths>. The prior spawn (bespoke) was stopped before it landed anything; re-cut on a fresh worktree from the amended HEAD.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-3 analysis @38948db85c + CTO ruling @21343 are the authority.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act; the consumer's rendered figures change (flagged to the CVO); no .tsx served, no served key moves.
</preflight>
**Preflight disposition:** a class-level qualification-rule fix (S11) + consumer routing (S10), to landed modules against landed data; no new gate/IAM/adversary/vendor plane; the authority is the L10 round-3 analysis + the CTO round-4 ruling.
