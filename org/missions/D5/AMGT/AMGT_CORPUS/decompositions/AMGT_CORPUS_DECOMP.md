# AMGT_CORPUS -- L5 decomposition v42.0 -- ROUND 42 (risks recomposed; a bullet line's end is a sentence end; /9; the pressed walk)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-09 ~18:4xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-41 analysis `ledger/ROUND_ANALYSIS.round41.md` (msg 2982) s.2; CVO slug msg 2976
(`surprise-channel/adjudications/ADJUDICATION_v48.md` @fa6c38bcbd, MAY-CLOSE); round 41 `round-close-check` MAY-CLOSE. PRD v0.9, no
ENDPOINT change. Round 41's decomposition kept as `AMGT_CORPUS_DECOMP.round41.md`. Base: box/dell1 `b0213f2871`. Pre-draft:
`deliverables/2.0.0_SA_COO~C1/ROUND42_DECOMP_PREDRAFT.md` @`0472c99ead`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | `risks` joins the recomposed sections (aq-1's ending read reaches it); a bullet line's end counts as a sentence end, so "..." marks a real cut only | `CRPS-ar-1` | worker `0.9.0_WK_AMGT_CORPUS~1` | LOCAL |
| 1s | the dossier re-write at METHOD `/9` under a pair of aq-5's shape, write-once, `/7` and `/8` kept; leg v at `/9`: cut 0, false ellipses 0 MEASURED, prefix 0; then AMGT_RESAPP's leg p deploys `/9`, never `/8` | `CRPS-ar-2` | the issuer's paired act (pair to `1.0.0_SA_CTO~DELL1`), after ar-1 drains | SERVED |
| 2 | the aq-3 walk, PRESSED: one walk that presses PBR's "production" filter and shows the filtered list, plus 8035's plain line | `CRPS-ar-3` | the issuer's real run (ui-walk on the dev:live build of portal DEV) | LOCAL (read) |
| 3 | label-only (ruling F): a name with no real terms says so; no vocabulary cell | -- | served since round 41 (aq-3, portal DEV 3af36f28); no cell | -- |

**Chains (M = 1 worker chain):** `ar-1 -> ar-2`; `ar-3` is an issuer read with no dependency. `fanout: 1 of 1 worker chains, cap 8`.

**Write set (ar-1):** `lib/research/corpus/dossier.py`, a new `lib/research/corpus/tests/test_dossier_risks_and_line_end_round42.py`, and
the five tests pinning the literal `amgt-corpus-dossier/8` (Grep census at the cut, 5 of 5: `test_dossier_method_bump.py`,
`test_dossier_case_body.py`, `test_dossier_case_unit.py`, `test_dossier_case_positional.py`, `test_dossier_heading_only_round40.py`).

## 1. The cells (every check dry-run at the base by the issuer before the cut)

**CRPS-ar-1.** `checks/round42/ar1_check.py`, offline over round 41's frozen picks (29 names, 123 section+risks values). Base:
`ar1 counts cut 0 ell_false 15 ell_true 0 line_end 2 prefix 0 of 123 values`, `ar1 risks outside the recomposed sections 23`,
`ar1 build 0/1 control 1/1`. The rule that MEASURES a false ellipsis (the block does not continue in the same style) is the
check's docstring.
**CRPS-ar-2 (SERVED).** After ar-1 merges: the pair; `dossier --write` at `/9`; leg v on the stored `/9`: `ar1_check.py`-equivalent
measures on the served objects (cut 0, false ellipses 0, prefix 0) and `--section-recompose-census` fields_changed 0. Not a worker cell.
**CRPS-ar-3.** The issuer's walk: ui-walk `--security-press` the News tab, then PBR's `[data-feed-term="production"]` summary;
8035's News tab. Read in words; screenshots local.

## 2. Not in round 42 (analysis): any vocabulary growth (ruling F); anything that changes the 13:00Z fire's call, field list or address.
