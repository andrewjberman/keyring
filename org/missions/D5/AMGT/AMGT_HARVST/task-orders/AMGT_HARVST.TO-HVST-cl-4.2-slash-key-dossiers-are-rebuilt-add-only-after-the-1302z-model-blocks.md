# AMGT_HARVST task order -- `HVST-cl-4` -- ROUND 97, workstream DOSSIER-WRITE-SLASH-2: 2 `research_dossier` OBJECTS ARE ADDED AGAIN FOR THE TWO SLASH-KEY SECURITIES `BP/_LN_Equity` AND `NG/_LN_Equity` AFTER THE 13:02Z MODEL BLOCKS (STAGED behind a signed never-widen pair and the host owner's notice) (CTO round-96 analysis enrichment item 2, msg 8092)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cl-4.2-slash-key-dossiers-are-rebuilt-add-only-after-the-1302z-model-blocks</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cl-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs a dossier, continuation or fund-form build in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; the only writes are `PutObject` under `amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_Equity/` and `.../security_key=NG-SLASH-_LN_Equity/`. The BLAST RADIUS is two new gold objects that the gateway serves the moment they land, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree whose `lib/research` is not the pinned one (HEAD's `lib/research` differs from the pin by another project's commit `33edcbdf16`), a `write_one` or `--write` run over all names, a name outside the list of two, a driver that writes before comparing the build with the served dossier, a moved field outside `fund_form_ref` and `model_rows` or different from the expected list, a model-block guard that is not run (the CTO's), an object written under the RAW spelling `security_key=BP/_LN_Equity/` (a second form), a retry loop, a `continuation.write_one` beside, and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cj-5` wrote the two slash-key dossiers at 11:30Z and 11:34Z on 2026-10-18; a harvest cycle then wrote new model blocks for both names at 13:02Z and 13:07Z. `HVST-cl-3`'s census (read-only, re-run by the issuer) shows that a rebuild would move exactly ONE served field for each name, `model_rows` (cause `model_block`; the model-block guard passes: BP 91 and 91 valued rows, NG 64 and 64). The CTO ordered the rebuild under the `cj-5` shape. **State plainly in `cl4_before.out`:** the served value that moves is `model_rows` (omitted from the gateway's response body by its size cap, proved at the S3 level) plus the pointers (`dossier_key`, `content_sha256`, the dossier entry of `source_keys`); `fund_form_ref` does NOT move; the rollback is an S3 delete that is not yours to take.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cl-3` is `<status>complete</status>` and merged (`b8014771a1`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round97/NEVER_WIDEN_HALF_COO_CL4_DOSSIERS_SLASH_AFTER_1302Z.md` (the issuer prints its sha256 in the GO) and the CTO half named in the GO. Read both and the `cj-5` pair they repeat; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cl4-dossiers-slash-after-1302z.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. **Work in a worktree of your own cut AT `4c7a60cabe` exactly**: print `git rev-parse HEAD` and `git diff 4c7a60cabe HEAD -- lib/research` (it must print empty) in `cl4_before.out`. The list files `deliverables/2.0.0_SA_COO_W1/round97/cl4_names.txt` (sha256 `1e8570870bcd47bc16b6958649b72797423afaaaa17c724c871317c3335bd923`, 2 lines) and `cl4_expected_moves.txt` (sha256 `e81381b913d0922c5448f5302a0330f39298313b1da48b90e729391fc61bcbb1`, 2 lines: `model_rows` for both names) are read from the repo at the issuer's branch (they are not in your pinned tree: read them from the shared checkout and print their sha256). Reuse your `cj5_run.py` driver of `HVST-cj-5` (its pre-write comparison, the CTO's model-block guard, `write_one`, the read-back and the manifest) as `cl4_run.py`: change only the list, the expected-moves file, the pin and the partition check below. **The guard's read of the model-block record:** `dossier.build()` returns no such record field, so read the status through `dossier._model_block_read` on the same client (as the census `cl3_census.py` did, `deliverables/0.9.0_WK_AMGT_HARVST~175/cl3_census.out` lines `GUARD`), print it, and if your `cj5_run.py` guard reads it another way print both: a difference is a STOP.
0. **Before-state, read only (`cl4_before.out`):** (i) the sha256 and line count of both list files; (ii) the count of objects under `amgt/harvest/gold/research_dossier/` and `amgt/harvest/gold/research-continuation/` (print them; the table held 1556 and 446 after `cj-5`; a different count: print it and name its writer or STOP); (iii) the scheduled-task list with its control (none runs a dossier, continuation or fund-form build in the window); (iv) the BEFORE gateway reads, for EACH of the four spellings `BP/_LN_Equity`, `BP-SLASH-_LN_Equity`, `NG/_LN_Equity`, `NG-SLASH-_LN_Equity`, with `fields` `["fund_form_ref","fund_of_record","last_stated_position","model_rows"]`, printing every returned `dossier_fields` and `continuation_fields` entry, `continuation_key`, `dossier_key`, `source_keys`, `content_sha256`, `as_of`, `duplicates_dropped`, `denominator_note`, `truncated`, `omitted_items` and `research_reports[]` entry; (v) how you count "a row with a value" for the model-block guard (as in `cj-5`). DO NOT call `etfs_compare_peers`; DO NOT run any module's `--write`.
1. **Canary:** `python -u cl4_run.py BP/_LN_Equity` (foreground); the driver checks the written object key lies under `security_key=BP-SLASH-_LN_Equity/` (a key under the raw spelling is a STOP). Then the four gateway reads of step 0 (iv) again as `cl4_canary.out`: for each of the four spellings every returned entry other than the pointers (`dossier_key`, `content_sha256`, the dossier entry of `source_keys`, `duplicates_dropped`, `denominator_note`; `model_rows` if the cap lets it through) is EQUAL to the before read; the `dossier_key` is the NEW object for ALL FOUR spellings. Anything else: STOP.
2. **The second name:** `python -u cl4_run.py NG/_LN_Equity` (foreground), then the gateway reads of both NG spellings against their before reads (only the pointers and `model_rows` move).
3. **After (`cl4_after.out`):** (i) the dossier count equals step 0 (ii) plus 2 and the continuation count equals its start count; (ii) the gateway's dossier pick (`harvest_research.py::_pick_dossier`; read its lines at the pinned tree: the function is at lines 270-287 at HEAD, not 239-255) over a fresh listing of each ENCODED partition names the manifest key (`pick_equals_manifest=<n of 2>`); (iii) the manifest holds 2 lines.
4. **Write `cl4_served.out`** ending with exactly these lines: `DOSSIERS_WRITTEN_AND_READ_BACK=PASS|FAIL`, `CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS|FAIL`, `PICK_NAMES_MANIFEST_KEYS=PASS|FAIL`, `COUNTS_AS_EXPECTED=PASS|FAIL`. In the ledger close say: no continuation was written; no object sits under the raw spelling; the 75 non-slash names, KMB and the 17 other names were not touched.
5. Commit the ledger close WITH the manifest. Tell the issuer when the first object is written and read through the four spellings, and when `cl4_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing further, file one row and tell me:** the worktree is not at `4c7a60cabe` or the `lib/research` diff is not empty, or either list sha256 differs; a scheduled task runs a dossier, continuation or fund-form build in the window; a site Z write to the prefix is in flight; a name not in the list; the pre-write comparison shows a moved field other than `model_rows` or an input kind other than `model_block`, or the model-block guard fails or its two reads differ; `write_one` prints `unchanged`; the object key is not under the ENCODED partition; AccessDenied, `GoldImmutableError` or a throttle (print its exact text); `put_performed` false; a read-back that differs; a count that is not +1 for the name; a missing manifest line; the canary read differs in anything the COO half does not name as expected, or any of the four spellings does not return the NEW `dossier_key`.
- **After the last write, a difference not named here:** write it plainly, do NOT self-grade, finish the read-only steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted.
- **Expected and NOT a failure:** the gateway returns the same new dossier for the raw and the encoded spelling; `model_rows` is omitted by the response-size cap (print `truncated` and `omitted_items`; equal before and after, or compare at the S3 level); the printed key is the raw `BP/_LN_Equity`; the new object has the SAME `as_of` date (2026-10-18) as the stored one and a different `inputs_sha16`, and wins the pick on `LastModified`.
- **Window:** from my GO to 60 minutes later; if the second name has not landed by then, stop and tell me.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cl4-dossiers-slash-after-1302z.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cl-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl4_served.out</invocation><expect>(?m)^DOSSIERS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cl-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl4_served.out</invocation><expect>(?m)^CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cl-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl4_served.out</invocation><expect>(?m)^PICK_NAMES_MANIFEST_KEYS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cl-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl4_served.out</invocation><expect>(?m)^COUNTS_AS_EXPECTED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that no continuation was written and exactly two objects were added (the pair's counts); AC2 is the proof that the served moves are only the named ones and that BOTH spellings serve the new object; AC3 is the proof that the gateway's pick names each written object.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cl-4.2-slash-key-dossiers-are-rebuilt-add-only-after-the-1302z-model-blocks.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cl-4.2-slash-key-dossiers-are-rebuilt-add-only-after-the-1302z-model-blocks` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cl-4.2-slash-key-dossiers-are-rebuilt-add-only-after-the-1302z-model-blocks.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions; run the row gate against your row WITHOUT any override first (the `Z-S106` override must cover that pre-existing pair only).
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** every command in this order is foreground and unbuffered; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefix are AMGT's own).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half, site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`) and the issuer's GO; SC1 may also be busy on `HVST-cl-2` or another lane's work. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-96 analysis (msg 8092) enrichment item 2. The census is `HVST-cl-3`. Decomposition section 132.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if the seat is idle.
- Dry run at the base: all four criteria FAIL as expected (the file does not exist).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>97</round>
<workstream>DOSSIER-WRITE-SLASH-2</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
