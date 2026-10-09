# AMGT_RESAPP task order -- `AMGT-mm-2` -- THE SECURITY ANALYSIS DESCRIPTION CARD SHOWS ONE PLAIN EMPTY-STATE LINE WHEN THE DESCRIPTION IS WITHHELD OR EMPTY (PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-mm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~349</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one component and its harness.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the harness renders statically.
comp-adversary: RUN at the cut -- `portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx:425-428` renders `served?.reason || 'No company description is on file.'` when no description text is served: the /overlay reason is an engineering string ("no description header scalar [...] and no served D-1 ..."), so NU's empty card would print it. Security Analysis is an Opal-internal (staff-only) page.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-349`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-mm-2` (round 88, decomposition s.96)

CTO~DELL1 round-87 analysis item 2 (DSGN_AMGTV1 is closed, so the wording is this project's). In the PORTAL repository, in a portal
worktree on a branch `wk-portal-amgt-mm2` cut from portal `DEV`: when the thesis description is empty or withheld (no served text;
`company_description` 0 sentences, any `description_verdict_state`, `withheld_failed` set or not), the card renders ONE plain line,
`No company description is available for this security yet.`, in navy body ink on the white panel (DESIGN.md C3) -- never the
served `reason` string. A served description renders exactly as today. Add `src/pages/SecurityAnalysis/__harness__/
descriptionEmpty.harness.cjs` (same instrument as `drafting.harness.cjs`: the ACTUAL component, transpiled, rendered by
react-dom/server) with three arms: NU-shaped empty + withheld -> the plain line and no reason text; empty without withheld -> the
plain line; a served description -> its text, unchanged. Then render the page headless on NU (`scripts/ui-smoke.mjs`, the
/frontend-dev method) and save the PNG under the portal worktree's `investigations/amgt-mm2/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W349-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only, branch `wk-portal-amgt-mm2` from `DEV`; never push; never touch `PROD`.
2. Edit `ThesisCards.tsx` and the new harness file only; no other component, no token change.
3. No deploy, no store write, no AWS call. `bun install` is allowed only if `node_modules` is absent in the worktree.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/descriptionEmpty.harness.cjs
portal/investigations/amgt-mm2/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~349/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-mm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/descriptionEmpty.harness.cjs; echo "exit=$?"</invocation><expect>run in the PORTAL worktree, all three arms pass: the empty + withheld card and the empty card show the plain line with no reason text, a served description renders unchanged; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-mm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bun run typecheck; echo "exit=$?"</invocation><expect>run in the PORTAL worktree, the portal typechecks (tsc -b) with 0 errors; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-mm-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~349 <0.9.0_WK_AMGT_RESAPP~349@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~349/AMGT_RESAPP.TO-AMGT-mm-2.the-description-card-shows-a-plain-empty-state.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the portal branch and commit hash;
- every criterion's output lines;
- the NU screenshot path and the CANVAS line ui-smoke printed;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-87 analysis @08279f2a4f item 2. A portal candidate touching a product file: the CTO reviews it before the DEV landing; PROD promote is a separate pair (Security Analysis is Opal-internal). AC3 is JUDGMENT: the CVO reads NU's screenshot at L9. Checks dry-run at the base (portal DEV c96efe17): AC1 base FAIL (no harness file); AC2 base PASS (a bound).

<status>pending</status>
<round>88</round>
<slot>0.9.0_WK_AMGT_RESAPP~349</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- issuer close 2026-10-09T21:0xZ: the portal DEV CANDIDATE is built -- portal branch wk-portal-amgt-mm2 @bfd177a1c3 (ThesisCards.tsx +2/-2, descriptionEmpty.harness.cjs, the NU screenshot); proof @886624a418 VALID, merged to box/dell1. Issuer re-run in the portal worktree: AC1 fails=0 (3 arms, 8 checks; the pre-change file fails 4); AC2 tsc -b exit 0 (worker). AC3 is JUDGMENT for the CVO at L9: investigations/amgt-mm2/nu-description-empty.png (FIXTURE-fed: BA's bundle re-keyed to NU with the description emptied and withheld -- no live read was in bounds). Owed: the CTO's product-file review before the DEV landing (sent); PROD is a separate pair. Issuer cleanup: the worker's dev server on port 5175 (the law is 5174) was still listening -- stopped (pid 12300).</status>
