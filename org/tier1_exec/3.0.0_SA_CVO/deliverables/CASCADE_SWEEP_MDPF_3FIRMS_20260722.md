# CASCADE SWEEP -- MDPF_3FIRMS PRD §2.2/§9 record-vs-live + 3F-B7 spot-verify

**Verifier:** `3.0.0_SA_CVO` · **2026-07-22** · **archetype:** VALIDATE · **Read-only. I fixed nothing,
touched no PRD text, dispatched nothing.**
**Assigned:** CTO cascade 204314Z + scope addition 204947Z, through the Andrew->CTO path.
**Authorization grounded before acting:** LD-0333 am.1 `@2eef569d2` -- dispatch hold `active ->
discharged_in_part`, scoped, single path retained. Verified at source, not accepted from the message.
**PRD vintage swept:** v1.7 `@bde6ef0da`. **All measurements 2026-07-22 ~2045-2110Z.**

---

# PART A -- 3F-B7 SPOT-VERIFY (CTO said this takes precedence)

## >> DECLARED CONFLICT OF INTEREST, STATED BEFORE THE VERDICT <<
**I diagnosed this same anomaly myself this morning** (`work_0544Z.md` item 2, committed `88851665d`):
same mechanism, same 65 IWM portfolios, same conclusion. **0.6.2's verdict AGREES WITH MY OWN PRIOR
FINDING, which is precisely the condition under which I am least critical.** I therefore verified the
headline by *independent measurement of the artifacts* rather than by reading their reasoning, and I
have listed below exactly which limbs I did NOT re-derive. **A verifier who already believes the
conclusion is the weakest instrument in the room; the mitigation is naming it, not claiming immunity.**

## A1. Headline identity -- **CONFIRMED, dollar-exact, both value axes**
Read directly from the served artifacts (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/`):

| | internal `as_of_date` | inflection `model_aua` | `partner_custody_total` |
|---|---|---|---|
| `2026-07-06.json` (9,967 B) | `2026-07-06` | **122,866,033.57** | **202,542,849.81** |
| `2026-07-10.json` (9,689 B) | **`2026-07-06`** | **136,859,722.32** | **202,320,728.81** |

0.6.2 claimed 136,859,722 / 122,866,034 and 202,320,729 / 202,542,850. **Every figure matches to the
cent.** And the mixed vintage is on the artifact's face: `source_vintage.overall = "2026-07-06"` while
`by_feeder.model_aua_positions.inflection = "2026-07-10"`.

**The axis-replacement is structurally confirmed, not inferred:** *both* files carry internal
`as_of_date = 2026-07-06`, so a newest-filename-wins dedup on the internal date necessarily replaces the
true 07-06 partition with the 07-10 snapshot. I did not have to trust the dedup description -- the
collision is visible in the two payloads.

## A2. Source citations -- **CONFIRMED AT THE CITED VINTAGE, positive-controlled**
- `mdpf_aggregate_aua.py:1150 @ed415e268` = `served_as_of_date = source_vintage["overall"] or date` -- **exact.**
- `:1176-1179 @ed415e268` = the `overall forced to min(as_of_by_partner)` rolled-forward rule -- **exact.**
- **Positive control:** file at that vintage is **1385 lines** -- a non-empty read, so an "exact match"
  is not being manufactured out of a broken `git show` (the `fatal:`-on-stderr / clean-empty-stdout trap).

## A3. Probe (a) -- **CONFIRMED by my own read.** `methodology_version = "v0_9_1"` on both partitions I
pulled. **But I record its limit, which the deliverable does not:** a constant tag proves no *recorded*
methodology change. An unrecorded change reads clean. It is corroborative, **not** discriminating on its
own -- and (d) is the limb actually carrying that weight, because a step present inside untouched
same-day bronze cannot have been manufactured downstream.

## A4. NOT RE-DERIVED BY ME -- stated, never implied clean
Probe **(b)** stayed-cohort level test (475 continuing, +$365,247/+0.29%), probe **(c)** full 65-portfolio
decomposition arithmetic and its 07-07->07-08 positive control, probe **(d)** bronze==silver==gold at
every present date. **I confirmed the mechanism these probes exist to discriminate; I did not re-run the
probes.** CTO asked "could they have failed?" -- (c) is the only one carrying its own stated positive
control (a different signature on a quiet pair), which is the right shape; (b) I cannot rate without
re-deriving it.

## A5. B7 VERDICT: **SOUND on the headline; the mechanism is real and dollar-exact.** The repull NO-GO
rests on a mechanism I independently confirmed. **Andrew's closing answer can carry independent
verification for the identity and the stamp mechanism, and a named could-not-verify for probes (b)/(c)/(d).**

---

# PART B -- §2.2 / §9 RECORD-vs-LIVE SWEEP

Instrument routed per Rule 21: `comp-which` -> **`comp-trigger`** (EventBridge/Scheduler forensics,
read-only). **It prints its own denominator and covers BOTH namespaces** -- the structural blindness
that produced the original defect. **Denominator on every scan below: 141 events-rules + 10 schedules,
us-east-1.**

## >> D1 (material) -- §2.2 LEG 2 STILL CARRIES THE CLAIM v1.7 CORRECTED IN §9. <<
§2.2 row `49F-model smartx/platform` still reads **"No EventBridge rule matching `smartx` found."**
§9 corrected exactly that claim in the **same version**. **The document contradicts itself at v1.7**, and
§2.2 is the surface the B-lane TOs are actively consuming. **Believed:** no smartx rule. **Measured:**
present.

## >> D2 (material) -- THE §9 CORRECTION IS ITSELF INCOMPLETE: 7 MATCHES, NOT 3. <<
§9 records "**3** smartx-named rules of 141." That counts **only the events-rules namespace.**

| namespace | name | state | schedule |
|---|---|---|---|
| events-rule | `opal-assets-silver-smartx-sweep-daily` | ENABLED | `cron(0 16 * * ? *)` |
| events-rule | `smartx-account-distribution-daily` | ENABLED | `cron(30 11 * * ? *)` |
| events-rule | `smartx-daily-export-trigger` | **DISABLED** | `cron(0 14 ? * MON-FRI *)` |
| **scheduler** | **`smartx-assets-daily-pull-daily`** | **ENABLED** | -- |
| **scheduler** | **`smartx-rest-pull-daily`** | **ENABLED** | -- |
| **scheduler** | `smartx-jwt-refresher-daily` | ENABLED | -- |
| **scheduler** | `smartx-model-monthly-pull-daily` | DISABLED | -- |

**CTO's own §9 note predicted this** ("Scheduler namespace ... structurally invisible to `list-rules`").
**The measurement confirms the prediction and supplies the names.** The two ENABLED scheduler *pull*
entries are strong candidates for the ingest mechanism **TO 3F-B2 was created to name** -- I am
surfacing that, **not** ruling on the TO. `grounding: comp-trigger smartx, denominator printed.`

## D3 -- eclipse absence claim **REPRODUCES**, now with a denominator and both namespaces
Single hit across 141+10: `opal-assets-silver-eclipse-sweep-daily` ENABLED `cron(0 16)`, FIRED 7x --
**the silver sweep §2.2 already names.** No eclipse-named *puller* in either namespace. §9's eclipse
limb (ruled UNVERIFIED at v1.7) can be recorded **VERIFIED-ABSENT for a name/target scan at this
denominator.** **Residual I will not paper over:** a name/target scan cannot see a puller named nothing
like "eclipse". 3F-B4's Lambda-destinations leg is still owed; **absence-of-a-name is not absence-of-a-
mechanism.**

## D4 -- every named rule + cron in §2.2: **CONFIRMED EXACT, ENABLED, with live fired-evidence**
`canonical-schwab-si2-08242234-daily-pull` `cron(15 10,22)` FIRED 14x · `opal-assets-silver-schwab-sweep-daily`
`cron(15 12)` 7x · `inf-api-assets-v2-daily` `cron(32 13)` 7x · `opal-assets-ingest-mirror-inf-daily`
`cron(15 14)` 7x · `opal-assets-silver-orion-sweep-daily` `cron(0 16)` 7x · `opal-assets-silver-eclipse-sweep-daily`
`cron(0 16)` 7x · `cot-bd-session-daily` `cron(0 2)` 7x · `opal-assets-silver-blackdiamond-sweep-daily`
`cron(0 5)` 7x · `cot-rebalancer-runner-daily` `cron(0 6)` 1x (consistent with a series that started 07-21).
**8 of 8 exact.** This is stronger than the PRD claimed: it asserted applied-truth ENABLED; the tool also
shows the rules *firing*.

## D5 -- silver depth: **6 of 6 CONFIRMED**
`fact_rps_s2` 540 parts 2024-05-24->2026-07-21 · `fact_assets` 2272 parts 2020-04-28->2026-07-22 ·
`fact_portfolios_full` 54 parts 2026-05-15->2026-07-21 · `fact_holdings_s2` 33 parts 2026-06-09->2026-07-20 ·
`fact_model_assignment` **exactly** `07-21`,`07-22` · `fact_model_aum_daily` 9 parts ->2026-07-22.

## D6 (minor, but it misled me twice) -- PATH NOTATION IN §2.2/§9
`fact_model_assignment` and `dim_model_portfolio` live under **`blackdiamond/cottonwood/`**, not under a
`rebalancer/` source (**no `rebalancer/` top-level prefix exists**) and not under the bucket-root `gold/`.
**The data claims are TRUE**; the notation invites a wrong prefix. Bucket-root `gold/` holds **exactly 10
objects** -- which independently **confirms §2.3's "10 objects, `gold/mdpf_revamp/`."**

## >> MY OWN FALSE ABSENCE, RECORDED BECAUSE IT IS THE CLASS UNDER AUDIT <<
My first `fact_model_assignment` probe returned **0 partitions**. That was **my wrong prefix, not missing
data** -- caught by positive-controlling the parent prefix instead of reporting the zero. A second guess
(`gold/dim_model_portfolio` under bucket-root, with `--max-items 4000`) returned another false zero.
**Both would have been "findings" had I reported the first number I got.** The instruction to print
denominators is what caught them. **This is the same failure that produced the defect I was sent to
audit, reproduced by the auditor inside the audit.**

## SCOPE HONESTY
§2.3/§2.4 excluded per CTO. **Nothing behavioral was exercised** -- record-vs-state only, as scoped;
`comp-trigger`'s fired-evidence is CloudWatch metric read, not a path I triggered. No PRD text touched.

---

# PART C -- WIDENED SCOPE (CTO 210204Z): shape-vs-role on the Cottonwood tables

## >> C1 -- MY OWN D5 NEEDS A CORRECTION, AND IT IS THE MOST INSTRUCTIVE FINDING IN THIS SWEEP. <<
I reported §2.2's Cottonwood depth row **CONFIRMED**. That confirmation was **true about the claim as
written and blind to the claim being about the wrong table.** I verified *"does `fact_holdings_s2` have
the stated depth"* -- it does -- and never asked *"is `fact_holdings_s2` the thing whose depth matters."*
**A record-vs-state sweep validates the ROW; it does not validate the ROW'S SUBJECT.** DS caught this
with a parquet footer read; my scan could not have, because it was pointed at the axis the document
chose. *(This is the same shape as VERIFICATION LAW #6 -- enumerate what a number is OF before
explaining it -- and I walked into it while auditing a document for exactly this class.)*

## C2 -- shape read, decisive, one parquet footer each (`date=2026-07-20`)
| table | rows | cols | leading columns | role |
|---|---|---|---|---|
| `blackdiamond/cottonwood/silver/fact_holdings` | **16,762** | **24** | `Market Value`, `Units`, `Unaccrued Market Value`, `Accrual`, `Relationship ID`, `PortfolioID`, `AccountID`, `Account Number` | **the real AUA source** |
| `blackdiamond/cottonwood/silver/fact_holdings_s2` | **5** | **7** | `c1`, `c2`, `_source_file`, `_source_as_of`, `_source`, `_feed`, `_schema_version` | **metadata sheet -- unnamed columns, not a fact table** |

**DS's §1.2 correction (`@58d24b18e`) is CONFIRMED exactly, independently, to the row and column.**

## C3 -- the depth row is RIGHT, for a reason unrelated to the naming defect
`fact_holdings` and `fact_holdings_s2` have **identical partition coverage: 33 partitions,
2026-06-09 -> 2026-07-20.** So §2.2's Cottonwood depth number **survives its own mis-naming.**
**Do not read that as the row being sound** -- it is the second "the coincidence that saved it is not a
design property" instance I have recorded today. **Correct number, wrong subject, and nothing in the
document distinguishes those two states.**

## C4 -- the `_s{N}` trap: CONFIRMED EMPIRICALLY, cross-vendor
| table | rows | cols | what `_s2` means here |
|---|---|---|---|
| `schwab/08242234/silver/fact_rps_s2` | **7,086** | **39** (`custdian_id`, `mstracct_number`, `business_date`, ...) | a **REAL balances table** |
| `blackdiamond/cottonwood/silver/fact_holdings_s2` | **5** | **7** | a **metadata sheet** |

**Same suffix, opposite meaning, in the same bucket.** The PRD's pinned warning is correct and is now
measured rather than asserted: **`_s{N}` carries NO schema contract, and a builder who reads it as one
has no way to discover the error except a footer read.**

## C5 -- CTO's instrument-family question, applied to my own rows
| my row | instrument | silent-absence failure mode? |
|---|---|---|
| D1-D4 trigger rows | `comp-trigger` | **NO** -- prints its own denominator, covers both namespaces, and reports "metric absence != event absence" unprompted. Best-behaved instrument I used. |
| D5 depth rows | `aws s3 ls` + `grep -c 'date='` | **YES** -- a wrong prefix returns `0`, byte-identical to an empty table. **It failed on me twice** (§ "my own false absence"). Only a positive control on the parent prefix distinguishes them. |
| D6 / gold hunt | `list-objects-v2` + `--max-items` | **YES** -- a truncating cap yields a false zero with no signal. |
| C2/C4 shape reads | parquet footer via pandas | **NO** -- a missing file raises; it cannot silently read as "small table". **This is why DS's method caught what every path-based scan missed.** |
**The pattern: every instrument that failed silently on me was one that answers a question with a
COUNT. The ones that could not fail silently either print a denominator or throw.**

-- `3.0.0_SA_CVO`
