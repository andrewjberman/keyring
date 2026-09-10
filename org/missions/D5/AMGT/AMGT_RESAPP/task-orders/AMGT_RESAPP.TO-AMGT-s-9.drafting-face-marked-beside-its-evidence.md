# AMGT_RESAPP.TO-AMGT-s-9 -- THE DRAFTING FACE: generated prose visibly MARKED, every sentence beside its evidence, the verbatim gate machine-checked -- the producer stubbed behind an interface until a word names a model

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~3</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-9; manifest row S9; verb: wire; the one APPLIED bar)

```
AMGT-s-9. THE DRAFTING FACE -- generated prose visibly MARKED, each sentence beside the evidence it was
drawn from; the verbatim gate (an exact normalised substring of the fetched text, else rejected and
regenerated) is machine-checked, never trusted. Proceeds on `AMGT-s-1` figures and `AMGT-s-4` evidence;
SA evidence joins when `AMGT-s-b4` lands.

FWD-9's bar, verbatim: "Machine-written prose is never mistaken for a firm view. DONE WHEN APPLIED --
the marking is in place and sits beside the evidence the sentence was drawn from. ACCEPT: An analyst can
tell at a glance which sentences a machine wrote and which the firm owns, and the machine-written ones
sit next to the evidence behind them. They are a starting point someone edits, not a finished claim."
THE ONLY APPLIED BAR OF THE FOURTEEN: it is a property of the built artifact, and this cell can meet it.

ANDREW'S RULING ON LIMB ORDER (brief O9): the AI drafts Adam's FIVE LIMBS first -- company description
(with segments), investment thesis, risks, CEO bio, and the recommendation -- and summarises the
evidence second.

⛔ THE PRODUCER IS A MODEL CALL AND A MODEL IS A VENDOR API. No word names a model for this project,
so this order STUBS the producer behind an interface and exercises everything else on fixtures. The
marking, the evidence binding and the verbatim gate are the APPLIED property; the model behind the
interface is a later order with the word.

WHAT TO PRODUCE, under lib/research/drafting/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~3/:

  (a) THE MARKING CONTRACT  lib/research/drafting/schema.json -- drafted_sections.json: [{section: one
      of the five limbs, sentences: [{text, generated: true, evidence: [item_id|figure_id, ...],
      verbatim_check: PASS|REFUSE, quoted_spans: [...]}]}]. REQUIRED: generated (always true for machine
      text), evidence (non-empty), verbatim_check. A sentence with empty evidence is INVALID.

  (b) THE VERBATIM GATE (C-VERBATIM-GATE)  lib/research/drafting/verbatim.py -- every quoted span in a
      sentence must be an exact NORMALISED substring of the source text it cites (normalisation stated
      in the docstring: whitespace collapsed, case folded, curly quotes straightened, nothing else); a
      span that is not -> REFUSE the sentence, which the pipeline REGENERATES rather than ships. The
      estate proved this form on ASTN_WSJFT; transfer it, do not loosen it.

  (c) THE PRODUCER INTERFACE  lib/research/drafting/producer.py -- draft(section, evidence) ->
      sentences, with ONE implementation at this cut: FixtureProducer, which returns hand-written
      sentences from a fixture file so the pipeline runs end to end. Its docstring states: "the model
      producer requires Andrew's per-use word naming the model (G-24); not wired by AMGT-s-9".

  (d) THE PIPELINE, exercised on one security AMGT-s-1 landed: evidence = its figures (from
      model_block_*.json) + AMGT-s-4's coverage_items for that key (if landed) -> FixtureProducer ->
      verbatim gate -> drafted_sections.json for the five limbs, every sentence marked and bound.

  (e) SPEC_SECTION_drafting.md for AMGT-s-5: the visual marking (what "at a glance" looks like), the
      evidence beside the sentence, the edit affordance.
```

## DEPENDENCIES

`AMGT-s-1` (figures) and `AMGT-s-4` (evidence). Same slot (~3), third in `AMGT-s-12 -> AMGT-s-4 ->
AMGT-s-9`; continue on the same context. SA evidence from `AMGT-s-b4` joins if landed.

## BOUNDS -- what this cell may not cross

```
⛔ G-24 / C-VENDOR-EGRESS: NO MODEL CALL. No API key read, no model host, no SDK import for a hosted
model. The FixtureProducer is the only producer. AC4 refuses a model client in the module.
⛔ C-VERBATIM-GATE: a non-verbatim span is REFUSED and the sentence regenerated; it is never shipped
with a warning. AC1 exercises both arms.
⛔ A VALUE MUST CARRY ITS CLAIM: generated=true on every machine sentence; a sentence without evidence
is invalid, not "unsourced".
⛔ C-NO-CONTACT: the five limbs are drafted toward Adam's editorial judgment, never sent to him.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD s.3 C-VERBATIM-GATE: "wherever output quotes a source, the quoted text must be an exact normalised
    substring of the fetched text; non-verbatim is rejected and regenerated. This is a GATE, not
    trust-the-model, it is machine-checkable, and the estate has already proved the form."
brief O9: the AI drafts the five limbs first, then summarises the evidence; the template is a FLOOR
    (pre-brief notes s.3.1) -- the analyst-specific sections are where the judgment lives.
AMGT-s-1's model_block_*.json and AMGT-s-4's coverage_items_*.json (landed): the evidence ids your
    sentences bind to; a sentence citing an id that does not resolve is INVALID (AC2).
comp-schedule (RUN): 25 gates armed, none this project's; G-24 binds this cell.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/drafting/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-9.drafting-face-marked-beside-its-evidence.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~3/`. Sibling deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W3-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-9"><invocation>python -m pytest lib/research/drafting/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- (1) the verbatim gate REFUSES a span that paraphrases its source; (2) it ADMITS the same sentence once the span is an exact normalised substring (the difference arm); (3) a sentence with empty evidence fails schema validation; (4) the pipeline on the fixture yields exactly the five limbs as sections</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-9"><invocation>python -c "import json,glob; d=json.load(open(glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/drafted_sections_*.json')[0])); ids=set(); [ids.update(json.load(open(f)).get('figure_ids',[])) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_*.json')]; [ids.update(i['item_id'] for i in json.load(open(f))['items']) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/coverage_items_*.json')]; S=[s for sec in d['sections'] for s in sec['sentences']]; print('sections', len(d['sections']), '| sentences', len(S), '| all generated=true', all(s['generated'] for s in S), '| all evidence resolves', all(s['evidence'] and all(e in ids for e in s['evidence']) for s in S), '| verbatim REFUSE shipped', sum(1 for s in S if s['verbatim_check']=='REFUSE'))"</invocation><expect>"sections 5", "all generated=true True", "all evidence resolves True", "verbatim REFUSE shipped 0" -- every machine sentence is marked, bound to evidence that exists, and no refused sentence reached the output (it was regenerated or dropped, never shipped); any False or a REFUSE count above 0 is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-9"><invocation>python -c "import io; t=io.open('lib/research/drafting/producer.py',encoding='utf-8').read(); print('producer declares the word it lacks', 'per-use word' in t and 'G-24' in t and 'not wired by AMGT-s-9' in t, '| FixtureProducer present', 'class FixtureProducer' in t)"</invocation><expect>"producer declares the word it lacks True | FixtureProducer present True" -- the interface exists, says on its face that no model is wired and why, and the fixture implementation drives the pipeline</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-9"><invocation>grep -r -c -i -E 'openai|anthropic|moonshot|kimi|bedrock|api_key|API_KEY|requests\.post|httpx' lib/research/drafting/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no model client, no key, no host under the module; the producer is a fixture until a word names a model</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-9"><invocation>git status --porcelain -- portal/ | grep -c -E '\.tsx$'</invocation><expect>exactly "0" -- NEGATIVE: no .tsx (C-DESIGN-SPEC-FIRST)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-9" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the gate refuses paraphrase and admits verbatim; the schema refuses unsourced prose; the five limbs are the sections.
- **AC2** (mechanical, read from the artifact): marked, bound, nothing refused shipped. The APPLIED bar, on the artifact.
- **AC3** (mechanical): the producer interface declares its missing word.
- **AC4**, **AC5** (mechanical, NEGATIVE): no model, no .tsx.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): read one drafted sentence beside its evidence as the spec section says it will render -- is it unmistakably a machine's starting point an analyst would edit, or does it read as the firm's view? And is the verbatim normalisation in the docstring tight enough that a near-quote could not slip through as "verbatim"?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>3</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-3 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q3, third in `AMGT-s-12 -> AMGT-s-4 -> AMGT-s-9`; also after `AMGT-s-1` (Q1's root); slot ~3 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim. The stubbed producer is G-24 applied to a cell whose engine is a model call: the APPLIED bar (marking beside evidence) is a property of the pipeline and is met without a model; the model is SURFACED in the drain-end read as a word Andrew has not given for this project.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; nothing this cell writes is in AWS
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library, fixtures and deliverables; no deployed resource changes and no vendor call.
