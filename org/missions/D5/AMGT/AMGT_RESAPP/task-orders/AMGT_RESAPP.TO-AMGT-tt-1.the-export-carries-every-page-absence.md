# AMGT_RESAPP task order -- `AMGT-tt-1` -- THE EXPORT CARRIES EVERY PAGE ABSENCE, AND THE VERDICT COUNTS A DROPPED ONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-tt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~163</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the checks READ a fixed capture outside the repository; nothing reaches AWS.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a verdict made blind to the defect it is meant to catch: AC2 runs the harness on two pinned PRE-FIX served exports that each drop one page absence, and requires NOT OK on both. Blind spot, stated: the export change reaches the served body only at tt-2.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-tt-1` (round 45, decomposition s.53)

FWD-30 says the rich export equals the page. **86 of 95 names drop exactly one page absence from the export, and the harness's
verdict never counts it.** Two limbs, one cell:

1. **The export carries every absence the page shows, as the page states it.** The page shows a name's posture absence in TWO places:
   the header's machine posture line and the Posture tab's line (`portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx:443`:
   "Posture: ABSENT -- <reason>. Nothing is rendered in its place."). The export (`lib/research/print/render_pack.py`,
   `_posture_markdown`, `:690`) writes ONE line. Measured on the served capture (`C:/tmp/amgt-r44-close`, read 2026-09-26T13:29Z):
   - RKT_LN_Equity: the export's line matches the page HEADER form (ending "-- a machine's view for a person to accept or reject,
     never an instruction."); the page's TAB form is not in the export.
   - AMD_US_Equity: the export's line matches the page TAB form (ending "Nothing is rendered in its place."); the page's HEADER form
     (ending "has not landed one") is not in the export.
   Make the export write the line the page shows in each place, byte-identical to the page's words, so no page absence is missing.
   The page is the reference: you change no page file.
2. **The verdict counts a dropped absence.** `portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` computes
   `absDiff.missing` and prints it, but its OK predicate (`:489-497`) tests only `pageAbsencesCoveredInRich` (a reason found anywhere).
   Add `absDiff.missing.length === 0` to the predicate. You are the harness's named `POD_DE_ANY` writer.

The checks read round 45's fixed capture through `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py` over the pinned population `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/population_at_cut.txt` (95 folders).
Unit tests for the export live in `lib/research/print/tests/`.

## 2. BOUNDS

1. **No server; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
2. **No page file, not `build_pack` (the pdf path), no data.** Never bend the product to the instrument, and never make the instrument
   blind to fit the product: the harness's page parser keeps reading the page as it is.
3. **Do not refresh the cache** (`C:/tmp/amgt-r44-close`) and do not edit `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/controls/`. Portal files commit inside `portal/` on
   `wk-AMGT_RESAPP-163-portal`, then the outer commit. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~163/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-tt-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-1.AC1.sh; echo "exit=$?"</invocation><expect>absences missing=0 on 95 of 95 names; EXPORT-COMPARE OK on 95 of 95; sweep rc=0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-tt-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-1.AC2.sh; echo "exit=$?"</invocation><expect>THE VERDICT COUNTS A DROPPED ABSENCE: YES on 2 of 2 (harness rc=1 on both pinned pre-fix exports) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-tt-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-1.AC3.sh; echo "exit=$?"</invocation><expect>pytest lib/research/print/tests: all passed -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~163/AMGT_RESAPP.TO-AMGT-tt-1.the-export-carries-every-page-absence.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.6 item 4. Base runs (round45/base-runs): AC1 FAILS (9 of 95), AC2 FAILS (rc=0 on both), AC3 PASSES (36 passed). AC1 and AC2 are the build checks; AC3 the bound. SERVED: the export change reaches the served body at tt-2.

<status>pending</status>
<round>45</round>
<slot>~163</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
