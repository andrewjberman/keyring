# NFRA_OPALAI task order -- `OA-w-2` -- S3: a commit inside a nested repo is graded by the parent's gates

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-w-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-w-2` (round 1, decomposition s.2/s.3)

`opal_ai` is now a mapped submodule of this workspace (`.gitmodules`). Commits made INSIDE it must pass the same gates as
the parent's (PRD C2): the lane check, the ASCII message rule, and `safe-commit.sh`. Today they cannot:
- `.tools/git-hooks/owned-paths-check.sh` reads `YAML="$REPO_ROOT/.owned-paths.yaml"` and
  `VALIDATE="$REPO_ROOT/.tools/owned-paths-validate.py"` (`:25-26`). Inside a nested repo, `REPO_ROOT` is the nested
  root, which has neither file, so in its default block mode it FAILS CLOSED on every commit (`:133-142`). That is why
  the lane file must land BEFORE any hook.
- `.tools/safe-commit.sh` takes `REPO_ROOT` from `git rev-parse --show-toplevel` (`:149`) and roots its audit log and its
  tool paths there.

Build:
1. `owned-paths-check.sh` resolves the SUPERPROJECT when run in a nested repo
   (`git rev-parse --show-superproject-working-tree`, or the main worktree of the superproject for a linked nested
   worktree). It reads the parent's `.owned-paths.yaml` and validator, and it grades the staged nested paths AS
   PARENT-RELATIVE paths (`opal_ai/<path>`), so a worker's `<paths>` grant (written parent-relative) and the lane rows
   match. In the parent it behaves exactly as today.
2. Lane rows for `opal_ai/**` in `.owned-paths.yaml`, following the file's existing grammar and the portal's
   precedent if it has one (read it; do not invent a lane class). They land BEFORE any hook.
3. `install-owned-paths.sh` can install the hook into a NAMED submodule's hooks dir (`--submodule <path>`), and stays
   idempotent.
4. `safe-commit.sh` run from inside a nested repo works: it finds the parent's tools, and its audit log goes to the
   parent's main-tree log.
5. **`.tools/tests/test_nested_repo_gates.sh`** (new): builds a SCRATCH superproject with a nested repo in a temp dir,
   copies this worktree's hooks, tools and a minimal lane file into it, and prints one `ok   [<arm>]` or
   `FAIL [<arm>]` line per arm. The arms are `nested-granted-pass`, `nested-violation-block`,
   `safe-commit-nested-landed` (the commit exists in the nested repo's `git log`) and `parent-unchanged` (in the
   fixture's parent, a granted commit passes and a violation blocks). It ends with `ARMS: <k> of 4 PASS` and exits 0
   only when all four pass.

## 2. BOUNDS

1. **Never install a hook into the real `opal_ai`** (the main tree's nested repo or any worktree of it): its hooks dir
   is shared by every opal_ai worktree, so a hook there would grade other workers' nested commits mid-round. The real
   install is the issuer's act at the round's last merge. Every proof runs on the scratch fixture.
2. A parent lane verdict must not change. The `parent-unchanged` arm shows it.
3. Standing: no push, no install of packages, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and
   report the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does
   not name.

## 3. SURFACES

<paths>
.tools/git-hooks/owned-paths-check.sh
.tools/git-hooks/install-owned-paths.sh
.tools/safe-commit.sh
.owned-paths.yaml
.tools/tests/test_nested_repo_gates.sh
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~5/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `.tools/owned-paths-validate.py`, `.gitmodules`.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W5-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-w-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w2.AC1.sh; echo "exit=$?"</invocation><expect>rc=0; named arms ok 4 of 4; ARMS: 4 of 4 PASS -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-w-2"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w2.AC2.sh; echo "exit=$?"</invocation><expect>lane-file entries naming opal_ai/: >=1; pre-commit hook there: absent -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~5/NFRA_OPALAI.TO-OA-w-2.nested-repo-gates.proof_of_spec.json`. Report once: what you changed and where, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S3 / A14. The issuer installs the hook into the real opal_ai at the round's last merge (after every
opal_ai cell has drained) and exercises one real nested commit through it.

<status>complete</status>
<round>1</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
