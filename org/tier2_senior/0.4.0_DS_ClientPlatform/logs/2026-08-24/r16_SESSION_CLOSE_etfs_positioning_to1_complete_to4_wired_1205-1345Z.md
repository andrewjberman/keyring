# 0.4.0_DS_ClientPlatform — SESSION-CLOSE: ETFS_POSITIONING TO-1 COMPLETE + TO-4 Half 2 wired (2026-08-21 20:05Z – 2026-08-24 13:45Z)

**Serial:** `0.4.0_DS_ClientPlatform` (base, PID 1624) | **Archetype:** BUILD
**Close-out under:** Andrew-direct 2026-08-24 ~13:3xZ, VERBATIM — *"everyone needs to close out
wherever theyre at to a safe position from which to restart with fresh context. Take /log across
fabric for each agent after they reach an appropriate stopping point."* (CTO 66150)
**Seat note from that order:** *"DS — the 3 cottonwood 2026-08-19 CONFLICT writes ride the same
PRD-round question; log and hold."*

---

## SAFE-POSITION ATTESTATION (NEVER#6)

**Nothing is half-landed.** Verified, not asserted:
- `git status --porcelain` over `data/etfs/`, `infra/aws/lambda/etfs-pipeline/`,
  `org/tier2_senior/0.4.0_DS_ClientPlatform/` → **empty** (no tracked modifications).
- **All 11 commits ON `origin/CLOUD`** (`git branch -r --contains` per commit = 1, read not inferred).
- **Zero in-flight S3 writes.** Every write this session completed and was listing-verified.
- All three `STRUCTURAL-TWOPHASE` comp-system overrides **discharged** in-session.
- No cron armed. Inbox Monitor `bl33zxoin` is the only background task.

---

## CURRENT STATE — THE HANDOFF FOR A FRESH SEAT

### What is LIVE right now
```
s3://opal-data-portal-v2/platinum/etfs/positioning_data.json
  76,149 B | LastModified 2026-08-24T12:30:47Z (s3api, UTC) | data_as_of 2026-08-21
  served at /api/general/etfs/positioning_data.json (401 unauthenticated BY DESIGN — auth gate)
  PFDE full n=90 weight_sum 1.0000 | PFOE full n=24 weight_sum 1.0000
  DIVZ / IDVZ  book_only, holdings [] , real book-level values (aum/yield/cost/beta)
  manifest: platinum/etfs/_manifests/2026-08-21/
gold behind it:
  s3://opal-data-assets/portal/gold/etfs/positioning/{book,holding}/date=2026-08-21/
```
⛔ **THIS ARTIFACT DOES NOT REFRESH ITSELF.** There is no producer schedule yet (that is AE's TO-5).
Today's bytes exist because I ran the chain by hand. **It will silently age until TO-5 lands.**

### The files I own
| Path | State |
|---|---|
| `data/etfs/scripts/gold/etf_positioning_gold.py` | stage 1, (a) plane → gold parquet |
| `data/etfs/scripts/gold/etf_positioning_publisher.py` | stage 2, gold → platinum JSON |
| `data/etfs/scripts/gold/test_etf_positioning_upgrade_forward.py` | **33/33 PASS** |
| `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py` | TrueShares call site wired |
| `.../deliverables/ETFS_POSITIONING.TO-1_PROOF_OF_SPEC.json` | **VALID rc=0, 6/6** |
| `.../deliverables/ETFS_POSITIONING_TO-1_SUB_ASSET_CLASS_VOCABULARY_v1.md` | the Rule-24 act |
| `.../deliverables/ETFS_POSITIONING_TO-1_INVOCATION_CONTRACT_FOR_TO-5.md` | AE's build input |

**NEITHER PRODUCER STAGE IS DEPLOYED.** Deliberate: deploying a producer nothing triggers is the
"pipeline with no schedule" shape one step early. The deploy lands **with** AE's trigger TF.

### Commits, all ON `origin/CLOUD`
`71265d372e` build · `990db50065` proof · `330052e2f5` proof+contract · `cdf78fd70b` **unit fix**
`b682443d36` **AC5 + trading-day fix** · `4e5800fde0` **TrueShares call site** · `3f5f18425b` cash
inference · `b4c92deb21` contract correction · `42dda5bb1f`/`759be6194d`/`46b40a0a29` comp-system
discharges.

### Premises a fresh seat MUST re-verify rather than inherit
| Premise | The primitive that falsifies it |
|---|---|
| Artifact is current | `aws s3api head-object --bucket opal-data-portal-v2 --key platinum/etfs/positioning_data.json` — compare `data_as_of` to `expected_last_trading_day` |
| Producer still has no schedule | `comp-trigger etf-positioning` (was: NO MATCH / 136 rules + 18 schedules) |
| bbg landing is scheduled, not ad-hoc | `bbg/{date}/run_manifest.json` → **`run_class`** field. NOT the partition list |
| DIVZ/IDVZ still shells | the served artifact's `holdings_status` per book |
| TrueShares capture live? | `TS_HOLDINGS_ENABLED` in the deployed function env **AND** DIVZ/IDVZ rows in `silver/holdings/` by **DISTINCT** count |

---

## OPEN, WITH OWNERS — none of it mine

1. **AE — TO-5**: producer schedule + Lambda TF. Sizing given from measurement (512 MB / 120 s).
   Parked at committed-not-applied per the close-out order.
2. **AE — TO-4 tail**: deploy `etfs-netassets-daily` **and set `TS_HOLDINGS_ENABLED=1`**.
   ⛔ **Without the env var the deploy looks successful and changes nothing** — the flag defaults
   off and the log prints `SKIP: [divz] trueshares holdings disabled`. At Andrew as land-before-close
   vs wait.
3. **DT** — page promote, on Andrew's word.
4. **COO** — D1_CATVIEWS decomp parks at its cell boundary; my read-ahead (66166) is with them.
5. **PRD round** — the 3 cottonwood 2026-08-19 CONFLICT writes (my seat note), and BQL entitlement.

---

## FINDINGS THAT OUTLIVE THIS SESSION

**1. The as-of resolver picked a SUNDAY.** I took the frontier from `lib/trading_calendar` and then
filtered the *candidates* without it. **Using the right instrument for one half of a comparison is
not using it.** It failed loud only by luck of an upstream schedule — had bbg written weekend
partitions it would have published Friday's numbers stamped Sunday, silently, with every structural
check passing. Fixed; selection extracted into a **pure testable function** (`select_as_of`) because
the defect needed a real Saturday in the bucket to appear and three days of green runs said nothing.

**2. A contract that fixes NAMES and omits UNITS hands the producer a decision it does not know it
is making.** Weight was 100x, holding aum 1e6x, `active` a bool the renderer read as "NO". Every
structural check passed. Caught by Andrew on the live page, not by me. Control added: a full book's
weights must sum to ~1.0; both mutants fire.

**3. A foreclosure claim I propagated was false.** I repeated "BAD_FLD not NOT_AUTHORIZED means
Bloomberg does not have the constituents" to Andrew. Site Z falsified it — BQL is **entitlement**-
walled and Bloomberg **does** hold them. The measurement was true of the *field* surface and I
generalised it to *all* surfaces. Corrected to Andrew directly. **A foreclosure is the most
expensive kind of wrong claim because it is a reason to stop looking.**

**4. A requirement stated as a MECHANISM sends the reader to build the mechanism.** I wrote
"trading_calendar must be on the layer at /opt/python/lib/" when the need was "must be importable."
AE pushed back rather than minting a layer for a 7 KB module; I reproduced their layout, verified
the import, and corrected the doc.

**5. Cash inference — gold taking a hand-off silver DECLARED.** The TrueShares capture emits
`is_cash: None` deliberately (Rule 17 puts that judgment at gold). Untaken, every cash row would
have landed as an **equity with no sector** and its weight counted into `alloc_equity` — wrong
allocation on a client-facing page, the day DIVZ/IDVZ rows arrive. Closed before it could fire.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-find` | Turned the vocabulary act from a MINT into an ADOPTION (12/12 values already in-estate); found the platinum-publisher precedent; measured the D1 registry's **zero code consumers** estate-wide |
| `comp-estate --definitions` | 65 ratified terms, zero collisions with the proposed vocabulary |
| `comp-trigger` | Established the schedule precedent AND measured AC4's true state (0 matches / 136 rules + 18 schedules) |
| `comp-system` | Three recompiles, each discharging a STRUCTURAL-TWOPHASE override |
| `comp-pipescript` | Ran for the deploy pattern; **exceeded its 120s window and was backgrounded — no conclusion rests on it**, recorded so the inventory is not overstated |

---

## Blockers

**None at this seat.** Everything remaining is owned elsewhere and named above.

## Next Steps (for the fresh seat, after the PRD round)

1. **Capture-first** (CTO's word): once AE's TrueShares deploy lands, verify DIVZ/IDVZ rows by
   **DISTINCT** constituent count — never row count, which grows on re-capture and proves nothing.
   Expect ~30 / ~46 as a sanity range only; **a count is not a list.**
2. Deploy both producer stages via `safe-deploy` **when the trigger TF is committed**, not before.
3. D1_CATVIEWS round-1 cells from COO's decomp. **Do not start TO-D1b/c/e — those are 08-19 TOs**
   and Andrew's clause excludes old TOs; wait for the re-cut.
4. Re-run the artifact-currency primitive above before trusting anything on the page.

**HOLDING per the close-out order.**
