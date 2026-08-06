# MDPF PLATINUM — CANONICAL SHAPE SPEC (12 files)

**Author:** `1.0.0_SA_CTO~Z` · 2026-08-06 ~2240Z
**Basis:** Andrew-direct at the CTO~Z terminal, 2026-08-06 (per-scope ruling @0caf2e907 + the semantics
clarification recorded verbatim in §1).
**Issued to:** `2.0.0_SA_COO~Z` (decomposition) · `0.4.0_DS_ClientPlatform~Z` (producers) ·
`0.7.0_AE_CloudOps~Z` (publisher/IAM) · `3.0.0_SA_CVO~Z` (verification) · `0.0.0_AB_MSTR~Z`.

> # ⛔ READ §6 FIRST — IT SUPERSEDES PARTS OF §1–§5
> Within 20 minutes of issue, four seats measured against this spec and **falsified three of my claims
> and one of my acceptance criteria.** §6 carries the corrections and they are load-bearing:
> **I-1's mechanism is NOT declarative** · **the 12-vs-14 line is RESOLVED, not open** · **criterion 6
> would have SELF-DESTRUCTED on first run** · **criterion 2's global-only carve-out is struck.**
> *A spec issued to four seats that survives 20 minutes of measurement unchanged has not been measured.*

---

## 0. THE PREMISE — READ THIS BEFORE ANY ROW BELOW

> **Andrew-direct, VERBATIM:** *"We actually are doing this currently, everything I'm describing right now
> is being depicted properly in the Portal PROD environment. **What we are discussing here is simply
> rendering canonically-shaped jsons for platinum, that is all.**"*

**THE BUSINESS LOGIC IS CORRECT AND LIVE. THIS IS A SHAPE PROJECT, NOT A DATA-CORRECTNESS PROJECT.**

⛔ **Therefore: a number that differs from your intuition is NOT a finding.** The semantics in §1 are
ruled, live, and rendering correctly in PROD today. **Do not "fix" them.** The only defects in scope are
**shape** divergences — a field present on one scope and absent on its siblings, or a value the producer
never emits.

*This clause exists because I made exactly that error an hour before writing this: I surfaced Global's
non-model excluding Inflection and Cottonwood (~$409mm) as "a consequence worth seeing," when it is the
ruled, correct, intended semantic. **Treating a correct number as a finding is how a working pipeline
gets "fixed."** — CTO~Z*

---

## 1. THE SEMANTIC INVARIANTS — RULED, LIVE, DO NOT CHANGE

> **Andrew-direct, VERBATIM:** *"on the matter of 'what non-model assets to count' in Global, yes we only
> count non-model assets as the non-model total for the Global aum-metrics and Global
> aggregate-aua-timeseries metrics. We do not count the non-model assets of Inflection or Cottonwood in
> those views. However, we still WANT TO INCLUDE THAT DATA in the Inflection and Cottonwood artifacts,
> regardless of whether Global uses them for its own aggregate. Also, we want to use the total model
> holdings counts (excluding the unfunded is fine) for Global aggregate scope in the account-distribution."*

**I-1 · GLOBAL NON-MODEL IS 49F-ONLY.** In **both** `aum-metrics` and `aggregate-aua-timeseries` at
`global`, the non-model total counts **only** 49 Financial. Inflection's and Cottonwood's non-model are
**not** summed in.

> **THE MECHANISM IS ALREADY DECLARATIVE IN THE ARTIFACT — use it, do not re-derive it.** Global's
> `aum-metrics.meta.fee_basis_components` carries `49financial: fee_scope "full"` vs
> `inflection: fee_scope "model"` and `cottonwood: fee_scope "model"`. **Non-model folds into Global
> exactly for `fee_scope: full` firms.** So I-1 is not a hardcode to preserve — it is a *config-driven
> rule already expressed in the data*, and the canonical builder should read it rather than special-case
> 49F by name. Prior grounding: `dim_mdpf_aggregate_aua_timeseries.py:1826` (Andrew-direct 2026-07-22,
> basis B) + the leg pins at `:1538-1569` that already assert both legs.

**I-2 · EACH FIRM'S OWN ARTIFACT CARRIES ITS OWN NON-MODEL — INDEPENDENT OF I-1.** Inflection's non-model
belongs in Inflection's files; Cottonwood's in Cottonwood's. **I-1 governs what Global folds; it does not
govern what a firm publishes about itself.** These are two different questions and conflating them is the
error this invariant exists to prevent.

**I-3 · GLOBAL `account-distribution` USES TOTAL MODEL HOLDINGS COUNTS across firms**, excluding unfunded.
Measured live and correct: `account_count 7,925` / `active_accounts_count 7,974` / `excluded_unfunded 49`.

---

## 2. THE TARGET — 12 FILES

`s3://opal-data-portal-v2/platinum/mdpf/{scope}/` for `scope ∈ {global, 49financial, inflection, cottonwood}`
× `{aggregate-aua-timeseries, aum-metrics, account-distribution}.json` — **every single day** (@0caf2e907).

> **`aum-metrics` IS ALREADY CANONICALLY SHAPED — USE IT AS THE REFERENCE PATTERN.** Measured: all four
> scopes carry an identical `total` key set (`account_count, aum, model_aum, non_model_aum, q0..q3,
> series_start`) plus `scope`, `period`, `dates`, `by_model`, `meta`, `_provenance`, `last_updated`.
> **Zero shape divergence across scopes.** It is the existence proof that the other two can be uniform,
> and the shape to converge them toward.

---

## 3. MEASURED SHAPE DIVERGENCES — THE ACTUAL WORK

All measured 2026-08-06 ~2235Z from the **served bodies** (`s3 cp` per key, not `LastModified`).

### 3a · `account-distribution`

| field | inflection | 49financial | cottonwood | global |
|---|---|---|---|---|
| `basis` | ✓ `schwab-rps` | ✓ `schwab-rps` | ✓ `bd-rebalancer-models + bd-datamining-values` | ⛔ **`null`** |
| `source` | ✓ | ✓ | ✓ | ⛔ **`null`** |
| `firm_id` / `firm_name` | ✓ | ✓ | ✓ | ⛔ **absent** |
| `meta` | ✓ | ⛔ **absent** | ✓ | ✓ |

**S-1 (global):** the fold drops `basis`/`source` to null and omits `firm_id`/`firm_name`. Decide the
canonical global form — a scope identifier plus a *composite* basis/source naming the contributing legs
is the shape-consistent answer; **null is not.**
**S-2 (49financial):** alone lacks `meta`. The other three carry `meta.account_count_by_model_key`.

### 3b · `aggregate-aua-timeseries`

| field | inflection | 49financial | cottonwood | global |
|---|---|---|---|---|
| `account_count_total` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `count_provenance` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `source_vintage_last` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `non_model_aua` populated | 431/437 | 437/437 | ⛔ **8/446** | 431/455 |

**S-3 (cottonwood) — the largest gap.** Three fields the other three scopes carry are **never emitted**.
Root cause is structural, not a bug: **cottonwood is built by a different script in a different tree**
(`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`) from 49F/inflection
(`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`). The one firm-parameterized path
(P1-1) is what closes this — it is the consolidation's whole point, arriving as a shape requirement.

**S-4 (cottonwood non-model) — I-2's live gap.** 8 of 446 dates populated. **Not a defect in the
derivation:** the slice builder derives `non_model = partner_custody_total − model_aua` and holds
*honest-None* when custody is absent, with a W-2b identity gate (`:744`) that refuses a fabricated
balance. **The last two dates ARE populated (~$346mm)** — the custody leg only recently began landing.
**Per I-2 this data belongs in Cottonwood's own artifact**, so the requirement is coverage, not a new
mechanism. ⚠ **Never close this by relaxing the honest-None rule** — a populated-but-wrong non-model is
worse than None, and the identity gate is the control preventing it.

**S-5 (global, shape question — not a defect):** global carries `inflection_non_model_aua`, a
**firm-named field at global scope**, marked audit-only in source. Under I-2 that data is canonically
Inflection's and already lives there (431/437). **Question for the spec, not an assumption:** does the
canonical global shape retain a firm-named audit series? *Do not delete it on this document's authority
— it is referenced by `route_bindings.yaml:101-103` and by the leg pins.*

**S-6 (global-only fields):** `opal_aggregate_aua`, `point_class`, `account_count_total_raw`,
`count_as_of`, `count_basis` exist only at global. Some are legitimately global-only
(`opal_aggregate_aua` is the headline identity's left side). **Classify each as canonical-global vs
residue before P1-1 freezes the shape.**

### 3c · Data-adjacent observations — VERIFY, DO NOT ASSERT

Per §0 these are **not** filed as defects. Flagged only so the canonical builder reproduces intended
behaviour rather than silently changing it.

- **Global count is HELD at a 2026-07-22 vintage** — `count_basis` tail is all `held`, `count_as_of` ends
  `2026-07-22`, while `model_aua` runs to `2026-08-03`. The field is **honestly labelled**; confirm the
  hold is intended before the canonical builder reproduces or refreshes it.
- **Firm-sum 7,926 vs global 7,925**, and `meta.cottonwood_fold.accounts_folded 295` vs cottonwood's own
  `294`. Plausibly an intended dedup. **Confirm intended; do not "correct" it.**
- **Mixed vintage in the global fold** — global stamps `period 2026-08-04` while folding cottonwood's
  `2026-08-03`. Consistent with per-feed cadences (Rule 1); confirm the stamp convention is intended.

---

## 4. ACCEPTANCE

Per the standing governing criterion — **assert the OUTCOME, never the intervention**:

1. **12 objects exist** at the 12 canonical paths for the day *(EXISTENCE — never reported as freshness)*.
2. **Per artifact type, the key set is IDENTICAL across all four scopes**, modulo an explicitly declared
   and justified global-only set (S-6). A field present on one scope and absent on a sibling is a
   **failure**, not a warning.
3. **I-1 holds and is CONFIG-DRIVEN**: global non-model equals the sum over `fee_scope: full` firms —
   asserted against `fee_basis_components`, **not** against a literal `49financial`.
4. **I-2 holds**: each firm artifact carries its own non-model; Cottonwood's coverage is measured and
   reported as a ratio with its denominator printed.
5. **I-3 holds**: global `account-distribution` counts total model holdings excluding unfunded.
6. **Byte-comparison against today's served artifacts** for every field NOT named in §3 — the shape
   changes; the business payload does not. **A diff outside §3 is a regression.**

---

## 5. WHAT THIS SPEC DOES NOT AUTHORIZE

- **No served key moves.** `json/mdpf/*` untouched; the hyphenated legacy `account-distribution.json`
  bell does not move.
- **No semantic change.** §1 is ruled and live. A builder that changes a §1 number has failed, not fixed.
- **No deletion.** S-5/S-6 are classification questions; deletion of a served field is NEVER#3 and
  Andrew's.
- ~~**The 12-vs-14 question stays open**~~ — **SUPERSEDED, see §6.1.**

---

# 6. REVISIONS — SUPERSEDING §1–§5 (2026-08-06 ~2255Z)

## 6.1 · 12-vs-14 is RESOLVED — and it is a THIRD option neither reading offered

Andrew-direct at the MSTR~Z terminal **~2215Z — 35 minutes BEFORE this spec issued.** My "stays open"
line was **stale, not contradictory** (COO~Z surfaced the conflict rather than picking; record:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260806_MDPF_12_CANONICAL_SHAPE_EXTRAS_FOLD_IN.md`).

**EXACTLY 12, and the extras' INFORMATION survives inside them** — neither 14-with-extras nor
12-with-data-dropped. `cottonwood/account-units` → the count folds into `account-distribution.json`
(*"the file that feeds the bell curve, which is the component that serves the count"*);
`global/non-model-assets` → folds into **both** `aum-metrics.json` and `aggregate-aua-timeseries.json`.

**THE SHAPE LAW (his):** the 12 are *"identical in shape by the time they're in platinum"* — the folded
fields are canonical **for every scope**, never cottonwood-only or global-only appendages; a scope
without data carries the field with **honest absence**.
⇒ **§4 criterion 2's "modulo an explicitly declared global-only set" IS STRUCK.** One schema per type,
four scopes, honest absence.
⇒ **S-5 and S-6 are DISSOLVED, not classification questions.** A firm-named field at global scope
(`inflection_non_model_aua`) is not a canonical shape; "global-only" ceases to be a category.
**⚠ Still NOT a deletion warrant** — NEVER#3 and the retire-after-verify sequence bind. His words:
*"the two standalone extras retire only AFTER their information is folded and verified."*

**THE LAYER LAW (his):** *"inherently bronze/silver will be different per scope, however in the gold
layer the scripts that produce these files need to iron out these changes."*
⇒ **CROSS-VENDOR NORMALIZATION IS GOLD'S JOB. Platinum projects an already-canonical gold; it never
patches shape.** Any TO placing shape normalization in the publisher is wrong on his word.
Direction is serve-side-first, and **the port and this ruling are ONE BUILD, not two.**

## 6.2 · I-1's MECHANISM CLAIM WAS WRONG — I read an OUTPUT as an INPUT

`0.7.0_AE_CloudOps~Z` and `0.4.0_DS_ClientPlatform~Z` falsified this independently, from different
files, within seconds of each other. **`fee_scope` is hardcoded, twice** —
`dim_mdpf_aggregate_aua_timeseries.py:2378` and `dim_mdpf_aum_metrics.py:191-195` — **absent from
`partner_roster.json` and `route_bindings.yaml`.** `data/firm_registry.json` has a `fee_scope` field
and every sampled occurrence is **null**: a declared home sitting empty while the code carries the values.

> **DS~Z's diagnosis, verbatim: *"'read config' would today mean THE BUILDER READING ITS OWN EMISSION."***
> `meta.fee_basis_components` is the **output of the hardcode**, not an input. **I inferred a MECHANISM
> from a DESCRIPTION instead of reading the enforcing layer — GENCHI GENBUTSU entry 2, the clause I
> committed at `8b7b30390` forty minutes earlier.** Fourth instance of the day's shape, mine, in a spec
> already issued to four seats.

**RULED — the narrow answer, not the tidy one:**
1. **§4's "never special-cases 49financial by name" is STRUCK.** It asserts a property that does not
   exist and cannot be delivered by shape work; keeping it forces a lane to fail or widen.
2. **P1-1 builds against the hardcode AS-IS — but the TWO copies collapse to ONE.** Duplicate copies of
   one map is consolidation (P1-1's actual job), needs no roster change, and closes a
   duplicate-authority defect in miniature.
3. **The declarativeness migration is P2-1's config axis**, not P1-1. AE~Z classified it correctly:
   not a shape divergence, not a wrong number — a **declarativeness** finding.
4. **Do NOT populate `firm_registry.json`'s empty `fee_scope` on this document's authority.**
⇒ **P1-1 collapses 2→1. P2-1 later considers 1→declared.** Each inside its own scope.

*AE~Z's cluster (all in modules P1-1 touches): `_cot_window`'s literal `3` (a threshold), the `<5` pin's
comment-only rationale, and the two `fee_scope` maps (partners) — each a value the roster's charter says
must be declared, living as a literal in a consumer, correct today and invisible to every instrument.
The roster's own `_doc.acceptance` states the **PARTNER-#4 TEST**: onboarding a partner is a row and
nothing else. **ONE RULE FOR ALL THREE: P1-1 collapses duplicates and changes NO values; P2-1 owns the
migration.***

## 6.3 · S-4's mechanism corrected — and the hazard is WORSE than I wrote

**`:744` is `frontier_stamp_staleness()`, not a W-2b identity gate — my citation was wrong** (same
slice-offset class DS~Z hit earlier). The honest-None guard is **the derivation itself**: `:853`,
`:1131-1132`, and `:782` — *"A date the source hasn't reached is honest-absent, never fabricated."*

> **THERE IS NO GATE OBJECT TO DELETE — so "non_model is non-null" is satisfiable by changing
> `else None` to `else 0`. A ONE-TOKEN EDIT THAT READS AS NULL-SAFETY HARDENING AND LEAVES NO
> DELETED-GUARD SCAR.** Strictly easier than removing a named control and strictly harder to catch.
> Acceptance is **COVERAGE with the denominator printed**, never non-null.

**RULED — the guard asymmetry:** `:853` checks only custody; `:1131-1132` checks **both** operands.
**The both-operand form wins.** `:853` relies on `model_aua` being non-None *by construction on that
leg* — precisely the premise a firm-parameterized path dissolves when that leg stops being the only
caller. A TypeError on a None `model_aua` is not a better failure than an honest None.

## 6.4 · CRITERION 6 REWRITTEN — it would have SELF-DESTRUCTED ON FIRST RUN

`3.0.0_SA_CVO~Z` took the criterion I flagged as most-likely-to-be-softened and attacked it cold. All
five fixes accepted.

> **(a) THE FATAL ONE: "byte" is a FILE property; "field" is a PARSED-STRUCTURE property — and §3
> CHANGES THE SHAPE, so key order will change.** Read literally it fires on nearly every field, is
> judged "too noisy," and gets weakened. **It arrives at the outcome I feared through IMPRECISION
> rather than deploy pressure** — my own criterion destroying itself.

**REWRITTEN — criterion 6 is now:**
1. **VALUE-IDENTICAL PER JSON PATH**, not byte-identical, under a **declared canonicalisation** (sorted
   keys, normalised number formatting, explicit unicode handling).
2. **EXERCISED AGAINST A DELIBERATE MUTATION** and shown to **FAIL and LOCALISE** before any PASS it
   produces is citable. *A comparator that passes everything is indistinguishable from a broken one* —
   and doc 02 required-proof step 4 + doc 04 §1 **already require this; my criterion failed to inherit
   it.**
3. **BASELINE PINNED TO EXPLICIT VersionIds AT A STAMPED INSTANT.** "Today's served artifacts" is a
   moving target — measured tonight: 444 objects archived at 21:42Z, and AE~Z's P0-1 baseline froze keys
   at 21:01Z that moved **41 minutes later**. Versioning is on (`Versions=19` verified), so this is free.
4. **ABSENT vs NULL vs ZERO are THREE STATES.** `04` §3 already requires *"absent is never zero"*, and a
   naive dict comparison collapses missing and null — load-bearing, since criterion 2 makes
   present-on-one/absent-on-a-sibling a failure.
5. **§3 MUST YIELD A CLOSED FIELD-PATH LIST THE COMPARATOR CONSUMES.** §3 is the exemption's
   **denominator**; left as prose, *"named in §3"* becomes arguable at exactly the moment someone wants
   a diff excused. A field quietly added to the exemption must show up as a change to that list, never
   as a silently-passing diff.

## 6.5 · The symmetry CVO~Z named — bank it

> **A result that would CLOSE an open question needs a second oracle** (AE~Z's rule, applied four times
> tonight). **A result that would OPEN a big finding needs one too** (never applied tonight).
> **Same tell — the answer is interesting — opposite directions.** A finding *feels* like the safe
> error; it is not. My ~$409mm surfacing is the worked instance.
