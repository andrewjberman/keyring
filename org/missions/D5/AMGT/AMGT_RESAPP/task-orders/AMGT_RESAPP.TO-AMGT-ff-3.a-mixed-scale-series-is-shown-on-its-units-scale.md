# AMGT_RESAPP task order -- `AMGT-ff-3` -- A DRIVER POINT SET STATED ON DIFFERENT SCALES IS SHOWN ON THE SCALE ITS SERIES UNIT NAMES, WITH EACH STATED VALUE KEPT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~389</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-3.a-mixed-scale-series-is-shown-on-its-units-scale</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a verifier rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r94_rescale_table.py and r94_locator.py read stored filing objects and silver rows with the caller's own credentials (GET only); r94_rescale.py reads nothing.
comp-adversary: RUN at the cut -- r94_rescale.py FAILs R1 at the base and PASSes R2-R7, and PASSes 7 of 7 against a throwaway candidate; r94_rescale_table.py over the 12 stored analysis objects FAILs T1 at the base (SAP expects 0 points, held whole) and PASSes T2, and PASSes both against the candidate (SAP 3 points at 13.745, 18.078, 21.05, 11 others equal); r94_locator.py reads 13 of 14 at the base (L5) and 14 of 14 against the candidate. r93_scale_set.py (5 of 5) is unchanged by construction (it passes no unit text).
EGRESS CLASS, declared: NONE (S3 GETs by the table and locator checks; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-389` (branch `wk-AMGT_RESAPP-389`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-389` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ff-3` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis item 4 (ss-2's exception clause, ruled and not built). Round 93's `_scale_set_reason` holds a kept point set WHOLE when its figures are
stated on more than one scale word (thousand, million, billion, trillion). SAP's 2023-2025 current cloud backlog (13,745 and 18,078 "million", 21.05
"billion", one passage) is held, and SAP's driver is empty. The series' own `unit` text says the scale the chart is in ("EUR billions and % growth at constant
currencies") and the scale words have fixed factors, so each figure can be SHOWN on that scale with its stated value kept.

Change `lib/research/filings/analyze.py`:

1. `_apply_point_verification(points, excerpt_text, passage_map, anchor=0, unit_text=None)` gains `unit_text`. After verification, when the verified points carry
   MORE THAN ONE scale word and `unit_text` names EXACTLY ONE scale word (whole word, singular or plural, case-insensitive, among thousand, million, billion,
   trillion) that is one of the scale words the points carry, and EVERY verified point carries a scale word: each verified point is KEPT with `value` set to
   `stated value x factor(its stated word) / factor(the unit word)` rounded to 9 decimals, and its entry carries `stated_value` (the value as it was),
   `stated_scale` (its own scale word) and `rescaled_to` (the unit word, singular). Every other mixed case is held WHOLE exactly as round 93 holds it (the same
   reason sentence naming the scales). A set with at most one scale word is unchanged byte for byte; a bare figure (no scale word) beside ONE scale word is not a mix.
2. Both callers pass the series' unit: the fresh two-pass run (`resolve_driver`'s verification call) and `reverify_stored_thesis_driver` pass
   `driver.get("unit")` (the string; None when absent). ONE verification path.

NOT in this cell: no change to the block, columnar, parenthetical or stated-in-period rules, to the scale-word window (12 characters after the figure's span,
a digit stops it), or to any stored object (no write).

Add `lib/research/filings/tests/test_rescale_scale_set.py` (pure, no network): one test per arm R1-R7 of `r94_rescale.py`, with the excerpts built in the test.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W389-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. The table and locator checks' S3 GETs and silver reads are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `analyze.py` minimally: do not reformat it and do not touch `fetch.py`, `passages.py`, `drafting_build.py` or any served reader.
5. Do not run `reverify_stored_thesis_driver` with `dry_run=False`, and do not call it in any way that writes.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/test_rescale_scale_set.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~389/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-3"><invocation>cd C:/dev/wk-resapp-389 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_rescale.py"; echo "exit=$?"</invocation><expect>PASS R1 (the SAP-shaped set is shown on the unit's scale, stated values kept), PASS R2, PASS R3, PASS R4, PASS R5, PASS R6, PASS R7; arms passed 7 of 7; R94 RESCALE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-3"><invocation>cd C:/dev/wk-resapp-389 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_rescale_table.py"; echo "exit=$?"</invocation><expect>12 objects listed; SAP_GY_Equity reads CHANGED with expected 3 points (13.745, 18.078, 21.05), the other 11 read equal; PASS T1, PASS T2; R94 RESCALE TABLE: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ff-3"><invocation>cd C:/dev/wk-resapp-389 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_locator.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round93_prep/checks/r93_scale_set.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_block_bound.py" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>the control: R94 LOCATOR: YES (14 of 14, L5 SAP shown on the unit's scale), R93 SCALE SET: YES (5 of 5), R92 BLOCK BOUND: YES (5 of 5) and every test under lib/research/filings/tests passes (no failed); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~389 <0.9.0_WK_AMGT_RESAPP~389@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~389/AMGT_RESAPP.TO-AMGT-ff-3.a-mixed-scale-series-is-shown-on-its-units-scale.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c item 4: "A rescale cell for a series whose excerpt STATES the conversion (SAP's 2023-2025 backlog is in millions and billions in one passage): shown on one scale, with the excerpt's conversion cited. ss-2's exception clause was ruled and not built. It is a producer-side rule with its tests; the served re-verify of SAP follows under its own pair." READ: the scale words ARE the stated conversion (a million is a thousand thousands; the excerpt prints both words for one series), so the factor is fixed; the rule's gate is that the series' own unit text names the target scale, so the chart's declared unit and its values agree (SAP's unit text reads 'billions' while the one value served before round 93 was 18,078 million). Where the unit names no scale, or a scale the points do not carry, or two, or a bare figure sits in the set, the set is held exactly as in round 93. The round-93 check `r93_scale_table.py` is superseded by `r94_rescale_table.py` (its T1 asserts SAP held); `r93_locator.py` by `r94_locator.py` (its L5 asserts SAP held). Producer-side: no stored object is rewritten by the cell; SAP's re-verify and splice is `AMGT-ff-5` (staged, its own pair).

<status>pending</status>
<round>94</round>
<slot>0.9.0_WK_AMGT_RESAPP~389</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-11T12:59Z (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-389 @95ed56fdc7 (code @bfd71e9edf) merged @ae14fab6f5, proof instance VALID; issuer re-run in the worktree: AC1 R94 RESCALE YES (7 of 7), AC2 R94 RESCALE TABLE YES (12 objects, SAP stored 0 -> expected 3 points at 13.745, 18.078, 21.05 with stated_scale and rescaled_to billion, 11 equal), AC3 R94 LOCATOR YES (14 of 14) + R93 SCALE SET YES (5 of 5) + R92 BLOCK BOUND YES (5 of 5) + 335 passed; drain checks py_compile rc 0, ruff clean, 540 passed. analyze.py +45/-5: `_unit_scale_word`, `_rescale_plan`, `unit_text` on `_apply_point_verification`; both callers pass the series unit (one verification path). Producer-side: no stored object is rewritten by the cell; SAP's re-verify and splice is AMGT-ff-5 under its own pair. Worker rows ruled: S1 (the worktree head was six drain merges past the cut; none touches the cell's paths) stands; S2 (resolve_driver has no driver object at its verification call and passes the cleaned local unit, the same string the stored driver carries) stands; S3 (the channel header says one fenced block, the file holds one row per block) stands.</status>
