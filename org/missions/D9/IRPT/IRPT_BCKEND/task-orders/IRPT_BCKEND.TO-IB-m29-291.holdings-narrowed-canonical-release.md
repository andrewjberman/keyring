# TO IRPT_BCKEND.TO-IB-m29-291 -- the narrowed Holdings class release: canonical first, a declared bd-securities fallback

<to_id>IRPT_BCKEND.TO-IB-m29-291</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~93</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-291`
(`decompositions/IRPT_BCKEND_DECOMP_R29_M.md`) | **outcome_ref:** FWD-5 (Holdings classes) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-291`. Andrew, ~05:0xZ: "PHYS is Commodities / Metals but it continues displaying in Alternatives." 1.0.0_SA_CTO
RULING 103169 admits a NARROWED release: the IR Holdings producer reads class and sub-asset from `etf-classifications`
for the tickers the table holds, with bd-securities as the fallback. The full canonical chain (IB-mr-251..272) stays
held because it would unclassify hundreds of securities.

A second reason this cell is urgent: CLOUD's investor_reporting suite is BROKEN (30 failed, 16 errors). The Holdings
producer `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`canonical_classifier` ~:828,
`_classifier_basis` ~:842, `classify_security` ~:857, and ~:919) reads the private `_ticker_map` / `_name_map` of the
BD library `data/black_diamond/scripts/gold/lib/etf_classifier.py`. MDPF_SECCLASS's thread moved that library to the
canonical table and removed those maps. The library's pre-change version is at `git show
1f327f52a2:data/black_diamond/scripts/gold/lib/etf_classifier.py`.

**The CTO's conditions (each a stop):**
1. The fallback is a DECLARED FWD-6 exception: owner `2.0.0_SA_COO~M`, the reason (the canonical table does not yet
   cover every held security), and the sunset (when MDPF_SECCLASS E8 and E9 land), written in the module's header and
   in the half.
2. A pre-release census lists every class-changing ticker with its weight, and the count moving to unclassified reads
   0 with its denominator.
3. This act has its own new halves, separate from IB-mr-251..272.
4. In the census, PHYS, GLD and VXX read from the TABLE.

**Build (LOCAL build + record: no upload, no mint, no deploy, no IAM apply):**
1. **The declared fallback.** Create `data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py` holding
   the pre-change library logic VERBATIM from `git show 1f327f52a2:data/black_diamond/scripts/gold/lib/etf_classifier.py`.
   Rename nothing that callers need. Its header is the FWD-6 declaration of condition 1. It only reads
   `bd-securities`, never writes it, and is used only as Holdings' fallback.
2. **Canonical first.** In `holdings_snapshot.py`, the classifier loads the one client
   `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` from its home (do not copy it), plus the
   fallback module. It stops importing the BD library.
   - **A ticker the table holds:** its `asset_class` and `sub_asset_class` are served exactly as the row holds them,
     with no fold, `asset_class_basis` `CANONICAL` and a class source of `etf-classifications`.
   - **Every other security** (no row, or no ticker): classified by the fallback exactly as today, with the same
     bases, the same refusals and the cash rule (CTO 101547) unchanged, and a class source of `bd-securities-fallback`.
   - **The served value set:** `unclassified` is served only where today's code also serves it. Every class the
     canonical branch can return must be in `ASSET_CLASS_VALUES`.
3. **Closure.** In `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE`, the fallback module and the one client (and
   anything it imports at load) replace the BD library. Re-trace the closure with a real build.
4. **IAM (desired, not applied).** In `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`, add
   `dynamodb:GetItem` and `dynamodb:Query` on `etf-classifications` and its index ARNs for the Holdings firm principals.
   Run `terraform fmt` and `terraform validate` only.
5. **Tests** in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py`:
   - a canonical row wins: PHYS reads commodities/Metals from the table even where the fallback would say
     alternatives/Gold;
   - a ticker the table lacks gets the fallback's class;
   - a security the fallback classifies never becomes unclassified;
   - the cash line is unchanged.
   The WHOLE investor_reporting suite must pass. Repair tests that stubbed the removed library by stubbing the one
   client and the fallback instead. No assertion is weakened.
6. **Census.** Run REAL local Holdings builds at all three firms against the LIVE table (read `table_rows_at_build`)
   and TODAY's served snapshots. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_NARROWED_CENSUS_20260930.json`
   as `{"table_rows_at_build", "firms": [{"firm", "as_of", "completed": true, "securities", "refused": 0, "guessed": 0,
   "to_unclassified": 0, "denominator", "moved", "moves": [{"symbol", "before", "after", "weight"}], "fallback",
   "placed": {"GLD": {"asset_class", "sub_asset_class", "class_source"}, ...}}]}`.
7. **The new half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_NARROWED_RELEASE_20260930.md`
   (`## The act`, `## Blast radius`, `Rollback per key`). It covers:
   - the declared exception;
   - the census, with the largest moves by weight;
   - every reader;
   - the writers counted;
   - both branches;
   - the release order: the IAM apply, then the drain, then the Holdings package re-mint (~M's act), then the served
     after-read of PHYS, GLD and VXX, which ~D shows Andrew.

### ACCEPTANCE

<criterion id="IBM29-291-AC1" cell_refs="IB-mr-291"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_CHECKS/r27_suite_whole.py data/assets/scripts/gold/investor_reporting/tests</invocation><expect>SUITE-WHOLE</expect></criterion>
`IBM29-291-AC1` -- the whole investor_reporting suite passes on the narrowed classifier, with the BD-library dependency
gone.

<criterion id="IBM29-291-AC2" cell_refs="IB-mr-291"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_CHECKS/r29_narrowed_census.py</invocation><expect>NARROWED-CENSUS</expect></criterion>
`IBM29-291-AC2` -- real builds at three firms: zero to unclassified, moves weighted, and PHYS/GLD/VXX from the table.

<criterion id="IBM29-291-AC3" cell_refs="IB-mr-291"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_NARROWED_RELEASE_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`IBM29-291-AC3` -- the new half, for the issuer to sign and send.

<expected_criteria>IBM29-291-AC1,IBM29-291-AC2,IBM29-291-AC3</expected_criteria>

Dry-run at the base 2026-09-30 05:2xZ (@874ab56b33): AC1 SUITE-BROKEN rc=1 (30 failed, 268 passed, 16 errors); AC2
NOT-CENSUSED (census absent); AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No upload, no mint, no deploy, no IAM apply. The BD library is READ only (git show); do not
  edit it. The builds READ the firm buckets, the table and the served snapshots.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W93-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
.tools/safe_deploy_core.py
infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_NARROWED_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_NARROWED_RELEASE_20260930.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R29_M.md</decomp_doc> (round 29, workstream ~M), cell `IB-mr-291`.
<owned_cells>IB-mr-291</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM29-291-AC1, IBM29-291-AC2, IBM29-291-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~93/IRPT_BCKEND.TO-IB-m29-291.holdings-narrowed-canonical-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM29-291-AC1,IBM29-291-AC2,IBM29-291-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the classifier change and the fallback module's declaration, the closure, the IAM diff, the suite line, the
census per firm (securities, moved with the largest by weight, fallback count, to_unclassified with its denominator,
PHYS/GLD/VXX), the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the release rides a Holdings re-mint (explicit act) under the new half.
comp-iam: RUN -- 1 file read (holdings_refresh.tf: a dynamodb:Scan grant per listed table; no etf-classifications read at CLOUD); BLIND: whether the live Holdings principals already read etf-classifications is unmeasured (the half names the apply as release step 1).
comp-adversary: RUN -- 1 suite run at CLOUD (SUITE-BROKEN 30 failed / 16 errors, cause: the BD library's private maps removed by MDPF_SECCLASS SC-t-1 @ae7aa281b0), 1 code read (holdings_snapshot.py :828-919 reads clf._ticker_map/_name_map), 1 ruling read (CTO 103169, four conditions); BLIND: the per-firm moves and fallback counts are unmeasured at the cut (step 6 measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO RULING 103169 (relayed by ~D 103170) on Andrew-direct ~05:0xZ; row MDPF_SECCLASS-S3 (the CLOUD suite break).
