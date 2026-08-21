# The $8.5M Cottonwood/BD plane gap — ACCOUNT-LEVEL DIAGNOSIS (Andrew-direct task, 2026-08-20 ~1840Z)

**Task (Andrew-direct, VERBATIM):** *"find that page, and cross reference the relationships/accounts
they list there to get to that +8m number and correspond it with the relationships/accounts that we
pick up and see what relationships/accounts we are missing. Then we need to triage that cohort and
understand the mechanism… if we are actually missing nothing and this is just a timing question
somehow, or if we are missing something and if so we need to understand the nature of that miss."*
**Egress:** standing (Cottonwood Black Diamond). **As-of date:** 2026-08-19 (both sides).

## VERDICT

**We ARE missing accounts — 117 of them — and it is NOT a timing question.** The cohort is
structural and one-natured: **100.00% of the supervised gap is outside-custodian feed accounts**
(529 plans, held-away, annuities) that Black Diamond's BI dashboard values but that never appear in
the DataMining holdings export our pipeline pulls.

## The reconciliation (closes to the cent)

| leg | accounts | value |
|---|---|---|
| BD dashboard firm total (live pull, 08-19) | 923 | $488,778,516.79 |
| our holdings extract (same date) | 941 | $480,261,559.55 |
| **BD-ONLY (missing from us)** | **117** | **+$12,867,460.17** |
| OURS-ONLY (we carry, BD dashboard scope drops) | 135 | −$4,231,550.68 |
| matched accounts, value deltas | 17 | −$118,952.26 |
| **NET** | | **$8,516,957.24** |

`488,778,516.79 − 480,261,559.55 = 8,516,957.24` — **identical**. Nothing is unexplained.

## The missing cohort, by mechanism (117 accounts, $12,867,460)

| class | n | market value | supervised |
|---|---|---|---|
| **DTCCR_** — 529 / CollegeAmerica plans | 78 | $4,991,175.36 | $4,991,175.36 |
| **ASLAA_** — held-away feed | 9 | $2,301,384.76 | $2,301,384.76 |
| **AEGON_** — annuity feed | 3 | $1,093,645.77 | $1,093,645.77 |
| **LNANN_** — annuity (Lincoln) | 1 | $231,632.40 | $231,632.40 |
| **plain-numeric custodial** (401k/plan accounts) | 26 | $4,249,621.87 | **$0.00** (all unsupervised) |

**THE DECISIVE LINE:** the four outside-custodian feed classes total **91 accounts /
$8,617,838.30 — and the supervised gap is $458,351,399.66 − $449,733,561.36 = $8,617,838.30.**
A 100.0% match, to the cent. The remaining 26 plain-numeric accounts are **entirely unsupervised**
($4,249,621.87) and therefore do not touch the supervised figure at all.

## Answering the three hypotheses Andrew named

1. **"Missing nothing, just timing"** — **REFUTED.** A timing miss would be date-shaped (a T-1/T-2
   lag on accounts we otherwise carry) and would appear as *value deltas on matched accounts*. Those
   exist but are trivial: 17 accounts, net **−$118,952** (0.02% of the book, largely cash-sweep
   timing). The $8.6M is 91 accounts **wholly absent**, not stale.
2. **"Very new clients"** — **REFUTED.** BD's own `newRelationshipAggregateResult` reads **$0.00**
   for the period; the cohort's relationships are existing ones. These accounts have been invisible
   to us continuously, not recently.
3. **"Odd attributes"** — **CONFIRMED, and the attribute is identified**: not a client trait but a
   **DATA-SOURCE trait**. Every missing supervised account carries a non-custodial feed prefix
   (`DTCCR_`/`ASLAA_`/`AEGON_`/`LNANN_`), i.e. positions BD ingests from outside-custodian
   channels — 529 plan administrators, held-away aggregation, annuity carriers. BD's BI dashboard
   values them; the DataMining holdings query we run does not return them.

## Why our pipeline does not see them (mechanism, and the honest limit)

Our bronze holdings extract is a **DataMining query** (persisted template 226355, qt1) — a
custodial-positions query. The missing accounts have **no custodial position rows**; their value in
BD arrives through the outside-feed channel. So the two planes are not disagreeing about the same
population: **the dashboard's population is a superset of the export's.** That is why BD's own two
DataMining exports (holdings and allocations) agree with each other and with us **to the penny**
($480,056,488.78 measured earlier today) — they share the export population — while the dashboard
sits $8.5M above all three.

⚠ **WHAT IS NOT YET PROVEN (stated, not glossed):** whether the outside-feed accounts are (a)
structurally unavailable through *any* DataMining query, or (b) available under a different
`queryTypeId` / level / a "include position-only accounts" option our template does not set. That
distinction decides the remedy and is one probe away (see below). Our own account-attributes pull
(943 accounts, AccountID-keyed) cannot answer it — it carries no account-number column to join on,
which is itself a small finding for the G1 template.

## The OURS-ONLY side (135 accounts, $4,231,551) — benign, and worth one line

**110 of the 135 are zero-value** — closed/empty accounts we still carry and BD's dashboard drops.
The 25 non-zero ($4.23M) are mostly 401(k)/plan accounts appearing under *different identifiers* on
our side (`ELLARD FAMILY HOLDINGS… 401(K)`, `Direct Supply, Inc. 401(k)`, `COTTONWOOD CAPITAL 401(K)`)
— the same economic accounts as several of BD's 26 plain-numeric rows, keyed differently. **This is
an identifier-alignment issue, not a coverage issue**, and it partially offsets the missing cohort.

## Recommended next acts (Andrew's call; nothing executed)

1. **ONE PROBE, in-house, ~30 min:** run a DataMining query with the *position-only / all-account*
   scope (or `queryTypeId` variants) filtered to three known missing accounts
   (`DTCCR_04003450617`, `ASLAA_E1080592`, `AEGON_000000111420TAL`). If rows return → our template
   scope is the defect and the fix is a template amendment (config, no code). If nothing returns →
   the feed genuinely does not traverse DataMining, and the remedy is a second source or a declared
   scope boundary.
2. **Then, and only then, the Manav/BD question** — now precisely framed: *"the BI dashboard values
   outside-feed accounts (DTCCR/ASLAA/AEGON/LNANN) that the DataMining holdings export omits — is
   there a query scope that returns them?"* Half-diagnosed, with the exact cohort attached.
3. **Serving decision (business, yours):** whether the Opal dashboard's supervised AUM should equal
   BD's $458.4M (requires ingesting outside feeds) or remain the $449.7M custodial-positions book
   **with the $8.6M outside-feed difference declared on the artifact face**. The gold artifact
   already carries a plane-gap declaration; this diagnosis makes it nameable rather than
   unexplained.

## Method note (for the record)

The first join keyed on the account-number trailing token and produced a **false cohort** — it
collapsed every multi-word account number (`ADC Investments Trust Alts`) to one key, manufacturing a
$19.8M phantom "missing alts" class and a matching phantom on the ours-only side. Caught by the
reconciliation failing to close, fixed with mask-aware normalized keys, and re-derived. The
published cohort is the v2 join, whose residual is **$0.00**. *An account-level diff that does not
reconcile to the firm delta is not a finding; it is an artifact of its own key.*
