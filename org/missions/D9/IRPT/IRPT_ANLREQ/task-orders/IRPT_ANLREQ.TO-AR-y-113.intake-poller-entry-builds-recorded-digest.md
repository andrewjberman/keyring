# TO IRPT_ANLREQ.TO-AR-y-113 -- the irpt-intake-poller map entry builds its recorded digest with NO parity skip

<to_id>IRPT_ANLREQ.TO-AR-y-113</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the floor of an `infra/` path; one live single-resource read). NOTHING is uploaded, applied, planned or invoked by this order.
**Decomp cell:** `AR-y-113` (`decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W53-S<k>`. The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either.
- **Every build here is `BUILD_ONLY=1` with `TMPDIR` set to a folder OUTSIDE the worktree.** Without `BUILD_ONLY=1` the build script
  UPLOADS: never run it so. Never set `BAU_PARITY_SKIP`.

### THE CELL (`AR-y-113`, inlined)

*The map entry of `irpt-intake-poller` builds its recorded digest with NO parity skip.*

Why. Row `IRPT_ANLREQ-D2-S34`: this function does not build from the source map. `BUILD_ONLY=1 bash
infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-intake-poller` ends `File not found:
infra/aws/lambda/investor-reporting/intake/firm_registry.json` and `PARTIAL -- 0 built, 1 failed`. The entry
(`functions["irpt-intake-poller"]` in `infra/aws/lambda/ci/lambda-source-map.json`) records `deployed_code_sha256`
`YpE2MyUwdGzMfLaUGXi8cClxoVHFFmOz5LT1BYmoTa8=`, deployed from commit `1545ec344242361d038d8378d784345c3af1878e` on 2026-10-04. A map
entry that cannot build cannot reproduce what is live. The map's job is to reproduce what is LIVE.

1. **Find why the member is missing.** Is `firm_registry.json` a tracked file that moved, a GENERATED file (look for its generator
   and for how other entries of this pipeline take it: `irpt-status`'s entry packages a `firm_registry.json`; read its `staged_from`
   row), or was it present at the deployed commit (`git show 1545ec3442:<path>` -- print a positive control beside an ABSENT)? Say
   which, with the evidence.
2. **One live read, to know the target:** `.tools/aws lambda get-function-configuration --function-name irpt-intake-poller`: record
   `CodeSha256` and `LastModified`. If it differs from the entry's recorded digest, the entry is stale: record both, and build
   toward the LIVE digest only if you can show which commit's bytes produce it; otherwise STOP and file a row. No other live call.
3. **Fix the ENTRY, not the tree:** make the entry take each member whose working-tree bytes are missing or differ from the deployed
   bytes from a pinned commit, by `staged_from` rows in exactly the form the entry's existing rows use (`pin`, `sha256` of
   `git show <pin>:<repo path>` bytes, computed in binary). If the parity check then names files of the source folder as outside the
   package, declare them in `outside_package` with a one-line reason each (the mechanism: build script lines 269-292 and 450-500;
   the composition-read entry is a worked example). Do not create or copy any file into the source folder. Do not add or remove a
   member of `files[]`. Change no other entry.
4. Build twice with no skip; both must print `BUILD_ONLY:` with the target digest. If the digest differs, do NOT adjust by trial:
   diff your build's members against the pinned blobs' hashes (and against the deployed commit's files), name the member that
   differs and why. If it cannot equal the target with pins, STOP, leave the entry building (if it now builds) and file a row
   stating the digest it builds and the member that differs.
5. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r11/INTAKE_POLLER_MAP_ENTRY.json`:
   `{"read_at": "<UTC>", "tree_head": "<short hash>", "missing_member": {"name": "...", "cause": "<one sentence>", "evidence":
   "<command and what it printed>"}, "live": {"code_sha256": "...", "last_modified": "...", "equals_recorded": true|false},
   "pins_added": [{"packaged_as": "...", "repo_path": "...", "pin": "...", "sha256": "..."}, ...], "outside_package": {...},
   "build": {"parity_skip": false, "sha256_first": "...", "sha256_second": "...", "members": <n>, "equals_target": true|false},
   "diff_lines": {"added": <n>, "removed": <n>}}`. Commit the map and this record.

### ACCEPTANCE

<criterion id="AR113-y-AC1" cell_refs="AR-y-113"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r11/ar11_checks.py y113-poller --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y113-POLLER-OK</expect></criterion>
`AR113-y-AC1`: a build with no parity skip prints the digest the entry records as deployed.

<expected_criteria>AR113-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply. No non-ASCII in what you add.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md</decomp_doc>
<owned_cells>AR-y-113</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR113-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-113.intake-poller-entry-builds-recorded-digest.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-113`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR113-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 map entry (its keys printed by the issuer; recorded digest and deployed commit read) and 1 build run at the base (PARTIAL, 0 built); NOT seen: why the member is missing and whether live equals the recorded digest (the worker reads both). comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- the function is scheduled but nothing here touches it or its trigger; the map is read at build time only, 1 reader (the build script). comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change; nothing is applied.
comp-adversary: RUN -- by reading 1 entry against 1 recorded digest; the lens: a file copied into the source folder to make the build pass (it would ship unpinned bytes), or a digest matched by trial. The face forbids both. NOT seen: whether the function belongs to another project whose lane holds this entry (IRPT_BCKEND IB-s-6 is named in its note).
lane: one map entry, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-11 analysis @6385a12ed2, item 3, read as: the composition-read half of row S34 was done in round 10
  (`AR-y-102`); this is the row's other function. `AR113-y-AC1` base: FAIL as expected (PARTIAL, 0 built).
- Seating: slot ~53 is reused; its earlier order is terminal.
