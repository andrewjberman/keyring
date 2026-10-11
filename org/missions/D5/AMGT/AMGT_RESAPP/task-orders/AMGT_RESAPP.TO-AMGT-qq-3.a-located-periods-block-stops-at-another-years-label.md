# AMGT_RESAPP task order -- `AMGT-qq-3` -- A LOCATED PERIOD'S BLOCK STOPS AT ANOTHER YEAR'S LABEL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-qq-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~383</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-qq-3.a-located-periods-block-stops-at-another-years-label</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a verifier change and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r91_locator.py reads stored filing objects with the caller's own credentials (GET only); r92_block_bound.py reads nothing.
comp-adversary: RUN at the cut -- r92_block_bound.py FAILs S1 and S5 at the base and PASSes S2-S4, and PASSes all five arms against a throwaway candidate that also leaves r91_locator.py at 13 of 13.
EGRESS CLASS, declared: NONE (S3 GETs of stored objects by the round-91 locator check; no vendor, SEC or model call).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-383`, cut from the current branch head). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AMGT-qq-3` (round 92, decomposition s.100)

CTO~DELL1 round-91 analysis item 5 (row D1-W372-S3, ARMED). `lib/research/filings/analyze.py::_apply_point_verification` verifies a driver
point only when its value is found inside the BLOCK that carries ITS OWN period label. `_period_blocks(period_labels, text_len)` (about
line 1131) gives each LOCATED label a block from its label to the NEXT LOCATED label by text position, or to the excerpt's end. Only the
periods a point set NAMES are located, so the LAST located period's block runs to the excerpt's end, and a figure the filing states for a
year the point set never names verifies for it. Measured on a synthetic excerpt by round 91's worker: a point `2025 = 18.08` verifies
against `... In 2024 revenue was 18.08 billion ...` (the figure is 2024's). The real excerpts hold only because a table label happens to
bound the block.

Bound every block at the first token of a DIFFERENT four-digit year (`19xx` or `20xx`, as a whole token: not part of a longer number and
not the digits of a decimal) that follows its own label, when that comes before the block's present end. A figure stated after another
year's token then belongs to that year. The period's own year, an `FY` alias of it (`FY2025`) and every other form `_locate_key` maps to
the same year do NOT end the block. Keep the bound inside `_period_blocks` or its single caller path so a fresh run and
`reverify_stored_thesis_driver` take it together (ONE verification path). Do not change the columnar, inline-parenthetical or
stated-in-period rules beyond what the bound requires; each must keep its present refusals and acceptances.

Add `lib/research/filings/tests/test_block_bound.py` (pure, no network): the synthetic refusal, the control that the period's own figure
stated before the other year still verifies, the two-period control, a figure stated far from its label with no other year between (a
bound by distance would refuse it: it must verify), and a table-row case where a figure after a different year line is refused.

ASCII only. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W383-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. The round-91 locator check's S3 GETs and silver reads are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit `analyze.py` minimally: do not reformat it and do not touch `fetch.py`, `passages.py`, `drafting_build.py` or any served reader.
5. Do not run `reverify_stored_thesis_driver` with `dry_run=False`, and do not call it in any way that writes.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/test_block_bound.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~383/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-qq-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_block_bound.py"; echo "exit=$?"</invocation><expect>PASS S1 (a figure stated for a different year is refused for the last located period), PASS S2 (control: the period's own figure still verifies), PASS S3 (control: both periods verify), PASS S4 (the bound is a different year token, not distance), PASS S5 (a figure after a different year token in a table row is refused); R92 BLOCK BOUND: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-qq-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_locator.py" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>the round-91 locator check still reads R91 LOCATOR: YES (13 of 13: L1-L4 verify, K1 keeps its span, E1 and X1-X7 hold) and every test under lib/research/filings/tests passes with 0 failed, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~383 <0.9.0_WK_AMGT_RESAPP~383@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~383/AMGT_RESAPP.TO-AMGT-qq-3.a-located-periods-block-stops-at-another-years-label.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of `analyze.py`, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-91 analysis @f6eb45c478 section 2 and item 5: the stored-object re-verification store write (item 4, `AMGT-qq-4`) runs only AFTER this cell merges, so no re-verification publishes through the hole. Producer-side. The close is two-part: the synthetic refusal and the control (AC1) and the round-91 locator check unchanged (AC2). The issuer also re-runs the dry-run re-verification over all stored analysis objects (12 at the cut) before merging and reads any point that was verified at the base and is held after as a candidate regression. Checks dry-run at the base: AC1 FAIL (S1, S5; S2-S4 PASS); AC2 PASS at the base for the locator check and the filings suite, FAIL until the new test file exists.

<status>pending</status>
<round>92</round>
<slot>0.9.0_WK_AMGT_RESAPP~383</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
