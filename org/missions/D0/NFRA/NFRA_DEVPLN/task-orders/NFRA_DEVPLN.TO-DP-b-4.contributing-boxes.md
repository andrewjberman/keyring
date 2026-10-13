# TO NFRA_DEVPLN.TO-DP-b-4 -- round 1 THREAD DP-b-4: `portal/CONTRIBUTING-BOXES.md` and the worker definition's portal step

<to_id>NFRA_DEVPLN.TO-DP-b-4</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~4</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-b-4` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-3, FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Every box must answer the same way where its portal feature lives and whose approval it needs. Write ONE page for every box to read, in the portal repo, and a short portal step in the worker definition.
Your worktree has the portal repo checked out at `portal/` (a linked worktree on its own branch). Write the page THERE (`portal/CONTRIBUTING-BOXES.md`), at most 90 lines, plain ASCII, headings and short bullets.

### THE PAGE SAYS (all of it, nothing else)

1. A FEATURE is one branch of the portal repo with a stated purpose and the pages it changes. Its name is `cand/<box>/<slug>` (`<box>` is the building box's name from `lib/devices.py`). One feature, one branch, one approval.
2. Build in a linked worktree on that branch: `git -C portal worktree add <path> -b cand/<box>/<slug> <last PROD release>`. The branch is cut from the last PROD release (the commit the last promote shipped; read it with
   `git -C portal rev-parse origin/PROD`), never from DEV, so it carries only its own commits. A branch cut from DEV is re-cut onto the PROD release by its owner before it is registered (a feature branch is not a shared branch).
3. Push the branch to origin under that name. Nothing of it is on DEV until approved: a box never pushes DEV.
4. Register it for approval: `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box <box> --branch cand/<box>/<slug> --purpose "<text>" --pages "<p1,p2>" --class <class> --how "<how to look at it>" --portal portal`
   (the tool reads the head and commit count itself and refuses a branch that carries commits already on DEV; `python .tools/open-calls.py add --help` is the authority on the options).
5. Whose approval, by class (the builder declares the class; the box CTO may raise it, never lower it; unsure is client-facing): `client-facing` (a page a partner-firm or client login can open) waits for Andrew;
   `opal-internal` (staff-only) waits for the building box's CTO lane; `test-only` (tests, fixtures, mocks only) waits for nobody.
6. After the row is closed `approved`, the feature reaches DEV only through `bash .tools/portal-merge-forward.sh cand/<box>/<slug>`, which merges and adds the `Feature:` and `Approved-By:` trailers. A declined feature stays on its branch.
7. PROD carries only approved features: the promote takes a list (`bash .tools/portal-release-build.sh --features <list>`), never live DEV whole.
8. One line: the answer to "may I push DEV?" is always "not until approved".

Then, in `.claude/agents/worker.md` (a workspace file in YOUR worktree, not under `portal/`), add ONE short subsection of at most 8 lines titled `**Portal changes.**` placed after the **Surprise.** paragraph: a portal change is made in the portal worktree
on a `cand/<box>/<slug>` branch, never pushed to DEV, registered by the issuer, and `portal/CONTRIBUTING-BOXES.md` is the rule. Change nothing else in that file; do not touch its frontmatter.

### RULES FOR THIS CELL

Commit the page inside the portal worktree with the portal repo's own `git add portal/CONTRIBUTING-BOXES.md` / `git commit -F <msgfile>` (message file written with the Write tool); if that commit is refused, leave the file uncommitted and file a
surprise row; the issuer commits it. Commit `worker.md` and the proof instance in the workspace worktree with `safe-commit.sh` as your definition says. No push anywhere. No non-ASCII.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPb4-AC1" cell_refs="DP-b-4"><invocation>bash org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/2.0.0_SA_COO~DV/checks/check_devpln_contributing.sh doc</invocation><expect>CONTRIBUTING-CHECK doc ok=True</expect></criterion>
`DPb4-AC1` -- the page exists, is at most 90 lines, plain ASCII, and carries the named anchors (the check script is the issuer's; run it, do not edit it).

<criterion id="DPb4-AC2" cell_refs="DP-b-4"><invocation>bash org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/2.0.0_SA_COO~DV/checks/check_devpln_contributing.sh worker</invocation><expect>CONTRIBUTING-CHECK worker ok=True</expect></criterion>
`DPb4-AC2` -- the worker definition points at the page and the branch name.
</proof_of_spec>

<expected_criteria>DPb4-AC1,DPb4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~4/NFRA_DEVPLN.TO-DP-b-4.contributing-boxes.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPb4-AC1,DPb4-AC2`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-b-4</owned_cells>
</decomp_ref>

<paths>
portal/CONTRIBUTING-BOXES.md
.claude/agents/worker.md
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
lane: the <paths> block IS the grant (worker RULING 1). Portal worktree: this order needs `--portal-ref` at the spawn.
</preflight>

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-BRANCH, C-CLASS, S06 (`CONTRIBUTING-BOXES.md`); ratified-text SIGNED by 3.0.0_SA_CVO~L (current). The CLI forms the page cites are the pinned interfaces in the decomposition; the issuer reads them against the built tools at the drain.
