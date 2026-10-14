# AMGT_RESAPP task order -- `AMGT-bm-2` -- THE SERVED FORWARD P/E IS WITHHELD WITH A STATED REASON WHEN ITS PRICE AND ITS EPS ARE IN DIFFERENT CURRENCIES, AND THE REASON IS SERVED AS `model.forecast_withheld` (ONE SOURCE FILE AND ONE TEST MODULE; THE SAME RULE AS ROUND 104'S FISCAL P/E)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~442</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bm-2.a-forward-pe-whose-price-and-eps-are-in-different-currencies-is-withheld-with-a-stated-reason</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one source file and one test module; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the check invokes the existing function (GET) and reads S3 under the box's own role; no grant is changed.
comp-adversary: RUN at the cut -- `r106_fwd_pe_check.py` reads `R106 FORWARD PE CHECK: NO (3 of 6 arms)` at the base (F1, F3, F4 FAIL; F2, F5, F6 PASS: the checkout's own handler equals the live function on every other path, so the check discriminates and its control arms hold); the population it reads is `r106_forward_pe_population.py` over the live function (278 rows, 60 in a different currency on 20 names, 18 minor-unit pairs kept).
EGRESS CLASS, declared: NONE beyond the Lambda invoke (GET) and S3 reads; no Bloomberg call, no write.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-442` (branch `wk-AMGT_RESAPP-442`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-442`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bm-2` (round 106, decomposition s.115)

CTO round-105 analysis (msg 5426, item 1, row W418-S2): PBR US's forward P/E (5.2x, 6.3x) sits beside a USD price and BRL EPS with no currency note. The rule is round 104's (`AMGT-bk-4`, `_derive_fiscal_pe` in `lib/research/api/scoped_amgt.py`: the cross-currency fiscal P/E is withheld with a reason): **a served forward P/E (`BEST_PE_RATIO` row of `model.forecast_figures`) whose price currency and consensus-EPS currency are DIFFERENT currencies is withheld**; the row is dropped from `forecast_figures`, and one entry per dropped row is served in a NEW key of the model block, `forecast_withheld`, as `{mnemonic: "BEST_PE_RATIO", fiscal_year, fiscal_period, reason}` with the reason `the price is in <code> and consensus EPS in <code>, and a ratio of different currencies is not shown` (the same words as bk-4's cross-currency reason, with the two ISO codes).

Definitions, exactly as the population was measured: the PRICE currency is the currency of the `PX_LAST` header figure served in the same `/thesis` body (`header_figures`; the fiscal `PX_LAST` rows of the model block carry the same currency: read it there in `read_model`, which does not see the header: take the currency of the latest `PX_LAST` row of `fiscal_year_figures`); the EPS currency is the `currency` of the `BEST_EPS` row of the SAME `fiscal_year` and `fiscal_period` in `forecast_figures`. Two codes are the SAME currency when equal case-insensitively (a minor unit over its major, `GBp` over `GBP`, stays: use `case_rule.is_minor_unit_quote` as `_derive_fiscal_pe` does) and DIFFERENT otherwise. If either currency is absent, the row is kept untouched (never withhold on a missing code). A `BEST_PE_RATIO` row with no `BEST_EPS` row of its period is kept. Every other forecast row (EPS, EBITDA, every mnemonic that is not `BEST_PE_RATIO`) is untouched, in order. `forecast_withheld` is `[]` when nothing is withheld (the key is always served in the model block, next to `fiscal_unresolved`). The stored Bloomberg values are not changed: the withholding is on the served rows only, in `read_model`, like `pe_withheld` of the fiscal side; the model-case readers read the stored block.

Measured at the cut (the live function, 95 names): 278 served forward P/E rows, 200 in the same currency, 18 minor-unit pairs (kept), **60 in a different currency on 20 names**; PBR US (USD over BRL) is the arm; `AZN LN`, `HSBA LN`, `RIO LN`, `BP/ LN` (GBp over USD), `TSM US` (USD over TWD), `1299 HK` (HKD over USD) are in the 60. The prepared population file is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/forward_pe_population.json`. Read `_derive_fiscal_pe` first: it is the shape to copy (its figures-and-withheld return, its minor-unit handling); do not invent a new style.

**RE-SEAT NOTE (second pass).** The first pass is committed (`1ed763b974`, `ed5f4b4723`): the code, the 15 tests and the instance; its rows W442-S1 and W442-S2 are ruled here. W442-S1: the live function has run with `AMGT_AIFILL_ROOT=/var/empty/aifill-hold` since 2026-10-14 05:10Z (`~R2`'s AI-fill hold, a configuration change on the same code), so the `ai_fill` block differs between the live function and a checkout run without it: the issuer's check had been dry-run before that change. The check is AMENDED (`r106_fwd_pe_check.py` now sets that variable and sets the `ai_fill` block aside in F5, as its docstring says; the amended file is on your branch). The issuer re-ran it from your checkout `ed5f4b4723`: `R106 FORWARD PE CHECK: YES (6 of 6 arms)`. W442-S2: `forecast_source_counts` counts the STORED rows (your reading stands: a withheld row is still a Bloomberg figure; counting served rows would move the census). Your remaining work: run AC1 again with the amended check, re-record AC1 (and AC2, AC3 unchanged) in the instance, run `python .tools/proof-of-spec-check.py` on the committed bytes, commit. Do NOT touch the code or the tests.

THEN write ONE new test module `lib/research/api/tests/test_forward_pe_withheld.py` with at least these cases, each a plain function over hand-built forecast rows (read `lib/research/api/tests/test_derive_fiscal_pe.py` and `tests/test_read_model_fiscal_unresolved.py` for the row shape): a USD price with a BRL EPS withholds both rows and the reason names USD and BRL; a GBp price over a GBP EPS keeps its row; a GBp price over a USD EPS withholds; equal codes keep; an absent price currency keeps; a `BEST_PE_RATIO` row with no `BEST_EPS` of its period keeps; a non-P/E forecast row is returned untouched and in order; `forecast_withheld` is `[]` when nothing is withheld; the served block carries the key. Then run AC1 to AC3. AC1 compares the checkout's own /thesis handler with the LIVE function's for all 95 names (about five minutes; set your tool timeout to 600000 ms). Report AC1's lines as printed.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. If a premise of this order does not reproduce (a function, a key or a count named here is not where the order says), file a BLOCKING row naming exactly what you found and stop that item: do not patch around it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Two files: `lib/research/api/scoped_amgt.py` and the new test module. Nothing else.
2. Read-only against the world: GET invokes and S3 reads; no deploy, no store write, no Bloomberg call. No `pip install`. Standing: no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_forward_pe_withheld.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~442/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bm-2"><invocation>cd C:/dev/wk-resapp-442 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/checks/r106_fwd_pe_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/forward_pe_population.json" --workers 4 | grep -E "^names|PASS|FAIL|R106"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a line `names 95 | base forward P/E rows 278 | candidate 218 | withheld 60 (population 60) | names with a withheld row 20 | status not (200, 200): []`, six `PASS` arm lines (F1 to F6) and `R106 FORWARD PE CHECK: YES (6 of 6 arms)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bm-2"><invocation>cd C:/dev/wk-resapp-442 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest lib/research/api/tests/test_forward_pe_withheld.py -q 2>&amp;1 | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`N passed` with N at least 8 and no `failed`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bm-2"><invocation>cd C:/dev/wk-resapp-442 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- . ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~442" ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel" | sort</invocation><expect>exactly two lines, `lib/research/api/scoped_amgt.py` and `lib/research/api/tests/test_forward_pe_withheld.py`</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~442 <0.9.0_WK_AMGT_RESAPP~442@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~442/AMGT_RESAPP.TO-AMGT-bm-2.a-forward-pe-whose-price-and-eps-are-in-different-currencies-is-withheld-with-a-stated-reason.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- AC1's output lines (the `names` line and the six arm lines);
- AC2's and AC3's output lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 5426 item 1 (W418-S2): a served-value move, so it carries its never-widen pair (`AMGT-bm-3`, RA1; the COO half is the issuer's, then the CTO's). The decision to WITHHOLD rather than state a basis is the issuer's, inside the CTO's `states its basis ... or is withheld with a reason` (decomposition s.115): 60 rows on 20 names; the 218 other rows are byte-equal. `scoped_amgt.py` is a shared file: `~R2`'s AIFILL edited it in other regions (fa-7); this cell edits `read_model` only, so the merge is a safe-merge, never a rebase.

<status>complete -- 2026-10-14T06:1xZ by the issuer (2.0.0_SA_COO~R1): worker ~442 (two passes) @98aa3b2e96 merged @3818736e6b, proof instance VALID (rc=0). The served forward P/E whose price and EPS currencies differ is withheld with a reason naming both codes and served as `model.forecast_withheld`: 60 rows on 20 names; 218 rows kept byte-equal; 15 unit tests. Re-read by the issuer: the amended check run from the worker's checkout (ed5f4b4723, same code) read `R106 FORWARD PE CHECK: YES (6 of 6 arms)`, 95 names, status 200 and 200; the worker re-ran AC1 on 7400079c19: 6 of 6 arms; the code reviewed by the issuer. The first pass's AC1 FAIL (the AI-fill hold's environment on the live function since 05:10Z: my check predated it) was my instrument's defect, amended @1bcfc2e957. Not applied: the redeploy and its never-widen pair are AMGT-bm-3.</status>
<round>106</round>
<slot>0.9.0_WK_AMGT_RESAPP~442</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
