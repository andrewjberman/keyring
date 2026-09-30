# AMGT_RESAPP task order -- `AMGT-zz-6` -- THE THESIS DRIVER'S CHART SERIES FROM THE FILING'S VERIFIED POINTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~185</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry run READS the stored source and analysis objects; the check wraps the S3 client so any put raises.
comp-adversary: RUN by the issuer at the cut -- AC1 refuses to call the function without dry_run and fails on any put.
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-zz-6` (round 51, decomposition s.59)

The /thesis page draws the thesis driver's chart from `scoped_amgt.thesis_driver_chart(driver, ...)` (`scoped_amgt.py:2267-2381`); its
filing branch needs >= 2 driver points each carrying a `span` (the producer's marker that the value was re-located in the source
excerpt), with `source: "filing"`. ASML_NA_Equity's stored analysis (`filings/v1/ASML_NA_Equity/000162828026011378.analysis.json`)
holds 3 driver points and resolution 'cited', but its chart reads ABSENT -- the stored points predate the span verification.
`lib/research/filings/analyze.py` `reverify_stored_thesis_driver(security_key, accession, client=None)` (`:1349`) re-verifies the
stored points against the source object's own `excerpt.text` through `_apply_point_verification` (the path a fresh run takes) and
REWRITES the analysis object unconditionally.

**Build:** `reverify_stored_thesis_driver` gains `dry_run=False`. With `dry_run=True` it computes exactly as today, WRITES NOTHING, and
returns `(analysis_doc, analysis_key, receipt)` with a receipt string naming the dry run. `dry_run=False` is byte-for-byte today's
behaviour. Then make the verification produce what the chart's filing branch needs for ASML: if the re-verified points still lack a
`span`, find why in `_apply_point_verification` against the stored excerpt and fix it there (a point whose value is NOT found in the
excerpt must stay unspanned -- never a guessed span). The REAL rewrite of ASML's object is AMGT-zz-8's act under its pair, not yours.
Tests (stubbed client): dry_run writes nothing; the default path still writes.

## 2. BOUNDS

1. `analyze.py` and the filings tests only. Do NOT edit `scoped_amgt.py` (another cell owns it this round): if the chart builder
   itself must change, file a row and stop on that criterion. No S3 write, no call with `dry_run=False` outside a stubbed test.
   Standing: no install, no push, no promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~185/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_6_reverify.py; echo "exit=$?"</invocation><expect>the dry run writes nothing; ASML's re-verified chart reads SERVED, source 'filing', &gt;= 2 numeric points; THE DRIVER CHART IS SERVED FROM THE FILING'S VERIFIED POINTS: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 111 (111 at the cut, plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~185/AMGT_RESAPP.TO-AMGT-zz-6.the-driver-chart-series.proof_of_spec.json`. Report once: why ASML's points lacked spans, what the dry run returns (points, spans), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 5, cell 6 (DSGN FWD-1 hop 4). Base: AC1 FAIL (no dry_run parameter; not called); AC2 PASS
111. The other 10 driver names hold 0 points (a fresh extraction, AMGT_CORPUS's producer; carried). zz_6_driver.py (95 s, a census,
PASS at base) is not a criterion. Served in zz-8 (ASML's real rewrite, under the pair).

<status>pending</status>
<round>51</round>
<slot>~185</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
