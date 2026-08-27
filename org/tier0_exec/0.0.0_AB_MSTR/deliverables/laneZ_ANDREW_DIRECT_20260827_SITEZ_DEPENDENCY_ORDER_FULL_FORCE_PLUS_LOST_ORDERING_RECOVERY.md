# ANDREW-DIRECT 2026-08-27 — sitez dependency order + full-force, AND the recovery capture of ordering data the rename destroyed

**Seat:** `0.0.0_AB_MSTR~Z` (site Z) · **Channel:** MSTR~Z terminal, direct · **Recorded:** same turn.

## 1. THE DIRECTIVE, VERBATIM

> "one shot pull, then instantiate CTO~Z and let them know to get organized in the sense of
> identifying any dependency order in sitez directives and begin full-forcing, bring COO~Z on
> as well"

**Discharged same turn:** `/git-pull once` → SITEZ up to date @`59bb2c153d`. `1.0.0_SA_CTO~Z`
spawned (PID 21128, LIVE) with the ordering task; `2.0.0_SA_COO~Z` spawned (PID 29092, LIVE)
alongside. Both briefed by MCP before registration completed. Pre-flight per `/mstr-spawn`: 1pt
process-truth 0 hits for both (positive control found the two genuinely-live serials), marker scan
0/16.

## 2. ⛔ WHY THIS RECORD EXISTS BEYOND THE DIRECTIVE — THE RECOVERY IS PERISHABLE

His first task for CTO~Z is **dependency order**, and **the ordering data is not in the register.**
Measured at `origin/CLOUD` HEAD, and independently re-derived by `0.0.0_AB_MSTR` (laptop, register
owner per LD-0341):

- **0 of 12 rows carry a `timeframe`/`target`/`due`/`eta` field — the field is absent from the
  schema entirely.** Fields at HEAD: `completion_bar`, `completion_bar_provenance`, `directive`,
  `members`, `placement`, `stance`, `title`.
- `"behind D1"` **0** · `"pends"` **0** · `"depends"` **0** · `"after D1"` **0** · `"blocked by"` **0**.

The schedules, the dependencies **and** the device legs were all riding in the **title
parenthetical**, and the 2026-08-27 rename to Andrew's operating-report names removed them from
**8 of 12 rows** (4 of the 8 are the laptop's, including D2's dated *"Fri PM target"*).

⚠ **WORSE THAN SILENCE:** D4's row still contains `D1` twice — *"shared with D1 and D3"* and *"the
four ETFs join D1's taxonomy"* — but **both record ADJACENCY, not ORDER.** A grep returns hits, so a
reader concludes the relationship is documented. **False confidence terminates the search; a false
zero invites it.**

### ⛔ THE CAPTURE IS TIME-CRITICAL AND THAT IS WHY IT IS COMMITTED HERE

`org/missions/DIRECTIVES.yaml` at SITEZ HEAD **still carries the old titles — SITEZ never took the
rename.** That makes this fabric the last readable home of the ordering data.
**The pending `CLOUD→SITEZ` merge will overwrite that file with CLOUD's renamed version and destroy
it.** The laptop pinned their own recovery at `5780da5da5`; this is the site-Z copy, captured
**before** the merge that would erase it.

**RECOVERED VERBATIM from `org/missions/DIRECTIVES.yaml` @`59bb2c153d`:**

```
D0  "Infrastructure (ongoing)"
D1  "MDPF asset-category views (~2wks)"
D2  "ADVI 49F end-to-end (Fri PM target)"
D3  "Account-level model overlay (~6-7wks, pends D1+D2)"
D4  "ETF positioning variant (3-8wks, behind D1)"
D5  "Alt research (ongoing)"
D6  "Opal Analyst + partner GraphQL (v0 ~2wks; SITEZ box legs + laptop cloud)"
D7  "Ticketing intake (THIS WEEK; SITEZ intake + laptop serve)"
D9  "Tax SMA ops (NEW; assess-first)"
```
*(D8/D10/D11 postdate this copy and never carried a parenthetical here.)*

### THE ORDERING THIS YIELDS — evidence, not a ruling

| relation | source | note |
|---|---|---|
| **D1 → D4** | *"behind D1"* | **Both ends are now MINE.** Pre-08-27 it crossed fabrics and had to be written down; one seat holding both is what made it invisible. |
| **D1 → D3** | *"pends D1+D2"* | D3 is the **laptop's**. A cross-fabric OUTBOUND dependency: sitez work on D1 unblocks their D3. |
| D6, D7 leg splits | *"SITEZ box legs + laptop cloud"*, *"SITEZ intake + laptop serve"* | `placement` preserves **directive-level** device ownership; the **leg-level** split survives nowhere. |
| D7 age | *"THIS WEEK"* as of 2026-08-19 | **8 days old at recording.** |

## 3. SCOPE — WHAT IS EXPLICITLY NOT AUTHORIZED BY THIS

⛔ **These parentheticals are EVIDENCE OF A PRIOR ORDERING, NOT A LIVE SCHEDULE.** Reviving
*"Fri PM target"* or *"THIS WEEK"* as current would **assert a commitment Andrew may have moved —
manufacturing a deadline rather than recording one.** Where the ordering is load-bearing, ask him.

⛔ **NEITHER SITEZ SEAT EDITS THE REGISTER.** `org/missions/.register-owner` names the laptop MSTR
(LD-0341). They have taken the **structural** remedy (`timeframe` + `depends_on` + leg-level
placement as FIELDS) and deliberately **not** restored the values, for the reason above.

⛔ **Neither act was wrong.** Andrew asked for his own names; the new titles are better. The
ordering simply had nowhere else to live — a correct change removing the only carrier of something
it was not about.

**Read CLOUD's register for CURRENT placement; read this fabric's for the LOST ordering. Neither
alone is right.** Our copy is stale by design: 9 rows to CLOUD's 12, **D8 absent here** though
`docs/architecture/D8*.md` exists, D1 still reading LAPTOP.

## 4. CONDITIONS AT DISPATCH

- Site Z was **OWNER-CURRENT and DRIVER-EMPTY** until this spawn: **1 live agent**, six directives
  placed ~00:0xZ, nothing seated. Verified on **two independent instruments** — broker query **and**
  a filesystem sweep — because a broker query alone is defeated by codex seats (laptop finding, same
  day).
- 377 open TOs / 140 projects, all assignees, whole fabric — a **FLOOR**; 89 serial-shaped tokens
  unclassified. Not any seat's backlog.
- `0.5.0_AE_OpalETL~Z` **DARK on six unread messages**, owning every teams-watch engine item —
  **routed, UNREAD**, not handled.
- `CLOUD→SITEZ` merge remains **MINE and gated on Andrew's explicit word**.
