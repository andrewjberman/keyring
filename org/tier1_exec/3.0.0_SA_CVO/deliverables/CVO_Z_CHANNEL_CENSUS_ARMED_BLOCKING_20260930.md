# CVO~Z CHANNEL CENSUS -- every gating row whose latest disposition is not terminal (AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP, DSGN_AMGTV1)

**Seat:** `3.0.0_SA_CVO~Z` - **Run:** 2026-09-30 ~17:4xZ, on Andrew's "go on your sequence" (`/next-calls` OPTION 1).

**Instrument:** the channel gate's own compiler, `.tools/surprise-row-gate.py`:
- `_gating_item_ids` gives the rows with `class: BLOCKING` or `hazard_standing: ARMED`;
- `_latest_dispositions` gives each row's latest disposition across investigations, adjudications and remediation;
- both are read from the INDEX.

A row is OPEN when its latest disposition is not GRADUATED, DISMISSED_WITH_REASON or DECOMP_INVALIDATING.

## DENOMINATORS

| project | channel files | gating rows | latest-disposition distribution | open | unknown |
|---|---|---|---|---|---|
| AMGT_CORPUS | 29 | 48 | GRADUATED 34, UNDER_INVESTIGATION 14 | 14 | 0 |
| AMGT_HARVST | 43 | 71 | GRADUATED 58, DISMISSED 9, UNDER_INVESTIGATION 4 | 4 | 0 |
| AMGT_RESAPP | 77 | 201 | GRADUATED 139, DISMISSED 50, UNDER_INVESTIGATION 12 | 12 | 0 |
| DSGN_AMGTV1 | 15 | 14 | GRADUATED 13, DISMISSED 1 | **0** | 0 |
| **total** | 164 | 334 | | **30** | 0 |

## CLASS B -- RESOLVED ON THE RECORD, NEVER DISPOSITIONED (this seat's own debt; CLOSED in this act)

Six rows. In most of them this seat wrote CARRIED, resolved or superseded in a prose table without a JSON `adjudicates` entry, so the
compile kept reading them open. Closed now:
- AMGT_CORPUS ADJUDICATION_v28: `Z-W1-S19` DISMISSED; `Z-W1-S20` and `Z-W2-S17` GRADUATED;
- AMGT_HARVST ADJUDICATION_v39: `Z-W70-S1` and `Z-W78-S2` GRADUATED;
- AMGT_RESAPP ADJUDICATION_v64: `Z-S314` GRADUATED.

Each cites the commit that resolved it. **After this act: 24 open.**

**The lesson, for this seat.** A prose table disposition is not a disposition. The compile reads only the JSON. So every CARRIED row
with a named resolution should be adjudicated in JSON the round it resolves.

## CLASS A -- OPEN WITH NO CONCRETE SEAT AS DISARM OWNER (routing ask to `1.0.0_SA_CTO~Z`)

| row | class / standing | disarm_owner as written | what it records |
|---|---|---|---|
| AMGT_CORPUS `Z-S3` | OBSERVATION / **ARMED** | "THE FABRIC, not this project and not any AMGT lane" | the notifier and the overdue-half re-route machinery |
| AMGT_RESAPP `Z-S237` | OBSERVATION / **ARMED** | "whoever owns .tools/safe-commit.sh's gate set" | a commit can land on a detached HEAD with every gate green |
| AMGT_RESAPP `Z-S248` | OBSERVATION / **ARMED** | "The owner of ... scheduled_daily_pull.cmd's ... legs" | a one-line hoist of the PY_AWS assignment |
| AMGT_RESAPP `Z-W177-S1` | BLOCKING / INERT | none | yy-2's pillar count |
| AMGT_RESAPP `Z-W177-S5` | BLOCKING / INERT | none | yy-3 AMENDMENT 1's lane refusal |
| AMGT_RESAPP `Z-W184-S1` | BLOCKING / INERT | none | AC3's api-suite 1 failed |

- **Three ARMED rows name a ROLE, not a seat.** An ARMED hazard disarms through its `disarm_owner` the same turn, and a role cannot
  act.
- **The ask:** name a seat for Z-S3, Z-S237 and Z-S248, or rule each INERT with its reason.
- The three BLOCKING/INERT rows with no owner are the RESAPP issuer's (`2.0.0_SA_COO~Z`) by the channel's convention. Their orders are
  terminal, so each is likely closable at the next RESAPP L8, and this seat will do that.

## CLASS C -- ARMED OR BLOCKING ROWS CARRIED FOR MANY ROUNDS (issuer-owned; for the next round analyses)

| project | rows | note |
|---|---|---|
| AMGT_CORPUS | `Z-S6`, `Z-S7`, `Z-S8`, `Z-S9` (ARMED, `2.0.0_SA_COO~X`) | Period sorting on raw strings, and the scanner's false-safe origins (lambda and class scopes, comprehensions, defaults). These are the channel's oldest open hazards. |
| AMGT_CORPUS | `Z-W2-S11` (BLOCKING/ARMED) | i-3's selection rule versus the team's true base case |
| AMGT_CORPUS | `Z-W1-S18` (ARMED) | `price_axis_pull.py:97-100` inserts a hard-coded workspace path into `sys.path`. That is a device-specific path in code (CLAUDE.md, LD-0405). |
| AMGT_CORPUS | `Z-W4-S6` (ARMED) | `peers/universe.py` reads the raw slash key. **The slash-key move ran at RESAPP round 53**, so this is now measurable: does the pool index resolve BP/NG? |
| AMGT_CORPUS | `Z-W1-S21`, `Z-W3-S10` (BLOCKING/INERT), `Z-W1-S22` (ARMED) | Round 25, in flight. **`Z-W1-S22` says the round-25 label rule is INERT because `_figure_currency`'s callers pass no security.** That rule is the fix for the served TSM mislabel (`Z-S69`, CORPUS v27 s.0), so the round-25 L8 must read the served label, not the unit test. |
| AMGT_HARVST | `Z-W56-S2`, `Z-W58-S1` (ARMED, `2.0.0_SA_COO~H`) | the harvest_grammar path, and the gold branch HOLD. The HOLD is now the contract's (v0.6-v0.8, `NO_DECLARED_PUBLISHER`), so `Z-W58-S1` is likely closable. |
| AMGT_RESAPP | `Z-S238`, `Z-S255`, `Z-S276`, `Z-W158-S1` (ARMED, `2.0.0_SA_COO~Z`) | `Z-S276` and `Z-W158-S1` ask whether the API Gateway route resolves a key containing `/`. **The round-53 slash-key move makes that measurable now.** `Z-S276`'s text says "carried to the round-41 analysis", which is 12 rounds ago. |
| AMGT_RESAPP | `Z-S319` (ARMED) | the MSYS-mangled content-sha256; the round-54 repair, with the interim act-start limb (v63) |
| AMGT_RESAPP | `Z-W180-S1` (BLOCKING/ARMED) | zz-1 AC1 versus `crosswalk.schema.json` `additionalProperties:false`; v61 wrote "resolved or routed" in prose only |

## WHAT THIS DOES NOT CLAIM

- It reads the channel, not the world. An open row may already be fixed in code; class C lists where a measurement would close one.
- DSGN_AMGTV1 reads 0 open. Its `Z-S1`, which this seat carried at v12-v14, has a terminal latest disposition in the compile.
