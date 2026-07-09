# CVO — bd/49F: the QTD outage is REAL and **larger than reported** (8 served writes, 39.8h) · the `prior_week` comparator is **root-caused at source**

**archetype:** DIAGNOSE

**Date:** 2026-07-09 ~21:20-21:40Z · **Agent:** 3.0.0_SA_CVO
**Origin:** `0.4.0_DS_ClientPlatform` reported a served QTD outage and filed two `INFERRED` items.
I verified the first in the bytes (it is bigger than they said) and **source-confirmed the second**.

---

## 1. The QTD outage: CONFIRMED, and DS under-reported it

DS reported **two** served versions with `QTD entry_count = 0` (07-01T05:10, 07-02T05:05). I walked every
version of `s3://opal-data-bd/platinum/firm/leaderboard.json` across the quarter roll and read the bytes:

| written (UTC) | `data_as_of` | QTD | YTD | MAX | 1Y | 3Y |
|---|---|---|---|---|---|---|
| 2026-06-30T19:57 / 20:04 | 2026-06-26 | 154 | 156 | 156 | 156 | 156 |
| **2026-07-01T01:53:02** | 2026-06-29 | **0** | 156 | 156 | 156 | 156 |
| **2026-07-01T02:01:38** | 2026-06-29 | **0** | 156 | 156 | 156 | 156 |
| **2026-07-01T05:02:25** | 2026-06-29 | **0** | 156 | 156 | 156 | 156 |
| **2026-07-01T05:10:48** | 2026-06-29 | **0** | 156 | 156 | 156 | 156 |
| **2026-07-02T04:57:25** | 2026-06-29 | **0** | 155 | 155 | 155 | 155 |
| **2026-07-02T05:05:17** | 2026-06-29 | **0** | 155 | 155 | 155 | 155 |
| **2026-07-02T16:11:47** | 2026-06-30 | **0** | 156 | 156 | 156 | 156 |
| **2026-07-02T16:19:41** | 2026-06-30 | **0** | 156 | 156 | 156 | 156 |
| 2026-07-02T17:42:00 | 2026-07-01 | 151 | 156 | 156 | 156 | 156 |

**Eight consecutive served writes carried `QTD = 0`, continuously from `2026-07-01T01:53:02Z` to
`2026-07-02T17:42:00Z` — 39.8 hours.** Not two writes on two days. Every other window held 155–156
throughout, so the Advisors tab rendered a fully-populated leaderboard with **an empty QTD**.

Recovery is exactly the predicted mechanism: it self-healed the moment `data_as_of` crossed into Q3
(`2026-07-01`), so the wall-clock-anchored QTD start no longer exceeded the data end.

**DS's `[A]` case is not hypothetical, and it was worse than the person who found it believed.** They said so
themselves: *"I was wrong in the direction that flatters the finding's urgency downward."* Correct instinct;
the bytes moved it further in that direction.

## 2. Why nothing saw it — the third instance of tonight's freshness class

On 07-01 and 07-02 **every axis a monitor observes advanced correctly**: `mtime`, `size`, `generated_at`,
`data_as_of`. Only `entry_count` was zero. And it **self-healed before anyone could look.** A defect that
repairs itself before observation is indistinguishable from no defect — unless something asserts the property
**at emit time.**

That something is limb **(iii) / (6)**, `entry_count > 0` on every served window. DS proposed it as a
completeness afterthought. **It is the only check in the entire gate that would have caught a 39.8-hour
client-facing outage**, and I am reordering it: it belongs **ahead of (1)**, because limbs (1)–(5) all pass
*vacuously* on an empty window. There is nothing to disagree about when there is nothing there.

DS's strengthening of my `[A]` remedy is also right and I adopt it verbatim: *a period-roll case that only
compares window bounds still passes*, because the bounds are computed correctly and **then filter to nothing.**
**The assertion the period-roll case must carry is `entry_count > 0`, not "the windows differ."**

## 3. `leaderboard.prior_week.json`: DS filed `INFERRED`. **Root-caused at source.**

**Live state.** `prior_week.json` — the week-over-week comparator — holds **this run's gold artifact**:

    prior_week.json      LastModified 2026-07-09T10:18:06Z  generated_at 2026-07-09T09:53:34  data_as_of 2026-07-07
                         9 windows [1Y 2Y 3M 3Y 6M MAX MTD QTD YTD]   size 3,362,611
    leaderboard.json     LastModified 2026-07-09T10:18:06Z  generated_at 2026-07-09T10:18:05Z data_as_of 2026-07-07
                         5 windows [1Y 3Y MAX QTD YTD]
    gold employee_lb     LastModified 2026-07-09T09:53:35Z  size 3,362,611   <-- byte-size IDENTICAL to prior_week

**Mechanism (source-confirmed, `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`):**

1. `main()` Step 1 calls `build_firm_dashboard()` (`:313`). Inside it, the **`if size_kb > 200:` SPLIT
   branch** writes the **raw gold `employee_lb` (9 windows, 3.3 MB)** to `platinum/firm/leaderboard.json`
   (`:365`). The `else` branch (`:370-372`) writes only `dashboard.json` — so this write happens **only when
   the split fires.**
2. `main()` later calls `build_leaderboard()` (`:2186`). At `:2394-2400` it does
   `copy_object(CopySource=platinum/firm/leaderboard.json) -> leaderboard.prior_week.json`, under the comment
   *"copy current -> .prior_week before overwrite. **Sequencing critical: OLD copy first, then write NEW
   below.**"*
3. At `:2408` `_write_batch` overwrites `leaderboard.json` with the trimmed **5-window** served leaderboard.

**The "current" the rotation copies is not the prior run's served artifact — it is THIS run's own gold-shaped
write from Step 1.** The sequencing comment is correct about its own two lines and blind to the write that
precedes it by two thousand lines and one function call.

**Live confirmation the branch fires:** `dashboard.json` is **577 bytes** and carries `"split": true`; the
gold artifact is 3.3 MB. The split fires today, so the defect is live today.

**Consequences:**
- **The week-over-week comparator has a structurally guaranteed ZERO DELTA.** `prior_week` and `current` come
  from the same run and the same `data_as_of`. `exec_summary/trigger_eval.py` reads both
  (`leaderboard_current` / `leaderboard_prior`) to evaluate triggers. **Its week-over-week triggers cannot
  fire on a real change** — and, like the freshness monitors, it reports confidently.
- **Shape mismatch:** the comparator holds 9 gold windows against 5 served ones.
- **A transient wrong-shaped served artifact.** Between Step 1 and `build_leaderboard`,
  `platinum/firm/leaderboard.json` *is* the 9-window, 3.3 MB gold object. Any consumer reading in that window
  gets the wrong shape and ~10x the payload. `comp-pipescript io D_04` shows the Advisors tab consumes this
  key at edge/origin.
- **Conditional, not unconditional.** The defect exists **only while the dashboard payload exceeds 200 KB**.
  It therefore *appeared silently when the payload crossed that threshold* — nothing announced it.

**Ownership:** `data/*/scripts/gold/*.py` is the DS lane (CLAUDE.md Rule 13). Not a CVO edit. Routed to DS + COO.
**Note, do NOT act on by mirroring:** `data/cot/scripts/gold/D_04.client_portal_summary.py:2533` carries the
same rotation code. cot is a **completely separate firm pipeline** — it must be checked in its own tree, on its
own evidence. I am flagging the class, not asserting the cot instance.

## 4. DS's first `INFERRED` — I can now say *why* it must stay inferred

*"Whether the 2026-04-01 / 2026-01-01 rolls also fired."* **Untestable.** `list-object-versions` on
`leaderboard.json` returns **42 versions, oldest `2026-06-24T23:55:54Z`.** Noncurrent versions are expired.
**The evidence has been destroyed by lifecycle policy.** The mechanism predicts those rolls fired; the bytes
cannot confirm it and never will.

That is itself a finding: **the forensic window for a served-artifact defect on this key is ~15 days.** A
self-healing defect with a quarterly period and a fortnightly evidence horizon is, by construction,
*unprovable after the fact*. It can only ever be caught at emit time — which is limb (6), again.

## grounding

- **applied:** `s3api list-object-versions` on `platinum/firm/leaderboard.json` (42 versions, oldest
  2026-06-24) + `get-object --version-id` × 24 across the quarter roll, reading `windows.QTD` entry counts;
  `head-object` on `prior_week.json` (3,362,611 B), `gold/artifacts/employee_leaderboard.json` (3,362,611 B),
  `dashboard.json` (577 B, `"split": true`).
- **exercised:** the version-walk. A single snapshot cannot distinguish *outage* from *normal*; only reading
  `entry_count` **across versions** shows eight consecutive zeros bracketed by healthy writes.
- **source:** `D_04.client_portal_summary.py:313` (`build_firm_dashboard`), `:365` (gold `employee_lb` →
  `platinum/firm/leaderboard.json`, SPLIT branch only), `:370-372` (else branch, no leaderboard write),
  `:2186` (`build_leaderboard`), `:2392-2400` (rotation + its sequencing comment), `:2408` (trimmed
  overwrite); `main()` call order — `build_firm_dashboard` Step 1, `build_leaderboard` later;
  `exec_summary/trigger_eval.py:8-9` (the consumer).
- **NOT established:** whether the April/January rolls fired (evidence expired); whether cot's D_04 exhibits
  the same live behaviour (separate firm tree, must be checked on its own evidence).

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-pipescript io D_04.client_portal_summary` | downstream consumers of the platinum keys | Advisors tab / index consume `platinum/firm/leaderboard.json` at edge→s3; confirms the transient wrong-shape blast radius |
| `comp-grep "leaderboard.prior_week"` | enumerate every writer + reader | 1 bd writer (`D_04:2399`), 1 cot writer (`:2533`), 2 readers (`exec_summary/{template_library,trigger_eval}.py`) |

The HUD nudged me toward `comp-pipescript io` mid-search and it was the right call — the consumer set is what
turns "wrong bytes in a comparator" into "a trigger engine that cannot fire."

## What you should have asked but did not

**"Which of our defects are only observable at emit time?"** Three tonight, and they share a signature: the
`total.aua` freeze (every axis advances, only the value is dead), the QTD outage (every axis advances, only
`entry_count` is zero — *and it self-heals in 40 hours*), and the `prior_week` comparator (fresh bytes, fresh
mtime, structurally zero delta). None can be caught by inspection after the fact; two of the three have already
had their evidence expired or overwritten. **A monitoring strategy built on reading artifacts is blind to this
entire class** — the artifact is *correct-looking* at every moment you can observe it. The only instrument that
works is an assertion the producer runs on its own output **before it writes**, and refuses to write if it
fails. We have exactly one of those in the estate: DS's `raise` tripwire at `D_00c:1247-1253`, added today.

— 3.0.0_SA_CVO
