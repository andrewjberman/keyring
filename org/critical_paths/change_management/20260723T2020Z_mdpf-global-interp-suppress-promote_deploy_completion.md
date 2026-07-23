# Deploy Completion — MDPF Global Interpolated-Suppression Promote (portal DEV->PROD v2.1.146)

**Status: CLOSED — completed in-session (NEVER#5). PROD 41ce41eb, tag v2.1.146 peel-verified.**
**Owner:** 0.2.0_DT_PortfolioAnalytics
**Authorization:** ANDREW-DIRECT (sovereign) at CTO's terminal 201936Z, VERBATIM: "I also still do not
see the frontend change regarding not showing the 'Interpolated' flags on the Global view." His word IS
the GO — supersedes the pending COO relay (COO acknowledged its 202228Z final-head gate was sent from
stale state 3 min after Andrew's word; both execs confirmed PROCEED — CTO 202837Z, COO 202839Z).
CTO co-owner concur 201700Z from the serve-arc side. RENDERER-DEPLOYED satisfied (renderer-only vs keys
already serving).
**Window:** 2026-07-23 ~20:20Z (Andrew-direct GO / begin) -> ~20:40Z (CI SUCCESS + tag peel-verified)

## Scope
Promote portal DEV @f6b24a13 -> PROD (v2.1.146). Follow-on to v2.1.145 (which ACTIVATED the Global view
but postdated f6b24a13, correctly excluding it). f6b24a13 = Andrew-direct x2 fix:
(1) Interpolated treatment is PER-FIRM only — the Global view SUPPRESSES band/overlay/legend/bar-outlines
    via the one trendInterpolatedDates choke point (materiality ruling; provenance channel still consumed;
    Cottonwood keeps full labeling; DOM-proven 0 interp-regions Global / 1 COT).
(2) W-3a tooltip double-count — interp_total is an ANNOTATION, excluded from tooltip total AND rows.
Renderer-only vs the json/mdpf/* keys already serving correct bytes — no artifact churn, no serve re-entry.

## Rollback
Rollback ref = PROD **5bc8be7e** (current head, tag portal-v2.1.145).

## DE evidence rider (recorded, DE-owned, trails the promote — non-blocking per CTO 201700Z)
(1) W-3a tooltip planted-mutant proof (naive-sum date fails pre-fix / passes post-fix) per the W-3 gate.
(2) post-promote live-verify all firms (condition-4, shared component): Global suppression +
    Cottonwood-keeps-labeling split renders exactly per Andrew's per-firm materiality ruling.

## Evidence
| Gate | Result |
|---|---|
| Delta at GO | 1 commit origin/PROD..origin/DEV = f6b24a13; local PROD reasserted to 5bc8be7e (Step 3) |
| Typecheck (pre-promote) | GREEN rc=0 on f6b24a13 (pre-flight); re-confirmed at push via VALGATE tsc |
| bun install | foreground rc=0 (420 packages) |
| Merge | --no-ff `41ce41eb` of EXPLICIT SHA f6b24a13 (not moving origin/DEV — DE was live-editing); parents == 5bc8be7e + f6b24a13 EXACTLY; 1 file (ModelPortfolios.tsx, the trendInterpolatedDates choke point) |
| Parity gate | git diff f6b24a13 HEAD == EMPTY (vs the explicit target, not the moving ref) |
| Push gates | provenance-read guard clean, VALGATE D-1 PASS, push-time tsc PASS |
| PROD commit | 41ce41eb6768b6ce8665558aa078140c1375f275 (5bc8be7e..41ce41eb) |
| CI | run 30042719899 conclusion: success (gh run view --json), headSha 41ce41eb |
| Tag | portal-v2.1.146; annotated; peeled ^{commit} == origin/PROD head EXACTLY |
| Workspace pointer | NO bump needed — gitlink already f6b24a13 (pointer CLOUD 63ddc1fcc from v2.1.145) == exactly what PROD now carries; portal deliberately NOT staged (main tree had advanced to DE's un-promoted e99583f6-dirty WIP — staging it would have wrongly captured v2.1.147 work) |
| Main tree | on DEV (advanced to e99583f6-dirty = DE's v2.1.147 WIP, DE-owned); ended at workspace root; worktree pruned (physical dir persists, Filename-too-long, inert) |

## Sequencing (COO 203949Z, CTO-aligned)
v2.1.147 = e99583f6 (plain-Interpolated label, already on origin/DEV) + W-3b non-model wiring in ONE
bundled head DE is committing now (~30-40min, mutant-gated). DT HOLDS v2.1.147 — does NOT promote
e99583f6 alone; GO on COO's word at DE's W-3b head committed + 4-view DOM + mutant gate PASS.
Rollback chain: 146 -> 5bc8be7e; 147 -> 41ce41eb (146's head).

## DE evidence rider (recorded, DE-owned, trails — non-blocking per CTO 201700Z)
(1) W-3a tooltip planted-mutant proof (naive-sum date fails pre-fix / passes post-fix).
(2) post-promote live-verify all firms: COO live-verifies Global 0 interp-regions on DE's relay.
