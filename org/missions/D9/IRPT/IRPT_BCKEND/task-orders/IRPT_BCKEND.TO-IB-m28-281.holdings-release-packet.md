# TO IRPT_BCKEND.TO-IB-m28-281 -- the Holdings release packet: post-backfill census and one release half for 251-272

<to_id>IRPT_BCKEND.TO-IB-m28-281</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~84</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-281`
(`decompositions/IRPT_BCKEND_DECOMP_R28_M.md`) | **outcome_ref:** FWD-5 (Holdings) | **depends_on:** IB-mr-272

---

## WORKER FACE

### THE CELL

`IB-mr-281`. Your slot's chain IB-mr-251 -> 261 -> 271 -> 272 is complete on branch wk-IRPT_BCKEND-84 and was HELD
from CLOUD until the MDPF_SECCLASS backfill wrote. It has now written: ledger mdpf-secclass-backfill-20260930 CLOSED
@f13cddd058. `etf-classifications` holds 2,309 rows (1,934 new `classified_by = scheduled` rows seeded from bd-securities
values on Andrew's word; no existing row changed; GLD, PHYS and VXX are seed rows). The chain's two halves, HOLDINGS_ETF_CLASSIFICATIONS
(251) and HOLDINGS_AGGREGATES (261), were measured before the backfill, and 251's before 271 turned its refusal
into unclassified-by-name. This order re-measures the whole chain and writes ONE release half for it.

**Build (LOCAL build + record -- no upload, no mint, no deploy, no IAM apply):**
1. **Census.** Run REAL local Holdings builds at all three firms on your branch HEAD, reading the LIVE table. Read its
   row count at build time. Compare each firm's built classes against TODAY's SERVED Holdings snapshot for that firm
   (the latest published document under its platinum holdings index). Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R28_RELEASE_CENSUS_20260930.json` as
   `{"table_rows_at_build", "firms": [{"firm", "as_of", "completed": true, "securities", "refused": 0, "guessed": 0,
   "moved", "moves": [{"symbol", "before": {"asset_class", "sub_asset"}, "after": {...}, "weight"}], "unclassified",
   "unclassified_names": [...], "placed": {"GLD": [class, sub], ...}, "aggregates_valid": true}]}`.
   `moved` counts securities whose served class changes. Name the served object's key and version.
2. **One release half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_CANONICAL_RELEASE_20260930.md`
   (`## The act`, `## Blast radius`, `Rollback per key`), covering 251+261+271+272 together. It covers:
   - per firm, the moved securities and their weight, and the unclassified ones, from step 1;
   - every reader: the portal Holdings allocation bars, treemap, security list and the new aggregate rows, exports, the
     holdings Lambda and its contract copy, and Positioning where it shares the table;
   - the writers of each served class property, counted and printed;
   - both branches: a security whose class moves, and one that stays;
   - the release order, in this sequence, each step its own act:
     - (1) the IAM apply, GetItem/Query on etf-classifications for the Holdings firm principals (the grant 251 drafted
       in `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`; AE lane);
     - (2) the drain of wk-IRPT_BCKEND-84 to CLOUD;
     - (3) the Holdings package re-mint and the directory bundle at MSTR's push;
     - (4) the holdings Lambda redeploy with the contract 272 re-staged;
     - all of them AFTER IB-mr-222 Part 2 reads the 2026-09-30 14:15Z scheduled fire;
   - rollback per key: the prior package object versions and the prior served document versions.
   The two older halves are superseded by this one. Say so at the top, and leave them unedited.

### ACCEPTANCE

<criterion id="IBM28-281-AC1" cell_refs="IB-mr-281"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R28_CHECKS/r28_release_census.py</invocation><expect>RELEASE-CENSUS</expect></criterion>
`IBM28-281-AC1` -- a post-backfill real-build census at three firms: complete, nothing refused or guessed, moves and
unclassified listed.

<criterion id="IBM28-281-AC2" cell_refs="IB-mr-281"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_CANONICAL_RELEASE_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`IBM28-281-AC2` -- the release half for the chain, for the issuer to sign and send.

<expected_criteria>IBM28-281-AC1,IBM28-281-AC2</expected_criteria>

Dry-run at the base 2026-09-30 02:3xZ (@f13cddd058): AC1 NOT-CENSUSED (census absent), AC2 NOT-READY (half absent) --
FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no deploy, no IAM apply. Do NOT merge CLOUD into the branch. The
  builds READ the firm buckets, the table and the served snapshots.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W84-S<k>`, next unused k), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R28_RELEASE_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_CANONICAL_RELEASE_20260930.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R28_M.md</decomp_doc> (round 28, workstream ~M), cell `IB-mr-281`.
<owned_cells>IB-mr-281</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM28-281-AC1, IBM28-281-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~84/IRPT_BCKEND.TO-IB-m28-281.holdings-release-packet.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM28-281-AC1,IBM28-281-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the table row count at build time, the census per firm (securities, moved with the largest moves by
weight, unclassified, GLD/PHYS/VXX), the served objects compared, the readers and writers counted, the half's path,
commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the release rides the existing Holdings cron after IB-mr-222 Part 2's fire.
comp-iam: RUN -- 1 file read (holdings_refresh.tf, 251's drafted EtfClassificationsRead statement, desired only); BLIND: whether the live Holdings firm principals already read etf-classifications is unmeasured (the half names the apply as release step 1).
comp-adversary: RUN -- 1 ledger read (mdpf-secclass-backfill-20260930 READBACK: 2,309 rows, 0 existing changed), 2 half reads (251 and 261 halves predate the backfill and 271); BLIND: the per-firm moved count against today's served snapshot is unmeasured at the cut (step 1 measures it).
lane: the <paths> block IS the grant.
</preflight>

Source: MDPF_SECCLASS release step 2 (ledger CLOSED @f13cddd058); Andrew-direct 2026-09-30 ~02:2xZ; hold ruling @469c404474.
