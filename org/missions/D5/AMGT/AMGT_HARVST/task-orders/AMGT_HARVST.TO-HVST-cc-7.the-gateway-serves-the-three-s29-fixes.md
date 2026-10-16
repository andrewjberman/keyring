# AMGT_HARVST task order -- `HVST-cc-7` -- ROUND 88, workstream S29-SERVE: THE OPAL GATEWAY SERVES THE D1-S29 FIXES AND EACH IS READ ON THE SERVED TOOL (STAGED behind `HVST-cc-1`, `HVST-cc-2` and `HVST-cc-3`)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order.
comp-iam: RUN at L5 -- the deploy path is `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` (S3 tarball, then an SSM pull on the instance); no grant is created or widened. The BLAST RADIUS is the whole `opal-gateway` service (every MCP tool it serves restarts), which the never-widen pair below must name with its rollback.
comp-adversary: RUN at L5 -- the adversary is a deploy of a tree that is not the merged one (a stale base), a served read that passes because the tool answered from a cache, a half-landed deploy (NEVER-2), and a fix declared served on the CRO's names without the CRO's own read.
</preflight>

## 0. THE CELL

`HVST-cc-1` (model figures carry `basis` and `figure_claim`), `HVST-cc-2` (a misfiled research report is excluded and named) and `HVST-cc-3` (a ticker-shaped query that matches no ticker slot never answers `exact` on a name) change `infra/aws/ec2/opal-gateway/app/` (`harvest_figures.py`, `harvest_research.py`, `harvest_identity.py`) and, for cc-2, `lib/research/corpus/typed.py`. The close condition of `D1-S29` (REMEDIATION_v19) is that the surfacing seat reads each defect on the SERVED data. This cell deploys the gateway from the merged tree and reads the three names on the served tools.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cc-1`, `HVST-cc-2` and `HVST-cc-3` are `<status>complete</status>` and merged into the branch the deploy script reads; the merge commit(s) are named in the issuer's send note.
- (b) A never-widen pair for the gateway deploy is SIGNED at the current bytes (COO half and CTO half, `ledger/`), naming the blast radius (the `opal-gateway` service and every tool on it), the rollback per artifact (the previous deployed tarball and its S3 key, read at the start), and the served reads below. The issuer sends the pair's path in the send note. Without it: DO NOT START.
- (c) A deploy ledger entry is open at the start and closed at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cc7-gateway-s29-20261016.json`).

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. Then: (1) record the running version and the previous tarball key in `cc7_before.out`; (2) deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the merged tree with `DEPLOY_BASE_REF` set as that script requires, never a bare `aws` update; (3) wait for the service health check and record it in `cc7_after.out`; (4) the three SERVED reads, each through the gateway tool as an Opal principal, recorded verbatim in `cc7_served.out`:
   - `harvest_resolve_security("PG")` -> status `candidates` (not `exact`); `harvest_resolve_security("PCG")` -> `exact` `PCG_US_Equity`;
   - `harvest_get_fundamentals(security_key="UNH_US_Equity", kind="model", mnemonics=["IS_DIL_EPS_CONT_OPS","IS_EPS"])` -> every `IS_DIL_EPS_CONT_OPS` figure carries a `figure_claim` containing `NOT the reported`, and every figure carries the key `basis`;
   - `harvest_get_research(security_key="KMB_US_Equity")` -> `fbd50086c4065785` is absent from `research_reports` and the response names the exclusion (identity mismatch).
(5) Write `cc7_served.out` ending with exactly these three lines: `SERVED_RESOLVE_PG=PASS|FAIL`, `SERVED_EPS_CLAIM=PASS|FAIL`, `SERVED_KMB_RESEARCH=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`; otherwise it is reported.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cc7-gateway-s29-20261016.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_RESOLVE_PG=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_EPS_CLAIM=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_KMB_RESEARCH=PASS$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the three build cells' merges and on the never-widen pair (start condition b). The receiving seat is `0.7.0_AE_CloudOps~HV1` (the fresh lane seated for this project because `0.7.0_AE_CloudOps~SC1` also holds an `MDPF_SECCLASS` order); it holds `HVST-cc-5` for about 12 hours, so the issuer may seat a second lane for this order at the send (one project per Tier-2 seat instance; a new lane carries only this project).
- Authority: CTO round-87 analysis (msg 6766) rulings for `D1-S29` and ERRATUM 1 (msg 6780); close condition of REMEDIATION_v19 (the surfacing seat reads each on the served data). After `AC1` to `AC3` the issuer asks `4.0.0_SA_CRO~DELL1` (the surfacing seat) to read the three names itself.
- **Not covered, named:** a silver REBUILD for KMB's misfiled report (the cc-2 on-the-fly check serves without it when the stored row carries the header; otherwise a rebuild is owed and is a later cell); adding Procter & Gamble or `KIMBERA MM` to the universe; the `modelSheet.ts` label.
- **SENT:** NOT YET.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>staged</status>
<round>88</round>
<workstream>S29-SERVE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
