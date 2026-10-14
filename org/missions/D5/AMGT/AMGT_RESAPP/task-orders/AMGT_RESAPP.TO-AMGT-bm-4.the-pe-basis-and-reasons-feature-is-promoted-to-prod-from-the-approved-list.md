# AMGT_RESAPP task order -- `AMGT-bm-4` -- THE P/E BASIS AND REASONS FEATURE IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bm-4</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bm-4.the-pe-basis-and-reasons-feature-is-promoted-to-prod-from-the-approved-list</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-pe-basis-and-reasons` reads `state=APPROVED valid=yes row=dell1-20261014T111220Z-faa4 ... head_sha=84fd6461bbf890508ded3a82f0fba344f382125c commits=3 class=opal-internal`; `git -C portal diff --name-status 7db035e4 84fd6461bb` reads five paths, all under `src/pages/SecurityAnalysis/` (three added under `__harness__/`, `tabs/ModelTab.tsx` and `types.ts` modified); origin/PROD reads `7db035e448` and origin/DEV `ab8ecc5662` at the cut (2026-10-14 ~11:4xZ), and the candidate is NOT yet in DEV: the merge-forward is the box manager's, asked of `0.0.0_AB_MSTR~DELL1`. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bm-4` (round 106, decomposition s.115)

The CTO closed the approval row `dell1-20261014T111220Z-faa4` APPROVED at head `84fd6461bb` (class Opal-internal: no word from Andrew; record `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_PORTAL_CAND_PE_BASIS_AND_REASONS_20261014.md`), and named this seat for the promote (CTO msg 5466). Do, in order:
1. **Wait for the merge-forward.** Run `git -C C:/dev/ajb_workspace/portal fetch origin DEV -q && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor 84fd6461bb origin/DEV && echo IN-DEV`. If it does not print `IN-DEV`, STOP and report that the merge-forward is not done: do not build, do not promote.
2. In the portal repository (`C:/dev/ajb_workspace/portal`), run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-pe-basis-and-reasons` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
3. Promote the release with `/prod-deploy`. The release carries ONE feature, five files under `src/pages/SecurityAnalysis/` (the Model tab's price basis under a historical P/E, the All-figures grid's dash reasons, a withheld forward P/E's served reason, and the harness with its two fixtures); no other candidate is in it. Your receipt names `/security-analysis` as Opal-internal.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT_BM4.md` with the sections `## Release` (the release branch, the PROD head before `7db035e4` and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

BAR: do NOT execute your older pending face `OPAL_ADVIPOINTERS.P4-PROMOTE-49F`; it reads pending but looks shipped and its issuer closes it. Use no other face and no other branch for this order.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section, `fcdfc34843`, Andrew-direct ~11:4xZ 2026-10-14; relayed by MSTR~DELL1 msg 5493): the merge-forward in step 1 is that script's run by the box manager, never yours.
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bm-4"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in src/pages/SecurityAnalysis/tabs/ModelTab.tsx src/pages/SecurityAnalysis/types.ts src/pages/SecurityAnalysis/__harness__/basisAndReasons.harness.cjs src/pages/SecurityAnalysis/__harness__/basisFixture.GOOGL_US_Equity.json src/pages/SecurityAnalysis/__harness__/basisFixture.PBR_US_Equity.json; do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 84fd6461bb:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>five lines `EQUAL <path>` (one per path, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bm-4"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `7db035e4` (the pre-promote head: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bm-4"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT_BM4.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/AMGT_RESAPP.TO-AMGT-bm-4.the-pe-basis-and-reasons-feature-is-promoted-to-prod-from-the-approved-list.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line, THEN stand down.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED SHELL cut 2026-10-14 ~11:4xZ. THE FLOW is `portal/CONTRIBUTING-BOXES.md` step 7 (the promote takes a list, never live DEV whole). THE GO is given when the merge-forward is done (MSTR~DELL1 reports the DEV head; the candidate is an ancestor of it) AND `0.4.0_DT_ClientPlatform` is seated (asked of MSTR~DELL1 at 11:2xZ, CTO msg 5466). The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home, commits under its own lane, and reports to `2.0.0_SA_COO~R1` and `1.0.0_SA_CTO~DELL1`. The class is Opal-internal (route `requireInternal`): no word from Andrew. bm-3 (the served redeploy) waits on THIS promote (the page lands first); bm-5 (census and the fresh-draw walk) waits on both.

<status>staged</status>
<round>106</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
