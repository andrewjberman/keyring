# DSGN_AMGTV1 round 31 -- CTO product-file review of portal 76a15c1b, `1.0.0_SA_CTO~Z`, 2026-10-03 ~17:4xZ

**Ask:** `2.0.0_SA_COO~D` msg 28895. Worktree `C:/tmp/wk-dsgn-amgtv1-82`, branch `dsgn-r31-onto-dev`, portal HEAD `76a15c1b0e`
(clean tree). It supersedes 2defab11.

**Ancestry, measured:** 2defab11 (rounds 29+30, approved @813d446c3b with ADDENDUM 1 @6fdc774fa2) is an ancestor, and so is origin DEV
`525c9404` (fetched 17:3xZ), so the landing is a fast-forward of current DEV. The only content new since this seat's last review is
two commits.

## What I read (every hunk)

| commit | files | verdict |
|---|---|---|
| `d32aa7ca` AV-zi-2 | `HeaderBrief.tsx`: `FEED_OPEN_AT_REST` 2 -> 1 | OK. SAUX-15 is MET per COO~D's close walk: the first panel sits at y 894. |
| `28a1a16c` AV-zi-1 (FWD-26) | `amgt-lead-panel.ts`, `LeadPanel.tsx`, `ChatterBubbles.tsx`, `PriceBars.tsx`, `useLeadPanelApi.ts`, `constants.ts`, `types.ts` | **OK.** One `Segmented` 30D / 90D / 365D (30 at rest) is held in LeadPanel and sent as `?days=` to BOTH routes. Each window has its own query key. The month cursor is retired: the Chatter face draws the served window's `articles_total`. The Price face prints the served `window_reason` as its designed empty state when a window serves 0 rows. RESAPP serves that key (`rolling_windows.price_window_not_produced`: `window_reason` and `ranking_reason`, `rows: []`, read at HEAD), so the 90D / 365D price presets render the qualified wait AS SERVED, deployed at KQSA62c3 (RESAPP round 64). |

**Noted, not blocking:** the chatter caption composes "Articles collected over the last N days to <end>, since <start>" from served
`window_days` / `window_end` / `window_start` instead of printing the served `window_note`. That is formatting of served values, with
no number invented (C-PRESENTATION-ONLY).

## Measured by this seat

- `tsc --noEmit -p tsconfig.app.json` on 76a15c1b: rc=0, 0 lines.
- COO~D's battery: no skip, all green (`round31/ROUND31_CLOSE.md` @b742fd0687). Its two issuer check amendments are COO~D's, cited
  there.

## Verdict

**APPROVED** for portal DEV as ONE landing carrying rounds 29, 30 and 31 (76a15c1b, a fast-forward of DEV 525c9404). It supersedes
2defab11 as the DEV candidate. The DEV push is `0.0.0_AB_MSTR~Z`'s on Andrew's word. If DEV moves again before the push, MSTR~Z merges
current DEV first (no rebase), runs battery29, and reads the overlap; a SecurityAnalysis overlap comes back to this seat. PROD stays
gated.
