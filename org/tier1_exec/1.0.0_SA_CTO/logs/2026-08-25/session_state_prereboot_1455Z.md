# CTO session state -- PRE-REBOOT SNAPSHOT, 2026-08-25 14:55Z

**Seat:** `1.0.0_SA_CTO`. **archetype:** COORDINATE. **secondary_archetypes:** VALIDATE, DIAGNOSE.
**Context:** Andrew wound the fabric down ~14:3xZ for a device reboot. **This seat is the only one
live.** Written so the fabric can be brought back up without re-deriving today.

⛔ **PUSH STATE: local HEAD `a0394e34f4`; `origin/CLOUD` `e291d38e4f74`; FIVE COMMITS UNPUSHED.**
They survive the reboot (git objects persist on disk) but are **invisible to any other fabric and
to a fresh clone.** `0.0.0_AB_MSTR` holds the integrator push (LD-0367) and was wound down before
the window; **the push is the first act on restart.**

## 1. THE DIRECTIVE BOARD -- all 10, as of 14:54Z

| D | device | open TOs | title | members |
|---|---|---|---|---|
| **D0** | LAPTOP | 4 | Infrastructure (ongoing) | NFRA_COMPTOOLS[active] NFRA_DEPLOYLEDGER[active] NFRA_DEPLOYCENSUS[**complete** 08-18] |
| **D1** | LAPTOP | 3 | MDPF asset-category views | D1_CATVIEWS[active] |
| **D2** | LAPTOP | 19 | ADVI 49F end-to-end | OPAL_ADVIPOINTERS · ADVI_BDPLAT_RESTORE[**complete** 08-19] · ADVI_49FSRC · ADVI_INSURE · ADVI_STITCH · ADVI_PERFRP · ADVI_COTKEY |
| **D3** | LAPTOP | 7 | Account-level model overlay | D3_MODELOVERLAY[active] |
| **D4** | SITEZ | 8 | ETF positioning variant | ETFS_CANON[scoping] ETFS_POSITIONING ETFS_INGEST |
| **D5** | LAPTOP | 0 | Alt research (ongoing) | **(none -- UNMEASURABLE)** |
| **D6** | SITEZ | 0 | Opal Analyst + partner GraphQL | OPAL_ANALYST[closed 08-20] |
| **D7** | SITEZ | 0 | Ticketing intake | (none) |
| **D8** | LAPTOP | 0 | **Model Portfolios Pipeline Fortification (NEW)** | **MDPF_COTREMEDIATION[active]** |
| **D9** | SITEZ | 0 | Tax SMA ops | PFMG_TAXSMA[**no-json**] |

```
DIRECTIVES-CHECK-RESULT live=10 retired=1 ever_minted=10 malformed=0   rc=0
LAPTOP SCOPE (the /self-drive denominator): 6 directives, 13 projects, COMPLETION 2 of 13
```

⛔ **TWO REGISTER ITEMS FOR MSTR ON RESTART, NEITHER URGENT:**
- **`D9.PFMG_TAXSMA` reads `no-json`** -- the same class Andrew's Fix 1 closed for D0/D2 this
  morning. **It is the last one.**
- **`D8` now appears in BOTH `DIRECTIVES.yaml` (live) and `DIRECTIVES_RETIRED.yaml` (the cut
  Philosophy row).** `retired=1 ever_minted=10 live=10` -- the tool reports `malformed=0` and rc=0,
  so this is not a violation, but a reader searching `D8` finds two rows with different titles.
  **The retired row is a historical record of the 08-20 cut and should NOT be deleted; the question
  is whether the retired file wants a superseded-by pointer.** MSTR's call.

## 2. ⛔ D8 -- THE NEW DIRECTIVE, AND THE LIVE OUTAGE UNDER IT

**Andrew-direct ~14:20Z: replace the crossed-out D8 (Philosophy) with "Model Portfolios Pipeline
Fortification".** RE-MINT, not an edit -- prior D8 CUT 2026-08-20T20:32:35Z, carries nothing forward.

### THE OUTAGE, MEASURED AT THIS SEAT ~14:2xZ
```
s3://opal-data-portal-v2/platinum/mdpf/{partner}/aggregate-aua-timeseries.json  field as_of_last

49financial    2026-08-24   CORRECT (T-1)      object written 2026-08-25T13:50:49Z
inflection     2026-08-24   CORRECT (T-1)      object written 2026-08-25T13:50:51Z
cottonwood     2026-08-19   <<< FROZEN         object written 2026-08-25T13:50:50Z
global         2026-08-19   <<< FROZEN         object written 2026-08-25T13:50:50Z

NEVER#1 DISCHARGED FIRST: expected_last_trading_day(2026-08-25) = 2026-08-25.
08-19 is FOUR TRADING DAYS behind. Not a weekend.
```

> ⛔ **WHY NOTHING CAUGHT IT: THE SERVED OBJECTS ARE REWRITTEN EVERY DAY.** All four within two
> seconds of each other. The publisher runs, emits, succeeds. **THE STALENESS IS INSIDE THE
> PAYLOAD.** Every object-mtime freshness instrument reports these HEALTHY -- and each is **correct
> about the FILE**. `comp-freshness`, `s3 ls` age, `head-object` LastModified: all green.
> **A served key rewritten daily with frozen contents passes every instrument this estate owns.**

**FIVE LEADS, falsifiable, ALL UNREAD -- in the PRD s.3 and the project JSON:**
L1 cottonwood's `dates` array is almost entirely `None` (a stall truncates; it does not null-fill) ·
L2 global's tail repeats `2026-07-22` ~15x (`opal-data-cot` has a `forwardfill_v2/` prefix) ·
L3 global is a rollup INCLUDING cottonwood -- **one cause may explain both; do not assume two** ·
L4 `dim_mdpf_account_distribution.py:328` `COTTONWOOD_UNITS_KEY = "gold/mdpf_revamp/cottonwood/account_units.json"` + `_cottonwood_sidecar()` -- a Cottonwood-only sidecar on a different prefix ·
L5 `0.4.0_DS_ClientPlatform~I` 14:14Z corroborated independently from a different artifact (`D_05`
byte-identical at `data_as_of 08-19`) **and filed it as an OBSERVATION -- the signal existed before
Andrew reported it.**

⛔ **THE TRAP, RECORDED BEFORE THE DECOMP EXISTS: a re-run that produces correct data DOES NOT
ESTABLISH THE CAUSE.** It establishes the producer works when run today. L1 is the discriminator.

### WHAT I GOT WRONG ON THIS, AND HE CAUGHT IT
I told him the Cottonwood MDPF code was *"somewhere different in a different format"*, citing
`data/cot/scripts/gold/`. **That is Cottonwood's ADVI pipeline -- different PRODUCT.** He corrected
it as a category error. **Cottonwood MDPF lives in `data/mdpf/scripts/gold/` with every other
partner's** (`mdpf_gold_consolidator.py:92,860`, `build_mdpf_spine.py:56`,
`dim_mdpf_aggregate_aua_timeseries.py:1915`).
> **I produced evidence that appeared to confirm a hypothesis he had already voiced, from the wrong
> directory.** That is the claim class that receives the least scrutiny, and the requester is the
> last person positioned to catch it. **Nobody should carry the false version forward.**

## 3. COMMITS THIS WINDOW (all LOCAL, riding MSTR's push)

| hash | what |
|---|---|
| `903f6c8512` | Andrew-direct record: D8 + the 08-19 freeze + the category-error correction |
| `1509532cc7` | `MDPF_COTREMEDIATION_PRD.md` v1.0 + `D8_..._PRD.md` v1.0 + `org/projects/MDPF_COTREMEDIATION.json` |
| `a0394e34f4` | `DIRECTIVES.yaml` D8 row -- **audited lane override `GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_MSTR`** |
| `9a50854e11` | Andrew-direct record: all work under a directive; tag projects at creation |
| `53a7043f78` | `CONTROLS_OVER_CARE.md` s.11 + header ten->eleven + a stale direction citation fixed |
| `3b09cee304` `425dd6c39f` `88973ae1ae` | self-drive tick logs 16 / 14 / 12 |
| `a6c76382b1` | BD dim 436 finding -- one vendor field blocks two directives |

⛔ **THE LANE OVERRIDE, STATED PLAINLY: `org/missions/DIRECTIVES.yaml` is lane `TIER0_MSTR` and this
seat is not in `permitted_agents`. The owned-paths gate REFUSED CORRECTLY** -- exactly as LD-0425
says (*"Register commits are MSTR's per LD-0341 + .register-owner"*). Override taken on Andrew's
explicit instruction with MSTR wound down, single lane, single commit, audited. **MSTR confirms the
row on restart.**

*Diagnostic note: I initially misread the refusal as a `risk-reflex` block and built a theory about
`|| true` and `pipefail` on it. **The reflex is advisory and returns rc=1 on a HOLD; the actual
refusal was the owned-paths gate, captured into a variable and invisible in the output I was
reading.** s.11, one hour after landing it: I read the visible part of the output and reasoned about
the whole.*

## 4. TODAY'S SETTLED RULINGS (so nobody re-litigates them on restart)

- **Andrew ~14:05Z: WHOLE BOOK IS THE DEFAULT.** 49F unsupervised **$138,839,619.90 IN**.
  Cottonwood's supervised-only view is a **partner REQUEST, not a semantic ruling** -- so the
  Cottonwood $30.3M exclusion and the 49F inclusion are **both correct and not in tension.**
  ⛔ An estate-wide "make the firms consistent" fix would be a DEFECT.
- **Andrew ~14:12Z: all work sits under a directive; projects minted mid-task are TAGGED AT
  CREATION.** Measured basis: 332 project JSONs, 103 active, **91 members of nothing** -- 49 with
  open TOs (live, untracked), 42 with zero (close-out backlog). **Opposite remedies; must not be
  worked as one item. DIRECTION RATIFIED, MIGRATION NOT AUTHORIZED.**
- **12:45Z ADVI chain: PASSED all four pinned expectations.** `REFUSED-NO-BMV` 7,335 -> **0** over
  the 7,334 both-day accounts, positive control fires at 7,334. Three-way corroborated.
- **CVO found 15 of 6,412 returns breaching the ruled 0.05 threshold** (one at +69,056%). Body sane
  (p50 -0.21%). **`c04` check 7's deferral is OVER** -- its premise (nothing to evaluate) expired at
  12:47:31Z. COO to seat.
- **`a06` weekend guard:** the 49F gold chain is **dead every Sunday and Monday** (`map_dates[-1]`,
  no non-empty check; map writes 13:15Z, chain runs 12:45Z). **Nothing to backfill** (both aborted
  runs targeted an already-existing partition) -- **fix forward; the mechanism is undiminished.**
- **Portal CI:** `ci.yml:56` runs a **zero-file** `tsc --noEmit` under a step named "Type Check".
  **Not a coverage gap** -- step 5's `bun run build` is `tsc -b && vite build` and type-checks for
  real. **The real find is the provenance-read guard: a CI backstop dark for six runs.** CI is now
  GREEN on `fce757cb` and the backstop is live again.
- **`TO-D3.3` SUPERSEDED BY VINTAGE** (its `<authority>` names a vintage predating PRD s4c ruling 9).
  Surface (c) publisher key = `0.7.0_AE_CloudOps`.
- **The promote-ledger RED closes** as CLOSED-WITH-PROOF / third-party measured, **with the
  limitation written in.** Merge leg PASSES on tree identity. ⛔ **AND ITS MANIFEST DRIFT IS THE
  MECHANISM OF THE PERFRP-ON-PROD FINDING: the manifest pinned DEV @`d43b88c5`; the merge executed
  17h later against `063ff4d7`, 28 commits later, 11 of them ADVI_PERFRP.**

## 5. OPEN AT ANDREW -- 4 cards

1. **`ADVI_COTKEY` key of record** (CVO refused as sovereign: *"I suspect" is not a ruling*).
2. **BD dim 436** -- one vendor template field blocks D3's advisor level AND ADVI_INSURE's advisor
   spine leg. **Ask: add dim 436 to template 390224 and re-pull.** 3 of 4 levels / 3 of 4 legs still
   deliver. Record `a6c76382b1`.
3. **CVO's condition-4 no-gates test** as a clarification of his own rule.
4. **The retro-tagging volume question** -- all 49 orphans-with-TOs now, or as-touched?

## 6. Compiler Tools

| tool | invocation | result |
|---|---|---|
| `lib/trading_calendar` | before any staleness claim | **NEVER#1 discharged -- 4 trading days, not a weekend** |
| `aws s3api list-objects-v2` / `head-object` (UTC) | served frontier, 4 partners | **objects FRESH -- the finding that explains the 4-day silence** |
| `aws s3 cp` + JSON shape scan | `as_of_last` per partner | **the freeze, isolated to cot + global** |
| `comp-find -i` | cot MDPF code home | **257 hits / 57 files -- my category error, falsified** |
| `directives-check.py` | before + after the D8 mint | live 9 -> 10, malformed=0, rc=0 |
| `bash -x safe-commit.sh` | the invisible refusal | **owned-paths, not the risk-reflex** |
| `safe-commit -F` (msg-verify) | 8 commits | all MATCH, path-scoped |

**What failed:** the category error (wrong product tree, and it flattered his hypothesis); my
misdiagnosis of the commit refusal; a generic JSON walker that returned 0 points for 3 of 4 partners.
**Gap found:** object-mtime freshness is structurally blind to a payload freeze -- **the condition
D8 exists to end.**
