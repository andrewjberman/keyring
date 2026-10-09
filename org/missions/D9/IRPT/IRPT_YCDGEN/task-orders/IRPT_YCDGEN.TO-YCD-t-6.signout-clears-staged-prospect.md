# IRPT_YCDGEN task order -- `YCD-t-6` -- ROUND 6 (THREAD): SIGN-OUT CLEARS THE STAGED PROSPECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6K.md</decomp_doc>
<owned_cells>YCD-t-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-t-6.signout-clears-staged-prospect</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~5</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE thread round; a CTO review (msg 64) already named the defect this cell fixes
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. No worker calls a vendor, writes the store, deploys or grants. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 addendum-K decomposition)

### `YCD-t-6` -- sign-out clears the staged prospect (hop 8 Open (page wiring); FWD-1)
- `portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts`: export ONE reset, `clearStagedProspectOnSignOut()`, that returns every piece of module state to its fresh-page-load value: `staged` (firm, file, result, uploadAttempt, parentInput), `notedDropdownFirm` and the published firm `catalogue`, and notifies the catalogue listeners. The existing test seam `resetStagedProspect()` may call it. Fix the header comment so it agrees with `ProspectComposer.tsx:156`, which preselects the tab's firm.
- `portal/src/contexts/AuthContext.tsx`: in `logout()`, call `clearStagedProspectOnSignOut()` directly beside `clearCanonicalDataAsOf()` (about line 643). Add one import. Change nothing else in this file.
- `portal/scripts/prospect-firm-exercise.mjs`: add a fourth arm, `signout`. It (1) stages a firm, a file, a review result, an uploadAttempt, a noted dropdown firm and a published catalogue through the store's own functions, (2) calls the new reset and checks that every one of them reads back at its fresh value, and (3) reads `src/contexts/AuthContext.tsx`, takes the body of `logout` and checks that it calls `clearStagedProspectOnSignOut()`. Step (3) is the pin that fails without the fix: before you finish, prove it by running the arm once against a temporary copy of the logout body with the call removed (it must print FAIL), and say so in your report. Leave the `firm`, `dropdown` and `remount` arms as they are.
- The portal is a git submodule: your worktree has a nested portal worktree on branch `wk-IRPT_YCDGEN-t6-portal`, cut from `cand-r6-prospect-firm` @4d16a2a0. Commit the `portal/...` files INSIDE it. No colour, layout or behaviour change beyond the reset.

## 2. THE CONTRACT YOU BUILD AGAINST

**R18(d) Sign-out clears the staged prospect.** `stagedProspect.ts` exports one reset that returns every piece of module state the card holds to its fresh-page-load value (firm, file, result, uploadAttempt, parentInput, notedDropdownFirm, the published firm catalogue). `logout()` in `AuthContext.tsx` calls it in the same block as `clearCanonicalDataAsOf()`. After a sign-out, nothing a previous user staged can be read back from the module. Why (CTO msg 64, 2026-10-07): `stagedProspect.ts:84` keeps the file and its review result in module memory; `logout()` clears the query cache but neither reloads nor resets this store, so the next user on the same tab gets the previous user's prospect holdings back.

## 3. WHAT YOU NEED TO KNOW (measured at the cut)

- Read first: `portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts` (state at about 83-86; `resetStagedProspect` near the end of section 2), `portal/src/contexts/AuthContext.tsx` lines 612-656, `portal/src/lib/dataAsOfCanonicalStore.ts:72` (the pattern to copy), `portal/scripts/prospect-firm-exercise.mjs` (its `check` / `finish` helpers and the `mod` / `src` loaders).
- The R18(c) behaviour is unchanged: a remount keeps the staged slot, and a change of firm clears it. The `remount` arm must still print `RESULT: remount PASS`.
- Baseline: from the portal directory, `bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis` is 40 pass and 11 fail BEFORE your edit (row W2-S15). Your edit must not change those counts; state them after your edit. Also run `bunx tsc --noEmit` from the portal directory and state its error count before and after.
- Staged file bytes are client data: no browser storage, no console print, no serialisation.
- Do NOT start a dev server (port 5174 belongs to one seat). This is a product-file change: it lands on DEV through the issuer, never by you.
- Encoding: ASCII only in code; no client figure and no secret in any committed file.

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`. NEVER: a vendor call, an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W5-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts
portal/src/contexts/AuthContext.tsx
portal/scripts/prospect-firm-exercise.mjs
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~5/IRPT_YCDGEN.TO-YCD-t-6.signout-clears-staged-prospect.proof_of_spec.json
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- after the sign-out reset every piece of staged state reads back fresh, and logout calls the reset
- **AC2** -- a staged file and its review result still survive a remount and are cleared by a change of firm
- **AC3** -- the card still sends the chosen firm on the upload and the submit with no client picked

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-t-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs signout</invocation><expect>^RESULT: signout PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-t-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs remount</invocation><expect>^RESULT: remount PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-t-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs firm</invocation><expect>^RESULT: firm PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit the portal files inside the nested portal worktree, then write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~5/IRPT_YCDGEN.TO-YCD-t-6.signout-clears-staged-prospect.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-t-6.signout-clears-staged-prospect` and commit it in the outer worktree. Report once: each mechanical criterion's verdict line with the output above it; the negative-control result; the bun and tsc counts before and after; the portal commit hash; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** addendum K cell (decomposition IRPT_YCDGEN_DECOMP_R6K.md), cut on 1.0.0_SA_CTO~DELL2 ruling msg 64 (q-6 REWORK: sign-out reset plus one failing-without pin, and the header comment aligned). Chain `~5`, a fresh slot. Base: portal `cand-r6-prospect-firm` @4d16a2a0 (q-6 stack merged with DEV 6b4e89a8; the CTO read it against DEV 8ddfe409 and merge-tree was clean). If the diff is only this, the whole stack lands on DEV with no second review (msg 64). Portal submodule cell. Risk WORLD: the gate's floor for portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~G2, 2026-10-07 ~08:2xZ):** worker 0.9.0_WK_IRPT_YCDGEN~5 @06752d1e52 (proof + row W5-S1), portal commit 949830e8 on branch wk-IRPT_YCDGEN-t6-portal (on top of cand-r6-prospect-firm @4d16a2a0). Re-run by the issuer in the worktree: signout, remount, firm and dropdown arms all PASS; instance VALID (rc=0); worker's negative control (call removed) printed FAIL. bun 40 pass / 11 fail before and after; tsc 0 errors before and after. Portal diff vs 4d16a2a0 is 3 files, +75/-4, the reset only: CTO msg 64's no-second-review condition holds. Row W5-S1 (bunx absent; bun x used) INERT.

**RE-PROOF (2.0.0_SA_COO~G2, 2026-10-07 ~12:1xZ, CTO~DELL2 msg 481):** the worker's run used packages from a registry fetch (row IRPT_YCDGEN-S15). Proof of record is the re-run on the shared lockfile-matched portal/node_modules (worktree C:/dev/wk-g2-pageproof, junction): typecheck rc=0; signout, remount, firm, dropdown PASS; bun test 32/16/1 over 48, equal at base 4d16a2a0 (standalone-worktree path artifact).

<round>6</round>
<workstream>R6K_SIGNOUT_RESET</workstream>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
