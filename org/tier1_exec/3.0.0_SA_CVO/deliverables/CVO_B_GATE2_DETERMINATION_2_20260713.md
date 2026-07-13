# GATE-2 DETERMINATION #2 — INF Advisor-of-Record (LD-0277)

**Lane:** `3.0.0_SA_CVO~B` — Andrew-direct DEDICATED validation lane. **My determination IS gate-2.**
**Hash:** **`8bd1d1b62`** — on `origin/CLOUD`, ancestor of my HEAD, **AoR `.py` tree CLEAN** (I ran the
committed code, not a tree). DS has confirmed this hash is frozen and that his in-flight F2-B work is **not**
in it.
**Supersedes:** my determination of 07:00Z, which I **retracted** at 07:05Z.

---

## DETERMINATION: **gate-2 VERIFIED at `8bd1d1b62`** — for the scope in §1, and **NOT** for the scope in §3.

**This clears gate-2. It does NOT authorize go-live.** Still required and NOT mine: **CHANGE-2** · the
**never-widen co-sign** (CTO~B + COO) · **Andrew's GO** · the **V4 served-verify on the first nightly after
activation** (NEVER#4). **Gate-2 verifies the MECHANISM AND (now) THE SERVED VALUE. Only the nightly verifies
DELIVERY.**

## 1. WHAT I VERIFIED — every arm run at `8bd1d1b62`, each with a control that can go RED

| arm | result |
|---|---|
| Complete key `(source_digest, fold_mode, code_digest)` — 8 arms, one process each | **8/8 discriminates** |
| — absent · not-self-describing · **MODE mismatch (the rollback)** · **SOURCE mismatch (in-place rewrite)** · **CODE mismatch (retired logic)** · pin-unset | all **RAISE** |
| — **legit cache reuse (`--single INF_D_00c`)** · fresh servicing-only under OFF | both **RETURN** — *a discriminator, not a brick* |
| **A3 THROUGH THE DISPATCH** (not resolver-direct) | **RAISES on the MODE branch** — artifact agreed on every other field; *the source is innocent* |
| **SERVED-VIEW arm** — does the fold reach `account_team`? | **RED @`69219a7db` (`peter_lee`) → GREEN (`noel_soderblom`)** |
| — branch axis (C_07 had a *third* override line, `:231`) | **answered BRANCH-INDEPENDENTLY: ZERO writes to `advisor_key` remain in C_07**; control finds **both** `:229` and `:231` at the bad hash |
| **SAME-DAY RE-RUN arm** (real dispatch + live S3) | **RED without the re-pin (the nightly aborts) → GREEN with it (the chain completes)** |
| Dispatch-pin ↔ loader-read **SEAM**, live | pin `d512e15a…` **==** read `d512e15a…` |
| F4 (fail-closed on the UNOBSERVABLE) · healthy control | RAISE/RAISE/RAISE · **control RETURNS the map** |
| F7 coverage_drop · F8 corrupt-event skip + INCOMPLETE→CANNOT-EVALUATE | both **GREEN** |
| Round-8 regression battery | **ALL LEGS GUARDED** |
| **Class sweep** — 11 of 49 gold scripts write `advisor_key` | **all 11 HAND-grounded. C_07 was the ONLY instance.** |
| SERVE-HELD (live primitive, denominator 108, positive control 2) | resolver **0** deployed · detector **0** deployed |

## 2. THE TWO THINGS THAT NEARLY SHIPPED, AND WHY THE GREENS ARE WORTH SOMETHING

- **I greened this once already and was wrong.** `INF_C_07` overwrote the canonical folded key with the
  servicing rep — `account_team` shipped **un-folded** — and **every arm I owned measured the RESOLUTION, not
  the SERVED VIEW.** DS found it and reported it against his own code. **A verifier that only ever asks the
  producer what it produced has not verified delivery.** The served-view arm now exists and it is the arm that
  should have existed from the start.
- **My own instruments lied to me TEN times tonight**, and **every single one was caught by a control failing —
  none by care.** Including: a `bash` that silently resolved to WSL (an empty chain read *reads as* "resolver
  absent" — the instrument could **manufacture the verdict under test**); a class census that scored the
  proven-RED C_07 as **SAFE** (declared **unusable**; all 11 sites hand-ground instead); a served-view arm that
  greened on **symbol-absence** and would have false-greened a *renamed* clobber; and a grep with conflicting
  matchers that printed **"NONE"** on a file I knew contained two override lines.

## 3. WHAT THIS DETERMINATION DOES **NOT** COVER — stated, not blurred

1. **F2-B is IN FLIGHT and is NOT in this hash.** DS is landing the **phantom-advisor** fix (`inflection_unmapped_rep`
   is in neither normalisation list, so a coverage regression would put a **phantom advisor holding real AUA on
   the SERVED per-advisor NNA** — dormant only because rep_id coverage is 849/849) plus per-reason unresolved
   counts. **It must be verified at its own hash before co-sign. My determination says nothing about it.**
2. **NO END-TO-END GOLD RUN.** CLAUDE.md forbids ad-hoc gold runs to validate. My arms drive the **real**
   chain-assembly path, the **real** consumer read path, the **real** re-pin function and the **real** C_07
   enrichment — they do **not** execute the gold scripts.
3. **V4 SERVED-VERIFY IS STILL REQUIRED AND IS NOT GATE-2.** Only the first nightly after activation verifies
   delivery.
4. Everything was hermetic or live-**read-only**. Nothing written; no gold run triggered.

**Nothing served · switch OFF · SERVE-HELD · the fold has never been ON — which is the only reason tonight was
a census and not a post-mortem.**
