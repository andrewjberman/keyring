# COO Session 33 — ADVI_STAUDT Authoring + Dispatch + Lane Sequencing
**Date:** 2026-04-20 (Mon, ET)
**Agent:** 2.0.0_SA_COO
**Companion log:** `startup_session33_reconciliation.md` (Friday→Monday gap reconciliation; commit `9229c21d`)

---

## What this log covers

This session began as a Monday-morning reconciliation (last COO log 2026-04-16; weekend gap, no commits Sat/Sun). Mid-session, CTO handed off the ADVI_STAUDT project — a deterministic 4-checkpoint reconstruction of ADVI gold + portal state to attribute Andrew's Friday breakage surfaces. Most of the session was spent decomposing that PRD into 4 lane TOs, iterating through 3 CTO amendments + 1 model restructure + 1 conditional-approve rework, dispatching GOs, and validating layer findings as they landed.

---

## Project context (CTO-handed-off)

**ADVI_STAUDT — Portal State Audit, Wed→Mon 2026-04-15..2026-04-20.** Read-only audit. Project JSON `org/projects/ADVI_STAUDT.json` (CTO commit `1472d1b7`). PRD `docs/architecture/ADVI_STAUDT.md`. Goal: reconstruct gold + portal state at 4 checkpoints (T0 Wed `544877cc` / T1 Thu `f177240b` / T2 Fri AM `ae759bbb` / T3 Mon current `cd177553`) so each of COO's 4 portal bugs + the live nna/-vs-nna_atomic/ schism can be attributed to a specific commit, with a recommended restore/keep/rewrite disposition for each.

**Two primary failure classes (Andrew lock 2026-04-20, PRD §3.0 — lead-with framing in every TO):**
- **Class 1 — NNA definition change** (grain AND path): D_02 `_nna_since` cumulative→daily flip at CN-P2; canonical prefix split between `gold/canonical/nna/` and `gold/canonical/nna_atomic/` (live schism after `cd177553` partial revert).
- **Class 2 — Group D mapping ambiguity** (tagged_aua source + role-split + fee-split): no shared canonical module; D_00c, D_02, D_04 each compute their own.

**Mandatory invariant per checkpoint per advisor:** `sum(role_breakdown[*].aua) == tagged_aua` AND `fee_breakdown.fee_paying.aua + fee_breakdown.no_fee.aua == tagged_aua`. Violations = mapping-ambiguity findings cited with advisor + checkpoint + delta.

---

## Authoring iterations

| Iteration | What changed | Commit | Driver |
|---|---|---|---|
| 1. Initial 4 TOs | Time-scoped lanes (~A=T0, ~B=T1, ~C=T2, ~D=synthesis). Inherited PRD §3.3 Group D primary focus verbatim. | `0b8fc46e` | CTO HANDOFF MCP 20260420T~12:00Z |
| 2. §3.0 + §3.4 amendments | Inserted §3.0 lead-with framing at top of every `<scope>`; appended §3.4 Group B+C material-change scope as `<amendment>` block. | `4da88cef` | CTO MCPs 20260420T~12:14Z + 20260420T121431Z |
| 3. LAYER × 4-checkpoint MATRIX rewrite | Full rewrite. Each lane now owns one LAYER (silver+A / B / C / D+synthesis) and walks all 4 checkpoints. Files renamed via `git mv`: `t0-wed-baseline.md → layer-silver-and-group-a.md` etc. Sequencing gates introduced (~A→~B→~C→~D on findings-file write; data collection parallel from T+0). New §4.0 investigative-discipline rule: "rule out from the source." | `6d5b4e05` | CTO URGENT AMEND §4 MCP 20260420T~12:30Z + Andrew clarification: "layer scoped AND time scoped — at each of those times, watch how those layers have evolved, cross-reference, comprehensive." |
| 4. CTO conditional-approve rework | Added `comp-build` step as Phase 0 step #2 in all 4 TOs (right after `git worktree add`, before any comp-pipescript). Without it, comp-* tools fall through to repo-root graph at CLOUD tip = T3 and invalidate the matrix. Plus 3 minor polish notes: ~B cusip T0/T1 expected-low; ~C polars probe pin silver-input version per checkpoint; ~B/~C/~D T0 pre-window-state classification. Status flipped staged→pending; GO MCPs dispatched. | `b94014d9` | CTO SHAPE REVIEW MCP 20260420T~12:49Z |

CTO + COO workflow held tight throughout — every amendment landed in COO's inbox while authoring was in flight; rewrites caught CTO's next pass before dispatch. No agent ever saw a stale TO.

---

## Lane dispatch + sequencing

**Agents (all `0.4.0_DS_ClientPlatform` with suffix; Andrew spawned them ~12:55Z):**

| Lane | Layer | TO | SLA | Upstream gate |
|---|---|---|---|---|
| ~A | SILVER + Group A | `ADVI_STAUDT.A.ds-a-layer-silver-and-group-a.md` | 6h | none (upstream-most) |
| ~B | Group B (B_00..B_03) | `ADVI_STAUDT.B.ds-b-layer-group-b.md` | 8h | ~A findings MCP |
| ~C | Group C (C_00..C_08; OWNS Class 1 NNA path producer C_01) | `ADVI_STAUDT.C.ds-c-layer-group-c.md` | 10h | ~B findings MCP |
| ~D | Group D (D_00..D_04) + cross-layer SYNTHESIS | `ADVI_STAUDT.D.ds-d-layer-group-d-and-synthesis.md` | 12h | ~C findings MCP |

**MCP serialization verified working** — GOs landed in the correct `~A/~B/~C/~D/read/` directories (broker `to=...~A` routing via `7186b183` server change is live; the response-string "delivered to {base} inbox" is just display formatting).

**Stale Run-9 messages in ~B inbox (from COO session 32 on Friday 2026-04-17, dispatched 14:19Z + 14:27Z) flagged by ~B → confirmed disregard** (superseded by Friday afternoon B_01 cap saga ship; ~B redirected to STAUDT.B as sole focus).

---

## Lane completion + cumulative findings

### ~A — SILVER + Group A — COMPLETE (commit `0d34f025`, ~17 min from GO)
Author: `0.4.0_DS_ClientPlatform~A`. 4 deliverables shipped under `STAUDT/layer_A/`. comp-build 1162/940 nodes/edges UNIFORM at all 4 checkpoints (CTO rework honored).

- **A-1:** `silver/transactions.cusip` ABSENT T0/T1, PRESENT T2/T3 (`80917a1e`). Direct upstream for B_01 cusip-keyed RPS correction.
- **A-2:** `silver/ULN/` ABSENT T0/T1/T2, PRESENT T3 (`6c80c5ed`, opal-data-schwab). Not consumed by production scripts yet.
- **A-3:** rolling-key revert net-zero (`c270a9b2` → `32fbb0d6`). No state change.
- **A-group scripts (A_00..A_04):** CLEAN-BILL T0=T1=T2=T3.
- **Group D dimensional inputs** (advisor_assignments_history / fee_rate_history / client_dimension): UNCHANGED in window — Class 2 mapping-ambiguity upstream rule-out CONFIRMED at A-layer.

### ~B — Group B — COMPLETE (commit `fd857154`, ~5 min after ~A gate release)
Author: `0.4.0_DS_ClientPlatform~B`. 5 deliverables shipped under `STAUDT/layer_B/`. 7 material findings (B-1..B-7) + 1 clean-bill. cusip coverage probe measured **98.30% at T3** (matches session-32 baseline).

**Headline finding — B-5 (cap-stack):** Synth-inject PIVOT gates 2/5/6 + Gate 3 silent-close are **T3 only** (`5438de6e..d39c4dff`). Drives ~$390M+ synth-MV compression between Friday morning and Friday afternoon. Any advisor's MV delta T2→T3 has a B-5 propagation path. **PIVOT 5 in plain English:** skip synth-injection on accounts where Schwab allocation < $1,000 (concrete dollar gate, not subjective).

**Two clean propagation chains documented:**
- **B-4 cusip rework T2 + A-1 silver/transactions.cusip T2** — clean causal handoff (silver added the column, B_01 used it).
- **B-5 PIVOT + B-1 bond-100x + B-2 tiered cap** composite T3 MV shift → C_03 ACCOUNT_PERFORMANCE → D_02 build_advisor_books → D_04 leaderboard override.

### ~C — Group C — COMPLETE (commit `b687ff47`)
Author: `0.4.0_DS_ClientPlatform~C`. 6 deliverables shipped under `STAUDT/layer_C/`. 5 material findings (C-1..C-5) + 1 clean-bill (C-6).

- **CLASS 1 path evidence (C-1/C-2/C-4):** `c01_nna_schema_diff.md` is THE Class 1 path-sub-class evidence. nna_atomic/ schema incompatibility (no `aua_current`/`growth`/`client_state`/`aua_residual`/`nna_clean`) + Apr 14 partition gap. **C-4 confirms the LIVE SCHISM at T3** — D_00c/D_02 read `nna_atomic/`, D_04/D_00b/D_01/C_08 reverted to `nna/` per `cd177553`.
- **CLASS 2 propagators (C-3/C-5):** `gold/canonical/role_aua/` historical backfill ran on top of corrupted `account_performance` (pre-`85bb2daa` phantom outflow data). Phantom outflow pulse confirmed at T0/T1, reset at T2/T3. Both feed D_00c/D_02 tagged_aua/role-split through canonical artifacts.
- **B→C propagation chains documented:** B-1/B-2/B-4/B-5 traced through C_03; saves ~D reconstruction work.

### ~D — Group D + cross-layer SYNTHESIS — IN FLIGHT (gate released ~13:30Z)
Author: `0.4.0_DS_ClientPlatform~D`. Phase 0 data collection ran in parallel with ~A/~B/~C (started ~12:55Z). Phase 1 (layer_d_findings) + 5 SYNTHESIS docs (2A group_d_tagged_aua_decomposition + 2B group_bc_propagation_matrix + 2C delta_table + 2D bug_attribution + 2E coo_handoff) writes **just authorized** as of ~13:30Z. SLA 12h.

**~D earlier flag** (proceeding correctly per §3.3 `<if_mismatch>`): comp-blast and comp-trace cannot resolve `_weighted_aua` or `tagged_aua` as function-level nodes in `D_00c.portal_leaderboard` — ADHC_ROUTER Phase 2 known graph gap. Disposition: bug_attribution.md will cite "blast radius: ADHC_ROUTER Phase 2 — graph coverage gap"; COO will manually validate downstream blast at fix-TO authoring.

**~D no-fee logic finding:** Andrew flagged that ~D noticed a no-fee bug "certainly related to some of the issues we were seeing in the portal." Specific text awaits ~D's `bug_attribution.md`. Most likely site is **`D_00c:565` silent clip** `no_fee_aua = max(0, tagged_aua - fee_aua)` — when `tagged_aua` under-computes (e.g., Travis $82M split-weighted vs $434M unsplit), the result clamps to $0 and the advisor silently drops off the no-fee leaderboard. Combined with `D_04`'s top-level `fee_breakdown.no_fee.aua` not swept by B1.fix `5114984b`, firm-level no-fee aggregate ends up materially understated.

---

## The original concern (Andrew, this session): historical NNA explosion

**Andrew's framing:** "We had hundreds of millions of NNA in 2020-2022 despite there not even being 50-100M in AUA at that time. That was the indicator of some initial glitch or at least material change in logic regarding NNA."

This is a stock/flow violation — flows can't sustainably exceed the underlying asset base. The audit findings give us the most likely causal stack:

1. **C_03 phantom outflow pulse (pre-fix, `85bb2daa`):** before Friday, `cum_inflows` and `cum_outflows` were not recomputed on a dense date grid post-merge cumsum. Phantom pulses appeared and inflated net flow when accumulated historically. ~C `c03_phantom_outflow_probe.md` confirms the pulse existed at T0/T1 and resets at T2/T3. NNA = inflows − outflows; if a pre-fix outflow disappeared, the gap surfaced as inflated NNA.
2. **CN-P1b historical backfill on corrupted upstream (~C C-3 + C-5):** Thursday's CN-P1b emitted 2,294 historical partitions / 9.2M rows of `nna_atomic`. Historical canonical NNA was computed against the phantom-outflow-pre-fix `account_performance`, then propagated forward as if authoritative.
3. **Class 1 NNA grain change (CN-P2 `b3f6b1ee` + `ebd737e3`):** D_02 `_nna_since` flipped from per-advisor cumulative to per-(date, advisor, role) daily. The new daily decomposition reads from the same backfilled canonical — historical inflation that was previously hidden inside one cumulative number now surfaces as a daily column that doesn't reconcile against AUA. The "$100M+ NNA on a $50M AUA book in 2020" is exactly the shape that would emerge.

**Connection to ~D's no-fee finding:** if `D_00c:565` silently clips no-fee to $0 for under-counted `tagged_aua` advisors, the firm-level no-fee NNA aggregate is understated. Combined with the historical NNA inflation at the canonical layer, the residual gets routed nowhere and the per-advisor invariant `sum(role_breakdown[*].aua) == tagged_aua` fails — exactly what ~D's mandatory invariant column will measure across all 4 checkpoints.

I MCP'd this framing to ~D explicitly so the synthesis leads with it.

---

## Decisions made this session

| Decision | Locked by | Rationale |
|---|---|---|
| Lane model = LAYER × 4-checkpoint matrix (not time-scoped) | Andrew + CTO 2026-04-20 | Walking upstream-first lets each lane definitively clear its layer or identify a suspect change, passing a clean baseline to the next. Cross-references layer × time comprehensively. |
| Sequencing gate on findings-file write, NOT data collection | CTO §4.5 | Allows full Phase 0 parallelism while preserving rule-out discipline. |
| `comp-build` mandatory in scratch worktrees before any comp-* call | CTO 12:49Z shape review | Without it, tools fall through to CLOUD-tip graph and invalidate the matrix. |
| ADHC_ROUTER Phase 2 graph gap (function-level `_weighted_aua` blast) accepted; cite gap in bug_attribution.md instead of skipping | CTO + COO | Per §3.3 `<if_mismatch>`. COO validates manually at fix-TO authoring. |
| Stale Run-9 messages in ~B inbox = disregard | COO | Superseded by Friday afternoon B_01 cap saga ship. ~B redirected to STAUDT.B as sole focus. |

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| (none) | — | This session was TO authoring + dispatch + lane validation. No COO-side comp-* runs. The 4 lane agents collectively ran comp-build + comp-pipescript io + comp-blast + comp-trace + comp-platinum across their layers × 4 checkpoints; their compiler-tools-log appends are recorded under each agent's lane (~A/~B/~C committed; ~D in flight). |

No append to `org/compiler-tools-log.md` from COO this session.

---

## Commits this session (COO-authored, chronological)

| SHA | Subject |
|---|---|
| `9229c21d` | Session 33 startup reconciliation — Fri→Mon gap (project JSONs + REGISTRY + COO prompt + log) |
| `0b8fc46e` | ADVI_STAUDT 4 lane TOs staged (initial time-scoped — superseded) |
| `4da88cef` | §3.0 + §3.4 amendments incorporated (superseded by layer-scoped rewrite) |
| `6d5b4e05` | LAYER × 4-checkpoint matrix REWRITE (filenames updated via git mv) |
| `b94014d9` | CTO rework (comp-build) + minor polish + flip staged→pending + GO dispatch |

---

## Next steps

1. **~D Phase 1 + 5 SYNTHESIS docs land** (12h SLA from ~C MCP at 13:30Z → target by ~01:30Z 2026-04-21 ET; agents have been turning around in minutes so likely sooner). Final MCP to CTO + COO + Andrew at synthesis-pack commit.
2. **COO validates ~D synthesis pack** when it lands — RAVC step 4 close + flip TO status. Specifically validate that 2A/2B/2C/2D each cite specific upstream evidence-pack rows, that 2E recommendations are file+line+proposed-change+acceptance-specific (authorable without re-investigation), and that the historical-NNA framing is led with in `bug_attribution.md`.
3. **COO authors fix-TOs from `coo_handoff.md`** per ~D's restore-to-T0 vs keep-T1/T2/T3 vs hybrid recommendations. Each fix-TO inherits compiler-mandate format (`<run>`/`<expect>`/`<if_mismatch>` triad in `<phase>` blocks per locked discipline 2026-04-15). Manual blast-radius assessment for D_00c._weighted_aua / tagged_aua sites per ADHC_ROUTER Phase 2 gap.
4. **ADHC_ROUTER Phase 2 graph-gap fix** — function-level blast nodes for `_weighted_aua` / `tagged_aua` should land in next planning pass after STAUDT closes (already on backlog per `comp_learns_architecture_prd` related Phase 2 items).
5. **Project JSON updates** at STAUDT closeout — flip `status: complete`, move REGISTRY row to Completed, add to recently-closed roster in COO prompt dashboard. Andrew receives final synthesis MCP from ~D.

**Standing items unaffected by STAUDT** (carry forward from startup reconciliation):
- CP-DS1 cap-timing-rule disposition still awaits Andrew sign-off (CTO MCP 20260417T174410Z).
- AE SSM d83a1d11 completion verified per CTO session 32 (D_04 sane post-prefix-swap).
- Weekend nightly natural-fire trail status (verified clean per CTO session 32).
- ADVI_ROLGAT awaits portal-v2.x.x PROD push window.

— 2.0.0_SA_COO
