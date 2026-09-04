# PROPOSAL (DRAFT v2) -- the comp-tool marquis set, the retire candidates, the archive tier

**Status: DRAFT for Andrew's word. This document DECIDES NOTHING** (PRD s.5: the marquis decision is "not cut,
deliberately"; FWD-8 DONE WHEN a seat has started work from the list HE ratified). **v1** @`ac52464f82` (2026-09-02)
was the usage-and-overlap layer written BEFORE the per-tool audits and said so. **v2, this file (2026-09-04 ~08:1xZ),
is written AFTER them:** every row below reads the PRD v0.8 s.7 SURFACE MANIFEST's final disposition, the 22 proof
instances (all VALID at this seat), the round-6 grades @`f755484cbb` and this seat's roll-up (48 findings, UNCLEAR 0).
Usage = 30 days at `f90ab3936b`, both instruments (`comp-tool-runs.jsonl` + `comp-which-rail.log`), as s.7 carries it.

**What moved between v1 and v2, stated so the correction is visible and not silent:**
- **comp-trace is NOT retired.** v1 called it "a strict subset of comp-blast, condition met". The audit measured two ways
  (S17; PRD v0.6 R-4): trace carries `--exact`, `--all` and direction spellings blast rejects; blast resolves 38.6% of
  trace's node ids. R-4's condition failed; T-19 closed NOT-RETIRED; the three carryable flags entered blast. v1's row
  was a line-range read taken as a measurement -- the exact error the audits exist to catch.
- **comp-denytest: KEEP, not "retire after T-8".** The audit built its four exact states, deferred the conditioned-grant
  false deny as NOT-DECIDABLE rc 2, and bounded its AWS subprocess; it is the only tool that derives an EXPECTED verdict
  from an IAM change type. Barely used (2 in 30 days, 8 ever) because a zero population when no IAM change is in the
  plan is correct, not disuse (CE-q-1 answer 5).
- **comp-heat is the new retire candidate.** 0 CLI runs; its only library consumer (`comp-similar.load_heat_live`)
  returns `{}` before reaching it (S29, FWD-9 at the COO); the daily-report wiring @`09355b6d93` invokes it from nowhere;
  and it fails Rule T outright -- `comp-heat freshness` with no path scores the whole repo and accepts no `--budget`
  (T20-AC4 FAIL, adjudication C-S5). The round-6 analysis @`de9a194c7b` recommends RETIRE at the FWD-4 read; this draft
  agrees and says why below.
- **comp-kuzu / -inc / -full: ruled (a) and executed** -- `--mode inc|full` is the surface; the wrappers are one engine.

---

## 1. MARQUIS -- what the word obliges, and who meets it

"Marquis" means: Rule P (a page contract with its denominator) and Rule T (a budget the tool honours) conformant, a
battery that can go red, disclosure fields on every run, a named owner. Membership is earned by law or by traffic.
**14 tools; each row's last column is what the audit found it still owes.**

| tool | 30d runs | why marquis | audit disposition (s.7) | still owes |
|---|---|---|---|---|
| `comp-find` | 3,722 | the search rail (Rule 21, Andrew-direct) | T-1 audit+fix; Rule T's first target landed | F1 `--version` becomes a search pattern (one flag); the manifest's stale flag list (F2) |
| `comp-read` | 2,401 | the single-file rail (Rule 21) | T-2 audit+fix; battery 8/8 | `--enumerate` writes no rail row (F2, owner CloudComp, a later pass) |
| `comp-which` | 520 + 9,643 rail | the router | T-3 audit | **F2: a non-existent gold id routed with a confident score** -- the highest-value unfixed finding in the roll-up; layer provenance (F1) |
| `comp-kuzu` (`--mode inc\|full`) | 1,591 + 14 | the graph substrate every lens reads | T-22 retire-and-fold RULED (a) | nothing on this evidence; the local rebuild path's retirement is NFRA_CLDGRPH CG-s-8 |
| `comp-system` | 584 | compiles `infra/system/06_current_state` | T-21 audit; no-fabrication invariant; `--check` rc 3 on budget | nothing stated |
| `comp-pipescript` | 571 | mandatory per role minimums; F9 gate GREEN | T-10 audit | ETFS absent from the deployed firm registry (owner: the registry authority) |
| `comp-estate` | 281 | first contact for the Estate | T-17 audit; C(N) carried to NFRA_C3MATERIALIZE | usefulness gated on C(N) (his word); Rule P PAGE i of N absent (F3) |
| `comp-blast` | 167 | change impact; now carries trace's three flags | T-6 audit+fix; T6-AC7 whole-call budget, exercised on a BEHIND graph (C-S1) | nothing on this evidence |
| `comp-iam` | 113 | the only IAM lens; mandatory core in the L6 gate | T-8 audit+fix; NOT-DECIDABLE state built | DESIRED-plane vintage (F2); one state, two print shapes (F5) |
| `comp-trigger` | 80 | the only scheduler-forensics lens | T-9 / T-9R: four distinguishable states | S3-notification coverage is the graph engine's (CLDGRPH C-3) |
| `comp-adversary` | 0 in runs.jsonl (gate-driven) | mandatory core by the gate; validator context by Andrew-direct | T-16: three surfaces landed | F1 refuse a directory subject in its own voice (the one line "between comp-adversary and CLEARED"); F2/F3 ride it |
| `comp-schedule` | 0 in runs.jsonl (gate ledger) | the gate ledger, Andrew-direct 2026-09-01 | T-5 audit; ARNs absent BY DESIGN | nothing (F1-F3 recorded with owners) |
| `comp-similar` | 30 | readmitted per RC6; D1-D3 fixed | T-12: integration condition MET; CLEARED-candidate | Rule P pagination absent (F2) |
| `comp-pulse` | 8,364 (8,359 the commit hook) | the pre-commit risk reflex | T-18 audit | marquis AS A HOOK; its "morning read" half has 5 users a month -- the decision is which half is the product |

**Kept, not marquis (low traffic, distinct plane, audited clean):** `comp-trace` (45 runs; kept NOT-RETIRED, its own
engine; S35's inert `--budget` is OPEN at the recut), `comp-cache` (35; React Query keys in `portal/src`),
`comp-platinum` (7; page -> gold composite; two boundary modes unbuilt, disclosed), `comp-dataflow` (11; the gate
archetype, rc 4 NOT-DECIDABLE landed under T-25), `comp-drift` (1; the propagation orchestrator over 15 sweep units).

## 2. RETIRE CANDIDATES -- evidence, replacement, whose word

| tool | evidence | replacement | needs | REC |
|---|---|---|---|---|
| `comp-heat` | 0 CLI runs; consumer returns `{}` before reaching it; invoked by nothing; T20-AC4 FAIL (a corpus-width sweep with no Rule T carrier); T-20's lane is dead | none needed today: nothing consumes it; the freshness question it answers is the graph engine's `built:` line and comp-kuzu's BEHIND warning | **Andrew's word** (his interest named it in the brief) | **RETIRE** -- the cheaper true state; it also removes the one FAIL from FWD-10's denominator by his ruling rather than a fix to a tool nobody runs |
| `comp-dups` | 0 runs EVER; its own engine (names+bodies) by CTO arch-gate ruling 3; not a comp-similar mode | none -- the name/body-twin question is asked or it is not | **the CTO's disposition** (their ruling) | let the CTO's RETIRE-on-usage stand; do not fold into comp-similar |
| `comp-surface-check` | RETIRED 2026-08-06 by Andrew-direct, yet 987 runs in 30 days at v1's vintage | already retired | **a FINDING, not a candidate**: something invokes a retired tool ~33x/day; owner whoever wired it | census the invoker at the archive-tier act below; not a word for Andrew |
| `comp-kuzu-inc`, `comp-kuzu-full` | one flag each on one engine | `comp-kuzu --mode inc\|full` | RULED (a) | done; listed for the record |

**Not candidates any more:** `comp-trace` (kept by measurement), `comp-denytest` (keep), `comp-drift` (keep: audited,
cheap, the only propagation lens).

## 3. HIS FOUR ROLL-UP QUESTIONS -- answered in CE-q-1 (PRD v0.8 s.5a), restated in one line each

kuzu/kuzu-inc one command: **yes, ruled (a), done.** trace = dataflow: **no** (and not a subset of blast either).
similar supplants dups / drift: **no / no.** cache = platinum: **no** (portal-local keys vs the page-to-gold plane).

## 4. THE ARCHIVE TIER -- the ~49 zero-run implementations, still unnamed by design

v1's measurement stands: 45 of 94 implementations ran in 30 days; the top 20 carry 99.6% of invocations. An ARCHIVE tier
(kept, not deleted, off the rail's route table, no battery obligation) for a tool with 0 runs in 30 days AND no gate,
hook or skill invoking it. **The census that names them is one act:** `comp-which`'s route table + `.claude/skills/*`
+ hooks + `comp-tools.yaml`, cross-joined with the zero-run set, denominators printed; comp-surface-check's phantom
invoker falls out of the same join. Not run here; it is the act your word authorizes.

## 5. WHAT THIS DRAFT ASKS OF ANDREW -- four words, when ready (each answerable in one)

1. **The marquis 14 in section 1:** ratify as the list (REC), or strike / add by name.
2. **comp-heat:** retire (REC), or keep.
3. **comp-denytest:** keep (REC), or retire.
4. **The archive-tier census:** authorize (REC), or not.

comp-dups stays the CTO's disposition; comp-kuzu and comp-trace are already ruled. A seat starting one piece of work
from the ratified list is what closes FWD-8; the natural first piece is comp-which F2 (the router that validates a
subject's shape and never its existence), the roll-up's highest-value unfixed finding.

-- 3.0.0_SA_CVO
