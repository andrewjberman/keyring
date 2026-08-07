# C3.ii — THE DECLARED×APPLIED JOIN, THE CONTROL PAIR, AND THE CANDIDATE CELL

**Author:** `4.0.0_SA_CRO` (build owner) · **TO:** `NFRA_VERTHARVEST.C3II.declared-plane-join`
@e0a8ef9ec7, amended @27051853cc · **Grounding:** `C3II_MACRO_REGISTRY_GROUNDING` v2 @251605d939
**Measurement vintage: 2026-08-07T165622Z** · **Zero production code. Nothing auto-named.**

> **INHERIT is ruled** (Andrew-direct ~1645Z: *"All your recs are approved, proceed"*). This takes
> `1.0.0_SA_CTO~C`'s `NFRA_VERTHARVEST_SPEC_20260807` forward and adds the declared plane. No second
> spec was authored or commissioned.

---

## 1 — THE 2×2, WITH ITS DENOMINATORS

**`denominator_grain`: MACRO CODES (registry rows).** Not projects, not resources.

| | **APPLIED** | **NOT-APPLIED** | **NOT-MEASURED** |
|---|---|---|---|
| **DECLARED** | **26** of 35 | **9** of 35 | **0** of 35 |
| **NOT DECLARED** | ⭐ **187** unmatched resources of **400** measured — **the product** | invisible by construction — a boundary, not a defect | — |

**`codes_planned` = 35** (known before any measurement fired) · `codes_measured` = 35 ·
`codes_failed[]` = **empty** · `codes_empty[]` = the 9 below.

**Applied plane, per limb, each with its own positive control:** `portal_pages` 17 · `data_trees` 17
· `lambdas` **197** · `eventbridge_rules` **139** · `s3_buckets` **30** = **400 resources**.

> **⚠ 35, not "~30".** The grounding estimated ~30 rows from a file read; the parsed count is **35**.
> That is the denominator this whole artifact rests on, so it is measured, not carried.

**DECLARED × NOT-APPLIED (9):** `ADHC` `BDPL` `CDRS` `CENG` `OPAL` `SHIF` `SXPL` `YALP` `YANG`

---

## 2 — THE CONTROL PAIR: **PASS**, and it passes for the *right* reason

| limb | code | expected | observed | |
|---|---|---|---|---|
| **negative** | `CENG` | MEASURED-EMPTY / kind=**RETIRED** / not matcher-limited | MEASURED-EMPTY / RETIRED / False | **PASS** |
| **positive** | `ADVI` | APPLIED, **same pass** | APPLIED (n=9) | **PASS** |

**The pair was asserted, not the single.** An absence oracle passes for many reasons; a position
oracle fails for one. The negative limb alone is satisfied *most cleanly* by a completely dead
measurement — only the positive limb, from the same pass, separates "correctly absent" from "nothing
was measured."

**Ground-truthed independently of my own matcher, with a positive control on the same pipes:**
`causality|ceng` → **0** lambdas, **0** rules, **0** buckets; `advisor` → **3** lambdas. So the zero
is a real zero, not a dead pipe. **The spec's premise holds and causality is genuinely unbuilt.**

**And the negative limb checks that it is not passing by accident:** `CENG` retains the live keys
`causality`/`ceng`/`engine` after ambiguity filtering, so its emptiness is an estate fact. A code
left with no usable key would be *matcher-limited*, and the limb rejects that case explicitly —
otherwise the control would pass because the code cannot be matched rather than because the estate
is empty, which is the same wrong-reason pass one level in.

---

## 3 — CRITERION 2a: the NOT-APPLIED cell splits

| kind | n | codes | basis |
|---|---:|---|---|
| **RETIRED** | 1 | `CENG` | naming act cited (Andrew 2026-08-05) + independently ground-truthed here |
| **ASPIRATIONAL** | 0 | — | derived from `TBD` markers; **none of the 9 carry one** |
| **UNCLASSIFIED** | 8 | `ADHC` `BDPL` `CDRS` `OPAL` `SHIF` `SXPL` `YALP` `YANG` | no naming act cited, no TBD marker — **named, never guessed into a class** |

**RETIRED is not inferred from an empty applied plane.** Doing so would make the control circular —
the thing being tested would define its own expected value. It requires a cited naming act, so it is
an explicit list; ASPIRATIONAL is derived from the declared plane's own `TBD` markers.

> **A finding the split produces, and it is the reason the split exists:** `TAXX` and `SSCN` are the
> registry's two `TBD` rows — declared ahead of build — and **both read APPLIED**. The estate has
> overtaken its own declaration. That is the registry being *authoritative-but-lagging*, visible only
> because retired and aspirational were not pooled.

---

## 4 — THE PRODUCT: the NOT-DECLARED × APPLIED candidate cell

**187 unmatched applied resources of 400 measured.** Top clusters (token → resources):

| n | token | | n | token |
|---:|---|---|---:|---|
| 23 | `yang` | | 6 | `runner` |
| 19 | `trigger` | | 6 | `generator` |
| 10 | `assets` | | 5 | `analysis` |
| 10 | `portfolio` | | 5 | `find` |
| 9 | `session` | | 5 | `seeking` / `alpha` |
| 8 | `generate` | | 5 | `globgrph` |
| 7 | `silver` | | 5 | `ycharts` |
| 6 | `smartx` | | 4 | `publisher` / `guard` / `ingest` |

**⚠ 187 IS AN UPPER BOUND, AND THE INFLATION IS NAMED.** Five declared codes — `ADHC` `BDPL` `SHIF`
`SXPL` `YALP` — are **matcher-limited**: after ambiguity filtering they retain no key beyond their
own 4-character code, which effectively never appears inside a resource name. **A key that exists
and can never fire is not a key.** Their live resources are therefore sitting in this pile: the
`bd-49f-*` and `bd-allocation-*` families belong to `BDPL`, the `yang*` cluster to `YALP`. So the
true undeclared population is **smaller than 187**, and the candidate list is a starting set for
Stage 2/3, not a finished answer.

**Nothing here is named, proposed-as-ratified, or admitted.** Naming is sovereign; this surfaces
candidates only, and the registry is a record of naming acts already performed.

---

## 5 — RULE-24 VERDICT ON THE REGISTRY AXIS (a finding, **not** a gate)

The candidate list ships regardless of this. The axis is Andrew's; `MACRO_CODES.md` was **read-only**
throughout — editing it mid-harvest would move the declared plane under my own measurement.

- **(i) MECE — fails, and more precisely than "arguably".** `ADHC` is defined as *"Ad-hoc (no
  permanent surface area)"* on a file defining macro codes **as** permanent surface areas. A residual
  bucket makes collective-exhaustiveness true **by construction**, so the CE limb still technically
  holds and carries **zero information**. It is not that MECE fails — **a residual bucket makes MECE
  unfalsifiable**, which is worse than failing it. Anything landing in `ADHC` is by construction a
  vertical the axis could not express.
- **(ii) SAME GRAIN — fails.** `POSN` (one portal page) · `OPAL` (an umbrella whose own row lists six
  projects) · `NFRA` (*"a MACRO, not a project key"*) · `ADHC` (an explicit non-surface) on one axis.
- **(iii) INTENT COHERENCE — holds** on the registry itself. *(It failed on the grounding's own 2×2,
  which pooled RETIRED with ASPIRATIONAL — now split, §3.)*
- **(iv) STATE COHERENCE — FAILS, and postulate (iv) requires naming which values do not move
  together.** *(Not run in the grounding; this is the addition.)* The state axis is
  *modelled / unmodelled by the taxonomy*, and one remedy does **not** move every value:
  - `POSN` + page-grain siblings → fixed by **RE-GRAINING** (promote to surface-area grain).
  - `OPAL` / `NFRA` umbrellas → fixed by a **LEVEL SPLIT**; the macro-vs-project two-level system
    already exists and these rows are the level boundary leaking onto the value axis.
  - `ADHC` → fixed by **NEITHER**. A residual bucket is not a mis-grained member; it is the *absence*
    of a member, dissolved only by modelling what is inside it — **unbounded work of a different
    kind**.
  **So "fix the macro registry axis" presents as one workstream and is three, and the third has no
  determinate size.** That is exactly what postulate (iv) exists to surface.
- **Conformance lag, self-recorded:** the `OPAL` row was added 2026-07-14 *"closing a lag"* against
  the file's own rule 6 (*added here before use*). Treat as **authoritative-but-lagging** — which is
  precisely why it joins to the applied plane rather than replacing it.

---

## 6 — THREE DEFECTS IN MY OWN INSTRUMENT, ALL FOUND MID-RUN

Recorded because each shipped a *clean-looking* result, and one of them **passed my own control**.

1. **`shell=True` → a page count wearing a total's clothes.** The shell did not strip the quotes
   around the JMESPath expression, so `aws` read `'Functions[].FunctionName'` as a **raw string
   literal** and returned that constant — printed **once per page**. Three limbs reported
   `status: measured` with **n = 4 / 2 / 1** against true populations of **197 / 139 / 30**. Every
   layer was silent and `rc=0`. Fixed by argv lists (no shell in the path) **plus a per-limb positive
   control** — a limb that cannot see a member known to exist is `FAILED`, not empty.
   > **AND MY CODE-LEVEL CONTROL PAIR PASSED THROUGH THIS.** `ADVI` was satisfied by a healthy
   > *local* limb while three *remote* limbs were dead. **A control at the wrong granularity reports
   > the health of whichever limb happens to be alive.** The pair is now asserted per-limb as well.
2. **Partial measurement reported as complete.** With three limbs dead, 16 codes still read
   `MEASURED-EMPTY` — including `CENG`, so the negative control passed on missing data. Fixed:
   **positive evidence stands alone; absence is only meaningful under complete measurement.** If any
   limb fails, no-evidence codes are `NOT-MEASURED`, never `MEASURED-EMPTY`.
3. **Token bleed across codes.** `CENG` declares `pipeline = "causality, news-pipeline"` and so
   inherited `news` — **NPPL's own surface** — matching all 34 `news-*` resources byte-identically to
   NPPL and failing the negative control. Fixed by the registry's own structure:
   **surface area is IDENTITY, pipeline is only USAGE** (rule 4 explicitly lets two surfaces share
   one pipeline), so a strong key outranks a weak one and a token claimed by two codes strongly is
   dropped from both. 13 ambiguous tokens dropped.
   *A fourth, smaller one: resource names were lowercased without camel-splitting, so declared
   CamelCase portal pages (`AdvisorIntelligence`) landed in the undeclared pile.*

**Every one of these is the same shape as the two figures that moved in this program today** (a 5.5×
marker-set swing and a 3.6× resolver swing): **a number whose frame was not printed beside it.**

---

## 7 — BOUNDARY DECLARATION (ratified four-part form)

- **`address_space`** — 35 declared codes × 400 applied resources across 5 limbs, each limb's count
  materialised client-side (the CLI auto-paginates; **no `--no-paginate` anywhere**).
- **`traversal_residue`** — the matcher is **INFERRED** except the `declared_portal_dir` limb, which
  uses a key the registry itself declares and carries no inference. **5 matcher-limited codes**
  (enumerated, not estimated). Applied plane does not include IAM roles, DynamoDB tables, CloudFront
  distributions, Step Functions, or portal `json/*` prefixes — **so the applied plane is larger than
  400 and the candidate cell is correspondingly incomplete.**
- **`presentation_residue`** — none. All 35 per-code records, all 187 unmatched names, and the full
  ambiguous-token list are in `c3ii/join.json`.
- **`failure_direction`** — where wrong, this **over-reports the candidate cell** (matcher-limited
  codes' resources appear undeclared) and **under-reports DECLARED × APPLIED**. It does *not* fabricate
  applied evidence: positive matches are name-grounded.
- **`known_negative`** — `CENG` was APPLIED under the pre-fix matcher and is MEASURED-EMPTY now.
  Stated so the control's PASS is not read as having been true all along.

---

## 8 — HONEST RESIDUE

- **The matcher is an inference and its precision is unmeasured.** I hand-checked the control codes
  and the CENG/NPPL bleed; I did **not** hand-audit all 400 match decisions the way TO-0's
  denominator was audited. A sampled precision measurement is the obvious next control.
- **`TAXX` reading APPLIED may be over-match** on the generic token `tax`; it is plausible (TAXSMA
  work is live) but not verified per-resource.
- **5 matcher-limited codes need a declared join key**, not a better guesser. The cheapest fix is a
  registry column naming each surface's resource prefix — **which is Andrew's file and his act**, so
  it is proposed here and not performed.
- **The cell sizes are now measured** where the grounding said they were unmeasured by construction —
  but only over the five limbs named above.

## APPENDIX — artifacts

| file | what |
|---|---|
| `scripts/c3ii_declared_plane_join.py` | parser + join + control pair; **self-test 19/19** incl. regressions for every defect in §6 |
| `deliverables/c3ii/join.json` | full per-code records, the 2×2, the control result, all 187 unmatched names |

```bash
python org/tier1_exec/4.0.0_SA_CRO/scripts/c3ii_declared_plane_join.py --self-test
python org/tier1_exec/4.0.0_SA_CRO/scripts/c3ii_declared_plane_join.py \
    --workspace . --out org/tier1_exec/4.0.0_SA_CRO/deliverables/c3ii/join.json
# exit 0 = control pair PASSED; exit 2 = FAILED, do not ship on the join
```
