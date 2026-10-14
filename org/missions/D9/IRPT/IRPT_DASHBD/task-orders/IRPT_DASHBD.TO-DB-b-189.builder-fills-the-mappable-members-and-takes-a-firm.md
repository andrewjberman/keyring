# TO IRPT_DASHBD.TO-DB-b-189 -- the household sample builder fills every member classified (a) mappable now, takes the firm as an argument with no firm branch outside an adapter, and rebuilds the same 49 Financial household; nothing else moves

<to_id>IRPT_DASHBD.TO-DB-b-189</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~154</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7451, ENRICHMENT item 2 ("Fill every (a) in this round. List (b) and (c) for round 102") and item 3's "same builder, same contract, no firm-specific branch outside its adapter (C-ADAPTERS)" | **Rows:** IRPT_DASHBD-D2-W154-S<k> | **Decomp cell:** `DB-b-189` (decomposition section 103) | **outcome_ref:** FWD-21 | **depends_on:** `DB-b-188` (the classification; this order is spawned after it drains).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-154` (branch `wk-IRPT_DASHBD-154`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~154/`.

**What exists.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py` builds ONE 49 Financial household into the performance-report contract's filled shape (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, `document.filled_report`): read its header in full (the household rule R1-R6, the window folds, the identity checks, the units, what it reads and writes). It writes `HOUSEHOLD_SAMPLE.json` to a private folder. Run: `python -I build_sample.py <repo_root> <private_out_dir>`. The current real sample (client data, read-only, sha256 `76a48793d6979ba66358d4e1d2cdc3d59d34c9a5217df1b7b421715925ddf16d`) is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE.json`; it holds 55 filled members and 62 absent. The previous cell classified every absent member: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~153/ABSENT_CLASSIFICATION.json` (class `a` = mappable now from an existing gold table, `b` = derivable by a ratified rule, `c` = truly absent), whose `evidence` names for each (a) member the table contract, the column and the fold. Read it in full.

**The cell (`DB-b-189`).**
1. **Copy, do not edit in place.** Copy `~141/build_sample.py` into YOUR folder and change your copy; the original and the old sample stay as they are (the checker verifies the old sample's bytes are untouched and your record states them).
2. **Fill every (a) member and ONLY the (a) members.** For each member classified `a`, the builder reads the named gold column and applies the named fold (the contract's fold text governs; never plug a residual, never write a zero for an absent source: an input that is missing on the day or lagging makes the member absent in words, as the builder's existing rules say). A member classified `b` or `c` stays absent with the reason the builder already gives. Every figure the previous sample held stays EXACTLY as it was (the checker compares every previously filled member).
3. **Take the firm as an argument.** The builder gets `--firm <firm_id>` (default `49financial`) and `--out <private_out_dir>`. Every firm-specific item (the bucket, the gold prefix, the household source) is DERIVED from `lib/opal_naming.py` `address()` and the firm registry `data/firm_registry.json`, never typed in the builder for one firm, except inside ONE function named `firm_adapter(firm)` that returns them and that raises `NotImplementedError("<firm>: no gold exists")` for a firm with no `irpt/` gold prefix. A needed branch anywhere else is a FINDING (a row), not a branch: `firm_branches_outside_adapter` in the record counts them and must be 0.
4. **Rebuild the SAME household** (same household rule, same reference hash) into the new private path `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~154/HOUSEHOLD_SAMPLE.json` (create the folder; this exact path is checked), plus the counts file the builder already writes beside it. S3 GET and LIST only. The identity checks the builder runs (counted checks, tolerance 1.00 dollar) must pass with none failing; a failing check is a finding: record the counts and stop.
5. **Record** `SAMPLE_FILL.json` in your folder with exactly: `prior_sample_sha256` (the old sample's sha256 above, unchanged on disk); `sample_sha256` (of the new sample); `newly_filled_ids` (the sorted ids that are filled now and were absent before: they must equal the (a) ids exactly); `filled_before` (55) and `filled_after` (55 plus the number of (a) members); `identity_checks` {`counted`, `passed`, `failed` 0, `not_gradeable`}; `window_residual_checks_failed` 0; `builder_sha256` (of your folder's `build_sample.py`); `firm_branches_outside_adapter` 0; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, ids and words only: no figure, no account number, no run of eight or more digits.
6. Run `bash .tools/commit-gate.sh <file>` on your builder (it is a `.py` file in a deliverables folder). The builder's own self-tests or an assertion that every filled id is an (a) id are welcome.

<criterion id="DB101-3-AC1" cell_refs="DB-b-189"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r101/p101_round101.py" . DB101-3-AC1</invocation><expect>DB101-3-AC1 PASS</expect></criterion>
`DB101-3-AC1` -- the old sample is untouched; the new private sample conforms to the filled-report shape (the round-97 shape check), is the same household, and has filled exactly the (a) members (no other id), with every previously filled figure unchanged; the identity checks counted some and failed none; the builder takes `--firm` and holds no firm branch outside its adapter; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB101-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~141/build_sample.py`, the old sample, the contract and the classification.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files and S3 LIST and GET of the gold tables the builder already reads. A denial is recorded verbatim, not retried by another route.
- **Client data.** The samples live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. Nothing of them goes in the repo, a row, a message or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An (a) member you find cannot be filled by its named column and fold is a FINDING row and the criterion fails: do not fill it by another route and do not fill any other member. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W154-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~154/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-189.builder-fills-the-mappable-members-and-takes-a-firm.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 103 (round 101), cell `DB-b-189`.
<owned_cells>DB-b-189</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB101-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~154/IRPT_DASHBD.TO-DB-b-189.builder-fills-the-mappable-members-and-takes-a-firm.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB101-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the members filled (count and the groups, by section) and the fold used per group; the filled count before and after of 117; the identity checks (counted, passed, failed, not gradeable); how `firm_adapter` derives its values; any (a) member you could not fill and why; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a builder script and a private sample; nothing is served, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 LIST and GET with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 8 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
