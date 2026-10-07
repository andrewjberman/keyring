# AMGT_RESAPP task order -- `AMGT-bb-22` -- THE DIVERGENCE SCORE READS THE DISPERSION FIELDS BLOOMBERG SERVES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-22</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~306</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- Bloomberg refuses 4 of the 6 names divergence.py asks for (probe of one name, 3 requests, 2026-10-07 15:17Z). Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-306` (branch `wk-AMGT_RESAPP-306`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-306`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-22` (round 78, decomposition s.86)

The divergence score asks for six Bloomberg fields about how far analysts disagree. A probe today showed Bloomberg does not
have four of them under the names our code uses, so the score can never be fed. Change the code to the names Bloomberg serves.

In `lib/research/scores/divergence.py`:
1. `CFPS_FIELDS` becomes `("BEST_CPS_STDDEV", "BEST_CPS", "BEST_CPS_NUMEST")`.
2. `EPS_FIELDS` becomes `("BEST_EPS_STDDEV", "BEST_EPS", "BEST_EPS_NUMEST")`.
3. The order inside each tuple keeps its meaning: standard deviation, then the consensus mean, then the number of estimates.
   Every use in the module reads the tuples by position; change no arithmetic and no guard.
4. Correct the module's opening text where it names the old fields, and say there that the mean is the consensus estimate
   field itself (`BEST_CPS`, `BEST_EPS`).

In `lib/research/scores/tests/test_house_fcf.py` and `lib/research/api/tests/test_score_modules.py`: rename the same four keys
in the test rows. Change no expected number.

Do not edit `lib/research/scores/run_scores.py`: it reads the two tuples and follows them. Do not run it: a store write is the
issuer's act. If any other `.py` under `lib/research/scores/` carries one of the four old names, rename it there and say so.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W306-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. You do not run the scores producer: a store write is the issuer's act.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/scores/divergence.py
lib/research/scores/tests/test_house_fcf.py
lib/research/api/tests/test_score_modules.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~306/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-22"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb22.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the two field lists are the served names; no refused name remains in the score modules or the two test files; C1-C2 PASS; R78 BB22 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-22"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb22.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the score tests pass; B1 PASS; R78 BB22 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~306 <0.9.0_WK_AMGT_RESAPP~306@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~306/AMGT_RESAPP.TO-AMGT-bb-22.divergence-reads-the-served-dispersion-fields.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling msg 31087; AMGT_CORPUS msg 31085. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_D_NOTES.md` (cell D5), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~306</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
