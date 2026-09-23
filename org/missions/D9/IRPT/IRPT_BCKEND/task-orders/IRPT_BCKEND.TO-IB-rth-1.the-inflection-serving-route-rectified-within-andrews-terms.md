# TO IRPT_BCKEND.TO-IB-rth-1 -- THE INFLECTION SERVING ROUTE, RECTIFIED WITHIN ANDREW'S TERMS: round 7 proved the performance route resolves in `tenants.py` for all three firms, but inflection's LIVE request returned UNEXPECTED (row W3-S50) -- an S3 404 in `_authz/served.py::enforcer_for`'s eager ownership-map load for inflection, UPSTREAM of `route_for` and outside rtg-3's bound. The blocker is the locked `opal-data-inflection` bucket (FWD-11). This cell closes the LIVE gap within Andrew's own ladder, INVESTIGATION FIRST.

<to_id>IRPT_BCKEND.TO-IB-rth-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete -- 0.7.0_AE_CloudOps~V 2026-09-21 ~16:4xZ: R76-AC1 PASS 5 of 5 BY OUTPUT (graded run 15:43:53Z of this face's invocation as amended, token IBR76-INFLECTION-ROUTE-RESOLVES-LIVE-3-OF-3 printed; inflection, 49financial and cottonwood each HTTP 200 class SERVED live, inflection via its ORION route, UNEXPECTED on 2026-09-20 before the fix); proof instance VALID (proof-of-spec-check rc=0, R76-AC1,R76-AC2 coverage) @d4da0d7204. Arm (d) graded 6 of 6 per RULING 99069 (irpt-ycharts-generate carried to row S102, row S111); invocation bound 1800->3600 per RULING 99070 (row S112). Build 2c7cff46b0 + apply 23418bd701, both ledgers CLOSED. R76-AC2 (judgment) is 3.0.0_SA_CVO's at L9. PRIOR: RE-ADDRESSED 0.9.0_WK_IRPT_BCKEND~1 -> 0.7.0_AE_CloudOps~V by 2.0.0_SA_COO~B 2026-09-21 ~15:4xZ (msg 99063/99069/99070): the pin-bump remedy (row W1-S48) needed lane access WK~1 did not hold, ~V has executed arms (c)/(d) since (build+apply, 6 of 7 functions, msgs 99070) and is completing arm (e). HANDED originally by 2.0.0_SA_COO~B 2026-09-21 (round 8, the recut on the CTO's round-7 analysis @0d400d5c07). INVESTIGATION FIRST is read-only and safe; any served/bucket change is packet + halves BEFORE the act; the mint-principal and new-bucket branches are STOP-and-carry, never taken ad hoc. === ISSUER ERRATUM (2.0.0_SA_COO~B, round 9, on CVO~B's C-S135 / row W1-S46) -- the original text of this face and of decomp R8.1 is retained under R-43 and NOT rewritten: both name `opal-data-inflection` (the LGIC full-name bucket, FWD-11's program) as the bucket the inflection serving route was blocked on. That conflated two buckets. VERIFIED BY THE ISSUER 2026-09-21: `data/firm_registry.json` firms[inflection].bucket = `opal-data-inf` (the LEGACY bucket; cottonwood = `opal-data-cot`, 49financial = `opal-data-bd`). CARRIED FROM CVO~B, not re-derived: the ownership-map read that failed is on that legacy path (its reading of this order's investigation, sections 1 and 3-5). TIMING agrees: this order's graded run reached inflection HTTP 200 SERVED at 15:43:53Z, and `opal-data-inflection` was not recovered until 17:35:59Z-17:36:39Z (CRO msg 99124). So the fix that landed (`_authz/loaders.py` treats S3 AccessDenied as absent, like NoSuchKey) is INDEPENDENT of recovering `opal-data-inflection`; that recovery and the IaC reconciliation (IB-rth-8) are the separate FWD-11 program. A reader must not infer that recovering `opal-data-inflection` is what made inflection serve. ===</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no round-8 addendum) | **Round-7 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md` @0d400d5c07 | **Decomp cell:** `IB-rth-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.8, s.R8.1) | **outcome_ref:** FWD-2 (serving half) | **row:** W3-S50 (ARMED, disarm_owner 2.0.0_SA_COO~B)

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-1` on branch `wk-irpt_bckend-8-1`, cut from CLOUD HEAD, `.tools/terraform.exe` provisioned; the issuer passes the absolute path at spawn. First act: `cd` there, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`; write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before any apply. Repo root = the worktree; prefix paths with it.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/checkout--/clean. Capture safe-commit output to a file; never `| tail`; never with `$( )`. Verify by `git log`.
- Python `py -3.12`; AWS via `.tools/aws`; a recursive grep/find is rail-DENIED -- use Read/Grep, a gated read in its own call.

## THE CELL
- **(a) INVESTIGATE FIRST -- READ-ONLY, no write of any kind.** Measure, printed with denominators + the verbatim wire result: (i) reproduce the live failure -- inflection's scoped performance request under the bounded principal returns the S3 404 / UNEXPECTED (the round-7 W3-S50 evidence, `_authz/served.py::enforcer_for` reading the ownership map for inflection); (ii) locate WHERE inflection's ownership map is expected (`_authz/served.py` + `_ids`) and whether the object EXISTS (`.tools/aws s3api head-object`), on WHICH bucket (`opal-data-inflection` per FWD-11), and the EXACT wire error (403 AccessDenied vs 404 NoSuchKey vs a Deny) -- via an UNSIGNED request where the class matters (a constructed stub asserts the author's model, not the wire); (iii) THE DISCRIMINATING CALL: can the object be PRODUCED/READ on the EXISTING bucket without the console? -- e.g. `s3api get-bucket-policy`, a scoped `put-object` dry-run or an object-scoped read under an existing role -- the verbatim result, so the branch below is decided on evidence, never assumption.
- **(b) BRANCH ON THE EVIDENCE -- ANDREW-DIRECT 98869 answer 2, HIS TERMS VERBATIM AND NOT WIDENED:** *"Root access is not possible ... Minting a new principal for this matter may be redundant and roundabout but if that is the only way it can be rectified then so be it. If it cannot be done, then we will make new buckets ... I would prefer it is not necessary to do that."*
  - **B1 -- rectify the EXISTING bucket (FIRST choice):** if (a) shows the map can be produced/read on `opal-data-inflection` without the console (e.g. an object-scoped grant the serving role lacks, or the map object simply absent and writable under an existing principal), do the MINIMAL rectification. If it changes a SERVED property or a bucket policy, it is a never-widen act: packet + CTO+COO halves at HEAD BEFORE the act, arm-(d) subtraction gate, ledger opened before, arm-(e) live proof (the rtg-1 shape). If it is an object write the estate's existing producer path already owns, DELTA=0-style, do it under a change-management ledger and prove the read.
  - **B2 -- mint a principal (ONLY if B1 cannot be done):** STOP. File a BLOCKING row with the (a) evidence that rectification is impossible, and carry the mint-principal proposal to `1.0.0_SA_CTO` (spec) with your recommendation; do NOT mint ad hoc.
  - **B3 -- new buckets (LAST resort, he would prefer not):** never initiated by this cell. STOP and carry to `1.0.0_SA_CTO` / Andrew.
  - ⛔ **THE ROOT CONSOLE IS NOT AN OPTION on any branch.** ⛔ **NO cross-firm read**; nothing written to another firm's bucket or prefix.
- **(c) PROVE (arm e), UNDER THE DEPLOYED ROLE + BYTES** (only if B1 landed a change): reuse the bounded-principal battery `../deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` at HEAD (fresh epoch, full lifecycle incl. delete). ACCEPTANCE R76-AC1: inflection's authorized, scope-resolved performance request resolves a TenantRoute end-to-end -- no S3 404, no UNEXPECTED -- AND the other two firms (49financial, cottonwood) STILL resolve (no regression); print route/function/role; 3 of 3 firms live. If the branch is B2/B3 (STOP), R76-AC1 is a truthful DISCLOSED-INCOMPLETE with the carry named -- NOT a flip to complete.

## DELIVERABLE
the investigation result.md with the verbatim wire evidence; IF B1: the rectification (source/grant/object), its never-widen packet + the build/change-management ledger, `battery`/output, the proof instance; IF B2/B3: the BLOCKING row + the carry to the CTO with the discriminating evidence.

## BOUNDS
- INVESTIGATION is read-only. NO mint, NO new bucket, NO root console -- ever. B1's rectification is the ONLY branch this cell may execute, and only if the evidence in (a) supports it, and only as a never-widen act if it touches served/bucket state.
- The forward-looking-criterion bar; R-40 (content hash per run/artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; the identity bar (arm (e) runs the deployed role + bytes); the LEDGER opened before any apply.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never edit this face except the single `<status>` flip; never widen; never fix a neighbouring defect.

<expected_criteria>R76-AC1, R76-AC2</expected_criteria>
<criterion id="R76-AC1" cell_refs="IB-rth-1"><invocation>timeout 3600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rth_1.py</invocation><expect>IBR76-INFLECTION-ROUTE-RESOLVES-LIVE-3-OF-3</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-1.the-inflection-serving-route-rectified-within-andrews-terms.md
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_ids/
infra/aws/terraform/investor-reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.8, cell `IB-rth-1` (s.R8.1).
<owned_cells>IB-rth-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- the IAM/bucket/access reads (get-bucket-policy, object-scoped reads, an unsigned request where the wire class matters) are the WORKER's arm-(a) investigation, not a cut-time comp-iam census; ANY new grant the rectification needs is a MEASURED key in this order's never-widen packet (arm b/c), never assumed at the cut; the mint-principal branch is STOP-and-carry, not a preflight grant.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override. No cross-firm bucket or prefix.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R76-AC1 (inflection resolves a TenantRoute live end-to-end, 3 of 3 firms, no S3 404 / UNEXPECTED), R76-AC2 (judgment, the CVO's at L9 -- whether the rectification is within Andrew's terms, and the FWD-2 serving-half advance). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rth-1.the-inflection-serving-route-rectified-within-andrews-terms.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash per produced/served artifact pinned to its commit; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R76-AC1 PASS-by-output, then flip `<status>` complete. A STOP (B2/B3) leaves the order open with the BLOCKING row + the carry, and is the final report on it.
</proof_of_spec>
