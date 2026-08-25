# /self-drive D4 -- ticks 7-8 log (2026-08-24 22:07Z-22:24Z) -- state: ARMED

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier: `org/XXX.md` CTO row · continues `ctoZ_self_drive_D4_tick6.md`.
**Log cadence:** every 2 ticks; next at tick 10 or DONE.

## SCOPE + COMPLETION

```
SELF-DRIVE D4 -> 1 directive -> 2 project(s) [ETFS_POSITIONING, +ETFS_INGEST(claimed)]
  device: sitez (basis: workspace path)   open TOs: 7   denominator: 1 of 9 live directives
  claim detection: 324 project JSONs scanned -> 2 PRD-path claims (1 already a member; dedup)
  COMPLETION TEST: NOT DONE -- 0 of 2 complete.  REACHABLE 2 / UNREACHABLE 0.
```

⭐ **THE UNREACHABLE MEMBER IS GONE, AND NOT BECAUSE I EDITED THE SET.** `ETFS_CANON` sat UNREACHABLE
from tick 1 and made this loop structurally unable to terminate. **Andrew-direct ~22:12Z, VERBATIM:
*"Agreed with your recs + We can revisit ETFS_CANON After INGEST is done"*** -- he SEQUENCED it, which
is stronger than the rec I put (which merely orphaned it). **CVO~Z's 4895 item is DISARMED BY HIS
WORD; the HELD-AT-STOP branch was never used.** That is exactly the outcome their refusal was
protecting: on tick 1 I proposed reaching a terminable state by dropping the member, and they ruled
*"a stop-condition that can be satisfied by shrinking its own member set is not a stop-condition, and
the driver is the party that benefits."* **The branch existed for eight ticks and never fired,
because the correct resolution came from the only seat that could give it.**

Register lag stands (row still reads `{ETFS_CANON: scoping, ETFS_POSITIONING: active}`, `open_tos: 5`,
`last 17:50Z`) -- MSTR~Z's edit, routed, and it is now a DEFERRAL to record, not a removal.

## CALLS

**ZERO open sovereign calls at this lane (tick 8).** All three cards carried since tick 1 were
answered in one line at 22:12Z. Nothing pitched to CVO~Z this window -- no empty pitch sent.
**NOT-MINE:** the three tooling/standards defects routed to base CTO (comp_closure member compare ·
proof-of-spec VALID-on-unrun + crash-on-malformed · the `firm` enum inexhaustive a second time) ·
`comp-closure` off PATH on site Z.

## RULINGS THIS WINDOW (all mine; none required CVO adjudication)

- **⭐ THE FIRE LANDED AND THE PIPELINE WORKS.** 22:00:11/12Z, scheduled. `opal-data-assets/trueshares/
  {DIVZ,IDVZ}/bronze/holdings/20260824/` -- first objects ever under either prefix. DIVZ 29 rows /
  99.80% / $308,141,496 · IDVZ 44 / 99.51% / $199,973,564, raw issuer CSV byte-for-byte. Silver
  187 rows, four funds. **F2's remediation is EXERCISED, not merely deployed.**
- **⛔ AND SIX SEATS INCLUDING ME READ A CLEAN 0/0 OUT OF THE WRONG BUCKET FOR AN HOUR.** Applied
  `BRONZE_BUCKET=opal-data-assets`, not `ETFS_BUCKET`; `opal-data-etfs/bronze/` does not exist as a
  prefix. **My control was in the wrong bucket too, so it could not discriminate.** Corrected against
  my own committed log (`45bdd334f9`), broadcast 5265-5270. **Then COO~Z corrected MY correction and
  was right: their reads were in the CORRECT bucket, so TO-1 AC4's 0->1 discriminator is INTACT and I
  had over-swept.** Their mechanical test replaces my diagnosis because it is checkable at authoring
  time: **is my control in the same bucket as my target?** Recorded `d86b71fd0a`.
- **Z-S16 ruled a RULE-17 VIOLATION, not an as-of convention** -- I read the OTHER end: bronze carries
  `Date = 8/24/2026` on every DIVZ/IDVZ row, silver stamps them `2026-08-21`. The issuer's date is in
  the bytes and silver overwrites it. **Scope then NARROWED by DS~Z at source and adopted: filepoint
  is correct BY CONSTRUCTION (`:612`->`:665`, one variable), so the value fix is TrueShares-only** --
  the cheapest way to break a working path is to repair it against a hazard it does not have.
- **SALXX / `is_cash`:** A5 admitted a money-market sleeve into the Bloomberg universe (verified at my
  seat: 187 rows, 73 nulls, SALXX in the derived 166). **A5 is correct and not revisited** -- the
  inclusion is the safety net working. The defect is one layer up: TrueShares silver populates
  `is_cash` for 0 of 73 rows. **OBSERVATION x INERT-TODAY, ARMED ON A NAMED EVENT** (the first served
  aggregate) -- so it is pre-encoded as acceptance criteria on the GICS TO, not left floating.
- **CONV-1 ruled** on DS~Z's correct mid-build STOP: 114 filepoint rows, `''` x110 / `'Y'` x4, **no
  `'N'` ever** -- blank is the vendor's NO, and their rule would have nulled 96% of the column.
  **RULED: the encoding is a property of the FEED, DECLARED per source and ASSERTED by the parser --
  never inferred from a census**, because "no N appeared today" makes every row's meaning a function
  of its cohort and the first `N` silently re-interprets 110 rows.
- **TO-5 AC3 ruled:** ad-hoc discharges it (the law's sanctioned QA instrument), **and I ADDED
  `AC7` -- the first SCHEDULED fire observed at its invocation record -- rather than read AC3's
  silence.** ⛔ **Plus the condition neither seat had stated: `platinum/etfs/positioning_data.json` is
  a LIVE SERVED KEY carrying DE~Z's whole Z-S12 evidence, so an "ad-hoc QA run" overwrites production
  serving in place.** Binding: tell DE~Z before the write, mark the artifact `run_class: adhoc`, and
  never cite it as production evidence.
- **Andrew's ruling recorded**: deliverable `31ad35e24b`, both project JSONs `a840c58804`,
  broadcast 5340-5345 same turn.

## THE CRITICAL PATH, NAMED AGAINST MY OWN HOLD

`ETFS_POSITIONING.TO-5` carries the **only** gold->platinum schedule and was HELD by me on Z-S19.
Census, token-walked: **136 EventBridge rules, 7 ETF-named, NONE producing etf-positioning gold or
platinum** -- third independent seat agreeing (DE~Z from the serving end, AE~Z from the rules end).
**COO~Z lifted the hold @45fdc270cc after verifying all FOUR parts of the ruling, having gone hunting
for the third specifically** because a 3-of-4 correction would have read complete. AE~Z picked it up
22:19Z, preconditions re-derived 3/3 at their own seat.
**Bronze exercised. Silver exercised. Gold never run. Platinum unmoved, byte-identical. The served
surface is verified by nobody** -- and a good hour does not retire the wrong-bucket lesson.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| directives-check.py --json | scope + denominator | D4: 2 members, 9 live directives |
| to-check.py --all | open TOs in scope | 7 (INGEST 2, POSITIONING 5) |
| agentbus-sqs.sh device | device guard | sitez, basis workspace path |
| comp-find / comp-find --name | GICS site, TO-5 file, TF search | GICS_SECTOR_NAME 1 hit / 28 files; no `*etf*positioning*.tf` (MEASURED zero over 7841) |
| raw aws (rail-checked) | applied env, bucket enumeration, token-walked rules, both-tool plane pin | the wrong-bucket finding; 136 rules; offset exactly -0400 |
| safe-commit | 6 commits ticks 7-8 | all PASS |

## Blockers

None at this seat. **Zero cards at Andrew.** Surfaced not chased: register member-set lag (MSTR~Z);
the three tooling defects at base CTO; `comp-closure` off PATH here.
