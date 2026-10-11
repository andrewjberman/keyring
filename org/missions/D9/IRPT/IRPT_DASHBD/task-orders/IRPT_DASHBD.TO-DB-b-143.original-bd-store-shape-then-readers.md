# TO IRPT_DASHBD.TO-DB-b-143 -- the ORIGINAL Black Diamond transactions store: does it hold a transaction once per id, or once per id and portfolio group -- counts on one day; and only if it repeats, every reader of it in four trees, keyed on the id or not

<to_id>IRPT_DASHBD.TO-DB-b-143</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~116</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5721 (2026-10-11 ~19:59Z), items 1 and 2 | **Rows:** IRPT_DASHBD-D2-W113-S2, IRPT_DASHBD-D2-W114-S1 | **Decomp cell:** `DB-b-143` (decomposition section 78) | **outcome_ref:** FWD-12 (the tie-out) and every consumer of that store | **depends_on:** DB-b-141 (drained @011cd1e142).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-116` (branch `wk-irpt-dashbd-76-116`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** The Black Diamond transactions COPY this project compared against lands a transaction once per portfolio group (DB-b-140;
re-run by the issuer on five days). DB-b-141 found the copy has one tracked reader, a project script. But the copy was made from
another store, the ORIGINAL silver transactions, which about 155 first-party files read, and nobody has looked at its shape
(`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~114/BD_TXN_READERS.json`, `adjacent_store_not_counted`). The CTO (msg 5721): "This
project found the shape, so it finishes the read; it corrects nothing outside itself. ... shape first, then the readers."

**The cell (`DB-b-143`).** A read. You change no code and correct nothing.
1. **The shape, first, on ONE day.** Find the original store's address from the code that writes or reads it. Read one recent day
   with the narrow projection the BOUNDS name. `shape` {read, day, rows, distinct_ids, ids_with_more_than_one_row, max_rows_per_id,
   repeats, how_firm_was_told}. `repeats` is true if any transaction id has more than one row that differs only in its portfolio
   group; if ids repeat for another reason (a correction, a reversal, two legs), say which column differs and set `repeats` by what
   you can show, or "NOT_ESTABLISHED" with why. **If `repeats` is false the cell ENDS here:** `readers_census: "NOT_NEEDED"`,
   `readers_census_why`.
2. **Only if it repeats: every reader, in four trees, denominator per tree.** `trees`: {workspace, portal, opal_ai, mcportal}, each
   {searched, files_searched, how}. The workspace is your worktree. `portal`, `opal_ai` and `mcportal` are empty gitlinks in a
   worktree: read them READ-ONLY in the shared checkout at `C:/dev/ajb_workspace/portal`, `C:/dev/ajb_workspace/opal_ai` and
   `C:/dev/ajb_workspace/mcportal` (native Grep and Glob over those absolute paths; state the commit each sits at with
   `git -C <path> rev-parse --short HEAD`); a tree you cannot read is `searched: false` with its reason. Falsify the domain first:
   list the address forms (prefix, table or dataset name, builder, registry row, a served API that fronts it) before you narrow.
   `readers`: [{tree, file, line, sums_amounts, keys_on_transaction_id (a dedupe on another key is false, with the key in `note`),
   what_it_serves (followed to the first served thing), served, owner (the project or seat that owns the file, from its path or the
   owned-paths map), note}]. Read each reader's code; do not class from a name.
3. `unkeyed_and_served`: "<tree>:<file>" for each reader that sums without the id AND serves something; for each, one sentence in
   `impact`. Each such reader is ONE ROW naming its owner (class OBSERVATION; ARMED only if you can show a served number is wrong
   today). `corrected: 0`, `s3_writes: 0`. No account id, client name or amount anywhere; the check refuses a run of 8 or more digits.
   Record `ORIGINAL_STORE_SHAPE.json`.

<criterion id="DB76-1-AC1" cell_refs="DB-b-143"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r76/p76_round76.py" . DB76-1-AC1</invocation><expect>DB76-1-AC1 PASS</expect></criterion>
`DB76-1-AC1` -- the original store's shape is counted on one day, and if it repeats a transaction every reader in the four trees is listed with whether it sums, whether it keys on the id, what it serves and who owns it. Base: FAIL.

<expected_criteria>DB76-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: ONE day of the original Black Diamond transactions store the copy was made from (its bucket and prefix taken from the code that lands or reads it, never typed; DB-b-141's record names it under `adjacent_store_not_counted`), read with a column projection of the transaction id, the portfolio group, the firm or tenant column and the date only. NO money column, NO account column leaves the object. If the store holds more than one firm, count 49 Financial's rows only and say how the firm was told. A denial is recorded verbatim, not retried by another route, and the shape reads NOT_ESTABLISHED.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~116/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W116-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-143.original-bd-store-shape-then-readers.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 78 (round 76), cell `DB-b-143`.
<owned_cells>DB-b-143</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB76-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/IRPT_DASHBD.TO-DB-b-143.original-bd-store-shape-then-readers.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB76-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the store's address form (not a key with an account in it), the day, the rows, the distinct transaction ids and how many ids have more than one row; whether it repeats; if it does: per tree the denominator, then ONE table of readers: tree, file:line, sums, keys on the id, what it serves, served to anyone, owner; the readers that sum without the id AND serve something; what you could not search; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one counts-only read of one day and a code census; nothing is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one governed read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
