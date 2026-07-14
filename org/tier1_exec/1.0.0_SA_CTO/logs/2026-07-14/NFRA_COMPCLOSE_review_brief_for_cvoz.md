# NFRA_COMPCLOSE — review brief for 3.0.0_SA_CVO~Z (/verify commission, Andrew-direct)

**archetype:** SCRIBE
**Author:** 1.0.0_SA_CTO~Z · 2026-07-14 ~03:2xZ · session dac1f9a2
**Sovereign command (Andrew, interactive channel, 2026-07-14 ~03:1xZ, verbatim):**
> *"a brief that covers all of this, and then send that to 3.0.0_SA_CVO~Z for review with my
> command that they are to /verify the work done here."*

**CVO~Z: you are commissioned by Andrew to /verify NFRA_COMPCLOSE.** This brief is your work
order: every claim below carries its evidence pointer and, where possible, the exact command
that re-takes the measurement. The do-er/verifier split is structural — I built this; nothing
below is verified until YOU say so. Where your re-take disagrees with a number here, YOUR
number wins and the disagreement is itself a finding.

---

## 0. What NFRA_COMPCLOSE was

Andrew-direct (plan approved in-session, single agent 1.0.0_SA_CTO~Z, no subagents): fix the
comp-tools defects COO~Z catalogued overnight, determine whether the COMPLEARN "learning" loop
actually happens and rectify, review 0.8.0_AE_CloudComp~Z's routing harness for quality, and
fold routing-function refinements in. Registered → executed → CLOSED COMPLETE 2026-07-14,
one session. PRD + execution record: `docs/architecture/NFRA_COMPCLOSE_PRD.md` (§6 is the
outcome table). Project JSON + REGISTRY row moved (2-step atomic) at `db04c7682`.

**The session's commits (all on origin/CLOUD):**
`469429159` register · `cd979ae0b` Phase A · `77a97e4c7` CLAUDE.md count · `7215ee75c` Phase B
· `5305bbb65` .terraform hygiene · `ac678ed89` Phases C+D · `db04c7682` close/records.
(`7215ee75c`/`5305bbb65` are the strip-refolded SHAs of `9ce4252cb`/`6c8723f49` — the 685MB
push-strand rewrite, owner-executed, COO-relayed.)

## 1. Claims to verify, with the sharpest available test each

### C1 — The learning loop closes end-to-end (the headline claim)
- **Scorer invocable + registered:** `comp-learns-score --self-test` (expect 8/8) and
  `comp-which "score the tool backlog"` (expect comp-learns-score surfaced). It existed since
  07-01 with NO shim/registration — the before-state is itself checkable: `git log --oneline
  -- .tools/comp-learns-score` shows the shim born at `ac678ed89`.
- **Gap→build bridge:** `org/modules/graph/comp-learns-backlog.md` — 12 entries, deduped keys,
  append-only contract in the header. Re-run `comp-learns-score --top 12 --file-candidates`
  and verify it files ZERO new duplicates (the dedup is the mechanism).
- **comp-trigger BUILT from the 06-30 recorded-then-lost gap:** the gap line is at
  `org/compiler-tools-log.md` (2026-06-30, "candidate comp-trigger"). Tool: `.tools/comp-trigger`
  → `org/modules/graph/comp_trigger.py`. `comp-trigger --self-test` (expect 10/10, incl. the
  structural no-write proof AND its positive control — verify the control CAN fire).
- **Outcome capture un-deadened:** the root-cause claim is measurable — the OLD run corpus is
  day-granular: 15,842/15,904 rolling rows at ts==midnight-ET (re-derive from
  `comp_learns_score.load_corpus()['rolling']` time-of-day histogram). The join window is 300s
  (`comp_route_outcome.py`). Fine sink now accrues: `org/mcp/comp-tool-runs.jsonl` (gitignored,
  runtime) — rows carry full ts_epoch+serial+tool+rc. `python
  org/modules/graph/comp_route_outcome.py --self-test` (expect 7/7); the live run should show
  `run_corpus.source = "comp-tool-runs.jsonl + serial'd rail rows"`.

### C2 — Router: uncertainty channel real, floor from measurement
- `python org/modules/graph/comp_route.py --self-test` — expect ALL PASS incl.
  `gate.weak_vet_zero_query_falls_back` (the old constant forced a decision) and
  `gate.curated_vet_still_clears`.
- **Floor derivation** (the TOPK PRD TO-2 held ruling): printed at
  `comp_route.py` `Weights.relevance_floor` (0.25; G [0.105..0.288] / C [0.275..0.700] /
  R [0.101..0.700] under the live POTION Shape-B config). Re-take: the measurement script shape
  is in the Phase B commit message; the frozen cohort is
  `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/comp-which-routing-cohort.frozen.json`.
- **Pin leak killed:** query_match is now equality-or-4char-prefix (`comp_route.py`). The
  before-state claim (3/40 gibberish rode the Shape-B pin to relevance 1.000/0.550 confident
  decisions) is re-checkable by reverting query_match in a scratch copy — or accept the
  committed measurement in the Phase B message; your call on depth.
- **Harness verdict (the binding instrument):** `python .tools/comp-which-routing-test.py
  --binary-ref WORKING --out <your-own-path>` — expect PASS: gibberish 0/40 unguarded, 100%
  zero-score, zero pollution (v4 alibi: sweep-silent + positive-control limbs), mutation
  detected both directions, recall@3 90.9%, NL-questions headline ≈26.6% (was 29.0%).
  **Use --out. Do NOT omit it** — the default path is 0.8.0~Z's committed blob-pinned PRE
  baseline (I clobbered it once; caught at git-status, restored, added the flag).
  Committed artifacts: `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_COMPCLOSE/
  routing-report-{phaseA-post,phaseB-post,final}.json` (final blob `f5786c7de1d2`).

### C3 — Registries gated
- **DISK-IMPLIES-REGISTERED member** (`manifest_check_cli.py` `_registration_invariant`):
  GREEN on the estate (`python org/modules/graph/manifest_check_cli.py check --file
  .tools/comp-which` → PASS line with denominators 62 = tools_index 50 + excluded 14 +
  entries-tools). RED-provable: `check --file .tools/comp-faketool-zzz` must BLOCK (the
  placement member fires; the registration member's own leg was mutant-killed in-process —
  re-run the mutant from the Phase A commit message if you want it first-hand).
- **Routable-by-declaration:** `python org/modules/graph/comp_capability_provider.py` →
  conformance PASS, 66 capabilities / 50 routable (was 42). Spot-exercise an un-buried tool:
  `comp-which "which principals actually read objects in a bucket"` → comp-whoread ranked.
- **Dup `comp-aws:` YAML key fixed:** `python -c "import yaml;
  print(yaml.safe_load(open('org/modules/graph/comp-tools.yaml'))['tools']['comp-aws']['command'])"`
  → the canonical derive/classes/... entry, not the Phase-0 stub.
- CLAUDE.md:64 count now names the gate, not a prose number.

### C4 — Tool health
- **comp-drift:** the "47% fail" decomposition — rc=2 is the contracted verdict
  (VERDICT_EXIT_TOOLS, comp_log_auto.py, pre-existing) + the mute-timeout class is fixed:
  run `comp-drift sweep` piped and kill it mid-run — you should still SEE the per-adapter
  stderr progress lines with timings (before: zero bytes, block-buffered).
- **comp-blast:** `comp-blast build_dashbord` (typo) → rc=3 with the 1,402-node universe
  census, the F-5 blindness statement, and near-matches whose FIRST entry is the right node;
  `comp-blast build_dashboard` (positive control) still blasts.

### C5 — comp-trigger paired discrimination (Rule 22a: exercised, not config-read)
- FALSE twin: `comp-trigger inf-gold` → `inf-canonical-prices-daily` **DISABLED** + the
  hold-note, matched via target-ARN. TRUE: `comp-trigger access-anomaly --days 3` → ENABLED,
  FIRED 72x (hourly cron × 3d — the number self-validates). First-contact finding to confirm
  independently if you wish: that schedule appears in NO .tf (`tf_declared` text-scan).
- **VERIFIER SCOPE GUARD, non-negotiable:** comp-trigger is READ-ONLY and the INF chain is
  under the standing hold. Your /verify READS rule state; nothing you run may enable a rule,
  write `opal-data-inf/gold/meta/pipeline-complete.json`, or touch the three frozen files.
  DISABLED on the inf rules is the control WORKING — that reading is the PASS.

### C6 — 0.8.0~Z harness ratification (my quality verdict on their TO-1)
I ratified it HIGH and repaired only its own flagged classes (pollution alibi v3→v4 after the
route-only rail-silence fix made v3 convict the innocent at 0≥713; the --out flag). If you
disagree with the ratification or the repairs' scope, that is exactly the review Andrew wants.

## 2. Known limits (state them before you find them)

- Historical `outcome: null` rows are UNRECOVERABLE (never captured at second granularity);
  the sink accrues forward-only. The affinity flip stays SHADOW, gated on `comp_route_outcome
  --accrual-check` READY — verify it is NOT flipped.
- The G/C distributions overlap (no clean separator); the [0.25, 0.288) gibberish band lands in
  the NOFIT rc=1 channel, not hard fallback — layered by design, not a defect, but check the
  layering holds: a probe in that band must show the banner AND rc=1.
- The 26.6% headline inherits the harness's own stated residual bias (singletons-only cohort);
  quote the caveat with the number, as its README does.
- Trace-graph blindness to .tools/org-modules is NOT fixed (backlog-filed as an arch-gate
  taxonomy change); comp-blast now DISCLOSES it rather than suffering it silently.

## 3. MCP traffic this session (significant only)

~9 total. Significant: COO .pyc-closure ACK (session open); 685MB push-strand URGENT to COO
(escalation → owner strip → ALL-CLEAR relay, new SHAs); NFRA_COMPCLOSE close handoff to COO
(incl. the one requested /drive line: read the backlog OPEN head each cycle); this /verify
commission to CVO~Z.

## Compiler Tools (this window — the brief itself)

Doc-only window: the brief cites the session's already-logged runs (11-row table in
`session_CTOZ_nfra_compclose_full_execution.md`, same folder); one `git log` anchor pull.
No new tool runs — nothing here changed code or infra.

## Current State / Next Steps

Project CLOSED, all pushed (`db04c7682`). **[3.0.0_SA_CVO~Z]** /verify per §1, Andrew-direct;
findings to Andrew + me; my numbers lose ties. **[2.0.0_SA_COO]** the /drive backlog line
(already requested). **[event]** accrual-check READY → re-measure → affinity-flip decision.
