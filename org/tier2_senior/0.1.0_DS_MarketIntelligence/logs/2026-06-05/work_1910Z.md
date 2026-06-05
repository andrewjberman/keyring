# Work — FIND_DUALBIZ Playwright escape-valve + depth run (2026-06-05)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE

Andrew-direct: wire the Playwright escape-valve, then run it to see roster depth.

## What shipped

1. **Playwright escape-valve WIRED** (`_util.fetch_browser`, commit cb375a3cc) — headless Edge via
   `channel='msedge'` (system Edge, no browser download); bronze auto-falls-back when curl returns
   non-200 or thin stripped-text (<400 chars). `--no-browser` to disable. Python `playwright` pkg only.
2. **Scorer regex loosened (the bigger win the escape-valve revealed).** The probe showed curl was
   ALREADY capturing disclosures the scorer missed (e.g. Hackmann "offered through Brookstone Wealth
   Advisors, LLC (BWA), a registered investment advisor" — the `(BWA)` parenthetical broke the old
   regex). Loosened `offered_through_ria` to absorb parentheticals + 'SEC-' prefix + 'Member FINRA/SIPC'
   within a 75-char window; still excludes the insurance-only 'products offered through [agency]' line.
3. **Roster depth run** (provider-driven harvest): added Merit Advisors (AE Wealth) + 3 Alphastar
   Wealth regional offices.

## Depth result (15 firms, 9 present)

From 3 providers (Alphastar / AE Wealth / Brookstone) + seeds: **15 firms, 9 present**, 11 independent
producing/integrated targets ranked above the acquired cluster. Top: Paraclete (ins6/sec9), Airlie,
Capital Wealth, Merit, Alphastar-EmeraldCoast. Acquired-megacap (Hackmann/Cornerstone/Brookstone/
RetirementWealth) correctly de-ranked to the bottom band despite some being present.

## The recall ceiling + the next high-yield vector

Plain disclosure-string WebSearch is hitting diminishing returns — results increasingly return the
provider RIA's own pages + **advisor directories** (getwarmer.com/firms/{ria}/advisors,
seniorfinanceadvisor.com, smartadvisormatch.com) rather than fresh producing domains. Those directory
pages ENUMERATE the full IAR/firm roster per provider -> the next high-yield source is **parsing the
directory roster pages** (+ SEC/FINRA IAPD branch lists, Engine B2). That scales to hundreds, not the
ad-hoc dozens. Gradient + RIA Insurance Solutions rosters still un-harvested. FIG = aggregator, no
producing disclosure (null, expected).

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh` (dualbiz .py) | All checks passed |
| `python pipeline.py --deep` | end-to-end; 15 firms / 9 present serving table emitted |
| Playwright Edge launch probe | OK (example.com title fetched headless) |

## Commits this session (my author line)

b1a9aa6d7 brief · 69d3c93a5 rulings+B1 PoC · e3d4337f1 pipeline codified · c31a53ae2 broader-scan ·
285c671e8 provider independence + insurance->security ranking · cb375a3cc Playwright + regex · (this: roster depth)

## Next

- Parse advisor-directory roster pages (getwarmer/seniorfinanceadvisor) + IAPD branch lists = roster depth at scale.
- Harvest Gradient + RIA Insurance Solutions producing rosters.
- (Optional) subpage/disclosure-page fetch to promote Airlie/Refined adjacent->present.
