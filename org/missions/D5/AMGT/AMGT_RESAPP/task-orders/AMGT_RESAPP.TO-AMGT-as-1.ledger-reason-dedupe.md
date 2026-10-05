# AMGT_RESAPP task order -- `AMGT-as-1` -- PLAIN WORDS, ONCE: THE /ledger FILINGS REASON STOPS REPEATING ITS CLAUSE; "FOR THE DRIVER CHART"

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-as-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~225</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time reason text and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; only served reason strings change.
comp-adversary: RUN by the issuer at the cut -- r69_served c29 FAILS at the base, local and deployed: C1 95 of 95 covered names' /ledger filings reasons repeat a clause; C2 DE /thesis serves "for driver chart".
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r69-225` (branch `wk-AMGT_RESAPP-225`, cut from the issuance commit with `--portal-ref 6936e92b`). Work and
commit only there. Start every shell call with `cd /c/tmp/r69-225`: a call that starts elsewhere resolves `git rev-parse
--show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-as-1` (round 68 analysis ruling 1; DSGN FWD-27, plain words)

`/security/<key>/ledger` builds each class's `source_reason` in `lib/research/api/scoped_amgt.py`. For the filings class it joins the
class reason to the overlay run-record reason. Both now say the same thing, so every covered name serves:

> "no filings source is set up yet and no filings run is recorded yet for this name: no filings run is recorded yet for this name"

1. **Print the clause once.** When the overlay reason says nothing the class reason does not already say, drop the overlay clause.
   When the overlay reason adds something (for example "the run record could not be read"), keep it.
2. **The article nit.** In the covered-no-block `/thesis` wording, the driver chart reads "... nothing is shown here for driver
   chart". Make it "for the driver chart". Check the other `for <topic>` phrases in the same family and give each its article where it
   reads wrong.
3. **The plant test** `lib/research/api/tests/test_ledger_reason_once.py` covers:
   - a filings class whose overlay reason restates the class reason prints it once;
   - an overlay reason that adds information is kept;
   - the DE driver-chart reason reads "for the driver chart".

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W225-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. If one api test fails only
because it reads a portal function absent at this worktree's portal ref (`test_model_words.py`), name it in your report and file no
row; the issuer grades the suite on the shared tree.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Reason TEXT only. No class, source, run, status code, key or figure moves.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~225/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-as-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_ledger_reason_once.py; echo "exit=$?"</invocation><expect>every plant case passes (a restating overlay clause printed once, an informative one kept, "for the driver chart"); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-as-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round69/checks/r69_served.py" --cell c29 --where local; echo "exit=$?"</invocation><expect>population names 95 with 0 non-200; C1 PASS 0 offenders; C2 PASS 0 hits; R69 C29 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-as-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c28 --where local &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell c25 --where local; echo "exit=$?"</invocation><expect>R68 C28 SERVED: YES and R67 C25 SERVED: YES (plain words hold, every class still sourced or reasoned); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~225 <0.9.0_WK_AMGT_RESAPP~225@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~225/AMGT_RESAPP.TO-AMGT-as-1.ledger-reason-dedupe.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the reason strings you changed, before and after;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-68 analysis @f54b52325e ruling 1; CVO ADJUDICATION_v82 @cc67db12e5. Served by as-2.

<status>pending</status>
<round>69</round>
<slot>0.9.0_WK_AMGT_RESAPP~225</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~03:5xZ):** CLOSED.
- Worker ~225: code `cb7ff2fb1a`, instance at `ce9eb1a5a8`, proof-of-spec-check VALID (rc=0) on the committed bytes.
- AC1 PASS 3 of 3; the mutant (code reverted) fails 2 of 3. AC2 PASS c29 local: 95 names, 570 classes, 0 offenders, 0 hits.
  AC3 PASS r68 c28 + r67 c25.
- The forecast reason also got its article. Served by as-2.

<status>complete</status>
