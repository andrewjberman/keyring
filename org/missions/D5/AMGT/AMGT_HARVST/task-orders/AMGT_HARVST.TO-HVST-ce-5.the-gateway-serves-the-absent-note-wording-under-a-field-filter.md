# AMGT_HARVST task order -- `HVST-ce-5` -- ROUND 91, workstream S29-WORDING-SERVE: THE OPAL GATEWAY SERVES THE ABSENT-NOTE WORDING UNDER A FIELD FILTER (STAGED behind a signed never-widen pair and the host owner's notice)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-5.the-gateway-serves-the-absent-note-wording-under-a-field-filter</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order.
comp-iam: RUN at L5 -- the deploy path is `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` (S3 tarball, then an SSM pull on the instance); no grant is created or widened. The BLAST RADIUS is the whole `opal-gateway` service (every MCP tool it serves restarts), which the never-widen pair below names with its rollback.
comp-adversary: RUN at L5 -- the adversary is a deploy of a tree that is not the live commit plus the two files (a stale base, or other seats' unreleased gateway changes at HEAD), a served read answered from a cache, a call of `etfs_compare_peers` (site Z row `Z-S375`: it can OOM the 1.8 GB host), and a half-landed deploy (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-ce-3` (merged `b77e08e198`) changes `infra/aws/ec2/opal-gateway/app/harvest_research.py`: with a non-empty `fields` argument, when every requested dossier field cites a misfiled report, `parts_absent.dossier` names only the requested fields it excluded; with no `fields` argument the sentence is unchanged. This cell serves it. **State plainly in `ce5_before.out`:** after `HVST-ce-4` no KMB field cites a listed report, so no live read triggers the new sentence; the offline test proves the sentence, and the live reads prove the release changed nothing else.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ce-3` is `<status>complete</status>` and merged (`b77e08e198`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round91/NEVER_WIDEN_HALF_COO_CE5_GATEWAY_WORDING.md` (sha256 `be0a5ad6d665a4b85972739a11e7535b820315a9e52378135790ca91e993c59f`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CE5_GATEWAY_WORDING_CTO_HALF.md`. Read both; their conditions C-1 to C-9 bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-ce5-gateway-wording-20261017.json`), with the restart window and the before and after tool-name counts.

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. **THE RELEASE IS CUT ON THE LIVE COMMIT, NEVER ON HEAD.**
0. **Before-state, read only (`ce5_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`, the commit the instance runs and `/opt/opal-gateway/.deployed_commit` (if they differ, STOP and file a row; the last report is `efcc8ae19f`, fetch it from `origin/rel-nfra-og-live-efcc8ae19f` if it is not in the store); the MCP tool-name count and `/health`; the previous tarball key. Then the BEFORE reads (C-7 of the COO half): `harvest_get_research` for `KMB_US_Equity` and `CPA_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of` and `source_keys`. DO NOT call `etfs_compare_peers`.
1. **Cut** `rel-amgt-harvst-ce5` from the live commit in a worktree of your own. Print `git show b77e08e198^1:infra/aws/ec2/opal-gateway/app/harvest_research.py` against `git show <live>:infra/aws/ec2/opal-gateway/app/harvest_research.py`: they must be IDENTICAL (md5 `6d9e0dd38166b82943d6834a0ce482b5` read by the issuer at `efcc8ae19f`); a difference means the live file changed: STOP, carry nothing, tell the issuer. Carry ONLY the two files of `HVST-ce-3` from `b77e08e198` (`harvest_research.py`, `tests/test_ce3_parts_absent_wording.py`); `git diff --name-status <live> rel-amgt-harvst-ce5` lists exactly those two paths (print it). Run `tests/test_ce3_parts_absent_wording.py`, `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py` and `tests/test_og_gt4.py` on the release branch (a test file the live base lacks is carried whole).
1b. **C-8, the host owner is told first.** After step 1 and BEFORE the deploy write `ce5_hostowner_note.out` (release commit, the two paths, the intended window start and end UTC, the rollback tarball) and tell the issuer. The issuer sends it to site Z through `0.0.0_AB_MSTR~DELL1` and sends GO. Do not deploy before that GO; an in-flight release on the host in your window is a STOP.
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (any count other than complete: STOP, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF=<the live commit>`, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `ce5_after.out`; they equal the before values (C-6).
3. **The reads after (`ce5_served.out`):** the same two reads of step 0, verbatim; every returned field entry and key equal to the before reads (`content_sha256`, `source_keys` equal).
4. Write `ce5_served.out` ending with exactly these lines: `RELEASE_TWO_PATHS_AND_EQUALITY=PASS|FAIL`, `SERVED_READS_UNCHANGED=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`.
5. **C-9:** right after the deploy tell the issuer the release branch name and commit; the issuer asks `0.0.0_AB_MSTR~DELL1` to push the ref and tells site Z. Record it in `ce5_after.out`.
6. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the deploy has landed and when `ce5_served.out` is written.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-ce5-gateway-wording-20261017.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/ce5_served.out</invocation><expect>(?m)^RELEASE_TWO_PATHS_AND_EQUALITY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/ce5_served.out</invocation><expect>(?m)^SERVED_READS_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ce-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/ce5_served.out</invocation><expect>(?m)^TOOLS_AND_HEALTH_EQUAL=PASS$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-ce-5.the-gateway-serves-the-absent-note-wording-under-a-field-filter.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-ce-5.the-gateway-serves-the-absent-note-wording-under-a-field-filter` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-5.the-gateway-serves-the-absent-note-wording-under-a-field-filter.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** nothing in this order is a long write run; if you start any process that outlives a tool call, start it unbuffered with its stdout and exit status logged to a file, and read that file; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- `HVST-cc-5`'s hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half of the pair. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: CTO round-90 analysis (msg 7721) item 5; `HVST-ce-3` (`b77e08e198`). The issuer's reservation, stated to the CTO in the pair: the wording has no live trigger after `HVST-ce-4`; the release may be batched with any other due gateway change.
- **Sequencing with the data chain:** this order touches the gateway only and does not depend on `HVST-cf-1`, `-2` or `-4`; it may run before or after them (the gold objects are read live, the lib code is not deployed).
- **Not covered, named:** any other gateway change; the corpus-wide `fund_form` rebuild.

**SUPERSEDED 2026-10-17T20:0xZ (issuer `2.0.0_SA_COO~W1`) by the CTO's amended round-90 item 5 (msg 7727):** the CTO did not sign the half and deferred this order: after `HVST-ce-4` no live read triggers the new sentence, so a gateway restart for it alone "is not worth the window". The two files (`harvest_research.py` and `tests/test_ce3_parts_absent_wording.py`, merged `b77e08e198`) ride the NEXT gateway release that is due for a live reason, under that release's own order and never-widen pair with the same controls (the cut on the live commit, the `<merge>^1` equality, C-6 to C-9). No GO was sent; nothing was started by SC1; the COO half (sha256 `be0a5ad6...c59f`) is void. The issuer carries the obligation in decomposition section 121a and in `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md`.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>superseded</status>
<round>91</round>
<workstream>S29-WORDING-SERVE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
