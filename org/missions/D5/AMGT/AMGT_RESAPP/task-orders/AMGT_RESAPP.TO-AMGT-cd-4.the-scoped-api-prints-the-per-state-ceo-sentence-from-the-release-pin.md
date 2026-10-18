# AMGT_RESAPP task order -- `AMGT-cd-4` -- THE SCOPED API PRINTS THE PER-STATE CEO-PROFILE SENTENCE FROM THE RELEASE PIN `d9cdd74096` (ONE CODE LEG, ONE MEMBER, A VERIFIED DELTA OF ZERO ON EVERY COVERED NAME)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cd-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cd-4.the-scoped-api-prints-the-per-state-ceo-sentence-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18): at the base (the LIVE function still the `ca-5` code, CodeSha256 `V9ZIXiUY..`): AC1 `PACK FORM` reads `YES (8 of 8 names)` (the pack's section form does not move in this act: AC1 is a REGRESSION control that PASSES at the base as expected), AC2 `MONEY VS PAGE` reads `YES (16 of 16 money lines)` (a regression control too), AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet there as expected, AC4 reads `members whose bytes differ: 1` and is true before the act (it grades the PIN). The act's OWN expected outcome is read by the issuer after the apply: THE PRINTED OUTPUT DOES NOT MOVE. MEASURED before the act (the CTO's round-121 grade): the 101-name census of the printed CEO line (`round122_prep/checks/r122_ceo_line_census.py`) of the LIVE function against this checkout's handler over the same live pool reads `COMPARE: 101 names in both captures, 100 byte-identical (pdf and rich), 0 MOVED, 1 skipped` (the skipped name `WALMEX*_MM_Equity` answers 500 from the handler on WINDOWS only, a `*` in a temp file name; the live function answers 200 for it and prints NO CEO line, so the change cannot move it): `DELTA: 0 (every printed CEO line is byte-identical)`. By the CTO's ruling that is DELTA=0 and needs no never-widen pair.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-cd-4` (round 122, decomposition s.131)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`d9cdd74096`** (branch `rel-amgt-cd4`, LOCAL on dell1; parent = the live pin `107fae40e9`, the `ca-5` build input; its only change is ONE member taken from this branch's merge `7a7a773265` of `AMGT-cd-1`: `lib/research/print/render_pack.py` blob `e83f9618952c` to `5d031ab30a55`, file sha256 `2f60c311f595` to `9de710064415`, `+28 -4`; `scoped_amgt.py` does not change, no import is added). **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `9de710064415`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD. No never-widen pair is owed (DELTA=0: the CTO's round-121 ruling, `ledger/ROUND_ANALYSIS.round121.R1.md` section 4 item 1: "If every line is byte-identical (HD US and BA US included), it is DELTA=0 and needs no pair"); the conditions below are the issuer's.

**THE CONDITIONS (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED. (The risk-reflex hold on `render_pack.py` cites the closure diff of the earlier redeploy records `amgt-rs-2` and `amgt-corpus-fwd12`: the content diff of condition 2 against the live package IS that closure for this act.)
2. **Before upload:** record the live `CodeSha256` (`V9ZIXiUYQTmDy9Efo4u9PgdNyn84DBsh9SVjgwMFYww=` at the cut), `LastModified` (`2026-10-18T16:12:11.000+0000`), the `RevisionId` (`92fc9ae9-8211-448c-ba88-07a09b319085`) and the `ca-5` artifact's S3 key and VersionId (`041tkPU3afZLQr_JrKu_vuEo3hX6Z4qe` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, uploaded 2026-10-18T16:09:02Z, the latest version of the key at the cut: that is the ROLLBACK TARGET; re-read the key's version list and confirm it is the version the function runs; the `ca-5` ledger entry `amgt-resapp-r120-ca5-ceo-three-states-source-not-stated-export-pillars-redeploy-dell1` in `org/critical_paths/change_management/` names the upload); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r122-packs-before2`** (the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `ca-5` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names on either format, or if the function does not answer.
5. **The issuer's reads (after your report):** the print route on BOTH formats for KMB US, RIO LN and GOOGL US, the all-names leak scan, the eight live rich exports, `r119_cross_surface.py` and **the 101-name census of the printed CEO line, live after the act against the live base (`C:/dev/ui-walk-evidence/r122-ceo-lines-live-base.json`): it must read `DELTA: 0`**. Any route over 20 s (70% of the 29 s timeout), a leak line, a cross-surface NO or any printed CEO line that moved is a rollback per condition 4, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.

The effect is: `_ceo_profile_sentence` has a branch for every known reading (a fixed per-state sentence only for a NON-plain reason; a plain reason prints byte-identically), an unknown reading prints a third sentence worded for the document, and the fixed fallback `no public profile is on file yet` is gone; **no printed line of any covered name moves**. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own captures are `C:/dev/ui-walk-evidence/r122-ceo-lines-live-base.json` and `r122-ceo-lines-cand.json` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `ca-5` entry did).
3. Standing: no push of shared branches.
4. A change the order does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `ca-5`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cd-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r122-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r122-packs-before2 C:/dev/ui-walk-evidence/r122-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cd-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (16 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US, the withheld figures graded as withheld); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cd-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than V9ZIXiUYQTmDy9Efo4u9PgdNyn84DBsh9SVjgwMFYww=> modified=<a time after the apply began> rev=<a RevisionId other than 92fc9ae9-8211-448c-ba88-07a09b319085> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-cd-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" d9cdd74096 --pin 107fae40e9 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin 107fae40e9 ref d9cdd74096 (d9cdd74096) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `e83f9618952c` and `5d031ab30a55`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-cd-4.the-scoped-api-prints-the-per-state-ceo-sentence-from-the-release-pin.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `ca-5` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-cd-4.the-scoped-api-prints-the-per-state-ceo-sentence-from-the-release-pin.proof_of_spec.json` (the FULL order name, exactly: `round-close-check` and the L6 gate look for that name; the path is under the limit). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry (after the issuer's word, condition 5). Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-cd-4` (decomposition s.131), the served half of the CTO's round-121 item 1. NO PAIR: the census of every covered name reads DELTA=0 (the CTO's rule); the CLAUDE.md hard stop reads "NEVER move served output without never-widen sign-off (CTO+COO); verified DELTA=0 needs no hold". The CTO is told in the round-122 packet. Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order. SC1 reads mail only when nudged (peek, then a queued nudge, with the batch COO's consent for a break between pairs). The issuer reads nothing from the function during SC1's pre-act print and apply. Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `ca-5` did.

<status>pending</status>
<round>122</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
