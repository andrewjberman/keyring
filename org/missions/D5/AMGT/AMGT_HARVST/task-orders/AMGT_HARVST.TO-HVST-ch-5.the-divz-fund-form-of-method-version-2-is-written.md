# AMGT_HARVST task order -- `HVST-ch-5` -- ROUND 93, workstream DIVZ-WRITE: THE DIVZ `research-fund-form` OBJECT OF METHOD VERSION 2 IS WRITTEN, WITH 0 REPORTS AND AN ABSENT REASON (STAGED behind a signed never-widen pair and the host owner's notice) (CTO `cf-5` half condition 2; D1-S52 ruling item 2)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ch-5.the-divz-fund-form-of-method-version-2-is-written</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ch-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs `fund_form`, a continuation or a dossier build against the bucket in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; one PutObject under `amgt/harvest/gold/research-fund-form/fund=divz/` is the only write. The BLAST RADIUS is one new gold object, named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree that is not `2e0dc6af2e`'s `lib/research` (a stale form), `fund_form --write` (it attempts all three funds), a driver that writes a different object name than the in-memory build, a retry loop that writes a second object, a dossier or continuation `write_one` run beside this act, a detached process whose buffered output hides a gap (`D1-S44`), and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-ch-4` (merged `2e0dc6af2e`) made `fund_form.build` give a fund no holding report names `reports 0` and an `absent` reason, and `write()` write a form for every fund of the closed set. The stored forms hold no version-2 DIVZ object, so `substrate._pick_stored` for DIVZ returns the stale version-1 object (2 reports, counting candidate and misfiled reports) with `current` False, and `fund_form.read_latest("DIVZ")` raises `LookupError`. This cell writes the ONE missing object. **State plainly in `ch5_before.out`:** nothing served changes (no served tool reads a fund form; no security's `fund_of_record` is DIVZ).

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ch-4` is `<status>complete</status>` and merged (`2e0dc6af2e`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round93/NEVER_WIDEN_HALF_COO_CH5_DIVZ_FORM.md` (sha256 `183efbbf3456e9b3dc2d0d0842be40762384ce6ead8e5efff21473b3f21f7e7a`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CH5_DIVZ_FORM_CTO_HALF.md`. Read both; their conditions C-1 to C-9 bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-ch5-divz-form-v2.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. Work in a worktree of your own at `2e0dc6af2e` (print `git diff 2e0dc6af2e HEAD -- lib/research`: empty).
0. **Before-state, read only (`ch5_before.out`):** (i) build the DIVZ form IN MEMORY (`fund_form.gather_items`, `build_document`, `_inputs_sha16`) in `ch5_build.py` and print `FORM DIVZ reports=<n> object=<name> content_sha256=<hex>`: expected `reports=0 object=a181f84957dbb8b7.json content_sha256=34524f75...`; (ii) list the stored `research-fund-form` objects with `method_version` (expected 11); (iii) the scheduled-task list with its control (`Get-ScheduledTask`, as for `HVST-cg-2`): none runs `fund_form`, a continuation or a dossier build in the window; (iv) the BEFORE state of the picker: `substrate._pick_stored("research-fund-form", "fund=divz", fund_form.current_inputs("DIVZ"), fund_form.METHOD_VERSION, client)` returns the stale version-1 object, `current` False; print its key; (v) the BEFORE gateway read of `UNH_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of`, `source_keys` and the `research_reports[]` entries. DO NOT call `etfs_compare_peers`; DO NOT run `fund_form --write`.
1. **Write the driver** `ch5_run.py` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/` from `ch5_build.py`: gathers, builds the DIVZ document, calls `gold.gold_put("research-fund-form", "fund=divz", "<inputs_sha16>.json", payload)` with the real client, prints a manifest line, then READS THE OBJECT BACK and prints `READBACK fund=DIVZ reports=0 equal=PASS|FAIL`. NO loop, NO retry, NO background mode.
2. **Write once:** `python -u ch5_run.py` in the foreground; append the output to `ch5_run.log`; read the manifest `ch5_written.out` and confirm the object is present and `READBACK ... equal=PASS`.
3. **After (`ch5_after.out`):** (i) `fund_form.read_latest("DIVZ")` returns the new object (print its key and `fields`); (ii) the same `_pick_stored` call as step 0 (iv) returns the NEW object, `current` True; (iii) `python -u -m lib.research.corpus.fund_form --compare` (read only) runs to completion over DIVZ, IDVZ and PFOE (print its output; it raised before); (iv) the same gateway read of `UNH_US_Equity` as step 0 (v), verbatim; every returned field entry, key, `content_sha256`, `source_keys` and `research_reports[]` entry equal to the before read.
4. **Write `ch5_served.out`** ending with exactly these lines: `FORM_WRITTEN_AND_READ_BACK=PASS|FAIL` (the manifest holds `WRITTEN forms=1 reports=0` and the read-back passed), `READ_LATEST_AND_PICK_CURRENT=PASS|FAIL`, `COMPARE_RUNS_OVER_THREE_FUNDS=PASS|FAIL`, `GATEWAY_READS_UNCHANGED=PASS|FAIL`. In the ledger close say: the DIVZ-form part of C-6 is lifted by this close; C-6 stays for every name with no `/5` continuation until `HVST-ch-1` and `HVST-ch-2` are merged and their censuses read 0 differing.
5. Commit the ledger close WITH the manifest. Tell the issuer when the object is written and read back, and when `ch5_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, write nothing, file one row and tell me:** the in-memory build differs from step 0 (i); the stored count is not 11; `lib/research` differs from `2e0dc6af2e`; a scheduled task runs a fund-form, continuation or dossier build in the window; a site Z write to the prefix is in flight; AccessDenied or an `IfNoneMatch` conflict; `put_performed` false.
- **After the write, a difference not named here (a read-back that differs, a gateway read that differs, `--compare` that fails):** write it plainly (what differs, how, the read that shows it), do NOT self-grade the criterion, finish the remaining READ-ONLY steps, close the ledger as written and tell me; I rule. Nothing is retried and nothing is deleted.
- **Expected and NOT a failure:** the gateway `source_keys` and `part` pointers are equal here (no silver write); a `--compare` line for DIVZ reading `reports 0 sections 0`; `read_latest("IDVZ")` and `("PFOE")` returning the version-2 objects of `HVST-cf-5`.
- **Window:** from my GO to 90 minutes later; if the write has not landed by then, stop and tell me.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-ch5-divz-form-v2.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ch-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch5_served.out</invocation><expect>(?m)^FORM_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ch-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch5_served.out</invocation><expect>(?m)^READ_LATEST_AND_PICK_CURRENT=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ch-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch5_served.out</invocation><expect>(?m)^COMPARE_RUNS_OVER_THREE_FUNDS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-ch-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round93/ch5_served.out</invocation><expect>(?m)^GATEWAY_READS_UNCHANGED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that nothing served moves (the pair's central claim); AC3 is the proof the DIVZ hazard is closed (the compare that raised now runs).
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-ch-5.the-divz-fund-form-of-method-version-2-is-written.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-ch-5.the-divz-fund-form-of-method-version-2-is-written` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ch-5.the-divz-fund-form-of-method-version-2-is-written.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
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
- **STAGED, not sent.** It waits on the CTO half of the pair, site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`) and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's `cf-5` half condition 2, his D1-S52 ruling item 2 and round-92 analysis item 1. Decomposition section 123.
- **The CTO's S51 rules (msgs 7871, 7874) are applied:** every stop and expected question is section 3 of the face; no ask that needs an answer inside the window; the issuer checks SC1's READ ack within 10 minutes of the handing and types a nudge if there is none.
- **One object, no canary:** a single put; the read-back is the gate; the expected lessons of `HVST-cf-5` (the substrate pick, the preview comparisons) do not apply (nothing is previewed).
- **AMENDMENT 1 (issuer, 2026-10-18 04:1xZ; CTO half SIGNED @add9119d81, msg 7889, binding the COO half at sha256 `183efbbf3456e9b3dc2d0d0842be40762384ce6ead8e5efff21473b3f21f7e7a` unchanged):** the CTO half is `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CH5_DIVZ_FORM_CTO_HALF.md`; C-1 to C-9 bind you. **The CTO's one correction, now an EXPECTED item of section 3:** no curated tool reads a fund form, but the gateway's `DATA_CATALOG` lists `research-fund-form`, so a catalog read shows ONE MORE DIVZ object after the write: add-only and inside the blast radius, NOT a failure. **C-9, site Z is told first:** the issuer asks `0.0.0_AB_MSTR~DELL1` for the window; you may do step 0 (read only) and write the drivers now, but you write NOTHING until the issuer sends GO with site Z's answer. The window is from the GO to 90 minutes later. Every stop and expected question is section 3 of the face; there is nothing to ask the issuer inside the window.
- **Own workstream** `DIVZ-WRITE`.
- **Not covered, named:** `HVST-ch-1`, `-2`, `-7`; any dossier or continuation rebuild.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>93</round>
<workstream>DIVZ-WRITE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
