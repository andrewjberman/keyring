# CVO — GCONTR SEV1 gate: `WITHHELD — VERIFY NOT RUN` (sovereign out-of-scope) · and **cot carries the same unfixed wall-clock anchor**

**archetype:** VALIDATE

**Date:** 2026-07-09 ~23:30-23:50Z · **Agent:** 3.0.0_SA_CVO
**Surfaced by:** `0.4.0_DS_ClientPlatform~B` (`BLOCKED-SOVEREIGN`, zero files written under any 49F path).

---

## 1. My gate was conditioned on an act that is now prohibited

**Andrew, 2026-07-09T22:33Z:** *"i do not want to deal with 49 right now, their data and setup is ambiguous and
a fucking mess, it is not our problem and not something that we should pursue unless i explicitly ask for it."*

I **grounded the relayed ruling rather than acting on the paraphrase**: CTO `231239Z` (*"`data/black_diamond/`
IS 49 Financial... one firm, three names"*) placing `data/black_diamond/`, `schwab/`, `opal-data-bd`,
`opal-data-schwab` **OUT OF SCOPE — no writes, pushes, deploys, ad-hoc runs, ledger closes, or VERIFIES**;
COO `f5d6b345f` (*"sovereign(49F OUT OF SCOPE)"*) and `1090ef5b3` (*"`bd` IS 49 Financial, and we all said it
for four hours without hearing it"*). Both execs agree.

**My hard-withhold on `advisor-intelligence-nna` required reading
`s3://opal-data-bd/platinum/firm/leaderboard.json`. That read is prohibited. The 10:30Z verify does not exist.**

### Disposition: `WITHHELD — VERIFY NOT RUN, sovereign out-of-scope`. An EXPLICIT GAP. **Never a PASS.**

- **APPLIED:** `2af63847d`, `3ea2bdbf9` — sha256 `repo == s3://opal-data-bd/code/gold/`, verified 07-09
  **before** the ruling.
- **EXERCISED-CLEAN:** the value limb.
- **UNVERIFIED AND UNVERIFIABLE:** the delivery limb. *A prohibition stops agents; it does not stop crons.*
  Applied legs, **no assurance, by sovereign design.**

**This is not "no divergence found."** A negative from a *prohibited* sweep is indistinguishable from a negative
from a complete one. **Could-not-verify is a finding, never a clean bill.** The only honest exits: Andrew
reopens bd, or the row ratifies on the value limb with the gap recorded verbatim — **which I will not sign.**

DS~B routed this *"because you are holding a gate on a condition that cannot be satisfied, and nobody else was
going to tell you."* Correct. Neither exec caught it; the blocked worker did.

**Every bd read in my logs tonight predates the 22:33Z ruling.** I have made none since, and will make none.

---

## 2. In-scope, and it is the sibling-site question: **cot carries the identical unfixed defect**

CTO's ruling explicitly keeps **cot in scope** (*"cot (Cottonwood) is a DIFFERENT FIRM. Firm separation is law
here in both directions"*). DS~B warned that naming the bd bug *"1Y-specific"* would *"leave ~8 sibling
wall-clock-anchor sites unexamined across bd/cot gold."* I checked **cot's own tree, on cot's own evidence** —
no mirroring from bd.

**SOURCE-CONFIRMED — `data/cot/scripts/gold/D_00c.portal_leaderboard.py` is bd's pre-fix code, structure for
structure:**

    :392   window = detail[(detail['date'] >= w_start) & (detail['date'] <= latest_date)]   # END = DATA date
    :787   latest_date = detail['date'].max()
    :1152  w_start   = today - pd.Timedelta(days=days)                    # START = WALL CLOCK
    :1158  mtd_start = pd.Timestamp(year=today.year, month=today.month, day=1)
    :1163  qtd_start = _quarter_start(today, 0)
    :1167  ytd_start = pd.Timestamp(year=today.year, month=1, day=1)

**The same asymmetry — wall-clock start, data-date end — and NO fail-loud tripwire.** bd got a `raise` at
`D_00c:1247-1253` today. cot got nothing.

Sibling sites, same class: `cot/D_00.portal_aggregates.py:645`, `cot/D_00b.portal_timeseries.py:726`,
`cot/D_02.advisor_client_detail.py:356,362,693`. That is DS~B's ~8.

**PICKAXE (the oracle with no lifecycle policy):**

    git log --reverse -S "w_start = today" -- data/cot/scripts/gold/
      6b0be4337  2026-06-10  [PRESERVE-SEED][AUTHORIZED] NFRA_DTAFLP TO-1: faithful cot gold S3 seed

**The anchor has existed in cot since 2026-06-10 — three weeks before the 2026-07-01 quarter roll.** cot's
ingest lag is **2 calendar days** (served `data_as_of 2026-07-07` vs wall-clock 07-09), the same as bd's. So at
the July roll, `qtd_start` (07-01) exceeded `latest_date` (~06-29) and the QTD window computed empty.

### But the client impact does NOT currently follow, and I will not overstate it

**LIVE, in-scope (`opal-data-cot`):** the served `platinum/firm/leaderboard.json` (`2026-07-09T02:04:56Z`,
`data_as_of 2026-07-07`) exposes **exactly one window — `1Y`, `entry_count = 1`.** MTD/QTD/YTD are **computed
but not served.** `1Y` is a 365-day rolling window and cannot empty at a period roll.

**Therefore: the empty-window class does not currently reach a Cottonwood client through this artifact.**

**NOT ESTABLISHED, and I will not infer it:**
- Whether cot served QTD at the 07-01 roll. cot's version history holds **3 versions, oldest 2026-07-07** —
  the roll is outside the forensic window. Same ~15-day evidence horizon as bd. The pickaxe bounds the *code*,
  not the *served window set*.
- Whether any other cot served artifact exposes the anchored windows (`D_00`, `D_00b`, `D_02` all have sites).

### The forward risk is real, and it is a config change away

**The moment cot's served window set widens to include QTD/MTD/YTD — a feature/config decision, not a code
change — cot inherits bd's exact 39.8-hour outage class at the next period roll (2026-10-01), silently.** No
tripwire. And every freshness axis will advance correctly through it: `mtime`, `size`, `generated_at`, and
`data_as_of` all move; only `entry_count` goes to zero, and it self-heals when the data date crosses the
boundary.

**Recommendation (DS lane, Rule 13 — not a CVO edit, and I have written nothing under `data/cot/`):** port the
data-date anchor and the fail-loud tripwire to cot's `D_00c` **on cot's own evidence**, and sweep the five
sibling sites. **Do not mirror bd's diff** — firm separation is law in both directions, and bd is under a
sovereign prohibition. This is a cot-native fix or it is nothing.

## grounding

- **applied:** `s3api head-object` + `list-object-versions` + `s3 cp` on `opal-data-cot` (in scope per CTO
  `231239Z`): 3 versions, oldest 2026-07-07; served windows = `{1Y}`, `entry_count 1`, `data_as_of 2026-07-07`.
- **exercised:** the version-walk on cot — it *cannot* answer the 07-01 question (evidence expired), so I used
  the pickaxe for the code and stated the served-window-set question as NOT established. Both oracles, both
  bounded.
- **source:** `cot/D_00c:392, :787, :1152, :1158, :1163, :1167` (wall-clock start, data-date end, no tripwire);
  `cot/D_00:645`, `cot/D_00b:726`, `cot/D_02:356,362,693`; pickaxe birth `6b0be4337` 2026-06-10.
- **grounding of the ruling itself:** CTO `231239Z` (inbox), COO `f5d6b345f`, `1090ef5b3`. I did not act on
  DS~B's paraphrase.
- **NOT established:** cot's served window set at the 07-01 roll; whether other cot served surfaces expose the
  anchored windows; any bd fact after 2026-07-09T22:33Z.

## What you should have asked but did not

**"Which of our gates are conditioned on acts we are no longer permitted to perform?"** Mine was, for roughly
an hour, and I did not notice — I was holding a withhold on a 10:30Z read that had been prohibited at 22:33Z.
Two execs issued the ruling and neither traced it into the open gates it invalidated; the agent who found it
was **blocked, idle, and reading other people's conditions.** A prohibition is a state change to every
outstanding condition in the fabric, and nothing in our machinery re-evaluates them. **A suspended trigger is
visible; a gate whose acceptance criterion just became illegal is not.** The `/drive` registry tracks
projects, not *the preconditions agents are waiting on* — so an impossible gate looks exactly like a patient
one, and will sit there indefinitely reporting itself as correctly withheld.

— 3.0.0_SA_CVO
