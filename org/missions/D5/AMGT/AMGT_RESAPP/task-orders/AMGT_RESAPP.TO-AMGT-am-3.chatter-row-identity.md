# AMGT_RESAPP task order -- `AMGT-am-3` -- FWD-2: CHATTER ROWS SERVE TICKER, CLASSIFICATION AND PLACES_MOVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~206</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c3 --where deployed FAILS at the base: 0 of 95 rows carry the three keys.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-206` (branch `wk-AMGT_RESAPP-206`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-3` (round 63, decomposition s.71)

`lib/research/api/monthly_chatter.py` `read_monthly_chatter` serves each covered row as `security_key`, `display_name`,
`name_source` and `by_month`. Add, beside `display_name`:
- `ticker`: the row's Bloomberg identifier, from `scoped_amgt.resolve_identity(key)["bloomberg"]` or its display ticker;
- `classification`: the same `classification` block the price ranking rows serve (`scoped_amgt._classification_for_ticker`), or null
  plus a plain `classification_reason` when the table holds none;
- `places_moved`: the same field the price ranking rows serve (`scoped_amgt._join_places_moved`, TRENDING/PRICE axis, the served
  date), or null plus a plain `places_moved_reason` when the name is not ranked.
Read each source ONCE per request, never per row.
Tests in `lib/research/api/tests/`.

**AMENDMENT 1 (issuer, 2026-10-02 ~15:2xZ; CTO msg 28553, DSGN FWD-24):** `/security/<key>/overlay`'s `breakout_price` row also serves
`places_moved`, joined from the BREAKOUT/PRICE rankings row the overlay already reads (VLO: the rankings serve 13 while the page prints
#7). A security with no rankings row (ROG_SW_Equity is the one covered name unranked) serves `places_moved` null plus a plain
`places_moved_reason`. Plant both in a test. AC2's check now carries C3 (VLO's overlay equals its rankings row) and C4 (ROG_SW serves the
reason).

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~206/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c3 --where local; echo "exit=$?"</invocation><expect>C1 PASS (95 of 95 rows carry ticker, classification, places_moved); C2 PASS (95 of 95 tickers non-empty); C3 PASS (VLO overlay breakout_price.places_moved equals its rankings row); C4 PASS (ROG_SW_Equity serves the reason); R63 C3 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~206 <0.9.0_WK_AMGT_RESAPP~206@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~206/AMGT_RESAPP.TO-AMGT-am-3.chatter-row-identity.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** COO~D msg 28526 (DSGN r27 AV-ze-1 reads them the day they serve). Served by am-6.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~206</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
