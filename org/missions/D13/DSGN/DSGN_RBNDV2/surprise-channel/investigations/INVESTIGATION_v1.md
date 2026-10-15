# DSGN_RBNDV2 -- surprise channel, INVESTIGATION v1 (laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "DSGN_RBNDV2-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~RB",
    "surfaced_at": "2026-10-15T03:59:17Z",
    "one_line": "Turning every panel variant white (C-PANEL) makes light-on-dark text idioms inside panel bodies near-invisible: 140 page files under portal/src/pages carry text-white, and the portal's own law says chart/mixed panels stay dark BECAUSE those idioms depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarmed when round 1's token cell lands the scoped ink-inversion rule and /market renders readable in the COO's close run; the walk (FWD-5, round 3) re-measures the rest.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/CLAUDE.md 'Known divergence': Panel variant chart/mixed resolve to the band and --bg-header/--bg-medium/--bg-card alias it because 4,887 light-on-dark idioms in src/pages/ depend on a dark container (rows DSGN_REBRND-W1-S9, W2-S5)",
        "portal/src/ui/components/panels/Panel.tsx:60-78 variant map: heatmap and nested are already white with dark text, chart and mixed are band-valued",
        "native Grep at the laptop portal checkout @97c66c93 (origin DEV is ad7c100b, not yet fetched): files under src/pages matching text-white 140, bg-white/ 96, border-white/ 92, of 397 page .tsx files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-PANEL: the panel primitives render a white surface with a 1px #C4CBDB border and 'no page file is edited for FWD-3's panel half'; FWD-3 ACCEPT: panels are white; FWD-5 expects only a FAINT red/green/signal colour on the new ground.",
    "world_is": "Page bodies inside chart/mixed panels were written for a dark ground and use text-white idioms; on a white panel those read invisible (white on white), a worse class than the 'faint' colour FWD-5 anticipates, and a page-file edit is not permitted for the panel half. No action taken beyond cutting round 1 so the token cell carries one scoped rule (inside the light panel, text-white/N reads navy ink) at the token seam; the walk re-measures.",
    "notes": "Ruled inside the COO's own decomposition (/canonical-drive obligation 7): no ENDPOINT change, no page edit. The counts are the laptop checkout's vintage; the first-issuance fetch to DEV's tip re-measures them. Not blocking the decomposition draft."
  },
  {
    "id": "DSGN_RBNDV2-W2-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The RB1S-AC2 difference control cannot report four of four: the base App.tsx declares SidebarLink as a function and has no const form, so the control reports three of four markers present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show ad7c100b5c:src/App.tsx line 165 reads 'function SidebarLink({' and no line of the base declares 'const SidebarLink' (native Grep over the base text)",
        "portal/src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-s.app-seam.test.ts@14b719cc base-control output: {\"NAV_SECTIONS\":true,\"function SidebarLink\":true,\"const SidebarLink\":false,\"<aside\":true}"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1S-AC2 (task order DSGN_RBNDV2.TO-RV-s-1): the same text checks run against git show ad7c100b5c:src/App.tsx report all four present, proving the test can fail.",
    "world_is": "The base carries NAV_SECTIONS, function SidebarLink and <aside, and no const SidebarLink. The test keeps the four absence arms on the current App.tsx (all hold) and asserts the three base markers present; the const marker is recorded as absent in the base output, not forced to present. The verdict was not weakened to pass.",
    "notes": "Raised for the COO's ruling on whether the control should name the function form."
  },
  {
    "id": "DSGN_RBNDV2-W2-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The collapsed-rail logo in the base is opal-icon-white.svg, which is invisible on the light sidebar ground; RV-s-1 renders opal-icon-black.svg for the collapsed icon.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show ad7c100b5c:src/App.tsx line 315 reads src=\"/logos/opal-icon-white.svg\" for the collapsed toggle icon",
        "portal/public/logos/ at ad7c100b5c ships opal-icon-black.svg, opal-logo-black.svg, opal-icon-color.svg and opal-logo-color.svg beside the white pair"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order RV-s-1: the COLLAPSED 48px icon rail keeps the current icons and its behaviour, on the same ground and border.",
    "world_is": "The current collapsed logo is white, so on the lavender ground it does not render. RV-s-1 switches only that asset to the existing black icon; the expanded wordmark is text per the A-light fixture. Whether navy ink or black is the right ink for the icon is a judgment for Andrew's read at the drain (RB1S-AC3).",
    "notes": "No new asset was added; the change is the src string of one image."
  },
  {
    "id": "DSGN_RBNDV2-W2-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The account-menu popup in App.tsx keeps its dark styling (bg-header, white/10 border, text-white/80) beside the light sidebar, because the order names the App.tsx edit as the extraction only.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarm when the account-menu popup is restyled to the light ground (in round 1's ink pass or a follow-on cell) and reads at the drain.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/App.tsx@14b719cc user-menu popup div: className bg-[hsl(var(--bg-header))] border border-white/10 rounded-[4px], and its two buttons use text-white/80 hover:bg-white/10 hover:text-white",
        "portal/src/App.tsx@14b719cc still computes the popup width from 14rem (w-56) and left 3.5rem/0.75rem, unchanged from the base"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order RV-s-1: 'This is the only edit to App.tsx' (the extraction); the foot is restyled to the light board; the popup is not named.",
    "world_is": "The popup opens from the restyled light foot and renders dark with white/80 text. If the token cell repoints --bg-header light, its text becomes near-invisible, the same class of defect as DSGN_RBNDV2-S1. The popup's width calc still refers to the old w-56 sidebar width (14rem minus padding); it is not moved by this cell.",
    "notes": "Left in place deliberately: restyling it would be a second App.tsx edit the order does not grant."
  }
]
```
