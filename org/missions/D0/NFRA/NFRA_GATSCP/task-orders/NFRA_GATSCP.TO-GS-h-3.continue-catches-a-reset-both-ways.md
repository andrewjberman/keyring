# TO NFRA_GATSCP.TO-GS-h-3 -- round 4 GS-h-3: safe-merge --continue refuses a clean path the merge brought in and the drain reset both ways

<to_id>NFRA_GATSCP.TO-GS-h-3</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~16</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-h-3` (`decompositions/NFRA_GATSCP_DECOMP.round4.md`) | **outcome_ref:** FWD-6 |
**rows:** D1-W13-S1 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

Round 3's GS-f-6 added `_verify_staged_carried` to `.tools/safe-merge.sh` (:318-333): after the merge commit it compares
the paths the commit changes against its first parent with the expected set (captured at :863 from `$STATE` on `--continue` plus
the staged array, checked at :900) and refuses with exit 7 when a path is missing -- EXCEPT a path whose working copy equals HEAD
(:326, `git diff --quiet HEAD -- "$p" && continue`), meant for a conflicted path resolved by keeping the first parent's bytes. Row
D1-W13-S1: that exemption also passes a path the merge brought in CLEANLY from the other parent and the drain then reset in both
the index and the working copy -- a lost change that looks like keep-ours. The CTO ruled (ROUND_ANALYSIS.round3.md section 3): judge
a path reset both ways; a real change is still graded. `.tools/tests/test_safe_merge_continue.py` (14 cases) drives real
conflicted merges in throwaway linked worktrees and prints `SM-CONTINUE ok=<bool> cases=<p>/<t>`.

### THE CELL

`GS-h-3`. Safe-merge --continue refuses a clean path the merge brought in and the drain reset both ways.

**Build:**
1. In `_verify_staged_carried`, apply the keep-ours exemption ONLY to paths that were CONFLICTED in this merge (the
   conflict set safe-merge already records for `--continue`; read how it is stored); a missing path that was not conflicted refuses
   even when its working copy equals HEAD. Exit codes unchanged.
2. Extend `.tools/tests/test_safe_merge_continue.py` with two cases, each printing one line `PASS <name>` or `FAIL <name>`:
   `clean-path-reset-both-ways-refused` (a third file changed only on the other branch, reset in index and working copy before
   `--continue`: exit 7 naming it) and `conflicted-keep-ours-admitted` (a conflicted file resolved to the first parent's bytes:
   exit 0). Keep every existing case; the last line stays `SM-CONTINUE ok=<bool> cases=<p>/<t>`.

### ACCEPTANCE

<criterion id="GH3-AC1" cell_refs="GS-h-3"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/checks/r4_reset_both.py"</invocation><expect>GS-H3-RESET ok=True</expect></criterion>
`GH3-AC1` -- the test is green with at least 16 cases, the clean reset-both-ways case is refused and the conflicted keep-ours case admitted (the negative arm).

<criterion id="GH3-AC2" cell_refs="GS-h-3"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_fastlane.py"</invocation><expect>GS-T3-FASTLANE ok=True</expect></criterion>
`GH3-AC2` -- safe-merge's self-test stays green and the fast lane keeps its tree check (a control).

<expected_criteria>GH3-AC1,GH3-AC2</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~16/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- Do NOT read, grep, copy, quote or attach any `org/**/W73_S*_EVIDENCE.json` (client account data; 0.0.0_AB_MSTR~DELL1 msg
  2718). If a git listing shows such a path, skip it.
- **Proof instance.** Fill `decomp_ref.vintage_commit` and every `commit_or_etag` with a real 7-40 hex commit or
  `PENDING-THIS-COMMIT`; never `HEAD` or a bare `PENDING`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W16-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/safe-merge.sh
.tools/tests/test_safe_merge_continue.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round4.md</decomp_doc> (round 4), cell `GS-h-3`.
<owned_cells>GS-h-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GH3-AC1, GH3-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~16/NFRA_GATSCP.TO-GS-h-3.continue-catches-a-reset-both-ways.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-h-3`,
validated with `python .tools/proof-of-spec-check.py <instance> GH3-AC1,GH3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

### AMENDMENT 1 (2.0.0_SA_COO~N1, 2026-10-09) -- the W73 bound widened (0.0.0_AB_MSTR~DELL1 msg 2745)

The W73 EVIDENCE files are out of the tree but remain in git history. Do NOT `git show`, `git log -p`, `git diff` with content, or
check out commits 1ba8eafcda or f5645bb6e9 or any `W73_S*` path, and do not read anything under
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`. Name-only listings (`--name-only`, `--name-status`) are
allowed; skip any W73 path they show. Graded by: GATE (viii) on the modified order.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 4, battery); BLIND: a refused act that never landed stays UNATTRIBUTED by construction.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @a33d3bde72; ROUND_ANALYSIS.round3.md ADDENDUM 1 @3a618c45ba; decomposition round 4. Base dry-run: see the issuance
commit.
