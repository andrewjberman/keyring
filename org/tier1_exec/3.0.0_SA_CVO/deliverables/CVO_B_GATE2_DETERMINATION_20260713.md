# GATE-2 DETERMINATION — INF Advisor-of-Record go-live (LD-0277)

**Lane:** `3.0.0_SA_CVO~B` — Andrew-direct DEDICATED validation lane. **My determination IS gate-2.**
**Hash verified:** **`69219a7db`** (round-8.2 FINAL; on `origin/CLOUD`; ancestor of my HEAD; AoR `.py` tree
clean — I ran the committed code, not a working tree).
**Date:** 2026-07-13

---

## >> RETRACTED 2026-07-13 07:05Z — **GATE-2 IS WITHHELD, NOT VERIFIED. DO NOT CO-SIGN.** <<

**I issued VERIFIED at 07:00Z. It was WRONG. Retracted four minutes later, before anyone acted on it.**

**Why:** `INF_C_07:229` inherits the canonical advisor_key and then **OVERWRITES it** —
`df['advisor_key'] = df['_key_override'].combine_first(df['advisor_key'])`, where `_key_override` is
`slug(accounts_v2.representative_name)` — **the SERVICING rep**. **Exercised:** canonical (folded)
`joe_brandenburg` → after the override → `inflection_wealth_mgmt`. **`combine_first` takes the override
FIRST; the override always wins; the fold is ERASED.** And `account_team` is both the frame the household
headline resolves from *and* the served view that C_01b/C_08/D_00/D_00b/D_00c/D_02/D_03/D_04 inherit. **So
under ON the fold never reaches the served views — which is the entire point of the project.**
*(Found by DS, reported against himself; I verified at source and exercised it rather than taking his word.)*

**WHY MY BATTERY PASSED ANYWAY — the instrument gap, stated plainly:**
**EVERY ARM I BUILT MEASURES THE RESOLUTION. NOT ONE MEASURES THE SERVED VIEW UNDER ON.**
- OFF arms: correctly green (under OFF the resolution *is* servicing, so an override to servicing is a no-op).
- My ON positive control asserted `fold == 164 == my independent oracle` — that measures **the resolver's
  OUTPUT**, not what C_07 does to it afterwards.
- My F5c perturbation arm proved the resolution **propagates**. It proves the value **arrives**; it does not
  prove nothing **overwrites** it downstream.

**This is the same shape as my own R-A finding — a value that is CORRECT AT THE POINT IT IS PRODUCED and
WRONG AT THE POINT IT IS CONSUMED. I found that class in the resolver and never pointed it at my own battery.**

**And the gap was already written in §4 of this very document** — *"gate-2 verifies the MECHANISM; only the
nightly verifies the DELIVERY"* — and I issued a green as though mechanism-verified were enough.
**A gap you have named and not closed is not a gap you have handled.**

**SECOND OPEN FINDING (mine, grounded structure / ungrounded branch — Rule 22):** the dispatch pins
`INF_AOR_ASOF` (`:1385`) and `INF_AOR_SRC_ETAG` (`:1422`) at **script load**, before `case "$MODE"` (`:1447`),
with **no re-pin** — while `CHAIN_FULL = CHAIN_PULL + CHAIN_COMPUTE` (`:345`) and `CHAIN_PULL` (`:337`)
contains **`INF_API_SILVER_ACCOUNTS_V2`, which REWRITES `accounts_v2`**. **The chain pins the source, then
rewrites the source, then reads it.** Branch (a): the pull rewrites the pinned partition → read-ETag ≠ pin →
resolver RAISES → **the whole nightly aborts on a healthy run** (the "total abort that looks exactly like the
guard working"). Branch (b): the pull writes a new partition → the resolver *and, post-my-F2-fix, `INF_A_00`*
resolve off the **pre-pull** partition → the freshly-pulled roster is ignored, and **the served dimension may
be one pull staler than before my fix — in which case that staleness is MINE.** Which branch obtains is
**NOT grounded**; routed to DS, who owns `convert_orion_api_to_silver`.

**NEXT ARM (should have existed from the start): a SERVED-VIEW arm under ON** — assert the **served
`account_team`** carries the FOLDED key for a mover. Not the resolver's output. The served artifact.

---
## (SUPERSEDED — the 07:00Z determination, retained for the record)

## ~~DETERMINATION: gate-2 VERIFIED for the round-8.2 delta~~ — **RETRACTED, see above**

**This clears gate-2. It does NOT authorize go-live.** Still required and NOT mine: CHANGE-2, the
never-widen co-sign (CTO~B + COO), **Andrew's GO**, and the **V4 served-verify on the first nightly after
activation** (§4.2 — gate-2 cannot substitute for it).

---

## 1. What was exercised, and what it proves

| # | Arm | Result |
|---|---|---|
| 1 | **The complete key** `(source_digest, fold_mode, code_digest)` — 8 arms, each in its own process | **8/8** |
| | absent · not-self-describing · **MODE mismatch (the rollback)** · **SOURCE mismatch (in-place rewrite)** · **CODE mismatch (retired logic)** · pin-unset | all **RAISE** |
| | **legit cache reuse** (`--single INF_D_00c`) · fresh servicing-only under OFF | both **RETURN** |
| 2 | **A3 THROUGH THE DISPATCH** (not resolver-direct) | **RAISES on the MODE branch** |
| 3 | **The dispatch-pin ↔ loader-read SEAM**, live | pin `d512e15a…` **==** read `d512e15a…` |
| 4 | **F2** — absent account | **RAISES** (structurally impossible; no longer served) |
| 5 | **F4** — None → RAISE · observed-and-empty → `{}` · stale → RAISE · **healthy control → the map** | **green, non-placebo** |
| 6 | **F7** — a vanished account | **EMITS `coverage_drop`** |
| 7 | **F8** — one corrupt event file | **skipped**, chain survives, basis marked **INCOMPLETE** → detector reports **CANNOT-EVALUATE**, not green |
| 8 | **Round-8 regression battery** | **ALL LEGS GUARDED** |

**A5 and the healthy controls are what make the other arms mean anything.** A key that raises on everything
is not a discriminator, it is a brick — and a brick gets disabled at 3am by the operator it wrongly
condemns. That failure mode killed `run_id`; this key survives it.

**On arm 2 specifically:** the leftover artifact was constructed to agree with the run on **every field the
guard checks except `fold_mode`** — `as_of` matches the pin, `source_digest` matches the partition's ETag,
`code_digest` matches the live lib. **The source is innocent.** That is exactly what a *prompt* rollback
leaves behind, and it is the only construction that proves anything. (When R-B landed, this fixture briefly
went green on the *not-self-describing* branch — a green that proved nothing. I caught it and repaired the
fixture before reporting.)

**On arm 3:** the key is fail-closed on an env var. The dispatch HEADs one object to pin it; the resolver
stamps whatever object its loader GETs. **Had those ever named different objects, every consumer would raise
on a HEALTHY nightly — a total abort indistinguishable from the guard working.** Nobody had exercised that
seam, including the CTO who specified it.

## 2. The one open item (LOW — cleanup, not a blocker)

`aor_resolution.load_prior_state` — the docstring states `"""(prior_state dict, first_run bool)"""` (a
2-tuple) while the function **returns 3** (`prior_state, first_run, bad_keys`; F8 added `bad_keys`). Every
real caller unpacks 3, so **nothing breaks** — but it is a **false contract claim in source**, in the very
function changed for F8, on the night we made *"a comment is a claim with no vintage and no test"* doctrine.
Fix the docstring.

## 3. Deploy state (verified, not assumed)

`comp-pipescript deployed` → `INF_A_0` **MISSING_ON_S3**, `INF_D_11` **MISSING_ON_S3**. **Nothing served.
Switch OFF. SERVE-HELD. Production harm NOT demonstrated** (the nightly fires `mode: full` —
`inf-pipeline/eventbridge.tf:237`, verified directly, never from a self-report).

## 4. EXPLICIT GAPS — stated, not blurred into a pass

1. **No end-to-end gold run.** CLAUDE.md forbids ad-hoc gold runs to validate work; validation rides the
   scheduled nightly. My arms drive the **real dispatch chain-assembly path** and the **real consumer read
   path** — they do **not** execute the gold scripts. **This is a real limit of gate-2 and I am not
   papering over it.**
2. **V4 served-verify is still REQUIRED and is NOT gate-2.** The first nightly after activation must be
   verified against the **served artifact** (NEVER#4). Gate-2 verifies the *mechanism*; only the nightly
   verifies the *delivery*.
3. Everything above is **hermetic or live-read-only**. Nothing was written, no gold run was triggered.

## 5. Method notes (why the greens are worth anything)

- **Commit-before-verify.** The tree moved under this analysis **five times**; two of my citations went
  stale mid-flight. Every number here is measured at a **committed hash**, and I independently confirmed
  DS's "comment-only" delta (`445711c2c`→`69219a7db`) rather than taking his word — the AoR-tree diff is one
  file, every changed line a comment.
- **My own instruments lied to me five times**, and each would have shipped a false result: a bare `bash`
  resolving to WSL (→ an empty chain read that **reads as "resolver absent"** — the instrument could
  *manufacture the verdict under test*); an exception truncated at exactly the point where the branches
  diverge; a mis-guessed column name that made the **healthy control raise**; a shell integer test that
  silently **defaulted** 8 scripts to a classification; and a grep returning "zero" because the code used a
  helper my pattern missed — which would have had me **accusing DS of a false commit message**. Every one
  was caught by a **control failing**, never by cleverness. *A control that fails is the instrument telling
  you to stop.*
- **My own battery encoded a defect as expected behavior.** R6 asserted *"absent account emits NOTHING —
  coverage axis owned elsewhere."* I measured the hand-off: **nothing owned it.** F7's fix now makes a
  vanished account emit — so **my fixture failed because the code finally became correct.** R6 is inverted.
  *A hand-off to an owner you have not verified is a deletion.*

---

**GATE-2: VERIFIED at `69219a7db`, subject to §4.** Go-live remains gated on CHANGE-2, the never-widen
co-sign, Andrew's GO, and the V4 served-verify.
