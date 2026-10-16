# TO IRPT_DASHBD.TO-DB-f-1901 -- the FWD-5 TRANSACTION CONTRACT 0.4.2, A DIRECT ACT: the CTO's final S6 ruling (ADDENDUM 2, msg 9382) is recorded in the contract: both legs of the Dividend Paid from Cash / Income Paid event stay INTERNAL, `round_132_censuses.s6_status` reads `RULED_INTERNAL`, and a new `s6_ruling` section cites the addendum, its pin, the census v2 counts and the release pair's one criterion; no flow class, column, producer or hash changes

<to_id>IRPT_DASHBD.TO-DB-f-1901</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1901</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>133</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, ADDENDUM 2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_131_20261016.md` @a5475b2fdd (msg 9382): "Census v2 shows two legs of one event (14,920 of 14,920). The income is booked by Dividend to Cash (INCOME), so both legs stay INTERNAL; counting them as income would count the dividend twice. Set contract s6_status to RULED_INTERNAL citing this addendum. The release pair carries one criterion: per event, the two legs' signed amounts sum to zero, printed as N of 14,920; any miss stops the release." | **Rows:** IRPT_DASHBD-D2-W1901-S<k> | **Decomp cell:** `DB-f-1901` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R133_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1901` (branch `wk-IRPT_DASHBD-1901`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1901/`. The folders `org/standards`, `lib`, `data/assets/scripts/gold/irpt_reporting`, `data/inf` and `infra/logic` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. **You have NO AWS in this order: make no AWS call of any kind.** No real client, household or account id, no client figure and no security name anywhere.

**Why.** The contract 0.4.1 on trunk records the S6 census as measured and states `s6_status` `REOPENED_FOR_CTO` (the CTO's own 95 percent test fired). The CTO has since ruled it final: INTERNAL, because the two descriptions are two legs of one event and the income is booked by `Dividend to Cash`. The contract must say so. Nothing else changes: no producer, no column, no flow class, no hash.

**The inputs (read, never edited).** (a) The contract 0.4.1 on trunk and its generator `deliverables/0.9.0_WK_IRPT_DASHBD~1801/gen_transaction_contract_0_4_1.py` (copy it to `gen_transaction_contract_0_4_2.py` in YOUR folder and change it; never edit the contract by hand); (b) `data/assets/scripts/gold/irpt_reporting/transaction_words.json`; (c) the issuer's records in `deliverables/2.0.0_SA_COO~F2/`: `R132_INFLECTION_S6_CENSUS_V2.json` (the census v2), `R132_INFLECTION_PAIRING_CENSUS.json`; (d) the checker `deliverables/2.0.0_SA_COO~F2/checks/r133/p133_contract.py` (**read it first; it states every rule; its reason lines tell you what to fix; it has a `--selftest`**).

**The cell (`DB-f-1901`).**
1. Adapt the generator to `gen_transaction_contract_0_4_2.py` and run it: it writes the contract AND `transaction_words.json`. Changes from 0.4.1, and only these: `contract_version` "0.4.2"; `supersedes` begins "0.4.1"; `authored_by` your serial; `round_132_censuses.s6_status` is "RULED_INTERNAL" when the two descriptions' paired rows over their total rows is below 0.95 (it stays "STANDS" at or above 0.95; `offsets_status` unchanged); `served_note` gains one sentence naming the ruling; and a NEW top-level key `s6_ruling` (the checker's `KEYS` list is the list) equal to: `{"addendum": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_131_20261016.md", "addendum_number": 2, "pin": "a5475b2fdd", "class": "INTERNAL", "descriptions": [the two description names, sorted], "rows_per_description": {name: rows}, "legs_with_the_other_legs_key": {name: same_key_as_a_row_of_the_other_description}, "income_booked_by": "Dividend to Cash", "reason": ..., "release_criterion": ...}` with the two count objects copied unchanged from `R132_INFLECTION_S6_CENSUS_V2.json` `per_description`. The `reason` is one or two sentences: the two descriptions are two legs of one event (every row of each has a row of the other with the same account, day and absolute amount) and counting a leg as income would count the dividend twice. The `release_criterion` is one sentence: per event the two legs' signed amounts sum to zero, printed as N of 14,920 (use the figure with its thousands comma, from the census), and any miss stops the release.
2. The words file keeps its sections; its `contract_version` becomes "0.4.2" (the checker compares it). Two runs of the generator are byte-identical.
3. Do not touch any other file. Run `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r132/p132_dates.py" . DBF132-1-AC2` and `python -I ".../checks/r132/p132_inflection.py" . DBF132-1-AC3` once each as a regression check (both PASSED before and must still print PASS); report their last lines.

<criterion id="DBF133-1-AC1" cell_refs="DB-f-1901" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r133/p133_contract.py" . DBF133-1-AC1</invocation><expect>DBF133-1-AC1 PASS</expect></criterion>
`DBF133-1-AC1` -- the contract 0.4.2 in one verdict: its form (the keys, version 0.4.2 superseding 0.4.1, the same 18 columns and schema hash), then every binding of 0.4.1 (keys, row filter and offset rule, the Inflection flow rule table, the 49 Financial classes, the Cottonwood section, reads, coverage, `business_date_rule`, `price_rule`, the census records, the words file equal to the contract's sections) plus `round_132_censuses.s6_status` `RULED_INTERNAL` and the `s6_ruling` section equal to the CTO addendum's terms and the census v2's counts. Base: FAIL (the contract is 0.4.1).

<expected_criteria>DBF133-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **AWS: none.** No call, no listing, no write.
- **NOT WIRED.** No producer is touched; the contract says `served` false.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1901-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write. ONE commit set. If a commit is refused because the order is `complete`, stop and report; the issuer reopens it.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1901/
org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/transaction_words.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1901.fwd5-contract-0-4-2-s6-ruled-internal-direct-act.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R133_F.md</decomp_doc> round 133, workstream ~F2 (F-SHIP), cell `DB-f-1901`.
<owned_cells>DB-f-1901</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: DBF133-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1901/IRPT_DASHBD.TO-DB-f-1901.fwd5-contract-0-4-2-s6-ruled-internal-direct-act.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF133-1-AC1 --governing-order <this order>` BEFORE the flip; pin the artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the last lines of the two regression runs; the contract's schema hash (it must not change); the value of `round_132_censuses.s6_status`; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract and its data file in a branch; no producer, wiring or deployment is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access in this order.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF133-1-AC1 FAILs at base and the checker's helpers are exercised by its self-test (57 arms).
lane: the <paths> block IS the grant.
</preflight>
