# TO NFRA_DEVPLN.TO-DP-j-1 -- round 8 ENRICHMENT DP-j-1: the DEV push gate drops its two direct-push exemptions (live FAST lease, plain test-only commit); /closer-drive lands through the merge-forward

<to_id>NFRA_DEVPLN.TO-DP-j-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-j-1` (`decompositions/NFRA_DEVPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-2, FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew changed the CLAUDE.md Portal law (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` row 6; commit `fcdfc34843`, read the Portal bullet at HEAD): portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row. Test-only needs no approver; a live FAST lease is its seat's approval (`open-calls.py approval-lease`, which writes an approval row).
The push gate `.tools/portal-hooks/dev_push_payload_gate.py` (read it whole, about 230 lines) still carries two direct-push exemptions. MEASURED: `python .tools/tests/test_dev_push_payload_gate.py` reads `cases=19/19 ok=True`; `decide()` returns `ADMITTED fast-lease` for any push by a seat with a live FAST lease (around line 183); `route_for()` returns route B for a commit whose changed paths are all test paths (around line 128). `portal-merge-forward.sh` writes the trailer `Approved-By: test-only @-` on a test-only merge (line ~196), which route A cannot verify (the row is `-`).

### BUILD

1. Remove the FAST-lease exemption from `decide()`: a live lease no longer admits a push (delete `fast_lease` and its call, and the module docstring line; keep `DRIVE_MODE_DIR` out of the file). A seat under a lease reaches DEV the same way as anyone: `approval-lease` writes its approval row and `portal-merge-forward.sh` lands the merge (route A).
2. Replace route B (a plain commit of test paths) with route B2: a TWO-parent merge whose body carries `Feature: <branch>` and the trailer `Approved-By: test-only @-`, where EVERY path the merge changes against its first parent matches `TEST_ONLY_RE`. Reuse `changed_paths(portal, parents, commit)`. A merge with that trailer that changes one non-test path is refused with a note naming the route and the path. A plain single-parent test-only commit is refused (route A says "not a two-parent merge"; no route B note admits it). Print `route=B` on a B2 pass (the summary words in the docstring change to match).
3. Tests, `.tools/tests/test_dev_push_payload_gate.py`: INVERT two existing cases (the "test-only commit admitted (route B)" case now expects REFUSED; the "live FAST lease for the serial admitted" case now expects REFUSED) and ADD exactly two: (a) a test-only MERGE with the trailer `Approved-By: test-only @-` is ADMITTED (route B); (b) the same trailer on a merge that also changes a non-test path is REFUSED. The last line goes from `cases=19/19` to `cases=21/21`. Keep every other case, including the real pre-push cases.
4. `.claude/skills/closer-drive/SKILL.md` step 5 (Land it), the Portal bullet: replace "pull-merge DEV, then push DEV yourself ... `.tools/hooks/never-rules-gate.sh` admits a DEV push only from a live FAST lease's seat" with the merge-forward route: write the lease row with `python .tools/open-calls.py approval-lease` as the file says, then `bash .tools/portal-merge-forward.sh cand/<box>/<slug> --push`; DEV only, PROD stays gated; the pre-push hook admits the push only as that approved (or test-only) merge. Keep the own-commits check and the "second seat merges forward, never by force" sentence. Change nothing else in the file. Read `.tools/open-calls.py approval-lease --help` for its flags before you write them.

### RULES FOR THIS CELL

Tests use `mktemp -d` repositories and a temporary state root; no S3 call; the real portal is read only; no push, merge or rebase of the real portal. Python standard library only; ruff clean on the two Python files; no non-ASCII in anything you add. The other open-calls and payload suites stay green (run `python .tools/tests/test_dev_push_payload_gate.py`, `bash .tools/portal-merge-forward.sh --selftest`, `bash .tools/portal-release-build.sh --selftest`). Do not edit `.tools/hooks/never-rules-gate.sh` or `CLAUDE.md` (not in your paths); if the never-rules gate still admits a lease push, append the row below and keep working. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path. Run every command under `timeout 120` or less.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working. Copy the shape of an existing row in that file (schema enums: `class` OBSERVATION or BLOCKING, `hazard_standing` ARMED or INERT, `disposition` UNDER_INVESTIGATION).

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPj1-AC1" cell_refs="DP-j-1"><invocation>python .tools/tests/test_dev_push_payload_gate.py</invocation><expect>cases=21/21 ok=True</expect></criterion>
`DPj1-AC1` -- the gate suite with its two inverted and two added cases (it reads 19/19 at the base).

<criterion id="DPj1-AC2" cell_refs="DP-j-1"><invocation>python .tools/portal-hooks/dev_push_payload_gate.py --portal portal --remote-ref refs/heads/DEV --remote-sha 514df1bbf04d91f88dad30f6336b8992228710a6 --local-sha ab8ecc5662c9166bc4b3ff3d9ba370733ba4d3cf</invocation><expect>route=A</expect></criterion>
`DPj1-AC2` -- the control against the REAL portal: the approved aifill merge that reached DEV is still admitted as route A.

<criterion id="DPj1-AC3" cell_refs="DP-j-1"><invocation>grep -c "portal-merge-forward" .claude/skills/closer-drive/SKILL.md</invocation><expect>^[1-9]</expect></criterion>
`DPj1-AC3` -- `/closer-drive` step 5 names the merge-forward (the count is 0 at the base).

<expected_criteria>DPj1-AC1,DPj1-AC2,DPj1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-j-1.dev-route-only-merge-forward.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPj1-AC1,DPj1-AC2,DPj1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID. Commit with safe-commit under your serial. Report once at the end: criteria with output, commit hashes, rows.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>DP-j-1</owned_cells>
</decomp_ref>

<paths>
.tools/portal-hooks/dev_push_payload_gate.py
.tools/tests/test_dev_push_payload_gate.py
.claude/skills/closer-drive/SKILL.md
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-j-1.dev-route-only-merge-forward.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the base measurements; BLIND to the filesystem around the cited paths. Finding inlined: removing route B alone would make `portal-merge-forward.sh`'s own test-only merge (`Approved-By: test-only @-`) unpushable, so B2 gives that trailer its own check.
lane: the <paths> block IS the grant (worker RULING 1). `.claude/skills/closer-drive/SKILL.md` is the skill the CTO named for this alignment (msg 109110).
</preflight>

Source: 1.0.0_SA_CTO msg 109110 ("cut the pre-push limb's two direct-push exemptions (test-only, live lease) and align /closer-drive step 5 to the merge-forward"); the Andrew-direct record named above; the round-7 analysis list. Portal worktree: this order needs `--portal-ref` at the spawn (the AC2 control reads `portal`).
