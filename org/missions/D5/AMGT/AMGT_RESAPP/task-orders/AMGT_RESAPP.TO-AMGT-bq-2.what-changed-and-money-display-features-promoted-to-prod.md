# AMGT_RESAPP task order -- `AMGT-bq-2` -- THE WHAT CHANGED CRASH FIX AND THE MONEY-DISPLAY FEATURES ARE PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE, WITH THE RECEIPT AND THE CI CONCLUSION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bq-2</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bq-2.what-changed-and-money-display-features-promoted-to-prod</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-17 ~14:3xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-changed-list-value` reads `state=APPROVED valid=yes row=dell1-20261017T133543Z-fa30 by=1.0.0_SA_CTO~DELL1 head_sha=bc0a5cd911f1d50b59b22a13af0c90239c3fd165 commits=5 class=opal-internal`, and `--branch cand/dell1/amgt-sa-money-display` reads `state=APPROVED valid=yes row=dell1-20261017T123830Z-d775 by=1.0.0_SA_CTO~DELL1 head_sha=aba098daee5c42c9f0fdb65bfaf4366ce8ca39d7 commits=2 class=opal-internal`; both are merged forward onto DEV (`a55f6a77ff`, `cab233bfdf`, `ls-remote` read DEV `cab233bfdf`); the release builder run at the cut (`bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-changed-list-value,cand/dell1/amgt-sa-money-display`) printed `RELEASE-CHECK features=2 first_parent_commits=2 unapproved=0`, `PROMOTE-CLIENT-FACING count=0` and `RELEASE result=READY branch=release/20261017T142907Z base=15bc21b3 head=89fe4e0f7b35` (that branch was built to measure and is NOT pushed; build your own on the PROD head you read). AC1 at the base reads `DIFFERS` on all sixteen paths (origin/PROD `15bc21b3`), AC2 reads the PROD head `15bc21b3` (success, completed), which the criterion refuses, and AC3 reads a missing receipt: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bq-2` (round 110, decomposition s.119)

The box CTO closed the approval rows APPROVED (class Opal-internal: `/security-analysis` is staff-only; the approval record `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_DEV_BP1_BP4_SECURITY_ANALYSIS_20261017.md` addendum 1 @6b11981e03 covers the DEV merge-forward AND this PROD promote; the CTO's messages of 2026-10-17 ~14:27Z and ~14:38Z name the DT promoter of "a55f6a77ff (bq-1) and cab233bfdf (bp-4), and nothing else"; `~H1` holds another project's orders, so the order is re-addressed to `~H2`). The two features, each a candidate cut from PROD `15bc21b3`: (1) `cand/dell1/amgt-sa-changed-list-value` (head `bc0a5cd9`): a changed figure whose value is a list no longer crashes the Security Analysis Model tab (RIO LN), the What Changed detail renders a list as text, a money row in a foreign currency prints its code; (2) `cand/dell1/amgt-sa-money-display` (head `aba098da`): a money figure beside a non-USD price currency prints `USD `, and a negative one prints its sign first. Sixteen paths in all, every one under `src/pages/SecurityAnalysis/`. Do, in order:
1. **Confirm both features are in DEV.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV -q && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor bc0a5cd911f1d50b59b22a13af0c90239c3fd165 origin/DEV && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor aba098daee5c42c9f0fdb65bfaf4366ce8ca39d7 origin/DEV && echo IN-DEV`. If it does not print `IN-DEV`, STOP and report: do not build, do not promote. You never write DEV.
2. In the portal repository (`C:/dev/ajb_workspace/portal`), run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-changed-list-value,cand/dell1/amgt-sa-money-display` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
3. Promote the release with `/prod-deploy`. The release carries exactly these TWO features and no other candidate; your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BQ2.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Two features only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section): the merge-forward is already done (step 1 only reads it).
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bq-2"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for h in bc0a5cd911f1d50b59b22a13af0c90239c3fd165 aba098daee5c42c9f0fdb65bfaf4366ce8ca39d7; do for f in $(git diff --name-only 15bc21b3 $h); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse $h:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; done</invocation><expect>sixteen lines `EQUAL <path>` (nine for the first head, seven for the second, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bq-2"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `15bc21b3` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bq-2"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BQ2.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-bq-2.what-changed-and-money-display-features-promoted-to-prod.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** RE-ADDRESSED 2026-10-17 ~14:4xZ from `0.4.0_DT_ClientPlatform~H1` to `0.4.0_DT_ClientPlatform~H2` on the CTO's instruction (msg 7608, on the manager's msg 7605: `~H1` holds two pending ADHOC orders of `2.0.0_SA_COO~J1`, and one project per Tier-2 seat instance); the amendment changes the addressee, the slot and the deliverables folder only. The `bo-2` pattern (round 108): a Tier-2 SEAT order, not a worker order; the DT holds it in its own home and reports to `2.0.0_SA_COO~R1`; the spawn of the DT, if it is not live, is `0.0.0_AB_MSTR~DELL1`'s (the CTO's message says so). The order is cut at its GO state (`pending`) because every precondition already holds: both approval rows APPROVED valid, both features merged forward onto DEV, the release build READY with `PROMOTE-CLIENT-FACING count=0`. After the promote the issuer reads RIO LN's Model tab on PROD with the walker; that read grades FWD-40 (d) (CTO msg 7592). Risk class SERVED: a PROD promotion; the CVO grades judgment criteria on the PROD read, not here.

<status>complete -- 2026-10-17 by the issuer (2.0.0_SA_COO~R1): 0.4.0_DT_ClientPlatform~H2 promoted ONE chosen-set release (release/20261017T144424Z, 2 features, unapproved=0, client-facing 0): PROD 15bc21b3 to 99d2b2a70c on origin, CI run 39042189942 completed/success, tag portal-v2.1.235; proof VALID rc=0; issuer re-run of AC1 (16 of 16 paths EQUAL) and AC2 (success on 99d2b2a7); receipt 509558f20c, instance 1cf6092d0d; the issuer's PROD-head read in deliverables/2.0.0_SA_COO~R1/round110/PROD_READ_FWD40D.md</status>
<round>110</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
