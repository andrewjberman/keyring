# AMGT_RESAPP.TO-AMGT-rc-19 -- THE UNRESOLVED-ROW CONTRACT: a fiscal figure whose corrected price is UNRESOLVED is MARKED or REFUSED, never silently left as the old calendar price wearing a trusted face

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rc-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 4/v4, FWD-1/FWD-3; fixes AMGT-rb-2 / finding C-S19 FAIL)

```
AMGT-rc-19. THE UNRESOLVED-ROW CONTRACT. AMGT-rb-2 wired the served pack's consumer to overlay AMGT-r-1's
corrected model_block_fye fiscal-period price onto each fiscal-year PX_LAST figure -- but only where the
corrected price is non-None. The CVO's control (C-S19, BLOCKING) found the hole: lib/research/provenance/
render_print.py `load_corrected_price_overlay` keeps only rows whose price is not None, and
`apply_corrected_price_overlay` `continue`s on a missing year -- so an UNRESOLVED corrected fiscal row
(AMGT-rb-1's fix now returns None for a future-only price) is DROPPED, and the consumer SILENTLY keeps the
OLD calendar-year price (BABA FY2025 146.58) UNMARKED, presented as trusted. Measured control: a fiscal
join of period_end 2025-03-31 with only a 2025-04-02 price returns price/date/gap None; the loader returns
{}; the render then retains 146.58 with no unresolved marker. C-S16 stays OPEN until this end-to-end
contract holds.

WHAT TO PRODUCE, under lib/research/provenance/ + lib/research/print/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) PRESERVE UNRESOLVED ROWS  load_corrected_price_overlay must PRESERVE a corrected row that exists for a
      fiscal year but carries price None (UNRESOLVED) -- distinct from a year the corrected lane does not
      cover at all. The three states must be distinguishable downstream: (i) resolved corrected price,
      (ii) corrected lane present-but-UNRESOLVED for this year, (iii) corrected lane absent for this year.

  (b) MARK OR REFUSE, NEVER SILENTLY KEEP  apply_corrected_price_overlay (and render_model_block) must, for
      state (ii), MARK or REFUSE the fiscal figure -- the calendar price may remain in source storage but
      NEVER silently regains trusted presentation. For state (iii) the original figure renders as before
      (no corrected lane = no claim). For state (i) the corrected price overlays as today.

  (c) THE END-TO-END TEST  a test that drives a FULL corrected-join None output (the CVO control:
      period_end 2025-03-31, only a 2025-04-02 price -> corrected None) straight through the NAMED consumer
      (render_pack.load_model_block / render_print.apply_corrected_price_overlay + render_model_block) to
      the RENDERED value, asserting the rendered fiscal line is MARKED/REFUSED and is NOT the bare stale
      146.58 trusted figure. Record the before(silent-keep)/after(marked) in unresolved_row_contract.result.md.
```

## DEPENDENCIES

**NONE for rc-19 itself.** (AMGT-rc-20, the vintage/derivation-identity cell, DEPENDS ON this cell -- same
consumer functions, same worker slot, queued after rc-19 lands.) Reads AMGT-r-1's landed fye_join /
model_block_fye lane and AMGT-rb-2's landed overlay (all at HEAD).

## BOUNDS

```
BLOCK STORE_CONTRACT rule 1: the overlay mutates only the IN-MEMORY dict; the original
  model_block_<security_key>.json on disk is NEVER opened for write, overwritten or aliased.
BLOCK NEVER SILENTLY KEEP A STALE CALENDAR PRICE: an UNRESOLVED corrected fiscal row is MARKED or REFUSED
  in the reading; it never renders as a bare trusted figure (that is the C-S19 defect).
BLOCK PRESERVE THE RESOLVED SAMPLE: BABA's resolved FY2025 still overlays to 132.23 @ 2025-03-31; a
  corrected-lane-absent figure still renders unchanged. Only the UNRESOLVED (present-but-None) case changes.
BLOCK NO NEW VENDOR CALL: the consumer reads only PERSISTED local JSON (no requests/urllib/socket/boto3/
  vendor import); AC3 refuses a network/vendor call in the consumer files.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @13ae38f3f89b (C-S19, BLOCKING): "unresolved_overlay_control: fiscal join of period_end
    2025-03-31 with only 2025-04-02 price returns price/date/gap None; loader returns {}; rendering then
    retains the original BABA FY2025 146.58 with no unresolved marker. load_corrected_price_overlay includes
    only rows whose price is not None; apply_corrected_price_overlay skips missing years. Preserve explicit
    unresolved corrected rows, distinguish missing lane/year from resolved data, and mark or refuse a fiscal
    price without valid corrected evidence."
L10 round-3 analysis @38948db85c s.C-S19: "MARK or REFUSE a fiscal price with no valid corrected evidence
    -- never silently keep the old calendar price. Test the named consumer from a full corrected-join None
    output straight through to the rendered value."
AMGT-rb-2 (landed): render_print.py load_corrected_price_overlay (filters price not None) + apply_corrected_
    price_overlay (continue on missing year); render_pack.py load_model_block imports both. render_print.py
    already carries an [UNRESOLVED UNIT] marker pattern for a different case (C-MARK-NOT-DEGRADE).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
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
  <criterion id="AC1" cell_refs="AMGT-rc-19"><invocation>python -m pytest integrations/bloomberg/research/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- the existing consumer-wiring tests still pass PLUS a NEW end-to-end test: a full corrected-join None output (period_end 2025-03-31, only a 2025-04-02 price -> corrected None) driven through the named consumer to the rendered value renders the fiscal figure MARKED/REFUSED, never the bare stale 146.58. A test that does not drive the None path end-to-end, or that still renders the bare calendar price, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rc-19"><invocation>python -c "r=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/unresolved_row_contract.result.md', encoding='utf-8').read(); low=r.lower(); print('names the None control', ('2025-03-31' in r and 'none' in low), '| shows MARKED/REFUSED outcome', ('mark' in low or 'refus' in low), '| not the bare 146.58', ('146.58' in r), '| distinguishes missing-lane from unresolved', ('missing' in low and 'unresolved' in low))"</invocation><expect>"names the None control True" AND "shows MARKED/REFUSED outcome True" AND "not the bare 146.58 True" (the doc cites 146.58 as the OLD silent-keep value it no longer presents as trusted) AND "distinguishes missing-lane from unresolved True" -- the result doc demonstrates the unresolved corrected row is marked/refused and the three states (resolved / present-but-unresolved / lane-absent) are distinguished. A missing element is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rc-19"><invocation>python -c "import pathlib,re; fs=[pathlib.Path('lib/research/provenance/render_print.py'), pathlib.Path('lib/research/print/render_pack.py')]; fs=[p for p in fs if p.exists()]; pat=re.compile(r'(?i)\b(requests\.|urllib\.request|httpx|aiohttp|socket\.|boto3|brightdata|blpapi|dapi|api\.)'); hits=[str(p) for p in fs if pat.search(p.read_text(encoding='utf-8'))]; print('consumer files', len(fs), '| network/vendor-call files', len(hits), hits)"</invocation><expect>"network/vendor-call files 0" with a non-zero "consumer files" denominator -- NEGATIVE: the consumer reads only persisted local JSON and renders; it makes no network or vendor call</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rc-19" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, end-to-end difference arm): the None corrected row is driven through the real consumer to the render and comes out marked, not the stale calendar price.
- **AC2** (mechanical): the result doc demonstrates the three states distinguished and the unresolved row marked/refused, not silently kept.
- **AC3** (mechanical, NEGATIVE): the consumer makes no network/vendor call.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): does the end-to-end contract hold -- an UNRESOLVED corrected fiscal row is marked or refused (never silently the old calendar price), with missing-lane distinguished from resolved? This is the C-S19 regrade; C-S16 closes only when it holds (with rc-20).

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.5 + L6 round 4) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-3 analysis @38948db85c (answering CVO slug REMEDIATION_v3 @13ae38f3f89b, finding C-S19) -> L5 recut decomposition v0.5 @06d72ff757 (section 12, AMGT-rc-19) -> this round-4 issuance.
**Chain:** round 4 (v4), the FIRST of a two-cell chain (AMGT-rc-19 -> AMGT-rc-20), one worker slot (~1); rc-20 handed after rc-19 lands.
**Provenance:** decomposition v0.5 section 12a's AMGT-rc-19 row; the defect is C-S19 (rb-2's overlay silently keeps the stale calendar price on an unresolved corrected row) per the CVO evidence @13ae38f3f89b.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-3 analysis @38948db85c is the authority.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act; the consumer's rendered figures change (flagged to the CVO) but no .tsx is served and no served key moves.
</preflight>
**Preflight disposition:** a consumer-code correctness fix to landed modules against landed data; no new gate/IAM/adversary/vendor plane; the authority is the L10 round-3 analysis.
