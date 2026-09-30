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
