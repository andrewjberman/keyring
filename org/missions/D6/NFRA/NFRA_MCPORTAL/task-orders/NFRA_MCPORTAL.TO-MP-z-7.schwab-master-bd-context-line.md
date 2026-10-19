# NFRA_MCPORTAL task order -- `MP-z-7` -- WORKSTREAM GWZ ROUND 1: the Gateway page states, once, which Schwab master Black Diamond reports

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-7</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~41</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named test asserts the line appears exactly once on a fixture with two segments, which is its own adversary arm.
EGRESS CLASS, declared: none. Make no network call.
</preflight>

## 1. THE CELL -- `MP-z-7` (workstream GWZ round 1, decomposition section GWZ1.2)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-gwz-41`, branch `wk-NFRA_MCPORTAL-41`;
- inside it, the mcportal worktree `C:/tmp/mp-gwz-41/mcportal`, branch `wk-NFRA_MCPORTAL-41-mcportal`, based on mcportal `59e802a` (the commit on origin DEV).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-gwz-41 &&` (the checks take their root from their own file, but your commands do not).
All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~41 <0.9.0_WK_NFRA_MCPORTAL~41@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~41 <0.9.0_WK_NFRA_MCPORTAL~41@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**The gap.** On the Gateway page a multi-vendor tool appears under "Schwab / 49 Financial" with Black Diamond indexes beside it, and Andrew reads that as an error. One part of it is a real, correct link: Schwab master 08335338 is the one account that Black Diamond reports. The page should say so in words once, so a correct pairing does not read as an error. (A different cell, `MP-z-8`, fixes the indexes that do NOT belong; do not touch the index lists here.)

Build (in `mcportal/src/pages/gateway/`):
1. `GatewayView.tsx`: render ONE paragraph, `<p className="gateway-context">`, near the top of the page, after the page's header and before the first channel section, with exactly this text: `Schwab master 08335338 is the one Black Diamond reports.` It appears once on the page, never once per segment or per channel. Style it with the page's existing classes or one small rule in `gateway.css` that reuses the page's existing ink and spacing (no new colours; read `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md` for the colour law if you add any rule).
2. ONE test in `gateway.test.tsx`, by this exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the name from your sources; put it as the literal first argument of its `test(...)`):
   - `the page states once that Schwab master 08335338 is the one Black Diamond reports`: render the existing segmented fixture (the one the existing test `a segmented bucket renders one sub-section per vendor and firm` uses, which has two or more segments) and count the occurrences of the exact text `Schwab master 08335338 is the one Black Diamond reports.` in the page's text; it must be 1. Add a second assertion in the same test: rendering the plain `fixture` (no segments) also shows it exactly once.
All existing tests keep their names and still pass. `bun test src` now reads 74 or more pass and 0 fail. Do not change any fixture.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not print or screenshot any real index name.
5. Your queue holds a SECOND order, `MP-z-8`, in the same files. You will be handed it after this one is done and reported; do not start it.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~41/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/gwz/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W41-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-7"><invocation>cd C:/tmp/mp-gwz-41 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/gwz/checks/z7.AC1.sh; echo "exit=$?"</invocation><expect>named test present in sources 1 of 1.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~41/NFRA_MCPORTAL.TO-MP-z-7.schwab-master-bd-context-line.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GWZ round-1 issuance (decomposition v19) from the CTO's round analysis `ledger/ROUND_ANALYSIS.z-round1.md` @11c572fef9, item 2. The CTO's line carries the master number in full; it already appears in the real index names on the same owner-only page, and the line is the CTO's wording. The cell does not reach the host: it rides the next mcportal bundle release.
Check dry-run at the base: see the issuance commit.

<status>pending</status>
<round>1</round>
<workstream>GWZ</workstream>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
