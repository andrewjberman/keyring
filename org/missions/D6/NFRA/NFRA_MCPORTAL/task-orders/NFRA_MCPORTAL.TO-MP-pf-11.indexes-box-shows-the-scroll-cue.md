# NFRA_MCPORTAL task order -- `MP-pf-11` -- WORKSTREAM PF ROUND 8: the Indexes box on the Gateway page shows the same scroll cue as a tools table

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-11</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-11</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~40</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2 plants a real-length unbroken index name in every list itself; it is the adversary arm.
EGRESS CLASS, declared: none. Make no network call. (The checks open a local browser on a local file.)
</preflight>

## 1. THE CELL -- `MP-pf-11` (workstream PF round 8, decomposition section PF8.1)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pf-40`, branch `wk-NFRA_MCPORTAL-40`;
- inside it, the mcportal worktree `C:/tmp/mp-pf-40/mcportal`, branch `wk-NFRA_MCPORTAL-40-mcportal`, based on mcportal `c66ca82952` (the commit live on origin DEV and on the host today).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-pf-40 &&` (the checks take their root from their own file, but your commands do not).
All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~40 <0.9.0_WK_NFRA_MCPORTAL~40@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~40 <0.9.0_WK_NFRA_MCPORTAL~40@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**The gap.** On the Gateway page each channel section ends with an "Indexes" paragraph (`<p class="gateway-indexes">`, in `src/pages/gateway/GatewayView.tsx`). Its rule in `src/pages/gateway/gateway.css` is only `overflow-x: auto`, so a name wider than the box scrolls and nothing tells the reader it can. The tools tables sit in `.gateway-scroll` boxes that carry a CSS-only cue: four `linear-gradient` layers (white end covers that move with the content, and navy-ink edge shadows that stay put), with `background-position`, `background-repeat`, `background-size` and `background-attachment: local, local, scroll, scroll`. Andrew's words for this page: "making sure that everything is readable by human eyes". Give the Indexes box the same cue.

Build (in `mcportal/src/pages/gateway/`):
1. `gateway.css`: the `.gateway-indexes` rule carries the same cue declarations as the `.gateway-scroll` rule, either by sharing them (put `.gateway-indexes` in the selector list, written so that the existing regexes in `gateway.test.tsx`, which look for `.gateway-scroll {` and `.gateway-indexes {` followed by their blocks, still find a block) or by repeating them. `overflow-x: auto` stays; the paragraph keeps wrapping between names; nothing else changes. The white end covers must match the colour of the surface the paragraph sits on (read the panel's background in the css), so that no white patch shows at an end.
2. ONE test in `gateway.test.tsx`, by this exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the name from your sources; put it as the literal first argument of its `test(...)`), reading `gateway.css` the way the existing test `a scroll box shows a cue that more columns lie off the edge` does:
   - `an index list carries the same scroll cue as a tools table`: the rule block or blocks selecting `.gateway-indexes` hold a `background-image` with `linear-gradient(` and a `background-attachment` that names `local` and `scroll`.
All existing tests keep their names and still pass. `bun test src` now reads 73 or more pass and 0 fail. Do not change the fixture.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof lines are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not print or screenshot any real index name.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~40/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W40-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-11"><invocation>cd C:/tmp/mp-pf-40 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf11.AC1.sh; echo "exit=$?"</invocation><expect>named test present in sources 1 of 1.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-11"><invocation>cd C:/tmp/mp-pf-40 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf11.AC2.sh; echo "exit=$?"</invocation><expect>cue at 390: indexes=[0-9]+ cued=[0-9]+ uncued=0 scrolls=[1-9].*same-as-table-cue=[0-9]+ ok=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-pf-11"><invocation>cd C:/tmp/mp-pf-40 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf8.AC2.sh; echo "exit=$?"</invocation><expect>long names at 390: scrollWidth=390 innerWidth=390 offenders=0 ok=yes.*long names at 1280: scrollWidth=1280.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~40/NFRA_MCPORTAL.TO-MP-pf-11.indexes-box-shows-the-scroll-cue.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1, AC2 and AC3;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-8 issuance (decomposition v18) from the CTO's round analysis @b6efe81187 (CVO v10 enrichment). Checks dry-run at the base (run from /c/Users, in the issuer's render checkout at mcportal c66ca82952 through `MP_PF8_MC`):
pf11.AC1 FAIL as expected (the named test absent in sources; `bun test src` 72 pass, 0 fail); pf11.AC2 FAIL as expected (`cue at 390: indexes=7 cued=0 uncued=7 scrolls=7 same-as-table-cue=0 ok=no`); pf8.AC2 PASS as expected (a bound: 390 of 390, 1280 of 1280, 0 offenders at both, the short-name control ok).
The fix reaches the host only with a new mcportal bundle release; nothing in this order deploys. The status flip is the issuer's.

<status>pending</status>
<status>complete</status>
<round>8</round>
<workstream>PF</workstream>
<slot>~40</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
