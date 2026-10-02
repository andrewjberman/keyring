# IRPT_DASHBD -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `0.4.0_DS_ClientPlatform~S` on the first row (the channel file mints on its first row, per the row gate).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a seat's row is `IRPT_DASHBD-S<k>`; a worker's row is `IRPT_DASHBD-W<n>-S<k>`; the CVO's adjudication rows
live in `../adjudications/` as `IRPT_DASHBD-C-S<k>`. **Append-only during the round.** Never edit an existing row.
**Denominator at this write:** 1 row (this file's first).


## IRPT_DASHBD-S1 -- the reporting-policy registry cannot express a GOLD PARQUET table, so DB-b-1's registry limb stops with the file untouched

```json
{
  "id": "IRPT_DASHBD-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-09-30T17:48:37Z",
  "one_line": "TO-DB-b-1's registry limb is REFUSED and stops there as the order instructs: infra/logic/registry/reporting_policies.json cannot express a GOLD PARQUET table. Both fields the order names are outside the validator's admitted sets -- tier 'gold' refuses with 'reporting tier/table is not admitted' (admitted: state, platinum) and extension 'parquet' refuses with 'reporting content format is not admitted' (admitted: csv, json, pdf). Probed in memory against the real validator; the registry file is UNTOUCHED (git status clean on that path). This does NOT affect the addresses: lib.opal_naming.address() and name() both answer for the two tables at HEAD, so the emit is unblocked and only the conformance-record limb stops.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PROBE, run against the real validator with the candidate row built IN MEMORY and the registry file never written: lib/opal_naming.py:_validate_reporting_policies(reg) with a policy row policy_id 'irpt-reporting-gold', source 'irpt', firms ['49financial'], families ACCOUNT_RETURN_DAILY and DIM_RETURN_METHOD at tier 'gold' / extension 'parquet' -> ValueError('reporting tier/table is not admitted'). Verbatim.",
      "THE TWO LIMBS, quoted from lib/opal_naming.py at HEAD: 'if spec[\"tier\"] not in {\"state\", \"platinum\"} or not re.fullmatch(r\"[a-z]+(?:_[a-z]+)*\", spec[\"table\"]):' and 'if spec[\"extension\"] not in {\"csv\", \"json\", \"pdf\"}:'. Neither admits the value the order names, and the table names themselves (account_return_daily, dim_return_method) DO satisfy the table regex -- it is the tier and the extension that refuse.",
      "THE FULL ACCEPT/REFUSE MATRIX over the nine tier x extension combinations, measured rather than reasoned: tier=gold refuses on ALL THREE extensions ('reporting tier/table is not admitted'); tier=state accepts json and csv and refuses parquet ('reporting content format is not admitted'); tier=platinum accepts json only, refuses parquet ('reporting content format is not admitted') and csv ('reporting platinum must be bounded JSON'). So there is NO combination that describes a gold parquet table, and no combination this cell could take without misdeclaring the tier or the format.",
      "THE ADDRESSES ARE UNAFFECTED, measured at HEAD: address('irpt','49financial','gold','account_return_daily','date=2026-09-29') -> s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-29; address('irpt','49financial','gold','dim_return_method','method_version=1') -> s3://opal-data-49financial/irpt/49financial/gold/dim_return_method/method_version=1; name('irpt','49financial','reporting-adapter','lambda') -> irpt-49f-reporting-adapter-lambda. The naming builder loads and answers; only the X10 conformance-record limb refuses.",
      "THE FILE IS UNTOUCHED: `git status --short infra/logic/registry/reporting_policies.json` returns empty after the probe. The order's instruction was 'leave the policy file untouched' and that is the measured state, not an intention."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-1 WORKER FACE, the contract files section: 'infra/logic/registry/reporting_policies.json: add the policy rows the LGIC validator admits for the two tables ... mirror the existing irpt-private-reporting policy's shape with a new policy_id \"irpt-reporting-gold\", source \"irpt\", firms [\"49financial\"], families for ACCOUNT_RETURN_DAILY (tier gold, table account_return_daily, extension parquet) and DIM_RETURN_METHOD.' Its refusal clause: 'If the validator refuses a field you cannot express, STOP on that limb, file the refusal text verbatim in a surprise row, and leave the policy file untouched: a builder refusal is a registry row for the LGIC lane, never a typed workaround.'",
  "world_is": "The validator admits neither field. tier 'gold' is not in {state, platinum} and extension 'parquet' is not in {csv, json, pdf}, and the nine-combination matrix shows no way to express the two tables without declaring a tier they are not or a format they are not in. The limb is stopped with the file untouched; every other limb of DB-b-1 proceeds, because address() and name() answer for both tables.",
  "notes": "READING FOR THE LGIC LANE, offered rather than assumed: the refusal may be CORRECT BY DESIGN rather than a gap to widen. Every field on a reporting_policies row is a RETENTION AND DISPOSAL record -- retention_policy_id, unreferenced_days, accepted_ceiling_days, physical_disposal, register_id X10 pointing at infra/logic/06_CONFORMANCE_LEDGER.md -- and the admitted tiers (state, platinum) and formats (csv, json, pdf) are exactly the shapes of a CLIENT-FACING REPORTING ARTIFACT. A gold parquet table is medallion data one tier below that, produced and superseded by its own pipeline, and it carries no disposal lifetime of the kind this record exists to hold. So the two candidate remedies are NOT symmetric: (1) widen the enums to admit gold/parquet, which makes this record carry two different kinds of object under one schema and is a Rule 24 (iii) intent collision; (2) rule that medallion gold tables are OUT OF SCOPE for the X10 reporting-policy carrier and that C-SOURCES' 'registration is a policy row this project adds in round 1' is satisfied for gold by the naming registry alone (scopes.json, which already resolves both addresses). I recommend (2) and did not take either -- the choice belongs to the LGIC lane and the CTO, not to this cell. CONSEQUENCE TO NAME FOR THE ISSUER: DB-1-AC1 reads 'the policy file names both tables and the naming builder still loads'. The second half passes at HEAD; the first half cannot pass while this refusal stands, so that criterion needs the issuer's amendment or the LGIC ruling before it can be graded. Nothing else in the cell is blocked."
}
```


## IRPT_DASHBD-S2 -- the order grants two org/standards/ paths its <paths> block cannot confer: that directory is an exec lane and the pre-commit hook refuses this seat

```json
{
  "id": "IRPT_DASHBD-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-09-30T21:10:06Z",
  "one_line": "TO-DB-b-1's <paths> grants two files under org/standards/ and its preflight states 'lane: the <paths> block IS the grant', but org/standards/ is lane ANY_EXEC in the owned-paths registry and this seat is not in permitted_agents, so the pre-commit hook REFUSES in block mode. The contract file is written, correct and gate-clean on every other limb; it simply cannot land under this seat's author line. The order's grant and the repository's ownership disagree, and the repository wins at the hook.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "REFUSAL VERBATIM, from .tools/safe-commit.sh with the contract in the pathspec: 'ERROR: owned-paths lane violation(s) detected (block mode): VIOLATION: org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json -- lane=ANY_EXEC (Any exec agent -- base or project-scoped CTO/COO/CVO/CRO ...); agent=0.4.0_DS_ClientPlatform~S not in permitted_agents' then 'ERROR: safe-commit did NOT commit (rc=1)'.",
      "THE ORDER'S OWN TEXT, both halves: the <paths> block lists 'org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json' and 'org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json'; the RECORD FACE preflight reads 'lane: the <paths> block IS the grant'. Both are quoted from IRPT_DASHBD.TO-DB-b-1 at HEAD.",
      "THE SAME COMMIT SUCCEEDS WITHOUT THAT ONE PATH, which is the control that isolates the cause rather than assuming it: the identical call over data/assets/scripts/gold/irpt_reporting/ and the deliverables file landed at 63b7945fc4 with every gate green (commit-gate clean, naming-gate CONFORMANT on all declared strings, missions-tree-check 0 violations). Only the org/standards/ path refuses.",
      "THE CONTRACT ITSELF IS NOT AT FAULT: 18 columns derived from the producer's own ARROW_SCHEMA, schema_hash b5fa8e4e48bf60ab5bb34cf7e4179ebfdcff8aa9d507ccedbd32eac700222058 recomputable from it, the rule-24 record complete with a word-boundary token census over a printed denominator of 12,876 files. It is written and sitting untracked in the working tree.",
      "AN OVERRIDE EXISTS AND WAS NOT TAKEN. CLAUDE.md 14a names GIT_COMMIT_AUTHOR_OVERRIDE=<LANE> as the audited escape from a lane refusal. It is not used here: the refusal is not a mis-stamped author, it is an OWNERSHIP boundary saying a Tier-2 data seat does not write the estate's shared standards directory, and spending an audited override to cross that is the kind of act the audit log exists to catch rather than to permit."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-1: 'The contract files (C-SHAPE, annex 17c, ADDENDUM ruling 12), written BEFORE the first upload: org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json ... org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json', with both paths in <paths> and the preflight's 'lane: the <paths> block IS the grant'.",
  "world_is": "A task order's <paths> block is not a lane grant. org/standards/ is owned by ANY_EXEC in the owned-paths registry and the pre-commit hook grades the COMMITTING AGENT against that, not against the order that sent it. So an order can name a path it cannot confer, and the mismatch is invisible until the commit -- after the file is written. Both contract files this cell owes are in that state; the second is not yet written only because it waits on the measured thresholds.",
  "notes": "NOT BLOCKED ON ANYTHING ELSE: the adapter, its declaration and the superseded-thresholds record landed at 63b7945fc4, and the emit is gated on the re-measured thresholds rather than on this. THREE REMEDIES, none taken, because the choice is the issuer's and the owned-paths registry's owner's: (1) an exec lands the two contract files on this seat's behalf, which is the smallest act and keeps the ownership boundary intact; (2) the owned-paths registry grants this seat the two named files, which is narrow but sets a precedent for every future adapter's contract; (3) the contracts move to a path this lane already owns -- but C-SHAPE names org/standards/ as the home ('ONE contract file per table under org/standards/'), so that is a PRD change and the most expensive of the three. I recommend (1) and note that (2) is what the order's own preflight already believed was true. CORRECTION TO THE RECORD, stated here because a commit message cannot be edited: 63b7945fc4's subject reads '... + the account_return_daily contract' and the contract is NOT in that commit -- the message was written before the refusal was known and the commit was retried with a narrower pathspec. The adapter and the declaration are in it; the contract is not. The next commit that carries the contract will say so, and this row is the pointer in the meantime."
}
```


## IRPT_DASHBD-S3 -- the in-kind unit price was a WHOLE POSITION'S MARKET VALUE (3,278x overstatement) and the withholding filter was dead -- both repaired, and the calibration they contaminated is void

```json
{
  "id": "IRPT_DASHBD-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T04:05:00Z",
  "one_line": "TWO DETERMINISTIC DEFECTS IN MY OWN ROUND-1 ADAPTER, found by the methodology review Andrew commissioned and confirmed at bytes here. (F01) FlowCache._closes() read src.get('price_column'); sources.json never declared one, so it fell back to position_value_column = market_value_settled_unsettled -- a WHOLE POSITION'S MARKET VALUE -- which classify_and_sum then multiplied by the transferred quantity. 32,587 of 43,447 in-kind legs over the 561-partition history reached that fallback and admitted $10,136,513,746,276.56 of in-kind value where the correct unit price admits $3,092,518,713.75: a 3,277.8x overstatement, worst single leg 941,822.4x. (F06) the income filter read inc[keycols[1]] = tr_cd while the WD withholding marker is on sb_cd = keycols[2], and every income row carries tr_cd == FC, so the exclusion was always true and withholding was NEVER excluded from income on any run. BOTH REPAIRED at 35e325eedc. THE CONSEQUENCE THAT MATTERS MORE THAN EITHER FIX: the three guard numbers I measured and committed as 'the data's own distribution' were instrument artifacts of F01, and are now quarantined rather than corrected.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "F01 AT BYTES, the fallback as it stood: FlowCache._closes() read `idcol, pxcol = src['inkind_identifier_column'], src['position_value_column']` then `col = src['price_column'] if src.get('price_column') else pxcol`. sources.json declares `inkind_price_column` ('price', the TRANSACTION row's price) and `position_value_column` but NO `price_column` -- measured: `'price_column' in src` is False, and the only price-bearing key is `inkind_price_column`. The call site at classify_and_sum computes `eff = row_px.where(row_px > 0, close)` then `value = qty * eff`, so the position total is multiplied by the quantity. Dimensionally invalid, silent, and live on every run that used the in-kind term.",
      "THE REAL UNIT PRICE, VALIDATED RATHER THAN CHOSEN BY NAME: dim_position carries `closing_price`. On date=2026-09-25, `quantity_settled_unsettled x closing_price` reproduces `market_value_settled_unsettled` to within ONE BASIS POINT on 106,307 of 106,578 comparable rows (106,835 rows in the partition), so it is the price the custodian's own market value is built from. `closing_price_unfactored` reproduces the identity equally well on this partition and was NOT taken: where the two diverge the factored price is the one the book uses, and picking the other would reintroduce a silent units question.",
      "THE ERROR MAGNITUDE, MEASURED TWICE AT DIFFERENT GRAINS. Per-position on date=2026-09-25: the multiplier `market_value_settled_unsettled / closing_price` has median 71.0x, p90 718.0x, max 5,353,077.5x over 106,578 rows. Per-leg over the whole 561-partition history (558 days carry an in-kind leg): admitted in-kind value $10,136,513,746,276.56 contaminated against $3,092,518,713.75 corrected, overstatement factor 3,277.8x, absolute overstatement $10,133,421,227,562.82; worst legs 941,822.4x (2025-12-30, $204,353,862,642.60 against a corrected $327,862.68), 213,720.7x (2026-07-20), 181,719.0x (2026-04-22).",
      "THE REPAIR IMPROVES COVERAGE RATHER THAN TRADING IT AWAY, which is the control that distinguishes a real fix from a narrowing: UNVALUED in-kind legs FALL from 4,487 to 579 of 43,447, because `closing_price` is populated on identifiers where `market_value_settled_unsettled` is not. Legs priced through the fallback rise from 28,100 to 32,008.",
      "F06 AT BYTES: `transaction_key_columns` is ['tran_srcde', 'tr_cd', 'sb_cd'], so `keycols[1]` is `tr_cd`. The filter was `inc = inc[inc[keycols[1]].str.upper() != 'WD']`. The income population is selected by `_category` matching divid|interest|coupon on cash rows with `_sign > 0`, and in the 187-row classification table every such code carries `tr_cd == FC`, so the comparison 'FC != WD' was always true and the filter removed nothing. A positional index into a declared list is why it was invisible: the line read plausibly and did nothing.",
      "THE REPAIRS, at 35e325eedc (author 0.4.0_DS_ClientPlatform~S, commit-gate PASS, naming-gate PASS, missions-tree-check 0 violations): `price_column: closing_price` is declared with its measured basis, and `_closes()` now RAISES SystemExit when no `price_column` is declared rather than substituting a different quantity -- an absent price is UNKNOWN and the caller already had a correct UNVALUED path. `withholding_code_column: sb_cd` is declared and read BY NAME, and the producer refuses if the declaration does not name a real transaction key, so a typo cannot restore a silently-dead filter.",
      "THE CALIBRATION IS QUARANTINED, NOT CORRECTED: deliverables/0.4.0_DS_ClientPlatform~S/MEASURED_THRESHOLDS_R1.json is renamed to MEASURED_THRESHOLDS_R1.SUPERSEDED_CONTAMINATED_INKIND_UNIT_PRICE.json carrying the reason, the root cause and the validating measurement. Its tails -- tolerance max 214.579843, large_flow max 217.995703, observed_r_p001 -0.912047 -- were recorded in my own session log as 'the data's own distribution' and were artifacts of F01. There is now NO live thresholds file, and the producer refuses an emit without --thresholds-in, so the cell fails closed by the order's own rule rather than by an added gate."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-1 C-METHOD: 'In-kind transfers valued at quantity x same-day close; an unpriced leg sets day_quality FLOW_UNRECONCILED rather than a zero-buried flow.' And the thresholds clause: tolerance 'at the p99 percentile of the reconciled-day differences (state the value and the percentile)', large_flow_share 'at the 99th percentile of the flow share', 'the plausibility band at [-0.5, +0.5] daily unless the data's own p99.9 says otherwise (state it)' -- all three 'written into dim_return_method and the method contract with the distribution figures beside them'.",
  "world_is": "'Same-day close' was implemented as a same-day POSITION TOTAL for 32,587 of 43,447 in-kind legs, so the term the order calls a close was a quantity-times-quantity product inflated 3,277.8x in aggregate. Because the thresholds are defined as percentiles OF THE PRODUCER'S OWN OUTPUT, the defect propagated straight into the numbers meant to police it: the order's rule faithfully executed over contaminated input yields a tolerance of 1.0677% and a large_flow_share of 0.000001, and both were committed as measurements. A calibration whose population is its own producer's output cannot detect a defect in that producer -- it absorbs it and reports it as the data's nature. Separately, foreign-tax withholding was never excluded from income because the filter indexed the wrong declared column.",
  "notes": "WHAT I AM NOT CLAIMING: that the repaired producer is now correct. Four further findings in the same review are confirmed and are NOT fixed here because their remedies are not this seat's -- they are rows S4 and S5 beside this one. A re-measure is deliberately NOT taken in this commit: the account-boundary defect sits in the ORDER'S OWN method text, so recalibrating now would bake a second known defect into the served numbers, and the review's own sequence puts the specification amendments before recalibration. That is a specification dependency, not an approval gate, and nothing about it is waiting on a human to say yes. THE GENERAL LESSON I OWE THE RECORD, because it is the one that will recur: I treated the in-kind fix of the prior session as the thing that REMOVED spurious gains (run 1 p99.9 +108% fell to +4.4%) and read that improvement as evidence the term was right. It was evidence only that the term had CHANGED. The improvement was real and the arithmetic underneath it was dimensionally wrong at the same time, and a before/after on a distribution cannot distinguish those two. The control that would have caught it in minutes is the one I ran only after being told to look: assert the units identity -- quantity x price == the book's own market value -- against the custodian's own columns, with a denominator. An identity check on a derived quantity is cheap and decisive where a distribution check is neither."
}
```


## IRPT_DASHBD-S4 -- three defects are in the ORDER'S OWN METHOD TEXT, so the remedy is an issuer amendment and not a code patch: the account boundary, the fee basis, and the flow-timing selection

```json
{
  "id": "IRPT_DASHBD-S4",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T04:05:00Z",
  "one_line": "THREE CONFIRMED DEFECTS WHOSE SOURCE IS THE TASK ORDER'S OWN TEXT, not the producer, so this seat cannot fix them without adjudicating its own scope. (a) THE ACCOUNT BOUNDARY: the order's face makes a matched cash leg across two accounts INTERNAL and the producer excludes INTERNAL from F_t, so a $500 transfer between two $100,000 accounts emits -0.5% and +0.5% as MEASURED returns instead of zero. The retiring engine ADMITS those legs at account grain by CTO ruling, so the order and the prior art disagree and the order is the one that is wrong. (b) THE FEE BASIS: fee classes are excluded from F_t and never added back, so a $500 advisory fee on a $100,000 account produces -0.5% while the emitted method row says fee_basis GROSS_ONLY and the order says 'GROSS of advisory fees'. The arithmetic is net and the label is gross. (c) THE TIMING SELECTION: DB-b-3 scores END using total_return_daily, which the guard may already have replaced, against START and MIDPOINT derived from raw value and flow fields -- not a like-for-like comparison -- and then asks for the winner to be written into the served method row without re-emitting the returns it would change.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "(a) THE ORDER'S FACE, quoted from TO-DB-b-1 at HEAD by printing the bytes at the cited lines rather than grepping for the quote: 'F_t = the net EXTERNAL flow (capital-in positive, capital-out negative) from fact_trn rows whose class is EXTERNAL under the code table and the pair-match rule (a CASH leg matched on (business_date, |gross|) across DIFFERENT accounts with opposite debit_credit is INTERNAL; unmatched is EXTERNAL by default).'",
      "(a) THE PRODUCER FAITHFULLY IMPLEMENTS IT, which is why this is a specification defect and not a bug: `if len(accts) > 1 and len(signs) > 1:` sets `_final = 'INTERNAL'` and increments `resolved_pair-match`; the flow term is then `ext = t[(t['_final'] == 'EXTERNAL') & t['_is_cash'] & t['_sign'].notna()]` and `flow = ext.groupby(acct_col)['_signed'].sum()`. INTERNAL never enters F_t.",
      "(a) THE PRIOR ART DISAGREES, BY CTO RULING, at account grain: c02_twr_engine.py carries `_GRAIN_CLASSES = {'account': ('EXTERNAL', 'INTERNAL'), 'relationship': ('EXTERNAL',)}` and `INTER_ACCOUNT_PROVENANCE = frozenset({'pair-match', 'text-counterpart'})`, then at its flow term `crosses = (led['final_class'] == 'EXTERNAL') | (led['resolution_provenance'].isin(INTER_ACCOUNT_PROVENANCE))`. So the served engine admits exactly the pair-matched legs the new order excludes, and its own comment states the reason: 'the two grains move under different filters BY DESIGN'.",
      "(a) MEASURED EXPOSURE over the 561-partition history, denominator printed: the pair matcher resolved 3,533 legs to INTERNAL (census key `resolved_pair-match`) and same-account-type-transfer resolved a further 8,130. Total INTERNAL cash rows 1,817,009 carrying $3,282,194,356.44 absolute and $84,076,455.58 net. The 3,533 pair-matched legs are the population this defect misplaces at account grain; the 8,130 type-transfers are correctly internal and must NOT be swept in with them.",
      "(a) THE MATCHER IS ALSO NOT PAIRING, a defect the review found that is independent of the boundary question: the code groups by rounded absolute amount and requires only `len(accts) > 1 and len(signs) > 1`, so a group of one debit and two equal credits marks ALL THREE legs INTERNAL without conserving value. Measured previously on six sampled days: 5 of 25 matched groups were not pairs.",
      "(b) THE FEE CONTRADICTION AT BYTES: the order reads 'GROSS of advisory fees: fee_amount null with fee_amount_reason FEE_RAIL_UNUSED; fee_basis GROSS_ONLY (C-FEERAIL). No net return.' The producer's code table maps 'FEE-MANAGEMENT', 'FEE-MANAGEMENT-VERIFIED', 'FEE-MANAGEMENT-INFERRED' and 'FEE-ADMIN' as their own classes, and the flow term selects `_final == 'EXTERNAL'` only -- so a fee debit reduces V_t and is never added back. MEASURED over the history: 122,496 FEE-MANAGEMENT cash rows, $58,046,472.89 absolute, $-9,790,125.69 net; plus 2,772 FEE-ADMIN rows, $36,129.45 absolute, $-34,008.91 net. The retiring engine by contrast computes a separate `fee_cf` term, so the prior art has the rail this order's arithmetic lacks.",
      "(c) THE TIMING CONTRADICTION: the producer always computes END and accepts a `winner` argument when emitting `flow_convention`, so the served method row can name a convention the emitted returns were not computed under, with `method_version` held constant across the change."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-1's C-METHOD flow clause (the pair-match rule making a cross-account cash leg INTERNAL), its C-FEERAIL clause ('GROSS of advisory fees ... fee_basis GROSS_ONLY. No net return.'), and TO-DB-b-3's convention-selection clause scoring END/START/MIDPOINT and writing the winner into the served method row.",
  "world_is": "The order's pair-match rule answers a RELATIONSHIP-grain question and the table it governs is ACCOUNT-grain, so money genuinely leaving a measured account is recorded as if it never moved; the retiring engine already separates those grains by CTO ruling and the new order silently collapses them. The fee clause names a basis the arithmetic does not produce: fees sit inside the value, so the series is net of fees deducted from the account while every label says gross. And the convention comparison scores a guard-substituted series against raw candidates, so its winner is not a measurement of the conventions at all.",
  "notes": "WHY I AM NOT PATCHING ANY OF THE THREE: each is a departure from the order's face, and amending a task order's criteria is the ISSUER's act (CLAUDE.md rule 27 L6), not the executing seat's. Rewriting the method text here would be exactly the scope adjudication the spine forbids, and it would also make the record say a seat measured something it was told not to. RECOMMENDED SHAPE, offered rather than taken, one per defect: (a) record whether an event crosses the MEASURED ACCOUNT boundary separately from whether it is internal to a larger relationship, admit a documented transfer as external capital without requiring its counterparty to be observed, and make the matcher one-to-one and conservation-checked -- the 8,130 same-account-type-transfers stay internal and must not be swept in. (b) For round 1, ONE consistent series honestly described as after fees and expenses reflected in the source account values, with fees billed outside the account not deducted; a gross-of-advisory-fee series needs verified fee identification and signed add-backs and is the larger scope. (c) Separate the convention that RAN from the one a comparison PREFERRED from the one a policy owner APPROVED, compare raw candidates on the same eligible population, and treat an implemented change as a new method_version with recomputation. A CORRECTION I OWE ON MY OWN EARLIER REPORT: I previously told the issuer that conditional in-kind transfers share the cash matcher's failure. That was wrong and the review established it -- the cash matcher does not pair IC rows, and conditional IC rows fall through to EXTERNAL. Specific preclassified INTERNAL in-kind codes still deserve review, but there is no second blanket fix to apply and I should not have implied one."
}
```


## IRPT_DASHBD-S5 -- the PRD itself mandates replacing a correct whole-account return with a partial-basket return, and no stage validates the value finally selected

```json
{
  "id": "IRPT_DASHBD-S5",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T04:05:00Z",
  "one_line": "TWO DEFECTS WHOSE SOURCE IS THE PRD, so the remedy is a CTO ruling. (a) THE GUARD'S SUBSTITUTION IS MANDATED: on guard disagreement the PRD requires total_return_daily to be replaced by holdings_price_return + income_return. The holdings producer's denominator is its INCLUDED, PRICED, LONG basket plus positive cash, and it reports excluded weight, negative value and leverage as separate fields -- which the new reader discards, loading only account id, daily return and status. The review demonstrated the consequence by executing BOTH supplied producers: $1,000 of priced assets rising 5% beside $9,000 of excluded-but-valued flat assets is a true whole-account +0.5%, the holdings producer returns +5% with status OK and excluded_weight 0.9, and the guard replaces the correct number with the wrong one. A fallback that is a DIFFERENT POPULATION is not a fallback. (b) NOTHING VALIDATES THE SELECTED VALUE: the plausibility band is applied to the RAW return before selection, and both the unvalued-in-kind branch and the ordinary guard-disagreement branch select a fallback without re-checking it, so a +60% neighbour is emitted against a 0% raw return and a 200% income-over-base fallback passes.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "(a) THE READER DISCARDS THE QUALIFICATIONS, at bytes in my own producer: holdings_price_returns() loads the holdings gold's account id, daily_return and status only. The excluded-weight, negative-value and leverage fields the holdings producer emits beside its return are never read, so the guard cannot know the basket it is comparing against covers 10% of the account.",
      "(a) THE SUBSTITUTION IS THE ORDER'S AND THE PRD'S RULE, NOT AN IMPLEMENTATION CHOICE: TO-DB-b-1's C-GUARD clause reads 'If |r_t - (holdings_price_return + income_return)| > tolerance the day is day_quality FLOW_UNRECONCILED, total_return_daily = holdings_price_return + income_return, return_basis HOLDINGS_INCOME_FALLBACK.' So the producer is correct with respect to its order and the order is wrong with respect to the arithmetic.",
      "(a) THE REVIEW EXECUTED BOTH ORIGINAL CALCULATIONS rather than reasoning about them, and reports the fixture result: true whole-account +0.5%, holdings producer +5% with status OK and excluded_weight 0.9, guard detects a 4.5 percentage-point difference and substitutes the +5%. This is a reproduction against the supplied sources, not a live production incidence measurement, and I am not claiming the latter.",
      "(b) THE ORDERING DEFECT: the unvalued-in-kind branch precedes the raw-return band check and selects the fallback directly, and the guard-disagreement branch selects without re-validating. The review's reproductions with the supplied +/-50% band: raw 0% with neighbour +60% emits +60%; an unvalued in-kind event with raw +800% and neighbour +60% emits +60%; raw 0% with neighbour 0% and income/base 200% emits +200%.",
      "(b) THE ACCEPTANCE CHECK DOES NOT CATCH IT, which is why the defect could pass a round: p1_1_ac2_guard_seam.py passes the out-of-band +60% fallback row. My own prior reading of that script found it coerces a null comparison return to 0.0 on a MEASURED day, so this is the second independent defect in the same check.",
      "(b) A CORROBORATING DETAIL I HAD ALREADY FOUND INDEPENDENTLY AND RECORDED, which raises rather than lowers confidence: AC2's docstring claims a `diff > tolerance` test on unreconciled days that its code does not make. Noted in my 2026-09-30 session log before this review existed."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The PRD's C-GUARD ruling and TO-DB-b-1's operative reading of it: on guard disagreement, 'total_return_daily = holdings_price_return + income_return, return_basis HOLDINGS_INCOME_FALLBACK', with the plausibility band at [-0.5, +0.5] as the stated protection against an implausible number reaching the table.",
  "world_is": "The two quantities are not comparable and not interchangeable. The holdings return explains a priced long basket; total_return_daily explains the whole account including cash, excluded and unpriced assets. Substituting one for the other converts a detected disagreement into a silent population swap, and because the band is checked before selection rather than after it, the band constrains a number that is then thrown away and not the number that is emitted. My earlier defence of this guard -- that the two calculations share no input -- is also wrong and I withdraw it: the holdings producer uses balance-derived cash and the in-kind path uses positions, so they are neither independent nor interchangeable. They are useful corroboration and nothing more.",
  "notes": "RECOMMENDED SHAPE, the CTO's to rule: keep the holdings comparison as an explicitly QUALIFIED DIAGNOSTIC carrying its coverage, denominator, valuation interval and leverage, compare only within a documented comparability domain, and do NOT substitute it into total_return_daily at all -- a day that cannot be measured is better emitted as NOT_MEASURABLE with the link broken than as a confident number from a different population. Independently of that ruling, add ONE final eligibility function applied AFTER selection -- required inputs present, values finite, method applicable, every blocking flag clear -- because the current code has no single place where the emitted answer is checked, and the band cannot acquire that role by being moved. Converting the difference to dollars does not cure a mismatched population, which is the other defence of the guard I withdraw."
}
```


## IRPT_DASHBD-S6 -- five further confirmed findings: unknown cash becomes zero flow, output depends on the run window, valuation intervals discard real custody boundaries, four acceptance checks pass wrong evidence, and foreign tax is classified as client capital in a table shared with SERVED data

```json
{
  "id": "IRPT_DASHBD-S6",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T04:05:00Z",
  "one_line": "FIVE FURTHER FINDINGS FROM THE SAME REVIEW, confirmed and grouped because they share no single remedy. (a) UNKNOWN CASH BECOMES ZERO: malformed amounts coerce to 0.0, unknown keys and UNRESOLVED rows are omitted from F_t, and an ABSENT transaction partition returns the same empty dicts as an empty one, so four malformed-cash fixtures emit +0.5% MEASURED with zero recognised flow. (b) RUN-WINDOW DEPENDENCE: first_seen is rebuilt per invocation from positive values inside the requested range, so a single-day liquidation request emits NO row while the same date inside a multi-day request emits one -- the answer depends on the batch boundary. (c) VALUATION INTERVALS: the producer links through the prior TRADING day even where the custodian provides a valid intervening balance; replaying the recorded January 8-10 values gives -0.286283% against -0.183062% through the real January 9 valuation, 10.32 basis points. (d) FOUR ACCEPTANCE CHECKS PASS WRONG EVIDENCE, including a tie-out record check that passes five copies of one period with a 50-point actual difference asserted as abs_diff=0. (e) FOREIGN TAX IS CLASSIFIED EXTERNAL in a code table SHARED WITH THE SERVED 49F ENGINE -- measured exposure 2,578 rows, $39,818.98 absolute, 229 accounts.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~P",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "(a) AT BYTES: `t['_gross'] = pd.to_numeric(t[money_col], errors='coerce').fillna(0.0)` turns a malformed amount into zero; the flow term selects `_final == 'EXTERNAL'` so UNRESOLVED and unkeyed rows are omitted; cash rows with an unreadable direction are counted into `cash_rows_with_unreadable_direction` and then dropped by `t.loc[~t['_is_cash'] | t['_sign'].isna()]` handling. The per-account `unvalued` map carries IN-KIND problems only, so no cash problem propagates a blocking state. MEASURED over the history: 114 UNRESOLVED rows ($3,449,448.08 absolute), 6 unkeyed rows, and 43,349 legs reaching EXTERNAL purely by the `external-by-default` branch.",
      "(a) ABSENCE AND EMPTINESS ARE THE SAME VALUE at the call site: read_partition returns None for a partition holding no object, and FlowCache.get turns both None and an empty frame into the same empty dicts. Listing only existing partitions cannot establish that every expected input arrived -- there is no completeness manifest.",
      "(b) AT BYTES: `first_seen` is initialised empty inside compute_range on every call and populated only from positive current values within the requested range, and the emitted manifest's `first_data_date` derives from it, so inception is a property of the REQUEST rather than of the account.",
      "(c) REPLAY OF RECORDED VALUES: -0.286283% under the order's carry-forward rule against -0.183062% linking through the custodian's own 2025-01-09 valuation, a 10.32 basis point difference on the $1,125,000 deposit day. These were values supplied in my own review package, replayed arithmetically, NOT independently re-fetched from custody -- so this is a confirmed arithmetic consequence of the interval rule, not a fresh custody measurement.",
      "(d) FOUR ORIGINAL CHECKS EXECUTED WITH SYNTHETIC IO, all PASS on inadequate evidence: p1_1_ac2_guard_seam.py passes the erroneous measured row and the out-of-band +60% fallback; p1_2_ac2_series_link_and_plan.py uses `float(return or 0.0)` on both sides and links across a null as zero, contradicting the contract's explicit gap-break rule; p1_3_ac2_method_winner_written.py passes START in the record, contract and method row while the returns are computed END; p1_3_ac1_tieout_record.py passes five copies of one period with an asserted abs_diff=0 against a real 50-percentage-point difference, because it computes statistics OF THE ASSERTED DIFFERENCES and never recomputes a difference from the stated returns. These are proof limitations in checks I wrote, not an allegation that anyone submitted false evidence.",
      "(e) THE SHARED TABLE, at bytes: org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json (187 rows) carries `FTP/FC/WD` partition EXTERNAL and `FTR/FC/WD` partition EXTERNAL -- foreign tax PAID and RECLAIMED, both read as client capital movements. Of 7 rows carrying WD on sb_cd, 2 are EXTERNAL and 5 INTERNAL. The table is consumed by data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py, the SERVED 49F chain, as well as by this adapter, and c02_twr_engine.py admits EXTERNAL into its flow term -- so the misclassification reaches served twr_daily and not only this round's gold.",
      "(e) THE EXPOSURE, MEASURED rather than asserted, over all 561 partitions (2024-07-08..2026-09-29): FTP 2,574 rows / $39,585.32 absolute / 229 accounts; FTR 4 rows / $233.66 / 4 accounts; TOTAL 2,578 rows / $39,818.98. Mean magnitude about $15 per row."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-1's C-METHOD ('a code whose category is not clearly one of these is NOT income and stays out of the numerator rather than being guessed into it'; foreign-tax WD 'is withholding, not a withdrawal', ruling 6.5), its SOURCE_LAG and history_scope states, the skipped-day rule, and the five round-1 acceptance checks as the evidence that grades the cell.",
  "world_is": "Ruling 6.5 says foreign-tax withholding is not a withdrawal; the shared code table says two of its codes ARE external capital, and that table -- not the ruling -- is what both engines execute. SOURCE_LAG is defined in the method and emitted by nothing. The checks that were to grade this cell pass on evidence that is wrong in the specific way each check exists to catch, so the round's acceptance evidence currently proves metadata agreement rather than arithmetic. And an unknown input -- a malformed amount, an unclassifiable code, a missing partition -- is in every case folded into a zero or an absence rather than propagating as a state a consumer can reject on, which is the one shape CLAUDE.md's value-must-carry-its-claim rule exists to forbid.",
  "notes": "GRADED INERT ON MAGNITUDE, NOT ON ABSENCE, and stated this way so the grader can disagree with the grading rather than with a verdict: limb (e) DOES reach served 49F data, which is the one hazard in this row that is live rather than prospective. I grade it INERT because $39,818.98 over 2,578 rows and 229 accounts is roughly $15 per row, which on a six-figure account is under a basis point and inside any plausible tolerance -- so no served return is materially wrong from this cause alone. `disarm_owner` is set to the issuer because that grading is a judgement about served client numbers and should not rest on the seat that introduced the surrounding work. IT IS THE SAME SHAPE AS ROW IRPT_BCKEND-S237 AND MUST NOT BE CONFLATED WITH IT: S237 is a $1,125,000 single-day closure defect worth up to +91.13 pp on 44 served account returns and remains the materially urgent one. ROUTING, since these five do not share a remedy: (a), (b) and the SOURCE_LAG emission are MINE and I will take them after S4 and S5 resolve, because the interval and boundary decisions change what the states must distinguish. (c) needs the issuer's choice between account x valuation-date and account x trading-day with internal subperiod linking -- not equivalent to the present endpoint formula, so it is a method amendment either way. (d) is mine to rewrite counterexample-first, and the counterexamples should be made to FAIL the current implementation before any of them is allowed to pass. (e) is the CRO's file and the served engine's lane; I am not editing a classification table that two engines execute and one of them serves clients."
}
```


## IRPT_DASHBD-S7 -- correction to my own row S6: the four acceptance checks are the ISSUER's surface, not this seat's (owned-paths lane TREE_DELIVERABLES)

```json
{
  "id": "IRPT_DASHBD-S7",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T04:15:00Z",
  "one_line": "CORRECTION TO MY OWN ROW S6, filed as a row because the channel is append-only and an existing row is never edited. S6's notes route limb (d) -- the four acceptance checks that pass wrong evidence -- with the words '(d) is mine to rewrite counterexample-first'. THAT IS WRONG AND I MEASURED IT AFTER WRITING IT: the checks live under org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/, which resolves to owned-paths lane TREE_DELIVERABLES, whose rule is that the owner is the SERIAL NAMED BY THE SUB-FOLDER. That serial is 2.0.0_SA_COO~P, so limb (d) is the ISSUER's surface and this seat cannot write it. The finding in S6 limb (d) stands exactly as filed and is unaffected; only its routing changes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE SIX CHECKS' ACTUAL PATHS, listed from the git index rather than from the review's archive-relative paths (which is how I mis-attributed them -- the package flattened them to spec/acceptance_checks/ and I reasoned from that shape): all six of p1_1_ac1_gold_under_contract.py, p1_1_ac2_guard_seam.py, p1_2_ac1_series_manifest.py, p1_2_ac2_series_link_and_plan.py, p1_3_ac1_tieout_record.py and p1_3_ac2_method_winner_written.py sit under org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/.",
      "THE LANE, resolved from .owned-paths.yaml rather than assumed: the target matches two patterns, 'org/missions/*/*/*/deliverables/**' -> lane TREE_DELIVERABLES and 'org/missions/**' -> lane TIER0_MSTR. TREE_DELIVERABLES carries permitted_agents [] and the description 'Project tree, deliverables/<SERIAL>/** -- NOBODY by enumeration. The owner is in the PATH (s.6 option ii, RULED): owned-paths-validate.py clause 4 (ADHC_OWNPTH.004) permits exactly the serial named by the sub-folder (or a ~lane of it).' The sub-folder names 2.0.0_SA_COO~P and this seat is not a lane of it.",
      "THIS IS THE SECOND TIME THIS ROUND THAT A PATH'S OWNER AND MY BELIEF ABOUT IT DIVERGED, and the first time is already on this channel: row S2 records the order granting two org/standards/ paths its <paths> block could not confer, discovered only at the commit after the file was written. Here I caught it before writing anything, by resolving the lane instead of inferring ownership from who wrote the file originally. Authorship is not ownership, and the registry is the only instrument that answers it."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "My own row IRPT_DASHBD-S6 notes, as committed at d8c2bad446: '(d) is mine to rewrite counterexample-first, and the counterexamples should be made to FAIL the current implementation before any of them is allowed to pass.'",
  "world_is": "The rewrite half of that sentence is right and the ownership half is wrong. The checks are in the issuer's deliverables folder and lane TREE_DELIVERABLES gives that folder's named serial sole write access, so this seat cannot land a single line of them. What I can legitimately offer is the counterexample SET -- the specific inputs each check must fail on, which S6 limb (d) already states precisely enough to implement from -- and the issuer or a worker it seats writes the checks.",
  "notes": "NO ACT IS OWED BY THIS SEAT ON LIMB (d) AND I AM NOT WAITING ON ANYTHING TO DO ONE. The four counterexamples, restated as acceptance inputs so the owning seat does not have to re-derive them from the finding: (1) the guard check must FAIL a row whose selected total_return_daily lies outside the plausibility band, and must FAIL a MEASURED day whose comparison return is null rather than coercing it to 0.0; (2) the link check must FAIL a series containing a null return rather than linking across it as zero -- `float(return or 0.0)` is the exact expression to delete, and the table contract's gap-break rule is the authority; (3) the method check must FAIL when the method row's flow_convention names a convention the emitted returns were not computed under, which means it has to read the arithmetic and not only compare metadata strings; (4) the tie-out check must RECOMPUTE each difference from the stated returns rather than taking an asserted abs_diff, must reject duplicate periods so five copies of one period cannot stand as five observations, and must refuse an empty per-convention summary. Each of the four currently PASSES on the evidence it exists to catch, so a counterexample that does not first FAIL against the present implementation has not been demonstrated to test anything."
}
```


## IRPT_DASHBD-S8 -- the review's F12 remedy has no precondition in this feed: dim_balance is clean, fact_trn carries no event identity, and the fix is upstream

```json
{
  "id": "IRPT_DASHBD-S8",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T05:15:00Z",
  "one_line": "THE REVIEW'S REMEDY FOR F12 HAS NO PRECONDITION IN THIS FEED, and settling that needed data the reviewer did not have. REVIEW.md F12 says to protect against duplicate inputs by using 'source event identity and an explicit version/correction rule, or verify a trustworthy upstream invariant', and explicitly could not say whether the live feed violates uniqueness. MEASURED over all 561 partitions: (a) dim_balance has NO violation -- 3,215,820 rows against 3,215,820 distinct (account, day) pairs, zero accounts with a second row, zero partitions carrying a second object -- so account_values()'s groupby.sum() is summing ONE row today and F12's balance half is LATENT, not live. (b) fact_trn carries NO USABLE EVENT IDENTIFIER: of 17 identifier-shaped columns among 140, not one is unique per row; the best is account_id at 6,014 distinct of 25,651, cashiering_transaction_identifier reaches only 244, and eleven are a single constant. So BOTH branches of the named remedy are unavailable -- there is no identity to dedup on and no verified invariant -- and the fix is an upstream silver change in another lane, not a producer edit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dim_balance, ALL 561 partitions (2024-07-08..2026-09-29), read not sampled: 561 read, 0 with more than one parquet object, 3,215,820 rows, 3,215,820 (account, day) pairs, 0 pairs carrying more than one row, worst rows-for-one-account 0. The row count EQUALS the pair count, which is the whole claim -- a single aggregate that cannot be true if any account repeats.",
      "WHY THAT MATTERS AT ALL, since a clean read looks like a non-finding: account_values() ends in `frame.groupby('_a')[value].sum().to_dict()`, so a second row for one account would DOUBLE V_t -- and V_t is both the numerator's base and the denominator of every return. The measurement is what demotes that from a live defect to a latent one; without it the sum and a true duplicate are indistinguishable from the code alone.",
      "fact_trn IDENTIFIER CENSUS on date=2026-09-29, 140 columns and 25,651 rows, counting DISTINCT values rather than reading column names: 17 columns are identifier-shaped by name. None is unique per row. account_id 6,014; dividend_interest_share_quantity 6,010 (a quantity, not an id -- it matched on the name token and is listed to show the census was not curated to a conclusion); order_number 480; cashiering_transaction_identifier 244; item_issue_id 149; rulst_sufid 4; cycle_id 2; and custdian_id, mstracct_number, underlying_itm_iss_id, unrul_sufid, s1_check_number, schwab_cashiering_unique_id, disburse_check_number, federal_bank_reference_number, recipient_maker_acct_number and order_id all carry exactly 1 distinct value.",
      "fact_trn DUPLICATES ON THE TEN COLUMNS THE PRODUCER READS, all 561 partitions: 1,099 of 3,209,771 rows (0.034%), 0 partitions with more than one object. THIS IS AN UPPER BOUND, NOT A DUPLICATE COUNT, and the distinction is the point: two genuine transactions can share account, code, amount and date, so a duplicate on the projected columns is not a duplicate EVENT. Resolving the 1,099 into real duplicates requires exactly the identity the previous limb shows does not exist.",
      "THE REVIEWER'S OWN LIMIT, quoted so the division of labour is visible rather than implied: F12 reads 'These demonstrations show missing protection, not that the actual silver feed currently violates uniqueness.' The archive held no custodian data, so this was not a gap in the review -- it is the half only a seat with read access could close."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "REVIEW.md F12's repair: 'Do not deduplicate genuine same-amount transactions by amount/date; use source event identity and an explicit version/correction rule, or verify a trustworthy upstream invariant.' And its scope note: 'These demonstrations show missing protection, not that the actual silver feed currently violates uniqueness.'",
  "world_is": "The prohibition is right and both permitted alternatives are currently closed. There is no source event identity in fact_trn to key a version/correction rule on, and no upstream uniqueness invariant has been verified for it -- only for dim_balance, where this row verifies one and finds it holds. So a producer-side dedup cannot be written correctly at all today: the only key available is the (account, code, amount, date) tuple the repair explicitly forbids keying on, and using it would silently delete genuine same-amount transactions. The honest producer-side position is the current one -- no dedup -- with the 0.034%% upper bound recorded rather than acted on.",
  "notes": "ROUTING, and it leaves this project: the remedy is an UPSTREAM SILVER change -- fact_trn's silver build would have to carry a stable per-event key, which is the Schwab ingest's lane (the 49-schwab-conv pod AE for the six silver tables), not this adapter's and not the issuer's. I am not editing a silver builder from a reporting cell. WHAT I RECOMMEND, offered rather than taken: (1) ask the ingest lane whether the raw Schwab CRS record carries a key that silver currently drops -- the 140-column partition has eleven single-valued identifier-shaped columns, which is the signature of a vendor field that is populated for some record types and not these, so the answer may be yes for a subset; (2) until then, leave the producer with NO dedup and treat the 0.034%% as a measured upper bound on possible duplication, which is a disclosure, not a defect; (3) keep account_values()'s groupby.sum() but do not rely on it being harmless -- it is harmless because the feed happens to carry one row per account-day, which is a property measured today and not a guarantee. A cheap guard that refuses rather than sums when an account repeats would make the invariant enforced instead of observed, and that is a producer edit I would take on the issuer's word. NOT CLAIMED: that the 1,099 rows are or are not real duplicates. That question is unanswerable from this feed, and saying so is the finding."
}
```


## IRPT_DASHBD-S9 -- the excluded-weight ceiling is nearly moot; ruling 18's leverage member bars 35.5% of the sample and the TaxSMA product is leveraged by design

```json
{
  "id": "IRPT_DASHBD-S9",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T06:40:00Z",
  "one_line": "THE EXCLUDED-WEIGHT CEILING THE ISSUER ASKED FOR IS VERY NEARLY MOOT, AND THE BINDING MEMBER OF RULING 18'S COMPARABILITY DOMAIN EXCLUDES THE PRODUCT THIS DASHBOARD REPORTS ON BY CONSTRUCTION. Measured over all 558 holdings partitions for the round-1 sample: excluded weight is 0.000000 at median, p75 and p90, p99 0.000029, max 0.004978, with 1,086 of 1,099 status-OK account-days exactly zero -- a 0.005 ceiling bars ZERO rows and 0.001 bars 11. But `leveraged` and `negative_value` flag EXACTLY THE SAME 390 rows (0 in either alone), and ruling 18 bars both, so 390 of 1,099 OK account-days (35.5%) are OUT OF DOMAIN on that member regardless of the ceiling. The concentration is the finding: the thread account is 0% barred while the five TaxSMA roster accounts run 28%, 65%, 86%, 89% and 94% barred. Their roster `strategy` reads 'Opal Tax SMA 200/145' -- a long/short extension strategy -- so leverage and negative positions are INHERENT to the product, not an anomaly in it. On the accounts the Investor Reporting dashboard exists to report, the guard that was Andrew's 'no hyper-exaggerated return' protection will mostly not run.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE OWED MEASUREMENT (amendment 5 (b): 'print it, stop, and report it'). Excluded weight over holdings_performance_daily, all 558 partitions 2024-07-09..2026-09-28, the six round-1 candidate accounts, 1,147 rows of which 1,099 status OK: median 0.000000, p75 0.000000, p90 0.000000, p99 0.000029, max 0.004978, days at exactly zero 1,086 of 1,099. Reading A (3 active + thread = 4 accounts) n=881, p99 0.000000, max 0.004978. Reading B (all 5 roster entries + thread = 6) n=1,099, identical max. NO CEILING IS PROPOSED HERE: ruling 18 gives that choice to the issuer and a producer does not pick the bound it is graded against.",
      "LEVERAGE AND NEGATIVE VALUE ARE ONE CONDITION, NOT TWO, which matters because the domain lists them as separate members and a reader would expect separate populations: leveraged true 390, negative_value non-zero 390, BOTH 390, leveraged-only 0, negative-only 0, and the two boolean masks are identical element-for-element over all 1,147 rows. Mechanically unsurprising once seen -- a short position carries a negative market value and produces leverage -- but it means tightening or relaxing either member moves the same 390 days.",
      "THE DOMAIN'S BINDING CONSTRAINT, measured against the ceiling's: out of domain on leverage/negative value = 390 of 1,099 OK rows (35.5%); out of domain on excluded weight at a 0.005 ceiling = 0 rows; at a 0.001 ceiling = 11 rows. So the member the issuer was asked to set is the one that does almost nothing, and the member already fixed by the ruling is the one that decides a third of the sample.",
      "PER ACCOUNT, status-OK rows and how many the leverage member bars: 0010783709 (THREAD, not a TaxSMA book) 558 OK / 0 barred / 0%; 0027265115 (ACTIVE) 134 / 119 / 89%; 0035940058 (PENDING_RESOLUTION) 127 / 119 / 94%; 0076459710 (ACTIVE) 57 / 37 / 65%; 0084073310 (ACTIVE) 132 / 37 / 28%; 0091939812 (PENDING_RESOLUTION) 91 / 78 / 86%. The split is exactly along product lines, which is what turns this from a data quirk into a design question.",
      "THE PRODUCT IS LEVERAGED BY DESIGN, from the roster's own field rather than inferred from the numbers: every one of the five entries in s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json carries `strategy` = 'Opal Tax SMA 200/145'. A 200/145 extension strategy holds roughly 200% long against 145% short, so `leveraged` true and a non-zero `negative_value` are the strategy operating normally. The thread account, which is not a TaxSMA book, is barred on 0 of 558 days -- the negative control that separates 'this product' from 'this feed'.",
      "A SEPARATE DISCREPANCY FOUND WHILE RESOLVING THE SAMPLE, recorded because it sets every round-1 denominator: ISSUER AMENDMENT 1 reads 'the five roster accounts (from ...taxsma_roster.json, field schwab_account, status active)'. The roster holds FIVE entries of which THREE are `status active`; the other two are `pending_resolution` (0035940058 'Bump', 0091939812 'Macy', neither resolved in dim_account_xref). 'Five roster accounts' and 'status active' cannot both select the same set. EMPIRICALLY RESOLVED IN FAVOUR OF ALL FIVE: the quarantined MEASURED_THRESHOLDS_R1 recorded reconciled_account_days 1098, and the status-OK holdings rows over all six accounts number 1,099 -- a one-row difference consistent with a first-day exclusion, while Reading A would have given 881. So the prior pass used all five plus the thread account. Stated rather than assumed, because the issuer owns the sample definition."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.4 ruling 18 (@a8a65b9f62): 'The guard GRADES a day only inside the domain (bounds measured in round 1 and written to dim_return_method with the tolerance: a ceiling on excluded weight, no leverage, no negative value, holdings status OK, the same valuation interval).' And TO-DB-b-1 amendment 5 (b): 'The comparability ceiling on excluded weight is chosen by the ISSUER from the distribution your first pass prints ... print it, stop, and report it.' Plus amendment 1: 'the five roster accounts (from ...taxsma_roster.json, field schwab_account, status active)'.",
  "world_is": "The domain was specified against a general notion of comparability and meets a population that is leveraged on purpose. 'No leverage' and 'no negative value' are the same single test here, and it removes 35.5% of the sample and the clear majority of every TaxSMA account's days, while the ceiling the issuer was asked to choose removes nothing at any value down to 0.005. So ruling 18 as written does not fail -- it applies exactly as specified -- and the consequence is that on the product the dashboard reports, most days are graded by no guard at all and fall to the flow-share bound alone (MEASURED when |F_t|/V_(t-1) is at or below the tolerance, otherwise FLOW_UNRECONCILED and NOT_MEASURABLE). That is a coherent and conservative outcome; it is also not the protection the guard was introduced to provide, and the gap is invisible from the ruling's text because nothing in it names the strategy.",
  "notes": "WHY THIS IS THE CTO's AND NOT THE ISSUER's, and why I did not choose a ceiling to make it go away: the ceiling is the issuer's by amendment 5 and I have printed it and stopped, as instructed. But no ceiling the issuer can pick changes the 390 days, because they are barred by a member the RULING fixes, so answering only the ceiling question would hand back a number that looks like a decision and settles nothing. `disarm_owner` is the CTO for that reason. THREE CANDIDATE SHAPES, none taken: (1) ruling 18 STANDS -- a leveraged day genuinely is not comparable to a long-only priced basket, and the honest consequence is that those days ride the flow-share bound, which is already a measured error bound and not a guess; this is the conservative reading and my recommendation if nothing else changes. (2) The leverage member is REPLACED by a quantitative bound (for instance short weight over account value under a measured ceiling), which would restore grading for the lower-leverage days -- but the distribution behind that bound has not been measured and I would need to print it first. (3) The guard's NEIGHBOUR is wrong for this product rather than the domain being wrong: holdings_performance_daily's denominator is 'included, priced, LONG basket plus positive cash' (row S5), so for a 200/145 book it omits the short side by construction and a like-for-like comparison may not exist at any excluded-weight ceiling. If (3) is the real answer then C-GUARD needs a different instrument for TaxSMA books, which is a PRD question and larger than this round. NOT CLAIMED: that any served number is wrong. Nothing is served, and the 35.5% figure is about how many days the guard can GRADE, not about how many are wrong."
}
```


## IRPT_DASHBD-S10 -- the tie-out's convention comparison has ONE discriminating day, and its abs_diff measures a day-set mismatch rather than disagreement

```json
{
  "id": "IRPT_DASHBD-S10",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T14:30:00Z",
  "one_line": "THE TIE-OUT'S CONVENTION COMPARISON CANNOT SEE THE DAYS THAT WOULD DECIDE IT, AND ITS abs_diff IS DOMINATED BY DAYS OPAL WITHHELD RATHER THAN BY ARITHMETIC. Two findings from one measurement. (a) END, START and MIDPOINT differ ONLY where external_flow is non-zero. Over the five eligible (account, period) pairs there are 10 flow-bearing account-days, of which EXACTLY ONE survives into the eligible population (2026-03-25, account 0027265115, flow $448,559.28, LARGE_FLOW/GRADED_AGREED). On three of the five periods ZERO flow days survive, so all three conventions are arithmetically IDENTICAL there -- and START/MIDPOINT are identical to nine decimals on ALL FIVE. The mechanical winner is START by a median margin of 0.000218941, which is one day in one account. (b) The abs_diff itself is large (median 1.6754%, max 3.6572%) because Opal's geometric link EXCLUDES the withheld days while Black Diamond's return INCLUDES them: on 0076459710 Opal links 34 of 38 days to +9.1259% against BD's +12.7830% over its full 38, and the two withheld days include the $1,108,201.80 inception funding. The two figures cover different day sets, so their difference is not a measure of agreement.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE DISCRIMINATING POPULATION, counted per period from the served gold: 0027265115 2026-04-08..2026-06-30 -> 58 days, 0 flow-bearing, 0 eligible; 0027265115 2026-07-01..2026-08-28 -> 42 days, 1 flow-bearing, 0 eligible (2026-07-07, -$2,423.40, FLOW_UNRECONCILED / NOT_GRADED_OUTSIDE_DOMAIN, withheld); 0076459710 2026-07-08..2026-08-28 -> 38 days, 2 flow-bearing, 0 eligible (2026-07-08 +$1,108,201.80 NOT_MEASURABLE / GUARD_NOT_REACHED and 2026-08-10 -$2,200.86 FLOW_UNRECONCILED, both withheld); 0027265115 2026-03-16..2026-06-30 -> 73 days, 3 flow-bearing, 1 eligible; 0027265115 2026-03-16..2026-08-28 -> 115 days, 4 flow-bearing, 1 eligible. TOTAL: 10 flow-bearing account-days across the five periods, 1 eligible.",
      "WHY THAT MAKES THE COMPARISON EMPTY, as arithmetic rather than as opinion: END is (V_t - F_t)/V_(t-1) - 1 and START is (V_t - V_(t-1) - F_t)/(V_(t-1) + F_t). Set F_t = 0 and both reduce to V_t/V_(t-1) - 1; MIDPOINT's denominator V_(t-1) + F_t/2 reduces the same way. So on a zero-flow day the three conventions are not merely close, they are the SAME NUMBER, and a comparison over a population of zero-flow days has nothing to rank.",
      "THE MEASURED CONSEQUENCE, from the run: per-convention median |opal - bd| is END 0.016972979, START 0.016754038, MIDPOINT 0.016754038 -- START and MIDPOINT equal to nine decimals, which can only happen if no day in the population has a non-zero flow except where they coincide. p90 is 0.028732093 for both and 0.029068539 for END; max is 0.036571503 for all three.",
      "THE abs_diff IS A DAY-SET MISMATCH, not an arithmetic disagreement, and the gap counts show it: the 116-day period links 104 days with 11 gap days in 11 segments; the 58-day period links 54 of 58; the 42-day links 39 of 42; 0076459710 links 34 of 38. Black Diamond's daysHeld for the same periods are 116, 58, 42 and 38 -- it holds every day. So Opal's number answers 'what did the measurable days do' and BD's answers 'what did the account do', and the difference between them is mostly the days Opal declined to measure.",
      "THE LARGEST SINGLE CASE IS THE CLEAREST: 0076459710 over 2026-07-08..2026-08-28, Opal +0.091258795 against BD +0.127830298, a 3.657 percentage-point difference. The account's inception funding of $1,108,201.80 lands on 2026-07-08 and that day is NOT_MEASURABLE (no prior value, GUARD_NOT_REACHED), so Opal's link begins after the money arrived while BD's covers the arrival. Nothing about that difference is evidence of a defect in either producer.",
      "THE CIRCULARITY, stated plainly because it is the part that will not fix itself: a convention differs only where there is a flow, and a flow large or unreconciled enough to matter is exactly what drives day_quality to LARGE_FLOW, FLOW_UNRECONCILED or NOT_MEASURABLE. The eligible population is therefore selected AGAINST the days that carry the signal. Amendment 3's 'ONE eligible population' rule is right -- it stops the earlier defect of scoring a guard-substituted series against raw candidates -- and it cannot manufacture discriminating days that the gold withholds."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-DB-b-3 amendment 3: 'END, START and MIDPOINT are ALL recomputed here from the same raw daily columns over ONE eligible population: the account-days whose emitted total_return_daily is non-null' and 'flow_convention_preferred (the lowest median of the three, ties to END: what this comparison prefers)'. And the summary clause: 'proposed_tieout_tolerance = the winner's p90 rounded up to the next 5 bp, with the sentence that defends it.'",
  "world_is": "Both instructions execute exactly as written and neither produces a usable answer on this evidence. flow_convention_preferred comes out START on a discriminating population of ONE account-day, and the p90 that sets the proposed tolerance comes out 2.8732%, which rounds to a 2.90% tie-out bar -- a bar that would admit a 2.9 percentage-point disagreement between Opal and the vendor on a client-facing return. That number is not an error in the rule; it is what the rule returns when the two series cover different day sets. Adopting it as a tolerance would enshrine the day-set mismatch as acceptable agreement.",
  "notes": "WHAT I DID AND DID NOT DO. I computed the record exactly as amendment 3 specifies, including the mechanical winner and the mechanical p90-to-5bp tolerance, because the order asks for them and `tieout_tolerance_proposed` is by its own name a PROPOSAL the CTO rules on. I did NOT quietly pick a different rule to get a better-looking number, and I did NOT write the preferred convention into the served method row -- amendment 3 forbids that and the served flow_convention stays END. WHAT I RECOMMEND, for the CTO's ruling: (1) do NOT adopt 2.90% as the tie-out bar. (2) Compare like day sets instead: either restrict the tie-out to periods where Opal withholds NO day (on this evidence that is zero of five periods, which is itself the finding), or have Black Diamond's own return recomputed over Opal's eligible day set, which the vendor API cannot do, or accept that the tie-out measures COVERAGE rather than AGREEMENT and rename what it reports. (3) Treat flow_convention_preferred as UNDETERMINED on this round rather than START: one discriminating day cannot rank three conventions, and recording START as 'preferred' invites a later reader to treat it as measured. (4) The enrichment that would actually settle it is a period set chosen for flow-bearing eligible days -- which needs either a tolerance wide enough to keep a large-flow day MEASURED, or the signed-basket instrument PRD ruling 20 names, and both are rulings rather than cell work. NOT CLAIMED: that either producer is wrong. The measured difference is explained by which days each one counts, and I have not found an arithmetic defect in this comparison."
}
```


## IRPT_DASHBD-S11 -- correction to my own row S10: START and MIDPOINT are identical on THREE of five periods, not all five; it is their MEDIANS that tie

```json
{
  "id": "IRPT_DASHBD-S11",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.4.0_DS_ClientPlatform~S",
  "surfaced_at": "2026-10-01T15:20:00Z",
  "one_line": "CORRECTION TO MY OWN ROW S10, filed as a row because the channel is append-only. S10 states that START and MIDPOINT are 'identical to nine decimals on ALL FIVE' periods. THAT IS FALSE: they are identical on THREE of the five -- exactly the three with no eligible flow day -- and they differ on both periods starting 2026-03-16 (START -9.7580% against MIDPOINT -9.7872% on the 06-30 end, and -5.8650% against -5.8954% on the 08-28 end). What IS identical is their per-convention MEDIAN, 0.016754038 for both, and that is the fact that matters: the median of five values lands on one of the non-discriminating periods, so the tie between the two conventions is produced by the summary statistic rather than by the returns agreeing. S10's FINDINGS ARE UNCHANGED and this detail arguably sharpens them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE FIVE PERIODS AS THE RECORD STATES THEM, START against MIDPOINT: 0027265115 2026-03-16..2026-06-30 -> -0.097580 vs -0.097872 (DIFFER); 0027265115 2026-03-16..2026-08-28 -> -0.058650 vs -0.058954 (DIFFER); 0027265115 2026-04-08..2026-06-30 -> -0.098772 vs -0.098772 (identical); 0027265115 2026-07-01..2026-08-28 -> +0.043139 vs +0.043139 (identical); 0076459710 2026-07-08..2026-08-28 -> +0.091259 vs +0.091259 (identical).",
      "THE TWO THAT DIFFER ARE EXACTLY THE TWO THAT CONTAIN THE ONE ELIGIBLE FLOW DAY (2026-03-25, account 0027265115, flow $448,559.28). The three that are identical are the three S10 already names as having ZERO eligible flow days. So the pattern is not a coincidence that weakens S10 -- it is S10's own mechanism showing through at period grain.",
      "THE MEDIANS, which is what I actually read: per_convention_summary medians are START 0.016754038 and MIDPOINT 0.016754038, equal; END 0.016972979. With five periods the median is the third-smallest difference, which falls on 0027265115 2026-07-01..2026-08-28 -- a period with no eligible flow day, where all three conventions are the same number by construction. The tie is therefore an artifact of WHICH period the median selects.",
      "HOW THE ERROR HAPPENED, because the mechanism is more useful than the correction: I read the per-convention SUMMARY (three identical medians, p90s and maxes) and stated it as a PER-PERIOD fact. The summary was true; the sentence I derived from it was about a different grain. It is the same wrong-grain move as reading a day-level census as an account-level claim, and CLAUDE.md rule 24 (ii) names the axis -- SAME GRAIN -- that it crosses."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "My own row IRPT_DASHBD-S10, as committed: 'START and MIDPOINT are identical to nine decimals on ALL FIVE' and, in the same row, 'START and MIDPOINT are identical to nine decimals on all five periods'.",
  "world_is": "They are identical on three of five periods and differ on two. The per-convention medians are identical, which is the real and more interesting fact: the statistic that ranks the conventions is computed at a grain where two of them cannot differ. Everything else in S10 stands as measured -- 10 flow-bearing account-days with 1 eligible, three periods with zero, START's median margin of 0.000218941 resting on a single day, and the abs_diff being dominated by the day-set mismatch rather than by arithmetic.",
  "notes": "ALSO CORRECTED IN THE SAME TURN, and found by the same check: the one-page md's first table row carried the 2026-04-08 period's returns against the 2026-03-16..2026-06-30 label, with invented day counts (69/73 and 4 gaps instead of the record's 65/73 and 8). I caught both by printing every cell of the table from the record before committing the md rather than trusting what I had typed. The JSON record was correct throughout -- only my prose copies were wrong, which is the argument for the record being the artifact and the md being a view of it. NO ACT IS OWED BY ANOTHER SEAT on this row."
}
```

## IRPT_DASHBD-W1-S1 -- series.json.gz has no X10 family: the validator refuses both the extension and a second family on the table; manifest family registered alone

```json
{
  "id": "IRPT_DASHBD-W1-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T02:45:00Z",
  "one_line": "TO-DB-b-2 amendment 1 asks for a platinum/reporting policy family PER served file; the X10 validator refuses series.json.gz (extension) and refuses two families on one table, so only the MANIFEST family is registered, as the amendment's own fallback says.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-2 ISSUER AMENDMENT 1 (PRD v0.3 ruling 16): add, for firm 49financial, the families the X10 register admits for the two served files, tier platinum, table reporting, one family per file; if the validator refuses series.json.gz as an extension, record the refusal text verbatim in a row and register the manifest family alone.",
  "world_is": "lib/opal_naming.py:_validate_reporting_policies, probed against the live registry with a candidate policy (probe script .scratch/pol_probe.py in the worker worktree, not committed): (A) a SERIES family with extension 'json.gz' -> ValueError 'reporting content format is not admitted' (the admitted set is csv/json/pdf, line 1822); (B) the same with a MANIFEST family beside it -> the same refusal; (C) SERIES with extension 'json' plus MANIFEST with extension 'json', both table 'reporting' -> ValueError 'reporting families must have distinct tables' (line 1819); (D) the MANIFEST family alone -> accepted. Registered: infra/logic/registry/reporting_policies.json policy irpt-dashbd-served-reporting, revision irpt-dashbd-x10-v1, firms [49financial], family SERVED_MANIFEST (platinum, reporting, json, unreferenced_days null, accepted_ceiling_days 2555), state PENDING_ENFORCEMENT with enforcement_ref null (an ACTIVE state requires an accepted enforcement commit this cell does not hold; nothing here calls reporting_destination, the publisher addresses the files with address()). lib.opal_naming.load_registry() loads; DB-2-AC1's policy limb reads 1 platinum/reporting family for 49financial.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming.py lines 1814-1825 @11bf813387",
      "infra/logic/registry/reporting_policies.json @11bf813387"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The series.json.gz file therefore has NO X10 family: its retention/disposal class is unregistered. Whether the registry should admit a gzip JSON format or two families per table is the registry owner's call; nothing in this cell depends on it."
}
```

## IRPT_DASHBD-W1-S2 -- the naming gate refuses the firm-tokened source-map key the order names; the artifact is keyed by the scope-less builder name

```json
{
  "id": "IRPT_DASHBD-W1-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T02:50:00Z",
  "one_line": "TO-DB-b-2 names the source-map entry and the build invocation irpt-49f-reporting-publish-lambda; the commit-time naming gate REFUSES a new hand-kept firm token ('49f') in lambda-source-map.json, so the entry is keyed irpt-reporting-publish-lambda (scope-less builder name) and the artifact is investor-reporting/irpt-reporting-publish-lambda.zip.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-2 WORKER FACE: 'Register the function in lambda-source-map.json (a new entry shaped like irpt-holdings-performance-lambda) and run build-and-upload.sh investor-reporting irpt-49f-reporting-publish-lambda'; the Terraform artifact_key is investor-reporting/<name>.zip.",
  "world_is": "safe-commit.sh's naming limb (.tools/naming-gate.py, ENFORCE) refused the commit with NAMING REFUSE infra/aws/lambda/ci/lambda-source-map.json irpt-49f-reporting-publish-lambda ('CONFORMANT as LAMBDA, but a NEW hand-kept carrier of 49f outside every permitted context: read it through lookup(49financial)') on the map key and on its iam_role value, and on the same name typed in two Terraform output descriptions. The existing firm-token keys in that map (bd-49f-*) predate the gate. Done instead: the map key is the scope-less builder name name('irpt', None, 'reporting-publish', 'lambda') = irpt-reporting-publish-lambda, derived in Terraform by an opal_name module with no scope; the Lambda FUNCTION is still the firm-scoped builder name (irpt-49f-reporting-publish-lambda, scope = the registry-derived firm) and its role irpt-49f-reporting-publish-role; the entry carries no iam_role (no tool reads it). The build invocation is build-and-upload.sh investor-reporting irpt-reporting-publish-lambda. The issuer's apply plans against artifact key investor-reporting/irpt-reporting-publish-lambda.zip.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "naming-gate output on the first safe-commit attempt of this worker's second commit, 2026-10-02 ~02:40Z",
      "infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf module irpt_reporting_publish_artifact_name"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S12 -- The served platinum file series.json.gz has NO retention family in the X10 register: the validator admits only csv/json/pdf and one family per table, so round 1 registered the manifest family alone (row W1-S1). Whether the register admits gzip JSON or a second reporting table is the register owner's question (CTO round-1 analysis E2); the served file is not blocked on it.

```json
{
 "id": "IRPT_DASHBD-S12",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T05:05:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "The served platinum file series.json.gz has NO retention family in the X10 register: the validator admits only csv/json/pdf and one family per table, so round 1 registered the manifest family alone (row W1-S1). Whether the register admits gzip JSON or a second reporting table is the register owner's question (CTO round-1 analysis E2); the served file is not blocked on it.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "4.0.0_SA_CRO (incumbent of lane IRPT_COMPLETION_REGISTRY, the X10 policy in infra/logic/registry/reporting_policies.json; naming-owner review per the lane note)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "row IRPT_DASHBD-W1-S1 (worker 0.9.0_WK_IRPT_DASHBD~1, merged @9000ce5a08): lib/opal_naming.py:_validate_reporting_policies refused a SERIES family with extension 'json.gz' ('reporting content format is not admitted', admitted set csv/json/pdf) and refused two families on table 'reporting' ('reporting families must have distinct tables'); the MANIFEST family alone was accepted.",
   "infra/logic/registry/reporting_policies.json at CLOUD @9000ce5a08: policy irpt-dashbd-served-reporting, revision irpt-dashbd-x10-v1, firms [49financial], one family SERVED_MANIFEST (platinum, reporting, json), state PENDING_ENFORCEMENT.",
   "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_1_B_20261002.md section 3 item E2: 'as a registry question to the registry's owner (infra/logic/registry/), carried as one row; not a build cell in this round. The served file is not blocked on it.'",
   "git show HEAD:.owned-paths.yaml: lane IRPT_COMPLETION_REGISTRY permitted_agents 4.0.0_SA_CRO, ~A, ~B, ~C, ~D, 2.0.0_SA_COO~M ('X10 twelve-family policy')."
  ]
 },
 "spec_asserts": "TO-DB-b-2 issuer amendment 1 on PRD v0.3 ruling 16: round-1 policy rows cover the platinum served files, one family per file (series.json.gz and manifest.json).",
 "world_is": "MEASURED: one of the two served files has a family; series.json.gz, the file the page reads, has none, so its retention and disposal class is unregistered.",
 "notes": "Two remedies the register owner can choose between: admit a gzip JSON content format, or admit a second reporting table (for example reporting_series) so the series takes its own family. Either is a register edit plus the validator's admitted set; neither is an IRPT_DASHBD build cell."
}
```

## IRPT_DASHBD-S13 -- Nothing refreshes the reporting gold the publisher reads: account_return_daily ends at date=2026-09-28 (559 partitions) and no schedule, runner or Lambda runs account_return_daily.py, so on 2026-10-02 the gold is three trading days behind T-1 and E1's 08:15 ET publisher schedule would republish the 2026-09-28 series every weekday.

```json
{
 "id": "IRPT_DASHBD-S13",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T05:20:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "Nothing refreshes the reporting gold the publisher reads: account_return_daily ends at date=2026-09-28 (559 partitions) and no schedule, runner or Lambda runs account_return_daily.py, so on 2026-10-02 the gold is three trading days behind T-1 and E1's 08:15 ET publisher schedule would republish the 2026-09-28 series every weekday.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "disarm_owner": "1.0.0_SA_CTO (an addendum to the round-1 analysis: the adapter's scheduled fire as a round-2 cell, and its order against E1's publisher schedule)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "aws s3api list-objects-v2 --bucket opal-data-49financial --prefix irpt/49financial/gold/account_return_daily/ --delimiter / (2026-10-02 ~05:1xZ): 559 date= partitions, newest date=2026-09-28.",
   "comp-find 'irpt_reporting|account_return_daily' infra/ data/assets/scripts/: 118 hits across 12,647 files; band CONFIG 11 of 11 are sources.json and the two new lambda-source-map.json entries (publisher, read route); no schedule, EventBridge rule, runner script or Lambda packages or invokes account_return_daily.py.",
   "decompositions/IRPT_DASHBD_DECOMP.md section 1, 'Carried, not cut': 'the scheduled fire of the adapter (round 2, its own ledger, as IB-er-203 was to IB-er-202)'; section 1 also: the adapter is 'run ad hoc for the round-1 sample (a QA run)'.",
   "lib/trading_calendar.py: 2026-10-02 is a Friday; the T-1 trading day is 2026-10-01; 2026-09-29, 09-30 and 10-01 are absent from the gold."
  ]
 },
 "spec_asserts": "CTO round-1 analysis @57304c750b section 3 E1: 'The 08:15 ET schedule is the production trigger (a success-of-upstream trigger would be a defect); the gold it reads is T-1.'",
 "world_is": "MEASURED: the gold is frozen at 2026-09-28 and nothing in the estate moves it; the 08:15 ET publisher would serve an as_of of 2026-09-28 on every weekday until the adapter runs on its own clock. CLAUDE.md: production pipelines MUST be scheduled; an ad-hoc gold run is QA evidence, never production.",
 "notes": "Recommended: add the adapter's scheduled fire as round-2 cell DB-b-7 (a scheduled Lambda packaging account_return_daily.py unedited, the holdings-performance pattern, its own root and ledger, firing before 08:15 ET), apply E1's read root now, and apply the publisher's schedule in the same packet only once the adapter's schedule is applied. The read route serves the 2026-09-28 series honestly meanwhile (its manifest carries as_of)."
}
```

## IRPT_DASHBD-S14 -- The reporting-read role reads more than the order's 'ONLY the platinum prefix': it also reads the directory pointer + artifact and the ownership map (the scope dependencies the shared boundary re-reads per request) and the service-profile row in opal-users-v2; the code cites row W1-S3 for this, which was never filed (the stopped worker's comment).

```json
{
 "id": "IRPT_DASHBD-S14",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T05:30:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "The reporting-read role reads more than the order's 'ONLY the platinum prefix': it also reads the directory pointer + artifact and the ownership map (the scope dependencies the shared boundary re-reads per request) and the service-profile row in opal-users-v2; the code cites row W1-S3 for this, which was never filed (the stopped worker's comment).",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "2.0.0_SA_COO~P (named in the E1 never-widen packet's blast radius; the CTO half reads it)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "infra/aws/terraform/investor-reporting/reporting-read/iam.tf:3-7 and statements ReadCurrentScopeDependencies (local.irpt_rr_scope_dependency_arns) and the service-profile policy :99-138 (dynamodb:Query on opal-users-v2/index/email-index, dynamodb:GetItem on opal-users-v2, kms:Decrypt via DynamoDB only) at CLOUD @76a5e50ed3.",
   "TO-DB-b-4 worker face: 'a role reading ONLY the platinum prefix of the firm bucket'.",
   "the channel at @76a5e50ed3 holds W1-S1 and W1-S2 only; iam.tf:7 cites 'row IRPT_DASHBD-W1-S3', which no channel file carries."
  ]
 },
 "spec_asserts": "TO-DB-b-4: the read function's role reads ONLY the platinum prefix of the firm bucket.",
 "world_is": "MEASURED: the role also carries the Holdings function's scope-dependency grants (directory + ownership map, object-scoped) and the service-profile read; without them the shared boundary cannot resolve a viewer's scope or a service principal's allowed firms. A product read beyond platinum: none. Write: none.",
 "notes": "Accepted as the boundary's own dependency, not a widening of the product read: the E1 packet lists every statement. iam.tf:7 is re-pointed from W1-S3 to this row."
}
```

## IRPT_DASHBD-S15 -- The read route is created in its own root against the existing portal API and is NOT in docs/contracts/investor-reporting/v1/routes.json, the file routetable.py calls the ONE carrier of the route table; so the unguarded-route census and the api root do not see it. The code cites row W1-S4 for this, which was never filed.

```json
{
 "id": "IRPT_DASHBD-S15",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T05:30:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "The read route is created in its own root against the existing portal API and is NOT in docs/contracts/investor-reporting/v1/routes.json, the file routetable.py calls the ONE carrier of the route table; so the unguarded-route census and the api root do not see it. The code cites row W1-S4 for this, which was never filed.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "1.0.0_SA_CTO (whether the route joins routes.json and the api root's function map, or stays in its own root with a census entry)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "infra/aws/terraform/investor-reporting/reporting-read/api.tf:1-11, :24-30 (aws_apigatewayv2_route under the EXISTING CUSTOM authorizer, local.portal_authorizer) at CLOUD @76a5e50ed3.",
   "infra/aws/lambda/investor-reporting/_authz/routetable.py:12-15: routes.json is 'the ONE carrier of the route table ... A route that is not here is not reachable, and a route that is here is.'",
   "TO-DB-b-4: 'adding a route to ANOTHER function's ROUTES or to the deployed boundary's route table raised EntryError' (IRPT_BCKEND-W88-S1), which is why the route was declared in its own root."
  ]
 },
 "spec_asserts": "routetable.py:12-15: every reachable route is in routes.json.",
 "world_is": "MEASURED BY CODE READ, NOT EXERCISED: once E1 applies, one reachable route exists outside routes.json, so routetable.py's census population omits it (its guardedness is then asserted by DB-4-AC1's local refusal arm only).",
 "notes": "Not a runtime refusal: API Gateway serves the route from this root's resources; the authorizer is the existing portal one. api.tf:11 is re-pointed from W1-S4 to this row."
}
```

## IRPT_DASHBD-W1-S5 -- the 1,498.38 USD residual on 0027265115 is a whole-window net of four offsetting classes, not one leg on 2026-07-07

```json
{
  "id": "IRPT_DASHBD-W1-S5",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T06:10:00Z",
  "one_line": "TO-DB-b-6: the 1,498.38 USD residual on 0027265115 is not on 2026-07-07 and not one leg; it is the whole-window net of four offsetting classes (in-kind -7,252.16, margin interest +10,724.31, per-asset trade/merger -3,277.48, cash +1,303.71), and DB-6-AC1 sums is_residual legs by absolute value so a signed net can only pass through a derived net leg.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-6 cell: the residual sits on a flow day after a 925.02 fee leg and is made by ONE leg (in-kind valued differently, internal-here/external-at-vendor, or other); DB-6-AC1 sums the is_residual legs in absolute value to the residual.",
  "world_is": "MEASURED: Opal gold external_flow over 2026-03-16..2026-08-28 = 1,043,100.5277 and Black Diamond account netAdditions for the same range = 1,044,598.9077, difference 1,498.38; the 2026-07-07 fee leg matches to the cent (Schwab TPFEE 2,423.40 = vendor fees 2,423.40). The difference decomposes across 8 in-kind legs, 1 margin-interest asset, 532 per-asset trade differences and the CASH asset with mixed signs; the record carries one derived net leg flagged is_residual and the components unflagged because the check adds absolute values.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/FLOW_RESIDUAL_0027265115_R2.json",
      "s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/2026-08-30/reporting_performance_22596361_2026-08-28.json",
      "s3://opal-data-assets/schwab/08335338/silver/fact_trn/date=2026-07-07/data.parquet",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r2/p2_6_ac1_flow_residual_record.py line 'resid_sum += abs(amount)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The Black Diamond transactions/activity family is not landed (bronze holds reporting_performance, allocation, costbasis, fees, roster); per-day vendor flow detail would live there. Grading of the net-versus-leg framing is the CTO's ruling."
}
```

## IRPT_DASHBD-S16 -- The seating lint (.tools/to-decomp-ref-lint.py, gate2, ANNOUNCE) read TO-DB-b-6's <issued_to> 0.9.0_WK_IRPT_DASHBD~1 as '0.9.0_WK_IRPT' and reported it as holding three open IRPT_BCKEND orders (IB-rth-3, IB-yr-242, IB-yr-261), which belong to 0.9.0_WK_IRPT_BCKEND~<n> slots: two projects' worker slots collapse to one seat. Armed (pipeline-gate2.enforce), it would refuse a correct issuance.

```json
{
 "id": "IRPT_DASHBD-S16",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T05:45:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "The seating lint (.tools/to-decomp-ref-lint.py, gate2, ANNOUNCE) read TO-DB-b-6's <issued_to> 0.9.0_WK_IRPT_DASHBD~1 as '0.9.0_WK_IRPT' and reported it as holding three open IRPT_BCKEND orders (IB-rth-3, IB-yr-242, IB-yr-261), which belong to 0.9.0_WK_IRPT_BCKEND~<n> slots: two projects' worker slots collapse to one seat. Armed (pipeline-gate2.enforce), it would refuse a correct issuance.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "1.0.0_SA_CTO (the gate's owner: the seating frame's serial parse, before pipeline-gate2.enforce is ever created)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "safe-commit output of the issuance @97eaff05ff, 2026-10-02 ~04:58Z: '[gate2] SEATING: this NEW task order for IRPT_DASHBD is addressed to 0.9.0_WK_IRPT, which already holds open TOs on 1 OTHER pipeline project(s): IRPT_BCKEND (3 open: IRPT_BCKEND.TO-IB-rth-3..., IRPT_BCKEND.TO-IB-yr-242..., IRPT_BCKEND.TO-IB-yr-261...)' then '[gate2] ANNOUNCE mode -- NOT blocking this commit.'",
   "org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-6.flow-residual-0027265115.md:5 <issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>; the three IRPT_BCKEND orders are issued to 0.9.0_WK_IRPT_BCKEND~<n> slots (to-check census at session start).",
   "CLAUDE.md rule 27: the seating rule is ONE PROJECT PER TIER-2 SEAT INSTANCE; a worker is a subagent slot, 0.9.0_WK_<CODE>~<n>, whose CODE is the project."
  ]
 },
 "spec_asserts": "to-decomp-ref-lint seating frame: one project per seat instance, keyed by the full serial.",
 "world_is": "MEASURED: the frame keys on a truncated serial, so every 0.9.0_WK_IRPT_* slot of every IRPT project is one 'seat'. ANNOUNCE today; the false refusal is reachable the moment the enforce file exists.",
 "notes": "Not this project's to fix; carried here because this order tripped it. The order stands as cut."
}
```

## IRPT_DASHBD-S17 -- Row S16 is NOT fixed at HEAD: the seating lint's SERIAL_RE fix @453c6430ec (the name class admits an underscore) is an ancestor of HEAD, and the round-3 issuance @c75ddc5d61 still printed 'addressed to 0.9.0_WK_IRPT' for both new orders, so the truncation happens on another path than SERIAL_RE.

```json
{
 "id": "IRPT_DASHBD-S17",
 "project": "IRPT_DASHBD",
 "fabric": "laptop",
 "surfaced_by": "2.0.0_SA_COO~P",
 "surfaced_at": "2026-10-02T07:00:00Z",
 "disposition": "UNDER_INVESTIGATION",
 "one_line": "Row S16 is NOT fixed at HEAD: the seating lint's SERIAL_RE fix @453c6430ec (the name class admits an underscore) is an ancestor of HEAD, and the round-3 issuance @c75ddc5d61 still printed 'addressed to 0.9.0_WK_IRPT' for both new orders, so the truncation happens on another path than SERIAL_RE.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "1.0.0_SA_CTO (the gate's owner; the CTO's round-2 analysis section 3 answered S16 as fixed)",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git merge-base --is-ancestor 453c6430ec HEAD -> true at CLOUD c75ddc5d61; git show 453c6430ec -- .tools/to-decomp-ref-lint.py: SERIAL_RE's name class changed from [A-Za-z0-9]* to [A-Za-z0-9_]*.",
   "safe-commit output of the round-3 issuance @c75ddc5d61, 2026-10-02 ~06:5xZ: '[gate2]   REFUSED: ...IRPT_DASHBD.TO-DB-b-7...' and '...TO-DB-b-9...', each with 'SEATING: this NEW task order for IRPT_DASHBD is addressed to 0.9.0_WK_IRPT, which already holds open TOs on 1 OTHER pipeline project(s): IRPT_BCKEND (3 open ...)'; ANNOUNCE mode, not blocking.",
   "both orders carry <issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to> (line 5)."
  ]
 },
 "spec_asserts": "CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_2_B_20261002.md section 3: 'S16 ... fixed @453c6430ec (SERIAL_RE admits an underscore) and on origin since the 2026-10-01 push. Answered.'",
 "world_is": "MEASURED: with the fix at HEAD, the lint's seating frame still keys the two new orders on '0.9.0_WK_IRPT'. Not measured: which function truncates (the issued_to parse or the holdings index).",
 "notes": "ANNOUNCE only; the orders stand as cut. S16 stays open under this correction."
}
```

## IRPT_DASHBD-W1-S6 -- TO-DB-b-7: no fire minute exists under the order's rule -- schwab dim_position and dim_balance for date=2026-09-29 landed 2026-09-30 17:46:40 ET (single object version, 12 hours after the 05:46 ET pat

```json
{
  "id": "IRPT_DASHBD-W1-S6",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T07:40:00Z",
  "one_line": "TO-DB-b-7: no fire minute exists under the order's rule -- schwab dim_position and dim_balance for date=2026-09-29 landed 2026-09-30 17:46:40 ET (single object version, 12 hours after the 05:46 ET pattern every other measured day holds), and holdings_performance_daily date=2026-09-28's current object was rewritten 2026-09-29 10:45:04 ET; the fire-time limb is STOPPED and no time is chosen.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-7: choose the earliest whole minute at or after the latest landing seen plus >= 10 minutes, strictly before the publisher's 08:15 ET; 'If no such minute exists (an input lands after 08:05 ET on any measured day), STOP that limb: it is a row naming the input and the days, never a later publisher time chosen here.' DB-7-AC1 and DB-7-AC3 grade a chosen time and a plan carrying the schedule at it.",
  "world_is": "MEASURED over the last 12 date= partitions (2026-09-15..2026-09-30) of each of the four inputs, America/New_York: fact_trn latest 05:46; dim_position and dim_balance latest 17:46 (date=2026-09-29 -> LastModified 2026-09-30 17:46:40 EDT, list_object_versions shows ONE version, so it is the first landing, not a rewrite; the other 11 days land 05:46); holdings_performance_daily latest 10:45 (date=2026-09-28 current version 2026-09-29 10:45:04, first version 2026-09-29 07:30:21 = the scheduled 07:30 fire; its other partitions are manual rewrites at 05:25 on 09-29, its organic scheduled landings so far are 09-28 at 07:30:21 and 09-30 at 2026-10-01 07:30:19). No chosen minute exists, so REPORTING_GOLD_FIRE_TIME_R3.json carries chosen_et and chosen_cron null with status STOPPED, DB-7-AC1 FAILs (not an HH:MM time) and DB-7-AC3 FAILs (no schedule at the recorded cron). The Terraform root reads the cron from the record and plans no schedule while it is null. INFORMATION, NOT A CHOICE: with the one 17:46 silver day set aside, the silver pattern is 05:46:44 and the holdings guard fires 07:30 and writes by 07:30:21, which would admit a minute in 07:41..08:14; setting it aside is the issuer's or the CTO's ruling. A fixed clock cannot cover a 12-hour-late silver day in either case: that day's partition is absent when a 07:xx fire runs.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json",
      "s3://opal-data-assets/schwab/08335338/silver/dim_balance/date=2026-09-29/data.parquet (list_object_versions: 1 version, LastModified 2026-09-30T17:46:40-04:00)",
      "s3://opal-data-assets/schwab/08335338/silver/dim_position/date=2026-09-29/data.parquet (list_object_versions: 1 version, LastModified 2026-09-30T17:46:40-04:00)",
      "s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/date=2026-09-28/data.parquet (2 versions: 2026-09-29T07:30:21-04:00, 2026-09-29T10:45:04-04:00)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the ruling: 2.0.0_SA_COO~P (the order) / 1.0.0_SA_CTO. Once a chosen_cron is written into the record, re-running terraform plan in infra/aws/terraform/investor-reporting/reporting-gold/ adds the schedule and its scheduler role with no other edit."
}
```

## IRPT_DASHBD-W1-S7 -- TO-DB-b-7: the order is silent on two facts the handler had to decide -- the served gold holds SIX accounts per partition (not the ~7,800 the silver carries), and the producer's main() --upload also r

```json
{
  "id": "IRPT_DASHBD-W1-S7",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T07:41:00Z",
  "one_line": "TO-DB-b-7: the order is silent on two facts the handler had to decide -- the served gold holds SIX accounts per partition (not the ~7,800 the silver carries), and the producer's main() --upload also rewrites dim_return_method (tieout null, measured_at now) which the role may not write; the handler takes the newest partition's account set and omits that one call.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-7: 'run the producer for EVERY trading day after it through T-1 ... upload' and DB-7-AC2 'reproduces the served partition row for row'; the role writes ONLY the account_return_daily gold prefix.",
  "world_is": "MEASURED: s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-28/ holds 6 rows (accounts 0010783709, 0027265115, 0035940058, 0076459710, 0084073310, 0091939812; manifest rows=6), so a scheduled run with no --accounts restriction would write ~7,800 accounts into a partition family of six. READ at account_return_daily.py main() (lines 1851-1856): every --upload ends with emit_method_row(..., tieout=args.tieout) -- a write to the dim_return_method prefix outside the role's grant, with tieout_tolerance_proposed null unless --tieout is passed. Handler decision (infra/aws/lambda/investor-reporting/reporting-gold/handler.py): accounts = account_ids of the gold's newest landed partition (event 'accounts' overrides); the producer's own load_declaration/firm_scope/first_data_dates/prefetch/compute_range/emit_day are composed as main() does, and emit_method_row is not called. The producer is unedited.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py main() lines ~1820-1858 @e1b160d340",
      "s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-28/manifest.json (rows 6; first_data_date keys: 6)",
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py compute()/run()"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Widening the population beyond six accounts is a separate deliberate act (the event's accounts key), not this function's default. Grading of the decision is the CTO's."
}
```

## IRPT_DASHBD-W1-S8 -- TO-DB-b-7: amendment 1 set aside one day, but 9 of the 12 holdings partitions are first-written by a 2026-09-28 20:25 ET bulk backfill; excluded as unscheduled writes, 07:41 ET chosen

```json
{
  "id": "IRPT_DASHBD-W1-S8",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T08:10:00Z",
  "one_line": "TO-DB-b-7 amendment 1 set aside ONE incident (the 09-29 silver day) but holdings_performance_daily's first versions for 9 of the 12 measured partitions (2026-09-15..09-25) are the 2026-09-28 20:25 ET bulk catch-up act, also after 08:05 ET; the worker excluded them as unscheduled writes on the amendment's own clause (a) and chose 07:41 ET.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-7 amendment 1: a landing is a partition's FIRST version's LastModified; one day is set aside as an incident; latest_landing_et is over the rest; days_measured >= 10; expected fire 07:41 ET (07:30:21 + 10 min).",
  "world_is": "MEASURED by list_object_versions over opal-data-49financial irpt/49financial/gold/holdings_performance_daily/: the partitions 2024-07-09..2026-09-25 (hundreds) were all first written by one manual backfill on 2026-09-28 20:25-21:36 ET and rewritten 2026-09-29 02:43/02:56 and 05:05/05:25; the guard's own scheduled writes exist for only two days (date=2026-09-28 first version 2026-09-29 07:30:21, date=2026-09-30 first version 2026-10-01 07:30:19), plus date=2026-09-29 first version 2026-10-01 03:13:37 (an unscheduled run, before 07:30). Read literally, first-version landings 2026-09-28 20:25 for 9 of the 12 window partitions put the latest landing at 20:26 and the order's own stop clause fires again; the record instead lists all 12 first versions (days_measured 12) and carries each of the 9 backfill partitions in `excluded` with reason, so latest_landing_et for the holdings input is 07:30 (03:13 and 07:30:21/07:30:19 remaining). The record's `excluded` list holds 11 entries (2 silver incident + 9 backfill). Result: chosen 07:41 ET, plan 7 to add, 0 change, 0 destroy. The extension of the ruling from one day to the backfill partitions is the worker's reading of clause (a) (a landing is the scheduled write), not stated in the amendment. Only two organic scheduled holdings landings exist, so the holdings input's scheduled-landing pattern rests on 2 days of 07:30:2x; the guard is a 07:30 cron, so it cannot land before 07:30.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json (excluded list, 11 entries)",
      "s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/ (list_object_versions, 12 window partitions)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Residual for the issuer's packet, also written into the record's notes: a day whose holdings guard lands after the fire emits with the guard not reached and is not re-emitted later. Owner of grading the extension: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S9 -- TO-DB-b-9: the served 49F engine reads a vendored COPY of the table from its deployed bundle (s3 _code/ref/), and the reporting-gold Lambda a pinned one -- the table edit alone moves neither

```json
{
  "id": "IRPT_DASHBD-W1-S9",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T08:50:00Z",
  "one_line": "TO-DB-b-9: the order names the CRO's repo file as THE table, but the served 49F engine does not read it -- it reads a vendored byte-identical COPY in its deployed bundle at s3://opal-data-49financial/_code/ref/, so the table edit reaches the served engine only if the packet's deploy leg also lands that copy; the census also finds the reporting-gold Lambda packages its own pinned table.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-9: 'every served engine that reads the table moves under ONE packet with both halves' and the cell's pointer to the served 49F engine's reader a05_ref_txn_classification.py, whose SOURCE_JSON resolves the repo path org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json.",
  "world_is": "MEASURED: a05_ref_txn_classification.py:40-45 tries the repo path first and otherwise reads _HERE/ref/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json (its own comment: the bundle layout reads a script-adjacent vendored copy that the deploy leg ships). The deployed bundle holds s3://opal-data-49financial/_code/a05_ref_txn_classification.py (2026-08-19 15:01, 6,278 bytes) and s3://opal-data-49financial/_code/ref/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json (2026-08-19 12:05, 64,794 bytes, sha256 d83ef318ed44... == the repo file's bytes today). So an edit of the CRO's file alone leaves the served 49F engine (gold/advi/reference/ref_txn_classification and canonical/flow_ledger, 562 partitions to 2026-09-30) classing FTP/FTR as EXTERNAL until that S3 copy is replaced. Two other homes of the table were found: infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-gold-lambda packages a PINNED table (pin 5bb3b2626d, blob sha256 0f34bef7c850...) with a pinned producer (pin e1b160d340), and data/assets/scripts/gold/irpt_reporting/sources.json carries withholding_override_comment text describing the override the patch retires.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py lines 40-45 @b7a512991b",
      "aws s3 ls s3://opal-data-49financial/_code/ (2026-10-02 08:3xZ): the two keys above; aws s3 cp of the ref copy hashed sha256 d83ef318ed443b71a96ba95a4930cc04c7ce3a42756a5927418aecaee531df08 == sha256sum of the repo file (CRLF working bytes; git blob form 0f34bef7c850...)",
      "infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-gold-lambda staged_from[] @b7a512991b",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/FTP_INTERNAL_BLAST_R3.json (the reader census)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Nothing moves in this cell. For the packet: the 49F half needs the vendored copy replaced in the same act (and a05 re-run so ref_txn_classification's table_version changes), the IRPT half needs the pinned table and producer re-staged together (the retirement alone, on the old table, would let FTP/FTR enter F_t). Owner of the packet: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S10 -- TO-DB-b-9: the code table is generated and the two foreign-tax cells read EXTERNAL because of rule ORDER in the builder, so the CRO's edit is two files

```json
{
  "id": "IRPT_DASHBD-W1-S10",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T09:05:00Z",
  "one_line": "TO-DB-b-9: the CRO's table is GENERATED, and the cause of FTP/FC/WD and FTR/FC/WD reading EXTERNAL is rule ORDER in its builder (wd-generic precedes foreign-tax in a first-match list); a hand edit of the JSON that the builder is later re-run over would silently revert, so the CRO's edit is two files.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-9: 'both codes move to INTERNAL (tax) in the table's owner's edit (4.0.0_SA_CRO)' -- the cell treats the table as a file to edit.",
  "world_is": "MEASURED by reading org/tier1_exec/4.0.0_SA_CRO/scripts/build_schwab_txn_classification.py @b7a512991b: RULES is a first-match list (classify() returns the first predicate that holds). Line 65 'wd-generic' R(sb={'WD','WI'}) -> EXTERNAL sits before line 74 'foreign-tax' R(code={'FTP','FTR'}) -> INTERNAL, so the cell (tran_srcde FTP, tr_cd FC, sb_cd WD) lands on wd-generic and the 'foreign-tax' rule only ever reaches the FC/FC cells (FTP/FC/FC 9 rows, FTR/FC/FC 12 rows, both INTERNAL in the table today). The BW* withholding codes on sb_cd WD are INTERNAL only because their 'withholding' rule (line 53) precedes wd-generic. The edited table copy used for the equivalence run therefore sets rule foreign-tax and partition INTERNAL on exactly the two cells, which is what moving foreign-tax ahead of wd-generic in the builder would regenerate.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/scripts/build_schwab_txn_classification.py lines 53, 65, 74 and classify() @b7a512991b",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json: FTP/FC/WD rule wd-generic EXTERNAL; FTP/FC/FC rule foreign-tax INTERNAL; FTR/FC/WD wd-generic EXTERNAL; FTR/FC/FC foreign-tax INTERNAL"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Nothing is edited here. For the CRO's edit: move the foreign-tax rule ahead of wd-generic in the builder (or hand-edit the two JSON rows and leave the builder note), and keep the two files agreeing. Owner: 4.0.0_SA_CRO / the packet's issuer."
}
```

## IRPT_DASHBD-S18 -- the PRD names a function that does not exist and none of the seven reporting-gold resources

```json
{
  "id": "IRPT_DASHBD-S18",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-02T09:50:00Z",
  "one_line": "The PRD cites none of the seven reporting-gold resource names now live (DB-b-7, applied 08:03Z), and the one function name it does print, irpt-49f-reporting-adapter-lambda (PRD v0.6 line 152, C-NAMES), does not exist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's DB-b-7 grade (2026-10-02 08:xZ-09:xZ): 7 of 7 live names equal lib/opal_naming.py name() output and the gold prefix equals address() output",
      "org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md:152 (C-NAMES) prints irpt-49f-reporting-adapter-lambda; lambda get-function on it: ResourceNotFound; positive control, get-function on the live reporting-gold function: OK; 0 of 7 live names occur in the PRD"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md rule 30: the L4 PRD cites builder output for every new address and name, and the CTO refuses a PRD that types one.",
  "world_is": "The live names are right (builder output) but the PRD that is supposed to carry them names a function that was never made and omits the seven that were. A reader of the PRD cannot find the deployed resources.",
  "notes": "INERT: the names are correct; the record is behind. Owner 1.0.0_SA_CTO (the PRD's author): a header-level addendum printing the seven builder outputs."
}
```

## IRPT_DASHBD-S19 -- DB-7-AC1 counts 12 landings for the binding input; 3 are kept after exclusions

```json
{
  "id": "IRPT_DASHBD-S19",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-02T09:50:00Z",
  "one_line": "DB-7-AC1 requires each input of the fire-time rule to have at least 10 measured landings; for holdings_performance_daily, the input that sets the 07:41 schedule, 9 of its 12 landings are excluded and 3 are kept (2 of them organic 07:30 fires), and AC1 counts all 12.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json, inputs entry for holdings_performance_daily: 12 landings, 'excluded' lists 9, 3 kept",
      "DB-7-AC1 re-run by this seat: PASS as worded (the count reads 12)",
      "the schedule live: cron(41 7 ? * MON-FRI *) America/New_York (this seat's DB-b-7 grade)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DB-7-AC1: each input with at least 10 measured landings, so the fire time rests on a measured distribution.",
  "world_is": "The binding input's fire time rests on 3 kept landings, 2 of them organic. The criterion passes because it counts landings before the exclusions it then applies. Whether 07:41 is late enough is untested on the days that were excluded.",
  "notes": "INERT until the first fire (11:41Z today) and the days after: a fire before its input lands is visible in the next morning's partitions. Owner 2.0.0_SA_COO~P (the issuer, who may amend its own criterion); A1 of ledger irpt-dashbd-reporting-gold-apply-20261002 is the first real read."
}
```
