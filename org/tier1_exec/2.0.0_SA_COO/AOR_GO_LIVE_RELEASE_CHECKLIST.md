# INF ADVISOR-OF-RECORD — GO-LIVE RELEASE CHECKLIST

**Owner:** `2.0.0_SA_COO` (I hold this and the never-widen co-sign)
**Status:** **PAUSED — both gates WITHHELD.** Not a schedule; a gate list.
**Last amended:** 2026-07-13T05:50Z — rollback leg re-pointed at `run_id` per CTO 054815Z (see §4, and read the
correction: my first version of that leg was itself defeated).

---

## 0. STATE (re-read this before touching anything)

**Nothing is served. Switch is OFF. SERVE-HELD. Zero live impact.** Every defect below is in the state a GO would
CREATE, not the state we are in. There is **no clock on this release** — the only pressure is not to ship a fix
that closes the loud path and leaves the silent one.

| Gate | Holder | Status |
|---|---|---|
| **gate-1** (architecture) | `1.0.0_SA_CTO~B` | **WITHHELD** |
| **gate-2** (validation) | `3.0.0_SA_CVO~B` | **WITHHELD** |
| **never-widen co-sign** | `2.0.0_SA_COO` (me) + CTO | **PAUSED** — requires both gates cleared first |
| **final GO** | **Andrew** (sovereign) | not requested |

Both gates were withheld **independently, for the same defect, neither having read the other.** That is the system
working. Do not read a withheld gate as a delay.

---

## 1. THE DEFECT CLASS THIS RELEASE EXISTS TO NOT SHIP

The rollback **fails OPEN, silently.** `RESOLUTION_KEY` is a fixed overwrite-latest key and the rollback is
flip-only, so **nothing deletes the artifact**; `load_resolution()` validates readable/non-empty/2-col and **never
reads the `as_of` it returns.** So post-GO, switch-OFF leaves the last ON run's resolution in place, it loads
clean, and consumers silently attribute off a **frozen** resolution — while `INF_D_11`, the detector that would
notice, is dropped by the *same* conditional.

**A green nightly is exactly what this failure produces.** Every assertion below exists because *absence of a
failure is not evidence of success.*

---

## 2. HARD PRECONDITIONS (all must be TRUE before a GO is even requested)

- [ ] **round-8.2 landed** — R1-RUN + R1-SRC + R1b + R2 + R3 + R4 + R5, and F2/F3/F5–F10. *(`0.4.0_DS`)*
- [ ] **R3 is LOAD-BEARING, not optional.** R1-RUN makes a skip LOUD; **R3 makes the skip not happen.** Without
      R3, a run-id assertion turns every `--chain incremental` recovery run into a **hard abort.** Ship them together.
- [ ] **CHANGE-3 silver raw passthrough** (`63dd76201`) deployed — a **HARD** go-live precondition. Until it lands,
      `advisor_of_record_raw` is genuinely ABSENT on live av2 and an ON-path run correctly RAISES.
- [ ] **gate-1 CLEARED** by `1.0.0_SA_CTO~B` on the **amended** F1 (not the original).
- [ ] **gate-2 CLEARED** by `3.0.0_SA_CVO~B` — **exercised THROUGH THE DISPATCH**, never resolver-direct. A
      resolver-direct harness always holds a freshly-written resolution and **cannot express** the
      artifact-present-but-resolver-skipped state. Its PASS is structurally incapable of seeing this class.
- [ ] **never-widen co-sign** (CTO + COO) — mine is PAUSED until the two above.
- [ ] **Andrew's explicit GO.**

---

## 2·0. ⛔ **"F1 IS CLOSED" IS NOT "8.2 IS CLEAR." DO NOT SCHEDULE THE CO-SIGN.**

*(CTO 061743Z, aimed at ME. Recorded here so it cannot be compressed later by the person it is aimed at.)*

**F1 CLASS: CLOSED** — by exercise, at DS's **committed** hash `c16b0c73b` (CVO~B, **8/8 arms**, matrix
`1e7d127e2`). Complete key `(source_digest, fold_mode, code_digest)`. A3 RAISES **through the real dispatch**;
A7 (retired resolver lib) RAISES; A8 (pin unset) RAISES fail-closed; **A5 (a legitimate `--single INF_D_00c`
rerun) still RETURNS** — *the guard discriminates; it is not a brick, and it will not be disabled at 3am by the
operator it condemns.*

> ### **THE BLOCKER HAS MOVED. IT HAS NOT LIFTED.**
> Gate-2 is **no longer blocked on F1**. It is blocked on **the REST of round-8.2** — **F2** (NaN advisor_key on
> the A_00/resolver as-of skew), **F3** (readable-but-incomplete cache greening a real change), **F4** (household
> RAISE + C_02's try/except gap), **F7/F8** (detector completeness), and **the 35/35 regression battery**.
> **CVO~B has run NONE of those at this hash.** She is starting them now.
>
> **That is a change in KIND — from an unresolved design question to ordinary verification work. It is real
> progress and it is NOT a green light.**

**THEREFORE, BINDING ON ME:**

- [ ] **I will NOT schedule, forecast, or hint at co-sign timing before those arms are green.** Not to CVO~B, not
      to Andrew, not in a status line. **A verification lane asked "when will you be done?" is a lane under
      pressure to be done**, and the entire value of gate-2 is that it is not.
- [ ] **CTO has told CVO~B that if he or I start talking co-sign timing, she should say so.** *I endorse that
      standing permission and I am recording it against myself.* If I create that pressure, she is right and I am
      wrong.
- [ ] **"F1 closed" gets reported as exactly that** — never as "8.2 nearly done," never as a percentage, never as
      an ETA. **Compression of this distinction IS the failure mode.**

**CVO~B ALSO EXERCISED A SEAM NOBODY HAD LOOKED AT — including CTO.** If the dispatch's **pin** and the
resolver's **stamp** ever named *different objects*, **EVERY consumer would raise on a HEALTHY nightly** — a total
abort **indistinguishable from the guard working correctly.** *A live outage risk sitting INSIDE the fix.* She
measured both against real S3; they agree. **That is a verification lane finding the failure mode of the thing it
was asked to bless.**

**DS fixed R-A STRUCTURALLY** — the ETag comes off the **very GET that produced the DataFrame** — rather than
bolting on another assertion. *The right instinct, and it belongs in the release record: the fix that cannot lie
beats the assertion that checks for lies.*

---

## 2·0b. MUST-FIX-BEFORE-GO — **G1-D1: a comment with NEGATIVE VALUE**

*(CTO~B gate-1, finding G1-D1. Non-blocking for F1; a live hazard; MUST NOT survive to GO. Routed to DS 062056Z.)*

- [ ] **`orion-gold-dispatch.sh:396-405` — rewrite it.** At `c16b0c73b` it still makes **three false claims**, in the
      very file the guard protects:
      1. that `load_resolution()` asserts **`as_of`** — **it deliberately does NOT** (a proxy that under-fires;
         the key repeats across different bytes);
      2. that the carried-over-resolution hole is **still open** — **it is CLOSED** (A3 exercised RED at this hash);
      3. that the remedy is a **RUN-IDENTITY stamp** — **`run_id` was CONSIDERED AND WITHDRAWN for OVER-FIRING.**

> **This is the pattern's THIRD instance tonight — and it has INVERTED.** It no longer overstates a guarantee;
> **it UNDERSTATES it and points the next reader straight at the destructive remedy we spent the night proving
> wrong.** An agent landing there at 3am mid-incident reads *"the fail-open is live, the fix is a run-identity
> stamp"* and goes and **builds `run_id`** — bricking every recovery run, at exactly the moment recovery runs
> matter most. **A comment is a claim with no vintage and no test.** This one has *negative* value.
> The rewrite must say **"`run_id` was withdrawn as over-firing — do not build it"** *explicitly*. The comment's
> job now is to stop the next person re-deriving a rejected fix.

### ⚠ PRESERVATION NOTES — things that are CORRECT and that a future reader may "helpfully" break

- **R4 covers ONLY chain literals, and that is RIGHT.** An invocation path (`--single`/`--from`) **has no chain
  literal**, so R4 *structurally cannot* cover it and **does not need to**. **The CHOKEPOINT covers the invocation
  surface; R4 covers the dispatch surface. Together they close both.** *Do not let anyone "fix" R4 to chase a path
  it was never meant to see.*
- **The completeness claim survived an ADVERSARY.** CTO~B flagged `explicit_map` as a possible unenumerated
  **fourth** input and then closed it at source (`aor_resolution.py:753` — `fold_map, explicit_map =
  build_advisor_of_record_fold(av2)`; **both derive from `accounts_v2`**, no independent second source, no
  independent vintage). **The enumeration holds.** That is the strongest confirmation available: *an adversary who
  went looking for the hole and reported there wasn't one.*
- **The test suite is NOT a placebo** — it carries GREEN arms reachable from a *different truth* than the RED ones
  (**A5** legit-cache-reuse → RETURNED; **A6** servicing-only-under-OFF → RETURNED, peter_lee, correct DELTA-0).
  **Without those two, the other six would be a brick that raises at everything.** It discriminates.
- **R4 carries its own negative control** (`test_r82_r4_negative_control_the_invariant_can_actually_fail`) — the
  invariant is proven **able to fail**. *An assertion never mutated has never been tested.*

---

## 2a. ⛔ CO-SIGN SEQUENCING — **I DO NOT CO-SIGN AGAINST TONIGHT'S NUMBERS**

*(CTO 061116Z. This is MY gate and this is the rule I hold myself to.)*

**Gate-2's verification is GREEN — and it is against DS's UNCOMMITTED WORKING TREE.** The lib moved under CVO~B
**three times tonight**, and two of her own citations went stale mid-analysis. **She will not sign gate-2 off a
moving target, and she is right** — Rule 22: *a line citation without a vintage is not a citation.*

**THEREFORE THE CO-SIGN RIDES A RE-RUN AT A COMMITTED HASH. THE ONLY LEGAL SEQUENCE:**

1. **DS COMMITS round-8.2** → hands CVO~B a **hash**.
2. **CVO~B RE-RUNS the full matrix AT THAT COMMIT.** (Not tonight's run. Not a working-tree run.)
3. **gate-2** (CVO~B) → **gate-1** (CTO~B) → **THEN my co-sign** → **then Andrew's GO.**

**A green verification against an uncommitted tree verifies NOTHING THAT WILL SHIP.** The tree is not the artifact.
**I will refuse a co-sign that cites a working-tree result, however green.**

**SoD NOTE:** base-CVO has **RECUSED** himself from certifying this fix — he is now an **author** on it (he found
the `code_digest` input). **Gate-2 is CVO~B's ALONE.** Correct call, endorsed by CTO, and I will not accept a
base-CVO sign-off as a substitute.

### THREE RESIDUALS — one is a SHIP-BLOCKER (with DS as conformance corrections, not new findings)

- [ ] **R-A — SHIP-BLOCKER. A FAIL-OPEN *INSIDE* THE GUARD BUILT TO CLOSE A FAIL-OPEN.** `source_digest()` HEADs
      **the PIN** while the loader **WALKS BACK** — so the resolver can stamp the digest of partition `P` while the
      fold was actually derived from `P-1`. **A false identity that fails OPEN, inside the mechanism.** Not
      shippable. *(This is the sixth instance tonight of **the repair inheriting the defect it repairs.**)*
- [ ] **R-B — `code_digest` NOT BUILT** (refs=0). The third input. Without it, a mid-day resolver-lib deploy + a
      resolverless run **passes the guard on RETIRED LOGIC.**
- [ ] **R-C — a live S3 HEAD on EVERY `load_resolution()` call**, inside 32-worker loops → a per-worker HEAD **and
      mid-chain NONDETERMINISM** (consumer A passes, consumer B raises, *same run, no bug*). A guard that answers
      differently to two consumers in one run is not a guard.

### WHAT IS ALREADY PROVEN (do not re-litigate)

- **ETag-keyed mutant matrix: 6/6** — including **A5: legitimate `--single` cache reuse → RETURNS.** The digest key
  does **not** brick the targeted-rerun ops surface. **It is a discriminator, not a brick.**
- **A3 THROUGH THE DISPATCH: GREEN**, raising on the **mode** branch — and the fixture was built so the artifact
  agrees on **every field except `fold_mode`** (`as_of` matches, digest matches; **the source is innocent**). That
  is what a *prompt* rollback actually leaves behind, and it is the only construction that proves anything.
  **The arm that killed the fix now clears it.**

---

## 2b. ⚠ THE REFRAME — **THE CHAIN-WIRING IS THE FIX. THE GUARD IS DEFENSE-IN-DEPTH.**

*(CTO 060522Z, R1 CLOSED. This re-ranks the whole release and it supersedes any earlier ordering in this file.)*

Every key we argued about for an hour — `as_of`, `run_id`, `(digest, mode)`, the final triple — answers exactly one
question: ***"is this LEFTOVER artifact safe to reuse?"***

**That question only exists because a chain can run WITHOUT the resolver.** Presence-gate `INF_A_0` into every
chain and **there IS no leftover**: the artifact is always rebuilt by the run that consumes it, and the entire
identity question **evaporates**.

> **We spent the night asking a GUARD to do a WIRING job.**

**THEREFORE, RANKED:**

1. **PRIMARY — presence-gate `INF_A_0` into ALL chains** (`CHAIN_COMPUTE` + `CHAIN_INCREMENTAL` + `CHAIN_GOLD_*`)
   and lift `INF_D_11` off the shared conditional. **This is the release item.**
2. **BACKSTOP — the `(source_etag, fold_mode, code_digest)` guard.** Defense-in-depth, not the fix.

**If the wiring lands and the guard does not, we are mostly safe. If the guard lands and the wiring does not, we
are ONE `--chain` FLAG from frozen attribution.** Rank them accordingly, and do not let the guard's cleverness
buy the wiring's priority.

---

## 3. ORDERING (what may deploy when)

**The dispatch is ORDER-INDEPENDENT under R5 — do not gate the release on proving deploy atomicity.**
`INF_AOR_FOLD_ACTIVE` was doing two jobs (semantic fold-vs-servicing **and** a deployment guard at `dispatch:353`).
R5 de-multiplexes them: the switch stays SEMANTIC; chain **entry** is **PRESENCE-gated**. Therefore:

- deployed EARLY (resolver `.py` not yet on S3) → resolver absent → not in chain → nightly runs as today. **Harmless.**
- deployed LATE → runs. **Harmless.**
- **any skew, either direction → harmless.** The deploy-skew hazard does not need proving away; **it stops existing.**

**THE ONE REAL ORDERING CONSTRAINT** (structurally held, so it is a checklist item, not a gate): **consumers must
not deploy ahead of the resolver.** A consumer calling `load_resolution()` with no artifact RAISES. Both are `.py`,
both carry the `DEPLOY-SERVE-HELD` sentinel, safe-deploy holds them as one group, and the failure mode is a **LOUD
abort (serve stale, never garbage)**. Verify the group lands together; do not treat it as a design risk.

- [ ] Resolver + detector + migrated consumers land as ONE serve-hold group.
- [ ] `INF_A_0` / `INF_D_11` confirmed **PRESENT on S3** (`comp-pipescript deployed`) — they are `MISSING_ON_S3` today.

---

## 4. THE ROLLBACK LEG — **THE ASSERTION IS `(source_content_digest, fold_mode)`**

> **CORRECTION ON THE RECORD — THIS LEG HAS NOW BEEN DEFEATED THREE TIMES. Every defeat came from EXERCISE, never
> from a re-read. All four versions are kept in place, because the pattern is the lesson.**
>
> - **v1 — "the nightly did not fail."** DEFEATED: **a green nightly is exactly what a fail-open rollback produces.**
> - **v2 — "the resolution's `as_of` ADVANCED."** DEFEATED (CTO 054815Z): **`as_of` can legitimately NOT advance on
>   a perfectly good run** (weekend / holiday / same-day re-run against a non-advancing partition). An assertion
>   that fires on a legitimate case is not an assertion; it is an alarm we will tune until it stops.
> - **v3 — "`run_id` is THIS run's."** DEFEATED (CTO 055214Z, base-CVO's falsifier): **it OVER-condemns.** The
>   resolution is a **pure function of its inputs**, so a legitimate recovery run reusing an identical artifact is a
>   **CORRECT CACHE, not staleness.** `run_id` hard-aborts on an artifact *provably identical* to what the run would
>   have produced — **a condemnation instrument with a destructive remedy** (the 3am re-run hits the raise and the
>   operator reaches for the switch). *I had already committed v3 as the answer.*
>
> **v2 UNDER-condemned; v3 OVER-condemned. I walked into BOTH ends of the same axis.** The error I kept making is
> the one this release exists to catch: **choosing a discriminator that is invariant under the failure it must
> detect** — and then, over-correcting, one that fires on the healthy case too.

**THE MEASUREMENT THAT KILLED v2 — and I verified it MYSELF rather than relay it, because the ruling turns on it:**

`accounts_v2` partitions are **MUTABLE — they are rewritten IN PLACE.** Each partition is ONE FIXED KEY
(`snapshot_date=<d>/data.parquet`), so a re-emit **overwrites the content under the same key.** CTO measured 6 of
69 rewritten after their own snapshot_date. My independent check (`s3api head-object`, **UTC** — *not* `s3 ls`,
which renders LOCAL time and is tonight's other trap):

```
snapshot_date=2026-04-28  ->  LastModified Mon, 11 May 2026 15:41:20 GMT   *** REWRITTEN
snapshot_date=2026-04-29  ->  LastModified Mon, 11 May 2026 15:41:20 GMT   *** REWRITTEN
snapshot_date=2026-05-07  ->  LastModified Mon, 11 May 2026 15:41:20 GMT   *** REWRITTEN
snapshot_date=2026-05-10  ->  LastModified Mon, 11 May 2026 15:41:20 GMT   *** REWRITTEN
snapshot_date=2026-07-12  ->  LastModified Sun, 12 Jul 2026 13:22:42 GMT   (same-day control)
```
All four at one identical timestamp — a single 05-11 backfill. **THE KEY REPEATS ACROSS DIFFERENT BYTES.**
So a resolution derived from the OLD 05-10 content passes a guard checking `as_of=05-10 + mode=ACTIVE`, while
consumers attribute the NEW content — **silently.** `(as_of, fold_mode)` is a complete identity **only if
partitions are immutable. They are not: 6 in 69.**

**THE DISCRIMINATING ASSERTION (v5 — FINAL, R1 CLOSED 060416Z):**

> **v4 (`source_content_digest, fold_mode`) WAS STILL INCOMPLETE.** Base-CVO found the **THIRD input nobody had
> keyed on: THE CODE.** The real surface is **`resolution = f(source_content, mode, THE CODE)`** — and he proved
> there is no fourth (`derive_advisor_key` is a pure slug, no I/O). **A mid-day resolver-lib deploy followed by a
> resolverless run: ETag matches, mode matches, the guard PASSES — and the artifact was computed by RETIRED
> LOGIC.** Reachable tonight, given how many times that lib has been touched.
>
> **THE KEY STOPPED MOVING ONLY WHEN THE INPUT SURFACE WAS ENUMERATED.** Every earlier key — mine and CTO's —
> was incomplete for the same reason: **we kept proposing keys without ever asking what the function's INPUTS
> were.** *Enumerate the state space before choosing a discriminator.*
>
> *(Multipart-ETag caveat killed by measurement: 69/69 objects are SINGLE-PART, so the ETag IS the content MD5 —
> it can only over-condemn, never fail open.)*

- [ ] **The resolution's `(source_etag, fold_mode, code_digest)` equals what THIS run would read.** Stamp the
      resolution with the **S3 ETag of the `accounts_v2` partition the resolver ACTUALLY READ** + the fold mode +
      **the digest of the resolver code that produced it**; assert all three. The ETag is **free** — same GET the
      loader already does. **The digest identifies the BYTES, not the name of the bytes; the code_digest
      identifies the FUNCTION, not the name of the function.**
- [ ] On a **correct** post-GO rollback: the resolver still runs, re-derives under `mode=OFF`, stamps the CURRENT
      digest + OFF → **the leg PASSES** and servicing attribution is served.
- [ ] On a **broken** rollback (resolver skipped): the stamped mode is `ACTIVE` while the run is `OFF` → **RAISE.**

**TRUTH TABLE — why this key dominates (it is the only one of the four right in every arm):**

| arm | verdict | note |
|---|---|---|
| legitimate cache reuse (identical inputs) | **RETURNS** | no over-condemnation — v3 failed here |
| A3: folded artifact on a switch-OFF run | **RAISES** | the original defect |
| **rewritten partition (same key, new bytes)** | **RAISES** | **neither v2 nor v3 catches this** |
| source advanced | **RAISES** | CVO~B's A2 arm |
| weekend non-advance, resolver ran | **RETURNS** | weekend-safety preserved |

**`run_id` is WITHDRAWN entirely. `as_of`-advanced is NOT the leg.** Do not reintroduce either.
- [ ] **The `as_of` field cannot be FABRICATED.** *(R1b.)* `aor_resolution.py:382` currently reads
      `as_of = os.environ.get('INF_AOR_ASOF','').strip() or str(pd.Timestamp.now(tz='UTC').date())` — when the pin
      is unset it stamps **wall-clock TODAY**, and `dispatch:1302` explicitly leaves it unset with a WARN when it
      cannot resolve the partition. **The failure path that most needs the assertion is the one handed a
      fabricated-fresh value.** An unresolvable pin must RAISE. *(Precedent: `inflection_rep_scope.py:250-254`
      already does this.)*
- [ ] **The detector is not gated on the thing it watches.** *(R2.)* `INF_D_11` comes off the semantic switch onto
      presence. **A detector gated on the same condition as the mechanism it watches is not a detector** — today a
      rollback drops the guarantee and its alarm in one flip.

---

## 5. RECOVERY RUNS ARE THE EXPOSURE — NOT THE NIGHTLY

The scheduled nightly is **SAFE** (cron + bronze-complete both fire `mode=full`, `eventbridge.tf:174,237` —
verified independently by CVO~B, not taken on report). **The exposure is RECOVERY runs, which fire exactly when
things are already broken.**

- [ ] `CHAIN_INCREMENTAL` (`:361`) — carries **5** AoR consumers, no resolver, **and runs
      `INF_API_SILVER_ACCOUNTS_V2`: it REFRESHES THE RESOLVER'S OWN SOURCE.** *It moves the ground and leaves the
      SSOT behind.* This is the sharpest single fact in the release.
- [ ] `CHAIN_GOLD_A/B/C/D` (`:365-369`) — 2+ AoR consumers, no resolver.
- [ ] The `:354` prepend touches `CHAIN_COMPUTE` **only**. R3 fixes today's five literals; **R4 (build-fail test)
      is what stops chain-literal #6** — and #6 will look exactly as safe as these five did.

---

## 6. POST-GO VERIFICATION (V4) — on the SERVED artifact, on the SCHEDULED nightly

**NEVER#4: validate on the scheduled nightly's artifacts. Never trigger an ad-hoc gold run to validate.**
**NEVER#5: never trust a producer's self-report or rc=0 — read the SERVED artifact.**

- [ ] Served `advisor_key` reflects AoR on the nightly's own output.
- [ ] `INF_D_11` (drift detector) **ran** and reported — its silence is not a pass.
- [ ] The mover census matches the pre-GO expectation (164 movers / firm $202.32M conserved / 871 — CVO~B's
      pre-grounded figures), and a DELTA is investigated, never explained.
- [ ] FE promote (`0.4.2_RD` — noel card, done-but-HELD, unpushed on portal DEV) — **re-spawn at go-live only.**

---

## 7. STANDING (survives any reboot)

- **SMS / alert-delivery: CANCELLED and STRUCK from this chain.** Andrew-direct — no alerts until the process is
  done and proven; miscalibrated alerts are device spam. Detectors WRITE findings; nothing pages Andrew.
  **Never gate a go-live on alert DELIVERY.**
- **A WITHHELD gate is a valid output and I back it.** Could-not-verify is a finding. Nobody greens anything to a clock.
- **Sovereign 49F/Schwab/bd hold STANDS** except inside OPAL_ASSETS' commissioned scope.
