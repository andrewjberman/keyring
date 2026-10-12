# TO IRPT_DASHBD.TO-DB-b-141 -- every reader in the repo of the Black Diamond transactions copy, each read for whether it keys on the transaction id -- a census, nothing corrected

<to_id>IRPT_DASHBD.TO-DB-b-141</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~114</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-75 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_75_20261011.md` @06b01d9b88, item 2, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v31.md` @ac4a24a07d | **Rows:** IRPT_DASHBD-D2-W113-S2 | **Decomp cell:** `DB-b-141` (decomposition section 77) | **outcome_ref:** FWD-12 (the tie-out) and every consumer of that copy | **depends_on:** DB-b-140 (drained @f7b1cc4571).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-114` (branch `wk-irpt-dashbd-75-114`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~114/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v31.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** DB-b-140 found that 49 Financial's Black Diamond transactions copy (`blackdiamond/49financial/silver_legacy/transactions/`,
and the same layout for any other firm) holds one row per transaction id AND portfolio group: a transaction in k groups is landed k
times. A reader that sums that copy by date without keying on the transaction id over-counts (row W113-S2). The issuer's own re-run
confirmed the rule on five days (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/RERUN_FIVE_DAYS_ROW_W111_S1.md`). The CTO: "every reader of the
Black Diamond transactions copy in the repo, denominator printed, each read for whether it keys on the transaction id. Name any that does
not, with what it serves; correct nothing this round."

**The cell (`DB-b-141`).** A read. You change no code.
1. **The domain, falsified first.** The copy is addressed in more than one way: by its prefix (`silver_legacy/transactions`,
   `blackdiamond/<firm>/...transactions`), by a table or dataset name, through a naming builder (`lib/opal_naming.py`), through a
   registry row (`infra/logic/registry/`), or through a helper that returns the path. Find the address forms by ONE unscoped read of the
   term over the corpus (`comp-find` with its denominator; or the native Grep tool over the tracked tree) before you narrow, and state
   `search` {method, patterns, files_searched}. A reader you could only find through an indirect address is still a reader.
2. **Each reader**, tracked code only (`data/`, `infra/`, `lib/`, `workflows/`, `integrations/`, `portal/` and `opal_ai/` if they are in
   your tree; say which trees you did not have): `readers`: [{file, line (where it reads the copy), firm_scope (which firm or any),
   sums_amounts (does it add a money column across rows), keys_on_transaction_id (does it dedupe or group by the transaction id before
   it sums or counts; a dedupe on another key is `false` with the key named in `note`), what_it_serves (the table, file, page or
   report its result feeds, followed to the first SERVED thing or to "nothing served: a project script"), note}]. `reader_count`.
   Project deliverable scripts under `org/missions/` are listed too, marked as such.
3. `not_keyed`: the files of the readers with `sums_amounts` true and `keys_on_transaction_id` false. For each, one sentence in
   `impact`: what would be over-counted and where it would show. Correct NOTHING: `corrected: 0`. A reader whose output is served and
   over-counts is a row (class OBSERVATION; ARMED only if you can show a served number is wrong today, with the evidence).
4. `s3_writes: 0`. Record `BD_TXN_READERS.json`.

<criterion id="DB75-1-AC1" cell_refs="DB-b-141"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r75/p75_round75.py" . DB75-1-AC1</invocation><expect>DB75-1-AC1 PASS</expect></criterion>
`DB75-1-AC1` -- every reader of the copy in the repo is listed with its line, whether it sums amounts, whether it keys on the transaction id and what it serves, with the search's denominator printed. Base: FAIL.

<expected_criteria>DB75-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~114/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W114-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~114/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-141.bd-transactions-copy-readers-keyed-on-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 77 (round 75), cell `DB-b-141`.
<owned_cells>DB-b-141</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB75-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~114/IRPT_DASHBD.TO-DB-b-141.bd-transactions-copy-readers-keyed-on-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB75-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the search and its denominator; ONE table of readers: file:line, sums amounts yes or no, keys on the transaction id yes or no, what it serves; the readers that sum without keying, named, with what each serves and whether that output is served to anyone; what you did not search; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a code census; nothing is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
