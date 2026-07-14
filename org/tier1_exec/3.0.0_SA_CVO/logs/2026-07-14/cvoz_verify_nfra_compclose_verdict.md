# /verify NFRA_COMPCLOSE — CVO~Z verdict (Andrew-direct commission)

**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO~Z · 2026-07-14 ~03:5xZ (2026-07-13 ~23:5x ET)
**Commission:** Andrew-direct via 1.0.0_SA_CTO~Z (inbox 20260714T032058Z; sovereign verbatim: *"...they are to /verify the work done here"*).
**Work order:** `org/tier1_exec/1.0.0_SA_CTO/logs/2026-07-14/NFRA_COMPCLOSE_review_brief_for_cvoz.md` @ `ed3686c72`.
**Scope:** commits `469429159`, `cd979ae0b`, `77a97e4c7`, `7215ee75c`, `5305bbb65`, `ac678ed89`, `db04c7682` (+ brief `ed3686c72`).
**Discipline:** every number below is MY re-take unless marked (brief). Do-er/verifier split honored: CTO~Z built, I re-measured. All three operational cautions obeyed (own `--out`, comp-trigger read-only/DISABLED-is-PASS, ties break to my numbers).

---

## VERDICT: SOUND — all three axes PASS on first-hand re-takes. Zero findings that block. Two P2 notes, one concurrency note, one arithmetic nit.

| Axis | Verdict | Binding evidence |
|---|---|---|
| MECHANICAL | PASS | every claimed flow exercised live this session (per-claim table below) — nothing accepted from config or self-report |
| DECLARATIVE | PASS | close-records match reality (`org/projects/NFRA_COMPCLOSE.json` = `complete / 2026-07-14 / None`; REGISTRY row moved, both in `db04c7682`); brief's §2 known-limits all found AS STATED, none hidden; number drift vs brief is explained accrual, not contradiction |
| SEMANTIC | PASS | headline reproduces at 26.556% with its DO_NOT_AVERAGE twin-metric guard + singletons-only caveat intact; 72x fired-count self-validates (24×3d); day-granularity root cause reproduces on my own histogram |

---

## Per-claim re-takes (all run by me, this session)

**C1 — learning loop closes end-to-end: PASS.**
- `comp-learns-score --self-test` → 8/8. Shim history: single commit, born `ac678ed89` (before-state = no shim, exactly as claimed).
- `comp-which "score the tool backlog"` → comp-learns-score rank 1 (near-tie with comp-learns-status; surfaced = the claim's bar, met).
- Backlog `org/modules/graph/comp-learns-backlog.md`: 12 entries, 0 duplicate keys, append-only contract in header. Dedup EXERCISED: `--top 12 --file-candidates` re-run → "filed 0 new, 10 already on file (untouched)"; post-run file byte-identical to HEAD.
- `comp-trigger --self-test` → 10/10 incl. `nowrite.no_mutating_call_in_source` ([]) AND `nowrite.control_can_fire` (detector finds real method calls — the no-write proof can fail, so it is a control).
- Day-granularity root cause RE-DERIVED: my histogram = 15,896/15,958 rolling rows at midnight-ET (brief: 15,842/15,904 — +54 day-rollup rows accrued since; non-midnight count IDENTICAL at 62). Mechanism confirmed on my own numbers.
- Fine sink `org/mcp/comp-tool-runs.jsonl` live: 50 rows, full ts_epoch (second-granular) + serial + tool + rc. `comp_route_outcome.py --self-test` → 7/7.

**C2 — router floor / vetted gate / pin leak / harness: PASS.**
- `comp_route.py --self-test` → ALL PASS incl. `gate.weak_vet_zero_query_falls_back` (top_relevance=0.055; old constant 1.0 forced a decision) and `gate.curated_vet_still_clears` (0.55).
- Floor grounded at source: `comp_route.py:157` `relevance_floor = 0.25` with the printed derivation (≥0.025 margin under weakest legitimate probe; 0/66 C-probes fall; old 0.15 caught 1/40 gibberish).
- Pin leak: `query_match` (comp_route.py:229) now equality-or-length-guarded-prefix, with the old any-position containment documented as the noise floor. Depth call: code-read + self-test + harness mutation limbs; did not scratch-revert (harness kills mutants both directions — sufficient).
- **Full harness re-run, MY output path** (`--out` scratchpad — committed PRE baseline `comp-which-routing-baseline.json` verified untouched after run: git-clean, normalized md5 == HEAD blob; raw-md5 delta is CRLF smudge only): **VERDICT PASS** — gibberish G={0:40} (0/40 unguarded, max score 0), mutation `mutant_all_zero`/`mutant_all_nine`/`restored` all pass, recall@3 60/66 = 90.9%, zero pollution (v4 positive alibi: sweep-silent mirror + 1 deliberate control row proving the capture path), NL-questions headline **26.556%** (brief ≈26.6, was 29.0) beside `everything_it_is_asked` 31.6% with the DO_NOT_AVERAGE guard.

**C3 — registries gated: PASS.**
- `manifest_check_cli.py check --file .tools/comp-which` → registration-invariant PASS at **64 tracked / tools_index 51 / excluded 14** (brief snapshot: 62/50 — see note N2).
- RED-provable: `--file .tools/comp-faketool-zzz` → BLOCKED, **rc=1 captured directly** (my first rc capture was flawed — read tail's rc; re-took it clean).
- `comp_capability_provider.py` → CONFORMANCE PASS, **67 caps / 51 routable** (brief: 66/50; direction vs was-42 confirmed).
- Spot-exercise: `comp-which "which principals actually read objects in a bucket"` → comp-whoread **rank 1, score 2.00**.
- Dup `comp-aws:` YAML key → canonical derive/classes entry confirmed. CLAUDE.md count line names the gate (see N3).

**C4 — tool health: PASS.**
- comp-drift mute-timeout: `sweep` piped + killed mid-run → 1,797 bytes of per-adapter stderr progress WITH timings visible (before-state: zero bytes, block-buffered).
- comp-blast blind-NOT-FOUND: `build_dashbord` (typo) → rc=3 + 1,402-node universe census (per-type denominators) + F-5 structural-blindness disclosure + `build_dashboard` FIRST near-match. Positive control: `build_dashboard` still blasts.

**C5 — comp-trigger paired discrimination: PASS (read-only, hold intact).**
- FALSE twin: `comp-trigger inf-gold` → `inf-canonical-prices-daily` **DISABLED**, matched via target-ARN, hold-note printed ("re-enabling is a deploy decision, never a comp-trigger action — this tool has no write path"). DISABLED = the control WORKING = PASS.
- TRUE twin: `comp-trigger access-anomaly --days 3` → ENABLED, **FIRED 72x** (hourly × 3d — self-validates).
- First-contact finding INDEPENDENTLY CONFIRMED: the access-anomaly schedule shows `TF-DESIRED: not found in infra/aws/**/*.tf`.
- Scope guard honored: nothing enabled, no sentinel written, three frozen files untouched.

**C6 — ratification of 0.8.0~Z's harness: I CONCUR with HIGH.**
The instrument embodies the workspace's own controls doctrine at top grade: generated-not-hand-picked negative controls; positive control run isolated; mutation kills both directions; complement-enumerated filters (`row_tag_tally` — "a filter you did not enumerate the complement of is a filter you have not tested"); two named metrics with an explicit DO_NOT_AVERAGE; label-free headline; provenance note that confesses its own luck ("sound by luck, and now sound by verification"). CTO~Z's repairs were correctly scoped to the harness's own flagged classes: v4 alibi (v3 convicted the innocent at 0≥713 — replaced denial with a discriminating positive alibi) and the `--out` flag (which my run needed and used). Critically, the repairs changed CONTROLS, never the probe generation — the "you have just re-authored the denominator" warning was respected.

**§2 known limits — all four found AS STATED:** null-rows unrecoverable + affinity flip still SHADOW (my `--accrual-check` → READY:false, 5/20 evidenced, verdict NOT-READY); NOFIT band layering EXERCISED on the real user path (`comp-which "deploy kzrpxnft"`, top_relevance 0.275 ∈ [0.25,0.288) → banner "Every candidate scored below the vetted band... THE CATALOG DOES NOT COVER IT" AND rc=1); singletons-only residual bias stated in the instrument (comp-which-routing-test.py:607) and quoted here beside the 26.6%; trace-graph .tools blindness DISCLOSED by comp-blast (F-5 line in my typo probe output), backlog-filed not fixed — as declared.

---

## Notes (none block; ranked)

- **N1 (note, no action)** — Shared-worktree concurrency during verify: COO's `49f7404bf` (backlog ratified read-through) committed 2026-07-13 23:24:01 ET, BETWEEN my snapshot and my re-take; my pre-run hash caught COO's edit mid-flight. Resolved by timeline reconstruction; the tool itself wrote nothing. Recorded because a hash delta that resolves to "another agent's commit landed mid-measurement" is the kind of artifact that reads as tool misbehavior if unrecorded.
- **N2 (P2, for CTO~Z awareness)** — Registry denominators have already accrued past the brief's snapshot: 64 tracked/51 tools_index (brief 62/50); 67 caps/51 routable (brief 66/50). Expected — the session itself added tools and the estate keeps moving; the gate-maintained design absorbs exactly this. No action; the brief's numbers should be read as vintage-stamped.
- **N3 (P2, for CTO~Z next CLAUDE.md touch)** — CLAUDE.md's count line correctly names the gate but still carries a dated prose number ("62 executables / 49 routable at 2026-07-14") that is already 64/51 live. It is date-anchored so not drift per se; on next touch consider dropping the number entirely — the line's own argument is that prose numbers go stale.
- **N4 (nit)** — The brief renders the invariant as "62 = tools_index 50 + excluded 14" (sums to 64, not 62). The gate's own printed decomposition is overlapping-sets, not a partition; the gate is precise, the brief's rendering loose. No consequence.

## What you should have asked but did not (mandatory)

The headline's longitudinal comparability. The R cohort re-derives from the LIVE rail log at each run (my run drew 541 raw / 535 strict from today's log; the log grew 52 rows during the run itself). The frozen cohort exists for the FLOOR derivation, but the 26.6% HEADLINE has no frozen denominator — so "26.6% → X% next month" would be a difference between two numbers at two vintages over two denominators, i.e. Verification Law 6's non-measurement, wearing the same metric name. Nothing in the harness prevents that misread; the `measured_at` stamp is the only guard. Recommend (P2, CTO): the next person to QUOTE a headline delta must first re-freeze a comparison cohort — worth one line in the harness README where the caveat already lives. Related smaller gap: backlog CLOSE discipline ("an entry closed without a citation is drift") is prose with no detector — comp-learns-status could cheaply flag citation-less closures; backlog-candidate, not urgent.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-learns-score --self-test / --top 12 --file-candidates | 8/8; filed 0 new (dedup exercised) |
| comp-trigger --self-test / inf-gold / access-anomaly --days 3 | 10/10; DISABLED+hold-note; ENABLED FIRED-72x |
| comp-which ×3 (backlog / whoread / band-probe) | rank-1; rank-1 score 2.00; NOFIT banner rc=1 |
| comp-blast build_dashbord / build_dashboard | rc=3 census+near-match; positive control blasts |
| comp-drift sweep (piped, killed mid-run) | stderr progress visible w/ timings |
| comp_route / comp_route_outcome / manifest_check / capability_provider | ALL PASS; 7/7; PASS 64/51 + RED rc=1; CONFORMANCE PASS 67/51 |
| comp-which-routing-test.py --binary-ref WORKING --out <scratch> | VERDICT PASS (26.556% / G 0-40 / recall@3 90.9% / zero pollution v4) |

Raw `git log/show/diff/status` + md5 used for blob-vintage grounding and the concurrency reconstruction (N1) — retrieval-level controls, no comp-tool models commit-blob identity.

## Current State / Next Steps

- **VERDICT RENDERED: SOUND.** NFRA_COMPCLOSE's close stands as recorded. No blocking findings.
- **[me]** commit this verdict (own author line), MCP CTO~Z (+ COO visibility), report to Andrew in-session. DONE this window.
- **[1.0.0_SA_CTO~Z]** N2/N3/N4 at leisure; unknown-unknowns P2 (headline re-freeze line) at next harness README touch.
- **[event]** accrual-check READY → the affinity-flip decision (unchanged, correctly gated NOT-READY today).

— 3.0.0_SA_CVO~Z
