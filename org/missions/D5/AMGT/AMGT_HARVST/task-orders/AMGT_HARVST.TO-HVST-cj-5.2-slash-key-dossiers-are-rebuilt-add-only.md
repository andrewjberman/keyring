# AMGT_HARVST task order -- `HVST-cj-5` -- ROUND 95, workstream DOSSIER-WRITE-SLASH: 2 `research_dossier` OBJECTS ARE ADDED FOR THE TWO SLASH-KEY SECURITIES `BP/_LN_Equity` AND `NG/_LN_Equity` (STAGED behind a signed never-widen pair, the gateway release `HVST-cj-3` read, and the host owner's notice) (CTO round-94 analysis section 3 and item 3; msg 7946)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cj-5.2-slash-key-dossiers-are-rebuilt-add-only</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cj-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs a dossier, continuation or fund-form build in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; the only writes are `PutObject` under `amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_Equity/` and `.../security_key=NG-SLASH-_LN_Equity/`. The BLAST RADIUS is two new gold objects that the gateway serves the moment they land, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree whose `lib/research` is not the pinned one, a `write_one` or `--write` run over all names, a name outside the list of two, a driver that writes before comparing the build with the served dossier, a moved field outside `fund_form_ref` and `model_rows`, a model-block guard that is not run (the CTO's, for `model_rows`), an object written under the RAW spelling `security_key=BP/_LN_Equity/` (a second form), a retry loop, a `continuation.write_one` beside, and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cj-4` wrote the 75 non-slash dossier objects (complete, re-read by the issuer). The two slash-key securities waited because a slash-key read returned half a record; `HVST-cj-3` (the gateway release) makes either spelling return the whole record, so the two dossiers can be written and read back through either spelling. **State plainly in `cj5_before.out`:** the served values DO move (`fund_form_ref` for BP only, `model_rows` for both, `as_of`, `dossier_key`, `content_sha256`); the rollback is an S3 delete that is not yours to take.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cj-3` is `<status>complete</status>`, `cj3_served.out` reads four PASS, and the GO says the issuer's own four-spelling reads of `BP/_LN_Equity` and `NG/_LN_Equity` came back whole.
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ5_DOSSIERS_SLASH.md` (the issuer prints its sha256 in the GO) and the CTO half named in the GO. Read both and the `cj-4` pair they repeat; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cj5-dossiers-slash.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. **Work in a worktree of your own cut AT `8f329a10b9` exactly**: print `git rev-parse HEAD` and `git diff 8f329a10b9 HEAD -- lib/research` (it must print empty) in `cj5_before.out`. The list files `deliverables/2.0.0_SA_COO_W1/round95/cj5_names.txt` (sha256 `1e8570870bcd47bc16b6958649b72797423afaaaa17c724c871317c3335bd923`, 2 lines) and `cj5_expected_moves.txt` (sha256 `726cbde1fd04e9fb5f1a9a3e62b8152aab2973bccf0d7a2a2a34e5b88820af36`, 2 lines) are read from the repo at the issuer's branch. Reuse your `cj4_run.py` driver of `HVST-cj-4` (its pre-write comparison, the CTO's model-block guard, `write_one`, the read-back and the manifest) as `cj5_run.py`: change only the list and the partition check below.
0. **Before-state, read only (`cj5_before.out`):** (i) the sha256 and line count of both list files; (ii) the count of objects under `amgt/harvest/gold/research_dossier/` (expected 1554) and `amgt/harvest/gold/research-continuation/` (expected 446); (iii) the scheduled-task list with its control (none runs a dossier, continuation or fund-form build in the window); (iv) the BEFORE gateway reads, for EACH of the four spellings `BP/_LN_Equity`, `BP-SLASH-_LN_Equity`, `NG/_LN_Equity`, `NG-SLASH-_LN_Equity`, with `fields` `["fund_form_ref","fund_of_record","last_stated_position","model_rows"]`, printing every returned `dossier_fields` and `continuation_fields` entry, `continuation_key`, `dossier_key`, `source_keys`, `content_sha256`, `as_of`, `duplicates_dropped`, `denominator_note`, `truncated`, `omitted_items` and `research_reports[]` entry; (v) how you count "a row with a value" for the model-block guard (as in `cj-4`). DO NOT call `etfs_compare_peers`; DO NOT run any module's `--write`.
1. **Canary:** `python -u cj5_run.py BP/_LN_Equity` (foreground); the driver checks the written object key lies under `security_key=BP-SLASH-_LN_Equity/` (a key under the raw spelling is a STOP). Then the four gateway reads of step 0 (iv) again as `cj5_canary.out`: for each of the four spellings every returned entry other than `fund_form_ref` and `model_rows` (BP; the list says what moves) is EQUAL to the before read; `dossier_key`, `as_of`, `content_sha256`, the dossier entry of `source_keys`, `duplicates_dropped` and `denominator_note` differ (EXPECTED); the `dossier_key` is the NEW object for ALL FOUR spellings. Anything else: STOP.
2. **The second name:** `python -u cj5_run.py NG/_LN_Equity` (foreground), then the gateway reads of both NG spellings against their before reads (only `model_rows` and the pointers move).
3. **After (`cj5_after.out`):** (i) the dossier count equals step 0 (ii) plus 2 and the continuation count equals its start count; (ii) the gateway's dossier pick (`harvest_research.py::_pick_dossier`, lines 239-255) over a fresh listing of each ENCODED partition names the manifest key (`pick_equals_manifest=<n of 2>`); (iii) the manifest holds 2 lines.
4. **Write `cj5_served.out`** ending with exactly these lines: `DOSSIERS_WRITTEN_AND_READ_BACK=PASS|FAIL`, `CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS|FAIL`, `PICK_NAMES_MANIFEST_KEYS=PASS|FAIL`, `COUNTS_AS_EXPECTED=PASS|FAIL`. In the ledger close say: no continuation was written; no object sits under the raw spelling; the 75 non-slash names, KMB and the 17 other names were not touched.
5. Commit the ledger close WITH the manifest. Tell the issuer when the first object is written and read through the four spellings, and when `cj5_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing further, file one row and tell me:** the worktree is not at `8f329a10b9` or the `lib/research` diff is not empty, or either list sha256 differs; a scheduled task runs a dossier, continuation or fund-form build in the window; a site Z write to the prefix is in flight; a name not in the list; the pre-write comparison shows a moved field outside the set or an input kind outside the set, or the model-block guard fails; `write_one` prints `unchanged`; the object key is not under the ENCODED partition; AccessDenied, `GoldImmutableError` or a throttle (print its exact text); `put_performed` false; a read-back that differs; a count that is not +1 for the name; a missing manifest line; the canary read differs in anything the COO half does not name as expected, or any of the four spellings does not return the NEW `dossier_key`.
- **After the last write, a difference not named here:** write it plainly, do NOT self-grade, finish the read-only steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted.
- **Expected and NOT a failure:** the gateway returns the same new dossier for the raw and the encoded spelling (after `cj-3`); `model_rows` may be omitted by the response-size cap (print `truncated` and `omitted_items`; equal before and after, or compare at the S3 level); the printed key is the raw `BP/_LN_Equity`.
- **Window:** from my GO to 60 minutes later; if the second name has not landed by then, stop and tell me.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cj5-dossiers-slash.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cj-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj5_served.out</invocation><expect>(?m)^DOSSIERS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cj-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj5_served.out</invocation><expect>(?m)^CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cj-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj5_served.out</invocation><expect>(?m)^PICK_NAMES_MANIFEST_KEYS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cj-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj5_served.out</invocation><expect>(?m)^COUNTS_AS_EXPECTED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that no continuation was written and exactly two objects were added (the pair's counts); AC2 is the proof that the served moves are only the named ones and that BOTH spellings serve the new object (the slash-key fix's own grade); AC3 is the proof that the gateway's pick names each written object.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cj-5.2-slash-key-dossiers-are-rebuilt-add-only.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cj-5.2-slash-key-dossiers-are-rebuilt-add-only` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cj-5.2-slash-key-dossiers-are-rebuilt-add-only.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
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
- **STAGED, not sent.** It waits on the CTO half, `HVST-cj-3` released and read (my four-spelling reads first), site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`, C-10) and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-94 analysis @428b762698 section 3 and item 3. Decomposition section 130.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if there is none.


**COMPLETE 2026-10-18T11:5xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** seat `0.7.0_AE_CloudOps~SC1`, GO 11:11:53Z with `GO_UTC` 11:15:00Z (site Z CLEAR 11:15Z-12:30Z, its CTO msg 35685 via MSTR msg 8013); SC1 was busy on the RESAPP `by-5` apply, so I typed the nudge when it was idle (11:22:25Z, READ 11:22:37Z); `BP/_LN_Equity` written 11:30:25Z (`as_of=2026-10-18.2d0238f7570cff0e.json`, 265,712 bytes) and `NG/_LN_Equity` 11:34:16Z (`as_of=2026-10-18.1af6506669c49a8a.json`), both under the ENCODED partition, none under the raw spelling; the CTO's model-block guard PASS for both (BP: stamp `20261017T130241Z` later than `20261011T130307Z`, 91 valued rows before and after); read-backs PASS; ledger `harvst-cj5-dossiers-slash` CLOSED 11:40:46Z, COMMITTED (`c199581bf6`); deliverables `4aa32e3e71`, `c9facabbb6`, `f7576dfed8` (the proof instance was INVALID twice on a row-pin class and fixed, stated in the ledger entry). Pair COO `1e2728c9...` + CTO `93f7352b2e` (citation fix `7de585d788`).
- **Read by me (not SC1's word):** `deliverables/2.0.0_SA_COO_W1/round95/cj5_issuer_verify.out`: 1556 objects in the table (1554 + 2), 446 continuations (unchanged); both gateway picks name the manifest key; method `/15`, hash recomputed equal, `subject.security_key` the raw name; **the fields that moved against the dossier served before are exactly the census's list: BP `fund_form_ref` and `model_rows`, NG `model_rows`**; proof instance VALID rc 0 (re-run here). **My own gateway reads after:** `BP/_LN_Equity` (the raw spelling, read right after the canary: new `dossier_key`, `fund_form_ref` on the version-2 IDVZ form `fund=idvz/65a5baab3afd06f0.json`, listed 16, distinct `as_of` 8, continuation, ai_fill, 7 reports and roster equal to before), `NG/_LN_Equity` and `NG-SLASH-_LN_Equity` (both: the new `dossier_key` `as_of=2026-10-18.1af6506669c49a8a.json`, `content_sha256` `5863bdfb...` equal, listed 15, everything else equal to my reads before the write).
- **SC1's plain limits:** BP was compared by script, NG by reading against its transcription (the tool results were inline); NG's pre-write gateway reads were not repeated (S3-level proof instead). My own reads of NG before the write (10:5xZ) and after cover the comparison. **Not read by me:** `BP-SLASH-_LN_Equity` after the write (SC1 read it; the raw spelling returned the same dossier); `model_rows` through the gateway for either name (the response-size cap omits it; BP's was compared at the S3 level by SC1 and by my script for both names).
- **What this does NOT prove:** the effect on consumers of these two dossiers (the RESAPP COO's measurement of 101 names was taken before these two writes); the rollback (an S3 delete of the two keys, Andrew's act) was not taken.
- **Own workstream** `DOSSIER-WRITE-SLASH`.
- **Not covered, named:** any other name; the path-component spelling question.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>95</round>
<workstream>DOSSIER-WRITE-SLASH</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
