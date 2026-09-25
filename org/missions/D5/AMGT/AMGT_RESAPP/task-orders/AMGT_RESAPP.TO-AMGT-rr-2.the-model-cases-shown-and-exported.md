# AMGT_RESAPP task order -- `AMGT-rr-2` -- THE MODEL CASES, SHOWN ON THE PAGE AND IN THE EXPORT, AND GRADED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rr-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~160</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the check READS the model-block store and the deployed function through the box's own credentials; it grants nothing.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is R-8's: a check that passes over every SERVED value. AC2 is the control that the new CASES grade can fail. Blind spot, stated: the page change lands on portal DEV only; the deployed page is not promoted.
EGRESS CLASS, declared: ONE AWS READ SURFACE for the check -- reads of Opal's own model-block store; no S3 write, no vendor, no server.
</preflight>

## 1. THE CELL -- `AMGT-rr-2` (round 43, decomposition s.51)

Row `AMGT_RESAPP-Z-S281`: on a SERVED case block the rich export prints "Upside / Base / Downside cases: SERVED -- the payload
carries no case block". **The page prints the same line:** `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` `CasesBlock` reads
only `model_cases.status` and `.reason`, never `base`, `upside` or `downside`. The served payload carries `status: SERVED`, three
case objects and no top-level `reason`, so both surfaces hide a served base (RKT_LN_Equity: base SERVED 7386.63 against px_last
4923, ratio 1.50) behind a contradiction. Equality passes because both are wrong the same way. **Three limbs, one cell:**

1. **The page.** `CasesBlock` renders EACH case the payload carries: a SERVED case shows its value and the formula it states; an
   ABSENT case shows its own reason (e.g. `currency_mismatch`, `forward_eps_not_positive`, `outside_band`, "methodology to be
   discussed with Andrew"). The top-level line no longer claims "no case block" over a block that exists.
2. **The export.** `lib/research/print/render_pack.py` `_model_cases_markdown` writes the SAME per-case lines the page renders,
   byte-identical wording, with unit tests in `lib/research/print/tests/`.
3. **The instrument (R-8).** `portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` GRADES the Model Cases block:
   it prints a `CASES page=N rich=N same=N missing=N extra=N` line over the case values and reasons, and `EXPORT-COMPARE OK` also
   requires CASES missing 0 and extra 0. You are its named `POD_DE_ANY` writer.

The check reads round 43's fixed capture (`C:/tmp/amgt-r43-cache`, outside the repository) through
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/sweep.py` (`--only KEY,...` while you work).

## 2. BOUNDS

1. **No server; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
2. **No other surface.** You change no other page file, not `build_pack` (the pdf path), and no data. A class you cannot close
   inside these files is a row, not a rescue. Never bend the product to fit the instrument.
3. **Do not refresh the cache.** `C:/tmp/amgt-r43-cache` is the fixed page. Portal files commit inside `portal/` on
   `wk-AMGT_RESAPP-160-portal`, then the outer commit. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~160/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rr-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-2.AC1.sh; echo "exit=$?"</invocation><expect>local rebuild over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0; cases over 89 of 89 compared names with missing=0 extra=0 and page greater than 0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rr-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-2.AC2.sh; echo "exit=$?"</invocation><expect>THE CASES AXIS CAN FAIL: harness on the cut's served body: rc=1 (the control needs 1) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rr-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-2.AC3.sh; echo "exit=$?"</invocation><expect>tsc -b --noEmit exit=0 -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rr-2" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-2.AC4.sh; echo "exit=$?"</invocation><expect>the rebuilt export's Model Cases section for RKT, ULVR and BA, for a person to judge beside the Model tab's case block whether each case says what the payload holds; RECORDED, no verdict</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~160/AMGT_RESAPP.TO-AMGT-rr-2.the-model-cases-shown-and-exported.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 items 3 and 4 in one cell: the harness is what proves the page and export fix. SERVED: the export change reaches the served body at rr-3; the page change reaches portal DEV only. The issuer's real run on 5174 reads the Model tab at the close. Print tests run as drain hygiene (three mechanical criteria).

<status>complete</status>
<round>43</round>
<slot>~160</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
