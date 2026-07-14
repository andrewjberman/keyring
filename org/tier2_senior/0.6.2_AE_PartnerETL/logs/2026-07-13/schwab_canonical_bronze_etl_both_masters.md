# 0.6.2_AE_PartnerETL -- Schwab canonical bronze ETL: the 11-day silent outage, the REST puller, and an oracle that does not ask the producer how it is doing

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, COORDINATE
**Date:** 2026-07-13 | **Window:** 20:36Z -> 2026-07-14 00:20Z | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Andrew-direct task (in-session, ~20:45Z): investigate the Schwab box pull mechanics for BOTH masters
(08242234 SmartX + 08335338 Black Diamond) and land all history raw at
`opal-data-schwab/{master}/bronze/{type}/{YYYYMMDD}/`, pulled daily.

**FOUND: the 08242234 daily pull has been DEAD SINCE 2026-07-02 and reported SUCCESS the entire time.**
~22 consecutive EventBridge cycles over 11 days, each exiting `rc=0`, each logging *"vendor likely not
posted"* -- while the vendor WAS posting. Proved it by enumerating Schwab's live catalogue: 5,966 files
available for 08242234, including 07-07 / 07-08 / 07-09 / 07-10. The data was sitting there the whole time.

**SHIPPED:** a REST puller (replacing the GUI channel), an INDEPENDENT freshness oracle, and the IAM to
land it. **The 4-trading-day gap is CLOSED** -- 07-07/08/09/10 all landed in the canonical layout.
Full-history backfill (5,966 files) queued.

**Also settled a $1.7b variance three senior agents had wrong**, and killed four separate defects that
would each have silently broken the new pipeline (below).

## Work done

### 1. DIAGNOSIS -- the producer that could not report its own death
The EventBridge cycle (`cron(35 8,20 * * ? *)`) kicks the SI2 GUI task, waits, then syncs. Box log:
```
[2026-07-13T20:35:12Z] delivery baseline newest=2026-07-02T08:37:33Z   <-- FROZEN since Jul 2
[2026-07-13T20:36:10Z] download task exited state=Ready lastResult=0x0 <-- "SUCCESS"
[2026-07-13T20:44:10Z] no new delivery data within 8min -- vendor likely not posted; proceeding
[2026-07-13T20:44:19Z] sync done lastResult=0x0                        <-- "SUCCESS"
```
The box's own delivery folder: newest file `CRS20260701`, written 2026-07-02. The `CRS20260706` data in S3
came from a MANUAL pull on 07-07, not the box. **The GUI channel's last real contribution was July 1.**
Trading-calendar resolved FIRST (NEVER#1): 07-11/12 were a weekend, so the real gap was **4 trading days**,
not 6 calendar days. Discriminated rather than suppressed.

### 2. THE 0833 BOOK -- $1,709,871,264.33 @ 2026-07-10 (Andrew-confirmed)
CTO asked for the one number that would settle an open OPAL_ASSETS variance. Read from the backfill,
read-only, no promote:
```
Net MV Positions            $1,679,098,580.36
Cash Balance Settled Only   $   30,699,884.91
------------------------------------------------
NET MV PLUS CASH            $1,709,871,264.33   <- Schwab's OWN computed total, D2 col[28]
```
`as_of` read from the file's own `H1` header (`H1|SCHWAB|0008335338|49 FINANCIAL|20260710|BDRECPOS|01.06`),
NOT from the filename. Cross-checked against the completely independent CBUGL (UPT+UPN) product:
**$1,679,111,800.69 vs $1,679,098,580.36 -- a delta of $13,220, 0.0008%.**
**Andrew, verbatim:** *"This number is correct from 49F Black Diamond... that is the correct number, it
lands where i expected it to."*

**>> AND THE NEAR-MISS IS THE FINDING, NOT THE NUMBER.** My first pass summed RPS `D1` (positions) and my
own denominator check returned **`OK`** -- because it validated the rows I had ALREADY SELECTED against
themselves. Schwab's own `T1` trailer caught what my check structurally could not:
```
T1: ...|20260710|BDRECPOS|00100550|00100556|
    100,550 = 93,406 (D1 positions) + 7,144 (D2 account balances)
    I had summed 93,406. I was 7,144 rows short.
```
**MATERIAL, not cosmetic: 1,167 accounts hold CASH ONLY and have ZERO position rows.** A D1-only total drops
those accounts entirely plus $30.7mm of cash.
> **A SELF-CONSISTENT CHECK OVER A TRUNCATED READ *PASSES*. THE DENOMINATOR YOU PRINT IS THE DENOMINATOR OF
> YOUR SELECTION, NOT OF THE SOURCE. Only an EXTERNAL oracle -- the vendor's own control count -- caught it.**
Also FALSIFIED CTO's cash-basis hypothesis for the residual $3.36mm (no cash column in the file reproduces
Manav's 1,713.23; reported the null rather than reaching for story #4). Refused to chase the overlap
implication that undercut a Tier-1 analysis -- Andrew ruled summing out of scope three times.

### 3. BUILT -- and every one of these is a defect that would have shipped silently

| # | Defect caught | Why it would have been invisible |
|---|---|---|
| 1 | **Boundary-lossy SDD search** | 1 wide search = 6,933 files; year-chunk = 6,903; month-chunk = 6,669. MORE chunks = MORE loss, **0 HTTP errors**. A naive `from=today/to=today` daily pull is the MOST-chunked search possible = worst case of the bug. Fixed: single wide rolling window + skip-if-landed (one mechanism = daily pull + backfill + self-heal). |
| 2 | **`fam`/`slm` ship `CS{MMDDYY}`, not `CRS{YYYYMMDD}`** | 1,006 of 6,932 files (14.5%). A `CRS(\d{8})` regex drops or mis-dates them, on exactly the 2 types nobody spot-checks. Fixed: partition date from the API's `AsOfDATE`; unparseable RAISES, never skips. |
| 3 | **The two masters ship DIFFERENT products** | 08242234 has `rlw`, NO `fam`/`slm`. 08335338 has `fam`+`slm`, NO `rlw`. My oracle had ONE shared type list -> would have demanded `08242234/fam` **every day forever**. Red day one, muted by week two. *A permanently-red alarm is a guard everyone has agreed to ignore.* |
| 4 | **UTC vs the NYSE clock** | Caught live at 00:10 UTC: box logged `frontier = 2026-07-13` while it was **8:10pm Monday in New York** (frontier should be Fri 07-10). Would have false-paged **every night, 8pm-midnight ET** -- the exact window a nightly cron runs in. **A daytime test cannot see this.** Fixed: `_market_today()` via `America/New_York`. |

**`sdd-daily-pull.ps1`** (REST, replaces the GUI channel):
- Wide rolling window, never `from=today`. Skip-if-landed -> idempotent + self-healing.
- Partition date from API `AsOfDATE`, cross-checked against the vendor's filename-embedded date (both
  encodings). DISAGREEMENT -> hard QUARANTINE.
- **Master OBSERVED from the vendor's bytes, never INFERRED from the request** (CTO~B ruling). No master
  attested -> QUARANTINE. *A default is an assumption with a shorter name.*
- **ZERO FILES ON A TRADING DAY IS A FATAL, not a shrug.** That is the exact cell the GUI channel died in.
- Denominator of the SOURCE: `enumerated == downloaded + skipped + failed` or RAISE.

**`schwab-bronze-freshness`** (the INDEPENDENT oracle -- Layer 2):
- **Reads ONLY landed S3 keys. Never the puller's exit code, log, or manifest.**
- **Denominator from the NYSE CALENDAR, not from the partitions it found** -- so a HOLE in the middle is
  caught, not just a feed that stopped. (CTO's catch; it was a live bug I had already committed.)
- **MUTANT SUITE 5/5** -- control silent, feed-stopped RED, absent RED, **THE HOLE RED** (naive check
  reports OK), healthy-Monday SILENT.

### 4. THE ZIP64 DISCOVERY -- and the ordering that saved us
Andrew instructed unzip-at-ingest. CTO ruled "land BOTH, the `.zip` WINS." I built raw-first, extract-second.
**The extractor then failed on 100% of files:**
```
entry compressed = 4294967295   <-- 0xFFFFFFFF = the ZIP64 sentinel
version needed to extract = 45 (ZIP64); compression method = 8 (plain DEFLATE)
.NET System.IO.Compression -> "A local file header is corrupt."   Info-ZIP + Python read it fine.
```
Schwab writes ZIP64 with sizes in the extra field. **.NET cannot resolve it. This is the platform, not a
patchable bug.**
> **BECAUSE THE RAW LANDED FIRST, WE LOST NOTHING -- 139 raw objects were already byte-perfect in S3 when
> the extractor died. Had we followed "unzip everything on ingest" and kept only the extract, this run would
> have landed NOTHING, or corrupt output, on a $1.7b custody feed. CTO's ruling was load-bearing within the hour.**
Unzip REMOVED from the puller -> moves to SILVER (Python/Linux, where ZIP64 works, and where DS must parse
these files anyway). **A CONVENIENCE STEP WAS FAILING THE LOAD-BEARING ONE.**
**CONTROL MOVING LAYERS, named so nobody finds the gap by accident: the `H1` header cross-check needs the
payload, so it CANNOT run at ingest. SILVER MUST IMPLEMENT IT.**

### 5. IAM -- and the second grant that would have failed SILENTLY
`simulate-principal-policy` (Rule 22a: one `--resource-arns` per call, positive control as a SEPARATE
invocation): `PutObject` on `08242234/bronze/...` -> **implicitDeny**; control on `01_raw/*` -> **allowed**.
Real deny, discriminating instrument. **`comp-iam` could not have found this -- it models `(action)`, never
`(action, resource)`.**
**AND THE NON-OBVIOUS HALF:** the existing `SchwabRawList` carries a `Condition` allowlisting `s3:prefix` to
`01_raw/*` ONLY -- which DENIES listing `{master}/bronze/`. The puller lists that prefix for skip-if-landed.
> **A PutObject deny SCREAMS. A ListBucket deny gets SWALLOWED by the code that depends on it** -- the puller
> would have re-downloaded the entire 3-year catalogue every run, or read the error as "nothing landed yet"
> and done the same, while looking healthy. **An idempotency check that cannot read its destination is not
> idempotent; it is a loop that has not noticed yet.**
Authored `SchwabBronzeList` + `SchwabBronzeWrite`. **Masters ENUMERATED, never wildcarded** -- a `*/bronze/*`
grant would let a mis-scoped run INVENT a master prefix and write there successfully, handing back the exact
guarantee the master-scoped keyspace exists to provide. CTO applied (`e6f618f66`, tag `schwab-si2-iam-v1.1.0`),
negative control confirmed (`99999999/bronze/` -> implicitDeny).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | route the box-IAM terraform question | PARTIAL -- top hit `comp-iam service <lambda>` (score 2.00) does not fit a raw EC2 role; fell through to `comp-grep` as designed (never dead-ended) |
| `comp-grep 'quartz-si2-spike-inline'` | locate the box IAM in TF | PASS -- `infra/aws/terraform/canonical-schwab-ec2/iam.tf:29`, 8 matches / 7 files / 20,498 scanned |
| `comp-grep '08335338' / 'SDDServices'` | find the REST backfill + SDD puller code | PASS -- located `sdd-backfill-08335338.ps1` (the working mechanism) + the whole `canonical-schwab-si2/` harness |
| `.tools/commit-gate.sh` | Rule 14 gate on every .py | PASS (BLOCKED once on ruff F401+E702 -- fixed, re-ran clean; the gate working) |
| `terraform validate` / `plan` | IAM change | PASS -- `0 to add, 1 to change, 0 to destroy` |
| `aws iam simulate-principal-policy` | Rule 22a live-primitive IAM check | PASS -- found the deny `comp-iam` structurally cannot see (it models `(action)`, not `(action, resource)`) |

**What worked:** `comp-grep`'s systems-context output surfaced the whole SDD harness in one call.
**What failed:** nothing blocking.
**GAP FOUND (routed to CTO):** `lib/trading_calendar.expected_last_trading_day()` returns *"today, if today
is a trading day"* -- the last trading SESSION, NOT the newest DATA that should exist. **For a T-1 feed those
differ by one trading day, EVERY trading day.** Any consumer using it as a DATA frontier is either
false-alarming daily or has had its threshold widened to compensate (silently costing a day of real
detection). The freshness probes, `comp-freshness`, and COO's served-aua-stale alarm all import it. **Worth an
estate sweep.** *The function is not wrong; its NAME invites exactly one wrong reading, and the estate is full
of T-1 feeds.*

## Deployment Sequence + Verification (AE)

```
IAM        e6f618f66 -> CTO safe-apply -> 0 add / 1 change / 0 destroy -> tag schwab-si2-iam-v1.1.0
CODE       local -> s3://opal-data-schwab/_ops/canonical-schwab-si2/ (Rule 12) -> box pulls -> SSM console-session
VERIFY     upload byte-count checked BOTH sides (never trust `aws s3 cp` rc=0 -- the shim can hang and report success)
```
**LANDED (ground truth from S3, NOT the puller's self-report):**
```
08242234/bronze/  322 objects and climbing (target 5,966)
  20260707 -> 11    20260708 -> 11    20260709 -> 11    20260710 -> 13     <-- THE 4-DAY GAP IS CLOSED
FAIL count this run: 0
```

## Blockers

**STOOD DOWN ON AN ANDREW HOLD (00:21Z), not a technical blocker.** Andrew, verbatim (relayed by CTO):
*"Wait to dispatch until I give the go, I want to respawn the workers first."* CTO's decision tree ->
**BRANCH 4** (puller in flight). Complied: brought the in-flight unit to a clean checkpoint and stopped.
**Nothing is half-landed. Nothing is lost. Everything restarts idempotently** -- which is precisely why it was
built that way.

## Current State (handoff -- zero prior context assumed)

**STOPPED CLEAN. The 10-day catch-up COMPLETED before the hold arrived -- it was not interrupted mid-flight:**
```
DENOMINATOR: enumerated=57  downloaded=57  skipped=0  failed=0  accounted=57
=== DAILY PULL OK: downloaded=57 skipped=0 enumerated=57 (master=08242234) ===
SchwabBackfill task state: Ready (idle)
```
**LANDED IN THE CANONICAL LAYOUT -- `s3://opal-data-schwab/08242234/bronze/{type}/{YYYYMMDD}/`:**
```
324 objects | 17 types | 77 date partitions | range 20230712..20260710 | ALL .zip (raw, byte-for-byte)
  acc 17  rld 77  rlu 1  rlw 3  rly 4  rps 17  rtu 1  rty 4  sec 17
  tcf 77  tcfx 17  tnn 4  trn 17  uln 17  ult 17  upn 17  upt 17

*** THE 4-TRADING-DAY GAP IS CLOSED ***
  20260707 -> 11    20260708 -> 11    20260709 -> 11    20260710 -> 13
```
**SAFE AT REST:** every object is a complete atomic PutObject of the vendor's raw bytes. Additive only --
`01_raw/` (7,142 objs) and `backfill/08335338/` (6,935 objs) are UNTOUCHED. No in-place rewrites.
**NOTHING CAN AUTO-START:** the EventBridge rule `canonical-schwab-si2-download-schedule` **still targets the
OLD `SchwabAutoDownload` GUI task** -- I never repointed it. Verified live. So the box will keep doing its
harmless nothing until someone deliberately repoints it. **The dead channel is still dead; it is just no longer
the only thing we have.**

- **NOT DONE (the remaining work, in order):** (1) finish the `08242234` full-history pull -- 324 of 5,966;
  re-run `sdd-daily-pull.ps1 -Master 08242234 -Mode download -LookbackDays 1300`, it will skip everything
  already down; (2) same for `08335338` (its 6,935 objects still sit at the OLD `backfill/08335338/` prefix);
  (3) deploy the freshness oracle -- needs TF + an SNS topic name + **CTO condition 1, a DID-NOT-RUN alarm on
  the oracle itself** (*a guard nothing invokes is indistinguishable from a guard that does not exist -- which
  is exactly how the channel we replaced died*); (4) **repoint EventBridge off the dead GUI task** -- the last
  step, and the one that actually turns the daily pull on.
- **Commits:** `339f089f3` (puller + oracle) `74b4d3a30` (calendar denominator + mutant suite) `29b0f38ea`
  (per-master types) `139aef923` (master observed from bytes) `e6f618f66` (IAM) `7a7d5b25e` (raw-only / ZIP64)
  `4809aba22` (NYSE clock). All on `origin/CLOUD`.
- **HELD, untouched:** silver/gold/served re-derives on either master, `ADVI_SCHWABAUTO` (the GUI-automation /
  session-capturer project), `ADVI_BDAPIMIG P1-DURABLE`, `data/black_diamond/`, `opal-data-bd`, mdpf, and
  `s3://opal-data-inf/gold/meta/pipeline-complete.json` (Door 6 -- dispatches the HELD INF chain).
  **Andrew lifted the PULL + RAW STORAGE. He did not lift the pipeline.**
- **⚠️ MY HALT GATE CANNOT SEE A `[STOP]` ADDRESSED TO ME.** My persistent Monitor drains the top-level inbox
  within ~5s; the gate only scans top-level unread. Top-level: 0. `read/`: 235+. **It returns PASS regardless
  of what is sent. Do not treat a HALTGT pass on my work as evidence I was not halted -- require an ACK.**
  Surfaced to CTO; not fixed by me (arch-gated to him).

## Next Steps

- **[0.6.2 self]** Finish the 08242234 full-history pull; run `08335338` into the canonical layout; then
  repoint the EventBridge target off the dead GUI task to `sdd-daily-pull.ps1`.
- **[1.0.0_SA_CTO]** (a) SNS topic name + GO for the oracle deploy **with** its did-not-run alarm in the SAME
  apply; (b) the `expected_last_trading_day()` estate sweep (gap above).
- **[0.4.0_DS_ClientPlatform]** Silver: the CBUGL converter (`UPT`/`UPN`, pipe-delimited -- NOT the RPS
  layout). **You inherit the H1 cross-check** (master + Business_Date from the file's own header) -- it cannot
  run at ingest because the payload is zipped, and Python/Linux is where ZIP64 works.
- **[1.0.0_SA_CTO~B]** cohort-8's `incomplete` will NOT clear when this data lands (mdpf emits no master
  marker, 0/427). **Fix the PRODUCER, never the disclosure.**

## MCP traffic

~18 messages. Significant: **Andrew-direct scope lift** (recorded verbatim +
broadcast same-turn -> CTO ADOPTED the scope read + arch-gated the design). **CTO:** GATE-2 GO (superseded),
arch-gate GO, apply-gate SIGNED, 3 binding conditions (2 of 3 met). **COO:** RAVC-4 close (withdrew his SS6
directive -- *"you were right, I was wrong"*); later asserted `08242234 STILL HELD` -- **I surfaced that his
boundary was wrong** (Andrew named 0824 to me directly, by number); **COO WITHDREW it.** **DS + CTO~B:** scope
corrections (summing is out of scope; record identity, do not resolve the sum) -- ACK'd, and I declined to
chase the overlap even holding the fact that undercut their analysis.
