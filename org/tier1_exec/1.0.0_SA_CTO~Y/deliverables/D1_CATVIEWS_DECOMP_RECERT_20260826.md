# D1_CATVIEWS decomp re-certification — independent re-derivation (post-invalidation signer)

**Signer:** `1.0.0_SA_CTO~Y` — the independence break: not the decomp author (`2.0.0_SA_COO`), not a prior
certifier (`3.0.0_SA_CVO` v1/v2, base `1.0.0_SA_CTO` v2.1). Commissioned by base CTO 73643 + 73654 on
CVO 73629 limb 2 (ratified 73633).
**Object:** `workflows/atom_decomposition/runs/d1-catviews/20260824T195537Z/DECOMP.md` @`ce04a311eb`
(31 cells claimed, s.4; working tree clean at read; only two runs exist under `runs/d1-catviews/` — no v3).
**Date:** 2026-08-26 ~21:1xZ. **Repo HEAD at read:** `78bd1fe6ef`.
**Method:** per the brief — artifacts pulled at my own hand from `org/projects/D1_CATVIEWS.json`; the
DECLARED DOMAIN read from the stage-2 PRD; the enumeration RE-DERIVED over that domain by tracing the
live estate (registry → projection → serving → portal → path-to-live), NOT from the prior cert's cell
partition. The prior certs are cited as findings only; no boundary inherited.

---

## 1. The declared domain, as read

Stage-2 PRD `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` @`5d356cc426`, s.8.1 (purpose) + s.8.3
(territory (a)–(g)) + s.8.6 (surface (h), the view tree) **+ s.8.6a (2026-08-25 ~04:2xZ, Andrew-direct:
the Client L1 VALUES SUPERSEDED — `Client - Opal Supervised` / `Client - Opal Unsupervised`, the OPAL
definition: residual account value of accounts holding Opal models — with its own Rule-24 record)** +
s.8.6b (presence vs drill). Domain: *everything that must be true for the ruled taxonomy + view tree to
be served end to end, every per-firm producer resolving membership through the ONE registry.*

⛔ **The vintage asymmetry that decides this cert:** DECOMP last moved 08-25 00:40Z (`ce04a311eb`).
s.8.6a's sovereign word is 08-25 ~04:2xZ. The ALL_SCOPE ruling (CTO 68692/69348) and the
`CLIENT_L1_RULE`/`CLIENT_L1_HELD` implementation landed after that. **The decomp structurally predates
the current domain.** Measured: `grep -c "Opal Supervised" DECOMP.md` = **0**, while
`mdpf_category_registry.py` @`4e791e1e82` carries the new form ×6 and PRD s.8.6a names the PRD itself
as the *previously*-stale surface, code-ahead.

## 2. Instruments (mine, with denominators)

| # | Instrument | Result |
|---|---|---|
| Y1 | `comp-find "category-views.json" --files` | 6 hits / 26,902 files — consumer `portal/src/api/endpoints/aum.ts` + DE proof-of-spec + DE log; no other producer-side namer (the emit derives from the scope map, consolidator) |
| Y2 | `comp-find "category_views" --files` | 65 hits / 26,900 — DEF band = registry + consolidator (the two producers); portal consumer confirmed |
| Y3 | source read, `mdpf_category_registry.py` @`4e791e1e82` | `VIEW_TREE` :76-135 (`Client > Opal Supervised`/`Opal Unsupervised`, path-keyed `DISPLAY_LABEL`), `CLIENT_L1_RULE` :680-684 (49f ALL_SUPERVISED, inf ALL_UNSUPERVISED, cot DERIVED), `CLIENT_L1_HELD` :686-720 (cot held, STOP, remedy MODEL_DETAIL_SCOPE=all → WSE_COTMDL), :722-736 global aggregates-never-computes |
| Y4 | source read, `mdpf_gold_consolidator.py` @`ec106e24eb` | `ARTIFACT_TYPE_SCOPE_SET` :128-164 — `category-views: ALL_SCOPE` (flip @`c6b5ab4efe` in the same commit as first global emission; `assert_scope_set_emitted()`); emit comprehension :1190-1201 iterates the type's own scope set |
| Y5 | source read, `portal/src/api/endpoints/aum.ts` @`d9e875db` (portal repo) | route `/api/general/mdpf/{firmId}/category-views.json` → `platinum/mdpf/*` via deployed CF rewrite confirmed 3/3 sibling types; discriminated-union consumer; COO 66633 withdrawn / CTO 68692 ALL_SCOPE recorded at the consumer site |
| Y6 | source read, `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py` @`af92b0afa3` | pin-assembly via `git show <pin>:<path>` (`pin_bytes` :230-232), refuses symbolic refs; the :266 interlock read IN FULL — disarm condition (a) met ≠ pin advance; NO-SHIP until Andrew's by-name lift; bundled registry copy is pre-defect AND unreferenced, both destroyed by an advance |
| Y7 | `git log` vintages | DECOMP `ce04a311eb`; PRD `5d356cc426`; registry `4e791e1e82`; consolidator `ec106e24eb`; aum.ts `d9e875db`; build_package `af92b0afa3` |

Instrument independence vs prior certs: the v2/v2.1 certs read the decomp against its own I5–I11 and the
TO faces; this pass re-derives from the SERVING CHAIN (Y1–Y6), a different axis of entry, and none of my
reads re-ran a prior cert's command.

## 3. My derived enumeration (summary)

Membership/vocabulary: registry module; view-tree nodes **in the 8.6a form**; the Client-L1 axis
identity question (now THREE bases: 08-19 Advised/Residual, 08-24 fee-taking, 08-25 Opal definition —
the last governs the view); SMA L1 by `strategy_id` (49F-only per the 00:3xZ word); Custom L2 vs
`dim_model_portfolio`; **the per-firm Client-L1 RULE axis (`CLIENT_L1_RULE`)**; **global composition +
derived hold**. Substrate: per-firm account-grain feeds **for the operative basis** (cot = rebalancer
model-detail at `MODEL_DETAIL_SCOPE=all`, the WSE_COTMDL remedy). Projection: the mint (with
`declared_rule`, HELD marker, scope-set derivation, `schema_version`); **the SCOPE axis**; gold
five-peer sum; legacy byte-unchanged; view-plane sum (with the HELD case); Insurance==0 emit guard.
Serving/consumption: platinum emit per scope + CF wildcard route (inside the producer's own emit — no
separate promoter exists to enumerate); portal consumes; empty-block fallback; renderers v1–v4 (8.6a
labels; HELD-with-reason as a distinct render state). Producer resolution: e-1..e-3 **+ the 49F SmartX
crosswalk→registry identity map** (ruled load-bearing by s.2.h.6). Specimen f-1. Boundaries g-1/g-2 **+
the WSE_COTMDL edge + the portal PROD-promote boundary**. Path-to-live: i-1, i-2, inv-5 (verified sound
at source). Acceptance: d-1 **on the Opal basis, behind the STOP**.

## 4. Comparison vs the 31-cell set (Rider 2, first output — sent as 73700/73701/73702)

**A. Members my derivation contains that the cell set does not (postulate-(i) CE gaps):**
- **A1** the Client-L1 RULE axis + HELD semantics (registry :680-736) — no cell governs it; it
  supersedes the basis cells c1–c3 measure.
- **A2** the SCOPE axis + global emission (consolidator :128-164, :1190-1201; registry :722-736) — no
  cell; its four-postulate record exists only as an in-code comment, unadopted by the decomp.
- **A3** the WSE_COTMDL cross-project edge (s.8.6a(iv)'s ONE remedy; held-reason quotes the CTO ruling
  verbatim) — undeclared, against the decomp's own 4a-UU precedent for ADVI_INSURE.
- **A4** portal render path-to-live (DEV → DT-lane PROD promote → CI) — R-i1's declared layer is
  producers only; no cell and no boundary cell covers the renderer's route: the same
  satisfiable-and-true seam class as finding 66916, one plane over.
- **A5** (verify-or-add) the 49F SmartX crosswalk→registry identity map vs e-1/e-2/e-3's enumerated
  map set.

**B. Existing cells whose boundary/content the current domain shifts:** r1 (node vocabulary + a
dead-node oracle), r2 (two-branch rule blind to the governing third basis), c1/c2 (census of a
superseded basis; inf's ruled rule is the OPPOSITE direction of its measured fee flag), c3 (object
moot under the ruled rules), b-1 amendment text, v2/v4 (labels; HELD ≠ unavailable), d-1 (STOP; Opal
basis; the $302.6M miscue is the measured cost of the basis the cell reads on), inv-4 (HELD case
undefined), R-h1 (intent line superseded by 8.6a's own record).

**C. Intact:** inv-1/2/3, a-1, c-2, e-1..e-3 (subject to A5), f-1, g-1/g-2, r3 (+2.h.6), r4 (+4a P1),
p1, p2, v1, v3, and the whole (i) surface (i-1, i-2, inv-5, R-i1).

## 5. Four-postulate assessment (Rule 24) of the decomp @`ce04a311eb`

- **(i) MECE — FAILS on COVERAGE.** Exclusivity: PASS — no two cells claim one surface; the 0.1 table +
  (h)/(i) tables partition cleanly. Collective exhaustiveness over the DECLARED DOMAIN (which includes
  s.8.6a and the post-08-25 rulings): **FAILS — A1–A4 are uncovered members** (A5 pending one
  verification). The CE hunt instrument was the serving-chain trace, able to find cells nobody named —
  and it did.
- **(ii) SAME GRAIN — PASS with a note.** Cells sit at operative-surface grain throughout; the note is
  B3: c1/c2 hold firm-grain answers about a predicate the domain no longer keys the view on — a
  IDENTITY-vintage failure (right cells, superseded referent), recorded under (iv) not (ii).
- **(iii) INTENT COHERENCE — PASS per axis as authored; one record superseded.** No axis mixes intents;
  R-i1 cleanly separates delivery-route from lane and storage. R-h1's *intent line itself*
  ("fee-taking, SOLELY") is superseded by s.8.6a's record — the axis needs re-authoring, not repair.
- **(iv) STATE COHERENCE — FAILS on the (h) Client family.** The family's state axis
  (LIVE/HELD/superseded-basis) has moved: the non-mover is now cottonwood's Opal-exposure substrate
  (WSE_COTMDL remedy, one remedy that moves both 8.6a values — 8.6a(iv)'s own record), while the decomp
  still names 49F's cross-plane join as the non-mover and DARK-is-empty as the membership. A decomp
  whose state axis names the wrong non-mover routes remediation at the wrong project.

## 6. VERDICT

**REFUSAL to certify the whole artifact as it stands @`ce04a311eb`** — postulate (i) COVERAGE and
postulate (iv) on the (h)/Client family fail against the current declared domain. The prior certs are
not impugned: each was true of what it read; the domain moved after the artifact.

**CERTIFIED AS A DELTA: the (i) surface** — `D1-i-1`, `D1-i-2`, `D1-inv-5`, `R-i1`. Mechanism verified
at source at my own hand (Y6): pin-assembly, two physically distinct channels, oracles correctly demand
bytes-at-packaged-vintage (never plan 0-diff, never ancestry — the 22a ephemeral-pin clause). The
invalidation that commissioned this re-cert is fully discharged on its own object. **Rec to the owner:
the (i) TO may cut now** — every A/B item lives on the (h)/Client-L1 family, orthogonal to (i) — with
the NO-SHIP fence on the TO face verbatim (`build_package.py:266` interlock: disarm-condition-met is
NOT a ship decision; pin advances only on Andrew's by-name lift).

**DISCHARGE CONDITION:** COO (owner) lands the absorbing amendment (v3 or in-place) covering A1–A4
(+A5 verified or named a member of e-3), re-scoping B1–B9. This seat re-reads and issues the full cert
same-day; the re-derived enumeration above is the worksheet it will be checked against, not the frame
the amendment must copy.

**Standing constraints honored:** ~X-cohort no-disturb (no ~X seat contacted; nothing here has an
~X-authored subject); the `build_package.py:266` trap met armed — read in full, no pin-advance
inference drawn; no gate manufactured — the refusal binds only this cert's own signature, and the (i)
TO cut is explicitly recommended forward.
