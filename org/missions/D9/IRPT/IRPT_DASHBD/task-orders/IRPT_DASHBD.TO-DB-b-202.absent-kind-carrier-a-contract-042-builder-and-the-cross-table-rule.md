# TO IRPT_DASHBD.TO-DB-b-202 -- the DATA HALF of the absent kind: contract 0.4.2 (Carrier A, the closed set of three kinds, the UNHELD value and its dash rule), the sample builder writes `kind`, fills the activity members that another table of the same report already prints, and the report's figures agree across tables

<to_id>IRPT_DASHBD.TO-DB-b-202</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~167</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>105</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-105 ANALYSIS item 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_105_20261014.md`, section 1 row "The absent kind" and section 2 cell 2) | **Rows:** IRPT_DASHBD-D2-W167-S<k> | **Decomp cell:** `DB-b-202` (decomposition section 107) | **outcome_ref:** FWD-21 | **depends_on:** none. The next order of your queue, `DB-b-203` (the view half), reads what you build; it stays `staged` until this one is complete.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-167` (branch `wk-IRPT_DASHBD-167`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report.

**Why.** The CVO graded the render's last judgment criterion FAIL because the report contradicts itself: the Activity Summary table prints "Not available yet" for Beginning Value and Net Gain (household and each account) under a note saying they "need more history", while the Portfolio Value Summary and the account value summaries print the same last-12-month Beginning Value and Net Gain on other pages. The CTO ruled the CAUSE is partly wording and partly data: (1) the kind of an absence is inferred from reason text; it becomes a FIELD; (2) a figure the report prints in one table must not be absent in another. Your cell is the DATA half; the view half is your next order.

**The ruling you implement (CTO, adopted).** Carrier A: an absent form is exactly `{"absent": "<words>", "kind": "<KIND>"}`. The closed set has THREE members: `NO_SOURCE_YET` (Opal has no source for the figure yet), `INSUFFICIENT_HISTORY` (the source holds too little history for the period; the remedy is time), `SOURCE_BREAK` (a source repair is the remedy: a missing row, a lagging row, a null return, a disagreeing guard). `NOT_HELD` is NOT a kind: an asset class the household holds none of is a VALUE, the text `UNHELD`, inside the `by_row` asset-class map (never an absent form); it prints the baseline's dash. `NOT_APPLICABLE` is not adopted (0 members on the sample).

**The cell (`DB-b-202`).**
1. **Read first.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~163/ABSENT_KIND_PROPOSAL.md` (the proposal: its carrier, its MECE tally), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (version 0.4.1; `document.absent_rule`, `document.filled_report`), the issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py` (your criterion: read `check_kind`, `check_sample_shape_k`, `kind_problems`, `cross_table_conflicts`; you may run `python -I <that file> --selftest .` from your root), and the previous builder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/build_sample.py` (its header states every rule and every read; do not change a rule that is not named here). The previous sample is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/HOUSEHOLD_SAMPLE.json` (read-only; the checker's rule finds 8 cross-table conflicts in it: act.beginning_value and act.net_gain, household and each of the 3 accounts, against pvs.last_12_months.* and avs.last_12_months.*).
2. **Contract 0.4.2** (the contract is YOURS to edit; no other file under `org/standards/`). Set `contract_version` to `0.4.2`; add the 0.4.1 bytes to `lineage` the way the existing entries are written (`{"contract_version": "0.4.1", "sha256": "c43306eb8681648025fbdbe548afc9de3d175d132ab9db81afcc42f0630124e5", ...}`); add `document.absent_kinds` = the list `["NO_SOURCE_YET", "INSUFFICIENT_HISTORY", "SOURCE_BREAK"]`; add `document.unheld_rule` (one or two sentences: in a `by_row` asset-class map an entry holding the text `UNHELD` means the household holds none of that class and prints the baseline's dash, never "Not available yet" and never zero; the text must contain the words `UNHELD`, `dash` and `by_row`); rewrite `document.absent_rule` so it names the `kind` field and the three members (the word `NOT_HELD` appears nowhere in `document`); update `document.filled_report.per_row_member_form` for the UNHELD text. NO member changes: every member in `members` stays byte-for-byte the 0.4.1 member. Valid JSON, ASCII.
3. **The builder.** Copy `~159/build_sample.py` to `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/build_sample.py` and edit YOUR copy only (`git add` it: it must be tracked). (a) `Absent` carries a `kind`; the emitted form is `{"absent": reason, "kind": KIND}`; the builder's own `is_absent_form`, `fully_absent`, counting and validation read the new form. (b) Assign the kind at EVERY site that creates an `Absent`, by this table: `INSUFFICIENT_HISTORY` for a reason that begins "history not yet built" and for a window the account did not span (NOT_SPANNED); `SOURCE_BREAK` for SOURCE_LAG on the anchor or on R, a missing row or a SOURCE_LAG flow on a window day, a null `total_return_daily`, a GRADED_DISAGREED guard state, and any BREAK window; `NO_SOURCE_YET` for every member the contract sources to ABSENT, every member outside the grant (the client summary, dim_return_method), the fee-basis label and any figure no table yet carries; a household sum absent because an account term is absent takes the kind of that account term. List your site-by-site assignment in the record. (c) The by_row asset-class entry for a class the household holds none of becomes the text `UNHELD` (it was an absent form with the reason "no holding in this asset class on as_of"); the shape rule keeps `UNHELD` only inside an asset-class key. (d) FILL, do not re-explain: `act.beginning_value`, `act.net_gain` and `act.ending_value` at household grain and at account grain are the SAME last-12-month window figure the builder already computes for `pvs.last_12_months.*` and `avs.last_12_months.*`; take their values from those same folds (no second derivation). `act.contributions`, `act.withdrawals`, `act.income` and every `hold.net_gain_*` and `hold.return_*` member stay absent with their TRUE kind: where the reason is the activity table's short history the kind is `INSUFFICIENT_HISTORY`, and the reason words must not claim that a figure the report prints elsewhere is missing. (e) The model benchmark members and the 12-month chart stay exactly as in `~159` (a later cell replaces that code with a reader).
4. **Build the sample.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/build_sample.py . --out C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~167/` (the builder's header names its flags; the default firm is 49financial; run it in the background and wait for its summary: it LISTs and GETs S3 as `~159` did, nothing more). It writes `HOUSEHOLD_SAMPLE.json` there. The sample must pass the issuer's `check_sample_shape_k`, have no cross-table conflict, carry at least two kinds, and carry at least one `UNHELD` entry.
5. **Record** `KIND_CARRIER_R105.json` in your folder with exactly: `contract` {`version` "0.4.2", `sha256`}; `sample` {`path` (the private path), `sha256`, `contract_sha256` (the contract's sha256 at the time of the build)}; `absent_by_kind` {`NO_SOURCE_YET`, `INSUFFICIENT_HISTORY`, `SOURCE_BREAK`: integer counts over EVERY absent form of the sample, members and by_row entries; the checker recomputes them}; `unheld_entries` (integer); `cross_table` {`pairs_checked` 6, `conflicts` 0}; `kind_sites` (a list of {`site`, `kind`, `why`} words, one per `Absent` creation site you assigned); `builder` {`file`, `sha256`, `tracked` true}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure; no run of 8 or more digits except in a `sha256` value or a `path`, `file`, `key` or `commit` field.

<criterion id="DB105-1-AC1" cell_refs="DB-b-202"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py" . DB105-1-AC1</invocation><expect>DB105-1-AC1 PASS</expect></criterion>
`DB105-1-AC1` -- the contract is 0.4.2 with the 0.4.1 bytes in its lineage, `absent_kinds` the three members, an `unheld_rule` naming UNHELD, the dash and by_row, an `absent_rule` naming kind and never NOT_HELD, every member byte-for-byte the 0.4.1 member (compared with the 0.4.1 version in git history); the private sample exists outside the repo, is bound to its sha256 and to the contract's, passes the kind-aware shape rule, every absent form is exactly {absent, kind} with a kind of the three, a reason beginning "history not yet built" is INSUFFICIENT_HISTORY, a member the contract sources to ABSENT is NO_SOURCE_YET, no unheld class is an absent form; the cross-table rule finds 0 conflicts across its 6 pairs; absent_by_kind equals the checker's count with remainder 0 and at least two kinds appear; unheld_entries equals the checker's count and is at least 1; the builder is the tracked copy in your folder, hashed, and writes the kind; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB105-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~159/build_sample.py`, every other contract, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files and the S3 GET and LIST the `~159` builder's header lists (nothing else; a denial is recorded verbatim, not retried by another route). Writes: the repo files of the grant and the private folder named above. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no `bun install`.
- **Client data.** The sample is client data: counts only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A cross-table pair whose two figures GENUINELY differ (both filled, different values) is a finding: file a row naming the pair and stop on that point; never plug a value. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W167-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-202.absent-kind-carrier-a-contract-042-builder-and-the-cross-table-rule.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 107 (round 105), cell `DB-b-202`.
<owned_cells>DB-b-202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB105-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/IRPT_DASHBD.TO-DB-b-202.absent-kind-carrier-a-contract-042-builder-and-the-cross-table-rule.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB105-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the contract change (version, lineage, the three kinds, the unheld rule); the count of absent forms by kind and of UNHELD entries; the cross-table pairs you filled and how (the same fold); each `Absent` site you assigned and any you were unsure of; any pair whose two figures genuinely differed; the builder's run summary; row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract edit, a private builder copy and a private sample; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 GET and LIST by the same builder `~159` ran, no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB105-1-AC1 FAILS at base (no record) and the checker's pure functions are exercised by its own self-test (14 arms, green and red) and by a real red arm on the round-104 sample (8 conflicts).
lane: the <paths> block IS the grant.
</preflight>
