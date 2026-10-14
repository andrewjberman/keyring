# AMGT_RESAPP task order -- `AMGT-ar-6` -- THE AI-FILL PAGE FEATURE IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-6</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ar-6.the-ai-fill-page-feature-is-promoted-to-prod-from-the-approved-list</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- at the cut: this order is a STAGED shell, and its subject (the re-cut branch `cand/dell1/aifill-blocks-prod`, its approval row, its merge-forward) does not exist until `AMGT-ar-5` and the steps after it. At the GO the issuer prints `python .tools/open-calls.py approval-status --branch cand/dell1/aifill-blocks-prod` and the surface check's line, in the GO. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-ar-6` (round 104, workstream AIFILLLAND, decomposition s.11)

The feature is the AI-fill page: eleven files under `src/pages/SecurityAnalysis/`, the CTO-approved candidate (call cf85, class Opal-internal: no word from Andrew), re-cut from PROD `7d5cb34d` as `cand/dell1/aifill-blocks-prod` by `AMGT-ar-5`. Its server side is DEPLOYED (95 names serve `ai_fill`). Do, in order:
1. In the portal repository (`C:/dev/ajb_workspace/portal`), the branch `cand/dell1/aifill-blocks-prod` is registered and approved (the GO prints its row and `approval-status`). Run `bash .tools/portal-release-build.sh --features cand/dell1/aifill-blocks-prod` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
2. Promote the release with `/prod-deploy`. The release carries ONE feature, eleven files under `src/pages/SecurityAnalysis/`. Your receipt names `/security-analysis` as Opal-internal.
3. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT_AIFILL.md` with the sections `## Release` (the release branch, the PROD head before `7d5cb34d` and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

BAR: use no other face and no other branch for this order. Do not execute any older pending face you hold.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. One feature only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase.
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
  <criterion id="AC1" cell_refs="AMGT-ar-6"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in src/pages/SecurityAnalysis/SecurityAnalysis.tsx src/pages/SecurityAnalysis/types.ts src/pages/SecurityAnalysis/components/AiFillBlock.tsx src/pages/SecurityAnalysis/components/SecurityOverlay.tsx src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx src/pages/SecurityAnalysis/tabs/ThesisTab.tsx src/pages/SecurityAnalysis/__harness__/aiFill.harness.cjs src/pages/SecurityAnalysis/__harness__/aiFill.fixture.json src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs src/pages/SecurityAnalysis/__harness__/execText.harness.cjs; do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 85d5749f:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>eleven lines `EQUAL <path>` (one per path, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-6"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `7d5cb34d` (the pre-promote head: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-6"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT_AIFILL.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED SHELL: the GO is written when ALL of: `AMGT-ar-5` complete and its branch carrying the eleven files blob-equal; the issuer has PUSHED `cand/dell1/aifill-blocks-prod` and the CTO has closed its approval row `approved`; the box manager has merged the same commits forward onto DEV (`.tools/portal-merge-forward.sh`), so the trunks do not diverge. The GO prints the row, `approval-status` and the surface check's line. THE FLOW is `portal/CONTRIBUTING-BOXES.md` step 7 (the promote takes a list, never live DEV whole), exactly as `AMGT-bk-7` ran it for `2.0.0_SA_COO~R1`. The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home. AC1's comparison object is the original approved candidate `85d5749f`: the re-cut branch is blob-equal to it by `AMGT-ar-5`'s AC1. AFTER the promote: the issuer asks the CVO for the five-name read on the live page.

<status>staged</status>
<round>104</round>
<workstream>AIFILLLAND</workstream>
<slot>0.4.0_DT_ClientPlatform</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
