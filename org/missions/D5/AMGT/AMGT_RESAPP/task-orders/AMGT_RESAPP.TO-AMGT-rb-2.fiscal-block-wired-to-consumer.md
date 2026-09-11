# AMGT_RESAPP.TO-AMGT-rb-2 -- THE FISCAL BLOCK, WIRED TO THE CONSUMER: name the provenance/print consumer that reads model_block and test that the served pack reads the CORRECTED model_block_fye lane, its own dedicated end-to-end criterion

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rb-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 2b, FWD-1/FWD-3; fixes AMGT-r-1 / finding C-S16 -- integration)

```
AMGT-rb-2. THE FISCAL BLOCK, WIRED TO THE CONSUMER. AMGT-r-1's derive_fye_fixed.py writes the corrected,
fiscal-period-joined block to a DISTINCT engine lane `derived/model_block_fye/` and explicitly EXCLUDED
replacing the original `model_block` artifacts or re-wiring the provenance/print consumers (STORE_CONTRACT
rule 1). The CVO's finding (C-S16): the provenance/print consumers still read the ORIGINAL `model_block`
lane, so the served analyst pack still reads the OLD calendar-year join -- r-1's fix is correct on the
sample but NOT YET the served figure. "Correct on a sample" and "connected end-to-end" are different
claims (CTO holes-scan tick 2 @f15af4dd7e); this cell closes the end-to-end gap and PROVES it with its own
acceptance criterion, never bundled into an underlying-correctness check.

WHAT TO PRODUCE, under integrations/bloomberg/research/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) NAME THE CONSUMER  identify the concrete provenance/print consumer path that reads `model_block` for
      the served analyst pack (search integrations/bloomberg/research/ and its consumers; name the module +
      function + the derived key it reads). Record it in consumer_integration.result.md.

  (b) WIRE IT TO THE CORRECTED LANE  make that consumer read the corrected `model_block_fye` derived lane
      (the smallest correct switch -- a parameter, a lane selector, or a read of the fye key), NEVER by
      overwriting or aliasing the original `model_block` artifacts (STORE_CONTRACT rule 1; derive_fye_fixed
      keeps writing the distinct `model_block_fye` engine). Depends on AMGT-rb-1 (the direction-corrected
      join) being landed first.

  (c) TEST IT END-TO-END, ITS OWN CRITERION  a test that NAMES the consumer and shows it reads the corrected
      lane and its derived vintage -- the difference arm: for BABA US Equity (FYE 31 March) the OLD
      `model_block` lane gives the calendar-year-end price and the corrected `model_block_fye` lane gives
      the fiscal-period-end price, and the WIRED consumer now returns the fiscal-period price. This is a
      SEPARATE acceptance from rb-1's underlying correctness -- end-to-end, not "correct on a sample".
```

## DEPENDENCIES

**DEPENDS ON AMGT-rb-1 (landed).** rb-1 corrects the fiscal join's direction; this cell wires the corrected
block to the consumer, so it is worked AFTER rb-1 lands (same worker slot ~1, this is the second order in
the queue). Reads AMGT-r-1's landed derive_fye_fixed.py / model_block_fye lane and the provenance/print
consumers (all at HEAD, including rb-1's landed fix).

## BOUNDS

```
BLOCK STORE_CONTRACT rule 1: NEVER overwrite or alias the original `model_block` artifacts or peer outputs;
  the corrected lane stays the DISTINCT `model_block_fye` engine. AC3 refuses an overwrite/alias.
BLOCK CONSUMER-WIRING IS ITS OWN ACCEPTANCE: name + test the consumer path and its derived vintage; do NOT
  fold it into an underlying-correctness check (CTO holes-scan tick 2). AC1/AC2 are the end-to-end proof.
BLOCK NO round-3 / .tsx: this wires the box-side served pack's join lane, not a UI surface.
BLOCK NO new vendor call: reads LANDED derived lanes; integrations/bloomberg/READ_HERE.md binds if any
  re-read is needed -- health first, NEVER a sign-in.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @b3acbcf3dd (C-S16, OBSERVATION re-cut as integration): "derive_fye_fixed.py writes
    derived/model_block_fye/. Worker 1 r-1 declared_exclusions explicitly excludes replacing model_block
    artifacts and wiring provenance/print consumers ... name and test the consumer path and its
    derived-artifact vintage before claiming the served analyst pack uses the corrected join. Do not
    overwrite peer outputs."
L10 round-2 analysis @c48576bf85 s.3 + CTO holes-scan tick 2 @f15af4dd7e: "make consumer-wiring its OWN
    acceptance criterion. 'Correct on a sample' and 'connected end-to-end' are different claims ... name +
    test the consumer path and its derived vintage, NOT bundle it into the underlying-correctness check."
AMGT-r-1 (landed): derive_fye_fixed.py ENGINE = model_block_fye (distinct lane); model_block_pull.py's
    model_block producer is the original lane; pull_consumer.py imports model_block_pull's stage functions.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rb-2.fiscal-block-wired-to-consumer.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path
you are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence, project AMGT_RESAPP, fabric site-z) and STOP on
that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rb-2"><invocation>python -m pytest integrations/bloomberg/research/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- the existing fye tests still pass PLUS a NEW consumer test: the named provenance/print consumer, when reading the corrected model_block_fye lane, returns the fiscal-period-end price for BABA and NOT the calendar-year-end price the original model_block lane gives (the end-to-end difference arm). A test that does not exercise the consumer, or does not show the lane difference, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rb-2"><invocation>python -c "import pathlib; r=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/consumer_integration.result.md', encoding='utf-8').read(); low=r.lower(); tf=[str(p) for p in pathlib.Path('integrations/bloomberg/research/tests').rglob('*.py') if 'model_block_fye' in p.read_text(encoding='utf-8')]; print('names a consumer module', ('.py' in low and 'consumer' in low), '| names model_block_fye', ('model_block_fye' in low), '| shows calendar-vs-fiscal', ('calendar' in low and 'fiscal' in low), '| a test reads the corrected lane', len(tf)>0)"</invocation><expect>all four True -- consumer-wiring as its OWN criterion: the result doc NAMES the concrete consumer module, names the corrected model_block_fye lane, shows the calendar-vs-fiscal difference for the wired consumer, and at least one test file reads the corrected lane. A missing element is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rb-2"><invocation>python -c "t=open('integrations/bloomberg/research/derive_fye_fixed.py', encoding='utf-8').read(); print('corrected lane is a distinct engine', ('model_block_fye' in t), '| original model_block not aliased in derive_fye_fixed', (t.count('ENGINE = \"model_block_fye\"') + t.count(chr(39)+'model_block_fye'+chr(39)) >= 1))"</invocation><expect>both True -- NEGATIVE: the corrected lane stays the DISTINCT model_block_fye engine and the original model_block artifacts are not overwritten or aliased (STORE_CONTRACT rule 1). If derive_fye_fixed no longer writes a distinct model_block_fye engine, it is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rb-2" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, end-to-end difference arm): the wired consumer returns the fiscal-period price for BABA, not the calendar-year price -- the served pack reads the corrected join.
- **AC2** (mechanical, consumer-wiring its OWN criterion): the consumer path is named and its corrected-lane read is tested, kept separate from underlying correctness (the CTO's refinement).
- **AC3** (mechanical, NEGATIVE): the corrected lane stays a distinct engine; the original model_block is not overwritten or aliased.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): does the served analyst pack now genuinely read the corrected fiscal join through the named, tested consumer path -- so C-S16 closes and the fiscal alignment can be claimed LIVE, not merely correct on a sample?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2b</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.4 + L6 round 2b) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-2 analysis @c48576bf85 (answering CVO slug REMEDIATION_v2 @b3acbcf3dd, finding C-S16) + CTO holes-scan tick 2 @f15af4dd7e -> L5 recut decomposition v0.4 @192c198231 (section 11, AMGT-rb-2) -> this round-2b issuance.
**Chain:** round 2b, the SECOND of a two-cell chain (AMGT-rb-1 -> AMGT-rb-2), one worker slot (~1); worked AFTER rb-1 lands (its worktree is cut fresh from the HEAD that carries rb-1's fix).
**Provenance:** decomposition v0.4 section 11a's AMGT-rb-2 row; the finding is C-S16 (r-1's corrected block not wired to consumers) per the CVO evidence @b3acbcf3dd and analysis s.3; consumer-wiring-as-its-own-AC is the CTO's refinement msg 21322.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-2 analysis @c48576bf85 is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act; wires a box-side derived-lane READ, moves no served key (the corrected lane already exists; this points a consumer at it).
</preflight>
**Preflight disposition:** an integration edit wiring a consumer to a landed derived lane, with a test; no new gate/IAM/adversary/vendor plane; depends on rb-1; the authority is the L10 round-2 analysis + the CTO's refinement.
