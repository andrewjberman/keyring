# GATE-2 DETERMINATION #3 -- **WITHHELD** at `59c24b46e` (HEAD)

**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated validation lane, LD-0277) · **date:** 2026-07-13
**determination:** **WITHHELD.** Three open items, none of which is my analysis being incomplete -- two are
real defects and one is an infrastructure block.
**supersedes:** determination #2 (`baa2af0f7`, VERIFIED at `8bd1d1b62`). **That determination no longer
binds:** the chokepoint lib MOVED under it (`dbab19e4c`, +102/-7). *A determination binds only at the hash
it was rendered on.*

Nothing served. Switch OFF. SERVE-HELD. No prod touch, no gold run, no re-derivation -- every arm is
hermetic or READ-ONLY, compatible with `[STOP] b7bce51bd`.

---

## 1. WITHHELD ON THREE

### (1) F2 -- the absent-floor closes the NULL and not the LOSS, at 2 of 3 call sites
**And I got this wrong first.** I exercised `INF_A_00`, saw it RAISE at `:302`, and rendered *"F2 is
CLOSED at HEAD."* **That was a census of ONE.** There are three FULL-ATTACH call sites.

Per-call-site census (denominator **3**; controls: A_00 proven-GUARDED, A_01 proven-UNGUARDED, both scored
correctly -- *a census that cannot score a known case is worthless*):

| call site | state | behaviour |
|---|---|---|
| `INF_A_00:274` | **GUARDED** | `:302` raises on `_n_absent` -- fails closed, does not over-condemn |
| `INF_A_01:203` | **UNGUARDED** | floors and continues |
| `INF_C_07:280` | **UNGUARDED** | floors and continues |

`attach_advisor_key(absent='unknown')` floors **`advisor_key`** (the field a human SEES) and has **no
absent-branch for `rep_bucket`** (`:749-756` -- there is none). `INF_09:193` filters
`rep_bucket == 'individual'` **before** grouping. Exercised on the real filter: the absent row carries a
**visibly-populated `advisor_key='unknown'`** all the way to the drop -- **$30.0 of $90.0 NNA vanishes,
with no alarm.** The comments at A_01/C_07 explicitly claim the floor protects against this. **It does not.**

> **A BACKSTOP THAT PROTECTS THE OBSERVABLE AND NOT THE UNOBSERVABLE IS A BACKSTOP FOR THE READER, NOT
> FOR THE DATA.** It closes the NULL and not the LOSS. **THE UNIT IS THE CALL SITE.**

**Defect DEMONSTRATED (mechanism, exercised). Harm NOT demonstrated** -- I have *not* grounded whether
`_n_absent > 0` is reachable at A_01/C_07 in prod (A_00's own comment argues the pin + digest assertion make
it structurally impossible). **I withhold anyway**, for the reason I wrote and CTO~B quoted back at me: *a
guard whose soundness rests on a property of the producer it exists not to trust is not a guard.*
Independently found by `1.0.0_SA_CTO~B` (gate-1 `d9fd3ff2e`, 30.0/60.0) and re-grounded here.
Arm: `aor_f2_pin_does_not_bind_a00.py` (A4/A5).

### (2) R2 -- the chokepoint asserts the COLUMN and serves the ROW
`aor_resolution.py:661/:675/:691` compare `sorted({...})` over `.dropna().unique()`. **`.dropna()` removes
NULL-stamped rows from the CHECK, not from the DATA** -- they stay in the frame and are returned to every
consumer. So the guard **RAISES on a missing COLUMN** and **SILENTLY ACCEPTS a ROW that cannot describe
itself.** Same principle, one grain down.

I re-exercised base CVO's fixture (`aor_r2_null_stamp.py`) myself rather than take it on report; it meets
the non-placebo bar (4 axes fire **and** C1 can go green -- reachable from different truths). **N2: ONE
correctly-stamped row vouches for 870 UNSTAMPED rows carrying FOLDED attribution, RETURNED and SERVED on an
OFF (rollback) run.** That is A3 walking back in through the null hole, on the chokepoint built to close A3.

**LATENT. Harm NOT demonstrated** -- today's producer stamps the three fields as loop-invariant scalars, so
it cannot emit a NULL (and an empty string is not dropped by `dropna()` and would already raise). **I do not
call it a blocker, and I withhold on it. Both, and they are consistent.**

**BAR ON THE FIX (mandatory, and it is the trap):** the fix must be **exercised for OVER-condemnation**.
`isna().any()` on an EMPTY frame returns `False`, and `:606` already raises on `len == 0`, so the
**zero-mover OFF path must survive**. *A fail-closed fix that fires on a legitimate zero is the disease it
was sent to cure* -- that is the F2-B defect that existed only in a ruling, and we must not build it for real.

### (3) V4 SERVED-VERIFY -- **NOT RUN. Blocked by the bronze STOP.**
**`WITHHELD -- V4 SERVED-VERIFY NOT RUN, blocked by the bronze STOP`. An EXPLICIT GAP, never a PASS.**
This is parked on an **infrastructure control, not on my analysis**. INF bronze is dead since 2026-07-10 and
`inf-gold-full-on-bronze-complete` is event-driven on bronze-complete, so the nightly cannot run; NEVER#4
forbids an ad-hoc gold run to validate. **There is no legal path to a served V4 today.**

> **AND I NAME THE SUBSTITUTION I COULD MOST EASILY HAVE MADE.** I *did* read the served
> `platinum/firm/advisor_nna_canonical.json` this session. **That is NOT a V4 and must not be laundered into
> one:** it is `generated_at 2026-07-10T14:49:57Z`, `data_as_of 2026-07-09` -- it **predates the AoR code and
> was produced under OFF.** It grounds the PHANTOM; it says **nothing** about whether the fold DELIVERS.
> *A frozen pre-AoR served artifact is a producer-side check wearing a served-side label.*
> **A fixture green is not a served green, and the gap is not closed by lowering the bar.**

**Do not let anyone "kick" the pipeline so I can verify.** The offer will be made in good faith and it is the
destructive act: repairing bronze fires the gold re-derive against a silver snapshot with ZERO ROWS for 14
accounts, and ~$439,326.22 of served NNA **ceases to exist while every guard reports GREEN.**

---

## 2. GREEN AT HEAD (each with a control that can go RED)

| arm | result |
|---|---|
| **8/8 key matrix** `(source_digest, fold_mode, code_digest)` | RAISES on mode / source / code / pin-unset; **A5 legit cache reuse RETURNS** (a discriminator, not a brick -- `--single INF_D_00c` still works) |
| **Round-8 battery** | **35 PASS / 0 FAIL.** *It had been ABORTING after 8 -- 27 arms had never run at HEAD.* |
| **Served-view arm under ON** | **GREEN at HEAD, and it DISCRIMINATES** -- RED at `69219a7db` (the proven-RED control), GREEN at `dbd10d7aa` + HEAD. **The fold SURVIVES to the served view.** C_07 stays closed. |
| **OFF-is-a-no-op** | DELTA-0: zero movers, 0 rows touched, frame byte-identical |
| **R5 presence-gating** (source-confirmed) | resolver prepended to **all EIGHT** consumer-carrying chains (`:445-452`); not-deployed branch **fails CLOSED** (`:433`) |
| **F2 at INF_A_00** | fails closed (`:302`) and does **not** over-condemn (healthy run returns) |

---

## 3. THE PHANTOM ADVISOR: **RED on the served spine, and NOT a gate-2 blocker** -- exercised, not assumed

The served spine carries **5 advisor keys, one of which is not an advisor**: `inflection_unmapped_rep`,
**$52,604.80**.

**My v1 arm ASSERTED, in prose, that this is "SWITCH-INDEPENDENT ... nothing to do with the AoR fold," and
NEVER TESTED IT.** A comment is a claim with no vintage and no test. It is now tested
(`aor_phantom_switch_arm.py`, PC1-PC3 all pass):

- `INF_C_01:463` floors to the phantom; `:474` runs `apply_resolution_fold` **on those same rows**. The
  switch and the phantom touch the same rows *in sequence* -- they are not obviously independent, and nobody
  had asked.
- The fold re-keys an account **iff it is a MOVER** -> a mover must be in the resolution -> the resolution is
  built from `accounts_v2`.
- **Grounded LIVE** (roster `snapshot_date=2026-07-12`, **873 rows**; positive control: account 42 IS found):
  accounts **560 / 703 / 1225 are ALL ROSTER-ABSENT** -> they can never be movers -> **the fold cannot reach
  them. DELTA-0. It does not block go-live.**
- **BUT SWITCH-DEPENDENCE IS REACHABLE.** "Roster-absent" (`accounts_v2`) and "null `rep_id` on the txn row"
  (`transactions`) are facts about **TWO DIFFERENT SOURCES, and NOTHING COUPLES THEM.** A roster-PRESENT
  account with a null txn `rep_id` is floored to the phantom **and is eligible to be a mover** -- exercised:
  the fold re-keys it and moves money **out** of the phantom bucket at go-live.

> **THE GREEN IS DATA-DEPENDENT, NOT STRUCTURAL.** Same shape as "dormant because coverage is 849/849":
> **armed, not fixed.**

**Its fix is BLOCKED** by `[STOP] b7bce51bd` (no `canonical_nna` re-derivation until the silver `rep_id` NULL
is fixed and a coverage assertion exists). It is a **separate, pre-existing chapter** (CTO/COO/base-CVO), and
per COO it stays separate: *two defects filed as one get fixed as one, and the second one survives.*

### The reconciliation identity is a TRAP -- it cannot detect this class in either direction
Read live: `sum(advisors) == firm_total` ties to **0.00** -- **because the phantom is COUNTED as an advisor.**
So the identity is **GREEN IN THE DEFECTIVE STATE**. And per COO's HOLD it **stays green through the
DELETION** (both sides lose the money at the same instant). **An identity that ties in the defect AND ties
through the deletion is not a detector.** Ruling (iii)'s `sum(advisors) + unattributed == firm_total`
inherits this: it catches SUPPRESSION and is **blind to DELETION**. The deletion mode needs a **coverage /
denominator assertion** -- which is exactly the F7 detector that was deleted. **F7 and the deletion mode are
the same hole.**

---

## 4. FOUR OF MY OWN INSTRUMENTS WERE BROKEN AT HEAD

**Not one was caught by being careful. Every one was caught by a control failing.** Committed `59c24b46e`.

1. **`aor_served_view_under_on.py` MISTOOK THE GUARD FOR THE DEFECT -- and failed in the DANGEROUS
   direction.** Any exception became `survived=False` and printed *"RED -- THE FOLD IS ERASED."* The actual
   exception was the **A8 pin-unset guard doing its job** -- the guard I had certified in the 8/8 matrix.
   *"I could not observe it"* and *"I observed the defect"* shared one signature (the F4 null rule, inside the
   arm built to catch that class). **A false RED's remedy is DESTRUCTIVE:** it would have had me reopening
   C_07, a closed and verified fix. Now supplies the pin the dispatch supplies, and an instrument break exits
   2 -- never RED.
2. **`aor_phantom_advisor_arm.py`'s GREEN condition REWARDED THE FORBIDDEN FIX.** v1 went GREEN the moment
   the catchall was added to `INF_D_00f`'s junk-normalisation list -- folding the residual into `'Other'`.
   That is ruling-(i)-**FORBIDDEN** (*"silently dropping a residual is how a reconciliation stops
   reconciling"*) and, after the grounding inverted, a **false statement on a served field** -- that money is
   a real advisor's. **My arm would have certified it.** v2 asserts membership in the **CANONICAL ROSTER**
   (`INF_C_01`'s rep_id->advisor map + the AoR SSOT), so it is blind to the NAME: `'Other'` stays RED, and a
   residual under a **new name** is caught by SHAPE (M1-M4 all behave).
3. **`aor_f2_pin_does_not_bind_a00.py` ENCODED THE DEFECT and would have DEFENDED it.** Its load-bearing line
   was `attach_advisor_key(dim, res)  # absent defaults to None` -- and that default **was** the F2 hazard,
   which the fix deleted. **The "obvious" repair was to re-add a default so my own test would pass:
   restoring the hazard to green my instrument.**
4. **`aor_r182_key_verify.py` was emitting a CONFIDENT FALSE *RED*, in my own voice.** It verifies the
   **2-input** key; the shipped key grew `code_digest`, so its unstamped fixtures raise **correctly** -- and
   it concluded, at exit 1: ***"DOES NOT DISCRIMINATE -- gate-2 stays RED. Do not ship this key."*** **THAT
   VERDICT IS FALSE.** It was **right when written, and the ground moved under it** -- the C_07 lesson turned
   on an instrument instead of a docstring. **A stale arm does not go quiet; it goes CONFIDENT.** Kept as the
   historical record, but it now detects that the key outgrew it and **refuses to render**.

---

## 5. WHAT THIS DETERMINATION DOES **NOT** COVER

- **V4 served-verify** (item 3 above) -- the only thing that verifies **DELIVERY**. Gate-2 verifies the
  MECHANISM and the SERVED VIEW; **only the nightly verifies delivery**, and it cannot run.
- **CHANGE-2**, the **never-widen co-sign** (NEVER#2), and **Andrew's GO** -- none of these are mine.
- **No end-to-end gold run** (forbidden: NEVER#4 + the bronze STOP). My arms drive the real chain-assembly
  logic and the real consumer read path; they do **not** execute the gold scripts.

**Clearing gate-2 would not authorize go-live. Nothing here does.**

---

-- `3.0.0_SA_CVO~B`
