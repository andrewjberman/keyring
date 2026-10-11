# AMGT_RESAPP task order -- `AMGT-ss-2` -- A DRIVER POINT SET WHOSE FIGURES ARE STATED ON DIFFERENT SCALES IS HELD AS A SET

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~385</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-2.a-point-set-on-two-scales-is-held-as-a-set</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a verifier change and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r93_scale_table.py reads stored filing objects and silver rows with the caller's own credentials (GET only); r93_scale_set.py reads nothing.
comp-adversary: RUN at the cut -- r93_scale_set.py FAILs M1 at the base (all three SAP-shaped points are kept) and PASSes M2-M5, and PASSes all five arms against a throwaway candidate; r93_scale_table.py over the 12 stored analysis objects FAILs T1 at the base (SAP expects 3 points) and PASSes T2, and PASSes both against the same candidate (SAP 0 points, 11 others equal their stored points).
EGRESS CLASS, declared: NONE (S3 GETs of stored objects by r93_scale_table.py; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-385` (branch `wk-AMGT_RESAPP-385`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-385` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ss-2` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 2 (row D1-S22). `lib/research/filings/analyze.py::_apply_point_verification` keeps a driver point when its
value's digits sit inside the block that carries its period label. It never asks what SCALE the figure is stated on. Measured on the live SAP
object (`filings/v1/SAP_GY_Equity/000110465926020058.analysis.json`, series "Current cloud backlog"): 2024 = 18,078 and 2023 = 13,745 are stated
"million", 2025 = 21.05 is stated "billion": three kept points, one chart axis, a factor of 1,000 apart in units.

Add the rule inside `_apply_point_verification` (so a fresh run and `reverify_stored_thesis_driver` take it together, ONE verification path):
after the existing verification, for each KEPT point read the scale word in the excerpt text: the first whole word, case-insensitive, of
`thousand`, `million`, `billion`, `trillion` that begins within 12 characters after the end of the point's `span` (spaces allowed; stop at a
digit). When the kept points carry MORE THAN ONE distinct scale word, HOLD ALL OF THEM: move every kept point to the dropped (held) list,
keeping its `period` and `value` (and any `units` the held records carry), each with a `reason` that names the scales found, for example
`the figures are stated on different scales in the filing (million, billion) and the excerpt gives no conversion for the series`. A point with no
scale word (a table cell) contributes no scale; a set with at most one distinct scale word is unchanged byte for byte.

NOT in this cell: no rescaling of a point, no use of a conversion the excerpt states (a later cell may), no change to the block, columnar,
parenthetical or stated-in-period rules.

Add `lib/research/filings/tests/test_scale_set.py` (pure, no network): one test per arm M1-M5 of `r93_scale_set.py`, with the excerpts built in the test.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W385-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. `r93_scale_table.py`'s S3 GETs and silver reads are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `analyze.py` minimally: do not reformat it and do not touch `fetch.py`, `passages.py`, `drafting_build.py` or any served reader.
5. Do not run `reverify_stored_thesis_driver` with `dry_run=False`, and do not call it in any way that writes.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/test_scale_set.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~385/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-2"><invocation>cd C:/dev/wk-resapp-385 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_scale_set.py"; echo "exit=$?"</invocation><expect>PASS M1 (the SAP-shaped set is held whole and the reason names both scales), PASS M2, PASS M3, PASS M4, PASS M5; arms passed 5 of 5; R93 SCALE SET: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-2"><invocation>cd C:/dev/wk-resapp-385 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_scale_table.py"; echo "exit=$?"</invocation><expect>12 objects listed; SAP_GY_Equity reads CHANGED with expected 0 points, the other 11 read equal; PASS T1, PASS T2; R93 SCALE TABLE: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ss-2"><invocation>cd C:/dev/wk-resapp-385 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_locator.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_block_bound.py" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>the control: R91 LOCATOR: YES (13 of 13), R92 BLOCK BOUND: YES (5 of 5) and every test under lib/research/filings/tests passes with 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~385 <0.9.0_WK_AMGT_RESAPP~385@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~385/AMGT_RESAPP.TO-AMGT-ss-2.a-point-set-on-two-scales-is-held-as-a-set.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 2: "A point set whose unit tokens differ (thousand, million, billion) across the sentences its figures sit in is held as a SET, unless the excerpt states the conversion. SAP then goes under its own pair." The exception clause is NOT implemented here (a stated conversion is not used to rescale): the issuer's reading is that holding is the safe floor and a rescale is a larger cell with its own table; recorded for the CTO's round-93 analysis. Producer-side: no stored object is rewritten by this cell; SAP's re-verify and splice is `AMGT-ss-4` (staged, its own pair). Note the visible effect for the pair: SAP's one served point (2024 = 18,078 under a billions unit text) leaves the chart, which is itself a scale error today.

<status>pending</status>
<round>93</round>
<slot>0.9.0_WK_AMGT_RESAPP~385</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
