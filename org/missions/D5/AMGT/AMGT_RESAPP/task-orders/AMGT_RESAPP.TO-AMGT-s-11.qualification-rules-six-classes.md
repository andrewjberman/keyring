# AMGT_RESAPP.TO-AMGT-s-11 -- THE QUALIFICATION RULES: six classes, each naming the input that makes it refuse, each threshold arriving WITH its distribution or not at all

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~8</issued_to>

## THE CELL, INLINED IN FULL (outcomes FWD-10 and FWD-3; manifest row S11)

```
AMGT-s-11. THE QUALIFICATION RULES -- one per class (a figure, a peer, an identity, a news or social
item, a source, a generated sentence), each NAMING the input that makes it refuse and EXERCISING that
input. Each rule's cell PRODUCES the distribution its threshold is drawn from and states the threshold
in its own deliverable -- no threshold exists anywhere upstream and none is invented here.

FWD-10's bar, verbatim: "A figure that failed its check is visible as failed. DONE WHEN EXERCISED -- a
check has actually refused something and the refusal was seen on the page." FWD-3: "An analyst can
defend every number on the page in a meeting. DONE WHEN EXERCISED." This cell builds the rules the
check face (AMGT-s-10) renders; the EXERCISED bars are served by the page and are not claimed here.

⛔ NO QUALIFICATION THRESHOLD EXISTS ANYWHERE UPSTREAM AND NONE IS INVENTED HERE. The brief refused to
set one; the PRD refused for a different reason -- the estate has not measured the distributions any
threshold would be drawn against, and an unmeasured exact constant fails closed while looking
principled. THE INSTRUCTION TO THIS CELL: a rule carries a threshold ONLY when it also carries the
distribution that threshold was drawn from, as an artifact you produced. A rule whose distribution
cannot be produced at this cut carries NO threshold, is marked held_back, and its class is NOT
displayed until a later cell produces the distribution (C-RULE-MUST-EXIST: not shipped dark).

WHAT TO PRODUCE:

  (a) THE RULES MODULE  lib/research/rules/
      A registry RULES = {class_name: Rule} over EXACTLY the six classes
          figure, peer, identity, item, source, sentence
      where a Rule carries: qualify(input) -> {verdict: PASS|REFUSE|PROVISIONAL, reason, evidence};
      refusal_input (the NAMED input that makes it refuse -- a concrete fixture, never None);
      pass_input (a concrete fixture it admits); threshold (None, or a number); distribution (None, or
      the path of the artifact under (b) the threshold was drawn from); held_back (True whenever
      threshold is None). PROVISIONAL is the third state: "we do not know" is never folded into PASS.

      The six rules' questions (brief III-B, verbatim):
        figure    is this the field we meant, on the basis we meant, from the vintage we meant?
        peer      is this comparable to THIS company -- and by what test?
        identity  is this SA symbol / IR domain / social account the same company as this Bloomberg ticker?
        item      is this ABOUT the security, or does it merely contain the string?
        source    is this publisher admissible -- and who decided?
        sentence  is every factual claim in it traceable to an admitted item?

  (b) THE DISTRIBUTIONS YOU CAN PRODUCE AT THIS CUT  .../deliverables/0.9.0_WK_AMGT_RESAPP~8/distributions/
      TWO classes have their data on this device already; produce their distributions and draw the
      threshold FROM them, stating the drawing rule:
        peer_overlap.json -- over every *ONE PAGER*.xlsx in the research corpus (READ-ONLY, outside
          the repo: C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research\),
          read the CSC sheet, extract Bloomberg-format tickers, and score each workbook's overlap with
          the KPN telecom set (KPN, Vodafone, BT, Orange, Telenor, Telekom Austria, Rogers, Telus,
          Swisscom, AT&T, Verizon, Telefonica). The distribution is the histogram of overlap counts
          with its denominator (workbooks found). The peer rule's threshold is drawn from the GAP in
          that histogram between the stale population and the genuine one; state the gap.
        figure_units.json -- over the CRO's measured field map
          (org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_BLOOMBERG_FIELD_MAP_20260910.md,
          measured on ONE security): the distribution of unit conventions and sign inversions across
          the mapped fields. The figure rule has NO numeric threshold; its refusal is categorical --
          a figure whose unit or sign status is not MEASURED is REFUSED -- and the distribution is what
          shows why (F4: absolute vs millions vs percent vs decimal, one sign inverted).
      FOUR classes have no data at this cut (item, source, sentence need fetched content, an allowlist,
      generated text; identity needs the resolver). Each carries its rule, its refusal fixture, its
      pass fixture, threshold None, distribution None, held_back True, and a `produced_by` field naming
      the cell whose deliverable will supply the distribution (item: AMGT-s-4/-b4/-13; source:
      AMGT-s-15; sentence: AMGT-s-9; identity: AMGT-s-12).

  (c) THE TESTS  lib/research/rules/tests/  runnable as `python -m pytest lib/research/rules/tests -q`
      Exactly TWELVE tests: for each of the six rules, one test that its refusal_input REFUSES and one
      that its pass_input PASSES -- the same rule, engaged and disengaged, in one harness (the
      difference arm). Plus the two invariants below as assertions inside the module's own import-time
      self-check, not as extra tests.

  (d) THE INVARIANTS, mechanical:
        every rule with threshold is not None also has distribution is not None
        every rule with threshold is None has held_back True
```

## DEPENDENCIES

**NONE.** No cell precedes it. Two cells wait on it: AMGT-s-10 (the check face renders these verdicts)
and AMGT-s-13 (the social feed is admitted by the item rule). Land it and they become cuttable.

## BOUNDS -- what this cell may not cross

```
⛔ NO THRESHOLD WITHOUT ITS DISTRIBUTION (PRD s.3, C-RULE-MUST-EXIST / C-CHECK-MUST-REFUSE). AC3 refuses a
module in which any rule carries a number it did not draw from an artifact you produced.

⛔ C-CHECK-MUST-REFUSE: every rule NAMES the input that makes it refuse and that input is RUN. A rule
whose refusal case was reasoned rather than exercised has not been tested. AC1 and AC2 together are
that bar.

⛔ C-SHARED-DEFECT: the peer distribution is the UNSCOPED pass over the population -- the pass that would
have caught a telecom set on 48 non-telecoms. Do not reduce it to a per-workbook check.

⛔ G-24 / C-VENDOR-EGRESS: NO VENDOR CALL. The item rule's distribution needs fetched content and this
order carries no word to fetch any; the class is held_back. No Bright Data, no Seeking Alpha, no HTTP
client in the module (AC5).

⛔ THE CORPUS IS READ-ONLY. Read the CSC sheets; write nothing into the library; copy no workbook into
the repo -- only the counts you derive.

⛔ A VALUE MUST CARRY ITS CLAIM: PASS | REFUSE | PROVISIONAL, never a bare boolean. A consumer rejects on
the verdict field.

⚠ BOUND EVERY READ. Each invocation runs under `timeout 120`; reading the CSC sheets of ~54 workbooks
with openpyxl (read_only=True, data_only=True, one sheet) fits; loading whole workbooks may not.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F6 (CITED): 48 of 54 workbooks carry the KPN telecom set; 4 own; 2 no CSC. Method in
    org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_LAMBDAS_PEERS_IRSCAN_20260910.md s.2. Your
    peer_overlap.json is the re-measurement as a DISTRIBUTION; AMGT-s-12 re-measures the same population
    as a partition. Two cells, two shapes, one corpus -- agreement is a finding for the drain.

F4 (CITED): the field map measured on SAP GY Equity -- CUR_MKT_CAP absolute while NET_DEBT/CURR_ENTP_VAL
    are millions; EQY_SH_OUT_REAL absolute while IS_SH_FOR_DILUTED_EPS is millions; margins percent
    where the workbook holds decimals; CAPITAL_EXPEND's sign inverted. The figure rule's refusal input
    is a figure whose unit_status is not MEASURED.

PRD s.3 C-VERBATIM-GATE: the sentence rule's shape is already proven on this estate -- an exact
    normalised substring of the fetched text, else REFUSE. Its refusal fixture is a sentence that
    paraphrases; its pass fixture is a verbatim one. No generated text exists yet; held_back.

comp-schedule (RUN to completion): 25 gates armed, none this project's; G-24 binds this cell.
comp-iam (RUN): no AWS resource touched by this cell.
Interpreter: `python` on PATH = Python311 with openpyxl and pytest importable (measured at the cut).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/rules/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-11.qualification-rules-six-classes.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~8/`, inside the granted prefix. The corpus
under OneDrive and the CRO's deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W8-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-11"><invocation>python -m pytest lib/research/rules/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "12 passed" with no "failed" and no "error" -- six rules, each REFUSING its named input and PASSING its pass input in one harness; fewer than twelve means a rule lacks one arm, and any failure means a rule does not refuse what it names</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-11"><invocation>python -c "from lib.research.rules import RULES; print('rules', len(RULES), 'classes', sorted(RULES), 'with a named refusal input', sum(1 for r in RULES.values() if r.refusal_input is not None), 'with a pass input', sum(1 for r in RULES.values() if r.pass_input is not None))"</invocation><expect>"rules 6 classes ['figure', 'identity', 'item', 'peer', 'sentence', 'source'] with a named refusal input 6 with a pass input 6" -- exactly the six classes brief III-B names, every one carrying both fixtures; a seventh class, a missing class, or a None fixture is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-11"><invocation>python -c "from lib.research.rules import RULES; a=[k for k,r in RULES.items() if r.threshold is not None and r.distribution is None]; b=[k for k,r in RULES.items() if r.threshold is None and not r.held_back]; print('thresholds without a distribution', len(a), '| unthresholded rules not held back', len(b))"</invocation><expect>"thresholds without a distribution 0 | unthresholded rules not held back 0" -- NEGATIVE and structural: no number was invented, and no class ships dark; a rule either carries its distribution artifact or is held back, and there is no third state</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-11"><invocation>python -c "import json; d=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/distributions/peer_overlap.json')); h=d['histogram']; print('peer overlap over', d['denominator'], 'workbooks; bins', len(h), 'sum', sum(h.values()), '| threshold', d['threshold'], 'drawn by:', d['drawing_rule'][:60])"</invocation><expect>a line in which "sum" EQUALS the denominator (every workbook found is in exactly one bin), the denominator is the count the script FOUND (not 54 copied from the brief), and "threshold" is a number followed by a non-empty drawing rule that names the gap in the histogram it was drawn from; a threshold with no drawing rule, or a sum that does not match, is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-11"><invocation>grep -r -c -i -E 'brightdata|seekingalpha\.com|/api/v3/|requests\.get|urllib\.request|httpx' lib/research/rules/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: no file under the module names a vendor host, the SA API path, or an HTTP client; the item class is held back precisely because this order has no word to fetch anything (G-24)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-11" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): every rule refuses what it names and admits what it names, engaged and disengaged in one harness -- the difference arm the spine requires of a control.
- **AC2** (mechanical): exactly the six classes, exactly two fixtures each. The domain is declared and MECE.
- **AC3** (mechanical, NEGATIVE, structural): no invented number, no dark class. The single bar this project's L1, L2 and L4 all refused to let slip.
- **AC4** (mechanical, a census): the one threshold that CAN be drawn at this cut arrives with its distribution, its denominator and its drawing rule. A threshold that arrives without its distribution is not a threshold.
- **AC5** (mechanical, NEGATIVE): no vendor host, no HTTP client.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): are the six refusal inputs REAL -- the kind of input the page will actually see (a figure with an inferred unit; a KPN set on a non-telecom; a paraphrase; an aggregator posing as IR) -- rather than strawmen a rule refuses trivially? And is the peer threshold's drawing rule one a reader would draw the same way from the same histogram?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- read one sheet per workbook, read_only.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>1</round>
<slot>~8</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q8, the root of `AMGT-s-11 -> AMGT-s-10`; slot ~8 drains that queue.
**Provenance:** the cell text is the decomposition's row verbatim. The two-distributions-now / four-held-back split is this issuer's reading of what data exists on this device at the cut: the corpus and the CRO's field map are here; fetched items, an allowlist, generated text and a resolver are other cells' outputs. held_back with produced_by is C-RULE-MUST-EXIST's "held back from the page" made a field a consumer can read.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, C1=23 C2=6 C3=12 C4=20 C5=335, 25 gates armed, none this project's; G-24 bound onto this cell
comp-iam: RUN -- 195 TF roles / 188 services / 167 Lambda / 21 EC2 / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors, DESIRED plane; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; nothing this cell reads or writes is in AWS
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library module, tests and JSON deliverables; no deployed resource changes.
