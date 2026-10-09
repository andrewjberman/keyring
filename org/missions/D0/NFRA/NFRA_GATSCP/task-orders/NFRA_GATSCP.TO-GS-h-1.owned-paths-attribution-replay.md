# TO NFRA_GATSCP.TO-GS-h-1 -- round 4 GS-h-1: the attribution replay of the census's 26 owned-paths refusals, each tied by a measured commit or UNATTRIBUTED

<to_id>NFRA_GATSCP.TO-GS-h-1</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~14</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-h-1` (`decompositions/NFRA_GATSCP_DECOMP.round4.md`) | **outcome_ref:** FWD-8 |
**rows:** D1-S7 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

Round 3's census (`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~12/GATE_CENSUS_round3.md`) counted 26
"false refusals" of `.tools/git-hooks/owned-paths-check.sh` in the week 2026-10-02T13:57Z..2026-10-09T14:03Z by pairing each BLOCK
line of `org/git-author-override-audit.log` with the first later OVERRIDE line by the same author within 400 lines. The issuer's
base measurement (`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/MEASURE_round4.md`, read it first)
reproduced the 26 pairs and found 19 refusals of the commit's own path (the author committed the blocked path between the BLOCK
and the OVERRIDE), 6 pairs whose OVERRIDE names a different lane than the BLOCK (the BLOCK lines 39887, 39959, 40602, 40786, 40874,
42229), and 1 never committed by anyone (44486). A BLOCK line is `<ts> BLOCK  <agent>  <n>  (<k> violation(s): VIOLATION: <path> --
lane=<L> ...; ...)` (first three violations only); an OVERRIDE line is `<ts> OVERRIDE  <agent>  <n>  (--author-override <LANE>
applied)`. The CTO ruled (ROUND_ANALYSIS.round3.md ADDENDUM 1): each of the 26 is tied by a measured commit hash or act key, never
"most likely"; anything untied prints UNATTRIBUTED.

### THE CELL

`GS-h-1`. The attribution replay of the census's 26 owned-paths refusals, each tied by a measured commit or UNATTRIBUTED.

**Build:**
Write, in your deliverables folder, a script `replay_owned_paths.py` and its output
`OWNED_PATHS_REPLAY_round4.json`: a list of exactly 26 objects, one per census pair, each
`{"block_line": <1-based line number in the log>, "author": <serial>, "paths": [<violating paths on that BLOCK line>],
"tie": "OWN-PATH" | "OTHER-ACT" | "UNATTRIBUTED", "commit": <hex or null>, "evidence": <one sentence>}`.
- `OWN-PATH`: `commit` is a commit authored by that serial (`git log --author`) that carries at least one of the paths
  (`git show --name-only`), landed after the BLOCK.
- `OTHER-ACT`: `commit` is the commit the paired OVERRIDE actually served (same author, landed within minutes after the OVERRIDE,
  carrying the OVERRIDE's lane's paths) and it carries NONE of the BLOCK's paths.
- `UNATTRIBUTED`: neither can be measured; `commit` is null and `evidence` says what was searched.
Never write "likely" or "probably". Also write `OWNED_PATHS_REPLAY_round4.md`: the counts per tie, the denominator, and the rule.
Edit no tool, no log.

### ACCEPTANCE

<criterion id="GH1-AC1" cell_refs="GS-h-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/checks/r4_replay.py"</invocation><expect>GS-H1-REPLAY ok=True</expect></criterion>
`GH1-AC1` -- 26 distinct BLOCK lines; every OWN-PATH tie re-measured against git (author and path); every OTHER-ACT commit carries none of the paths; UNATTRIBUTED names no commit.

<expected_criteria>GH1-AC1</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~14/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- Do NOT read, grep, copy, quote or attach any `org/**/W73_S*_EVIDENCE.json` (client account data; 0.0.0_AB_MSTR~DELL1 msg
  2718). If a git listing shows such a path, skip it.
- **Proof instance.** Fill `decomp_ref.vintage_commit` and every `commit_or_etag` with a real 7-40 hex commit or
  `PENDING-THIS-COMMIT`; never `HEAD` or a bare `PENDING`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W14-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round4.md</decomp_doc> (round 4), cell `GS-h-1`.
<owned_cells>GS-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GH1-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~14/NFRA_GATSCP.TO-GS-h-1.owned-paths-attribution-replay.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-h-1`,
validated with `python .tools/proof-of-spec-check.py <instance> GH1-AC1` BEFORE the flip.
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
