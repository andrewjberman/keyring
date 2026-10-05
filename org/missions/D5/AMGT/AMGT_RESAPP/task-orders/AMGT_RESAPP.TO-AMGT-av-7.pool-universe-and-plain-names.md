# AMGT_RESAPP task order -- `AMGT-av-7` -- THE POOL UNIVERSE DRY-RUN UNBLOCKED (95 OF 95) AND PLAIN DISPLAY NAMES ON PEERS (DSGN FWD-27)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~243</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- the dry-run writes nothing; the `--write-pool` is av-8's store-write leg under a pair.
comp-adversary: RUN by the issuer at the cut -- r72 c47 FAILS (local): `build_universe --dry-run` raises on the missing `sec/harvest/bronze/company_tickers/date=2026-09-22/sec_ticker_cik_cache.json`; r72 c45 FAILS on deployed: 680 of 735 peers subjects/members lack a non-capitals `display_name`.
EGRESS CLASS, declared: NONE. **Never fetch from SEC (that is egress off Opal):** use the newest STORED cache object; if none is stored, file a row and stop on that criterion.
</preflight>

**Your worktree:** `C:/tmp/r72-243` (branch `wk-AMGT_RESAPP-243`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-243`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-7` (round 72, decomposition s.80)

Row Z-W233-S2: the pool universe object `universe/v1/2026-09-16.json` holds 53 of 95 covered names. Its writer is
`lib/research/identity/build_universe.py`, run as `--as-of D --write-pool`. Its last authors were this project's workers.
1. **Unblock the dry-run.** `load_sec_cache` (~`:532`) refuses when the pinned `date=2026-09-22` object is absent. Make it read the
   NEWEST stored object under `sec/harvest/bronze/company_tickers/`, and disclose its date in the output (never a silent fallback).
   Then `--as-of <today> --dry-run` names all 95 covered keys.
2. **DSGN FWD-27:** `/security/<key>/peers` serves `display_name` on the subject and on every member, through `_clean_display_name`
   (`lib/research/api/scoped_amgt.py` ~`:899`): no vendor capitals ("BOEING CO/THE" becomes "Boeing").
3. **Plant tests** for both.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W243-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. NO `--write-pool`, no store write (av-8's leg). No other served field changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/identity/build_universe.py
lib/research/identity/
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~243/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c47 --where local; echo "exit=$?"</invocation><expect>build_universe --dry-run rc 0; covered named 95 of 95; C1 PASS; R72 C47 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c45 --where local; echo "exit=$?"</invocation><expect>population names 95 with non-200 0; C1 PASS failing 0; R72 C45 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~243 <0.9.0_WK_AMGT_RESAPP~243@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~243/AMGT_RESAPP.TO-AMGT-av-7.pool-universe-and-plain-names.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the suites' last lines;
- the SEC cache date used;
- the pool key a --write-pool would write;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 7; row Z-W233-S2; DSGN msg 29751 (4). The pool write is av-8's leg (a served-data move: the pair names its readers).

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~243</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
