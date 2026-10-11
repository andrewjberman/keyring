# TO IRPT_DASHBD.TO-DB-b-137 -- R45 presented once more as REFRESH 4: the same release with today's producer, so the first run after it stops writing the 24 keys -- a packet, no apply

<to_id>IRPT_DASHBD.TO-DB-b-137</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~110</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 5375 (2026-10-11 ~16:41Z) item 3, on DB-b-131's read | **Rows:** IRPT_DASHBD-D2-W100-S3, IRPT_DASHBD-D2-W101-S1, IRPT_DASHBD-D2-W101-S2 | **Decomp cell:** `DB-b-137` (decomposition section 73) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-132 and DB-b-134 (drained @02c31eaa62).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-110` (branch `wk-irpt-dashbd-71-110`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~110/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why again.** REFRESH_3 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~101/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_3.md`, both halves
signed today) pins the producer at `17304421c8`. Since then the producer changed three times: DB-b-128 (row 3's income reason reworded),
DB-b-132 (`served_thresholds`: both manifest writers serve the five thresholds and their claims and nothing else) and DB-b-134 (a refusal
in `method_version_of`). The CTO (msg 5375): "DB-b-132 is not a second release. R45 is not applied before Monday, so present it once more
as REFRESH 4 with DB-b-132's members added: the first run after it stops writing the 24 keys." You APPLY NOTHING. REFRESH_3's halves stand
until REFRESH_4's are signed.

**The cell (`DB-b-137`).** Read REFRESH_3's packet and record (`R45_REFRESH3.json` beside it) first, and follow its method section by
section. Write `NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_4.md` in your folder and `R45_REFRESH4.json`:
1. `members`: every file the release ships that differs from live's bytes, each {file, pin (the commit that last changed it on trunk
   today), sha256 at that pin, changed_since_refresh_3 (one line, or "unchanged")}. The check runs `git show <pin>:<file>` and compares
   the hash. The producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` is a member at today's pin.
2. **What changes for served objects, per key class**, beyond REFRESH_3: (a) every daily returns manifest written after the release
   carries a thresholds object of six keys instead of the whole file -- run the candidate producer dry on the kit day REFRESH_3 used
   (no upload, exactly as REFRESH_3 ran it) and record `manifest_thresholds_keys` (the key NAMES of the candidate manifest's thresholds
   object); (b) nothing else in the returns manifest moves except what REFRESH_3 already named; (c) the data tables: `kit` {ran, tables,
   tables_equal_to_live_pinned, reason}. If the kit cannot run without something this order does not grant, `ran: false` with exactly what.
3. **The method row.** REFRESH_3 established that the release cannot write 49 Financial's method row 2. Confirm that still holds at
   these pins (the handler omits the call), and say what a LATER `main()` upload would now write to the method manifest (six keys).
4. **The thresholds file in the package.** REFRESH_3's condition 1 keeps the PINNED 24-key file in the package. With DB-b-132 the
   manifests no longer copy it whole. State both options for the halves as an open question, with what each changes: keep the pinned
   file, or ship the tracked file with a claim per threshold (`data/assets/scripts/gold/irpt_reporting/MEASURED_THRESHOLDS_R1.json`;
   DB-b-131 measured its five values equal to the package's). Choose neither.
5. **What this release does NOT do**, stated in the packet: it rewrites no manifest already served; every manifest written before it
   keeps the whole object, and removing a prior version is a delete and Andrew's act.
6. Blast radius and rollback per key class as REFRESH_3 states them; the carried conditions (build from pins; one dry-run invoke against
   memory and time; wait for Monday 2026-10-12 07:41 ET's fire; the scheduled site read at first fire; no `main()` upload under this pair;
   an applier the gates admit). What is live today, read. `packet` {path, sha256}; `s3_writes: 0`.

<criterion id="DB71-2-AC1" cell_refs="DB-b-137"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r71/p71_round71.py" . DB71-2-AC1</invocation><expect>DB71-2-AC1 PASS</expect></criterion>
`DB71-2-AC1` -- the R45 release is presented on today's producer with every member pinned and hashed, the manifest's thresholds object shown to hold six keys, and the packet bound by hash. Base: FAIL.

<expected_criteria>DB71-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS reads are limited to `get-function` / `get-function-configuration` of the ONE reporting-gold function, to state what is live; no write.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~110/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W110-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~110/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-137.r45-refresh-4-with-served-thresholds.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 73 (round 71), cell `DB-b-137`.
<owned_cells>DB-b-137</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB71-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~110/IRPT_DASHBD.TO-DB-b-137.r45-refresh-4-with-served-thresholds.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB71-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the members with their pins and hashes and what changed in each since REFRESH_3; what the returns manifest's thresholds object holds at these pins (key names); the kit comparison, or exactly why it did not run; what is live today; the open questions for the two halves; and any row ids.

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
