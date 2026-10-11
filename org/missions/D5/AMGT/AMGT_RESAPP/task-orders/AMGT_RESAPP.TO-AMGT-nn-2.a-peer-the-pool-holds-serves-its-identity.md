# AMGT_RESAPP task order -- `AMGT-nn-2` -- A PEER MEMBER THE IDENTITY POOL HOLDS UNDER `<TICKER> US` SERVES THAT IDENTITY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-nn-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~351</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, one decorator, one test.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only, through the route's own existing readers.
comp-adversary: RUN at the cut -- the live peers route serves 12 of 12 members UNRESOLVED (KlosR/ap8O, 2026-10-11); the crosswalk resolves the bare ticker "INTC" UNRESOLVED and "INTC US" MEASURED (INTC_US_Equity); the check r89_peer_identity.py FAILs I1 at the base (0 of 7) and PASSes I2, I3.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-351`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-nn-2` (round 89, decomposition s.97)

CTO~DELL1 round-88 analysis item 3 (row D1-S16). The peers route (`read_peer_set`, `lib/research/api/scoped_amgt.py`, about line 2270)
serves the stored `peers/v1/<key>/<as_of>.json` with decorators and NEVER rewrites the stored object. Every stored member reads
`identity.resolution` UNRESOLVED because the producer resolved the bare scanner ticker ("INTC"); the crosswalk holds the Bloomberg form
("INTC US" -> `INTC_US_Equity`). Build the same kind of serve-time decorator `_with_numeric_tickers` is (read it, and
`lib/research/peers/numeric_tickers.py`, and `lib/research/api/tests/test_numeric_member_tickers.py`, first):

1. New pure module `lib/research/peers/listed_identity.py` (no read, no write; the route hands in the lookup), with
   `is_us_listed(member)` (true when `member["country"] == "United States"` and `member["ticker"]` is a non-empty ASCII alphabetic
   string) and `listed_fields(member, resolve_form)` returning `{"security_key": key, "identity": identity}` when
   `resolve_form(ticker.strip() + " US")` returns a key, else `{}`. `identity` is the member's prior identity dict copied, with
   `security_key=key`, `resolution="MEASURED"`, `matched_as="us_listed_ticker"`, and any `error` removed (the shape
   `numeric_tickers._matched` builds).
2. In `scoped_amgt.py` add `_with_listed_identity(served)`: for each member that is a dict, `is_us_listed`, has no non-empty
   `security_key`, and whose `identity.resolution` is not already `MEASURED`, replace it with a COPY updated by `listed_fields(member,
   _resolve_held_form)`. Members are never removed or reordered; a member the pool does not hold is left exactly as it was (never a
   guessed key); a `_resolve_held_form` that raises is caught per member and leaves that member unchanged.
3. Wire it into `read_peer_set` so it runs BEFORE `_with_price_currency` (that decorator reads the member's identity key):
   `_with_price_currency(_with_numeric_tickers(_with_listed_identity(_with_reason_classes(...))))`. Nothing else in that chain changes.
4. Tests in the new file `lib/research/api/tests/test_peer_listed_identity.py`, in the style of `test_numeric_member_tickers.py`
   (monkeypatch `scoped_amgt._resolve_held_form`): a US alphabetic member the pool holds gets the key and a MEASURED identity; one the
   pool does not hold is untouched; a non-US member and an all-digit member are untouched; a member already MEASURED is untouched; the
   input list is not mutated; a raising lookup leaves the member as it was.

Do NOT change the producer (`lib/research/peers/engine.py`), the portal, or any stored object. Stamp any surprise row's `surfaced_at`
with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W351-S<k>` (dell1's registered coordinate is D1), `disarm_owner`
`2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `lib/research/api/scoped_amgt.py` (the one decorator and its one call site) and add the two new files named. The
   second order on this worktree (`AMGT-nn-3`) also edits `scoped_amgt.py`; leave its decorator to it.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/peers/listed_identity.py
lib/research/api/tests/test_peer_listed_identity.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~351/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-nn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peer_identity.py" --where local; echo "exit=$?"</invocation><expect>the printed denominators read 12 members and 10 United States members with at least 1 resolvable under '&lt;T&gt; US'; PASS I1 (every resolvable member serves identity MEASURED with the crosswalk's own key and a matching top-level security_key), PASS I2 (no member outside the pool's holdings serves a MEASURED identity), PASS I3 (nothing removed or reordered; ticker, name, price, country equal to the stored object's); R89 PEER IDENTITY: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-nn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_numeric_member_tickers.py lib/research/api/tests/test_peer_price_currency.py lib/research/api/tests/test_adapter_hookups_bb17.py lib/research/peers/tests -q; echo "exit=$?"</invocation><expect>the existing peers and numeric-ticker tests pass with 0 failed (91 passed at the base); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-nn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests/test_peer_listed_identity.py -q; echo "exit=$?"</invocation><expect>the new test file passes with at least 6 tests and 0 failed; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~351 <0.9.0_WK_AMGT_RESAPP~351@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~351/AMGT_RESAPP.TO-AMGT-nn-2.a-peer-the-pool-holds-serves-its-identity.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the number of members served MEASURED and the denominator line AC1 printed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's. Your next order on this slot is `AMGT-nn-3`; the issuer continues you with it.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-88 analysis @6ad172c28d item 3. nn-3 follows on the same slot (one write set). The redeploy that serves this is `AMGT-nn-7` (staged). Item 2 (D1-S14) is NOT served by this order: a resolved key has no model block for a non-held peer, so no currency follows (decomposition s.97a). Checks dry-run at the base: AC1 FAIL (I1 0 of 7); AC2 PASS (a bound, 91 passed); AC3 FAIL (no file).

<status>pending</status>
<round>89</round>
<slot>0.9.0_WK_AMGT_RESAPP~351</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
