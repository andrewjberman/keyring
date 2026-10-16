# TO IRPT_DASHBD.TO-DB-f-802 -- the FWD-5 WORDS PROPOSAL: Opal's closed set of transaction type words (each carrying its action and flow class), a per-firm mapping table in which every source value from the round-120 record maps to exactly one Opal type word or to UNMAPPED with a reason, and the taxonomy-law (rule 24) record with a word-boundary census over the measured denominator; a proposal record for the CTO to ratify, nothing written to a contract

<to_id>IRPT_DASHBD.TO-DB-f-802</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~802</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-120 analysis for F-SHIP ruling 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_120_20261016.md`, msg 8917: "`~F2` PROPOSES and this seat RATIFIES ... a per-firm mapping table in which every source value maps to exactly one Opal word or to `UNMAPPED` with a reason. That last condition is the subtraction: a source value with no row voids the proposal. Action words: a firm with no action field gets its action DERIVED from the type value through the same table, never typed by hand.") | **Rows:** IRPT_DASHBD-D2-W802-S<k> | **Decomp cell:** `DB-f-802` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R122_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-802` (branch `wk-IRPT_DASHBD-802`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~802/`. The folders `data/assets/scripts/gold/irpt_reporting`, `data/inf`, `docs/briefs`, `org/standards` and `org/tier1_exec/4.0.0_SA_CRO/deliverables` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files and a PROPOSAL record: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** FWD-5 (transactions browse, filter, sort, export): the PRD's ACCEPT shows each transaction's action and type "in Opal's own words ... not the custodian's codes". No file defines those words (round 120, `deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json`, field `opal_vocab_home`). The transaction contract cannot be written without them, and a value-enum proposal "arrives with its four-postulate record and a word-boundary token census, or it is not a proposal" (CLAUDE.md rule 24). The CTO ratifies this proposal into the contract after you.

**The denominator (do not change it).** `deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json`: per firm the `action_codes` and `type_codes` lists (49 Financial 3 action + 15 type, Cottonwood 0 + 16, Inflection 0 + 48; 82 values in all) and `brief_flow_classes.count` (7, listed at `docs/briefs/reporting-dashboard-backend-brief-20260930.md` line 78). The population your mapping must cover is exactly that list: no value added, none left out.

**The cell (`DB-f-802`).**
1. **Read the meanings.** 49 Financial: the CRO classification table under `org/tier1_exec/4.0.0_SA_CRO/deliverables/` whose name carries `SCHWAB_TRANSACTION_CODE_CLASSIFICATION` (rows with tr_cd, sb_cd, category, rule, desc), and `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`FINAL_BY_PARTITION`, about lines 230-242). Cottonwood: `TYPE_CLASS` and `WORD_SIGN` in `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (about lines 94-115). Inflection: `data/inf/scripts/silver/orion_cashflow_taxonomy.yaml` (each entry's description and bucket). The 7 flow classes: the brief line above. Use `comp-find --files '<term>' <folder> --limit 20` for any search and print each denominator you cite.
2. **Define Opal's words.** Propose ONE closed list of Opal TYPE words (plain English a client reads, 1 to 3 words each, ASCII, for example the family of deposit, withdrawal, transfer in, transfer out, buy, sell, dividend, interest, fee, tax withheld, corporate action, journal, adjustment; the list is yours to propose, and as short as the denominator allows) and ONE closed list of Opal ACTION words (a handful, for example contribution, distribution, trade, income, fee, transfer, adjustment). Each type word carries: `definition` (one plain sentence), `action` (one action word from your action list) and `flow_class` (one of the brief's 7 flow classes, by the brief's own name). An action is therefore DERIVED from the type through this one table, never typed on a transaction by hand.
3. **Map every source value.** One row per value in the denominator (82 rows when the record is unchanged): `firm`, `field` ("type" or "action"), `source_value` (exactly as the round-120 record spells it), and for a type value `opal_type` (a word from your type list) or `UNMAPPED`; for an action value (49 Financial's `tr_cd` markers) `opal_action` (a word from your action list) or `UNMAPPED`. A row mapped to `UNMAPPED` carries `reason` (why no Opal word fits, or why the value is a marker rather than a type). A mapping is the meaning the repository's own tables give the value, read at the line you cite in `reason` or in the definition; where the repository gives no meaning for a value, it is `UNMAPPED` with that reason, never a guess.
4. **The law record.** `postulates` holds exactly four strings, keys `mece`, `same_grain`, `intent_coherence`, `state_coherence`, each at least 40 characters: (i) MECE over a DECLARED domain (name the domain, the denominator, and the uncovered-member hunt BY SUBTRACTION: how the 82 were checked against the mapping); (ii) same grain (the enum's grain: one transaction line, not one transaction group); (iii) intent coherence (one axis: what a transaction IS, not what it does to the portfolio's return; flow class is a separate axis); (iv) state coherence (name which values one remedy does NOT move: for example a value moved from UNMAPPED to a word changes no other row). `census`: `method` "word-boundary", `denominator_total` (the count of the round-120 values), `brief_flow_classes` (the record's count), `per_type_word` (an object: each Opal type word, and `UNMAPPED`, to the number of type rows mapped to it, computed from your mapping), `unmapped` (the number of rows, type or action, mapped to `UNMAPPED`).
5. **Record** `FWD5_WORDS_PROPOSAL_R121.json` in your folder with EXACTLY these top-level fields: `as_of` (ISO date), `claim` (one of `measured`, `inferred`, `held`, `absent`; use `inferred`), `postulates`, `opal_actions` (list of {`word`, `definition`}), `opal_types` (list of {`word`, `definition`, `action`, `flow_class`}), `mapping` (list of rows as step 3), `census`, `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Words are letters and spaces only, 2 to 41 characters. No run of 8 or more digits outside a `path`, `file`, `key`, `where` or `vintage` field; ASCII only; no account id, no client figure, no security name.

<criterion id="DBF122-1-AC1" cell_refs="DB-f-802"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r122/p122_words.py" . DBF122-1-AC1</invocation><expect>DBF122-1-AC1 PASS</expect></criterion>
`DBF122-1-AC1` -- the form of step 5 holds; the checker computes the subtraction from the round-120 record: every (firm, field, source value) in it has exactly one mapping row, no row names a value the record does not hold, no value is mapped twice; every type word and action word a row uses is defined in the lists, each type word carries a defined action and a flow class, and an `UNMAPPED` row carries a non-empty reason. Base: FAIL (no record).
<criterion id="DBF122-1-AC2" cell_refs="DB-f-802"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r122/p122_words.py" . DBF122-1-AC2</invocation><expect>DBF122-1-AC2 PASS</expect></criterion>
`DBF122-1-AC2` -- the law record: `postulates` has exactly the four keys, each 40 characters or more; the census method is word-boundary; `denominator_total` equals the round-120 population, `brief_flow_classes` equals the record's count, `per_type_word` equals the counts the checker computes from your mapping, and `unmapped` equals its count of `UNMAPPED` rows; the reads block is all zero, the four flags are false, the record is ASCII with no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF122-1-AC1,DBF122-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, table, brief, the round-120 record, the issuer's check.
- **A PROPOSAL, A READ.** Nothing is written to `org/standards/`, no contract file is created, nothing is deployed, applied, published or pushed; no AWS call; no network. The CTO ratifies into the contract, not you.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A zero is never read as "does not exist" without the tool's printed denominator beside it. If the round-120 record's denominator seems wrong, file a row and still map what it holds.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W802-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~802/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-802.fwd5-opal-action-and-type-words-proposal-rule24-record-and-per-firm-mapping.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R122_F.md</decomp_doc> round 122, workstream ~F2 (F-SHIP), cell `DB-f-802`.
<owned_cells>DB-f-802</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF122-1-AC1, DBF122-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~802/IRPT_DASHBD.TO-DB-f-802.fwd5-opal-action-and-type-words-proposal-rule24-record-and-per-firm-mapping.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF122-1-AC1,DBF122-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the number of Opal type words and action words; how many rows are UNMAPPED and the two most common reasons; the per-firm row counts; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a proposal record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF122-1-AC1 and AC2 FAIL at base (no record) and the checker's helpers are exercised by its self-test (9 arms), including the missing, duplicate and undefined-word cases.
lane: the <paths> block IS the grant.
</preflight>
