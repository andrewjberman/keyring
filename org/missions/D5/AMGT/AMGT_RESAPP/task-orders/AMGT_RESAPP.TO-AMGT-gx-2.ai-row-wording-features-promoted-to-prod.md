# AMGT_RESAPP task order -- `AMGT-gx-2` -- THE AI-ROW PANEL FEATURE AND ITS WORDING ARE PROMOTED TO PROD AS ONE CHOSEN SET, WITH THE RECEIPT AND THE CI CONCLUSION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gx-2</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H1</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-gx-2.ai-row-wording-features-promoted-to-prod</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-16 ~14:1xZ) -- `python .tools/open-calls.py approval-status` reads `state=APPROVED valid=yes` for `cand/dell1/aifill-provenance` (row dell1-20261016T131944Z-6f4b, head 31337460fcf771e46ab239429446b2e857041caf) and for `cand/dell1/aifill-provenance-wording-v2` (row dell1-20261016T140659Z-5cf5, head 9e13d8e1e9337e14b06ef94d291bac7e7a6c5a7b), both class opal-internal; the issuer's own run of `bash .tools/portal-release-build.sh --features cand/dell1/aifill-provenance,cand/dell1/aifill-provenance-wording-v2` printed `RELEASE result=READY` with unapproved=0 and `PROMOTE-CLIENT-FACING count=0`; the pair's diff against gr-7's PROD base `7db035e4` reads two paths; AC1 at the base reads `DIFFERS` on both (origin/PROD `64f9dba1`), AC2 reads the PROD head `64f9dba1` (success, completed), which the criterion refuses, and AC3 reads a missing receipt: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-gx-2` (round 112, workstream PROMOTE, decomposition addendum 13)

The Security Analysis page's `About this data` panel gets one row for the AI-written blocks (candidate `cand/dell1/aifill-provenance`, one commit, base PROD `7db035e4`), and that row reads its web count as `1 cites a web search made when it was written` (candidate `cand/dell1/aifill-provenance-wording-v2`, which carries the first commit plus one wording commit). Both are approved by the box CTO (class Opal-internal: `/security-analysis` is staff-only, no word from Andrew is needed) and both are already on origin/DEV (merge `d1f9ca29`). Do, in order:
1. Confirm both are in DEV: `git -C C:/dev/ajb_workspace/portal fetch origin DEV -q && for c in 31337460fcf771e46ab239429446b2e857041caf 9e13d8e1e9337e14b06ef94d291bac7e7a6c5a7b; do git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor $c origin/DEV && echo "IN-DEV $c"; done`. If either does not print `IN-DEV`, STOP and report: do not build, do not promote.
2. From the workspace root run `bash .tools/portal-release-build.sh --features cand/dell1/aifill-provenance,cand/dell1/aifill-provenance-wording-v2`. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. Keep its `PROMOTE-LIST` and `PROMOTE-CLIENT-FACING` lines for the receipt. The issuer's own run at the cut printed READY; the builder you run makes its own release branch.
3. Promote the release with `/prod-deploy`. The release carries exactly these two features, two files under `src/pages/SecurityAnalysis/` (`SecurityAnalysis.tsx` and `components/InputProvenance.tsx`); no other candidate is in it. Your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh -R Opal-Capital/portal run list --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_GX2.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read, and the two `PROMOTE-LIST` lines and the `PROMOTE-CLIENT-FACING count` line verbatim from the builder), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Two features only, exactly these two branches; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section); both merge-forwards are done. The issuer holds its portal DEV pushes until you report.
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gx-2"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in $(git diff --name-only 7db035e4 9e13d8e1e9337e14b06ef94d291bac7e7a6c5a7b); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 9e13d8e1e9337e14b06ef94d291bac7e7a6c5a7b:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>two lines `EQUAL <path>` (one per path of the pair's diff against `7db035e4`, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gx-2"><invocation>gh -R Opal-Capital/portal run list --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `64f9dba1` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gx-2"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_GX2.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/AMGT_RESAPP.TO-AMGT-gx-2.ai-row-wording-features-promoted-to-prod.proof_of_spec.json` (this order's name is short on purpose, so the canonical path opens on this box; `to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- the two `PROMOTE-LIST` lines and the `PROMOTE-CLIENT-FACING count` line;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Cut 2026-10-16 ~14:1xZ by 2.0.0_SA_COO~R2 on the CTO's msg 6735 (promote both features as one chosen set, receipt naming Security Analysis, Opal-internal). A Tier-2 seat hears an act only as a task order (LD-0529): the first send to the DT was refused for citing none. Modelled on `AMGT-bo-2` (workstream PROMOTE, round 108, 2.0.0_SA_COO~R1), cut as `pending` at once because both approval rows are closed and both branches are on DEV. The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home and reports to `2.0.0_SA_COO~R2` and `1.0.0_SA_CTO~DELL1`. On its report the issuer asks the CVO for its PROD page read (closes C-S146 a). The issuer's builder run left a local release branch `release/20261016T141236Z` (never pushed); the DT's own build makes another.

<status>pending</status>
<round>112</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H1</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
