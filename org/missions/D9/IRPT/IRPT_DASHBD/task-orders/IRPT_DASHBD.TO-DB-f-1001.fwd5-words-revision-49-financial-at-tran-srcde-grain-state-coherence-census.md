# TO IRPT_DASHBD.TO-DB-f-1001 -- the FWD-5 WORDS REVISION: 49 Financial mapped at tran_srcde grain (all 157 codes of the CRO classification table, each to one Opal type word or to UNMAPPED with a reason), state coherence per word, Cottonwood and Inflection carried over unchanged, and the word-boundary census repeated; a revised proposal record for the CTO to ratify, nothing written to a contract

<to_id>IRPT_DASHBD.TO-DB-f-1001</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1001</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>124</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-122 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_122_20261016.md`, msg 9036): "NOT RATIFIED. One revision is ordered ... 49 Financial's mapping at `tran_srcde` grain. Each of the 157 codes maps to exactly one Opal type word, or to `UNMAPPED` with a reason. The action word is derived from the same table ... `sb_cd` TR gets its own row, decided on the code's description, never by the `sb_cd` it sits under." | **Rows:** IRPT_DASHBD-D2-W1001-S<k> | **Decomp cell:** `DB-f-1001` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R124_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1001` (branch `wk-IRPT_DASHBD-1001`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1001/`. The folders `data/assets/scripts/gold/irpt_reporting`, `data/inf`, `docs/briefs`, `org/standards` and `org/tier1_exec/4.0.0_SA_CRO/deliverables` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files and a PROPOSAL record: no AWS call of any kind, no network, no vendor call, no secret read. No real client, household or account id and no client figure is ever written in the repo, a row or your report.

**Why.** Round 122's proposal mapped 49 Financial at the `sb_cd` grain (15 values). The CVO graded it against rule 24 and found the domain falsified: the firm's real code space is `tran_srcde`, 157 codes in the CRO classification table (187 rows, because a `tran_srcde` can appear under several `tr_cd`/`sb_cd` pairs). On that domain 56 of 187 rows sat under unmapped `sb_cd` values, and 9 of the 15 `sb_cd` values span several CRO categories while 6 of them were mapped to one word. The CTO ordered this revision. The Cottonwood (16 types) and Inflection (48 Orion descriptions) rows are NOT revisited.

**AMENDMENT 1 (the issuer's, 2026-10-16 ~05:1xZ, after the CTO's round-123 analysis, msg 9064).** The 49 Financial domain is the UNION of two sources, not the CRO table alone: (1) the CRO table's 157 distinct `tran_srcde`; (2) the codes in 49 Financial's LIVE silver, which a worker cannot read (no AWS), so the issuer read them: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/R124_LIVE_SILVER_CENSUS_49F.json` (read 2026-10-16T05:00:00Z, 572 partitions, 3,349,750 rows, 160 distinct codes). Differences: 3 codes are in the silver and not in the table (`EXWT`, `RDPC`, `SQDAJ`; the record gives their `tr_cd`, `sb_cd`, row count, day range and the transaction words their descriptions carry), and none is in the table and not in the silver. So the mapping has 160 rows. Each silver-only code gets its own row decided on those description words (a code you cannot decide is `UNMAPPED` with that reason). Every row carries three more booleans: `in_cro_table`, `in_live_silver`, `not_observed` (true exactly when the code is not in the live silver). The census adds `live_silver_distinct_tran_srcde`, `silver_only_count`, `table_only_count` and `live_read` (copy `read_at_utc`, `rows`, `partitions` from the census record). Where the text below says 157 or 221, read 160 and 224. The checker was amended to match (`checks/r124/p124_words49.py`, 13 self-test arms).

**The inputs (read, never edited).** (a0) The live census record named in AMENDMENT 1 above. (a) The CRO table `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`: a JSON list of 187 rows with `tran_srcde`, `tr_cd`, `sb_cd`, `rows`, `category`, `desc`, `rule`, `partition`. (b) The round-122 proposal `deliverables/0.9.0_WK_IRPT_DASHBD~802/FWD5_WORDS_PROPOSAL_R121.json` (its vocabulary of 21 type words and 8 action words, and its Cottonwood and Inflection rows). (c) `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`FINAL_BY_PARTITION`, about lines 230-242) for the partition-to-final map.

**The cell (`DB-f-1001`).**
1. **Print the denominator.** From the CRO table, with a short python read, print the row count, the number of distinct `tran_srcde` (157), the distinct `rule` values and the number of `tran_srcde` codes whose rows carry more than one distinct `rule` (10). Put these four numbers in your report.
2. **Map 49 Financial at `tran_srcde` grain.** One mapping row per distinct `tran_srcde` of the UNION (160 rows): `firm` "49financial", `field` "tran_srcde", `source_value` (the code exactly as the table or the census spells it, including any punctuation), `opal_type` (a word from your type list, or `UNMAPPED`), `cro_rules` (the sorted list of the distinct CRO `rule` values of that code's rows, copied from the table; the empty list for a silver-only code), `in_cro_table`, `in_live_silver`, `not_observed` (booleans, see AMENDMENT 1), and `reason`. The meaning of a code is what the CRO table gives it (its `rule`, `category` and `desc`); decide each code on its OWN description and rule, never by the `sb_cd` or `tr_cd` it sits under. `reason` is required for a silver-only code (decided on the description words the census record gives), and when the row is `UNMAPPED` (why no Opal word fits, or why the table gives no single meaning) and when the code's rows carry more than one distinct rule and you still map it to one word (why one word is right; if you cannot say, it is `UNMAPPED`). The code `TRADE` (the table's description "ADJUSTING ENTRY", category Trades) gets its own row decided on that description and says so in `reason`. No 49 Financial `action` rows: the action word is derived from the type word through the type table.
3. **The vocabulary.** Keep the round-122 words unless the 157 codes need a change; you may add a type word (each with `definition`, `action` and `flow_class` from the brief's seven classes) or retire one no row uses. A type word no row maps to is retired (the census must show no zero-count word).
4. **Carry over Cottonwood and Inflection unchanged.** Copy their rows (16 and 48, `field` "type") from the round-122 proposal byte for byte; the checker compares them to that proposal. Their words must remain defined in your type list.
5. **State coherence (iv).** `state_coherence_by_word`: an object with exactly one entry per type word in your list and one for `UNMAPPED`, each a string of 20 or more characters naming the values a single remedy does NOT move (for example, that changing the word of one code moves no other code; that a code's word change does not change the action of another word). `unmapped_policy`: one of `shown`, `excluded`, `counted`, and the `postulates.state_coherence` text says what that means for the page and the export. `cross_firm_statement`: one sentence, containing the words "another firm", stating that remapping a code of one firm never moves another firm's rows.
6. **The law record and the census.** `postulates` (exactly four strings, keys `mece`, `same_grain`, `intent_coherence`, `state_coherence`, each at least 40 characters; `mece` and `same_grain` must name the `tran_srcde` domain and print the denominator and the subtraction). `census`: `method` "word-boundary", `denominators` {"49financial": 160, "cottonwood": 16, "inflection": 48}, `denominator_total` (224), `cro_rows` (187), `cro_distinct_tran_srcde` (157), `live_silver_distinct_tran_srcde` (160), `silver_only_count` (3), `table_only_count` (0), `live_read` {`read_at_utc`, `rows`, `partitions`}, `per_type_word` (an object: each type word, and `UNMAPPED`, to the number of mapping rows with that word, over all three firms, computed from your mapping), `unmapped` (the count of `UNMAPPED` rows).
7. **Record** `FWD5_WORDS_PROPOSAL_R124.json` in your folder with EXACTLY these top-level fields: `as_of` (ISO date), `claim` (use `inferred`), `postulates`, `state_coherence_by_word`, `unmapped_policy`, `cross_firm_statement`, `opal_actions` (list of {`word`, `definition`}), `opal_types` (list of {`word`, `definition`, `action`, `flow_class`}), `mapping` (224 rows), `census`, `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0} and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Words are letters and spaces only, 2 to 41 characters. ASCII only. No run of 8 or more digits outside a `path`, `file`, `key`, `where` or `vintage` field. No account id, no client figure, no security name.

<criterion id="DBF124-1-AC1" cell_refs="DB-f-1001"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r124/p124_words49.py" . DBF124-1-AC1</invocation><expect>DBF124-1-AC1 PASS</expect></criterion>
`DBF124-1-AC1` -- the form of step 7 holds; the checker computes the 49 Financial denominator as the union of the CRO table's distinct `tran_srcde` and the live census record's codes (160): every code has exactly one mapping row at field `tran_srcde`, no row names a code the table lacks, no code is mapped twice; each row's `cro_rules` equals the table's distinct rules for that code (empty for a silver-only code) and its three membership booleans are right; a silver-only code carries a reason; every row is a defined type word or `UNMAPPED`; an `UNMAPPED` row carries a reason; a code with more than one distinct rule that is mapped to a word carries a reason; the Cottonwood and Inflection rows equal the round-122 proposal's. Base: FAIL (no record).
<criterion id="DBF124-1-AC2" cell_refs="DB-f-1001"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r124/p124_words49.py" . DBF124-1-AC2</invocation><expect>DBF124-1-AC2 PASS</expect></criterion>
`DBF124-1-AC2` -- the law record: four postulates (the `mece` and `same_grain` texts name `tran_srcde`); `state_coherence_by_word` has exactly one string of 20 or more characters per type word plus one for `UNMAPPED`; `unmapped_policy` is one of the three; `cross_firm_statement` holds the words "another firm"; every type word carries a defined action and a flow class; the census denominators, the table, silver, silver-only and table-only counts and `live_read` equal the checker's,  `per_type_word` and `unmapped` equal the counts the checker computes from the mapping; reads zero, flags false, ASCII, no digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF124-1-AC1,DBF124-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the CRO table and its note, every code file, the round-120 and round-122 records, the issuer's check.
- **A PROPOSAL, A READ.** Nothing is written to `org/standards/`; no contract is created; nothing is deployed, applied, published or pushed; no AWS call; no network. The CTO ratifies into the contract, not you.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A code the table gives no meaning is `UNMAPPED` with that reason, never a guess. If the table's counts differ from the 187 and 157 above, file a row and map what the table holds.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1001-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1001/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1001.fwd5-words-revision-49-financial-at-tran-srcde-grain-state-coherence-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R124_F.md</decomp_doc> round 124, workstream ~F2 (F-SHIP), cell `DB-f-1001`.
<owned_cells>DB-f-1001</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF124-1-AC1, DBF124-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1001/IRPT_DASHBD.TO-DB-f-1001.fwd5-words-revision-49-financial-at-tran-srcde-grain-state-coherence-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF124-1-AC1,DBF124-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the four denominator numbers of step 1 and the three silver-only codes with how you decided each; the number of type words and action words; how many of the 157 codes are UNMAPPED and the three most common reasons; how many multi-rule codes you mapped to a word and how you decided; how you decided `TRADE`; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a proposal record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF124-1-AC1 and AC2 FAIL at base (no record) and the checker's helpers are exercised by its self-test (11 arms), including the missing, duplicate, carried-row and multi-rule cases.
lane: the <paths> block IS the grant.
</preflight>
