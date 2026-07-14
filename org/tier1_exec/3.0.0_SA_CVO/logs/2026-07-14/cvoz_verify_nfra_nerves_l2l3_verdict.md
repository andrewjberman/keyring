# /verify NFRA_NERVES L2+L3 — VERDICT: **SOUND** (one P2 finding)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO~Z · 2026-07-14 ~073x-074xZ
**Commission:** 1.0.0_SA_CTO~Z formal commission 072145Z (supersedes my proactive self-scope, per my own offer).
**Subject:** delivery commits `4b9a04954` (PRD v1.0) / `17911a819` (L2) / `907620c80` (L3a) / `6acff6026` (L3b) / `08a3c1094` (lane-split + F3 rider).
**Routing:** CTO~Z ONLY, per the Andrew-direct ~Z comms partition (recorded @ `76fad8514`). This committed file is the record COO folds from later.
**Constraint compliance:** every step was a read-only graph/text query or a self-test; no verb touched the frozen three; nothing created/resolved a basename collision or turned a RED guard GREEN; the INF chain was not advanced (functional test applied per step).

---

## L2a — ONE resolver: **PASS**

- Import graph: all three layers COMPOSE the keystone — `nerves_traffic.py:55` (`from nerves_resolve import resolve_many`), `nerves_accrete.py:53` and `nerves_lexical.py:56` (`from nerves_resolve import resolve`). None re-implements resolution.
- Lexical sweep (comp-grep, on-rails; denominator printed by the tool): `def resolve` → **7 matches / 6 files / 438 files scanned** in `org/modules/graph/`. The 5 non-nerves hits are pre-existing, differently-scoped functions (`comp_dispatch.resolve_ids` = TO chains; `comp_gitdrill.resolve_files` = git queries; `comp_toolgraph.resolve_backends`; `extract_routes.resolve_s3_key`; `graph_cache.resolve_freshness`). No second ref→node-address resolver exists in the substrate.
- `nerves_resolve --self-test`: **10/10 live** (graph/compiler/repo/cloud tiers, bash-shim + bare-function + frozen-file addressability, UNADDRESSED-is-a-finding, denominator-present, WEAK-band-exists).

## L2b — universal traffic record: **PASS** (with P2-1 below)

Exercised live twice (my invocations, not the builder's):
- `scan --since-days 35 --limit 6000`: 24,338 seen | 9,755 attempts | 6,904 addressed → 70.8%; REFS 16,399 addressable-shaped (labeled **"THE DENOMINATOR"** in-output) | 4,444 unaddressed → 72.9%; LEXICAL 8,112 banded-not-counted; **PHANTOM-LIMB 729** (delivery 718 + a day's corpus growth — direction and magnitude consistent).
- `--limit 100000`: 119,062 seen | 10,475 attempts | 7,611 addressed → 72.7%.
- **Per-stream anchors reproduce the delivery exactly:** git 99.1% of attempts (delivery 99.0%), runs **100.0%** (the bash-shim fix holding), telem **0 attempts with the hard limit stated in-output** ("records THAT a tool ran, NOT what it touched").
- UNADDRESSED is a visible top-12 band (CloudFront/FIRM_ID/TypeScript/data_as_of/...) — never dropped; matches the claimed honest-blind-spot classes.
- `--self-test`: **10/10 live**, including both denominator controls (english-words→lexical-band-zero-misses; path-shaped ghost still fires).

## L3a — CO_CHANGE accretion + consumer: **PASS**

- Committed artifact `nerves-edges.json`: **270 edges exactly**; stats block prints every denominator (6,688 commits / 5,281 files / 10,258 candidate pairs / min_support 3 / half-life 21d) and the sweep exclusion **on its face** (28 commits > 25 files excluded).
- **Asymmetry preserved, not averaged:** both `conf_src_to_dst` and `conf_dst_to_src` on every edge; 207/270 differ materially.
- **My independent control arms (not the builder's pairs).** I recomputed co-change from raw `git log --name-only` myself (denominator: 6,729 commits scanned, 2,587 kept at 2–25 files) and cross-checked mid-list pairs:
  - `advisor_timelock.py <-> tests/test_advisor_timelock.py`: my git-truth support **7** == artifact support **7**, conf 0.875/1.0 — and the asymmetry is semantically right (every test change accompanied the lib; the lib moved once without the test).
  - `inflection_rep_scope.py <-> test_aor_fold_derivation.py`: my git-truth support **8** == artifact support **8**.
  - Negative discrimination: my hand-picked "obviously coupled" pair (`smartx_assets_pull/pull.py <-> smartx_client.py`) has git-truth co-change support **1** → correctly **ABSENT** (min_support=3). My hand-chosen control measured the author, not the instrument — the instrument was right.
- `--self-test`: **6/6 live** (273 edges from 6,723 commits — today's corpus; decay monotonicity + both control arms held).
- **Consumer exercised:** `comp-blast build_dashboard` prints the CO-CHANGE layer under the structural blast **with its commit denominator** (6,688) — 5 rows (4 @ 27%/n=4, 1 @ 20%/n=3), matching the delivery example, with the drift-predictor framing and the Goodhart line ("a coupling is a fact about history, never an endorsement").

## L3b — THE LEXICAL UNLOCK: **PASS**

Each frozen file exercised in its **own invocation**; negative controls **separate**:
- `comp-blast build_assets_dim.py` → **!! HOLD, 47 claims**, doc:line cited (`docs/references/INCIDENTS_2026-07-13.md:54`, `memory/MEMORY.md:81`, `memory/project_inf_chain_held_shut_...door5.md:3`, ...). The HOLD prints on the verdict's own stream **before** the NOT-FOUND path — the graph does not model the silver tier, and the warning fires anyway (bug #4's fix live: the hold is a fact about the FILE, not our modelling of it).
- `comp-blast _orion_api_silver_lib.py` → **!! HOLD, 37 claims**, carrying `[ambiguous ref -- verify it is THIS file]` — the over-warn-on-HOLD asymmetry (bug #3's split) working: ambiguous HOLDs kept-and-marked, never dropped.
- `comp-blast convert_transactions_to_silver.py` → **!! HOLD, 4 claims**.
- Negative control 1 (builder's cited clean file, separate run): `INF_D_02b.top_holdings.py` → **no HOLD banner** (grep count 0).
- Negative control 2 (**my own pick**, same INF gold neighborhood — the sharpest discrimination: frozen-three vs their own chain-mates): `INF_D_00d.cumulative_chart.py` → **no HOLD/RISK/DOCTRINE banner**. The instrument can fail, and doesn't.
- `nerves_lexical --self-test`: live PASS incl. `ACCEPTANCE.ALL_THREE_frozen_files_carry_a_HOLD` ({build_assets_dim: True, _orion_api_silver_lib: True, convert_transactions_to_silver: True}) and `citation.every_claim_cites_doc_and_line`; corpus 1,469 docs / 619 HOLD-carrying nodes.

## F3 rider (in `08a3c1094`): **PASS**

Verified at source, not from the commit message: the docstring hunk in `.tools/comp-which-routing-test.py` keeps the delta-refreeze RULE, removes the retracted premise ("re-derives from the live rail log each run"), re-grounds it on both-ends-one-frozen-cohort (exactly how the 26.441%→25.050% n=562 measurement was made), and carries the provenance block naming the retraction with `:87-93` line cites. A doctrine line no longer rests on a claim its author withdrew.

---

## Findings

- **P2-1 (declarative, CTO~Z): the L2b headline snapshot is not re-derivable from the record.** "18,244 events / 60.9% hit-rate / REF 10,347" appears in `17911a819` and `org/projects/NFRA_NERVES.json` **without the invocation that produced it** (`--limit`/`--stream` materially change all three numbers; rail is UNCAPPED in `--stream all`, so no flag combination I could reconstruct reproduces 18,244). My re-takes (70.8% @ limit-6000, 72.7% @ limit-100000, phantom 729) are directionally consistent and every per-stream anchor matches, so nothing contradicts the claim — but a headline number without its invocation is the same class as a line citation without a vintage. Mechanism-specific fix (owner: CTO~Z, next touch): print the full argv + per-stream row-counts into the summary block (the tool already prints denominators — add the invocation), and pin flags beside any number quoted into a commit/JSON. Not gate-blocking; the instrument itself is honest.
- **FYI (environment, not NERVES; no action owed by CTO~Z):** comp-blast printed `STALE_NODE_WARN: lambda:opal-assets-ingest-mirror` SHA drift since last comp-build — C2 mirror work landed after the last build; the provenance discipline is doing its job. Routine `comp-build` refresh clears it.

## Unknown-unknowns (mandatory)

What the commission did not ask: **whether the risk-edge corpus REBUILDS on doc change.** The lexical unlock's 41,540-line `nerves-risk-edges.json` is a committed artifact; the HOLD verdicts I exercised read the corpus as of its build. When the INF hold LIFTS (the standing expectation), the hold claims in memory/MEMORY.md and the hold doc go away or invert — and a **stale danger map that keeps shouting HOLD after the sovereign lift is the same instrument-lies class in the other direction** (it trains agents to ignore warnings, bug #3's own rationale). Nothing in L2/L3 states the regen trigger or staleness bound for `nerves-risk-edges.json`/`nerves-edges.json`. That is L1/L5 territory (standing producers / pulse) — but the artifacts shipped NOW and the lift could come before L1 does. Worth one line in the PRD naming the regen owner + trigger.

## Verdict

**NFRA_NERVES L2+L3: SOUND.** All commissioned limbs PASS by exercise; the one P2 is a reproducibility-discipline nit on a recorded number, not a defect in the shipped instruments. The lexical unlock discriminates in both directions on my own controls, and the frozen three all warn with citations — the danger map is live.

— 3.0.0_SA_CVO~Z
