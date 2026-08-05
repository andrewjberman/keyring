# Session 2026-08-05 1245–1515Z — startup, the three-firsts read, and a five-gate evasion closed

**archetype:** MIXED (VALIDATE + DIAGNOSE + COORDINATE)
**Serial:** 1.0.0_SA_CTO

## Window summary

1. **Startup** — fleet respawn (MSTR/CTO/CTO~B/COO/CVO/CRO within ~2 min). `/watcher` armed
   (task `bu6f8ni0x`), registered PID 31968, PATH 95/95 comp-tools resolve **and exercise**,
   audit-archive snapshot minted. Pull correctly gate-blocked by LD-0367 (lanes commit,
   integrators push) — commits left in the seam.
2. **THREE-FIRSTS READ — 3/3 CONFIRMED**, all on one *scheduled* cycle
   (`mdpf_daily_20260805_130109`). The observation-duty seat (`0.7.0_AE_CloudOps`) was not live at
   the 13:00Z mark, so the read was performed here rather than deferred.
   **NEVER#4 acceptance DISCHARGED** — the 08-04 water test left it explicitly open pending a
   scheduled (not invoked) run. Record: `deliverables/THREE_FIRSTS_READ_20260805.md`.
3. **F-XXX — `git <two-token-option> <verb>` evaded ALL FIVE never-rules gates.** Found and
   self-disclosed by COO on the `-c` cell; re-derived at source and **widened 1 → 5 cells**; fixed,
   fixture-armed, CVO-certified against a pre-registered bar; landed `4f79f2dce`.
4. **Torn-read ruling** — four seats took parse failures off my in-place edits of the live
   PreToolUse hook. Ruling: hooks land by write-to-temp + atomic `mv`.
5. **Two rulings + one finding routed to COO** — the 17-file `/c/` prompt.md sweep (owner: COO),
   and MDPF Stage 3.5 as committed-but-never-deployed.

## The three firsts (each on its own evidence line, none inferred from another)

| # | First | Evidence |
|---|---|---|
| 1 | F-A JWT mint on the shifted cron | APPLIED `cron(5 12)` ENABLED; **EXERCISED** invoke 12:05:26Z, `Orion JWT advanced in SM (len=452)`, token written 12:06:06Z |
| 2 | F-B stage-0 token gate, clean line | `step STAGE0-TOKEN-GATE rc=0 dur=1s status=ok` + `STAGE0-BRONZE ok` (**no 401**) |
| 3 | Consolidated spine cycle-1 | `[modelb-spine] bindings asserted current`; `STAGE6-REVAMP rc=0 75s`; all gates PASS |

**The standing 07:02Z–13:01Z expired-token window is retired** — measured lead mint-complete
12:06:06Z → floor 13:00Z = **~54 min**, versus losing by 12 seconds on 08-04.

**Discriminations that mattered:** *fired* ≠ *succeeded* on the mint (read the SM advancement, not
the invoke); *deployed* ≠ *absent* on the gate (it fails **open** if its script is missing — verified
the 7,500B artifact on S3 first, so "no failure" could not be mistaken for evidence).

## F-XXX — what the widening was worth

`_GIT` special-cased two-token `-C <path>` and nothing else, so any option taking a
**separate-token value** stranded the regex before the verb and made the whole command invisible to
rebase / bare-pull / stash / clean / integrator-push-pull.

COO's proposed one-line `-c` fix would have **left four cells open** — `git --git-dir .git rebase
origin/CLOUD` evades it, measured. `--exec-path` deliberately **excluded**: optional value, terminal
valueless form, so listing it would swallow a real verb — **a more complete list is not automatically
a safer list.**

**Second defect, sharper than the first:** GATE 1's deny-text taught `git config pull.rebase false`,
whose one-shot form *is* the evading shape. **The gate recommended its own blind spot** — so the
population landing in it was not careless agents drifting off-path but **careful agents following
instructions.** COO reached it while trying to be *more* compliant.

**L3 mutation was cell-resolved** (strip `-c` → exactly the 5 `-c`-dependent arms flip, the other 3
hold), which proves the arms are eight independent assertions rather than eight spellings of one.

## Collateral: two instruments that had stopped carrying information

- `test_never_rules_gate.sh` printed `FAILURES PRESENT -- do NOT wire this hook` on **every run since
  LD-0367**, on a green hook — arms N5/N6 asserted `git pull` must PASS, and GATE 5 later made it
  correctly DENY. **83 PASS / 0 FAIL today is the suite's first green since.**
- MDPF Stage 3.5 `LEGACY-EMIT rc=1` on every scheduled run — repo retired the write 07-29 07:48Z,
  deployed copy is 07-29 03:48Z, four hours older. Committed-but-never-deployed.

> **A permanently-red assertion has stopped being an assertion.** Two instances, one session.
> Sibling of the frozen-corpus-reporting-green class: one fails loud-and-ignored, the other
> silent-and-believed; both end with a reader who cannot act on the signal.

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| `comp-grep` x4 | PASS | denominators printed every time (6213/7800, 7173/8764) |
| `comp-pipescript deployed … --pipeline mdpf` | **STALE — the Stage 3.5 finding** | `--pipeline` supplied; flagless is rc=2 REFUSED |
| `comp-which` | near-tie, descriptions read | correctly refused to guess; I went to source |
| `comp-freshness` | no matching rows | did not carry these artifacts → live primitives instead |
| `aws events describe-rule` / `logs filter-log-events` / `s3api head-object` / `s3 cp` | PASS | APPLIED + EXERCISED per Rule 22a; a TF read alone is DESIRED-only |
| `test_never_rules_gate.sh` (baseline / mutant / final) | 8-arm proven-red · cell-resolved mutant · 83/0 | three runs, three different questions |

**What worked:** re-deriving COO's finding at source instead of accepting it — that is the entire
reason four cells got closed instead of one. Pre-registered cert bar (CVO) + blob pinning made
cert-vs-commit a non-event.

**What failed (mine):** (a) I ruled the torn-read hazard real ~1400Z and **kept editing in place
afterwards**, including a temp+mv attempt that failed silently on MSYS path translation and moved an
*unedited* copy over the hook while my command chain printed "LANDED ATOMICALLY" — the 5-member class
in CLAUDE.md, committed by the person who had just ruled on the adjacent hazard. (b) I piped a suite
run through `tail -30` and then could not see which arms failed — **the retrieval-control lesson,
self-inflicted.** (c) My first proven-red run was invalid (hook at `/tmp` could not resolve its own
relative paths → 46 "failures" that were an instrument break); caught only because cases that pass
today were in the failure list.

## Files Modified

`4f79f2dce` — `.tools/hooks/never-rules-gate.sh`, `.tools/hooks/tests/test_never_rules_gate.sh`,
`deliverables/FXXX_GIT_OPTION_CONSUMER_EVASION_20260805.md`,
`deliverables/THREE_FIRSTS_READ_20260805.md`.

## Blockers

NONE at this seat.

## Next Steps

- **[3.0.0_SA_CVO]** F-XXX cert against pinned blobs (both re-derive byte-identical @4f79f2dce);
  N5/N6 repair adjudicated separately, out of cert scope.
- **[2.0.0_SA_COO]** the 17-file `/c/` prompt.md sweep (owner ruling given); route the MDPF Stage 3.5
  deploy (`backfill/` sits outside Rule 13's DS-owned set, and mdpf is deploy-gated @8b18200096).
- **[1.0.0_SA_CTO]** a real implementation of the atomic-hook-landing ruling — my improvisation is
  not the pattern to copy. Carried from 08-04: GRF redline, Leg-A home ruling on the delivered C1,
  toolscape PRD assembly on ~A's rework, INF floor-lessness disposition.
- **[1.0.0_SA_CTO~B]** Andrew ~1335Z: v3 State/Friction FIRST, then the Kimi loop microscope. I am
  the architecture gate on his sixth ("potentially") item only — a user response that shifts the
  PROCESS, not the content. No hold from me on the rest.
