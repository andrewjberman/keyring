# AMGT_RESAPP.TO-AMGT-s-8 -- THE PEER SET: comparable to THIS company, or ABSENT WITH A REASON -- never another company's list, never the corpus's stale sheet

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~4</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-8; manifest row S8; claim today: BROKEN)

```
AMGT-s-8. THE PEER SET -- comparable to THIS company, or absent with a stated reason. RE-MEASURES F6
FIRST (48 of 54 carrying another company's set) on the SharePoint corpus through the Opal gateway,
read-only; then a per-name rule PLUS one unscoped pass over the population -- the pass that would have
caught a telecom set on 48 non-telecoms.

FWD-8's bar, verbatim: "The comparison block is about the company on the page. DONE WHEN EXERCISED --
an analyst who distrusted it has stopped. ACCEPT: The list of comparable companies is genuinely about
the company being shown. Where a sensible comparison cannot be worked out, the page says so rather
than showing another company's list."

THE ONE MEASURED DEFECT OF THIS PROJECT: 48 of 54 one-pagers carry KPN's telecom comps -- on ASML,
AstraZeneca, BP, Boeing, Costco, Hermes and 42 others (F6). The corpus CANNOT be a source of truth for
peer sets (the CRO's s.2 consequence 1). Any feature that seeds peers from existing packs inherits
KPN's comps for 48 names.

WHAT TO PRODUCE, under lib/research/peers/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~4/:

  (a) F6 RE-MEASURED FIRST -- by RE-RUNNING AMGT-s-12's script, not by a third implementation:
        python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.py
      Record its output line verbatim in your deliverable with the time you ran it. That is the
      "re-measure first" the PRD asks of a cell that relies on F6; two cells have measured it and yours
      is the third read of the same instrument, which is corroboration only if it prints the same
      partition -- say whether it did.

  (b) THE PEER ENGINE  lib/research/peers/engine.py -- peers(security_key) -> peer_set.json:
        {security_key, basis: analyst|derived|absent, test: "<the comparability test, stated>",
         members: [...], reason: "<why absent, or how derived>", vintage}
      THE TEST, stated in code and in the deliverable: comparable = same Bloomberg industry subgroup
      AND a market-cap band the engine names (e.g. within 0.2x-5x of the subject). The engine reads
      the SUBJECT's classification from the record AMGT-s-1 landed (its header scalars include the
      classification fields the CRO mapped; read model_block.json, make NO new Bloomberg call).

  (c) THE HONEST OUTPUT AT THIS CUT: a DERIVED set needs a CANDIDATE UNIVERSE classified by subgroup.
      Classifying the 89 covered names is 89 unique securities on Bloomberg -- the quota decision the
      brief flags (F2: "the binding constraint is UNIQUE SECURITIES TOUCHED"; "the limit itself is
      unmeasured") -- and it is NOT this order's to spend. So for each of the securities AMGT-s-1
      landed, the engine emits basis: absent with reason "candidate universe not classified; a quota
      decision (F2) precedes derivation" -- WHICH IS THE OUTCOME'S OWN BAR: "where a sensible
      comparison cannot be worked out, the page says so rather than showing another company's list."
      An `analyst` basis is the path for a set a person enters: the engine accepts one and marks it.

  (d) THE UNSCOPED PASS (C-SHARED-DEFECT)  lib/research/peers/shared_defect.py: over every peer_set
      the engine has emitted in a run, REFUSE if any two subjects in different subgroups carry the same
      member set (the F6 shape). Fixture: two non-telecoms handed KPN's set -> REFUSE, naming the pair
      and the shared set; two telecoms handed KPN's set -> ADMIT (the difference arm).

  (e) THE CORPUS IS NEVER A SOURCE: the engine has no code path that reads a *.xlsx or a CSC sheet.
      AC5 refuses one.
```

## DEPENDENCIES

`AMGT-s-12` (the identity layer; and its f6_remeasure.py is the instrument you re-run). Reads
`AMGT-s-1`'s landed blocks for the subject's classification. Slot ~4 spawns after AMGT-s-12 lands.

## BOUNDS -- what this cell may not cross

```
⛔ F2 / G-24: NO NEW BLOOMBERG CALL and NO NEW SECURITY. The subject's classification is read from the
record AMGT-s-1 landed. Classifying a candidate universe is a quota decision that precedes this cell
and is Andrew's; the engine says "absent with reason" rather than spending it. AC6.
⛔ THE CORPUS IS NEVER A SOURCE OF PEERS. Read it only through AMGT-s-12's re-measure script (a); the
engine itself reads no workbook. AC5.
⛔ C-SHARED-DEFECT: the unscoped pass is not optional and not per-name.
⛔ C-IDENTITY-RESOLVED: a member of a derived set is named by the identity layer's key, never by a bare
name that could be another company.
⛔ A VALUE MUST CARRY ITS CLAIM: basis is analyst|derived|absent; never a list with no basis.
⛔ C-DESIGN-SPEC-FIRST: no .tsx. Deliver SPEC_SECTION_peers.md for AMGT-s-5.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F6 (CITED; re-measured by AMGT-s-12 and by AMGT-s-11's distribution): 48 stale / 4 own / 2 no-CSC of
    54; the 4 real sets are unmistakably JUDGMENT (Imperial Brands vs Japan Tobacco; Lenovo vs
    Asus/Acer). peers.basis is `analyst` when populated -- 7.4% of the time.
PRD s.6 (CITED, UNVERIFIED): whether the stale sheet reaches the PRINTED packs is not traced; do not
    conclude packs shipped wrong.
AMGT-s-1's field map (landed): the header scalars include industry classification mnemonics if the
    CRO mapped them; if the record carries none, the engine's `absent` reason says "subject
    classification not in the landed record" -- a finding, and a row.
comp-schedule (RUN): 25 gates armed, none this project's; G-24 binds this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/peers/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-8.peer-set-comparable-or-absent-with-a-reason.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~4/`. AMGT-s-12's and AMGT-s-1's deliverables
and the store are READ; the corpus is READ only through AMGT-s-12's script.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W4-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-8"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.py</invocation><expect>the "F6 RE-MEASURED: stale-set N / own-set M / no-CSC Z of D workbooks; vintage ..." line -- run by THIS worker, recorded verbatim in the deliverable beside AMGT-s-12's own output and a one-word verdict on whether the partition agrees; no run, or an unrecorded run, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-8"><invocation>python -m pytest lib/research/peers/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- (1) the shared-defect pass REFUSES two non-telecom subjects carrying KPN's set and names the pair; (2) it ADMITS two telecom subjects carrying it (the difference arm); (3) an analyst-entered set is marked basis analyst; (4) a subject with no classification in its record yields basis absent with the stated reason</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-8"><invocation>python -c "import json,glob; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/peer_set_*.json'); ps=[json.load(open(f)) for f in fs]; print('peer sets', len(ps), '| bases', sorted(set(p['basis'] for p in ps)), '| every set carries test+reason', all(p.get('test') and p.get('reason') for p in ps), '| any absent without reason', any(p['basis']=='absent' and not p.get('reason') for p in ps))"</invocation><expect>"peer sets" at least 3 (one per security AMGT-s-1 landed), every basis from the closed set analyst|derived|absent, "every set carries test+reason True", "any absent without reason False" -- the page will SAY why a comparison is absent rather than show another company's list</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-8"><invocation>python -c "import json,glob; kpn={'KPN','VOD','BT','ORA','TEL','TKA','RCI','T','SCMN','VZ','TEF'}; hits=0; [ (hits:=hits+(1 if kpn &amp; set(m.split()[0] for m in p.get('members',[])) and p['basis']!='analyst' else 0)) for p in (json.load(open(f)) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/peer_set_*.json'))]; print('derived or absent sets carrying a KPN telecom ticker', hits)"</invocation><expect>"derived or absent sets carrying a KPN telecom ticker 0" -- NEGATIVE: the stale set did not reach any non-analyst output; if a subject genuinely is a telecom, its analyst-basis set is exempt by construction and the derived path is not exercised at this cut</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-8"><invocation>grep -r -c -i -E 'openpyxl|\.xlsx|xlrd|CSC' lib/research/peers/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE and structural: the engine has no code path into a workbook; the corpus is never a source of peers</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-8"><invocation>grep -r -c -i -E 'blpapi|blp_client|ReferenceDataRequest|8194' lib/research/peers/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no Bloomberg call from this cell; the subject's classification is read from the landed record and the candidate universe is a quota decision that is not spent here</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-s-8" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): F6 re-measured first, by the instrument that already exists, and its agreement stated.
- **AC2** (mechanical): the shared-defect pass refuses the F6 shape and admits its legitimate twin; the analyst and absent paths work.
- **AC3** (mechanical): every output carries basis, test and reason. "Says so" is a field.
- **AC4**, **AC5**, **AC6** (mechanical, NEGATIVE): KPN's set reached nothing; no workbook path; no Bloomberg call.
- **AC7** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): read one `absent` peer set -- is the reason one an analyst would accept on the page ("not derivable until the universe is classified") rather than a blank, and is the comparability test stated precisely enough that a second engineer would derive the same set from the same classified universe when the quota word comes?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q4, `AMGT-s-8` alone; slot ~4 spawns after `AMGT-s-12` lands.
**Provenance:** the cell text is the decomposition's row verbatim. The "absent with reason at this cut" shape is this issuer's reading of F2: a derived set needs a classified universe, classifying it is the quota decision the brief names as unmeasured and Andrew's, and the outcome's own ACCEPT names "says so" as the correct output when a comparison cannot be worked out. The quota decision is SURFACED in the drain-end read.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource beyond reading the store
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; the engine reads the store and a sibling's deliverable
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library and deliverables; no deployed resource changes.
