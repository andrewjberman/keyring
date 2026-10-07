# AMGT_RESAPP task order -- `AMGT-bb-9` -- THE COUNTRY IN PLAIN CASE (DSGN_AMGTV1 FWD-27)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~295</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_B_NOTES.md) -- The country header figure is all capitals on 95 of 95 covered names, 22 distinct values. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-295` (branch `wk-AMGT_RESAPP-295`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-295`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-9` (round 78, decomposition s.86)

The page prints "Country: UNITED STATES" because the country arrives from the data vendor in capitals and is passed
through. Serve it in plain case.

Create `lib/research/api/country_name.py` (standard library only) exporting TWO functions:

`plain_country(value)` returns the country text in plain case.
1. A value that is not text, is empty, or already carries a lower-case letter is returned unchanged.
2. Otherwise each run of letters becomes one word with a capital first letter and the rest lower case: "UNITED
   STATES" -> "United States", "HONG KONG" -> "Hong Kong", "BRITAIN" -> "Britain".
3. The words "of", "and" and "the" stay lower case unless they open the name: "ISLE OF MAN" -> "Isle of Man",
   "TRINIDAD AND TOBAGO" -> "Trinidad and Tobago".
4. Punctuation and spacing are kept; each side of a hyphen is its own word: "GUINEA-BISSAU" -> "Guinea-Bissau".
5. No country is renamed. "BRITAIN" stays "Britain"; do not turn it into another name.

`with_plain_country(header_figures)` returns a NEW list for the header figures of one company.
6. The entry whose `mnemonic` is `COUNTRY_FULL_NAME` and whose `value` is text is replaced by a COPY with `value`
   set to `plain_country(value)` and a new key `value_as_stored` holding the text as it was.
7. Every other entry is the same object, in the same position. The list handed in and its entries are not changed.
   A list with no such entry comes back as an equal new list.

The 22 values served today, all of which must come out right: BRAZIL, BRITAIN, CANADA, CHINA, FINLAND, FRANCE,
GERMANY, HONG KONG, INDIA, ITALY, JAPAN, MEXICO, NETHERLANDS, PANAMA, PHILIPPINES, SINGAPORE, SPAIN, SWEDEN,
SWITZERLAND, TAIWAN, UNITED STATES, URUGUAY.

Plant tests in `lib/research/api/tests/test_country_name.py`: the 22 values, the three shapes of rules 3 and 4, the
unchanged cases of rule 1, and rules 6 and 7.

You do NOT edit `lib/research/api/scoped_amgt.py`.

**The hookup the adapter cell makes:** where each bundle is assembled, AFTER the figure checks have been computed
from the stored list: `"header_figures": country_name.with_plain_country(header_figures)` in `read_security_overlay`
(`scoped_amgt.py:3472`) and in `read_thesis_bundle` (`:3632`). The checks at `:3447` and `:3628` keep reading the
stored list, so no check result moves.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W295-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited: the round's adapter cell, AMGT-bb-17, makes every hookup. Name yours in your report.
3. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
4. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/country_name.py
lib/research/api/tests/test_country_name.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~295/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb9.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the 22 country values served today read in plain case (22 of 22); small words stay lower and hyphen parts are cased; a plain, empty or non-text value comes back unchanged; the country entry is a re-cased copy with the stored text kept and nothing else moves; C1-C4 PASS; R78 BB9 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb9.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>BA_US_Equity's stored record reads "United States" with "UNITED STATES" kept beside it, the entry count is unchanged and no other value moved; C1-C2 PASS; R78 BB9 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~295 <0.9.0_WK_AMGT_RESAPP~295@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~295/AMGT_RESAPP.TO-AMGT-bb-9.the-country-in-plain-case.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 30870 and round-77 enrichment item 7. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_B_NOTES.md` (cell B3), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~295</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
