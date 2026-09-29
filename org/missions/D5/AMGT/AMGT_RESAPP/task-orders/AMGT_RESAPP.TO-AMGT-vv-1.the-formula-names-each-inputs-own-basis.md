# AMGT_RESAPP task order -- `AMGT-vv-1` -- THE RULE'S VALUE IS A "HISTORICAL-MULTIPLE REFERENCE" WHOSE FORMULA NAMES EACH INPUT AS ITS BASIS OBJECT DOES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-vv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~168</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read committed fixtures; nothing reaches AWS. The served text reaches the Lambda at vv-4.
comp-adversary: RUN by the issuer at the cut -- AC1 pins the three served VALUES exactly, so a text edit that also moves a number FAILS; AC2 compares the page against the export over three case lines, so a relabel on one side only -- or a harness parser that stops seeing the relabelled line (it would read 2 lines, not 3) -- FAILS.
EGRESS CLASS, declared: NONE. No server, no fetch, no network, no Bloomberg call.
</preflight>

## 1. THE CELL -- `AMGT-vv-1` (round 47, decomposition s.55)

Two CTO rulings on the rule's served value (the adjusted consensus EPS x adjusted trailing-median P/E construction):

1. **The formula names each input as its basis object does** (round-46 analysis, ruling 1). The P/E input's `basis` names the
   adjusted construction; the EPS input's `basis` is the block's own `BEST_EPS` figure's basis -- Bloomberg's consensus definition
   -- and says nothing about "adjusted". The served `formula` becomes EXACTLY:
   `Bloomberg consensus EPS (FY1, BEST_EPS) x adjusted trailing-median P/E (PX_LAST / IS_COMP_EPS_ADJUSTED)`
   It lives in `lib/research/api/case_rule.py` (`BASE_FORMULA`, `:70`; used `:245`).
2. **The rule's value is RELABELLED "Historical-multiple reference" everywhere it is served or shown, never "Base case"**
   (the anchor ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_RESAPP_BASE_CASE_ANCHOR_20260929.md`, ruling 2 -- the
   team's own Base, where one exists, leads on the page; that ordering is another project's, not this cell's). Concretely:
   - the served `base` case object carries `"label": "Historical-multiple reference"` on EVERY branch (SERVED and every ABSENT,
     including `scoped_amgt._model_cases`'s own no-`cases` branch, `:2984-2993`); `upside`/`downside` stay the ruled ABSENT object,
     unlabelled; the payload key stays `base` and the `cases` list stays `["Upside", "Base", "Downside"]` (consumers key on it);
   - the export's case line (`lib/research/print/render_pack.py` `_model_case_line`, `:741-766`) and the page's
     (`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` `ModelCaseLine`, `:221-236`) print `<label>: <STATUS> -- <detail>` when
     the case carries a `label`, else `<Name> case: <STATUS> -- <detail>` as today -- identically on both sides (FWD-30 compares them
     byte for byte);
   - the export-compare harness's CASES parser (`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs`, `:389`,
     today `^(Upside|Base|Downside) case: (SERVED|ABSENT) -- .+$`) also admits the `Historical-multiple reference: ` line, so the
     Base line stays inside the compared set.
   The window, every value, every input object, every refusal and the band are unchanged. Update the tests that assert the old text.

## 2. BOUNDS

1. **Text and label only.** No number, input object, refusal branch or band changes; no other served key moves.
2. **No server; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/api/case_rule.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/**
lib/research/print/render_pack.py
lib/research/print/tests/**
integrations/bloomberg/research/tests/**
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~168/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; the fixtures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/fixtures/`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-vv-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-1.AC1.py; echo "exit=$?"</invocation><expect>THE RULE'S VALUE IS A LABELLED REFERENCE, FORMULA BASIS-TRUE, VALUES UNMOVED: 4 of 4 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-vv-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC2.py; echo "exit=$?"</invocation><expect>PAGE AND EXPORT PRINT THE SAME CASES: 2 of 2 names (each: harness rc=0; CASES page=3 rich=3 same=3 missing=0 extra=0) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-vv-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC3.sh; echo "exit=$?"</invocation><expect>all passed (no failed, no error) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the served text and label with the values pinned (three stored blocks + a no-cases block) and the export line; AC2 the page and the
export print the same THREE case lines; AC3 the case, export and producer-guard suites.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~168/AMGT_RESAPP.TO-AMGT-vv-1.the-formula-names-each-inputs-own-basis.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-46 analysis s.4 item 1 (ruling 1, @0e405cc330), widened at the cut by the CTO's anchor ruling 2 (msg
20260929T050711Z) -- one served-text pair. Base: AC1 FAIL (0 of 4: old formula, no label, "Base case" line), AC2 FAIL at portal DEV 5fac7a37
(the harness does not load the redesigned page -- vv-5 fixes it first on this worker), AC3 PASS. SERVED: reaches the Lambda at vv-4. Shares `scoped_amgt.py` with vv-2, which is spawned after
this order drains.

<status>pending</status>
<round>47</round>
<slot>~168</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
