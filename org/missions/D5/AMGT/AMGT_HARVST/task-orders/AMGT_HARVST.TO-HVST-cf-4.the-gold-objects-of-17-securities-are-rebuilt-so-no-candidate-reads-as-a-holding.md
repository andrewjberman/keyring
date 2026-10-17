# AMGT_HARVST task order -- `HVST-cf-4` -- ROUND 91, workstream CS61-REBUILD: THE GOLD CONTINUATION AND DOSSIER OF 17 SECURITIES ARE REBUILT SO NO CANDIDATE READS AS A FUND OF RECORD AND NO DESCRIPTION PARAGRAPH READS AS A POSITION; MNST, THE JP NAMES, UNH AND A CONTROL ARE READ ON THE SERVED TOOL (STAGED behind a signed never-widen pair)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cf-4.the-gold-objects-of-17-securities-are-rebuilt-so-no-candidate-reads-as-a-holding</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cf-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched; the two writers run in foreground commands of this seat, one name at a time.
comp-iam: RUN at L5 -- the writers put objects into `opal-data-harvest` through the principal dell1's existing harvest tooling already holds (`lib/research/harvest/store.py::_default_client`); NO grant, key or policy is created or widened. The BLAST RADIUS is the 17 securities' served `harvest_get_research` answer (the never-widen pair below names it and the add-only rollback).
comp-adversary: RUN at L5 -- the adversary is a rebuild run from a tree that is not the signed one (other seats' unmerged `lib/research` changes at HEAD, or the `fund_form` change that must NOT be in it), a list longer than the signed one, a build that still serves a fund of record from a candidate line because the branch check was skipped, a detached process that dies silently with its buffer (row `D1-S44`), a half pair, and a served read answered from a cache.
</preflight>

## 0. THE CELL

The CTO's analysis (`ledger/ROUND_ANALYSIS.round90.md` @307764abfe) graduated `C-S61`: the gateway serves `fund_of_record` `PFOE` for names whose only line is `CANDIDATE FOR PFOE`. `HVST-cf-1` counted it over all 94 names; `HVST-cf-2` (merged `80d0701876`) makes `fund_of_record` come only from a line that states a holding and a description paragraph never a position, and its census (`deliverables/0.9.0_WK_AMGT_HARVST~160/cf2_census.out`) names the 17 securities whose served value changes. The objects are immutable: this cell writes NEWER objects (continuation method `amgt-corpus-continuation/5`). The CTO's close condition: **MNST served with no PFOE `fund_of_record`, UNH unchanged, and a control; the four JP names' served read in the proof (msg 7735).**

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cf-2` is `<status>complete</status>` and merged on `box/dell1` (`80d0701876`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round91/NEVER_WIDEN_HALF_COO_CF4_GOLD_REBUILD_C_S61.md` (sha256 `275d5739cb747a2be93c5ad32bb06bc83530f3028bb60199167c100c719695b0`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CF4_GOLD_REBUILD_C_S61_CTO_HALF.md`. Read both before you start; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A change-management ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cf4-gold-rebuild-20261017.json`).

## 2. THE ACT (dell1)

0. **Before-state, read only (`cf4_before.out`):** (i) cut a worktree of your own at commit `80d0701876` (`git worktree add <path> 80d0701876`; sparse is enough: `lib`, `integrations/bloomberg/research`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`) and run every builder and writer FROM IT; print `git diff 80d0701876 HEAD --stat -- lib/research` of the main tree (informational); (ii) print `sha256sum` of `deliverables/2.0.0_SA_COO_W1/round91/cf4_securities.txt` and compare it with the signed `221a63c311c9d0f13baeff2a346169b62f27cec7d32c33270ba1b2e1ac58ee48`; a difference: STOP; the 17 names in the file are the ONLY names you write; (iii) THE CONTROL AND UNH BEFORE: read `harvest_get_research` for `CPA_US_Equity` and `UNH_US_Equity` through the gateway as an Opal principal with `fields` `["fund_of_record","last_stated_position"]` and print the entries, `content_sha256`, `as_of` and `source_keys`; run `continuation.build("UNH_US_Equity")` in memory from the pinned tree and print its two fields (they equal the served ones: fund `PFOE`, position `Maintain positions in PFOE and DIVZ`, `line_only` true, no `stance`); (iv) read `MNST_US_Equity` and `8306_JP_Equity` served BEFORE and print their two fields. DO NOT call `etfs_compare_peers`.
1. **Canary: `MNST_US_Equity` then `8306_JP_Equity`.** For each, as a separate FOREGROUND command (`python -u`, output appended to `cf4_run.log`): (a) `continuation.build(security_key)` (writes nothing): print the two fields; compare with the name's `CHANGED` line in `cf2_census.out` (`fund_after`, `position_after` first 60 characters, `stance_after`); MNST: `fund_of_record` absent, position `CANDIDATE FOR PFOE`, stance `candidate`; `8306_JP_Equity`: `last_stated_position` absent; a difference (Branch B): STOP, write nothing; (b) `continuation.write_one(security_key)`; (c) `dossier.build(security_key)` in memory (it reads the NEW continuation) and print the two fields; (d) `dossier.write_one(security_key)`; record every put in `cf4_written.out` (C-3). Then read both served into `cf4_canary.out`. Canary FAIL: STOP and tell the issuer.
2. **The other 15, serially, in file order,** each name a separate foreground command with 1(a) to 1(d) and the branch check of the COO half; after each name read `cf4_written.out` and confirm BOTH keys of that name are there before starting the next (C-5); a gap, an error or a silent command is a STOP with the exact text; no retry loop; no grant request.
3. **Served reads after all 17 (`cf4_served.out`):** `UNH_US_Equity` and `CPA_US_Equity` (equal to the step-0 reading), `MNST_US_Equity`, the four JP names, and the first, a middle and the last name of the sorted file other than the canaries: verbatim fields, `as_of`, `source_keys`.
4. Write `cf4_served.out` ending with exactly these lines: `SERVED_CANARY=PASS|FAIL`, `SERVED_UNH_AND_CONTROL_UNCHANGED=PASS|FAIL`, `WRITTEN continuation=<n> dossier=<n>` (17 and 17 when complete). A FAIL is reported with the read; nothing is deleted by you.
5. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the canary has been read served, and again when `cf4_served.out` is written.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cf4-gold-rebuild-20261017.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cf-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/cf4_served.out</invocation><expect>(?m)^SERVED_CANARY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cf-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/cf4_served.out</invocation><expect>(?m)^SERVED_UNH_AND_CONTROL_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cf-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/cf4_served.out</invocation><expect>(?m)^WRITTEN continuation=17 dossier=17$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cf-4.the-gold-objects-of-17-securities-are-rebuilt-so-no-candidate-reads-as-a-holding.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cf-4.the-gold-objects-of-17-securities-are-rebuilt-so-no-candidate-reads-as-a-holding` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cf-4.the-gold-objects-of-17-securities-are-rebuilt-so-no-candidate-reads-as-a-holding.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long write run (CTO round-90 item 3, row `D1-S44`):** every name a separate FOREGROUND command, unbuffered, logged; no `nohup`, no detached or background process; the manifest checked after each name.
- Do not edit this order file: the issuer flips its status.
- `HVST-cc-5`'s hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST. (This order writes the harvest bucket `opal-data-harvest` AMGT objects only; no firm data bucket.)
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: CTO round-90 analysis (msg 7721) item 2 and msg 7735; `HVST-cf-1` (`934ecb88c5`), `HVST-cf-2` (`80d0701876`). **The issuer's error this order corrects:** round 90's `HVST-ce-4` served `fund_of_record` from `CANDIDATE FOR` lines.
- **Sequencing hazard (decomposition 121):** the run is from a worktree at `80d0701876`, which holds NO `fund_form` change; `HVST-cf-3` (the fund_form code) is not merged until this order's rebuild is done, because a changed `fund_form.gather_items` makes every dossier build find no stored fund form.
- **Add-only, named:** gold puts never overwrite; the old objects stay; the rollback is an Andrew-confirmed delete of the manifest keys.
- **Not covered, named:** the `fund_form` rebuild (`HVST-cf-3`, `-5`); the `line_only` text; any gateway release.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>staged</status>
<round>91</round>
<workstream>CS61-REBUILD</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
