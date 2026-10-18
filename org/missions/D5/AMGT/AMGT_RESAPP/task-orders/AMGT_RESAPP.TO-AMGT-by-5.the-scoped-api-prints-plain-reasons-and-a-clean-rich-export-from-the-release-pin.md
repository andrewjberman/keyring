# AMGT_RESAPP task order -- `AMGT-by-5` -- THE SCOPED API PRINTS PLAIN REASONS IN THE PACK AND A CLEAN RICH EXPORT, FROM THE RELEASE PIN `d4c6f1c533` (ONE CODE LEG, TWO MEMBERS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-by-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-by-5.the-scoped-api-prints-plain-reasons-and-a-clean-rich-export-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18): at the base (the LIVE function still the `bx-5` code, CodeSha256 `Rycs0LV..`): AC1 `PACK FORM` reads `YES (8 of 8 names)` (the pack's section form does not move in this act: AC1 is a REGRESSION control that PASSES at the base as expected), AC2 `MONEY VS PAGE` reads `YES (16 of 16 money lines)` (a regression control too), AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet there as expected, AC4 reads `members whose bytes differ: 2` and is true before the act (it grades the PIN). The act's OWN expected outcome is read by the issuer after the apply and was measured at the base: the LIVE rich exports carry 2 `s3://` lines and 2 `AMGT-` lines each (RIO LN, ICT PM, GOOGL US) and RIO LN's raw market cap; the candidate (this checkout's handler over the live pool) reads 0 of each and RIO LN's four figures withheld, and an all-names leak scan of 0 leaking lines of 101.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-by-5` (round 118, decomposition s.127)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`d4c6f1c533`** (branch `rel-amgt-by5`, LOCAL on dell1; parent = the live pin `9ab6d36305`, the `bx-5` build input; its only changes are TWO members taken from the round-118 merge `ebe4f0bda9`: `lib/research/print/render_pack.py` blob `329f8b4e9304` to `3ddc696def09`, file sha256 `004bafd2338f` to `5f4cffc172ba`; and `lib/research/api/scoped_amgt.py` blob `43c8139d2d2d` to `75a6e6480d7d`, file sha256 `472df817702c` to `1fcf51f05afc`). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND118_PACK_REASON_MAPPER_AND_RICH_EXPORT_REDEPLOY_COO_HALF.md` @6b38f6b2e8 (sha256 `a647dcd622f98498d5b744a4f88f3560325545161637b1c1438ba5b9a5a49a9a`), CTO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND118_PACK_REASON_MAPPER_AND_RICH_EXPORT_REDEPLOY_CTO_HALF.md` @a23b7c68b4 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly TWO members, `lib/research/print/render_pack.py` at sha256 `5f4cffc172ba` and `lib/research/api/scoped_amgt.py` at sha256 `1fcf51f05afc`; any other member, or either at another hash, is a STOP BEFORE UPLOAD.

**THE PAIR'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`Rycs0LVaL8jbdI1bL1+M5o+KSy+HOGehQucN2ysFstE=` at the cut), `LastModified` (`2026-10-18T08:51:36.000+0000`), the `RevisionId` (`05fed159-4f5f-487e-ad82-37934272468c`) and the `bx-5` artifact's S3 key and VersionId (`2TBErsoGd68qZqe3kUnuh0PFFYreDnLO` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`; the `L6` row of the ledger entry `amgt-resapp-r117-bx5-pack-summary-currency-passages-redeploy-dell1`, file under `org/critical_paths/change_management/`, names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r118-packs-before2`** (the live data moves between days, so the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bx-5` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names on either format, or if the function does not answer.
5. **Latency (the CTO half's condition 3):** after the apply and your own reads, the ISSUER reads the print route on BOTH formats (`format=pdf` and `format=rich`) for KMB US, RIO LN and GOOGL US, and the all-names leak scan and the eight live rich exports. Any route over 20 s (70% of the 29 s timeout), or a leak line, or a rich export still naming `s3://` or `AMGT-`, is a rollback per condition 4, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.

The effect is: every served reason the printed pack can print goes through one plain-sentence mapper (a reason naming a storage path, a key, an order id, a vendor error or a field code prints the site's own fixed sentence; an absent or `None` posture reads `No positioning view is on file for this name.`); the `format=rich` export applies the same mapper, withholds the four header money figures the page withholds (`Bloomberg does not confirm this figure's currency`, no amount) and guards each of its three readers (a raising reader is an absent input and prints its absence sentence); **nothing else moves**. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own earlier captures are `C:/dev/ui-walk-evidence/r118-packs-after-cj4/`, `C:/dev/ui-walk-evidence/r118-cand-packs/`, `C:/dev/ui-walk-evidence/r118-cand-rich/`, `C:/dev/ui-walk-evidence/r118-rich-before/` and `C:/dev/ui-walk-evidence/r118-leak-scan-live.json` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bx-5` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `bx-5`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-by-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r118-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r118-packs-before2 C:/dev/ui-walk-evidence/r118-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-by-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (16 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US, the withheld figures graded as withheld); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-by-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than Rycs0LVaL8jbdI1bL1+M5o+KSy+HOGehQucN2ysFstE=> modified=<a time after the apply began> rev=<a RevisionId other than 05fed159-4f5f-487e-ad82-37934272468c> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-by-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" d4c6f1c533 --pin 9ab6d36305 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin 9ab6d36305 ref d4c6f1c533 (d4c6f1c533) | members whose bytes differ: 2`, then the rows `lib/research/api/scoped_amgt.py` with blobs `43c8139d2d2d` and `75a6e6480d7d` and `lib/research/print/render_pack.py` with blobs `329f8b4e9304` and `3ddc696def09`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-by-5.the-scoped-api-prints-plain-reasons-and-a-clean-rich-export-from-the-release-pin.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bx-5` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-by-5.the-scoped-api-prints-plain-reasons-and-a-clean-rich-export-from-the-release-pin.proof_of_spec.json` (the FULL order name, exactly: `round-close-check` and the L6 gate look for that name; the path is under the limit). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry (after the issuer's word, condition 5). Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-by-5` (decomposition s.127), the served half of the CTO's round-117 items 1 and 2. Pair signed on both halves (CTO half @a23b7c68b4, msg 8007). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. SC1 reads mail only when nudged (round 117: a typed prompt after a screen look; it may be inside another COO's batch: ask that COO for a break and use its consent). The issuer reads the result only after the applier's report, never during. Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `bv-5`, `bw-5` and `bx-5` did. The CTO's condition: the 20 s bar on BOTH routes (pdf and rich). The CTO's round-119 row: `UNKNOWN_VERDICT_SENTENCE` (render_pack.py:840) prints `steer_clear`, an underscore the mapper itself treats as not plain: not this act's.

<status>pending</status>
<round>118</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
