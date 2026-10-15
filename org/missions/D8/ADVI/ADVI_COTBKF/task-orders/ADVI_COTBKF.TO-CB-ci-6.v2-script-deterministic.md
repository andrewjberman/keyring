# TO ADVI_COTBKF.TO-CB-ci-6.v2-script-deterministic -- round 87 CB-ci-6: the V2/V3 build script made deterministic (a total sort key), measured across hash seeds, with the V2 residual against the pin stated

<to_id>ADVI_COTBKF.TO-CB-ci-6</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~169</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-6` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ch-1 (merged @3fce5cc614, status superseded by this cell)

---

## WORKER FACE

### THE CELL

**What is left of CB-ch-1.** You rewrote the lost round-85 build script as `data/assets/scripts/silver/cotbkf_active_set_v2.py` (merged at `3fce5cc614`). It reproduces `REVERSE_MATCH_V3.csv` byte for byte and `ACTIVE_COTTONWOOD_SET_V2.csv` to 41,793 of the pin's 41,826 rows (33 pinned-only, 32 rebuilt-only; ticker the only difference on the paired rows). Your row `ADVI_COTBKF-D1-W169-S4` (established) found that the script's row ORDER depends on `PYTHONHASHSEED`: three runs gave three hashes, because the sort lacks a tie-break; the pinned file orders its 61 tied groups by `held_to` and `window_basis`. A script that gives a different file on each run is not a reproduction of anything. This cell fixes that one defect, proves it across seeds, and states the residual; it does not chase the remaining 33/32 rows.

**Your items.**

1. **One change to the script:** a TOTAL sort key for the window file: `(account_key, source_side, cusip, held_from, held_to, window_basis)` (the candidate your measurement on the pinned ordering supports; if your measurement shows the pinned order needs a different total key, use that and say why in the record). No other behavioural change. Add one test to `data/assets/scripts/silver/tests/test_cotbkf_active_set_v2.py` (added test only, no existing test edited): `test_row_order_is_independent_of_input_order_and_hash_seed`, on stub frames that contain tied groups, shuffled two ways, giving identical output bytes.
2. **Commit the script and the test FIRST.** Then run the build FROM THE COMMIT three times, each with a different `PYTHONHASHSEED` (0, 1 and 2), each writing to its own subfolder under `C:/dev/_cotbkf_rebuild_20261015/seed<k>/` (outside the repository). Compute the sha256 of both CSVs of each run.
3. **Compare** each run's V2 and V3 with the pins (`5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae` for V2, `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f` for V3) and the three runs with each other. If the three are equal to each other, the script is deterministic, whether or not they equal the pin. State the residual against the pin as a multiset diff (rows equal, pinned-only, rebuilt-only, by side/class, counts only; as you did in `REBUILD_RECORD.json`). If V2 now EQUALS the pin, say so; that is the best outcome, and it is not required.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/DETERMINISM_RECORD.json` with exactly these top-level keys: `script_path`, `script_blob` (`git rev-parse HEAD:<script_path>` after your last commit), `sort_key`, `runs` (a list of 3: `{"seed", "v2_sha256", "v3_sha256", "out_dir"}`), `deterministic` (true only if the three V2 hashes are equal AND the three V3 hashes are equal), `v2_equals_pin`, `v3_equals_pin`, `residual` (the multiset diff, counts only, or `null` if V2 equals the pin), `not_established`; and a short `.md`. No account number, name or value in either.

### ACCEPTANCE

<criterion id="CB87ci6-AC1" cell_refs="CB-ci-6"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/DETERMINISM_RECORD.json',encoding='utf-8'));h=[(r['v2_sha256'],r['v3_sha256']) for r in d['runs']];print('V2-DETERMINISM runs=%d distinct_v2=%d distinct_v3=%d deterministic=%s'%(len(h),len(set(x[0] for x in h)),len(set(x[1] for x in h)),d['deterministic']))"</invocation><expect>V2-DETERMINISM runs=3 distinct_v2=1 distinct_v3=1 deterministic=True</expect></criterion>
`CB87ci6-AC1` -- three runs under three hash seeds give one V2 hash and one V3 hash.

<criterion id="CB87ci6-AC2" cell_refs="CB-ci-6"><invocation>python -c "import json,hashlib,os;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/DETERMINISM_RECORD.json',encoding='utf-8'));h=lambda p:hashlib.sha256(open(p,'rb').read()).hexdigest();ok=[h(os.path.join(r['out_dir'],'ACTIVE_COTTONWOOD_SET_V2.csv'))==r['v2_sha256'] and h(os.path.join(r['out_dir'],'REVERSE_MATCH_V3.csv'))==r['v3_sha256'] for r in d['runs']];print('V2-RUN-FILES rehash_match=%s v3_equals_pin=%s v2_equals_pin=%s'%(all(ok) and len(ok)==3,d['v3_equals_pin'],d['v2_equals_pin']))"</invocation><expect>V2-RUN-FILES rehash_match=True v3_equals_pin=True</expect></criterion>
`CB87ci6-AC2` -- the recorded hashes are the hashes of the files on disk now, V3 still equals its pin, and whether V2 equals its pin is printed (either answer passes).

<criterion id="CB87ci6-AC3" cell_refs="CB-ci-6"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/DETERMINISM_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['script_path']]).decode().strip();print('V2-SCRIPT-COMMITTED blob_equal=%s'%(b==d['script_blob']))"</invocation><expect>V2-SCRIPT-COMMITTED blob_equal=True</expect></criterion>
`CB87ci6-AC3` -- the script at HEAD is the script the three runs came from.

<expected_criteria>CB87ci6-AC1,CB87ci6-AC2,CB87ci6-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_rebuild_20261015/` (the `seed0`, `seed1`, `seed2` subfolders, two CSVs each). You change no other file; you do not edit the pinned files, `NONE_REASON_LIST.md`, any other script or test, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of exactly the prefixes `cotbkf_active_set_v2.py` reads (the same ones as in your first run). State each listing's denominator. No write, delete or serve; no other bucket or prefix; not the restricted CRM prefix. Do not run `aws sts get-caller-identity`.
- **Account numbers and values never appear in the repository, a report or a message,** except in the CSVs outside it. Do not look for the account-id scan's pinned set.
- **NEVER** `--apply`, `--remint`, an S3 write or delete, a vendor call. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. A script is never left only in scratch.
- **ONE repair only.** The change in item 1 is the repair. Do not spend further repairs on the 33/32 residual in this cell; state it.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W169-S<k>` (k continues after your S4; `date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool. If the three seeds give different hashes after the total key, that is a finding for a row, not a reason to keep repairing.

<paths>
data/assets/scripts/silver/cotbkf_active_set_v2.py
data/assets/scripts/silver/tests/test_cotbkf_active_set_v2.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-6`.
<owned_cells>CB-ci-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci6-AC1, CB87ci6-AC2, CB87ci6-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~169/ADVI_COTBKF.TO-CB-ci-6.v2-script-deterministic.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci6-AC1,CB87ci6-AC2,CB87ci6-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. Declare the outside CSVs in `declared_exclusions` if the checker refuses them as file artifacts. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three hashes per file across the seeds, and whether V2 now equals the pin. Then: the sort key used and its basis; the residual (counts only); every S3 read with its denominator; the three criterion lines; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of silver and holdings tables and files in a scratch folder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the criterion is determinism across three seeds, not equality to the pin, so the cell cannot be passed by fitting the pin; V3 stays pinned as a control; BLIND: three seeds are a sample (a fourth could still differ if some other ordering source exists); the residual 33/32 rows are stated and not explained.
lane: the <paths> block IS the grant (worker RULING 1). Continues the slot ~169 on the same worktree and branch.
</preflight>

Source: row `ADVI_COTBKF-D1-W169-S4` (established); `ADVI_COTBKF.TO-CB-ch-1` (superseded by this cell); `1.0.0_SA_CTO~DELL1` ruling item 1.
