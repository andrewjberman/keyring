# CVO DISPOSITION — the `Unreconciled_Aua` contested cell (my s4 exit-bar cell), on ~C's Run-28 finding

**archetype:** VALIDATE + DIAGNOSE
**Cell owner:** 3.0.0_SA_CVO (one cell, one owner — s4 exit bar) · 2026-08-20 ~2215Z
**Input:** 4.0.0_SA_CRO~C atom_layer0 Run 28 (bundle `workflows/atom_layer0/runs/unreconciled_aua/20260820T214623Z/`,
`DECLARED_FRONTIER_EXHAUSTED`, characterize-not-fix), routed via CRO base msg 63901.
**Bound on what I may do:** Andrew-ruled residency (*"rec apprved"*): the cell **STAYS IN-REGISTRY until the
P4/P5 vocabulary unification resolves the contest**; a rename of a served field is NEVER#3 + a DS/AE
instrument act. **So this is a DISPOSITION of the finding + the card brief — not a status flip, not an edit.**

## 1. ~C's characterization — CONFIRMED at source, every leg independently

**"One name, two served computations":** TRUE.
- `INF_D_04.client_portal_summary.py` — `unreconciled_aua = round(float(total_aua) - holdings_total, 2)`
  (repo :899 / deployed :897): a **framing IDENTITY**, ~0.00 by construction. Served on
  `platinum/firm/header_metrics.json` → `total.unreconciled_aua` (live bytes read: **0.0**, data_as_of 08-19).
- `INF_D_02.advisor_client_detail.py` `_book_fee_split` (:1655-1692) — `out['unreconciled_aua'] += _aua` for
  every account with **no billing row**: an **attribution RESIDUAL** that CAN be nonzero. Served on
  `platinum/advisors/{advisor_key}/book.json` → `book.unreconciled_aua` (+ `unreconciled_account_count`).

**The name is RIGHT for D_02 and WRONG for D_04 — agreed.** The D_04 field asserts an attribution gap it does
not measure (attribution completeness lives in `identity_gap`, fail-closed); the D_02 field measures exactly
what the name says. **One rename of the D_04 field resolves both** — the registry entry already scopes itself
to the D_04 sense, so the rename also dissolves the contest at the registry.

## 2. What my own measurement ADDS (read at the served + deployed planes, 2026-08-20 ~2210Z)

**(a) In production today the two quantities are NOT measurably distinct — both serve 0.0.** Across all
5 populated advisor books (`inflection_wealth_management`, `joe_brandenburg`, `noel_soderblom`,
`patrick_scanlan`, `peter_lee`; `unknown` has no `book` block): `book.unreconciled_aua = 0.0` on every one,
while `unreconciled_account_count` = 4 / 1 / 5 / 3 / 22 = **35 unreconciled accounts, all carrying zero
current AUA** (`_aua = adv_df['aua']`, :1678 — zero-balance accounts with no billing row, the ordinary case).
**So the residual is structurally nonzero-capable but empirically 0.0 at this vintage.** A card that says
"D_02 is the live nonzero one" would be wrong today; the honest line is *"D_02 can be nonzero; D_04 cannot."*

**(b) ~C's OPEN READ is CLOSED: deployed-vs-repo for both scripts.** Raw sha differed for both (D_02
116,966 vs 119,508 B; D_04 229,933 vs 225,566 B) — **ALL line-ending artifact** (repo D_02 has 2,542 CRLF
lines, deployed 0; deployed D_04 has 4,466 CRLF, repo 0). CRLF-normalized: **D_02 IDENTICAL (0 changed
lines)**; **D_04 differs by exactly 2 repo-only lines** — a blank + `# DEPLOY-SERVE-HELD: advisor-of-record
daily fold pending arch-gate (live CTO) + NEVER#2 sign-off` — a held-deploy comment, content-neutral to the
computation. **That IS the "2-line offset" (:897 deployed / :899 repo). The 08-12 cert's deployed read
stands; no content delta.** *(Disclosed: my first two sha compares read "NOT IDENTICAL" and I nearly carried
that forward — the CRLF normalization is the control that caught it; same class as the day's other
instrument errors.)*

**(c) The missing `unreconciled_basis` on the served header is DESIGNED, not stale.** Deployed D_04 writes
the basis only into the `_derive_fee_earning_aggregates` dict (:794/:912), consumed at :1324 as `fee_block`;
`build_header_metrics` copies **only `fee_block['unreconciled_aua']`** into the served total (:1349) —
the basis string is never served. Served `header_metrics.json` is *newer* than the deployed code (12:40:08Z
today vs 08-11 code write; the scheduled INF gold run `pipeline-complete.json` 12:43Z) — one producer, one
run, no second writer.

**(d) FE consumer census, both names:** `portal/src` carries **zero** references to `unreconciled_aua` /
`unreconciled_basis` / `unreconciled_account_count` (positive control: `header_metrics` is read by
`advisor-intelligence.ts`, `PartnerAnalytics.tsx`, `ClientsTab.tsx`). **Both fields are served-but-unrendered
today** — the NEVER#3 cost of a rename is bounded to the served keys; no display consumer breaks. (This is a
served-plane + renderer-plane read; a display claim needs no further plane — the renderer census is the
plane for "is it displayed.")

## 3. DISPOSITION (cell owner)

- **The finding is ACCEPTED as input; the cell stays `contested_unresolved` and in-registry** per the Andrew
  residency ruling — nothing flips tonight.
- **The resolution path is the rename of the D_04 served field** (`total.unreconciled_aua` on
  `header_metrics.json`) to a name that says what it computes — a framing-identity check — e.g. the
  registry's own language, `frame_identity_residual` / `holdings_frame_check` (naming is the card's business,
  not mine to pre-empt). D_02's field keeps its name (correct). The registry entry then un-contests by
  tracking the renamed D_04 field OR by re-scoping to D_02 — one act, card-decided.
- **It is a served-key act → NEVER#3 (CTO+COO never-widen sign-off), DS/AE instrument (INF_D_04 is
  0.4.0_DS's script, Rule 13 deploy path), CTO gate on the schema consequence.** P4/P5 vocabulary
  unification is the vehicle the residency ruling already names.
- **I TAKE CRO's OFFER to draft the card for Andrew**, with the facts below required on its face.

## 4. What the card MUST carry (the verify-lens conditions)

1. Both served keys + both computations, cited at the deployed line (D_04 :897; D_02 :1689) — not repo.
2. **"D_02 CAN be nonzero; D_04 CANNOT" — never "D_02 is nonzero"** (today both 0.0; 35 zero-AUA accounts).
3. FE-unrendered on both names (renderer census, positive-controlled) → bounded NEVER#3 cost; still NEVER#3.
4. The deployed-vs-repo open read is CLOSED (CRLF artifact; 2 repo-only comment lines) — the card does not
   inherit ~C's "OPEN READ" caveat.
5. The `unreconciled_basis` absence from served bytes is by construction (never served), not drift.
6. Rename mechanics: DS lane edits INF_D_04 + Rule-13 deploy; served key changes at the next scheduled INF
   run; portal `types.ts HeaderTotal` carries the field name in its type (unrendered but typed) — the DT
   lane's one-line follow; registry v3.x bump re-scopes the entry and lifts `contested_unresolved`.
7. Stability frame (Rule 24 iv): the D_02 field and the registry entry move together under one act; the
   D_04 rename is the single remedy that moves both — stated, so the card is one decision not two.

— 3.0.0_SA_CVO
