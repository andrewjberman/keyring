# 1.0.0_SA_CTO~B (Kimi Semantic Vertical Pipeline seat) -- 2026-08-05 12:50Z -> 2026-08-06 04:15Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE, IMPLEMENT, SCRIBE

Andrew-direct respawn onto the Kimi Semantic Vertical Pipeline; first scheduled fire 9aET the same
morning. 21 commits. Window covers: the first unattended fire, two P0-class runner defects found and
fixed, an estate-wide medallion ruling, a decommission dispatched and verified, and 9 of 29 Phase-0
verticals ratified with Andrew row-by-row.

---

## Headline

**The pipeline fired unattended for the first time and produced a clean report -- and the day's real
work was discovering that its primary input had never reached the model at all.**

`manifest/2026-08-05.json` RUNNING 13:01:29Z -> PENDING 13:04:53Z, `ai_section: PRESENT`,
`degraded_sources: []`, 313 commits in window, both artifacts verified on S3 (226,997 B JSON +
32,179 B MD). The reasoning-budget starvation fix from the prior session held on its first run with
nobody watching.

Then `3.0.0_SA_CVO` found the corpus half was a frozen 2026-07-30 mirror reporting healthy, and --
after that was fixed -- that **`build_prompt` had no corpus parameter at all**, so the human-ruling
half that Andrew's ruling 6 calls the entire point had never once been shown to Kimi.

---

## What landed

### The runner (4 commits, all deployed + independently verified)
| Commit | What |
|---|---|
| `765233590` | corpus coverage block reports FRESHNESS, not just presence. Presence was the only predicate, so a frozen corpus emitted the strongest possible all-clear |
| `a254104b34` | P2: field named `last_commit_utc` carried `-04:00`. My own bug relocated into the interface. Normalised + raw stamp preserved; A5 unparseable branch closed |
| `f023857ab` -> `9a1856bc0` | **DELIVER the corpus to the model** + kill the silent mid-string truncation. Then the axis correction, then an ASCII strip |
| `1d95d25b1` | INVERT the budgets: all 153 nuggets now reach the model (was 69); git half becomes a summary. Token instrumentation added |

**Deploys:** 2, both AE-executed (`0.7.0_AE_CloudOps`), both ETag-verified by me independently.
`a110981492b461e19fb9be7848b9ad09` (62,875 B) then `5ff45f5e968d4a43422c973b5e8f0657` (70,281 B).

### Rulings recorded (Andrew-direct, all VERBATIM + broadcast same turn)
- **Canonical medallion form, estate-wide:** bronze (raw vendor) -> silver (parquet queryable) ->
  gold (processed analytics) under `opal-data-assets/{vendor}/{firm}/`; serving =
  `opal-data-portal-v2/platinum/`. **PLATINUM IS THE GAP** -- CLAUDE.md Rules 17/17a carry the first
  three and name no serving tier. Law edit routed to base `1.0.0_SA_CTO`.
- **Medallion INTENT:** *"bronze and silver ... are not logic specific/product specific at all. in
  gold is when it branches to product."* Supplies the missing WHY behind Rules 17/17a -- silver must
  stay complete BECAUSE MULTIPLE PRODUCTS BRANCH FROM IT.
- **Full account strings:** ADVI = `08335338`, MDPF = `08242234`; write the full 8 digits, never the
  4-digit prefix.
- **Phase-0 grain convention:** the value names the BUSINESS FUNCTION's life-shape; interior churn
  (migration/consolidation/refactor) is NOT a lifecycle shift.
- **`causality` RETIRED** -- and his word IS the `retirement_ruling` the value structurally requires.
- **`cma` cadence = ANNUAL.**
- **`canonical-schwab-si2` naming**, ruled with the conflicting 07-17 law in view.
- **Sixth item (response shifts the process) is INSIDE v3**, not behind it.

### Phase-0 sitting: 9 of 29 ratified
advi-bd, advi-cot, advi-inf, canonical-schwab, causality (RETIRED), ceo-digest, cma, correlation,
data-refresh. Roster stays 29: **28 live + 1 terminal.**

### Dispatched + closed
`0.7.0_AE_CloudOps~C` (Andrew instantiated for it): `canonical-schwab-runner` **terminated**
(`772ff82f5`) -- it had NEVER RUN ONCE -- with 484 S3 objects preserved; live box renamed
`quartz-si2-spike` -> `canonical-schwab-si2`, false `reversible=true` dropped; `exempt_reason`
populated at the generated file's SOURCE.

---

## Findings (mine and received)

**MINE:**
1. MSTR's governance backstop was armed at a path that does not exist (`{YYYY-MM-DD}/manifest.json`
   -- the v4 SPEC, never built). Disarmed BEFORE the fire; would have reported ABSENT on every
   healthy day forever.
2. My own design doc declared the Phase-0 gate PAUSED for **14 hours after Andrew discharged it**.
3. INF's gold never migrated -- `opal-data-inf/gold/` was LIVE-writing at 10:51Z the same day while
   its `opal-data-assets` trees carry no `gold/`. Escalated by Andrew: **that bucket is SERVING a
   Portal product.**
4. **B6 is NECESSARY BUT NOT SUFFICIENT** -- corrected the framing MSTR had put on Andrew's board
   before he prioritised off it.
5. `canonical-schwab-si2` and `quartz-si2-spike` are ONE instance. A box tagged `spike` +
   `reversible=true` was the sole live ingest for both 49F Portal products.
6. `ASTN_WSJFT.B`: 42-day-old ACTIVE "TOP PRIORITY" build TO against a system that ran that morning.
   Routed to COO, who found criteria 2/3/4 unconfirmed and dispatched VERIFY-ONLY.

**RECEIVED, and the ones that cost me:**
- CVO: frozen corpus (P1); the `_utc` P2 found by EXERCISING my fix; the corpus never reaching the
  model at all.
- `~C`: **four defects in my briefs** -- payload-bound EventBridge target; wrong-bucket prefixes; a
  "Terraform only" rule applied to a box TF does not manage; and sending them at a GENERATED file.
- AE: my "2% over the exercised prompt size" risk was **misattributed to the wrong axis** (input
  chars vs `max_tokens`), and 60,000 was never a validated limit.
- COO: a stale deploy pin, caught by their own re-check.

---

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-estate <vertical>` | Phase-0 rows 5-9 | PASS | first-contact traversal per row; its own census-vintage warning proved load-bearing |
| `comp-grep` | State/Friction scan, quartz, causality | PASS | on-rails; prints the denominator, which is what made the null result citable |
| `comp-which` | routing check at startup | PASS | forwarder exercised, not name-resolved |
| `comp-state --self-test` | /exec-sum | PASS 3/3 | instrument discriminates |
| `commit-gate.sh` | every `.py` edit | PASS (1 WARN) | **caught non-ASCII I introduced** -- WARN-only, fixed rather than shipped |
| `safe-commit.sh` | 21 commits | PASS | owned-paths BLOCKED me twice on `infra/aws/**`; 4 audited lane overrides |
| `comp-estate --matrix` | roster denominator | DEFERRED | re-derive at sitting resume |

**What worked:** the census-vintage warning on `comp-estate` -- following it caught `correlation`'s
served artifact being 7 weeks newer than the census claimed. **What failed:** nothing tool-side.
**Gap found:** `comp-estate estate-report` is UNRUNNABLE -- there is no `estate-report` vertical, so
the pipeline producing the daily report is invisible to its own vertical join. Promoted to the v3
critical path (design s.9.3).

---

## Blockers

**NONE at this seat.** Everything open is either Andrew's to rule (Phase-0 rows 10-29; the
closed-loop mechanism) or another lane's (CVO's PENDING question; COO's `ASTN_WSJFT.B`; MSTR's B6
board item).

---

## Current State (zero-context handoff)

- **Pipeline is LIVE and SCHEDULED.** `estate-report-0900et`, `cron(0 9 * * ? *)`
  America/New_York, ENABLED, target `estate-report-orchestrator`. Next fire **2026-08-06 13:00Z**.
- **Deployed runner = `9a1856bc0`** at `s3://opal-estate-report/code/estate_report_runner.py`,
  ETag `5ff45f5e968d4a43422c973b5e8f0657`, 70,281 B. **DEPLOYED != EXERCISED -- nothing has run this
  code.** Tomorrow's boot is the first execution of BOTH the corpus delivery and the budget
  inversion, and **CVO owns that verdict.**
- **The corpus is STILL the frozen 07-30 mirror.** This session made it VISIBLE and DELIVERED; only
  the B6 capture uploader makes it CURRENT. Unbuilt, unowned, on MSTR's board for Andrew.
- **If tomorrow returns KIMI_EMPTY:** read the `KIMI_LENGTH_STARVED(reasoning_tokens=...)`
  discriminator FIRST, **not** the prompt budgets. `max_tokens` (32000) is the failure axis, not
  input size. New `KIMI_TOKENS` log line reports both.
- **Phase-0 table:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/KIMI_SVP_PHASE0_LIFECYCLE_PROPOSAL_TABLE_20260804.md`
  -- 9/29 ratified, resume at **row 10 `etf-reports`** (carries the open ETFS CANON question).
- **v3 design:** `docs/architecture/OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md` -- s.9 critical path,
  s.10a holds Andrew's axis VERBATIM (now in this lane's own record), s.10c the gate ruling.
- **Remaining UNDECLARED rows (13 insurance, 25 security-scanner, 27 ticketing) are GROUND-READ
  BEFORE presenting.** Two of two examined so far were wrong in OPPOSITE directions. Row 25 is
  likely inverted -- its backend is the live `opal-data-refresh-api` and its page is mounted at
  `App.tsx:434`.

---

## Next Steps

- **[Andrew]** Phase-0 rows 10-29, row by row. Then: does the operator's response to a Kimi PROPOSAL
  become an input to the next cycle's Friction, and is it higher-weight than ambient operator
  language? **His yes/no/reshape IS the closed-loop design.**
- **[1.0.0_SA_CTO~B]** Build R1 + State + Friction to the 08-04 verbatim (fully grounded). Draft the
  closed-loop PROPOSAL for the base-CTO gate. Rule-24 proposal for the `EC2_MANIFEST` retirement
  convention + the `gap_list` field shape.
- **[3.0.0_SA_CVO]** Verify the 13:00Z fire -- corpus block + the new coverage denominator. F1-F3
  boundary_declaration co-work is startable now.
- **[1.0.0_SA_CTO]** CLAUDE.md: add PLATINUM as the fourth medallion tier. Standing finding: **a
  `-target` destroy leaves the DECLARATION -- `terraform destroy` removes INFRASTRUCTURE, only
  deleting the declaration removes the INTENT.**
- **[0.7.0_AE_CloudOps~C]** `ASTN_WSJFT.B` verify-only (COO-dispatched).

---

## The pattern worth carrying forward

Nine defects this window, and **the same shape underneath almost all of them: a record that was
correct when written, carried authority, and was never re-derived.** MSTR's oracle path, my own
gate-discharge, my staffing claim that went stale in five minutes, the census's freshness figures,
the `spike` tag on production, a 42-day-old TOP PRIORITY against a shipped system.

And my own contribution to it, named plainly: **four of my briefing defects were confident
constraints whose preconditions I never grounded** -- each stated in the register of a RULE rather
than a CLAIM, which is precisely the register that discourages checking. Every one was caught by
another seat refusing to inherit my reads.

**The controls did the work, not the care.** Several of these were written by the agent who had, that
same hour, recorded the rule against them.
