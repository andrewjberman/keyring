# AMGT_RESAPP.TO-AMGT-rc-20 -- THE VINTAGE / DERIVATION IDENTITY: observation date and derivation identity are DISTINCT fields, the corrected artifact key is retained, and render_figure_line emits fig.source rather than a hardcoded vendor

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rc-20</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 4/v4, FWD-1/FWD-3; fixes AMGT-rb-2 / finding C-S20 OBSERVATION)

```
AMGT-rc-20. THE VINTAGE / DERIVATION IDENTITY. AMGT-rb-2's overlay collapsed three distinct provenance
facts. The CVO's control (C-S20): apply_corrected_price_overlay replaces `fig.vintage` with the price
OBSERVATION DATE (corrected.price_date, e.g. 2025-03-31) and DROPS the corrected artifact's derivation key
(derived/model_block_fye/<sec>/<stamp>/model_block_fye.json); render_figure_line HARDCODES "Bloomberg" and
never emits `fig.source` (which the overlay already sets to "... (fiscal-period join, model_block_fye)").
So the served figure cannot say WHICH corrected derivation produced it, and two derived vintages sharing one
observation date are indistinguishable. This is within rb-2's own named-vintage acceptance -- not new vendor
work.

WHAT TO PRODUCE, under lib/research/provenance/ + lib/research/print/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) DISTINCT FIELDS  carry OBSERVATION DATE (the price_date the figure is as-of) and DERIVATION / LANDING
      IDENTITY (the exact corrected artifact key, or an equivalent immutable pin) as SEPARATE fields on the
      overlaid figure -- never one substituted for the other. Retain the corrected key through the named
      consumer (render_pack.load_model_block) and its provenance render (render_model_block).

  (b) render_figure_line EMITS THE SOURCE  render_figure_line renders `fig.source` (which the corrected
      overlay sets), never a hardcoded "Bloomberg" -- a figure whose source is the fiscal-period join reads
      as such; a plain Bloomberg figure still reads "Bloomberg" via its own source field.

  (c) THE VINTAGE TEST  a test DISTINGUISHING two derived vintages that share ONE observation date -- two
      model_block_fye derivations with the same price_date but different derivation stamps/keys render (or
      carry) DISTINCT derivation identities. A render that shows the same line for both fails this.
```

## DEPENDENCIES

**DEPENDS ON AMGT-rc-19 (landed).** rc-19 rewrites the same overlay functions (load/apply_corrected_price_
overlay) for the unresolved-row contract; this cell adds the vintage/derivation-identity fields on top, so
it is worked AFTER rc-19 lands (same worker slot ~1, second in the queue; its worktree is cut from the HEAD
carrying rc-19). Reads AMGT-r-1's landed derive_fye_fixed.py (the corrected key shape) and AMGT-rb-2's overlay.

## BOUNDS

```
BLOCK OBSERVATION DATE != VINTAGE != DERIVATION IDENTITY: three distinct provenance facts; never collapse
  any two. The corrected artifact key (or an immutable pin) is retained, not replaced by the price date.
BLOCK render_figure_line EMITS fig.source: no hardcoded vendor string; the source field is the carrier.
BLOCK STORE_CONTRACT rule 1: the overlay mutates only the in-memory dict; the original model_block on disk
  stays byte-unchanged; the corrected model_block_fye artifact is READ, never rewritten.
BLOCK NO NEW VENDOR CALL / within rb-2's named-vintage acceptance: reads only persisted local JSON.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @13ae38f3f89b (C-S20, OBSERVATION): "apply_corrected_price_overlay replaces fig.vintage with
    corrected.price_date; load_corrected_price_overlay returns fiscal rows only. render_figure_line hardcodes
    Bloomberg and does not emit fig.source. corrected_derived_key records derived/model_block_fye/
    BABA_US_Equity/<stamp>/model_block_fye.json; current_consumer.wired carries price_date and a generic
    model_block_fye tag, not that immutable key. Carry observation date and derivation/landing identity as
    distinct fields; retain the exact corrected key. Add a test distinguishing two derived vintages with the
    same observation date."
L10 round-3 analysis @38948db85c s.C-S20: "Carry observation date + derivation identity as DISTINCT fields;
    retain the corrected key through the consumer + provenance; add a test distinguishing two derived
    vintages at the same observation date."
AMGT-rb-2 (landed): apply_corrected_price_overlay sets fig.source but render_figure_line ignores it and
    hardcodes "Bloomberg"; fig.vintage is overwritten with price_date. derive_fye_fixed.py writes the
    corrected key derived/model_block_fye/<sec>/<stamp>/model_block_fye.json.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/provenance/
lib/research/print/
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rc-20.vintage-derivation-identity.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence, project AMGT_RESAPP, fabric site-z) and STOP on that
criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rc-20"><invocation>python -m pytest integrations/bloomberg/research/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- the existing consumer/unresolved tests still pass PLUS a NEW test distinguishing two derived vintages that share ONE observation date: two model_block_fye derivations with the same price_date but different derivation keys/stamps carry (or render) DISTINCT derivation identities. A test where both collapse to the same line is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rc-20"><invocation>python -c "import importlib.util as u; s=u.spec_from_file_location('rp','lib/research/provenance/render_print.py'); m=u.module_from_spec(s); s.loader.exec_module(m); fig={'value':132.23,'unit':'USD','mnemonic':'PX_LAST','basis':{'mnemonic':'PX_LAST','definition':'last price'},'vintage':'20260911T073934Z','observation_date':'2025-03-31','source':'fiscal-period join (model_block_fye)','derivation_key':'derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json'}; line=m.render_figure_line(fig); print('emits source', ('fiscal-period join' in line or 'model_block_fye' in line), '| not hardcoded-only Bloomberg', ('Bloomberg' not in line) or ('model_block_fye' in line), '| carries observation date', ('2025-03-31' in line))"</invocation><expect>"emits source True" (render_figure_line renders fig.source, so the fiscal-period-join source appears) AND "not hardcoded-only Bloomberg True" (a non-Bloomberg source is not overridden to Bloomberg) AND "carries observation date True" (the observation date 2025-03-31 appears distinct from the derivation identity) -- the line carries observation date and derivation source as distinct facts. A line that still hardcodes Bloomberg over the source is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rc-20"><invocation>python -c "import importlib.util as u; s=u.spec_from_file_location('rp','lib/research/provenance/render_print.py'); m=u.module_from_spec(s); s.loader.exec_module(m); line=m.render_figure_line({'value':1,'unit':'x','basis':{'mnemonic':'M','definition':'d'},'vintage':'v','source':'TEST-SRC-XYZ'}); print('renders the given source', 'TEST-SRC-XYZ' in line, '| does not force Bloomberg', 'Bloomberg' not in line)"</invocation><expect>"renders the given source True" AND "does not force Bloomberg True" -- NEGATIVE: a figure whose source is TEST-SRC-XYZ renders that source and is NOT overridden to a hardcoded "Bloomberg". A line still hardcoding "Bloomberg" is the C-S20 defect and is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rc-20" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): two derived vintages at one observation date are distinguishable -- the derivation identity is carried, not collapsed into the observation date.
- **AC2** (mechanical): a corrected figure's rendered line carries the observation date AND the derivation source as distinct facts.
- **AC3** (mechanical, NEGATIVE): render_figure_line emits fig.source, never a hardcoded vendor.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): are observation date and derivation identity distinct, the corrected artifact key retained through the consumer and provenance, so a reader can tell which corrected derivation produced a served figure and two vintages at one observation date apart? This completes C-S16 with rc-19.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.5 + L6 round 4) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-3 analysis @38948db85c (answering CVO slug REMEDIATION_v3 @13ae38f3f89b, finding C-S20) -> L5 recut decomposition v0.5 @06d72ff757 (section 12, AMGT-rc-20) -> this round-4 issuance.
**Chain:** round 4 (v4), the SECOND of a two-cell chain (AMGT-rc-19 -> AMGT-rc-20), one worker slot (~1); worked AFTER rc-19 lands (its worktree is cut fresh from the HEAD carrying rc-19).
**Provenance:** decomposition v0.5 section 12a's AMGT-rc-20 row; the finding is C-S20 (rb-2 collapses observation date/vintage/derivation identity and hardcodes the source) per the CVO evidence @13ae38f3f89b.
> **NOTE (2.0.0_SA_COO~ZZZ, CTO ruling @21343).** rc-20 stays its own fix (distinct from rc-19's class-level qualification rule). Frame it as EXTENDING S3's provenance vintage/source handling (render_print.py IS the S3 provenance render) -- carry observation date + derivation identity as distinct fields and emit fig.source -- rather than minting a bespoke field. Keep it separate from rc-19.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-3 analysis @38948db85c is the authority.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act; provenance fields change (flagged to the CVO); no .tsx served, no served key moves.
</preflight>
**Preflight disposition:** a provenance/consumer correctness fix to landed modules; no new gate/IAM/adversary/vendor plane; depends on rc-19; the authority is the L10 round-3 analysis.
