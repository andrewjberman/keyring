# AMGT_RESAPP task order -- `AMGT-av-5` -- NUMERIC MEMBER TICKERS RESOLVE OR CARRY A PLAIN REASON; F6'S MEASURE RE-RUN ON SERVED PEERS (DSGN FWD-8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~241</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the crosswalk and the scanner rows are already read; no write.
comp-adversary: RUN by the issuer at the cut -- r72 c44 FAILS on deployed: 94 numeric-ticker members over 24 names, all unresolved and unexplained.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r72-241` (branch `wk-AMGT_RESAPP-241`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-241`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-5` (round 72, decomposition s.80)

PRD v0.39 FWD-8 DONE WHEN (PRD `:549-552`): on every covered name the comparison block's subject identity equals the page's, and
F6's measure re-run reads 0 wrong.

1. **Numeric tickers** (all from `scanner:acwx`): 85 are 6-digit scanner ids; 9 are 4-digit Japanese codes, which map to
   `<code> JT`.
   - In `lib/research/peers/universe.py` (~`:440-475`) or `read_peer_set` (`lib/research/api/scoped_amgt.py` ~`:2138`), resolve each
     through the crosswalk: the JP code form, then a name match. A name match resolved 5 of 94 in the research read.
   - A member that does not resolve serves a plain `ticker_reason` (e.g. "This listing has only an exchange number; we have no
     company match for it yet").
2. **F6's measure re-run on SERVED peers:** write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~241/f6_served.py`.
   - Apply F6's method (overlap >= 6 with the fixed 12-name KPN set, per `deliverables/0.9.0_WK_AMGT_RESAPP~3/f6_remeasure.py`,
     read only) to every covered name's served `/peers` members.
   - Print `F6 WRONG n of N`. Write its own output file; never overwrite ~3's.
3. **Plant tests** in `lib/research/peers/` or `lib/research/api/tests/`.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W241-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add identity or the reason field only. No member is removed.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/peers/
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~241/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c44 --where local; echo "exit=$?"</invocation><expect>population names 95 with non-200 0; C1 PASS failing 0; R72 C44 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~241/f6_served.py"; echo "exit=$?"</invocation><expect>a line `F6 WRONG n of N` with N the covered names that serve members; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~241 <0.9.0_WK_AMGT_RESAPP~241@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~241/AMGT_RESAPP.TO-AMGT-av-5.numeric-member-tickers.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the suites' last lines;
- resolved and reasoned counts;
- the F6 line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 5; DSGN msg 29751 (3). Served by av-8.

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~241</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
