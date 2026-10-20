# NFRA_MCPORTAL task order -- `MP-zo-1` -- WORKSTREAM OGW ROUND 1: the /opalgateway page -- pick a person, see their reach, subtract, restore, stop (FWD-23, 24, 25, 27)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zo-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zo-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~42</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the last-admin test plants the only master admin and asserts no request is sent; that is its own adversary arm.
EGRESS CLASS, declared: none. Make no network call (the tests mock fetch).
</preflight>

## 1. THE CELL -- `MP-zo-1` (workstream OGW round 1, decomposition section OGW1.1)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-ogw-42`, branch `wk-NFRA_MCPORTAL-42`;
- inside it, the mcportal worktree `C:/tmp/mp-ogw-42/mcportal`, branch `wk-NFRA_MCPORTAL-42-mcportal`, based on mcportal `21ad404` (origin DEV).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-ogw-42 &&`.
All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~42 <0.9.0_WK_NFRA_MCPORTAL~42@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~42 <0.9.0_WK_NFRA_MCPORTAL~42@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**What exists and what is wanted.** Andrew wants one page, `mcp.opalinvest.dev/opalgateway`, where he picks a person, sees what they can reach, and subtracts or restores a channel or a tool, or stops and restores the person, in one act each. The pieces are built on the People page: `src/pages/people/PersonAccessPanel.tsx` (reads the person's record and history, posts ONE change at a time, re-reads), `PersonAccessView.tsx` (the channel and tool switches, the stop/restore button, the history), `personAccess.ts` (the change builders) and the people data from `GET /api/admin/people` (`PeoplePerson`: `who`, `kind`, `how`, `tier`, `channels` with their tools, `principal {tid, oid}`). The served API behind the panel is mounted by another project and is not live yet, so everything here is proven on fixtures and a mocked fetch.

Build (new directory `mcportal/src/pages/opalgateway/`, plus the small edits named):
1. **Route and shell.** Route `/opalgateway`, page id `opalgateway`, label `Opal Gateway`, appended LAST in `PAGES` (`src/shell/pages.ts`, after People) with a comment naming PRD v0.10 FWD-23; registered in `src/App.tsx`; listed in `public/routes.json` (keep the list sorted as it is). Where an existing test pins the page list, the sidebar order or the routes list, extend that assertion by exactly this one entry and report the change (file, test, old, new).
2. **The page** (`OpalGateway.tsx` container, `OpalGatewayView.tsx` pure view, `opalgateway.css`, `index.ts`): load the people data the way `src/pages/people/People.tsx` does (reuse its loader or hook; do not duplicate the fetch code if a shared one exists); list each person that has a principal; the picked person (state, and `?person=<tid>/<oid>` in the URL preselects) shows: tier, how they reach, and their channels and tools exactly as the people data lists them (that data IS the gateway's own admission chain; never retype a rule), and hosts the EXISTING `PersonAccessPanel` for that person. Do NOT reimplement the switches or the stop button: use the panel as is. The page reads through the panel; a pick of another person reads that person's record, never the last one's.
3. **Last-admin guard (FWD-27).** When the picked person's `tier` is `master_admin` and NO other listed person has tier `master_admin`, the stop control is disabled and the text `This is the last master admin; the page will not stop it.` shows beside it, and no request is sent. For any other person the stop control behaves as the panel already does. (The people data does not show other people's stopped flags, so a listed master_admin counts as active: this is conservative and stated in the order, not a defect.) Implement the guard around the panel without editing the panel's own files unless that is the only way; if you must edit a People file, keep the People tests green and report it.
4. **People links in.** Each person section on the People page gets a link `Manage access` to `/opalgateway?person=<tid>/<oid>` (only for a person that has a principal).
5. **SEVEN tests**, each by its exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each as the literal first argument of its `test(...)`; use fixtures with synthetic names, never real people or accounts; put the tests in `src/pages/opalgateway/opalgateway.test.tsx`, except the last two which go where the sidebar and People tests live):
   - `the opalgateway page lists each person and shows the selected person's channels, tools and tier`
   - `subtracting one tool from the opalgateway page posts one change and the switch reads off after the re-read` (mock fetch: the POST body is ONE change denying that tool; the next GET returns the record with the tool in `tools_deny`; the switch then reads off)
   - `restoring that tool posts one change and the switch reads on again`
   - `stopping and restoring a person each post one change`
   - `the page refuses to stop the last master admin and sends no request` (assert the fetch mock saw ZERO POSTs; add the contrast in the same test: with a second master_admin listed the stop control is enabled)
   - `opalgateway is the last sidebar entry and is listed in routes.json`
   - `the people page links each person into opalgateway`
All existing tests keep their names and pass (apart from the one-entry extensions of item 1). `bun test src` now reads 86 or more pass and 0 fail. Do not change any existing fixture; add new ones.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway (Python) file, no Lambda, no Terraform, no `package.json` or `bun.lock`, no deploy, no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not print a real name, email or account.
5. Your queue holds a SECOND order, `MP-zo-2` (the audit list, same page). You will be handed it after this one is reported; do not start it.

## 3. SURFACES

<paths>
mcportal/src/pages/opalgateway/
mcportal/src/pages/people/
mcportal/src/shell/
mcportal/src/App.tsx
mcportal/public/routes.json
mcportal/src/pages/gateway/gateway.test.tsx
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~42/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file (notably `src/api/admin.ts`, which you may NOT edit in this order), `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md` (the colour law: use the page's existing classes; any new rule reuses existing ink and spacing, no new colours), and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W42-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zo-1"><invocation>cd C:/tmp/mp-ogw-42 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo1.AC1.sh; echo "exit=$?"</invocation><expect>named tests present in sources 7 of 7.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~42/NFRA_MCPORTAL.TO-MP-zo-1.opalgateway-page-person-reach-and-switches.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you changed or extended (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the OGW round-1 issuance (decomposition v20) from PRD v0.10 (text 9b4bbcfbb9, ADMITTED) and the CTO's cut instruction (file ferry 2026-10-20 17:50Z, broker down). Thread first: subtract and restore for one person. The served half (the mount `OG-mp-1`, the writer deploy, the bundle release, the driven FWD-29 proof) is NOT in this order. FWD-26 add and the WIDENING label wait on NFRA_OPLGTW round 48.
zo1.AC1 base: FAIL as expected (`bun test src` 79 pass, 0 fail; named tests present in sources 0 of 7; min 86), run in the provisioned slot-42 worktree at mcportal 21ad404, 2026-10-20 ~18:3xZ.

<status>complete -- drained 979787698da (worker 0.9.0_WK_NFRA_MCPORTAL~42); AC1 PASS: named tests 7 of 7, bun test src 86+ pass 0 fail (issuer re-ran at 89 pass), mutant control 1 of 5 fail, tsc rc 0, build rc 0; mcportal e05fc91 (LOCAL on branch wk-NFRA_MCPORTAL-42-mcportal until MSTR~Z pushes DEV). Built on fixtures; the served page waits on the mount OG-mp-1, the writer deploy and the bundle release.</status>
<round>1</round>
<workstream>OGW</workstream>
<slot>~42</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
