# TO NFRA_GATSCP.TO-GS-h-2 -- round 4 GS-h-2: owned-paths-check writes one act key and the act's full path list on every line it logs

<to_id>NFRA_GATSCP.TO-GS-h-2</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~15</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-h-2` (`decompositions/NFRA_GATSCP_DECOMP.round4.md`) | **outcome_ref:** FWD-8 |
**rows:** D1-S7 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/git-hooks/owned-paths-check.sh` takes the agent from `GIT_AUTHOR_NAME` (:124-125), the staged list from
`OWNED_PATHS_STAGED_FILES` or `git diff --cached --name-only` (:168-172), and writes to `AUDIT_LOG` (:115, test seam
`OWNED_PATHS_AUDIT_LOG`). An OVERRIDE (non-empty `GIT_COMMIT_AUTHOR_OVERRIDE`) writes `<ts> OVERRIDE  <agent>  <n>  (--author-override
<VALUE> applied)` and exits 0 before any check (:201-205); a BLOCK writes `<ts> BLOCK  <agent>  <n>  (<k> violation(s): <first three
VIOLATION lines>)` and exits 1 (:259-268); PASS lines are written at :184, :224, :252, :274. Nothing links an OVERRIDE to the BLOCK it
admits, and a BLOCK names only three paths, so a census can only guess (round 3's 26 "false refusals" were such guesses). The CTO
ruled (ROUND_ANALYSIS.round3.md ADDENDUM 1): BLOCK and OVERRIDE lines carry the act key and the full path list.

### THE CELL

`GS-h-2`. Owned-paths-check writes one act key and the act's full path list on every line it logs.

**Build:**
Compute once, after the staged list is known: `ACT_KEY` = the first 12 hex characters of sha256 over the agent serial, a
newline, and the staged paths sorted (`LC_ALL=C sort -u`) and newline-joined (use `sha256sum`; Git Bash has it). Append
` act=<ACT_KEY> paths=<N>:<p1>|<p2>|...` (every staged path, `|`-separated, sorted) to EVERY BLOCK, OVERRIDE and PASS line the hook
writes once the list is known (the merge-exemption and no-staged-files PASS lines may carry `act=none paths=0:`). Move the
OVERRIDE branch below the point where the staged list is read if it is above it. Change no verdict and no exit code. Add a
`--self-test`-free proof: the check below drives the real hook against a temp log.

### ACCEPTANCE

<criterion id="GH2-AC1" cell_refs="GS-h-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/checks/r4_actkey.py"</invocation><expect>GS-H2-ACTKEY ok=True</expect></criterion>
`GH2-AC1` -- a planted act writing outside the seat's paths is still refused, its BLOCK line carries act= and both paths; the same act's OVERRIDE line carries the same key; an own-path act has a different key.

<expected_criteria>GH2-AC1</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~15/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- Do NOT read, grep, copy, quote or attach any `org/**/W73_S*_EVIDENCE.json` (client account data; 0.0.0_AB_MSTR~DELL1 msg
  2718). If a git listing shows such a path, skip it.
- **Proof instance.** Fill `decomp_ref.vintage_commit` and every `commit_or_etag` with a real 7-40 hex commit or
  `PENDING-THIS-COMMIT`; never `HEAD` or a bare `PENDING`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W15-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/git-hooks/owned-paths-check.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round4.md</decomp_doc> (round 4), cell `GS-h-2`.
<owned_cells>GS-h-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GH2-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~15/NFRA_GATSCP.TO-GS-h-2.block-and-override-carry-the-act.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-h-2`,
validated with `python .tools/proof-of-spec-check.py <instance> GH2-AC1` BEFORE the flip.
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
