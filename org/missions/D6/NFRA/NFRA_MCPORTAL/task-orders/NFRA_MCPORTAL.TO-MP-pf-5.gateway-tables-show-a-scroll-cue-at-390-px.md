# NFRA_MCPORTAL task order -- `MP-pf-5` -- WORKSTREAM PF ROUND 3: a Gateway table that scrolls inside its box shows a cue that more columns lie off the edge

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~35</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named test pins the rule; the issuer looks at the render at 390 px after the merge.
EGRESS CLASS, declared: none. Make no network call.
</preflight>

## 1. THE CELL -- `MP-pf-5` (workstream PF round 3, decomposition section PF3.2)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pf-35`, branch `wk-NFRA_MCPORTAL-pf-35`;
- inside it, the mcportal worktree `C:/tmp/mp-pf-35/mcportal`, branch `wk-NFRA_MCPORTAL-pf-35-mcportal`, based on mcportal `421f8fb` (the commit live on origin DEV today).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~35 <0.9.0_WK_NFRA_MCPORTAL~35@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~35 <0.9.0_WK_NFRA_MCPORTAL~35@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**What a reader saw (the CVO's grade of this page at 390 px).** No text is squished or broken inside a word, and the page never scrolls sideways. But every table scrolls INSIDE its box (class `gateway-scroll`, `overflow-x: auto`), so at 390 px
the right-hand columns (Kind, Tools and Holders on the summary table; Data class and Indexes on a tools table) are off the right edge, and nothing on the screen says there is more to the right. A reader may think the table ends at the edge.

**Build** (in `mcportal/src/pages/gateway/gateway.css`; `GatewayView.tsx` only if the CSS cannot do it):
1. A **scroll cue on every `.gateway-scroll` box**, in CSS only (no script, no timer, no new dependency, no new element): a soft fade or edge on the side that still has columns to scroll to, which disappears when the box is scrolled to that end. The standard CSS-only way is
   paired gradients on the box's `background`, two with `background-attachment: local` (a white cover that scrolls with the content and hides the shadow at the end the reader has reached) and two with `background-attachment: scroll` (the fixed shadow on the box edge); the box keeps
   `overflow-x: auto`. Colour: the existing tokens only. The cue colour is the ink token at low opacity, for example `rgba(22, 51, 114, 0.18)` (the ink is navy `#163372`); the cover is the panel's white. No new colour, no new font.
2. Nothing else on the page changes: the cells still keep their text on one line, `min-width: max-content` stays on the table, headings still wrap between words only, and the page itself still never scrolls sideways at 390 px.

**Test**, ONE, by this exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the name from your sources; put it as the literal first argument of its `test(...)`), in `src/pages/gateway/gateway.test.tsx`, reading `gateway.css` the way the existing test
`every table cell keeps its text on one line` does:
- `a scroll box shows a cue that more columns lie off the edge`: the `.gateway-scroll` rule block in `gateway.css` holds `overflow-x: auto`, a `linear-gradient` background, and a `background-attachment` value that names BOTH `local` and `scroll`.
All existing tests keep their names and still pass. `bun test src` now reads 71 or more pass and 0 fail.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof lines are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a).

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~35/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W35-S<k>` (k from 1).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root `C:/tmp/mp-pf-35` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-5"><invocation>cd C:/tmp/mp-pf-35 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf5.AC1.sh; echo "exit=$?"</invocation><expect>named test present in sources 1 of 1.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~35/NFRA_MCPORTAL.TO-MP-pf-5.gateway-tables-show-a-scroll-cue-at-390-px.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-3 issuance (decomposition v13) from the CTO's round-2 analysis @bfe9f3549c (cell S2) and the CVO's grade Z-C-S38 (the 390 px bound). Check dry-run at the base (the render worktree at 421f8fb): `bun test src` 70 pass 0 fail, the named test
absent, so AC1 FAILs as expected. One criterion, so no fourth. The 390 px screenshot of the cue is the issuer's one real run after the merge (not a worker criterion): headless Edge floors at 477 px, so it is taken in a real browser at a true 390 px viewport.
The cue shows on the live page only after the mcportal bundle reaches the host (OG-ap-23).

<status>pending</status>
<status>complete</status>
<round>3</round>
<workstream>PF</workstream>
<slot>~35</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
