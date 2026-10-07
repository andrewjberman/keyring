# NFRA_CTLPLN -- ARMED rows whose disarm owner is `2.0.0_SA_COO~C`: what the artifact reads at 2026-10-07 ~13:0xZ

**Author:** `2.0.0_SA_COO~C`. **For:** `3.0.0_SA_CVO` (the dispositions are the adjudication's to write; a row is never edited) and
the round's close. **Read at:** trunk `7b3c62daf0`. **Denominator:** 17 rows of 71 in
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` read `hazard_standing: ARMED` (counted by
parsing every row); 11 name this seat as disarm owner, alone or with the CTO (W1-S1, W3-S2, W3-S3, W5-S1, W9-S1 to W9-S4, W12-S1,
W14-S2, S13). The other 6 (S1 Andrew; W4-S1, W4-S2, W8-S2, W14-S3 the CTO; Z-S1 `2.0.0_SA_COO~Z`)
are not this seat's to state, except W14-S3, which a ruling this seat executed has closed and is listed for that reason.

Each line is a MEASURED read of the artifact, not the row's own word. "DISARMED" means the hazard the row names no longer exists
on the trunk or in the applied state; "OPEN" names the owner and the condition.

| row | hazard, in short | reads now | evidence |
|---|---|---|---|
| W1-S1 | a Dell deploy that passes a role needs `iam:PassRole`, which is denied | DISARMED by ruling and build | CT-c-3 merged and APPLIED (TO-APPLY-3, complete): `DenyPassRoleExceptNamed` with a rendered named list; `PASSROLE-RENDER applied=0 named=0 ... ok=True`. A role is passed only after an admitted role request; the route is `org/devices/role_request.py`. First live round trip NOT run (see OPEN below). |
| W3-S2 | the bus's primary watch path did not check the sender's tailnet name | DISARMED | `.tools/agentbus-consumer.py:73-137` carries the register check (commit `221ee5b0b6`, CT-b-3 amendment 2) |
| W3-S3 | a refused message stayed on the queue and blocked the group | DISARMED | same commit: a refused message is recorded under `org/mcp/inbox/_agentbus_refused/` and deleted (`agentbus-consumer.py:93-123`) |
| W5-S1 | two readers outside CT-c-6's grant admitted only laptop and site-z | DISARMED | CT-d-6 merged @f0060c6aa5; issuer's run on the trunk today: `FABRIC-READERS ids_ok=9/9 schema_ok=5/5 rowschema_ok=12/12 readers_ok=9/9 old_grammar_left=0 enum_equal=True gate_selftest=ok ok=True` |
| W9-S1, W9-S2 | the row schemas refused a Dell fabric value and a Dell id | DISARMED | same run: `schema_ok=5/5 rowschema_ok=12/12` |
| W9-S3, W9-S4 | three more readers of the old id grammar | DISARMED | same run: `readers_ok=9/9 old_grammar_left=0`; issuer's trunk run `FABRIC-CENSUS files_scanned=1733 hits=64 ... unclassified=0 ok=True` |
| S10 (INERT, listed for completeness) | a census that failed once its own files were committed | repaired | the same `FABRIC-CENSUS` line, run on the trunk after the merge |
| W14-S3 (owner the CTO) | the naming gate refused policy files that name existing functions | DISARMED by ruling and build | CTO msg 106190 form (b): Terraform builds the Deny from the census under `tests/`; CT-a-1 merged @47a20c88e4 with no override; `ROUTES-RENDER ... header_ok=True ok=True` |
| W14-S2 (with the CTO) | both Dells can rewrite a command document | PARTLY: OPEN | The routes Deny (signed, order TO-APPLY-6 pending, NOT applied) refuses the rewrite on the 12 documents feeding YES hosts. It stays allowed on every other document, the two resident ones included. Owner of the remainder: `1.0.0_SA_CTO` (the boundary ruling accepts it at the role reached). |
| W12-S1 | three Lambda-vendored copies of the trading calendar keep the old silent fallback | OPEN, PARKED | Decision of this seat as issuer: NO re-vendor cell in this project. The three functions belong to three other pipelines; replacing a vendored copy is a deploy of each, in each owner's lane (rule 30's non-application: an existing pipeline is not changed as a rider). Reach: a pre-2024 holiday, or any date from 2028-01-01; the row reads two of three call sites pass current dates and the third an event day (UNKNOWN). Un-parks: the next deploy of any of the three functions, or 2027-12-01, whichever is first. Carrier: this file and the row; owner to name: `1.0.0_SA_CTO` at the round-N analysis. |
| S13 | bun fetches from the public registry on a run outside a node_modules tree | OPEN, ARMED | cell CT-k-2 AMENDMENT 5 handed (worker ~13, running); interim rule CTO msgs 106214 and 106220 on all three boxes |

**Not yet run, and named so a DISARMED line above is not read as EXERCISED:** the first live role request round trip
(`dell2-20261007T085711Z-7b15`, admitted; the laptop apply and its pair are not cut); a named-commit deploy read-back from a Dell;
the exercised refusals from a Dell box. Each is an outcome read for the round's close, not a row.
