# 1.0.0_SA_CTO — MDPF reset, the directive, and the first publish

**archetype:** COORDINATE
**Session:** 2026-07-28, ~2000Z → ~2350Z (this log covers ~2140Z→2350Z; the earlier window is logged in
`MDPF_A2_SERVING_ORIGIN_RULING_AND_THE_SILENT_SENTINEL_20260728.md` + `MDPF_CTO_RULINGS_AND_OPEN_GATES_20260728_2140Z.md`).
**Lanes:** `0.7.0_AE_CloudOps` · `0.4.0_DS_ClientPlatform` · `0.2.0_DT_PortfolioAnalytics` (spawned ~2342Z) ·
`2.0.0_SA_COO` · `3.0.0_SA_CVO` · `0.0.0_AB_MSTR`.

## 1. What this window was

Andrew reset the fabric (~2218Z: *"too much information floating around... firing from the hip"*), issued the
three-part MDPF order of operations (~2157Z), the DONE definition (~2230Z), the ETF pivot ranking (~2242Z),
and the consumer re-point order (~2334Z). The window's product is **the reset directive**
(`org/critical_paths/MDPF_RESET_DIRECTIVE_20260728T2220Z.md`, 12 commits `8a613e6541`→`3ea9ab61e6`) and its
execution: **by 23:20Z the publisher existed, was scheduled, and had published the canonical tree to
`platinum/` — 11/11 both directions against a pre-pinned design set — and by end of window the consumer
re-point (WO-3) was in gated execution.**

## 2. Milestones landed (all verified on live primitives, ledgers closed)

- **`cycle-complete.json` emitted for the FIRST TIME in the product's history** (22:55:12Z) — after the
  Stage-6 grant acceptance (`:523` wrote+verified) and a one-cent tolerance recalibration (ruled ±$0.02 vs
  AC7's $0.011 precedent, delta logged every run, gate stays a gate; S3-staged copy only, divergence recorded).
- **First canonical publish** (23:20Z): egress role, own `cron(15 16)` with reasoned phase, PIN-4 event log
  from birth, provenance stamp per object, live-serve grant flipped under complete paper (Andrew 2157Z + CTO +
  COO 221211Z scoped `platinum/mdpf/*` only). **Cottonwood reached platinum for the first time ever.**
- **Emitter totals-refusal live** (v0.34.0, exercised): `_total__partner_aua` refuses partial/zero sums with
  named legs, where old code minted $0-stamped-fresh (the 07-18 $137.17mm incident class, dead).
- **DS trio:** fold carried-within-declared-cadence (headline $1,826.1mm → **$1,950,519,805.86**, exercised,
  450 gates PASS) · `_interpolated` read-preference removed (45 interpolated slots gone = proof-of-consumption)
  · window double-count corrected (5→3 per the roster's own `_basis_note`; age-4 boundary test).
- **G7 complete:** the "976-line generation gap" was a CRLF diff artifact (real pair gap: 26 lines, two-way
  merge); the substantive gap is the slice; **Finding-A mechanism source-confirmed: a two-date fact on a
  one-date key** (dim keyed by assignment date, values as-of value_date, slice counting coverage on the
  partition key) — one family with the DDB 2-of-447 class; fix approved post-fires with a loud
  collision-assert.
- **Roster runtime presence closed** (the F-3/G5 gap): published to the script-adjacent key, durability
  grounded (per-file cp deploy side; `--delete` is the propagating direction), CODE_TREES slot resolved with a
  recorded republish owner; emitter consumes it VENDORED via BUILD_MANIFEST — two consumers, one authority.
- **E1 ruled** (retire-and-consolidate the dead 49F ETF producer, gated on a basis verification) and the
  **WO-4d evidence** established never-wired-BY-DESIGN with both premises superseded.

## 3. Rulings issued this window (details in the directive amendments)

Reading-1 cottonwood (canonical only; GO cancelled) · fold carry-within-declared-cadence (neither naive
roll-forward nor absent-at-frontier) · 4a-before-4c (*never restore flow into an unguarded coalescer*) ·
WO-5 census keys on DECLARED cadence, observations corroborate (COO's correction, accepted) · deploy freeze
until the three fires (with the Andrew-ordered flip as its designed exception) · Mechanism A for WO-3 (*the
portal speaks URLs, the edge speaks keys*) with refresh-before-flip · flip acceptance = **continuity across
07-22/23** (COO's measured −$130.95mm cliff), not the headline · vintage_state enum stays as_of-derived
(contract coupling deferred to the instrument pass) · the 07-20-true/07-22-labeled vintage + ~$759k delta
DISCLOSED on the flip rather than blocking it.

## 4. Corrections involving me this window

1. **WO-5 spec keyed on observations one message after ruling nobody may** — COO applied my own law back;
   accepted without modification (`3fa042158b`).
2. **Relayed an unmeasured mechanism into a dispatch** (emitter "selects a stale source") — refuted by COO's
   32-cohort trace while AE coded against it; stopped in time (Amendment 3).
3. **Read AE's lapsed heartbeat + stale registration summary as a session death** — built a state-sync for a
   successor that didn't exist; AE's correction crossed it. Cost: one redundant message.
4. **Promised DS's spawn-queue message "before the session comes up" and hadn't sent it** — MSTR's spawn
   report surfaced the gap; delivered before DS finished startup.
5. **A malformed template send from my terminal** — refused by the sender-identity guard, nothing delivered.
6. **My "976-line generation gap" framing** propagated an instrument artifact (CRLF) as a magnitude — the
   do-not-deploy ruling survived on its real leg (the slice), but the number was the diff tool's, not the code's.

## 5. Compiler Tools

| tool | result |
|---|---|
| `comp-routes behaviors` | grounded the WO-3 mechanism question (behavior 18 router wiring); its DESIRED-plane disclosure respected — mechanism labeled INFERRED, DT's Step-0 source-confirms |
| `comp-pipescript deployed --pipeline mdpf` (via ~C earlier; path-form lesson enforced in every dispatch tonight) | the STALE findings that seeded G7 |
| `comp-grep` | `build_global_artifact` 3-leg confirmation (the falsifier of my earlier chain) |
| live primitives (`s3api`, `lambda get-function-configuration`, `events list-rule-names-by-target`, DDB via lanes) | every state claim in the directive's amendments carries its own grounding time |
| `comp-freshness` | GAP (bare invocation returns help; DDB cohort tables unsupported) — recorded in the earlier deliverable, unchanged |

## 6. Open at window end (owners on every row)

| item | owner | clock |
|---|---|---|
| refresh trio → platinum content = 1,950,519,805.86 | AE | tonight, in flight |
| WO-3 Step-0 report → flip (gates: AE confirmation + DT's own headline+continuity read + CTO GO) | DT | tonight |
| three unattended fires = D2 evidence (15:00Z / 16:15Z / 17:15Z) | schedules + CVO stage-2 (PIN-5: role attaches to the serial) | tomorrow |
| 4c apply (post-17:15Z, before/after pair as acceptance) → 4b backfill | AE | tomorrow |
| G7 fix cluster (re-key + W-2b; pair merge separate; dim backfill after) | DS, CTO gate | post-fires |
| WO-5 schedule census (declared-cadence predicate) · WO-0 stale ledgers | COO | open |
| E-queue (E1 ruled; E2–E4) | post-MDPF-validation, per Andrew ~2336Z | gated |
| A.3 freshness-instrument re-point (flagged-not-folded) · missions.yaml `portal/**` gap (MSTR self-flagged) | CTO route / MSTR | open |

**Serve state at log time: the frozen `json/mdpf/*` set is still what clients see; the flip is the next event.**
