# TO IRPT_DASHBD.TO-DB-b-126 -- R45 presented again on current bytes: a third release packet whose members are pinned today, with the sources.json that rides it named, and DB-b-115's manifest fields read -- no apply

<to_id>IRPT_DASHBD.TO-DB-b-126</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~101</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-W88-S1 (ARMED), IRPT_DASHBD-D2-W88-S3 (ARMED) | **Decomp cell:** `DB-b-126` (decomposition section 70) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-124 (its read of rows W88-S1 and W88-S3).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-101` (branch `wk-irpt-dashbd-68-101`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~101/`. Read first: section 2 (item 2) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why again.** The CTO's half on R45 is VOID (analysis section 2 item 2): it was signed on bytes that predate later cuts. The producer has
changed again today (DB-b-122: method row 3 states income absent, two new columns on the method row, contract 0.6.0). A release built from
the old pins would not carry that; a release built from HEAD would also give 49 Financial's method row 2 the two new columns, which the
CTO's half on DB-b-122 says needs to be NAMED in its own pair (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_METHOD_ROW3_INCOME_CTO_HALF.md`,
condition 5). So R45 is presented again, on current bytes, as a packet. You APPLY NOTHING.

**The cell (`DB-b-126`).** Read the two earlier packets first
(`deliverables/0.9.0_WK_IRPT_DASHBD~92/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_2.md` and the COO half
`deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_R45_RELEASE_REFRESH2_COO_HALF.md`) and follow REFRESH_2's method. Write
`NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_3.md` in your folder and `R45_REFRESH3.json`:
1. `members`: every file the release ships, each pinned at the commit that last changed it on trunk today, with its sha256 at that pin, and
   one line on what changed since REFRESH_2's pin (or "unchanged").
2. `sources_json` {pin, declares_method_version_for_49f} with the line that declares it. This is row W88-S1's disarm.
3. The kit comparison on the kit day REFRESH_2 used: run the candidate members (dry, no upload, exactly as REFRESH_2 ran it) and state
   `kit` {rows, method_version_equal_rows, equal}. If the kit cannot run without something this order does not grant, say exactly what.
4. `manifest_fields`: what the candidate's returns manifest states for `method_version`, `valuation_source`, `fee_treatment`,
   `price_basis` (row W88-S3's disarm is `method_version` 2 stated, not the literal `absent`).
5. In the packet, a section the pair must sign: **what a release at these pins changes for 49 Financial's served objects beyond R45's
   original scope** -- the method row 2's two new columns (`income_basis_claim`, `income_basis_reason`), with their values for row 2, and
   every reader of that method row counted with file and line (N readers = N rules read). Blast radius per key and rollback per key (the
   prior S3 object version of the function's code; the prior version of each served key if the bucket is versioned).
6. What is live today (function CodeSha256, the code object's version id), read, not assumed. `s3_writes: 0`.

<criterion id="DB68-3-AC1" cell_refs="DB-b-126"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-3-AC1</invocation><expect>DB68-3-AC1 PASS</expect></criterion>
`DB68-3-AC1` -- the R45 release is presented on today's bytes with every member pinned and hashed, its sources.json declaring method_version for 49 Financial, the kit comparison and the manifest fields read. Base: FAIL.

<expected_criteria>DB68-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS reads are limited to `get-function` / `get-function-configuration` of the ONE reporting-gold function and a `head-object` of its ONE current code object, to state what is live; no write.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~101/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W101-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~101/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-126.r45-presented-again-current-bytes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-126`.
<owned_cells>DB-b-126</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~101/IRPT_DASHBD.TO-DB-b-126.r45-presented-again-current-bytes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the members with their pins and hashes and what changed since REFRESH_2; which sources.json rides the release and the line where it declares method_version; the kit comparison's row counts; the four manifest fields as the candidate writes them; what is live today; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a packet only; the apply is a later act under a newly signed pair, after Monday's R44 acceptance fire.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; single-resource reads of one function.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
