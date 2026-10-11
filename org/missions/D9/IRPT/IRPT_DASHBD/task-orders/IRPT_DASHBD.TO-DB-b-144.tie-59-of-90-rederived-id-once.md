# TO IRPT_DASHBD.TO-DB-b-144 -- "59 of 90 tie, 31 do not" re-derived with each transaction id counted once, before that number is shown again

<to_id>IRPT_DASHBD.TO-DB-b-144</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~117</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5721 (2026-10-11 ~19:59Z), its last line (row W114-S1) | **Rows:** IRPT_DASHBD-D2-W114-S1 | **Decomp cell:** `DB-b-144` (decomposition section 78) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-142 (drained @fc42bbcab0: its re-read holds the transaction id for the accounts of the 51).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-117` (branch `wk-irpt-dashbd-76-117`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~117/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~108/UNCLASSED_90.json` states that a simple sum of the ledger's Contribution and
Withdrawal rows ties the custodian's net additions for 59 of the 90 segments and not for 31. That sum was made WITHOUT keying on the
transaction id, on a copy that repeats a transaction once per portfolio group (rows W113-S2, W114-S1). The CTO: "re-derive '59 of 90
tie' with each id counted once before that number is shown again."

**The cell (`DB-b-144`).** Read-only; you change no code and no served thing, and you do NOT edit ~108's record.
1. **Reproduce the original count** exactly as ~108 made it (its scripts under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`:
   `read90.py`, `table90.py`, `class90.py`; cite the lines that make the sum and the tie test, and its tolerance): `naive` {tie,
   do_not_tie}. A count other than 59 and 31 is a STOP with a row.
2. **Re-derive with each transaction id counted once**, same tie test and tolerance, for all 90: you need the transaction id for the
   accounts of all 90 segments. ~115's re-read (`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~115/`) holds it for the accounts of the
   51; read the tree once more for the rest, keeping the id (its script shows how). `id_once` {tie, do_not_tie}; `moved` (segments
   that change side) with `moved_to_tie` and `moved_to_not_tie`.
3. Say in one sentence what the corrected count does and does not change: it is a description of the ledger against the custodian's
   own net additions; it moves no segment between classed, contested and unclassed, and you move none.
4. `client_figures: 0`, `s3_writes: 0`. Counts only: no account id, no client name, no amount. The check refuses a record holding
   any run of 8 or more digits. Your tables and scripts go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~117/`. Record
   `TIE_59_OF_90_REDERIVED.json`.

<criterion id="DB76-2-AC1" cell_refs="DB-b-144"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r76/p76_round76.py" . DB76-2-AC1</invocation><expect>DB76-2-AC1 PASS</expect></criterion>
`DB76-2-AC1` -- the count of the 90 segments whose ledger contributions and withdrawals tie the custodian's net additions is re-derived with each transaction id counted once, beside the naive count. Base: FAIL.

<expected_criteria>DB76-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: 49 Financial's OWN Black Diamond transactions tree, the prefix workers ~108, ~113 and ~115 read (taken from their scripts, never typed), for the accounts of the 90 segments that ~115's re-read does not already hold with the transaction id. No other firm's prefix, no other bucket. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~117/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W117-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~117/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-144.tie-59-of-90-rederived-id-once.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 78 (round 76), cell `DB-b-144`.
<owned_cells>DB-b-144</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB76-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~117/IRPT_DASHBD.TO-DB-b-144.tie-59-of-90-rederived-id-once.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB76-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how the original 59 and 31 were computed (file and line of the earlier script) and that you reproduced them; the same count with each id counted once; how many segments change side and in which direction; what you read; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a re-derivation of one count from one firm's custodian tree; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
