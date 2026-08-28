# CTO~Z — D1 + D4 architecture gate, post-kill fabric, 0045-0435Z

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 00:45Z -> 04:35Z (first log of this session;
predecessor closed with the handoff @`9728617de3` at the fabric kill)
**Basis:** ANDREW-DIRECT "bring tier1 agents on, they need to finish D1 and D4", then four further
sovereign messages in-window (scope, comp-find bulletin, smoke-test feedback, INT default).

---

## 1. WHAT THIS WINDOW WAS

Post-kill relaunch. Fabric grew 4 -> 14 live seats. **Andrew smoke-tested the Satellites view at
~04:2xZ and it PASSED** ("looks very good, its basically done") with three change requests, plus a
fourth item (INT default) at ~04:3xZ. That is D4's reserved bar, exercised.

⛔ **NOT A CLOSURE.** His standing word is *"definitively done"*; he said *"basically done ... a
couple points id add"*. The points are the remaining distance and nobody writes a closure.

## 2. RULINGS ISSUED (13; full text @`a25b663169`, amended @`fb89150b94`)

| # | Ruling | State |
|---|---|---|
| 1 | GICS industry group is a **NEW PARALLEL field**; `sub_asset_class` not overwritten | stands |
| 2 | Book-grain satellite return is **PRODUCER-SIDE or ABSENT**, never client-side from snapshot weights | stands |
| 3 | The **PRODUCER converts** constituent weights to percentage; consumer contract does not move | stands |
| 4 | First-leg-wins guarded on **`returns` agreement**, not shared `as_of` | replaced the as_of form |
| 5 | Satellites fetch: scoped route, firm resolved to **BUCKET** never a key segment | stands |
| 6 | Do NOT strike the "WHY THERE IS NO PREDICATE" section; strike its conclusion, keep the sweep | stands |
| 7 | `BLOCKED-BY-GATE` + its `required:["status_reason"]` conditional as ONE act | CVO CERTIFIED w/ findings |
| 8 | **A directive or status claim carries its VINTAGE**; one without is a HYPOTHESIS | adopted fabric-wide |
| 9 | GICS condition-(ii) work runs BESIDE item 2 (working assumption, reversible) | stands |
| 10 | Served key `industry_group` OPTIONAL snake_case **+ `industry_group_basis` beside it** | LIVE on running bytes |
| 11 | ~~two edge changes are ONE DEPLOY~~ | **WITHDRAWN** — premise falsified by a plan |
| 12 | **APPLY != SHIP** on Lambda and edge tiers | stands |
| 13 | A criterion retired UNREACHABLE must **name the event that lifts it** | stands |

**Also ruled in-window:** never edit evidence to satisfy an instrument (cell_refs / status enum);
AC3 terminal-withheld (refused rewriting a landed partition to pass a check); internal viewer is not
a firm, so the router's 400 is correct and the UI was missing a selection; `MODEL_BOOKS` order is an
index contract for the blend, so change the DEFAULT never the ARRAY.

## 3. WHAT I GOT WRONG (7, each caught by a peer or by my own later measurement)

| Claim | Truth | Caught by |
|---|---|---|
| "GOLD HAS NEVER RUN" (relayed, no vintage) | running daily, `run_class: scheduled`, 3 days | my own measurement |
| condition (i) DISCHARGED on the data plane | 4/4 FULL is a **lucky Tuesday** — one `as_of` for four funds | `2.0.0_SA_COO~Z` |
| satellites fetch prefix | `/api/scoped/satellites/` — built that way **by my own B1 ruling** | `0.7.0_AE_CloudOps~S` |
| "the AE half may be DONE" | route DESIRED, **0 of 26 behaviors** deployed | `0.7.0_AE_CloudOps~S` |
| binding-now row 11 says strike | I ruled against **my own table** without reading it | myself, late |
| ULT = Ultra-SHORT -> ladder broken | **Ultra-LONG**. No anomaly existed | `0.4.0_DS_ClientPlatform~L` |
| "Andrew can smoke-test on DEV" | **there is no DEV site** — CI validates, only PROD deploys | myself, on his question |

⛔ **COMMON MECHANISM: I reasoned from a SUMMARY of my own ruling instead of the ruling.** A handoff,
a status line, a binding-now row quoted from memory are lossy copies that **read as citations**, so
the usual unsourced-feeling tell never fires. Banked to memory.

## 4. Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-state` | `--self-test` | **PASS 4/4** | gated the /exec-sum drift half |
| `comp-find` | `-i` token census, 4 tokens + 3 baselines | **PASS** | printed denominators are what made the Rule-24 proposal a proposal |
| `comp-which` | A.3 startup exercise + gold-schedule search | **PARTIAL** | correctly DECLINED to route the schedule question; near-tie surfaced, no silent guess |
| `comp-routes` | `rewrites` | **PASS + trap** | found the scoped-route family; **its own printed DESIRED-plane bound is the one I then violated** |
| `comp-estate` | `--resource etfs` | **PARTIAL** | 1 chain, not the serving surface; fell back to a rail-checked TF read |
| `to-check.py` | `--all` | **PASS** | surfaced 5 stale ETFS_POSITIONING faces + `unresolved_serials=42` rather than a silent zero |

**What worked:** `comp-find`'s printed denominator, and `to-check` DISCLOSING its unresolved residue
instead of reporting zero — both turned an assertion into a measurement.
**What failed:** nothing returned a wrong answer. `comp-estate --resource etfs` was simply the wrong
instrument for a serving question.
**Gap found:** ⛔ **`comp-find` DOES NOT LOG.** `0.7.0_AE_CloudOps~Z` measured 0 of 3,648 rows in
`comp-tool-runs.jsonl` while having run it — 23 other tools log. Anyone checking uptake on the tool
Andrew named in his bulletin reads ZERO forever, indistinguishable from total non-adoption. Surfaced
to the D0 / `0.8.0_AE_CloudComp` class (laptop-placed); NOT chased.
**Second gap:** Rule 21's "live hard-deny" is **half true** — the `infra/*.tf` grep limb fired on me;
the raw-`aws` INSPECTION limb did not fire for two seats on two command shapes. Open call at Andrew.

## 5. MCP traffic

~95 messages sent, 12 broadcasts. Significant: 4 ANDREW-DIRECT records + same-turn broadcasts (scope,
comp-find bulletin, smoke-test feedback, INT default); 13 architecture/taxonomy rulings; the
BLOCKED-BY-GATE proposal to CVO; the vintage-law ruling to 7 seats; 6 self-corrections to the same
list I had ruled to.

## 6. Blockers

**NONE at this seat.** Every gate discharged. Verified: no D1/D4 item lacks an owner (the one that
did — `D1_CATVIEWS.TO-I1-DS`, dead seat `~T` — was re-seated at 03:56Z, `pid 30236`, confirmed live).

## 7. Current State (for a reader with zero context)

**SERVED / DEPLOYED, measured on running bytes:**
- `s3://opal-data-cot/platinum/satellites/registry.json` — 2,196 B, `as_of 2026-08-27`, 9 books,
  9/9 summing to 100.000 within the consumer epsilon, `claim: measured`.
- `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json` — 128,122 B, last scheduled write
  2026-08-27T13:01:25Z, 4 books / 4 FULL / 0 SHELL.
- `etf-positioning-producer` Lambda — `CodeSha256 EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=`,
  4 members incl. `BUILD_MANIFEST.json`, `source_vintage` pin `25f30acc63` (carries TO-7 per-fund
  as-of). `HOLDING_KEYS` arity **15** — `industry_group` AND `industry_group_basis` both served.
- CloudFront `EVTSA9VEHNZVH` — 27 behaviors; `/api/scoped/satellites/*` origin-request ->
  `shared-advisor-router:25` (post-satellites version).
- `cot-satellites-registry-producer-daily` — `cron(0 7 * * ? *)`, **ENABLED**, targets the right
  function. Last producer run 01:39:12Z was **ad-hoc**; first SCHEDULED fire **07:00Z**.
- `mdpf-scheduled-floor` — ENABLED on the **EventBridge Scheduler** plane (NOT Rules). ⛔
  `gold-lambda.tf` claimed "DEPLOYED UNWIRED ... only ad-hoc QA" — **false, corrected @`89c6409419`**;
  read literally it argued FOR the act that destroys `TP1AE-AC1`.
- portal `origin/DEV` = `8c2ba9bb` — design pass + firm selector. ⛔ **NOT PUBLISHED ANYWHERE.**
  `ci.yml` on DEV validates only; `deploy.yml` on PROD is the sole publish path; one site origin
  `opalinvest-portal`. **There is no DEV site.** Local run only.

**TIME-TRIGGERS (no session survives to these):**
- **07:00Z** satellites registry producer, first scheduled fire.
- **13:00Z** ETFs producer — proves the GICS chain end to end.
- **13:30Z** mdpf scheduled floor — `TP1AE-AC1`, and the DE fixture re-derivation gates on it
  (NOT on 13:00Z — corrected before the cell was cut).
⛔ **NO AD-HOC RUN BEFORE EITHER.** The wait IS the evidence; an early fire destroys the discriminator.

**ANDREW'S FOUR OPEN ITEMS (all cut/seated, none blocked):** hide Satellite 98 (render-layer filter
ONLY — registry keeps 9, page shows 8); no firm selector (comment, do not delete, default cottonwood);
colour gradient orange->red starting at Satellite 15 leftmost across the 8 displayed books; INT default
for **new users first visit only** (his 08-24 remembered-choice ruling stands; layer 2 sits above
`books[0]` and may short-circuit).

## 8. Next Steps

1. **[2.0.0_SA_COO~Z]** Reconcile 4 world-done `ETFS_POSITIONING` faces (evidence filed @11743/11751)
   — the driver cannot read "complete" while they read ACTIVE. Do NOT sweep `TO-P1-AE`: zero movement
   for ~9h is BY DESIGN.
2. **[2.0.0_SA_COO~Z]** Two re-facings from ruling 13: `INGEST-TO5-AC4` KNOWN-UNREACHABLE ->
   GATED-ON-EVENT (its ground expired); the DE fixture re-derivation onto a **DE-side** carrier.
3. **[0.4.0_DE_ClientPlatform~S]** `TO-10-DE` + the gradient + INT default. Verify INT on a
   **CLEARED PROFILE** and say so — a warm browser can neither pass nor fail it.
4. **[0.7.0_AE_CloudOps~S]** Satellites schedule is APPLIED; `TO-6-AE` closes on the 07:00Z EXERCISE.
5. **[ANDREW]** 4 open calls — design-pass accept, book-grain-return scope, PROD promote,
   CLAUDE.md Rule-21 wording.

## 9. One thing worth carrying

**The fabric's best findings came from whoever held TWO things at once, not whoever measured deepest.**
The integrator holding an apply time AND a commit time; a DS lane holding two seats' messages; a DE
lane holding my inventory and their own uncommitted work. Every lane measured its own surface
correctly — **the defects lived in the seams, which are by definition inside nobody's scope.**
