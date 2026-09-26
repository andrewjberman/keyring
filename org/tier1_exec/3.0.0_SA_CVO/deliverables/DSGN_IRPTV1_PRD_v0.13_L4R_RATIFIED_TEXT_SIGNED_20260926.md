# L4-R review -- DSGN_IRPTV1 PRD v0.13, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`6ce514ca80` (v0.13). **Half:** ratified-text,
`half_hash` `ca5635125a23`, ENDPOINT hash `d465c3306197`, re-measured with `prd_signoff_lib` at the pin and matching
delivery 101501. **Prior:** SIGNED at v0.11 @`d4b01fd615`. v0.12 was brief-half only.

**Verdict: SIGN.** Section-slice diff of v0.11 against v0.13: the ENDPOINT adds FWD-21, FWD-22 and FWD-23, and
nothing else in it moves. FWD-1 to FWD-20 are byte-unchanged, and CONTRACTS is byte-equal.

## The three outcomes against their ratified pin

The pin is the UI review brief `docs/briefs/irpt-ui-review-brief-20260926.md` @`fd463341e3` (Andrew-direct
2026-09-26):
- **FWD-21 carries O6**: "Every holdings view shows every account of the client" (UIR-39). The ACCEPT names the four
  views and the two-account case.
- **FWD-22 carries O9**: "each security once with its total, every tile legible, filters grouped by account"
  (UIR-41, 42, 43). The per-model split one click away is UIR-43's wording in the PRD's findings table.
- **FWD-23 carries O10**: "as of the last trading day, and model amounts are the positions actually held" (UIR-23,
  UIR-48). The ACCEPT's "or is plainly labelled as a target" is the PRD's own UIR-48 routing: until the backend states
  how model amounts are formed, no view presents them as held.

Each DONE WHEN is an EXERCISED act a seat can take on a real client.

**Coherence.**
- FWD-21 and FWD-14 agree: every account is included, and the pie stops at models.
- FWD-22 and FWD-14 agree: the map at rest shows totals, and a model's securities are drilled on it.
- FWD-23 needs no contract change beyond the "Not promised" list. The T-1 date is the producer's scheduled
  publication, and the target label is the page's own words.

**Hygiene.** The ENDPOINT section holds 0 seat serials (regex census). Ids run FWD-1 to FWD-23 with no gap, and the
header `endpoint_outcomes` matches.

## Observations (not blocking; for the next ENDPOINT bump)

- **O1 -- two meanings of "other" on the securities map.** FWD-22 groups small holdings into "one labelled 'other'
  tile". "other" is also a served asset class: the HoldingsSnapshot wire enum admits `'other'`, and IV-e-27 renders
  the IR 'Other' class. An advisor cannot tell the two apart. A distinct label for the group, such as "smaller
  holdings", removes the collision.
- **O2 -- FWD-21's "never one".** "A client with two accounts shows two, never one" is absolute. FWD-2 and FWD-19 let
  the advisor narrow a view to one account on purpose. The ACCEPT's "silently" carries the intent, and the DONE WHEN
  reads the client view. "unless the advisor narrowed it" would make the grade unambiguous.
- **O3 -- FWD-23 rests on IRPT_BCKEND (~M).** UIR-23 is met by ~M's scheduled T-1 publication, and UIR-48 by ~M's
  statement of how model amounts are formed. This is stated in the PRD's findings table, in the same shape as FWD-1's
  dependence on the served `spread`. The close grades read ~M's delivery, not only this project's cells.

-- `3.0.0_SA_CVO`, 2026-09-26 ~21:3xZ
