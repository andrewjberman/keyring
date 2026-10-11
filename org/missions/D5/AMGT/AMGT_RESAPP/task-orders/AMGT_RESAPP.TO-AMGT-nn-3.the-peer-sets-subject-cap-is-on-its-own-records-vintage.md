# AMGT_RESAPP task order -- `AMGT-nn-3` -- THE PEER SET'S SUBJECT MARKET CAP IS ON THE VINTAGE OF THE SUBJECT'S OWN CURRENT RECORD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-nn-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~351</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, one decorator, one test.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only, through the route's own existing model-block reader.
comp-adversary: RUN at the cut -- the stored ASML peers object carries subject cap 541,931.78 at 2026-09-19T07:53:19Z; the subject's current model block (derived/model_block/ASML_NA_Equity/20261010T130156Z) derives 621,657.44 at 2026-10-10T13:01:55Z through engine._subject_from_model_block; r89_subject_cap.py FAILs C1 and C3 at the base and PASSes C2.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the SAME slot as `AMGT-nn-2` -- you are continued on it, with `AMGT-nn-2`'s commits inherited. Work and commit only in that worktree. Start every shell call with `cd` into its path.

## 1. THE ACT -- `AMGT-nn-3` (round 89, decomposition s.97)

CTO~DELL1 round-88 analysis item 4 (row D1-S15). The peers route serves the stored object with decorators and never rewrites it. The
stored `subject` carries the subject's cap as the producer read it at build time (`market_cap_musd`, `market_cap_vintage`,
`cap_vintage`, `cap_source`, `market_cap_raw`); the subject's own current model block is newer. The producer derived those fields with
`engine._subject_from_model_block(security_key, block)` (`lib/research/peers/engine.py`, about line 337). Build a serve-time decorator:

1. New pure module `lib/research/peers/subject_cap.py` (no read, no write) with `refresh_fields(stored_subject, derived_subject)`:
   when `derived_subject["market_cap_musd"]` is a number it returns `{market_cap_musd, market_cap_raw, market_cap_vintage,
   cap_vintage, cap_source}` taken from `derived_subject`, plus `cap_stored_vintage` (the stored `cap_vintage` it replaces) and
   `cap_refresh = {"status": "REFRESHED", "reason": <one plain sentence naming the two vintages>}`; otherwise it returns only
   `cap_refresh = {"status": "ABSENT", "reason": <plain sentence: the subject's own record states no market cap, so the stored figure
   and its vintage are served as they were>}`.
2. In `scoped_amgt.py` add `_with_subject_cap(served, security_key)`: read the subject's block with `_read_model_block_pool(security_key)`
   (the reader `_record_trading_currency` already uses), derive with `engine._subject_from_model_block(security_key, block)`, and copy
   the subject with `refresh_fields` applied. If the block is None, or the read raises, the stored cap fields are served unchanged and
   `cap_refresh = {"status": "UNREADABLE" if the read raised or its record status is POOL_READ_FAILED else "ABSENT", "reason": <plain
   sentence>}` is added. Every other subject field and every member is served exactly as stored.
3. Call it in `read_peer_set` right after `_with_subject_display_name(served, security_key)` and before the other decorators; touch
   no other line of that chain.
4. Tests in the new file `lib/research/api/tests/test_peer_subject_cap.py` (monkeypatch `scoped_amgt._read_model_block_pool`): a fresh
   block replaces the five cap fields and records the stored vintage; an unreadable block (raise) and an absent block (None) leave the
   stored fields unchanged and say why; a block with no cap leaves the stored figure; no member is touched; the stored dict is not
   mutated.

Do NOT change the producer, the portal, member caps, `cap_ratio_to_subject`, or any stored object. Stamp any surprise row's
`surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W351-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `lib/research/api/scoped_amgt.py` (the one decorator and its one call site) and add the two new files named. Leave
   `AMGT-nn-2`'s decorator and module as they are.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/peers/subject_cap.py
lib/research/api/tests/test_peer_subject_cap.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~351/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-nn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_subject_cap.py" --where local; echo "exit=$?"</invocation><expect>PASS C1 (the served subject's market_cap_musd, market_cap_vintage, cap_vintage and cap_source equal the subject's current model block's), PASS C2 (every other subject field and every member's ticker, name, price, cap, ratio and distance equal the stored object's), PASS C3 (an unreadable block serves the stored cap unchanged and says why in cap_refresh); R89 SUBJECT CAP: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-nn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_numeric_member_tickers.py lib/research/api/tests/test_peer_price_currency.py lib/research/api/tests/test_adapter_hookups_bb17.py lib/research/api/tests/test_peer_listed_identity.py lib/research/peers/tests -q; echo "exit=$?"</invocation><expect>the existing peers tests and AMGT-nn-2's new file pass with 0 failed; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-nn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_peer_subject_cap.py -q; echo "exit=$?"</invocation><expect>the new test file passes with at least 5 tests and 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~351 <0.9.0_WK_AMGT_RESAPP~351@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~351/AMGT_RESAPP.TO-AMGT-nn-3.the-peer-sets-subject-cap-is-on-its-own-records-vintage.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the stored and served subject cap and vintage AC1 printed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-88 analysis @6ad172c28d item 4 (D1-S15), the "move to the header's vintage" branch; the "drop with its reason" branch is the ABSENT/UNREADABLE arm (the stored figure is kept and `cap_refresh` says why -- nothing is invented). The portal's subject row already prints the header tile's cap (AV-zzr-1); this brings the API's `peers.subject` to the same record. Member caps and ratios stay as the producer stored them; the stored object is never rewritten. Second order on slot ~351, after nn-2 (one write set, scoped_amgt.py). Served by `AMGT-nn-7`. Checks dry-run at the base: AC1 FAIL (C1, C3); AC2 PASS minus the new nn-2 file (a bound); AC3 FAIL (no file).

<status>pending</status>
<round>89</round>
<slot>0.9.0_WK_AMGT_RESAPP~351</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
