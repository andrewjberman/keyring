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

## IRPT_DASHBD-S20 -- the picker suffix and the body date "data through" from two fields nothing ties

```json
{
  "id": "IRPT_DASHBD-S20",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-02T13:10:00Z",
  "one_line": "The account picker's dashboard suffix dates its 'data through' from manifest.as_of (pickerSuffix.ts:30) while the page body prints series.as_of (DashboardPerformance.tsx:241); reportingRead.ts:57-74 never checks they are equal, so a manifest and series of different vintages would show one account two 'data through' dates.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal origin/DEV 3bbf3914 (item 72, 0531cc65): pickerSuffix.ts:28-34, DashboardPerformance.tsx:241, reportingRead.ts:57-74, read by this seat's grade 2026-10-02 12:xZ",
      "CTO RULINGS batch 128 item 1: the suffix carries 'the same basis words the body shows (... data through ...)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Batch 128 item 1: one return series per page; the suffix and the body show the same basis, including the same 'data through' date.",
  "world_is": "Two fields stand for one date and nothing ties them. Not observed on served data: the publisher writes both files in one run today.",
  "notes": "INERT. Owner 2.0.0_SA_COO~D: read one date for both, or refuse the pair when manifest.as_of and series.as_of differ."
}
```

```json
{
  "id": "IRPT_DASHBD-S21",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~P",
  "surfaced_at": "2026-10-02T13:36:00Z",
  "one_line": "DB-b-8 Q1: the deployed publisher writes an account's two platinum keys, then heads the series object, and its role has PutObject but no GetObject on platinum/reporting, so HeadObject answers 403 and the run aborts after the FIRST account.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lambda invoke irpt-49f-reporting-publish-lambda payload {} at 13:35:40Z: StatusCode 200, FunctionError Unhandled, ClientError (403) HeadObject at handler.py:158 (requestId a4019573-aaa5-4a52-91f8-d54dfe249a99)",
      "list-object-versions platinum/reporting/: only account=0010783709/{series.json.gz,manifest.json} gained versions (o_ptRn2R..., CGN8oqs2..., 13:36:00Z); the other 10 keys unchanged",
      "infra/aws/terraform/investor-reporting/reporting-publish/iam.tf (dd3d644cd6): 'PutObject only -- no GetObject, no delete' on platinum/reporting/*"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The packet (blob 38a6eb19a1) expected Q1 to write 12 new versions as_of 2026-10-01; the role policy was planned without the read the handler's read-back needs.",
  "world_is": "Two keys were written, then the run failed. Rolled back per the signed half: copy-object from the recorded versions at 13:3xZ, new current versions qvtMQgRd (series) and S4JjNhUe (manifest), ETags equal to the 02:30Z versions, manifest as_of 2026-09-28. All 12 served keys equal the pre-act state. Monday's scheduled fire would fail the same way.",
  "notes": "Remedy (this seat, inside its decomposition; the served change goes under the packet's amendment with both halves): iam.tf adds s3:GetObject on the same platinum/reporting/* ARNs (plan 0/1/0, the role policy only). Disarm owner 2.0.0_SA_COO~P; if the amendment is not applied before Monday 2026-10-05 07:00 ET, the schedule goes DISABLED (the packet's stop path)."
}
```

## IRPT_DASHBD-W1-S11 -- TO-DB-b-10: the estate's BD client needs a session-token GET before the performancePeriod POST, so 'no other vendor call' has one unavoidable companion

```json
{
  "id": "IRPT_DASHBD-W1-S11",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T13:45:00Z",
  "one_line": "TO-DB-b-10: the estate's Black Diamond client cannot POST performancePeriod without first minting the ClientView bearer with GET /session/token, so the one pull made 3 performancePeriod requests plus 1 session-token GET, and 'no other vendor call' read literally has no executable form.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-10 BOUNDS: the vendor call is the one pull and NO other call; vendor_calls equals the performancePeriod requests (AC1) and is at most 5.",
  "world_is": "MEASURED from infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py get_clientview_token() (lines 144-152): the bearer is minted by GET /session/token on the .bd.identity cookie, and the POST needs it. The run made 1 session-token GET and 3 performancePeriod POSTs (0027265115, 0076459710, 0084073310), all HTTP 200, 0 retries, 0 performanceSeries, and no call for the 2 unmapped accounts. BD_LIKEDAY_PULL_R4.json counts vendor_calls = 3 (the requests, as AC1 grades) and records session_token_mints = 1 beside it, so the extra request is on the record. No credential, cookie or token was written or printed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:144-152 get_clientview_token (read-only)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/BD_LIKEDAY_PULL_R4.json: vendor_calls 3, session_token_mints 1, transport_retries 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the L9 reader: a future per-use word should name the session-token GET as part of the pull. Also recorded, no action taken: 0084073310's first segment 2026-03-20..2026-08-04 (94 days, Opal +24.23%, BD +23.97%) precedes the roster trade_start_date 2026-08-05, and BD agrees with the gold over it. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-S22 -- the tie-out's largest disagreement has no stated reason; the income signs differ

```json
{
  "id": "IRPT_DASHBD-S22",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-02T18:45:00Z",
  "one_line": "The round-4 tie-out's largest disagreement (0027265115, 2026-06-25..07-06, Opal +3.4935% against Black Diamond +2.2806%, 1.21 points over 7 like days) carries no stated reason, and its cause is findable: Opal books income +0.4627% on 06-25 alone, while Black Diamond reports the window's income as -2,470.31 on an account that is about 47 pct short. None of the 14 pairs carries a reason field.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's re-derivation (2026-10-02 18:3xZ): served gold opal-data-49financial/irpt/49financial/gold/account_return_daily, 7 of 7 trading days 06-25..07-06 for 0027265115, total_return_daily linked = +3.4935% (equal to the record); income_return 06-25 = 0.004627, other days 0.000001-0.000153; return_basis TWR on 7 of 7",
      "RAW_BD_PERIOD_0027265115.sanitised.json.gz (deliverables/0.9.0_WK_IRPT_DASHBD~1), dateRangePoints[3] 2026-06-25..07-06: timeWeightedReturns.return 0.022805706 (equal to the record), daysHeld 7, income -2,470.31, netAdditions 4,402.22, fees 0.0; the as-of point (2026-10-01) shortAllocation 0.4729",
      "TIEOUT_49F_BLACKDIAMOND_R4.json: 14 pairs, keys account..abs_diff; no reason field on any pair"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-8 ACCEPT: the two returns agree within a tolerance Andrew accepts and every day they disagree carries a stated reason (C-TIEOUT: flow timing, missing price, income date).",
  "world_is": "Agreement is good on most windows (median 0.16 pct) but the disagreeing windows are unexplained, and the largest has an income-sign difference: positive income in Opal where Black Diamond nets income negative, as a short book paying dividends would (inferred: the short allocation was read at 10-01, not in June). If Opal counts dividends received but not dividends paid on shorts, the method overstates income for short-heavy accounts.",
  "notes": "INERT for the served page until the dashboard figure reaches clients through the read route. Owner 2.0.0_SA_COO~P (the tie-out's reasons; the income treatment of short positions in the producer). The tolerance itself is 1.0.0_SA_CTO's to rule (PRD Q2)."
}
```

## IRPT_DASHBD-W1-S12 -- TO-DB-b-11: 885 of the 7,570 population accounts carry no positive value on the newest day, so the producer emits 6,686 rows and the publisher (which publishes the newest gold partition's accounts) would give them no manifest

```json
{
  "id": "IRPT_DASHBD-W1-S12",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T20:10:00Z",
  "one_line": "TO-DB-b-11: the holdings population at date=2026-10-01 is 7,570 accounts, but 885 of them have no positive whole-account value on that day, the producer yields 6,686 rows for it, and reporting-publish takes its account set from the newest GOLD partition, so those 885 accounts (875 NO-PRIOR-HOLDINGS) get no manifest or series; P-1 says every 49 Financial client.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order and the fold-in P-2: every 49 Financial account in the holdings population gets a published manifest and series; the account set is never fewer than the newest reporting partition's.",
  "world_is": "MEASURED 2026-10-02: population 7,570 (holdings_performance_daily date=2026-10-01, 7,570 distinct ids); dim_balance net_mv_plus_cash sums positive for 6,685 of them and not for 885 (0 absent from dim_balance; holdings status NO-PRIOR-HOLDINGS 875, NON-POSITIVE-BASE 6, ALL-HOLDINGS-EXCLUDED 3, OK 1); the producer over all 7,570 yields 6,686 rows on that day (compute is by design: an account with no positive value has no return). The gold account set (this build) is the full population, but a zero-value account has no row, and the publisher reads wanted = newest gold partition's accounts, so a closed or unfunded account that HAS earlier history gets no refreshed series. Whether the page must show those clients is the issuer's and CVO's call.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/P2_SCALE_R5.json population + producer blocks",
      "infra/aws/lambda/investor-reporting/reporting-publish/handler.py _newest_accounts (the publisher's account rule, unchanged by this build)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken. A candidate for the packet: publish the union of every account in any gold partition (history), not only the newest. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S13 -- TO-DB-b-11: the deployed reporting-publish Lambda is timeout 300 s / 1024 MB (the order's limit is 900), and the shard fan-out needs lambda:InvokeFunction on itself, which the role was not shown to hold

```json
{
  "id": "IRPT_DASHBD-W1-S13",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T20:10:00Z",
  "one_line": "TO-DB-b-11: reporting-publish is deployed at timeout 300 s and 1024 MB (reporting-publish/lambda.tf:44-45), not the 900 s of the order and AC1; the one-invoke publish at 7,570 accounts needs 1,582 MB peak and ~450 s, so the build shards it (8 invokes of ~947 accounts, ~67 s and ~392 MB each) and a scheduled fire self-invokes once per shard, which needs lambda:InvokeFunction on the function's own ARN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: 'lambda_timeout_s 900, and how the publisher stays under it'; BOUNDS: no Terraform and no IAM change in this cell.",
  "world_is": "MEASURED: reporting-publish/lambda.tf timeout 300, memory 1024 (held); the live publish fire 2026-10-02 used 241 MB and 14.5 s at 6 accounts; the local whole-population in-memory run peaked at 1,582 MB. The fan-out raises on a refused self-invoke (it never half-lands silently), so a missing permission fails the daily fire LOUDLY, not silently. The shard split is a stable crc32 hash of the account id, so each account is in exactly one shard whatever the population is when the shard runs.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf:44-45 timeout 300, memory_size 1024",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/P2_SCALE_R5.json publisher block; p2_publisher_measure_r5.py output"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the issuer's packet: grant the publish role lambda:InvokeFunction on its own function (or replace the self-invoke with 8 EventBridge targets carrying {shard, shards}); no timeout or memory change is needed at the measured numbers. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S14 -- TO-DB-b-11: the reporting-gold handler's resume rule only extends past the newest landed day, so the backfill of the new accounts into the 562 landed partitions is not an act this function can perform

```json
{
  "id": "IRPT_DASHBD-W1-S14",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T20:10:00Z",
  "one_line": "TO-DB-b-11: after the account-set widening deploys, the daily fire adds the population from the NEXT day only; the 562 landed partitions (2024-07-08..2026-10-01) hold 6 accounts, and handler.run() computes only days after the newest landed one, so history for the other ~7,560 accounts needs a separate rewrite of 562 served partitions (a never-widen act).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: the backfill and the deploy are the issuer's packet; this cell records a plan that respects the Lambda limit.",
  "world_is": "MEASURED: account_return_daily holds 562 partitions of 6 rows each at date<=2026-10-01; reporting-gold/handler.py run() takes days from select_days(newest_landed, today) and refuses when the gold holds no partition; its CLI is --local only. The plan recorded in P2_SCALE_R5.json backfill.plan is a driver composing handler.compute() with the producer's emit_day over the explicit population in 23 chunks of <=25 days, in-region (laptop link measured ~35 KB/s, ~12 h), ~1.1 h upper bound, under a ledger and a sign-off with DELTA=0 on the 6 served accounts.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py run() and select_days (resume rule)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/P2_SCALE_R5.json backfill block"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No handler change made for it (outside the order). Also recorded: the laptop could not run the 561-partition inception scan (single 578 KB GET 2.7-50 s), so the producer's laptop seconds are a scaled measurement; the Lambda numbers are projected from the live fire's CloudWatch REPORT lines. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S15 -- TO-DB-b-12: the directory carries OPAQUE ids (cli_/acc_) while the platinum series are keyed by the custodian number, so the summary joins them through the one normalizer and is keyed by the opaque client id

```json
{
  "id": "IRPT_DASHBD-W1-S15",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T22:45:00Z",
  "one_line": "TO-DB-b-12: the order says `client` is 'its id and its account ids, from the 49 Financial directory'; the directory's account ids are opaque (acc_<24 hex>) and the published series sit under account=<10-digit custodian number>, so the summary cannot be built from the directory and the series alone without minting each published account's opaque id (_ids/ids.py opaque_account, the same join reporting/entry.py raw_account_for makes). The summary therefore carries the directory's opaque ids, its address is client=<cli_ id>, and the custodian number is never written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: build_client_summary(client, accounts); accounts holds each account's built series and manifest; no key-space statement.",
  "world_is": "MEASURED: directory 2026-09-24 (4,620 entries, 4,620 client ids, 7,576 account ids, all opaque); the 6 published raw keys mint to 6 opaque ids and all 6 are in the directory (published_accounts_not_in_directory = 0 in CLIENT_SUMMARY_R5.json). The caller keys `accounts` by the client's account id; the dry run does the mint. The directory pointer's own vintage is 2026-09-24 (latest.json written 2026-09-25).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting/entry.py:188-196 raw_account_for",
      "infra/aws/lambda/investor-reporting/_ids/raw_keys.json 49financial.account",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/client_summary_dryrun_r5.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the issuer's packet: the publisher's deployed path must do the same raw->opaque mint when it writes summaries (publisher.py stays pure and takes the already-joined map). The summary's contract file should name the key space. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S16 -- TO-DB-b-12: a window holding a NOT_MEASURABLE (null-return) day is null with status BREAK, so 5 of the 6 published accounts have a null SI today; the order only said 'null when the series does not span it'

```json
{
  "id": "IRPT_DASHBD-W1-S16",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T22:45:00Z",
  "one_line": "TO-DB-b-12: the order defines null only for a window the series does not span. Five of the six published series carry null-return days after the inception day (3 to 11 each), and a link across one is not a geometric link of the series. The worker's rule: such a window is null with window_status BREAK (never bridged, never zero-filled), and each account carries window_status {MEASURED|NOT_SPANNED|BREAK} per window so a consumer can reject on the reason; the client also lists unpublished_account_ids so a partial client never reads as whole. These three keys are additions to the order's list.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: 'A window is null when the series does not span it, never a partial'; the series contract: a null total_return_daily 'breaks the link with a stated gap'.",
  "world_is": "MEASURED on the 6 published series (.scratch pull 2026-10-02): null-return days after day 0 = 0, 10, 8, 5, 2, 4 for the six accounts; in the dry run, an account whose gap lies inside the window answers BREAK (example in CLIENT_SUMMARY_R5.json shape: SI BREAK, QTD MEASURED). The tests pin: spans -> MEASURED equals the geometric link; not spanned -> NOT_SPANNED; a gap -> BREAK in every window that contains it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting-publish/publisher.py window_return",
      "infra/aws/lambda/investor-reporting/reporting-publish/tests/test_client_summary.py",
      "org/standards/IRPT_DASHBD_SERIES_CONTRACT.json (null rule)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "If the issuer wants a window linked across a stated gap instead (a figure with a gap count), that is a rule change here and in the page. Owner: 2.0.0_SA_COO~P."
}
```

## IRPT_DASHBD-W1-S17 -- TO-DB-b-13: the S22 income fix admits the debit leg of QDV, NDV and PDV only; the plain DIV key is left out because one of its 39 debit rows in 2026 is a long fund with zero shares, and the column that would separate them is not declared

```json
{
  "id": "IRPT_DASHBD-W1-S17",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T23:20:00Z",
  "one_line": "TO-DB-b-13: the S22 income fix admits the debit leg of QDV, NDV and PDV only; the plain DIV key is left out because one of its 39 debit rows in 2026 is a long fund with zero shares, and the column that would separate them is not declared",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: 'Fix the treatment by the code, not by account. Long positions' income does not move'; refusal clause: a fix that moves any account without a short position is a defect.",
  "world_is": "MEASURED over the 188 fact_trn partitions 2026-01-02..2026-10-01 (SHORT_INCOME_INVARIANCE_R6.json and a scratch census): debit rows on FC/DV by key: QDV 592 and NDV 22, every one with a negative dividend_interest_share_quantity (a short position's dividend); DIV 38 with negative shares and 1 with zero shares (0.37, a long fund, account-day with no short market value); adjustment keys (DIVAJ, DFRAJ, NDVAJ, NDRAJ ...) are debits too, 5,000+ rows, which REVERSE an earlier credit and stay out. Admitting DIV by key alone would move that one no-short account-day by -0.37, which the refusal clause forbids; admitting it by share quantity needs dividend_interest_share_quantity declared as a read column, and sources.json is outside this order's paths. Short-account DIV debits (38 rows, 822.51 absolute in 2026) therefore stay unbooked as income.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/SHORT_INCOME_INVARIANCE_R6.json",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py SHORT_PAID_DIVIDEND_KEYS",
      "data/assets/scripts/gold/irpt_reporting/sources.json (transaction_columns derives the read set from this file)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P. To admit DIV: declare the share-quantity column in sources.json and require it negative on the debit leg. Income is not an input of total_return_daily, so no served return moves either way."
}
```

## IRPT_DASHBD-W1-S18 -- TO-DB-b-13: Opal's account value (net_mv_plus_cash) leaves out the Schwab margin_balance that Black Diamond's value includes; with it added the three pairs beyond 0.35 pp fall to 0.0044, 0.0264 and 0.0493 pp. A ruling on the value basis is owed

```json
{
  "id": "IRPT_DASHBD-W1-S18",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T23:20:00Z",
  "one_line": "TO-DB-b-13: Opal's account value (net_mv_plus_cash) leaves out the Schwab margin_balance that Black Diamond's value includes; with it added the three pairs beyond 0.35 pp fall to 0.0044, 0.0264 and 0.0493 pp. A ruling on the value basis is owed",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO",
  "spec_asserts": "C-VALUE (ratified): V_t is the custodian's own whole-account value, declared as dim_balance.net_mv_plus_cash; the order expected each pair beyond 0.35 pp to carry a stated reason and a code defect among them to be fixed and re-measured.",
  "world_is": "MEASURED at all 6 window endpoints of the 3 pairs (DECOMPOSE_THREE_PAIRS_R6.json): Black Diamond's beginning and ending value = Opal's net_mv_plus_cash + dim_balance.margin_balance + Black Diamond's own accrual, difference 0.00 at 6 of 6. Schwab's own equity field (eqty_excl_option / eqty_incl_option) = net_mv_positions + margin_balance, so for a margin account net_mv_plus_cash is not the equity: e.g. 0084073310 on 2026-10-01 net_mv_plus_cash 1,009,937.16, margin_balance 5,579.04, equity 1,015,516.20 = Black Diamond's ending value to the cent. Replaying the windows with V + margin_balance (counterfactual, written nowhere): 0084073310 0.7078 -> 0.0264 pp; 0027265115 04-09..04-30 0.4555 -> 0.0493 pp; 0027265115 06-25..07-06 1.2130 -> 0.4738 pp (and -> 0.0044 pp with row S20's flow). The declaration's identity check (net_mv_plus_cash - net_mv_positions = money_mkt_funds + net_credit_debit, 92,407 of 92,407) tests the column against itself and cannot see margin_balance. The fix is a change of the ratified value basis in sources.json (outside this order's paths) and moves every margin account's served series, so it is not made here. Pairs 2 and 3 are recorded as defect=false (a basis difference against the ratified text, ruling owed), a classification the CTO may overturn.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/DECOMPOSE_THREE_PAIRS_R6.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/TIEOUT_49F_BLACKDIAMOND_R6.json",
      "data/assets/scripts/gold/irpt_reporting/sources.json account_value_column"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED: the reporting gold is scheduled (DB-b-7) and the dashboard figure reaches clients through the read route, so every margin account's return is off Schwab's equity by up to the margin_balance share of value (0.55 pct of value on these accounts) until ruled. Owner of the ruling: 1.0.0_SA_CTO; owner of the packet: 2.0.0_SA_COO~P (a value-basis change is a new method_version and a recomputation, per the method-row contract). FWD-8 should not be graded REALIZED on defect=false alone before this is answered."
}
```

## IRPT_DASHBD-W1-S19 -- TO-DB-b-13: the method row now writes tieout_tolerance and tieout_tolerance_ruling, two columns the dim_return_method contract (0.2.0) does not declare, so its schema_hash is stale for the next write

```json
{
  "id": "IRPT_DASHBD-W1-S19",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T23:20:00Z",
  "one_line": "TO-DB-b-13: the method row now writes tieout_tolerance and tieout_tolerance_ruling, two columns the dim_return_method contract (0.2.0) does not declare, so its schema_hash is stale for the next write",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: emit_method_row writes tieout_tolerance = 0.0035 and tieout_tolerance_ruling = '1.0.0_SA_CTO RULINGS batch 181'; tieout_tolerance_proposed is kept (null) unless the row's contract says otherwise.",
  "world_is": "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json declares 18 columns and neither new one; its landed row carries tieout_tolerance_proposed = 0.037 (written by DB-b-3 with --tieout), so a re-run without --tieout would write null there, a producer default the contract does not call for. Adding two columns changes the table's parquet schema and therefore its schema_hash; the contract file is outside this order's paths. The handler does not call emit_method_row (reporting-gold/handler.py), so nothing is written until the issuer's packet runs the producer with --method-row-only --tieout 0.037.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json columns, landed_row",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py emit_method_row",
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py (docstring: omits the emit_method_row call)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P: contract bump (0.3.0, new schema_hash, rule24 record for the two columns) lands with the method-row packet, with --tieout 0.037 so the landed proposal is kept."
}
```

## IRPT_DASHBD-W1-S20 -- TO-DB-b-13: Schwab's INTRA/FC/IN 'MARGIN INT ADJ' credit (4,429.53 on 2026-06-25) is return in Opal and a net addition in Black Diamond, and margin interest charged (INTR/FC/IN debit, 3,106.83 on 06-29) is in neither Opal's income term nor its flow

```json
{
  "id": "IRPT_DASHBD-W1-S20",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~1",
  "surfaced_at": "2026-10-02T23:20:00Z",
  "one_line": "TO-DB-b-13: Schwab's INTRA/FC/IN 'MARGIN INT ADJ' credit (4,429.53 on 2026-06-25) is return in Opal and a net addition in Black Diamond, and margin interest charged (INTR/FC/IN debit, 3,106.83 on 06-29) is in neither Opal's income term nor its flow",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Income is recognised on cash receipt from the CRO's classification table; the pair's reason must be measured.",
  "world_is": "MEASURED for 0027265115: fact_trn 2026-06-25 carries INTRA/FC/IN CREDIT 4,429.53 'MARGIN INT ADJ', classed INTERNAL / 'Dividends and Interest' by SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json, so it is not an external flow and stays inside the return; Black Diamond's window point 06-25..07-06 shows netAdditions 4,402.22. Treating the 4,429.53 as a flow on that day moves the pair from 0.4738 to 0.0044 pp (counterfactual, after the margin_balance addition of row S18). Separately, INTR/FC/IN DEBIT 3,106.83 on 06-29 ('INTEREST 05/28 THRU 06/28') is a debit outside the fixed income term by design (only QDV/NDV/PDV debits are admitted), so Opal's signed window income is 4,312.61 against Black Diamond's -2,470.31; the remainder is not measured here (Black Diamond's accrual source is not in the stored response). Whether a margin-interest adjustment is return or a contribution is not decidable from the Schwab bytes alone.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Schwab silver fact_trn date=2026-06-25 and date=2026-06-29, account 0027265115",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json (INTRA, INTR on FC/IN)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/RAW_BD_PERIOD_0027265115.sanitised.json.gz dateRangePoints[3]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P (the classification table is 4.0.0_SA_CRO's file, not edited). One day, one account in the sample."
}
```

## IRPT_DASHBD-W2-S1 -- TO-DB-b-15: under the equity basis 4 of 14 pairs stay beyond 0.35 pp, and 2 of them (0076459710 08-11 and 08-21) are NEW or WORSE than round 4 -- Black Diamond's own accrual and its fee treatment, both outside Opal's figure by ruling

```json
{
  "id": "IRPT_DASHBD-W2-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~2",
  "surfaced_at": "2026-10-03T01:40Z",
  "one_line": "TO-DB-b-15: under the equity basis 4 of 14 pairs stay beyond 0.35 pp, and 2 of them (0076459710 08-11 and 08-21) are NEW or WORSE than round 4 -- Black Diamond's own accrual and its fee treatment, both outside Opal's figure by ruling",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order expects the equity basis to bring the pairs to the tolerance, with Black Diamond's accrual stated per pair (batch 193); a pair beyond 0.35 pp carries a measured reason.",
  "world_is": "MEASURED over all 14 pairs, method_version 2: 10 within, 4 beyond. Beyond: 0027265115 06-25..07-06 0.4738 pp (S22; the 4,429.53 MARGIN INT ADJ credit, batch 195 RETURN; 0.0044 pp if that credit were a flow); 0076459710 08-11..08-19 0.4998 pp (round 4: 0.3307) and 0076459710 08-21..09-09 0.4608 pp (round 4: 0.0076): Black Diamond's value = equity + its accrual to the cent at 28 of 28 endpoints, its accrual moved +6,022.40 then -5,766.11, which alone is 0.4999 pp and 0.4501 pp of its beginning value, leaving 0.0001 pp and 0.0107 pp; the two windows mirror each other (receipt booked in the second); 0084073310 03-20..08-04 0.4045 pp (round 4: 0.2606): Black Diamond's return equals ending/beginning value - 1 (0.239661) so its 3,020.96 fee stays inside its return (0.3961 pp of beginning value) while Opal is gross of fee. Equity moved the largest round-4 pairs to 0.0264 pp (0084073310 08-21) and 0.0493 pp (0027265115 04-09), max abs diff 1.2130 -> 0.4998 pp. Opal's window fee flow for 0084073310 was inferred from the return, not read as a flow.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/TIEOUT_49F_BLACKDIAMOND_R8.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/OPAL_REMEASURE_FOURTEEN_R8.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/RAW_BD_PERIOD_0076459710.sanitised.json.gz dateRangePoints[1],[2]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 1.0.0_SA_CTO at the round-8 analysis (whether the tolerance is to be read on an accrual-adjusted or fee-adjusted Black Diamond figure, or the 0.35 pp bar stands with these reasons). Nothing applied to the producer for this; the ruling stated Black Diamond's accrual stays outside Opal's figure and Opal is gross of fee by C-FEERAIL."
}
```

## IRPT_DASHBD-W2-S2 -- TO-DB-b-15: the one-rule proof needed a definition of 'margin_balance 0 that day' (the daily row also reads the prior day), and a null margin_balance makes the value ABSENT; 0 nulls exist in 3,230,967 history rows

```json
{
  "id": "IRPT_DASHBD-W2-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~2",
  "surfaced_at": "2026-10-03T01:40Z",
  "one_line": "TO-DB-b-15: the one-rule proof needed a definition of 'margin_balance 0 that day' (the daily row also reads the prior day), and a null margin_balance makes the value ABSENT; 0 nulls exist in 3,230,967 history rows",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Every account whose margin_balance is 0 that day computes identical rows apart from method_version; a null margin_balance is never silently zero, counted, and a row is filed if any exist.",
  "world_is": "MEASURED on 2026-10-01 over the 6,861 rows both versions emit (base-commit producer and the worktree producer on the same cached balance bytes): 6,788 accounts have margin_balance exactly 0 on 10-01 AND on the prior trading day 09-30 -- 0 of 6,788 rows changed apart from method_version. 28 accounts have margin 0 on 10-01 but nonzero on 09-30; all 28 rows change, correctly, because the daily return's base V(t-1) is the prior day's equity. 45 rows with nonzero margin all change. The record's zero_margin_accounts is the 6,788 (zero on both inputs of the row). Null margin_balance: 0 rows on 2026-10-01 and 0 of 3,230,967 rows over 563 partitions (2024-07-08..2026-10-01); null net_mv_plus_cash also 0. The producer treats a null component as an ABSENT value (account-day left out of the value map, printed, next day's base absent -> NOT_MEASURABLE), never zero; no day is affected today. Row set: 2 accounts emit a row only under equity (inception moves earlier by a positive equity), 0 only under net_mv_plus_cash; positive population 6,685 -> 6,686 (0 positive-to-nonpositive, 1 nonpositive-to-positive); guard_state over the 6,861 common rows: GRADED_AGREED 6,635 -> 6,639, GRADED_DISAGREED 13 -> 9, GUARD_NOT_REACHED 184 -> 184, NOT_GRADED_OUTSIDE_DOMAIN 29 -> 29.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/POPULATION_EQUITY_R8.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/population_equity_r8.py",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2/scan_balance_history_r8.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P (reads the definition at the P-2 packet). The 'before' producer is git show 1ce7e8e9f0 of account_return_daily.py and sources.json, run unmodified apart from its path anchor."
}
```

## IRPT_DASHBD-W2-S3 -- TO-DB-b-15: emit_method_row writes two more columns (value_basis, value_basis_ruling) that the dim_return_method contract does not yet carry, the same shape as row W1-S19

```json
{
  "id": "IRPT_DASHBD-W2-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~2",
  "surfaced_at": "2026-10-03T01:40Z",
  "one_line": "TO-DB-b-15: emit_method_row writes two more columns (value_basis, value_basis_ruling) that the dim_return_method contract does not yet carry, the same shape as row W1-S19",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "emit_method_row records the new version and its basis, citing 1.0.0_SA_CTO RULINGS batch 193; the contract file is outside this order's paths.",
  "world_is": "MEASURED: the row dict now carries value_basis ('EQUITY = net_mv_plus_cash + margin_balance') and value_basis_ruling ('1.0.0_SA_CTO RULINGS batch 193') beside the tolerance fields; org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json lists neither column, so a landed method_version=2 row would add two columns to the table's parquet schema and change its schema_hash. The reporting gold handler does not call emit_method_row, so nothing is written until the issuer's method-row packet. Also for that packet: the publisher refuses a file of mixed method_version (publisher.py:173), so every landed gold day must be rewritten under version 2 before it is served.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py emit_method_row",
      "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json columns"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P: contract bump lands with the method-row packet, in the same commit as the W1-S19 columns."
}
```

## IRPT_DASHBD-W3-S1 -- TO-DB-b-16: DB9-1-AC2 cannot pass - the existing test_one_route_and_function_name asserts len(entry.ROUTES) == 1, and the order's own second route (DB9-1-AC3) makes it fail; the test file is outside the order's paths

```json
{
  "id": "IRPT_DASHBD-W3-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~3",
  "surfaced_at": "2026-10-02T23:59:00Z",
  "one_line": "TO-DB-b-16: DB9-1-AC2 cannot pass - the existing test_one_route_and_function_name asserts len(entry.ROUTES) == 1, and the order's own second route (DB9-1-AC3) makes it fail; the test file is outside the order's paths",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "The order says the account route's behaviour is unchanged and 'an existing test that moves is a defect', and DB9-1-AC2 wants the whole reporting/tests suite at least 14 passed and 0 failed (11 pass at the base).",
  "world_is": "MEASURED at 713110dbeb plus this worker's edits: reporting/tests/test_reporting_entry.py::test_one_route_and_function_name asserts `len(entry.ROUTES) == 1` (line 74). With the summary route added to ROUTES (which DB9-1-AC3 requires, exactly one summary key plus the account key) that assertion fails with `assert 2 == 1`; the other 10 tests of that file and the 10 new summary tests pass (pytest: 1 failed, 20 passed). The account route's behaviour and the other 10 existing tests are unchanged. test_reporting_entry.py is not in the order's <paths>, so this worker did not edit it; DB9-1-AC2's checker reads '1 failed' and prints FAIL. The needed edit is one line in that file (len(entry.ROUTES) == 2, or assert the account key maps to OPERATION and the summary key to SUMMARY_OPERATION) and a grant for the path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_entry.py:74 (test_one_route_and_function_name)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_1_ac2_read_route_summary_tests.py (rejects any '<n> failed')",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r9/p9_1_ac3_summary_route_declared.py (requires exactly one summary key in ROUTES)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P (the issuer amends its own order's paths): add test_reporting_entry.py to the grant and recut or amend DB-b-16, or edit that one assertion at the drain. DB9-1-AC1 and DB9-1-AC3 PASS; DB9-1-AC2 is FAIL by this row alone."
}
```

## IRPT_DASHBD-W4-S1 -- TO-DB-b-17: the deployed publisher cannot run the summaries pass until its zip carries the opaque-id normalizer and the firm registry, and its environment names the directory bucket; neither is in this cell's paths

```json
{
  "id": "IRPT_DASHBD-W4-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~4",
  "surfaced_at": "2026-10-03T00:30:00Z",
  "one_line": "TO-DB-b-17: the summaries pass needs _ids/ids.py (+ raw_keys.json, data/firm_registry.json) and the directory bucket at run time, and the irpt-reporting-publish-lambda package map and lambda.tf carry none of them, so the pass refuses by name on the first deployed fire until the issuer's packet adds them",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: the pass reads the directory and mints opaque cli_/acc_ ids 'through _ids as reporting/entry.py does'; the order's paths are handler.py, publisher.py, the new test, and iam.tf; the trigger and deploy are the issuer's P-2 packet.",
  "world_is": "MEASURED at 713110dbeb: infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-publish-lambda lists handler.py, publisher.py, lib/opal_naming.py, org/standards/NAMING_SCHEMA.json, infra/logic/registry/*.json and sources.json, and NO ids.py, raw_keys.json, data/custodian_key_seam.json or firm_registry.json (the reporting-read-lambda entry stages all four). infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf sets no environment (IRPT_DIRECTORY_BUCKET_MAP, which _authz/loaders.py reads, is unset). handler.py therefore loads ids.py from the zip root or the repo's _ids package (the repo path is what the tests and the local dry run use), reads the bucket from IRPT_DIRECTORY_BUCKET_MAP or the registry beside ids.py, and otherwise raises SystemExit REFUSED naming the missing piece. The scheduled series fire never reaches this code (the module adds only stdlib imports at load; _ids_module is called only inside the summaries pass), so the 08:15 ET fire is unchanged. Local dry run (reads only) over the live directory and the 6 published accounts: 4,620 clients, 6 summaries built, 4,614 without a published account, 0 refused.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json irpt-reporting-publish-lambda files / staged_from @713110dbeb",
      "infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf (module irpt_reporting_publish: no environment)",
      "infra/aws/lambda/investor-reporting/reporting-publish/handler.py _ids_module, directory_bucket",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~4/READ_COST_R9.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P (P-2 packet): stage ids.py, raw_keys.json, data/custodian_key_seam.json and data/firm_registry.json as packaged_as paths in the publish entry (ids.py at the zip root, as the read entry does), or set IRPT_DIRECTORY_BUCKET_MAP in lambda.tf; the two files this cell may not edit. Also ids.py reads IRPT_FIRM_REGISTRY or a firm_registry.json beside it."
}
```

## IRPT_DASHBD-W4-S2 -- TO-DB-b-17: the deployed publish function's timeout is 300 s, not the 900 s the order budgets, and the per-account read cost is a laptop measurement, so the summaries pass is sharded by client to fit 300 s

```json
{
  "id": "IRPT_DASHBD-W4-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~4",
  "surfaced_at": "2026-10-03T00:30:00Z",
  "one_line": "TO-DB-b-17: the order budgets the 900 s Lambda limit; reporting-publish/lambda.tf sets timeout = 300, and no in-region read cost could be measured (invoke is out of bounds), so the projection rests on laptop latency and the shard size is chosen to fit 300 s",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order: 'It must fit the 900 s Lambda limit at 4,620 clients and 7,570 accounts. Measure the per-account read cost with S3 READS on what is published today, and state the projection with its basis. If it does not fit, shard BY CLIENT.'",
  "world_is": "MEASURED 2026-10-03 from the laptop (S3 reads only), 6 published accounts: 1.126 s per account sequentially (two GETs, ~0.56 s each), 0.234 s per account through a 16-worker pool (24 account reads in 5.62 s); series 6,255 gzip bytes and 187 days on average; directory 6,526,009 bytes in 21.3 s, parse 0.02 s; one delimiter listing 1.09 s. A re-run of the same script (READ_COST_R9.json holds this one, the first run's values are in this row) read 0.257 s per account sequentially, 0.190 s through 16 workers, the directory in 34.8 s, the listing in 0.78 s: latency from the laptop varies run to run, and the projection below takes the slower per-account figure of the two runs. (1 page per 1,000 prefixes, so 8 pages at 7,570 accounts). PROJECTION at laptop latency, the pessimistic bound: 7,570 accounts x 0.234 s = ~1,770 s in ONE invoke, which does not fit 900 s (nor the deployed 300 s); sharded by client at SUMMARY_SHARD_CLIENTS = 300 it is 16 shards of ~470 accounts, ~110 s of reads plus ~30 s of directory and listing, ~140 s per shard, which fits 300 s with margin. In-region latency is not measured here and is expected lower. The live local dry run built 6 summaries in 1.9 s.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~4/READ_COST_R9.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~4/measure_read_cost.py",
      "infra/aws/terraform/investor-reporting/reporting-publish/lambda.tf timeout = 300, memory_size = 1024"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P: the first deployed summaries fire's CloudWatch REPORT line is the in-region measurement; the fan-out reuses the function's own-invoke grant. The projection is a scaled laptop figure, not a Lambda measurement."
}
```


## IRPT_DASHBD-W5-S1 -- the read entry's staged_from_note says 'one pin' after the re-pin

```json
{
  "id": "IRPT_DASHBD-W5-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~5",
  "surfaced_at": "2026-10-03T02:35:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-DB-b-18: the read entry's _staged_from_note says its shared boundary members sit at ONE pin; re-pinning the members rounds 6-9 changed (served.py, enforce.py, maintained_sources.py, NAMING_SCHEMA.json, sources.json) leaves that note stale, and the order grants the pins but not the note",
  "spec_asserts": "Order item 2: re-pin every staged_from member whose blob changed, members that did not change keep their pins. lambda-source-map.json irpt-reporting-read-lambda._staged_from_note: 'The shared boundary members are the Holdings function's own closure ... at one pin'.",
  "world_is": "After the re-pin the read entry's 28 staged members sit at 5 pins: 5f582dca96 (23 members), acce364286 (served.py), 7605bbf5ab (enforce.py), bb255c4cb2 (maintained_sources.py), aa2b5a42ff (NAMING_SCHEMA.json) and 6ce75d3385 (sources.json). The note was left byte for byte as found. DB10-1-AC2 PASS grades pins and blobs, not the note, so the stale sentence does not fail anything; a reader taking 'one pin' at its word would assume the Holdings closure is byte-identical to the Holdings function's own, which it no longer is for three members.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json irpt-reporting-read-lambda staged_from at this order's commit",
      "git log -1 --format=%H -- <member> for each of the five moved members"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P: reword the note when the read function is next rebuilt, or accept the divergence knowingly; served.py and enforce.py changed after the Holdings pin, so whether the read artifact should track the Holdings closure or its own HEAD is the issuer's call."
}
```


## IRPT_DASHBD-W5-S2 -- the 0.3.0 schema_hash needs --tieout at the method-row write

```json
{
  "id": "IRPT_DASHBD-W5-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~5",
  "surfaced_at": "2026-10-03T02:35:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-DB-b-18: the 0.3.0 schema_hash types tieout_tolerance_proposed as double, which holds only if the P-2 packet's method-row write passes --tieout; without it the producer writes None, pyarrow types the column null, and the served hash differs from the contract's",
  "spec_asserts": "emit_method_row(..., tieout=None) puts the tieout argument into the row as tieout_tolerance_proposed; the 0.2.0 contract declares that column double, nullable, 'a future method_version is emitted before its tie-out has run'.",
  "world_is": "The row is built by pa.Table.from_pydict({k: [v]}), so a Python float is double and None is null. The 0.3.0 hash 73e80ef7920f59134eda5ab06dfea766de295bd71e71b398023b52ae8acbe919 is over the 22 'name:type' lines with double for that column, as the landed version-1 row (0.037) carried it. A method-row-only write with no --tieout would land a null-typed column and a different hash; the contract provenance states the dependency and says the hash is re-read from the served artifact at the packet's write. The producer was not changed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py emit_method_row, lines 1729-1775 at 1067171ecd",
      "org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json schema_hash_provenance at 0.3.0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~P: pass --tieout on the packet's --method-row-only write, or ask the producer's owner for a typed schema on that column; compare the served schema_hash to the contract's after the write."
}
```

## IRPT_DASHBD-S23 -- routes.json omits both live reporting routes

```json
{
  "id": "IRPT_DASHBD-S23",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-03T19:25:00Z",
  "one_line": "docs/contracts/investor-reporting/v1/routes.json declares 19 routes and omits both live reporting routes, GET .../reporting/{account_id}/{which} and GET .../reporting/client/{client_id}/summary. Both are declared in reporting/entry.py:92,373, live on the API gateway behind irpt-49f-reporting-read-lambda, and called by PROD portal v2.1.197. The file's own note says every route the product needs is covered.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's grade of the B2 promote 2026-10-03 ~18:5xZ-19:2xZ: routes.json at CLOUD HEAD, 19 entries, neither reporting route; entry.py ROUTES; API gateway routes and the read Lambda's CodeSha256 read via boto3; PROD bundle strings carry the summary route"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "routes.json is the published inventory of the routes the product calls (its own note).",
  "world_is": "The contract inventory lags the served surface by two routes. A census or gate reading routes.json, such as the _authz unguarded census, cannot see them.",
  "notes": "INERT (the routes are guarded in code). Owner 2.0.0_SA_COO~P (the reporting routes' issuer; the file sits in ~Y's lease surface): add both routes to routes.json with their guard, and re-run any census that reads it."
}
```

## IRPT_DASHBD-S24 -- 557862f1: the pin cannot see the skip direction; a failed PATH B manifest can leave Loading

```json
{
  "id": "IRPT_DASHBD-S24",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-03T20:09:00Z",
  "one_line": "557862f1 (the Performance tab skips the PATH A read when PATH B serves the account) has a pin that cannot see the skip's direction. With `!pathBServes` at ReportingTab.tsx:745, or both skips inverted, the pin and the 44 ReportingTab files give the same 106/1/1. By reading: an account the client summary lists, whose own manifest read fails, sends neither request and stays on Loading; Refresh skips again.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's portal grade 2026-10-03 ~19:5xZ-20:1xZ (scratch worktree of origin/DEV, removed after): pin 1/1; NEG fails; MUT `!pathBServes` at :745 passes; both-inverted 106 pass / 1 fail (iv-e-69, pre-existing) / 1 skip, the same as head",
      "ReportingTab.tsx:490-497, :692, :745 at 557862f1 (the stuck-on-Loading path is read, not run)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A FAST pin discriminates its claim (rows S54, S55); a read that is skipped has a way back when the read it defers to fails.",
  "world_is": "Inverting the skip would stop PATH A for Inflection and Cottonwood with every test green. The Loading hang is inferred from the code.",
  "notes": "INERT (DEV only; not on PROD 98a98e70). Owner 2.0.0_SA_COO~D: one assertion through the component that a PATH A account still requests PATH A and a PATH B account does not; and fall back to PATH A (or show ERROR) when the PATH B manifest read fails."
}
```

## IRPT_DASHBD-S25 -- the PATH A skip reads the account's own answer only; pinned through the component (disarms S24)

```json
{
  "id": "IRPT_DASHBD-S25",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D",
  "surfaced_at": "2026-10-03T20:38:00Z",
  "one_line": "The Performance tab's own PATH A read now skips only on the account's OWN served PATH B answer, and a pin runs the real report effect in both directions plus the S24 case (portal f2d2f17c).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal f2d2f17c (origin DEV, push output 49d0a98a..f2d2f17c): ReportingTab's report effect calls pathBServes(focusedAccountId, dashboards, null) -- its own dashboard only; the picker keeps the summary (it reads its line from it)",
      "path-a-skip-component.test.tsx runs the real report effect (useState slots 5/7/8 seeded behind initial-value guards; the effect run once after the render): nothing known -> PATH A asked; own dashboard served -> not asked; summary lists it but own read absent (S24) -> asked; fixture plane -> asked",
      "mutants, applied and restored: inverted (!pathBServes) fails (a)(b)(c); the pre-S24 summary skip fails (c); no skip fails (b)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarms IRPT_DASHBD-S24: the pin now sees the skip's direction through the component, and an account whose own PATH B read failed asks PATH A (no Loading hang), measured by the mutants the row named.",
  "spec_asserts": "Row S24: a FAST pin discriminates its claim; a skipped read has a way back when the read it defers to fails.",
  "world_is": "Holds at DEV f2d2f17c. The first-load race measured at 19:59:41Z stands: both PATH A GETs leave before the PATH B manifest answers, so the skip saves requests only once the answer is in hand.",
  "notes": "DEV only; not on PROD 98a98e70."
}
```

## IRPT_DASHBD-W7-S1 -- the shape ruling and the pull record are untracked in the base checkout, absent from the worker worktree


```json
{
  "id": "IRPT_DASHBD-W7-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~7",
  "surfaced_at": "2026-10-04T23:59:00Z",
  "one_line": "The DB-b-20 folder's E3_SHAPE_RULING.json and BD_POPULATION_PULL_E3.json are untracked in the base checkout and absent from a worker worktree, so `run --go` cannot be exercised there; the ruling's bearer line ('one, minted once') is superseded by batch 248.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-21 worker face: `run` refuses unless the DB-b-20 folder's E3_SHAPE_RULING.json exists and reads its pace_rps.",
  "world_is": "In worktree wk-irpt-dashbd-7 (base b77b84cbb4) the folder deliverables/0.9.0_WK_IRPT_DASHBD~6/ holds the plan and script but not E3_SHAPE_RULING.json or BD_POPULATION_PULL_E3.json; both exist only in the base checkout ajb_workspace (untracked). The script reads the ruling from that sibling folder at run time, so the issuer runs it from the checkout that holds the file; the tests stub the ruling. The ruling text still says bearer 'one, minted once'; the completion script re-mints every 10 calls per batch 248.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls of the worktree folder deliverables/0.9.0_WK_IRPT_DASHBD~6 at b77b84cbb4: no E3_SHAPE_RULING.json, no BD_POPULATION_PULL_E3.json",
      "ls of C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6: both present"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W9-S1 -- Declaring the two reporting routes as DECLARED in routes.json passes AC1 but reds 5 tests the grant cannot touch: the ce


```json
{
  "id": "IRPT_DASHBD-W9-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~9",
  "surfaced_at": "2026-10-05T08:01:41Z",
  "one_line": "Declaring the two reporting routes as DECLARED in routes.json passes AC1 but reds 5 tests the grant cannot touch: the census's literal IN_LANE_FUNCTIONS (2) and the response-contract rule of test_seam_paired (3); AC2 FAILS.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P",
  "spec_asserts": "TO-DB-b-23: adding two route objects and updating _denominator leaves test_unguarded_census.py at 0 failed (DB15-1-AC2, base PASS); the census reading an unguarded route would be the finding.",
  "world_is": "Both routes read as GUARDED (census prints 'WHOLE FILE: OK: every route is guarded', irpt-49f-reporting-read-lambda guarded, mark True). The failures are of the test's own literals: (1) test_zero_of_n_over_the_routes_this_order_may_open asserts out_of_lane == {} but the frozenset IN_LANE_FUNCTIONS (test_unguarded_census.py:60-72) does not name irpt-49f-reporting-read-lambda, so 2 routes are out of lane; (2) test_the_whole_file_census_is_zero asserts set(functions) == set(IN_LANE_FUNCTIONS), and irpt-49f-reporting-read-lambda is extra. Result '2 failed, 7 passed'. Separately _contracts/tests/test_seam_paired.py (outside the grant) fails 3 of 65: test_every_declared_route_has_a_response_contract_whose_refs_resolve asserts a response schema for every DECLARED route's operation (reporting-read has none), and the known-good/known-bad control raises TypeError for reporting-read and reporting-summary-read. The routes carry response_schema null + a reason because the live success body is a raw object, not an envelope; making these green needs either response schemas under docs/contracts/investor-reporting/v1/responses/ (outside the grant) or an edit to the census literal set (refusal clause: not done). Census and seam test were NOT edited. The routes.json change is committed as ordered; the order is left open.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python p15_cells.py . DB15-1-AC2 -> 'FAIL: census: 2 failed, 7 passed in 2.31s'; pytest _authz/tests/test_unguarded_census.py output: 'OUT OF LANE, named and not counted: GET .../reporting/{account_id}/{which} -- irpt-49f-reporting-read-lambda (carries the guard mark: True)'",
      "pytest -q _contracts/tests/test_seam_paired.py in infra/aws/lambda/investor-reporting -> '3 failed, 62 passed' (AssertionError: reporting-read at :522; TypeError at :775)",
      "pytest _authz/tests/test_guarded_entries.py 32 passed; test_selection_contract 2, test_upload_contract 8, test_owned_request_contracts 3 all passed with the change"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W9-S2 -- routes.json is the ONE CARRIER the api Terraform root reads; two DECLARED rows with a handler outside route_functions wo


```json
{
  "id": "IRPT_DASHBD-W9-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~9",
  "surfaced_at": "2026-10-05T08:01:41Z",
  "one_line": "routes.json is the ONE CARRIER the api Terraform root reads; two DECLARED rows with a handler outside route_functions would break its next plan, and the reporting-read root already declares the same two route_keys.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P",
  "spec_asserts": "routes.json _carrier: infra/aws/terraform/investor-reporting/api/routes.tf derives aws_apigatewayv2_route resources from every status DECLARED row via function_key_by_name[r.handler]; TO-DB-b-23 premise: the change is 'docs and contract inventory only'.",
  "world_is": "api/routes.tf:41-44 maps every DECLARED row through local.function_key_by_name[r.handler]; route_functions (api/integrations.tf:25-35) holds 7 functions and not irpt-49f-reporting-read-lambda, so the lookup has no key (inferred from reading, no plan run: no AWS). Were it keyed, the same route_keys are already created by aws_apigatewayv2_route.irpt_reporting_read and .irpt_reporting_read_summary in reporting-read/api.tf:24,34, a duplicate. The next api-root plan after this change merges therefore needs either route_functions/a filter in api/routes.tf (outside the grant) or a status the api root skips. The handler name irpt-49f-reporting-read-lambda is the order's, not the Terraform builder name.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/api/routes.tf lines 34-44 and integrations.tf lines 25-35 at 9e1d65bc19",
      "infra/aws/terraform/investor-reporting/reporting-read/api.tf lines 24-36 at 9e1d65bc19"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W9-S3 -- Amendment 1's ROUTED_ELSEWHERE rows leave two out-of-grant contract tests red on no_handler_at_head == total - declared


```json
{
  "id": "IRPT_DASHBD-W9-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~9",
  "surfaced_at": "2026-10-05T08:40:00Z",
  "one_line": "Amendment 1's ROUTED_ELSEWHERE rows leave two out-of-grant contract tests red: both assert _denominator.no_handler_at_head == total - declared, which counts every non-DECLARED row as handler-less.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P",
  "spec_asserts": "Amendment 1: the two reporting rows take status ROUTED_ELSEWHERE and _denominator states routed-here 19 + routed-elsewhere 2 = 21; the order's refusal clause says a test outside the grant is not edited but filed.",
  "world_is": "infra/aws/lambda/investor-reporting/_contracts/test_owned_request_contracts.py:62 and _contracts/test_upload_contract.py:65 assert contract['_denominator']['no_handler_at_head'] == len(rows) - len(declared). With 21 rows, 19 DECLARED and 2 ROUTED_ELSEWHERE that right side is 2, while the two rows HAVE a handler and the file states no_handler_at_head 0 (setting it to 2 would be false). Both tests fail 'assert 0 == (21 - 19)'; they passed with the rows DECLARED. The fix is an edit to those two assertions (subtract ROUTED_ELSEWHERE rows) or a ruling that no_handler_at_head counts them; neither is in the grant. test_seam_paired.py passes (63 passed) and the census passes (9 passed), so DB15-1-AC1/AC2/AC3 and DB-GUARD are unaffected. Separately, running _authz and _contracts in ONE pytest process fails test_seam_paired[performance-report] on ImportError 'LiveTransport' from 'transport' (a module-name collision between the two suites' sys.path entries); each suite alone is clean of it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pytest -q _contracts in infra/aws/lambda/investor-reporting -> '2 failed, 183 passed' (test_public_routes_are_declared_against_the_installed_status_handler; test_route_denominators_are_measured_and_upload_is_declared_against_generate), both 'assert 0 == (21 - 19)'",
      "_contracts/test_owned_request_contracts.py:60-62 and _contracts/test_upload_contract.py:62-65 read at the worker worktree HEAD"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W10-S1 -- the ruling's bearer line already named batch 248; batch 249 added


```json
{
  "id": "IRPT_DASHBD-W10-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~10",
  "surfaced_at": "2026-10-05T08:00:00Z",
  "one_line": "TO-DB-b-24 says the ruling's bearer line reads 'one, minted once'; the shared-checkout file already read 're-minted ... every 10 calls (batch 248 ...)' and named no batch 249.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-24 worker face: the ruling's bearer line still reads 'one, minted once'; correct it to name batches 248 and 249.",
  "world_is": "The copy of E3_SHAPE_RULING.json read from the shared checkout (876 bytes, 2026-10-05 05:30 local) already carried a bearer line naming batch 248 and not 'minted once'; it named no batch 249. Only the bearer value was rewritten, to name batch 248 (re-mint before the measured expiry) and batch 249 (one coordinator-owned shared bearer, re-minted on an interval, never one sign-in per worker); every other byte is identical (git diff --no-index: 1 line changed). Row W7-S1 described an older state of the line.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cat of the copied E3_SHAPE_RULING.json before the edit: bearer line begins 're-minted through the 49F sign-in path every 10 calls (batch 248 class (a) ...'",
      "git diff --no-index --stat shared-checkout copy vs worktree file: 1 insertion, 1 deletion"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```


## IRPT_DASHBD-W12-S1 -- the E2 tie-out: day coverage does not dominate; BD fees are consistent with most of the UNEXPLAINED rows

```json
{
  "id": "IRPT_DASHBD-W12-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~12",
  "surfaced_at": "2026-10-05T17:30:00Z",
  "one_line": "TO-DB-b-26 E2 tie-out: 6,975 of 9,078 graded segments sit outside 0.35 pp and 6,250 of them have no reason in the closed set; 4,905 of those are consistent with BD's own reported fees (a class the closed set lacks), and 3,395 segments carry a BD +1 day offset that is the 2025-01-09 market closure.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-26: an OUTSIDE row carries a reason from FLOW_TIMING, MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS or UNEXPLAINED; the round-1 reading says day-coverage dominates the difference.",
  "world_is": "Over 9,082 planned segments (9,078 graded, 4 NOT_GRADABLE BD_NO_VALUE): 2,103 WITHIN, 6,975 OUTSIDE = FLOW_TIMING 150, MISSING_PRICE 2, INCOME_DATE 568, COVERAGE_DAYS 5, UNEXPLAINED 6,250. Day coverage does NOT dominate here: BD daysHeld equals Opal's linked days on 5,678 segments, exceeds by exactly 1 on 3,395 (every one spans 2025-01-09, the national day of mourning market closure, which BD counts and Opal's trading calendar does not; no return effect), and differs by 5 or more on only 5. The BD request is feeMethod NetOfFees and the served series carries no fee (fee_amount_reason FEE_RAIL_UNUSED); BD's response reports fees per range. Netting BD's own reported fees (fees / average of beginning and ending value) from Opal's link lands within 0.35 pp of BD on 4,905 of the 6,250 UNEXPLAINED rows. Fees are not in the closed reason set, so those rows stay UNEXPLAINED with an OBSERVATION BD_FEES clause in `evidence`; the signed difference is BD below Opal on 8,054 of 9,078 graded segments. FLOW_TIMING and INCOME_DATE evidence is a re-link test (alternate flow convention, or income removed, lands within tolerance), which fees could confound; it is a necessary-not-sufficient reading. The served series now holds 6,869 accounts in 563 partitions against the plan's 6,863 accounts (the plan's own opal_twr matched the re-link on all 9,082 segments).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/TIEOUT_49F_BD_POPULATION_E2.json counts block and per-row evidence, produced by tieout_e2.py from s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/ (5,252 objects) and s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/ (563 partitions)",
      "measured on the record: segments whose BD daysHeld - Opal linked days == 1: 3,395, all 3,395 contain 2025-01-09; segments containing 2025-01-09 with offset 0: 0",
      "counts.unexplained_consistent_with_bd_fees = 4905 of outside_by_reason.UNEXPLAINED = 6250"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S26 -- W9-S1, W9-S2, W9-S3 disarmed at HEAD by re-measure

```json
{
  "id": "IRPT_DASHBD-S26",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T07:36:00Z",
  "one_line": "Rows W9-S1, W9-S2 and W9-S3 re-measured at CLOUD 71556f1a8d: the two reporting routes are ROUTED_ELSEWHERE, the census and _contracts suites pass, and the api root skips non-DECLARED rows, so all three hazards are disarmed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W9-S1",
    "IRPT_DASHBD-W9-S2",
    "IRPT_DASHBD-W9-S3"
  ],
  "spec_asserts": "W9-S1/S2/S3 (disarm_owner 2.0.0_SA_COO~P, whose IRPT_DASHBD successor lane on dell2 is 2.0.0_SA_COO~D2): declaring the reporting routes in routes.json reds the census, the seam test and two _denominator identities, and two DECLARED rows with an unmapped handler would break the api root's next plan.",
  "world_is": "routes.json at 71556f1a8d: 21 rows, 19 DECLARED and 2 ROUTED_ELSEWHERE (both reporting routes); _denominator no_handler_at_head 0. pytest -q _contracts in infra/aws/lambda/investor-reporting: 190 passed. pytest -q _authz/tests/test_unguarded_census.py: 9 passed. infra/aws/terraform/investor-reporting/api/routes.tf:40-43 builds irpt_routes only from rows with status DECLARED, so the two ROUTED_ELSEWHERE rows never reach function_key_by_name and create no duplicate of reporting-read/api.tf's routes. Fixed by DB-b-23 amendments 1 and 2 (@a414382a19, @bf68fca0ed).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python read of docs/contracts/investor-reporting/v1/routes.json at 71556f1a8d: Counter DECLARED 19, ROUTED_ELSEWHERE 2",
      "pytest -q _contracts -> 190 passed; pytest -q _authz/tests/test_unguarded_census.py -> 9 passed (dell2, 2026-10-07 ~07:3xZ)",
      "infra/aws/terraform/investor-reporting/api/routes.tf lines 40-43 at 71556f1a8d: `if r.status == \"DECLARED\"`; no terraform plan run (none needed: the filter is read from source, INFERRED for the plan itself)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "notes": "fabric reads laptop because the ratified enum is laptop | site-z; the seat runs on dell2, a box the enum does not yet name.",
  "dismissal_reason": "Disarms IRPT_DASHBD-W9-S1, W9-S2 and W9-S3: each hazard's condition is absent at HEAD, measured by the tests and the source line each row named."
}
```

## IRPT_DASHBD-W13-S1 -- dell2 identity is denied on the 49financial gold bucket

```json
{
  "id": "IRPT_DASHBD-W13-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~13",
  "surfaced_at": "2026-10-07T08:50:00Z",
  "one_line": "The dell2 agent identity is explicitly denied on s3://opal-data-49financial (the served 49F daily-return gold), so the GROSS tie-out record cannot be produced here; the BD bronze read in opal-data-assets succeeded.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-27 worker face: run tieout_e2_gross.py once; it reads the served 49F series (round-17 read_gold, s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=*/data.parquet) and writes TIEOUT_49F_BD_POPULATION_E2_GROSS.json.",
  "world_is": "ListObjectsV2 on opal-data-49financial as arn:aws:iam::313476888478:user/cloudops-dell2-agent-user returns AccessDenied 'explicit deny in a resource-based policy'; HeadObject on date=2025-01-09, 2025-01-08 and 2026-10-02 partitions returns 403. Only the default AWS profile exists on the box. The bronze read (5,252 objects, 50 s) in opal-data-assets succeeded. No record, so DB18-1-AC1..AC3 cannot pass; script and 4 offline tests (4 passed) are committed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python tieout_e2_gross.py . --cache .scratch/c.pkl on dell2 2026-10-07: botocore AccessDenied ListObjectsV2 opal-data-49financial",
      "boto3 head_object x3 on gold partitions: 403 Forbidden"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Unblock: run the committed script from a seat whose identity can read the 49financial bucket (round 17 evidently did), or grant read."
}
```

## IRPT_DASHBD-W13-S2 -- W13-S1 resolved: 3.0.0_SA_CVO ran tieout_e2_gross.py unchanged on the 

```json
{
  "id": "IRPT_DASHBD-W13-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~13",
  "surfaced_at": "2026-10-07T09:46:55Z",
  "one_line": "W13-S1 resolved: 3.0.0_SA_CVO ran tieout_e2_gross.py unchanged on the laptop @e6ed5380e6 and the record is copied byte-exact (4,196,573 bytes, sha256 febe370fbed76497).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "W13-S1: the GROSS record cannot be produced on dell2 because its identity is denied on s3://opal-data-49financial.",
  "world_is": "The record exists: git show e6ed5380e6:org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_W13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json redirected into the worker folder; 4196573 bytes, sha256 febe370fbed7649795ed75b80198f09250a88f5ca061a650c0ee514b8752d83c. This worker made no AWS call and did not re-run the script.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "sha256sum and wc -c on the copied file, dell2 2026-10-07: febe370fbed76497..., 4196573",
      "issuer ruling from 2.0.0_SA_COO~D2 under 1.0.0_SA_CTO~DELL2's standing rule (fenced firm-bucket read runs on the laptop, returns as a file)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The fence is real but the record was produced by the laptop run @e6ed5380e6 by 3.0.0_SA_CVO and delivered as a file, so the tie-out no longer needs a dell2 read.",
  "notes": "fabric reads laptop because the ratified enum is laptop | site-z; the seat runs on dell2."
}
```

## IRPT_DASHBD-W13-S3 -- DB18-1-AC2 FAILs on the laptop record: 1 of 9,078 graded rows has bd_f

```json
{
  "id": "IRPT_DASHBD-W13-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~13",
  "surfaced_at": "2026-10-07T09:46:55Z",
  "one_line": "DB18-1-AC2 FAILs on the laptop record: 1 of 9,078 graded rows has bd_fees_reported -52.99 (non-zero) but a null bd_fee_addback.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "p18_gross.py DB18-1-AC2: bd_fee_addback is null exactly when bd_fees_reported is null or zero; the order allows a null add-back also when the average value is not positive.",
  "world_is": "Record at e6ed5380e6: one segment 2026-06-17..2026-07-21, verdict OUTSIDE, reason UNEXPLAINED, bd_fees_reported -52.99, bd_fee_addback null, bd_gross_return equal to bd_return. The checker's nullness rule does not admit the order's own non-positive-average (or negative-fee) null, so either the checker or the record's one row is the defect; the script's counts are unaffected by either reading (that row is OUTSIDE and stays UNEXPLAINED).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python p18_gross.py . DB18-1-AC2 -> 'FAIL: 1 rows where bd_fee_addback's nullness disagrees with bd_fees_reported' then 'DB18-1-AC2 FAIL'",
      "python read of the record's segments: exactly 1 row with (fees in None/0) != (addback is None)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not fixed here: the record is not to be edited and the script is not to be re-run. Needs the issuer to amend AC2 (admit a null add-back on a non-positive average or negative fee) or to order a re-run."
}
```

## IRPT_DASHBD-W13-S4 -- W13-S3 resolved: checker defect, fixed by amendment 1

```json
{
  "id": "IRPT_DASHBD-W13-S4",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~13",
  "surfaced_at": "2026-10-07T09:54:14Z",
  "one_line": "W13-S3 resolved: it was a checker defect, fixed by amendment 1 @c6442ceec1; DB18-1-AC2 now passes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "W13-S3: DB18-1-AC2 FAILs because 1 of 9,078 graded rows has a non-zero bd_fees_reported and a null bd_fee_addback.",
  "world_is": "Amendment 1 (c6442ceec1) rules the checker, not the record, defective: the order nulls the add-back where BD's average value is not positive, and the one disagreeing range (2026-06-17..2026-07-21: fees -52.99, bmv 0.01, emv -0.70) is such a range. Re-run from the worktree: DB18-1-AC1 PASS, DB18-1-AC2 PASS, DB18-1-AC3 PASS.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python p18_gross.py . DB18-1-AC2 -> 'OK: addback null on 1231 of 9078 graded rows, exactly where BD reported no fee or on the 1 measured non-positive-average range(s); 4 tests passed' then 'DB18-1-AC2 PASS'",
      "git show c6442ceec1: amendment 1 of IRPT_DASHBD.TO-DB-b-27"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W13-S3 was a checker defect, fixed by amendment 1 @c6442ceec1, and DB18-1-AC2 now passes.",
  "notes": "fabric reads laptop because the ratified enum is laptop | site-z; the seat runs on dell2."
}
```

## IRPT_DASHBD-S27 -- W13-S1 and W13-S3 resolved at the round-18 drain

```json
{
  "id": "IRPT_DASHBD-S27",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T10:03:55Z",
  "one_line": "W13-S1 and W13-S3 are resolved: the fenced 49F gold read ran on the laptop (3.0.0_SA_CVO @e6ed5380e6), and the AC2 failure was a checker defect fixed by amendment 1 (@c6442ceec1); DB-b-27 and DB-b-28 merged @0f304c6405.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W13-S1",
    "IRPT_DASHBD-W13-S3"
  ],
  "spec_asserts": "W13-S1: the GROSS record cannot be produced because the dell2 identity is denied on opal-data-49financial. W13-S3: DB18-1-AC2 fails on one row with fees -52.99 and a null add-back.",
  "world_is": "W13-S1: under 1.0.0_SA_CTO~DELL2's standing rule the laptop's 3.0.0_SA_CVO ran the order's script at fb966b0a72 unchanged (@e6ed5380e6); the worker copied the record byte-exact (sha256 febe370fbed76497..., 4,196,573 bytes). The fence itself stands; no fence was widened from dell2. W13-S3: the issuer read the landed bronze object for 2026-06-17..2026-07-21 (fees -52.99, beginningMarketValue 0.01, endingMarketValue -0.70): a non-positive average value, which the order nulls; amendment 1 makes the checker admit that literal range, and a negative control without it still fails. Issuer re-run at the drain: DB18-1-AC1..3 and DB18-2-AC1..3 PASS, both instances VALID.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "e6ed5380e6 (laptop run)",
      "c6442ceec1 (amendment 1)",
      "0f304c6405 (drain)",
      "s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/ (the one bronze object read, by the dell2 identity)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolves W13-S1 (the read was made where the fence allows it) and W13-S3 (a checker defect, fixed in the issuer's own check); DB-b-27 is complete with a VALID instance."
}
```

## IRPT_DASHBD-W14-S1 -- closure_align_e1p needs a laptop run (gold bucket fenced here)

```json
{
  "id": "IRPT_DASHBD-W14-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~14",
  "surfaced_at": "2026-10-07T10:20:39Z",
  "one_line": "closure_align_e1p.py reads the served 49F gold series, which this box's identity is denied on; the E1' record needs a laptop run, then the file handed back.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-29 worker face: Opal's side is read from s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/; phase 2 needs CLOSURE_ALIGN_E1P.json.",
  "world_is": "Script and 4 offline tests (4 passed) are committed; the closure set re-derives to 2,299 from the GROSS record. The gold read is fenced on this box (see W13-S1). Run on the laptop from the repo root: python \"org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/closure_align_e1p.py\" . -- it writes org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~14/CLOSURE_ALIGN_E1P.json beside the script. Return that file for phase 2.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pytest on tests/test_closure_align_e1p.py: 4 passed",
      "closure_set() over the GROSS record: 2299 segments",
      "IRPT_DASHBD-W13-S1: same identity denied on opal-data-49financial"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Accrual choice for the closure day: mean income_return over the segment's linked days (judgment recorded in the script docstring)."
}
```

## IRPT_DASHBD-W14-S2 -- W14-S1 fence opened; script ran on dell2

```json
{
  "id": "IRPT_DASHBD-W14-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~14",
  "surfaced_at": "2026-10-07T10:47:30Z",
  "one_line": "W14-S1's gold fence opened; closure_align_e1p.py ran on dell2, no laptop run needed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "W14-S1: closure_align_e1p.py needs a laptop run because the gold bucket is fenced on this box.",
  "world_is": "At 10:44Z the dell2 identity lists the gold account_return_daily prefix; the script ran here (564 partitions, 0 vendor calls, no S3 write): 2299 closure segments, 0 within, 2299 outside.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "NFRA_CTLPLN TO-APPLY-4 amendment 1 @aefcf32c11",
      "253c4cbf38 (record and counts-only summary)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W14-S1's fence opened (TO-APPLY-4 @aefcf32c11) and the script ran on dell2."
}
```

## IRPT_DASHBD-S28 -- W14-S1 resolved: the 49F fence opened; DB-b-29 ran on dell2

```json
{
  "id": "IRPT_DASHBD-S28",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T10:55:40Z",
  "one_line": "W14-S1 is resolved: the 49F fence opened for dell2 (TO-APPLY-4 amendment 1 @aefcf32c11), the laptop relay was withdrawn, and DB-b-29 ran on dell2 and merged @33949e002d.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W14-S1"
  ],
  "spec_asserts": "W14-S1: the E1' record cannot be produced on dell2 because the dell2 identity is denied on s3://opal-data-49financial.",
  "world_is": "At 10:44Z cloudops-dell2-agent-user listed s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/ (KeyCount 1); it was AccessDenied at 08:55Z. 0.0.0_AB_MSTR~DELL2 measured the same at ~10:45Z (msg 373). The worker ran closure_align_e1p.py on dell2 over 564 partitions with no AccessDenied; DB19-1-AC1..AC3 PASS on the issuer's re-run, proof VALID.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aefcf32c11 (TO-APPLY-4 amendment 1)",
      "issuer list probe 2026-10-07T10:44Z",
      "253c4cbf38, 04d545b951 (worker)",
      "33949e002d (drain)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolves W14-S1: the fence it named opened by the fence-join apply, and the read ran on this box; no fence was widened by this lane."
}
```

## IRPT_DASHBD-W18-S1 -- the Schwab trade-leg tokens the class split reads (tr_cd TR, trade_typcd BUY/SELL) have no home in sources.json, which this cell cannot edit, so account_class_daily.py carries them in one declared block

```json
{
  "id": "IRPT_DASHBD-W18-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~18",
  "surfaced_at": "2026-10-07T11:49:00Z",
  "one_line": "TO-DB-b-33: the class split needs trade legs (tr_cd TR, trade_typcd BUY/SELL, ticker_symbol) that sources.json does not declare; the file is outside this order's paths, so the tokens sit in TRADE_LEG_DECLARATION in account_class_daily.py.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "C-ADAPTERS (account_return_daily.py docstring, sources.json doc): Schwab codes are allowed to exist only inside the adapter's sources.json, and the producer types no bucket, prefix or column of its own.",
  "world_is": "sources.json (data/assets/scripts/gold/irpt_reporting/sources.json) declares the cash code FC and the in-kind code IC but no trade code or trade direction column. NF_c needs buys minus sells, so account_class_daily.py names tr_cd TR, trade_typcd {BUY, SELL} and the identifier columns in a single module-level TRADE_LEG_DECLARATION block. Measured on the window 2026-09-28..2026-10-05: 26,400 TR rows, trade_typcd BUY 24,810 (debit_credit DEBIT) and SELL 1,590 (CREDIT), none other; trade_date equals the partition date on every row.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/sources.json (no trade key)",
      "data/assets/scripts/gold/irpt_reporting/account_class_daily.py TRADE_LEG_DECLARATION",
      "fact_trn partitions 2026-09-28..2026-10-05 read from s3 (read-only), 6 of 6 partitions"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Remedy for the release cell: add trade_code_value, trade_direction_column and trade_direction_map to the declaration (its paths), and have the producer read them. One edit, no behaviour change."
}
```

## IRPT_DASHBD-W18-S2 -- most single-stock holdings are not named by the classification module, so they land in `unclassified`, which is a large class in the local run

```json
{
  "id": "IRPT_DASHBD-W18-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~18",
  "surfaced_at": "2026-10-07T11:49:30Z",
  "one_line": "TO-DB-b-33: etf_classification.py @63fa1a2e32 names 197 tickers (ETFs and funds); individual stocks and money-market funds are not among them, so they are `unclassified`: 45 of the 78 distinct holdings in the local run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD C-CLASSES: each holding maps through the classification source; 'No row means UNCLASSIFIED; nothing is guessed'. The cell treats unclassified as the exception.",
  "world_is": "The module's ETF_CLASSIFICATIONS holds 197 tickers: equity 87, fixed_income 81, structured 13, commodities 11, alternatives 5. On dim_position date=2026-10-01 (all accounts) 2,175 distinct tickers are not named and 236 position rows carry no ticker; by market value about 16.0 percent of all position value falls to `unclassified`. Single stocks (for example large-cap names) and the money-market funds SWVXX, SNVXX and SWGXX are unnamed. In the 61-account local run, 45 of 78 distinct holdings are `unclassified` and 30 of 992 class rows carry that class. The producer sends them to `unclassified` as ordered; the class is therefore large and its return is real, but the six-class split of those accounts is partial.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/v2_portal/_shared/etf_classification.py @63fa1a2e32, ETF_CLASSIFICATIONS counted: 197",
      "dim_position date=2026-10-01 read from s3 (read-only): 107,633 rows, 2,175 unnamed tickers",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~18/CLASS_DAILY_LOCAL_RUN.json holding_map: 78 holdings, 45 unclassified"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a defect of this cell. For the served release and the frontend (C-HONESTY): whether single stocks need a source that names them is MDPF_SECCLASS's question, not this producer's."
}
```

## IRPT_DASHBD-W19-S1 -- `ETFClassifier.get_classification` returns None on a DynamoDB error, which a reader cannot tell from a ticker the table does not hold

```json
{
  "id": "IRPT_DASHBD-W19-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:30:52Z",
  "one_line": "TO-DB-b-34: the shared client swallows ClientError/BotoCoreError and returns None, so an AccessDenied on etf-classifications reads as 'ticker not held' and every holding would land in `unclassified`; the class producer reads the client's table handle directly instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-34 item 0: read each holding's class through ETFClassifier, one GetItem per ticker, 'A ticker the table does not hold is unclassified'.",
  "world_is": "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py get_classification() catches (BotoCoreError, ClientError), logs, and returns None; the same None is returned for a ticker with no item. Through that method a role that lacks dynamodb:GetItem would make the whole day `unclassified` and the day would still be written and served as if measured. account_class_daily.ClassTable therefore calls `ETFClassifier(...).table.get_item(Key={'ticker': t})` itself (same client, same table, same single-item read) and raises ClassTableUnreadable on an error, so the day is refused by name. Other callers of get_classification/get_asset_class were not examined by this cell, so the hazard for them is unassessed here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py lines 71-84 @a96e00c279: except (BotoCoreError, ClientError) -> return None",
      "data/assets/scripts/gold/irpt_reporting/account_class_daily.py ClassTable.get and tests/test_account_class_daily.py::test_a_table_read_failure_is_not_an_absence"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The client file is outside this cell's grant and is not edited. Whether the shared client should distinguish an error from an absence is the toolchain owner's question."
}
```

## IRPT_DASHBD-W19-S2 -- the reporting-gold bundle is pinned in lambda-source-map.json, not in lambda.tf; the source map is outside this cell's grant, so the packaging half of item 2 is not done

```json
{
  "id": "IRPT_DASHBD-W19-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:30:52Z",
  "one_line": "TO-DB-b-34 item 2 says lambda.tf pins the bundle; the pins (`staged_from`: repo_path, commit pin, sha256, packaged_as) live in infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-gold-lambda, which this order's paths do not include, so account_class_daily.py and etf_classifications_dynamodb.py are NOT yet bundle members.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-34 item 2: 'infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf: the bundle gains account_class_daily.py and _shared/etf_classifications_dynamodb.py (read how the current bundle pins account_return_daily.py, and pin the same way)'.",
  "world_is": "lambda.tf declares only the function, its artifact_key and the layer; its header says the bundle is built through infra/aws/lambda/ci/lambda-source-map.json + build-and-upload.sh. In that file the entry irpt-reporting-gold-lambda (line ~6048) lists the members and a `staged_from` array of pinned blobs, each with a commit `pin` and a `sha256`. A pin is a commit, so the two new members can only be pinned AFTER the commit that carries their final bytes. lambda.tf gained a comment naming the two members; nothing else in the packaging could be done inside the grant. Consequence if the apply ran on today's artifact: the handler's guarded import of account_class_daily fails, the class stage logs `CLASS_SKIPPED <day> account_class_daily not importable`, and the returns table is written unchanged. The class table would never be written until the pins land.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json entry irpt-reporting-gold-lambda (artifact_s3_key investor-reporting/irpt-reporting-gold-lambda.zip, last_deployed_commit 829e46ed7f) @4c34d86104",
      "infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf header comment and the module block: no staged_from"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the missing step: the issuer, who adds the two pins to the source map (commit-pinned, sha256-verified) and rebuilds the artifact before the apply. The never-widen packet lists this as a precondition, not as part of the signed act."
}
```

## IRPT_DASHBD-W19-S3 -- the order says the handler lists the class prefix for the newest landed day; the handler does not, so the class-prefix read grant is wider than any use

```json
{
  "id": "IRPT_DASHBD-W19-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:30:52Z",
  "one_line": "TO-DB-b-34 item 3 grants read on the class prefix 'the handler lists it for the newest landed day'; the handler lists only the returns prefix (day selection is the returns table's), so the class-prefix List/Get is granted and unused.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-34 item 3: 'Read access to the class prefix (the handler lists it for the newest landed day)'.",
  "world_is": "handler.run() and run_backfill() call newest_landed_day() on the returns prefix only, and emit_classes() emits the same days the returns path emitted; nothing lists or reads account_class_daily. The grant was made as ordered (the same prefix the role writes, ListBucket by prefix pattern and GetObject, no other bucket); it is a read of one more prefix of the same firm bucket that the code does not exercise.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py run(), run_backfill(), emit_classes() @ this cell's commit",
      "infra/aws/terraform/investor-reporting/reporting-gold/locals.tf irpt_rg_gold_read_prefixes (three prefixes)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "If a later cell makes the class table's own newest day matter (a class-only catch-up), the grant is already there; if not, dropping it is a one-line change to irpt_rg_gold_read_prefixes."
}
```

## IRPT_DASHBD-W19-S4 -- a class day skipped on a scheduled fire is not retried by the next fire

```json
{
  "id": "IRPT_DASHBD-W19-S4",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:30:52Z",
  "one_line": "TO-DB-b-34: the scheduled path selects days AFTER the newest landed returns day, and the returns day is written first, so a class day that was skipped (named in the log) stays a gap in account_class_daily until a backfill event rewrites it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-34 item 1: 'A day the class producer cannot emit is logged by name and does not stop the returns table.'",
  "world_is": "select_days(newest_landed, today) takes the returns table's newest landed date= partition as its floor, so after a fire that wrote the returns day and skipped the class day the next fire starts from the day after. Nothing in the scheduled path compares the two tables. The gap is visible in the fire's log (`CLASS_SKIPPED <day> <reason>`) and in the returned `class_failed`, and it is closable by the existing backfill event (a backfill object with start and end, accounts set to population), which now rewrites both tables for landed days; no mechanism makes either happen on its own. The never-widen packet names this under Branch B.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py select_days() and run() @ this cell's commit",
      "infra/aws/lambda/investor-reporting/reporting-gold/tests/test_class_table_emission.py::test_a_class_failure_leaves_the_returns_table_written_and_is_logged_by_name"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Armed only once the apply lands and only on a day the class stage fails. Disarm: the issuer reads the first fire's log in the after-read and runs the backfill event for any skipped day; a standing class-gap check is not built here (monitor moratorium)."
}
```

## IRPT_DASHBD-W19-S5 -- the recorded "about 16 percent unclassified" is an all-account figure; on the 61-account sample the module gives 1.8 percent and the table 0.15 percent, so the sample cannot confirm the all-account share

```json
{
  "id": "IRPT_DASHBD-W19-S5",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:33:44Z",
  "one_line": "TO-DB-b-34: the order asks for the table-based unclassified share against 'round 21's module-based share'; the 16 percent (W18-S2) is every account on dim_position 2026-10-01, while round 21's 61-account sample re-measures at 1.804 percent on 2026-10-05 under the module and 0.153 percent under the table.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-34 item 0: 'Re-run the round-21 sample's 61 accounts and print the unclassified share against round 21's module-based share'; row W18-S2: about 16 percent of value unclassified.",
  "world_is": "Round 21's own record carries no market values, so its module-based share on the sample was not recorded; this cell re-measured it on identical positions by classifying the same rows from the module dictionary (that pass reproduces round 21's 992 class rows and 30 unclassified rows exactly). Sample, 2026-10-05: module 1.804 percent, table 0.153 percent; holdings not in the source 45 of 78 under the module, 9 of 78 under the table. The 16 percent is the all-account share under the module on 2026-10-01 and is not reproducible from a 61-account sample. The table-based all-account share is unmeasured: it is the apply's after-read A3.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/RELEASE_LOCAL_RUN.md section B",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/class_share_61_driver.py (the driver that produced both columns)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a defect. The release figure the CTO's criterion 3 wants is the served partition's, read at the apply."
}
```

## IRPT_DASHBD-W19-S6 -- the class catch-up from the class table's own newest partition disarms W19-S4 and uses the class-prefix read grant W19-S3 named unused

```json
{
  "id": "IRPT_DASHBD-W19-S6",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~19",
  "surfaced_at": "2026-10-07T12:49:00Z",
  "one_line": "TO-DB-b-34 amendment 1: the scheduled fire now catches the class table up from its own newest landed partition, which disarms W19-S4 and gives the class-prefix read grant named unused in W19-S3 its use.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-34 amendment 1 @e765698322: 'The handler computes the class table from ITS OWN newest landed partition: on each scheduled fire it lists the class prefix, and emits every trading day after its newest class day through the newest returns day just written (bounded by MAX_DAYS_PER_FIRE), so a class day skipped on one fire is retried on the next.'",
  "world_is": "handler.catch_up_classes() lists the class prefix (the list grant ListExactlyTheThreeGoldPrefixes already covers it), takes class_owed_days(newest class day, days written this fire) and emits those days oldest first, at most MAX_DAYS_PER_FIRE (10); a day older than this fire's returns days is recomputed through compute() as a read and nothing is written to the returns table for it. A day that still fails is logged `CLASS_SKIPPED <day> <reason>`; a failed class listing is logged `CLASS_CATCHUP_LIST_FAILED` and owes only this fire's days; the returns table is never held. No class day is written beyond max(written returns days). The W19-S4 gap (a skipped class day stays a gap until a backfill) is closed in code, and the read grant W19-S3 named unused is now exercised by the listing. Nothing is deployed: the hazard stays inert until the apply, and the apply's packet names the retry under Branch B.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py catch_up_classes() and class_owed_days()",
      "infra/aws/lambda/investor-reporting/reporting-gold/tests/test_class_catch_up.py::CatchUpTests::test_a_skipped_day_is_retried_on_the_next_fire",
      "infra/aws/lambda/investor-reporting/reporting-gold/tests/test_class_catch_up.py::CatchUpTests::test_the_catch_up_never_writes_a_day_beyond_the_newest_returns_day",
      "infra/aws/lambda/investor-reporting/reporting-gold/tests/test_class_catch_up.py::OwedDaysTests (bound, weekend, holiday, no class partition)"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed by the amendment-1 code fix: the next scheduled fire retries a skipped class day, proven by the two named tests; nothing is deployed, so there is no live hazard left to investigate.",
  "notes": "Disarms IRPT_DASHBD-W19-S4 (disarm owner 2.0.0_SA_COO~D2 named a backfill; the code now does it on the next fire) and uses the class-prefix read grant named unused in IRPT_DASHBD-W19-S3."
}
```

## IRPT_DASHBD-S29 -- round 22's rows resolved at the drain

```json
{
  "id": "IRPT_DASHBD-S29",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T12:57:04Z",
  "one_line": "Round 22's rows resolved at its drain @d48052d79b: W19-S2 ruled a release precondition, W19-S3 and W19-S4 closed by the class catch-up (amendment 1 @e765698322), W18-S1 closed by the trade-leg tokens moving into sources.json.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W19-S2",
    "IRPT_DASHBD-W19-S3",
    "IRPT_DASHBD-W19-S4",
    "IRPT_DASHBD-W18-S1"
  ],
  "spec_asserts": "W19-S2: the bundle pins sit outside the grant; W19-S3: the class-prefix read grant is unused; W19-S4 (ARMED, disarm owner this seat): a class day skipped on a fire is never retried; W18-S1: the trade-leg tokens sit in the producer, not the declaration.",
  "world_is": "W19-S2: the source map's staged_from pins are written at deploy time against the commit that carries the files; the never-widen packet now names them as an apply precondition (three entries, pinned to the drain commit with sha256), and the map is unedited (0-line diff). W19-S3 and W19-S4: handler.py's catch_up_classes() lists the class prefix and emits every trading day after the newest class day through the newest returns day (at most 10 per fire); tests test_a_skipped_day_is_retried_on_the_next_fire and test_the_catch_up_never_writes_a_day_beyond_the_newest_returns_day pass (96 passed across both test folders at the drain). Nothing is deployed, so the hazard was never live. W18-S1: sources.json carries the trade-leg tokens and the producer reads them there; returns DELTA=0 against the base handler AND base sources.json (sha256 11453fc7... both sides).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "e765698322 (amendment 1)",
      "bae1e8bd8b, 1a9f68b833 (worker)",
      "d48052d79b (drain)",
      "issuer re-run: DB22-1-AC1..AC3 PASS, proof VALID; pytest 96 passed"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each named row's condition is resolved at HEAD by the drained code and packet; W19-S4 disarms by the catch-up before any deploy."
}
```

## IRPT_DASHBD-W20-S1 -- the custodian's lot-table names and columns are typed in account_activity_lots.py (LOT_SOURCE), not declared in sources.json, because sources.json is outside TO-DB-b-35's grant

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~20",
  "surfaced_at": "2026-10-07T14:28:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W20-S1",
  "one_line": "C-ADAPTERS: the lot adapter's declaration (fact_rld, fact_uln, fact_ult and the columns read from them) sits in the producer's LOT_SOURCE block, not in sources.json, because sources.json is not in TO-DB-b-35's <paths> grant.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "C-ADAPTERS and sources.json's own header: the producer types no bucket, prefix or column of its own, the declaration is data; the order's <paths> block (the write grant) lists no sources.json.",
  "world_is": "The three custodian lot tables and the 30-odd column names the lot tables read have no entry in sources.json, so account_activity_lots.py carries them in one LOT_SOURCE dict. Everything else is read from the declaration through the served producer's loaders: the bucket, the transaction prefix (the lot prefixes are its siblings), the account column and padding, the trade code and its column. Nothing deploys from this file in this cell (no upload path exists), so no served surface reads the typed names.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py@cfb9a56b0b LOT_SOURCE block",
      "org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-35.activity-and-lot-tables.md <paths> block"
    ]
  },
  "notes": "Remedy for a later cell that holds sources.json in its grant: add a lot_source entry to the Schwab source, have LOT_SOURCE read it, and re-run ACTIVITY_LOTS_LOCAL_RUN.json at DELTA=0. Round 22's W18-S1 was the same shape and closed the same way."
}
```

## IRPT_DASHBD-W20-S2 -- the activity identity ties on the named account-window; 20 of 2181 sampled account-days and 39 of 91 sampled account-windows fall outside it

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~20",
  "surfaced_at": "2026-10-07T14:28:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W20-S2",
  "one_line": "The activity identity ties on the named account-window (gap inside one cent) but not everywhere: 20 of 2181 graded account-days (8 accounts) exceed the rounding allowance, and 39 of 91 graded account-windows are above one cent.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order: beginning value + contributions - withdrawals + realized + unrealized change + income = ending value, within one cent, for ONE account and the window; if it cannot be made to hold on the sampled account-window, file BLOCKING and stop.",
  "world_is": "It holds on the named account-window (DB23-1-AC1 PASS), so the BLOCKING condition is not met. Across the 100-account sample it holds for 52 of 91 graded windows within one cent; the rest are either rounding (every lot figure is a 2 dp amount and an account may carry hundreds of lots; the day grain derives an allowance from the lot counts) or a real difference. 20 account-days across 8 accounts exceed the allowance and are labelled GAP_ABOVE_ALLOWANCE with identity_gap carried, never plugged into a term; the largest are four to seven figures on days where the custodian value moves with no matching lot, flow or income figure (value held outside the lot tables, or a flow the served classifier books against another account-day). The cause is NOT diagnosed here. The account ids and amounts are in the record, not in this file.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json@cfb9a56b0b window_identity and coverage_census",
      "org/standards/IRPT_DASHBD_ACCOUNT_ACTIVITY_DAILY_CONTRACT.json@cfb9a56b0b coverage enum and rule24_record"
    ]
  },
  "notes": "For the round-23 analysis: the next enrichment names which of the two causes moves the GAP rows (a flow classified onto the wrong day, or value outside the lot tables) before the table is released."
}
```

## IRPT_DASHBD-W20-S3 -- neither close_event_id nor event_id identifies one lot; the tables key a realized lot by the closing and opening event ids and sum open-lot rows that share an id

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~20",
  "surfaced_at": "2026-10-07T14:28:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W20-S3",
  "one_line": "The custodian's lot event ids do not identify one lot: close_event_id repeats across the lots of one order (131 distinct values over 726 realized lots) and event_id repeats within an account on the unrealized tables, so the lot keys are composites.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order ties each realized lot to its closing transaction and builds a per-lot unrealized table; it does not say how a lot is keyed, and the prior art reads the lots as rows.",
  "world_is": "Realized: the pair (close_event_id, close_open_event_id) is unique over all 726 sampled lots and is the lot_id; close_event_id alone is shared by every lot of one order. Unrealized: (event_id, cusip, acquired_date, original purchase date) leaves 28 lot-day rows in 160,549 sharing a key with another row, which the table sums with source_rows saying how many rows made the figure; sums are exact, no figure is lost. A repeat of a realized lot id refuses, so a source change shows rather than merging silently. One more measured property: each fact_rld partition holds only the lots closed that day (closing_date equals the partition date on every partition read), not a cumulative file, so the vintage read is the 24 per-day partitions 2026-09-01..2026-10-05.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py@cfb9a56b0b realized_rows and unrealized_rows",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json@cfb9a56b0b rld_vintage"
    ]
  }
}
```

## IRPT_DASHBD-W21-S1 -- the served flow rule drops every CONDITIONAL-BY-COUNTERPARTY row on pandas 3: `_final is None` never matches a NaN

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T15:58:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S1",
  "one_line": "On pandas 3.0.6 account_return_daily.classify_and_sum assigns _final = None into a frame column, the column becomes str dtype and the None becomes NaN, so `_final is None` matches nothing and every CONDITIONAL-BY-COUNTERPARTY row is dropped from the flow and is not counted as UNRESOLVED.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "classify_and_sum (account_return_daily.py lines 508-611) resolves a CONDITIONAL-BY-COUNTERPARTY row by same-account-type-transfer, then the pair matcher, then the text counterpart, and defaults an unmatched row to EXTERNAL; FINAL_BY_PARTITION maps that class to None and the code reads 'unresolved so far' as `_final is None`. The round-23 identity record treats the flow term as complete.",
  "world_is": "pandas 3.0.6 on this machine: `t['_final'] = [list holding str and None]` yields a str-dtype column in which the None is NaN (a 3-line probe returns [False, False, False] for `v is None`). So _pending() is empty on every day, no stage runs, nothing defaults to EXTERNAL, and the census shows the rows only as `ft_excluded_class-nan_rows` (71, 38, 32, 74 on four of the days). 6 cash journal rows and 5 in-kind rows of the largest-gap account are dropped this way; the same producer with `pd.options.future.infer_string = False` resolves them (flow -351,775.00 on 2026-09-02 against 0.00 as run, -3,000,165.12 on 2026-09-14, 12 days printed in the record). The 91 graded accounts carry 24 CONDITIONAL rows over 7 types. WHETHER THE LAMBDA RUNTIME THAT SERVES account_return_daily CARRIES pandas 3 IS UNMEASURED: comp-find found no pandas pin under infra/aws/lambda/investor-reporting (0 requirements files over 578 files scanned).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/GAP_DIAGNOSIS_E1.json conditional_class_evidence (12 days, as-run and counterfactual flow per account) and largest_gap_window.evidence_rows (11 rows)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py lines 510-535 (_final assigned from a list holding None) and 528-529 (_pending)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/gap_diagnosis_e1.py flow proof, run on pandas 3.0.6"
    ]
  },
  "notes": "ARMED because a pandas 3 host silently under-reads every journal and transfer of assets, in the served-producer file and in every table built on it. The producer was not edited (read-only grant). The remedy is a one-line comparison (pd.isna) in a served file, which is not this order's grant; E2's order must either grant it or state a different disarm."
}
```

## IRPT_DASHBD-W21-S2 -- fixing the named cause does not tie the in-kind windows: 7 of 39 gaps stay above 0.05 with the CONDITIONAL rows resolved

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T15:58:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S2",
  "one_line": "With the CONDITIONAL rows resolved (the counterfactual run) 7 of the 39 windows still miss by more than 0.05, two of them by about 1.6 million and 92 thousand, because the identity has no term for in-kind lots, for a basis posted after receipt, or for a basis adjustment.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The round-24 cut reads E2 as 'fix the named cause and re-grade': one cause for the 39 gaps, found by E1.",
  "world_is": "E1 names five causes over the 9 MISSING-TERM windows (CONDITIONAL_FLOW_NOT_READ 4, LOT_BASIS_MOVED_WITHOUT_FLOW 2, LOT_BASIS_ABOVE_ORIGINAL_COST 3, FEE_ADMIN_HAS_NO_TERM 1, WITHHELD_TAX_HAS_NO_TERM 1; two windows carry two). Resolving the first only closes 2 windows (the cash-only ones); the two in-kind windows turn into other gaps because an in-kind arrival brings a lot whose whole value is gain (cost basis 0 until posted) and the flow also counts the arrival (window gap -1,607,156.91 and +92,255.50), and the lot table lags the balance by one trading day on an in-kind journal out. FEE-ADMIN, a withheld-tax debit and the ADJ in-kind removal move value and map to no term, and a basis wedge on new lots (cost_basis_unamortized above the cash paid, 99.94 on one lot) shifts the gain. Each is a term or a definition the identity lacks, not a rounding.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/GAP_DIAGNOSIS_E1.json gap_classes.counterfactual and gap_classes.rows (each MISSING-TERM row carries its components, residual and evidence rows)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/GAP_DIAGNOSIS_E1.json unmapped_value_movers (10 types)"
    ]
  },
  "notes": "For the round-24 analysis: the enrichment list for E2 should state which of the five the re-grade must close and which it carries forward as a stated unmapped term; an identity that ties on the cash-only windows and not on the in-kind ones is a partial FWD-4."
}
```

## IRPT_DASHBD-W21-S3 -- the census grain: a type is key plus side, because a key can carry opposite signs

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T15:58:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S3",
  "one_line": "The order asks for a sign per type, but one tran_srcde/tr_cd/sb_cd key carries both a credit and a debit (BKSWP, BRSWP, $JNL, TOA), so the census is keyed on the key plus its debit_credit side: 35 types over 30 keys.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The task order lists 'every type, its row count, its sign as the activity rule reads it (+, - or UNSIGNED)', one sign per type.",
  "world_is": "The rule signs a cash row from debit_credit (C +, D -) and an in-kind row from L/S, so the sign belongs to the row's side, not the key. The census in GAP_DIAGNOSIS_E1.json is keyed on tran_srcde/tr_cd/sb_cd/debit_credit (35 rows over 2,662 fact_trn rows of the 91 graded accounts; 30 distinct keys), and `unmapped_value_movers` names types in the same form.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/GAP_DIAGNOSIS_E1.json type_census and type_census_scope.type_grain"
    ]
  }
}
```

## IRPT_DASHBD-S30 -- W21-S1 disarmed for the served gold (layer pandas 2.2.3 measured)

```json
{
  "id": "IRPT_DASHBD-S30",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T16:04:58Z",
  "one_line": "W21-S1 disarmed for the served gold: the served reporting-gold function's layer carries pandas 2.2.3, so the None-to-NaN drop in classify_and_sum is pandas-3-only and hits LOCAL runs on dell2 (pandas 3.0.6), which DB-b-37 now runs under the served behaviour.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W21-S1"
  ],
  "spec_asserts": "W21-S1: classify_and_sum in the served producer resolves CONDITIONAL-BY-COUNTERPARTY rows with _final is None; under pandas 3 the None becomes NaN and the rows drop from the flow uncounted; whether the Lambda runtime carries pandas 3 was unmeasured.",
  "world_is": "MEASURED: irpt-49f-reporting-gold-lambda takes pandas from irpt-performance-native-layer (lambda.tf:34-53); the layer's latest version is v1 (created 2026-09-24, python3.12), and its zip in the account's lambda-layers bucket lists pandas-2.2.3.dist-info, numpy-1.26.4.dist-info and pyarrow-14.0.2.dist-info (zip directory read by ranged S3 reads; nothing executed). So the served account_return_daily gold is not affected. This box runs pandas 3.0.6, so the round-23 local identity run was. DB-b-37 amendment 1 runs the call under the served behaviour and asserts the conditional rows resolve. LATENT: the served code still drops these rows if its layer ever moves to pandas 3; that hardening belongs to a release cell of the served producer.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda list-layer-versions irpt-performance-native-layer: v1, 2026-09-24",
      "layer zip directory: pandas-2.2.3, numpy-1.26.4, pyarrow-14.0.2",
      "local python -c pandas.__version__: 3.0.6",
      "infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf:34-53"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The hazard is not live on the served gold (pandas 2.2.3 measured); its local effect is handled by DB-b-37 amendment 1; the latent pandas-3 hardening is named for the served producer's next release."
}
```

## IRPT_DASHBD-W21-S4 -- after the three fixes one in-kind account still misses: the custodian re-selects the relieved lots the day after an in-kind departure

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T16:46:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S4",
  "one_line": "One of the 91 windows still fails after amendment 1's three rules, because the custodian re-selects which lots an in-kind departure relieved on the next trading day, moving cost basis with the share count, the flow and the value all unchanged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Amendment 1 rules 1-3 name the causes of the in-kind windows (dropped conditional rows, in-kind transfers at transfer-date value, unmapped value movers) and expect the re-grade to close them.",
  "world_is": "After the rules, 55 of 91 windows tie within one cent and 36 do not: 32 ROUNDING, 3 MISSING-TERM (a basis above the cash paid, unchanged from DB-b-36) and 1 OTHER. The OTHER window carries two signatures: a lot table that trails the balance by one trading day on an in-kind departure (two day gaps that net to zero over the two days), and a single day on which the custodian re-selects the lots relieved by the departure of the day before (the lots' share count is the same before and after, no flow, no sale, and the day's gap equals the change in the custodian's summed cost basis to the cent). The second is a restatement of basis that moves no value; no rule in the order maps it, and a term built from the lot table's own basis change would zero the gap by construction, so it is carried as a gap.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json regrade.failures (the class OTHER row carries both signatures and its day gaps)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/identity_regrade_e2.py classify_failure"
    ]
  },
  "notes": "For the round-24 analysis: either the identity states a restatement term (a decision about what unrealized_change means when basis moves with no value) or the window stays a listed failure. Not plugged here."
}
```

## IRPT_DASHBD-W21-S5 -- the lot table trails the balance on an in-kind departure, so the leg is matched to the lots on the day they post (a choice the order did not state)

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T16:46:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S5",
  "one_line": "On one in-kind departure the custodian's unrealized lots still carry the position on the leg's day and drop it on the next trading day, so an in-kind leg waits up to 3 trading days for its lots; the 3 is a chosen bound, not a measured one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Amendment 1 rule 2: an in-kind departure is a WITHDRAWAL at its market value on the transfer date, and the lots that left are measured from it; the order states no timing between the leg and the lot table.",
  "world_is": "Of the 4 in-kind departures matched in the window, 3 post on the leg's own day and 1 posts one trading day later (the balance has already dropped the position, the lot table has not). The producer keeps the flow on the leg's day and books the departure gain on the day the lots post, so the two days carry equal and opposite gaps (each stays GAP_ABOVE_ALLOWANCE) and the window over both ties. The bound LEG_LAG_DAYS = 3 is a choice: one lagged departure is the only sample, and a leg not posted within the bound is listed unmatched, never bent.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json inkind.matched_departures (leg_day, lag_trading_days)",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py LEG_LAG_DAYS and _one_security"
    ]
  },
  "notes": "A longer history of in-kind departures would measure the lag; until then the bound is the producer's, stated here."
}
```

## IRPT_DASHBD-W21-S6 -- pandas' option context is process-global: the served runtime must wrap the whole flow prefetch, not one call

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~21",
  "surfaced_at": "2026-10-07T16:46:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W21-S6",
  "one_line": "Amendment 1 rule 1 says to run the served call under pd.option_context(\"future.infer_string\", False); the context is global to the process, so a context entered per call inside the producer's thread pool restores the option under a sibling thread still classifying.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Amendment 1 rule 1: run the call under pd.option_context(\"future.infer_string\", False) where the option exists, and assert that the CONDITIONAL rows resolved.",
  "world_is": "pandas options are process-wide state, not thread-local, and compute_local classifies the flow days on a ThreadPoolExecutor of 12. The context is therefore held around the whole pool, and ServedFlowCache.get refuses to classify a day when the option is not in force (a test covers the refusal). Because the producer needs each day's own transaction frame for its in-kind and income supplements, ServedFlowCache reproduces FlowCache.get call for call; a control reads three days with both and finds the returned tuples equal on 3 of 3, and the same served call on pandas' default string behaviour differs on the conditional-bearing days (2 of 2 sampled).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json controls",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py served_runtime, ServedFlowCache, compute_local"
    ]
  },
  "notes": "If the served producer is ever hardened (a pd.isna test in classify_and_sum, named in S30), this wrapper becomes redundant and its refusal can go with it."
}
```

## IRPT_DASHBD-W22-S1 -- the lag order measures all trades but the bound governs in-kind legs; reinvested-dividend lots carry the trade date in orgpurch_date

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~22",
  "surfaced_at": "2026-10-07T17:47:52Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W22-S1",
  "one_line": "The order measures the lag of every trade, but LEG_LAG_DAYS governs only in-kind legs; and a reinvested-dividend buy has no lot acquired on its trade date, its same-day lot carries the trade date in orgpurch_date instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DB-b-38 item 1: for every trade that should produce or relieve a lot (buys, sells, in-kind), find its lot row and the lag in trading days; the measured distribution sets LEG_LAG_DAYS.",
  "world_is": "LEG_LAG_DAYS is read only by _one_security, for in-kind legs; the buy and sell lags (873 of 887 trades) are measured beside it and do not feed any producer rule. Matching a buy to its lot by acquired_date left 7 of 765 buys unmatched, all sb_cd RD (reinvested dividend): the custodian posts their lot the same day with acquired_date earlier and orgpurch_date equal to the trade date. They match on orgpurch_date at lag 0. Result: 887 of 887 matched, 886 at lag 0 and 1 at lag 1 (an in-kind departure), so LEG_LAG_DAYS is 1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/LOT_LAG_E2.json lags, by_kind, buys_matched_by",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/lot_lag_e2.py buy matching",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py LEG_LAG_DAYS, _one_security"
    ]
  },
  "notes": "The sample holds 14 in-kind legs; the bound is measured on a window with 1 lagged leg. A longer history would tighten it. The producer lists a leg past the bound and never bends it."
}
```

## IRPT_DASHBD-W22-S2 -- A realized lot names the open lot it closed by its opening event id, and that id repeats within an account when a wash sale re-dates a lot, so the sal

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~22",
  "surfaced_at": "2026-10-07T18:48:59Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W22-S2",
  "one_line": "A realized lot names the open lot it closed by its opening event id, and that id repeats within an account when a wash sale re-dates a lot, so the sale linked to no single lot.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DB-b-39 item 2: change the activity or lot rule so every account with the same pattern is handled. The producer links a realized row to the prior day's open lot by close_open_event_id and security alone.",
  "world_is": "In the 91-account window one sale of 0.94 shares was listed SALE_NOT_LINKED_TO_ONE_LOT: its opening event id is shared by a second, smaller lot (acquired a different day), so two open lots matched. The realized row carries its acquired_date; adding it to break a tie links the sale to exactly one lot (0 unlinked sales in the re-run, from 1). This is a linking rule, not a figure: no sale is linked that was not already unique on event id, and a tie still unresolved stays unlinked and listed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py _sold_lot",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/WINDOWS_E1.json rule_audit.unmatched (empty)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json inkind.unmatched (round 24: 1 listing)"
    ]
  },
  "notes": "Round 24 left that sale unlinked and its basis at the custodian's figure; with the wash-sale rule it had to be linked or it would have opened a new cent-sized gap."
}
```

## IRPT_DASHBD-W22-S3 -- The wash-sale rule adds a basis_source member (WASH_SALE_EXCLUDED_BASIS) and the method and schema versions move (3 and 1.2); the lot contracts under 

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~22",
  "surfaced_at": "2026-10-07T18:48:59Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W22-S3",
  "one_line": "The wash-sale rule adds a basis_source member (WASH_SALE_EXCLUDED_BASIS) and the method and schema versions move (3 and 1.2); the lot contracts under org/standards do not list basis_source.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DB-b-39 item 2 names a rule change in the activity or lot rule; it does not name a schema member.",
  "world_is": "Measuring a lot from the cash paid needs the custodian's figure and the identity's figure to differ with a stated reason, which basis_source already carries for in-kind lots. The axis stays one-intent (which cost the lot is measured from) with three members in a stated precedence (IN_KIND over WASH_SALE over CUSTODIAN). org/standards/IRPT_DASHBD_ACCOUNT_LOT_*_CONTRACT.json do not mention basis_source (round 24 added it without a contract line), and are outside this order's paths, so they were not edited. METHOD_VERSION 2 to 3 and SCHEMA_VERSION 1.1 to 1.2 mark the change; no table is written to S3, so no served consumer reads either.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py BASIS_SOURCES, METHOD_VERSION, SCHEMA_VERSION",
      "org/standards/IRPT_DASHBD_ACCOUNT_LOT_UNREALIZED_DAILY_CONTRACT.json (no basis_source column)"
    ]
  },
  "notes": "For the CTO's next analysis: the two lot contracts need a basis_source and custodian_cost_basis line before any table is served."
}
```

## IRPT_DASHBD-W22-S4 -- Removing served_runtime() (DB-b-40 item 1) leaves round 24's regrade helper unable to regenerate: it calls aal.served_runtime().

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~22",
  "surfaced_at": "2026-10-07T19:25:53Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W22-S4",
  "one_line": "Removing served_runtime() (DB-b-40 item 1) leaves round 24's regrade helper unable to regenerate: it calls aal.served_runtime().",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DB-b-40 item 1: set the option once at the producer's entry and remove the per-call context.",
  "world_is": "deliverables/0.9.0_WK_IRPT_DASHBD~21/identity_regrade_e2.py calls aal.served_runtime() in its control block (two uses); with the function removed that file raises AttributeError if run again. It is a round-24 deliverable outside this order's paths, so it was not edited; the round-24 record it wrote (IDENTITY_REGRADE_E2.json) is unchanged and this worker's windows_e1.py does not use the removed name.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/identity_regrade_e2.py run_flow_served and main controls",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py set_served_runtime, classify_flow_days"
    ]
  },
  "notes": "Regenerating round 24's record needs either aal.set_served_runtime() in that helper or the pre-b-40 producer; neither is a data change."
}
```

## IRPT_DASHBD-W22-S5 -- The served classify_and_sum cannot take a frame whose index repeats a label: it addresses rows with t.at[label, column].

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~22",
  "surfaced_at": "2026-10-07T19:25:53Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W22-S5",
  "one_line": "The served classify_and_sum cannot take a frame whose index repeats a label: it addresses rows with t.at[label, column].",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DB-b-40 item 2: make classify_and_sum resolve the conditional class without depending on None surviving a column; change nothing else.",
  "world_is": "While testing that the hardened column does not depend on the frame's index, a frame with a repeated index label (as pd.concat of several partitions without ignore_index would give) made the unchanged stage 1 (t.at[idx, detail_col] or '') raise ValueError (the truth value of a Series is ambiguous). The same happens on the unhardened source, so it predates this order. The served read path builds one partition's frame per call, so the repeated-label case is not reached today; the new test uses a unique, shuffled index. Not changed here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py classify_and_sum stage 1 (t.at[idx, detail_col])",
      "data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py test_classify_and_sum_does_not_depend_on_the_frame_index_when_it_holds_the_final_column"
    ]
  },
  "notes": "A reset_index(drop=True) on the copy at the top of classify_and_sum would remove it; out of scope for an order that changes nothing else in the file."
}
```

## IRPT_DASHBD-W23-S1 -- The role's silver read set holds only the three custody prefixes, but the activity and lot producer reads the custodian's lot tables, which sit beside them.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:21:51Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S1",
  "one_line": "The role's silver read set holds only the three custody prefixes, but the activity and lot producer reads the custodian's lot tables, which sit beside them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-41 item 4: the write ARNs become the returns, class and three new prefixes; read on the three prefixes for the newest-landed-day listing. Nothing in the order grants the role a read of the custodian's lot tables.",
  "world_is": "account_activity_lots.py reads fact_rld, fact_uln and fact_ult (and fact_trn) under the silver custody root, siblings of the transactions prefix. The role's silver read set (locals.tf irpt_rg_silver_prefixes) was dim_position, dim_balance and fact_trn only, so with the order's grants alone every activity and lot day would fail AccessDenied at the first lot read and land as LOTS_SKIPPED (Branch B on every fire). This cell adds the custodian's lot-table prefixes to the silver READ set, derived in locals.tf from the declaration's lot_source (the move W20-S1 asked for), never typed: GetObject and the ListBucket prefix pattern on three more prefixes. No write, no Delete, no other bucket. The packet names it for the CTO half to sign. Whether the silver bucket's own policy admits the role on those prefixes is not read by this cell.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/reporting-gold/locals.tf irpt_rg_silver_prefixes (this cell's commit)",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py read_window / lot_prefix",
      "data/assets/scripts/gold/irpt_reporting/sources.json lot_source"
    ]
  },
  "notes": "The after-read A5 prints the role policy; the silver statements are the ones to read for the three added prefixes."
}
```

## IRPT_DASHBD-W23-S2 -- The lots stage costs about twice the returns stage in time and four times in peak memory on 20 accounts for one day; at population scale it is unmeasured against a 900 s, 2048 MB function.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:21:51Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S2",
  "one_line": "The lots stage costs about twice the returns stage in time and four times in peak memory on 20 accounts for one day; at population scale it is unmeasured against a 900 s, 2048 MB function.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "spec_asserts": "TO-DB-b-41 item 4: the schedule does not change; item 6: record the run's wall time and peak memory.",
  "world_is": "20 accounts, 2026-10-05, one local process: the unextended handler 34.6 s and 228 MB peak working set; the extended handler 69.5 s and 992 MB, with 1,330 unrealized-lot rows. The round-23 record (deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json) gives a population of 7,597 accounts, 380 times the sample, so the lots stage's rows, its pandas row loops and its memory at population scale are not measured and may exceed the function's 900 s timeout or 2048 MB. The lots stage runs AFTER the returns and class stages, so a timeout or out-of-memory kill there cannot lose a returns or class day; it would end the invocation in error each fire, the lots days would never land, and nothing in this root notifies anyone.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/RELEASE_LOCAL_RUN.json wall_seconds, peak_working_set_mb",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json population"
    ]
  },
  "notes": "The first fire's after-read (packet A1) shows whether the day landed; an ad-hoc dry_run invoke measures the duration before the organic fire. Memory and timeout are in lambda.tf and unchanged by this order; changing them is a later cell's act.",
  "disarm_owner": "2.0.0_SA_COO~D2"
}
```

## IRPT_DASHBD-W23-S3 -- The activity and lot producer had no emit function, so the handler could not emit through it; emit_day() is added to the producer.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:21:51Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S3",
  "one_line": "The activity and lot producer had no emit function, so the handler could not emit through it; emit_day() is added to the producer.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-41 item 3: the handler emits the same day of the three tables through account_activity_lots.py's own functions. The producer's header and a test said it has no upload path.",
  "world_is": "account_activity_lots.py carried compute_local and write_parquet (local) and no function that writes S3; test_the_addresses_are_builder_output_and_the_producer_has_no_write_path asserted no put_object, upload_file or stream_to_parquet in the file. This cell adds ONE function, emit_day() (the account_class_daily.emit_class_day shape: the builder address, data.parquet then manifest.json, a refusal on an empty day, a row off the day and a repeated primary key), and changes that test to allow exactly that one function and nothing else in the file. The producer's CLI still has no upload path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py emit_day, PRIMARY_KEYS",
      "data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py test_the_addresses_are_builder_output_and_the_only_write_path_is_emit_day"
    ]
  },
  "notes": "Both files are in the order's paths."
}
```

## IRPT_DASHBD-W23-S4 -- No file names 'the round-24 sample'; the first 20 accounts of the 100-account list the later rounds graded were used, and that day holds no realized lot for them.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:21:51Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S4",
  "one_line": "No file names 'the round-24 sample'; the first 20 accounts of the 100-account list the later rounds graded were used, and that day holds no realized lot for them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-41 item 6: the extended handler's --local mode for 2026-10-05 over the round-24 sample's first 20 accounts. Item 1: prove uniqueness of the primary key on the local run's rows.",
  "world_is": "Round 24's record (deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json exercise_selection) names its population as the 91 graded accounts of the round-23 sample; the list itself is the `accounts` array of deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json (100 accounts). The first 20 of that array were used and the source is written into RELEASE_LOCAL_RUN.json. On 2026-10-05 those 20 accounts close no realized lot (0 rows), so a one-day run cannot show the realized key unique; KEY_UNIQUENESS_WINDOW.json runs the same 20 accounts over 2026-09-01..2026-10-05 (24 trading days: 432 activity, 30 realized and 30,183 unrealized rows, 0 repeated keys) and exercises emit_day(upload=False) on every day.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/RELEASE_LOCAL_RUN.json accounts_source, primary_key_uniqueness",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/KEY_UNIQUENESS_WINDOW.json"
    ]
  },
  "notes": "If a different list was meant, release_local_run.py takes the list from one constant and reruns in about two minutes."
}
```

## IRPT_DASHBD-W23-S5 -- terraform is not on this box, so the HCL edits in locals.tf, iam.tf and lambda.tf are unvalidated and the plan counts in the packet are read from the diff, not from a plan.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:21:51Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S5",
  "one_line": "terraform is not on this box, so the HCL edits in locals.tf, iam.tf and lambda.tf are unvalidated and the plan counts in the packet are read from the diff, not from a plan.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-41 items 4 and 7: edit the three .tf files; the packet carries a targeted plan command and its expected counts. NO terraform init, plan or apply is permitted to this cell.",
  "world_is": "No terraform or tofu binary resolves on PATH, so terraform fmt and validate were not run either. The new locals (the derived silver lot prefixes, the three gold table prefixes, the five write ARNs) were emulated in Python from sources.json and scopes.json and printed in the packet; the expressions used are split, trimsuffix, slice, join, concat, distinct and a for expression, all in the language since 0.12. The expected plan (0 to add, 3 to change, 0 to destroy) is derived from which resource arguments the diff touches, and the issuer reads the real plan before the halves are used.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/reporting-gold/locals.tf (this cell's commit)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~23/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE.md Plan"
    ]
  },
  "notes": "A plan that differs from the expected counts stops the apply; the packet says so."
}
```

## IRPT_DASHBD-W23-S6 -- The deployed bundle pins a returns producer that is not the one at HEAD, so a rebuilt artifact changes the served returns code by 4 lines the local DELTA=0 run does not cover.

```json
{
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~23",
  "surfaced_at": "2026-10-07T22:34:50Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_DASHBD-W23-S6",
  "one_line": "The deployed bundle pins a returns producer that is not the one at HEAD, so a rebuilt artifact changes the served returns code by 4 lines the local DELTA=0 run does not cover.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "spec_asserts": "TO-DB-b-41: the returns output must not change by a byte (DELTA=0); the round-22 packet's precondition 1 lists three pins (account_class_daily.py, the class client, sources.json) and no re-pin of account_return_daily.py.",
  "world_is": "The source map entry irpt-49f-reporting-gold-lambda pins data/assets/scripts/gold/irpt_reporting/account_return_daily.py at bc50d5711e with sha256 cb38fe16f002a1cf5a07ddd704f01a6992528bbec04f2486e13dca3e6b734529. The file at this branch's HEAD has sha256 9935f5c7bcd7bd9ca071ae7b7a672a49a5d96fcb0cd7d558c9fc3bc49157fc19: commit ba544b6064 (TO-DB-b-40, round 25) changed classify_and_sum (the _final column held as object and tested with isna; 4 insertions, 3 deletions). The local release run compares the round-25 handler with the extended one over the SAME returns producer (HEAD's), so it shows 0 bytes of change from this cell's handler and declaration, and says nothing about bc50d5711e versus HEAD. The round-25 record (PANDAS_ONCE_E3.md) shows equal output with string inference off, the behaviour of the layer's pandas 2.2.3, which could not be run on this box. The packet names the re-pin as precondition 1 pin 0 and puts DELTA=0 on the served returns in its after-read (A4).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json functions.irpt-49f-reporting-gold-lambda.staged_from[0]",
      "git log bc50d5711e..HEAD -- data/assets/scripts/gold/irpt_reporting/account_return_daily.py -> ba544b6064",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/PANDAS_ONCE_E3.md Controls"
    ]
  },
  "notes": "The deploying lane may keep the old pin (the activity producer then imports the older returns producer) or re-pin; the packet's after-read A4 reads the served T-1 against a local run of the unextended handler either way.",
  "disarm_owner": "2.0.0_SA_COO~D2"
}
```

## IRPT_DASHBD-S31 -- W23-S2 ruled: the release apply waits on a population-scale measurement of the lots stage

```json
{
  "id": "IRPT_DASHBD-S31",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T23:24:36Z",
  "one_line": "W23-S2 disarmed by gating: the COO half of the activity-and-lot release packet is WITHHELD until the lots stage is measured at the 7,597-account population inside the function's 900 s and 2048 MB; the first-fire dry_run sizing in the packet is not accepted in its stead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W23-S2"
  ],
  "spec_asserts": "W23-S2: the lots stage is unmeasured at the 7,597-account population against the 900 s / 2048 MB function; the packet's COO half text accepts the sizing risk for the first fire with a dry_run read.",
  "world_is": "MEASURED by the worker (RELEASE_LOCAL_RUN.json): 20 accounts, one trading day, one process -- unextended handler 34.6 s and 228 MB peak; extended 69.5 s and 992 MB, the lots stage adding about 35 s and about 764 MB. The population is 7,597 accounts (380 x the sample). Nothing measured says the stage fits; a stage that never fits would log LOTS_SKIPPED on every fire and serve nothing. The hazard is live only at the apply, and the apply needs the COO half: the issuer withholds it until a measurement at population scale (one trading day, all 7,597 accounts, wall time and peak memory printed) shows the stage fits, or the stage is split so it does. Routed to 1.0.0_SA_CTO~DELL2 in the round-26 packet as an enrichment for round 27.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.9.0_WK_IRPT_DASHBD~23/RELEASE_LOCAL_RUN.json: wall time and peak memory before and after",
      "deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json: population 7,597",
      "infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf: timeout 900, memory 2048"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S32 -- W23-S6 ruled: the account_return_daily re-pin waits on DB-b-43 (pandas 2.2.3)

```json
{
  "id": "IRPT_DASHBD-S32",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-07T23:24:36Z",
  "one_line": "W23-S6 disarmed by gating: the packet's pin 0 re-pins account_return_daily.py to the round-25 hardening, which DB-b-43 has not yet tested on the served layer's pandas 2.2.3; the COO half is WITHHELD until DB-b-43 passes there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W23-S6"
  ],
  "spec_asserts": "W23-S6: the deployed pin of account_return_daily.py (bc50d5711e) differs from HEAD by the round-25 classify_and_sum change (ba544b6064); the local equality run used HEAD on both sides, so it does not cover the change; the packet adds a re-pin as pin 0.",
  "world_is": "The re-pin would ship classify_and_sum's object-dtype + isna change to the served function, which runs pandas 2.2.3. Its only evidence is the round-25 equality with string inference off on pandas 3.0.6. DB-b-43 (the None test on pandas 2.2.3) could not run on the laptop (pandas 2.3.3, MSTR msg 1136) and runs on dell2 once the approved Python 3.12 kit lands. The issuer withholds the COO half until DB-b-43 passes on 2.2.3; a byte-equality of the returns table under 2.2.3, old pin against new, is added to the after-read before the apply.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json irpt-49f-reporting-gold-lambda pin bc50d5711e",
      "commit ba544b6064",
      "MSTR msg 1136: laptop pandas 2.3.3",
      "decomposition section 26a: DB-b-43"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W26-S1 -- The lots stage refuses at population scale on a repeated realized lot id, after 244.7 s and above the memory limit.

```json
{
  "id": "IRPT_DASHBD-W26-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~26",
  "surfaced_at": "2026-10-08T03:40:17Z",
  "one_line": "At the 49F population the extended handler's lots stage REFUSES on a repeated realized lot id (87 ids, 175 rows, 36 accounts) after 244.7 s and a 2,759.5 MB peak working set: the memory limit is breached by 711.5 MB before the refusal, and the lots tables are not produced.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-46 item 1: run the extended handler's --local for 2026-10-06 over its own population (7,597 accounts) and record wall and peak per stage, with the per-account tail; the producer's realized_rows docstring: a realized lot id is unique on every partition measured, so a repeat is a source change to look at.",
  "world_is": "Measured with the handler and producer unchanged (SIZING_S31.json): returns 122.6 s / 257.8 MB, class 92.7 s / 295.6 MB, lots 244.7 s / 2,759.5 MB (process peak), total 461.1 s / 2,759.5 MB against 900 s / 2048 MB. The lots stage read the 7,597 accounts and classified the flow, then realized_rows raised SystemExit 'realized lot id ... appears twice in one frame' (handler.lots_days caught it: LOTS_SKIPPED, handler.local raised REFUSED). The 2026-10-06 fact_rld partition holds 2,523 rows, 2,435 distinct ids, 87 ids repeated (175 rows, one id three times), 36 accounts, 0 ids across more than one account, 0 rows equal to another in all columns (REALIZED_ID_REPEAT_COUNTS.json). The stage never reached the activity loop, the in-kind step or the writes, so the stage's full wall and peak are unmeasured (not extrapolated) and the memory figure is a floor; the earlier 20- and 100-account local runs did not report it. The timeout is not breached up to the refusal (461.1 s of 900 s). Served on pandas 2.2.3 / Linux; this run is pandas 3.0.6 / Windows working set, so the memory figure is a laptop measure.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/SIZING_S31.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/REALIZED_ID_REPEAT_COUNTS.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/sizing_s31.py",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py realized_rows (the repeat refusal)",
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py lots_days, local"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "With the repeat unresolved, a served fire would spend about 245 s and over 2.7 GB on the lots stage and then skip the three tables each day; the limit of 2048 MB would be crossed in the lots stage. Whether the repeat is a source change to dedupe, to key by another column, or to refuse by design is a producer decision outside this order's paths. The population-scale completion time and peak need a re-run once the repeat is resolved."
}
```

## IRPT_DASHBD-W26-S2 -- The per-account tail of the lots stage is null: the stage is batched and the refusal precedes its only per-account loop.

```json
{
  "id": "IRPT_DASHBD-W26-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~26",
  "surfaced_at": "2026-10-08T03:40:17Z",
  "one_line": "The lots stage has no per-account step to time except the activity row loop, which the refusal prevented from running, so the per-account seconds tail (p50, p95, p99, max) is null in SIZING_S31.json and DB27-2-AC1 FAILs on it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-46 item 1 and 3: record the seconds per account for the lots stage, with per_account_seconds {p50, p95, p99, max}; the criterion DB27-2-AC1 requires all four non-null.",
  "world_is": "compute_local batches its reads, flow classification and unrealized-row build over all accounts at once (read_window 15.2 s, first_data_dates 118.3 s, unrealized_rows 108.9 s, classify_flow_days 1.4 s, realized_rows 0.01 s inside the 244.7 s stage); the only per-account call is activity_row in the final loop, reached after realized_rows, which refused. So no per-account sample exists (per_account_samples 0). The stage's mean is 0.0322 s per account (244.65 s over 7,597), a batch mean and not a tail; the tail is not derived from it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/SIZING_S31.json per_account_samples, lots_substeps_seconds",
      "data/assets/scripts/gold/irpt_reporting/account_activity_lots.py compute_local"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S33 -- W26-S1 gated: lots stage refuses and crosses 2048 MB at population scale

```json
{
  "id": "IRPT_DASHBD-S33",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-08T04:25:43Z",
  "one_line": "W26-S1 gated: the activity-and-lot release stays withheld; the lots stage refuses at population scale on 87 realized lot ids repeated within one day's frame (36 accounts) and peaks at least 2,759.5 MB against 2,048 MB. The key and the memory fit go to 1.0.0_SA_CTO~DELL2 as round-28 work.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "adjudicates": [
    "IRPT_DASHBD-W26-S1"
  ],
  "spec_asserts": "W26-S1: the lots stage of the extended reporting-gold handler refuses at population scale and crosses 2048 MB, so the release as prepared would skip the three tables on every fire.",
  "world_is": "MEASURED (DB-b-46, SIZING_S31.json and REALIZED_ID_REPEAT_COUNTS.json): 7,597 accounts, 2026-10-06; returns 122.57 s / 257.8 MB, class 92.69 s / 295.6 MB, lots 244.65 s to the refusal / 2,759.5 MB peak; total 461.06 s. realized_rows raised on a repeated realized lot id: 2,523 rows, 2,435 distinct ids, 87 ids repeated (175 rows; one thrice), 36 accounts, 0 ids spanning accounts, 0 full-row duplicates. The 20-account sample showed neither. Not live: the release apply is gated on the COO half, which stays withheld (S31, S32, and now this). The remedy is a design call -- the realized lot key and how the lots stage fits in the function -- and goes to the CTO.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.9.0_WK_IRPT_DASHBD~26/SIZING_S31.json",
      "deliverables/0.9.0_WK_IRPT_DASHBD~26/REALIZED_ID_REPEAT_COUNTS.json",
      "commit f70cc737df"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W27-S1 -- The quantity closed alone separates the 175 repeated-id rows; the contract key keeps lot_id because the whole day needs it.

```json
{
  "id": "IRPT_DASHBD-W27-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~27",
  "surfaced_at": "2026-10-08T10:46:26Z",
  "one_line": "Among the 175 repeated-id realized rows the quantity closed alone is already unique (175 of 175), so lot_id is not necessary within those rows; the key is lot_id plus quantity because lot_id is necessary over the whole 2,523-row day.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-47 item 1 and DB28-1-AC1: the smallest column set beginning with the current key under which the 175 rows are unique, with each key column necessary (dropping any one leaves fewer than 175).",
  "world_is": "MEASURED (LOT_KEY_E1.json): over the 175 rows quantity alone separates all 175 (every other table column fewer), so within those rows only quantity is necessary and key_columns is [quantity], its drop leaving the current key at 87 of 175. Over the whole day frame (2,523 rows) dropping lot_id from the contract key (account, date, lot_id, quantity) leaves 2,357 unique, so lot_id stays necessary to the table key and the contract primary_key is the current key plus quantity. The minimality list therefore reports the necessary column within the 175, and the contract key is the wider five-column key.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/LOT_KEY_E1.json columns_of_the_contract_key_each_dropped_one_at_a_time, whole_day_frame"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W27-S2 -- The lots peak is flat across batch sizes (about 1.7 GB): a batch-independent component sets it, and 250 per batch is over 900 s.

```json
{
  "id": "IRPT_DASHBD-W27-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~27",
  "surfaced_at": "2026-10-08T14:07:26Z",
  "one_line": "Batching bounds the lots stage but the peak does not fall with the batch size: 1,713 MB at 250 accounts per batch and 1,735 MB at 1,000, so a component the batch does not shrink sets it; and 250 per batch takes 905.7 s in total, over 900.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-48 item 1: the lots stage processes accounts in bounded batches so its peak memory does not grow with the population; DB28-2-AC1 grades the lots peak flat across two batch sizes (max/min <= 1.25).",
  "world_is": "MEASURED (BATCHED_E2.json, 7,604 accounts, 2026-10-06, pandas 3.0.6 not the served 2.2.3): batch 250 lots 684.61 s / 1,713.4 MB, total 905.67 s; batch 1000 lots 495.54 s / 1,735.3 MB, total 768.91 s; max/min 1.013. Round 27's unbatched run reached at least 2,759.5 MB and refused. The peak is flat across batch sizes, so what sets it was not found to be the batch; the balance-history scan (paid once, population-wide) and the day's partitions are the batch-independent reads in the stage but were not isolated here. Smaller batches cost wall time (31 batches vs 8). The population at run time was 7,604 against the order's 7,597.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/BATCHED_E2.json runs, lots_peak_max_over_min"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S34 -- DB-b-49 recompose control misses on 440 of 2,299: BD's split halves do not chain to BD's own full segment

```json
{
  "id": "IRPT_DASHBD-S34",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-08T17:16:48Z",
  "one_line": "DB-b-49's recompose control does not hold on 440 of 2,299 accounts: BD's two split halves chained do not reproduce BD's own full-segment gross within 0.35 pp (max 724.16 pp), so on those accounts branch B's right-half gap cannot yet be read as Opal-vs-BD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-49 item 3: the recompose control ((1+left)(1+right)-1 against BD's full-segment gross in the round-18 record) shows the two pulls agree with each other.",
  "world_is": "MEASURED (TIEOUT_SPLIT_E1.json recompose): compared 2,299, within 0.35 pp 1,859, not comparable 0, max abs diff 724.16 pp. Branch B stands on the rule (tied_both 431 of 2,299 vs 1,149.5; left half 2,220 tied, right half 465). The 440 disagreeing accounts and the outlier were not examined; whether they overlap the 1,868 right-half misses is unmeasured. Next-round candidate for 1.0.0_SA_CTO~DELL2's round-28 analysis.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json recompose",
      "commit a556d87e79"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W30-S1 -- fee_amount is zero on every served day of the E2 population's right halves

```json
{
  "id": "IRPT_DASHBD-W30-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~30",
  "surfaced_at": "2026-10-08T19:09:34Z",
  "one_line": "fee_amount carries no variance over the 1,528 E2 right halves (every window-day value is 0 or null), so its correlation with the gap is undefined and it is listed under drivers_undefined, not drivers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-51 item 2: record drivers as one {component, corr} per component including fee_amount, corr = Pearson correlation of the per-account fee_amount / first-day market_value_eod with the signed gap.",
  "world_is": "MEASURED (RIGHT_GAP_E2.json statistic, drivers_undefined): the per-account fee_amount sum / first-day market_value_eod takes ONE distinct value (0.0) across all 1,528 accounts, min 0.0 max 0.0, so Pearson is undefined. The check DB29-2-AC2 requires every drivers entry to carry a numeric corr, so fee_amount is recorded in drivers_undefined with its reason rather than as a filled figure; five components remain in drivers (needs >= 3). Whether the gold fee_amount is unpopulated for this firm, or fees are genuinely absent from the served series, was not examined.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~30/RIGHT_GAP_E2.json drivers_undefined"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W30-S2 -- round 18's read_gold fixes its column list; the further components were read by a sibling reader

```json
{
  "id": "IRPT_DASHBD-W30-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~30",
  "surfaced_at": "2026-10-08T19:09:34Z",
  "one_line": "The imported round-18 reader (tieout_e2_gross -> tieout_e2.read_gold) reads a fixed column list without income_received, fee_amount, day_quality or carried_days, so right_gap_e2.py reads the same partitions with those columns and imports only the constants, _num and segment_days.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-51 worker face: round 18's reader of the served series is imported, not restated.",
  "world_is": "MEASURED (tieout_e2.py read_gold, local cols list): the list is account_id, business_date, market_value_eod, external_flow, income_return, total_return_daily, holdings_price_return_reason; the order needs four columns it lacks, and the list is a function-local, so it cannot be extended by import. right_gap_e2.py::read_gold repeats the partition-listing and GET loop (S3 reads only) with the order's columns; bucket, prefix, number coercion and the segment rule come from the import. 566 partitions listed; all 2,238 distinct accounts requested (the union of the 1,528 E2 and 2,220 control sets) have served rows.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py read_gold",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~30/right_gap_e2.py read_gold"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W29-S1 -- 437 of S34's 440 are not a split-pull defect: BD's net returns chain, and the gross gap is round 18's fee add-back being evaluated on a different value basis per range.

```json
{
  "id": "IRPT_DASHBD-W29-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~29",
  "surfaced_at": "2026-10-08T18:30:00Z",
  "one_line": "On 437 of the 440 non-recomposing accounts BD's NET returns chain to BD's full-range NET within 0.35 pp (day counts and held flags agree); the gross gap comes from the round-18 fee add-back fees / ((bmv + emv) / 2), which is not additive across ranges and reaches -8.6 on a closing account with a negative fee.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-27 (round 18) reader: gross = BD net twr + fees / ((bmv + emv) / 2) is a sound gross basis for any range, so halves chained should reproduce the full-range gross (DB-b-49 recompose control).",
  "world_is": "MEASURED (S34_CLASS_E1.json, 880 landed objects re-read): net chain within tolerance on 437 of 440; 3 are over tolerance on net (0.40 to 0.45 pp) with near-zero opening values; 18 have ending value 0 on the full range (denominator is half the opening value); 30 carry a negative fee on a point; the 724.16 pp outlier has fees -175.99 on a left half with bmv 40.69 / emv 219.04 (add-back -1.36) and -174.9 on the full range with emv 0 (add-back -8.60). The gross basis therefore cannot be compared across ranges of different length on small or closing balances. Not examined: how many of the 9,078 round-18 segments outside S34 carry the same distortion within tolerance.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~29/S34_CLASS_E1.json counts, outlier, sub_counts"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W31-S1 -- The one-batch run (batch size 0) ended about 900 s into the lots stage with no record and no cap line.

```json
{
  "id": "IRPT_DASHBD-W31-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~31",
  "surfaced_at": "2026-10-08T20:05:00Z",
  "one_line": "The batch-size-0 run of round 28's runner ended near 900 s into the lots stage at 2,733 MB with no DONE line, no record file and no STOPPED_AT_CAP line; the runner's own cap is 3,600 s, so something else ended the process.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-52 item 1: a run is stopped by the runner at 3,600 s and recorded; every run yields {lots, total} figures.",
  "world_is": "MEASURED: batch 0 over 7,604 accounts: the last PROGRESS line is elapsed 900.4 s, stage lots, working set 2,706.6 MB, peak 2,733.1 MB; no rec file written; the 2,000 and 4,000 runs before it (757.55 s, 813.18 s) and four after it ended normally. Who ended the process was not found (not the runner's watchdog: it writes the record first). The run is entered in LOTS_750_E3.json from its log line only. It could not have met the bar: past 750 s and over the 2,048 MB limit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~31/LOTS_750_E3.json runs[order 3]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W31-S2 -- The same batch size read 757.55 s and 692.81 s: the 750 s bar sits inside the run-to-run spread on this box.

```json
{
  "id": "IRPT_DASHBD-W31-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~31",
  "surfaced_at": "2026-10-08T20:05:00Z",
  "one_line": "Batch size 2,000 gave a total of 757.55 s and then 692.81 s (and the default run, also 2,000, 666.98 s), so a single total near 750 s decides little: the spread at one size is 90 s with two other workers running on the machine.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-52: choose the batch size whose total is <= 750 s; DB29-3-AC2 reads one default run <= 750 s.",
  "world_is": "MEASURED (LOTS_750_E3.json, 7,604 accounts, 2026-10-06, one process at a time, 2 other workers' light analyses on the same 16-core machine): totals at 2,000 per batch 757.55 s, 692.81 s, 666.98 s; 1,500: 627.25 s; 3,000: 707.34 s; 4,000: 813.18 s; round 28's 1,000 read 768.91 s. Lots peak fell from 1,735 MB (1,000) to 1,477 to 1,664 MB (2,000, two runs), so the peak is not monotone in the batch size either. Two of three 2,000 runs are under 750 s; the served Lambda's own wall time at this size was not measured (local, pandas 3.0.6, not the served 2.2.3).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~31/LOTS_750_E3.json runs, default_run"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S35 -- corrects W30-S1: the right-half gap is the tie-out's additive fee add-back (compounded: 1,334 of 1,527 tie)

```json
{
  "id": "IRPT_DASHBD-S35",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T21:17:33Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Corrects IRPT_DASHBD-W30-S1 and this seat's ADJUDICATION_v15 lead: the 1,528 'real misses' are mostly the tie-out's ADDITIVE fee add-back, not Opal vs BD. Compounding BD's add-back ((1+net)(1+add-back)-1) instead of adding it moves the median right-half gap from +0.567 pp to +0.043 pp and the tied count from 0 to 1,334 of 1,527.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json (per-half bd_net_return, bd_fee_addback, bd_return = gross with additive add-back; this seat's computation, dell2, 2026-10-08 ~21:1xZ)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py:27-31 (add-back = fees / ((bmv + emv) / 2), added to BD's net TWR)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py:25 and :1276 (Opal's daily is GROSS by design; fee_amount null with FEE_RAIL_UNUSED)"
    ]
  },
  "spec_asserts": "ADJUDICATION_v15 / REMEDIATION_v13 (W30-S1): Opal's fee_amount is 0 because Opal does not deduct an advisory fee BD deducts; the fix is Opal's fee feed.",
  "world_is": "Wrong on both counts. (1) Opal's account_return_daily is gross of fees BY DESIGN (fee_amount null, reason FEE_RAIL_UNUSED); right_gap_e2 counted the null as 0. There is no broken fee feed. (2) The split tie-out already compares Opal gross to BD gross, where BD gross = BD net TWR + fees/average balance, ADDED. 1,527 of the 1,528 right halves carry an add-back (median 2.388 pp; the halves are long, median 629 days vs 183 for the tied left halves), and the gap is a steady fraction of it (gap/add-back median 0.25, p10 0.15, p90 0.34). An additive add-back omits the fee-times-return interaction over a long, positive period (median BD net 22.7%). Compounding it: median gap +0.043 pp (p10 -0.096, p90 +0.244), within 0.35 pp on 1,334 of 1,527 (was 0). About 193 accounts remain off after the correction."
}
```

## IRPT_DASHBD-W34-S1 -- TO-DB-b-53's chain test cannot hold to 1e-9 with the unchanged linear add-back (fees / average balance); it ho

```json
{
  "id": "IRPT_DASHBD-W34-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~34",
  "surfaced_at": "2026-10-08T22:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "TO-DB-b-53's chain test cannot hold to 1e-9 with the unchanged linear add-back (fees / average balance); it holds only when the range's reported fees are the compounded daily fee drag.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/test_tieout_compound.py (range_inputs docstring; test_compounded_gross_of_adjacent_ranges_chains_to_the_whole, test_additive_gross_does_not_chain)"
    ]
  },
  "spec_asserts": "TO-DB-b-53 item 2: on a synthetic account with constant daily net return and constant daily fee rate, the two halves' compounded gross chained as (1+a)(1+b)-1 equals the whole within 1e-9, with the add-back unchanged.",
  "world_is": "With the add-back fees/((bmv+emv)/2) and fees proportional to days (constant daily fee rate f over N days gives add-back N*f), the chained halves differ from the whole by N1*N2*f^2 (about 3.9e-4 at f=4e-5 daily, 120 and 130 days), far above 1e-9. The test therefore builds the range's reported fees as ((1+f)^N - 1) * average balance, so the unchanged add-back equals the compounded daily fee drag and the compounded gross chains exactly; the additive form then misses by about 5e-4. Consequence: the compounded basis is exact for a fee that accrues geometrically and is a first-order approximation for BD's real linear fee accrual; the residual is of order N1*N2*f^2, which is small against the 0.35 pp tolerance for realistic fee rates."
}
```

## IRPT_DASHBD-W34-S2 -- Compounding the fee add-back moves 2,224 round-18 OUTSIDE segments to WITHIN but also 181 round-18 WITHIN segm

```json
{
  "id": "IRPT_DASHBD-W34-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~34",
  "surfaced_at": "2026-10-08T22:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Compounding the fee add-back moves 2,224 round-18 OUTSIDE segments to WITHIN but also 181 round-18 WITHIN segments to OUTSIDE; FLOW_TIMING outside rises 333 -> 370.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/TIEOUT_COMPOUND_E1.json verdict_moves_vs_round18, before_outside_by_reason, after_outside_by_reason"
    ]
  },
  "spec_asserts": "TO-DB-b-53 / S35: compounding the add-back brings BD gross closer to Opal; the order expected a drop in misses.",
  "world_is": "On the 9,078 graded segments the compounded basis nets 5,416 -> 7,459 within (+2,043): 2,224 OUTSIDE->WITHIN, 181 WITHIN->OUTSIDE, 6,673 unchanged. The 181 reversals are segments the additive form tied by offsetting error; the order does not ask for their cause and it was not measured. After-outside by reason: UNEXPLAINED 1,203 (was 3,279), FLOW_TIMING 370 (333), INCOME_DATE 40 (44), COVERAGE_DAYS 5 (5), MISSING_PRICE 1 (1); the extra FLOW_TIMING rows are newly outside segments whose alternate-flow re-link lands within tolerance."
}
```

## IRPT_DASHBD-W33-S1 -- The dell2 process reaper killed two of this order's runs mid-lots-stage; killed runs are not timings.

```json
{
  "id": "IRPT_DASHBD-W33-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~33",
  "surfaced_at": "2026-10-09T00:11:00Z",
  "one_line": "The dell2 process reaper killed two of this order's runs mid-lots-stage; killed runs are not timings.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-55 item 1: each run is one process that runs to its DONE line or to the runner's 3,600 s cap.",
  "world_is": "MEASURED: run 3 (planned at 2,000) last progress line at 360.0 s, 2026-10-08T21:48:14Z, killed 21:48:23Z; run 13 (at 1,500) last progress line at 630.3 s, killed 22:23:31Z; both in the lots stage, neither wrote a record or a DONE line, neither is the runner's cap. Times per the issuer's ruling (2.0.0_SA_COO~D2, 22:3xZ: the dell2 /govern reaper; now paused). Neither is entered as a timing; both are in LOTS_P95_E3.json interrupted_runs. Completed runs: 2 at 2,000, 5 at 1,500, 5 at 1,000. This worker's own stop of the loop after run 3 found no live process.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~33/LOTS_P95_E3.json interrupted_runs"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W33-S2 -- The 1,500 default failed the p95 bar on spread alone: five completed runs read 655 to 955 s, and 1,000 read 608 to 659 s.

```json
{
  "id": "IRPT_DASHBD-W33-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~33",
  "surfaced_at": "2026-10-09T00:11:00Z",
  "one_line": "The 1,500 default failed the p95 bar on spread alone: five completed runs read 655 to 955 s, and 1,000 read 608 to 659 s.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-55: the default is lowered until p95 of five or more runs is <= 750 s; round 29 read one 1,500 run at 627.25 s.",
  "world_is": "MEASURED (7,604 accounts, 2026-10-06, one process at a time, 16-core box with another worker's light S3 analysis): 2,000: 824.30 s, 835.42 s (two runs, loop stopped by this worker after the second since two runs at that size already forced p95 over 750 s); 1,500: 672.24, 655.47, 955.01, 905.77, 782.71 s (p95 945.16); 1,000: 625.42, 607.93, 608.27, 659.12, 621.07 s (p95 652.38, lots peak max 1,763.4 MB against 2,048). The 1,500 spread (300 s) is larger than any between-size difference, so box load, not batch size alone, moved those runs; the 2,000 runs here are 70 to 140 s slower than round 29's three at the same size. The served Lambda was not measured.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~33/LOTS_P95_E3.json runs"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W35-S1 -- The daily-mean fee base fixes 134 of the 181 crossovers but itself moves 133 segments from WITHIN to OUTSIDE against round 30 (net +629 within).

```json
{
  "id": "IRPT_DASHBD-W35-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~35",
  "surfaced_at": "2026-10-09T01:00:00Z",
  "one_line": "The daily-mean fee base fixes 134 of the 181 crossovers but itself moves 133 segments from WITHIN to OUTSIDE against round 30 (net +629 within).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-57 item 3: the fix is a module that re-grades all 9,078 segments with after_within >= 7,459; the order does not ask whether the fix reverses segments.",
  "world_is": "MEASURED: tieout_compound_v2.py (add-back on the mean served daily market value of the linked days) grades 8,088 within / 990 outside of 9,078; against round 30 it moves 762 OUTSIDE to WITHIN and 133 WITHIN to OUTSIDE, 8,183 unchanged. The 133 reversals are not classed here (not asked). Of the 181 crossovers, 134 return to WITHIN, 47 stay OUTSIDE (23 flow-timing residue, 22 additive-tie coincidence, 2 negative fee total).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json verdict_moves_vs_round30",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/CROSSOVER_E1.json fix_regrade"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W36-S1 -- The fee-base correction (mean daily value) moves 762 segments to WITHIN but 133 round-30 WITHIN segments to OUTSIDE; the average of begin and end value is not the only fee-base reading.

```json
{
  "id": "IRPT_DASHBD-W36-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~36",
  "surfaced_at": "2026-10-09T01:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Re-forming the fee add-back on the mean daily served value moves 762 round-30 OUTSIDE segments to WITHIN and 133 round-30 WITHIN segments to OUTSIDE (net +629, 7,459 -> 8,088 of 9,078).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/UNEXPLAINED_CLASSES_E2.json fix.regrade_all_segments"
    ]
  },
  "spec_asserts": "TO-DB-b-58: a class disposed 'fixed' carries its re-graded effect; round 30's formation (fees / ((bmv + emv) / 2)) is the stated fee base of the tie-out.",
  "world_is": "MEASURED on the 9,078 graded segments, baseline re-derived here and equal to round 30's record (7,459 within): the fee base 'mean daily served value over the linked days' gives 8,088 within; 762 OUTSIDE->WITHIN, 133 WITHIN->OUTSIDE. Of the 1,203 UNEXPLAINED, 618 move to within. The 133 reversals are segments the (bmv + emv) / 2 base tied and the mean-value base does not; their cause was not measured. The fix is a function in a new module (fee_base_gross); the served tie-out and round 30's reader are unchanged and nothing is adopted by assumption."
}
```

## IRPT_DASHBD-W37-S1 -- The 370 FLOW_TIMING misses are the served END convention by construction, so within_flow_end is 0 of 370; two segments read 98 and 172 pp at START.

```json
{
  "id": "IRPT_DASHBD-W37-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~37",
  "surfaced_at": "2026-10-09T01:00:00Z",
  "one_line": "The 370 FLOW_TIMING misses are the served END convention by construction, so within_flow_end is 0 of 370; two segments read 98 and 172 pp at START.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-59: grade the 370 both ways and print the swing; the counts go to the CTO with no convention adopted.",
  "world_is": "MEASURED: the END re-link (round 17 link_alt_flow END) equals the served opal_return on 370 of 370 rows, and the round-30 population is the abs_diff_pp > 0.35 rows at the served convention, so within_flow_end = 0 of 370 and within_flow_start = 337 of 370. START moves 356 rows closer to BD and 14 further. Two segments read 172.33 and 97.92 pp at START against 1.17 and 1.08 at END (swing -171.15 and -96.84): link_alt_flow START divides by V_(t-1) + F_t, which approaches zero when a flow nearly offsets the prior value (MEASURED on both: one day's external flow is -100.59 and -99.97 percent of the prior day's value, so the START denominator is near zero or negative), so those two START figures are a denominator artifact of the reader, not a finding about BD. Nothing was filled or adopted; both are in the record as computed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~37/FLOW_TIMING_E3.json rows"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W39-S1 -- 26 of the 170 LARGE_FLOW_DAY misses carry BD fees equal to minus netAdditions; the add-back and the TWR are of a flow

```json
{
  "id": "IRPT_DASHBD-W39-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~39",
  "surfaced_at": "2026-10-09T02:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "26 of the 170 LARGE_FLOW_DAY misses are not a large-flow valuation: BD's fees field equals minus its netAdditions and the money gain is about zero, so the fee add-back and the TWR are both of a flow.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/LARGE_FLOW_E3.json rows sub_class BD_FEE_FIELD_IS_FLOW and counts"
    ]
  },
  "spec_asserts": "TO-DB-b-62: the 170 are LARGE_FLOW_DAY, a flow of at least 25% of the prior day's value sets the segment's return and BD's per-flow valuation is not in the landed period point.",
  "world_is": "MEASURED on the 170: for 26 rows BD fees is negative and equals minus netAdditions to within a dollar or 0.2%, and ending - beginning - netAdditions is about zero (cash-only or sweep accounts: Opal's linked return is 0.0000 to 0.19), while BD's TWR reads -0.34 to 2.15. The fee add-back (fees / mean daily value) is then an add-back of the contribution, not of a fee, which is why round 31's classifier reached these only at the large-flow step. Grading them on BD's own landed gain over the mean daily value lands 23 of the 26 within 0.35 pp (module large_flow_e3.py, landed_gain_return); nothing is adopted into the reader of record, and the other 144 are not a fee-field effect. Whether the 26 also appear among round 31's FEE_ADDBACK_NOT_APPLICABLE or the 9,078 outside the 170 was not measured."
}
```

## IRPT_DASHBD-W38-S1 -- Round 31's classifier (~36) and the reader of record (~35's v2) form the daily mean differently: ~36 keeps negative daily values, v2 keeps positives only; 8 segments hold a negative value.

```json
{
  "id": "IRPT_DASHBD-W38-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~38",
  "surfaced_at": "2026-10-09T02:00:00Z",
  "one_line": "~36's mean_daily_value keeps negative daily values, v2's daily_mean_value keeps positives only; making ~36 import v2's base unchanged moves its record (evidence strings, 8 segments).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-60: ~35's v2 and ~36's classifier agree on the daily-mean fee base; ~36 can import it, defining none of the five names, with its output unchanged.",
  "world_is": "MEASURED: the two means are not the same function. mean_daily_value (~36) averages every non-zero served market_value_eod; daily_mean_value (v2) averages the positive ones. They differ on the 8 of 9,082 planned segments whose served days hold a negative value. A first run of ~36 importing v2's function unchanged rewrote UNEXPLAINED_CLASSES_E2.json (evidence strings of 6 rows: mean value and the abs_diff figures; cause classes of the rows shown unchanged). The reader of record therefore carries a flag, daily_mean_value(days, positive_only=True) and fee_base_gross(..., positive_only=True); ~36 binds both with positive_only=False (functools.partial), and its JSON and MD re-run byte-identical. The grading of record (v2, positive_only=True) is the 8,088; whether the negative-value segments should average positives only is a question for the CTO, not decided here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py daily_mean_value",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~36/unexplained_classes.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W38-S2 -- The criteria bind REGRADE_E1.json's reader_sha256 to the reader at HEAD, but DB-b-61 edits the reader after DB-b-60 commits; REGRADE_E1.json was regenerated under the final reader.

```json
{
  "id": "IRPT_DASHBD-W38-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~38",
  "surfaced_at": "2026-10-09T01:08:00Z",
  "one_line": "DB32-1-AC2 and DB32-2-AC2 both require REGRADE_E1.json's reader_sha256 to equal the reader's bytes at HEAD, while DB-b-61 must edit the reader (FLOW_CONVENTION) after DB-b-60 commits.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-60/61: REGRADE_E1.json carries reader_sha256 = sha256 of tieout_reader.py at the DB-b-60 commit; the checks p32_round32.py DB32-1-AC2 and DB32-2-AC2 compare it with the reader at HEAD.",
  "world_is": "MEASURED: DB-b-61 changes tieout_reader.py (FLOW_CONVENTION = \"start\", the guard), so the sha recorded at the DB-b-60 commit (096c2a2f76) no longer equals HEAD's, and DB32-1-AC2 and DB32-2-AC2 (which reads REGRADE_E1.json through the same sha limb) would FAIL at the DB-b-61 commit. REGRADE_E1.json was therefore regenerated with the final reader (--flow end, the reader's explicit end-of-day option): 9,078 segments, within 8,088, byte-identical grades; only reader_sha256 differs from the DB-b-60 commit's copy. All four criteria print PASS at the DB-b-61 commit. The DB-b-60 proof's recorded outputs are the values at 096c2a2f76.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py regrade()"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W38-S3 -- The flow-start near-zero guard threshold (2%) was chosen from the project's existing near-zero boundary after 1% let two 97 and 117 pp artifacts through; within moves 8,310 to 8,319 across 1% to 10%.

```json
{
  "id": "IRPT_DASHBD-W38-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~38",
  "surfaced_at": "2026-10-09T01:08:30Z",
  "one_line": "A first guard at 1% of the prior value missed two segments (flow -98.9% of the prior value, denominator 1.05% and 1.07%) that read 117 and 97 pp at flow-start; the guard is 2%.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-61: guard the near-zero START divisor with a stated rule, never a silent fill.",
  "world_is": "MEASURED on the 9,078: the rule is V_(t-1) + F_t >= GUARD_FRAC * |V_(t-1)|, else the day keeps its served return and is counted (guard_days). At 1% the guard covered 491 days and two segments still read 116.5 and 97.4 pp (denominator 1.07% and 1.05% of the prior value, end value about 0.1% of it). GUARD_FRAC = 2% is round 31's NEAR_ZERO_BOUNDARY (unexplained_classes.py); it covers 533 days in 446 segments. Sensitivity of the within count: 1% 8,310; 2% 8,315; 5% 8,315; 10% 8,319. The threshold is a convention of this reader, not a measurement of BD; the CTO may re-set it, the number is a module constant.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py guarded_days",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~38/REGRADE_FLOWSTART_E2.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W42-S1 -- Round 32's large_flow_e3.py calls a name (uc.mean_daily_value) that the reader promotion removed; it cannot be re-run as committed.

```json
{
  "id": "IRPT_DASHBD-W42-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~42",
  "surfaced_at": "2026-10-09T01:35:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Round 32's record module large_flow_e3.py no longer runs as committed: its classify calls uc.mean_daily_value, a name round 32's reader promotion removed from the round 31 module.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py classify (uc.mean_daily_value, landed_gain_return)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/NEAR_ZERO_E3.json overlap_round32.shim"
    ]
  },
  "spec_asserts": "TO-DB-b-65 names round 32's records as read-only sources; DB-b-62's module is the record of how LARGE_FLOW_E3.json was produced and is expected to be re-runnable.",
  "world_is": "MEASURED: calling large_flow_e3.classify raises AttributeError: module 'unexplained_classes_r31' has no attribute 'mean_daily_value' (W38-S1's reader promotion rebound the round 31 module's names to functools.partial(reader.daily_mean_value, positive_only=False) as daily_mean_value and dropped mean_daily_value). The committed LARGE_FLOW_E3.json predates that. Worker ~42 imports the module read-only and sets uc.mean_daily_value = uc.daily_mean_value in its own process (stated in NEAR_ZERO_E3.json overlap_round32.shim); control: classify re-run on round 32's own 170 rows reproduces its recorded counts exactly (10 classes, 170 of 170). No file of round 32 was edited; the same one-line alias in large_flow_e3.py would restore its re-runnability and is the CTO's or the issuer's to order."
}
```

## IRPT_DASHBD-W40-S1 -- Two earlier modules no longer run at HEAD: ~39 large_flow_e3.py and ~35 crossover_e1.py call a fee-base name that round 32's promotion to the reader removed from their namespace.

```json
{
  "id": "IRPT_DASHBD-W40-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~40",
  "surfaced_at": "2026-10-09T01:37:00Z",
  "one_line": "Two earlier modules no longer run at HEAD: ~39 large_flow_e3.py and ~35 crossover_e1.py call a fee-base name that round 32's promotion to the reader removed from their namespace.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-63: port the two rules from ~39's module; the ~35 and ~36 importers still run unchanged.",
  "world_is": "MEASURED: large_flow_e3.py line 117 and 279 call uc.mean_daily_value, which unexplained_classes.py defined before 096c2a2f76 and no longer does (only daily_mean_value, a functools.partial of the reader's); large_flow_e3.py therefore raises AttributeError at HEAD. crossover_e1.py calls v2.daily_mean_value , which tieout_compound_v2.py no longer defines after the promotion; it raises AttributeError at HEAD, before and after this task order's edit (the edit touches neither name). tieout_compound_v2.py and unexplained_classes.py DO run and re-write byte-identical records. The ~39 rules were ported from its source; the reader uses its one daily_mean_value (positive values) where ~39 used the pre-promotion non-zero mean, and the 26 BD_FEE_FIELD_IS_FLOW segments grade 23 within, the count round 32 recorded.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/crossover_e1.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W40-S2 -- FIRST_DAY_FLOW_AT_START is gated here on a structural predicate, not on ~39's landing-within-tolerance test; it fires on 144 segments, ties 15 more and loses 14.

```json
{
  "id": "IRPT_DASHBD-W40-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~40",
  "surfaced_at": "2026-10-09T01:37:30Z",
  "one_line": "FIRST_DAY_FLOW_AT_START is gated here on a structural predicate, not on ~39's landing-within-tolerance test; it fires on 144 segments, ties 15 more and loses 14.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-63: gate each fix by a predicate stated in the code; ~39 recorded 4 segments, 4 tie.",
  "world_is": "MEASURED on the 9,078: ~39's test for the class was 'the largest flow is on the first day AND START on that day lands within 0.35 pp of BD', a test on BD's own figure, which would make those segments within by selection. The reader's predicate is structural: the first day's flow is at least 25% of the served value just before the segment and the START denominator clears the 2% guard. It fires on 144 segments: the 4 of round 32 all tie; 96 stay within; 15 more move OUTSIDE to WITHIN; 14 move WITHIN to OUTSIDE (the in_to_out list, reason FIRST_DAY_START_NOT_BD: BD does not land on START timing for those segments). Net +1 from this rule. Adding ~39's 'no later day holds a larger large flow' lowered within by 4 and in_to_out by 2, and was not kept. The CTO may re-set the predicate; the cost of the outcome-gated form is that the grade is no longer a test on those segments.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py first_day_flow_start",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~40/REGRADE_FIXES_E1.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W40-S3 -- BD_FEE_FIELD_IS_FLOW fires on 85 segments of the 9,078, not the 26 round 32 found in the large-flow class; 69 move OUTSIDE to WITHIN and none move the other way.

```json
{
  "id": "IRPT_DASHBD-W40-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~40",
  "surfaced_at": "2026-10-09T01:38:00Z",
  "one_line": "BD_FEE_FIELD_IS_FLOW fires on 85 segments of the 9,078, not the 26 round 32 found in the large-flow class; 69 move OUTSIDE to WITHIN and none move the other way.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-63: the fix is gated by a stated predicate; ~39 found 26 segments, 23 tie.",
  "world_is": "MEASURED on the 9,078: the predicate (fees negative and equal to minus netAdditions within the larger of 1.00 and 0.2% of netAdditions) was written for the 170 large-flow misses; applied to the whole population it fires on 85 segments (the 26 plus 59 elsewhere). Against round 32's flow-start re-grade: 69 OUTSIDE to WITHIN, 11 stay within, 5 stay outside, 0 WITHIN to OUTSIDE. The reader grades such a segment on BD's landed gain over the mean daily value against the reader's own (flow-start) Opal link. The 59 outside the large-flow class are a finding of this re-grade, not of round 32.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~40/REGRADE_FIXES_E1.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S36 -- round 33 near-zero classes ran on a shim that substitutes a different mean under the old name

```json
{
  "id": "IRPT_DASHBD-S36",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T01:46:14Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Round 33's near-zero classes (DB-b-65: 79 of 153 'fixed') ran through a shim that rebinds uc.mean_daily_value := uc.daily_mean_value, but W38-S1 MEASURED those as different functions (mean_daily_value averages every non-zero daily value, daily_mean_value only the positive ones). So DB-b-65's E3 counts rest on a substituted fee base, not the one round 31's classifier defined.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/near_zero_e3.py:189-193 (the shim) and NEAR_ZERO_E3.json:1572 (records it as applied)",
      "investigation row IRPT_DASHBD-W38-S1 (INVESTIGATION_v1.md ~:3224-3228: 'the two means are not the same function')",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py:117 and :279 still call uc.mean_daily_value (this seat's comp-find, 22 hits over the project)"
    ]
  },
  "spec_asserts": "A record module's numbers are produced by the function it names; a missing name is repaired at its import, not substituted by a different function under the old name.",
  "world_is": "Nothing served moves (the tie-out is project-owned). The effect on DB-b-65's 79 is unmeasured: the shim only changes accounts with negative daily values in the window, and near-zero-balance accounts are exactly where those occur. Re-run E3 with round 31's own mean (or the reader's, under its own name) inside the same repair cell as W40-S1/W42-S1."
}
```

## IRPT_DASHBD-W43-S1 -- The round 33 shim never reached the near-zero classification: it fed only the cross-tab against round 32's classify, so the shim-free re-run leaves the 153 rows, the 79 fixed and every ~35/~36/~39 record unchanged.

```json
{
  "id": "IRPT_DASHBD-W43-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~43",
  "surfaced_at": "2026-10-09T02:03:07Z",
  "one_line": "The round 33 shim never reached the near-zero classification: it fed only the cross-tab against round 32's classify, so the shim-free re-run leaves the 153 rows, the 79 fixed and every ~35/~36/~39 record unchanged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-66 / row S36: DB-b-65's 79 fixed rests on a substituted fee base and is not counted until a shim-free re-run; the re-run is expected to change records only where the shim was wrong.",
  "world_is": "MEASURED shim-free on the 153: near_zero_e3.py's own classify and landed_gain_return call the reader of record's daily_mean_value (positive_only=True) directly, so the shim (which rebinds a name only round 32's large_flow_e3.classify read) never touched them. The shim-free run gives the same 153 rows in the same sub-classes as NEAR_ZERO_E3.json, fixed_within 79 of 79, and round 32's classify reproduces its recorded 170-row counts with the reader's daily_mean_value at positive_only=False. Re-running the ~36, ~39 and ~35 modules on the same read of S3: all six output files byte-identical. Tie-out: the reader alone grades 8,385 of 9,078 within, 31 of them among the 153 (the BD_FEE_FIELD_IS_FLOW rule the reader adopted in round 33); with the 48 GAIN_AGREES_NEAR_ZERO_BASE rows graded on landed gain the total is 8,433, not 8,385 plus 79.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~43/NEAR_ZERO_SHIMFREE_E1.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/near_zero_e3.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W44-S1 -- The offline kit installs but cannot run the round 30 runner: it packages no psutil and no boto3, which the runner and the handler's --local mode import.

```json
{
  "id": "IRPT_DASHBD-W44-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~44",
  "surfaced_at": "2026-10-09T02:23:25Z",
  "one_line": "The offline kit installs but cannot run the round 30 runner: it packages no psutil and no boto3, which the runner and the handler's --local mode import.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-67 step 1-2: the kit (7 wheels: numpy, pandas, pyarrow, dateutil, pytz, six, tzdata) installed offline into a py312 venv is enough to run lots_750_run.py default over the handler's --local mode.",
  "world_is": "MEASURED: the offline install succeeded (no wheel missing), but batched_e2_run.py imports psutil and handler.local imports boto3/botocore (S3 reads of the run's inputs), and neither is in the kit or the venv. Resolved without any network: copied boto3, botocore, s3transfer, jmespath, urllib3 and psutil from dell2's own user site-packages (Python312, Roaming) into .scratch/sidepkgs and added a .pth file to the venv; pandas, numpy and pyarrow stay the kit's (the run's own process prints 3.12.10 / 2.2.3 / 1.26.4 / 14.0.2). These side packages are not the measured libraries; their resident size is part of the baseline in every earlier round's runs too. The next kit should list psutil, boto3 and their dependencies, or the order should say the venv takes them from the box.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/batched_e2_run.py:31 (import psutil is inside main; handler.local imports boto3 at infra/aws/lambda/investor-reporting/reporting-gold/handler.py:591)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~44/kit_run.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W46-S1 -- DB-b-43's test (test_account_return_daily_none.py) fails 4 of 4 on the pandas 2.2.3 kit because it forces future.infer_string ON, a mode pandas 2.2.3 only half supports; the same four pass on the kit with the option left off and on pandas 3.0.6, so criterion DB35-1-AC1 (db_b_43_test passed > 0, failed == 0) cannot be met as written.

```json
{
  "id": "IRPT_DASHBD-W46-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~46",
  "surfaced_at": "2026-10-09T03:02:00Z",
  "one_line": "DB-b-43's test fails 4 of 4 on the pandas 2.2.3 kit (it forces future.infer_string ON; pandas 2.2.3's pyarrow-string str.contains rejects the compiled INCOME_CATEGORY_RE), passes 4 of 4 on pandas 3.0.6 and 4 of 4 on the kit with the option left off.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-69 step 1 and DB35-1-AC1: DB-b-43's test data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py on the kit is recorded with passed > 0 and failed == 0 (the S32 read the CTO's round-34 ADDENDUM 3 asks the packet to carry).",
  "world_is": "MEASURED, one process each: on the kit (Python 3.12.10, pandas 2.2.3, numpy 1.26.4, pyarrow 14.0.2) `python -m pytest` on that file gives 4 failed, 0 passed, every failure `TypeError: expected bytes, re.Pattern found` raised at account_return_daily.py:720 (`t[\"_category\"].str.contains(INCOME_CATEGORY_RE, na=False)`) through pandas/core/arrays/string_arrow.py:359 `pc.match_substring_regex(...)`. The test's run() calls pd.set_option('future.infer_string', True) whenever the option exists, which on 2.2.3 turns the column into the experimental pyarrow-backed string dtype; that dtype's str.contains hands the compiled pattern to pyarrow. On the tested version (Python 3.14.7, pandas 3.0.6) the same file gives 4 passed. With the option left at the kit's own default (off, the served setting that account_activity_lots.set_served_runtime() holds) the four test bodies, run through deliverables/0.9.0_WK_IRPT_DASHBD~46/s32_db43_option_off.py, give 4 passed, 0 failed; the full kit run (batch 1000, 7,604 accounts) logs `future.infer_string = False (served behaviour in force: True)` and completes with 0 refusals; and classify_and_sum on three real custodian days is equal between the kit and pandas 3.0.6 (S32_READ_E1.json). So the producer is not shown wrong on the kit; the test, as written, exercises a pandas-3 mode that the served runtime never enters, and cannot pass on 2.2.3. The record carries passed 0 / failed 4 as measured, so DB35-1-AC1 prints FAIL and the order stays open. No file under data/ was edited (outside the grant). The CTO or the issuer decides whether the S32 read accepts the option-off run as the kit evidence or the test is amended to skip the forced-ON arm where pandas < 3.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py:66-71 (run() sets future.infer_string to the argument whenever the option exists)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py:720",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/S32_READ_E1.json (db_b_43_test, db_b_43_test_option_off, db_b_43_test_tested_version)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/s32_db43_option_off.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W46-S2 -- The kit carries no pytest, so DB-b-43's test cannot run on it without a side-load; pytest and its pure-Python dependencies were copied from dell2's own site-packages, offline.

```json
{
  "id": "IRPT_DASHBD-W46-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~46",
  "surfaced_at": "2026-10-09T03:02:30Z",
  "one_line": "The kit packages no pytest, which DB-b-43's test imports; pytest, _pytest, pluggy, iniconfig, packaging, colorama, pygments and py.py were side-loaded from dell2's Roaming site-packages through a second .pth file, offline.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-69 step 1: DB-b-43's test is run on the kit (the venv built from the kit's wheels plus the boto3 and psutil side-load of row W44-S1).",
  "world_is": "MEASURED: the test file imports pytest at its line 15 and the kit venv has none (`No module named 'pytest'`). Copied, with no network, from C:/Users/Test/AppData/Roaming/Python/Python312/site-packages into .scratch/testpkgs and added by a .pth file: pytest 9.0.2, _pytest, pluggy, iniconfig, packaging, colorama, pygments, py.py. They are the test runner only; pandas, numpy and pyarrow under test are the kit's (the failing run prints them from its own traceback paths: .scratch/kitvenv/Lib/site-packages/pandas, pyarrow). The next kit order should list pytest and its dependencies, or say the venv takes them from the box.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py:15",
      "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_DASHBD-W44-S1 (the same gap for boto3 and psutil)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-S37 -- Row W23-S1's open read: the silver bucket admits the role on the three lot-table prefixes (no read Deny, SSE-S3, same account).

```json
{
  "id": "IRPT_DASHBD-S37",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~D2",
  "surfaced_at": "2026-10-09T03:24:00Z",
  "one_line": "Row W23-S1's open read: the silver bucket opal-data-assets admits the reporting-gold role on the three added lot-table prefixes; its policy carries no read Deny and its encryption is SSE-S3, so the role's own grant governs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The R35 packet's Unmeasured (row W23-S1) and the CTO half's condition (1.0.0_SA_CTO~DELL2 msg 2286): whether the silver bucket's own policy admits the role on fact_rld, fact_uln and fact_ult is read before the apply.",
  "world_is": "MEASURED 2026-10-09 ~03:23Z, s3api get-bucket-policy opal-data-assets: 2 statements. DenyParquetUnderBronze17a denies s3:PutObject of */bronze/*.parquet only. AllowMdpfPortalCloudFrontOACRead allows the CloudFront service GetObject on one json key. Neither denies GetObject or ListBucket to a principal of this account. get-bucket-encryption: AES256 (no KMS key policy in the path). The caller account is 313476888478, the account the role lives in, so the role's identity grant alone decides the read. A Branch-B AccessDenied on a lot read can therefore only come from the role policy, which after-read A5 prints.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-policy --bucket opal-data-assets (2 statements, read 2026-10-09 ~03:23Z)",
      "aws s3api get-bucket-encryption --bucket opal-data-assets (AES256)",
      "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_DASHBD-W23-S1"
    ]
  },
  "notes": "Resolves the open read of IRPT_DASHBD-W23-S1. The bucket policy is live state at the read time; a later policy edit is not covered.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W49-S1 -- The registry has no custody master or bindings for the Orion source, so the adapter's declaration carries no registry_key and the run takes it on the command line; the firm's own bucket holds only irpt/ while its Orion data sits in the routed legacy alias.

```json
{
  "id": "IRPT_DASHBD-W49-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~49",
  "surfaced_at": "2026-10-09T04:14:00Z",
  "one_line": "The registry has no custody master or bindings for the Orion source, so the adapter's declaration carries no registry_key and the run takes it on the command line; the firm's own bucket holds only irpt/ while its Orion data sits in the routed legacy alias.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-72: the adapter resolves its firm and addresses from the registry; the 49 Financial declaration carries a registry_key naming a custody MASTER row.",
  "world_is": "MEASURED 2026-10-09 ~04:0xZ: lookup of the firm key returns class FIRM with bucket_provisioned true and bindings aua_source/model_source/fee_scope/delivery_cadence all null; no MASTER row exists for the Orion/Fidelity custody. A listing of the registry bucket shows one prefix (irpt/); the Orion silver (api_dims positions_mv, performance, transactions, eclipse) and gold are in the bucket the entry's alias list names (plane bucket, routed true, lookup false). So orion_sources.json has no registry_key field (the naming gate refuses a typed firm token), the script takes --registry-key, and the bucket is derived from the alias. NEEDED, NOT ADDED (registry is outside the grant): a scopes.json MASTER row for the Orion/Fidelity custody carrying the firm and vendor, so a declaration can name it as 49 Financial's does, and a decision on whether the reporting-gold home for this firm is the provisioned firm bucket (irpt/ only) or the routed alias.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/scopes.json (firm entry: bucket_provisioned true, bindings null, aliases with routed bucket)",
      "lib/opal_naming.py lookup of the firm key, and an S3 list of the registry bucket (prefix irpt/ only) and of the routed alias (silver/, gold/, bronze/)",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/orion_sources.json (doc field)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W49-S2 -- The reported source is NET of fees and the contract's total_return_daily is GROSS: the contract-literal tie-out is 24 of 562 account-windows within 0.35 pp, and the same inputs with the fee left inside the return are 421 of 562.

```json
{
  "id": "IRPT_DASHBD-W49-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~49",
  "surfaced_at": "2026-10-09T04:14:00Z",
  "one_line": "The reported source is NET of fees and the contract's total_return_daily is GROSS: the contract-literal tie-out is 24 of 562 account-windows within 0.35 pp, and the same inputs with the fee left inside the return are 421 of 562.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-72: our total_return_daily compounded over the source's window ties to its reported return at 0.35 pp, each firm against its own reported source (PRD v0.8 @3eb7dbcf36).",
  "world_is": "MEASURED: silver api_dims performance at snapshot 2026-10-08 reports twr_calc_method TWR, twr_tax_method Before-Tax, twr_fee_method Net of Fees, twr_annualized Annualized, window Rolling 3-Year, for 562 of 927 accounts. The contract (account_return_daily, C-FEERAIL) is gross of advisory fees with fee_amount null. Gross basis: 24 of 562 within 0.35 pp; 400 misses are class FEE_BASIS_GROSS_VS_NET (the net recomputation is within tolerance). Net basis: 421 of 562 (median gap 0.11 pp over the 483 computable windows). The record carries both. NEEDED: a ruling on whether C-TIEOUT for this firm compares on the source's fee basis (the net recomputation) or on the contract's gross basis with the fee difference classed, as this cell did.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (within, net_basis, class_counts)",
      "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json (fee_amount_reason FEE_RAIL_UNUSED)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W49-S3 -- Two flow classes depart from the firm's ratified cashflow taxonomy and were chosen by measurement: Internal Account Journal In/Out and Federal/State Tax Withheld enter F_t as boundary-crossing flows.

```json
{
  "id": "IRPT_DASHBD-W49-S3",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~49",
  "surfaced_at": "2026-10-09T04:14:00Z",
  "one_line": "Two flow classes depart from the firm's ratified cashflow taxonomy and were chosen by measurement: Internal Account Journal In/Out and Federal/State Tax Withheld enter F_t as boundary-crossing flows.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "data/inf/scripts/silver/orion_cashflow_taxonomy.yaml v2: the journal pair is INTERNAL (ratified, intra-account) and the tax-withheld types are RETURN (CTO Item 2).",
  "world_is": "MEASURED on the 562-window sample, net-of-fee basis, 0.35 pp: contributions and distributions only, 285 within (calendar-day/365 annualisation); adding the journal pair, 339; adding Federal and State Tax Withheld as outflows, 413 (293, 348, 421 under the declared trading-day/252 one). A journal leaves one account and arrives in another, so at account grain it crosses the boundary (the 49 Financial producer's own inter-account rule); withholding is cash taken from a client's distribution. The taxonomy governs NNA and is unchanged; the departure lives only in orion_sources.json (inter_account_comment, tax_withheld_comment) and is reproducible from flow_set_probe in the record. NEEDED: the CTO's word on whether the return adapter may differ from the NNA taxonomy on these two classes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (flow_set_probe)",
      "data/inf/scripts/silver/orion_cashflow_taxonomy.yaml (Internal Account Journal In/Out; Federal/State Tax Withheld)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W49-S4 -- No Eclipse tax lot rows are landed anywhere the firm's S3 holds Eclipse data, so every sampled account is NO_LOTS; the lot rows that do exist are the firm's own FIFO lots derived from transactions and are not Eclipse tax lots.

```json
{
  "id": "IRPT_DASHBD-W49-S4",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~49",
  "surfaced_at": "2026-10-09T04:14:00Z",
  "one_line": "No Eclipse tax lot rows are landed anywhere the firm's S3 holds Eclipse data, so every sampled account is NO_LOTS; the lot rows that do exist are the firm's own FIFO lots derived from transactions and are not Eclipse tax lots.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-72 / ADDENDUM 4 E3: lots_status is POPULATED only where Eclipse tax lots are SHOWN populated for the account (rows read, with a count).",
  "world_is": "MEASURED 2026-10-09: the four Eclipse tables silver lands for the 2026-10-08 snapshot (model_composition 9 rows, models 18, portfolios_full 863, portfolios_simple 846) carry no lot-shaped column (0 of 169 columns); the 13 bronze Eclipse objects for the snapshot carry no lot-shaped name. The Eclipse catalog lists GET /v1/holding/holdings/{id}/taxlots, but no pull of it is landed. Census: NO_LOTS for 562 of 562 sampled accounts. For context only, gold/lots (built by the firm's FIFO script from transactions) holds 46,415 rows for 489 of the 562 accounts; it is derived, not Eclipse, and promotes nothing. NEEDED to reach POPULATED: a landed Eclipse taxlot pull per holding; not built here (a vendor call and an S3 write are outside the grant).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (lots_evidence)",
      "data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md line 345",
      "data/inf/scripts/gold/INF_B_02.canonical_lots.py (docstring: FIFO from Orion TRN silver)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W49-S5 -- The source reports a return for 562 of its 927 accounts, all over one Rolling 3-Year window starting 2023-10-09 and annualised with a year-count the vendor does not state; 79 of the 562 hold zero value for part of the window, so their link breaks.

```json
{
  "id": "IRPT_DASHBD-W49-S5",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~49",
  "surfaced_at": "2026-10-09T04:14:00Z",
  "one_line": "The source reports a return for 562 of its 927 accounts, all over one Rolling 3-Year window starting 2023-10-09 and annualised with a year-count the vendor does not state; 79 of the 562 hold zero value for part of the window, so their link breaks.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-72: the comparison source's own window and a reported return per sampled account.",
  "world_is": "MEASURED: twr_value is null for 365 of 927 accounts at the snapshot (their window starts run from 2023-10-11 to 2026-10-07, every one after the common 2023-10-09 start); the 562 with a value all start 2023-10-09 and end 2026-10-08 (752 trading days). The vendor states Annualized but no day-count; three conventions were tried on the same sample (net-basis within 413, 414, 421; gross 24 each) and trading-day/252 is declared as a HELD reading chosen by fit. 79 of the 562 hold a position value of zero for part of the window (accounts liquidated or emptied), so their daily link breaks and they are classed LINK_BROKEN_NO_BASE rather than compared. The sample is therefore a 3-year annualised view of mature accounts, not a short-window one. NEEDED: whether a second, shorter reported window exists in an earlier landed performance partition (the partitions since 2026-04-28 were not read beyond the latest snapshot).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (sample, annualisation_probe, class_counts)",
      "silver api_dims performance snapshot_date=2026-10-08 (927 rows, 562 with twr_value)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W48-S1 -- No Commonwealth-reported window overlaps the Black Diamond source's value coverage for the same account, so Co

```json
{
  "id": "IRPT_DASHBD-W48-S1",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~48",
  "surfaced_at": "2026-10-09T04:05:00Z",
  "one_line": "No Commonwealth-reported window overlaps the Black Diamond source's value coverage for the same account, so Cottonwood's tie-out is 0 of 61 account-windows, every miss structural and none an arithmetic disagreement.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-71: a sample window over at least 10 accounts is compounded from the adapter's total_return_daily and compared with the reported return for the same account and window at 0.35 pp (PRD v0.8 FWD-11, C-TIEOUT).",
  "world_is": "MEASURED 2026-10-09 ~04:0xZ by reading S3 only. The reported source EXISTS on S3: the Commonwealth delivery dated 2026-06-23, silver performance table (Month, Year, InceptionToDate; TWR, PerfNum in percent, 1,519 accounts) and its crosswalk (471 of 1,533 accounts MATCHED to a current custody account by rule R2-in-kind-transfer; 1,062 NOT_MATCHED). The source the adapter reads (Black Diamond silver fact_holdings) holds value from partition 2026-06-09 only (89 partitions to 2026-10-07; 980 accounts); fact_unrealized reaches back to 2026-04-22 but holds lot value without cash, so it is not a whole-account value. The Commonwealth delivery's last window ends 2026-06-23 and the only windows ending on or after 2026-06-01 are month-to-date rows starting 2026-06-01 (190 rows, 61 of them for MATCHED accounts). Every one of the 61 starts before the source can supply a base value: 28 end before 2026-06-09 (no source value in the window), 33 end 2026-06-09 or later but their base day precedes the first partition (20 of the 61 windows hold source rows on some of their trading days, but a part-window figure is not the reported window). within = 0, denominator = 61, accounts = 61; the 61 misses carry the classes WINDOW_ENDS_BEFORE_SOURCE_COVERAGE (28) and WINDOW_STARTS_BEFORE_SOURCE_BASE (33). The 0-of-61 therefore says nothing for or against the adapter's arithmetic; Closing this needs either Black Diamond history before 2026-06-09 that includes cash, or a Commonwealth window that starts after 2026-06-09, and the delivery holds neither.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/COT_RETURNS_TIEOUT.json",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/tieout.py",
      "infra/logic/registry/scopes.json (key z09, class MASTER)"
    ]
  },
  "notes": "Ask for the issuer: whether FWD-11's tie-out is to be re-cut against a window that exists once Commonwealth is the registered reported source or a later Black Diamond-era comparison source is named. The record does not choose.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-W48-S2 -- Two inputs the Cottonwood adapter needs are absent from its source: a cash balance held outside the holdings t

```json
{
  "id": "IRPT_DASHBD-W48-S2",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~48",
  "surfaced_at": "2026-10-09T04:06:00Z",
  "one_line": "Two inputs the Cottonwood adapter needs are absent from its source: a cash balance held outside the holdings table, and the net-or-gross basis of the reported figure.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-71 and C-VALUE: V_t is the custodian's WHOLE-ACCOUNT value, cash included; the tie-out compares like with like.",
  "world_is": "MEASURED by reading S3. (1) Black Diamond silver fact_holdings carries Market Value, Units, Accrual, Unaccrued Market Value and a Cash Equivalent flag per position, and NO account-level cash or equity column; the adapter sums Market Value (cash-equivalent positions included), which is the whole-account value only if the custodian keeps no cash outside positions. Unmeasured here. (2) The Commonwealth performance rows carry NetGross = True on all 80,709 Month rows, with no key in the landed table saying whether True means net of fees; the adapter is GROSS of fees (C-FEERAIL), so a fully overlapping window would still need that basis named before a difference could be classed as fee-driven. Also: the adapter's holdings_price_return guard is not reached offline (guard_state GUARD_NOT_REACHED on every row) and large_flow_share is a held 0.25, not the producer's measured p99.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/adapter_source.json",
      "commonwealth silver performance schema (NetGross: bool)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-D2-W47-S1 -- The step-7 dry_run read 304 MB and 29.4 s because it computed one day with no source partition (SOURCE_LAG), so it does not size the class or lots sta

```json
{
  "id": "IRPT_DASHBD-D2-W47-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~47",
  "surfaced_at": "2026-10-09T04:06:43Z",
  "one_line": "The step-7 dry_run read 304 MB and 29.4 s because it computed one day with no source partition (SOURCE_LAG), so it does not size the class or lots stage; row W23-S2 is not discharged by it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "TO-DB-b-70 step 7 and CTO condition 1: a {\"dry_run\": true} invoke reads the Lambda's own Duration and Max Memory Used against 900 s and 2048 MB before the organic fire, as the lots-stage sizing (packet Unmeasured, W23-S2).",
  "world_is": "MEASURED 2026-10-09 04:03Z, RequestId ef733674-6c4d-4f9f-b6e4-045778c0a185: Duration 29367.78 ms, Max Memory Used 304 MB. The log shows 'computing 1 day(s) 2026-10-08..2026-10-08', '2026-10-08 SOURCE_LAG: no balance partition', 0 rows, and 'lots newest landed: account_activity_daily=None ...' with empty class_rows, lots_rows and lots_catch_up. The newest dim_balance partition is date=2026-10-07 and balance partitions land about 09:46Z the following day (date=2026-10-06 LastModified 2026-10-07T09:46:56Z; date=2026-10-07 2026-10-08T09:46:43Z). The function ran no class or lots compute, so AC2 reads PASS on numbers that carry no information about the 7,604-account lots stage (kit reference 1672.3 MB, 374.93 s). The first fire is the first at-scale run on the Lambda.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/R35_APPLY_RECORD.json dry_run.report_line",
      "aws s3api list-objects-v2 opal-data-assets schwab/08335338/silver/dim_balance/ date=2026-10-06 and date=2026-10-07 LastModified",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md Unmeasured"
    ]
  },
  "notes": "Not a STOP: the dry_run was under 85% and wrote 0 objects, as the order's criterion reads. The first fire is held until the 2026-10-08 silver partitions land (about 09:46Z), because an ad hoc fire before then is a SOURCE_LAG no-op; its REPORT line is the real sizing read.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-D2-W47-S2 -- record-terraform-deploy.sh also writes and commits infra/aws/terraform/investor-reporting/CHANGELOG.json, outside this order's grant, so the source ma

```json
{
  "id": "IRPT_DASHBD-D2-W47-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~47",
  "surfaced_at": "2026-10-09T04:06:43Z",
  "one_line": "record-terraform-deploy.sh also writes and commits infra/aws/terraform/investor-reporting/CHANGELOG.json, outside this order's grant, so the source map was stamped by its scoping half record-deploy-scope.py directly.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-70 step 6: run infra/aws/lambda/ci/record-terraform-deploy.sh so the source map's deployed_code_sha256 records the live hash; the order's grant names the source map and not infra/aws/terraform/**.",
  "world_is": "MEASURED by reading the script (lines 448, 800-827, 886-888): after the stamp it runs a CHANGELOG writer on infra/aws/terraform/<pipeline>/CHANGELOG.json, git-adds it and commits it with the source map. That path is not in <paths>. Ran instead: python infra/aws/lambda/ci/record-deploy-scope.py investor-reporting --function irpt-49f-reporting-gold-lambda --code-sha256 <live CodeSha256>, which is the wrapper's own stamping step (1 of 15 rows stamped, 14 untouched), committed @443bd67448. No CHANGELOG entry exists for this deploy.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/record-terraform-deploy.sh:448,800-827,886-888",
      "infra/aws/lambda/ci/record-deploy-scope.py",
      "infra/aws/lambda/ci/lambda-source-map.json @443bd67448"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-D2-W47-S3 -- The worktree has no terraform binary and no .terraform, so init and the plan used the main checkout's terraform.exe and a local-directory provider mir

```json
{
  "id": "IRPT_DASHBD-D2-W47-S3",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~47",
  "surfaced_at": "2026-10-09T04:06:43Z",
  "one_line": "The worktree has no terraform binary and no .terraform, so init and the plan used the main checkout's terraform.exe and a local-directory provider mirror of aws 5.100.0, with no download.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-70 step 4 runs the targeted terraform plan in infra/aws/terraform/investor-reporting/reporting-gold/ from the worktree, and the order forbids downloading any package or program.",
  "world_is": "MEASURED: .tools/terraform.exe is absent in the worktree and the root has no .terraform. Used C:/dev/ajb_workspace/.tools/terraform.exe (v1.15.8, SAFE_APPLY_TERRAFORM for the apply) and ran terraform init -plugin-dir=<the ycharts root's .terraform/providers>, which holds aws 5.100.0 windows_amd64; init completed with no network fetch of the provider. The lock file and .terraform are git-ignored (git status clean after init).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform init output 'successfully initialized' 2026-10-09 ~03:57Z",
      "git status --porcelain infra/aws/terraform/investor-reporting/reporting-gold (empty after init)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-D2-W47-S4 -- Pins 0-4 leave four CHANGED bundle members (opal_naming.py, systems.json, exemptions.json, reporting_policies.json) packaged at their older source-map

```json
{
  "id": "IRPT_DASHBD-D2-W47-S4",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~47",
  "surfaced_at": "2026-10-09T04:06:43Z",
  "one_line": "Pins 0-4 leave four CHANGED bundle members (opal_naming.py, systems.json, exemptions.json, reporting_policies.json) packaged at their older source-map pins, not the HEAD bytes the packet's file list prints.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-DB-b-70 step 3 sets pins 0 to 4 exactly as the packet's Preconditions table lists; the packet's file list prints sha256 at HEAD for all 19 members and marks opal_naming.py, systems.json, exemptions.json and reporting_policies.json CHANGED.",
  "world_is": "MEASURED: the built bundle stages those four from the pins already in the source map (b5dc2e63d1, 224058ea3f, 8b4c15c6ba, 11bf813387), whose sha256 values (for example opal_naming.py 4eb46f70...) differ from the packet's list (9d301e1c...). The packet itself says the four are outside this function's data path (a census switch, a vendor row, a bucket-policy exemption row, an unrelated policy row), and the order lists pins 0 to 4 only, so they were left. The deployed bundle is the signed behaviour; its bytes for those four members are the older ones.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json @d5c11dc683 staged_from",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md 'The build's file list'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_DASHBD-D2-W47-S5 -- The amended sizing read (dry_run + backfill, population, 2026-10-07) logged LOTS_SKIPPED on a realized-lot key repeat in batch 2 of 8, so lots_rows is

```json
{
  "id": "IRPT_DASHBD-D2-W47-S5",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_DASHBD~47",
  "surfaced_at": "2026-10-09T04:17:24Z",
  "one_line": "The amended sizing read (dry_run + backfill, population, 2026-10-07) logged LOTS_SKIPPED on a realized-lot key repeat in batch 2 of 8, so lots_rows is 0 and precondition 3 is not met; the first fire was NOT run.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~D2",
  "spec_asserts": "Ruling AMENDMENT 1 on TO-DB-b-70: a {dry_run, backfill D..D, accounts population} invoke on the newest landed returns day sizes the lots stage over the population (accounts >= 7000, lots_rows > 0) at under 85% of 900 s and 2048 MB; the R35 packet (S33) measured no refusal on the kit run of 2026-10-06 and says the producer refuses only a row identical in every column or a repeat of the whole realized key.",
  "world_is": "MEASURED 2026-10-09 04:13Z, RequestId c42b0fd6-494f-4444-8cf7-d1e02ff8c38b (the live function, population 7604, event dry_run + accounts population + backfill 2026-10-07..2026-10-07): rows 6897 DRY, class rows 25019 DRY, then 'LOTS_SKIPPED 2026-10-07 SystemExit: REFUSED: realized lot id <two ids joined by /> repeats with the same closing date and quantity: the key is not unique', after 'batch 2 of 8'. Duration 129821.09 ms, Max Memory Used 1200 MB (to the refusal; the stage did not finish, so these are not the lots stage's peaks). lots_rows {} and lots_failed one entry. Gold prefix object counts before and after equal (returns 1132, the other four 0). The 2026-10-07 data therefore carries a realized-lot key repeat the 2026-10-06 kit run did not, and the deployed producer (account_activity_lots.py @18a7702338) refuses it. Consequence if left alone: the 07:41 ET scheduled fire runs the lots catch-up (activity table empty, so oldest days first, up to 10), each day that carries a repeat is LOTS_SKIPPED, returns and class are still written, and after-read A1 (zero LOTS_SKIPPED) cannot pass. Separately, the first attempt (RequestId 2b6a404d-cdad-4dbb-889e-f8f82af94215) put accounts inside the backfill object as the ruling's text shows and was REFUSED at once (accounts is an event-level key per handler.py:31 and :499), nothing written; the second used the handler's documented shape.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/R35_APPLY_RECORD.json dry_run and dry_run_first",
      "infra/aws/lambda/investor-reporting/reporting-gold/handler.py:494-531",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md S33 and Branch B"
    ]
  },
  "notes": "STOPPED here per the ruling's item 4 (the read did not pass): no first fire, A1 to A6 unread, ledger leg A1 open. The sizing read to try next is the same event on 2026-10-06, the day the kit ran clean, or a list of accounts without the repeat; the issuer decides. Plain Lambda facts for the decision: 2 of 8 batches took about 130 s in total with the returns and class stages first, so the full stage is not read.",
  "disposition": "UNDER_INVESTIGATION"
}
```
