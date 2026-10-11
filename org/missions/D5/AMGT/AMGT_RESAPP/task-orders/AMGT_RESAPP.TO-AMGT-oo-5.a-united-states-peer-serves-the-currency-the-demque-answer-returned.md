# AMGT_RESAPP task order -- `AMGT-oo-5` -- A UNITED STATES PEER SERVES THE CURRENCY THE DEMQUE ANSWER RETURNED (pure half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-oo-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~362</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-oo-5.a-united-states-peer-serves-the-currency-the-demque-answer-returned</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a pure function and its test, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud call; this cell reads no store (the answer is a function argument).
comp-adversary: RUN at the cut -- r90_currency_answered.py FAILs C1-C4 at the base (the function has no `answered` parameter) and PASSes C5, and PASSes all five arms against a candidate implementation held in a throwaway runner (nothing written to the tree).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-362`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AMGT-oo-5` (round 90, decomposition s.98)

CTO~DELL1 round-89 analysis item 1 (D1-S14, United States rows). A peer member's `price` is the Security Scanner's row price and the
row carries no currency field. `lib/research/peers/price_currency.py` serves a member's currency from its own company record's
`CRNCY` header figure, or a plain reason. Request `AMGT_RESAPP-S14-CRNCY-SCANNER-US` (MDPF_DEMQUE) returns CRNCY for the United
States scanner rows. This cell is the PURE half that consumes that answer; it reads no store.

Change `price_currency_fields(member, currencies, unreadable=())` to `price_currency_fields(member, currencies, unreadable=(),
answered=None)`:

- `answered` is a dict mapping a bare scanner ticker (upper case) to the currency code the answer returned, or None;
- precedence, unchanged where `answered` is None: a `price_currency` the member already carries; then no price -> `REASON_NO_PRICE`;
  then a record key whose stated currency is in `currencies`; THEN, NEW, the answer; then the existing reasons;
- the answer is used only when ALL hold: `answered` is a dict; the member's `country` equals `"United States"`; its `ticker` is a
  non-empty ASCII alphabetic string; `ticker.upper()` is a key of `answered`; the value is a string of exactly three upper-case ASCII
  letters; and the member has no record key, or its record states no currency (`REASON_NO_RECORD` and `REASON_NO_FIGURE` are the two
  reasons it replaces; `REASON_UNREADABLE` and `REASON_NO_PRICE` stay);
- the served fields for an answered member are exactly `{"price_currency": <code>, "price_currency_claim": "measured",
  "price_currency_source": "DEMQUE:AMGT_RESAPP-S14-CRNCY-SCANNER-US"}`; no `price_currency_reason` key beside them;
- NOTHING infers a currency: not from the country, the exchange, the cap currency or a default. A member the answer does not cover
  keeps its reason and carries no `price_currency` key;
- `price` and `cap_currency` are never touched; no existing caller's output changes when `answered` is not passed.

Add the test file `lib/research/peers/tests/test_price_currency_answered.py` (pure, no network, no AWS): one test per rule above and
one per negative arm (uncovered US member; non-US member sharing an answered ticker; a malformed answered value: blank, two letters,
lower case, a word; a record that states its own currency wins over the answer; `answered=None` equals the old output).

Do NOT edit `lib/research/api/scoped_amgt.py` or any reader, and do not add a loader for the answer: where the answer lives and its
shape are not decided, and the reader and wiring are a later cell.

ASCII only. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W362-S<k>`,
`disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. Do not add a key, a default or an inference that is not in section 1.

## 3. SURFACES

<paths>
lib/research/peers/price_currency.py
lib/research/peers/tests/test_price_currency_answered.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~362/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-oo-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round90_prep/checks/r90_currency_answered.py"; echo "exit=$?"</invocation><expect>PASS C1 (a covered United States member serves the answered code as MEASURED with its source), PASS C2 (an uncovered member keeps its plain reason, no currency key), PASS C3 (a non-United-States member sharing an answered ticker is not served), PASS C4 (a malformed answered value is never served), PASS C5 (every round-89 case is byte-equal); R90 CURRENCY ANSWERED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-oo-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/peers/tests/test_price_currency_answered.py lib/research/api/tests/test_peer_price_currency.py -q; echo "exit=$?"</invocation><expect>the new test file and the existing route-level price-currency test both pass with 0 failed, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~362 <0.9.0_WK_AMGT_RESAPP~362@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~362/AMGT_RESAPP.TO-AMGT-oo-5.a-united-states-peer-serves-the-currency-the-demque-answer-returned.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of `price_currency.py`, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-89 analysis @34a0c14300 item 1. The item is STAGED on the DEMQUE answer (a dependency between two projects, never a wait on time); THIS order is its pure half, which depends on none of that and so runs now (obligation 2: an uncovered FWD-serving cell with no unmet dependency is cut this tick). The DEMQUE request `AMGT_RESAPP-S14-CRNCY-SCANNER-US` is filed (@b6e42f51a8), carries no quote and no answer yet, and the answer's address and shape are not stated in the DEMQUE PRD (its C-HOMES names only the demand ledger and the standing-request state object). THE WIRING IS CELL `AMGT-oo-6`, STAGED, ITS ORDER CUT AT THE GO (a face cannot be sufficient before the answer's address and shape exist). It waits on: (1) the answer landing, with its address and shape read by the issuer; then it adds the one reader (the answer's address from builder output, `lib/opal_naming.py address()`; a failed or absent read serves NO currency and names why) and its wiring at the call site in `lib/research/api/scoped_amgt.py`, with a criterion that runs against the real answer and the round-90 NEGATIVE arm (a peer with no answer keeps its reason). The CTO is told in the round's one message that oo-6 has no order yet and why. The pure half is cut now because it depends on none of those: it takes the answer as an argument. SERVED reach needs a later redeploy of `opal-amgt-scoped-api` (a WORLD seat order under its own never-widen pair; nn-5's `crosswalk.py` rides there only by blob). 138 of the 1,038 requested rows are held names whose currency is already served (round90_prep/ISSUER_READS.md). Checks dry-run at the base: AC1 FAIL (C1-C4; C5 PASS); AC2 FAIL (the new test file is absent).

<status>pending</status>
<round>90</round>
<slot>0.9.0_WK_AMGT_RESAPP~362</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- issuer close 2026-10-11T06:0xZ (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-362 @34167321f0 (code 4872a357ff) merged @a423f1d667, proof instance VALID (worker run and issuer re-run); issuer re-run in the worktree: AC1 R90 CURRENCY ANSWERED YES (C1-C5), AC2 42 passed; drain checks py_compile rc 0, ruff clean, 122 passed over the peers folder and the two api tests. The pure half only: the reader and its wiring are AMGT-oo-6 (staged on the DEMQUE answer). Rows: none.</status>
