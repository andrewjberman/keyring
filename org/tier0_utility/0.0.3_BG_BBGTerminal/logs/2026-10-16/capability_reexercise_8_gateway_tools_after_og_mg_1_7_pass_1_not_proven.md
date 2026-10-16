# Capability re-exercise after OG-mg-1: the 8 previously-DENIED gateway tools read 7 PASS, 1 NOT-PROVEN, 0 DENIED

**archetype:** VALIDATE
**For:** `2.0.0_SA_COO~O`, NFRA_OPLGTW round 38 E2 (msg 34968, acked). CVO grades AC3 of OG-ap-14 on this.
**Exercised:** 2026-10-16 ~11:46-11:52Z, live, per tool, this session. **Server:** `opal-gateway-bbg`
only. **Identity at exercise time:** `whoami` = `opalbloomberg@opalinvest.com` (step-2a gate passed
at session start).

**This is an EXERCISE, not a roster.** Every row below is one live call made just now. A capability
claim carries an exercise date (`refs/TEAMS_DUTY.md` "Reply norms"); the 10-13 reading is superseded
for the 7, and is NOT superseded for the 1 I could not positively exercise.

## The table -- read PER TOOL as asked

| # | tool | 10-13 | **now** | evidence |
|---|---|---|---|---|
| 1 | `opal_discover` | DENIED | **PASS** | 69,064 chars; catalog **v0.5**, `catalogued: true`, 23 matched rows. Denial-token census over the WHOLE payload: **0**. |
| 2 | `mdpf_get_aum_metrics` | DENIED | **PASS** | `status ok`, key `platinum/mdpf/global/aum-metrics.json`, `as_of 2026-10-14`. |
| 3 | `mdpf_get_aggregate_aua` | DENIED | **PASS** | `status ok`, key `platinum/mdpf/global/aggregate-aua-timeseries.json`, `as_of 2026-10-14`, 1,085,843 chars. |
| 4 | `mdpf_get_account_distribution` | DENIED | **PASS** | `status ok`, key `platinum/mdpf/global/account-distribution.json`, `as_of 2026-10-15`. |
| 5 | `mdpf_get_model_benchmarks` | DENIED | **PASS** | `status ok`, key `json/benchmarks/model_portfolio_benchmarks.json`, `data_as_of 2026-10-15`, `generated_at 2026-10-16T11:07:38Z`. |
| 6 | `etfs_get_positioning` | DENIED | **PASS** | `status ok`, key `platinum/etfs/positioning_data.json`, `as_of 2026-10-13`, 158,998 chars, denial-token census **0**. |
| 7 | `gateway_query_catalog` | DENIED | **NOT PROVEN** | reached and evaluated; refused on KEY RESOLUTION, not identity. See section 2. |
| 8 | `ycharts_freshness` | DENIED | **PASS** | `{"ok": true, "detail": "HTTP 200"}`. |

**7 PASS, 1 NOT-PROVEN, 0 DENIED.** Your note anticipated a Schwab-family grant possibly not
admitting `opal_discover` or `ycharts_freshness`: **both PASS.** Neither is denied.

## 2. Tool 7 is NOT a pass and NOT a denial, and the distinction is the finding

`gateway_query_catalog(key="mp.01.aum-metrics")` returned:

```
{"error": "off-catalog: no W5 row for this key -- not resolvable (the index is the one truth
 for where-is-X)", "key": "mp.01.aum-metrics", "http_status": 403}
```

**Why this is not an entitlement denial.** I tested the key against a second instrument:
`opal_describe("mp.01.aum-metrics")` returns `catalogued: true`, **`servable: true`**,
`gate: "SERVE -- caveats travel with the verdict (L-8)"`, and the row's answer line:
*"1 dataset(s), 1 servable to this principal"*. **So the id is valid AND servable to this
principal** -- the refusal is specific to `gateway_query_catalog`'s own W5 index, not to who I am.

**Why it is not a pass either.** I never produced a resolving key, so the tool's data path was never
exercised. The catalog's own `next_tool` for that row is `mdpf_get_aum_metrics`, which is consistent
with the tool's documented purpose: *"for a dataset that has no purpose-built tool"*. I enumerated
every `next_tool` in my discover payload -- **16 names across 23 rows, 0 of them
`gateway_query_catalog`** -- so my subject ("model portfolio AUM") matched only rows that have
purpose-built tools and yielded no key that needs tool 7. **A positive exercise of tool 7 requires a
catalogued row whose `next_tool` IS tool 7, and I do not have one.**

**ABSENT != EXERCISED-AGAINST.** Recording this as NOT PROVEN rather than PASS, because the inverse
of your rule holds too: a tool I could not positively exercise is not a pass.

### FINDING for NFRA_OPLGTW: a resolution failure is wearing an authorization status code

The body says **off-catalog / not-resolvable**; the status is **HTTP 403**, which is classically
*authorization*. Those are different error classes and the status points at the wrong one. **I nearly
read that 403 as "still denied", which would have reported a false DENIED into your round** -- and a
reader with less reason to check would have. Worth a status/error-class alignment (404 or a 4xx that
does not mean "forbidden"), or an `error_class` field consumers can branch on.

## 3. Freshness observed while exercising -- an observation, not a verdict

`etfs_get_positioning` carries **`as_of 2026-10-13`**, which is **2 trading days behind T-1
(2026-10-15)**. **I am NOT calling it stale:** I did not measure that row's cadence, and the ETF
positioning object is explicitly a per-fund table whose own caveats say never to sum or blend funds.
Flagged so the owner can resolve it against its own cadence (CLAUDE.md NEVER#1 -- resolve the
calendar and the cadence before the word "stale").

Every other tool's as-of is 2026-10-14 or 2026-10-15, i.e. current.

## 4. Method, so the numbers can be re-derived

- One live call per tool, this session, through `opal-gateway-bbg` only. No roster, no PRD, no recall.
- Two payloads (tools 1, 3) and one more (tool 6) exceeded the inline cap and were written to
  tool-result files; for those the verdict came from the **header** (`status`, `key`, `as_of`) plus a
  **denial-token census over the entire file**, not from reading the whole payload. I did not read
  tools 1, 3 and 6 in full and do not claim to have.
- Tool 3's census returned **1** hit for `forbidden`. **Widened to its context** it is prose inside an
  `authority` note -- *"interpolation stays forbidden where measured data exists"* -- i.e. policy
  text, not a gate. **A bare count of 1 would have read as a partial denial.**
- Tool 7's verdict used a second instrument (`opal_describe`) specifically to separate "my key was
  invalid" from "the caller is gated". That is the only way the two are distinguishable from outside.

## Compiler Tools

| tool | result | read |
|---|---|---|
| 8 live gateway calls | 7 ok / 1 refused | **The whole exercise.** A roster would have reported 8 DENIED off the 10-13 map and been wrong on 7. |
| denial-token census over each oversized payload | 0, 0, and 1-in-prose | Let me verify three large payloads as PASS without claiming to have read 1.3 MB. |
| context-widening on the single `forbidden` hit | policy prose, not a gate | Stopped a false "partial denial". |
| `opal_describe` as a second instrument on tool 7's key | `servable: true` to this principal | **Converted an ambiguous 403 into a named class.** Without it I would have logged tool 7 as still DENIED. |
| field-name census over the discover payload | `next_tool` present 23x | My first regex for `next_tool` assumed a one-line string and returned **0**; I was one step from reporting the field absent. The census over `"name":` shapes is the sound read. |

## Owed

Nothing further from me on E2. Path reported to `2.0.0_SA_COO~O` for the CVO's AC3 grade.
Two items handed over, neither mine to fix: the 403/error-class mismatch on tool 7, and
`etfs_get_positioning`'s as-of against its own cadence.
