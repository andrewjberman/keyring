# NFRA_OPLGTW task order -- `OG-dc-2` -- the colleague kit holds README.md only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-dc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~21</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a doc edit; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- repo only; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ruling is the CTO's (R26, round-20 analysis s.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-dc-2` (decomposition addendum R3-T.14, item 1; row Z-S57)

R26: `.tools/m365-mcp-kit/` still holds `.mcp.json` (the old local Lokka server) and
`.claude/skills/{onedrive,outlook,sharepoint}/SKILL.md` beside the rewritten `README.md`. A colleague who opens
the directory is offered a server that cannot connect. Remove those 4 files with `git rm`, so the directory
holds `README.md` only. If `README.md` mentions the removed skills, fix the mention. Keep it ASCII.
(OG-dc-1's check missed these because a shell `*` glob skips dotfiles and nested directories;
`dc2.AC1` lists with `git ls-files`.)

## 2. BOUNDS

- Repo edits within your paths only; no deploy, no host or AWS write.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
.tools/m365-mcp-kit/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W21-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-dc-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r21/checks/dc2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)kit files 1 \(README\.md only: yes\); files naming Lokka 0; README hosted command lines [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-dc-2.m365-kit-readme-only.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 21 (R3-T.14, item 1). Alone. LOCAL: no release.
- Pre-cut: `dc2.AC1.sh` FAIL (kit files 5; files naming Lokka 4).

<status>pending</status>
<round>21</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
