# TO IRPT_DASHBD.TO-DB-b-119 -- every reader of the returns manifest named with file and line, the count printed, and whether each accepts a key it does not know -- the CTO half's condition 1 before the R45 apply

<to_id>IRPT_DASHBD.TO-DB-b-119</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~94</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>63</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's R45 refresh 2 half, condition 1 (msg 4126; `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R45_RELEASE_REFRESH2_CTO_HALF.md`), enrichment item E1 | **Decomp cell:** `DB-b-119` (decomposition section 65) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-117 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-94`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~94/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report.

**The cell (`DB-b-119`).** The R45 gold release adds three keys to the SERVED returns manifest (`valuation_source`, `fee_treatment`, `price_basis`); see
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~92/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_2.md`, section "Manifest comparison". Both
halves are signed. The CTO's half adds one condition before the apply: the packet counted the manifest's WRITERS, not its READERS. This cell counts the
readers. A reader that refuses or misbehaves on a key it does not know is a STOP back to the CTO.

The object: `manifest.json` beside each `date=` partition of the gold table `account_return_daily`, at the address
`opal_naming.address("irpt", <firm>, "gold", "account_return_daily", "date=<day>")` (written by `emit_day` in
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, ~line 1863).

1. **Scopes, each with its denominator.** Search by subtraction from "every place code that could read this object lives", never by recall:
   - this workspace repo (`comp-find`, corpus all), for the table name with `manifest`, the address builder call with that table, and generic manifest
     loaders that take a partition address;
   - the portal checkout `portal/` (its own repo: read it with `git -C portal grep` on named patterns, or Grep over the `portal/src` folder);
   - `opal_ai/` and `mcportal/` if present (say ABSENT if a directory is not there; an absent directory is not a zero);
   - the Lambda sources under `infra/aws/lambda/` that read the gold tier (the investor-reporting publish and API functions among them).
   Record each as {scope, files_scanned, patterns, hits}.
2. **Readers.** For every place that reads the manifest object's bytes (not the parquet beside it), record {file, line, in_repo, how_it_reads,
   unknown_key, evidence}: `unknown_key` is `ACCEPTS` (it reads named keys and ignores the rest, or passes the dict through), `STRICT` (it validates
   against a closed key set, a schema with no additional properties, a fixed-width unpack, or an equality against a stored manifest), or
   `NOT_ESTABLISHED` (say what would establish it). `evidence` quotes the line that decides it. Checks and tests that compare a manifest to a golden
   file count as readers too, marked as such: a golden comparison that pins the key set is STRICT for the test, and you say whether it gates anything
   at deploy.
3. **`reader_count`**, and **`verdict`**: `STRICT_READER_FOUND` if any reader is STRICT; `UNDETERMINED` if none is STRICT and any is
   `NOT_ESTABLISHED`; `NO_STRICT_READER` otherwise. Zero readers is a legitimate count only with every scope's denominator printed beside it.
4. Write `RETURNS_MANIFEST_READERS.json` and a one-page `.md`.

<criterion id="DB63-1-AC1" cell_refs="DB-b-119"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r63/p63_round63.py" . DB63-1-AC1</invocation><expect>DB63-1-AC1 PASS</expect></criterion>
`DB63-1-AC1` -- every reader of the returns manifest is named with file and line over scopes that print their denominators, each graded on an unknown key, with a verdict that follows from the readers. Base: FAIL.

<expected_criteria>DB63-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/`, `portal/` or `org/standards/`.
- **AWS:** none. NO Black Diamond or vendor call, no secret read, no S3 read or write, no deploy, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~94/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~94/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-119.returns-manifest-readers.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 65 (round 63), cell `DB-b-119`.
<owned_cells>DB-b-119</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB63-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~94/IRPT_DASHBD.TO-DB-b-119.returns-manifest-readers.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB63-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, each scope with its denominator, every reader with file, line and its unknown-key grade, the count, the verdict, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only census; no producer, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; API functions are read as sources only.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB63-1-AC1 FAIL at base (no record). CTO half condition 1, msg 4126.
lane: the <paths> block IS the grant.
</preflight>
