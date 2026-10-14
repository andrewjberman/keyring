# AMGT_RESAPP task order -- `AMGT-bk-7` -- THE HEADER MONEY-AND-DASH-REASONS FEATURE IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-7</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-7.the-header-money-and-dash-reasons-feature-is-promoted-to-prod-from-the-approved-list</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-header-money-and-dash-reasons` reads `state=APPROVED valid=yes ... head_sha=624e2533f665bf786e41594adba17b82c447aa7d commits=1 class=opal-internal`; `r103_feature_surface_check.py --portal portal --base 10e7664d --head 624e2533f6` read YES (4 files: 4 page) on the branch; the candidate tip is an ancestor of DEV 5e40e54119. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bk-7` (round 104, decomposition s.113)

CTO msg 5289 closed the approval row `dell1-20261014T001511Z-633a` APPROVED (class Opal-internal: no word from Andrew), and the CTO named this seat for the promote (msg 5297). Do, in order:
1. In the portal repository (`C:/dev/ajb_workspace/portal`), the branch `cand/dell1/amgt-sa-header-money-and-dash-reasons` is LOCAL at tip `624e2533f6` (already in DEV `5e40e54119`; its remote copy was deleted after the merge-forward). Run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-header-money-and-dash-reasons` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
2. Promote the release with `/prod-deploy`. The release carries ONE feature, four files under `src/pages/SecurityAnalysis/`; the AI-fill candidate (row cf85) is NOT in it. Your receipt names `/security-analysis` as Opal-internal.
3. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT.md` with the sections `## Release` (the release branch, the PROD head before `10e7664d` and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

BAR: do NOT execute your older pending face `OPAL_ADVIPOINTERS.P4-PROMOTE-49F`; it reads pending but looks shipped (tag `portal-v2.1.165`, `d9a98bcc` in origin/PROD) and its issuer closes it. Use no other face and no other branch for this order.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

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
  <criterion id="AC1" cell_refs="AMGT-bk-7"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in src/pages/SecurityAnalysis/components/HeaderCards.tsx src/pages/SecurityAnalysis/components/StatTile.tsx src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx src/pages/SecurityAnalysis/__harness__/tileMoneyAndReasons.harness.cjs; do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 624e2533f6:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>four lines `EQUAL <path>` (one per path, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-7"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `10e7664d` (the pre-promote head: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-7"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform/PROMOTE_RECEIPT.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
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

**ISSUER NOTES:** THE FLOW is `portal/CONTRIBUTING-BOXES.md` step 7 (the promote takes a list, never live DEV whole). The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home, commits under its own lane, and reports to `2.0.0_SA_COO~R1` and `1.0.0_SA_CTO~DELL1`. The older pending face it holds belongs to another project (ADVIPOINTERS) and is closed by that issuer; the order bars it. The class is Opal-internal (route `requireInternal`): no word from Andrew. bk-5 (census re-run and the ten-name walk) reads the page after this promote.

<status>complete</status>
<round>104</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
