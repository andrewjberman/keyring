# TO NFRA_DEVPLN.TO-DP-e-4 -- round 4 ENRICHMENT DP-e-4: the structural close of S03 -- a DEV payload limb in the portal repo's pre-push hook

<to_id>NFRA_DEVPLN.TO-DP-e-4</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~3</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-e-4` (`decompositions/NFRA_DEVPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-3, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Portal DEV is to be written only through `.tools/portal-merge-forward.sh`, which refuses without an approved row and merges with two trailers. A command gate (`.tools/hooks/never-rules-gate.sh`) sees only the command a seat types, so a seat running its OWN script that does `git push origin ...:DEV` is invisible to it. The structural close is a check in git's own `pre-push` limb of the portal repo, which runs on every push, typed or scripted. The portal repo's hook is `.tools/portal-hooks/pre-push` (its installed copy `portal/.git/hooks/pre-push` is byte-identical; install is a copy by `.tools/portal-hooks/install.sh`, NOT part of this order). It already runs a VALGATE D-1 gate per pushed ref in a `while read -r local_ref local_sha remote_ref remote_sha` loop. Read it.

### BUILD

1. A new checker `.tools/portal-hooks/dev_push_payload_gate.py` (Python standard library): `python dev_push_payload_gate.py --local-sha <sha> --remote-sha <sha> --remote-ref <ref> [--portal <repo path, default .>] [--prod-ref origin/PROD]`. Prints ONE last line `DEV-PUSH-GATE result=ADMITTED|REFUSED|SKIPPED reason=<token|-> commits=<n>`; exit 0 for ADMITTED and SKIPPED, 1 for REFUSED.
2. `--remote-ref` other than `refs/heads/DEV`: `SKIPPED reason=not-dev`. A delete (local sha all zeros), a new branch (remote sha all zeros) or a push whose remote sha is not an ancestor of the local sha: `REFUSED` with reason `delete`, `new-ref` or `not-fast-forward`.
3. Otherwise walk `git rev-list --first-parent --reverse <remote-sha>..<local-sha>`. Each commit must pass at least one route; a commit that passes none is listed (short sha, subject, why) and the whole push is `REFUSED reason=unapproved-commit`:
   - ROUTE A, an approved feature: the commit has exactly two parents and its message body carries both `Feature: <branch>` and `Approved-By: <who> @<row>`, and the approval reader says `APPROVED valid=yes` for `<branch>` with `row` equal to the trailer's row and `head_sha` equal to the commit's SECOND parent. Call the reader as `${OPAL_APPROVAL_STATUS_CMD:-python <hook dir>/../open-calls.py approval-status} --branch <branch>` (its ONE output line grammar: `APPROVAL branch=<b> state=<ABSENT|OPEN|APPROVED|DECLINED|UNREADABLE> valid=<yes|no|-> row=<id|-> by=<who|-> head_sha=<sha|-> commits=<n|-> class=... box=... pages=...`). An unreadable or unparsable reader is not-approved (fail closed).
   - ROUTE B, test-only (CLAUDE.md law): every path the commit changes against its first parent matches `(^|/)(__tests__|__harness__|__fixtures__|__mocks__)/|\.(test|spec)\.[cm]?[jt]sx?$|(^|/)(tests?|e2e|fixtures?)/` and there is at least one path.
   - ROUTE C, a PROD-into-DEV back-merge (settlement rule): the commit has two parents and its second parent is an ancestor of `--prod-ref`.
4. A live FAST lease (CLAUDE.md law): if `$OPAL_AGENT_SERIAL` equals the `seat` of a lease file in `${DRIVE_MODE_DIR:-<workspace>/org/mcp/drive_mode}/*.json` whose `mode` is `FAST` and whose `expires_epoch` is greater than now, the whole push is `ADMITTED reason=fast-lease` (print which lease file). An absent, expired or unreadable lease admits nothing.
5. In `.tools/portal-hooks/pre-push`, inside the existing per-ref loop and after the VALGATE D-1 block, call the checker for a ref that is exactly `refs/heads/DEV`; if it exits non-zero set the push blocked and print its lines plus one line `ERROR: portal DEV is written only through .tools/portal-merge-forward.sh (an approved feature row)`. Resolve the checker the same way the hook resolves the D-1 gate (canonical source or installed copy); if the checker cannot be found print `WARN` and do NOT block (a missing checker must not stop work on a box that has not installed it). Change nothing else in the hook.
6. Test `.tools/tests/test_dev_push_payload_gate.py` on temporary git repositories (a bare origin, a clone, DEV and PROD branches) with a fixture approval command: route A admitted; route A with a different row, with a head that is not the second parent, with state OPEN, and with an unreadable reader each refused; a plain commit refused; a test-only commit admitted; a PROD-into-DEV back-merge admitted; a non-DEV ref skipped; a delete, a new ref and a non-fast-forward each refused; a live FAST lease for `$OPAL_AGENT_SERIAL` admitted and an expired one not. Also drive the real `pre-push` script with a pushed-ref line on stdin for one admitted and one refused case. Last line `DEV-PUSH-GATE-TEST cases=<k>/<n> ok=True|False`.

### RULES FOR THIS CELL

Read only against the real portal; every write is in temporary directories. You do NOT install the hook (do not touch `portal/.git/hooks`), push, merge or rebase. No non-ASCII. Python standard library only; ruff clean; the bash edit stays Git Bash default utilities only. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W3-S<k>`, next unused k after the highest `W3-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPe4-AC1" cell_refs="DP-e-4"><invocation>python .tools/tests/test_dev_push_payload_gate.py</invocation><expect>ok=True</expect></criterion>
`DPe4-AC1` -- the test above, every case passing.

<criterion id="DPe4-AC2" cell_refs="DP-e-4"><invocation>python .tools/portal-hooks/dev_push_payload_gate.py --portal portal --remote-ref refs/heads/DEV --remote-sha a577cba5644192bf1f62b10dc03dd3657e12b59f --local-sha 24877b67b7a175bcfe73c779f69c0bf7c3c639c8</invocation><expect>DEV-PUSH-GATE result=ADMITTED</expect></criterion>
`DPe4-AC2` -- the seam against the REAL portal: the one push that really reached DEV through the route (the integrator's merge `24877b67` of `cand/laptop/contributing-boxes`, row 9e8a, read through the real `approval-status`) is admitted.

<criterion id="DPe4-AC3" cell_refs="DP-e-4"><invocation>python .tools/portal-hooks/dev_push_payload_gate.py --portal portal --remote-ref refs/heads/DEV --remote-sha 10e7664d6c4824cb88f04acf47f06264345b5b8b --local-sha b5222d78784e779fe0411516b5073f697665bded</invocation><expect>DEV-PUSH-GATE result=REFUSED</expect></criterion>
`DPe4-AC3` -- the difference control on the real portal: the declined example's plain commit pushed onto DEV is refused.
</proof_of_spec>

<expected_criteria>DPe4-AC1,DPe4-AC2,DPe4-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~3/NFRA_DEVPLN.TO-DP-e-4.dev-push-payload-limb.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPe4-AC1,DPe4-AC2,DPe4-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round4.md</decomp_doc>
<owned_cells>DP-e-4</owned_cells>
</decomp_ref>

<paths>
.tools/portal-hooks/dev_push_payload_gate.py
.tools/portal-hooks/pre-push
.tools/tests/test_dev_push_payload_gate.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-e-4.dev-push-payload-limb.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the three exemption routes; BLIND to the filesystem around the cited paths. Findings inlined: every exemption widens what DEV admits, so each is a named route with its own test and its own refusal control; the limb fails closed on an unreadable reader; a missing checker warns and does not block (it must not stop a box that has not installed it).
lane: the <paths> block IS the grant (worker RULING 1). The hook's lane owner signs the limb before install (CTO addendum); install is not this order.
</preflight>

Source: `ledger/ROUND_ANALYSIS.round3.md` @75335735b6 ADDENDUM ~22:3xZ (CTO msg 108963): "the structural close is a payload check in the portal repo's git pre-push limb ... a round-4 cell for this project". The CTO's named file is the workspace repo's hook; the portal repo's own hook is `.tools/portal-hooks/pre-push` (issuer reading, recorded in the decomposition). Portal worktree: this order needs `--portal-ref` at the spawn.
