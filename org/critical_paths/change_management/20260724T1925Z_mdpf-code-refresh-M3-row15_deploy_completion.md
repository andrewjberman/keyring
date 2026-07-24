# Deploy Completion Ledger — MDPF gold code refresh (M3 / closure row 15 precursor)

**Opened:** 2026-07-24T19:25Z — **BEFORE the first byte moved** (NEVER#6).
**Owner:** `0.7.0_AE_CloudOps~B` · **Authorizer:** `2.0.0_SA_COO` GO @192108Z · **Verifier:** `0.4.0_DS_ClientPlatform~A`
**Status:** `OPEN`

---

## What this is, and what it is NOT

**It is the production deploy of 20 commits that have never run in production, onto a client-facing producer,
in one step** (CTO's framing, promoted to the first constraint). **It is NOT a routine sync.**

**Scope: FOUR EXPLICIT KEYS. No `--delete`. No prefix sync.** COO ruling @191311Z, binding.

---

## Why the gap exists — the MECHANISM, source-confirmed

`mdpf` is **absent from `.tools/safe_deploy_core.py` `PIPELINE_MAP`** (`:22-26` — only `black_diamond`,
`inf`, `cot`). Live invocation: `file_to_s3_target('data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py')`
returns **`None`**. COO re-exercised it with a **discriminating positive control**
(`data/black_diamond/scripts/gold/anything.py -> ('opal-data-bd', 'code/gold/anything.py', 'bd')`).

> **There has never been an automated path that would deploy mdpf gold code. This is not a missed step in a
> working mechanism — there is no mechanism.** Corroborated from the other side: every push today reported
> `safe-deploy -- no deploy-scope script files detected`, four times.
> **THEREFORE THIS REFRESH REPAIRS A SYMPTOM AND THE GAP WILL RE-ACCUMULATE** unless the coverage question is
> answered. Routed to CTO as the substance behind row 19. *Mechanism asserted; intent NOT asserted.*

---

## Pre-deploy state — ROLLBACK TARGETS (captured before any write)

`opal-data-mdpf` versioning: **`Enabled`** (verified live). **Rollback = restore the prior version ID, NOT a
re-upload of an old blob.**

| key (under `code/scripts/gold/`) | pre version ID | pre size | pre LastModified |
|---|---|---|---|
| `dim_mdpf_aggregate_aua_timeseries.py` | `nLuWoyenxWPBDaYFTPj_xt7r_oH2BCCe` | 51,999 | 2026-07-21T17:42:40Z |
| `dim_mdpf_aum_metrics.py` | `HZ2R0h3enypxSN7Gc.jhlJVlWdAnpMYE` | 12,421 | 2026-07-23T10:55:29Z |
| `dim_mdpf_account_distribution.py` | `3m2piQC7rWvxyoqygJHCXJlz5m7RjjO9` | 18,027 | 2026-07-21T17:42:42Z |
| `dim_mdpf_non_model_assets.py` | `KA8Hcq9AOYrIcLjAf5RxEJe6Ch3mRBYR` | 20,381 | 2026-07-21T17:42:43Z |

---

## Deploy-from commit and expected landed bytes

**`554968126d` (`origin/CLOUD`)** — chosen over local HEAD because all four files' last-touching commits are
contained in `origin/CLOUD`, and each blob OID is **identical at `origin/CLOUD` and `HEAD`** (COO
re-verified independently).

**METHOD: upload the GIT BLOB, not the working tree** — `git cat-file blob origin/CLOUD:<path>`. The blob is
LF by definition, so the landed object is **byte-for-byte identical to the artifact the verifier compares
against**; raw byte equality becomes sound rather than tolerated.

| key | blob OID | expected landed bytes | from |
|---|---|---|---|
| `dim_mdpf_aggregate_aua_timeseries.py` | `7cf5462a9` | **124,241** | 51,999 (+72,242) |
| `dim_mdpf_aum_metrics.py` | `a34ef58bf` | **20,135** | 12,421 (+7,714) |
| `dim_mdpf_account_distribution.py` | `8ff806446` | **22,623** | 18,027 (+4,596) |
| `dim_mdpf_non_model_assets.py` | `2b1a02436` | **24,634** | 20,381 (+4,253) |

> **TRIPWIRE, STATED BEFORE THE FACT (given to the verifier at 191750Z):** landed sizes of
> **126,323 / 20,542 / 23,083 / 25,130** mean the WORKING TREE was uploaded (blob + line count, CRLF) and the
> deploy has **FAILED** — it is not a pass to be explained away. *A control that cannot be retro-fitted to my
> own result.*

---

## Why `--delete` is disqualified (6 objects, 3 classes)

- **(A) FOUR ARE LIVE MONOLITH-LINEAGE CODE** sourced from `data/assets/`, not `data/mdpf/` — the cottonwood
  pair + slice builders, `build_dim_model_portfolio.py`, `rebalancer_schemas.py`. A `data/mdpf/`-scoped
  `--delete` **would delete the monolith code from the runner while we are mid-migration TO the monolith.**
- **(B) `backfill/build_custody_crosswalk_cache.py`** (7,907 B) — **no repo source anywhere.**
- **(C) `backfill/.crosswalk_cache.pkl`** (185,393 B) — a built artifact that cannot be re-uploaded from a
  repo, **and its builder is the class-B file.** Unrecoverable in one step.
- `:125` of the dispatch **already carries `--delete` on the S3→box direction**, so a clean box needs no
  second `--delete` on repo→S3. COO has additionally preserved both S3-only objects off-prefix.

**Class A vintage, content-verified (normalised):** `build_dim_model_portfolio.py` on S3 **is HEAD**; pair and
slice each match a real commit **one behind** (`fa491f9b6` 07-23, `ab1f0074b` 07-22). **Stale-by-one-commit,
NOT unversioned** — an earlier raw-byte read suggested otherwise and was a CRLF artifact.

---

## Rollback pin — VERIFIED, and the caveat CTO could not clear is now CLEARED

CTO condition 1 and base lane both flagged: *"versioning Enabled is a bucket property, not proof this version
survives a lifecycle rule neither of us has read."* **I read it.**

```
opal-data-mdpf lifecycle: expire-noncurrent-versions-14d  (NoncurrentDays: 14, prefix "", Enabled)
                          abort-incomplete-mpu-7d
```
> **SO THE VERSION-ID ROLLBACK IS REAL BUT TIME-BOUNDED — 14 DAYS, THEN THE HANDLE EVAPORATES.** That is
> exactly why the independent byte-copy pin was required rather than nice-to-have. **The byte copy is the
> durable rollback; the version ID is the fast one.**

**INDEPENDENT BYTE-COPY PIN TAKEN AND READ BACK** (not trusting the copy's rc):

| key | pinned bytes | sha256 (12) | ETag |
|---|---|---|---|
| `dim_mdpf_aggregate_aua_timeseries.py` | 51,999 | `cd13f202d7c9` | `283b395f660f0de09137282be00b1afe` |
| `dim_mdpf_aum_metrics.py` | 12,421 | `4f060caecbec` | `a9dbddd024bba8fe245219a7cee0ead8` |
| `dim_mdpf_account_distribution.py` | 18,027 | `defd2a394b4e` | `fca2b76ce1e17b42e726fec6f5c7230c` |
| `dim_mdpf_non_model_assets.py` | 20,381 | `dd928907cd01` | `716bc7c7749b854b69fd31916d4e7917` |

The timeseries ETag reproduces the base lane's independently-measured `283b395f660f0de09137282be00b1afe`
exactly — two lanes, same object, same handle.

---

## Dependency check — `comp-pipescript io` (Andrew-direct ~1924Z: comp-tools FIRST)

> **THE FOUR FILES ARE ONE CHAIN, NOT FOUR INDEPENDENT DEPLOYS.** This is the thing the diff does not show
> and a path-extractor cannot see:

```
Order 50  account_distribution      -> writes gold/mdpf_revamp/{firm}/account_distribution.json
Order 60  aggregate_aua_timeseries  -> READS  gold/mdpf_revamp/{*}/account_distribution.json  [runtime-resolved]
Order 70  aum_metrics               -> READS  {49financial,global,inflection}/aggregate_aua_timeseries.json
Order 90  non_model_assets          -> READS  {global,inflection}/aggregate_aua_timeseries.json  [runtime-resolved]
```
Monolith silver reads surfaced by the graph (invisible to a path grep): `fact_assets`,
`fact_model_allocation_roster`, `fact_model_aum_daily`, `fact_portfolios_full`, `fact_rps_s2`,
`fact_allocation_valuation`.

**CONSEQUENCE FOR ANY MIXED-COMMIT PIN:** a pin puts a producer and its consumers on different vintages
across a live producer/consumer boundary. **Checked, with a positive control** — no Order-70/90 consumer at
`554968126d` references the rows-5/6 fields a pin would withhold:

```
dim_mdpf_aum_metrics.py       count_basis 0 · count_as_of 0 · account_count_total_raw 0
dim_mdpf_non_model_assets.py  count_basis 0 · count_as_of 0 · account_count_total_raw 0
POSITIVE CONTROL: the producer at the same commit has count_basis 7, count_as_of 7
```
**The grep would have found them. It found none. The partial pin is downstream-safe.**

---

## Legs

| # | Leg | Status | Evidence |
|---|---|---|---|
| 1 | S3 landing — per-file, verified against the named blob (size **and** sha256), never a `cp` rc | `PENDING` | |
| 2 | On-box sync confirmation — the runner's `:125` pull actually carries the new bytes | `PENDING` | |
| 3 | **First scheduled run** — the real test. `DEPLOYED = downloaded AND imported.` | `PENDING` | |

---

## Watch items for leg 3

- ⚠ **`dim_mdpf_account_distribution.py` IS THE FRONTIER-STAMP SOURCE** and its deployed vintage predates the
  definition DS~A source-confirmed in GC-W2b. **This refresh may CHANGE a served number.** It is the file most
  likely to move output. **The refresh is NOT clean on "no errors" if a served count shifts** — that is a
  result to explain, not noise to absorb.
- The served artifacts were fresh at 07-23T21:47:06Z **carrying classes the deployed code cannot emit**, and
  base `0.7.0` proved the trigger was never invoked 07-19..07-23. **We still do not know what produced them.**
  Changing code under a producer whose current behaviour is unexplained is a reason to watch leg 3 closely.
- A `cp` reporting success while S3 keeps the old artifact is a **same-day estate scar** (the `aws` shim hang
  under `--quiet`). Leg 1 therefore re-reads from S3; it does not trust the upload's exit code.

---

## Rollback

Restore the prior version ID per key (table above) via `aws s3api copy-object` with `?versionId=`, then
re-verify size + sha256 against the **pre-deploy** blob. No re-upload of an old blob, no guesswork.
