# NFRA_MCPORTAL task order -- `MP-pf-8` -- WORKSTREAM PF ROUND 5: the Indexes paragraph on the Gateway page scrolls inside its own box, so the page never scrolls sideways at 390 px

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-8</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-8</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~38</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2 plants a real-length unbroken index name in every list itself; it is the adversary arm.
EGRESS CLASS, declared: none. Make no network call. (AC2's check opens a local browser on a local file.)
</preflight>

## 1. THE CELL -- `MP-pf-8` (workstream PF round 5, decomposition section PF5.1)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pf-38`, branch `wk-NFRA_MCPORTAL-38`;
- inside it, the mcportal worktree `C:/tmp/mp-pf-38/mcportal`, branch `wk-NFRA_MCPORTAL-38-mcportal`, based on mcportal `090b9cdc85` (the commit live on origin DEV and on the host today).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-pf-38 &&` (the checks take their root from their own file, but your commands do not).
All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~38 <0.9.0_WK_NFRA_MCPORTAL~38@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~38 <0.9.0_WK_NFRA_MCPORTAL~38@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**The defect (measured on the real served data).** On the Gateway page each channel section ends with an "Indexes" paragraph (`<p class="gateway-indexes">`, in `src/pages/gateway/GatewayView.tsx`): the channel's index names joined by commas. A real name is one unbroken token of about 65 characters
(for example `opal_data_assets_silver_commonwealth_cottonwood_account_day_value`), wider than the paragraph's 328 px column at a 390 px screen. It overflows the paragraph, widens its panel and widens the PAGE: at 390 px the page measured 561 px wide, so it scrolls sideways.
Andrew's words for this page: "making sure that everything is readable by human eyes and not wrapped or squished on text and segments". A name must not be cut or broken mid-word, and the page must not scroll sideways: the name scrolls inside its own box. The fixture's names are short, which is why nothing caught it.

Build (in `mcportal/src/pages/gateway/`):
1. `gateway.css`: the `.gateway-indexes` rule takes `overflow-x: auto`. The paragraph keeps wrapping between names (at the commas); a single name wider than the box scrolls inside it. Nothing else changes: the cells still keep their text on one line, headings still wrap between words only, the cue on `.gateway-scroll` stays.
   If AC2 still reads a page wider than its viewport after that, AC2's output ends its measurement line with the first offending elements (`DIV.mcp-page,SECTION.mcp-panel,...`); an offender is an element outside every scroll box whose content is wider than its own box (a scroll box is a `.gateway-scroll` box or any element whose own `overflow-x` is `auto` or `scroll`, such as the Indexes paragraph after step 1: wider content INSIDE it is the point of the fix, never an offender; AMENDMENT 1, the issuer's, after the first AC2 run counted the paragraph itself). Give the next offender the same treatment (a scrolling box, never a mid-word break), inside this directory only, and name each in your report.
2. `gateway.cgroup.fixture.ts`: the `opal-data-assets` channel's `indexes` list and one of that channel's tools' `indexes` lists gain the name `opal_data_assets_silver_commonwealth_cottonwood_account_day_value` (65 characters), so the checked-in fixture exercises it.
   If an existing test pins an index count or an index list of the fixture, change only that number or list to the new truth and name each change in your report.
3. ONE test in `src/pages/gateway/gateway.test.tsx`, by this exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the name from your sources; put it as the literal first argument of its `test(...)`), reading `gateway.css` and the fixture the way the existing test `a scroll box shows a cue that more columns lie off the edge` does:
   - `an index list holding an unbroken real-length name scrolls inside its own box`: the `.gateway-indexes` rule block in `gateway.css` holds `overflow-x: auto`, and some channel's `indexes` in `CGROUP_BREAKDOWN` holds a name of 60 or more characters with no space in it.
All existing tests keep their names and still pass. `bun test src` now reads 72 or more pass and 0 fail.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof lines are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not screenshot or print any real index name beyond the fixture's.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~38/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W38-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-8"><invocation>cd C:/tmp/mp-pf-38 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf8.AC1.sh; echo "exit=$?"</invocation><expect>named test present in sources 1 of 1.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-8"><invocation>cd C:/tmp/mp-pf-38 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf8.AC2.sh; echo "exit=$?"</invocation><expect>long names at 390: scrollWidth=390 innerWidth=390 offenders=0 ok=yes.*long names at 1280: scrollWidth=1280.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~38/NFRA_MCPORTAL.TO-MP-pf-8.indexes-paragraph-scrolls-inside-its-own-box.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1 and AC2;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any further offender you had to fix, or none;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-5 issuance (decomposition v15) from row Z-S64 and the CTO's ruling msg 34947 ("CUT NOW"). The CTO's wording asked for "one test asserts scrollWidth equals the viewport at 390 px on the served body": a renderToStaticMarkup test cannot measure layout and the served body carries real Schwab master numbers in its index names (it must not enter the repo),
so the measurement is AC2, a real-browser check that plants the real-length name itself; AC1's test pins the rule and the fixture. This reading is reported to the CTO in the drain packet.
Checks dry-run at the base (in the issuer's render checkout at mcportal 090b9cdc85, run from /c/Users): pf8.AC1 FAIL as expected (71 pass, the named test absent); pf8.AC2 FAIL as expected (`long names at 390: scrollWidth=557 innerWidth=390 offenders=16`; the short-name control and 1280 px read ok).
The fix reaches the host only with a new mcportal bundle release (a new mcportal_commit in EC2_MANIFEST); nothing in this order deploys. The status flip is the issuer's.

<status>pending</status>
<status>complete</status>
<round>5</round>
<workstream>PF</workstream>
<slot>~38</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
