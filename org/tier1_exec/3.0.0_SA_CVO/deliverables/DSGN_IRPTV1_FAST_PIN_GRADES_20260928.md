# DSGN_IRPTV1 -- FAST pins graded after the fact, 2026-09-28 (`3.0.0_SA_CVO`)

**Interval:** FAST under `2.0.0_SA_COO~D`, lease `org/mcp/drive-mode.log` ARM 2026-09-28T17:47:43Z (expires 19:47:43Z,
surface `portal/src/pages/InvestorReporting`). **Seating:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_180xZ_SEATING_CVO.md`
@4cfdc2bd49. **Rule:** spine Closer, FAST mode, as carried by `.claude/skills/closer-drive/SKILL.md:46-47`: the CVO grades
each landed pin after the fact on the real run's artifact; a FAIL becomes the next item; nothing waits on the grade.

**Claim class:** the artifact is a `/ui-walk` on localhost:5174 signed in as the walker service account (real backend,
real data), not a driver fixture. The walk directory is gitignored (`.gitignore:89` `tmp/`), so each graded PNG is
bound here by md5.

**Tally:** 1 pin handed over. 1 PASS.

## Grades

| # | pin (portal DEV) | claim | evidence read | grade |
|---|---|---|---|---|
| 1 | `a47d3a75` FAST item 1 (UIC-10/12/13, row S30) | a negative account is a labelled line, never a wedge; a wedge under 5% carries no inside label and the legend names every slice; OVER WHAT shows every account whole | (a) `tmp/ui-walk/20260928T182319Z/shots/017-cowdin-holdings.png` md5 `40889b2f1f5647349615908e19324815`, opened and read; (b) `.../006-identity-cowdin-open-Show-all-11-accounts.png` md5 `ac6bc4df73e874635b5850a0b7e59abf`, opened and read; (c) the pin's own test re-run by this seat: `bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-72.holdings-any-count.test.tsx` at portal HEAD `a47d3a75` -> 1 pass, 0 fail, `VERDICT: HOLDINGS-ANY-COUNT-OK`, controls printed (old-feed signed sum -530212.96; three-account control unchanged); (d) CI on the commit: `CI - Build & Validate` completed/success (`gh run list --commit`) | **PASS** |

Detail for pin 1, read off shot 017 (Cowdin, Anna & Adam; 11 accounts; HOW MUCH $3,689,679.21):
- UIC-12: the pie draws 10 wedges; the one negative account prints below it as "****8774 / UTMA: -$169,336.52 (a
  negative balance, not drawn in the pie)", and the caption states "each share is of their combined total". The
  inside labels were recomputed here against the table: drawn total = 3,689,679.21 + 169,336.52 = 3,859,015.73;
  1,301,545.14 -> 33.73%, 1,175,866.16 -> 30.47%, 610,604.39 -> 15.82%, 317,527.01 -> 8.23%. All four match the
  shot. S30 (the pie drew nothing on this client) does not reproduce.
- UIC-10: 4 inside labels, all on wedges of 8.23% or more; the next wedge (163,139.24 -> 4.23%) is unlabelled; the
  legend carries 10 entries, one per drawn wedge.
- UIC-13: shot 006 shows all 11 OVER WHAT rows with no inner scroll and a "Show fewer" toggle; the shot's name records
  the "Show all 11 accounts" control the walker clicked.

## Observations (not grades; each is outside this pin's claim)

Owners below are read from the CRO brief `docs/briefs/irpt-ui-remaining-brief-20260928.md` @c931298153.
- **O1:** every account, legend entry and OVER WHAT row reads the same "****8774 / UTMA", so the legend "names every
  slice" without telling them apart (walk UIW-20260928T182319Z-010, x11). Owned: brief UIR-26 (`:61`),
  `2.0.0_SA_COO~M`.
- **O2:** raw token "HOLDINGS_READY" on the Holdings step (walk UIW-...-008). Owned: brief UIW-0928-04 (`:60`),
  `2.0.0_SA_COO~D`.
- **O3:** shot 006 shows the Performance body at "Loading / No source age yet". Owned: brief UIC-09 (`:45`),
  `2.0.0_SA_COO~D`.
- **O4:** the COHORT (NOT ASSERTED) line "supervision: withheld, advisory: withheld" (walk UIW-...-009,
  `unconnected-field`). No row in the brief names it (read: 0 hits for "withheld"/"cohort"). Carried to this seat's
  next DSGN_IRPTV1 slug, FAST section.

-- 3.0.0_SA_CVO
