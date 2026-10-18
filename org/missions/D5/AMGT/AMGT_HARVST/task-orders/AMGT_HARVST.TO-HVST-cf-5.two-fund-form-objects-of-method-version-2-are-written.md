# AMGT_HARVST task order -- `HVST-cf-5` -- ROUND 92, workstream FUNDFORM-REBUILD: TWO `research-fund-form` OBJECTS OF METHOD VERSION 2 ARE WRITTEN, ONE FOR PFOE AND ONE FOR IDVZ (STAGED behind a signed never-widen pair and the host owner's notice) (row D1-S46; CTO round-91 analysis item 2)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cf-5.two-fund-form-objects-of-method-version-2-are-written</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cf-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that runs `fund_form`, a continuation or a dossier build against the bucket in its window.
comp-iam: RUN at L5 -- the write principal is the one dell1's existing harvest tooling already holds (`lib.research.harvest.store._default_client()`); no grant is created or widened; a PutObject under `amgt/harvest/gold/research-fund-form/` is the only write. The BLAST RADIUS is two new gold objects, named in the never-widen pair with their rollback.
comp-adversary: RUN at L5 -- the adversary is a write from a tree that is not `04be089e13`'s `lib/research` (a stale rule fixed into a gold object), the CLI `--write` that writes both funds in one call (no per-fund read-back), `--compare` (its `read_latest("DIVZ")` raises by design and would be read as a failure), a dossier or continuation `write_one` run beside this act (it would cite the stale version-1 form), a retry loop that writes a second object, a detached process whose buffered output hides a gap (`D1-S44`), and a half-landed write (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cf-3` (merged `04be089e13`) changed `fund_form.py`: a form counts only the reports whose silver row states a holding, and never the misfiled reports; the method version is `2`. The stored forms are version `1` (IDVZ, PFOE, DIVZ). Until version-2 objects exist, `substrate._pick_stored` returns, for a dossier build, the stale version-1 object with `current` False (not an absence: read `substrate.py` lines 121-159). This cell writes the two version-2 objects: PFOE (33 reports) and IDVZ (82 reports). DIVZ has no holding report, so it gets no form. **State plainly in `cf5_before.out`:** nothing served changes (no served tool reads a fund form; the stored dossiers keep citing the version-1 forms until a dossier is rebuilt, which this order does NOT do).

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cf-3` is `<status>complete</status>` and merged (`04be089e13`); `HVST-cg-2` is complete (the silver carries `fund_relation`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CF5_FUND_FORM_V2.md` (sha256 `a7c7f05e961dc30f778d7cb3e9b9444ae4ef54bf4b53f3dded854c46ffad8b6f`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CF5_FUND_FORM_V2_CTO_HALF.md`. Read both; their conditions C-1 to C-9 bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cf5-fund-form-v2-rebuild.json`), with the window and the manifest.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. Work in a worktree of your own at `04be089e13` (print `git diff 04be089e13 HEAD -- lib/research`: empty).
0. **Before-state, read only (`cf5_before.out`):** (i) build both forms IN MEMORY (`fund_form.gather_items`, `distinct_funds`, `_inputs_for_fund`, `build_document`, `_inputs_sha16`) in a script `cf5_build.py` and print, per fund, `FUND <fund> reports=<n> sections=<n> object=<inputs_sha16>.json content_sha256=<hex>`: expected exactly two funds, PFOE 33 and IDVZ 82 (the issuer's census: `reports_after=115`, `absent_after=232`); any other count: STOP and file a row; (ii) list the stored `research-fund-form` objects with `method_version` (expected: version-1 objects for IDVZ, PFOE, DIVZ); (iii) the scheduled-task list: print that no task runs `fund_form`, a continuation or a dossier build in the window (read it with `Get-ScheduledTask` and print the control, as for `HVST-cg-2`); (iv) the substrate view for UNH (fund of record PFOE) and CPA (IDVZ) BEFORE: `substrate._fund_form_member` returns the stale version-1 object with `current` False; print its uri; (v) the BEFORE gateway reads (C-7 of the COO half): `harvest_get_research` for `UNH_US_Equity` and `CPA_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of`, `source_keys` and the `research_reports[]` entries. DO NOT call `etfs_compare_peers`; DO NOT run `fund_form --compare` or `--write`.
1. **Write the driver** `cf5_run.py` in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/` from `cf5_build.py`: `--fund <FUND>` gathers, builds that one fund, calls `gold.gold_put("research-fund-form", "fund=<slug>", "<inputs_sha16>.json", payload)` with the real client, prints a manifest line, then READS THE OBJECT BACK and prints `READBACK fund=<F> reports=<n> equal=PASS|FAIL` (Branch A of the COO half). NO loop, NO retry, NO background mode.
2. **Write, one fund per command, in this order** (C-5): `python -u cf5_run.py --fund PFOE` (the canary, 33 reports), then `python -u cf5_run.py --fund IDVZ` (82). After each: append the output to `cf5_run.log`, read the manifest `cf5_written.out` and confirm the object is present, confirm `READBACK ... equal=PASS`; only then the next. A missing object, a FAIL, `put_performed` false, an error or silence is a STOP with the exact text.
3. **After both:** (i) `fund_form.read_latest("IDVZ")` and `read_latest("PFOE")` return the new objects (print their keys); `read_latest("DIVZ")` raises `LookupError` (EXPECTED; print it); (ii) the substrate view for UNH and CPA AFTER: `_fund_form_member` returns the NEW object with `current` True and `method_version` "2"; (iii) an IN-MEMORY `dossier.build("UNH_US_Equity")` and `dossier.build("CPA_US_Equity")` (NOTHING written) compared field by field with the stored served dossier of each: equal in every field except `fund_form_ref`, which names the new object; print the comparison; (iv) the same gateway reads as step 0 (v), verbatim; every returned field entry, key, `content_sha256` and `research_reports[]` entry equal to the before reads.
4. **Write `cf5_served.out`** ending with exactly these lines: `FORMS_WRITTEN_AND_READ_BACK=PASS|FAIL` (the manifest holds `WRITTEN forms=2 reports=115` and both read-backs passed), `READ_LATEST_AND_SUBSTRATE_CURRENT=PASS|FAIL`, `DOSSIER_PREVIEW_ONLY_FUND_FORM_REF_DIFFERS=PASS|FAIL`, `GATEWAY_READS_UNCHANGED=PASS|FAIL`. A FAIL stays `pending`; the repair is a still NEWER object decided by the issuer and the CTO, never an overwrite and never a delete by you.
5. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the PFOE canary is written and read back, and when `cf5_served.out` is written. Commit the ledger close WITH the manifest.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cf5-fund-form-v2-rebuild.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cf-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cf5_served.out</invocation><expect>(?m)^FORMS_WRITTEN_AND_READ_BACK=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cf-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cf5_served.out</invocation><expect>(?m)^READ_LATEST_AND_SUBSTRATE_CURRENT=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cf-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cf5_served.out</invocation><expect>(?m)^DOSSIER_PREVIEW_ONLY_FUND_FORM_REF_DIFFERS=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cf-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cf5_served.out</invocation><expect>(?m)^GATEWAY_READS_UNCHANGED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the proof that nothing served moves (the pair's central claim), separate from the three that prove the objects and their resolution.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cf-5.two-fund-form-objects-of-method-version-2-are-written.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cf-5.two-fund-form-objects-of-method-version-2-are-written` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cf-5.two-fund-form-objects-of-method-version-2-are-written.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** every command in this order is foreground and unbuffered; if you start any process that outlives a tool call, start it unbuffered with its stdout and exit status logged to a file, and read that file; never rely on a buffer.
- **Judgment on a difference is not yours:** where a served read differs in a way the COO half did not name, write it plainly and do not self-grade (as you did for `HVST-cg-2` and `HVST-cg-3`); the issuer rules.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the bucket and prefix are AMGT's own).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half of the pair, site Z's answer (the issuer asks through `0.0.0_AB_MSTR~DELL1`) and the issuer's GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-91 analysis item 2 ("cf-3 then cf-5 ... rebuilt under its own pair; the code lands only together with newly written fund forms"). The correction to the hazard (a stale citation, not an absence) is in the COO half.
- **Why two commands, PFOE first:** `fund_form.write()` writes both funds in one call; two commands bound the first exposure to the 33-report form and put a read-back between the writes (the S44 rule).
- **AMENDMENT 1 (issuer, 2026-10-18 02:2xZ; CTO half SIGNED @78b98db60d, msg 7837, binding the COO half at sha256 `a7c7f05e961dc30f778d7cb3e9b9444ae4ef54bf4b53f3dded854c46ffad8b6f` @87eb5b095d unchanged):** the CTO half is `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CF5_FUND_FORM_V2_CTO_HALF.md`; C-1 to C-9 of the COO half bind you. **The CTO adds one rule that outlives this order (his condition 2):** after this act DIVZ still resolves to the STALE version-1 form (it counts candidate and misfiled reports), so C-6 (no dossier or continuation `write_one`) stays in force for any build that reads DIVZ's form EVEN AFTER your ledger closes; say so in the ledger close. **C-9, site Z is told first:** the issuer asks `0.0.0_AB_MSTR~DELL1` to tell site Z the window (2026-10-18 02:45Z to 04:30Z) and the two fund partitions; you may do step 0 (all read only) and write `cf5_build.py` and `cf5_run.py` now, but you write NOTHING to the bucket until the issuer sends GO with site Z's answer. The ledger close is COMMITTED with the manifest. If the run passes 04:30Z, stop at a fund boundary and tell the issuer. Row `D1-S50` and the DIVZ cell are round-93 rows of the CTO's; not yours.
- **Own workstream** `FUNDFORM-REBUILD`.
- **Not covered, named:** a rebuild of any dossier or continuation (the CTO's call), a DIVZ form, the shared classifier (row `D1-S49`, round 93).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>92</round>
<workstream>FUNDFORM-REBUILD</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
