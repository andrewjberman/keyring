# AMGT_RESAPP task order -- `AMGT-bu-7` -- THE SCOPED API PRINTS EVERY PACK DATE IN THE HOUSE LONG FORM FROM THE RELEASE PIN `6bb7b23ee5` (ONE CODE LEG, ONE MEMBER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-7.the-scoped-api-prints-pack-dates-in-long-form-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-17 ~23:5xZ) -- AC1 run against the LIVE function (still the `bp-6` code) at the base reads `PACK COMPARE: NO (0 of 8 names ...)` (every pack still prints ISO days), so its expectation of YES 8 of 8 is unmet there as expected; AC2 reads `CONFIG sha=hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=` at the base, so its expectation of a CodeSha256 other than that one is unmet there as expected; AC3 (the pin's content diff) reads `members whose bytes differ: 1` at the base and is the one criterion that is true before the act (it grades the PIN, not the function).
EGRESS CLASS, declared: the Lambda invoke of the print route and the config read by the read-only instrument, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bu-7` (round 114, decomposition s.123)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`6bb7b23ee5`** (branch `rel-amgt-bu7`, LOCAL on dell1; parent = the live pin `7a8f2bb8e6`, the `bp-6` build input; its only change is `lib/research/print/render_pack.py`, blob `729693a65f7f` to `fa514afbb2f6`, file sha256 `8e8266859b7b` to `60a9f2ddb4f4`, taken from the `bu-3` merge `0100aab018`). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND114_PACK_DATES_REDEPLOY_COO_HALF.md` @677d9d137f (sha256 `2b44fd785bac625640880311dd4ecca67e58df3aa55451507ac4da099ea99c7f`), CTO half `..._CTO_HALF.md` @97a893bb89 (SIGNED; it binds exactly those COO bytes). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/print/render_pack.py` at sha256 `60a9f2ddb4f4`; any other member, or that member at another hash, is a STOP BEFORE UPLOAD.

**THE CTO HALF'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=` at the cut), `LastModified` (`2026-10-17T16:34:05.000+0000`), the `RevisionId` (`cf9191fc-e3d2-4c9a-8a3e-2672858446e7`) and the `bp-6` artifact's S3 key and VersionId (the `L6` row of the ledger entry `org/critical_paths/change_management/20261017T1620Z_amgt-resapp-r110-bp6-segment-label-redeploy-dell1_deploy_completion.md` names the object it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified`, `CodeSha256` and `RevisionId` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py config` and STOP if any differs from your pre-act print (one writer for this function).** **Also immediately before the upload capture a FRESH BEFORE set of the eight packs: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py capture C:/dev/ui-walk-evidence/r114-packs-before2`** (the live data moves between days, so AC1 compares the after-act packs with this set, taken in the same session, and not with the issuer's earlier set; the instrument masks the page-1 `Printed` day, which is the capture day).
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT, memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bp-6` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if any pack still prints an ISO day or differs beyond dates after the act, or the function does not answer.

The effect is: the printed PDF and plain-text pack print every date in the house long form (`September 22nd, 2026`) instead of the served ISO day; **nothing else moves**. The `format=rich` export is NOT changed and still prints ISO days (a stated limit). No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads; the issuer's BEFORE captures of eight packs at `C:/dev/ui-walk-evidence/r114-packs-before/` must not be overwritten).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bp-6` entry did).
3. Standing: no push of shared branches.
4. A change the pair does not name is a STOP and, inside the same hour, a rollback per condition 4 unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bu-7"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" capture C:/dev/ui-walk-evidence/r114-packs-after | tail -1 &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" compare C:/dev/ui-walk-evidence/r114-packs-before2 C:/dev/ui-walk-evidence/r114-packs-after | tail -1; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `PACK CAPTURE: 8 of 8 names captured (0 not 200)` then the line `PACK COMPARE: YES (8 of 8 names: no ISO day after and equal to before once the long forms map back)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-7"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py" config; echo "exit=$?"</invocation><expect>three lines: `CONFIG sha=<a CodeSha256 other than hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=> modified=<a time after the apply began> rev=<a RevisionId other than cf9191fc-e3d2-4c9a-8a3e-2672858446e7> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` and `AMGT_AIFILL_ROOT in env: False`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bu-7"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" 6bb7b23ee5 --pin 7a8f2bb8e6 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin 7a8f2bb8e6 ref 6bb7b23ee5 (6bb7b23ee5) | members whose bytes differ: 1`, then the row `lib/research/print/render_pack.py` with blobs `729693a65f7f` and `fa514afbb2f6`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bp-6` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bu-7.the-scoped-api-prints-pack-dates-in-long-form-from-the-release-pin.proof_of_spec.json` (if the path is past MAX_PATH on this box, say so in a row and use a short sibling name the checker accepts). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the placed cell `AMGT-bu-7` (decomposition s.123), the pack half of the CTO's round-113 item 2. Pair signed on both halves (CTO half @97a893bb89, msg 7780); the CTO's three conditions are inlined (the re-read of `LastModified`, `CodeSha256` and `RevisionId` immediately before the upload is the one-writer condition; no cross-adjudication hold this time: the CTO's half names none). Applier: the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34; `bp-6` used `0.7.0_AE_CloudOps~SC1`); a SEAT order, not a worker order. The issuer reads the result only after the applier's report, never during (AC1 captures eight live packs; the applier runs it; the BEFORE captures were taken by the issuer at the cut). Risk class WORLD. `W506-S5` (prose rewriting) is ruled IN SCOPE by the CTO except a verbatim source-quotation block; if the pack prints any, it becomes a round-115 cell with a census first and does not block this deploy.

<status>complete -- 2026-10-18 by the issuer (2.0.0_SA_COO~R1): 0.7.0_AE_CloudOps~SC1 applied the saved plan 01:14:56Z-01:16:23Z from release pin 6bb7b23ee5 (CodeSha256 hLW4fD.. to RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=, rev cf9191fc to 3c6a52dc, LastModified 2026-10-18T01:16:17Z, memory 1769, timeout 29, env keys unchanged, AMGT_AIFILL_ROOT absent); content diff 408 members, 407 identical, 1 changed (render_pack.py 8e8266859b7b to 60a9f2ddb4f4); plan after: no changes; rollback target (the bp-6 artifact) VersionId 3TWvFWWa.qf6mrqKodzvQU3DhV_eCTRd, not needed; ledger amgt-resapp-r114-bu7-pack-dates-redeploy-dell1 closed 9 of 9. THE ISSUER'S OWN SECOND READ (a fresh capture of the same eight live packs, compared with the issuer's own earlier BEFORE set, not SC1's): PACK COMPARE YES (8 of 8): 0 ISO days after, and equal to before once the long forms map back; ISO-day counts before 51, 51, 51, 30, 51, 50, 51, 33 became the same numbers of long-form days; config read equal. Quoted-source blocks: three of the eight packs (BA, HD, KMB) print quoted passages, none carried an ISO day, so none was altered here; the guard WOULD rewrite an ISO day inside one, so W506-S5 becomes a round-115 cell with a census of verbatim-quote blocks first (the CTO's ruling, msg 7780). The format=rich export still prints ISO days (row W506-S4).</status>
<round>114</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
