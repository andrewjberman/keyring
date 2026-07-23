# NFRA_PSTMRT s.7 item 1 — firm_registry.json content-parity verification

**Verifier:** `3.0.0_SA_CVO~Z` · **Date:** 2026-07-23 ~00:5xZ · **archetype:** VALIDATE
**Charter:** CTO~Z 20260722T223511Z msg + nudge 20260723T004501Z (Andrew-word); program authority Andrew-direct @`7cc6376e5`.
**Target:** `data/firm_registry.json` @ HEAD `3449c8733` (registry landed @`6b67c241c`, 2026-07-22T18:34-04:00).
**Method:** content parity vs the three sources cited in `_meta.grounding`, each read at the same pinned HEAD. Repo-content parity is verified by reading the repo artifacts at a stated vintage; no live/deployed claim is made here (G2b consumer binding is main-fabric, out of scope).

## Verdict: **DOES NOT FULLY TIE — 2 material findings + 1 citation gap; all other checks PASS**

## Denominators (printed per the postmortem standard)

| Check | Denominator | Result |
|---|---|---|
| Registry rows | 4 firms + 1 pseudo | all checked |
| Source 1 `firm-config.mjs` FIRM_CONFIG (vintage `3e0f224e2`) | 5 entries; 12 field-comparisons (firm_id/display_name/bucket × 4 registry firms) | 11/12 tie; **1 mismatch (F1)**; reverse direction 4/5 entries registered — **1 unregistered (F2)** |
| Source 2 `variance_dimensions.yaml` dimensions.firm | values 3, firm_names 3, alias sets 3 | 9/9 tie (see convention note) |
| Source 3 publisher `PUBLISH_MAP` (13 entries) | firm-position segments under `json/mdpf/` = {global, 49financial, inflection, cottonwood} | exact match: registry enabled mdpf-scope {49financial, inflection, cottonwood} + `global` pseudo; mockadv correctly absent; 0 unregistered |
| FIRM_BUCKET_MAP | derived from FIRM_CONFIG at `firm-config.mjs:70-74` | same content by construction |
| Deliberate nulls (aua_source/model_source/fee_scope/delivery_cadence) | 16 null cells | NOT-YET-BOUND by design (G2b) — confirmed not findings, per charter |
| email_domain | 3 values + 1 null | ties to estate canonical (see F3) but source UNCITED in `_meta.grounding` |

## F1 (MATERIAL) — cottonwood `display_name` contradicts its own cited grounding source

Registry: `"Cottonwood"` (`data/firm_registry.json:55`). Cited source: `firm-config.mjs:51-54` =
**`displayName: 'Cottonwood Capital Advisors'`** — the entry EXISTS, landed @`3e0f224e2`
(FIRMSEP.10, 2026-06-09), **six weeks before the registry was seeded** — not a vintage race.
CTO~Z's stated premise ("no firm-config entry exists for it yet; FE S2c is the source when it
lands") is **false at source**. Corroboration: `docs/architecture/ADVI_PRTORG.md:169` treats
"Cottonwood Capital Advisors" as the name to confirm. **Recommendation:** set the registry
display_name to the grounded value, or record in-file why "Cottonwood" is deliberately preferred
pending FE S2c — an undocumented divergence from the cited SSoT source is exactly the drift class
this registry exists to kill.

## F2 (MATERIAL — the program's own defect class) — `demo` firm unregistered

`FIRM_CONFIG` carries a 5th entry: **`demo`** (bucket `opal-data-demo`, display "Demo Advisory
(demo tenant)", added @ADVI_DEMOV1.001, `firm-config.mjs:42-50`). It is absent from the registry —
neither `firms[]` nor `pseudo[]`. The registry's own law line 1 says **"THIS FILE IS THE ONE FIRM
ENUMERATION"**, and PRD §2.3 rules an unregistered member "as loud as a missing one." As seeded,
the registry under-enumerates against its own cited grounding source — the seed itself exhibits
the postmortem's class (a firm-set structure whose denominator is its own configuration).
**Recommendation:** add a `demo` row (kind `test` or a new `demo` kind; scopes portal-only as
live) or a recorded exemption with authority + expiry (§2.5 shape). Note the schema is
v1-frozen-additive — a row addition is legal; a new `kind` value should get a ~Z gate note.

## F3 (MINOR — citation gap, content ties) — `email_domain` has no cited grounding

`_meta.grounding` cites sources for firm_ids/display, tree_tokens/aliases, and mdpf scope — none
for `email_domain`. The values themselves DO tie to the estate canonical:
`comp-constants.config.yaml:620` FIRM_EMAIL_DOMAINS (firmAccess.ts lane) = 49financial.com /
inflectionwealthmgmt.com / cottonwood.com, and `cottonwood.com` is the live AUTH_COTTON allowlist
domain. **Recommendation:** add the FIRM_EMAIL_DOMAINS citation to `_meta.grounding` so the field
stops being ungrounded-by-citation. (No claim is made here about whether cottonwood.com is the
firm's true corporate domain — that is AUTH_COTTON's settled surface; this check binds the
registry to the estate canonical, which it matches.)

## Convention note (not a finding)

Alias representation differs by convention: the variance catalog includes the canonical id inside
its alias lists (`cot: [cottonwood]`); the registry factors it into `firm_id` and keeps `aliases`
canonical-id-free (`[]`). Set-union under the gate's declared matching (firm_id + tree_token +
aliases) is identical, so no functional gap — but the P2 parity assertion
(`firm_names/firm_aliases parity with the registry`, PRD §3.2) should state this normalization
explicitly or it will false-flag drift on day one.

## RE-VERIFY @`c8751cf23` (2026-07-23 ~01:0xZ) — **CLEAN, s.7-i1 CLOSES FULLY-TIES**

CTO~Z adopted all three findings + the convention note @`c8751cf23` (source-verified before
editing; the F1 premise owned as a stale-vintage read of the 05-08 seed notes). Re-verified
against the same three grounding sources (unchanged since `3449c8733`):

| Check | Denominator | Result |
|---|---|---|
| FIRM_CONFIG field matrix | 15 comparisons (5 firms × firm_id/display/bucket) | **15/15 tie**; reverse 5/5 registered, 0 unregistered |
| F1 | `display_name` cottonwood | == `firm-config.mjs:53` "Cottonwood Capital Advisors" ✔ |
| F2 | demo row vs `firm-config.mjs:42-50` + scope consistency | bucket/display exact; mdpf:false ↔ absent from PUBLISH_MAP ✔; pipeline:false + tree_token null ↔ absent from variance catalog ✔; email_domain null ↔ absent from FIRM_EMAIL_DOMAINS ✔; kind=demo enum law line present (~Z-gated) ✔ |
| F3 | `_meta.grounding.email_domain` | citation present (FIRM_EMAIL_DOMAINS / firmAccess.ts:74 / AUTH_COTTON) ✔ |
| Convention note | PRD §3 item 2 + `_meta.grounding` | `aliases ∪ {firm_id}` normalization stated in both ✔ |
| Diff blast radius | `git diff 3449c8733..HEAD` on registry + PRD | only the adopted changes; no unrelated drift |

**s.7 item 1: PASS.** Items 2–4 remain build-gated.

## Compiler tools used

`comp-glob` (source location, 2 runs) · `comp-grep` (email-domain grounding sweep, 3 runs) ·
`comp-system --check` (LD-0319 load control: SYSTEM CURRENT, 0 drifted) · rail-checked single-file
greps for PUBLISH_MAP + PRD section extraction. Registry/PRD/firm-config read in full via Read.
