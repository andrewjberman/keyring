# Benchmark defect CLOSED: second re-pull carried Yang's re-saved _ETF CIX to the served key

**archetype:** VALIDATE

**Window:** 2026-10-07 01:13Z - 01:32Z | **Seat:** 0.0.3_BG_BBGTerminal | **Trigger:** msg 30487,
Andrew verbatim *"go, route it"* relayed from the laptop CRO (record @6f6bb92e90).

## Current State

**CLOSED on the served key.** `json/benchmarks/model_portfolio_benchmarks.json`:
`data_as_of 2026-10-05`, `generated_at 2026-10-07T01:28:16Z`, **index_benchmark null 0 of 50**,
**etf_benchmark null 0 of 50**. Confirmed by my OWN S3 read at 01:31Z, independently of
`0.0.0_AB_MSTR~Z`'s read -- it asked for corroboration rather than acceptance, and every figure
matched.

## What I did

Second move-aside + re-pull. I did NOT send: MSTR sent through its own gateway connection, mine
having timed out.

| step | measured |
|---|---|
| collision pre-check | 0 existing `*20261005*bkp2*` -> clear |
| rename | prior pair -> `v1 bkp2` (8,711,802 / 17,919,590); `v1 bkp` KEPT; nothing deleted |
| after | 0 unsuffixed, 2 `bkp`, 2 `bkp2` -- three generations retained |
| pull | tplus1, target 20261005, exit 0, `RESULT: PASS`, **0 `Loading existing data` lines** |

## The three series Andrew named -- 3 of 3, with discrimination

| series | PREV | NEW | rows |
|---|---|---|---|
| `.UST_ETF` | 2026-09-29 | **2026-10-05** | 718 -> 722 |
| `.ST_ETF` | 2026-09-29 | **2026-10-05** | 718 -> 722 |
| `.LT_ETF` | 2026-09-29 | **2026-10-05** | 718 -> 722 |

All 13 custom CIX now end 2026-10-05.

>> **The load-bearing part is not the 3, it is the 10.** Exactly **3 of 13 advanced**; the other
ten held unchanged and POSITIVE CONTROL `SPX Index` held at 2026-10-05 / 1446 rows. A pull that
moved everything would have produced the same three green rows while proving nothing about Yang's
re-save. The unchanged majority is what makes this attributable.

## Served delta across tonight's two sends

| field | pre | after send 1 (00:18:26Z) | after send 2 (01:28:16Z) |
|---|---|---|---|
| `index_benchmark` | 50/50 null | **0/50** | 0/50 |
| `etf_benchmark` | 40/50 | 40/50 | **0/50** |
| `index_spread` | 50/50 | 0/50 | 0/50 |
| `etf_spread` | 40/50 | 40/50 | **0/50** |
| TOTAL return cells null | **288/450** | 153/450 | **45/450** |

`benchmark_last_date` = `{index: 2026-10-05, etf: 2026-10-05}` on all five models (Ultra-Short,
Short, Intermediate, Long, Ultra-Long).

## The residual 45 is STRUCTURAL -- and this is now evidence, not a hypothesis

45 = exactly **15 on each of three volatility fields** (`model_volatility`,
`index_benchmark_volatility`, `etf_benchmark_volatility`).

**`model_volatility` sat at 15 while every benchmark field was null.** A field that was never
broken carrying the identical count is the discriminator: 15 is the FLOOR for periods too short
to compute volatility over, not leftover damage. Earlier tonight I could only say it "looks
structural" because I had one field's count and no baseline; the baseline is what settled it.
**Stating the weaker claim first and upgrading it on evidence is the right order -- the figure did
not change, the warrant did.**

## Carried, not mine

- **Lost receipt on a successful act.** MSTR reports that on BOTH `confirm=True` sends the
  `opalgateway` MCP transport dropped after 120 s and the tool response was lost -- while the send
  landed each time. Placed with `2.0.0_SA_COO~O`. Worth naming the inverse: a send that did NOT
  land would look identical from the caller's side. A dropped receipt is not evidence either way,
  and only the served artifact settles it -- which is how both sends were actually confirmed.
- Both gateway MCP servers read CONNECT_TIMEOUT in my session. **The S3 read path is unaffected**
  (`.tools/aws` shim + `portal_lookup.py`, not MCP) -- which is why I could still verify after
  losing the ability to act. Worth keeping: the measuring instrument and the acting instrument
  failed independently tonight, and only one of them mattered for the truth.
- R1 sign-in coordinate drift still unfixed; `bbcomm` has held the entitled DAPI session with
  `wintrv` ABSENT across 7 samples (15:21Z -> 21:40Z). **Still not established** that it survives
  to the 07:00 fire.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `.tools/aws s3api head-object --query` | detect the republish cheaply | LastModified 16:16:52Z -> 00:18:28Z -> 01:28:1xZ; sizes 19,610 -> 19,652 -> 19,692 |
| `.tools/aws.cmd s3api get-object` | read the served artifact | via PowerShell + native path; the `/tmp/` form returns rc=0 and writes NOTHING here |
| `portal_lookup.py get benchmarks` | the correct served object | the key that actually feeds the view, after yesterday's wrong-artifact error |
| cma interpreter + pickle | CIX last-date census | long-format `groupby("bbg_ticker")`, 13 of 84 tickers, with an SPX control |

**What failed / gaps:** nothing new tonight. The two standing items are unchanged and both
outside my fence: the `/terminal-upload` skill's stale variant path
(`workflows/bloomberg/` vs `integrations/bloomberg/pipeline/`), and `publish_to_portal.py` GATE 3
being unable to express "same date, corrected content" -- which is why BOTH of tonight's fixes had
to go through the gateway rather than the production publish leg.
