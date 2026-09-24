# AMGT_RESAPP task order -- `AMGT-rm-7` -- THE DEPLOY LEG: `opal-amgt-scoped-api` carries `?format=rich`, under NEVER-2, by the AE lane

<!-- ===================== WORKER FACE -- the whole of the assignee's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through Terraform (its existing resource), nothing else.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared (AMENDMENT 2): the Terraform apply for ONE Lambda function (`opal-amgt-scoped-api`, `infra/aws/terraform/harvest/scoped-amgt-api.tf`) through `safe-apply`; EXACTLY ONE S3 ARTIFACT WRITE -- the function's code package `research/opal-amgt-scoped-api.zip` built and uploaded by the estate's own `build-and-upload-scoped-amgt.sh` (the apply's stated precondition), with the PRIOR artifact preserved first (its VersionId recorded if the artifact bucket is versioned, else a copy to a sha-named backup key beside it) so the rollback is a re-point, never a rebuild; direct invokes of that function for the verify-after; no vendor call, no other S3 write, no S3 delete.
</preflight>

**Assignee `0.7.0_AE_CloudOps~A`** (R-58 @`6b3cda855b`: *"the deploy leg belongs to the AE CloudOps lane"* -- Rule 13's
split, the Terraform-only NEVER line, and this lane's precedent on this exact function). **This order is PENDING until
`AMGT-rm-4` has merged into CLOUD** -- the issuer sends the binding commit hash the moment it lands; act on nothing before
that message. It is cut now because L6 is ONE issuance covering every cell.

## 1. THE ORDER

Deploy `opal-amgt-scoped-api` so that `GET {ROUTE_PREFIX}/security/{security_key}/print?format=rich` returns
`text/markdown` (rl-10's `build_rich_text` through rm-4's `_print_pack` branch) while `GET .../print` with no `format`
returns the SAME PDF bytes as before the deploy. R-57 ruled NO never-widen pair is needed (the default path is a verified
DELTA=0 on every existing response); NEVER-2 still binds: **the change-management ledger entry is opened BEFORE the apply
and closed on the verify-after, in the same session, or the deploy is rolled back and escalated loud.**

## 2. THE ACT, in order

1. **Pre-flight, read from the store not the report:** `git log -1 --format=%h -- lib/research/api/scoped_amgt.py` on CLOUD
   equals the commit the issuer's message names (the binding); `aws lambda get-function-configuration --function-name
   opal-amgt-scoped-api --query CodeSha256` recorded as the BEFORE sha; ONE direct invoke of `.../security/BA_US_Equity/print`
   (no format) with the response body's sha256 recorded as the BEFORE pdf sha; ONE direct invoke with `format=rich` recorded
   as the BEFORE behaviour (expected: today's pdf, since the running bytes ignore the parameter).
2. **Open the NEVER-2 ledger entry** (`org/critical_paths/change_management/`, slug `amgt-rm-7-print-format-rich`, legs
   L1 code sha moved / L2 pdf default byte-identical / L3 rich served), naming the ONE function, the binding commit, the
   BEFORE shas, and the rollback (re-apply the previous package -- name it by its CodeSha256).
3. **Build and upload the artifact, then apply.** First `build-and-upload-scoped-amgt.sh` (the repo at the binding commit; it writes the ONE artifact object named in the egress class -- record the object's bucket, key, size and content sha256 BEFORE and AFTER, and the prior artifact's VersionId or backup key, in the ledger entry as the rollback); then **apply through `safe-apply`** on `infra/aws/terraform/harvest/scoped-amgt-api.tf` (the print-deps layer
   `print-deps-layer.tf` only if rm-4's report says a dependency moved; expected: none). Never `aws lambda
   update-function-code`; never a bare `terraform apply`.
4. **Verify-after on the deployed function:** CodeSha256 moved (AFTER != BEFORE); direct invoke with no format returns
   200 `application/pdf` whose CONTENT-STREAM DIGEST -- the page count plus each page's DECODED content stream, sha256 over that
   sequence, no file-level metadata and no xref offsets -- is EQUAL to the BEFORE read's (L2, the DELTA=0 that R-57's no-pair
   rests on, stated on the CONTENT-STREAM plane -- AMENDMENT 3, on the lane's measurement: the raw pdf carries a render-time
   /CreationDate; rl-10's pin REMOVES that entry and shifts every xref offset after it, so a metadata-stripping normaliser
   also reads FAIL on a correct deploy; the content-stream digest survives the stamp, the pin, and stays sensitive -- CAT differs;
   a different content-stream digest is the ROLLBACK trigger; raw and metadata-normalised shas printed beside it for the record); direct invoke with `format=rich` returns 200 `text/markdown` with a body larger
   than 20 KB whose first line is a Markdown heading naming the security (L3); direct invoke with `format=xml` returns 400.
   **The negative control on the pdf leg:** the same invoke on a second key (`CAT_US_Equity`) reads a DIFFERENT sha from
   BA's (so "equal" is a comparison that can fail).
5. **Close the ledger entry** with the three legs proven and the four invoke reads pasted; commit the entry and your
   deliverables under your own lane.

## 3. BOUNDS

1. ONE function, ONE apply, in one session; the entry opened before and closed after. No other resource in the plan may
   change -- a plan that shows a second resource moving is a REFUSAL (print it, stop, report).
2. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches (you commit LOCAL; `0.0.0_AB_MSTR~Z`
   pushes), no promote of the portal (the client action ships with the portal's own deploy, not yours).

## 4. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
infra/aws/terraform/harvest/print-deps-layer.tf
infra/aws/lambda/research/scoped_amgt_api/**
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/AMGT_RESAPP_RM4B_20260924/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 5. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls org/critical_paths/change_management/ | grep amgt-rm-7-print-format-rich &amp;&amp; .tools/aws lambda get-function-configuration --function-name opal-amgt-scoped-api --query CodeSha256 --output text</invocation><expect>THE LEDGER ENTRY EXISTS (opened before the apply, its BEFORE shas inside) AND THE CODE MOVED: the entry file listed; the deployed CodeSha256 printed and DIFFERENT from the BEFORE value the entry records (print both)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/AMGT_RESAPP_RM4B_20260924/verify_after.py</invocation><expect>THE DEFAULT IS BYTE-IDENTICAL AND RICH IS SERVED, on the DEPLOYED function by direct invoke: BA_US_Equity no-format -> 200 application/pdf, CONTENT-STREAM DIGEST (page count + each page's decoded content stream) EQUAL to the BEFORE read's recorded in the ledger (both printed side by side; the raw and the metadata-normalised shas printed beside them for the record); BA_US_Equity format=rich -> 200 text/markdown, body larger than 20 KB, first line a Markdown heading naming the security; format=xml -> 400; the negative control CAT_US_Equity no-format -> a pdf sha DIFFERENT from BA's (printed)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c "CLOSED" org/critical_paths/change_management/$(ls org/critical_paths/change_management/ | grep amgt-rm-7-print-format-rich | head -1) &amp;&amp; git log -1 --format=%h -- org/critical_paths/change_management/</invocation><expect>THE ENTRY CLOSED IN THE SAME SESSION with all three legs proven and the invoke reads pasted, and the closing commit landed (its hash printed) -- a RED or OPEN entry at the end of the session is a rollback-and-escalate, never a hand-off</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/AMGT_RESAPP_RM4B_20260924/AMGT_RESAPP.TO-AMGT-rm-7.the-deploy-leg.proof_of_spec.json`,
graded by `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3`. Report to `2.0.0_SA_COO~Z`
by broker (this is a seat order, not a worker subagent): the BEFORE/AFTER CodeSha256, the pdf sha pair, the rich body size,
the ledger entry path and its closing commit, and any row. **The status flip is the ISSUER'S.**

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

**ISSUER AMENDMENT 3 (15:2xZ, on `0.7.0_AE_CloudOps~A` msg 25587):** amendment 2(b)'s metadata-normalised comparand ALSO fails
under rl-10's pin (measured by the lane: the pin removes the /CreationDate entry and shifts the xref, 77,862 -> 77,388 bytes,
normalised digest moves); L2's comparand is now the CONTENT-STREAM DIGEST (page count + decoded content streams), which reads
equal across the stamp and the pin and differs on CAT. Nothing else moves.

**ISSUER AMENDMENT 2 (15:1xZ, on `0.7.0_AE_CloudOps~A` msg 25584, rows Z-S253 / Z-S254):** (a) the egress class gains EXACTLY
ONE S3 artifact write -- the function's code package via the estate's own build-and-upload script, the apply's stated
precondition that no cell owned (the decomposition's s.46d(iv) had rm-4 "does not deploy" and rm-7 "changes no code";
the union was short one member, the issuer's gap); the prior artifact is preserved first and named as the rollback in the
NEVER-2 entry; (b) AC2/L2's comparand is the /CreationDate-normalised sha256 (the raw pdf is never byte-equal across two
requests; rl-10 pinned CreationDate=None so the raw sha moves by that pin alone after the deploy) with the CAT control
unchanged. The order is otherwise as amended at 1; it stays GO on the binding 3350abb022.

**ISSUER AMENDMENT 1 (12:5xZ, on `0.7.0_AE_CloudOps~A` msg 25524):** the two `lib/research/**` entries are REMOVED from
`<paths>` -- the resolver refuses them to the AE lane (BASE_EXEC) and the order asks only a READ of one of them (step 1's
`git log -1`), which no grant governs; a write surface is what `<paths>` names, so an entry the assignee cannot write is a
defect in the face, not a permission the assignee should route around. Nothing else on the face moves; the order stays
PENDING rm-4's merge.

**ISSUER NOTES:** a SEAT order (v2 shape: broker-delivered, the assignee a Tier-2 lane), cut in the round's ONE issuance
with the edge rm-4 -> rm-7; the assignee is told to act only on the binding message that follows rm-4's drain. R-58 named
the lane; R-57 ruled no pair; NEVER-2 binds the entry. Seating: `0.7.0_AE_CloudOps~A` holds AMGT_RESAPP work (the H03 leg)
and no open order on another pipeline project at the cut (to-check read).

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~16:2xZ.** Flipped by the ISSUER; the lane left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat at HEAD on the lane's instance @f9d68312f2 under
org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/AMGT_RESAPP_RM4B_20260924/). THE DEPLOY: artifact research/opal-amgt-scoped-api.zip
VersionId ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe -> 9z.fsHGW7ZN2Qf2yU_rsnv0wiL7uKqRS (807,904 -> 844,437 bytes), built at 19a22f2f51 which
contains rm-4's 791806b1c9, the prior version preserved by bucket versioning and named as the rollback; plan 0/1/0 in place touching
only s3_object_version, source_code_hash, last_modified (28 attributes and 4 blocks unchanged); apply 1 changed; replan No changes.
L1: CodeSha256 -> y5bJBQsP8Q7Lfudb5nwc5wEr72IcH53uS5cz2T8bn/w=, equal to the artifact's metadata and the local sha. L2: content-stream
digest 5f150ad66d00e76f5364058eda899723f0b1a9623af058ce558f974ac6c5d602 EQUAL before and after; CAT 7c017870... DIFFERENT, so equal was
free to fail. On the same real bytes the raw sha and the /CreationDate-normalised sha both read NOT EQUAL (77,862 -> 77,828 bytes, the
entry present -> absent): amendments 1 and 2's comparands would each have graded this correct deploy FAIL and fired the rollback
branch; amendment 3 stands vindicated on the deploy, not on the lane's simulation. L3: format=rich -> 200 text/markdown 58,549 bytes,
first line "# BOEING CO/THE [BA US Equity] Research Note"; format=xml -> 400 naming pdf and rich. NEVER-2 entry
20260924T1523Z_amgt-rm-7-print-format-rich opened @192d45272d BEFORE the build (the artifact write being the irreversible act), closed
@35038a7459 at 15:58:26Z with all three legs proven; deploy_ledger lists nothing open. Rows: Z-S253 (INERT), Z-S254 (ARMED), Z-S256
(the build's lib/ precondition, INERT) -- DISARMED on the issuer's word, Z-S258 the carrier (filed by the lane, each remedy on its own
evidence line; ARMED rows stay in place). Three blockers on one order, each one layer deeper than the last (the artifact write no cell
owned; the pin's effect on the comparand; the generated-module stamp no AMGT cell moved): the lane's --build-only-at-cut remedy is
adopted for this issuer's next deploy cut. NOT CLAIMED, carried to the analysis: rm-4's rich CONTENT is graded on the worker's fixture
(162/162 figures, 43/43 cites), never on the live body; the build pip-downloads pinned wheels from PyPI inside the named script -- an
egress the face inherited by naming the script rather than declaring; AC3's raw grep needed a rail marker; a recorded invocation typed
as a shell command fails invocation-alignment against the file's XML-escaped `&&`.

<status>complete</status>
<round>38</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
