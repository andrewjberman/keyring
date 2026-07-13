# GATE-1 VERDICT — AoR round-8.2

> ## ⬛ FINAL DETERMINATION @ `445711c2c` (round-8.2 COMPLETE): **WITHHELD** — on exactly TWO items, both small.
>
> **1. F4-B is NOT IMPLEMENTED** (`grep -c expect_nonempty` = **0**). Base CTO's three F4 points all landed and verify (`None` → RAISE; C_02's laundering try/except removed). **But `len(account_team) == 0` still returns `{}`** — and a truncated/zero-row parquet is a **SUCCESSFUL read**, so the household re-key **silently vanishes through the identical door F4 just closed.** `account_team` is C_07's output *in the same chain*, and we already run a feed (49F allocations) alternating 46K/1.2M rows because BD returns undersized stubs. **The library's own reasoning for returning `{}` is CORRECT — which is precisely why the discriminator cannot live in the library.** Chokepoint fails closed on the **UNOBSERVABLE**; the **CALLER DECLARES** whether zero is legitimate for its firm (Inflection cannot have zero households — ~286 across four advisors). *An empty frame and an empty firm are byte-identical; somebody has to SAY.*
>
> **2. F2-B — NEW: the SSOT hands the UNRESOLVED label back to each view.** `aor_resolution.py:673-680` — `absent: str | None = None`, *"None → leave the existing/NaN value untouched (**THE CALLER'S FILL SEMANTICS APPLY**)"*. The callers duly invent their own: **SEVEN scripts, FIVE names, one condition** — `inflection_unmapped_rep` (C_01:463) · `unknown` (C_01b:168, C_05:204-205) · `Unknown` (D_00d:427,548; D_04:1978,1982) · `Other` (D_00f:493; D_04:2473,2476) · `unassigned` (D_03:583,592). A NaN `advisor_key` is **reachable BY DESIGN** (`:154`), so under ON **one unresolved account appears under five different labels on five served surfaces** and its AUA/NNA silently drops out of every real advisor's numbers. **A per-view derivation SURVIVING INSIDE THE FIX — not of the resolved value, of the UNRESOLVED one.** The SSOT killed per-view derivation for the resolved 99% and **formally licensed it for the residual. Both instruments are blind: the census hunts banned SYMBOLS (`fillna` is not one); the detector diffs the LEDGER (an unresolved account has no advisor to diff).**
> **Scope: PRE-EXISTING, not a round-8.2 regression → NOT a round-8.2 blocker, but a SWITCH-ON blocker** (same class as `INF_D_04`'s `derive_advisor_key`). **RULING: ONE canonical `UNRESOLVED_ADVISOR_KEY`, DECLARED in the lib, inherited by every view, `absent=` defaulting to it, + the unresolved COUNT emitted per run.**
>
> **VERIFIED at the final hash:** the presence-gate is real and **never reads `INF_AOR_FOLD_ACTIVE` on any path** · **all 8 chains still carry the resolver — the dispatch is byte-identical to `c16b0c73b`, so none of the three later commits re-touched a chain literal** · A_00 **RAISES fail-closed** on the as-of skew (F2's producer; F2-B is about the consumers) · F7's deleted coverage detector rebuilt.
> **NOT independently exercised by me:** F3 · F5 · F6 · F7 · F8 · F9 · F10 — **gate-2 (CVO~B) carries that at the same hash, and I say so rather than pass them by omission.** *A gate that quietly counts unreviewed items as clean is the failure this whole round was about.*
>
> **AND MY OWN CENSUS INSTRUMENT FAILED FIRST:** my regex `\['advisor_key'\]\s*=` **matched `== adv` as an assignment** — it counted *comparisons* as *writes*, and `INF_D_02` first read as "11 assignments" when they are filters. **A census that cannot tell a read from a write.** F2-B is what the *corrected* instrument found. *Check a census regex against a known write AND a known read before you trust its output.*

---

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

## 5. THE WIRING — verified, and it is the actual fix

> *"The chain-wiring is THE FIX. The guard is defense-in-depth. We spent the night asking a guard to do a wiring job."* — base CTO. Correct, so I verified the wiring, not just the guard.

**The presence-gate is REAL.** `orion-gold-dispatch.sh:408 @ c16b0c73b` — `_aor_script_deployed()` is
`aws s3api head-object --bucket "$INF_S3_BUCKET" --key "code/gold/$1"`.
**Chain entry is keyed on the SCRIPT EXISTING in the deployed S3 prefix. It never reads `INF_AOR_FOLD_ACTIVE` on any path** — no default, no `:-`, no semantic-switch read. **My opening instinct — that an `INF_AOR_FOLD_ACTIVE=${X:-1}` would LOOK unconditional and still drop the resolver on an explicit `0` (precisely the switch-OFF path the rollback uses) — is now STRUCTURALLY IMPOSSIBLE.** The de-multiplex (R5) is real, not cosmetic.

**R3 chain census — the resolver is prepended to ALL EIGHT consumer-carrying chains** (:425-434):
`CHAIN_COMPUTE` · `CHAIN_FULL` · **`CHAIN_INCREMENTAL`** · `CHAIN_GOLD_A` · `CHAIN_GOLD_B` · `CHAIN_GOLD_C` · `CHAIN_GOLD_D` · `CHAIN_GOLD_CD`.
Cross-checked against my own enumeration of all **nine** `load_resolution()` call-sites: **every chain carrying one gets the resolver**; `CHAIN_PULL` / `CHAIN_SILVER_PREP` / `CHAIN_ECLIPSE` carry none. **`CHAIN_INCREMENTAL` — the killer, because it refreshes `INF_API_SILVER_ACCOUNTS_V2` (the resolver's OWN source) and then runs five consumers — now carries it. It no longer moves the ground and leaves the SSOT behind.**

**The DETECTOR is lifted off the resolver's conditional** — its own presence check, its own variable, appended to `CHAIN_COMPUTE` only (a group-stage recovery run has nothing new in the ledger and must never become an alerting surface). **A rollback can no longer drop the resolver AND its alarm in one flip.**

**Invocation axis (`--single`/`--from`) is closed by the CHOKEPOINT, not the wiring — and that is correct**: an invocation path *has* no chain literal for R4 to see. **The wiring closes the chains; the guard closes the invocations. Neither can do the other's job.**

## 6. RELEASE MECHANICS — an ORDER, not merely "atomic"

`INF_A_0` and `INF_D_11` are **`MISSING_ON_S3`**. The consumers are now **fail-closed**: once deployed they RAISE unless a resolver ran in that chain and stamped a matching artifact.

**Resolver FIRST is PROVABLY SAFE — order it, do not merely synchronise it:**

1. **Upload `INF_A_0.aor_resolver.py` + `INF_D_11` to `code/gold/` FIRST; verify presence** (`comp-pipescript deployed` → MATCH, not MISSING_ON_S3).
   → **The intermediate state is SAFE BY CONSTRUCTION:** the presence-gate admits the resolver to every chain, it runs and writes a stamped artifact, and the **still-stale consumers never read it** (pre-round-8; they do not call `load_resolution`). Nothing serves differently.
2. **THEN deploy the consumers** — they arrive fail-closed into a world where a correctly-stamped resolution **already exists**.

> **Reverse the order and every AoR consumer RAISES on the first nightly — the ENTIRE INF chain aborts.** The dispatch concedes it at :415. **A NEVER#6-shaped half-landing reachable from a correct-looking deploy — and ordering it away costs nothing.**

## 7. F4 — SUPERSEDED (accepted), + **F4-B** (mine, new)

**F4 supersession ACCEPTED**, verified at source: `aor_resolution.py:578` — `if account_team is None or len(account_team) == 0: return {}` — **collapses `None` (read FAILED) and empty (read OK) into one return.** `INF_C_02.client_performance.py:466-472` catches the read error, sets `_acct_team = None`, and calls the map **OUTSIDE the try**, so `{}` is falsy and the re-key silently vanishes. **My original F4 hardened the missing-column branch — a stale deploy, rare and self-announcing — and left the branch that actually fires: a transient read blip, common and invisible.**

**F4-B — FIXING `None` IS NECESSARY AND NOT SUFFICIENT.** A truncated/zero-row parquet is a **successful read**: throws nothing, returns 0 rows, hits `len()==0`, returns `{}`, and the re-key vanishes through the identical door. **`len()==0` is not safe merely because the read did not throw** — and it is not exotic: the 49F allocations feed **already** alternates 46K/1.2M rows because BD returns undersized stubs.
**An OBSERVED zero is only safe if zero is a value the system can LEGITIMATELY take — and Inflection cannot have zero households** (~286 across four advisors). **But the LIBRARY must not raise on empty either** — that over-condemns a genuinely zero-household firm (*the `run_id` mistake in miniature*).
> **THE DISCRIMINATOR DOES NOT LIVE IN THE LIBRARY. The chokepoint fails closed on the UNOBSERVABLE (`None`); the CALLER DECLARES whether zero is legitimate for its firm.** (`expect_nonempty`, required + declared — the same declared-not-observed principle as `source_masters` and the `(source_digest, fold_mode, code_digest)` key.) *An empty frame and an empty firm are byte-identical; the data cannot tell you which you have.*

## 8. THE COMMENT FINDINGS — four now, and the fourth is the worst class

**G1-D1** (dispatch:396-405) — describes an `as_of` assertion that does not exist, a hole that is closed, and a remedy that was rejected. **G1-D2** (`INF_A_00:233`, `INF_A_01:173`) — asserts INVOCATION where the guard asserts CONTENT. **G1-D3** (dispatch:415) — tells the operator, *in a log line read during an incident*, that the consumer fails closed at *"the run-as-of assertion."* **There is no run-as-of assertion.**

**G1-D4 — and it is a NEW and WORSE class.** `INF_C_02:462-464` reads *"…**no-ops if account_team is unavailable**."* **That comment is TRUE.** It accurately describes the defect, phrased as deliberate graceful degradation.
> **A FALSE comment gets caught the moment someone checks it against the code. A TRUE comment that describes a defect as a FEATURE is never checked at all** — it reads as considered, so the reader moves on. It survived weeks and a 32-agent review. **When the behaviour is fixed, the comment MUST be rewritten, or the next reader will "restore" the no-op believing it was intended.**

---

*Gate-1 is a gate, not a signature. F1 earned its close by exercise — A3 through the real dispatch, and GREEN arms reachable from a different truth than the RED ones. The remainder has not been exercised at this hash, so the remainder is withheld.*
