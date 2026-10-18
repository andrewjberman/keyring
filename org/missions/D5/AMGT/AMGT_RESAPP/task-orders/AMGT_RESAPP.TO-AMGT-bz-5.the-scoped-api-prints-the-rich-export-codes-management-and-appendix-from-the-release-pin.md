# AMGT_RESAPP task order -- `AMGT-bz-5` -- THE SCOPED API PRINTS THE RICH EXPORT'S CURRENCY CODES AND THE PDF'S MANAGEMENT LINES, AND A PLAIN APPENDIX, FROM THE RELEASE PIN `2771164d0d` (ONE CODE LEG, ONE MEMBER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bz-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bz-5.the-scoped-api-prints-the-rich-export-codes-management-and-appendix-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18): at the base (the LIVE function still the `by-5` code, CodeSha256 `H3dCSGL..`): AC1 `PACK FORM` reads `YES (8 of 8 names)` (the pack's section form does not move in this act: AC1 is a REGRESSION control that PASSES at the base as expected), AC2 `MONEY VS PAGE` reads `YES (16 of 16 money lines)` (a regression control too), AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet there as expected, AC4 reads `members whose bytes differ: 1` and is true before the act (it grades the PIN). The act's OWN expected outcome is read by the issuer after the apply and was measured at the base: the cross-surface read (`r119_cross_surface.py`: the PDF's Management section against the export's) reads `NO (0 of 8)` on the LIVE captures, the three live exports carry no currency code on any money row and each says `could not be read` once; the candidate (this checkout's handler over the live pool) reads `YES (8 of 8)`, the money rows carry GBp, PHP and USD, and the candidate PDF text is identical on 8 of 8.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bz-5` (round 119, decomposition s.128)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`2771164d0d`** (branch `rel-amgt-bz5`, LOCAL on dell1; parent = the live pin `d4c6f1c533`, the `by-5` build input; its only change is ONE member taken from the round-119 merge `b6f5989705`: `lib/research/print/render_pack.py` blob `3ddc696def09` to `a281246c18c0`, file sha256 `5f4cffc172ba` to `ce54affc8f87`; `scoped_amgt.py` does not change). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND119_RICH_EXPORT_CODES_MANAGEMENT_AND_APPENDIX_REDEPLOY_COO_HALF.md` @2f657c667b (sha256 `2ff43a0a2cd975228c45e46bb3677b1563819a3fdf9b021b596d00a501fb4dba`), CTO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND119_RICH_EXPORT_CODES_MANAGEMENT_AND_APPENDIX_REDEPLOY_CTO_HALF.md` @318bedccc3 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `ce54affc8f87`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD.

**THE PAIR'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`H3dCSGLEs4abPk0alOWclPZX1U6lYrxEXkhGZOAJ434=` at the cut), `LastModified` (`2026-10-18T11:14:20.000+0000`), the `RevisionId` (`caab3655-4909-4c3d-ba32-76446effe97d`) and the `by-5` artifact's S3 key and VersionId (`xr.zAPt5G9_Tjw8D60wN54ZgecD0x9P4` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`; the `L6` row of the ledger entry `amgt-resapp-r118-by5-plain-reasons-rich-export-redeploy-dell1`, file under `org/critical_paths/change_management/`, names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r119-packs-before2`** (the live data moves between days, so the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `by-5` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names on either format, or if the function does not answer.
5. **Latency and the cross-surface read (the CTO half's conditions):** after the apply and your own reads, the ISSUER reads the print route on BOTH formats for KMB US, RIO LN and GOOGL US, the all-names leak scan, the eight live rich exports and `r119_cross_surface.py` (the PDF's Management section against the export's, per name). Any route over 20 s (70% of the 29 s timeout), or a leak line, or a cross-surface NO, or a rich export still carrying `could not be read`, is a rollback per condition 4, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.

The effect is: the rich export's measured money rows carry the figure's own currency code (the same `_own_currency` reader as the PDF; the UNMEASURED figures stay withheld with the page's words); the rich export's management section prints the PDF's own CEO-profile sentence and the management passages the pack prints, instead of the reading word `the object could not be read`; the PDF appendix's served source and basis definition go through the plain-reason mapper at six sites; the unknown-verdict sentence reads `steer clear`; **nothing else moves**, and the PDF text of the eight names is expected identical. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own earlier captures are `C:/dev/ui-walk-evidence/r119-packs-before/`, `C:/dev/ui-walk-evidence/r119-rich-before/`, `C:/dev/ui-walk-evidence/r119-cand-packs/` and `C:/dev/ui-walk-evidence/r119-cand-rich/` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `by-5` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `by-5`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bz-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r119-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r119-packs-before2 C:/dev/ui-walk-evidence/r119-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bz-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (16 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US, the withheld figures graded as withheld); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bz-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than H3dCSGLEs4abPk0alOWclPZX1U6lYrxEXkhGZOAJ434=> modified=<a time after the apply began> rev=<a RevisionId other than caab3655-4909-4c3d-ba32-76446effe97d> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bz-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" 2771164d0d --pin d4c6f1c533 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin d4c6f1c533 ref 2771164d0d (2771164d0d) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `3ddc696def09` and `a281246c18c0`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bz-5.the-scoped-api-prints-the-rich-export-codes-management-and-appendix-from-the-release-pin.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `by-5` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bz-5.the-scoped-api-prints-the-rich-export-codes-management-and-appendix-from-the-release-pin.proof_of_spec.json` (the FULL order name, exactly: `round-close-check` and the L6 gate look for that name; the path is under the limit). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry (after the issuer's word, condition 5). Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-bz-5` (decomposition s.128), the served half of the CTO's round-118 items 1 to 4. Pair signed on both halves (CTO half @318bedccc3). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. SC1 reads mail only when nudged (it is often inside another COO's batch: peek, then a queued nudge, with that COO's consent for a break between pairs). The issuer reads the result only after the applier's report, never during, and reads nothing during its pre-act print and apply (three early reads of mine in earlier rounds are on record: do not repeat). Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `bv-5` to `by-5` did. The CTO half's condition 3 (the cause of C-S195 NAMED in the round-119 record) is met by `deliverables/0.9.0_WK_AMGT_RESAPP~518/BZ2_RECEIPT.md` `## Cause` (62 of 62 citations resolve) and by the round-119 L8 packet: both routes read ONE management object; the export printed the reader's label (`UNREADABLE_OBJECT`, mapped to `the object could not be read`) through a words table and never called the PDF's `_ceo_profile_sentence`.

<status>pending</status>
<round>119</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
