# AMGT_RESAPP task order -- `AMGT-xx-1` -- FWD-30'S ONE GRADER KEYS ON THE PAGE'S DATA ATTRIBUTES AND NAMES CASES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-xx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~173</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local checks; read-only lambda:Invoke of the deployed function through capture_lib, as the sweep already does.
comp-adversary: RUN by the issuer at the cut -- AC1 re-grades three served names two of which failed on wording alone; AC3 plants a wording change and an attribute change on a real rendered page (positive control + difference control).
EGRESS CLASS, declared: NONE. Opal's own deployed function, S3 and DynamoDB, read-only.
</preflight>

## 1. THE CELL -- `AMGT-xx-1` (round 49, decomposition s.57)

FWD-30 asks: does the page's reading of a security equal its rich export, figure by figure, cite by cite, absence by absence,
case by case? Its ONE grader is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py`. Today
`--served` captures, per research-library name, the deployed function's routes (through
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py`) and the deployed rich body
(`print?format=rich`), then runs the PAGE side through another project's page harness
`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs`, which matches absence lines by their visible WORDS.
The page's owner (DSGN_AMGTV1) rewords sentences for readers, so the grade moves every time the page is rewritten: at round 48's
close it read 62 of 96 OK, every failure an absence stated in different words (row Z-S305).

**Build, inside `round45/checks/` only:**
1. **A page reader keyed on attributes.** `sweep.render_page_html(fixture_path) -> str` renders the SecurityAnalysis page from a
   captured served fixture (the way the harness renders it: node, from `portal/`, `react-dom/server` `renderToStaticMarkup`;
   put any node script you need beside `sweep.py`, e.g. `round45/checks/page_render.cjs`, and run it with `cwd=portal`).
   `sweep.page_facts_from_html(html) -> dict` returns four sets keyed `"FIGURES"`, `"CITES"`, `"ABSENCES"`, `"CASES"`, read ONLY
   from the page's data attributes, never from visible text: `data-model-row`, `data-model-cell`, `data-model-refused`,
   `data-model-case-status`, `data-model-case-reason`, `data-cite-resolved`, `data-posture-*`, `data-exec-officer` (all on portal
   DEV now). Each fact is a normalised key the RICH side can produce too (e.g. an absence as its section + served reason code or
   field, a figure as line + year + value), so equal data reads equal regardless of wording.
2. **The rich side read to the same keys.** `sweep.rich_facts(rich_text, fixture) -> dict` (same four sets) from the deployed rich
   body; where the rich text alone cannot give a key, read it from the captured served payload that produced it.
3. **One comparison that names what differs.** `sweep.compare_facts(page, rich) -> {"verdict": "OK"|"NOT_OK", "reason": ...,
   counts...}`; `reason` names EVERY class that differs and no other (`"CASES differ"`, `"ABSENCES+CASES differ"`), `""` when OK.
   The sweep's TSV `reason` column is this value.
4. **The grade line.** The sweep prints exactly one line
   `FWD-30 GRADE: equal E of I identified names; unidentified U of F folders; keyed on: data-attributes`
   where a folder whose identity does not resolve (today `Hitachi 6501 JP`) is COUNTED as unidentified and printed, never a
   CAPTURE_FAILED row or a TypeError. Exit 0 only when E == I.
Keep `--served`, `--live`, `--require-cases`, `--only`, `--cache`, `--out` working. The harness is NOT called by the grade any more.

**Where the page has no attribute for a fact** you need: do NOT edit anything under `portal/`, and do NOT fall back to text. File a
surprise row naming the fact and the element (the issuer asks DSGN_AMGTV1 for the attribute through its round) and grade that
class on what the attributes DO carry, saying so in the row.

## 2. BOUNDS

1. Write only inside `round45/checks/` (plus your deliverables and the surprise channel). `portal/**` is READ-ONLY -- another
   project's surface. No product code under `lib/`.
2. No S3 write, no deploy, no server, no vite. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`; node from `portal/` (its `node_modules` are provisioned).

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~173/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository including `portal/`; the deployed `opal-amgt-scoped-api` through capture_lib; Opal S3/DynamoDB.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-xx-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-1.AC1.sh; echo "exit=$?"</invocation><expect>FWD-30 GRADE: equal 3 of 3 identified names; ...; keyed on: data-attributes -- and FWD-30 GRADER KEYED ON DATA ATTRIBUTES READS THE NAMED SET EQUAL: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-xx-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-1.AC2.py; echo "exit=$?"</invocation><expect>four planted pairs each "ok", THE REASON NAMES THE CLASS THAT DIFFERS: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-xx-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-1.AC3.py; echo "exit=$?"</invocation><expect>(a) wording plant -&gt; facts EQUAL; (b) attribute plant -&gt; facts DIFFER; THE GRADE KEYS ON THE ATTRIBUTE, NOT THE WORDS: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built grade on three served names (ASML and BABA failed on wording alone at round 48); AC2 the reason names the class;
AC3 the positive control that the key is the attribute, with its difference control.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~173/AMGT_RESAPP.TO-AMGT-xx-1.fwd30-grader-keys-on-data-attributes.proof_of_spec.json`. Report once: what you changed and where, the attribute each class keys on, any fact with no attribute (and its row), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-48 analysis s.4 row 1 and rulings 1-2 (@1dfd5c0970). Base: AC1 FAIL (no GRADE line; 17 s), AC2 FAIL (no
compare_facts), AC3 FAIL (no render_page_html / page_facts_from_html). The issuer's real run at the drain: the full `--served --live
--require-cases` sweep over 96 folders, expected 95 of 95 identified equal, Hitachi printed unidentified. Worktree with portal at
DEV `ea248519`.

<status>complete</status>
<round>49</round>
<slot>~173</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
