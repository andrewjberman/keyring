# AMGT_RESAPP task order -- `AMGT-ba-27` -- THE /freshness PAGE IS DEV ONLY: THE PORTAL'S OWN DEV-ONLY MARK ON ITS NAV ENTRY AND ITS ROUTE (ANDREW-DIRECT 2026-10-07)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-27</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~288</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; two tokens in one page file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no read path; a client-side route guard that already exists.
comp-adversary: RUN by the issuer at the cut -- r77_ba27 AC1 FAILS at portal DEV 659104f4 (the nav entry reads requiresTier 'internal' only; the route reads requireInternal only) and AC2 PASSES there (Investor Reporting carries the mark; 1 nav entry and 2 routes). A green arm built by sed reads YES on both.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r77-288` (branch `wk-AMGT_RESAPP-288`, cut from the issuer's tree with `--portal-ref 659104f4 --node-modules link`; `659104f4` is the portal DEV head). Work and commit only there. Start every shell call with `cd /c/tmp/r77-288`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. Your portal checkout is `C:/tmp/r77-288/portal`, on its own branch `wk-AMGT_RESAPP-288-portal`.

## 1. THE ACT -- `AMGT-ba-27` (round 77, decomposition s.85 ADDENDUM 1)

Andrew, verbatim, 2026-10-07 ~04:2xZ: "is freshness page dev only? if not it should be". It is not: on portal PROD and DEV the
/freshness page is shown to every Opal-internal user. The portal already has a dev-only mark (Investor Reporting carries it):
`requiresDev: true` on a nav entry hides it from any user whose `userType` is not `Dev`, and `requireDev` on a route's
`ProtectedRoute` refuses the route to them.

In `C:/tmp/r77-288/portal`:
1. **Bring the approved page candidate in first.** The round's /freshness page change is one commit, `504ddb3d`, on the local
   portal branch `resapp-r77-ba4-freshness`. Merge it into your portal branch with a merge commit
   (`git -C portal merge --no-ff resapp-r77-ba4-freshness`); it merges clean onto `659104f4` (measured). Do not edit its files.
2. **Add the mark, two tokens in `portal/src/App.tsx`:**
   - the nav entry `{ path: '/freshness', label: 'Freshness', icon: Clock, requiresTier: 'internal' }` gains `requiresDev: true`
     (keep `requiresTier: 'internal'`);
   - the route `<Route path="/freshness" element={<ProtectedRoute requireInternal><Freshness /></ProtectedRoute>} />` gains
     `requireDev` beside `requireInternal`.
   Add ONE comment line above the nav entry: `// Andrew-direct 2026-10-07: the /freshness page is dev only (requiresDev + requireDev).`
3. Change nothing else: no other page's mark, no page file, no test rewrite.
4. Run `bun run typecheck` and `bun test src/pages/Freshness/` in `portal/` and report each last line.
5. Commit the App.tsx change on your portal branch (one commit on top of the merge). Do NOT push any portal branch.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W288-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no push, no store write, no other portal file.
2. The mark is the portal's existing one. Do not add a new guard, a feature flag or an environment check.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/App.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~288/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-27"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba27.py" --crit AC1 --portal portal; echo "exit=$?"</invocation><expect>C1-C3 PASS: the /freshness nav entry carries requiresDev: true and stays internal, its route carries requireDev and requireInternal, the page is still mounted; R77 BA27 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-27"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba27.py" --crit AC2 --portal portal; echo "exit=$?"</invocation><expect>C1-C2 PASS (the control): Investor Reporting keeps its mark and no other page gained or lost one; R77 BA27 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit your record in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~288 <0.9.0_WK_AMGT_RESAPP~288@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~288/AMGT_RESAPP.TO-AMGT-ba-27.freshness-page-dev-only.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the PORTAL candidate: the merge commit and the mark commit (short hashes), the branch, and that nothing was pushed;
- every criterion's output lines;
- the typecheck and the page test last lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Andrew-direct at this seat, record `org/tier1_exec/2.0.0_SA_COO~Z/deliverables/ANDREW_DIRECT_20261007_042xZ_FRESHNESS_PAGE_DEV_ONLY.md`. A direct act on his word, mid-round: decomposition s.85 ADDENDUM 1 adds the one cell. The applied reading is the portal's existing dev-only mark; the other reading (the page off the PROD branch) is named in the record and not taken. The candidate this produces replaces `504ddb3d` as the ONE /freshness candidate for the DEV push (the page change the CTO approved @aa1a306ec2, plus the mark); it then needs a PROD promote to take effect where non-Dev users see the page today. Checks dry-run at the base: ba-27 AC1 base FAIL as expected; AC2 base PASS as expected.

<status>pending</status>
<slot>0.9.0_WK_AMGT_RESAPP~288</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
