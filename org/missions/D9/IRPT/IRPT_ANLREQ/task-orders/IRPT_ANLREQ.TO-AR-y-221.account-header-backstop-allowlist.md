# TO IRPT_ANLREQ.TO-AR-y-221.account-header-backstop-allowlist -- the r19.2 backstop rebuilt on the allowlist (r19.3)

<to_id>IRPT_ANLREQ.TO-AR-y-221</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~67</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-221` (`decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~67`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-67` (branch `wk-IRPT_ANLREQ-67`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~67 <0.9.0_WK_IRPT_ANLREQ~67@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W67-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13, after the first worker's report; this order is re-opened and a fresh worker continues in the SAME worktree `C:/dev/wk-irpt-anlreq-67`, slot `~67`, on top of the first worker's commits).** The first worker built the allowlist (a root header enters the backstop only when each word BEFORE the root is a modifier and each word AFTER it is an identifier-tail word; `alias` a tail word, `primary` a modifier; the attribute blocklist removed; READER_VERSION `irpt-template-reader.r19.3`) and its 16 negative and 5 positive controls behave as named (commits 3f9a884a98 controls alone, 55d1755d39 rule). Three EXISTING tests fail only because they use the header `Acct Ref Ext` as a backstop-only positive, and `ext` is in neither word list: `test_an_account_root_header_with_two_identifier_values_is_read_as_an_account_column`, `test_the_backstop_words_say_what_is_seen_and_ask`, `test_a_digit_run_column_with_no_separator_under_a_root_is_read_as_an_account_column`. **The issuer's ruling (the CTO's allowlist: an unknown word keeps a header OUT of the backstop; `ext` is NOT added to the tail words):** change those three tests' HEADER to `Client Primary Acct` (two modifiers and the root: the header rule rejects it, the allowlist admits it, so the tests still exercise the VALUES path; the issuer measured `Client Primary Acct`, `Sub Client Acct` and `Subacc` as `VALUES` with two identifier-like values on the first worker's reader) and keep each test's assertion otherwise; add one negative-control test that `Acct Ref Ext` with two identifier-like values is NOT turned back (the allowlist's price, named); do not touch the rule. Re-run the two checks, keep the proof honest (the first worker's FAIL rows stay; add the new run), commit, flip the order to `complete` only when `y221-allowlist` and `y221-keep` both print OK and the proof is VALID. Gate limb that graded this amendment: none stated (the issuer amends a pending order's text).

### THE CELL (`AR-y-221`, inlined) -- THE BACKSTOP ON THE ALLOWLIST. BUILD. Nothing is released by this order.

*The r19.2 backstop excludes a root header only when it carries one of 17 listed attribute words, and the CVO ran the neighbours that are not on the list (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md`, AR211-y-AC3J): `Acct Cost Basis`, `Acct Gain`, `Acct Weight`, `Acct Description`, `Acct Currency`, `Acct Custodian` are still turned back as two accounts. A list of attribute words cannot be complete.* The CTO withdrew the blocklist ruling and ruled the ALLOWLIST (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` section 2 item 1): a header with an account root enters the backstop only when EVERY other word is an identifier-tail word, with `alias` added to the tail words and `primary` to the modifiers, so `Acct Alias` and `Primary Acct` still read as account columns.

**Read first:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md` (the AR211 section: the six neighbours and the remedy), `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` section 2 item 1, the rule in `infra/aws/lambda/investor-reporting/intake/template_reader.py` (`ACCOUNT_ROOTS`, `ACCOUNT_MODIFIERS`, `ACCOUNT_TAIL_WORDS`, `ACCOUNT_ATTRIBUTE_WORDS`, `_has_account_root`, `_identifier_like`, `_several_accounts`; `READER_VERSION` is `irpt-template-reader.r19.2` at the trunk head) and the r20 record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~60/r20/ACCOUNT_HEADER_REPAIR.json`.

1. **The controls are in the criterion already** (the check `y221-allowlist` lists them); name them FIRST in `r21/ACCOUNT_HEADER_ALLOWLIST.json` (`negative_controls` and `positive_controls`, header and values, exactly the check's lists: the ten r19.2 negatives plus the CVO's six, and the five positives), and commit that file ALONE before the rule changes; say the commit hash.
2. **Change the rule:** a header that carries an account root (`acc`, `acct`, `accnt`, `subacc`) enters the backstop ONLY when every OTHER word of the header is in `ACCOUNT_TAIL_WORDS` (add `alias`) or `ACCOUNT_MODIFIERS` (add `primary`). Replace the attribute-word blocklist by this test (remove the constant if nothing else uses it; if something does, say what). Keep repair (b) of r19.2 (a digits-only run counts as an identifier only when no value in its column carries a number separator). Note in a comment what adding `alias` and `primary` also does to the header rule (`Account Alias`, `Primary Account` become header-rule matches) and keep `ACCOUNT_HEADER_EXCLUDED` as it is.
3. **Move the version legitimately:** `READER_VERSION` becomes `irpt-template-reader.r19.3` and the pin (the digest the stored-input tests carry) moves in the same commit as the rule.
4. **Tests:** in `intake/tests/test_account_value_backstop.py` keep the five named tests, and add one test per negative control (the six neighbours included) and per positive control; every earlier test keeps passing (364 at the base).
5. **Write `r21/ACCOUNT_HEADER_ALLOWLIST.json` (completed):** the rule in words, the tail-word and modifier sets as they now are, the new `READER_VERSION` and digest, the commit hashes, `claim`, `not_read`, and the residual you can still see (a header whose other words are ALL identifier-tail words but whose values are not account numbers).
6. **In your report:** the rule in two sentences, the control commit hash, the new `READER_VERSION` and digest, every existing test whose expectation changed.

### ACCEPTANCE

<criterion id="AR221-y-AC1" cell_refs="AR-y-221"><invocation>python C:/dev/wk-irpt-anlreq-67/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y221-allowlist --root C:/dev/wk-irpt-anlreq-67</invocation><expect>Y221-ALLOWLIST-OK</expect></criterion>
`AR221-y-AC1`: none of the sixteen one-account negative controls (the ten of r19.2 and the CVO's six neighbours) is turned back, the five positive controls (the two-account controls, `Acct Alias`, `Primary Acct`) are, and the five named backstop tests pass.

<criterion id="AR221-y-AC2" cell_refs="AR-y-221"><invocation>python C:/dev/wk-irpt-anlreq-67/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y221-keep --root C:/dev/wk-irpt-anlreq-67</invocation><expect>Y221-KEEP-OK</expect></criterion>
`AR221-y-AC2`: the difference control -- the whole intake test folder passes (364 at the base) and `READER_VERSION` differs from r19.2.

<criterion id="AR221-y-AC3J" cell_refs="AR-y-221" judgment="true"/>
`AR221-y-AC3J` (judgment, graded at L9, never by you): the allowlist closes every attribute neighbour, known or not, keeps both identifier forms, and the controls were named before the rule changed.

<expected_criteria>AR221-y-AC1 AR221-y-AC2 AR221-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_account_value_backstop.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md</decomp_doc>
<owned_cells>AR-y-221</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-y-221.account-header-backstop-allowlist.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-221`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the r20 build (drained @81bf63c241): the rule is used by `_several_accounts` only; the reader is BUILT, NOT RELEASED (live is r18.1), so nothing live changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CVO's round-20 grade against the cell; the lens: an allowlist that turns back a one-account file whose other words happen to be tail words, or that stops reading a real identifier form. The order names sixteen negative and five positive controls, committed alone before the rule. NOT seen: real client headers (0 read; the population is constructed).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis item 1 as round 21 workstream `Y`. Base: `AR221-y-AC1` FAIL as expected (the six neighbours are turned back).
- The r19.3 release pair is item 4, not this order.
