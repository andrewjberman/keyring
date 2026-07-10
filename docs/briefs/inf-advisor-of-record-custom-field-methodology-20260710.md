# BRIEF — Inflection advisor ownership: the `Advisor of Record` custom field is the correct key, and the pipeline keys on the wrong one

**Status:** Finding + migration proposal — HAND-OFF to `1.0.0_SA_CTO~B`
**Author:** `0.0.0_AB_MSTR` (ad-hoc Orion pull, Andrew-authorized 2026-07-10)
**Scope:** ADVI_INFLEC (inf) — in-scope. Read-only Orion pull; no writes to Orion.
**Date:** 2026-07-10

---

## 1. Executive finding

Inflection's **true advisor ownership** is carried in an Orion **account custom field**
(`udf7ADVISOROF`, label "Advisor Of Record"), **not** in the `Representative` field the current
inf-pipeline uses to key `advisor_key`. The two disagree materially:

| Methodology | Accounts | Asset value (current MV) |
|---|--:|--:|
| **Current pipeline** — Representative, scoped to rep_id ∈ {3, 11, 12} | 850 | **$182.97M** |
| **Advisor of Record** — `udf7ADVISOROF` custom field | 900 | **$203.65M** |

The gap is **not noise** — it is a **$24.6M block of advisor-owned AUM (92 accounts) that the current
methodology cannot see**, because those accounts are custodially assigned to *external-firm reps* (rep_id
6/5/9/14) while Inflection designates them as its own advisor-of-record accounts. Minus $3.9M (42 accounts)
that the rep-scope over-includes (rep-scoped but no advisor-of-record designation).

**Canonicalized advisor rollup (the numbers Andrew validated), advisor-of-record method:**

| Advisor of record | Accounts | Asset value |
|---|--:|--:|
| Peter Lee | 502 | $133.09M |
| Joe Brandenburg | 154 | $29.19M |
| **Patrick Scanlan** (= "Patrick Scanlan" + "Scanlan_IWM") | 171 | $23.67M |
| **Noel Soderblom** (= "Noel Soderblom" + "Soderblom_IWM") | 64 | $12.42M |
| Jeremy Keil | 8 | $5.12M |
| Tim DeMuth | 1 | $0.16M |
| **Total (advisor-owned)** | **900** | **$203.65M** |

Andrew's three confirmations against this:
1. **Patrick Scanlan** — the raw field splits him into `Patrick Scanlan` ($17.3M/84) + `Scanlan_IWM`
   ($6.4M/87); **summed = $23.67M/171, the correct number.**
2. **Noel Soderblom** — `Soderblom_IWM` ($3.6M/19) + `Noel Soderblom` ($8.9M/45) = **$12.42M/64. This
   advisor does not appear in the main advisor (Representative) view in Orion at all** — it is the clearest
   proof the rep view is lossy. This is an advisor Inflection wants to track and currently cannot.
3. **Peter Lee ($133.1M) and Joe Brandenburg ($29.2M)** — correct under advisor-of-record.

---

## 2. How this was found (endpoints, backend, fields)

**Endpoint (single call, the whole answer):**
```
GET https://api.cloud.orionadvisor.com/api/v1/Portfolio/Accounts?top=5000
Authorization: Session <jwt>        # NOT "Bearer" — Bearer silently 401s
App: OrionConnect
Origin/Referer: https://api.cloud.orionadvisor.com/...   # CSRF-adjacent, required
```
- **Auth:** the shared Orion Connect JWT, `s3://opal-data-inf/orion/jwt/current.json` (`a_c=4698` = the
  Inflection *platform* database — shared by several firms). Same JWT that authenticates Envision +
  Portfolio. Freshness gate: `data/inf/manual_api/jwt_freshness.py`.
- **Response:** JSON array, **3,113 account objects**, ~8.1 MB, total current MV **$685.19M** (all firms on
  the shared platform, not just Inflection).

**Backend discovery — the key insight:** Orion's `/Portfolio/Accounts` account object exposes **custom
fields (UDFs) INLINE** as keys of the form `udf<n><LABEL-truncated>`. Enumerating every `udf*` key across
the roster surfaced the advisor fields the reverse-engineered API catalog had never cataloged:

| Inline key | Meaning (label truncated ~12 chars) | Populated | Sample |
|---|---|--:|---|
| **`udf7ADVISOROF`** | **Advisor Of Record** | 900 | `Peter Lee` |
| `udf1:7ADVISOR` | Advisor (fully present, has a literal `Unassigned` bucket) | 3,113 | `Jeremy Keil C00966812` |
| `udf7HISTORICA` | Historical (bool flag) | 3,113 | `False` |
| `udf7CSPDATED` | CSP dated (date) | 1,061 | `2022-05-12` |
| `udfAIP` | AIP (household) | 765 | `Donald & Kathleen Achatz` |

**Fields used to produce the snapshot** (all from the same object, no Envision query needed):

| Requested field | Orion object key |
|---|---|
| Account ID | `id` |
| Account Name | `name` |
| Advisor of Record (custom field) | **`udf7ADVISOROF`** |
| Market value | **`currentValue`** (current account MV; `accountStartValue` = beginning) |
| (comparison) Representative | `representative` / `representativeId` / `representativeNumber` |

> Note: this did **not** require the Envision querybuilder (`ExcelReports/Verbose` → `Generate` → poll).
> The direct Portfolio roster carries account id, name, market value, AND the custom field in one GET. If a
> querybuilder version is later wanted for a saved/scheduled artifact, the udf path in querybuilder is still
> undiscovered (a separate discovery task) — the roster is the pragmatic source.

**Reproduction:** `scratchpad/orion_advisor_snapshot.py` (enumerate) + `aggregate_by_advisor.py` (roll up).
Raw account-level CSV delivered to Andrew: `account_id, account_name, advisor_of_record, advisor_udf,
representative, current_value_MV, is_active` (3,113 rows).

---

## 3. How the pipeline keys advisor ownership TODAY (the research)

The current inf-pipeline keys advisor ownership on the **Representative** (the custodial download rep),
never on the advisor-of-record custom field. Chain:

| Layer | File | What it does |
|---|---|---|
| **Silver** | `data/inf/scripts/silver/convert_orion_api_to_silver.py` | Maps `Representative.Id`→`rep_id`, `Representative.Name`→`rep_name`, `Ending MV`→`account_aua`. **Keeps only** `rep_id, rep_name, account_id, account_name, household_id, account_aua, snapshot_date`. **Drops every `udf*` custom field.** Applies `filter_to_inflection(rep_id ∈ {3,11,12})`. |
| **Silver lib** | `_orion_api_silver_lib.py::slug_advisor_key(rep_name)` | `advisor_key` = snake-cased slug of `rep_name`. |
| **Gold** | `INF_A_01.advisor_assignments.py` | "current rep assignment per account," sourced from `accounts_v2` silver (one row/account = one current rep). Single rep per account, no SCD. |
| **Gold** | `INF_C_07.advisor_attribution.py` | Emits `account_team` / `relationship_team` / `rel_architect_lookup` keyed on `advisor_key`. `advisor_key` derived from `rep_name`, then **overridden** by `_apply_accounts_v2_advisor_key_override` to a `rep_id`-sourced value (INFGRD FLAG-2 fix, to reduce cross-firm *name* contamination). |
| **Config** | `data/inf/config/dim_inf_advisor_office.csv` | Advisor dim, header states scope: *"Inflection Wealth Management only per SCOPE A (rep_name == 'Inflection Wealth Management')… Other Orion reps belong to external firms… filtered at silver per SCOPEFIX."* |

**Downstream consumers of `advisor_key`:** `INF_C_01b` (role AUA), `INF_C_08` (advisor fee efficiency),
and the D-chain publishers (`INF_I_D00/D00b`, `INF_D_00c`, `INF_D_02`, `INF_I_D03`, `INF_D_04`). Every
per-advisor AUA/NNA/fee number the portal shows for Inflection is built on this rep-derived `advisor_key`.

**So the current methodology is: `advisor = Representative`, scoped by `rep_id ∈ {3,11,12}`.** It has been
patched repeatedly to fight *name* contamination (INFGRD FLAG-2, DIAGFIX.011, ADVI_DWSPLT) — but every patch
stays inside the rep model. The advisor-of-record custom field is not pulled, stored, or referenced anywhere.

---

## 4. Why the rep model is wrong (mechanism, quantified)

`Representative` is a **custodial / download attribute** — which rep code an account downloads under — not
the firm's advisor-ownership designation. Three failure modes, all measured on the live roster:

1. **It FRAGMENTS one advisor across rep entries.** Patrick Scanlan's accounts split into a `Patrick
   Scanlan` rep and a `Scanlan_IWM` rep; the rep view reports only the first. The advisor-of-record field
   carries both and sums to the correct $23.67M.
2. **It MISSES advisor-owned accounts under external reps.** **92 accounts / $24.63M** carry an Inflection
   advisor-of-record but sit under rep_id 6/5/9/14 (outside the `{3,11,12}` scope) — invisible to the
   pipeline. rep_id=6 alone holds 83 of them. **This is the entire Noel Soderblom book plus the Scanlan_IWM
   accounts.** Soderblom does not appear in the main advisor view at all.
3. **It OVER-INCLUDES.** 42 accounts / $3.95M are inside the `{3,11,12}` rep-scope but carry no
   advisor-of-record designation — house/unassigned accounts the rep-scope sweeps in.

**Net:** rep-scope $182.97M (850 acct) vs advisor-of-record $203.65M (900 acct). The rep model **understates
Inflection advisor AUM by ~$20.7M net (~$24.6M gross of the drop), and mis-attributes advisors it does
capture.**

**Alignment signal:** advisor-of-record covers $203.65M / 900 accounts — essentially the Inflection book —
while the $481.5M "unassigned" is the *other firms* on the shared platform. **The custom field is itself a
cleaner Inflection-membership signal than the `rep_id ∈ {3,11,12}` proxy**, because Inflection populates it
only for its own accounts.

---

## 5. Migration path — rep model → advisor-of-record model

Ordered, each a discrete change:

1. **Capture the UDFs in the silver pull.** `convert_orion_api_to_silver.py` currently drops all `udf*`
   fields; add `udf7ADVISOROF` (and `udf1:7ADVISOR` as a secondary) to the retained account columns. The
   source pull is already `/Portfolio/Accounts` (the roster used here) — no new endpoint.
2. **Re-key `advisor_key` on advisor-of-record**, not `rep_name`/`rep_id`, in `INF_A_01` +
   `INF_C_07::_apply_accounts_v2_advisor_key_override`. Keep the D-chain schema (`architect = advisor_key`)
   so consumers are unmodified.
3. **Replace the `rep_id ∈ {3,11,12}` scope** with "has an Inflection advisor-of-record" as the membership
   test (validate the two agree except for the 92/$24.6M and 42/$3.9M deltas above — those deltas are the
   *correction*, not a regression).
4. **Add a canonicalization map** for the `*_IWM` name variants (`Scanlan_IWM → Patrick Scanlan`,
   `Soderblom_IWM → Noel Soderblom`) — the field is human-entered and needs a small controlled vocabulary.
   Extend `dim_inf_advisor_office.csv` to key on advisor-of-record identities, not rep names.
5. **Reconcile** the migrated per-advisor AUA against Section 1's validated table before publishing.

---

## 6. Open items for the owner (`CTO~B` + Andrew)

- **Confirm the full label** of `udf7ADVISOROF` in Orion admin (the key truncates it) — verify it is the
  designation Inflection treats as advisor-of-record, and confirm whether `udf1:7ADVISOR` (the fully-present
  "Advisor" field with an `Unassigned` bucket) has any role.
- **Governance of the field:** who maintains advisor-of-record in Orion, and how consistently? The 2,213
  blank accounts are (hypothesis) other firms — confirm no Inflection account is silently blank.
- **The `*_IWM` variants:** are they a data-entry artifact to canonicalize, or a real sub-designation
  (e.g., IWM = a partner/branch) worth keeping as a second dimension?
- **Scope decision:** advisor-of-record as BOTH the scope and the attribution, or attribution-within-a-
  confirmed-scope. Section 4's alignment argues for the former.
- **Querybuilder path** (only if a scheduled Envision artifact is wanted): the querybuilder column path for
  this UDF is undiscovered; the roster GET is sufficient for the snapshot.

---

## Appendix — artifacts

- Account-level CSV (3,113 rows, all advisor fields side-by-side + MV): delivered to Andrew.
- Reproduction scripts: `scratchpad/orion_advisor_snapshot.py`, `scratchpad/aggregate_by_advisor.py`.
- Current-pipeline files cited: `convert_orion_api_to_silver.py`, `_orion_api_silver_lib.py`,
  `INF_A_01.advisor_assignments.py`, `INF_C_07.advisor_attribution.py`, `dim_inf_advisor_office.csv`.
- Auth reference: `data/inf/API/AUTHENTICATION.md`; endpoint catalog: `data/inf/API/domains/portfolio/`.
