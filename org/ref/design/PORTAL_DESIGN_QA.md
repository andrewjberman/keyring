# Portal Design QA Reference

Reference for all RD agents. Read before every portal session. Run the Pre-Commit
Checklist before committing any visual changes.

Adapted from Impeccable (Paul Bakaus, Apache 2.0) for the Opal dark-mode data portal.

---

## 1. Control Label Standard (Canonical Pattern)

Every dropdown, toggle, or selector label in a page control bar MUST use:

```tsx
<span className="text-xs text-white/50 tracking-wider">Label:</span>
```

Rules:
- **Always** Title Case with colon: `View:`, `Period:`, `Display:`, `Metric:`
- **Always** `text-xs text-white/50 tracking-wider` -- no exceptions
- **Never** `text-sm`, `text-[10px]`, `font-medium`, `uppercase`, `/40`, `/60`, `/80`
- **Never** omit the colon
- `<span>` or `<label>` element -- either is fine, but style must match exactly

This was audited and standardized across all 14 portal pages on 2026-04-07.

---

## 2. Typography for Data-Dense UIs

### Tabular Numbers

All numeric columns in data tables MUST use tabular figures for vertical alignment:

```css
.data-table { font-variant-numeric: tabular-nums; }
```

In Tailwind: `tabular-nums` class on any element containing aligned numbers.

### Type Scale

Use the Tailwind fixed scale. Do NOT use fluid `clamp()` sizing -- data-dense
dashboards need spatial predictability, not viewport-responsive text.

| Role | Tailwind | Use |
|------|----------|-----|
| Control labels | `text-xs` (12px) | Dropdown/toggle labels in control bars |
| Table headers | `text-xs` or `text-[10px]` | Column headers (with `uppercase tracking-wider`) |
| Body / data values | `text-sm` (14px) | Table cell values, descriptions |
| Panel titles | via `PanelHeader` | Never hand-roll panel title styles |
| Section headers | `text-sm font-semibold` | Sub-sections within panels |

### Hierarchy Through Multiple Dimensions

Do not rely on size alone. Combine 2-3 of:
- **Size** (3:1 ratio between heading and body)
- **Weight** (bold vs regular)
- **Opacity** (`text-white` vs `text-white/50`)
- **Tracking** (`tracking-wider` for labels, normal for values)
- **Position** (top/left = primary)

### Line Height on Dark Backgrounds

Light text on dark backgrounds looks lighter than the same weight on light backgrounds.
If readability feels thin, increase `leading` by 0.05-0.1 over what you would use on
a light background.

---

## 3. Color Rules (Dark Mode Portal)

### Tinted Neutrals

Our `white/50`, `white/60` opacity approach is correct for dark mode. Pure gray
(`#808080`) looks dead on colored backgrounds -- always use white with opacity.

### The 60-30-10 Rule

- **60%** = Dark surfaces (`--bg-page`, `--bg-card`, `--bg-header`)
- **30%** = Text, borders, inactive states (`text-white/50` through `text-white/80`)
- **10%** = Accent (`--primary`, `--success`, `--danger`)

Accent colors work because they are rare. If everything is indigo, nothing is.

### Never

- Pure black `#000` for large surfaces (use `--bg-page`)
- Pure white `#fff` for text (use `text-white` which is themed)
- Gray text on colored backgrounds (use a shade of the background or white with opacity)
- Gradient text for metrics or headings
- Hardcoded hex values -- always use CSS variables or Tailwind semantic tokens

### Semantic Color Assignments

| Positive | Negative | Neutral / Zero | Inactive |
|----------|----------|----------------|----------|
| `text-[hsl(var(--success))]` | `text-[hsl(var(--danger))]` | `text-white/40` | `text-white/30` |

Zero-parity values (`abs(value) < 0.005`) display gray, not red.

---

## 4. Spatial Design

### Spacing System

Use the Tailwind 4px base grid: `1` (4px), `2` (8px), `3` (12px), `4` (16px),
`6` (24px), `8` (32px). Name by relationship (`gap-3`), not value.

Use `gap` instead of margins for sibling spacing -- eliminates margin collapse.

### Visual Rhythm

Do NOT use identical spacing everywhere. Create rhythm:
- Tight groupings within related controls (gap-2)
- Generous separation between control groups (gap-4 or gap-6)
- Dividers (`<div className="w-px h-5 bg-white/10" />`) between logical groups

### Cards Are Not Always Required

Spacing and alignment create visual grouping naturally. Use Panel primitives
when content is truly distinct. Never nest panels inside panels -- use spacing,
typography, and subtle dividers for hierarchy within a panel.

### Optical Adjustments

- Text at `margin-left: 0` can look indented due to letterform whitespace
- Geometrically centered icons often look off-center visually
- Play icons shift right, arrows shift toward their direction
- Touch targets need 44px minimum even if visual element is smaller

---

## 5. Interaction States

Every interactive element needs these states designed:

| State | Visual Treatment |
|-------|------------------|
| Default | Base styling |
| Hover | Subtle color shift (`hover:bg-white/10`) |
| Focus | Visible ring (`:focus-visible` only, not `:focus`) |
| Active | Pressed-in, darker |
| Disabled | Reduced opacity, `cursor-not-allowed` |
| Loading | Spinner or skeleton |

### Focus Rings

Never `outline: none` without replacement. Use `:focus-visible` to show focus
only for keyboard users:

```css
button:focus-visible {
  outline: 2px solid hsl(var(--primary));
  outline-offset: 2px;
}
```

Our standard Tailwind: `focus:outline-none focus:ring-2 focus:ring-[hsl(var(--primary))]`

---

## 6. Pre-Commit QA Checklist

Run through this before committing any visual changes. If any item fails, fix it
before committing.

### Labels & Text
- [ ] All control bar labels use canonical pattern (`text-xs text-white/50 tracking-wider` + colon)
- [ ] Consistent capitalization (Title Case for labels, UPPERCASE only for table column headers)
- [ ] No orphaned parentheticals in column headers (prefer clean names; keep only essential units like `(Bn)`)
- [ ] Numeric columns use `tabular-nums` or `font-variant-numeric: tabular-nums`

### Color & Tokens
- [ ] No hardcoded hex colors -- all use CSS variables or design tokens
- [ ] Zero-parity values render gray (`text-white/40`), not red
- [ ] Positive/negative values use `--success` / `--danger` tokens
- [ ] No pure gray on colored backgrounds

### Panels & Layout
- [ ] Using Panel primitives (`<Panel>`, `<PanelHeader>`, `<PanelContent>`)
- [ ] Correct panel variant selected (chart / nested / mixed / heatmap)
- [ ] PanelHeader follows LEFT (Title > Help > Timestamp) | RIGHT (Actions) pattern
- [ ] Spacing uses Tailwind scale values, not arbitrary `px` values

### Interactions
- [ ] All interactive elements have hover states
- [ ] Focus indicators present (`:focus-visible`)
- [ ] Disabled states visually distinct
- [ ] Loading states for async operations
- [ ] Touch targets >= 44px

### Consistency
- [ ] New pattern matches existing equivalent elsewhere in portal
- [ ] No `text-sm` where `text-xs` is the established pattern (or vice versa)
- [ ] No new opacity values where established ones exist (`/50` for labels, `/60` for secondary text)
- [ ] Chart library usage matches page convention (Recharts vs ApexCharts)

---

## 7. Normalization Protocol

When issued a task order to normalize or audit a page:

1. **Scan control labels** -- grep for `text-xs.*text-white` and `text-sm.*text-white` in your page directory. Flag any that deviate from the canonical pattern.

2. **Scan color usage** -- grep for hardcoded hex (`#[0-9a-fA-F]`), Tailwind direct colors (`bg-blue-`, `text-red-`), and non-standard opacities.

3. **Scan spacing** -- look for arbitrary values (`p-[13px]`, `gap-[7px]`) that should use the scale.

4. **Scan panel structure** -- verify all panels use `<Panel variant=...>` and `<PanelHeader>`. Flag any custom `div` containers that should use the primitives.

5. **Cross-reference** -- compare your page's patterns to the reference implementations:
   - `portal/src/pages/Positioning/` (complex nested layouts)
   - `portal/src/pages/MarketPerformance/` (clean page structure)
   - `portal/src/pages/FactorTilts/` (multiple control bars with canonical labels)

6. **Fix** -- apply corrections. Do not summarize what needs fixing. Open the file, change the value, save it.

---

## Attribution

Sections 2-5 adapted from [Impeccable](https://impeccable.style) by Paul Bakaus.
Licensed under Apache 2.0. See NOTICE.md in source distribution for full attribution.
Section 1 and 6-7 are Opal-specific standards established by CTO audit 2026-04-07.
