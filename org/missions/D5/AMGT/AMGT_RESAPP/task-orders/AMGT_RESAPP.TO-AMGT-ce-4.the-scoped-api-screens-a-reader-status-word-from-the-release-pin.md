# AMGT_RESAPP task order -- `AMGT-ce-4` -- THE SCOPED API SCREENS A READER STATUS WORD FROM A SERVED REASON, FROM THE RELEASE PIN `9281d3c0b2` (ONE CODE LEG, ONE MEMBER, A VERIFIED DELTA OF ZERO ON EVERY COVERED NAME)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ce-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ce-4.the-scoped-api-screens-a-reader-status-word-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-19): at the base (the LIVE function still the `cd-4` code, CodeSha256 `UdNfBJqF..`): AC1 `PACK FORM` is a REGRESSION control (the printed pack does not move in this act) and is graded against a before set taken the same session; AC2 `MONEY VS PAGE` is a regression control; AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet there as expected; AC4 reads `members whose bytes differ: 1` and is true before the act (it grades the PIN). The act's OWN expected outcome is read by the issuer after the apply: THE PRINTED OUTPUT DOES NOT MOVE. MEASURED before the act: the 101-name census of the printed CEO line (`round122_prep/checks/r122_ceo_line_census.py`) of the LIVE function (`C:/dev/ui-walk-evidence/r122-ceo-lines-live-after.json`) against this checkout's handler over the same live pool (`r123-ceo-lines-local-candidate.json`) reads `COMPARE: 101 names in both captures, 100 byte-identical (pdf and rich), 0 MOVED, 1 skipped` (the skipped name `WALMEX*_MM_Equity` answers 500 from the handler on WINDOWS only, a `*` in a temp file name; the live function answers 200 for it and prints NO CEO line, so the change cannot move it): `DELTA: 0 (every printed CEO line is byte-identical)`. By the CTO's round-122 ruling that is DELTA=0 and needs no never-widen pair.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-ce-4` (round 123, decomposition s.132)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`9281d3c0b2`** (branch `rel-amgt-ce4`, LOCAL on dell1; parent = the live pin `d9cdd74096`, the `cd-4` build input; its only change is ONE member taken from this branch's merge `6cbbd1e980` of `AMGT-ce-1`: `lib/research/print/render_pack.py` blob `5d031ab30a55` to `023406bfda53`, file sha256 `9af5d3b144ed`, `+3 -0`; `scoped_amgt.py` does not change, no import is added). **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `9af5d3b144ed`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD. No never-widen pair is owed (DELTA=0: the CTO's round-122 analysis, `ledger/ROUND_ANALYSIS.round122.R1.md` section 4 item 2: "The 101-name census then reads DELTA 0 ... DELTA 0 needs no pair"); the conditions below are the issuer's.

**THE CONDITIONS (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2 (slug `amgt-resapp-r123-ce4-status-word-screen-redeploy-dell1`); its CLOSE is COMMITTED. (The risk-reflex hold on `render_pack.py` cites the closure diff of the earlier redeploy records: the content diff of condition 2 against the live package IS that closure for this act.)
2. **Before upload:** record the live `CodeSha256` (`UdNfBJqFC1IBUnpFjTCh+etviWiwoE9WEHynZiuw35w=` at the cut), `LastModified` (`2026-10-18T22:39:05.000+0000`), the `RevisionId` (`66f7c293-2273-4d6a-8c89-45328b6d3495`) and the `cd-4` artifact's S3 key and VersionId (`lBeU2g53TMxeRkB3x.gXs16hAv0w5Z2D` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, content-sha256 `UdNfBJqFC1IBUnpFjTCh+etviWiwoE9WEHynZiuw35w=`: that is the ROLLBACK TARGET; re-read the key's version list and confirm it is the version the function runs; the `cd-4` ledger entry `amgt-resapp-r122-cd4-per-state-ceo-sentence-redeploy-dell1` in `org/critical_paths/change_management/` names the upload); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r123-packs-before`** (the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **The plan is code-only:** the saved plan must read exactly 1 to change, 0 to add, 0 to destroy, graded from the plan JSON, and only the function's code attributes (`source_code_hash` and its S3 object version) change. The function is `module.scoped_amgt_api` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, so the route IS a plan on the harvest root (AMENDED 2026-10-19 ~16:3xZ after SC1's msg 8391; my first text wrongly called the harvest root out of bounds). The root's flag defaults are misaligned (CTO msg 8348, row `AMGT_HARVST-D1-W183-S14`): a plain plan reads destroys, and **a plan that reads any destroy is a STOP, never applied.** The permitted plan passes the SAME three variables the root was last applied with (`dossier_refresh_build_enabled=true`, `dossier_refresh_run_enabled=true`, `dossier_refresh_image_digest=<the applied digest>`), read back from the last applied stage's record before the plan, so that the plan differs from the applied state in the function's code only. **A nonzero add or destroy, a changed attribute other than the code ones, or a state lock held by another stage (W1's HVST-cn-7) is a STOP;** do not plan or apply while a W1 stage holds the lock.
4. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
5. **Rollback:** re-point the function to the `cd-4` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names on either format, or if the function does not answer.
6. **The issuer's reads (after your report):** the print route on BOTH formats for KMB US, RIO LN and GOOGL US, the all-names leak scan, the eight live rich exports, `r119_cross_surface.py` and **the 101-name census of the printed CEO line, live after the act against the live base (`C:/dev/ui-walk-evidence/r122-ceo-lines-live-after.json`): it must read `DELTA: 0`**. Any route over 20 s (70% of the 29 s timeout), a leak line, a cross-surface NO or any printed CEO line that moved is a rollback per condition 5, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.

The effect is: a served reason that carries one of the reader's status words (`ABSENT`, `CONFIRMED` and the six underscore words) is not plain, so the pack prints the calling site's own fixed sentence instead of the word; **no printed line of any covered name moves** (none carries a status word today). No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own captures `C:/dev/ui-walk-evidence/r122-ceo-lines-live-after.json` and `r123-ceo-lines-local-candidate.json` must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `cd-4` entry did).
3. Standing: no push of shared branches.
4. A change the order does not name is a STOP and, inside the same hour, a rollback per condition 5 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `cd-4`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ce-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r123-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r123-packs-before C:/dev/ui-walk-evidence/r123-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ce-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (16 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US, the withheld figures graded as withheld); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ce-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than UdNfBJqFC1IBUnpFjTCh+etviWiwoE9WEHynZiuw35w=> modified=<a time after the apply began> rev=<a RevisionId other than 66f7c293-2273-4d6a-8c89-45328b6d3495> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ce-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" 9281d3c0b2 --pin d9cdd74096 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin d9cdd74096 ref 9281d3c0b2 (9281d3c0b2) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `5d031ab30a55` and `023406bfda53`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-ce-4.the-scoped-api-screens-a-reader-status-word-from-the-release-pin.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `cd-4` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-ce-4.the-scoped-api-screens-a-reader-status-word-from-the-release-pin.proof_of_spec.json` (the FULL order name, exactly: `round-close-check` and the L6 gate look for that name; the path is under the limit). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry (after the issuer's word, condition 6). Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-ce-4` (decomposition s.132), the served half of the CTO's round-122 item 2 (W524-S1). NO PAIR: the census of every covered name reads DELTA=0 (`r123-ceo-lines-local-candidate.json` against `r122-ceo-lines-live-after.json`, the live function after `cd-4`); the CLAUDE.md hard stop reads "NEVER move served output without never-widen sign-off (CTO+COO); verified DELTA=0 needs no hold". Pin built from the live pin `d9cdd74096` by plumbing (a temporary index, ONE blob replaced), branch `rel-amgt-ce4`, LOCAL on dell1. Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order. SC1 reads mail only when nudged. The issuer reads nothing from the function during SC1's pre-act print and apply. Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `cd-4` did.

<status>complete</status>
<round>123</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
