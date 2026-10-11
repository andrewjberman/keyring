# ADVI_FIRMBKTS task order -- `FB-g-31` -- ACT 4: THE EIGHT IRPT RE-PINS (`_authz/loaders.py` AT THE FLIP COMMIT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-31</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~54</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one repository file; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository file only: no AWS act, no upload (the builds you run are BUILD_ONLY). The deploy of what this commit pins is a separate order under the act 4 pair (COO ADDENDUM 2, CTO ADDENDUM 5, SIGNED).
comp-adversary: RUN by the issuer -- at base `r4_repin.py` reads 1 of 3 (R2 the eight builds PASS as the control; R1 and R3 FAIL: no re-pin). The rehearsal in a scratch tree read all eight builds with the canonical bucket in each `loaders.py`. Blindness: BUILD_ONLY proves the artifact's bytes, not a deployed function.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-31` (round 4, workstream `REPIN`; act 4's IRPT leg)

Each of the eight investor-reporting consumers STAGES `_authz/loaders.py` into its artifact from a PINNED commit
(`staged_from` row: `repo_path`, `pin`, `packaged_as`, `sha256`). The flip commit changes that file's bytes; moving the
pins is what moves a deployed byte. You re-pin ONE member in EIGHT functions to the flip commit, and nothing else.

### 1a. Steps (the whole spec)

The flip commit is `FLIPCOMMIT` (40 hex; the issuer fills it at the GO). For each of these eight function keys in
`infra/aws/lambda/ci/lambda-source-map.json` (under `functions`): `irpt-49f-reporting-read-lambda`, `irpt-directory-search`, `irpt-export-render`, `irpt-holdings`,
`irpt-narrative`, `irpt-performance-adapter`, `irpt-status`, `irpt-ycharts-generate`: in its `staged_from` list, the ONE row
whose `repo_path` is `infra/aws/lambda/investor-reporting/_authz/loaders.py`:
1. set `pin` to the 40-hex `FLIPCOMMIT`;
2. set `sha256` to the SHA-256 (hex) of `git show FLIPCOMMIT:infra/aws/lambda/investor-reporting/_authz/loaders.py` (bytes).
Change no other row, no other field, no other function, and keep the file's own formatting (indent, key order, line
endings). Then commit the one file.

### 1b. Rules

1. Edit the file by TEXT (a precise replacement of the two values per row), not by loading and re-dumping it, so no other
   byte moves. If a row's `pin` is not one of the three known pins (`d8d8e7d868bc...`, `361c44fa9d40...`, `0642c9d00454...`),
   or a function has no such row or two, STOP and file a BLOCKING row.
2. `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <function>` is local and allowed (it uploads
   nothing and leaves the source map untouched). Never run it without `BUILD_ONLY=1`.
3. ASCII only. If the commit is refused by a gate, do not override or force: file a BLOCKING row with the gate's lines.

## 2. BOUNDS

1. One commit; one file. No deploy, no upload, no push.
2. The builds are the check: if any of the eight reads a hash mismatch, STOP before the commit and file a BLOCKING row.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~54/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~54/ADVI_FIRMBKTS.TO-FB-g-31.irpt-repins.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-31"><invocation>cd /c/dev/wk-firmbkts-54 &amp;&amp; timeout 280 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_repin.py --arms repin --flip FLIPCOMMIT --root /c/dev/wk-firmbkts-54 --base HEAD~1; echo "exit=$?"</invocation><expect>ROUND 4 REPIN: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-31"><invocation>cd /c/dev/wk-firmbkts-54 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-54 --allow infra/aws/lambda/ci/lambda-source-map.json --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~54/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/lambda/ci/lambda-source-map.json; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 runs after your commit (so `HEAD~1` is the base): the source map differs only by the eight rows' two fields to the flip
commit, all eight builds pass, and each artifact's `loaders.py` equals the flip commit's blob and carries the canonical
bucket. AC2 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-31.irpt-repins.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~54`. The re-pin
commit FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_FIRMBKTS-D1-W54-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs, the eight
BUILD_ONLY hashes, and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED for the window. Spawned only after `FB-g-30` is merged and its full commit hash is known; the worktree
is cut from that merged head and `FLIPCOMMIT` in the two invocations is filled with it. Rehearsal hashes are in the act-4 COO
ADDENDUM 2. After this commit the build-and-upload of each function (and its scoped plan and apply) is `FB-f-11`'s IRPT leg.
Workstream `REPIN`. Class WORLD by the path floor.

<status>parked</status>
<round>4</round>
<workstream>REPIN</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-31</to_id>
<slot>~54</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
