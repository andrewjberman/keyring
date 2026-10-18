# AMGT_RESAPP task order -- `AMGT-bw-5` -- THE SCOPED API PRINTS THE PACK AS A NOTE WITH EACH MONEY FIGURE IN ITS OWN CURRENCY, FROM THE RELEASE PIN `fe04d740bf` (ONE CODE LEG, TWO MEMBERS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bw-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bw-5.the-scoped-api-prints-the-pack-as-a-note-with-each-money-figure-in-its-own-currency-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-18) -- at the base (the LIVE function still the `bv-5` code, CodeSha256 `lp+7X1V..`): AC1 `PACK FORM` reads NO (the live pack has no appendix heading), AC2 `MONEY VS PAGE` reads `NO (11 of 17 money lines)`, AC3 reads the pre-act CodeSha256 so its expectation of another one is unmet, AC4 reads `members whose bytes differ: 2` and is true before the act (it grades the PIN). All four are unmet or true as expected. The act's expected outcome was measured BEFORE the cut with this checkout's own handler over the live pool: `MONEY VS PAGE: YES (15 of 15 money lines)` and `PACK FORM: YES (8 of 8 names)`.
EGRESS CLASS, declared: the Lambda invoke of the print and thesis routes and the config read by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bw-5` (round 116, decomposition s.125)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`fe04d740bf`** (branch `rel-amgt-bw5`, LOCAL on dell1; parent = the live pin `d4bba34eb8`, the `bv-5` build input; its only changes are TWO members taken from the round-116 merge `b1628a34ef`: `lib/research/print/render_pack.py` blob `89d4c2a34b89` to `7f0f0d70a3ca`, file sha256 `8a1f47d8c6cd` to `7f5c5bb94a18`; and `lib/research/api/scoped_amgt.py` blob `a75ab14fd16d` to `43c8139d2d2d`, file sha256 `73f53b54747d` to `472df817702c`). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND116_PACK_FORM_AND_CURRENCY_REDEPLOY_COO_HALF.md` @b5c979c224 (sha256 `764716037aaf6d8b503fa98396f0aaeed75e6876fa0e6c3ee50af648f1b1bc3a`), CTO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND116_PACK_FORM_AND_CURRENCY_REDEPLOY_CTO_HALF.md` @aaa5219ad5 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly TWO members, `lib/research/print/render_pack.py` at sha256 `7f5c5bb94a18` and `lib/research/api/scoped_amgt.py` at sha256 `472df817702c`; any other member, or either at another hash, is a STOP BEFORE UPLOAD.

**THE PAIR'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`lp+7X1VkDi7sFz3v5W3yZSlWFZaMQSKo7knlvp1GxBQ=` at the cut), `LastModified` (`2026-10-18T03:07:37.000+0000`), the `RevisionId` (`e4e64b80-28bf-4e1a-8f68-f85e312db781`) and the `bv-5` artifact's S3 key and VersionId (`kF6PjYv9I.PZF9kNMUGxBM98ZYpE922E` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`; the `L6` row of the ledger entry `amgt-resapp-r115-bv5-rich-export-quotes-redeploy-dell1`, file under `org/critical_paths/change_management/`, names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r116-packs-before2`** (the live data moves between days, so the criteria compare the after-act capture with this one, taken in the same session; the instrument masks the page-1 `Printed` day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bv-5` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if the pack form check (AC1) or the money check (AC2) reads NO, if the print route answers with a non-200 for any of the eight names, or if the function does not answer.

5. **Latency (the CTO half's condition 3):** after the apply and your own reads, the ISSUER times the print route for KMB US, RIO LN and GOOGL US. Any one over 20 s (70% of the 29 s timeout) is a rollback per condition 4, which the issuer orders; keep the rollback ready until the issuer's word, and do not close the entry before it.

The effect is: the printed pack reads as a note (Summary, Risks and considerations, Company description, Management, Positioning, Peers, What changed, then the model figures as an appendix); every money amount prints the currency its own figure carries, or the page's words `currency not stated`; the print route reads the thesis bundle, the peer set and the posture the rich export already reads, each guarded; **nothing else moves**. No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; its own earlier captures are `C:/dev/ui-walk-evidence/r116-packs-before/`, `C:/dev/ui-walk-evidence/r116-cand-packs/` and `C:/dev/ui-walk-evidence/r116-money-base.txt` and must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bv-5` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600; AC4 is a fourth criterion for the one reason that the pin's content diff is the act's own bound and the config read its own control, as in `bv-5`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bw-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r116-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_form_check.py" C:/dev/ui-walk-evidence/r116-packs-before2 C:/dev/ui-walk-evidence/r116-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK FORM: YES (8 of 8 names)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bw-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 600 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116_prep/checks/r116_pack_money_vs_page.py" | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `MONEY VS PAGE: YES (N of N money lines)` with the two N equal (15 at the cut; the live pack against the page's served figure for ICT PM, RIO LN and GOOGL US); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bw-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than lp+7X1VkDi7sFz3v5W3yZSlWFZaMQSKo7knlvp1GxBQ=> modified=<a time after the apply began> rev=<a RevisionId other than e4e64b80-28bf-4e1a-8f68-f85e312db781> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bw-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" fe04d740bf --pin d4bba34eb8 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin d4bba34eb8 ref fe04d740bf (fe04d740bf) | members whose bytes differ: 2`, then the rows `lib/research/api/scoped_amgt.py` with blobs `a75ab14fd16d` and `43c8139d2d2d` and `lib/research/print/render_pack.py` with blobs `89d4c2a34b89` and `7f0f0d70a3ca`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bv-5` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bw-5.the-scoped-api-prints-the-pack-as-a-note-from-the-release-pin.proof_of_spec.json` (if the path is past MAX_PATH on this box, say so in a row and use a short sibling name the checker accepts). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-bw-5` (decomposition s.125), the served half of the CTO's round-115 items 1 to 3. Pair signed on both halves (CTO half @aaa5219ad5). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. SC1 may need a screen nudge to read it (`/unstick --peek`, then a typed prompt). The issuer reads the result only after the applier's report, never during. Risk class WORLD. The REDEPLOY workstream carries it beside the round's issuance, as `bv-5` did.

<status>complete</status>
<round>116</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
