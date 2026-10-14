# TO IRPT_DASHBD.TO-DB-b-182 -- state the shape of a filled report in the contract (0.3.0) exactly as the tested components read it, and make the sample builder emit that shape: account entries with an account id, last four, first data date and a status per window; per-account values wrapped in by_row; the real sample rebuilt

<to_id>IRPT_DASHBD.TO-DB-b-182</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~148</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>97</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7349 (render the real sample), blocked by worker ~146's row IRPT_DASHBD-D2-W146-S1 | **Rows:** IRPT_DASHBD-D2-W146-S1 | **Decomp cell:** `DB-b-182` (decomposition section 99) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-175, DB-b-176, DB-b-179 (all drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-148` (branch `wk-IRPT_DASHBD-148`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~148/`. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~148/` (exists).

**Why.** The real sample cannot be rendered. The report contract's `document` layout (version 0.2.0) never said how a filled report names its accounts or keys its per-account values, so two workers read it two ways. The sample builder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py`) writes: top-level keys `household`, `rows`, `values`, `windows`; account entries `{account_key, last_four}`; per-account values as a bare map `{<account>: figure}`. The components (`portal/src/pages/InvestorReporting/dashboard/report/reportModel.ts` on the portal branch `wk-IRPT_DASHBD-142-portal`, read it with `git -C portal show wk-IRPT_DASHBD-142-portal:src/pages/InvestorReporting/dashboard/report/reportModel.ts`; the type `FilledReport` and its tests) read: top-level keys `household` and `values` only; account entries `{account_id, last4, first_data_date, window_status}`; household `{household_ref, as_of, first_data_date, accounts}`; a per-account (or per-class) value as `{"by_row": {<account id or asset class>: figure}}`. The components are tested and built; **the contract adopts their reading and the builder conforms to it.** (Nothing else is changed: the 117 members, the eight sections and every source stay.)

**The cell (`DB-b-182`).** A contract edit, a builder change, a rebuild. Nothing portal is edited.
1. **State the shape in the contract.** Edit `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (existing file): `contract_version` `0.3.0`; extend `lineage` with the CURRENT bytes' entry `{"contract_version": "0.2.0", "sha256": "<sha256 of the file as it stands before your edit>", "reason": "<one line: the filled-report shape stated>"}` (keep the existing 0.1.0 entry); add under `document` a key `filled_report` with EXACTLY these keys: `top_level_keys` `["household", "values"]`; `household_fields` `["household_ref", "as_of", "first_data_date", "accounts"]`; `account_entry_fields` `["account_id", "last4", "first_data_date", "window_status"]`; `window_status_values` `["MEASURED", "NOT_SPANNED", "BREAK"]`; `per_row_member_form` (a sentence: a member whose grain is an account, or an asset class, holds `{"by_row": {"<account_id or asset class>": figure}}`, a figure being a number, a text or the absent form); `window_status_rule` (a sentence: for each of the four windows, NOT_SPANNED when the account has no value on the window's opening anchor day, BREAK when a day inside the window has no return, else MEASURED, read from the return table); `first_data_date_rule` (a sentence: an account's first_data_date is the date of its first row in the account return table; the household's is the earliest of its accounts'). Also fix the old `document.shape` text where it contradicts this (it names `windows` and `rows` as top-level keys: they are no longer part of a filled report). Change no member. `bash`-free: edit with a script file under python -I, UTF-8, same indentation, trailing newline.
2. **Make the builder conform.** Edit `build_sample.py` (existing, tracked, in `~141`'s folder, in your grant): the filled report it writes has exactly the top-level keys `household` and `values`; `household` is `{household_ref, as_of, first_data_date, accounts}`; each account entry `{account_id, last4, first_data_date, window_status}` (account_id the 10-character custodian form, last4 the account's last four, first_data_date from the account's first row in the return table, window_status per the rule above, from data the builder already reads); every per-account and per-class value is wrapped `{"by_row": {...}}`. The class rows and the `windows` block are not part of a filled report any more (`hold.allocation` and the other per-class values live in `values` as by_row). Bind the contract's bytes in the build record as before.
3. **Rebuild and reconcile.** Run the builder (S3 GET and LIST only, as before) into the private folder and then overwrite `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE.json` with the new file (the render and the checker read that path; keep the old file as `HOUSEHOLD_SAMPLE.before_shape.json` beside it). The household rule is the SAME as round 94's (do not reselect: assert the same household reference hash as the current build record, else file a row and stop). Regenerate `~141/HOUSEHOLD_SAMPLE_BUILD.json` so that round 94's criterion still passes on it: `python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-2-AC1` must print PASS (counted identity checks still all within one dollar), and DB94-1, 3, 4 and 6 must still pass with the 0.3.0 contract (the checker accepts a record bound to a lineage version).
4. **Record** `SAMPLE_ALIGN.json` in your folder with exactly: `sample_sha256` (of the new private sample file); `contract_sha256` (of the contract file as you leave it); `build_record_sha256` (of the regenerated `~141/HOUSEHOLD_SAMPLE_BUILD.json`); `code` {`file` (the builder), `sha256` (its committed bytes), `tracked` true}; `accounts` (the count in the sample); `per_row_members` (the count of values holding `by_row`); `reads` {`vendor_calls` 0, `s3_writes` 0, `secret_reads` 0}; `sample_kept_private` true; `pushed` false; `served_values_changed` false; `limits`. Counts and hashes only.

<criterion id="DB97-1-AC1" cell_refs="DB-b-182"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r97/p97_round97.py" . DB97-1-AC1</invocation><expect>DB97-1-AC1 PASS</expect></criterion>
`DB97-1-AC1` -- the contract is above 0.2.0 with the 0.1.0 and 0.2.0 bytes in its lineage and `document.filled_report` stating the shape; the private sample has exactly the keys `household` and `values`, account entries with the four fields, window statuses from the enum, accounts in id order, the household first date the earliest, every member of the contract present, every per-row value wrapped in `by_row` with keys that are the household's accounts or asset classes, every contract-ABSENT member in the absent form; the record binds the sample, the contract, the builder and the regenerated build record; round 94's DB94-2-AC1 still passes; no write, no vendor call; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB97-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every portal file and the other contracts.
- **No S3 write, no vendor call, no secret read, no deploy, no push, no portal edit.** S3 GET and LIST of the irpt gold prefixes and the granted crosswalk prefix, exactly as the builder read them before.
- **Client data stays private.** The sample and its backup live only in the private folders; the repo gets counts and hashes.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W148-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (every `.py` passes `bash .tools/commit-gate.sh`); run its gates in the background and wait for them. ASCII only in anything tracked.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~148/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE_BUILD.json
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-182.filled-report-shape-stated-and-sample-conformed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 99 (round 97), cell `DB-b-182`.
<owned_cells>DB-b-182</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB97-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~148/IRPT_DASHBD.TO-DB-b-182.filled-report-shape-stated-and-sample-conformed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB97-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; DB94-1, 2, 3, 4 and 6's last lines; the new contract version; the counts (accounts, per-row members, identity checks); anything the old shape carried that the new one drops; any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a contract edit and a private rebuild; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GET and LIST with the identity the builder already used; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (contract at 0.2.0) and its shape checks are dry-run on 16 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
