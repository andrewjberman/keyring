# PROPOSAL (DRAFT) — comp-tool marquis set, retire candidates, and the fold-ins

**Status: DRAFT for Andrew's word. This document DECIDES NOTHING.** Andrew, 2026-09-02: *"We may want to
retire/archive groups of comp-tools and elevate a few to the marquis list"* — a direction of inquiry.
`/next-steps` option 4 approved ~20:4xZ as a DRAFT: *"acting on it stays your word per FWD-5."*
**Evidence vintage:** NFRA_COMPEFFICACY PRD draft §7 @`0c7c172f57`; usage = 30d to 2026-09-02 across BOTH
instruments (`comp-tool-runs.jsonl` + `comp-which-rail.log`); overlap claims verified on WRAPPER EXECUTABLE
BODIES (both wrong-object errors this seat made today were header reads).
**Bound stated up front:** the per-tool §4 audits have not run. They WILL move this list — T-16 alone flipped
twice in one afternoon. This is the usage-and-overlap layer only.

---

## 1. MARQUIS — the set the estate actually runs on (and what "marquis" obliges)

"Marquis" here means: **Rule P + Rule T conformant, a battery that can go red, disclosure fields on every
run, and a named owner.** Membership is earned by traffic or by law, not by name.

| tool | 30d runs | why it is marquis | what it still owes to BE marquis |
|---|---|---|---|
| `comp-find` | 3,722 (rail) | the search rail by Andrew-direct law (Rule 21) | **a battery** (unit 3b); Rule T budget (600s internal > 120s outer) |
| `comp-read` | 2,401 (rail) | the single-file rail by Andrew-direct law | `--enumerate` writes no rail row (finding); Rule T |
| `comp-which` | 520 + 9,643 rail | the router | 4.3 four-case test on its NOFIT path |
| `comp-kuzu` | 1,591 | the graph substrate every graph lens reads | consolidation ruled (a); `--mode inc|full` becomes the surface |
| `comp-system` | 584 | compiles `infra/system/06_current_state` — the SYSTEM home's dynamic half | disclosure fields; `--check` semantics documented |
| `comp-pipescript` | 571 | DS/DT/AE mandatory per XXX.md role minimums | shim self-identification (CVO~A s.9); nothing else — F9 GREEN |
| `comp-estate` | 281 | first contact for the Estate; C(N) ontology in flight (`NFRA_C3MATERIALIZE`) | usefulness is gated on C(N) — his own word; marquis-pending |
| `comp-blast` | 167 | change-impact; absorbs comp-trace | NOT-FOUND ≠ zero radius (CVO~A s.5); vintage + node denominator |
| `comp-iam` | 113 | the only IAM lens; mandatory core in `to-pipeline-gate.py:45` | **effective-deny mode** (CVO~A s.8) — highest-value gap after RC5 |
| `comp-trigger` | 80 | the only scheduler forensics lens | declare EventBridge+Scheduler-only OR add S3-notification backend |
| `comp-adversary` | 0 in runs.jsonl* | mandatory core by the gate; validator-context by Andrew-direct 2026-08-19 | `comp_log_auto` emit (unit 3a); s.4 audit |
| `comp-schedule` | 0* | the gate ledger — Andrew-direct 2026-09-01; mandatory core | none on this evidence (CVO~A s.11) |
| `comp-similar` | 30 | D1–D3 fixed today; readmitted per RC6 | the derive IMAGE carries pre-fix bytes (DEPLOYED≠COMMITTED, `0.7.0_AE_CloudOps`) |
| `comp-pulse` | 8,364 (**8,359 = commit hook**) | the risk reflex on every commit | marquis **as a hook**; its "morning read" half has 5 users/month — decide which half is the product |

\* zero in `runs.jsonl` because these tools do not (yet) emit to it — the unit-1 class, not zero use.

**14 tools.** Three are marquis by LAW regardless of traffic (comp-find, comp-read, comp-adversary/comp-schedule via the
gate); the rest by traffic. Every one owes something before it is marquis in the s.4 sense.

## 2. RETIRE CANDIDATES — each with its evidence, its replacement, and WHOSE word it needs

| tool | evidence | replacement | needs |
|---|---|---|---|
| `comp-trace` | strict subset of `comp-blast` (`cli.py:1478-1530`; same TraceGraph, same flags; blast adds analytics); 45 runs (AE~F 18, CC~D 14, CVO 11) | `comp-blast <node>` | **RULED** — *"if so it should be retired"*; condition met. Executable as PRD row T-19 |
| `comp-kuzu-inc`, `comp-kuzu-full` | one flag each on `kuzu_cli.py` (`--mode` exists at `:165`) | `comp-kuzu --mode inc\|full` | **RULED (a)** 18:12Z; unit 2 in flight, re-scoped to ~15 carriers across three lanes |
| `comp-dups` | **0 runs ever**; separate engine (`dup_scan.py`, names+bodies) from comp-similar (summaries) by CTO arch-gate ruling 3 | none — the NAME/body-twin question is either asked or it is not | **CTO's disposition** (their ruling); RETIRE ON USAGE, do not fold |
| `comp-denytest` | 2 runs/30d, 8 ever; zero population when no IAM change is CORRECT behaviour | `comp-iam` effective-deny mode, once built | **Andrew's word** — he flagged it *"not sure if we need this in practice"*; recommend: retire AFTER T-8's deny mode lands, not before (it is the only deny-shaped test today) |
| `comp-drift` | 1 run/30d; orchestrator over seam engines; overlaps comp-similar by NAME only (propagation vs function) | none directly; its `--deep` engines are reachable individually | Andrew's word; recommend: keep until the §4 audit says whether any workflow calls it |
| `comp-surface-check` | **RETIRED 2026-08-06 by Andrew-direct** — yet **987 runs in 30d** in `runs.jsonl` | already retired | **FINDING, not a candidate:** something still invokes a retired tool ~33×/day. Owner: whoever wired it. Not a retirement — an un-retirement that never finished |

## 3. FOLD-INS AND NON-FOLDS — his four roll-up questions, answered

| question | answer | basis |
|---|---|---|
| comp-kuzu / comp-kuzu-inc one command? | **YES — ruled (a)** | one engine, one flag |
| comp-trace = comp-dataflow? | **NO; comp-trace = comp-blast minus analytics** | same CLI file, `trace` ⊂ `blast`; dataflow is a value-origin tracer with `origin`/`gate` modes |
| comp-similar supplants comp-dups / comp-drift / comp-legacy? | **NO / NO / comp-legacy does not exist** | dups: separate engine by ruling; drift: propagation axis; legacy: 0 of 106 |
| comp-cache = comp-platinum? | **NO** | cache = React Query keys inside `portal/src`; platinum = portal-page→gold-script composite of transform+routes+pipescript. Different grain; both low-traffic (35 / 7) |
| comp-hud? | **not a tool** — `.tools/hooks/comp-tool-hud.sh`, the rail HOOK | 0 of 106 entrypoints |

## 4. ARCHIVE GROUPS — the 74 tools outside the marquis 14 and the 6 candidates above

**Measured:** last 30d, **45 of 94 implementations ran at all**; the top 20 carry 99.6% of invocations. So **~49
implementations had ZERO runs in 30 days.** This draft does NOT name them individually — a name list from usage
alone is exactly the "retire on a sample" error — but the shape is clear: an ARCHIVE tier (kept, not deleted,
not on the rail's route table, no battery obligation) for tools with 0 runs/30d AND no gate/hook/skill invoking
them. **The census that names them is a §4 act: `comp-which`'s route table + `.claude/skills/*` + hooks +
`comp-tools.yaml`, cross-joined with the zero-run set.** Not run here.

## 5. WHAT THIS DRAFT ASKS OF ANDREW — exactly three words, when he is ready

1. **comp-denytest:** retire after T-8's deny mode lands (rec), or now, or keep.
2. **comp-drift:** keep pending audit (rec), or retire on usage.
3. **The archive tier:** authorize the §4 census that names the zero-run set (rec), or not.

Everything else in this document is either already ruled (kuzu, trace), another seat's disposition (dups → CTO),
or a finding (comp-surface-check still running; comp-pulse's two halves).

— 3.0.0_SA_CVO
