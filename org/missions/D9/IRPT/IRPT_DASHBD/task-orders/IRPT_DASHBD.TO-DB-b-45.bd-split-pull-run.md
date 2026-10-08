# TO IRPT_DASHBD.TO-DB-b-45 -- FWD-8: run the split Black Diamond pull ONCE on the laptop (2,299 calls, 4,598 ranges, read-only, new partition), under Andrew's per-use word and dell2's signed pair

<to_id>IRPT_DASHBD.TO-DB-b-45</to_id>
<project>IRPT_DASHBD</project>
<issued_to>2.0.0_SA_COO~D2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2; the act runs on the laptop) | **Ordered by:** laptop 1.0.0_SA_CTO msg 106630,
relayed by 0.0.0_AB_MSTR~DELL2 msg 1145 ("~D2 cuts a task order to a fresh laptop 0.7.0_AE_CloudOps~I; dell2's own pair signs"; "It
reaches the seat as a task order from 2.0.0_SA_COO~D2 on a published branch, with the script's pin"; "The seat reads Andrew's word
@5ef6d33141 itself before step 1; if it does not cover the pull, it does not run") | **Decomp cell:** `DB-b-45` (decomposition section
27) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-44 (merged @35a0fc34d4).

**Risk WORLD:** a vendor call and S3 writes. Pair: `deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PAIR_BD_SPLIT_PULL.md` (COO half signed; the
CTO half by 1.0.0_SA_CTO~DELL2). The GO is the laptop CTO's, on both halves signed.

---

## WORKER FACE

You are `0.7.0_AE_CloudOps~I` on the laptop. Run everything from the repository root of a checkout of the published dell2 branch the GO
names, at the pin it names (on origin in `q/dell2/seat-work-2240/r2` @eaae449ef2, or later). Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~I/`.

**The act.** ONE read-only Black Diamond pull for IRPT_DASHBD's FWD-8: for each of 2,299 accounts, ONE `performancePeriod` call carrying
two date ranges, the account's closure segment split at 2025-01-09 (start .. 2025-01-08, and 2025-01-10 .. end). The plan is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/SPLIT_PULL_PLAN.json` (2,299 requests, 4,598 ranges, 0 unmapped,
`pull=split20261007`). The runner is `.../0.9.0_WK_IRPT_DASHBD~25/bd_split_pull.py`; it lands each response at its plan key under
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=split20261007/`, and refuses: without `--go`; if the plan
does not re-derive identically; if the plan is not exactly 2,299 requests, 4,598 ranges and 0 unmapped; if anything is already landed
under that prefix; if round 14's ruling differs. Dell2 ran it and aborted before any vendor call (it cannot read
`blackdiamond/49f/session`); this run is the first use of the word.

1. **Read Andrew's word first**:
   `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261007_211xZ_DELL2_GO_WITH_YOUR_REC_TWO_PORTAL_LANDINGS_BD_VENDOR_PULL.md`
   at @5ef6d33141 (`git show 5ef6d33141:<path>`). If it does not cover ONE read-only BD pull of 2,299 accounts, 2,299 calls and 4,598
   date ranges, STOP: run nothing, file a row.
2. **Run once:** `python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/bd_split_pull.py" . run --go`. Do not
   re-run it. It writes `SPLIT_PULL_RUN.json` beside the script.
3. **Sweep at most once**, only if the run ended with FAILED accounts (at most 105, every class transport, 5xx or 429):
   `python ".../bd_split_pull.py" . sweep --go`. It writes `SPLIT_PULL_SWEEP.json`.
4. **Return the record(s) as FILES**, byte-exact, to the issuer through 0.0.0_AB_MSTR, for
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/SPLIT_PULL_RUN.json` (and `SPLIT_PULL_SWEEP.json`). The issuer
   grades the criteria on dell2.

<criterion id="DB27-1-AC1" cell_refs="DB-b-45"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r27/p27_pull_run.py" . DB27-1-AC1</invocation><expect>DB27-1-AC1 PASS</expect></criterion>
`DB27-1-AC1` -- the returned record: not aborted; landed + FAILED close over the plan's 2,299 with FAILED <= 105; no call outside the
plan. Base: FAIL (no record).

<criterion id="DB27-1-AC2" cell_refs="DB-b-45"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r27/p27_pull_run.py" . DB27-1-AC2</invocation><expect>DB27-1-AC2 PASS</expect></criterion>
`DB27-1-AC2` -- S3: the keys under `pull=split20261007` equal the record's landed accounts. Base: FAIL (no record).

<expected_criteria>DB27-1-AC1,DB27-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The plan, the runner and round 14's scripts are run, never edited.
- **Vendor:** ONLY the runner's calls, ONE run and at most ONE sweep. No other Black Diamond call, no other firm, no wider plan.
- **AWS:** the 49F session secret read by the runner's sign-in; S3 writes ONLY under `pull=split20261007/`. No IAM change, no other write.
- **Refusal clause.** A second run, a plan edited to widen it, a write outside the new prefix, a credential, bearer or response body
  written anywhere, or a run without Andrew's word read first is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~I/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/SPLIT_PULL_RUN.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~25/SPLIT_PULL_SWEEP.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-45.bd-split-pull-run.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 27 (round 27, workstream BD), cell `DB-b-45`.
<owned_cells>DB-b-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB27-1-AC1, DB27-1-AC2. Graded by the issuer on dell2 from the returned records; the instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/IRPT_DASHBD.TO-DB-b-45.bd-split-pull-run.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB27-1-AC1,DB27-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the pin you ran at, that Andrew's word was read first, the run's and sweep's denominators, landed and FAILED counts, any
abort, and the returned file sizes.


## AMENDMENT 1 (2026-10-08 ~00:3xZ, issuer 2.0.0_SA_COO~D2, on Andrew-direct ~00:0xZ relayed by 0.0.0_AB_MSTR~DELL2 msg 1163) -- re-pointed to dell2

Andrew, verbatim (via laptop 1.0.0_SA_CTO msg 106648): "Why is laptop running any of this, that's the whole point of the dell boxes is to
run the heavy jobs there". Laptop CTO ruling: no new Dell run on a laptop seat; an access refusal is answered by the grant (the secrets
grant widens to every secret a Dell project's code reads by name, at laptop 2.0.0_SA_COO~C). So this order runs ON DELL2, by the issuer,
once `cloudops-dell2-agent-user` can read `blackdiamond/49f/session`. The laptop seat `0.7.0_AE_CloudOps~I` is not used. Steps 1-3 are
unchanged and run from the dell2 repository root; step 4's return is replaced by the record landing beside the script, which the issuer
copies byte-exact to `deliverables/2.0.0_SA_COO~D2/relay/`. The pair (COO @20669fcec6, CTO @5a223f2a26) stands: the act, its blast
radius, its one use of the word and its rollback are unchanged; only the machine moves. Criteria unchanged.
No gate limb graded this modification (LIMB 6 does not fire on a modification; GATE (viii) grades the unchanged `<placeholders>NONE</placeholders>`).

---

## RECORD FACE

<preflight>
comp-blast: DECLARED -- the blast radius is the pair's: Black Diamond reads (2,299 calls + bounded retries + one sweep) and new keys under one new BD bronze prefix; nothing existing is written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no IAM change; the laptop seat's existing grant reads the 49F session secret. Adding the secret to the Dell grant is a separate cell at laptop 2.0.0_SA_COO~C (msg 1145).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a one-off run under a per-use word; no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB27-1-AC1 and AC2 base FAIL (no record), dry-run at base c5e3b46a7b 2026-10-07 ~23:5xZ.
lane: the <paths> block IS the grant. Authority: Andrew's per-use word @5ef6d33141 (MSTR msg 1103); pair: NEVER_WIDEN_PAIR_BD_SPLIT_PULL.md.
</preflight>
