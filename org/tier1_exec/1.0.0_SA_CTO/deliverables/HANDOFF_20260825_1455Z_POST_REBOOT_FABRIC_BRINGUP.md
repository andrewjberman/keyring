# HANDOFF -- POST-REBOOT FABRIC BRING-UP, 2026-08-25 14:55Z

**From:** `1.0.0_SA_CTO` (last seat live before the reboot).
**For:** whoever reads this first on restart -- **`0.0.0_AB_MSTR` primarily**, then CTO/COO/CVO.
**Companion:** `org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-25/session_state_prereboot_1455Z.md`
(the full board + today's settled rulings). **This file is the ACT LIST.**

---

## ⛔ ACT 1 -- PUSH. NOTHING ELSE UNTIL THIS IS DONE.

```
local HEAD    a0394e34f4
origin/CLOUD  e291d38e4f74
UNPUSHED      5 commits
```
**`0.0.0_AB_MSTR` holds the integrator push (LD-0367) and was wound down before the window.** The
commits survive the reboot on disk, but they are **invisible to site Z, to a fresh clone, and to
every seat that pulls before the push.**

⛔ **AMONG THE UNPUSHED IS THE D8 REGISTER ROW AND THE ENTIRE `MDPF_COTREMEDIATION` REGISTRATION.**
Until the push, a seat that pulls sees **no D8 and no such project** -- and Andrew's instruction was
that this project exist so the fabric could be brought up on it.

## ACT 2 -- CONFIRM THE REGISTER ROW I WROTE IN YOUR LANE

**`0.0.0_AB_MSTR`: I committed `org/missions/DIRECTIVES.yaml` under
`GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_MSTR` (audited, single lane, @`a0394e34f4`).** The owned-paths
gate **refused correctly** -- that file is your lane and I am not in `permitted_agents`. I took the
override on Andrew's explicit instruction to register the project with you wound down.

**Confirm the row reads as you would have written it. If it does not, it is yours to correct.**
Verified at my seat: `directives-check` rc=0, `malformed=0`, `live=10`, D8 `prd_exists=True`,
member resolves `active`.

**TWO REGISTER ITEMS, neither urgent:**
- **`D9.PFMG_TAXSMA` reads `no-json`** -- the last instance of the class Andrew's Fix 1 closed for
  D0/D2 this morning.
- **`D8` now appears in BOTH the live register and `DIRECTIVES_RETIRED.yaml`** (the cut Philosophy
  row). `malformed=0`, so not a violation -- but a reader searching `D8` finds two rows with
  different titles. **The retired row is the historical record of the 08-20 cut and must NOT be
  deleted.** Whether it wants a superseded-by pointer is your call.

## ⛔ ACT 3 -- THE LIVE OUTAGE. THIS IS THE WORK.

**`cottonwood` and `global` Model Portfolios served data are FROZEN AT 2026-08-19 -- four trading
days.** Andrew found it; the estate did not.

```
platinum/mdpf/{partner}/aggregate-aua-timeseries.json   as_of_last
  49financial 2026-08-24  OK      inflection 2026-08-24  OK
  cottonwood  2026-08-19  FROZEN  global     2026-08-19  FROZEN
NEVER#1 discharged: expected_last_trading_day(2026-08-25) = 2026-08-25.
```

⛔ **THE SERVED OBJECTS ARE REWRITTEN DAILY -- all four within 2 seconds at 13:50:49-51Z. The
publisher runs and succeeds; the staleness is INSIDE THE PAYLOAD.** Every object-mtime freshness
instrument reads HEALTHY **and is correct about the FILE.**
> **DO NOT VERIFY ANY PART OF THIS WORK WITH AN OBJECT TIMESTAMP.** That blindness is the reason it
> ran four days, and it is the condition D8 exists to end.

**OWNER:** `2.0.0_SA_COO` -- **atom-decomp of the operative surfaces FIRST (Rule 27 stage 3), before
any TO exists.** Project `MDPF_COTREMEDIATION`, PRD `docs/architecture/MDPF_COTREMEDIATION_PRD.md`
v1.0, `dep_stage: PRD`.

⛔ **THE REPAIR IS A SEPARATE PROJECT FROM THE FORTIFICATION AND MUST STAY THAT WAY.** His words
carry both halves -- *"fixed immediately"* AND *"take this as an opportunity"*. **A repair folded
into a directive-scale item inherits the directive's timeline.**

⛔ **THE TRAP, RECORDED BEFORE ANYONE IS SEATED: a re-run that produces correct data DOES NOT
ESTABLISH THE CAUSE.** It establishes the producer works when run today. **L1 (the null-filled
`dates` array) is the discriminator** -- if a re-run yields good data and nobody can say why the
array was null-filled, AC1 and AC5 are UNMET and the defect recurs on whatever caused it.
*Same shape as the a06 weekend outage ruled this morning, where the obvious fix would have inverted
the map/chain ordering and broken the four working days.*

**FIVE LEADS -- falsifiable, ALL UNREAD. The first cell reads the producer at source:**
| # | lead |
|---|---|
| L1 | cottonwood's `dates` array is almost entirely `None` -- **a stall truncates; it does not null-fill** |
| L2 | global's tail repeats `2026-07-22` ~15x; `opal-data-cot` carries a `forwardfill_v2/` prefix |
| L3 | **global is a rollup INCLUDING cottonwood -- one cause may explain both. Do not assume two.** |
| L4 | `dim_mdpf_account_distribution.py:328` `COTTONWOOD_UNITS_KEY = "gold/mdpf_revamp/cottonwood/account_units.json"` + `_cottonwood_sidecar()` :331, while `served_freshness_config.yaml:174` points at `portal/gold/mdpf/cottonwood/` |
| L5 | `0.4.0_DS_ClientPlatform~I` 14:14Z, independently, different artifact: `D_05` byte-identical at `data_as_of 08-19`. **Filed as an OBSERVATION** |

⛔ **L5 IS ALSO A FINDING ABOUT US: the signal existed and reached the fabric as a note.** A
four-trading-day freeze on a client-facing surface warrants more than an observation. **Raising that
ceiling is D8 work, not this project's.**

## ACT 4 -- WHAT NOT TO REDO (settled today; re-litigating costs the restart)

- **Cottonwood MDPF code is NOT misplaced.** It is in `data/mdpf/scripts/gold/` with every other
  partner's. **I claimed otherwise citing `data/cot/scripts/gold/`; that is Cottonwood's ADVI
  pipeline and Andrew corrected it as a category error.** The false version must not travel.
- **Whole book is the default** (~14:05Z). 49F **$138.8M IN**. Cottonwood's supervised-only view is
  a **partner request**, so the two firms' different treatments are **both correct and not in
  tension.** ⛔ An estate-wide consistency fix would be a DEFECT.
- **All work sits under a directive; projects are tagged AT CREATION** (~14:12Z). 91 active projects
  are members of nothing -- **49 live (open TOs), 42 close-out backlog, OPPOSITE REMEDIES.**
  **DIRECTION RATIFIED, MIGRATION NOT AUTHORIZED.** Volume question is a card at Andrew.
- **The 12:45Z ADVI chain PASSED** all four pinned expectations; `REFUSED-NO-BMV` 7,335 -> 0.
- **Nothing to backfill for a06** -- both aborted runs targeted an already-existing partition. **The
  weekend-outage mechanism is undiminished; fix forward.**
- **Portal CI is GREEN on `fce757cb`** and the provenance backstop is live after six dark runs.
  `ci.yml:56`'s zero-file typecheck is a **log-honesty defect, NOT a coverage gap** (step 5 type-checks).
- **The promote ledger closes** as CLOSED-WITH-PROOF / third-party measured, limitation written in.

## ACT 5 -- QUEUED WORK AT SEATS THAT WENT DOWN

| seat | state at wind-down |
|---|---|
| `2.0.0_SA_COO` | both decomp seats delivered + at CVO; **owes: the promote-ledger close (text supplied 13:09Z), `ci.yml:56` cell, a06 guard seat, c04 check 7, the twr status-vocabulary owner** |
| `3.0.0_SA_CVO` | 15 channel items disarmed; **holds `D1_CATVIEWS.TO-R1-DE` uncertified**; s.14(c) re-derivation done 6/6 |
| `0.4.0_DE~C` / `~D` | both idle, nothing staged/dirty, TO-R1-DE delivered + **UNCERTIFIED** |
| `0.4.0_DS~J` / `~K` | both TOs COMPLETE + ACCEPTED; **advisor level NOT BUILDABLE pending BD dim 436** |
| `0.7.0_AE~H` | WSE_COTMDL R1+R2 landed; acceptance discharges on the **2026-08-26 06:00Z** scheduled fire |
| `0.4.0_DS~G` | GLD-f-1 discharged on the 12:45Z read; **f-3 is COO's open NEVER#6 ledger entry** |

## ACT 6 -- 4 CARDS AT ANDREW

1. `ADVI_COTKEY` key of record. 2. **BD dim 436 vendor ask** -- one template field blocks two
directives (record `a6c76382b1`). 3. CVO's condition-4 no-gates test. 4. Retro-tagging volume.

---

**`/self-drive laptop directives` was ARMED at this seat (cron `f03462e0`, 30m, ticks 1-16) and dies
with the session.** Its carrier clause is the `org/XXX.md` Step 1b-F row; **a successor re-arms from
that row and nothing else** -- never from memory, never from a log. **Scope is now 6 directives / 13
projects** (D8 joined), completion **2 of 13**.
