# AMGT_RESAPP task order -- `AMGT-ab-1` -- THE D-1 DRIVER SPLICE: ASML'S DRAFTING DOCUMENT TAKES THE REWRITTEN DRIVER, NOTHING ELSE MOVES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~186</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the check READS the stored objects; this order writes nothing to AWS (the one write is AMGT-ab-6's act).
comp-adversary: RUN by the issuer at the cut -- AC1 requires exactly one moved key and the SERVED reader's own validator; base FAIL (no splice_driver).
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ab-1` (round 52, decomposition s.60)

The served `/thesis` driver chart reads the driver embedded in the D-1 drafting document `s3://opal-data-harvest/drafting/v1/<key>.json`
(`scoped_amgt.py:1876`), not the filings analysis object. ASML_NA_Equity's analysis (`filings/v1/ASML_NA_Equity/000162828026011378.analysis.json`)
now carries 3 driver points each with a `span`; its stored D-1 document still carries the old 3 points with no span, so the chart reads
ABSENT. `lib/research/filings/drafting_build.py` builds D-1 documents (`build_drafting_document(analysis)`, which carries
`"thesis_driver": analysis.get("thesis_driver")` at `:365`) and rebuilds the pool through ONE writer (`_rebuild_pool`, `:484`,
`analyze.write_outputs(None, analysis, document, write_pool=True, drafting_only=True, client=client)`). **A full rebuild of ASML is NOT
acceptable:** measured at the cut it also drops served sentences (company_description 6 -> 1, investment_thesis 1 -> 0, risks 2 -> 0).

**Build:** `splice_driver(stored_document, analysis, provenance) -> document` -- a pure function returning a COPY of the stored D-1
document with ONLY `thesis_driver` replaced by `analysis.get("thesis_driver")` (never mutating its input; every other key byte-equal),
AND the splice's PROVENANCE recorded in the document -- `provenance` = {"analysis_key": <the analysis object's key>,
"analysis_version_id": <its S3 VersionId>} -- so the D-1 document is never silently mixed-vintage (AMENDMENT 1). Record it inside
`thesis_driver` or in ONE added top-level key, wherever `lib/research/drafting/schema.json` (the served reader validates against it)
admits it; if the schema admits neither, that is a row and a stop on AC1, never a schema edit (the schema is not in your paths). The
CLI reads the analysis object's VersionId with head_object. And a CLI mode
`--splice-driver --only-keys K1,...` with `--dry-run` (prints, per key, the moved top-level keys, the driver's points and spans, and
the served validator's verdict, and writes nothing) and `--pre-act-dir DIR` (saves each key's pre-act bytes before the write), writing
through the SAME one writer `_rebuild_pool` uses. It refuses (non-zero exit, nothing written) when the spliced document fails
`lib.research.api.scoped_amgt._validate_drafting_document`, or when the analysis accession differs from the stored document's. Tests
(stubbed client): only `thesis_driver` moves; dry-run writes nothing; a failing document is refused.

## 2. BOUNDS

1. `drafting_build.py` and ONE new test file under `lib/research/filings/tests/` only (another cell adds its own test file there; do not
   edit other tests). NO live `--splice-driver` run without `--dry-run`, no S3 write. Standing: no install, no push, no promote, no deploy,
   no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~186/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ab-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_1_splice.py; echo "exit=$?"</invocation><expect>differing top-level keys: 'thesis_driver' plus at most one provenance key; driver points 3, spanned 3; served validator: True; input mutated: False; provenance ... recorded: True; THE D-1 DOCUMENT TAKES THE SPANNED DRIVER AND NOTHING ELSE MOVES: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ab-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m lib.research.filings.drafting_build --splice-driver --only-keys ASML_NA_Equity --dry-run; echo "exit=$?"</invocation><expect>one ASML_NA_Equity line naming the moved keys as only thesis_driver, 3 spanned points, the validator's verdict, and that it wrote nothing -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ab-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 118 (118 at the cut, plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~186/AMGT_RESAPP.TO-AMGT-ab-1.the-d1-driver-splice.proof_of_spec.json`. Report once: the CLI's exact invocation for the live act, what the dry-run printed, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis item 1; ruling 5. Cut as a SPLICE at the cut (s.60b.1): the preview (`ab_1_preview.py`) shows a full
rebuild drops served sentences. Base: AC1 FAIL (no splice_driver); AC2 FAIL (argparse refuses --splice-driver); AC3 PASS 118. The live
write is ab-6's act under the pair.

<status>pending</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, 2026-09-30 ~07:3xZ, before spawn):** CTO msg 27014 condition 1 -- the splice records its provenance (analysis key + VersionId) in the document; AC1's check amended to require it (moved keys: thesis_driver plus at most one provenance key). Base still FAIL (no splice_driver).
<round>52</round>
<slot>~186</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
