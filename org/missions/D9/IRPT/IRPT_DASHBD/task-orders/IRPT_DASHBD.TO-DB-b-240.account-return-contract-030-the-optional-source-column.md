# TO IRPT_DASHBD.TO-DB-b-240 -- the ACCOUNT RETURN CONTRACT 0.3.0, the OPTIONAL `source` column (round 120, workstream B-49F): the contract declares a nullable string column `source` whose values are words (`orion`, `computed from Black Diamond values and flows`, `computed from custodian holdings`), with its OWN schema hash, WITHOUT touching the 19 existing columns or their hash; a record names the three emitters that must add the column at their own landing; nothing is emitted or landed

<to_id>IRPT_DASHBD.TO-DB-b-240</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~194</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 120 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-120 ANALYSIS (B-49F) section 2 ruling 4 and section 3 cell 4 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md @5e358b0a8f`: "The return contract gains a `source` column (a minor bump; values are words such as `orion`, `computed from Black Diamond values and flows`, `computed from custodian holdings`), so the page can state it. The adapter's landing pair carries it") | **Rows:** IRPT_DASHBD-D2-W194-S<k> | **Decomp cell:** `DB-b-240` (decomposition section 118) | **outcome_ref:** FWD-11 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-194` (branch `wk-IRPT_DASHBD-194`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~194/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~194/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.**

**Why.** The account return contract (`org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`, version 0.2.0, 19 columns, `schema_hash` over the sorted `name:type` lines) is the table's published shape; the producer and the Inflection and Cottonwood adapters each carry their own arrow schema and check it against that hash, and every landed partition has the 19 columns. A page must be able to say where a return comes from, so the table needs a `source` column. Adding it to `columns` would change the hash every producer, adapter, test and landed partition is checked against. So the column is declared as OPTIONAL: a new top-level key `optional_columns` beside `columns`, with its own `schema_hash_with_optional` (the hash over the 19 columns plus `source:string`); the 19 columns, their hash and every existing check stay exactly as they are, and each emitter adopts the column at its OWN landing (a table written without it reads as having no source label). This cell edits the contract only and records the emitters.

**The cell (`DB-b-240`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_srccol.py` (your criteria; the contract clauses and the record's exact form are in its docstring and clauses); the contract and its `columns`, `schema_hash`, `schema_hash_basis`, `schema_hash_control`, `supersedes`; the producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` and the two adapters `adapters/inflection_account_return_daily.py` and `adapters/cottonwood_bd_account_return_daily.py` (each declares an arrow schema: find it).
2. **The contract 0.3.0.** Set `contract_version` to "0.3.0". Add the top-level key `optional_columns` = a list of ONE object {`name` "source", `type` "string", `nullable` true, `meaning` (words: where this account-day's return comes from, so a page can state it), `values` (a list that includes `orion`, `computed from Black Diamond values and flows` and `computed from custodian holdings`, as words), `rule` (words that include what an ABSENT or null `source` means: the table was written before the column existed, or the emitter has not adopted it, and the page states no source), `since_schema_version` ("1.1")}. Add `schema_hash_with_optional` = the sha256 over the sorted `name:type` lines of the 19 columns plus `source:string`, joined by newline (the method of `schema_hash_basis`; the checker recomputes it). Append to `supersedes` an entry {`contract_version` "0.2.0", `schema_hash` (the 0.2.0 `schema_hash`, unchanged), `changes` (words)}. Change NOTHING else: `columns`, `schema_hash`, `enums` and every other key stay byte-for-byte (the checker hashes the `columns` and recomputes `schema_hash`).
3. **The record** `RD_SOURCE_COLUMN_R120.json` in your folder with EXACTLY these fields: `contract_version` ("0.3.0"); `optional_column` {`name` "source", `type` "string", `values` (the list)}; `hash_with_optional` (equal to the contract's); `emitters` (a list of exactly 3, in this order, each {`file`, `kind` ("producer" or "adapter"), `schema_line` (the integer line in that file where its arrow schema or column list is declared; the checker confirms the line mentions the schema), `must_add_at_landing` true, `words` (what that emitter changes to carry the column and what it must NOT change: its 19-column hash for tables already landed)}): `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py`, `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py`; `words` (one paragraph); `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `schema_hash`, `hash_with_optional` or `line` field.

<criterion id="DB120-4-AC1" cell_refs="DB-b-240"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_srccol.py" . DB120-4-AC1</invocation><expect>DB120-4-AC1 PASS</expect></criterion>
`DB120-4-AC1` -- the contract reads 0.3.0; its 19 `columns` and their `schema_hash` are unchanged (the checker recomputes the hash and hashes the column definitions); `optional_columns` holds exactly `source` (string, nullable, meaning, rule, since_schema_version, and the three required values); `schema_hash_with_optional` equals the recomputed hash over the 19 columns plus `source:string`; `supersedes` carries the 0.2.0 entry. Base: FAIL (version 0.2.0).
<criterion id="DB120-4-AC2" cell_refs="DB-b-240"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_srccol.py" . DB120-4-AC2</invocation><expect>DB120-4-AC2 PASS</expect></criterion>
`DB120-4-AC2` -- `RD_SOURCE_COLUMN_R120.json` has exactly the form of step 3; its `hash_with_optional` equals the contract's; it names the producer and the two adapters in order, each with a schema line that exists in its file and mentions the schema; the flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB120-4-AC1,DB120-4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the producer, both adapters and their tests, every other contract, the module `filled_report_values.py`, `lib/`, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. No S3, no AWS, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the hash method does not reproduce the contract's own `schema_hash` over the 19 columns (the checker's `schema_hash` does), file a BLOCKING row with both hashes and stop. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W194-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~194/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-240.account-return-contract-030-the-optional-source-column.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 118 (round 120, workstream B-49F), cell `DB-b-240`.
<owned_cells>DB-b-240</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB120-4-AC1, DB120-4-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~194/IRPT_DASHBD.TO-DB-b-240.account-return-contract-030-the-optional-source-column.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB120-4-AC1,DB120-4-AC2` (the two ids as ONE comma-joined argument) BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the two hashes (the unchanged one and the new one, first 12 characters); the three emitters' schema lines; reads and writes. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract text and a record in a branch; nothing is wired, emitted, landed or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; no AWS is read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms for each clause); DB120-4-AC1 and AC2 FAIL at base (version 0.2.0, no record) and the checker's clauses are exercised by its self-test (hash arms, a red contract arm, a green and six red record arms).
lane: the <paths> block IS the grant.
</preflight>
