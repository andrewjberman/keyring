# TO NFRA_CTLPLN.TO-CT-ab-5 -- workstream XBLIMB round 1 (cell CT-ab-5): safe-apply's cross-box check stops only on a real open deploy or a real open call (dell2 row D2-S32)

<to_id>NFRA_CTLPLN.TO-CT-ab-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~79</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>XBLIMB</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-5` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-5, FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/safe-apply.sh` (about :92-160) calls `.tools/crossbox-deploy-check.py --files-vs-trunk` (:121) and acts on its verdict (:124-132); it only WARNs today because the switch file `org/mcp/seat-gates.crossbox.safe-apply.enforce` is absent (:94). The CTO's ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_S27_S32_TOOL_FINDING_OWNERS_COMP_IAM_AND_SAFE_APPLY_CROSSBOX_LIMB_20261012.md`, lines about 21-32; read them) keeps it at WARN until two false STOPs are fixed. MEASURED in `.tools/crossbox-deploy-check.py`:
- OPEN-DEPLOY arm, `measure_open_deploy` (about :352-490): runs `git worktree list` (:360) and `git ls-tree HEAD` per worktree (:385) and unions every worktree's `org/critical_paths/.open_deploys/` sentinels. Its only stale filter is "the trunk deleted this sentinel" (:403-441). So a merged, finished worktree whose HEAD still carries an old sentinel reads OPEN (the false STOP; 69 worktree HEADs on dell2).
- OPEN-CALL arm, `measure_open_call` (about :149-207): `mention_patterns` (:88-96) matches a BARE root-name token for Terraform roots (:94-95), and `mentions()` (:99-106) runs that regex over each call's whole JSON plus body (:177) and each row (:200), so a word that happens to equal a root's name stops an apply. It prints no calls-scanned denominator.
- The test file `.tools/tests/test_apply_who_and_crossbox.py` prints `APPLY-GATES-TEST cases=<k>/<n> ok=` and reads `cases=93/96 ok=False` at the base: cases 83 and 84 (the OPEN-DEPLOY race: a worktree removed between the list and the ls-tree read; a worktree listed but unreadable) and one more fail today.

### BUILD

1. OPEN-DEPLOY: a worktree's sentinel counts as OPEN only when that worktree's HEAD is NOT an ancestor of the shared trunk HEAD the check compares against (`git merge-base --is-ancestor <wt HEAD> <trunk>` is false); a worktree whose HEAD is contained in the trunk is not counted, and its sentinel is printed as `STALE-MERGED`. Keep the existing "trunk deleted it" filter. Make the race cases 83 and 84 pass as their text says, and find and fix (or explain in your report) the third failing case.
2. OPEN-CALL: match an open call against a Terraform root only by the root's PATH (`infra/aws/terraform/<root>` or `<root>/`) or by a root named in the call's own `--roots`/`roots` field; never by a bare token in free text.
3. Both arms print a denominator line: `OPEN-DEPLOY worktrees_scanned=<n> open=<k> stale_merged=<m>` and `OPEN-CALL calls_scanned=<n> matched=<k>`.
4. Add cases to `.tools/tests/test_apply_who_and_crossbox.py` (temporary git repositories only): a merged worktree with an old sentinel is not OPEN; an unmerged worktree with a sentinel is OPEN; a call whose text contains a root's bare name but not its path does not match; a call naming the root's path does. Do NOT create the ENFORCE switch file.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No terraform, no aws, no push; tests in temporary directories only. `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; standard library; Python 3.11; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W79-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab5-AC1" cell_refs="CT-ab-5"><invocation>python .tools/tests/test_apply_who_and_crossbox.py</invocation><expect>ok=True</expect></criterion>
`CTab5-AC1` -- every case passes, the old 96 and the new ones (report the whole last line with its denominator).
</proof_of_spec>

<expected_criteria>CTab5-AC1</expected_criteria>

The invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~79/NFRA_CTLPLN.TO-CT-ab-5.crossbox-limb-false-stops.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab5-AC1`, flip `<status>` to `complete` only when it passes and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-5</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-deploy-check.py
.tools/tests/test_apply_who_and_crossbox.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a real open deploy hidden by the ancestor filter (the unmerged-worktree case stays OPEN); a real call missed because it names the root only in prose (the call's roots field and path still match); the switch flipped to ENFORCE by the cell (forbidden); BLIND: a sentinel on a box branch not checked out as a worktree here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round11.md section 3 item 4; CTO ruling @374118e5cd.
