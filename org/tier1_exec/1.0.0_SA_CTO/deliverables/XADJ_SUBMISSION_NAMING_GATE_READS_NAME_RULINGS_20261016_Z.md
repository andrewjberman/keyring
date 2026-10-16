# Cross-adjudication submission -- `.tools/naming-gate.py` never reads `name_rulings.json`; OG-ap-23 is blocked

By `1.0.0_SA_CTO~Z`, 2026-10-16 ~03:5xZ. Raised by `2.0.0_SA_COO~O` msg 34707. Rows: NFRA_OPLGTW Z-W111-S7, S11..S14, Z-W113-S1.

## Context

- The commit-time naming gate (`.tools/naming-gate.py`, LGIC_ENFORCE EN-g-1) is in ENFORCE (`org/mcp/naming-gate.enforce`).
- On the OG-ap-23 release commit it REFUSES 10 lines:
  - 8 in `client_adapter_bd49f.py`: Black Diamond upstream column, table and response-key names such as `bd_account_id`
    and `market_value_profile`, graded as INSTANCE_PROFILE among other types;
  - 2 `etfs` field names in `portal_json_served.py`.
- The registry already has the carrier for exactly this case. `infra/logic/registry/name_rulings.json` answers "a name
  that is NOT a stored-file path and that the check could not answer", with `canonical` or `none_owed`.
- Four `none_owed` rows are merged @2ed472c4b9.
- But only `naming-apply-gate.py:282` (`ruling_amend`, keyed by node type) reads that file. `naming-gate.py`'s carrier
  verdict (`:2356`) does not, so the rows change nothing.
- Without a fix the gateway finish (Andrew, EOD Fri 10-16 ~22:00Z) cannot commit its release.

## Position

**Fix the gate, not the names.** `naming-gate.py` grades a (name, type) that has a `name_rulings.json` row as RULED:
- `canonical` set: the code must use it, else REFUSE;
- `none_owed`: admitted, with the row cited in the verdict line.

It reuses the `ruling_amend` lookup that `naming-apply-gate.py` already ships; there is no new file and no new class.
Proof:
- the gate's `--selftest` stays green;
- a planted name with NO row still REFUSES;
- a planted `none_owed` row admits exactly its (name, type) and not the same name under another type.

Writer: the LGIC_ENFORCE owner if live today. Otherwise a site Z cell under `2.0.0_SA_COO~O`, with this exact
diff scope (`.tools/naming-gate.py` + its selftest), merged through `safe-merge` and named to the LGIC owner for
review after the fact. No override is placed in either case. `2.0.0_SA_COO~O` adds the `etfs` row.

## Why it gave pause

### Ambiguity
The gate is shared tooling on every box's commit path. A change to its verdict is a law-adjacent change, but it
implements the registry's own written contract. The gate not reading the file is the defect; reading it is not a new rule.

### Out of pattern
A site Z seat would be editing an LGIC_ENFORCE file. Recent authors of `naming-gate.py` include site Z and dell2 seats
(2bd24f66b2, df822c81b3, 13e7c017f7), so cross-box edits to it are already the pattern.

### Other solutions
(1) `NAMING_PLACE_OVERRIDE` on the release commit. It is audited, but it is an override of a gate for a known defect,
and every later commit of these files pays it again. (2) An R20 departure for Andrew. A departure is for a deliberate
deviation from the canon; this is the canon's own carrier, unread.
