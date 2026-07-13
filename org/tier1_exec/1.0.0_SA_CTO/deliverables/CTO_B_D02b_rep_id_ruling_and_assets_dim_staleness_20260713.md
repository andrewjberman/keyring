# CTO~B RULING — INF_D_02b rep_id "inversion": NOT A DEFECT (fix CANCELLED)
### + a separate LIVE finding: INF top_holdings is built on 69-day-old positions

**Author:** `1.0.0_SA_CTO~B` · **Date:** 2026-07-13 · **archetype:** DIAGNOSE
**Status:** RULED — the staged D_02b fix is **CANCELLED**. Do not "align" the map.
**Grounding vintage:** all source reads `@ 5581c0de1` (working tree clean for the cited files); all data/served reads live 2026-07-13T05:2x–05:3xZ.

---

## 1. THE HYPOTHESIS (as staged)

> `INF_D_02b` carries a LOCAL rep_id map reversing peter↔patrick vs canonical.

Filed as HYPOTHESIS-only pending a Rule-22 source-grounded mechanism; no fix authorized until CTO~B ruled.
**This is that ruling. The literal reversal is REAL. The DEFECT IS NOT.**

## 2. THE SOURCE FACT (the smoking gun — and it is a false one)

| file:line @ 5581c0de1 | rep_id `3` | rep_id `6` | rep_id `11` | rep_id `12` |
|---|---|---|---|---|
| `INF_D_02b.top_holdings.py:73-78` | IWM | joe_brandenburg | **peter_lee** | **patrick_scanlan** |
| `INF_C_01.canonical_nna.py:375-380` | IWM | joe_brandenburg | **patrick_scanlan** | **peter_lee** |
| `lib/inflection_rep_scope.py:526-531` | IWM | joe_brandenburg | **patrick_scanlan** | **peter_lee** |

Three maps, identical key set `{3,6,11,12}`, **agreeing on 3 and 6 and disagreeing ONLY on 11/12** — a 2-vs-1
outlier on exactly the transposed pair. As compelling a source-level defect signature as this codebase produces.
It is wrong.

## 3. WHY IT IS NOT A BUG — the two silver dims genuinely TRANSPOSE rep_id

Measured live (2026-07-13). `accounts_v2` carries the **human name** beside the id, so it is self-naming:

| | `silver/api_dims/accounts_v2/snapshot_date=2026-07-12`<br>(C_01 + lib's input) | `silver/api_dims/assets/snapshot_date=2026-05-05`<br>(**D_02b's input**) |
|---|---|---|
| **rep_id 12** | **"Peter Lee" — 628 accounts (BIG)** | 145 accounts |
| **rep_id 11** | **"Patrick Scanlan" — 141 accounts** | 567 accounts (BIG) |
| rep_id 6 | "Joe Brandenburg" — 83 | 67 |
| rep_id 3 | "Inflection Wealth Management" — 21 | 15 |

**`rep_id` 11 and 12 are transposed BETWEEN THE TWO DIMS.** Same column name, two different id-spaces.
**Each map is therefore CORRECT FOR ITS OWN INPUT.**

## 4. THE SERVED ARTIFACT CONFIRMS IT (Rule 22a — a behavior claim is grounded on the served artifact)

| advisor | `top_holdings.json` `total_market_value` (INF_D_02b) | max `account_count` | `book.json` clients (**INF_D_02** — independent producer) |
|---|---|---|---|
| peter_lee | **$160,608,037** | 442 | **193** |
| patrick_scanlan | $20,425,843 | 93 | 66 |
| joe_brandenburg | $19,353,828 | 65 | 27 |

Peter's artifact holds Peter's **large** book. The **deployed** D_02b (`s3://opal-data-inf/code/gold/`, uploaded
2026-07-10) carries the same `'11': 'peter_lee'` map. **The map that "looks reversed" is the one producing the
RIGHT served answer.**

## 5. THE HARM THE "FIX" WOULD HAVE DONE

Aligning D_02b's map to canonical is a **2-line diff that reads as "conform to the SSOT."** It would rebuild
`peter_lee/top_holdings.json` from rep-11 rows of the **assets** dim — Patrick's 66-client book — and hand
**Inflection's largest advisor ($160.6M, 193 clients) the wrong book**, and vice versa.
**It converts a CORRECT served artifact into a WRONG one, on the firm's two biggest advisors, via a diff that
looks like a cleanup.** Cancelled before DS reached it.

## 6. WHAT IS ACTUALLY WRONG (the real, and much smaller, finding)

Two silver dims silently disagree on the meaning of a column called `rep_id`. **The next person to notice the
"reversal" walks into the same trap.** The remedy is NOT to change either map — it is to make the id-spaces
unmistakable:

- Name the input dim explicitly at each of the three maps (necessary, insufficient — *a comment is what I would
  have ignored*).
- **Better: an ASSERTION that fails if the assumed rep→advisor binding does not hold in the partition being read**
  (e.g. assert the rep_id owning the largest book in `accounts_v2` resolves to `peter_lee`). An assertion binds; a
  comment persuades.

Owner: silver-dim owner, **post-round-8.2**. Explicitly NOT an 8.2 item — do not widen 8.2.

---

## 7. SEPARATE + LIVE — INF top_holdings runs on **69-day-old** positions

Found while grounding §3. **Not part of the D_02b ruling and not a gate-1 item.**

`INF_D_02b`'s only position source is `silver/api_dims/assets/` — **FROZEN at `snapshot_date=2026-05-05`,
3 partitions total.** Freshness sweep of every INF api_dim (2026-07-13):

| dim | latest partition | # partitions |
|---|---|---|
| `accounts_v2` | 2026-07-12 | 69 |
| **`positions_mv`** | **2026-07-12** | **2,271** |
| `activity` / `billing` / `performance` / `household_rep_mapping` | 2026-07-12 | 60 / 1,567 / 64 / 70 |
| **`assets`** ← *D_02b's only source* | **2026-05-05** | **3** |
| `assets_v2` | 2026-04-29 | 1 |
| `household` | 2026-04-28 | 1 |

`assets` (3 partitions) and `assets_v2` (1) look like **bootstrap dims superseded by `positions_mv` and never
migrated**; D_02b was authored 2026-04-28 against `assets` and left there.

**So INF's served firm-level AND per-advisor `top_holdings` are built on MAY position data.**

**And the label currently hides it.** The served artifact says `data_as_of: 2026-07-10` — the **run** date,
emitted by the pre-07-10 code. The **currently deployed** code derives it from the partition column
(`snapshot_date = str(df['snapshot_date'].iloc[0])`, deployed :272-274), so **the next nightly will emit
`data_as_of: 2026-05-05`** — honest at last, and it will surface the 69-day staleness on the portal.

**NOT claimed:** FE harm. `comp-pipescript io INF_D_02b` reports **no route match** for these platinum keys
(possible catch-all serve), so what the portal actually renders from them is **UNVERIFIED**. The claim is that
the artifact is 69 days stale and, today, mislabeled. Routed to COO as its own item.

---

## 8. THE LESSON — the same shape as tonight's F1 inversion, opposite direction

F1: a source-level mechanism read as **fail-closed**, exercised as **fail-open**.
D_02b: a source-level pattern read as **a defect**, measured as **correct**.

Both were overwhelmingly convincing on the code axis. Both were **one measurement** from the truth.
The measurement was cheap in both cases — a `representative_name` column, and a served `total_market_value`.

> **A source-level pattern is a HYPOTHESIS about the data, and the data is right there.**
> Rule 22 is not paperwork; it is the only thing standing between a persuasive diff and a corrupted served artifact.

**Denominators printed for every scan in this document.** (`comp-grep`: 5 matches / 1 file / 192 scanned;
`s3 ls assets/`: 3 partitions, not a `tail`.)
