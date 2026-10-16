# TO IRPT_DASHBD.TO-DB-f-1402 -- the FWD-5 COTTONWOOD WORDS RE-CUT: the type word decided on the (Transaction Type, Transaction Sub Type) pair (33 pairs, denominator printed from the live data), the action word taken from the vendor's Action column (87 values), each mapped exactly once or to UNMAPPED with a reason, flow class per code from the vendor's External Flow column, state coherence per word, and the rule-24 record and token census repeated for Cottonwood only; a revised proposal record for the CTO to ratify, nothing written to a contract

<to_id>IRPT_DASHBD.TO-DB-f-1402</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1402</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>128</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-126 analysis for F-SHIP (msg 9133, ruling 2: "Cottonwood's ratified words are SUSPENDED and re-cut at the true grain ... The type word is decided on the finest code that changes meaning: the (`Type`, `Sub Type`) pair, with its denominator printed from the live data. The action word comes from `Action` (87 values), each mapped exactly once or to `UNMAPPED` with a reason. The flow class is per code. The rule-24 record and token census are repeated for Cottonwood only. 49 Financial and Inflection stay RATIFIED.") | **Rows:** IRPT_DASHBD-D2-W1402-S<k> | **Decomp cell:** `DB-f-1402` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R128_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1402` (branch `wk-IRPT_DASHBD-1402`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1402/`. The folders `data/assets/scripts/gold/irpt_reporting`, `docs/briefs` and `org/standards` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. You read NO source (no AWS, no network, no vendor call, no secret read): the live read is the issuer's, recorded in the census, and you work from it. No real client, household or account id, no client figure and no security name in the repo, a row or your report.

**Why.** Round 124 ratified Cottonwood's words at the coarse grain: the 16 `Transaction Type` values, mapped alone (round 122 proposal, carried unchanged). The CVO's read of the live table found the true code space is finer: `Transaction Type` has 16 values, `Transaction Sub Type` 31 and `Action` 87, and the pairs of type and sub type are 33. A word per type alone merges lines that mean different things (the same fault the CVO found for 49 Financial's `sb_cd` in round 122), and the action must come from the vendor's own `Action` column, not be derived from the type. The CTO suspended the Cottonwood words and ordered this re-cut.

**The inputs (read, never edited).** (a) The live census `deliverables/2.0.0_SA_COO~F2/R128_LIVE_SOURCE_CENSUS_3FIRMS.json`, section `firms.cottonwood`: `pairs` (33 objects: `transaction_type`, `transaction_sub_type`, `rows`, `external_flow`: the row count per External Flow value `Contribution`, `Withdrawal` or `None`), `values.Action` (87 values with row counts), `values["Transaction Type"]` and `values["Transaction Sub Type"]`, and the counts; read at 2026-10-16 from 125 partitions. (b) The ratified vocabulary `deliverables/0.9.0_WK_IRPT_DASHBD~1001/FWD5_WORDS_PROPOSAL_R124.json`: 21 type words and 8 action words (with definitions; you reuse them and may ADD words, each with a definition). (c) The adapter `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (`TYPE_CLASS`, `WORD_SIGN`, about lines 91-115: how the code treats the types and the External Flow words). (d) The checker `deliverables/2.0.0_SA_COO~F2/checks/r128/p128_cwwords.py` (read it first; its reason line tells you what to fix).

**The cell (`DB-f-1402`).**
1. **Print the denominators** from the census with a short python read and put them in your report: the number of distinct `Transaction Type`, `Transaction Sub Type` and `Action` values and the number of distinct pairs.
2. **Map the 33 pairs.** One mapping row per pair: `firm` "cottonwood", `field` "type_pair", `source_value` the pair spelled `<Transaction Type> | <Transaction Sub Type>` (a space, a bar, a space; exactly the census's strings), `opal_type` (a word from the ratified 21, a word you add, or `UNMAPPED`), `flow_class_none`, and `reason`. The type word is decided on the PAIR (the finest code that changes meaning): two pairs under one type may get different words. `reason` is required when the row is `UNMAPPED` (why no word fits; a pair you cannot decide from its vendor words is `UNMAPPED`, never a guess).
3. **Flow class, per code, from the vendor's External Flow column.** The vendor marks a line's external flow as `Contribution`, `Withdrawal` or `None`, and the code treats `Contribution` as money in and `Withdrawal` as money out. So a line's flow class is **EXTERNAL_IN when its External Flow is Contribution, EXTERNAL_OUT when it is Withdrawal, and, when it is None, the pair's own class** `flow_class_none`: one of INTERNAL, INCOME, FEE, CORPORATE_ACTION or UNRESOLVED (never EXTERNAL_IN or EXTERNAL_OUT). `flow_class_none` is **null exactly when the pair has no `None` rows in its `external_flow`** (a pair that is only ever Contribution or Withdrawal). Record the rule once as `external_flow_rule`: `{"Contribution": "EXTERNAL_IN", "Withdrawal": "EXTERNAL_OUT"}`.
4. **Map the 87 Action values.** One mapping row per Action value: `firm` "cottonwood", `field` "action", `source_value` (exactly the census's string, including any trailing space or punctuation), `opal_action` (a word from the ratified 8, a word you add, or `UNMAPPED`), and `reason` (required for `UNMAPPED`). The action word comes from the Action value, not from the type.
5. **Added words.** `opal_types_added` and `opal_actions_added`: lists of {`word`, `definition`} (empty lists if you add none); a word is letters and spaces only, 2 to 41 characters, not a duplicate of a ratified word. `unmapped_display`: "Unclassified".
6. **State coherence (iv).** `state_coherence_by_word`: an object with exactly one entry per type word USED in your type mapping and one for `UNMAPPED`, and `state_coherence_by_action`: exactly one entry per action word used in your action mapping and one for `UNMAPPED`; each a string of 20 or more characters naming the values a single remedy does NOT move (for example, that remapping one pair moves no other pair, no action value and no other firm's row).
7. **The law record and the census.** `postulates` (exactly four strings, keys `mece`, `same_grain`, `intent_coherence`, `state_coherence`, each 40 or more characters; `mece` and `same_grain` must name the "Transaction Sub Type" grain and `mece` the "Action" domain, with the denominators and the subtraction). `census`: `method` "word-boundary"; `denominators` {"type_pairs": 33, "actions": 87}; `distinct` {"transaction_type": 16, "transaction_sub_type": 31, "action": 87} copied from the census record's counts; `per_type_word` (an object: each type word and `UNMAPPED` to the number of pair rows with it), `per_action_word` (the same for action words), `unmapped` {"type_pairs": n, "actions": n}.
8. **Record** `FWD5_WORDS_COTTONWOOD_R128.json` in your folder with EXACTLY these top-level fields: `as_of` (ISO date), `claim` (`inferred`), `postulates`, `opal_types_added`, `opal_actions_added`, `external_flow_rule`, `unmapped_display`, `mapping` (120 rows when you add none: 33 + 87), `state_coherence_by_word`, `state_coherence_by_action`, `census`, `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0} and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. ASCII only. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `vintage`, `rows`, `partitions_read` or `read_at_utc` field. No account id, no client figure, no security name.

<criterion id="DBF128-2-AC1" cell_refs="DB-f-1402"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r128/p128_cwwords.py" . DBF128-2-AC1</invocation><expect>DBF128-2-AC1 PASS</expect></criterion>
`DBF128-2-AC1` -- the form of step 8 holds; the checker computes the Cottonwood denominators from the live census (the 33 distinct type and sub-type pairs and the 87 Action values): every pair and every Action value has exactly one mapping row, no row names a value the census lacks, none is mapped twice; every type word and action word used is defined (ratified or added) or `UNMAPPED` with a reason; each pair's `flow_class_none` is null exactly when the census shows no External Flow `None` rows for it and one of INTERNAL, INCOME, FEE, CORPORATE_ACTION or UNRESOLVED otherwise. Base: FAIL (no record).
<criterion id="DBF128-2-AC2" cell_refs="DB-f-1402"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r128/p128_cwwords.py" . DBF128-2-AC2</invocation><expect>DBF128-2-AC2 PASS</expect></criterion>
`DBF128-2-AC2` -- the law record: four postulates (the `mece` and `same_grain` texts name the Transaction Sub Type grain, `mece` the Action domain); `external_flow_rule` is the one rule of step 3; `unmapped_display` is `Unclassified`; the two state-coherence objects have exactly one string of 20 or more characters per word used plus one for `UNMAPPED`; the census method is word-boundary and its denominators, distinct counts, per-word counts and unmapped counts equal the checker's from the census record and the mapping; reads zero, flags false, ASCII, no digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF128-2-AC1,DBF128-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the census, the ratified proposal, the adapter, the contract and producer in flight, the brief, the issuer's checker.
- **A PROPOSAL.** Nothing is written to `org/standards/`; no contract file is touched; nothing is deployed, applied, published or pushed; no AWS call by you; no network. The CTO ratifies, not you.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A value the vendor's words give no meaning is `UNMAPPED` with that reason, never a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1402-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1402/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1402.fwd5-cottonwood-words-recut-type-subtype-pairs-and-action-values.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R128_F.md</decomp_doc> round 128, workstream ~F2 (F-SHIP), cell `DB-f-1402`.
<owned_cells>DB-f-1402</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF128-2-AC1, DBF128-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1402/IRPT_DASHBD.TO-DB-f-1402.fwd5-cottonwood-words-recut-type-subtype-pairs-and-action-values.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF128-2-AC1,DBF128-2-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the step-1 denominators; how many type words and action words you added; how many pairs and Action values are UNMAPPED and the most common reasons; how you set `flow_class_none` for the pairs that carry both Contribution and None rows; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a proposal record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call by the worker and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF128-2-AC1 and AC2 FAIL at base (no record) and the checker's helpers are exercised by its self-test (11 arms).
lane: the <paths> block IS the grant.
</preflight>
