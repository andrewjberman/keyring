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

## 4. THE ROLLBACK LEG — **THE ASSERTION IS `run_id`, NOT `as_of`**

> **CORRECTION ON THE RECORD.** My first version of this leg asserted *"the nightly did not fail."* That is
> defeated: **a green nightly is exactly what a fail-open rollback produces.** I then amended it to *"the
> resolution's `as_of` ADVANCED."* **That is ALSO defeated** — CTO 054815Z: **`as_of` can legitimately NOT advance
> on a perfectly good run** (a non-advancing source partition — a weekend, a holiday, a same-day re-run). An
> assertion that fires on a legitimate case is not an assertion; it is an alarm we will tune until it stops.
>
> I made, twice, the exact error this release exists to catch: **I picked a discriminator that is invariant under
> the failure it is meant to detect.** Recording it rather than quietly fixing it, because the pattern is the
> lesson.

**THE DISCRIMINATING ASSERTION:**

- [ ] **`run_id` is THIS run's.** `INF_AOR_RUN_ID` is exported once per chain start, **per-INVOCATION, never
      data-derived**; the resolver stamps it; `load_resolution()` asserts it. A resolution carried over from any
      other run — including a same-day re-run against the same partition — **fails this check by construction.**
      *(This is R1-RUN. The event ledger already got this right — per-run key, uncollapsible. The resolution was a
      fixed key stamped with a repeating value. **The fix is a better IDENTITY, not a better comparison.**)*
- [ ] **`as_of` matches the pinned source partition.** *(R1-SRC — KEPT, not replaced.)* **`run_id` catches the WRONG
      RUN; `as_of` catches the WRONG SOURCE.** Both earn their place; CVO~B's A2 arm fires on `as_of`. Neither is
      redundant.
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
