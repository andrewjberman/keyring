# NFRA_MCPORTAL task order -- `MP-pd-4` -- WORKSTREAM PC ROUND 2: the People page controls -- channel and tool switches, stop and restore, the person's history (F2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-4</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~28</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a row with no principal, a record kind not live, a refused write).
EGRESS CLASS, declared: none. Every fetch in a test is a stub.
</preflight>

## 1. THE CELL -- `MP-pd-4` (workstream PC round 2, decomposition sections PD.1 and PD.3)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pd-28`, branch `wk-NFRA_MCPORTAL-pd-28`;
- inside it, the mcportal worktree `C:/tmp/mp-pd-28/mcportal`, based on mcportal `17dcbb2` (the commit live on the gateway today:
  the People page, the three-state git panel, the Gateway page and the Control Plane). `node_modules` is linked. Do not run
  `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author
`0.9.0_WK_NFRA_MCPORTAL~28 <0.9.0_WK_NFRA_MCPORTAL~28@opal.agent>`. mcportal is its own repo, outside the workspace's safe-commit
lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via `.tools/safe-commit.sh`.
Never push either repo.

Andrew picks a person on the People page (`src/pages/people/`, read it whole first with its test file and `src/pages/gateway/**` as
your model for structure, fetch and style) and today only READS what that person reaches. This cell adds the WRITE half, against
two backend shapes that parallel cells build. Build against them exactly; do not rename a field.

**The People rows gain `principal`.** `GET /api/admin/people` rows now carry `"principal": {"tid": "<guid>", "oid": "<guid>"} | null`.
Add it to the `People` row type in `src/api/admin.ts` (as optional-null, so an old response still parses).

**The access endpoint.** Both owner-gated, same origin:
- `GET /api/admin/people/{tid}/{oid}/access` answers 200 `{"tid", "oid", "record_kind": "live" | "not live", "record": <body> | null,
  "read_at"}`, where the body is `{"status": "active" | "revoked", "revision": <int>, "stopped": <bool>, "tools_allow": [..],
  "tools_deny": [..], "channels_allow": [..], "channels_deny": [..], "updated_at", "updated_by"}`.
- `POST /api/admin/people/{tid}/{oid}/access` takes `{"change": {...}, "expect_revision": <int> | null}`, where `change` holds any of
  `stopped` (bool), `status`, `tools_allow`, `tools_deny`, `channels_allow`, `channels_deny` (a key present REPLACES that field; a key
  absent keeps it). It answers the writer's verdict: `{"verdict": "WRITTEN" | "REFUSED", "reason": <string> | null, "detail",
  "result": {"tid", "oid", "revision", "record"}}`. `expect_revision` is the record's current `revision`, or null when `record` is null.
- The person's history is the existing `GET /api/admin/changes?tid=<tid>&oid=<oid>` list (each entry has `action`, `when`, `who`,
  `verdict`, `reason`, `before`, `after`); the page shows only entries whose `action` is `set_person_access`.

Build:
1. **`src/api/admin.ts`**: `getPersonAccess(tid, oid)`, `setPersonAccess(tid, oid, change, expectRevision)` (a thin POST; it returns
   the verdict object whether WRITTEN or REFUSED and throws only on a transport failure, the way `narrowGrant` handles a refusal), and
   `getPersonChanges(tid, oid)` (the `changes` list filtered to `set_person_access`). Types as above.
2. **On the People page**, for the selected person:
   - if the row's `principal` is null: no control, and the text "no principal id: cannot be changed from here yet";
   - otherwise load `getPersonAccess`. If `record_kind` is "not live": no control, and the text "per-person control is not live yet";
   - otherwise show, for each channel the person holds (and each tool within it) a switch that reads the person's CURRENT state
     (a tool or channel in `tools_deny` / `channels_deny` reads off), a "Stop this person" / "Restore this person" button reflecting
     `stopped`, the record's `revision` and `updated_at`, and the person's history list (newest first, each entry showing when, who,
     the verdict and the reason, and the change as a before-and-after of the changed field);
   - a switch or button POSTs ONE change with `expect_revision` = the record's current revision (null if `record` is null): switching a
     channel off sets `channels_deny` to the current list plus that channel; on removes it; the same for tools with `tools_deny`;
     stop sets `stopped` true; restore sets it false. Never send a list you did not just read.
   - after the POST, re-read the record and the history from the endpoints; do not update the page from the POST's body alone. A REFUSED
     verdict shows the reason and detail on the page and leaves the displayed state as it was (the re-read shows the truth).
   - writes are Andrew's only: the server enforces it, and a 403 shows "not allowed" without a retry.
3. Style and layout follow `portal/DESIGN.md` through the existing People page (the light canvas, white hairline panels, navy ink,
   one band per page). No new dependency, no alert or notification, no auto-refresh timer.

**Tests**, by these exact names (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each
name as the literal first argument of its `test(...)`/`it(...)`):
- `person row with a principal shows channel and tool switches`
- `a row without a principal shows no control and says why`
- `record kind not live reads per-person control is not live yet`
- `stop and restore post the change with the expected revision`
- `a refused write shows the reason and changes nothing on the page`
- `history lists only set_person_access entries for the person`
- `access client posts change and expect_revision` (in `src/api/admin.test.ts`)
- the existing `routes json equals the app routes` must still pass (this cell adds no route, so `public/routes.json` is unchanged).

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway file, Terraform or the manifest.
   Make no deploy and no network call.
2. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row.
3. Standing rules: no push and no vendor call. Commit the mcportal files with plain `git commit` in the nested worktree, and the
   workspace files via `.tools/safe-commit.sh`, each with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as
   written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
mcportal/src/pages/people/
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~28/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/gateway/**`, `mcportal/src/pages/control-plane/**`, every other mcportal file, `portal/DESIGN.md`,
and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W28-S<k>` (the next free k for W28). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root `C:/tmp/mp-pd-28` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd4.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 8 of 8; pass=8 or more; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~28/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.proof_of_spec.json`.
Report once, with:
- the check output;
- the mcportal commit hash or hashes, and the workspace commit hash;
- which fields of the contract you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC round-2 issuance (decomposition v10) from PRD v0.8 FWD-21. The drain runs `bun run build`
and `tsc -b` once (spine v3.16). The nested mcportal worktree is cut at origin DEV `17dcbb2`. Whether the access endpoint answers
"not live" depends on NFRA_OPLGTW OG-cp-1 being released (PD.0 item 3); the page must render both states. Check dry-run at
base: AC1 FAIL in the issuer's tree (`mcportal/src/pages/people` absent there, the issuer's mcportal checkout is README only);
in the worker's nested worktree the people folder exists, and a `git grep` of the eight names at mcportal 17dcbb2 finds 1 of 8
(only `routes json equals the app routes`; measured 18:2xZ), so the count reads 1 of 8 there.

<status>pending</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
