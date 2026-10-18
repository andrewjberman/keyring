# AMGT_RESAPP task order -- `AMGT-bx-5` -- THE SCOPED API PRINTS THE SERVED RECOMMENDATION, THE PAGE'S CURRENCY RULE AND THE LABELLED CLEARED PASSAGES, FROM THE RELEASE PIN `9ab6d36305` (ONE CODE LEG, ONE MEMBER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bx-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bx-5.the-scoped-api-prints-the-pack-summary-currency-and-passages-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18): at the base (the LIVE function still the `bw-5` code, CodeSha256 `lNWo6Cm6..`): AC1 `PACK FORM` reads `NO (3 of 8 names)` (the live packs carry the posture sentence's `s3://` path and `AMGT-rj-11`), AC2 `MONEY VS PAGE` reads `NO (12 of 16 money lines)` (four header money figures still print an amount the page withholds), AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet, AC4 reads `members whose bytes differ: 1` and is true before the act (it grades the PIN). All four are unmet or true as expected. The act's expected outcome was measured BEFORE the cut with this checkout's own handler over the live pool: `PACK FORM: YES (8 of 8 names)` and `MONEY VS PAGE: YES (16 of 16 money lines)`.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bx-5` (round 117, decomposition s.126)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`9ab6d36305`** (branch `rel-amgt-bx5`, LOCAL on dell1; parent = the live pin `fe04d740bf`, the `bw-5` build input; its only change is ONE member taken from the round-117 branch `0367a39372`: `lib/research/print/render_pack.py` blob `7f0f0d70a3ca` to `329f8b4e9304`, file sha256 `7f5c5bb94a18` to `004bafd2338f`). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND117_PACK_SUMMARY_CURRENCY_AND_PASSAGES_REDEPLOY_COO_HALF.md` @871379e429 (sha256 `60734f0e8167154f8c732b86ebf71cc97141959b3c24fa941395ce9db487f041`), CTO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND117_PACK_SUMMARY_CURRENCY_AND_PASSAGES_REDEPLOY_CTO_HALF.md` @2a3c57d709 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `004bafd2338f`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD.

**THE PAIR'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`lNWo6Cm6AjLrkBeu2rB25cpbcaVTXLgVH7RQ+dQGmtg=` at the cut), `LastModified` (`2026-10-18T05:52:41.000+0000`), the `RevisionId` (`2eecd7e1-03b4-4f34-bec7-767bbd437a6e`) and the `bw-5` artifact's S3 key and VersionId (`EVD2sGd8Bb.DGRU1XjvuhPJ6cOJo.otg` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`; the `L6` row of the ledger entry `amgt-resapp-r116-bw5-pack-note-currency-redeploy-dell1`, file under `org/critical_paths/change_management/`, names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r117-packs-before2`** (the live data moves between days, so the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bw-5` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names, or if the function does not answer.
5. **Latency (the CTO half's condition 3):** after the apply and your own reads, the ISSUER times the print route for KMB US, RIO LN and GOOGL US. Any one over 20 s (70% of the 29 s timeout) is a rollback per condition 4, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.
6. **The passages' negative control (the CTO half's condition 3):** the issuer has read the pool BEFORE the cut, 2026-10-18 ~07:4xZ, with a denominator: `95` ai_fill documents under `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/`, `475` blocks, `134` with text, ALL `CLEARED`, **none uncleared with text, so no live name holds an uncleared block**; an uncleared block is held back by the reader as an INVALID document (served with empty blocks). The live negative arm is therefore HD US and TSM US, whose five blocks all carry no text: after the apply their packs print NO machine-drafted passage and NO `machine-drafted, cleared` line (the issuer reads it); the uncleared arm itself is proven by the unit control `M4` of the merged tree. You record nothing for this condition beyond your own capture.

The effect is: the printed pack's `Summary` leads with the served recommendation (the cited `last_stated_position`: its text, the fund and weight and one `Source:` line); no state sentence of the pack names a storage path, a key, an order id or a vendor error; a header money figure whose basis is UNMEASURED is printed as the page's words `Bloomberg does not confirm this figure's currency` with no amount, and a measured figure prints its own currency or `currency not stated`; a cleared machine-written passage of `ai_fill` prints where the page shows it, followed by `machine-drafted, cleared <date>`, and an uncleared or withheld block prints nothing; **nothing else moves**. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own earlier captures are `C:/dev/ui-walk-evidence/r116-packs-issuer-after/`, `C:/dev/ui-walk-evidence/r117-cand2-packs/` and `C:/dev/ui-walk-evidence/r117-money-base.txt` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bw-5` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `bw-5`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bx-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r117-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r117-packs-before2 C:/dev/ui-walk-evidence/r117-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bx-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (16 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US, the withheld figures graded as withheld); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bx-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than lNWo6Cm6AjLrkBeu2rB25cpbcaVTXLgVH7RQ+dQGmtg=> modified=<a time after the apply began> rev=<a RevisionId other than 2eecd7e1-03b4-4f34-bec7-767bbd437a6e> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bx-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" 9ab6d36305 --pin fe04d740bf | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin fe04d740bf ref 9ab6d36305 (9ab6d36305) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `7f0f0d70a3ca` and `329f8b4e9304`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bx-5.the-scoped-api-prints-the-pack-summary-currency-and-passages-from-the-release-pin.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bw-5` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bx-5.the-scoped-api-prints-the-pack-summary-currency-and-passages-from-the-release-pin.proof_of_spec.json` (the FULL order name, exactly: `round-close-check` and the L6 gate look for that name; the path is under the limit). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry (after the issuer's latency word, condition 5). Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-bx-5` (decomposition s.126), the served half of the CTO's round-116 items 1 to 4. Pair signed on both halves (CTO half @2a3c57d709, msg 7956). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. SC1 may need a screen nudge to read it (`/unstick --peek`, then a typed prompt). The issuer reads the result only after the applier's report, never during. Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `bv-5` and `bw-5` did. The CTO's passages control: the pool read gave 95 documents, 475 blocks, none uncleared with text; HD US and TSM US are the live negative arm.

<status>complete</status>
<round>117</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
