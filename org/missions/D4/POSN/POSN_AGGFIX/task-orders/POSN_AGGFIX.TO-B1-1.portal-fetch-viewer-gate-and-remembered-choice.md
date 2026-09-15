# TO POSN_AGGFIX.TO-B1-1 -- THE PORTAL'S DATA HALF: the page predicate read, ONE fetch for the Opal-only file, the page fetching it only for an Opal viewer and merging the aggregate into the data the Holdings tab reads, and the book set honouring a remembered aggregate only for a viewer whose own set holds it -- with the five model views captured BEFORE any edit (AF1-s-3, AF1-s-12, AF1-s-13, AF1-s-15; FWD-1, FWD-2, FWD-7, FWD-9)

<to_id>POSN_AGGFIX.TO-B1-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-EXISTING-PREDICATE, C-OPAL-ONLY-DATA, C-DEFAULT-UNLESS-REMEMBERED, C-FIVE-BOOKS-UNCHANGED, C-PORTAL-PROMOTE) - **Decomp
cells:** `AF1-s-3`, `AF1-s-12`, `AF1-s-13`, `AF1-s-15` - **Issuance:** round 1, slot `~3`, FIRST of three orders in this slot's queue (then
TO-B2-1, then TO-B3-1); runs in PARALLEL with slots `~1` and `~2`, whose files are disjoint from yours. **COMMIT YES, PROMOTE NO:** the
gitlink never moves and nothing is pushed.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~3;`. Your workspace worktree is
`/c/tmp/wk-aggfix-1-3` (branch `wk-posn_aggfix-1-3`, a sparse cone; do NOT re-create it). Your portal worktree is
`/c/tmp/wk-aggfix-1-3/portal`, a linked worktree of the portal repo on YOUR branch `wk-aggfix-1-3-portal`, PRE-CUT by the COO FROM portal
`edf85ce503` (origin/PROD); verify with `git -C /c/tmp/wk-aggfix-1-3/portal rev-parse --abbrev-ref HEAD` and
`git -C /c/tmp/wk-aggfix-1-3/portal merge-base --is-ancestor edf85ce503 HEAD`. Its `node_modules` is a junction to the main portal install
(vite and playwright-core present; never touch package.json or the lockfile). First act: `git rev-parse --abbrev-ref HEAD` and
`test -d org && test -d .tools && echo TREE-OK`. Workspace commits via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_AGGFIX~3 <0.9.0_WK_POSN_AGGFIX~3@opal.agent>" -F <msgfile> -- <paths>` (msgfile by
the Write tool, PURE ASCII). Portal commits inside the portal worktree on your branch:
`git -C /c/tmp/wk-aggfix-1-3/portal commit --author "0.9.0_WK_POSN_AGGFIX~3 <0.9.0_WK_POSN_AGGFIX~3@opal.agent>" -F <msgfile> -- <paths>`.
Never push, merge, rebase, `checkout --`, `clean`; never `git add portal` in the workspace. Append your branch line to
`org/missions/D4/POSN/POSN_AGGFIX/ledger/PORTAL_REFS.md` at your first portal commit. Every portal bar below is anchored on the FIXED commit
`edf85ce503`, never on a drain ref. Scratch in `/c/tmp/wk-aggfix-1-3/.scratch/` only.

## THE CELLS (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-3` -- what the page's internal check admits (S3, C-EXISTING-PREDICATE).** At the portal base `edf85ce503`: read `isInternal` /
`isDev` in `src/contexts/AuthContext.tsx` (L5: :736-737, :750-751, :118-119) and where `firmId` and `userType` come from (the JWT claims);
record which viewers `isDev()` admits beyond Opal staff, if any. The gate in AF1-s-11 mirrors this reading; a viewer class the two
readings treat differently is a BLOCKING row.

**`AF1-s-12` -- the fetch (S12, C-OPAL-ONLY-DATA).** `portal/src/api/portal-proxy.ts`: `getPositioningData` (:1177) byte-unchanged; ONE new
exported fetch for `/api/general/positioning/opal_aggregate.json` returning the 1.1 payload typed, through the same `apiRequest` helper.

**`AF1-s-13` -- the page hands the predicate down and fetches only for Opal (S13, C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED).**
`portal/src/pages/Positioning/Positioning.tsx`: `internal` (:267) is passed to the `HoldingsTab` mount (:642); the aggregate fetch runs only
when `internal` is true and only in Models mode; on `status OK` with holdings its `current_holdings.AGG` is merged into the Positioning data
object the tab reads; otherwise nothing is merged. Advisor and client code paths issue no request for the key. How the aggregate behaves
while an internal viewer has a partner firm selected is read from the page and recorded (C-ONE-BOOK).

**`AF1-s-15` -- the book set and the remembered choice (S15, C-EXISTING-PREDICATE, C-DEFAULT-UNLESS-REMEMBERED).**
`portal/src/pages/Positioning/shared/bookSet.ts`: `capabilitiesFor(mode)` (:299) stays mode-only and gains NO aggregate capability; the
no-aggregate rationale (:238-257, :39-46) is rewritten to cite this project and the viewer-scoped entry; a remembered or hand-edited `'AGG'`
is honoured only when the viewer's own book set contains it and otherwise falls back to the ordinary default, mirroring the existing
`visibleModes` check on remembered mode.

**THE 1.1 CONTRACT your fetch types (decomposition s.1.1; the producer and the edge are cut against the same keys):**
```
{ "status": "OK" | "UNAVAILABLE", "reason": null | "<one line>", "generated_at": "<ISO Z>", "data_as_of": "<YYYY-MM-DD>",
  "current_holdings": { "AGG": { "holdings": [ <exactly today's AGG holding shape> ], "total_aum": <float> } },
  "weights": { "UST": w, "ST": w, "INT": w, "LT": w, "ULT": w },
  "weights_source": { "key": "...", "version_id": "...", "period": "..." },
  "members": { "UST": aum, ..., "ULT": aum, "blends": [ { "model_name": "...", "aum": x, "constituents": { ... } } ] },
  "left_out": [ { "model_name": "...", "aum": x } ],
  "reconciliation": { "five_primary_sum": x, "members_sum": y, "file_total_model_aum": z, "gap": z - y, "gap_explanation_ref": "..." } }
```
The page offers an aggregate ONLY when `status == "OK"` and `current_holdings.AGG.holdings` is non-empty.

**Measured by the issuer at portal `edf85ce503` -- read each back:** `Positioning.tsx` (652 lines) `useAuth` :54, `const { claims, isInternal,
isDev } = useAuth()` :260, `visibleModes = modesFor(claims?.firmId ?? null)` :261, `const internal = isInternal() || isDev()` :267;
`shared/bookSet.ts` (644 lines) the no-aggregate rationale :238-257 and `capabilitiesFor` :299; `tabs/HoldingsTab.tsx` (1854 lines) imports
`resolveBooks, capabilitiesFor` from `../shared/bookSet` :16, `const caps = capabilitiesFor(bookMode)` :627, FIRST-RENDER LANDING :841-848;
`src/api/portal-proxy.ts` `getPositioningData` issues `/api/general/positioning/positioning_data.json` at :1178. The removal diff is
`git -C <portal> show d53049a0 -- src/pages/Positioning` (5 files, 183 insertions, 308 deletions). **Fixtures:** the served AGG block of
`s3://opal-data-portal-v2/json/positioning/positioning_data.json` VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou` re-keyed into the 1.1
payload (status OK) is the aggregate fixture; the same object minus `current_holdings.AGG` is the shared-file fixture. **The render harness
you reuse:** `org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~26/w3_dom_read.mjs` (system Edge, the stubbed
`/auth/refresh` SESSION at :45-50, the longest-substring fixture router at :56-66) -- copy it into your deliverables and vary the SESSION's
user claims per viewer class, reading `AuthContext.tsx` for the claim shape of an advisor and a client.

## YOUR ACT

1. BEFORE YOUR FIRST PORTAL EDIT: `<FIVE_BOOKS_DOM_B>` run on your branch at `edf85ce503` with the shared-file fixture as an advisor and as
   a client, Models mode, each of UST ST INT LT ULT: the Portfolio Composition and Holdings Breakdown text per book saved to
   `B_DOM_BEFORE.json` in your deliverables. TO-B2-1 and TO-B3-1 compare against this file; it is never re-captured.
2. `portal-proxy.ts`: the one new exported fetch and its types. `Positioning.tsx`: `internal` passed to the `HoldingsTab` mount; the
   internal-only, Models-only fetch; the merge through ONE exported pure helper (for example `mergeOpalAggregate(data, payload)`) placed in
   `shared/bookSet.ts`. `bookSet.ts`: the viewer-scoped aggregate entry in the book resolution the tab uses, the remembered-choice check,
   and the rewritten rationale. `HoldingsTab.tsx` is NOT yours in this order (TO-B2-1 restores the UI).
3. Commit in the portal worktree; append PORTAL_REFS; commit deliverables in the workspace; record every criterion.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W3-S<k>` (start at S1; class OBSERVATION or BLOCKING only; pure ASCII), inside the fenced
json array of `org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md` per the investigation schema (`project`
POSN_AGGFIX, `fabric` site-z, `disposition` UNDER_INVESTIGATION; ARMED needs `disarm_owner` `2.0.0_SA_COO~Z`). Keep working.

## CRITERIA -- structured, one clause each

<criterion id="B1-AC1" cell_refs="AF1-s-3"><invocation>timeout 120 python <PREDICATE_READ_B1></invocation><expect>from `git -C /c/tmp/wk-aggfix-1-3/portal show edf85ce503:src/contexts/AuthContext.tsx`: the isInternal and isDev bodies with line numbers, the lines where claims.firmId and claims.userType are assigned and from what source, a line `PAGE PREDICATE: firmId === 'opal-capital' OR userType === 'Dev'` (or the exact predicate read, if different), and one line per viewer class the predicate admits beyond firmId opal-capital (or `NONE BEYOND OPAL STAFF AND DEV`).</expect></criterion> `B1-AC1` -- THE PAGE'S PREDICATE, READ AT THE BASE.

<criterion id="B1-AC2" cell_refs="AF1-s-13,AF1-s-15"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --capture-before --out org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/B_DOM_BEFORE.json</invocation><expect>run at portal HEAD == edf85ce503 (printed) before any portal edit; 10 captures (advisor and client x UST ST INT LT ULT), each with the composition labels and the breakdown rows counted and saved; a line `CAPTURED 10 of 10`; the claim sets used for advisor and client printed.</expect></criterion> `B1-AC2` -- THE FIVE MODEL VIEWS, CAPTURED BEFORE ANY EDIT.

<criterion id="B1-AC3" cell_refs="AF1-s-12"><invocation>timeout 60 git -C /c/tmp/wk-aggfix-1-3/portal diff edf85ce503 HEAD -- src/api/portal-proxy.ts</invocation><expect>only added lines: one exported fetch function issuing /api/general/positioning/opal_aggregate.json through apiRequest and its types; no hunk inside getPositioningData.</expect></criterion> `B1-AC3` -- ONE NEW FETCH, THE OLD ONE UNTOUCHED.

<criterion id="B1-AC4" cell_refs="AF1-s-13,AF1-s-15"><invocation>timeout 300 bash <UNIT_RUN_B1></invocation><expect>the unit control for the pure helpers, printed per case with PASS: merge with status OK and holdings present puts current_holdings.AGG into the data; status UNAVAILABLE merges nothing; OK with empty holdings merges nothing; the resolved book set for an internal viewer with the aggregate merged has Aggregate FIRST, and without it has no Aggregate; advisor and client never have Aggregate; a remembered 'AGG' for a client falls back to the ordinary default and for an internal viewer with the aggregate merged is honoured; capabilitiesFor(mode) returns output identical to the edf85ce503 version for every mode; and a NEGATIVE CONTROL case (the remembered-choice check disabled in memory) reports the client landing on 'AGG'.</expect></criterion> `B1-AC4` -- THE HELPERS DO WHAT THE CELLS SAY, WITH A CONTROL THAT CAN FAIL.

<criterion id="B1-AC5" cell_refs="AF1-s-13"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --network-arms</invocation><expect>on your branch HEAD, the page opened in Models mode as Opal staff, as an advisor and as a client, with every request URL recorded: requests to opal_aggregate.json -- Opal staff 1 or more, advisor 0, client 0 (a table of the three counts); and the same three in ETFs mode: 0, 0, 0.</expect></criterion> `B1-AC5` -- ONLY AN OPAL VIEWER, ONLY IN MODELS MODE, ASKS FOR THE FILE.

<criterion id="B1-AC6" cell_refs="AF1-s-15"><invocation>timeout 60 git -C /c/tmp/wk-aggfix-1-3/portal diff edf85ce503 HEAD -- src/pages/Positioning/shared/bookSet.ts</invocation><expect>the capabilitiesFor function body and BookSetCapabilities carry no hunk; the rationale comment at the former :238-257 is rewritten to cite POSN_AGGFIX and the viewer-scoped entry; the helper and the book-resolution change are the only other hunks.</expect></criterion> `B1-AC6` -- NO AGGREGATE CAPABILITY ON THE MODE.

<criterion id="B1-AC7" cell_refs="AF1-s-12,AF1-s-13,AF1-s-15"><invocation>timeout 900 bash <TYPECHECK_RUN_B></invocation><expect>the portal's own typecheck command printed (read from package.json at your portal HEAD) and run through the junctioned install with exit 0 and 0 errors; then the same command on a scratch copy carrying one deliberate type error exits non-zero (the command can fail).</expect></criterion> `B1-AC7` -- THE TYPECHECK, SHOWN ABLE TO FAIL.

<criterion id="B1-AC8" cell_refs="AF1-s-13"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --compare-before org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/B_DOM_BEFORE.json</invocation><expect>on your branch HEAD with the same fixtures, the 10 advisor and client captures IDENTICAL to B_DOM_BEFORE.json (`IDENTICAL 10 of 10`), and a control capture with one fixture weight mutated reported as a difference.</expect></criterion> `B1-AC8` -- WHAT ADVISORS AND CLIENTS SEE HAS NOT MOVED.

<criterion id="B1-AC9" cell_refs="AF1-s-13" judgment="true"/> `B1-AC9` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** what the page does with the aggregate while an internal viewer has a partner firm selected (C-ONE-BOOK), as read and recorded, and whether that behaviour could lead an Opal user to read Opal's mix as a partner's. Record the readings and offer NO verdict.

<expected_criteria>B1-AC1, B1-AC2, B1-AC3, B1-AC4, B1-AC5, B1-AC6, B1-AC7, B1-AC8, B1-AC9</expected_criteria>

<placeholders>PREDICATE_READ_B1, FIVE_BOOKS_DOM_B, UNIT_RUN_B1, TYPECHECK_RUN_B</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-B1-1.portal-fetch-viewer-gate-and-remembered-choice.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_AGGFIX/ledger/PORTAL_REFS.md
portal/src/api/portal-proxy.ts
portal/src/pages/Positioning/Positioning.tsx
portal/src/pages/Positioning/shared/bookSet.ts
portal/src/pages/Positioning/README.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-3 AF1-s-12 AF1-s-13 AF1-s-15</owned_cells>
Read-dependencies, NOT claimed: the 1.1 contract. DOWNSTREAM: `AF1-s-14` (TO-B2-1) builds on your helpers and your B_DOM_BEFORE.json;
`AF1-s-11` (TO-C1-1, slot ~2) mirrors your B1-AC1 predicate; `AF1-s-16` (TO-B3-1) compares against B_DOM_BEFORE.json.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; no deploy, no promote, no push in this order; the portal promote is Andrew's word.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or cloud write; the fixtures come from one read-only S3 object version.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the advisor and client claim sets for the render harness are not constructed by the issuer; (2) whether the portal has a TypeScript unit runner beyond the one POSN_ASTTAX round 6 used is unread -- read that round's recorded invocation first; (3) where the remembered book is stored (the storage key name) is unread by the issuer; (4) the partner-firm selection behaviour for internal viewers is unread.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/POSN_AGGFIX.TO-B1-1.portal-fetch-viewer-gate-and-remembered-choice.proof_of_spec.json
</proof_of_spec>
