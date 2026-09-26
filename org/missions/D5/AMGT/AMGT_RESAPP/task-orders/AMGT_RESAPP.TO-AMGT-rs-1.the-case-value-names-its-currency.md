# AMGT_RESAPP task order -- `AMGT-rs-1` -- THE CASE VALUE NAMES ITS CURRENCY, ON THE PAGE AND IN THE EXPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rs-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~161</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the checks READ a fixed capture outside the repository; nothing reaches AWS.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a currency guessed rather than read: AC1 requires the name's own CRNCY, read off the same payload the page reads, and a case whose own quote_currency disagrees is a row. Blind spot, stated: the page change lands on portal DEV only.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-rs-1` (round 44, decomposition s.52)

The Model tab and the rich export now print a SERVED case as "Base case: SERVED -- 7386.63633 (consensus EPS (FY1) x trailing-median
P/E)" -- a value with NO currency, beside a Price tile quoted in GBp. **Make every SERVED case name its currency, on the page and in
the export, byte-identical:**

1. **The currency is the price's.** The served guard admits a base only inside [0.33, 3.0] of the name's own `px_last`, so the case is
   in the unit of that price. The page's Price tile prints that unit from the header figure `CRNCY` (`overlay.header_figures`,
   mnemonic `CRNCY`). Write the case as `<value> <CRNCY>` -- e.g. "Base case: SERVED -- 7386.63633 GBp (consensus EPS ...)".
2. **Never guess.** Of 48 SERVED cases at this capture, 45 carry no `quote_currency` and 3 carry `GBp`. Where a case carries its own
   `quote_currency` and it DISAGREES with `CRNCY`, or `CRNCY` is absent, the case prints no currency and you file a row -- you do not
   choose between them.
3. **Both surfaces.** `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (`ModelCaseLine` / `modelCaseDetail`) and
   `lib/research/print/render_pack.py` (`_model_case_line`), with unit tests in `lib/research/print/tests/`. The harness
   (`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs`) keeps grading the case lines; if its CASES
   extraction needs to learn the currency token, you are its named `POD_DE_ANY` writer.

The checks read round 44's fixed capture (`C:/tmp/amgt-r43-live95`, outside the repository: the LIVE research library, 95 folders, read
at 2026-09-26T03:55:02Z) through `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/sweep.py`.

## 2. BOUNDS

1. **No server; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
2. **No other surface.** No other page file, not `build_pack` (the pdf path), no data. Never bend the product to the instrument.
3. **Do not refresh the cache.** Portal files commit inside `portal/` on `wk-AMGT_RESAPP-161-portal`, then the outer commit. Python
   from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~161/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rs-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/rs-1.AC1.py; echo "exit=$?"</invocation><expect>served cases carrying their price currency: 48 of 48 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rs-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/rs-1.AC2.sh; echo "exit=$?"</invocation><expect>local rebuild over 95 of 95 folders: OK 95, NOT_OK 0, CAPTURE_FAILED 0; cases over 95 of 95 compared names with missing=0 extra=0 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rs-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/rs-1.AC3.sh; echo "exit=$?"</invocation><expect>tsc -b --noEmit exit=0 -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rs-1" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/rs-1.AC4.sh; echo "exit=$?"</invocation><expect>the rebuilt export's Model Cases section for RKT, AMD and GOOGL, for a person to judge beside the Model tab whether each served value reads as a price in a named currency; RECORDED, no verdict</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~161/AMGT_RESAPP.TO-AMGT-rs-1.the-case-value-names-its-currency.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.4 item 1 (the slug's own recommendation). SERVED: the export change reaches the served body at rs-2; the page change reaches portal DEV only. AC1's 48 is the count at the fixed capture; a case withheld under limb 2 is a row and an issuer amendment, not a silent pass.

<status>complete</status>
<round>44</round>
<slot>~161</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
