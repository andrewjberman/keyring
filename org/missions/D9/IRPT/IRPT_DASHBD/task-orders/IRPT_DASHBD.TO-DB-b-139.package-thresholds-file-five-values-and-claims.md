# TO IRPT_DASHBD.TO-DB-b-139 -- the 24-key thresholds file inside the function's package is replaced by a file of the five values and their claims: the kit run on that file, and the packet for the swap as its own later release -- no apply

<to_id>IRPT_DASHBD.TO-DB-b-139</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~112</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 5496 (its signed half on R45 REFRESH 4 @e969a090cc, answer to question 5): "One cell in your next issuance replaces it with a file of the five values and their claims, after a kit run on that file." | **Rows:** IRPT_DASHBD-D2-W100-S2, IRPT_DASHBD-D2-W100-S3 | **Decomp cell:** `DB-b-139` (decomposition section 75) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-137 (drained @ca0e108aba; both halves on REFRESH 4 signed).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-112` (branch `wk-irpt-dashbd-73-112`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~112/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** Both halves on R45 REFRESH 4 are signed with the PINNED 24-key thresholds file still inside the package, because that is what
its kit measured. The CTO's half states the cost "and not accepted as permanent: the code package still holds the 24-key file. One cell
in your next issuance replaces it with a file of the five values and their claims, after a kit run on that file." Two of those 24 keys
hold account-number-shaped digit runs (row W100-S3). You APPLY NOTHING, and you do not touch REFRESH 4's packet or its halves.

**The cell (`DB-b-139`).** Read REFRESH 4's packet and record first
(`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~110/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_4.md`, section "The thresholds file in the
package", option B; `R45_REFRESH4.json`; `R45_REFRESH4_DELTA0.json`; `method_scripts/`). Reuse its harness unchanged.
1. **The replacement file.** `data/assets/scripts/gold/irpt_reporting/MEASURED_THRESHOLDS_R1.json` (tracked by DB-b-125, last change `aaeb1866ff`): read its top-level keys.
   The file that rides the package must hold EXACTLY the five threshold values and `threshold_claims` (a claim per value), nothing
   else. If the tracked file already is that, it is the replacement as it stands: change nothing. If it holds any other key (a note,
   a basis, a source), say which, and make the file exactly the six keys, moving nothing's VALUE and no claim; whatever you remove
   goes into a sibling `MEASURED_THRESHOLDS_R1.provenance.json` in the same folder (so the reasons behind the claims are not lost),
   and the folder's tests that read the file (`tests/test_thresholds_file_claims.py` and any other) pass before and after.
   `file` {path, pin (the commit that last changed it once you are done), sha256 at that pin, top_level_keys}; `changed_by_this_cell`.
2. **The kit run on that file.** Build the kit exactly as REFRESH 4's (`kit_new7`): the same four members at REFRESH 4's pins, every
   other staged file at its source-map pin, with ONE difference: the thresholds file in the kit is the replacement. Run the same kit
   day (2026-10-08), dry. `kit` {ran, tables, tables_equal_to_refresh4 (how many of the output tables are byte-equal to REFRESH 4's
   candidate run), tables_equal_to_live_pinned, reason}. The five values are equal by DB-b-131's measure, so the tables are EXPECTED
   equal: an unequal table is a finding, reported as measured with which table, never explained away. From the kit's captured returns
   manifest: `manifest_thresholds_keys` and `claims_served` (the five claims as served). Everything the kit downloads or writes stays
   under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~112/`.
3. **The packet**, `NEVER_WIDEN_PACKET_GOLD_PACKAGE_THRESHOLDS_FILE.md` in your folder, for the swap as ITS OWN release AFTER REFRESH 4
   is applied (it does not amend REFRESH 4): the one member that changes (the thresholds file: its `repo_path`, pin and sha256, and the
   source-map entry that must be re-pinned, by line); what changes for served objects per key class (the claims a returns manifest
   serves; nothing else, by the kit); what the package no longer contains (the count of keys dropped and how many carry a run of 8 or
   more digits: counts only); writers and readers counted as REFRESH 4 counted them; both branches; rollback per key; the conditions it
   inherits (pins, one dry-run invoke, an applier the gates admit, read at the first fire); and that it is ordered after REFRESH 4's
   apply and its first-fire read. `packet` {path, sha256}. Both halves UNSIGNED; you sign nothing.
4. What is live today, read. `s3_writes: 0`. No value of the old file's other keys is printed, kept in the repo or reported: counts
   and key names only. The check refuses a record holding any run of 8 or more digits. Record `THRESHOLDS_FILE_SWAP.json`.

<criterion id="DB73-1-AC1" cell_refs="DB-b-139"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r73/p73_round73.py" . DB73-1-AC1</invocation><expect>DB73-1-AC1 PASS</expect></criterion>
`DB73-1-AC1` -- the replacement file holds exactly the five values and their claims at a pin, the kit is run on it and compared with REFRESH 4's run, and the packet for the swap is bound by hash. Base: FAIL.

<expected_criteria>DB73-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS reads are limited to `get-function-configuration` of the ONE reporting-gold function (to state what is live) and the kit run's own S3 GETs and LISTs of the served inputs for the kit day, exactly as REFRESH_4's kit made them (row D2-W110-S1 records that reading; it is granted here in words). No write: the kit's data writer is stubbed and its capture client refuses a write verb.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~112/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W112-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~112/
data/assets/scripts/gold/irpt_reporting/MEASURED_THRESHOLDS_R1.json
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-139.package-thresholds-file-five-values-and-claims.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 75 (round 73), cell `DB-b-139`.
<owned_cells>DB-b-139</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB73-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~112/IRPT_DASHBD.TO-DB-b-139.package-thresholds-file-five-values-and-claims.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB73-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the replacement file's path, pin, sha256 and key names; whether you changed the tracked file and why; the kit run -- tables, how many equal REFRESH 4's run, the manifest's thresholds key names and the five claims served; what the packet states as its members and its place after REFRESH 4; what is live; anything not established; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a kit run and a packet; the swap is a later release under its own signed pair, after REFRESH 4 is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one function read and the kit's own reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
