# AMGT_RESAPP task order -- `AMGT-bb-8` -- EACH PEER PRICE WITH THE CURRENCY OF ITS OWN LISTING (FWD-8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~294</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_B_NOTES.md) -- price_currency is served on 25 of 676 priced peer rows; 3 of those 25 carry another listing's currency. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-294` (branch `wk-AMGT_RESAPP-294`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-294`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-8` (round 78, decomposition s.86)

A peer row's price comes from the Security Scanner, which quotes each price in that listing's own trading currency
and stores no currency beside it. Today the page is served the currency of the peer's matched company record. That is
right when the record is the same listing as the price, and wrong when it is not: Taiwan Semiconductor's Taiwan price
of 2,365 is served with "USD" because the company matched to its US listing.

Create `lib/research/peers/price_listing.py` (standard library only) exporting ONE function:

`record_for_price(member, resolve)` returns `{"record_key": <key or None>, "basis": <word or None>, "reason": <sentence or None>}`.
- `member` is one peer row as served: it carries `ticker`, `country` (the scanner's country name, such as
  "United States" or "Taiwan"), and `identity`, a dict whose `security_key` is the company record the row was matched
  to, or `None`.
- `resolve` is a function the caller hands in: `resolve("MSFT US")` returns a record key or `None`. Do not import the
  pool list yourself.

Rules, in order:
1. **Own ticker.** The row has a record key and the row's `ticker` equals the key's first part (the text before the
   first underscore: `HD` for `HD_US_Equity`, `8306` for `8306_JP_Equity`). Return that key, `basis: "own_ticker"`.
2. **Refused: a US listing behind a foreign price.** The row has a record key that ends `_US_Equity`, its ticker is
   not the key's first part, and its `country` is not "United States". Return no key, no basis, and this reason:
   "This price is quoted on the company's home exchange. The company record we hold is its United States listing, so
   that record's currency is not used for this price."
3. **Name match, same country.** The row has any other record key. Return it, `basis: "name_match"`.
4. **US ticker.** The row has no record key, its `country` is "United States" and its `ticker` is letters only. Ask
   `resolve(ticker + " US")`. If it returns a key, return it with `basis: "us_ticker"`.
5. **Otherwise** return `{"record_key": None, "basis": None, "reason": None}`. For a row that is not a United States
   row with a letters-only ticker, do not call `resolve` at all.
6. Never work out a currency from a country, an exchange code or the market-cap currency. This function chooses a
   record or refuses one; the currency is read from that record by the caller.
7. The reason uses none of: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate,
   stage, input ledger, bronze.

Plant tests in `lib/research/peers/tests/test_price_listing.py`: one case per rule, the `BRK.B` ticker (not letters
only: rule 5), and a `resolve` that raises (let it raise; the caller decides).

You do NOT edit `lib/research/api/scoped_amgt.py` or `lib/research/peers/price_currency.py`.

**The hookup the adapter cell makes:** in `_with_price_currency` (`scoped_amgt.py:2371-2400`), the record asked for a
row's currency becomes `price_listing.record_for_price(m, _resolve_held_form)["record_key"]` in place of
`price_currency.member_record_key(m)` (`:2382-2384`; `_resolve_held_form` is at `:2328-2333`). At `:2398`, a row whose
answer carries a `reason` is served `price_currency_reason` equal to that reason and no `price_currency`. The currency
itself is still read by `_record_trading_currency` (`:2357-2368`).

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W294-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited: the round's adapter cell, AMGT-bb-17, makes every hookup. Name yours in your report.
3. This cell does not close FWD-8: about 600 rows have no currency in any stored file. Do not add a vendor call to find one.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/peers/price_listing.py
lib/research/peers/tests/test_price_listing.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~294/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb8.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>HD keeps its own record; the Taiwan row matched to TSM_US_Equity is refused with a plain reason; Roche keeps its Swiss record; MSFT takes the record named for "MSFT US"; Samsung gets none and the list is not asked; C1-C5 PASS; R78 BB8 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb8.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>over the stored peer sets of 2317_TT_Equity, BA_US_Equity and VLO_US_Equity every row gets an answer, the row 688910 matched to TSM_US_Equity is refused, and no answer pairs a US-listing record with a row from another country; C1-C3 PASS; R78 BB8 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb8.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the existing price-currency tests still pass; R78 BB8 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~294 <0.9.0_WK_AMGT_RESAPP~294@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~294/AMGT_RESAPP.TO-AMGT-bb-8.peer-price-with-its-own-listing-currency.proof_of_spec.json`.
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

**ISSUER NOTES:** DSGN_AMGTV1 FWD-8, carried by CTO round-77 enrichment item 7 and msg 31020. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_B_NOTES.md` (cell B2), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~294</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
