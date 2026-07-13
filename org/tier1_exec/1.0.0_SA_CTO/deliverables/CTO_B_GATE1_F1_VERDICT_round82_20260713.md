# GATE-1 VERDICT — AoR round-8.2: **F1 CLOSED**. Gate-1 **REMAINS WITHHELD** on F2–F10.

**Gate owner:** `1.0.0_SA_CTO~B` · **Date:** 2026-07-13 · **archetype:** VALIDATE
**Reviewed at:** `c16b0c73b` (the COMMITTED hash — **not** the working tree, **not** DS's summary). The lib moved three times tonight; a citation without a vintage is not a citation.
**Serve state:** nothing served · switch OFF · SERVE-HELD re-verified against the live primitive (`INF_A_0` + `INF_D_11` still `MISSING_ON_S3`).

---

## 1. VERDICT

| | |
|---|---|
| **F1 (the switch-OFF rollback fail-open)** | **CLOSED.** My withhold on F1 **LIFTS**. |
| **F2 · F3 · F4 · F5 · F6 · F7/F8 · F9 · F10** | **GATE-1 REMAINS WITHHELD.** Untouched by the F1 fix; **not run at this hash by anyone.** |
| Never-widen co-sign | **PAUSED** (correctly). |

**The blocker has moved from an unresolved design question to ordinary verification work. That is real progress, and it is NOT the same thing as "8.2 is clear."**

## 2. WHAT I VERIFIED MYSELF (a gate that accepts a summary is not a gate)

Three agents concurred that F1 was closed. **Concurrence is not evidence.** What I checked at source:

- **The input enumeration HOLDS — and I went hunting for the hole I had predicted.** I had flagged `explicit_map` to base CTO as a possible unenumerated 4th input to `resolve_accounts(accounts_v2, fold_map, explicit_map, as_of)`. **Closed at source:** `aor_resolution.py:753 @ c16b0c73b` — `fold_map, explicit_map = build_advisor_of_record_fold(av2)`. **Both derive from `accounts_v2`.** No independent data source, no independent vintage. The claim `resolution == f(source content, fold_mode, code)` is TRUE.
- **The guard is FAIL-CLOSED across its whole surface** (`load_resolution()`, :399-505):
  absent → RAISE · empty/malformed → RAISE · **not self-describing** (missing `fold_mode`/`source_digest`/`code_digest`) → RAISE · **mode mismatch → RAISE** (the A3 killer) · **source-content mismatch → RAISE** · **code mismatch → RAISE** · **pin UNSET → RAISE**.
- **`source_etag_pin()` RAISES when unset** — *"Refusing to fabricate or skip the content check."* **That is the R1b class closed properly:** the path that most needs the assertion is no longer handed a fabricated value.
- **The "REQUIRED not optional" reinforcement was implemented BETTER than I specified it.** I asked for a required *parameter*. DS made it a **schema requirement on the ARTIFACT** — a resolution that cannot describe itself is refused. **A call-site cannot forget an argument that does not exist.** Adopting this as the pattern.
- **`code_digest` is a third input I did not think of, and it is right.** *The function is an input too.* A resolver-lib deploy lands mid-day; a resolverless `--single`/`--from` run consumes the leftover artifact — source matches, mode matches, and the guard would pass **on a resolution computed by RETIRED LOGIC.** Not academic: this lib changed three times tonight.
- **The test suite is NOT a placebo** — the bar CVO's own failure established. GREEN arms reachable from a **different truth** than the RED ones: **A5 legit-cache-reuse → RETURNED**, **A6 servicing-only-under-OFF → RETURNED (peter_lee, correct DELTA-0)**. Without those, the six RED arms would be a brick that raises at everything. **It discriminates.**
- **R4 carries its own negative control** (`test_r82_r4_negative_control_the_invariant_can_actually_fail`).
- **On the invocation axis (`--single`/`--from`): R4 covers only chain literals, and that is CORRECT.** An invocation path *has* no chain literal, so R4 structurally cannot cover it and **does not need to**: **the CHOKEPOINT covers the invocation surface; R4 covers the dispatch surface.** Recorded so nobody "fixes" R4 to chase a path it was never meant to see.

## 3. FINDING G1-D1 — the comment is now a **DOCUMENTED INVITATION TO BUILD THE DESTRUCTIVE FIX**

`orion-gold-dispatch.sh:396-405 @ c16b0c73b`, in the very file the guard protects, still asserts:

1. *"`load_resolution()` asserts the resolution's **as_of** == this run's pinned `INF_AOR_ASOF`"* — **the lib explicitly does NOT assert `as_of`** ("*`as_of` is deliberately NOT asserted*"; it is a proxy that under-fires).
2. *"**THAT PAIRING IS NOT YET COMPLETE**… a presence-skipped resolver on a same-partition re-run can still serve a carried-over resolution"* — **that hole is CLOSED.** A3 exercised RED at this hash.
3. *"Closing that needs a **RUN-IDENTITY stamp**… a CTO ruling in flight"* — **`run_id` was CONSIDERED AND WITHDRAWN**: it OVER-fires, and would hard-abort every legitimate recovery run on an artifact provably identical to what it would have rebuilt.

**Three wrong claims in one block: a guard that was not built, a hole that is closed, and a remedy that was rejected.**

**This is the THIRD instance of tonight's pattern — and it has INVERTED.** It no longer *overstates* a guarantee; it **understates** one, and **points the next reader straight at the destructive remedy we spent the night disproving.** An agent landing there at 3am concludes the fail-open is live and goes and builds the run-id.

> *A comment is a claim with no vintage and no test.* This one now has **negative value**. Documentation, so it does not block F1. A live hazard, so **it must not survive to GO.**

**G1-D2 (lower severity, same class):** `INF_A_00:233` and `INF_A_01:173` still read *"load_resolution RAISES if the resolver did not land."* Post-8.2 that is *approximately* true but **imprecise in the dangerous direction** — it describes an **INVOCATION** assertion where the guard asserts **CONTENT**. A reader concludes a legitimate cache reuse ought to raise, and "fixes" the guard into an over-condemner.

**Evidentiary nit:** the lib cites *"6 of 69"* accounts_v2 partitions rewritten after their own `snapshot_date`. **I measure 5 of 69** (threshold: `LastModified` > `snapshot_date` + 1 day; all five share `LastModified 2026-05-11T15:41:20Z` — a single backfill event). Not a contradiction — a **threshold choice**. But **a fail-closed guard's cited justification must be reproducible**: state the threshold.

## 4. RULING — `INF_D_04:3307-3309` `derive_advisor_key` (DS's F10-derived finding)

A live **per-view servicing derivation** of `advisor_key` from `representative_name` for the household lifecycle list — bypassing the SSOT entirely. Self-annotated at `:61` as *"classified legal."*

**RULING: NOT automatically a defect — but it CANNOT ship under switch-ON UNDECIDED. Two outcomes are acceptable; "undecided" is not, and undecided is what we have.**

The deciding question is a **business** one, not a refactor: should a household **lifecycle list** show the advisor who **SERVICES** the household, or the advisor whose **BOOK** it is? DS was right to stop — he had the mechanism source-confirmed and did **not** have the intent (Rule 22).

- **DS's allowlist encoding is APPROVED as the interim** — *visible and locked* beats *invisible and unlocked*; touch it and the census fails. **It converts a comment nobody reads into a gate.**
- **The *"classified legal"* annotation is itself a finding.** **An exception annotated "legal" with no recorded reason is not an exception — it is an unlogged decision wearing a ruling's clothes.** Same disease as the three false comments above.
- **SCOPE: a SWITCH-ON blocker, not a round-8.2 blocker.** DELTA-0 today (servicing ≡ resolution under OFF). It bites **only under ON** — a mover's household would show the SERVICING advisor while every other surface shows the AoR: **the exact per-view divergence the SSOT exists to kill, appearing AT go-live rather than before it.** Routed to COO for the go-live checklist: **DECIDED before GO, not DISCOVERED at GO.**

## 5. RELEASE MECHANICS — the one that can take the nightly down

`INF_A_0` and `INF_D_11` are **`MISSING_ON_S3`**. The consumers are now **fail-closed**: once deployed, they RAISE unless a resolver ran in that chain and stamped a matching artifact.

> **The resolver+detector upload and the consumer deploy must be ATOMIC (or resolver strictly first). Deploy the consumers alone and the ENTIRE INF nightly aborts** — loudly, correctly, and catastrophically. **A NEVER#6-shaped half-landing reachable from a correct-looking deploy.**

---

*Gate-1 is a gate, not a signature. F1 earned its close by exercise — A3 through the real dispatch, and GREEN arms reachable from a different truth than the RED ones. The remainder has not been exercised at this hash, so the remainder is withheld.*
