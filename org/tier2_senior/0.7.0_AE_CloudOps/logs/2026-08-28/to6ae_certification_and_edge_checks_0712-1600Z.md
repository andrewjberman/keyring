# 0.7.0_AE_CloudOps~S (lane ~S, THIRD seating) — TO-6-AE certified; two authorised edge checks

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

**Window:** 2026-08-28T07:12Z -> 16:0xZ. Prior log: `to6ae_ac3_scheduled_fire_0604-0712Z.md` (same dir).
**Written under the ~16:0xZ Andrew-direct reboot order.** Not a session-close by choice.
**Commits this window:** `c3d3d89ad0` · `4c4ddf701f` · `30813d8fc3` (+ memory, outside the repo).
**MCP:** ~30 inbound, all READ-ACKed individually as opened; 6 outbound sends.

---

## 1. THE HEADLINE — `ETFS_SATELLITES.TO-6-AE` IS CERTIFIED AND CLOSED AT THIS SEAT

`3.0.0_SA_CVO~Z` certified `T6AE-AC3` **EXERCISED** @`d680df0e74`. `T5DS-AC6` is
**RELOCATED-AND-DISCHARGED**, met BY AC3 rather than by the relocation.

⛔ **READ CRITERION-WISE, NEVER AS ONE DISCHARGE — TWO CERTIFICATES:** `AC1/AC2/AC4/AC5` @`324330f5f2`
+ `AC3` @`d680df0e74`. A bare "5 of 5" asserts a single discharge nobody performed.
⛔ **`T6AE-AC5` IS NOT RE-DERIVED** by the 07:00Z fire — 9 members published, not zero, so the
empty-publish path did not execute. ⛔ **NOT A PROJECT CLOSURE.**

## 2. THE THREE COMMITS

| commit | what | why it mattered |
|---|---|---|
| `c3d3d89ad0` | `<status>` token[0] -> bare `complete` | the emphasis mark made `_classify_status()` fall through to ACTIVE; face said DISCHARGED, register said ACTIVE. Verified `TO-6-AE` 0 occurrences against a positive control of 2 on `TO-P1-AE` |
| `4c4ddf701f` | added the pending-certification fact | `2.0.0_SA_COO~Z`'s census found this face was the ONE of 12 whose pending-cert fact was on **no artifact at all** — it lived only in a broker message and my liveness summary |
| `30813d8fc3` | retired that same marker once AC3 certified | I authored the sentence; it went false at 15:2xZ and I was the seat with a trigger to return |

⭐ **Read `_classify_status()` at source** (`.tools/to-check.py:189-203`) and settled a bound
`1.0.0_SA_CTO~Z` had stated openly: the no-match fallthrough **is** `ACTIVE`. Added what neither seat
had — **`UNKNOWN` already exists at `:198` but is bound to EMPTY, not to UNPARSEABLE**, so the fix is a
re-binding rather than a new enum member. Also measured: nothing strips **leading** markdown, so
`**complete**` fails identically — token[0] must be a **bare** word.

## 3. TWO AUTHORISED READ-ONLY CHECKS (scoped GO, `2.0.0_SA_COO~Z` msg 13197)

Raised when `1.0.0_SA_CTO~Z` found a client-facing panel printing internals and named an audience
determination as **owed before anything on that panel is prioritised**, with no seat assigned.

**Mechanism finding (mine, and it relocated the remedy):** `CategoryViewTree.tsx:212` carries only the
amber TITLE; the body is **the emitter's own `predicate_reason`, rendered verbatim**. ⛔ **No portal
change can fix it — a producer writes engineer-facing prose into a field the DOM prints.**

```
CHECK 1  DEPLOYED-plane auth   /api/general/* carries auth-validator-edge:18 LIVE on EVTSA9VEHNZVH
                               (Deployed, 27 behaviors + default). DESIRED == APPLIED.
CHECK 2  /json-tiered/*        origin originPath="" -> key space is EXACTLY json-tiered/
                               375 objects, ALL market-overview.
                               json-tiered/platinum* = 0   vs control platinum/mdpf/cottonwood/ = 5
                               >> key spaces DISJOINT BY PREFIX. NOT a second door to platinum.
```
⚠ **Bounds stated and held:** key NAMES not payloads; path-normalisation **untested**; second-door
question only. ⛔ **I did NOT convert `AUTH:yes` into `not client-reachable`**, even after the deployed
plane agreed — authentication is not authorisation. **Andrew closed the audience question himself:
*"opal staff and advisors only."***

## 4. VERIFICATION (actual output)

```
d680df0e74   exists, 127 insertions, creates cvoZ_ETFS_SATELLITES_TO6AE_AC3_CERTIFICATION_20260828.md
NEG CONTROL  fabricated sha d680df0e74deadbeef -> "Not a valid object name"  (the read discriminates)
criterion set @324330f5f2 vs @HEAD: T6AE-AC1..AC5 IDENTICAL; <expected_criteria> IDENTICAL
POS CONTROL  git show returned 83 lines at that ref (an MSYS mangle returns CLEAN-EMPTY)
```

## 5. COMPILER TOOLS

| tool | run | result |
|---|---|---|
| `comp-which` | "which portal routes are gated by auth and which are public" | PASS — routed to `comp-routes behaviors` |
| `comp-routes behaviors` | full behavior + auth-map census | PASS — 28 behaviors, DESIRED plane |
| `comp-routes trace` x2 | the two candidate paths | PARTIAL — `/api/general/*` resolved; `/json-tiered/*` **UNRESOLVED**, which its own banner says is missing COVERAGE, not absence. That is why check 2 went to the live key space |
| `comp-routes edge-versions` | pinning axis | PASS — all 5 routers DYNAMIC `qualified_arn [OK]` |
| `comp-find` x2 | the client-facing strings | PASS — located `CategoryViewTree.tsx:212` + the two corroborating TO artifacts |

**What worked:** `comp-which` picked the right tool first try. **Gap found:** `comp-routes` is
DESIRED-plane and says so in its own banner — it cannot answer a deployed-plane security question, so
the live reads were required (Rule 22a).

## 6. BLOCKERS

**NONE at this seat.** Nothing outstanding.

**Owned elsewhere, listed so they are not read as mine:**
- [`0.0.0_AB_MSTR~Z`] `30813d8fc3` and everything since `d2d78d73b0` need the push. **GATE 5.**
- [`2.0.0_SA_COO~Z`] the TO-6-AE **disposition** and any AC-table edit; `POSN_TENANCY.TO-4-AE`
  (issued to `0.7.0_AE_CloudOps~Y`, NOT `~S` — I declined that call in 13271 and the decline was
  ratified); `ETFS_POSITIONING` TO-1/TO-5, which need an **executor** act, not a certifier one.
- [Andrew] the Bloomberg field-width vendor call — **HELD**.

## 7. CURRENT STATE (zero prior context)

- `ETFS_SATELLITES.TO-6-AE` — 5 of 5 across **two** certificates. Face at
  `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ETFS_SATELLITES.TO-6-AE.registry-producer-schedule.md`;
  evidence in `org/tier2_senior/0.7.0_AE_CloudOps~S/deliverables/` (AC3_FIRE_EVIDENCE, POSTFIRE_RUNBOOK,
  PREFIRE_BASELINE). The producer `cot-satellites-registry-producer` wrote the registry successfully for
  the first time at 07:00:19Z.
- ⛔ **The face is register-invisible BY DESIGN and that is correct** — token[0] `complete` means the
  WORK is complete. The register cannot express "built but not certified" (per-criterion vector vs
  per-TO scalar). Diagnosed, deliberately NOT patched.
- **Nothing was invoked all session.** Every AWS call was head/get/list/describe/filter. No alarm,
  monitor, checker or notification was built. Zero crons.
- **Push state, MEASURED at ~15:2xZ:** `30813d8fc3` **LOCAL**; `origin/SITEZ` = `d2d78d73b0`.
  ⚠ **Perishable — re-measure before quoting.**

## 8. NEXT STEPS

- [`0.0.0_AB_MSTR~Z`] Push. That is the only act between this seat's work and durability off-device.
- [this lane] **Nothing.** Do not re-execute anything in section 2 — all three commits are landed and
  the third one deliberately supersedes the second.
