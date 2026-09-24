# NFRA_OPALAI task order -- `OA-w-4` -- S2: the census tools count work done inside submodules

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-w-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~7</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-w-4` (round 1, decomposition s.2/s.3)

PRD FWD-10: agents' work reports and progress views count work done in `opal_ai`. Measured at the cut: neither census
tool reads any submodule. Each runs one `git log` in the parent (`.tools/fabric-commits.py:54`,
`.tools/activity-check.py:107-108`), so portal's commits are not counted either. `.gitmodules` now maps `portal` and
`opal_ai`. Build:
1. **`fabric-commits.py`**: `--json` output gains a top-level `by_repo` object. It holds `parent` = the parent's commit
   count over the window, EXACTLY as today's scrape counts it (unchanged), plus one key per path `.gitmodules` maps: an
   integer count of that nested repo's commits over the same window when it is initialised in this checkout, else the
   string `"UNINITIALISED"` (never 0, never omitted). Nested commits join `by_author`/`by_project` the same way parent
   commits do. The default text report prints the repos line too.
2. **`activity-check.py`**: its header line gains a field `repos: parent=<n> <path>=<n|UNINITIALISED> ...`, and nested
   commits by fabric serials count in the per-agent views, tagged with their repo.
3. Mapped paths come from `.gitmodules` (`git config -f .gitmodules --get-regexp path`), never a hard-coded list. An
   unmapped gitlink (`models/factor_scanner`) is not iterated.

## 2. BOUNDS

1. The parent repo's own counts do not change. AC1's bound arm checks it.
2. **`opal_ai` is initialised in your worktree** (a nested worktree at `<worktree>/opal_ai`, holding
   `0.0.0_AB_MSTR~Z`'s 2026-09-24 init commit `90ca424fc7`). `portal` is NOT provisioned in your worktree, so it must
   read `UNINITIALISED`.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.tools/fabric-commits.py
.tools/activity-check.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~7/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W7-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-w-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w4.AC1.sh; echo "exit=$?"</invocation><expect>tool: parent=N (before<=N<=after) opal_ai>=1 portal=UNINITIALISED or an integer -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-w-4"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w4.AC2.sh; echo "exit=$?"</invocation><expect>repos: parent=N opal_ai>=1 portal=UNINITIALISED or an integer -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~7/NFRA_OPALAI.TO-OA-w-4.census-iterates-submodules.proof_of_spec.json`. Report once: what you changed and where, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S2 census half / A10's census limb. `/integrate`, the sparse-cone recipe and the startup init are NOT
this round (decomp s.9 item 4).

<status>pending</status>
<round>1</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
