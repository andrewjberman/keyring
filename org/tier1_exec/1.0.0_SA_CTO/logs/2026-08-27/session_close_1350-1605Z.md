# 1.0.0_SA_CTO~Z — session close 13:50–16:05Z — sitez directive order, then the cottonwood mint-day chain break

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

**Serial:** `1.0.0_SA_CTO~Z` (site Z). **Window:** whole session, first log.
**Commits:** 7, all on `origin/SITEZ`.

---

## 1. WHAT THIS SESSION WAS

Andrew-direct at launch: *"identify dependency ORDER across the sitez directive set (D1 D4 D6 D7 D8
D9), then full-force."* That task completed in ~25 minutes. **The rest of the session was a live
client-facing data investigation that the ordering work surfaced**, ending in a fix applied,
exercised and verified, and a same-day recovery of a missed data day.

---

## 2. THE ORDERING TASK (discharged)

The register carries **no** ordering fields (0 of 12 rows; the fields do not exist in the schema).
Schedules, dependencies and device legs rode in the **title parenthetical**, and the 2026-08-27
rename deleted them from 8 of 12 rows. Recovered from SITEZ HEAD `@59bb2c153d` (pre-rename titles);
current placement read at `origin/CLOUD`. **Neither copy alone is sufficient.**

- **E1 — D1 BEFORE D4.** *"behind D1"*, corroborated independently from the other end by D4's own
  live stance (*"the four ETFs join D1's taxonomy — one registry serves both"*). Binds D4's
  **taxonomy layer only**; its ingest legs are not behind D1.
- **E2 — D1 BEFORE D3** (laptop's). Outbound obligation, not an inbound constraint.
- **E3 — RETRACTED** (see §4).

⛔ **E1 IS NOW INVISIBLE IN THE REGISTER.** It crossed fabrics when written, so it had to be written
down; since 08-26 D1 and D4 are both site-Z, and the sentence carrying it was deleted the next day.
**A dependency stops being recorded exactly when it stops crossing an organisational boundary —
which is when it also stops being obvious.**

Final order (post Andrew's Model Portfolios priority ruling): **D1 → D4 → D8**; D6/D7/D9 stood down
by his word.

---

## 3. THE INVESTIGATION — cottonwood, root cause found and fixed

**Chain, established at source:** the BD session cookie hit `MAX_SESSION_AGE_DAYS=7` at 8.0d →
`cot-bd-session-trigger` diverted to `mode=session-refresh` → mint **SUCCEEDED** (`rc=0`,
`state=LOGGED_IN`) → **and nothing pulled bronze**, because the rule carrying
`session-fetch Success → bronze` did not exist.

**It was KILLED, not never-built** (`5b989deb27`, "K2 dead event leg"). Its justification:
*"fired 1x/7d while the chain completed DAILY without it."* ⛔ **INVERTED — it fired 1x/7d because
that is the mint day, the one day it carries anything. The kill measured the days the rule is silent
BY DESIGN and concluded it had no consumer.**

Falsified 4-for-4 (`aws ssm list-commands`): mint days 08-03 / 08-11 / 08-19 / **08-27**; bronze
missing on exactly the two post-kill mints.

**SEVERITY, measured and narrower than "data loss":** BD's rolling ~14-day export window recovers the
gap on the next run — natural experiment at 08-19, where `_complete/2026-08-18.json` **and**
`2026-08-19.json` were both written `2026-08-20T11:45:54Z`. True impact: **~24h extra staleness on
~1 day in 7, self-healing.**

**Cadence corrected** (Andrew-direct *"Yes that config is what needs to change"*): cottonwood value
feeds `D+2` → `T-1` in `data/mdpf/config/partner_roster.json`. Grounded on write-times (47 partitions,
D+2 observed nowhere) **and** BD's own native xlsx report criteria (`sheet2.xml`: `Created (Eastern)`,
`End Date` = D-1 for holdings/allocations, **D-0 for transactions/realized** — cadence is per-TABLE).

---

## 4. MY OWN ERRORS THIS SESSION — seven, one class

Recorded because the pattern is the finding: **every one was validating against something that
DESCRIBES the system rather than the system.**

| # | error | falsified by |
|---|---|---|
| 1 | partner-to-partner freshness control | void across different declared cadences — could not have returned "healthy" for a D+2 partner |
| 2 | trusted the roster's declared `D+2` | the feed's own write times |
| 3 | trusted a docstring's "ONE committed authority" | two sha256 hashes |
| 4 | census of the wrong EventBridge plane (`events` vs `scheduler`) | `0.7.0_AE_CloudOps~Z` — R2 was already built |
| 5 | `git log --since` given a UTC cutoff | takes LOCAL time; returned a clean zero for my own commits inside a merge window |
| 6 | hand-dispatched 4 lambdas | `/mdpf-refresh` already existed — Build Ladder rung 2, on Andrew's own *"I just run the skill"* |
| 7 | leaned on `MAX_SESSION_AGE_DAYS=7` as if measured | Andrew: *"we do not even know if the cookie would ever die"* — a policy choice |

**#1 produced a FALSE client-facing outage claim that reached MSTR~Z and was heading to Andrew.**
Retracted @`d01190795f`; the relay was stopped before it landed.

---

## 5. COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise | PASS | forwarder ran, produced its own banner; PATH 98/102 |
| rail markers | 3x `# rail-checked:` | N/A | config-field fan-out, roster-copy enumeration, scheduler hunt — all off-rail by domain |

**What worked:** the PreToolUse **risk-reflex** found the second `partner_roster.json` home during a
commit — a defect I had not looked for and would not have found. **What failed:** nothing.
**Gap found:** ⛔ **no comp-tool models CONFIG-FIELD FAN-OUT** (which consumers read a given config
file, and which copy each resolves). That gap is exactly what let four diverged roster homes persist;
`comp-aws` models resource edges, not intra-payload field flow. **Candidate tool, routed as a
finding.**

---

## 6. DELIVERABLES + COMMITS

| commit | what |
|---|---|
| `57ae04ffef` | the recovered dependency order (E1/E2/E3) |
| `d01190795f` | **retraction** of my own false cottonwood defect |
| `b3ed0e8d69` | COT session-chain parity SPEC + roster `D+2`→`T-1` |
| `f56af5748a` | spec amend: correction reached 1 of 3 roster homes |
| `9a3dab252a` | spec amend: R2 already built (Scheduler plane); R1 was KILLED |
| `b2051ccb8a` | **law edit** — `/self-drive D4` struck from `org/XXX.md` 1b-F |
| `b3e22750c9` | spec amend: 7d is a refresh schedule, not a measured lifetime |

---

## 7. CURRENT STATE (zero-prior-context handoff)

**FIXED AND VERIFIED.** `cot-session-complete` restored by `0.7.0_AE_CloudOps~Z` (`57a373d336`), tag
`cot-pipeline-v0.7.6`. Verified by me on live primitives: rule ENABLED, correct pattern
(`opal-cot-bd-session-fetch` / `Success` / `aws.ssm`), target `cot-bd-session-trigger`
`{"mode":"bronze-run"}`. **A3 negative control: 4 real different-document Success events excluded
while the positive fired, `TriggeredRules` = exactly 1.**

**RECOVERY COMPLETE, SAME DAY.** `/mdpf-refresh status` — all four scopes `as_of_last=2026-08-26`
`[OK behind=1]`, written ~15:42Z. Cottonwood moved `08-25 → 08-26` and I confirmed the two legs that
were blocked at 15:35Z (assets bronze 404→present `15:39:29Z`; silver gained `date=2026-08-26`).
**No settled day was restated** (cottonwood-scoped check).

**MERGE.** CLOUD→SITEZ landed `5edabd600a`; `origin/SITEZ` **0 behind CLOUD** (was 1,122). All 8
session commits (mine + AE's) reachable from the landed head — **nothing unseated**. AE's pre-staged
deliverable preserved unstaged with content intact.

**OPEN — 9 CONFLICT-HELD GOLD KEYS.** Investigated per Andrew. **6 of 9** (49financial, inflection)
are **pure run metadata** — no business data differs, no action. **3 of 9, all `global`**, differ
**because the recovery worked**: at 13:30Z global computed 08-26 with cottonwood
`carried_at_declared_cadence(as_of=2026-08-25)`; at 15:42Z it recomputed with the real data.
**The guard is serving the carried version and holding the accurate one.**

**ROSTER — FOUR HOMES, THREE CONTENTS** (read on deployed bytes):
`data/mdpf/config/` `4c104d9b` **T-1** ✅ · emitter `af44aaad` D+2 · S3 runner `af44aaad` D+2 ·
**`mdpf-gold-lambda` bundled `e86e4631` D+2** (a pre-edit build artifact of the config copy).
⚠ **Impact UNESTABLISHED**: `_cot_carry_policy` computes the window from `max_lag` alone and treats
the cadence offset as provenance *"NEVER as an addend"* — so the deployed `D+2` may be inert to
computation and affect only what the artifact reports. **Determine before describing it as a data fix.**

---

## 8. BLOCKERS

None. Nothing in this lane is blocked on another agent.

---

## 9. NEXT STEPS

- **[Andrew]** re-land fork: the tool deletes **all 9** conflicts (`reland()` takes every
  `status == "conflict"` row, no per-key scoping); he authorized **3** and said leave 6 alone.
  **REC (a)** — run the sanctioned tool; the 6 re-land business-identical.
- **[Andrew]** `D1_NAMEDISCOVERY` certification — decomp complete on this fabric post-merge, certifier
  `3.0.0_SA_CVO`, **alternate base `1.0.0_SA_CTO`**. One certification from TOs.
- **[Andrew]** `D1_CATVIEWS` seating — both lanes 0 commits/48h, stopping 12 min apart on 08-25; the
  register clause protecting them as *"in flight"* was written 08-26.
- **[0.7.0_AE_CloudOps~Z]** R2 write-up (ratify `cot-bd-session-daily-et` + ET-boundary reasoning);
  then the **rescoped** roster propagation — **three acts, not one**: emitter edit + F-3 publish, and
  a **Terraform redeploy** of `mdpf-gold-lambda` so its bundled copy re-bakes.
- **[open, unowned]** the conflict guard counts `_provenance.*` / `meta.generated_at` as business-diff,
  so **every same-day re-run conflicts on every pre-existing key by construction** — a false-positive
  generator that hides real conflicts.
- **[open, unowned]** `transactions` / `realized` are D-0 same-day feeds with **no roster rows at all**.

## 10. THE ONE PATTERN WORTH GENERALISING

**A config-provenance field in the output artifact is what made four diverged roster homes visible.**
No census found them. The gold run's manifest recorded `config_hashes.partner_roster_sha256`, the hash
matched nothing I expected, and reading the deployed package settled it. **Make the artifact state
which config it consumed** — cheap, and it caught what four separate searches did not.
