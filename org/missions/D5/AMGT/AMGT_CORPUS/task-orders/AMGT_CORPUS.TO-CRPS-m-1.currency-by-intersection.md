# AMGT_CORPUS task order -- `CRPS-m-1` -- ROUND 11: a served case's currency is set when the pack's symbol and the listing agree on exactly one ISO code (the intersection)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; the served rewrite is the issuer's drain act.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 11, FIRST of two orders on this slot (the second, `CRPS-m-2`, edits
the same file after this one). Serves **FWD-12** (a value must carry its claim).

## 1. THE CELL -- `CRPS-m-1`

**Where this came from.** `lib/research/corpus/dossier.py` `_case_currency(symbol, listing_currency)` returns
`(currency, currency_basis)` for a served case. Today it sets a currency only when the symbol ALONE maps to exactly one ISO code
(`_SYMBOL_ISO`) AND that code equals the listing; `$` maps to (USD, CAD, AUD), so it never sets. The listing comes from the
name's stored model block (`_listing_currency(model_block)`). The CTO's round-10 analysis, ruling 2: the criterion is
*"a currency only where the pack and the listing agree on exactly one"* -- `$`'s ISO set intersected with a USD listing is
exactly {USD}, so the criterion admits it; the current code is stricter than the rule. The ten symbol-bearing names measured
last round: AZN U+00A3 on GBp; BP/ `$` on GBp; CPA `$` on USD; ML U+20AC on EUR; ORA `$` on EUR; SAP `$` on EUR; SHOP `$` on
CAD; SPOT `$` on USD; TTE `$` on EUR; UNVGY `$` on USD.

**RULED -- what you build:**
1. `currency` = the single element of (the symbol's ISO set in `_SYMBOL_ISO`) intersected with {the listing currency} when that
   intersection has exactly one element; otherwise `null`. `currency_basis` when set: `"symbol's ISO set and the listing agree
   on exactly one code"`; when null, the existing basis values: `"not stated in the pack"` (no symbol),
   `"listing currency not on the block"` (no listing), `"symbol's currency differs from the listing"` (empty intersection).
   The old `"symbol is ambiguous across currencies"` can no longer occur when a listing is present; keep it only if a path
   still produces it, and say which.
2. Nothing converts; the listing never SUPPLIES a currency the symbol does not admit; a symbol with no ISO entry stays null.
3. Implement the rule literally for every name. **By this rule SHOP_CN_Equity (`$` on a CAD listing) gets CAD** -- the analysis
   expected only CPA, SPOT, UNVGY to move; do not special-case SHOP either way. The issuer's never-widen pair decides it before
   anything is served; report SHOP's line explicitly.
6. **AMENDMENT 1 (issuer, on the CTO half's refusal, `ledger/NEVER_WIDEN_ROUND11_DOSSIER_REWRITE_CTO_HALF.md`):** the CTO
   amended its round-10 ruling 2. A currency is set only where the intersection rule of item 1 gives exactly one code AND the
   symbol is NOT a bare `$` on a non-USD dollar listing (CAD, AUD, NZD, HKD, SGD and any other `$`-currency). There the
   currency stays `null` with the basis `"a bare $ on a non-USD dollar listing: the pack may state the reporting currency"`.
   A bare `$` on a USD listing still sets USD; every other symbol keeps the intersection rule. Why (the CTO's measurement):
   SHOP_CN's pack implies a price of ~173.5 against a CAD `PX_LAST` of 206.0 and Shopify reports in USD -- the payload cannot
   tell CAD from USD. Add tests: `$` + CAD -> null with the new basis; `$` + AUD -> null; `$` + USD -> USD.
4. `lib/research/corpus/tests/test_dossier_case_currency_intersection.py` (new): `$` + USD -> USD; `$` + CAD -> CAD; `$` + EUR ->
   null (differs); pound + GBp -> null (differs); euro + EUR -> EUR; no symbol -> null (not stated); no listing -> null.
5. `test_dossier_case_unit.py` may change only where it pins the old ambiguous-`$` outcome; name each such test.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_currency_intersection.py
lib/research/corpus/tests/test_dossier_case_unit.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-m-1.currency-by-intersection.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/m1/`.

## 4. BOUNDS
- Pure ASCII source (symbols as `\u` escapes), LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`. Do not
  change `METHOD_VERSION` in this order (m-2 does). Importing `dossier` must still load no PDF library.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m1_AC2.sh</invocation><expect>(?m)^m1 names 95 currency_set 4 CPA_US_Equity=USD ML_FP_Equity=EUR SPOT_US_Equity=USD UNVGY_US_Equity=USD$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m1_AC3.sh</invocation><expect>(?ms)^m1 SHOP_CN_Equity listing CAD currency None basis a bare \$ on a non-USD dollar listing.*^m1 CPA_US_Equity listing USD currency USD </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe over every resolved name's real extraction and block: exactly CPA, SPOT and
  UNVGY carry USD and ML keeps EUR -- SHOP is NOT in the set (AMENDMENT 1); AC3 the SHOP arm and its control: SHOP_CN reads null
  with the carve-out's basis, a `$` on a USD listing (CPA) still reads USD.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-m-1.currency-by-intersection.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's full line (every set name); SHOP's currency and basis; then the issuer continues you on `CRPS-m-2`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-10 analysis s.2 ruling 2 + s.4 item 1 @`8b54c2b4fd`. The analysis expects "CPA, SPOT, UNVGY -> USD, and
no other name moves"; its own intersection rule also moves SHOP_CN (`$` on CAD) -> CAD. Built literally; decided in the pair.
Checks dry-run at the base: AC1 FAIL (no tests ran); AC2 FAIL ('m1 names 95 currency_set 1 ML_FP_Equity=EUR').
**AMENDMENT 1 (2026-09-29 ~08:5xZ, issuer):** on the CTO half's refusal (SHOP_CN: CAD cannot be told from USD), rule 6 adds the
carve-out; AC2's expect tightened to the exact set without SHOP; AC3 (the SHOP arm + a USD `$` control) added. Dry-run at
trunk b274848977: AC2 FAIL (SHOP_CN=CAD in the set), AC3 FAIL (SHOP currency CAD), its control arm PASS (CPA USD). The order
is REOPENED (`pending`) for the same worker; the CTO re-signs on the re-measured half.

<risk>SERVED</risk>
<status>complete</status>
<round>11</round>
<slot>~1</slot>
<fabric>site-z</fabric>
