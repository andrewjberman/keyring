# AMGT_RESAPP task order -- `AMGT-bp-6` -- THE SCOPED API CARRIES THE SEGMENT-COLUMN LABEL FROM THE RELEASE PIN `7a8f2bb8e6` (ONE CODE LEG, ONE MEMBER) -- HELD FOR THE LAPTOP CTO'S RULING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bp-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bp-6.redeploy-the-scoped-api-carrying-the-segment-column-label-from-the-release-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule, layer, memory, timeout or environment moves.
comp-adversary: RUN at the cut (2026-10-17 ~15:4xZ) -- AC1's census run against the LIVE function (still the `bm-3` code) at the base reads `names 95 | EQUAL 82 | LABEL_NOTE 13 | OTHER 0 | ERROR 0`, so its expectation of `EQUAL 95` is unmet there as expected; AC2's script reads `RIO_LN periods[4] label=Period 5` and `CONFIG sha=UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=` at the base, so its expectation of `Year not stated (column 5)` and a CodeSha256 other than that one is unmet there as expected; AC3 (the pin's content diff) reads `members whose bytes differ: 1` at the base and is the one criterion that is true before the act (it grades the PIN, not the function).
EGRESS CLASS, declared: the Lambda invoke and S3 reads of the live pool by the read-only instruments, the upload through `upload_verified.sh`, and the one apply; nothing else.
</preflight>

## 1. THE CELL -- `AMGT-bp-6` (round 109 placed, cut in round 110, decomposition s.118 and s.119)

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the RELEASE PIN **`7a8f2bb8e6`** (branch `rel-amgt-bp6`, LOCAL on dell1; parent = the live pin `3818736e6b`, the `bm-3` build input; its only change is `lib/research/api/segment_served.py`, blob `cd72ba96223a` to `cbf094d0b633`, taken from the bp-3 merge). The pair is the authority on what may move: COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND110_SEGMENT_LABEL_REDEPLOY_COO_HALF.md` @170bfbb9a1 (sha256 `10880f423cc6a8031ae250abe94696436bfc9f3c8ddda32931f48905e017d27f`), CTO half `..._CTO_HALF.md` @d6de7cba95 (SIGNED). READ BOTH WHOLE FIRST. **THE BUILD'S OWN CONTENT DIFF AGAINST THE LIVE PACKAGE IS THE AUTHORITY ON WHAT SHIPS:** the package may differ from the live one in exactly ONE member, `lib/research/api/segment_served.py` at blob `cbf094d0b633`; any other member, or that member at another blob, is a STOP BEFORE UPLOAD. The Terraform plan must show the function's CODE only; a plan that moves the environment, role, layers, memory or timeout is a STOP. The model for every leg is the `bm-3` entry `org/critical_paths/change_management/20261014T1252Z_amgt-resapp-r106-bm3-fwd-pe-withhold-redeploy-dell1_deploy_completion.md` (legs L1 to L11: pin read in a detached worktree, rollback table, wheel folder re-hash, build with the content diff printed first, `upload_verified.sh`, saved-plan `safe-apply`, the record step): follow its route; the legs that read the forward P/E (L5, L7, L8, L9) do NOT apply.

**THE HOLD (a STOP, do not upload before it clears).** The CTO half is signed, and the call went to the laptop CTO as cross-adjudication `XA-20261017T152527Z-e56b` (the shared `lib/` tree). **You prepare and you may build, but you do NOT upload and you do NOT apply until `python .tools/xadj.py show --id XA-20261017T152527Z-e56b` prints `State: RULED` with the ruling `(a)`.** Read it again immediately before the upload; `OPEN`, or a ruling other than (a), is a STOP and a report.

**THE CTO HALF'S CONDITIONS, inlined (each a STOP if it cannot be met):**
1. **NEVER-2 first:** open the change-management entry BEFORE condition 2; its CLOSE is COMMITTED.
2. **Before upload:** record the live `CodeSha256` (`UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=` at the cut), `LastModified` (`2026-10-16T09:12:01.000+0000`), the `RevisionId` (`54f36694-8c00-4ce9-9dc1-dcfa3be92406`) and the `bm-3` artifact's S3 key and VersionId (the `L6` row of the `bm-3` entry names the artifact it uploaded: that is the ROLLBACK TARGET); then print the built package's content diff against the live package. **IMMEDIATELY before the upload, re-read `LastModified` and `CodeSha256` with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round110_prep/checks/r110_bp6_config_and_label.py` and STOP if either differs from your pre-act print.**
3. **After the apply:** read back the new `CodeSha256` (it must differ from the pre-act one) and confirm the environment is UNCHANGED; in particular `AMGT_AIFILL_ROOT` stays ABSENT (the AI-fill hold is lifted and stays lifted), memory 1769, timeout 29, environment keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
4. **Rollback:** re-point the function to the `bm-3` artifact recorded in condition 2, by the same saved-plan route, and read back a `CodeSha256` EQUAL to the pre-act one. Roll back in the same window if any name reads LABEL_NOTE or OTHER after the act, or the function does not answer.

The effect is: a segment-table period whose year is not resolved and which carries a figure is served `label` `Year not stated (column <n>)` instead of `Period <n>`, and the three period-note sentences say "the years ... are not stated"; **nothing else moves** (measured over all 95 resolved names: 82 equal, 13 label or note only, 0 other). No data object is written, no S3 delete. **No other reader of the function runs during your pre-act print and the apply** (the issuer holds its reads).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the code of `opal-amgt-scoped-api` and the files it names; no other function, no role, route, schedule, layer or environment variable.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install` (the build runs with the wheel folder `PIP_NO_INDEX=1`, as the `bm-3` entry did).
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
  <criterion id="AC1" cell_refs="AMGT-bp-6"><invocation>cd C:/dev/ajb_workspace &amp;&amp; PYTHONPATH="$(pwd)" timeout 890 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round110_prep/checks/r110_bp3_served_delta.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/bp6_post_act_census.json" --workers 6 | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `names 95 | EQUAL 95 | LABEL_NOTE 0 | OTHER 0 | ERROR 0 | columns relabelled 0 (names with one: 0)` (the live function now equals the checkout on the segment block); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bp-6"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round110_prep/checks/r110_bp6_config_and_label.py"; echo "exit=$?"</invocation><expect>four lines: `CONFIG sha=<a CodeSha256 other than UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=> modified=<a time after the apply began> rev=<a RevisionId other than 54f36694-8c00-4ce9-9dc1-dcfa3be92406> mem=1769 timeout=29 state=Active update=Successful`, `ENV keys=['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']`, `AMGT_AIFILL_ROOT in env: False`, and `RIO_LN periods[4] label=Year not stated (column 5) fiscal_year=None top_level_sum=106861.0 (status 200)`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bp-6"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" 7a8f2bb8e6 --pin 3818736e6b | head -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `pin 3818736e6b ref 7a8f2bb8e6 (7a8f2bb8e6) | members whose bytes differ: 1`, then the row `lib/research/api/segment_served.py` with blobs `cd72ba96223a` and `cbf094d0b633`; and exit=0 (the pin, unchanged before and after the act)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the `bm-3` artifact's key and VersionId and the pre-act `CodeSha256`) as the discriminating control, at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_RESAPP.TO-AMGT-bp-6.redeploy-the-scoped-api-carrying-the-segment-column-label-from-the-release-pin.proof_of_spec.json` (the order's file name is the one for the canonical path; if the path is past MAX_PATH on this box, say so in a row and use a short sibling name the checker accepts). `proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step (the pre-act print, the content diff, the plan denominators, the apply output, the post-act read-back);
- the change-management entry's slug and state;
- every criterion's output lines;
- the `xadj` state you read before the upload;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** The placed cell `AMGT-bp-6` of rounds 109 and 110 (decomposition s.118, s.119). The pair is signed on both halves (CTO half @d6de7cba95, msg 7645); the CTO's four conditions plus one are inlined (the re-read of `LastModified` and `CodeSha256` immediately before the upload). **THE HOLD:** the call reads CROSS-BOX (the shared `lib/` tree), so the CTO sent it to the laptop CTO as `XA-20261017T152527Z-e56b` (REC (a)); this order is cut at `pending` so the applier can prepare and build, and the order states the upload and the apply wait on that xadj reading RULED (a). The applier is the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34; CTO msg 6816 names `0.7.0_AE_CloudOps~SC1`), which holds other AMGT_HARVST work; the order is a SEAT order, not a worker order. The issuer reads the result: after the apply the issuer re-runs the census (AC1) as a second reader only after the applier's report, never during. Risk class WORLD: a deploy; the CTO's exercised read and the change-management entry are its evidence. The base measurements named in the preflight were read at the cut (2026-10-17 ~15:4xZ): the live `CodeSha256` `UIkRgr9gbz2R...`, `LastModified` 2026-10-16T09:12:01Z, `RevisionId` `54f36694-...`, environment keys without `AMGT_AIFILL_ROOT`, RIO LN `periods[4].label` `Period 5`, and the pin's one-member diff.

<status>complete -- 2026-10-17 by the issuer (2.0.0_SA_COO~R1): 0.7.0_AE_CloudOps~SC1 applied the saved plan 16:32:39Z-16:34:12Z from release pin 7a8f2bb8e6 (CodeSha256 UIkRgr9g.. to hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=, rev cf9191fc, LastModified 2026-10-17T16:34:05Z); the issuer's second read at ~16:5xZ: config sha hLW4fD.., env keys HARVEST_ARTICLES_TABLE and HARVEST_METRICS_TABLE only (AMGT_AIFILL_ROOT absent), RIO LN periods[4] label 'Year not stated (column 5)', census names 95 EQUAL 95 LABEL_NOTE 0 OTHER 0 ERROR 0 (deliverables/2.0.0_SA_COO~R1/round110_prep/bp6_post_act_census.json); AC1-AC3 PASS; instance VALID at 748a26e496; ledger amgt-resapp-r110-bp6-segment-label-redeploy-dell1 closed by SC1</status>
<round>110</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~SC1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
