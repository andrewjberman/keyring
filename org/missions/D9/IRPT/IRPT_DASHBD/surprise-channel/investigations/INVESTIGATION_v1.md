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
