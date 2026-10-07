# AMGT_RESAPP task order -- `AMGT-bb-13` -- PEERS V BELOW THREE PEERS READS NOT AVAILABLE WITH ITS REASON (ROW Z-S162)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~298</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- The floors today are 6 peers per measure and 8 for the score; no distinct reason is served below 3. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-298` (branch `wk-AMGT_RESAPP-298`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-298`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-13` (round 78, decomposition s.86)

Add the three-peer rule to Peers V. It lives inside `score_peers_v` in `lib/research/scores/peers_v.py`, so this cell edits
that one existing file (you are its only writer this round) and adds one new test file.

Andrew's word, 2026-10-07: with fewer than 3 peers, Peers V reads not available, with a reason naming the count; it is never
a value computed on 1 or 2 peers.

1. Add a constant `MIN_PEERS_TO_COMPARE = 3` and a function `short_peer_set_reason(count)` returning exactly
   `"0 peers; 3 are needed"`, `"1 peer; 3 are needed"`, `"2 peers; 3 are needed"` (the 3 comes from the constant).
2. In `score_peers_v`, right after the subject is removed from the peer set and `K` is counted: when `K` is below
   `MIN_PEERS_TO_COMPARE`, return at once with `V` None, `K`, `M` an empty list, `state` `classify.ABSENT_SOURCE`, `reason`
   and `absent_reason` both that sentence, and `measures` holding ALL SIX measure ids, each
   `classify.absent(classify.ABSENT_SOURCE, <that sentence>)`. No measure is computed and no other reason is given.
3. At 3 peers or more, change NOTHING: the same keys, values and sentences as today. The older floors stay exactly as they
   are (8 peers for the score, 3 measures, 6 peers per measure), and so do the two `assert` lines and every existing name
   (`MEASURE_NOT_COMPUTABLE_REASON`, `LEGACY_MEASURE_NOT_COMPUTABLE_REASON`, `SCANNER_FACTOR_MAP`, ...).
4. Add one line to the module docstring's GUARDS paragraph stating the rule and its date.
5. Plant tests in a NEW file, `lib/research/scores/tests/test_peers_v_short_set.py`: plants at 0, 1 and 2 peers (the
   sentence on the score and on all six measures; no value anywhere), a plant at 3 (the sentence is not used), a plant at 8
   (a score is served, equal to the score before your change), the subject listed among its own peers is not counted, and
   both row vocabularies.

**You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/scores/run_scores.py`, `classify.py` or
`test_peers_v_mapping.py`.** No adapter hookup is needed: the adapter serves the stored record as written. Say in your
report that the page shows the new sentence only after the scores producer (`run_scores`) is run again, which is a store
write and the issuer's act, not yours.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W298-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. The floors of 6 and 8 are not changed. You do not run the scores producer: a store write is the issuer's act.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/scores/peers_v.py
lib/research/scores/tests/test_peers_v_short_set.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~298/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-13"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb13.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>plants at 0, 1 and 2 peers read no score and the count sentence on the score and on all six measures; the sentence carries no status word or symbol; at 3 peers the sentence is not used; at 8 peers the score is -1.0823626487770477 as before; C1-C4 PASS; R78 BB13 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-13"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb13.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the floors read (8, 3, 6); the two existing test files of this score pass; C1-C2 PASS; R78 BB13 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-13"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb13.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>every plant case in test_peers_v_short_set.py passes; R78 BB13 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~298 <0.9.0_WK_AMGT_RESAPP~298@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~298/AMGT_RESAPP.TO-AMGT-bb-13.peers-v-below-three-peers.proof_of_spec.json`.
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

**ISSUER NOTES:** Andrew's word relayed in CTO msg 30663, row Z-S162. Issuer default: CALLS_AT_THE_CUT_20261007.md section B. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_A_NOTES.md` (cell A4), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~298</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @1423b8974b; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads exit 0 and SERVED: YES; the new sentence is stored only at the next scores run</status>
