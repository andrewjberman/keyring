# CVO — CORRECTION to my own committed record: cot limb (2) is **VALUE-class, LIVE and SERVED**. My sentence was the vacuous one.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~01:15–01:25Z · **Agent:** 3.0.0_SA_CVO
**Corrects:** `cvo_GCONTR_gate_WITHHELD-verify-not-run_sovereign_plus_cot_carries_the_same_unfixed_anchor.md` §2 (committed earlier tonight)
**Raised by:** `0.4.0_DS_ClientPlatform~B`, correction request. **Verified independently by me, on cot's own evidence.** No bd file opened.
**Status:** RECORD CORRECTION ONLY. No code touched. cot is Andrew-PARKED; the fix is DS-lane (Rule 13).

---

## 1. What I wrote, and why it was the wrong sentence

I wrote: *"the empty-window class does not currently reach a Cottonwood client through this artifact"* and framed cot's
exposure as **forward risk** — *"the moment cot's served window set widens … cot inherits bd's exact outage class."*
I also called `1Y` *"a 365-day rolling window."*

**Each clause is true of the EMPTY class. All of them are false of the class that is actually shipping.** I audited
cot for the defect bd *displayed* (emptiness at a period roll) instead of the defect bd *had* (a populated, plausible,
wrong window). bd's harm was never emptiness — it was `$3,516,778.16` of NNA flow silently dropped from **1Y**.
Emptiness was the 3Y/QTD symptom. **Mis-valuation was the 1Y symptom, and 1Y is the window that ships.**

## 2. The two classes are different defects

| class | mechanism | cot exposure |
|---|---|---|
| **EMPTY** | `mtd/qtd/ytd_start` > `latest_date` at a period roll → zero rows | computed, **NOT served.** My §2 was right. No client impact. |
| **VALUE** | wall-clock `w_start` vs data-date END → window **short by the ingest lag** | **SERVED. The only window cot ships.** |

## 3. Independently verified — cot source + cot served artifact, no bd, no ad-hoc run

**Source** (I opened each; DS~B's line numbers hold, one path did not — see §5):

    lib/gold_utils.py:118-119   def _today(): return pd.Timestamp.now(tz='UTC').normalize()...   # WALL CLOCK
    D_00c:1253                  today = _today()                                    -> 2026-07-09 at generation
    D_00c:60                    WINDOWS = {'3M':90,'6M':180,'1Y':365,'2Y':730,'3Y':1095}
    D_00c:1152                  w_start = today - pd.Timedelta(days=days)           -> 2025-07-09
    D_00c:787                   latest_date = detail['date'].max()                  -> 2026-07-07
    D_00c:392                   window = detail[(date >= w_start) & (date <= latest_date)]

**Served** (`s3://opal-data-cot/platinum/firm/leaderboard.json`, operational `cp`, read-only):

    available_windows = ['1Y']          windows.1Y.entry_count = 1
    data_as_of        = 2026-07-07      generated_at = 2026-07-09T02:04:55Z
    window_bounds     = ABSENT

**Arithmetic:**

    as-built  (wall-clock start) : [2025-07-09 .. 2026-07-07]   span = 363d
    correct   (data-anchored)    : [2025-07-07 .. 2026-07-07]   span = 365d
    DROPPED from a window LABELLED "1Y": 2025-07-07 (Mon), 2025-07-08 (Tue)

> **Two business days of `nna_daily`, short at the START, on a window labelled `1Y`. Not empty. Populated,
> plausible, and mislabelled.** Exactly bd's defect, on the one window cot serves.

**Magnitude: UNMEASURED.** It needs `gold/canonical/nna/` for those two dates, and I will not trigger an ad-hoc gold
run (CLAUDE.md NEVER rule). `entry_count = 1` bounds the blast radius to one Cottonwood employee's leaderboard NNA —
**a small blast radius is not correctness.**

## 4. This is the founding sentence again, in a third subsystem tonight

`window_bounds` is **ABSENT** from cot's artifact, so the divergence is **unobservable downstream**. Every freshness
axis — `mtime`, `ETag`, `data_as_of`, `generated_at` — advances correctly, and `entry_count` is a healthy `1`.
**Every instrument reads GREEN while the value is quietly short.**

That is the third instance tonight, in a third subsystem: the telemetry error log reporting a flawless clean bill
while 57% of calls were lost; `comp-iam`'s output being independent of the property it measures; and now a served
artifact whose freshness axes all confirm a number none of them measured. **The artifact cannot be audited from its
own output** — the same law, again: *no instrument may ground a claim about its own completeness.*

## 5. Two things DS~B did not have

**(a) His `_today` citation does not resolve.** He cited `data/cot/scripts/gold/gold_utils.py:118-119`. **That file
does not exist.** The real definition is `data/cot/scripts/gold/lib/gold_utils.py:118-119` — right line, missing
`lib/`. The claim survives because I found and read the real one. Recording it because a citation that does not
resolve is precisely what Rule 22 exists to prevent, and he is the agent who taught me to re-derive rather than
relay.

**(b) The correct pattern already exists inside cot's own tree — and this is the useful part.**

    D_04.client_portal_summary.py:2408-2415
        _window_starts['QTD'] = _dt.date(_as_of.year, _q_month, 1).isoformat()
        _window_starts['YTD'] = _dt.date(_as_of.year, 1, 1).isoformat()      # <-- anchored on _as_of (DATA)

**`D_04` already anchors on the data date, not the wall clock.** So the cot-native fix has a **cot-native
precedent**: `D_00c` can be repaired against `D_04`'s own idiom without importing one line of bd's diff. That
satisfies Rule 13 firm separation *and* CTO's "a cot-native fix or it is nothing" — not as a constraint to work
around, but because the pattern was already there.

**(c) A dormant trap, correctly NOT counted in the ~8 live sites.** `lib/gold_utils.py:122-123
`_window_start(days) = _today() - Timedelta(days)`` is wall-clock and, as far as I can find, **has no cot caller** —
`D_02:355` defines its own local `_window_start(today, days)`. It is not a live site today. It is a loaded helper in
the shared lib that will anchor the next author who imports it. Re-anchor or delete it in the same pass; do not
inflate the site count with it.

## 6. Disposition

**Correction ACCEPTED and entered.** cot limb (2) is recorded as **VALUE-class exposure, LIVE and SERVED (a 363-day
"1Y")** — not solely forward/empty-class risk. The sentence *"does not currently reach a Cottonwood client"* is true
of the empty class and **false of the served one**, and DS~B is right that it is the sentence someone quotes in six
weeks. It was in a log I committed. I am the agent who spent tonight arguing that an instrument's silence is not a
negative result, and I shipped a clean bill on the strength of the one window I checked for the one symptom I
expected.

**No fix from me.** Verifier is not do-er. `data/cot/scripts/gold/*.py` is DS-lane; a cot gold push **auto-deploys**
(`safe-deploy.sh`), so it is NEVER#2 never-widen (CTO+COO sign-off), it needs a COTTONWOOD-tenant probe, and cot is
**Andrew-PARKED** (*"cot is more important but we'll circle back for it"*). DS~B is authoring it uncommitted and
holding for sign-off. That is correct and I endorse the restraint.

## grounding

- **desired/source:** `data/cot/scripts/gold/lib/gold_utils.py:118-119,:122-123`; `D_00c:60,:392,:787,:1152,:1253`;
  `D_02:355,:660`; `D_04:2408-2415` (the data-anchored counter-example)
- **applied:** served `s3://opal-data-cot/platinum/firm/leaderboard.json` — `available_windows=['1Y']`,
  `1Y.entry_count=1`, `data_as_of=2026-07-07`, `generated_at=2026-07-09T02:04:55Z`, **`window_bounds` ABSENT**
- **exercised:** the date arithmetic against the served `data_as_of` and the generation-time wall clock →
  `[2025-07-09 .. 2026-07-07]` = 363d; drops 2025-07-07 (Mon), 2025-07-08 (Tue)
- **NOT established:** the dollar magnitude (needs `gold/canonical/nna/`; no ad-hoc run); whether other cot served
  surfaces expose anchored windows; cot's served window set at the 2026-07-01 roll (evidence horizon expired — still
  open from my prior log)
- **scope:** zero bd/49F/Schwab files opened. A repo-wide `comp-grep` for `def _today` incidentally *listed* bd paths
  in its index output; none were opened and nothing bd was derived from.

## What you should have asked but did not

**"Did I audit for the defect, or for the symptom I happened to see?"**

bd showed me emptiness, so I swept cot for emptiness, found none in the served set, and wrote a clean bill. The
mechanism I had already source-confirmed — wall-clock start against a data-date end — **produces a short window
every single day, and empties one only at a period roll.** The empty case is the *rare* branch. I audited the rare
branch, on the artifact where the common branch was live, and reported the common branch as a forward risk.

A blocked worker with no gate to hold read my conclusion and caught it. That is the second time tonight the same
agent has corrected a Tier-1 exec's record — the first was my own gate, conditioned on an act that had become
prohibited an hour earlier. **Both times the finding required only reading someone else's conclusion against the
evidence they themselves published.** Nothing in our machinery does that, and the two people best positioned to do
it are whoever is currently blocked and whoever is currently idle.

— 3.0.0_SA_CVO
