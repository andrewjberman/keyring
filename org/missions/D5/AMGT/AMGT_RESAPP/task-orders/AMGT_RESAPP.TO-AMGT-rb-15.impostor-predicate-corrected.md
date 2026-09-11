# AMGT_RESAPP.TO-AMGT-rb-15 -- THE IMPOSTOR PREDICATE, CORRECTED: the code enforces the stated truth table, verification is bound to company identity, and a must-fail negative control catches a repeat silent OR-not-AND no-op

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rb-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~5</issued_to>

## THE CELL, INLINED IN FULL (round 2b, FWD-14; fixes AMGT-r-15 / finding C-S14 FAIL)

```
AMGT-rb-15. THE IMPOSTOR PREDICATE, CORRECTED. AMGT-r-15's lib/research/lists/impostor.py ADVERTISES, in
its docstring, `official := (check1 OR check2) AND (any further evidence)`. The CODE does not enforce it:
`strong = check1 or check2; if strong: return official` -- so the "AND (any further evidence)" is UNMET, and
an 8-case enumeration ADMITS check2-alone (False,True,False -> official) and check1-alone. Worse, check2
("the platform's verification mark is present") is an untyped boolean NOT bound to COMPANY IDENTITY: a
verification mark that does not attest THIS company's identity, plus a copied bio, still passes. The CVO
graded it FAIL (C-S14): the two passing fixture arms do not establish real official-versus-impostor
discrimination. This predicate feeds the Coverage tab's social layer, so a silent OR-not-AND no-op is
higher-stakes than an ordinary regrade -- a repeat silent failure must be caught IN round-2b.

WHAT TO PRODUCE, under lib/research/lists/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~5/:

  (a) THE INTENDED TRUTH TABLE, STATED AND ENFORCED  clarify the INTENDED truth table and the identity
      meaning of "verification", and make the CODE enforce exactly the STATED contract (resolve the
      docstring-vs-code contradiction in favour of the stated rule -- require the co-occurrence where the
      rule intends it). BIND check2 to COMPANY IDENTITY: a verification mark that does not attest the
      company's own identity is NOT check2 (type it -- e.g. check2 becomes identity-bound, an untyped
      "verified" boolean is insufficient). Emit a machine-readable enumeration of every input combination ->
      verdict at deliverables/0.9.0_WK_AMGT_RESAPP~5/impostor_truth_table.json, each row tagged.

  (b) THE MUST-FAIL NEGATIVE CONTROLS, in tests/test_impostor.py  a test that MUST FAIL if the predicate
      ever silently reverts to the OR no-op:
        - the COPIED-BIO-ONLY impostor (only check3, no strong signal) is REFUSED as impostor -- the exact
          silent-failure case, named by the CTO (holes-scan tick 2 @f15af4dd7e);
        - VERIFICATION-WITHOUT-FURTHER-EVIDENCE: a bare verification mark with no company-identity binding
          does NOT admit official;
        - a MARK THAT DOES NOT ATTEST COMPANY IDENTITY plus a copied bio does NOT admit official.
      The difference arm: each control REFUSES where the OLD (round-2) code ADMITTED.

  (c) NO REAL HANDLE IS RESOLVED  the predicate stays a RULE over caller-supplied attributes; no handle in
      social_accounts.json is fetched, no vendor is called, no owner is assigned. Update the
      social_accounts.json schema/rule text to state the corrected contract.
```

## DEPENDENCIES

**NONE.** Independent of the other round-2b cells. Corrects AMGT-r-15's landed impostor.py and its tests;
reads AMGT-s-15's landed social_accounts.json.

## BOUNDS

```
BLOCK C-NO-CONTACT / NO VENDOR CALL: the predicate is a RULE over caller-supplied booleans/attributes; it
  fetches no handle, calls no social platform or vendor, and the two lists' OWNERS stay UNASSIGNED
  (Andrew's per-use word, round 3). AC3 refuses a network/vendor call in lib/research/lists/.
BLOCK ALL REAL HANDLES STAY UNRESOLVED: no handle in social_accounts.json is resolved or attested.
BLOCK CODE == STATED CONTRACT: the executed predicate matches its own docstring truth table exactly; a
  docstring that says AND while the code does OR is the defect and is refused (AC1/AC2).
BLOCK THE NEGATIVE CONTROL MUST FAIL IF THE BUG RETURNS: the copied-bio-only impostor is REFUSED; if the
  predicate reverts to admitting a weak/identity-blind signal, the control fails loudly (AC2).
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @b3acbcf3dd (C-S14, BLOCKING): "the implementation is strong = check1 or check2 and
    immediately returns official; it does not enforce the advertised AND with further evidence. Independent
    eight-case enumeration admits check2 alone and check1 alone ... a non-identity-bound verification mark
    plus copied bio still passes ... the caller contract never distinguishes identity-bound verification.
    (false,true,false) -> official and (false,false,true) -> impostor. Add negative controls for
    verification without further evidence and for a mark that does not attest company identity."
L10 round-2 analysis @c48576bf85 s.2 + CTO holes-scan tick 2 @f15af4dd7e: "clarify the intended truth
    table and the identity meaning of verification; require the co-occurrence where intended ... carry a
    negative control that MUST fail -- an impostor account passing ONLY check-3 -- so a repeat silent
    failure is caught in round-2b, not after."
AMGT-r-15 (landed): impostor.py evaluate_official_vs_impostor(check1,check2,check3); the docstring states
    the AND-clause; the code does check1 OR check2 -> official. tests/test_impostor.py is the difference arm.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/lists/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rb-15.impostor-predicate-corrected.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~5/` (where AMGT-r-15's social_accounts.json
lives). A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot satisfy
as written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W5-S<k>` continuing your prior sequence --
your next is `AMGT_RESAPP-Z-W5-S2`, project AMGT_RESAPP, fabric site-z) and STOP on that criterion if you
need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rb-15"><invocation>python -m pytest lib/research/lists/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- AMGT-r-15's tests still pass PLUS the new negative controls: the copied-bio-only impostor is REFUSED, a bare verification mark without company-identity binding does NOT admit official, and a mark not attesting company identity + a copied bio does NOT admit official. A predicate that admits any of these fails a test and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rb-15"><invocation>python -c "import json; t=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/impostor_truth_table.json')); rows=t if isinstance(t,list) else t.get('rows',[]); import re; low=json.dumps(t).lower(); copied_bio_only=[r for r in rows if str(r.get('label','')).lower().find('only')>=0 and 'check3' in str(r.get('label','')).lower()]; official_on_weak=[r for r in rows if str(r.get('verdict','')).lower()=='official' and str(r.get('label','')).lower().find('identity')>=0 and str(r.get('label','')).lower().find('not')>=0]; print('rows', len(rows), '| copied-bio-only verdicts', sorted({str(r.get('verdict','')).lower() for r in copied_bio_only}), '| any official-on-non-identity', len(official_on_weak))"</invocation><expect>a non-empty "rows" count, "copied-bio-only verdicts ['impostor']" (the must-fail control: only check3 is REFUSED as impostor, never official/unresolved-admitted), and "any official-on-non-identity 0" (no identity-blind verification is admitted official). A copied-bio-only row verdict of 'official', or any official-on-non-identity, is the C-S14 defect and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rb-15"><invocation>python -c "import pathlib,re; fs=list(pathlib.Path('lib/research/lists').rglob('*.py')); pat=re.compile(r'(?i)\b(requests\.|urllib\.request|httpx|aiohttp|socket\.|boto3|brightdata|twitter\.com|x\.com|linkedin\.com|api\.)'); hits=[str(f) for f in fs if pat.search(f.read_text(encoding='utf-8'))]; print('py files', len(fs), '| network/vendor-call files', len(hits), hits)"</invocation><expect>"network/vendor-call files 0" with a non-zero "py files" denominator -- NEGATIVE: the predicate resolves no handle and calls no platform or vendor; it is a pure rule over caller-supplied attributes</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rb-15" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): the tests, including the must-fail negative controls, pass -- a silent OR-not-AND revert is caught.
- **AC2** (mechanical, the must-fail control as data): the truth table shows the copied-bio-only impostor is REFUSED and no identity-blind verification is admitted official -- the exact C-S14 holes.
- **AC3** (mechanical, NEGATIVE): no network/vendor call; the predicate is a pure rule.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): read the corrected predicate and its truth table -- does it genuinely discriminate an official account from an impostor (verification bound to company identity, co-occurrence required where intended), rather than admit on the weakest or the identity-blind signal? This is the C-S14 regrade.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2b</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.4 + L6 round 2b) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-2 analysis @c48576bf85 (answering CVO slug REMEDIATION_v2 @b3acbcf3dd) + CTO holes-scan tick 2 @f15af4dd7e -> L5 recut decomposition v0.4 @192c198231 (section 11, AMGT-rb-15) -> this round-2b issuance.
**Chain:** round 2b, an independent chain of one.
**Provenance:** decomposition v0.4 section 11a's AMGT-rb-15 row; the defect is C-S14 (r-15 predicate OR-not-AND, identity-blind verification) per the CVO evidence @b3acbcf3dd; the must-fail control is the CTO's refinement msg 21322.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-2 analysis @c48576bf85 is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move (a pure rule + tests).
</preflight>
**Preflight disposition:** a logic + contract + test correction to a landed module; no new gate/IAM/adversary/vendor plane; the authority is the L10 round-2 analysis + the CTO's holes-scan refinement.
