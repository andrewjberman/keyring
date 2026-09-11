# AMGT_RESAPP.TO-AMGT-r-15 -- THE IMPOSTOR AND-CLAUSE: the official-vs-impostor test requires the weak check (3) to CO-OCCUR with a strong check (1 or 2), so a copied bio alone no longer admits

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-r-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~5</issued_to>

## THE CELL, INLINED IN FULL (round 2, FWD-14; fixes AMGT-s-15's AC6 FAIL)

```
AMGT-r-15. THE IMPOSTOR AND-CLAUSE. AMGT-s-15's official-vs-impostor test is a bare OR of three unequal
checks, so an impostor beats the WEAKEST: a copied "official account of <domain>" bio admits on check
(3) alone. The remedy the L10 analysis names: require check (3) (the bio / self-description, the
weakest and most forgeable) to CO-OCCUR with check (1) OR check (2) (the stronger signals -- e.g. a
verified badge, a link FROM the company's own IR domain), so no account is deemed official on the
forgeable check alone.

WHAT TO PRODUCE, under lib/research/lists/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~5/:

  (a) THE AND-CLAUSE  in the official-vs-impostor test carried by social_accounts.json's schema AND the
      predicate that evaluates it: official := (check1 OR check2) AND (any further evidence); check3
      ALONE is NOT sufficient -- it may only strengthen a result that already has check1 or check2.
      State the three checks and the AND-clause in the schema, precisely enough to apply without
      re-derivation.

  (b) THE DIFFERENCE, EXERCISED  two fixtures: an IMPOSTOR account passing ONLY check (3) (the copied
      bio) is REFUSED; an OFFICIAL account passing check (3) AND (check1 OR check2) is ADMITTED. The
      refuse-then-admit pair is the whole point.
```

## DEPENDENCIES

**NONE.** Independent. Reads AMGT-s-15's landed lists module and social_accounts.json.

## BOUNDS

```
⛔ THE AND-CLAUSE IS THE FIX, NOT A NEW OWNER: the two lists' owners stay UNASSIGNED (C-NO-CONTACT --
Andrew names them; this cell does not).
⛔ G-24: NO VENDOR CALL, NO social lookup, NO HTTP fetch -- the test is a RULE over an account's
attributes, exercised on FIXTURES; no handle is resolved live. AC3.
⛔ NOTHING IS ADMITTED OR MEASURED for a real account by this order -- the fix is to the TEST; the map's
handles stay UNRESOLVED (their content awaits a vendor word, AMGT-s-13's).
⛔ A VALUE MUST CARRY ITS CLAIM: the test returns official|impostor|unresolved with its reason, never a
bare boolean.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
L10 analysis @4d31cf4caa s.2 (FWD-14): "the official-vs-impostor test is a bare OR of three unequal
    checks, so an impostor beats the weakest (a copied 'official account of <domain>' bio admits on
    check 3 alone). Remedy: require check (3) to CO-OCCUR with (1) or (2)".
AMGT-s-15 (landed): publishers.json / social_accounts.json with the official_vs_impostor_test in the
    schema, owner UNASSIGNED, the rot signal; PART V's "an impostor or fan account must be
    distinguishable from the official one".
comp-schedule (round 1): G-20 (no alarm) and G-24 bind s-15's family; neither is touched by a rule edit.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/lists/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-r-15.impostor-and-clause.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~5/`. AMGT-s-15's landed lists module is READ.
A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot satisfy as
written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W5-S<k>` continuing your sequence, project
AMGT_RESAPP, fabric site-z) and STOP on that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-r-15"><invocation>python -m pytest lib/research/lists/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- AMGT-s-15's original 2 rot tests still pass, PLUS the impostor pair: (1) an account passing ONLY check (3) (a copied "official account of &lt;domain&gt;" bio) is REFUSED as not-official; (2) an account passing check (3) AND (check1 OR check2) is ADMITTED official (the difference arm). A bare-OR test that admits the check-3-only impostor fails this and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-r-15"><invocation>python -c "import json; s=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/social_accounts.json')); t=json.dumps(s.get('official_vs_impostor_test','')); import re; print('states an AND-clause', bool(re.search(r'(check ?3|bio|self.?desc).*(co-?occur|AND|together with).*(check ?1|check ?2)|(check ?1|check ?2).*AND.*(check ?3)', t, re.I)), '| check3-alone insufficient stated', 'alone' in t.lower() or 'not sufficient' in t.lower() or 'insufficient' in t.lower())"</invocation><expect>"states an AND-clause True | check3-alone insufficient stated True" -- the schema's official_vs_impostor_test text names the co-occurrence rule (check 3 must accompany check 1 or 2) and says check 3 alone is insufficient; a schema still describing a bare OR is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-r-15"><invocation>grep -r -c -i -E 'requests\.|urllib\.request|httpx|brightdata|api\.|twitter\.com|x\.com|linkedin\.com' lib/research/lists/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no HTTP client, no vendor host, no platform URL under the module; the test is a rule over attributes exercised on fixtures, not a live lookup (G-24)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-r-15" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): the check-3-only impostor is refused and the genuinely-official account is admitted.
- **AC2** (mechanical): the schema states the AND-clause so a later resolution applies it without re-deriving it.
- **AC3** (mechanical, NEGATIVE): no live lookup -- the fix is to the rule.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): is the AND-clause one that would actually separate a fan/impostor account from the company's own -- would a real copied-bio impostor be refused, and a real official account (verified or IR-linked) still admitted?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.3 + L6 round 2) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L10 round-1 analysis @4d31cf4caa -> L5 recut decomposition v0.3 @3d2d7af6e0 (section 10, AMGT-r-15) -> this round-2 issuance.
**Chain:** round 2, an independent chain of one.
**Provenance:** decomposition v0.3 section 10a's AMGT-r-15 row; the defect is s-15 AC6 FAIL and the L10 analysis s.2/s.4.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-20/G-24 bind s-15's family, neither touched by a rule edit.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 analysis @4d31cf4caa is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act.
</preflight>
**Preflight disposition:** a rule edit to a landed module exercised on fixtures; no new gate/IAM/vendor plane; the authority is the L10 analysis.
