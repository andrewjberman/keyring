# TO NFRA_DEVPLN.TO-DP-d-2 -- round 3 ENRICHMENT DP-d-2: merge-forward falls back to a local-only branch when the default fetch finds the ref absent on origin

<to_id>NFRA_DEVPLN.TO-DP-d-2</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-d-2` (`decompositions/NFRA_DEVPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/portal-merge-forward.sh <branch> --repo <portal>` fetches `origin` for `DEV` and for the branch before it decides (it has a `--no-fetch` to skip that). When the branch exists ONLY locally (never pushed), the fetch of the branch finds no such ref on origin and the script stops with `REFUSED reason=fetch-failed`. That is the wrong refusal: a missing ref on origin is not a network failure, and the script already knows how to read a local branch. MEASURED at the cut: with a real local-only branch `cand/laptop/local-only-probe` in the portal repo, `bash .tools/portal-merge-forward.sh cand/laptop/local-only-probe --repo portal` prints `... result=REFUSED reason=fetch-failed ...`. The portal checkout in your worktree is a linked worktree of the same repository, so that local branch is visible to you (read only; do not fetch).

### BUILD

In `.tools/portal-merge-forward.sh`:
1. The default fetch distinguishes the two causes. Fetch `DEV` first: a failure there is still `fetch-failed` (a network or remote failure refuses). Then check whether the branch exists on origin (`git ls-remote --exit-code origin refs/heads/<branch>`: exit code 2 means the ref is absent, any other non-zero is a failure). Absent on origin: do NOT fetch it, do NOT refuse; continue with the local branch exactly as `--no-fetch` would, and print one stderr line `NOTE: <branch> is not on origin; using the local branch`. Present on origin: fetch it as now. A failed `ls-remote` for any reason other than "absent" is `fetch-failed`.
2. A branch absent BOTH on origin and locally is still `REFUSED reason=branch-not-found` (not `fetch-failed`).
3. The self-test gains cases in its temporary origin and clone: a branch pushed to the origin after the clone is picked up by the default fetch (already covered; keep it); a local-only branch that has an approved fixture row proceeds and merges under the default fetch; a branch absent everywhere is `branch-not-found`; a deliberately broken remote makes `DEV`'s fetch print `fetch-failed`. Every existing case stays; update the case count in the selftest's last line only.

### RULES FOR THIS CELL

Nothing you run pushes, or changes the real portal's DEV, PROD or main tree: tests use `mktemp -d` repositories. The real portal is read only (it is not fetched; the AC2 call below makes one read-only `ls-remote` and `fetch` of DEV on the real origin, which is allowed because it writes only remote-tracking refs). Git Bash default utilities only; quote every expansion. No non-ASCII. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path argument.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W2-S<k>`, next unused k after the highest `W2-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPd2-AC1" cell_refs="DP-d-2"><invocation>bash .tools/portal-merge-forward.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPd2-AC1` -- the self-test, every case (old and new) passing.

<criterion id="DPd2-AC2" cell_refs="DP-d-2"><invocation>bash .tools/portal-merge-forward.sh cand/laptop/local-only-probe --repo portal</invocation><expect>result=REFUSED reason=no-approval-row</expect></criterion>
`DPd2-AC2` -- the seam against the REAL portal repo and the real local-only branch: it now gets past the fetch and is refused for the right reason, no approval row (it touches a non-test file). Nothing is merged, pushed or left behind.
</proof_of_spec>

<expected_criteria>DPd2-AC1,DPd2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-d-2.merge-forward-local-branch.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPd2-AC1,DPd2-AC2`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round3.md</decomp_doc>
<owned_cells>DP-d-2</owned_cells>
</decomp_ref>

<paths>
.tools/portal-merge-forward.sh
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-d-2.merge-forward-local-branch.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Finding inlined: "ref absent on origin" must be told apart from "origin unreachable" by ls-remote's exit code, or an outage would silently fall back to a stale local branch.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round2.md` @8cf96d5f52 item 5 (row W2-S7); W2-S8 is not cut (a checker advisory outside this project's paths). Portal worktree: this order needs `--portal-ref` at the spawn.
