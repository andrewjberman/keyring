# NFRA_MCPORTAL task order -- `MP-zp-1` -- WORKSTREAM OGP ROUND 1: on /opalgateway a stopped person's switches read OFF, and the audit list reads again after a change (FWD-29, FWD-28)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zp-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zp-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~46</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- each test plants the contrary state (a running person; a list that was not re-read) and asserts the page does not claim the stopped or fresh reading.
EGRESS CLASS, declared: none. Make no network call (the tests mock fetch).
</preflight>

## 1. THE CELL -- `MP-zp-1` (workstream OGP round 1, decomposition section OGP1.1)

You have two worktrees, nested: the workspace worktree `C:/tmp/mp-ogp-46` (branch `wk-NFRA_MCPORTAL-46`) and, inside it, the mcportal worktree `C:/tmp/mp-ogp-46/mcportal` (branch `wk-NFRA_MCPORTAL-46-mcportal`), based on mcportal `f90f03a`. `node_modules` is linked. Do not run `bun install` or `bun add`. Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-ogp-46 &&`. Commit code in the mcportal worktree with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~46 <0.9.0_WK_NFRA_MCPORTAL~46@opal.agent>`. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~46 <0.9.0_WK_NFRA_MCPORTAL~46@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**What was seen.** The issuer rendered `/opalgateway` from the built page on fixtures and drove one person through a tool off and on, then stop and restore (screenshots: `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/render_20261021/og_stopped.png` and `og_after_refresh.png`). Two defects:
1. **A stopped person's switches still read ON.** After "Stop this person" the Access section says `Status: stopped` and the button reads `Restore this person`, but every channel and tool switch stays checked. A stopped person is admitted nothing by the gateway, so a switch that reads on is a page that disagrees with the gateway (PRD v0.10 FWD-29: "a switch that is on while a different gate refuses is a FAIL").
2. **The audit list does not re-read after a change.** After four changes were written from the panel the list at the foot of the page still read `No access changes recorded.` until Refresh was pressed. FWD-28 wants every driven act to appear in the list.

Build (in `mcportal/src/pages/opalgateway/`, plus the small edits named):
1. **Stopped reads off.** When the picked person's record is `stopped`, the page shows every channel and tool switch unchecked and disabled, and states once, in the Access section, `Stopped: the gateway admits nothing for this person. Restore to use the switches.` The stored `tools_deny` and `channels_deny` are not changed by this (a restore returns the person to exactly what the record said before the stop; the display is a reading, not a write). Do it with an optional prop (default off) on the shared access view so the People page keeps behaving as it does today: the People tests stay green and unchanged.
2. **The list re-reads after a write.** When the panel finishes a write (the change was posted and the record re-read), the page re-reads the audit list once. Do it with an optional callback prop on the panel (default none) and a write counter beside the page's read counter; do not poll. The component wiring cannot be mounted under `bun test` here (no DOM), so it is not tested by a mount: the issuer proves the wiring by rendering the built page after the drain.
3. **TWO tests**, each by its exact name, as the literal first argument of its `test(...)` (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; synthetic fixtures only; in `src/pages/opalgateway/opalgateway.test.tsx` or a sibling test file there):
   - `a stopped person's tool and channel switches read off and are disabled on the opalgateway page, and the page says the gateway admits nothing` (include the contrast in the same test: the same person running reads every switch on and enabled, and the stored deny lists are unchanged)
   - `the opalgateway audit list read key advances when a write finishes and when Refresh is pressed, and not otherwise` (a PURE test, no mounting: put the rule that combines the page's read counter and its write counter into the audit list's read key in one exported function in `gatewayModel.ts`, the page calls it, and the test asserts the key is unchanged by no event, differs after one finished write, differs after one Refresh, and that a write and a Refresh give different keys from each other)
All existing tests keep their names and pass, the People tests included. `bun test src` now reads 91 or more pass and 0 fail.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway (Python) file, no Lambda, no Terraform, no `package.json` or `bun.lock`, no deploy, no network call. Do NOT edit `src/api/admin.ts`.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it.
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author. Do not print a real name, email or account.

## 3. SURFACES

<paths>
mcportal/src/pages/opalgateway/
mcportal/src/pages/people/PersonAccessPanel.tsx
mcportal/src/pages/people/PersonAccessView.tsx
mcportal/src/pages/people/personAccess.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~46/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md` (the colour law: use the page's existing classes; no new colours), and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W46-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them). `surfaced_at` = `date -u +%FT%TZ`. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zp-1"><invocation>cd C:/tmp/mp-ogp-46 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zp1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests present in sources 2 of 2.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-zp-1"><invocation>cd C:/tmp/mp-ogp-46 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zp1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)tsc rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~46/NFRA_MCPORTAL.TO-MP-zp-1.opalgateway-stopped-and-audit-refresh.proof_of_spec.json`, run `proof-of-spec-check.py` on it as the worker rules say, and report once, with: the output of AC1 and AC2; the mcportal commit hash or hashes and the workspace commit hash; every existing assertion you changed (file, test, old, new), or none; `bun run build` in the nested worktree (rc); any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut from the issuer's own look at the built page (2026-10-21 ~01:2xZ; vite on :5174 at mcportal f90f03a, fixtures through playwright route mocks; screenshots committed under `deliverables/2.0.0_SA_COO~MP/ogw/render_20261021/`), before Andrew's sitting so FWD-29 and FWD-28 read true on the page he uses. A SEPARATE workstream (OGP) because `to-pipeline-gate` allows one issuance per workstream round and OGW round 2 already has one; the write surface is disjoint from every live order (`MP-zo-4` writes only its deliverables). Not in this order (stated): the History and audit rows list bookkeeping fields (`revision`, `expect_revision`, `updated_at`) and, on a first write, the whole record `none to ...`; a first-write row reads long. That is a readability polish to hand to the next enrichment list, not a defect against an FWD. Checks dry-run at base in the provisioned slot-46 worktree (mcportal f90f03a, 2026-10-21 ~01:4xZ): zp1.AC1 FAIL as expected (`bun test src` 89 pass, 0 fail; named tests present in sources 0 of 2; min 91); zp1.AC2 PASSES at base (tsc rc 0) by design: it is a type-check guard against the worker's edit, not a build criterion.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~MP, 2026-10-21 ~02:1xZ), after worker ~46's row Z-W46-S1 (BLOCKING):** the second test as first written needed a mounted component, and mcportal has no DOM library (bun 1.3.14 has no `document`; the zo-1 worker's report had already said the suite has no DOM and no click test). The fault is the issuer's, not the worker's: the test is replaced by a pure test of the read-key rule (face above), `zp1.AC1.sh` carries the new name, the floor stays 91 pass. The worker's code (`98c0065`) stands; it extracts the key rule into `gatewayModel.ts`. Gate limb that graded the modification: none (to-pipeline-gate grades a modified order only for `<placeholders>`, NONE).

<status>pending</status>
<round>1</round>
<workstream>OGP</workstream>
<slot>~46</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
