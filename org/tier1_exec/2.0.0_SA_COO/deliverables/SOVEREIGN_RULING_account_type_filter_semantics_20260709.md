# SOVEREIGN RULING — 49F "Account Type" filter semantics

**Ruled by:** Andrew Berman (sovereign), 2026-07-09T~22:10Z, via 2.0.0_SA_COO, both domains printed.
**Decision routed by:** `2.0.0_SA_COO` · **Found by:** `0.4.0_DS_ClientPlatform~B` (`37cecb3fe`) · **A_00 enrichment blocked fabric-wide by:** `1.0.0_SA_CTO` (`220052Z`) pending this ruling.
**Brief:** `docs/briefs/bd-account-type-filter-semantics-decision-20260709.md`

---

## THE RULING: **(A) — Make the control WORK.**

**Repoint the filter's option-value source from `accounts_dimension.account_type` to `account_owner_type`.**

The control then offers `Sole / Joint / Trust`. **Every option matches real rows.** Cheap, immediate, no producer
dependency. The portal does **not** gain IRA/Brokerage/RothIRA filtering, and the label `"Account Type"` now
denotes **ownership structure**. Andrew was shown that cost explicitly and accepted it.

**Rejected:** (B) repoint the *column* to `account_type` + fix the enrichment — it would couple a client-facing
control to the exact upstream fragility (0-row-stub) that has frozen the served AUA for nine days.
(C) two distinct filters — correct but gated on the same enrichment. (D) leave it empty.

---

## WHY THE OBVIOUS FIX WAS THE WRONG ONE — the number that decided it

Both domains measured against `silver/allocations/2026-07-08` (the last partition with rows):

```
in BOTH -- would work BY COINCIDENCE  :  Joint, Trust                              (  2 of 30 )
values-only -- select ZERO rows       :  IRA Brokerage RothIRA InheritedIRA SEP SIMPLE 401K 403B
                                         529 HSA Annuity Bank Charitable Corporate CreditCard
                                         EducationSavings Estate Guardian Insurance LLC Loans
                                         Mortgage Other Savings TermLife UTMA
                                         InheritedRothIRA "No Account Type Assigned"  ( 28 of 30 )
column-only -- NEVER OFFERED          :  Sole   <-- 6,063 accounts, the LARGEST cohort
```

> **Today's empty dropdown is not merely broken — it is the only state in which this control cannot lie.**
> Populate `account_type` and a user selects `IRA`, gets an empty result set, **and believes it.**
> `Joint` and `Trust` would work **by accident.** (`0.4.0_DS~B`)

**Fixing `A_00` alone was strictly worse than leaving it broken.** A visibly-broken control becomes a
silently-wrong one. This is the **third `loud → quiet` inversion** of 2026-07-09, alongside `fabric-check`'s
deploy gate (fixing the false-REDs alone would have made the gate permanently silent, because a clean fabric is
the normal state) and the `DryRun` parameter. CTO: *"it is becoming the most expensive move we make."*

---

## BINDING SEQUENCE — (A) LANDS BEFORE ANY `A_00` ENRICHMENT FIX

> ### CORRECTED 2026-07-09T22:15Z. THE ORIGINAL REVISION OF THIS SECTION SAID STEP 1 LANDS **"NOW."** THAT WAS WRONG AND DANGEROUS, AND IT WAS MINE.
> `0.4.0_DS~B` refused the dispatch and named the hazard (`221212Z`). **`safe-deploy.sh` (pre-push hook, Rule 13)
> auto-deploys `data/black_diamond/scripts/{gold,silver,bronze}/*.py` → `opal-data-bd/code`.** A commit+push of
> `A_00` or `D_00` **puts new code into the ~04:00Z scheduled gold** — the exact run gated for the 49F un-freeze,
> whose success is already a coin flip on `perf.date.max()`. `comp-pipescript deployed` currently reports
> `4 MATCH, 0 STALE`.
>
> **And step 2 edits `D_00` — the script that holds the served AUA** (`_resolve_served_aua`, the BRANCH-A
> last-good hold, `b5a95c9f5`). **A filter fix has no business riding into the freeze-plane's producer on the
> night we are trying to un-freeze it.** Nothing here is "just a doc change."

**NOTHING IN THIS SEQUENCE LANDS BEFORE THE ~04:00Z WINDOW CLOSES AND `0.6.0` HAS REPORTED WHETHER THE UN-FREEZE
FIRED.** Every step below is a real deploy to a live code prefix and each opens a `deploy_ledger.py open` entry
(NEVER#6 binds; a begun deploy finishes in-session or rolls back).

0. **GATE:** 04:00Z window closed + `0.6.0`'s un-freeze report in + **CTO has ratified the ABSTAIN verb (below).**
1. **THEN:** `row_count > 0` + **ABSTAIN-FROM-THE-ENRICHMENT-JOIN** + a **loud alarm** in `A_00`. Keeps the
   columns null; makes the producer loud. **Loud-and-null.** Exercise **both directions** — it must alarm on the
   0-row stub *and* stay silent on the real `07-08` partition — then commit, push (auto-deploys), verify
   `comp-pipescript deployed` MATCH, close the ledger.
2. **THEN (A):** repoint the value source to `adim['account_owner_type']` (`D_00.portal_aggregates` →
   `_dim_values()` → `gold/artifacts/filters/dimensions.json`). **DS lane, Rule 13.** Verify on the **SERVED**
   `filters/dimensions.json` after the **next scheduled gold** that `account_type.values == {Sole, Joint, Trust}`.
   **Never an ad-hoc gold run (NEVER#4).**
3. **ONLY AFTER (A) IS SERVED** does populating `account_type` become safe. Until then the **CTO prohibition
   stands**: nothing populates `account_type`. It will look like an obvious one-line win to whoever touches
   `A_00` next. **It is not.**

**Inverting 2 and 3 re-creates the exact defect this ruling exists to prevent.**

---

## THE `ABSTAIN` VERB IS UNRATIFIED AND ONE READING TAKES OUT THE ESTATE. CTO MUST RATIFY IN WRITING.

`0.4.0_DS~B` refused to write code against it, correctly. *Abstain from **what**?*

- **Reading 1 — intended, safe.** Abstain from the **allocation-enrichment join**. `account_type` /
  `account_registration_type` stay null — **byte-identical to today's output** — and the producer alarms loudly.
  **Zero downstream change.** This is **loud-and-null.**
- **Reading 2 — catastrophic.** Abstain from **writing `accounts_dimension_latest.parquet` at all**, because the
  guard failed. `comp-pipescript io A_00` says that artifact feeds **17 scripts**: `A_01, A_04, B_00, B_01, B_02,
  C_00, C_01, C_02, C_03, C_05, C_06, C_07, D_00, D_00b, D_00f, D_01, D_04`. **It would take out the entire bd
  gold DAG**, including `C_02`'s certification and `D_00`'s served output. This is **loud-and-gone.**

> **The guard's trigger condition — a 0-row allocations partition — IS TRUE RIGHT NOW, and true on most recent
> dates. Reading 2 does not fail rarely. It fails TONIGHT, on the first run.**

**THE TEXT CTO MUST RATIFY, VERBATIM:**
> `A_00` abstains from the **allocation enrichment join only**. It **ALWAYS** writes
> `accounts_dimension_latest.parquet`. On `row_count == 0` it leaves `account_type` /
> `account_registration_type` null, emits a loud alarm, and **proceeds**. It **never** skips the dimension write.

**This is the same shape as the P3 `req1` verb:** *a one-word instruction whose two readings differ by an
estate.* It is also this session's own thesis, turned on my own artifact — **I wrote a word that names a
behaviour without specifying which behaviour**, exactly as `comp-freshness` names "freshness" without specifying
which property. **A verb is a wrapper. Ratify the property.**

The prohibition's *reason* goes in the code at the site (the way `_drift_warn_alert` carries CTO's promotion
conditions), so it outlives everyone's memory of why it exists.

---

## OPEN, AND DELIBERATELY NOT SELF-ANSWERED

**The label.** Under (A) the control is titled `"Account Type"` and denotes ownership. Andrew accepted that cost
knowingly. **Relabelling it `Ownership` would remove the stated cost at near-zero incremental effort** — and a
name that does not describe what the thing measures is *precisely* the defect class this entire session has been
chasing (`comp-freshness` "freshness" = a filename; `gap_pct` "gap" = two co-dependent operands;
`source_vintage_last.status: current` = a status excluding its stale inputs). **Surfaced to Andrew + CTO as a
follow-up. NOT self-authorized — the ruling is (A) as written, and (A) does not include a relabel.**

---

## THE FINDING'S PROVENANCE, because the method is the transferable part

`0.4.0_DS~B` resolved every `account_type` reference **to the frame it is read from**, not by grep. Eight
candidates → **one** real served consumer:

- `D_00.portal_aggregates:355-360` loads it from the dimension, `_dim_values():822-824` runs `series.dropna()`,
  and the result is written to `gold/artifacts/filters/dimensions.json`. **Served object, LastModified
  `2026-07-09T09:53:12Z`:** `account_type values=0` while `architect=56 · implementor=50 · state=49 · region=19 ·
  tax_status=3`.
- **`C_02` is NOT a reader** (`:319/:325` read `silver['account_type']`). Nor `C_04`, nor `E_19`.
- **`D_04` is NOT a reader** — it reads `silver_agg['account_type']` off the allocations parquet where the column
  **is** populated. **`D_04` was one of the two scripts CTO pre-committed as a P0 trigger. It is a grep
  false-positive.**
- **`D_00b` loads `account_type` from the dimension (`:1314`) and never uses it.** Loads-and-discards — a
  "who loads it" trace scores it a consumer; it emits nothing.

**Severity: S2, not P0** — argued **down** by the lane that found it, against an exec's pre-registered trigger.
CTO accepted, and named why his own trigger was unsound: **it bound severity to the reader's *identity* — itself
a proxy — and would have fired on false evidence.** *"An empty dropdown and a wrong $1.837B are not the same
plane, and flattening them costs the word P0 its meaning."*

## ONE ROOT, NOT THREE BUGS

`account_type` (0/10,545), `account_registration_type` (0/10,545), and `A_04`'s `client_dimension.account_types`
(0/3,771, **read by nobody** — a dead field that dies in the dimension) all descend from **one existence-guarded
join onto a 0-row partition** in `A_00`:

```
A_00:333  if not alloc_keys:                     # guards ONLY on "no files at all"
A_00:337  latest_key = sorted(alloc_keys)[-1]    # newest BY NAME = 2026-07-09.parquet = 0-ROW STUB
A_00:340  alloc = pd.read_parquet(...)           # read SUCCEEDS. zero rows.
A_00:347  print(f"{len(enrichment):,} accounts with type/registration data")   # prints "0". PROCEEDS.
```

**Same byte-vs-row proxy as `C_02`'s certification path (`:309-310`).** Two scripts, one defect. Existence is
the proxy; rows are the property.

## BOUNDS ON THE NEGATIVE (stated unprompted by the finder — a negative is a claim about the query)

`D_00` is a **confirmed** consumer. *"Nothing else consumes it"* is **NOT claimed.** Untraced: dynamic column
access (`df[col]`, `regex=`, `**kwargs`); `merge()`-and-carry with `_x`/`_y` survivors; **the portal frontend
reading `filters/dimensions.json` directly**; Athena / Lambdas / notebooks; **the entire cot tree** (828 cot
accounts); and whether `B_01`'s null-enriched `holdings_lots` reaches any served artifact.

> `B_01:450` was traceable **only because its column list is a literal.** A computed list would have been
> invisible to the very method that found this.
