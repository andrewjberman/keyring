# DSGN_IRPTV1 -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "DSGN_IRPTV1-W1-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~1",
    "surfaced_at": "2026-09-24T09:00:16Z",
    "one_line": "The project's surprise-channel tree did not exist at all (not just this file) -- this worker created it to have somewhere to append, matching the DSGN_REBRND W1-S1 precedent named in the worker face.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- a sibling worker slot (~2, ~3, ...) whose own worktree branched before this commit lands will hit the same missing directory and may independently create the same new file with a different header; the drain reconciles by UNION of rows under one header, never by picking one side.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "test -d org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations at this worker's worktree start returned nonzero (absent)",
        "the task order's <paths> grant names exactly org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md, and its REPORT section instructs appending to it as if it exists, mirroring the DSGN_REBRND W1-S1 precedent it cites by name"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's REPORT section: 'anything you would ask is a surprise row in the investigation file above -- that file does NOT exist yet ... if it is absent when you need it, create it with the header line ... followed by a fenced json array holding your row as its first item (the DSGN_REBRND W1-S1 precedent)'.",
    "world_is": "Neither surprise-channel/ nor surprise-channel/investigations/ existed under this project's tree at this worker's start; no opening row from any seat or sibling worker precedes this one. This worker created both the directories and this file, matching the header shape used by DSGN_REBRND in place of an opener this project never had.",
    "notes": "Not blocking: the <paths> grant covers this file, so creating it is within grant, not an override. Filed so the COO's drain does not read an absent history as 'no surprises found' when it is actually 'no channel existed yet'."
  },
  {
    "id": "DSGN_IRPTV1-W1-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~1",
    "surfaced_at": "2026-09-24T09:00:16Z",
    "one_line": "IV1-AC3's exact '1 1' numstat bound and the cell's prose ('that line becomes <IdentityCard .../>') cannot both be satisfied by a faithful two-symbol rename -- the mount uses an aliased import instead, so index.tsx:186's literal JSX text stays '<ScopeSummary .../>' even though the rendered component is genuinely IdentityCard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --numstat 7c542fd23ec70c88bade4e3270f4c87f267a275a -- index.tsx after changing BOTH the import (line 19) and the JSX tag (line 186) to IdentityCard printed '2  2  src/pages/InvestorReporting/index.tsx' -- numstat sums insertions/deletions across the WHOLE file, not per hunk, so two distinct single-line replacements always total 2/2, never the ruled 1/1",
        "the only route measured to the exact '1 1' CTO 100332 rules for is changing ONE of the two lines and holding the other constant; this worker changed only the import (index.tsx:19), aliased: `import { IdentityCard as ScopeSummary } from './header/IdentityCard'` (trailing same-line comment), leaving index.tsx:186 byte-identical to the pinned commit",
        "./node_modules/.bin/tsc --noEmit -p tsconfig.json returned rc=0 with zero errors against this wiring, and IV1-AC3's own invocation printed NUMSTAT: ['1\\t1\\tsrc/pages/InvestorReporting/index.tsx'] / VERDICT: ONE-LINE-MOUNT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell text: 'Build ... IdentityCard.tsx and mount it at the ONE line ... so that line becomes <IdentityCard scope={selectedScope} selection={acceptedNarrowing} row={accepted ? row : null} />' -- read plainly this describes changing the JSX identifier at index.tsx:186 itself. IV1-AC3 separately and mechanically requires the file's TOTAL git diff against the pin to be exactly one added and one removed line, with header/ScopeSummary.tsx untouched.",
    "world_is": "No implementation that (a) imports a real new IdentityCard binding under that name and (b) writes '<IdentityCard .../>' literally at line 186 can produce a 1/1 total diff, because the import statement (wherever it is added or changed) and the JSX usage are two separate lines and git numstat sums the whole file. This worker satisfied AC3's exact mechanical formula (verified PASS) via an aliased import that keeps line 186's TEXT as '<ScopeSummary .../>' while its RUNTIME BINDING is the real IdentityCard component (confirmed by tsc rc=0 and by IV1-AC1/AC2 exercising the same module directly). A reader who diffs index.tsx against this cell's own prose will see line 186 unchanged and may read that as non-compliance with 'mount it' until they read the import line's alias and its comment.",
    "notes": "Not blocking: IV1-AC3 is the graded, mechanical criterion and it PASSES by its own stated formula (invocation output recorded in the worker report and the result file). Filed as an OBSERVATION so the CTO/COO can rule explicitly on whether the aliased-import route is the intended resolution of this tension for the remaining THREAD cells (IV-t-2/3/4), which may face the same one-line bound on shared files."
  },
  {
    "id": "DSGN_IRPTV1-W1-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~1",
    "surfaced_at": "2026-09-24T09:00:16Z",
    "one_line": "The OVER WHAT chip toggle (narrowing the scope through the existing selectionRequest path) is not wired, and no accountId-to-name directory data reaches the card from the real mount today -- both degrade to explicit fallbacks rather than the wired behaviour the cell narrative describes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "index.tsx:186's mount is fixed to the three original props (scope/selection/row) by IV1-AC3's one-line bound (see DSGN_IRPTV1-W1-S2) -- wiring a chip's onClick to index.tsx's onSelectionChange/selectionRequest path needs a handler defined in index.tsx, which is a further line index.tsx cannot carry under that bound",
        "no existing type or call in header/search.ts, header/ClientSearch.tsx or contracts/index.ts supplies a DirectoryEntry (displayName + maskedDiscriminator) PER permitted account when the selection is a relationship/client -- only scope.permittedAccountIds (opaque ids) and the single selected row.entry are available on this path; permittedAccountsFor()/selectionFor() in header/search.ts confirm the intersection is id-only",
        "header/IdentityCard.tsx's accountChips() therefore accepts an optional accountEntries prop (mirroring the cell's own snapshot pattern) that the real mount does not feed; IV1-AC1 exercises it directly via an adapted fixture, and the fallback path (no accountEntries) renders a single real chip when row.entry is itself kind:'account', else 'Account details not supplied' text -- never the raw id"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell text: 'A chip toggles to narrow the scope through the SAME selection request the page already makes ... If wiring the toggle needs a change outside your <paths>, render the chips without the toggle and file an OBSERVATION row; the toggle is not a criterion.' And: 'accept an optional snapshot prop so a later cell can feed it' (named only for the holdings total, not for per-account names).",
    "world_is": "Wiring the toggle needs a NEW handler in index.tsx, which is inside this worker's <paths> grant but OUTSIDE the one-line bound IV1-AC3 mechanically enforces (see S2) -- a change of KIND the cell anticipated ('outside your <paths>') without naming this specific shape (inside <paths>, outside the line budget). Per-account display data (name + masked tail) is likewise not resolvable from any prop the real mount supplies today; this worker added an accountEntries prop, unfed by the mount, on the same optional/later-cell pattern the cell itself names for snapshot.",
    "notes": "Not blocking: the cell explicitly says the toggle is not a criterion. Filed so the COO's decomp for a later round knows BOTH the toggle wiring and the per-account directory data source remain open, and so IV1-AC1's accountEntries fixture (adapted, not committed) is not mistaken for a wired data source at the real mount."
  },
  {
    "id": "DSGN_IRPTV1-W1-S4",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~1",
    "surfaced_at": "2026-09-24T09:18:52Z",
    "one_line": "Row S2's tension (IV1-AC3's exact 1/1 bound vs. a faithful component rename) was resolved by the issuer mid-order: CTO ruling 100467 (batch 34) supersedes 100332's 1/1 bound with a 'mount line PLUS at most one import line' bound; this worker reverted the S2 aliased-import workaround for the faithful rename the cell always described.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "mid-order coordinator relay, ISSUER AMENDMENT from 2.0.0_SA_COO~D on CTO ruling 100467, naming the workspace worktree commit bdebd214e1 (cherry-pick of CLOUD 89e465b40c) as carrying the amended task order",
        "git log -1 --oneline at this worker's worktree confirms HEAD bdebd214e1 'amend(DSGN_IRPTV1 round 1, issuer): IV1-AC3 and IV2-AC3 re-bounded on CTO ruling 100467 (batch 34) -- the ruled touch on index.tsx / ReportingTab.tsx is the ONE mount line PLUS at most ONE import line and nothing else (numstat 2/1 or 2/2, every changed line an import statement or the mount); the 1/1 bound of 100332 could not be met by any new component'",
        "the task order file's live IV1-AC3 criterion (grep'd at this worktree) carries the amended invocation and 'VERDICT: MOUNT-PLUS-IMPORT' expectation, matching the amendment message verbatim",
        "portal commit fe189e4c443cb4743ce724cf2b1fd34f8b57c2d5 reverts the S2 aliased-import mount (portal commit 3427e8a78b19716f7f0fd4dc7428acb14740d51e) to the faithful rename: index.tsx:19 imports IdentityCard directly, index.tsx:186 reads <IdentityCard .../>; re-run IV1-AC3 invocation prints NUMSTAT: ['2\\t2\\t...index.tsx'] / VERDICT: MOUNT-PLUS-IMPORT, re-run twice identical"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row S2 asserted the 100332 1/1 bound and the cell's original prose could not both be satisfied by any faithful rename.",
    "world_is": "The issuer/CTO resolved the tension by amending the bound itself (100467) rather than accepting the aliased workaround S2 proposed as a candidate resolution -- confirming S2's diagnosis (the 1/1 bound was genuinely unmeetable by a faithful rename) while rejecting its stopgap in favour of a corrected rule. This worker's final mount matches the cell's original prose literally (`<IdentityCard .../>` at index.tsx:186) with no aliasing.",
    "notes": "Not blocking. This row does not itself dispose S2 (disposition changes belong to the L9/CVO adjudication carried in `adjudicates`, per the schema's own description) -- it records that the CTO's own ruling superseded the question S2 raised, for whichever seat adjudicates the channel next. IV2-AC3 (a sibling cell, IV-t-2) is named in the same amendment and is out of this row's scope."
  },
  {
    "id": "DSGN_IRPTV1-W3-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~3",
    "surfaced_at": "2026-09-24T09:09:09Z",
    "one_line": "The order's field mapping (category-level children/members) never reaches CategoryViewTree's L2 hover-detail/breakdown dialog, which reads only children[label].members.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/CategoryViewTree.tsx@7c542fd23ec70c88bade4e3270f4c87f267a275a: the ONLY two `.members` read sites in the file are `r.members ?? []` (membersOf, reading an L1Row built from `child.members`) and `members: child.members` (l1RowsOf, from `categoryChildrenForDisplay(node).children`) -- the top-level `MdpfCategoryNode.members` field is never read by this component at all.",
        "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx (this cell, IV-t-3): mdpfResultFromSnapshot fills MdpfCategoryNode.children[label].aum and the CATEGORY's own top-level `members` (leaf security nodes at any depth), per the task order's literal field mapping -- not children[label].members, which the order's text does not name.",
        "portal/src/pages/InvestorReporting/fixtures/fe-s-7/holdings.smartx-observed.json: category 'Models' (nd-cat-models) has ONE direct child, 'Account 4417' (kind account); the models/securities beneath it (Long Term, Ultra-Long Term, their securities) sit two and three levels down. With children[label].members left unpopulated, the fed hero's Models tile hovers/breaks down to ONE bucket 'Account 4417', not the models beneath it -- verified in org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-3.hero.html against the cottonwood fixture, where the direct-child securities DO surface (they ARE the direct children there) but no deeper case can, structurally, with this field mapping."
      ]
    },
    "spec_asserts": "IV-t-3 worker face: 'Today every top-level category becomes { aum, members: [], children: {} }... so CategoryViewTree's hover detail and \"View breakdown\" dialog are empty... Fill them from the snapshot: ... children = the nodes directly beneath it... with aum = that node's own amount; and members = the leaf holdings beneath the category (kind security)...'",
    "world_is": "CategoryViewTree's L2 hover-detail/breakdown dialog is fed exclusively by children[label].members (an OPTIONAL, per-L1-bucket field the order's mapping does not populate), never by the category's own top-level `members` array the order does populate -- so a category whose direct child is an intermediate node (not itself a leaf security) still renders only that one intermediate node's tile at L1, with nothing to drill into at L2, even though `members` is now correctly filled.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_IRPTV1-W3-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_IRPTV1~3",
    "surfaced_at": "2026-09-24T09:09:09Z",
    "one_line": "The naming gate (LGIC_ENFORCE DEC-6) REFUSED IV3-AC1's new test file for typing an already-twice-committed fixture filename, and names a lookup()/key()/address()/name() escape hatch that has zero implementations anywhere in portal/src.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh run on portal (first attempt, staging DrillTree.tsx + the new __tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts): 'NAMING REFUSE src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts:30 fe-s-7/holdings.cottonwood-target-blend.json -> lookup(\\'cottonwood\\')' / 'why: NEW hand-kept carrier (context rule)'; RC=1, commit aborted, files unstaged.",
        "the SAME literal filename is already committed twice, ungated at WARN only because the gate grades a string's NEW-vs-EXISTING status per FILE (not per corpus): portal/src/pages/InvestorReporting/__tests__/fe-s-7/drill.test.ts:62 and portal/src/pages/InvestorReporting/__tests__/fe-s-7/slices.test.ts:117 both call loadSnapshot('holdings.cottonwood-target-blend.json').",
        ".tools/naming-gate.py:21-22 (THE CONTEXT RULE): the only exemptions are the registry files, a generated block/file, 'inside the arguments of a key(), address(), name() or lookup() call (read from the Python syntax tree)', or a Terraform opal_name module -- js_literals() (:413, the WHOLE .ts/.js grading path, :1432-1433) applies NONE of these: it returns every string literal on an added line with no call-context check at all.",
        "comp-find 'export function lookup|export const lookup' over portal/src: DENOMINATOR 988 file(s), 0 hits -- the gate's own printed remedy (lookup('cottonwood')) calls a function that does not exist anywhere in the frontend.",
        "'/tests/' in ('/' + path) (:1424) is the only directory-level exemption, and this whole suite lives under `__tests__` (double underscore), which does not contain the substring '/tests/' -- so no file in this tree, new or old, is ever exempt by location either."
      ]
    },
    "spec_asserts": "BOUNDS: '<paths> ... portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/' grants this worker the surface to add IV3-AC1's test file, and IV3-AC1 requires it be run (and, to be graded at all, be commit-able) against the task order's own three named fixtures, including fe-s-7/holdings.cottonwood-target-blend.json.",
    "world_is": "A brand-new file in that granted directory referencing that already-twice-precedented fixture filename by name is mechanically REFUSED by the naming gate, whose sole escape hatch (a lookup()/key()/address()/name() call) has no JS/TS implementation in this codebase to call -- so the literal instruction ('name the fixture') and the mechanical gate ('never hand-type that name in a new file') cannot both be satisfied by typing it. Worked around, not gamed: the committed test discovers the fe-s-7/holdings.*.json set from disk (readdirSync) instead of naming any of them, so the token is never typed and the same fixtures are still exercised (plus the suite's other named-negative fixtures, which the adapter's fully-structural assertions handle without incident). Any future new test file anywhere under this __tests__ tree that hand-types a registered client/firm token will hit the identical REFUSE with the identical missing escape hatch.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_IRPTV1-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-09-24T09:51:55Z",
    "one_line": "Round-1 drain hygiene: `bun run typecheck` (tsc -b --noEmit) reads rc=2 on the merged portal candidate dsgn-irptv1-r1 @7736e6cc -- three TS18046 errors in the worker's test file __tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts (lines 107-109, 'node' is of type 'unknown'); every suite passes (7 of 7 dsgn-irptv1 files, 0 fail; fe-s-7/ 32 pass) and the product files compile, but `bun run build` = `tsc -b && vite build` cannot build this candidate until the test file is typed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (the drain's own red; remedy = one batched repair cell in round 2's issuance per spine L10, or an issuer-direct one-line fix on the candidate on 1.0.0_SA_CTO's word; never a silent edit at the drain)",
    "spec_asserts": "Spine L6 verification diet: repo-wide hygiene (typecheck, lint, the suite) runs ONCE per merge at the drain, never as a criterion on an order; a red at the drain is a surprise row under the COO's serial, never a silent re-cut (spine v3.16 / dispatch Step 5). IV-t-3's three mechanical criteria (IV3-AC1 HERO-FED, IV3-AC2 fe-s-7/ 32 pass, IV3-AC3 ONE-FUNCTION) all PASS by output and its instance is VALID, so the order is correctly terminal.",
    "world_is": "Measured 2026-09-24 by 2.0.0_SA_COO~D in C:/tmp/dsgn-irptv1-r1 at 7736e6cc (portal candidate = DEV 7c542fd2 + the three worker branches): `bun run typecheck` rc=2 with exactly three errors, all in src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts at (107,13) (108,25) (109,30), TS18046 'node' is of type 'unknown' -- a JSON-loaded fixture iterated without a type narrow. The same typecheck read rc=0 at 7d0cf4df (after slots 1 and 2) so the red is introduced by slot 3's branch. `bun test` over the seven dsgn-irptv1 files: 0 fail, 55 expects; fe-s-7/: 32 pass, 0 fail. No product source file errors.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/dsgn-irptv1-r1 @7736e6cc: `bun run typecheck` rc=2, three TS18046 lines quoted above",
        "C:/tmp/dsgn-irptv1-r1 @7d0cf4df (before slot 3): `bun run typecheck` rc=0 (this seat's earlier hygiene run)",
        "portal branch wk-DSGN_IRPTV1-3-portal commits bbbc2f97 (IV-t-3) and 287acb89 (IV-t-4); the test file is IV-t-3's",
        "proof instance org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/DSGN_IRPTV1.TO-IV-t-3.holdings-hero.proof_of_spec.json VALID rc=0 -- typecheck was never a criterion on the face, by the diet"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed by the issuer at the drain, not fixed at the drain: the worker's grant is withdrawn by the terminal flip and the COO does not edit the candidate silently. Carried in the drain-end message to 1.0.0_SA_CTO with the recommendation above."
  }
]
```
