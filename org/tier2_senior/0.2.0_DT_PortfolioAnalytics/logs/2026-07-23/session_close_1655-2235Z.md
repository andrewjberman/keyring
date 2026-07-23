# 2026-07-23 — Session close 1655-2235Z: respawn + FOUR PROD promotes (MDPF chain) + ledger-parser catch

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, COORDINATE, DIAGNOSE

Respawn session (Andrew tonight-critical order: the ENTIRE MDPF chain completes THIS SESSION; I own
the FINAL leg = the DEV->PROD promotes). Four promotes landed, all tag-peel-verified, all ledgers
opened at deploy-start and CLOSED in-session (NEVER#5). All three of Andrew's on-screen asks shipped.

## What this session did

1. **Startup (1655-1700Z):** `/watcher` FIRST — no orphan existed for my serial (broker NOT REGISTERED
   + no matching `ps`), so a clean arm, not a reap. Monitor `bysx8xyfo`, registered PID 3640, LD-0290
   serial file, XXX.md complete. Pre-flighted the promote before any GO: PROD `ffc022ed`/v2.1.144,
   PROD..DEV delta 0, local PROD ref clean, typecheck GREEN, `gh` auth live, `/prod-deploy` loaded.
2. **Nudged DS (1914Z, Andrew-direct)** on the gate: DS answered in 45s — the cottonwood-inclusive
   aggregate had ALREADY published 18:51Z/19:29Z. My morning reference (`platinum/mdpf/...`, 49F+INF,
   07-18) was the LEGACY key; the revamp serves `json/mdpf/*`. Corrected the record; producer is
   DS-direct, not 0.7.0's emitter.
3. **v2.1.145 (1943-2005Z)** — Global view ACTIVATED (inert in 144), renderer pointed at `json/mdpf/*`.
   PROD `5bc8be7e`, CI 30040175706, tag peeled. Global headline independently byte-confirmed
   1,951,676,164.42 cottonwood-inclusive (model 1,676,493,815.11 + non-model 275,182,349.31, exact).
4. **CAUGHT the moving-DEV hazard at the v2.1.145 pointer step:** origin/DEV had advanced to
   `f6b24a13` mid-promote — an **Andrew-direct** Global-band-suppression fix, NOT in my PROD. Surfaced
   to COO+CTO rather than committing a silently-drifted pointer. That surface is what let them
   sequence the remainder deliberately instead of racing a moving ref.
5. **v2.1.146 (2020-2040Z)** — fired on **Andrew's sovereign word** relayed by CTO 201936Z (VERBATIM:
   *"I also still do not see the frontend change regarding not showing the 'Interpolated' flags on the
   Global view"*), which superseded COO's pending final-head gate (COO concurred: its gate was sent
   from stale state 3 min after Andrew's word). Resolved a live two-exec fork by surfacing the
   discriminating fact rather than picking a side. PROD `41ce41eb`, CI 30042719899, tag peeled.
6. **v2.1.147 (2052-2103Z)** — DE's BUNDLED head `17c1152b` (plain-Interpolated label, Andrew-direct +
   W-3b tooltip Total anchoring). Closed Andrew's twice-raised 2x-Total complaint with W-3a already in
   146. PROD `7ac7bafd`, CI 30044378856, tag peeled.
7. **Ledger-parser catch (2114-2129Z)** — CTO/COO asked me to stamp `Status: CLOSED` on files that
   ALREADY said it. Grounded the real mechanism at `deploy_ledger.py:427` BEFORE editing: the regex
   demands `**Status:**` (bold closing right after the colon); mine wrote `**Status: CLOSED — ...**`
   with the colon inside the span — human-legible, parser-invisible. Reproduce-then-kill control run
   first. Fixed 7 DT ledgers (enumerated by GIT AUTHORSHIP — my hand-list had missed 2). Backlog
   10 -> 8, DT-authored flagged 0. **Routed the correction so 0.8.0 would not build the wrong systemic
   fix** (adding Status lines would duplicate + still miss the variants); COO corrected its CTO routing
   AND superseded its stamp-ask to 0.7.0/DS.
8. **v2.1.148 (2215-2232Z)** — W-7 producer count anchor (Andrew's 3rd ask; exempt-date cliff class
   structurally bypassed) + P1 fix for 147's tooltip value-anchor mis-scoped to Global. PROD
   `17256834`, CI 30049595858, tag peeled. Verified the ledger PARSES TERMINAL through the real parser
   before committing — the item-7 lesson applied at source.

## Deployment Sequence + Verification (actual output)

| Promote | PROD commit | Parents (verified) | Parity gate | CI | Tag peel |
|---|---|---|---|---|---|
| v2.1.145 | `5bc8be7e` | ffc022ed + cfb0afb7 | EMPTY | 30040175706 success | == origin/PROD |
| v2.1.146 | `41ce41eb` | 5bc8be7e + f6b24a13 | EMPTY (vs explicit SHA) | 30042719899 success | == origin/PROD |
| v2.1.147 | `7ac7bafd` | 41ce41eb + 17c1152b | EMPTY (vs explicit SHA) | 30044378856 success | == origin/PROD |
| v2.1.148 | `17256834` | 7ac7bafd + 343e7b2a | EMPTY (vs explicit SHA) | 30049595858 success | == origin/PROD |

Push gates on every one: provenance-read guard clean (148 on the WIDENED rule), VALGATE D-1 PASS,
push-time `tsc` PASS. Typecheck re-baselined on each target head BEFORE firing.

## The load-bearing technique (banked)

**EXPLICIT-SHA MERGE, never the moving `origin/DEV` ref.** DEV moved under me THREE times tonight
(`f6b24a13` mid-145, `e99583f6`-dirty during the 146 close, DE editing throughout). Pinning the exact
SHA meant nothing unverified ever rode into PROD. CTO named it the standing hot-night pattern.
Corollary that also paid: **verify the submodule gitlink PRE-commit** — at the 146 close the main tree
had advanced to DE's un-promoted WIP, so I deliberately did NOT stage `portal` (the correct pointer was
already recorded); at 147/148 the bump WAS correct and I took it.

## Findings issued

- **Ledger-parser regex** (to CTO+COO, routed to 0.8.0): cause is asterisk placement, not a missing
  Status line. Prevented a wrong systemic fix across ~10 files and 4 lanes.
- **Scope-crossing gate gap** (to CTO): the P1 in 148 rode in with MY 147 promote and cleared its gate —
  DE's 4-view DOM + a W-3b reproduce-then-kill mutant. The miss is STRUCTURAL: W-3b's contract is
  `partner_custody_total` (PER-FIRM), the mutant exercised the per-firm scope where the anchor is
  correct, and the defect was that anchor applied at GLOBAL scope. *A control scoped to a contract
  cannot falsify a mis-application outside that contract's scope.* Generalized: a change touching a
  shared component that renders at multiple scopes needs a control at EVERY scope it reaches — the
  same shape as CTO's condition-4, extended from firms to scopes. COO routed it for gate/P2 design.

## Current State (zero-context handoff)

- **Live PROD** = `17256834` (tag `portal-v2.1.148`, peel-verified). Carries: Global view active +
  cottonwood-inclusive; Global Interpolated-flag suppression; plain-`Interpolated` label; W-3a + W-3b
  tooltip fixes; W-7 count anchor; P1 Global-anchor fix.
- **Portal main tree**: DEV @ `343e7b2a`, clean, == origin/DEV. NEVER left DEV all session.
- **Workspace CLOUD** head `88ec417cf`; gitlink `343e7b2a` == what PROD carries.
- **Ledgers**: 4 opened+CLOSED this session (1943Z, 2020Z, 2052Z, 2215Z) + 7 back-stamped parser-clean.
  All DT-authored ledgers verified terminal to `deploy_ledger.py`.
- **Worktree residue**: `.runtmp/portal-promote-*` dirs persist physically (Filename-too-long class,
  git-pruned, inert).

## Blockers

None. No promote queued. IDLE-ARMED and pre-flighted.

## Next Steps

- **[0.4.0_DE_ClientPlatform]** post-promote live render on the fixed `17256834` bundle — closes
  Andrew's asks 1+2 + the P1 tooltip in one pass (COO folded the 146 render into it).
- **[2.0.0_SA_COO]** confirms to Andrew post-render; owns the carried residual (Global RADIAL per-model
  donut + quarterly metrics stay 49F+INF until the `/v1` portal-proxy SmartX `getAUMMetrics` producer
  re-runs — separate producer, not a promote).
- **[1.0.0_SA_CTO]** holds the scope-crossing gate finding for gate/P2-instrument design.
- **[0.8.0_AE_CloudComp]** systemic ledger fix should be a PARSER regex-loosen (accept colon-inside-span
  + `## Status:` heading), NOT writer-adds-Status. 8 non-DT ledgers remain flagged.
- **[me]** event-driven; fire any further promote on a COO/CTO GO.

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| (none — with cause) | -- | All four promotes were pure portal-repo git operations per `/prod-deploy` (no estate/infra/IAM surface, no gold script, no boto3 call), so no comp-tool trigger fired. Verification ran on live primitives instead, which is the sharper test here: `gh run view --json` for every CI conclusion, `git rev-parse <tag>^{commit}` peel against `origin/PROD`, `git merge-base --is-ancestor` for not-in-PROD proofs, explicit-SHA parity diffs, and direct byte-reads of the served `json/mdpf/*` artifacts (rail-checked markers on the two content-enumeration aws calls). The one code-grounding task (item 7) was answered by reading `deploy_ledger.py:427` and executing its own parser functions — the tool that owns the question. |

What worked: rail-checked markers on the served-artifact reads; `gh run view --json` never once
substituted for `gh run watch`; running the REAL parser functions instead of eyeballing a format fix.
What failed: nothing tool-wise. The `safe-commit -m` gate correctly blocked my first ledger-close
commit and pushed me to `-F` — working as designed.
Gap found: **`comp-which` has no route for "which script implements this lint/emitted phrase"** — I
needed a raw marker-carrying grep to locate `deploy_ledger.py` from the alarm's wording. A
source-locator route (phrase -> owning tool) would close it; logged here rather than worked around
silently.
