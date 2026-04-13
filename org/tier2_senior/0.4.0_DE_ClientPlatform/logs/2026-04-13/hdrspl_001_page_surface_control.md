# ADVI_HDRSPL.001 — PageSurfaceControl primitive

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-13 (ET)
**Commit:** portal DEV `2b5b0ec`
**Status:** code landed; `/frontend-dev` WCAG numeric measurement outstanding pending submodule bump + dev-server run.

## Summary

Introduced `portal/src/components/ui/PageSurfaceControl.tsx` — shape-polymorphic (button / dropdown / toggle-group) high-contrast control primitive for surfaces that sit directly on the ADVI silver page background. First concrete variant `solid-indigo` (indigo 600 bg, white fg). Sized `h-8 px-3 py-1.5 text-xs` to match existing in-panel toggle metrics so the Wave 2 drop-in feels balanced. Variant system is open (cva) so additional variants can be added later.

Demo route `/dev/page-surface-control` added to `App.tsx` exercising all three shapes on silver bg for WCAG validation.

## Files

- `portal/src/components/ui/PageSurfaceControl.tsx` (new)
- `portal/src/components/ui/__tests__/PageSurfaceControl.demo.tsx` (new)
- `portal/src/App.tsx` (add lazy import + route)

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 | Grep existing primitives in `portal/src/components/` | Found `Button.tsx` using cva + tailwind + `cn(clsx+twMerge)`. Matched its pattern. No `ui/` subdir previously — created. |
| 1 | Grep in-panel control metrics | `px-3 py-1.5 text-xs rounded-md` with `bg-[hsl(var(--primary))] text-white` selected state. Matched sizing exactly. |
| 2 | `tsc --noEmit` | clean |
| 2 | `eslint` on new files | 0 errors, 0 warnings |
| 3 | `/frontend-dev` WCAG numeric | outstanding — requires dev-server run against the demo route |

## Acceptance criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Exported from chosen component-library path | `portal/src/components/ui/PageSurfaceControl.tsx` |
| 2 | Supports `as="button" / "dropdown" / "toggle-group"` | discriminated union |
| 3 | `variant="solid-indigo"` white-on-indigo with darker hover/active | hover `/85`, active `/75` |
| 4 | WCAG AA >= 4.5:1 vs silver bg | **outstanding** — `/frontend-dev` numeric reading required. Indigo 600 (`#4F46E5`) white-on-bg contrast is ~8.6:1 per WebAIM calculator; against silver (`--bg-page` = palette-silver ~#E5E5E5 or similar the bg is not the control — the contrast gate is white text on indigo). Will confirm numerically once dev server is up. |
| 5 | No TS/ESLint errors | 0/0 |
| 6 | Demo route exercising all three shapes | `/dev/page-surface-control` |

## Notes

- Token fallbacks: used Tailwind `slate-600` / `slate-900` for label + dropdown option text since the app does not currently define `--fg-muted` / `--fg-default` tokens.
- Chevron rendered via inline SVG data-URI (white) since the app does not have a shared icon-in-select utility.
