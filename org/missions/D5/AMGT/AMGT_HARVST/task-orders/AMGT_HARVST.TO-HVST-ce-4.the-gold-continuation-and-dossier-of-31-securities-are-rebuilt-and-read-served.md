# AMGT_HARVST task order -- `HVST-ce-4` -- ROUND 90, workstream S43-REBUILD: THE GOLD CONTINUATION AND DOSSIER OBJECTS OF 31 SECURITIES ARE REBUILT AND READ ON THE SERVED TOOL (UNH shows fund PFOE; KMB cites neither Mexico report; a control name is unchanged) (STAGED behind a signed never-widen pair)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-4.the-gold-continuation-and-dossier-of-31-securities-are-rebuilt-and-read-served</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched; the two writers run in a foreground session of this seat, once.
comp-iam: RUN at L5 -- the writers put objects into `opal-data-harvest` through the principal dell1's existing harvest tooling already holds (`lib/research/harvest/store.py::_default_client`); NO grant, key or policy is created or widened. The BLAST RADIUS is the 31 securities' served `harvest_get_research` answer (the never-widen pair below names it and the add-only rollback).
comp-adversary: RUN at L5 -- the adversary is a rebuild run from a tree that is not the merged one (other seats' unmerged `lib/research` changes at HEAD), a list longer than the signed one, a build that still cites a Mexico report written because the scan was skipped, a served read answered from a cache, a half-written pair (continuation without its dossier), and a control that was never read before the first write.
</preflight>

## 0. THE CELL

`HVST-ce-2` (merged `344ea6a5fc`) makes the continuation derivation read a pdf `Recommendation: <content>` line as a FALLBACK (continuation method `amgt-corpus-continuation/4`), and `HVST-ce-6` (merged `87b542aed4`) makes the library read no report on the misfiled list. Neither changes a stored object: the gold objects are rebuilt by running the writers. The census of `HVST-ce-2` (`deliverables/0.9.0_WK_AMGT_HARVST~156/ce2_census.out`, 94 of 94 securities) names 30 securities whose `fund_of_record` and `last_stated_position` go from ABSENT to a value (UNH: fund `PFOE`, `Maintain positions in PFOE and DIVZ`) and no value-to-value change; `KMB_US_Equity` is the thirty-first (its dossier must stop citing `fbd50086c4065785` and `1a3b56044db679a5`). This cell rebuilds those 31 and reads them served. The CTO's close condition: **the live gateway read of UNH shows fund PFOE plus a control name unchanged; the KMB dossier graded on the live read.**

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ce-2` and `HVST-ce-6` are `<status>complete</status>` and merged on `box/dell1` (`344ea6a5fc`, `87b542aed4`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round90/NEVER_WIDEN_HALF_COO_CE4_GOLD_REBUILD.md` (sha256 `5b486cda583f96ac546085975496b1f0675b1d7ebb4f9e73a1ff1df2223c6149`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CE4_GOLD_REBUILD_CTO_HALF.md`. Read both before you start; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A change-management ledger entry is open at the start and closed at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-ce4-gold-rebuild-20261017.json`); it names the bucket and the two object families and holds the manifest `ce4_written.out`.

## 2. THE ACT (dell1)

0. **Before-state, read only (`ce4_before.out`):** (i) cut a worktree of your own at commit `344ea6a5fc` (`git worktree add <path> 344ea6a5fc`; sparse is enough: `lib`, `integrations/bloomberg/research`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`) and run every builder and writer FROM IT; print `git diff 344ea6a5fc HEAD --stat -- lib/research` of the main tree (informational: if it lists changes, you run from your worktree anyway); (ii) print `sha256sum` of `deliverables/2.0.0_SA_COO_W1/round90/ce4_securities.txt` and compare it with the signed value `7881772da6e204818fd50a02050cc7456b7de5a6d0912b6d663817f12930c67b`; a difference: STOP; the 31 names in the file, in file order, are the ONLY names you write; (iii) THE CONTROL BEFORE: read `harvest_get_research("CPA_US_Equity")` through the gateway as an Opal principal and print its `fund_of_record` and `last_stated_position` entries, `as_of` and `source_keys` (CPA is not rebuilt; it must read the same after); (iv) read UNH and KMB served BEFORE and print `fund_of_record`, `last_stated_position` (or the absent reason) and, for KMB, `misfiled_fields_excluded` and the count of strings in the response that contain either Mexico id.
1. **Canary: `UNH_US_Equity` then `KMB_US_Equity`, serially.** For each, in this order: (a) `continuation.build(security_key)` (writes nothing): print `fund_of_record` and `last_stated_position`; for UNH they must be `PFOE` and `Maintain positions in PFOE and DIVZ` with `line_only` true (a different outcome: STOP, write nothing, tell the issuer); for KMB, both branches of the COO half are valid; scan the built JSON text for `fbd50086c4065785` and `1a3b56044db679a5` and print both counts (must be 0 each, else STOP); (b) `continuation.write_one(security_key)`; (c) `dossier.build(security_key)` (in memory; it reads the NEW continuation): scan its JSON the same way for KMB (counts 0), print for UNH the two fields; (d) `dossier.write_one(security_key)`. Record every put in `ce4_written.out` (C-3 of the COO half). Then read UNH and KMB SERVED (as in 0 iv) into `ce4_canary.out`: UNH fund `PFOE` and the position text with `line_only` true; KMB: no string with either Mexico id, `misfiled_fields_excluded` as the gateway computes it (the filter may now find nothing to drop). Canary FAIL: STOP and tell the issuer.
2. **The other 29, serially, in file order,** each with 1(a), (b), (c), (d) and the branch check of the COO half: the built `fund_of_record` token and position text must equal the census line of `ce2_census.out` for that name (`CHANGED <name> fund_after=... position_after=...`, the position compared on its first 60 characters); a difference is Branch B of the COO half: STOP before that name's write, write nothing for it, record it, and go on to the next name only after the issuer's word. Any error (`GoldImmutableError`, AccessDenied, a throttle) is a STOP with the exact text; no retry loop; no grant request.
3. **Served reads after all 31 (`ce4_served.out`):** UNH, KMB, the first, a middle and the last name of the sorted list other than UNH/KMB, and the CONTROL `CPA_US_Equity`: verbatim fields, `as_of`, `source_keys`. The control's two fields equal the step-0 reading.
4. Write `ce4_served.out` ending with exactly these lines: `SERVED_CANARY=PASS|FAIL`, `SERVED_SAMPLE_AND_CONTROL=PASS|FAIL`, `WRITTEN continuation=<n> dossier=<n>` (31 and 31 when complete). A FAIL is reported with the read; nothing is deleted by you.
5. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the canary has been read served, and again when `ce4_served.out` is written.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round90/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round90/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-ce4-gold-rebuild-20261017.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round90/ce4_served.out</invocation><expect>(?m)^SERVED_CANARY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round90/ce4_served.out</invocation><expect>(?m)^SERVED_SAMPLE_AND_CONTROL=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ce-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round90/ce4_served.out</invocation><expect>(?m)^WRITTEN continuation=31 dossier=31$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-ce-4.the-gold-continuation-and-dossier-of-31-securities-are-rebuilt-and-read-served.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-ce-4.the-gold-continuation-and-dossier-of-31-securities-are-rebuilt-and-read-served` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-4.the-gold-continuation-and-dossier-of-31-securities-are-rebuilt-and-read-served.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.
- `HVST-cc-5`'s hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST. (This order writes the harvest bucket `opal-data-harvest` AMGT objects only; no firm data bucket.)
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half of the never-widen pair. The receiving seat is `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: CTO round-89 analysis (msg 7642) items 1 and 3; `HVST-ce-1` (`CAUSE=rule_miss`, `REBUILD_ENTRY`, no one-name continuation CLI so the writer is called as a function); `HVST-ce-2` census (30 absent-to-value, 0 value-to-value); `HVST-ce-6`. Close conditions: UNH served with fund PFOE and a control unchanged; KMB's dossier cites neither Mexico report.
- **Why the dossier build comes after the continuation write:** `dossier.build` reads the stored continuation through `substrate.substrate` (newest object), so a dossier built before the continuation is written would carry the OLD continuation; the dossier's no-op rule (`write_one` writes nothing when the fresh inputs equal the stored ones) is therefore not triggered once the continuation is new.
- **Add-only, named:** gold puts never overwrite; the old objects stay; the rollback is an Andrew-confirmed delete of the new keys listed in `ce4_written.out`. The other 63 securities of the 94 (the census lists 30 and KMB is the thirty-first) are not touched.
- **Not covered, named:** the corpus-wide `fund_form` object (`D1-W158-S2`); a rebuild of securities outside the signed list; the `line_only` text cut at a line break.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>staged</status>
<round>90</round>
<workstream>S43-REBUILD</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
