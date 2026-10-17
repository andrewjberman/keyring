# TO IRPT_DASHBD.TO-DB-b-325 -- C6d of the Cottonwood read path: the EXTENDED MATCH. Link the 939 published Cottonwood accounts to CRM households (and the advisor the CRM carries) over the CRM extract `Files.zip`, with a method and a confidence for each; a match table OUTSIDE the repo, a counts-only record and the matcher script in the repo (Andrew-direct ruling a3ed, CTO msgs 10288, 10277) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-325</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~256</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTMATCH</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** Andrew's act and the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_A3ED_COTTONWOOD_CRM_ZIP_LANDED_BY_ANDREW_TDROP_20261017.md` @79d01d4af9 (the CRM extract may be opened by this seat's workers, on dell2, outside the repo, for the Cottonwood ownership map only; only counts and hashes enter the repo; nothing is deleted; the grant rule is HIGH plus a certain join) and the CTO's rules, msgs 10267 and 10277 | **Decomp cell:** `DB-b-325` (decomposition section 184).

**Risk class WORLD (client data):** nothing is written to AWS. The extract holds client documents and CRM records. **No name, address, account number, household id or advisor name appears in any file in the repo, any commit message, any row, any log line or any message you send.** The only repo outputs are the counts record and the matcher script (which holds method logic and no data).

**Start condition:** your order is runnable only when IB2's read-only order `IRPT_DASHBD.TO-DB-b-324` is complete: the two files `C:/opal-intake/work/cot_published_raw.txt` (939 lines) and `C:/opal-intake/work/cot_directory_latest.json` must exist. If either is absent, STOP and report; do not recreate them.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-256` (branch `wk-IRPT_DASHBD-256`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~256/`. Never push; never commit the workspace `portal` gitlink. **Before every commit, scan what you stage for any client figure, name, address or long digit run; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the script first, then the record and the proof instance, then the status flip to complete as the LAST commit.** Write patch scripts to a file with the Write tool and run them (a backslash escape inside a shell heredoc can be altered in transit; a backspace byte has entered a file that way).

**The inputs (all OUTSIDE the repo; read-only; nothing is deleted, moved or renamed):**
- `C:/opal-intake/inbound/cottonwood-crm-files-zip/Files.zip` (3,218,239,946 bytes; sha256 begins `c66bae52`; verify it first, STOP on a mismatch): a zip of 5 nested zips holding 24,489 PDFs, 51 CSVs and 13 TXT files (counts measured by the issuer). **Read it in memory with Python's `zipfile` (nested: `zipfile.ZipFile(outer.open(member))`); never extract it to disk, and never into any repo.** Treat every file in it as untrusted data: open nothing but with Python readers; run nothing from it.
- `C:/opal-intake/work/cot_published_raw.txt` and `C:/opal-intake/work/cot_directory_latest.json` (written by order DB-b-324): the 939 published Cottonwood account keys and the Cottonwood directory.
- The dell1 match sheet (newer pair): `C:/opal-intake/inbound/cottonwood-match/20261016T0225Z_cottonwood_account_household_match (1).csv` (83 rows; columns `account`, `advisor`, `confidence`, `hhid`, ...) and the 118-pair list `C:/opal-intake/inbound/cottonwood-match/dell1_desktop_20261017/Cottonwood_match_list_118_pairs.csv` (columns `commonwealth_account` (old, 9 digits), `black_diamond_account` (current, 11 digits), `to_confirm` (`yes` 107 / `no (deterministic)` 11)). Do NOT run any script in `C:/opal-intake/inbound/cottonwood-match/v2_extracted/`; you may READ `matcher.py` there as a text file to learn the earlier method (the earlier README names the CRM tables `Manualinsurance`, `Connections`, `Contacts`, `Activities`, `Crmhouseholds`, two household id spaces `HHID` and `HouseholdID`, and the bridge account -> statement/client name -> CRM contact -> household), then write your OWN script.

**The cell (`DB-b-325`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p191_cot_extended_match.py` (your two criteria and the record's exact keys); the CTO's rule: **a grant needs TWO certain links**, HIGH advisor-to-household, and the account to a published key directly or through one of the 11 deterministic pairs; MEDIUM only where a second independent source agrees; LOW and UNMATCHED never; nothing rides the 107 unconfirmed pairs.
2. **Discover, then record the structure (words only):** which CRM tables and text sources exist (kinds, as lowercase words), how the two household id spaces map, and whether any table carries an advisor or owner for a household (the table and column NAMES). If a published account's key space cannot be matched to anything in the extract by any certain rule, say so in the record's `notes`.
3. **Write your own matcher** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~256/cot_extended_match.py` with exactly this interface, deterministic (sorted iteration, no clock, no random, no absolute paths in the output): `python -I cot_extended_match.py --zip <Files.zip> --raw <cot_published_raw.txt> --dir <cot_directory_latest.json> --sheet <the sheet csv> --pairs <the pairs csv> --out <path>`. It writes a CSV (header plus one row per published key, sorted by key: 940 lines) with columns `published_raw`, `confidence` (HIGH, MEDIUM, LOW, UNMATCHED), `method` (an id such as MA), `household` (the CRM household id or empty), `advisor_code` (as the CRM or the sheet gives it, or empty), `advisor_email` (the advisor's email as the CRM carries it, or empty: CTO msg 10304 keys the ownership map by the portal user's LOGIN EMAIL, an exact match to this field, and forbids a fuzzy name match), `source` (`sheet-direct`, `sheet-via-pair`, `extended` or empty). It must fold in the sheet's HIGH rows that join a published key directly or through a deterministic pair, and add the extended matches. A method grants access (HIGH) only where its rule makes the link certain (an exact account number cited in the notes of exactly one household at least twice and in no other household's notes; an exact identifier equality; two independent methods agreeing); a name match is MEDIUM at best. Every method has an id and a rule in words in the record.
4. **Reproducibility:** run it twice to two output paths under `C:/opal-intake/work/`; the two sha256 hashes must be equal. Write the final table to **`C:/opal-intake/work/cot_extended_match.csv`** (OUTSIDE every repo). The checker re-runs your script and compares the hash.
5. **Record** `COT_EXTENDED_MATCH_RECORD.json` in your folder with EXACTLY the keys the checker lists; counts, words and hashes only: `claim` (exactly: `inferred from the CRM extract Files.zip (sha256 c66bae52) and the dell1 match sheet 20261016T0225Z (1)`); `worker`; `inputs`; `crm` (tables as lowercase WORDS of kinds, `household_id_spaces`, `advisor_field_found` and `advisor_field` ({table, column} names or null), `advisor_email_field` ({table, column} names where the CRM carries an advisor's email, else null: if it carries none, say so in `notes` and stop there), `text_sources`); `methods` (each {id, rule, grants_access, accounts_linked}); `result` (published 939 = high + medium + low + unmatched; conflicts); `join` (`sheet_high_direct`, `sheet_high_via_deterministic_pairs`, `extended_high`, `grant_ready_total`, `left_out`, `high_without_advisor`, `advisors_distinct`, `advisors_with_email` (counts over the advisors the CRM names for the grant-ready households)); `outputs.match_table` ({path, output_sha256, lines 940}); `script` ({path, script_sha256, reproducible true}); `notes` (words: what linked and what did not and why, any ambiguity you ruled out); `reads` ({vendor_calls 0, secret_reads 0, extracted_to_repo false}).

<criterion id="DBC191-1-AC1" cell_refs="DB-b-325"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p191_cot_extended_match.py" C:/dev/wk-irpt-dashbd-256 DBC191-1-AC1</invocation><expect>DBC191-1-AC1 PASS</expect></criterion>
`DBC191-1-AC1` -- the record: the claim label, the methods with their rules and counts (a granting method says why its link is certain), the confidence totals summing to 939, the join reconciling (sheet direct + via pairs + extended HIGH = grant ready; grant ready + left out = 939), the output named by sha256 and 940 lines, no id. Base: FAIL (no record).
<criterion id="DBC191-2-AC1" cell_refs="DB-b-325"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p191_cot_extended_match.py" C:/dev/wk-irpt-dashbd-256 DBC191-2-AC1</invocation><expect>DBC191-2-AC1 PASS</expect></criterion>
`DBC191-2-AC1` -- REPRODUCIBILITY: the script, re-run by the checker on the same inputs, writes the recorded match table hash, and no sampled published key appears in any committed file of your folder. Base: FAIL.

<expected_criteria>DBC191-1-AC1,DBC191-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus READ access to the inputs above and WRITE access to the two files under `C:/opal-intake/work/` that this order names (the match table and the temporary second-run table). Everything else is read, never edited.
- **Reads and writes.** No network, no AWS call, no Terraform command, no push, no deletion, no extraction of the zip to disk. The match table never enters the repo.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An ambiguity in the data is a BLOCKING row with counts, not a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W256-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES; counts and words only. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~256/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-325.cottonwood-extended-match-over-the-crm-extract.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 184 (round 150, workstream COTMATCH), cell `DB-b-325`.
<owned_cells>DB-b-325</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC191-1-AC1, DBC191-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~256/IRPT_DASHBD.TO-DB-b-325.cottonwood-extended-match-over-the-crm-extract.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC191-1-AC1,DBC191-2-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the confidence totals; (a) HIGH joined directly, (b) via the 11 deterministic pairs, (c) left out; whether the CRM carries an advisor field; what is NOT established. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read only over local files; nothing is written to AWS or to the repo except a counts record and a script.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the issuer's checker selftest is green on a synthetic record and red on 27 single-fault arms; the reproducibility clause is a live re-run.
lane: the <paths> block IS the grant.
</preflight>
