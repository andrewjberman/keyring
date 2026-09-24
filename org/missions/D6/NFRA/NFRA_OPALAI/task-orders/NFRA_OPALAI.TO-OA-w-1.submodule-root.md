# NFRA_OPALAI task order -- `OA-w-1` -- THE ROOT: opal_ai becomes a mapped submodule a worker slot can be provisioned with

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: GIT-FETCH from https://github.com/Opal-Capital/opal_ai.git (Opal's own private repo), read-only. No push.
</preflight>

## 1. THE CELL -- `OA-w-1` (round 1, decomposition s.2/s.3)

A new private repo, `Opal-Capital/opal_ai`, becomes a real submodule of this workspace at `opal_ai/`, beside the existing
gitlinks `portal` (@`46c0ae112c`) and `models/factor_scanner` (@`c59b266adf`). Today `.gitmodules` is 0 bytes, and the
remote's `DEV` = `PROD` = HEAD = `90ca424fc7551019cc493847637258adf3c1c4b5` (a README only). Build three things:

1. **`.gitmodules`** maps `portal` (`url = https://github.com/Opal-Capital/portal.git`) and `opal_ai`
   (`url = https://github.com/Opal-Capital/opal_ai.git`, `branch = DEV`). Do NOT map `models/factor_scanner`; that waits
   on its owner's word.
2. **The gitlink** `opal_ai` at `90ca424fc7551019cc493847637258adf3c1c4b5`. `git submodule add` or an index entry of
   mode 160000 both work. The parent commit carries `.gitmodules` and the gitlink together. Do not commit a checked-out
   nested repo's files into the parent.
3. **`.tools/wk-provision.sh` generalised.** Today `cmd_portal` hard-codes `portal` (`:77` `nested="$main/portal"`, `:81`
   `ls-tree HEAD portal`, `:100` `$worktree/portal`, `:217-218` in remove). Add `--nested <path>=<ref>` to `provision`
   (repeatable), provisioning a nested worktree for ANY path `.gitmodules` maps, exactly as `cmd_portal` does for portal:
   branch `<super-branch>-<path with / as ->`, off `<ref>` resolved in the MAIN tree's nested repo. `remove` tears every
   provisioned nested worktree down the way portal's is (the placeholder dir is recreated empty; never `worktree
   prune`). **When the main tree's copy of the named submodule is not initialised** (no `.git` at `$main/<path>`),
   refuse with rc 2 and the line `REFUSED: <path> is uninitialised in the main tree (git submodule update --init <path>)`,
   BEFORE anything is created. Portal's own flags and behaviour are unchanged (`--portal-ref`, `node_modules`
   linking, the self-test arms), and `node_modules` handling stays portal-only.

## 2. BOUNDS

1. Your worktree has no nested repos provisioned. AC2 initialises `opal_ai` INSIDE YOUR WORKTREE from the real remote;
   that clone lives under your worktree's git dir and dies with the teardown. Never touch the MAIN tree's `opal_ai`:
   initialising it is the issuer's hookup after the merge.
2. Do not run `wk-provision.sh --self-test`. It provisions real portal worktrees; the issuer runs it at the drain.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.gitmodules
opal_ai
.tools/wk-provision.sh
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~1/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W1-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC1.sh; echo "exit=$?"</invocation><expect>opal_ai.url=https://github.com/Opal-Capital/opal_ai.git opal_ai.branch=DEV portal.url=https://github.com/Opal-Capital/portal.git gitlink=160000 90ca424fc7551019cc493847637258adf3c1c4b5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC2.sh; echo "exit=$?"</invocation><expect>submodule update rc=0; opal_ai HEAD=90ca424fc7551019cc493847637258adf3c1c4b5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC3.sh; echo "exit=$?"</invocation><expect>main-tree opal_ai initialised=no; rc=2; created=no; REFUSED: opal_ai is uninitialised in the main tree ... -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~1/NFRA_OPALAI.TO-OA-w-1.submodule-root.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the root. Hookup at merge: `git submodule update --init opal_ai` in the main tree, then every
opal_ai cell's slot is provisioned with `--nested opal_ai=<main-tree opal_ai HEAD>`. The drain runs
`wk-provision.sh --self-test` once (portal unchanged).

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
