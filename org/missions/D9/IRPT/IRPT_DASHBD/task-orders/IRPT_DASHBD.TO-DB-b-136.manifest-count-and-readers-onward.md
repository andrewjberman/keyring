# TO IRPT_DASHBD.TO-DB-b-136 -- how many served 49 Financial manifests carry the whole thresholds object -- a key listing, no bodies -- and whether any of the ten readers of a returns manifest passes that object onward

<to_id>IRPT_DASHBD.TO-DB-b-136</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~109</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>71</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 5375 (2026-10-11 ~16:41Z) item 1 and 2, on DB-b-131's read | **Rows:** IRPT_DASHBD-D2-W100-S3, IRPT_DASHBD-D2-W105-S1 | **Decomp cell:** `DB-b-136` (decomposition section 73) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-131 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-109` (branch `wk-irpt-dashbd-71-109`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~109/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** DB-b-131 read the thresholds file inside the LIVE function's package and ONE daily returns manifest of 49 Financial: both carry a
24-key thresholds object with 14 digit runs of 8 or more, two keys named `per_account_*` (record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~105/PACKAGE_AND_MANIFEST_READ.json`). The CTO (msg 5375): "It is every daily manifest the
live package writes, and Monday's fire writes another." Two things decide how the question is put to Andrew: HOW MANY, and whether the
object travels beyond the bucket.

**The cell (`DB-b-136`).** Read-only. You change no code. Record `MANIFEST_COUNT_AND_READERS.json` in your folder.
1. **Which prefixes.** Read `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` and `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`: every
   `manifest.json` the package writes whose body includes the thresholds object (`build_manifest` for the daily returns; `emit_method_row`
   for the method row; say for each other table's manifest whether it carries the object or not, from the code). `prefixes`: [{role,
   carries_thresholds_object (from the code), listed, manifests, first_date, last_date, reason}]. No bucket name or key is written with an
   account id in it; a prefix is described by its role and its table name.
2. **Count by key listing.** For each prefix that carries the object: list it to the end and count the keys named `manifest.json`, with
   the first and last partition dates. `total_manifests` is the sum over listed prefixes. `bodies_read: 0`. State plainly that a count of
   keys says how many objects COULD carry the object; whether each does was read for one day only (DB-b-131), and manifests written before
   the thresholds file gained its 24 keys may differ: say what the code and git history show about when it did, if they show it.
3. **The ten readers.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~94/RETURNS_MANIFEST_READERS.json` lists ten readers of the returns
   manifest (file and line). For EACH, read the code at that line and what it does with what it read: does it pass the `thresholds` object,
   or the whole manifest, onward -- into a return value another module uses, a response, a file, a log line, a page? `readers`: [{file,
   line (exactly as the census has them), passes_onward (bool), to_what (a sentence; "nothing: it reads N named members and drops the
   rest" is an answer)}]; `any_passes_onward`. A reader you cannot find at its line any more is read at where it moved to, and you say so.
4. `s3_writes: 0`. The check refuses a record holding any run of 8 or more digits.

<criterion id="DB71-1-AC1" cell_refs="DB-b-136"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r71/p71_round71.py" . DB71-1-AC1</invocation><expect>DB71-1-AC1 PASS</expect></criterion>
`DB71-1-AC1` -- the 49 Financial manifests the live package writes are counted per prefix by key listing with first and last dates, and each of the ten readers is read for whether it passes the thresholds object or the whole manifest onward. Base: FAIL.

<expected_criteria>DB71-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim, and nothing else: `s3api list-objects-v2` (paginated to the end, counted client-side) on the prefixes the live package writes for 49 Financial, each address taken from the producer's own builder, never typed. NO `get-object`, NO body of any object. A denial is recorded verbatim, not retried by another route, and that prefix reads `listed: false` with its `reason`.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~109/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W109-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~109/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-136.manifest-count-and-readers-onward.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 73 (round 71), cell `DB-b-136`.
<owned_cells>DB-b-136</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB71-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~109/IRPT_DASHBD.TO-DB-b-136.manifest-count-and-readers-onward.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB71-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table of prefixes: its role, the count of manifest keys, first and last dates; the total; ONE table of the ten readers: file:line, passes onward yes or no, to what; anything not listed and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; key listings and a code read; nothing served is written or read by body.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; list calls on one firm's own prefixes; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
