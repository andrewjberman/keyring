# AMGT_HARVST task order -- `HVST-ch-7` -- ROUND 93, workstream CONT-M5: 78 `research-continuation` OBJECTS OF METHOD 5 ARE WRITTEN, ONE PER SECURITY WITH NO CONTINUATION AT THE CURRENT METHOD (STAGED behind a signed never-widen pair and the host owner's notice) (CTO round-92 analysis item 4; msg 7903)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ch-7.78-continuations-of-method-5-are-written</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ch-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs a continuation, dossier or fund-form build against the bucket in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; the only writes are `PutObject` under `amgt/harvest/gold/research-continuation/security_key=<KEY>/` for the 78 names of the list. The BLAST RADIUS is 78 new gold objects, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree that is not `091ebacda9`'s `lib/research` (the CTO found HEAD differs by 22 files), a `dossier.write_one` or `continuation --write` of all names beside this act, a name outside the list, a driver that writes before comparing the build with the served object, a retry loop that writes a second object for a name, a detached process whose buffered output hides a gap (`D1-S44`), a canary not read through the gateway before the other 76, and a half-landed batch (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-ch-8` (merged `091ebacda9`) measured that, for each of 78 securities whose newest continuation is at method `/3` (56) or `/4` (22), the continuation `continuation.build` makes today has EVERY field equal to the served one and the same `inputs`. This cell writes the 78 `/5` objects, add-only, so that each name has a continuation at the current method. **State plainly in `ch7_before.out`:** the served values do not change; only each name's `continuation_key` and `source_keys` come to name the new object.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ch-1`, `-2` and `-8` are `<status>complete</status>` and merged (`091ebacda9`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round93/NEVER_WIDEN_HALF_COO_CH7_CONTINUATIONS_M5.md` (sha256 `19d80c8bf6bafa94157d1152cc2bcf9f8a11a58fe0c21dc877c49f0dbf8f213c`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CH7_CONTINUATIONS_M5_CTO_HALF.md` (signed `5d4e716fd1`). Read both; their conditions C-1 to C-10 and the CTO's three conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-ch7-continuations-m5.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. **Work in a worktree of your own cut AT `091ebacda9` exactly** (the CTO measured that today's HEAD differs from it by 22 files under `lib/research/print/` and `lib/research/api/`, so a later commit does not qualify): print `git rev-parse HEAD` in `ch7_before.out`, and the list file `deliverables/2.0.0_SA_COO_W1/round93/ch7_securities.txt` (read it from the repo at HEAD of the issuer's branch; its sha256 must read `db965262ed4c02179c43bb8346a5c4d24953cc638b669c6a354dff36fae698ac`, 78 lines).
0. **Before-state, read only (`ch7_before.out`):** (i) per name of the list (the SAME comparator as `HVST-ch-8`'s `deliverables/0.9.0_WK_AMGT_HARVST~168/ch8_census.py`, which you run unchanged for the whole of step 0 (i)): `CENSUS-CONT-REBUILD ... names=78 unchanged=78 changed=0 ... inputs_equal=78 name_exists=0` expected; (ii) the count of objects under `amgt/harvest/gold/research_dossier/` (print it; C-8 compares); (iii) the scheduled-task list with its control (`Get-ScheduledTask`): none runs a continuation, dossier or fund-form build in the window; (iv) the BEFORE gateway reads of `UNH_US_Equity` and `CPA_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned `continuation_fields` and `dossier_fields` entry, `continuation_key`, `dossier_key`, `source_keys`, `content_sha256`, `as_of` and `research_reports[]` entry. DO NOT call `etfs_compare_peers`; DO NOT run any module's `--write`.
1. **Write the driver** `ch7_run.py` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/`: takes one or more names from the list as arguments (a name not in the list is a STOP); for each name, in the order given: (1) builds in memory and compares `fields` with the gateway-served continuation's `fields` (STOP before that name's write on any difference); (2) calls `continuation.write_one(security_key)`; (3) reads the object back and checks Branch A of the COO half; (4) appends the manifest line to `ch7_written.out` and flushes it BEFORE the next name. It has a plan mode that refuses a write outside GO to GO+120 minutes. NO loop over the list, NO retry, NO background mode.
2. **Canary:** `python -u ch7_run.py UNH_US_Equity` then `python -u ch7_run.py CPA_US_Equity`, each its own foreground command; then the gateway reads of step 0 (iv) again, as `ch7_canary.out`: every returned entry, `content_sha256`, `as_of`, `dossier_key` and report entry equal to the before read; `continuation_key` and `source_keys` differ ONLY by naming the new `/5` object (EXPECTED). Anything else: STOP.
3. **The other 76:** in sorted order, at most 10 names per foreground command (`python -u ch7_run.py <10 names>`), a batch stopping at its first anomaly; append each command's output to `ch7_run.log`. Between batches print the running count of manifest lines.
4. **After (`ch7_after.out`):** (i) `deliverables/0.9.0_WK_AMGT_HARVST~165/ch1_census.py` re-run unchanged (read only): `with_current=95 no_current=0 new_differs_from_gateway=0` expected; (ii) the dossier object count equals step 0 (ii); (iii) the manifest holds 78 lines and the stored continuation count is the start count plus 78.
5. **Write `ch7_served.out`** ending with exactly these lines: `CONTINUATIONS_WRITTEN_AND_READ_BACK=PASS|FAIL` (manifest 78 lines, every read-back equal), `CANARY_GATEWAY_EQUAL_EXCEPT_POINTERS=PASS|FAIL`, `PICKER_CENSUS_ALL_CURRENT=PASS|FAIL`, `DOSSIER_COUNT_UNCHANGED=PASS|FAIL`. In the ledger close say: the standing instruction against continuation rebuilds is lifted for these 78 names by the CTO's msg 7903; dossiers are not rebuilt.
6. Commit the ledger close WITH the manifest. Tell the issuer when the canary is written (before the 76), when the last name is written and read back, and when `ch7_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing further, file one row and tell me:** the worktree is not at `091ebacda9` or the list sha256 differs; step 0 (i) does not read `names=78 changed=0`; a scheduled task runs a continuation, dossier or fund-form build in the window; a site Z write to the prefix is in flight; a name not in the list; the pre-write comparison differs for a name; AccessDenied, `GoldImmutableError` or a throttle (print its exact text); `put_performed` false; a read-back that differs; an object count that is not +1 for the name; a missing or late manifest line; the canary gateway read differs from the before read in anything but `continuation_key` and `source_keys`.
- **After the last write, a difference not named here:** write it plainly (what differs, how, the read that shows it), do NOT self-grade the criterion, finish the remaining READ-ONLY steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted. A written object is repaired by a still newer `/5` object decided by the issuer and the CTO, never by deletion.
- **Expected and NOT a failure:** the gateway `continuation_key` and `source_keys` name the new object after the write; a name whose key has a slash (`BP/_LN_Equity`, `NG/_LN_Equity`) lands under its slash-encoded partition (a SEAT READ of the partition is the check; see row `AMGT_HARVST-D1-W168-S2`); the stored dossiers still cite the OLD continuation keys; `name_exists=0` before the write.
- **Window:** from my GO to 120 minutes later; if the 78th name has not landed by then, stop and tell me. Do not exceed the window to finish.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-ch7-continuations-m5.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ch-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch7_served.out</invocation><expect>(?m)^CONTINUATIONS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ch-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch7_served.out</invocation><expect>(?m)^CANARY_GATEWAY_EQUAL_EXCEPT_POINTERS=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ch-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch7_served.out</invocation><expect>(?m)^PICKER_CENSUS_ALL_CURRENT=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-ch-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch7_served.out</invocation><expect>(?m)^DOSSIER_COUNT_UNCHANGED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that no dossier was written (the pair's C-6); AC2 is the proof that nothing served moves but the pointers (the pair's central claim); AC3 is the proof every name now resolves to a current continuation.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-ch-7.78-continuations-of-method-5-are-written.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-ch-7.78-continuations-of-method-5-are-written` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ch-7.78-continuations-of-method-5-are-written.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
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
- **STAGED, not sent.** It waits on site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`, C-10) and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-92 analysis item 4, his scope ruling (msg 7903) and his signed half (`5d4e716fd1`, msg 7909). Decomposition section 123d (cell DEFINED) and 123e (cut).
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; no ask that needs an answer inside the window; I check SC1's READ ack within 10 minutes of the handing and type a nudge if there is none.
- **The CTO's correction applied:** the worktree is AT `091ebacda9` exactly, `git rev-parse HEAD` printed (his condition 1); the COO half's "or a later commit" limb is not usable at today's HEAD.
- **Window set by me:** GO to GO+120 minutes (78 writes with read-backs, two gateway reads and a census of 1,215 requests); the pair left the length to the order.
- **Own workstream** `CONT-M5`.
- **Not covered, named:** any dossier rebuild; the 17 names already at `/5`; the `substrate.py` line 158 fallback.

**COMPLETE 2026-10-18T05:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** seat `0.7.0_AE_CloudOps~SC1`, GO 05:02Z (site Z CLEAR for 05:00Z-07:30Z, msg 7913): canary UNH `b89177eb` and CPA `96cd31de` written 05:09Z and read back, gateway before and after equal but the two pointers; the other 76 in batches of 10; last name 05:15:16Z, inside the window, no STOP; manifest 78 `WROTE` lines; ledger `harvst-ch7-continuations-m5` CLOSED 05:21:55Z, COMMITTED (`1996542f8c`); deliverables `1ef5c34de1`. Pair COO `19d80c8b` + CTO `5d4e716fd1`. SC1 had not read the staged order or the GO until I typed a nudge at 05:01Z (the D1-S51 lapse again); it then read and acted.
- **Read by me (not SC1's word):** `deliverables/2.0.0_SA_COO_W1/round93/ch7_issuer_verify.out`: 95 partitions, 446 objects (368 + 78); all 78 manifest names distinct and equal to the list; each new object is the newest of its partition by the gateway's rule, method `/5`, recomputed `content_sha256` equal, `fields` and `inputs` EQUAL to the previous newest object (56 previous at `/3`, 22 at `/4`, as the census said); `BP/_LN_Equity` and `NG/_LN_Equity` under their slash-encoded partitions; dossier objects 1479, unchanged. **The picker census re-run by me** (`ch7_ch1_census_issuer.out`): `securities=95 with_current=95 no_current=0 new_differs_from_gateway=0`. **A gateway read of a NON-canary name** (`GPN_US_Equity`): `continuation_key` is the manifest key `e03d0e939d3c000b.json`. **Proof instance VALID rc 0 (re-run here).** `ch7_served.out` AC1 to AC4 PASS.
- **Standing instruction (section 122g / CTO round-92 ruling) is LIFTED for these 78 continuations** (CTO msg 7903) and stays in force for DOSSIERS. Every continuation of the 95 now has a current-method object; the picker and the gateway agree for all 95.
- **Not seen:** the gateway was read for 3 names (UNH, CPA by SC1; GPN by me), not for all 78; the other 75 are proven by the bucket (the manifest key is the gateway's newest), not by a served read.


<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>93</round>
<workstream>CONT-M5</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
