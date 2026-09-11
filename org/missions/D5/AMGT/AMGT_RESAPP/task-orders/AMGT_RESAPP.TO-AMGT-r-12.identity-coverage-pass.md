# AMGT_RESAPP.TO-AMGT-r-12 -- THE IDENTITY COVERAGE PASS: resolve the UNRESOLVED tickers where a MEASURED source exists, and SURFACE the folder-name fallback as a design question rather than coding it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-r-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~4</issued_to>

## THE CELL, INLINED IN FULL (round 2, FWD-8/FWD-13; fixes AMGT-s-12's 57 UNRESOLVED residual)

```
AMGT-r-12. THE IDENTITY COVERAGE PASS. After W7-S3's remediation the identity layer is 32 MEASURED /
32 distinct / 57 UNRESOLVED (of 89) -- honest, not a regression, but four surfaces hang off it and the
coverage is thin. Resolve the UNRESOLVED tickers WHERE A LEGITIMATE MEASURED SOURCE EXISTS, and SURFACE
the folder-name fallback (the SAP-GY-style placeholder case) as an identity-layer DESIGN QUESTION for
Andrew -- do NOT code the fallback (the L10 analysis: "an identity-layer design question, not a
mid-cell edit").

WHAT TO PRODUCE, under lib/research/identity/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~4/:

  (a) THE COVERAGE PASS  extend build_universe.py (or a pass beside it) to resolve an UNRESOLVED
      bloomberg_ticker to MEASURED ONLY from a legitimate source: (i) the sa_ids AMGT-s-b4 landed
      (sa_ids.json -- the SA symbol confirms the identity for those tickers); (ii) a workbook cell that
      carries the SUBJECT'S OWN ticker and is NOT the shared template placeholder (a value shared by 2+
      folders stays downgraded per W7-S3's AC7 pass); (iii) a coverage-universe cross-reference if one
      exists on this device. Each newly-MEASURED cell names its source in evidence. Regenerate
      universe.json.

  (b) THE UNSCOPED PASS STILL HOLDS: no MEASURED value is shared by two or more folders (AC7 from
      round 1) -- resolving must not re-introduce a shared placeholder. distinct == MEASURED still.

  (c) THE DESIGN QUESTION, WRITTEN NOT CODED  in the deliverable (DESIGN_QUESTION_identity_fallback.md):
      state the folder-name INFERRED fallback precisely -- what it would infer (e.g. "SAP GY" folder ->
      "SAP GY Equity" ticker), its confidence, its failure mode (an ambiguous or renamed folder), and
      the trade-off (coverage gained vs. a value that carries an INFERRED not MEASURED claim). This is
      for Andrew to decide; the cell does NOT implement it (AC3 refuses a folder-name-to-ticker
      inference in the code).

  (d) THE RESIDUAL, PRINTED  a per-name line for every still-UNRESOLVED folder with its reason (no
      workbook / placeholder-only / ex-US name with no measured source), summing to the residual count.
```

## DEPENDENCIES

**NONE among the round-2 cells.** Reads AMGT-s-b4's sa_ids.json (landed), the research corpus (READ-ONLY),
and its own universe.json (landed). Independent of AMGT-r-4.

## BOUNDS

```
⛔ NO FOLDER-NAME FALLBACK CODED. The fallback is the design question; it is WRITTEN for Andrew, never
implemented in this cell. AC3 refuses a folder-name-to-ticker inference in the module.
⛔ A VALUE MUST CARRY ITS CLAIM: a newly-resolved ticker is MEASURED only if read from a real source
named in evidence; otherwise it stays UNRESOLVED. Never INFERRED-dressed-as-MEASURED.
⛔ THE AC7 UNSCOPED PASS HOLDS: no MEASURED value shared by 2+ folders (resolving must not re-introduce
a placeholder). distinct == MEASURED.
⛔ G-24: NO NEW VENDOR CALL. Resolve from landed artifacts (sa_ids, workbooks, the corpus) only.
⛔ THE CORPUS IS READ-ONLY. Read it; write nothing into the OneDrive library.
⚠ Bound every read under `timeout 120`; read one sheet per workbook where a workbook read is needed.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
W7-S3 (round 1, remediated): 16 template-placeholder "AAPL US" values downgraded to UNRESOLVED; the AC7
    unscoped pass (no MEASURED value shared by 2+ folders) is the invariant that must survive this pass.
L10 analysis @4d31cf4caa s.2/s.4 (FWD-8/13): "the 57 UNRESOLVED residual remains (coverage, not a
    regression)"; "resolve the 57 UNRESOLVED; the folder-name fallback for the SAP-GY-style placeholder
    is an identity-layer design question, not a mid-cell edit".
AMGT-s-b4 (landed): sa_ids.json -- MEASURED sa symbols for BABA/RTX/+1, a legitimate identity source.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/identity/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-r-12.identity-coverage-pass.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~4/`. AMGT-s-b4's sa_ids.json, the corpus and
AMGT-s-12's landed identity module are READ.
A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot satisfy as
written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W4-S<k>` continuing your sequence, project
AMGT_RESAPP, fabric site-z) and STOP on that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-r-12"><invocation>python -c "import json,collections; u=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json')); m=[n['bloomberg_ticker']['value'] for n in u['names'] if n['bloomberg_ticker']['status']=='MEASURED']; c=collections.Counter(m); shared=[(v,k) for v,k in c.items() if k>1]; s=collections.Counter(n['bloomberg_ticker']['status'] for n in u['names']); print('MEASURED', len(m), '| distinct', len(c), '| shared', len(shared), '| partition', dict(s), 'of', u['denominator_folders'])"</invocation><expect>"MEASURED" GREATER THAN 32 (the coverage pass resolved at least one more from a legitimate source), "distinct" EQUAL to "MEASURED" and "shared 0" (the AC7 unscoped invariant holds -- no re-introduced placeholder), and the partition summing to the denominator (89); MEASURED still 32, or shared above 0, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-r-12"><invocation>python -c "import json; u=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json')); unres=[n for n in u['names'] if n['bloomberg_ticker']['status']=='UNRESOLVED']; print('UNRESOLVED', len(unres), '| every one carries a reason', all(n['bloomberg_ticker'].get('evidence') for n in unres), '| newly MEASURED cite a source', all(n['bloomberg_ticker'].get('evidence') for n in u['names'] if n['bloomberg_ticker']['status']=='MEASURED'))"</invocation><expect>"every one carries a reason True" and "newly MEASURED cite a source True" -- every still-UNRESOLVED folder states WHY (no workbook / placeholder-only / no measured source) and every MEASURED value names its evidence; a bare UNRESOLVED or an evidence-less MEASURED is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-r-12"><invocation>python -c "import io,glob; t=''.join(io.open(f,encoding='utf-8').read() for f in glob.glob('lib/research/identity/*.py')); dq=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/DESIGN_QUESTION_identity_fallback.md'); import re; coded=bool(re.search(r'folder[_ ]?name.*(->|to|infer).*ticker|infer.*ticker.*from.*folder', t, re.I)); print('folder-name fallback coded in module', coded, '| design question written', len(dq)==1)"</invocation><expect>"folder-name fallback coded in module False | design question written True" -- NEGATIVE and structural: the fallback is SURFACED for Andrew as a written design question, never implemented in the identity module; a folder-name-to-ticker inference in the code is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-r-12" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, a census): coverage rose from a legitimate source AND the no-shared-placeholder invariant survived.
- **AC2** (mechanical): every value carries its claim -- MEASURED names a source, UNRESOLVED names its reason.
- **AC3** (mechanical, NEGATIVE, structural): the folder-name fallback is Andrew's decision, written not coded.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): are the newly-MEASURED resolutions genuinely read from a real source (not an inference wearing MEASURED's name), and does DESIGN_QUESTION_identity_fallback.md state the trade-off well enough that Andrew could rule on the fallback without re-deriving it?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.3 + L6 round 2) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L10 round-1 analysis @4d31cf4caa -> L5 recut decomposition v0.3 @3d2d7af6e0 (section 10, AMGT-r-12) -> this round-2 issuance.
**Chain:** round 2, an independent chain of one.
**Provenance:** decomposition v0.3 section 10a's AMGT-r-12 row; the residual is W7-S3's remediation aftermath and the L10 analysis s.2/s.4.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-24 binds (no new vendor call).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 analysis @4d31cf4caa is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act.
</preflight>
**Preflight disposition:** a coverage pass over landed artifacts + a written design question; no new gate/IAM/vendor plane; the authority is the L10 analysis.
