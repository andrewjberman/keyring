# TO MDPF_SECCLASS.TO-SC-e40 -- round 8 SC-e-40: FWD-4 -- the copy census, with surfaces S22 to S26 in its denominator and a planted-copy control

<to_id>MDPF_SECCLASS.TO-SC-e40</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~28</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-40` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none (slot ~28's first order)

**Issuer note (record, not face):** provision this slot with `.tools/wk-provision.sh provision MDPF_SECCLASS 28 --path <p>
--portal-ref <portal DEV HEAD at the cut>`. The census reads `portal/src`, and a worktree without the portal reads S16, S23
and S24 as absent.

---

## WORKER FACE

### THE CELL

`SC-e-40`. FWD-4: "Anyone can prove there is no second definition of a security's class left anywhere in Opal's code".
ACCEPT: "a check anyone can rerun lists every place in the code that assigns a class to a security outside the one shared
list, and says how many places it looked at; at the end it lists none, and when an old copy is deliberately put back as a
test, the check finds it" (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12, :56-62).

**The instrument does not exist yet. Build it.** R8 called this cell a "re-run" and pointed at task order
`MDPF_SECCLASS.TO-SC-e3` for the instrument's path. TO-SC-e3 is the round-2 BD thread re-census, not the FWD-4 census. No
round built the FWD-4 instrument (round-1 decomposition :50 deferred it; manifest row S14 reads "NEW census instrument ...
unmeasured"). This round builds it, and today's run is its first.

**The one shared list (C-TABLE, PRD :223), which is NOT a copy:** the table `etf-classifications`; the seed source
`infra/aws/lambda/v2_portal/_shared/etf_classification.py`; the seed path
`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py`; and the one client
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`. The shipped copies of `_shared` modules that a
deploy places beside a function are the same list only when byte-equal to the `_shared` source. Report each one with its
byte verdict.

**What counts as a copy** (each hit is one `copies` entry with `path`, `line`, `surface` and `kind`):
- `kind=literal`: a ticker-to-class mapping in code. A dict, object or table literal maps security identifiers to one of
  the class tokens (`cash`, `fixed_income`, `equity`, `structured`, `alternatives`, `commodities`, plus legacy
  `multi_asset`, `other`, `unclassified`, and the human labels such as `Fixed Income`).
- `kind=client-copy`: a file named `etf_classification*.py` or `etf_classifications_dynamodb.py` outside `_shared/` that
  is not byte-equal to its `_shared` source.
- `kind=old-list`: code that reads or writes `bd-securities`.
- `kind=model`: a model classifier that writes a class (the C-VENDOR list, PRD :227).

Tests and fixtures are counted in their own band (`band: test`). They are listed, never silently dropped.

**The denominator.** Print the files scanned. Scan every tracked code file in the repo (`git ls-files`, extensions
`.py .ts .tsx .js .jsx .sh .sql .json`) and in the portal (`git -C portal ls-files src`). The JSON's `surfaces` object holds
every manifest surface whose outcomes name FWD-4: S06, S07, S10, S11, S12, S13, S14, S15, S16 (PRD :322-332). It also holds
the five surfaces the v0.12 addendum added (PRD :556-561), each `{"paths": [...], "scanned": true, "copies": <n>}`:
- S22 `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` (a reader of the old list);
- S23 `portal/src/pages/Attribution/constants/etf-categories.ts` and `portal/src/pages/Attribution/constants/holdings-shared.tsx`;
- S24 `portal/src/lib/tickerRegistry.ts`;
- S25 `data/black_diamond/scripts/classification/resolve_tickers.py`;
- S26 the geography list in the positioning function. The PRD writes `yang-generate-positioning/lambda_function.py:95`, and
  the real path is `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`
  (measured at the cut).

S14 is the instrument itself, with its path. A surface whose file is missing is reported as `scanned: false` with the
reason, never as zero.

**Build:**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/fwd4_copy_census.py`:
   - It reads code only, with no AWS call.
   - It writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD4_CENSUS_20261007.json` with
     `{"denominator_files", "scopes", "surfaces", "copies", "plant"}`.
   - It prints `FWD4-CENSUS denominator_files=<n> copies=<k> literal=<a> client-copy=<b> old-list=<c> model=<d> test=<t>`.
   - It finishes within 120 s.
2. `--plant`, the negative control:
   - Copy the bytes of one real copy the census reports to a NEW path inside a scanned scope, under a name that exists
     nowhere else.
   - Re-run the scan, assert that the planted path is reported with the same `kind`, then delete the plant.
   - Print `FWD4-PLANT found=True planted=<path> kind=<kind> removed=True`, or `found=False ...`.
   - The plant is never committed. Run `git status` after it to confirm.
3. Record the plant result in the JSON's `plant` field.

### ACCEPTANCE

<criterion id="SC8-e40-AC1" cell_refs="SC-e-40"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/fwd4_copy_census.py</invocation><expect>FWD4-CENSUS denominator_files=</expect></criterion>
`SC8-e40-AC1`: the census runs over the whole code corpus and prints its denominator and its copies by kind.

<criterion id="SC8-e40-AC2" cell_refs="SC-e-40"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/fwd4_copy_census.py --plant</invocation><expect>FWD4-PLANT found=True</expect></criterion>
`SC8-e40-AC2`: an old copy put back as a test is found, then removed. This is the planted-copy control.

<criterion id="SC8-e40-AC3" cell_refs="SC-e-40"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_fwd4_census_surfaces_check.py</invocation><expect>FWD4-SURFACES ok=True</expect></criterion>
`SC8-e40-AC3`: the census JSON's denominator holds every FWD-4 manifest surface plus S22-S26, each scanned with its paths
existing, and every copy names its path, line and surface.

<expected_criteria>SC8-e40-AC1,SC8-e40-AC2,SC8-e40-AC3</expected_criteria>

Dry run at the base 2026-10-07 (@1640a0e86e):
- AC1 base: FAIL as expected (instrument absent);
- AC2 base: FAIL as expected (instrument absent);
- AC3 base: FAIL as expected (`FWD4-SURFACES ok=False reason=census-json-absent`). Its required set reads 14 surfaces at
  the base: S06 S07 S10 S11 S12 S13 S14 S15 S16 S22 S23 S24 S25 S26.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under
  `.scratch/`, uncommitted.
- **Read code only.** No edit to any surface the census reports: a copy is reported, never fixed here. No AWS call. No
  vendor or model call.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row (id
  `MDPF_SECCLASS-W28-S<k>`). Do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/fwd4_copy_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD4_CENSUS_20261007.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ everything else named here and never edit it, including `r10_fwd4_census_surfaces_check.py`.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-40`.
<owned_cells>SC-e-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e40-AC1, SC8-e40-AC2, SC8-e40-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~28/MDPF_SECCLASS.TO-SC-e40.fwd4-copy-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e40-AC1,SC8-e40-AC2,SC8-e40-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the denominator, copies by kind and by surface, the shipped `_shared` copies' byte verdicts, the plant line,
commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code-only census; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- cell-specific reads at the cut: TO-SC-e3 (the round-2 thread re-census, not the FWD-4 instrument; R8's pointer is wrong), comp-find for an existing FWD-4 instrument over the decompositions, MDPF_SECCLASS_M, the CTO deliverables and .tools (none; R1 decomp :50 deferred it), PRD manifest S06-S16 and addendum S21-S26, path probes for S22-S26 (S26's PRD path is short; real path measured). BLIND: portal/ is empty in an unprovisioned worktree (issuer note above).
lane: the <paths> block IS the grant.
</preflight>

Source: DECOMP_R8 @495efa3c32 cell SC-e-40; PRD v0.12 @87ad6d2e4c FWD-4, C-TABLE, C-VENDOR, manifest, addendum S21-S26.
