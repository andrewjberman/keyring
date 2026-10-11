# AMGT_RESAPP task order -- `AMGT-qq-1` -- A MINOR-UNIT CURRENCY IS NEVER SERVED BESIDE A SCANNER PRICE, AND A SERVED CURRENCY CARRIES NO STALE REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-qq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~381</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-qq-1.a-minor-unit-currency-is-never-served-beside-a-scanner-price</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a serve-time decorator and its test, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read: the currency is read from the record the route already reads; nothing is added to any role.
comp-adversary: RUN at the cut -- r92_currency_guard.py FAILs G1 and G3 at the base and PASSes G2 and G4, and PASSes all four arms against a throwaway candidate (nothing written to the tree). Census of the live function 2026-10-11 (2,230 member rows, 243 subjects): 12 rows serve GBp beside a pound price (AZN, BP, IMB, RIO, SSE); every other served currency equals its record's own CRNCY; 156 rows serve a currency beside a stale reason text.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-381`, cut from the current branch head). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AMGT-qq-1` (round 92, decomposition s.100)

CTO~DELL1 round-91 analysis items 1 and 2 (row C-S55). The peers route serves each member's `price_currency` from the CRNCY header
figure of the member's own record (`lib/research/peers/price_currency.py::price_currency_fields`, called from
`lib/research/api/scoped_amgt.py::_with_price_currency`). The scanner quotes every price in the MAJOR unit of its currency. A record whose
CRNCY is a MINOR-unit code (Bloomberg writes the pence code `GBp` and the South African cents code `ZAc` with a lower-case last letter;
`GBX` and `ILA` are all-capitals) states the quote unit of the RECORD's own price, not of the scanner's. Measured on the live route: 12
member rows on 5 UK securities serve `GBp` beside the scanner's pound price (AZN 120.32 against the record's PX_LAST 11998.0 GBp), a 100x
mislabel; every other served currency (USD 125, CHF 9, EUR 8, JPY 6, HKD 1) equals its record's own CRNCY. Separately, 156 live rows serve a
`price_currency` beside the producer's stored `price_currency_reason` text, which then contradicts the served code. Two changes:

1. In `price_currency.py` add `is_minor_unit(code)`, pure: true for a string of exactly three ASCII letters whose LAST letter is
   lower-case, or that is `GBX` or `ILA`; false for anything else (so `USD`, `EUR`, `CHF`, `SGD`, `JPY`, `HKD`, `GBP`, `ZAR` are false).
   Add `REASON_MINOR_UNIT`, one plain sentence that says the company record states its price in a minor unit (pence, for the UK) while the
   scanner's price is in the major unit, so no currency is shown. In `price_currency_fields`, where the currency comes from a RECORD
   (`currencies[key]`), a minor-unit code is NOT served: return `{"price_currency_reason": REASON_MINOR_UNIT}`. NO conversion, NO
   rewriting of `GBp` to `GBP`, NO inference from the country. The branches for a stored `price_currency` the member already carries and
   for an answered currency (AMGT-oo-5) are unchanged.
2. In `scoped_amgt.py::_with_price_currency`, after the member is merged with its fields, when the served fields carry
   `price_currency`, remove the member's `price_currency_reason` key (it is the producer's stale text); when they carry a reason, behaviour
   is unchanged (the existing code removes `price_currency`).

NOTHING else moves: not `price`, `cap_currency`, `identity`, `price_currency_claim`, the listing rule (`price_listing.py`), any other
decorator or any other member field. Member count and order are unchanged. No stored object is rewritten.

Add the test file `lib/research/peers/tests/test_price_currency_minor_unit.py` (pure, no network, no AWS): one test per rule above, the
major-unit codes served unchanged, a minor-unit code from `currencies` refused, the stored-currency and answered-currency branches
unchanged, and the route-level decorator removing a stale reason when a currency is served and leaving a member with no key on its plain
reason.

ASCII only. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W381-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. Do not touch `lib/research/peers/numeric_tickers.py`, `price_listing.py`, `listed_identity.py` or `lib/research/identity/crosswalk.py`.
5. `scoped_amgt.py` is a large file: make the smallest edit that satisfies section 1; do not reformat or reorder it.

## 3. SURFACES

<paths>
lib/research/peers/price_currency.py
lib/research/api/scoped_amgt.py
lib/research/peers/tests/test_price_currency_minor_unit.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~381/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-qq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_currency_guard.py"; echo "exit=$?"</invocation><expect>PASS G1 (a minor-unit CRNCY serves no currency and a plain reason), PASS G2 (control: a major-unit CRNCY is served unchanged), PASS G3 (route level: GBp becomes a reason, EUR a code with no stale reason, no key a plain reason), PASS G4 (nothing else moves); R92 CURRENCY GUARD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-qq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/peers/tests/test_price_currency_minor_unit.py lib/research/peers/tests/test_price_currency_answered.py lib/research/peers/tests/test_price_listing.py lib/research/api/tests/test_peer_price_currency.py -q; echo "exit=$?"</invocation><expect>the new test file and the three existing price-currency, listing and route-level test files pass with 0 failed, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~381 <0.9.0_WK_AMGT_RESAPP~381@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~381/AMGT_RESAPP.TO-AMGT-qq-1.a-minor-unit-currency-is-never-served-beside-a-scanner-price.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of `price_currency.py` and of `scoped_amgt.py`, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-91 analysis @f6eb45c478 items 1 and 2 (rows C-S55 and the 156 stale reasons); CTO half of the round-91 redeploy pair ADDENDUM 2 @303cc90e42. THE ISSUER'S ERROR it answers: the round-91 redeploy's COO half treated currency as independent of identity; it follows identity through this decorator, and the live base already did this on 12 UK rows. pp-1's identity code is already merged (@62c242efc4); this cell is the currency half, and `AMGT-qq-5` (staged) carries both in ONE redeploy with its expected outcome measured member by member BEFORE the pair is signed (round92_prep/checks/r92_minor_unit_census.py is its close). Design choice, stated: refuse and give a reason, do not translate `GBp` to `GBP`. A translation is measurable (the record's PX_LAST over the scanner price is about 100 on all five securities) but it is an inference about the scanner's unit that the analysis did not rule ("where the unit is unknown, no currency is served"); a later cell may serve the major-unit code with a measured ratio. Checks dry-run at the base: AC1 FAIL (G1, G3; G2 and G4 PASS); AC2 FAIL (the new test file is absent).

<status>pending</status>
<round>92</round>
<slot>0.9.0_WK_AMGT_RESAPP~381</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
