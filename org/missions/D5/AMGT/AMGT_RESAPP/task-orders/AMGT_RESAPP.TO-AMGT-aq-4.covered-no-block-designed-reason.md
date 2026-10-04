# AMGT_RESAPP task order -- `AMGT-aq-4` -- Z-S86: A NAME THE ESTATE COVERS WITH NO MODEL BLOCK SERVES THESIS AND PEERS WITH THEIR DESIGNED REASON, NEVER A 404

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aq-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~222</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; the routes read what they read today, plus the declared coverage list.
comp-adversary: RUN by the issuer at the cut -- r67_served c26 FAILS at the base, local and deployed: DE_US_Equity thesis and peers answer 404 ('no security matches: it is not in the identity crosswalk, not a landed model block ...'); the control ZZZZ_US_Equity answers 404.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r67-222` (branch `wk-AMGT_RESAPP-222`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r67-222`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aq-4` (round 67, decomposition s.75; Z-S86, CORPUS round-34 ruling 4)

CORPUS round-34 ruling 4 (row Z-S86): DE_US_Equity (Deere) answers 404 on thesis and peers. Deere has no model block and is not
in the refresh. It is NOT in `lib.research.coverage.covered_universe.covered_security_keys()` (95 keys) and NOT in the identity
crosswalk, so `resolve_identity` refuses it.

1. **Find and name the universe** in which the estate covers Deere (for example the CORPUS coverage list or the research universe the
   CORPUS analysis read). Declare it in code with its source, the same way the other declared lists are.
2. **For a key in that universe with no model block,** `/security/{key}/thesis` and `/security/{key}/peers` answer 200 with their
   designed answer: no fabricated figure, and a plain reason that the name is covered and has no model block yet.
3. **A key covered nowhere** (for example ZZZZ_US_Equity) still answers 404 with its refusal.
4. **The plant test** `lib/research/api/tests/test_covered_no_block.py`:
   - a covered key with no block answers 200 with its reason on both routes;
   - an uncovered key answers 404.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W222-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Every name that answers today keeps its answer; only a covered-without-block name changes from 404 to its designed answer.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~222/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_covered_no_block.py; echo "exit=$?"</invocation><expect>every plant case passes (a covered key with no block: 200 with its reason on thesis and peers; an uncovered key: 404); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c26 --where local; echo "exit=$?"</invocation><expect>C1 PASS on thesis and peers for DE_US_Equity; C2 PASS (ZZZZ_US_Equity 404); R67 C26 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aq-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c14 --where local; echo "exit=$?"</invocation><expect>R64 C14 SERVED: YES (the repairs' reasons and keys unchanged); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~222 <0.9.0_WK_AMGT_RESAPP~222@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~222/AMGT_RESAPP.TO-AMGT-aq-4.covered-no-block-designed-reason.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- the api suite's last line
- the functions you changed
- the universe you named and its source
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-66 analysis @d76db3486c ruling 6; CORPUS round-34 analysis @83cd052a9c ruling 4; row Z-S86. Served by aq-5.

<status>pending</status>
<round>67</round>
<slot>0.9.0_WK_AMGT_RESAPP~222</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
