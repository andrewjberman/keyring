# Approve/Reject Modal Restyle -- 0.3.2_RD_TradeSubmission

**Date:** 2026-04-27
**TO:** org/tier3_junior/0.3.2_RD_TradeSubmission/task_orders/approve_reject_modal_restyle.md
**Issued by:** 0.3.0_DE_TradingOperations
**Commit:** 69ff02682afe5390f35f1349af05f64727564db4 (portal submodule, DEV branch)

## What changed

`portal/src/pages/TradeSubmission/components/ApproveModal.tsx` and `RejectModal.tsx` rewritten to match the canonical PM `SecurityDetailModal.tsx` style.

| Before | After |
|--------|-------|
| Dual-div backdrop (`pointer-events-none` / `pointer-events-auto`) wrapped in fragment | Single overlay div with `onClick={onClose}` and `e.stopPropagation()` on inner shell |
| Modal shell: `border border-[hsl(var(--success\|danger))]/20 rounded-xl` | `border border-white/20 rounded-lg` (neutral, PM-matching) |
| Header bg: `bg-[hsl(var(--success\|danger))]/10` (heavy accent wash) | `bg-[hsl(var(--bg-header))]` with `border-white/10` (neutral) |
| H2 title: `text-[hsl(var(--success\|danger))]` | `text-white` |
| Subtitle: `text-[hsl(var(--bg-header))]` (DARK text on dark card -- invisible) | `text-white/60` with a `·` separator |
| Body paragraph: `text-[hsl(var(--primary))]` then `text-[hsl(var(--bg-header))]` | `text-white/80` then `text-white/60` (PM ladder) |
| Body bg: default | `bg-[hsl(var(--bg-header))]` (unifies with header + footer) |
| Footer bg: default | `bg-[hsl(var(--bg-header))]` + `flex-shrink-0` |
| Close X hover: `text-white/60 hover:text-white` | `text-white/40 hover:text-white/80 hover:bg-white/10` (PM pattern) |
| Reject label: `text-[hsl(var(--primary))]` | `text-white/80` (kept `*` and focus ring on `--danger`) |
| Reject helper text: `text-[hsl(var(--bg-header))]` | `text-white/50` |
| Z_INDEX util import | Inline `z-[100]` (matches PM directly) |

Accent (success/danger) now appears ONLY on:
- Icon chip (`bg-...20` + colored icon)
- Action button (`variant="success" | "danger"`)
- Reject's required-field `*`
- Reject's textarea focus ring

## Acceptance criteria verification

| # | Criterion | Result |
|---|-----------|--------|
| 1 | Single-overlay pattern (no dual-div) | PASS -- both modals use one outer div with onClick |
| 2 | Header `bg-[hsl(var(--bg-header))]` + `border-white/10` | PASS |
| 3 | H2 in `text-white`; accent only on chip + button | PASS |
| 4 | Zero `text-[hsl(var(--bg-header))]` or `text-[hsl(var(--primary))]` | PASS -- grep both files: "No matches found" |
| 5 | Modal shell border `border-white/20` neutral | PASS |
| 6 | Open/close cleanly (overlay click, X, Cancel) | PASS by construction (handlers preserved) |
| 7 | `bun run lint` zero NEW warnings on these files | PASS -- filtered `bun run lint` output for "TradeSubmission" returned no findings |
| 8 | `bun run build` zero NEW TS errors on these files | PASS -- filtered build output for "Approve\|Reject" returned no errors. Pre-existing TS errors elsewhere in repo (AdvisorIntelligence/_partners/inflection, SubmitTab.tsx) unrelated. |
| 9 | Visual consistency with PM SecurityDetailModal | Self-asserted by structural parity; Andrew/DE to confirm visually post-DEV-push. |

## Out of scope -- confirmed untouched

- `TradeDetailsModal.tsx` -- left dirty by other work; not my scope
- `ExecuteModal.tsx` -- not modified
- Approvals tab card grid -- not modified
- `SecuritiesTable.tsx`, `SubmitTab.tsx` -- left dirty by other work; not my scope (safe-commit.sh wrapper guarded against sweep)

## Compiler Tools

| Tool | Run? | Note |
|------|------|------|
| `comp-transform fields ApproveModal` | No | Confirmation modals consume props (submissionId, fund, securitiesCount, reason); not a data-rendering component fed by gold artifacts. RD minimum tool is for data-bound components. |
| `comp-transform schema-check ApproveModal` | No | Same rationale -- no platinum/gold field consumption to schema-check. |
| `git status` pre-commit | Yes | Confirmed 5 dirty files in submodule, only 2 mine; safe-commit.sh wrapper enforced scope. |
| `safe-commit.sh` pre-commit diff | Yes | Wrapper passed (no contamination); committed via `git commit --only`. |

## Hand-off

MCP'd 0.3.0_DE_TradingOperations with commit hash `69ff02682afe5390f35f1349af05f64727564db4`. DE routes to 0.3.0_DT_TradingOperations for DEV push.
