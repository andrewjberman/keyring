# AMGT_HARVST task order -- `HVST-cj-4` -- ROUND 95, workstream DOSSIER-WRITE: 75 `research_dossier` OBJECTS ARE ADDED, ONE PER SECURITY WHOSE SERVED DOSSIER WOULD MOVE AND WHOSE KEY HAS NO SLASH (STAGED behind a signed never-widen pair and the host owner's notice) (CTO round-94 analysis section 3 and item 2; msg 7946)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cj-4.75-non-slash-dossiers-are-rebuilt-add-only</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cj-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs a dossier, continuation or fund-form build against the bucket in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; the only writes are `PutObject` under `amgt/harvest/gold/research_dossier/security_key=<KEY>/` for the 75 names of the list. The BLAST RADIUS is 75 new gold objects that the gateway serves the moment they land, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree whose `lib/research` is not the pinned one, a `dossier.write_one` or `--write` run over all names (it would also write KMB and the two slash names), a name outside the list, a driver that writes before comparing the build with the served dossier, a moved field outside `fund_form_ref` and `model_rows` that is written anyway, a retry loop that writes a second object for a name, a detached process whose buffered output hides a gap (`D1-S44`), a canary not read through the gateway before the other 73, a `continuation.write_one` slipping in beside, and a half-landed batch (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-ci-3` (merged `15ef6e687d`) measured that, for 77 of the 95 securities, the dossier `dossier.build` makes today differs from the one the gateway serves, and only in `fund_form_ref` (to the version-2 fund forms) and `model_rows` (from a newer `model_block` input). The CTO ruled (msg 7946): the rebuild runs for every name WITHOUT a slash in its key (75 of the 77), under its own pair; the two slash-key names wait. This cell writes the 75 new dossier objects, add-only. **State plainly in `cj4_before.out`:** the served values DO move (`fund_form_ref`, `model_rows`, `as_of`, `dossier_key`, `content_sha256`, the dossier entry of `source_keys`): the new object is served the moment it lands, and the rollback is an S3 delete that is not yours to take.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ci-3` is `<status>complete</status>` and merged (`15ef6e687d`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ4_DOSSIERS_NONSLASH.md` (the issuer prints its sha256 in the GO) and the CTO half in `org/missions/D5/AMGT/AMGT_HARVST/ledger/` named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cj4-dossiers-nonslash.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. **Work in a worktree of your own cut AT `8f329a10b9` exactly (the commit `HVST-ci-3`'s census ran on; `git worktree add <path> 8f329a10b9`; it is an ancestor of `15ef6e687d` and reachable in the repository)**: print `git rev-parse HEAD` in `cj4_before.out`, and `git diff 8f329a10b9 HEAD -- lib/research` (it must print empty: the CTO's C-1). The list file `deliverables/2.0.0_SA_COO_W1/round95/cj4_names.txt` and `cj4_expected_moves.txt` are read from the repo at the issuer's branch (their sha256: names `ebcec99e045a59d0871b25532ff9d74b337c00ddefe568a4d5303cf86947567e`, 75 lines; expected moves `ba4cd92ef19efc12f84a292de3df35743732ee9ac39291323611e31ab5ad88ff`, 75 lines).
0. **Before-state, read only (`cj4_before.out`):** (i) the sha256 and line count of both list files; (ii) the count of objects under `amgt/harvest/gold/research_dossier/` (expected 1479 at the time of the census; print the actual) and under `amgt/harvest/gold/research-continuation/` (expected 446); (iii) the scheduled-task list with its control (`Get-ScheduledTask`): none runs a dossier, continuation or fund-form build in the window; (iv) the BEFORE gateway reads of `UNH_US_Equity` and `CPA_US_Equity` with `fields` `["fund_form_ref","fund_of_record","last_stated_position","model_rows"]`, printing every returned `dossier_fields` and `continuation_fields` entry, `continuation_key`, `dossier_key`, `source_keys`, `content_sha256`, `as_of`, `duplicates_dropped`, `denominator_note`, `truncated`, `omitted_items` and `research_reports[]` entry. DO NOT call `etfs_compare_peers`; DO NOT run any module's `--write`.
1. **Write the driver** `cj4_run.py` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/`: takes one or more names from `cj4_names.txt` as arguments (a name not in the list is a STOP); for each name, in the order given: (1) builds in memory with `dossier.build(security_key)` and compares it with the dossier the gateway serves (copy the pick rule of `infra/aws/ec2/opal-gateway/app/harvest_research.py::_pick_dossier`, lines 239-255; read them first): the moved `fields` must be a SUBSET of `{fund_form_ref, model_rows}` and the differing `inputs` kinds (the dossier's own names for them; read `dossier.build`) a subset of `{continuation, fund_form, model_block}` (STOP before that name's write otherwise); **AND the CTO's model-block guard (his half, condition 1; read `lib/research/corpus/dossier.py` lines 1185-1250, `_model_block_read`, and 1511-1513 first), for a name whose build moves `model_rows`: the build's model-block record reads `status: SERVED`; the timestamp in its object key (`derived/model_block/<slash_safe_key>/<timestamp>/model_block.json`) is LATER than the model-block stamp in the stored dossier's `inputs`; and the number of rows of the new `model_rows` that carry a value is NOT lower than the same number for the served `model_rows` (read the shape of `model_rows` first; print in `cj4_before.out` how you count "a row with a value", and print the two counts per name in the manifest); for a name whose build does not move `model_rows`: the record still reads SERVED, or the served `model_rows` is already built from no block; otherwise STOP before that name's write (a `READ_FAILED` or `ABSENT` block moves only `model_rows` and would serve emptier rows); (2) calls `dossier.write_one(security_key)`; if it prints `unchanged ... wrote 0` that is a STOP; (3) reads the object back and checks Branch A of the COO half; (4) appends the manifest line to `cj4_written.out` and flushes it BEFORE the next name. It has a plan mode that refuses a write outside GO to GO+150 minutes. NO loop over the list, NO retry, NO background mode.
2. **Canary:** `python -u cj4_run.py UNH_US_Equity` then `python -u cj4_run.py CPA_US_Equity`, each its own foreground command; then the gateway reads of step 0 (iv) again, as `cj4_canary.out`, compared with the before reads entry by entry as the COO half's C-7 names: `fund_form_ref` and `model_rows` move as `cj4_expected_moves.txt` says for that name and in no other way; `dossier_key`, `as_of`, `content_sha256`, the dossier entry of `source_keys`, `duplicates_dropped` and `denominator_note` differ (EXPECTED); everything else EQUAL. Anything else: STOP.
3. **The other 73:** in sorted order, at most 10 names per foreground command (5 if a command would near the tool's ten-minute limit; each name costs two builds), a batch stopping at its first anomaly; append each command's output to `cj4_run.log`. Between batches print the running count of manifest lines.
4. **After (`cj4_after.out`):** (i) the dossier object count equals step 0 (ii) plus the number of manifest lines, and the continuation count equals its start count; (ii) for every manifest name, the gateway's dossier pick rule applied to a listing of its partition names the manifest key (print a count `pick_equals_manifest=<n of n>`); (iii) the manifest holds 75 lines (or fewer with the reason of each name not written).
5. **Write `cj4_served.out`** ending with exactly these lines: `DOSSIERS_WRITTEN_AND_READ_BACK=PASS|FAIL` (manifest 75 lines, every read-back equal), `CANARY_GATEWAY_MOVES_AS_NAMED=PASS|FAIL`, `PICK_NAMES_MANIFEST_KEYS=PASS|FAIL`, `COUNTS_AS_EXPECTED=PASS|FAIL`. In the ledger close say: no continuation was written; the two slash-key names, KMB and the 17 other unchanged names were not rebuilt.
6. Commit the ledger close WITH the manifest. Tell the issuer when the canary is written (before the 73), when the last name is written and read back, and when `cj4_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing further, file one row and tell me:** the worktree is not at `8f329a10b9` or the `lib/research` diff against it is not empty, or either list sha256 differs; the model-block guard of step 1 (1) fails for a name; a scheduled task runs a dossier, continuation or fund-form build in the window; a site Z write to the prefix is in flight; a name not in the list; the pre-write comparison shows a moved field outside the set or an input kind outside the set; `write_one` prints `unchanged`; AccessDenied, `GoldImmutableError` or a throttle (print its exact text); `put_performed` false; a read-back that differs; an object count that is not +1 for the name; a missing or late manifest line; the canary gateway read differs from the before read in anything the COO half does not name as expected.
- **After the last write, a difference not named here:** write it plainly (what differs, how, the read that shows it), do NOT self-grade the criterion, finish the remaining READ-ONLY steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted. A written object is repaired by a still newer dossier object decided by the issuer and the CTO, never by deletion.
- **Expected and NOT a failure:** the gateway `dossier_key`, `as_of`, `content_sha256` and the dossier entry of `source_keys` name the new object after the write; `duplicates_dropped.research_dossier` and the `denominator_note` count one more object; `fund_form_ref` and `model_rows` move as the list says; the continuation entries stay equal; the stored continuations still cite nothing of the dossier; `model_rows` may be large (the gateway may report `truncated` or `omitted_items` for it: print them, equal before and after is the check); `BP/_LN_Equity`, `NG/_LN_Equity` and `KMB_US_Equity` are not in the list.
- **Window:** from my GO to 150 minutes later; if the 75th name has not landed by then, stop and tell me. Do not exceed the window to finish.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cj4-dossiers-nonslash.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cj-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj4_served.out</invocation><expect>(?m)^DOSSIERS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cj-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj4_served.out</invocation><expect>(?m)^CANARY_GATEWAY_MOVES_AS_NAMED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cj-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj4_served.out</invocation><expect>(?m)^PICK_NAMES_MANIFEST_KEYS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cj-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj4_served.out</invocation><expect>(?m)^COUNTS_AS_EXPECTED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that no continuation was written and that exactly the manifest names were added (the pair's C-6 and C-8); AC2 is the proof that the served moves are only the ones the pair names; AC3 is the proof that the gateway now picks every written object.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cj-4.75-non-slash-dossiers-are-rebuilt-add-only.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cj-4.75-non-slash-dossiers-are-rebuilt-add-only` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cj-4.75-non-slash-dossiers-are-rebuilt-add-only.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** every command in this order is foreground and unbuffered; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefix are AMGT's own).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half of the pair, site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`, C-10) and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-94 analysis @428b762698 (msg 7946) section 3 RULING and item 2. Decomposition section 125.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; no ask that needs an answer inside the window; I check SC1's READ ack within 10 minutes of the handing and type a nudge if there is none (the second recorded instance for row `D1-S54`, if it happens).
- **The worktree pin is mine and is `15ef6e687d` (the commit after the `ci-3` merge):** the census I re-ran ran on the shared tree after `6837f7c754`; the commits between touch `lib/research/print` and `lib/research/api` (RESAPP), not the dossier build. I have NOT diffed the `lib/research/corpus`, `harvest` and `identity` trees of the census run against `15ef6e687d`; the per-name pre-write comparison in the driver is what grades the write, not this pin.
- **Window set by me:** GO to GO+150 minutes (two builds per name, about a minute each, 75 names, plus the canary reads and the after-census); the pair left the length to the order.
- **The 18 unchanged names are not rebuilt, and I name KMB** (a differing continuation key only; `write_one` would write it; no served field moves): the CTO's ruling names the 77 moved names. KMB is a question I leave with him in the half.

- **AMENDMENT 1 (issuer, 2026-10-18 ~07:3xZ; the CTO half is SIGNED `b9e244d5a9`, msg 7949, binding the COO half at sha256 `35e368f31b784a7d4e285dafd124588e56b87fb8773c272dfda052b7b7972e57` unchanged; his half is `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CJ4_DOSSIERS_NONSLASH_CTO_HALF.md`):** (1) **the model-block guard** (his condition 1) is added to step 1 (1) and to the STOP list; (2) **the worktree pin changes from `15ef6e687d` to `8f329a10b9`**: his C-1 requires the `lib/research` diff from the census commit to the worktree commit to print empty, and `15ef6e687d` differs from `8f329a10b9` by `substrate.py` (the `ci-2` fallback fix, 14 lines) and RESAPP's `lib/research/print` files; I measured that diff (`git diff --stat 8f329a10b9 15ef6e687d -- lib/research`), so the pin is the census commit itself. The `ci-2` change cannot reach this act (no partition falls to the fallback: `ci-1`'s census, 0 of 109) and my own re-run of the `ci-3` census on the later tree is identical to the worker's; (3) KMB stays out (his acceptance). No criterion text changed. **Gate:** a modification of a non-terminal order that declares `<placeholders>NONE</placeholders>`; GATE (viii) grades such a modification (it graded `ci-1`'s amendment); the commit's gate output is read and stated in the next note.
- **Own workstream** `DOSSIER-WRITE`.
- **Not covered, named:** the two slash-key dossiers (item 3, after `HVST-cj-2`); KMB and the 17 equal-input names; any continuation write.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>95</round>
<workstream>DOSSIER-WRITE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
