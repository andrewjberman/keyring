# AMGT_RESAPP task order -- `AMGT-at-3` -- EVERY PEER MEMBER SERVES ITS PRICE CURRENCY, OR A REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~228</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only stores the function already reads; no write. A read of a NEW S3 path is named in your report (the redeploy cell simulates it).
comp-adversary: RUN by the issuer at the cut -- r70_served c32 FAILS at the base on deployed: 95 names, 676 peer members, 676 with no price currency and no reason.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only. A figure or leg that needs a NEW vendor pull is served with a plain reason and filed as a row for Andrew's act, never pulled.
</preflight>

**Your worktree:** `C:/tmp/r70-228` (branch `wk-AMGT_RESAPP-228`, cut from the issuance commit with `--portal-ref 6936e92b`). Work
and commit only there. Start every shell call with `cd /c/tmp/r70-228`: a call that starts elsewhere resolves `git rev-parse
--show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-at-3` (round 70, decomposition s.78; CTO round-69 analysis item 3; DSGN FWD-8)

`/security/<key>/peers` `members` serve `price` and `cap_currency` but no price currency, so the peer page cannot
average its Price column on any name.

1. **Serve `price_currency` on every member,** from the same stored source the member's `price` comes from (the Security Scanner
   universe the Peers engine reads, `lib/research/peers/`).
   - A member whose source carries no currency serves a non-empty `price_currency_reason` in plain words.
   - Do not infer a currency from the country.
2. **The plant test** `lib/research/api/tests/test_peer_price_currency.py` covers:
   - a member with a sourced currency serves it;
   - a member without one serves the reason;
   - `price` and `cap_currency` are unchanged.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W228-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. If one api test fails only because it
reads a portal function absent at this worktree's portal ref (`test_model_words.py`), name it in your report and file no row; the issuer
grades the suite on the shared tree.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add `price_currency` / `price_currency_reason` only. No member, rank, price or cap moves.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block,
   estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/peers/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~228/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_peer_price_currency.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell c32 --where local; echo "exit=$?"</invocation><expect>population names 95 with members read and 0 non-200; C1 PASS 0 members failing; R70 C32 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-at-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py" --cell c14 --where local; echo "exit=$?"</invocation><expect>R64 C14 SERVED: YES (the repaired keys still reach peers); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~228 <0.9.0_WK_AMGT_RESAPP~228@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~228/AMGT_RESAPP.TO-AMGT-at-3.peer-price-currency.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions you changed;
- any new S3 read path;
- any row, including any vendor leg listed for Andrew.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-69 analysis @0bdf5b47ae item 3 and rulings 1-2; routed from DSGN_AMGTV1 FWD-8. Served by at-6.

<status>pending</status>
<round>70</round>
<slot>0.9.0_WK_AMGT_RESAPP~228</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
