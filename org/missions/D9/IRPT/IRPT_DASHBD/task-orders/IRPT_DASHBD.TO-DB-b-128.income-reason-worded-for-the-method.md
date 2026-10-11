# TO IRPT_DASHBD.TO-DB-b-128 -- the served income reason on method row 3 is reworded for the METHOD, not one channel: the producer, its test, the contract's example, and the small never-widen packet for the one served object -- no S3 write

<to_id>IRPT_DASHBD.TO-DB-b-128</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~103</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 5, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-S13 | **Decomp cell:** `DB-b-128` (decomposition section 70) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-127 (the same producer file; it runs after it on the same worker chain).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-103` (branch `wk-irpt-dashbd-68-103`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~103/`. Read first: section 2 (item 4) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is wrong.** Method row 3 (positions-based) is ONE row for ANY positions-based entry, but since today its `income_basis_reason` reads
"FWD-3 does not separate income: it sits inside the value through the cash leg, so this method states no income basis (its income columns
are null on every row)": that names one project's outcome id and describes one channel's table. The reviewer (row D2-S13) and the CTO
(item 4): the reason is worded for the METHOD.

**The cell (`DB-b-128`).**
1. **Rule-24 record first** (`INCOME_REASON.json`, `rule24`: `mece`, `same_grain`, `intent_coherence`, `state_coherence`, each {finding,
   evidence}): the reason is a property of the method row; does one sentence hold for every entry that can name row 3 today (list them from
   `sources.json`, underscore entries included)? If a channel that DOES separate income could name row 3, the reviewer's alternative applies
   (that channel gets its own method row): then STOP with a row and build nothing.
2. **The words.** Reword `METHOD_ROWS[3]`'s income reason in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` so it states what the METHOD does, in plain
   words, naming no project outcome id, no firm, no custodian and no single channel (`channels_named: []`): for example, that a
   positions-based method values the account from its positions and cash, so income is inside the value and is not stated separately. Use
   your own sentence if it is truer; record `reason_before` and `reason_after`. No other member of the row moves; row 2 does not move.
3. The test that pins row 3's reason and the contract's example row follow; the contract's `schema_hash` does NOT move for a wording change
   (say so if it does, and why); `tests` {passed, failed}.
4. **The reader, named** (`reader_named` {file, line}): the one reader of the served method row
   (`data/assets/scripts/silver/commonwealth_account_return_daily.py`, the mint's verify), and that it reads no income member.
5. **The small packet, no S3 write:** `NEVER_WIDEN_PACKET_METHOD_ROW3_INCOME_REASON.md` in your folder, following
   `deliverables/0.9.0_WK_IRPT_DASHBD~97/NEVER_WIDEN_PACKET_METHOD_ROW3_INCOME.md` section by section: the object's address (the dry run's,
   never typed), its two keys as they are NOW (after today's rewrite at 10:38Z: read them), the writers and readers counted, the exact
   before and after row (one member changes, plus `measured_at`), both branches, rollback per key by the prior version id (the bucket is
   versioned), and that the apply names an applier the gates admit (row W87-S1: not a worker). `packet` {path, sha256, object_address};
   `s3_writes: 0`.

<criterion id="DB68-5-AC1" cell_refs="DB-b-128"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-5-AC1</invocation><expect>DB68-5-AC1 PASS</expect></criterion>
`DB68-5-AC1` -- the income reason is worded for the method and names no single channel, with its rule-24 record, the method row's reader named, and the packet for the one served object bound by hash. Base: FAIL.

<expected_criteria>DB68-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. ONE AWS read is allowed: a `list-objects-v2` or `head-object` on the ONE served prefix the packet names (Cottonwood `dim_return_method`, `method_version=3`), to state its two keys' ETags and version ids as they are now.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~103/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W103-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~103/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-128.income-reason-worded-for-the-method.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-128`.
<owned_cells>DB-b-128</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-5-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~103/IRPT_DASHBD.TO-DB-b-128.income-reason-worded-for-the-method.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the reason before and after; the rule-24 findings in a line each; the reader of the method row (file:line) and that it reads no income member; the contract's version and hash if they moved; the tests; the packet -- the object's address, its two keys as they are now, the before and after row, the rollback; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one sentence in one served method row with zero readers of that member; the rewrite is a later act under its own signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one single-prefix read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
