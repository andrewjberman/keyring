# AMGT_RESAPP task order -- `AMGT-bv-5` -- THE SCOPED API PRINTS THE RICH EXPORT'S DATES IN THE HOUSE LONG FORM AND KEEPS EVERY SOURCE QUOTATION BYTE-FAITHFUL, FROM THE RELEASE PIN `d4bba34eb8` (ONE CODE LEG, ONE MEMBER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bv-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bv-5.the-scoped-api-prints-rich-export-dates-and-keeps-quotes-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18 ~02:4xZ) -- AC1 (the pack text) run against the LIVE function (still the `bu-7` code) at the base reads `PACK SAME: YES` (the pack text is expected UNCHANGED by this act, so AC1 is a REGRESSION guard that PASSES at the base as expected; its control, the same compare of the candidate against the pre-`bu-7` ISO-era set, reads NO); AC2 (the rich export) at the base reads `RICH COMPARE: NO (0 of 8 names ...)` (the live export still prints ISO days, so no name shows fewer after: unmet as expected); AC3 reads `CONFIG sha=RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=` at the base, so its expectation of a CodeSha256 other than that one is unmet there as expected; AC4 (the pin's content diff) reads `members whose bytes differ: 1` at the base and is true before the act (it grades the PIN, not the function). The act's expected outcome was measured BEFORE the cut: this checkout's own handler over the live pool for the eight names reads `RICH COMPARE: YES (8 of 8)` and `PACK SAME: YES (8 of 8)`.
EGRESS CLASS, declared: the Lambda invoke of the print route and the config read by the read-only instrument, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bv-5` (round 115, decomposition s.124)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`d4bba34eb8`** (branch `rel-amgt-bv5`, LOCAL on dell1; parent = the live pin `6bb7b23ee5`, the `bu-7` build input; its only change is `lib/research/print/render_pack.py`, blob `fa514afbb2f6` to `89d4c2a34b89`, file sha256 `60a9f2ddb4f4` to `8a1f47d8c6cd`, taken from the `bv-2` merge `6d4b263da2`). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND115_RICH_EXPORT_AND_QUOTES_REDEPLOY_COO_HALF.md` @5ceeba9ba5 (sha256 `bf0155b742577bb6dc17046d7f66d170d653e194eb39dd0a3503db6ba9516ca4`), CTO half `..._CTO_HALF.md` @858057f985 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `8a1f47d8c6cd`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD.

**THE CTO HALF'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=` at the cut), `LastModified` (`2026-10-18T01:16:17.000+0000`), the `RevisionId` (`3c6a52dc-425f-457c-b2a7-74342fa318f3`) and the `bu-7` artifact's S3 key and VersionId (`pXDgyepp27ULWCB5z9kMRHNjyk.8qIgh`; the `L6` row of the ledger entry `amgt-resapp-r114-bu7-pack-dates-redeploy-dell1`, file under `org/critical_paths/change_management/`, names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs AND the eight rich exports: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r115-packs-before2` and `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture-rich C:/dev/ui-walk-evidence/r115-rich-before2`** (the live data moves between days, so the criteria compare the after-act captures with these, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bu-7` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack text changes (AC1 reads NO), the rich export does not show fewer ISO days with its text otherwise equal (AC2 reads NO), or the function does not answer.

The effect is: the `format=rich` markdown export prints every date in a non-quote line in the house long form (`October 17th, 2026`) instead of the served ISO day or timestamp; a source's own words (filing-sentence blocks and the export's block-quoted evidence passages) print exactly as served; **nothing else moves**, and the printed PDF/txt pack of these names is expected UNCHANGED. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own earlier captures are `C:/dev/ui-walk-evidence/r114-packs-issuer-after/` and `C:/dev/ui-walk-evidence/r115-rich-before/` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bu-7` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `bu-7`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bv-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r115-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" same C:/dev/ui-walk-evidence/r115-packs-before2 C:/dev/ui-walk-evidence/r115-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK SAME: YES (8 of 8 names: the pack text equals the before set)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bv-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture-rich C:/dev/ui-walk-evidence/r115-rich-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" compare-rich C:/dev/ui-walk-evidence/r115-rich-before2 C:/dev/ui-walk-evidence/r115-rich-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `RICH CAPTURE: 8 of 8 names captured (0 not 200)` then the line `RICH COMPARE: YES (8 of 8 names: equal to before once the long forms map back, and fewer ISO days after)`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bv-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=> modified=<a time after the apply began> rev=<a RevisionId other than 3c6a52dc-425f-457c-b2a7-74342fa318f3> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bv-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" d4bba34eb8 --pin 6bb7b23ee5 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin 6bb7b23ee5 ref d4bba34eb8 (d4bba34eb8) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `fa514afbb2f6` and `89d4c2a34b89`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bu-7` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bv-5.the-scoped-api-prints-rich-export-dates-and-keeps-quotes-from-the-release-pin.proof_of_spec.json` (if the path is past MAX_PATH on this box, say so in a row and use a short sibling name the checker accepts). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-bv-5` (decomposition s.124), the served half of the CTO's round-114 items 2 and 3. Pair signed on both halves (CTO half @858057f985, msg 7842); the CTO's three conditions are inlined (the re-read of CodeSha256, RevisionId and LastModified immediately before the upload is the one-writer condition; no cross-adjudication hold). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34; `bu-7` used `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. SC1 may need a screen nudge to read it (the round-114 `bu-7` order sat unread for an hour in its inbox; `/unstick` peek, then a typed prompt, took). The issuer reads the result only after the applier's report, never during. Risk class WORLD. `W506-S5` is closed on the quote census (CTO msg 7842).

<status>complete -- 2026-10-18 by the issuer (2.0.0_SA_COO~R1): 0.7.0_AE_CloudOps~SC1 applied from release pin d4bba34eb8 at 03:06:09Z to 03:07:48Z (CodeSha256 RY998VO4.. to lp+7X1VkDi7sFz3v5W3yZSlWFZaMQSKo7knlvp1GxBQ=, rev 3c6a52dc.. to e4e64b80.., LastModified 2026-10-18T03:07:37Z, memory 1769, timeout 29, env keys unchanged, AMGT_AIFILL_ROOT absent); content diff 408 members, 407 identical, 1 changed (render_pack.py 60a9f2ddb4f4 to 8a1f47d8c6cd); plan after: no changes; rollback target (the bu-7 artifact) VersionId pXDgyepp27ULWCB5z9kMRHNjyk.8qIgh, not needed; ledger closed. THE ISSUER'S OWN SECOND READ (fresh captures of the same eight live packs and rich exports, compared with the issuer's own earlier BEFORE sets of ~02:20Z, not SC1's): PACK SAME YES (8 of 8: the pack text unchanged); RICH COMPARE YES (8 of 8): ISO days before 619, 599, 592, 250, 388, 523, 604, 270, after 0 on every name, the same numbers of long-form days, and the export otherwise equal once the long forms map back; config read equal. Expected outcome as measured before the cut (the checkout's handler over the live pool): the same. W506-S5 closed on the quote census (CTO msg 7842).</status>
<round>115</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
