# AMGT_RESAPP task order -- `AMGT-bk-4` -- THE SERVED FISCAL P/E IS PX_LAST / IS_EPS OF THE SAME YEAR, WITH A MINOR UNIT SCALED AND A DIFFERENT CURRENCY WITHHELD (A BUILD; ONE FILE; STAGED BEHIND bk-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~415</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-4.the-served-fiscal-pe-is-price-over-reported-eps-of-the-same-year</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one source file and one test module; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the check invokes the existing function (GET) and reads S3 under the box's own role; no grant is changed.
comp-adversary: RUN at the cut -- `r104_pe_check.py` reads `R104 PE CHECK: YES (6 of 6 arms; names 95, rows 464 served, 154 withheld)` on the prepared candidate (blob 351f9a1d7a8a) and NO at the base (P1 and P4 FAIL: the base serves Bloomberg's own values); arm P5 is the control (a derived value moved by 0.01 reads a P1 failure); `r104_pe_delta.py` reads YES on a synthetic pre/post and NO when a team_sheet moved.
EGRESS CLASS, declared: NONE beyond the Lambda invoke (GET) and S3 reads; no Bloomberg call, no write.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-415` (branch `wk-AMGT_RESAPP-415`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-415`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bk-4` (round 104, decomposition s.113)

CTO ruling (msg 5244 (iii)) and refinement (msg 5262), on the round-103 analysis item 2 (iii): the five 2025 P/E figures the CVO found do not follow from the printed EPS and price (SAN FP 20.4x against 72.09 / 6.40; the 2025 column's own EPS is `IS_EPS` and its price `PX_LAST`, and 82.72 / 6.402 is 12.9x). The served historical P/E becomes `PX_LAST / IS_EPS` of the SAME fiscal year, so the page agrees with itself. Bloomberg's own `PE_RATIO` stays STORED in the model block and is not served on this row.

The change is PREPARED and dry-run; apply it on the merged result of `AMGT-bk-1` (the same file, blob `96642b55204d`), then add the unit tests below. ONE source file, `lib/research/api/scoped_amgt.py`:

    cd C:/dev/wk-resapp-415 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/r104_pe_source.patch"

What it does: `_derive_fiscal_pe(fiscal)` returns the figures list and the withheld entries. For each fiscal year with a `PE_RATIO` row: both `PX_LAST` and `IS_EPS` of that year present, numeric and positive, in the SAME currency code -> the row's value is `round(PX_LAST / IS_EPS, 4)`, every other key of the row unchanged, `basis` = `{mnemonic, definition: "price / reported EPS (IS_EPS), FY<year>", derived_from: [PX_LAST, IS_EPS]}`; a minor unit of the same currency (`case_rule.is_minor_unit_quote`: GBp over GBP) divides the minor side by `case_rule.MINOR_UNIT_FACTOR` (100) and the definition adds `, the price side brought from GBp to GBP (divided by 100)`; otherwise the row is dropped from the figures and a `fiscal_unresolved` entry `{mnemonic: PE_RATIO, fiscal_year, reason}` is added, the reason naming WHY (an input absent; EPS not positive; the price not positive; a currency not stated; or `the price is in <code> and reported EPS in <code>, and a ratio of different currencies is not shown`). `read_model` applies it to the served figures only: the model cases read the stored block. If `git apply` refuses, STOP and file a BLOCKING row: do not edit by hand.

THEN write ONE new test module, `lib/research/api/tests/test_derive_fiscal_pe.py`, with at least these cases, each a plain function over hand-built figure rows (read `tests/test_read_model_fiscal_unresolved.py` for the row shape): same-currency positive inputs derive the quotient and the basis; GBp price over GBP EPS divides the price by 100 and says so; GBp over USD is withheld naming both codes; EPS zero and negative are withheld; an absent PX_LAST is withheld; a non-PE row is returned untouched and in order; a year with PE_RATIO but with no inputs is withheld with the absent reason.

Then run AC1 to AC3. AC1 compares the checkout's own /thesis handler with the LIVE function's for all 95 names (about four minutes; set your tool timeout to 600000 ms). Report AC1's before/after sample lines and the `WITHHELD BY REASON` line as printed.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Two files: `lib/research/api/scoped_amgt.py` (by the prepared patch, then nothing more) and the new test module. Nothing else.
2. Read-only against the world: GET invokes and S3 reads; no deploy, no store write, no Bloomberg call. No `pip install`. Standing: no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_derive_fiscal_pe.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~415/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bk-4"><invocation>cd C:/dev/wk-resapp-415 &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_pe_check.py" | grep -E "^names|WITHHELD|PASS|FAIL|R104"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the lines `names 95 (read failures 0)`, `WITHHELD BY REASON:` and the verdict `R104 PE CHECK: YES (6 of 6 arms; names 95, rows R served, W withheld)` with PASS on P1 to P6; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-4"><invocation>cd C:/dev/wk-resapp-415 &amp;&amp; PYTHONPATH="$(pwd)" timeout 300 python -m pytest lib/research/api/tests/test_derive_fiscal_pe.py -q 2>&amp;1 | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>`N passed` with N at least 7 and no `failed`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-4"><invocation>cd C:/dev/wk-resapp-415 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- . ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~415" ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel" | sort</invocation><expect>exactly two lines, `lib/research/api/scoped_amgt.py` and `lib/research/api/tests/test_derive_fiscal_pe.py`</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~415 <0.9.0_WK_AMGT_RESAPP~415@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~415/AMGT_RESAPP.TO-AMGT-bk-4.the-served-fiscal-pe-is-price-over-reported-eps-of-the-same-year.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- AC1's output lines including the five sample names' before/after lines (the check prints them) and the `WITHHELD BY REASON` line;
- AC2's and AC3's output lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** GO 2026-10-13T22:5xZ by the issuer: `AMGT-bk-1` is complete and MERGED (@8203952bad); the file's blob at HEAD is `96642b55204d`, the base this order's patch expects. CTO 5244 (iii) and 5262: exact arithmetic on two served figures; Bloomberg's PE_RATIO stays stored; a minor unit of the same currency is an exact scale (the ruled qq-1 / CRPS-g-1 rule, `case_rule`), true cross-currency stays withheld because an FX rate and date would be a choice this cell does not make. Measured at the cut over 618 live P/E name-years: 464 derived, 154 withheld (126 cross-currency, 28 EPS not positive). A derived row moves the served value, so it moves under a PAIR (bk-2): the pair names the 95 x 10 cells and prints before/after for five names. STAGED behind bk-1 because both edit one file.

<status>pending</status>
<round>104</round>
<slot>0.9.0_WK_AMGT_RESAPP~415</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
