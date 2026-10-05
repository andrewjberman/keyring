# TO IRPT_BCKEND.TO-IB-pr-319 -- the never-widen withdrawal packet for the 49F perfrp leaf (W100-S2 / W121-S1, CTO batch 251)

<to_id>IRPT_BCKEND.TO-IB-pr-319</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~122</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 251 @8ea5889048 (msg 105089): "Withdraw the leaf;
keep the portal's call". The packet carries the bucket's versioning state, every perfrp_* key under platinum/advi/*/ across all
firms with its writer, the withdrawal set, rollback per key, a stop on an ETag differing from the census read, and an after-read on
PROD with one 49F login. | **Decomp cell:** `IB-pr-319` (decomposition section 44) | **outcome_ref:** FWD-8 | **depends_on:**
IB-pr-318 (merged @0f69381e7c).

THIS CELL WRITES NOTHING TO AWS. The CTO signs the packet; the S3 delete is Andrew's.

---

## WORKER FACE

**The question.** The W100-S2 census
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~121/W100S2_READERS_CENSUS.json`) found the 49F leaf
`s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json` still loadable from the PROD portal. The leaf
carries an inflated 2025-01-10 day. The CTO rules to withdraw it. The portal's call site designs a 404 as the shell state, so no
product change is needed. Your job is the packet that makes the withdrawal safe to sign: what exactly goes, how it comes back, and
how the result is read.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-122`. Run everything from its root.

**What you read** (reads only):
1. **Versioning:** `s3.get_bucket_versioning(Bucket="opal-data-portal-v2")`. Record the `Status`, or `"never-enabled"` if absent.
2. **Every perfrp key:** list `platinum/advi/` in that bucket (paginate), and keep every key whose basename starts with `perfrp_`.
   This covers all firms. For each key record `key`, `etag`, `size` and `last_modified`.
3. **The writer of each key:** the code or job that writes it. Search `infra/`, `data/` and `org/modules/graph/` with the native Grep
   tool for `perfrp_` and the `platinum/advi` prefix, and name the file and line. If no writer is found, write `"none found"` with
   the search and the file count searched.
4. **Which keys carry 2025-01-10:** `get_object` each `perfrp_performance_*` key (only the performance leaves) and record
   `carries_20250110` true or false, with the field path where the date appears. Non-performance perfrp keys get
   `carries_20250110: false` and `"not read: not a performance leaf"`.

**What you produce:**
- `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~122/W100S2_WITHDRAWAL_PACKET.json` holds:
  - `versioning`;
  - `perfrp_keys`, the list from reads 2-4, and `perfrp_keys_denominator`, its length;
  - `withdrawal_set`: the 49F account leaf plus any performance leaf measured to carry 2025-01-10, and nothing else;
  - `rollback`, one entry per withdrawal key. If versioning is Enabled, give the version id to restore. Otherwise give a byte copy
    saved BEFORE the delete to a named backup address (state the address; do not write it) and the restore command;
  - `stop_rule`: the act stops if a key's ETag at act time differs from the ETag in this packet;
  - `after_read`: after the delete, one 49F login on PROD (`https://opalinvest.dev/advisor-intelligence`), where the leaf request
    returns 404 and the page shows its designed shell state;
  - `blast_radius`: the keys the act may touch (exactly the withdrawal set) and what it never touches.
- `W100S2_WITHDRAWAL_PACKET.md` beside it: the same content as a one-page record for the CTO's signature (`CTO half: ____`) and
  Andrew's word on the delete (`Andrew: ____`).

<criterion id="IB50-1-AC1" cell_refs="IB-pr-319"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r50/p50_withdrawal_packet.py" . IB50-1-AC1</invocation><expect>IB50-1-AC1 PASS</expect></criterion>
`IB50-1-AC1` -- the packet carries the six parts batch 251 names: versioning, every perfrp key with its writer and its
2025-01-10 measurement plus the denominator, a withdrawal set holding the account leaf and only measured carriers, rollback per
withdrawal key, a stop rule naming the ETag, and an after-read naming PROD and a 49F login. Base: FAIL.

<expected_criteria>IB50-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only (list, head, get, get_bucket_versioning). No put, copy, delete, or policy, versioning or logging change.
- **Refusal clause.** Any write to AWS is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~122/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-319.w100-s2-withdrawal-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 44 (round 50, workstream ~P), cell `IB-pr-319`.
<owned_cells>IB-pr-319</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB50-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~122/IRPT_BCKEND.TO-IB-pr-319.w100-s2-withdrawal-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB50-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the versioning state, the perfrp key denominator, the withdrawal set, the
criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only packet; 0 served bytes move in this cell; the withdrawal itself is a separate signed act.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes; the census already read the route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB50-1-AC1 base FAIL (no packet), dry-run at base ca6ba8a72f 2026-10-05 ~01:5xZ.
lane: the <paths> block IS the grant.
</preflight>
