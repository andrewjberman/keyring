# MDPF_CANON -- the MDPF canon migration: gold as dated parquet at the builder's address per R7 (each firm's in its own bucket, the composite in opal-data-mdpf), each firm's served slice in that firm's own bucket, one publisher, and two legacy trees retired only on proof

```json
{
 "project": "MDPF_CANON",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v2.27",
 "step": 4,
 "brief_ref": "docs/briefs/d8-mdpf-canon-migration-brief-20260913.md@fd579d3caf",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10"],
 "status": "RATIFIED"
}
```

**v2.0 is this PRD MOVED into its tree home and brought current in the same act.** v1.0 and v1.1 lived at
`docs/architecture/MDPF_CANON_PRD.md` (@`dfc492aa83`, @`6f53713982`, rulings folded @`6e0a07d934`), had no PRD header,
and were never decomposed because the project was never registered. That path now carries a moved notice. Its three
stale items are amended here (DEC-1), and its founding content -- A-1 to A-3, rows B1 and B2, and the three
final-step obligations -- is carried forward below.

**v2.4, v2.5 and v2.6 (2026-09-16 ~18:3xZ to ~19:1xZ, `1.0.0_SA_CTO`) -- every typed data home became the builder's address, and every restatement of the old single-bucket bar followed it (v2.6: the two DEFINED OUTCOME lines the CVO's unscoped re-read found after its own census missed them).** Andrew's call 3
(~18:2xZ, record @50d1b9403e: *"(a), yes. Should be using LGIC_NAMING patterns in both cases"*) decided gold's home per R7 through
`address()`; v2.4 restated CONTRACTS :177's gold instance and M2, which had typed the product bucket for every scope against the same
sentence's builder mandate (the CVO's 97324 finding, its own disclosure that it signed v2.2 without catching it). v2.5 finished the job
on both halves' findings: the title, FWD-1's bar (which counted places and could not tell a correct four-bucket build from a wrong
one-bucket build; it now names the rule), PATHS, the SURFACE MANIFEST and BRIEF COVERAGE row 4 (the brief's "one bucket" superseded for
firm-attributable tables), and the `state` instance, which cited R21 for an address R21 itself (his GAP-1 ruling, 09-13) and Rule 30 both
home in the firm bucket and which `address()` already returns that way -- a standing ruling applied, no new question. The 08-18 "MDPF gold
stays at opal-data-assets/portal/gold/" word is superseded for firm-attributable tables only; `global` and the code home are untouched.

**v2.7 (2026-10-01T08:23Z, `1.0.0_SA_CTO`) -- four cell candidates carried in from MDPF_COTREMEDIATION's close; ENDPOINT and CONTRACTS are unchanged.** Rulings batch 71 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`. Rows M13 to M16 below are the served-shape and process items that project's channel left open (`org/surprise_channel/MDPF_COTREMEDIATION/REMEDIATION_v1.md`, rows S3, S13, S16, and the registry's process cell). They are placed here because this project defines the pipeline's contract step and its served shape. No outcome is added; each row serves an existing FWD.

**v2.8 (2026-10-01T09:53Z, `1.0.0_SA_CTO`) -- one more cell candidate, M17, placed from MDPF_TAXSMA's row S5 (rulings batch 78); ENDPOINT and CONTRACTS are unchanged.**

**Brief:** `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md` @`fd579d3caf`, author `4.0.0_SA_CRO~D`.
- The later touch @`9ba5e5370d` is a one-line diff to the REFS `PROJECT` line.
- The endpoint was cut from @`c2884cbb19`. The only change between that and @`fd579d3caf` is the runner-name correction
  in IV.8 and O6: the fence keys on the scope slot, not on a name outside its patterns. That moves a mechanism, not an
  outcome, so no FWD id moves.
- There are 30 coverage entries below.

**Endpoint:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D8_MDPF_CANON_MIGRATION_20260913.md`, cut
@`d2ceedadbb`, ruling stamps @`e2210bf34c`. Andrew confirmed its DONE WHEN lines ~18:4xZ 2026-09-13.

**Registration and order:**
- Registered @`003034456d` under D8/MDPF.
- In `org/missions/SEQUENCE.yaml` it is in stage 2. Its hold (at REGISTERED until LGIC_ENFORCE's PRD is admitted) is
  MET, because LGIC_ENFORCE v1.1 is admitted.
- Its FWD-2 and FWD-6 wait per firm on `ADVI_FIRMBKTS`'s router flip for that firm and its first-hour read (v2.11, R1), and FWD-6 also waits on LGIC_ENFORCE's fence (its
  cell E5). The other six outcomes do not wait on either.

**Rulings this PRD executes, verbatim anchors:**
- **A-1, A-2, A-3** -- Andrew-direct 2026-08-25 ~20:4xZ: *"regarding D10, it varies, I specify them on a per instance
  basis. Regarding 2, should be neither, we should handle all of this including gold parquet artifacts all in
  opal-data-mdpf. Regarding 3, should be a full history to the extent we have it in nice clean dated/timestamped-in-title
  parquets and each day we just add a row."*
- **The layout** -- ~20:5xZ the same night: *"Layout reconciliation i would like it if we could follow similar pattern as
  we developed in opal-data-assets."*
- **The three final-step obligations** -- ~20:5xZ: *"you will of course have to check the relevant /seams between silver
  to gold per pipeline and you'll have to find that platinum portal publisher lambda and make sure that it is repointed
  to the relevant locations in opal-data-mdpf. you will also of course have to make sure that any vms/resources that drew
  code from opal-data-assets/portal/ are pulling from canonical path in opal-data-mdpf"*.
- **B1** -- 2026-08-27 19:05Z: *"Option 1 with a repoint is fine"*. **B2** -- a standing declared exception (call-6
  split (c), relay 76365).
- **Route (c) and a dedicated runner** -- 2026-09-12 ~13:4xZ: *"C"*, then *"There should be a dedicated mdpf runner for
  this also not reusing a firm specific runner"*.
- **Client platinum per firm** (2026-09-12 ~16:01Z, `e29a895ce3`), with Rule 17b amended per tenancy.
- **The source-first key string** (~03:2xZ 2026-09-13), ratified as LGIC_NAMING S1.
- **D8 as this project's home** (~03:2xZ).
- **The nine calls of ~01:3xZ 2026-09-13**: D10-2 (the spelled-out firm buckets survive), and GAP-1 and GAP-2.
- **The fence re-derived from the scope slot, on three conditions** (~18:4xZ card 1), carried by LGIC_ENFORCE.
- **The 45-day window** (~18:4xZ card 2), read with ~03:xxZ 2026-09-14 (*"none of the legacy channels are quiet because
  they are the active channels for the firms now"*).

**The ENDPOINT section below is the endpoint's outcome block verbatim, except for four kinds of removal:**
- the two `DEPENDS` lines, on FWD-2 and FWD-6, which are carried in CONTRACTS and the order above;
- FWD-8's inheritance line, which is carried as a CONTRACTS row;
- the `(s.N)` pointers into the endpoint file;
- the `PRD ACn` pointers to the superseded PRD's acceptance criteria, which are mapped in DEC-3.

This follows the precedent `3.0.0_SA_CVO` accepted on the three D14 PRDs.

**v2.1 (2026-09-14) answers `4.0.0_SA_CRO`'s REFUSED brief half** (review
`docs/briefs/sources/MDPF_CANON_L4_BRIEF_REVIEW_v2_0_20260914.md` @`4d08ce88b2`, stamp @`61e981a6e3`):
- **R1:** the firm slice's key is the schema's five-segment form, with the served file in the partition slot the
  schema calls "a named leaf", and one exact builder vector. The builders cover every NEW address; the historical
  `global` path is bounded out, not moved (CONTRACTS, M9, M10, PATHS, manifest).
- **R2:** the bronze move waits on the builders like every other cell that writes a new key (DEC-15, arc, M8).
- **R3:** the portal's existing requests keep their URLs, because the portal is frozen, and a tenant-asserting
  compatibility mapping at the edge carries them, proven through the page's own request path before any slice moves
  (CONTRACTS, DEC-5, M9, PATHS, manifest).

CONTRACTS changed, so both halves are owed again.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Anyone can tell how current any model-portfolio figure is from where it is
         kept, and every one of them is kept where the one naming rule puts it
         DONE WHEN  EXERCISED -- someone has actually answered a dated question this way
         ACCEPT     asked "what did 49 Financial's total assets read on a particular day
                    last month", someone answers from the name of the stored file alone,
                    without opening it -- and every stored figure of this kind is where
                    the one naming rule puts it, that firm's own bucket for a firm's
                    figures and the product bucket for the cross-firm composite, full
                    history, one addition per day -- where today the same figures sit in
                    two places under two different naming habits, and neither is where
                    the rule puts them
         SOURCE     brief Part I O1; bar Part III O1

  FWD-2  A firm's advisors read their model-portfolio figures from that firm's own
         storage, and another firm's advisors cannot reach them even with the address
         DONE WHEN  EXERCISED -- someone has deliberately tried to reach one firm's
                    figures while signed in as another, and been refused
         ACCEPT     someone signed in as an Inflection advisor, holding the exact address
                    of 49 Financial's figures, tries to open them and cannot, because they
                    live in storage that is not Inflection's -- and a 49 Financial advisor
                    opening the same page sees their own figures exactly as before -- where
                    today all three firms' figures sit side by side in one shared place
                    that any signed-in advisor's page may ask for
         SOURCE     brief Part I O2; bar Part III O2

  FWD-3  The combined all-firms figure stays where it is, and anyone can read the
         written reason why
         DONE WHEN  EXERCISED -- someone asked why it did not move has pointed at the
                    written reason
         ACCEPT     someone asked why the combined figure across all firms was not moved
                    into any one firm's storage points at a written explanation of why it
                    reveals nothing about any single firm's clients -- so nobody moving data
                    later sweeps it into one firm's storage by mistake -- where today that
                    explanation is owed and not written
         SOURCE     brief Part I O3 -- NO Part III bar; cut from Part I alone

  FWD-4  The one step that turns stored figures into what the page shows reads only
         from the model-portfolio store, and what people see does not change
         DONE WHEN  EXERCISED -- the before-and-after comparison has been run and read
         ACCEPT     someone compares what the page shows before and after the switch and
                    finds every figure identical -- comparing the figures people actually
                    read, never the timestamps that change every day anyway -- and the step
                    that prepares the page takes its input from the model-portfolio store
                    and nowhere else; it is the LAST thing switched over, not the first
         SOURCE     brief Part I O4; bar Part III O4

  FWD-5  Everything that produces model-portfolio figures writes to the model-portfolio
         store and reads its raw inputs from the shared intake, and none of its working
         code is kept anywhere else
         DONE WHEN  EXERCISED -- the search has been run and read
         ACCEPT     a search of everything that builds these figures finds nothing still
                    writing to, reading from, or running code out of the old places -- any
                    leftover mention is history, not a live instruction -- while the saved
                    copies kept for rolling back stay exactly as they are
         SOURCE     brief Part I O5; bar Part III O5

  FWD-6  A dedicated runner writes each firm's figures into that firm's storage, and
         the rule keeping firms' data apart was never loosened to allow it
         DONE WHEN  EXERCISED -- a run for one firm has written into that firm's storage
                    with the separation rule unchanged
         ACCEPT     a run for one firm writes that firm's figures into that firm's own
                    storage, and the rule stopping one firm's systems touching another
                    firm's data is word-for-word what it was before -- nobody loosened it to
                    make the run work -- where today the shared runner would be turned away
                    from that storage by that very rule
         SOURCE     brief Part I O6; bar Part III O6

  FWD-7  Model-portfolio raw vendor data is received in the same place as everyone
         else's
         DONE WHEN  EXERCISED -- the receiving step has been run on demand and its output
                    read where it landed
         ACCEPT     the step that receives model-portfolio raw data is run deliberately and
                    its output lands in the shared intake alongside every other vendor's --
                    the next routine daily delivery landing there too is the confirmation,
                    never the proof
         SOURCE     brief Part I O7 -- NO Part III bar; cut from Part I alone

  FWD-8  The two old copies are gone, and the protective hold no longer points at
         something that does not exist
         DONE WHEN  EXERCISED -- the retirement proof has been produced and read
         ACCEPT     before either old copy is removed, someone shows a record that nothing
                    read or wrote it for the agreed stretch, from a named instrument rather
                    than a list of the readers anyone happened to know about; and the
                    protective hold either points at the thing it exists to protect or is
                    formally closed with the reason written -- where today it names something
                    already gone while the real thing it should protect is written every day
         SOURCE     brief Part I O8 ("Decommission is a proof (sibling O6)"); bar Part III
                    O8 (which covers the hold half only)

  FWD-9  The AUA Trend shows custom models as ONE block and the strategy groups as
         chips, in the colors the Total Assets breakdown already uses
         AT GLOBAL, the Trend draws every group from 2024-11-01 by the
         rule table of the Global Trend history (the L10 ADDENDUM
         v2.20), and: (a) the per-model lines on dates where Global
         holds one firm (the five models before 2026-05-15; Custom from
         2026-05-15 to 2026-07-19) draw ONLY for an internal session
         (`firmId` = the internal firm), read from that firm's own
         served series, which an internal session may read; the Global
         served leaves keep FWD-3's fold and gain no single-firm value;
         a demo-tenant session draws exactly as an internal session
         (v2.23, Andrew 2026-10-15); every other session (a claim with
         no firmId) draws on those dates one "Models" band (`model_aua`) and keeps
         exception (ii) of clause (2), its boundary sentence and its
         printed gap; (b) Client Supervised on every date =
         `non_model_aua` minus the two Opal SMA strategies (Dividend,
         Growth) and, before 2025-03-27, Opal Global All Equity Total
         Return, each from SMArtX `fact_model_aum_daily`
         `closing_equity` before 2026-05-18 and from the served
         carve-outs after; "Other AUA" is not drawn at Global; (e) ETF
         Strategies draw from 2024-11-01 (SMArtX before 2026-05-18,
         the served carve-outs plus `sma_additive_aua` after); ALT
         Strategies = `tax_additive_aua` only, and Muni is a Custom
         member, never ALT; (c) on a date with no
         total, and for a group's null on a date with one, the group
         carries its last known value as point class `carried` (claim
         held), forward only, never before the group's first value;
         (d) for an internal session the groups sum to the Total to the
         cent on every dated row. Firm scopes are unchanged by (a)-(d),
         except that at a firm scope the Client chips draw on the
         as-of date only, and the dated category-views history route
         has no required reader (v2.23). (f) AT COTTONWOOD (v2.23): the
         window starts at the first measured total (2026-06-09); the
         Total is `partner_custody_total`; Other AUM = that total minus
         `model_aua` on every total-bearing row; the model leg carries
         its last measured value on a date where it is absent (point
         class `carried`); the interpolated model mix before 2026-07-20
         keeps its marking; the groups sum to the Total to the cent.
         (g) MUNI (v2.23): the Cottonwood muni portfolio (Opal Muni
         Income) is a Custom Model, displayed as "Opal Municipal Bonds",
         inside "Custom Models" at Cottonwood and at Global, never Other
         AUM or non-model.
         DONE WHEN  EXERCISED -- on Model Portfolios > AUA TREND ANALYSIS > Trend (the
                    period-end bars, the daily area chart, the legend and the
                    tooltip), read on `bun run dev:live --port 5174` (portal
                    `package.json` `dev:live`, `scripts/dev-live.mjs`) at a
                    STATED portal commit against the live services, at Global
                    and at each firm scope the page offers:
                    (1) THE SERIES SET. The five canonical Opal models (Ultra
                    Short-Term to Ultra Long-Term) are one series each. Then:
                    - "Custom Models" (Total Assets L1 key `Custom`): every
                      model line that is not canonical, ETF or ALT, INCLUDING,
                      at Global, FWD-3's pooled "Other Models" line, which it
                      replaces (no separate "Other Models" series remains);
                    - "ETF Strategies" (`ETF Strategies`, matching Total
                      Assets): `pfde` (= `sma_additive_aua`) PLUS the two
                      carve-out SMA lines `opal_div_sma` and `opal_growth_sma`.
                      Those two sit INSIDE `non_model_aua`, so they are carved
                      OUT of it by their own served `by_model` values (exact
                      members, not an estimate). Measured against the Client
                      gap: equal to the cent on 2026-08-27 only. Over the 21
                      dated objects the remainder after the carve-out runs
                      from -4,649.20 to +301,207.84 (the category-views
                      snapshot and the time series are different reads of the
                      same day; cause not established);
                    - "ALT Strategies" (`ALT Strategies`): the stacked member is
                      `tax_additive_aua` ONLY, the headline component (`tax` in
                      `by_model` is the same dollars, equal to the cent, and is
                      not stacked);
                    - non-model AUA (`non_model_aua`). On a date WITH a
                      category-views object it is split into "Client
                      Supervised" (`Client - Opal Supervised`), "Client
                      Unsupervised" (`Client - Opal Unsupervised`) and "Other
                      AUA" (the remainder: `non_model_aua` minus the two Client
                      chips minus the two carve-out SMA lines). It is drawn
                      only when ABOVE zero. Where it is zero or BELOW zero it
                      reads ABSENT: no band is drawn, there is no clamp, and
                      the amount below zero is printed with the read as that
                      date's basis difference. On a date WITHOUT one it is ONE
                      series, "Other
                      AUA" (`non_model_aua` minus the two carve-out SMA lines),
                      and the two Client chips draw nothing. The Client chips
                      read the dated category-views objects through a
                      READ-ONLY served history route over the existing objects
                      in `opal-data-assets/portal/gold/mdpf/global/
                      category-views/` (no new data, no back-cast; its own cell
                      under its own never-widen pair). The grade is read with
                      that route live. Membership is from
                      `data/mdpf/scripts/gold/mdpf_category_registry.py`
                      VIEW_TREE (Client: the `fee_taking` axis, :150-157) and
                      the issuer's map (`deliverables/2.0.0_SA_COO~D1/round7/
                      FWD9_GROUPING_READ.md` :28-32). Colors are
                      `portal/src/components/CategoryViewTree.tsx` `L1_COLOR`
                      (:87-95), with Custom = `PALETTE.fuchsia500`, the
                      "Models" card hover color, EXCEPT "ALT Strategies", which
                      stays `vermilion500` on the Trend (Andrew-direct
                      2026-10-01 ~19:4xZ, "we canonically use vermillion for
                      alts", pinned by `ModelPortfolios.taxsma-color.test.ts`;
                      his 2026-10-13 words name only the Custom color);
                    (2) THE SUMS. On each drawn date every grouped series
                    equals the sum of its served members to the cent (abs
                    diff <= 0.01): the time series' `by_model` for Custom,
                    ETF and ALT, and that date's category-views node for the
                    Client chips. The whole stack sums to
                    `opal_aggregate_aua` to the cent (CN-d-3's property, kept;
                    the Total is model + non-model + `sma_additive_aua` +
                    `tax_additive_aua`; the carve-outs are drawn once, under
                    ETF, never also inside Other AUA), EXCEPT (i) on a dated
                    object where the Other AUA remainder is below zero: there
                    the stack EXCEEDS the Total by exactly |remainder|,
                    printed, and (ii) on a date where
                    FWD-3's fold
                    suppresses the pooled "Other Models" line at Global (fewer
                    than 2 firms hold it). There the stack is BELOW the Total
                    by exactly the suppressed amount, read from the fold's own
                    record and never drawn, as FWD-3 requires. (ii) covers the
                    dates before `per_model_detail_begins` (2026-05-15), where
                    the fold suppresses EVERY model line: the stack is below
                    the Total by the whole model AUA, the page states "per-model
                    detail begins <date>; earlier model assets are in the Total
                    and are not broken out", and the gap is printed (v2.18);
                    (3) THE DRAW, printed with the read: date A is the as-of
                    frontier (`lib/trading_calendar.prev_trading_day` of the
                    build date); date B is 2026-08-27, the first
                    category-views date; date C is the trading day before
                    2026-08-27; date D is the first trading day between
                    2026-08-27 and the frontier with no category-views
                    object; date E is 2026-09-30, the dated object with the
                    most negative remainder (-4,649.20). B, and A when it
                    carries an object, are the present arms; C and D are the
                    absent arms; E is the negative-remainder arm (Other AUA
                    absent, the excess printed and equal to |remainder| to the
                    cent);
                    (4) ABSENT, on C and D: no Client bar or area segment is
                    drawn, the tooltip carries no Client row (or one reading
                    "absent", never "$0"), and the legend chips stay with no
                    value for that date. A measured zero is shown as "$0",
                    never "-$0". The negative arm is today's build, which
                    lists about 17 individual series
         ACCEPT     The trend reads as a few meaningful groups, not a crowd of
                    individual models, it matches Total Assets, and it adds up.
         SOURCE     Andrew-direct 2026-10-13 ~18:4xZ at the dell2 terminal, record
                    ANDREW_DIRECT_20261013_184xZ_MODEL_PORTFOLIOS_AUA_TREND_GROUP_CUSTOM_MODELS_AND_CHIPS.md
                    @5e80d5eb9b (owner MDPF_CANON)

  FWD-10 Cottonwood's figures count only the assets Cottonwood supervises, and the
         total matches the one Cottonwood sees in Black Diamond for the same day
         DONE WHEN  EXERCISED -- read on the Cottonwood view of Model Portfolios (the
                    headline total, the Total Assets breakdown and the AUA Trend)
                    on `bun run dev:live --port 5174` at a STATED portal commit
                    against the live services, for a STATED value date:
                    (a) every Cottonwood figure counts only accounts whose BD
                    `Account Supervised` reads `Supervised`; history applies
                    today's flags, and the served meta says so in a field; the
                    model and SMA legs move only by Unsupervised accounts that
                    carry them (measured 0 of 130 on 2026-10-16); the Global
                    composite folds Cottonwood's supervised book through its
                    sums; 49 Financial and Inflection are byte-identical before
                    and after (their whole-book rule of 2026-08-25 stands);
                    (b) the Cottonwood total equals the BD Dashboard
                    "Supervised" figure for that value date, or the page's
                    source line names the remaining difference and its cause.
                    Until (b) closes, the source line says the figure is BD's
                    export valuation of supervised accounts and does not claim
                    a tie to the BD Dashboard. Negative arm: today's build,
                    554,632,228.45 on 2026-10-15 including 33,071,069.62 of
                    Unsupervised accounts, against BD Dashboard Supervised
                    530,421,988
         ACCEPT     Cottonwood's advisors see only the assets they supervise, and
                    the total they see here is the number Black Diamond shows
                    them for that day, or the page says plainly by how much and
                    why it differs.
         SOURCE     Andrew-direct 2026-10-17 ~01:0xZ at the 4.0.0_SA_CRO~DDD
                    terminal, record org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/
                    ANDREW_DIRECT_20261017_010xZ_COTTONWOOD_SUPERVISED_ONLY_MATCH_BD.md
                    @f67b4711f1; re-affirms Andrew-direct 2026-08-25 ~14:05Z
                    (a78c51158c)
```

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| the canonical key string, MDPF's instances | **consumed** (ruled) | `{source}/{scope}/{tier}/{table}/{partition}`, verbatim, with `{source}` = `mdpf` and `{scope}` one of `49financial`, `inflection`, `cottonwood`, `global`, `demo` in the LONG form. The instances, each the builder's output and none typed: gold at the address `address("mdpf", {scope}, "gold", {artifact}, "date={YYYY-MM-DD}")` returns under R7 -- the firm bucket for the firm scopes, `s3://opal-data-mdpf/` for `global` only (X2's composite branch) -- on Andrew-direct 2026-09-16 ~18:2xZ, call 3, record @50d1b9403e; state at the address `address()` returns for the `state` tier under R21 and Rule 30 (the firm bucket for the firm scopes, `s3://opal-data-mdpf/` for `global`); bronze at `address()`'s output for the bronze tier (R4; today `s3://opal-data-assets/mdpf/{scope}/bronze/{feed}/...`); a firm's served slice at `address()`'s output for the platinum tier (R7; today `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/{leaf}.json`), where `{table}` is the snake_case artifact and the partition slot holds the schema's "named leaf" form: the kebab-case served file itself. The vector: `key("mdpf", "49financial", "platinum", "aum_metrics", "aum-metrics.json")` returns `mdpf/49financial/platinum/aum_metrics/aum-metrics.json`, and `address()` over the same arguments returns it under `s3://opal-data-49financial/`. **Every NEW address comes from `LGIC_ENFORCE`'s `key()` and `address()`, never typed.** The one exception is the combined slice `s3://opal-data-portal-v2/platinum/mdpf/global/...`: it is historical, tier-first, and stays exactly where it is (X2), so no builder produces it and nothing moves it to satisfy this row | ruled by Andrew ~03:2xZ and ratified as `LGIC_NAMING` S1; the builders are `LGIC_ENFORCE`'s |
| the gold artifact | **produced** | parquet only; one partition per day, carrying its date in the key; the full history backfilled from the current JSON to the extent it exists; history is never rewritten. The artifacts are `account_distribution`, `account_units`, `aggregate_aua_timeseries` and `aum_metrics` (snake_case) | the publisher; any reader that needs a figure's vintage |
| the served platinum JSON | **produced**, by the publisher alone | the leaves `aggregate-aua-timeseries`, `account-distribution`, `aum-metrics`, `account-units`, `category-views` and the derived read-only `category-views-history` (FWD-9; v2.17) (kebab-case), their data-bearing leaves byte-unchanged across every cutover, with `_provenance.written_at` excluded because it advances daily. The publisher is the one place parquet becomes JSON, and it reads only `opal-data-mdpf` | the portal's Model Portfolios page |
| each firm's bucket and its serving grants | **consumed** | the bucket exists, serves, and carries its serving grants, per firm | produced by `ADVI_FIRMBKTS`, per firm; FWD-2 and FWD-6 wait on it for that firm |
| the scoped route for a firm's slice | **produced** | the portal's existing requests keep their URLs (`/api/general/mdpf/{firm}/...`); the portal is frozen, so no caller changes. The edge maps them: `global` keeps its current general handling unchanged, and a firm segment resolves through the registry, aliases included, to one firm and is served, from that firm's bucket at the key above, to two kinds of session only: a session whose validated tenant resolves to that same firm, and an internal Opal staff session (tenant `opal-capital`), for which the path segment IS the selection because the frozen portal's selector sends no `?firm=` on these requests (`ModelPortfolios.tsx:357-358`, Andrew's MDPF_SCOPED.S5). Any other firm's session is refused. This is the boundary the scoped router already enforces by comparing resolved buckets (`shared-advisor-router/index.mjs:367-373` @`40697fe79d`), never a bare segment-equals-tenant test. **Keeping the old URL never keeps general authorization for firm data** | the portal's Model Portfolios page and its wrappers (`aum.ts`, `portal-proxy.ts`); the edge routers and CloudFront behaviours; the router's firm map is `LGIC_ENFORCE`'s generated view |
| the dedicated runner | **produced** | one principal per firm, named by `name()` (`mdpf-49f-runner-role` and its siblings), whose only write grant is `opal-data-{firm}/mdpf/{firm}/platinum/*` in its own firm's bucket; its host is built by this project | the per-firm slice writes |
| the firm gold writer | **produced** | one principal PER FIRM, its name `name()` output with the firm in its scope slot (so `LGIC_ENFORCE`'s scope-derived Deny admits it unchanged), assumed by `mdpf-gold-lambda`; its ONLY write grant is `address()`'s firm gold prefix (`opal-data-{firm}/mdpf/{firm}/gold/*`), never platinum, never another firm. The MDPF_TAXSMA precedent (`mdpf-pipeline/iam.tf` per-firm gold roles). v2.9, L5 call msg 2990, ruled (a) | the gold Lambda (M2) assumes it; M10's runner is unchanged and stays platinum-only |
| the separation rule | **consumed** | `LGIC_ENFORCE`'s scope-derived Deny on each firm bucket, which admits a principal whose name carries that firm in its scope slot. **For FWD-6, "word-for-word what it was before" means the run needs NO edit to it: no exemption row, no carve-out, and the rule's bytes are identical before and after the run** | produced by `LGIC_ENFORCE` (its fence row, and its cell E5 on the template) |
| the decommission standard | **consumed** | for each retiring tree: 45 CONSECUTIVE days in which a named instrument records no data event on the tree except an excluded probe. It starts no earlier than that instrument's observed-live stamp, any other event restarts it, and it counts only once every reader is repointed. Each removal is then its own act | `ADVI_FIRMBKTS`'s FWD-6 window ruling (its tree row @`9819855eda`), on Andrew's ~18:4xZ card 2 and ~03:xxZ word |
| the combined slice's written basis | **produced** | `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/X2_GLOBAL_BASIS.md`: why the combined all-firms figure reveals nothing about any single firm's clients | the ledger's X2 row (`LGIC_CANON`); anyone moving data later |
| inherited law | **consumed** (ruled) | A-1 to A-3 as quoted above; B1 (repoint the RPS read through `opal-data-assets`) and B2 (the JWT read stays, a standing exception, ledger X1); route (c) and the dedicated runner; Rule 17b; the canon's R4-R7, R11, R12, R16-R19 and R21 | Andrew's words; the law surface; `LGIC_CANON`'s canon |

**v2.10 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~22:0xZ), msg 3244 (`2.0.0_SA_COO~D1`):** the M1, M7 and M11 documents live in their author's serial folder under `deliverables/`, because the owned-paths lane admits no root file (row D1-W5-S1). The ledger X2 row cites that path. A wording change only: the ENDPOINT is unchanged.

**v2.9 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~18:4xZ), L5 call msg 2990 (`2.0.0_SA_COO~D1`), ruled (a):** firm-scope GOLD is written by a per-firm gold-writer principal, not by widening the platinum runner. Least privilege per tier, and the live Deny admits it with no edit (FWD-6). It adds one CONTRACTS row and one SURFACE MANIFEST row. The ratified-text half re-signs.

## THE DECISIONS -- CLOSED AT L4

- **DEC-1 The move, and the three stale items.** This file is the PRD. `docs/architecture/MDPF_CANON_PRD.md` becomes a
  moved notice, not a deletion, because other documents cite that path.
  - (a) **The directive is D8** (Andrew ~03:2xZ). The old header said D10.
  - (b) **The old s.2 and AC5 are retired and replaced by a boundary.** They put platinum and compute "out of scope",
    and read at HEAD that means platinum's HOME, so AC5 graded FWD-2 and FWD-6 as defects. Law moved after 08-25:
    client platinum is per firm (~16:01Z 09-12), Rule 17b is per tenancy, and the dedicated runner was asked for
    (~13:4xZ 09-12). **What stays untouched is the conformant compute chain (the four staggered schedules and the
    event accelerator) and platinum's SHAPE.** What moves is the HOME of the three firm slices. What is ADDED is the
    dedicated runner, which changes nothing in the existing chain.
  - (c) **The old s.3 tier-first layout** (`opal-data-mdpf/gold/{scope}/{artifact}/date=...`) **is replaced by the
    source-first string**, as ratified at `LGIC_NAMING` S1. The moved notice at the old path says so and cites that
    PRD, which is the replacement notice `LGIC_NAMING`'s cell N5 needs before its FWD-4 can grade (row LGIC_NAMING-S4).
    A reader who learned `opal-data-assets` reads an MDPF key the same way.
- **DEC-2 The gold artifact (A-3), carried.** Parquet per day, vintage in the key, the full history backfilled from the
  current JSON to the extent it exists, one new partition a day, history never rewritten. **A VINTAGE IN THE KEY CANNOT
  BE FORGED BY A REWRITE**, and that was the 08-25 outage: a fresh mtime over a five-day-frozen payload that every
  instrument read as healthy. It is built correct the first time: no dual-write, no shadow prefix, no standing parity
  comparator (Andrew's complete veto). The underscore and hyphen twins converge on one convention: snake_case in the
  parquet artifact, kebab-case in the served leaves.
- **DEC-3 The old nine acceptance criteria, mapped.**
  - AC1 and AC6 -> FWD-1.
  - AC2 and AC8 -> FWD-5.
  - AC3 and AC7 -> FWD-4.
  - AC4 -> FWD-8.
  - AC5 is retired (DEC-1 b).
  - **AC9 is KEPT, as a control beneath FWD-5 (cell M4):** every silver-to-gold seam passes `/seams` on all three axes,
    grounded on the DEPLOYED artifact. It is the control that would have caught the 08-25 outage. The endpoint said
    dropping it "should be a decision someone makes, not a gap nobody noticed", and the decision is to keep it.
- **DEC-4 The order of acts**, carried from the old s.5 onto the new outcomes:
  1. the reader census;
  2. the emitter, correct the first time;
  3. the backfill;
  4. the readers repointed one at a time, each after its `/seams` read;
  5. **the publisher LAST**;
  6. the served bytes proved unchanged;
  7. the firm slices, per firm, as each firm's bucket serves;
  8. the runner;
  9. the retirements, each on its own proof.
- **DEC-5 FWD-2 is a route-class change, not a prefix edit** (finding IV.6), **and the portal's callers do not
  change** (`4.0.0_SA_CRO` R3).
  - Today every firm's slice is fetched on the GENERAL route from the general bucket, keyed by a firm id the client
    supplies. `aum.ts`, `portal-proxy.ts` and the Model Portfolios page ask for `/api/general/mdpf/{firmId}/...`, and
    `public-data-router` rewrites that to `/platinum/mdpf/*` in `opal-data-portal-v2` (`index.mjs:51-54`).
  - The portal is frozen, so the transition is a **tenant-asserting compatibility mapping at the edge**, not a caller
    edit:
    - `/api/general/mdpf/global/...` keeps its current general handling, unchanged.
    - Any other firm segment resolves through the registry, aliases included, to one firm. It is served from that
      firm's bucket at the five-segment key to two kinds of session only: a session whose validated tenant resolves
      to that same firm, and an internal Opal staff session (`opal-capital`).
    - For staff the path segment IS the selection, because the frozen portal's firm selector sends no `?firm=` on
      these requests (`ModelPortfolios.tsx:357-358`, Andrew's MDPF_SCOPED.S5: staff keep the selector, no regression).
    - This is the tenancy boundary the scoped router already enforces on `/api/scoped/*` by comparing resolved buckets
      (`shared-advisor-router/index.mjs:367-373` @`40697fe79d`), no wider and no narrower. A bare segment-equals-tenant
      test would refuse the `mockadv` alias and Opal's own staff; FWD-2 asks only that another firm's advisors cannot
      reach the slice.
    - Another firm's session is refused. **Keeping the old URL never keeps general authorization for firm data.**
  - Which CloudFront behaviour and which router function carry it is read from the live behaviours at L5, because the
    brief's Part VII says the scoped router was not re-read. It is portal-auth Terraform, applied by the infrastructure
    lane through `safe-apply`, with never-widen sign-off (CTO and COO) on every served key.
  - **Readiness precedes the switch, per firm:** the mapping is deployed and proven against the slice where it lives
    today, and only then does the origin flip to the firm bucket.
  - The proof runs through the page's own request path:
    - a 49 Financial session loading the Model Portfolios page sees its figures exactly as before;
    - an Inflection session requesting 49 Financial's exact URL is refused;
    - the combined `global` slice still loads for every session that could load it before.
- **DEC-6 The dedicated runner, and who builds its host.** The endpoint left the host's builder as an open question.
  **This project builds it.**
  - It is additive compute: a new principal and its host. MDPF is its only user, and Andrew asked for it by name.
  - Finding IV.11's "compute must not be touched" binds the EXISTING chain, which the runner does not change.
  - Name: one role per firm from `name()` (`mdpf-49f-runner-role` and its siblings). Its only write grant is its own
    firm's `mdpf/{firm}/platinum/*`.
  - Under `LGIC_ENFORCE`'s scope-derived fence, a principal carrying the bucket's firm in its scope slot is admitted
    by construction, so the runner needs no exemption and the fence is never edited for it (the CONTRACTS row).
  - FWD-6 cannot grade until that fence is applied on the template (its cell E5, the sequence's manual gate).
- **DEC-7 FWD-3: the basis is written.** A worker writes `X2_GLOBAL_BASIS.md`: the aggregation level, the minimum
  number of firms in any combined figure, and why no per-account or per-firm row survives into it. The CVO grades it
  at L9. Moving the ledger's X2 row from OWED to GRANTED needs Andrew's acknowledgement, as every register entry has
  had. That is a later card and not a gate on FWD-3, whose bar is that the reason is written and can be pointed at.
- **DEC-8 FWD-7: the bronze move.** `opal-data-mdpf/mdpf/bronze/` (830 objects at the brief's read) moves to
  `opal-data-assets/mdpf/{scope}/bronze/{feed}/...`, and the receiving step is repointed. The step is run on demand and
  its output read where it landed; the next routine delivery landing there confirms it. Removing the old bronze is an S3
  delete, so it is a separate act needing a human's confirmation.
- **DEC-9 FWD-8: the standard is consumed, and its instrument is MISSING.**
  - The two retiring trees are `opal-data-assets/gold/mdpf_revamp/` and `opal-data-assets/portal/gold/mdpf/`. The
    organisation trail's read selector covers `opal-data-49financial`, `-bd`, `-cot` and `-inf` (card 3, validated
    @`231cd62ec5`). **It does not cover `opal-data-assets`.**
  - **A correction to this seat's own endpoint stamp:** it recorded card 3 as closing FWD-8's instrument "on both
    counts". Card 3 named the legacy firm buckets and nothing in `opal-data-assets`, and Andrew's own card said the
    logging *"is billed, which makes it your word"*.
  - **So the instrument for these two trees is one open call at Andrew**: turn on read logging scoped to those two
    prefixes only. REC: yes, scoped to the two prefixes, so its cost is those prefixes' reads and nothing else in the
    estate's largest bucket.
  - Until he rules, cell M11 proves everything but the window, and the window cannot start: data events do not backdate.
  - **The window counts only after every reader is repointed** (the ~03:xxZ reading): a tree the chain still writes
    daily is not quiet.
  - **The hold** (`DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial_20260722.md`, in the COO's custody) is either
    re-pointed at the key its producer reads today (`platinum/mdpf/49financial/aggregate-aua-timeseries.json`, per the
    producer's `:361`), or superseded with the producer's `:476-500` date-join read and cited. It is never cleared on
    the 404 alone.
- **DEC-10 The stale served key** `json/portfolios/aum-timeseries.json` (row G5), unwritten since 07-27, gets its own
  never-widen row: finish the staged repoint, or retire the key with its portal readers named. Not both, and not
  neither.
- **DEC-11 Closed since v1.1.**
  - B1 and B2 stand as ruled.
  - The old s.7.2 (D10-2) is closed, because ~01:3xZ card 2 ruled the spelled-out firm buckets survive and the legacy
    three retire after migration.
  - The old s.8 is superseded by this PRD's decisions and manifest.
- **DEC-12 MDPF_GLOBAL is NOT absorbed.** It is a different product outcome: the Opal-level Global segment taxonomy
  (the `segment_v1` contract, per its register row). Andrew kept it open by name on 2026-08-25 (*"Keep all of them
  open"*). The write-grant question it once held is answered in shape by DEC-6.
- **DEC-13 Cells are cut against the LIVE plane.** The declared trigger map disagrees with the 08-25 inventory on
  MDPF's clock (finding IV.10). No cell reads schedules from the map.
- **DEC-14 Never, in this project:**
  - a change to the conformant compute chain or to platinum's SHAPE;
  - a move of the combined `global` slice;
  - a touch of the frozen rollback objects at `opal-data-mdpf/code/scripts/gold/`;
  - a dual-write, a shadow prefix or a standing comparator;
  - a served key moved without never-widen sign-off;
  - an S3 delete without a human's confirmation and, for the retiring trees, the FWD-8 proof.
- **DEC-15 The key-bearing cells wait on `LGIC_ENFORCE`'s builders.** The emitter and the repoints take their strings
  from `key()` and `address()` (its cell E3). A hand-spelled canonical key in a migration would be the pattern breaking
  in the project built to fix it (that project's brief, Part V). At the three-COO cap, `LGIC_ENFORCE`'s L5 is first in
  the sequence's queue. **So every cell that writes, repoints or runs against a new address waits on it: M2 to M6, M8,
  M9 and M10.** Only M1, a read-only census, and M7, a document, do not. **M6 also waits on row LGIC_NAMING-S7** (`4.0.0_SA_CRO` R4): the code home has two candidate addresses, the brief's root home and the schema's code tier, and the builders cannot follow both. For the accrual bundle they are `s3://opal-data-mdpf/code/mdpf/gold/mdpf-accrual-bridge.tar.gz` (IV.5) and `key("mdpf", "global", "code", "gold", "mdpf-accrual-bridge.tar.gz")`, which is `mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz`. So no new code packaging is written until S7 rules one, and CONTRACTS' "every NEW address comes from `key()` and `address()`" stays true for code as for everything else. The bronze move's read-only part, listing the
  objects and their receiving step, sits in M1; the move itself waits (`4.0.0_SA_CRO` R2).

## PROJECT ARC AND DEFINED OUTCOME

**Defined outcome:**
- Every MDPF figure is dated parquet where the one naming rule puts it: a firm's figures in that firm's own bucket, the cross-firm composite in the product bucket.
- Each firm's served slice is in that firm's own bucket, behind a route that asserts the tenant.
- One publisher reads only the buckets the rule names for the figures it serves, and what people see did not change.
- A dedicated runner writes each firm's slice with the fence untouched.
- The bronze is in the shared intake.
- The two legacy trees are gone, on proof, and the hold is true.

**Arc:**
1. The reader census and the combined slice's basis (M1, M7), which wait on nothing.
2. Then, once `LGIC_ENFORCE`'s builders exist: the emitter and backfill (M2, M3), the bronze move (M8), the repoints
   and seams (M4, M6), and the publisher (M5), last among readers.
3. Then, per firm as `ADVI_FIRMBKTS` delivers: the compatibility route proven first, then the slice (M9); and the
   runner (M10), once the fence is applied.
4. Then the retirements (M11), and the stale key (M12).

It closes when every FWD grades REALIZED.

## CELL CANDIDATES

One row per candidate cell. The decomposition at L5 is the COO lane's, and it may split, merge or re-sequence these.

| cell | serves | brief sections consumed | contracts consumed (C) / produced (P) | paths: reuse | paths: new home | fixtures / evidence | acceptance clause draft |
|---|---|---|---|---|---|---|---|
| M1 the reader census | FWD-5, FWD-8 | IV.2; IV.3; Part V bullet 3; Part VII bullet 1 | -- | `comp-find` over the corpus, unscoped; Terraform; `EC2_MANIFEST.json`; the portal source | `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/READER_CENSUS.md` | every reader and writer of both trees, the served key and the old bronze, each with its evidence line and its instrument; IV.2's 16 definitions and 50 config sites as the floor | every reader the unscoped read finds is listed or excluded with a reason, denominator printed; the instrument is named (a name census proves presence, never absence) |
| M2 the emitter | FWD-1 | O1; IV.1; IV.5; Part V bullets 1-2 | C the key string, `key()` and `address()`; P the gold artifact | -- | the address `address()` returns per scope under R7 (the firm bucket for firm scopes, `opal-data-mdpf` for `global`); never typed here | one partition written for today for every artifact and scope; the twins diffed before convergence | a dated question is answered from a key alone; the emitter writes no string it did not get from the builders; no second write path exists |
| M3 the backfill | FWD-1 | O1; A-3 | P the gold artifact | the current JSON artifacts in both trees | the same prefix | every historical date the JSON holds, one partition each, with the count printed against the source's | the full series is the partition set; no date is rewritten |
| M4 the repoints and the seams | FWD-5 | O5; IV.3; IV.4; AC9 | C the key string | the producer scripts M1 names | -- | one reader at a time; each seam's `/seams` read on the MECHANICAL, DECLARATIVE and SEMANTIC axes, grounded on the DEPLOYED artifact | a search finds no producer writing to, reading from, or running code out of the old places, and the leftovers are history; every seam passes all three axes |
| M5 the publisher | FWD-4 | O4; IV.4; the second final-step obligation | C the gold artifact; P the served JSON | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/` | -- | the served leaves diffed on data-bearing values before and after, with the population named (the brief's three denominators, 522, 492 and 13, reconciled first) | every figure is identical; the publisher reads only `opal-data-mdpf`; it is switched last |
| M6 the code homes | FWD-5 | IV.4; the third final-step obligation | -- | `EC2_MANIFEST.json` (the accrual bundle); the gold Lambda's Terraform and source map | the code home in `s3://opal-data-mdpf/`, at the one address LGIC_NAMING-S7 rules (HELD until then) | per artifact class -- the accrual bundle (runner code, R16) and the gold Lambda's zip (a Lambda artifact: R16 does not reach it and it keeps its source-map tie, but R1 grades its key) -- the packaging declarations changed to the ruled address, never an object hand-copied; the frozen rollback objects listed before and after | no resource pulls code from `opal-data-assets/portal/`; the rollback objects are byte-identical |
| M7 the combined slice's basis | FWD-3 | O3; IV.7 | P `X2_GLOBAL_BASIS.md` | `infra/logic/06_CONFORMANCE_LEDGER.md` X2 | `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/X2_GLOBAL_BASIS.md` | the aggregation level, the minimum firm count, and why no per-firm or per-account row survives | a reader asked why `global` did not move points at the paragraph; the ledger's X2 row cites it |
| M8 the bronze move | FWD-7 | O7; R4 | C the key string, `key()` and `address()` (waits on `LGIC_ENFORCE` E3) | the receiving step; M1's bronze listing | `s3://opal-data-assets/mdpf/{scope}/bronze/` | every destination key generated by `address()`, never typed; the step run on demand; its output read where it landed | the output lands beside every other vendor's, at builder-generated keys; the next routine delivery lands there too, as confirmation only |
| M9 a firm's route and slice | FWD-2 | O2; IV.6; Part V bullet 5 | C the firm's bucket and grants, `key()` and `address()`; P the compatibility route | `public-data-router`, the scoped router and the auth validator at the edge; the live CloudFront behaviours; the portal's callers `aum.ts`, `portal-proxy.ts` and the Model Portfolios page (read, not edited) | `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/` | per firm, after `ADVI_FIRMBKTS` reports that firm's bucket serving; the mapping deployed and proven against today's location before the origin flips; never-widen sign-off (CTO and COO) on every served key | through the page's own request path: a 49 Financial session sees its figures exactly as before; an internal Opal staff session selecting 49 Financial sees the same figures; an Inflection session requesting 49 Financial's exact URL is refused; `global` still loads as before; no portal source is changed |
| M10 the dedicated runner | FWD-6 | O6; IV.8 | C the fence, `key()` and `address()`; P the runner | -- | the runner's host and its per-firm roles | a run for one firm, after `LGIC_ENFORCE` E5 applies the fence; the fence's bytes read before and after | the run writes only builder-generated keys under that firm's `mdpf/{firm}/platinum/`; the fence's bytes are identical before and after, with no exemption row added |
| M11 the retirements and the hold | FWD-8 | O8; IV.9; IV.12 | C the decommission standard | the hold file; the three prior cleanups' kill lists (the negative control) | `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/` | the hold re-pointed or superseded with the producer's read cited; the read instrument's observed-live stamp; the 45-day record per tree, once every reader is repointed | the record shows no reader or writer for the whole stretch on a named instrument; the hold is true; each removal is its own confirmed act |
| M12 the stale served key | FWD-4, FWD-5 | Part V bullet 10 | P the served JSON | `dim_mdpf_aum_timeseries.py`; the portal's readers of the key | -- | the key's portal readers named; one of the two dispositions chosen | the staged repoint is finished, or the key is retired with its readers named; not both |
| M13 the silver-contract step | FWD-5 | IV.4 | C the key string | `data/assets/scripts/silver/mirror_conversion.py` `assert_declared_header`; the vendor template change path | -- | the 2026-08-20 change (commit 17c38a26f2) replayed as the fixture: a bronze-shape change with no silver declaration | a bronze-shape change cannot ship without its silver declaration in the same act; the replayed change is refused before any object is written |
| M14 the served date axis | FWD-4 | O4 | P the served JSON | the cottonwood slice and the global fold; `lib/trading_calendar.py` | -- | the nine non-trading dates on the cottonwood and global axes (row MDPF_COTREMEDIATION-S3), read from the served payloads; never-widen sign-off (CTO and COO) | no scope's served axis carries a non-trading date, or the payload states in a field why two scopes do; the other two scopes are byte-identical before and after |
| M15 the account count's meaning | FWD-4 | O4 | P the served JSON | the publisher; the by-model counts | -- | row MDPF_COTREMEDIATION-S13: cottonwood total 361 against a by-model sum of 542 on 2026-09-29, the other three scopes equal. RULED (batch 71): `account_count_total` means DISTINCT ACCOUNTS in every scope, never the by-model sum; whether cottonwood's 361 is that count is read first | every scope's total is the distinct-account count and the payload names that basis in a field a consumer can read; a scope whose accounts hold more than one model shows total below the by-model sum, stated |
| M16 the run manifest's status | FWD-1 | O1 | P the gold artifact | the gold run manifest writer | -- | row MDPF_COTREMEDIATION-S16 (evidence of 2026-08-26, NOT re-read): reconciliation PASS on a run that built 6 of 12 objects | the status field is computed over the scopes the run set out to build; a run made partial on purpose cannot read PASS |
| M17 the runner's dead stage | FWD-8 | O8; IV.9 | C the decommission standard | the EC2 daily runner's Stage 6 (the parallel revamp stage) and its completion marker `gold/mdpf_revamp/meta/cycle-complete.json` | -- | row MDPF_TAXSMA-S5 as read by `4.0.0_SA_CRO` on 2026-10-01 (`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/ARMED_ROWS_READ_20261001.md`): the stage red since at least 2026-09-18, its marker last written 2026-08-14, the four staged spines written by the Gold function itself; why it first failed is UNMEASURED and is read before anything is removed | the stage is retired under the decommission standard and is NOT repaired: a repaired stage would be a second writer of the staged spines, which M2 forbids; the spines' one writer is named, and the day's served output is byte-identical before and after |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| new | the address `address()` returns per scope for the gold and state tiers under R7 and R21 (`opal-data-{firm}` for the firm scopes, `opal-data-mdpf` for `global`); never typed | M2, M3 | the gold artifact and its state |
| new | the code home in `s3://opal-data-mdpf/`, at the address LGIC_NAMING-S7 rules: the brief's `code/mdpf/gold/...` or the schema's `mdpf/global/code/gold/...` (the accrual bundle and the gold Lambda's zip, by packaging declaration) | M6 | the code home, HELD on S7 |
| new | `s3://opal-data-assets/mdpf/{scope}/bronze/` | M8 | the bronze home |
| new | `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/{leaf}.json` | M9, M10 | each firm's served slice, at the five-segment key |
| new | `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/` (the TREE_DELIVERABLES lane admits only serial folders) | M1, M7, M11 | the census, the basis, the retirement records |
| edit | `data/mdpf/scripts/gold/*`, `data/assets/scripts/gold/build_cottonwood_mdpf_*.py`, the SmartX reader of the combined slice | M4 | the repoints |
| edit | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/` and its Terraform | M5 | the publisher |
| edit | `infra/aws/ec2/EC2_MANIFEST.json`; `gold-lambda.tf`; `lambda-source-map.json` | M6 | the code homes |
| edit | `public-data-router`, the scoped router and the CloudFront behaviours for `/api/general/mdpf/{firm}/...` | M9 | the tenant-asserting compatibility route |
| read | `portal/src/api/endpoints/aum.ts`, `portal/src/api/portal-proxy.ts`, the Model Portfolios page | M9 | the callers whose URLs stay; not edited, because the portal is frozen |
| new | the runner's host and its per-firm IAM roles | M10 | the dedicated runner |
| edit | the hold file | M11 | re-pointed or superseded |
| edit | `docs/architecture/MDPF_CANON_PRD.md` | DEC-1 | the moved notice (landed with this PRD) |
| read | the two retiring trees; `opal-data-portal-v2/platinum/mdpf/`; `infra/logic/06_CONFORMANCE_LEDGER.md`; `infra/logic/02_DOCTRINE.md` | M1-M12 | the substrate |

## BRIEF COVERAGE

**Denominator.** The brief @`fd579d3caf` has **30 headings outside code fences**:
- 9 top-level: the title and Parts 0 to VII;
- 8 outcomes, O1 to O8;
- 12 findings, IV.1 to IV.12;
- `## REFS TO CARRY`.

Each is an entry. Every entry maps to a decision, a cell and an outcome, or carries `NOT CONSUMED` with its reason.

| # | entry | consumed by | outcome |
|---|---|---|---|
| 1 | title / preamble | the preamble above; DEC-14 | all |
| 2 | PART 0 how the blind constraint was honoured | NOT CONSUMED as work: a method record. Its one carried fact (MDPF_GLOBAL's grant question seen and not used) is DEC-12 | -- |
| 3 | PART I heading | structural | -- |
| 4 | O1 vintage from the key; one bucket -- "one bucket" SUPERSEDED for firm-attributable tables by Andrew's call 3 @50d1b9403e (per firm by R7; the composite stays in the product bucket) | DEC-2; M2, M3 | FWD-1 |
| 5 | O2 a firm's slice in its own bucket; another firm refused | DEC-5 (the compatibility route; callers unchanged); M9 | FWD-2 |
| 6 | O3 the combined slice stays, with its reason | DEC-7; M7 | FWD-3 |
| 7 | O4 one publisher, reading only the MDPF store | DEC-4 (last); M5 | FWD-4 |
| 8 | O5 every producer in the MDPF store; no code elsewhere | DEC-3 (AC9 kept); M4, M6 | FWD-5 |
| 9 | O6 a dedicated runner; the fence untouched | DEC-6; the fence and runner rows in CONTRACTS; M10 | FWD-6 |
| 10 | O7 bronze in the shared intake | DEC-8; DEC-15 (M8 waits on the builders); M8 | FWD-7 |
| 11 | O8 both trees gone; the hold true | DEC-9; M11 | FWD-8 |
| 12 | PART II the boundary | CONTRACTS; DEC-1 (b); DEC-6 (the host); DEC-12 | all |
| 13 | PART III the qualitative bar | the ENDPOINT's ACCEPT lines; the acceptance drafts | all |
| 14 | PART IV heading | structural | -- |
| 15 | IV.1 the live trees | M2, M3 (fixtures); M1 | FWD-1 |
| 16 | IV.2 378 mentions; 16 definitions and 50 config sites | M1 | FWD-5 |
| 17 | IV.3 the producers across three trees | M1, M4 | FWD-5 |
| 18 | IV.4 the publisher and the two code artifacts | M5, M6 | FWD-4, FWD-5 |
| 19 | IV.5 the canonical path strings | the key-string row in CONTRACTS (ratified as `LGIC_NAMING` S1; the firm slice's five-segment form and its vector; the historical `global` path bounded out); DEC-1 (c) | FWD-1, FWD-2 |
| 20 | IV.6 firm slices on the general route | DEC-5 (the named callers and their tenant-asserting mapping); M9 | FWD-2 |
| 21 | IV.7 the combined slice's basis owed | DEC-7; M7 | FWD-3 |
| 22 | IV.8 the runner's name | DEC-6; M10 | FWD-6 |
| 23 | IV.9 the hold names a missing key | DEC-9; M11 | FWD-8 |
| 24 | IV.10 the trigger map disagrees | DEC-13 | FWD-5 |
| 25 | IV.11 compute and platinum shape conformant | DEC-1 (b); DEC-14 | all |
| 26 | IV.12 three prior cleanups | M11 (their kill lists as the negative control); M2 (the producer's output replaced, which no kill list can do) | FWD-8, FWD-1 |
| 27 | PART V what must be true | the path string (CONTRACTS); the emitter right first time (DEC-2); readers named first (M1, M11); the publisher last (DEC-4, M5); per-firm slice gates (DEC-5, M9); the runner's name (DEC-6); the basis (DEC-7); the hold (DEC-9); the frozen rollback (DEC-14); the stale key (DEC-10, M12); B1 and B2 (DEC-11) | all |
| 28 | PART VI status | NOT CONSUMED: not outcome-bearing; its figures are re-read in M1 | -- |
| 29 | PART VII what the brief does not claim | no producer traced (M1 names its instrument); schedules not re-read (DEC-13); the scoped router not re-read (M9 reads it first); three platinum denominators (M5 reconciles them); the date-join not read (DEC-9, M11); the basis not drafted (M7); the twins not diffed (M2). Effort: NOT CONSUMED, and no estimate is made here | all |
| 30 | REFS TO CARRY | NOT CONSUMED as work: a link list. Its WAITING-ON items are closed: the path string (`LGIC_NAMING` S1), the runner's name (DEC-6), the basis (M7), the directive home (D8, ruled), MDPF_GLOBAL (DEC-12) | -- |

## SURFACE MANIFEST

Surfaces this project writes, reads or executes.

| surface | kind | cell | owner |
|---|---|---|---|
| the gold and state addresses `address()` returns per scope under R7 and R21 (`opal-data-{firm}` for the firm scopes, `opal-data-mdpf` for `global`; never typed); the code home at the address LGIC_NAMING-S7 rules | new objects, and packaging declarations for the code (held on S7) | M2, M3, M6 | MDPF_CANON |
| `s3://opal-data-assets/mdpf/{scope}/bronze/` | new objects (the bronze move) | M8 | MDPF_CANON |
| `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/` | APPLIED: the served slices move to the five-segment key; never-widen sign-off per served key | M9 | MDPF_CANON, per firm, after `ADVI_FIRMBKTS` delivers that firm |
| `public-data-router`, the scoped router and the CloudFront behaviours for `/api/general/mdpf/{firm}/...` | APPLIED: the tenant-asserting compatibility route; `global` unchanged | M9 | MDPF_CANON, through the infrastructure lane |
| the portal's callers (`aum.ts`, `portal-proxy.ts`, the Model Portfolios page) | read only: their URLs stay, because the portal is frozen | M9 | -- |
| the publisher Lambda and its Terraform | APPLIED: the port to parquet | M5 | MDPF_CANON |
| the producer scripts; `EC2_MANIFEST.json`; `gold-lambda.tf`; `lambda-source-map.json` | edits | M4, M6 | MDPF_CANON; deploys ride their owners' paths (Rule 13) |
| the runner's host and its per-firm IAM roles | APPLIED: new compute and principals | M10 | MDPF_CANON, through the infrastructure lane |
| the per-firm gold-writer roles and their trust on `mdpf-gold-lambda` | APPLIED: new principals, one write grant each (firm gold prefix) | M2 | MDPF_CANON, through the infrastructure lane |
| the hold file | an edit | M11 | its custodian, under the order |
| `docs/architecture/MDPF_CANON_PRD.md` | the moved notice | DEC-1 | 1.0.0_SA_CTO |
| `org/missions/D8/MDPF/MDPF_CANON/deliverables/<author serial>/` | documents | M1, M7, M11 | MDPF_CANON |
| the two retiring trees, the old bronze prefix, and the stale served key | REMOVALS: each its own act, with a human's confirmation, and for the trees the FWD-8 proof | M8, M11, M12 | MDPF_CANON |
| the conformant compute chain; platinum's shape; `platinum/mdpf/global/` EXCEPT the FWD-3 fold objects and the FWD-9 history leaf (`category-views-history`), each under its own never-widen pair (v2.17); the frozen rollback objects; B2's JWT read; `opal-data-demo`'s slice beyond the demo-tenant ruling | excluded | -- | untouched |

## L10 ADDENDUM, v2.11, 2026-10-11 -- sequencing against ADVI_FIRMBKTS (`1.0.0_SA_CTO~DELL1`, carrying cluster-lead rulings R1-R5)

**Source:** Andrew-direct ~18:1xZ ("we need to make sure that sequencing/dependency order does not cause breaks"), and the cluster lead's
ruling, `1.0.0_SA_CTO` (laptop) record `ANDREW_DIRECT_20261011_181xZ_FOUR_QUESTIONS_FIRMBKTS_CANON_SEQUENCING_CVO_ONLINE_COO_C_MODEL_POLICY_READ.md`
s.5 (box/laptop @7a7e9b47c6). The `/legacy-transform` runs are `workflows/legacy_transform/mdpf/20261011T181700Z-98fc86e/` (573 rows, 484 tensions,
contract ACCEPT) and `workflows/legacy_transform/blackdiamond-49financial/20261011T181009Z-27c2695/` (453 rows, 349 tensions, contract ACCEPT).

- **R1, ONE wording of the wait.** This project's per-firm wait on ADVI_FIRMBKTS is the ROUTER FLIP: that firm's act-4 flip and its first-hour read.
  It is not "the cutover" or "the bucket serves". Lines :50, :196 and :371 read in that sense from v2.11. M9 for Inflection waits on ADVI_FIRMBKTS
  F8 (Andrew's FWD-7/8), not on F4.
- **R2, shared files have ONE owner until the flip lands.** `shared-advisor-router`, the guard, the CloudFront behaviours,
  `data/mdpf/config/bronze_homes.json`, `firm-config.mjs` and the portal-auth WAF rider are ADVI_FIRMBKTS's write surface through act 4 and
  its read-back. This project touches none of them before that. Ownership passes per file by a line in ADVI_FIRMBKTS's flip receipt.
- **R3:** the `mdpf/{firm}/platinum/*` serving grant is ADVI_FIRMBKTS's named cell, cut BEFORE M9. M9 does not infer it.
- **R4:** the joint census of MDPF readers of `opal-data-bd`, `-inf` and `-cot` is a precondition of ADVI_FIRMBKTS F12's 45-day clock per bucket.
  Measured at this addendum: the MDPF principals reaching `opal-data-bd` are N = 3 (`mdpf-daily-runner-ec2-role`, `mdpf-feeder-trigger` and its
  role). Their grants there are five prefixes: `gold/aua_certification/`, `investor-reporting/directory/`, `schwab/silver/rps/`,
  `silver/allocations/`, `silver/fees/`. NONE is among the 11 classes act 2 moves, so Monday's acts freeze nothing MDPF reads.
  `investor-reporting/directory/` couples this project to IRPT_BCKEND's directory move (ADVI_FIRMBKTS D1-S24) and to F12's retirement of
  `opal-data-bd`: it is named in the census.
- **R5:** `ledger/ROUND_ANALYSIS.round4.md:31` ("round 3 holds the 49 Financial cutover") is wrong. The flip is ADVI_FIRMBKTS round 4 and has not
  run; it is corrected in the round-5 analysis.

**Not changed:** every ENDPOINT outcome. The CONTRACTS row at :196 is reworded, not narrowed (proportionate sign-off: no re-sign withheld).

## L10 ADDENDUM, v2.12, 2026-10-13 -- FWD-9: the AUA Trend groups custom models and strategy groups (`1.0.0_SA_CTO~DELL1`)

**Source:** Andrew-direct ~18:4xZ at the dell2 terminal, during his localhost:5174 smoke of portal DEV `f6ef1d25`. Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_184xZ_MODEL_PORTFOLIOS_AUA_TREND_GROUP_CUSTOM_MODELS_AND_CHIPS.md` @5e80d5eb9b, on origin/box/dell2 and
reaching dell1 at the next integrator pass. It was read here from `origin/box/dell2`. The owner is MDPF_CANON (relayed by MSTR msg 5064).

- **New outcome FWD-9** (ENDPOINT above). It is presentation of a page already on PROD: the grouping and colors reuse the Total Assets breakdown's, so no new color is needed.
- **CORRECTED** (`2.0.0_SA_COO~D1` msg 5071, `deliverables/2.0.0_SA_COO~D1/round7/FWD9_GROUPING_READ.md` @1c9f519b6f): "no new data" is TRUE for Custom Models, ALT and ETF
  Strategies, but NOT for the two Client chips.
  - The time series carries no per-date supervised/unsupervised split; only 21 dated category-views objects carry it (2026-08-27 to 2026-10-12), against 495 time-series
    dates.
  - **Ruling (i):** the Client chips draw on the dated objects only, and read absent before and between them (exactness: no back-cast, no interpolation).
  - No new served key is minted for history. The series grows as the dated objects accrue.
- **Where the grouping happens:** server-side, if the served payload is what the chart iterates, so the page does not invent groups. Otherwise in the portal component, reusing
  the Total Assets breakdown's grouping function. The cut names which, and reuses rather than re-implements (build ladder step 2).
- **Client-facing:** Model Portfolios is open to partner firms. The PROD promote of this change waits on Andrew's word, carried as a card with the before/after, beside the
  FWD-3 `/portfolios` card. It is not a blocker of any other promote.
- **Sequencing:** round 6 is executing, so this enters at the round-6 L10 as a round-7 item beside the frontier account counts.

**L4-R:** an ENDPOINT change, so the ratified-text half is re-owed to `3.0.0_SA_CVO`. The brief half is accepted (Andrew's own words).

-- 1.0.0_SA_CTO~DELL1

**v2.13 (2026-10-13 ~19:1xZ), on `3.0.0_SA_CVO`'s REFUSAL of v2.12** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_MDPF_CANON_v2.12_RATIFIED_TEXT_20261013.md`
@1337ef5c75). FWD-9's DONE WHEN is rewritten to take all seven items:
1. the draw is named (dates A to D);
2. the comparison is to the cent against the served members;
3. membership, colors and labels are cited by path and line;
4. the Client source is unchanged (ruling (i));
5. **the stack composition is defined.** The CVO measured Supervised plus Unsupervised about 21-23M short of `non_model_aua` on 3 of 3 dates, so the Client chips SPLIT
   non-model AUA with an explicit "Other AUA" remainder and never sit on top of it. The whole stack sums to `opal_aggregate_aua`. At Global, Custom Models absorbs
   FWD-3's pooled "Other Models";
6. the absent observable is named, and "-$0" is ruled out;
7. the build mechanism is named.

**Andrew's PROD card carries:** "Client chips: 21 of 495 dates, from 2026-08-27", and the "Other AUA" remainder with its size on the frontier date.

-- 1.0.0_SA_CTO~DELL1

**v2.14 (2026-10-13 ~19:2xZ), on `3.0.0_SA_CVO`'s REFUSAL of v2.13** (review ADDENDUM @556bc01b3e; measured overshoot 21,121,201.39 on 2026-10-09 and 22,794,766.25 on
2026-08-27, equal to the two carries to the cent):
- (a) ETF stacks `pfde` only. The two carries are not drawn, and are not carved out of Other AUA, since no measured rule exists and none is estimated.
- (b) ALT stacks `tax_additive_aua` only.
- (c) The sum-to-Total arm states the fold-suppression exception, read from the fold's record.

-- 1.0.0_SA_CTO~DELL1

**v2.15 (2026-10-13 ~19:2xZ), on `2.0.0_SA_COO~D1`'s three FWD-9 forks (msgs 5086-5088):**
- **Fork 2: ETF Strategies = `pfde` plus the two carve-out SMA lines, carved out of `non_model_aua`.** This REVERSES v2.14 (a). The issuer measured the CVO's 21-23M Client gap
  equal, to the cent, to the two carve-out lines on both sampled dates. So a measured rule exists: the carve-outs are exact served members, and ETF then matches Total
  Assets' grouping. The stack still sums to the Total.
- **Fork 1: the Client chips need a served history route.** It is a READ-ONLY route over the existing dated objects: no new data, and not the "new served key for history"
  ruling (i) refused, which was a back-cast. It is cut as its own cell under its own pair, and FWD-9 is graded with it live. The cell may ship the chips as-of only first;
  that interim is not the grade.
- **Fork 3: ALT on the Trend stays `vermilion500`.** Andrew's 2026-10-01 word, "we canonically use vermillion for alts", is his latest on alts; the 10-13 instruction pins
  only the Custom color, and "the Total Assets colors" for the four chips was the recorder's reading. The pin test stands. **Noted for Andrew** (no change here): Total Assets
  itself colors ALT `green400` (2026-09-15), which disagrees with his 10-01 canon.

-- 1.0.0_SA_CTO~DELL1

**v2.16 (2026-10-13 ~19:2xZ), on `3.0.0_SA_CVO`'s REFUSAL of v2.15** (review ADDENDUM @dbba589a4c):
- (i) The measurement is restated truthfully: the gap equals the carve-outs to the cent on 2026-08-27 only, and lies within -4,649.20 to +301,207.84 over the 21 dates.
- (ii) A negative remainder reads ABSENT, with no clamp, and its size is printed as the date's basis difference. The sum-to-Total arm states that the stack exceeds the Total by
  exactly |remainder| there.
- (iii) Date E (2026-09-30) is a named arm.
- **Noted for a later cell, not FWD-9:** why the category-views snapshot and the time series disagree by up to about 300K on the same day. Cause not established.

-- 1.0.0_SA_CTO~DELL1

**v2.17 (2026-10-14 ~16:2xZ), on the CN-j-1 publisher pair's item 3 (`2.0.0_SA_COO~D1` msg 5640; CTO half `ledger/NEVER_WIDEN_R7_J1_PUBLISHER_CTO_HALF.md` @9a492909b7):**
- (i) The scope row that excluded `platinum/mdpf/global/` wholesale predated FWD-3's fold and FWD-9's route. It now excludes it EXCEPT the FWD-3 fold objects and the FWD-9 history leaf, each under its own pair. The ENDPOINT governs; this aligns the row to it.
- (ii) The CONTRACTS row for the served platinum JSON now names `category-views` and the derived read-only `category-views-history` leaf, both produced by the publisher alone.
- No ENDPOINT text moves. The CONTRACTS change re-opens the ratified-text half for `3.0.0_SA_CVO`; the brief half is untouched.

-- 1.0.0_SA_CTO~DELL1

**v2.18 (2026-10-14 ~18:5xZ), on `2.0.0_SA_COO~D1` msg 5715 (`round7/STACK_SUM_MEASURE_20261014.md` @caec08b05f; the CVO's D1-C-S73 stack-sum finding):**
- On all 383 dates before `per_model_detail_begins` (2026-05-15) the stack misses the whole model AUA ($437M to $1.35B), because the FWD-3 fold suppresses every model line held by fewer than two firms.
- **Ruled: exception (ii) covers those dates. The amount is NOT drawn as a band** (the issuer's REC (iii)). A band of suppressed model dollars would draw exactly what FWD-3 forbids. The page states the boundary in words, and the gap is printed by the readback.
- ENDPOINT text moves (FWD-9 clause (2)), so the ratified-text half is re-owed to `3.0.0_SA_CVO`.

-- 1.0.0_SA_CTO~DELL1

**v2.19 (2026-10-14 ~20:4xZ), on Andrew's /portfolios smoke and his Variant 1 word:**
- Records: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73 (+ addendum 1 @c0d1b030bf), and `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_204xZ_MDPF_GLOBAL_TREND_VARIANT_1_AND_SATELLITE_GLD_RETURNS.md` @ab28358b88.
- VERBATIM: "If we're going to do it like this, breaking all this stuff out, then we have to figure out how to render it historically ... if we are missing totals on any given day, just roll forward last known values"; and "Call 3, only opal staff see global, that is correct. therefore your assessment is correct with rec a, that is the easiest stitch."
- **The v2.18 exception (ii) for the dates before 2026-05-15 is RETIRED at Global.** FWD-9 carries the v2.19 OVERRIDES (a)-(d) at its head. The rule table, the identities and the period-end oracle are the CRO spec @8025c4d7f1 (Variant 1). They are cited, not restated.
- **FWD-3 is unchanged for every served leaf except this one.** The Global Trend's history may show single-firm model lines: 49 Financial before 2026-05-15, and Inflection's Custom from 05-15 to 07-19. That rests on Andrew's stated fact that only Opal staff can open Global. If a partner login can ever open Global, this exception lapses.
- **Where it lands:** the producer (`mdpf_gold_consolidator`) emits the pre-05-15 per-model values, Custom by difference, and the `carried` rows, under a never-widen pair, with every Global leaf read before and after and the headline sums byte-equal. Then the portal (`trendGrouping.ts`, `ModelPortfolios.tsx`), on a client-facing row for Andrew. Two composition steps stay and are footnoted: Inflection enters on 05-15, and Cottonwood enters on 05-28, interpolated to 07-20.
- ENDPOINT text moves (FWD-9 head), so the ratified-text half is re-owed to `3.0.0_SA_CVO`.

-- 1.0.0_SA_CTO~DELL1

**v2.20 (2026-10-14 ~20:4xZ), on `3.0.0_SA_CVO`'s refusal of v2.19 (msg 5865; `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_MDPF_CANON_v2.19_RATIFIED_TEXT_20261014.md` @897fe1d0d1):**
- The CVO measured on PROD 5ab67a651a that the external demo tenant opens Global (`ModelPortfolios.tsx:271`, `:375-379`; `firmAccess.ts:115-117`). So "only Opal staff see Global" does not hold for every session.
- **Ruled: the CVO's option 3, built as a READ-SIDE stitch.** The pre-2026-05-15 per-model lines, and Custom from 05-15 to 07-19, draw only for an internal session. They are read from the single firm's own served series (49 Financial; Inflection), which an internal session may already read. The Global served leaves keep FWD-3's fold and gain no single-firm value. So a non-internal login cannot reach those values through the page or through the Global API. That session keeps v2.18 exception (ii) and draws one Models band. Option 3 needs no Andrew word, and it keeps his Variant 1 for every staff session, which is the audience he named.
- **Consequence for "Where it lands" (v2.19):** the producer cell no longer emits pre-05-15 per-model values into a Global leaf. Client Supervised by difference, ETF/ALT and `carried` remain. `carried` rows written into the Global leaf are a served change under a never-widen pair. The stitch is portal work, on a client-facing row for Andrew.
- **Rule table and oracle:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @8025c4d7f1 (Variant 1 for an internal session; Variant 2 for every other session).
- Per the CVO's secondary note, provenance moved out of ENDPOINT. ENDPOINT text moves, so the ratified-text half is re-owed.

-- 1.0.0_SA_CTO~DELL1

**v2.21 (2026-10-14 ~20:5xZ), on the Global Trend spec amendment 1 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @686f769e63; CRO msg 5869):**
- Andrew, VERBATIM (at the `4.0.0_SA_CRO~DELL1` terminal): "Close but we might as well put the SMA strategies in there, we do have them" / "no muni in SMAs, Muni is no longer SMA" / "muni is just a custom model".
- FWD-9's head gains (e), and (b) is restated. The SMArtX `closing_equity` equals the served carve-outs to $0.00 on all 103 overlap dates, so Client Supervised is continuous across 2026-05-18, and the partition stays exact on 487 dated rows (the amended oracle in the spec).
- The SMA strategies are Opal products, which FWD-3's fold already reads as held at no firm (the fe9b ruling). They therefore draw for EVERY session, not only internal ones.
- **Where it lands, added:** a new SMArtX read in `mdpf_gold_consolidator`. Its key is checked against the naming gate and the registry before the commit; a refusal is a registry row (the XA-ad15 precedent). The category tree drops "Muni SMA" from `SMA > ALT Strategies`. That is a served change to category-views, under the same never-widen pair.
- ENDPOINT text moves again before the CVO's signature, so one re-sign covers v2.20 and v2.21.

-- 1.0.0_SA_CTO~DELL1

**v2.22 (2026-10-15 ~14:4xZ), on the CVO's round-9 L10 slug (msg 6035; `ADJUDICATION_v15.md` @f0bdabc5c2, `ADJUDICATION_v16.md` @fbbe2b1283):**
- CN-j-1 AC4 graded NOT MET (C-S83): no portal code reads `category-views-history`, so the Client chips draw on the as-of date only.
- **Ruled: the reader requirement is retired, not built.** v2.19-v2.21 already removed the Global reader: Client Supervised comes from the Global difference, and Client Unsupervised and the chips are retired at Global. CN-j-2 was withdrawn on a reader census of 0 across base, DEV and PROD.
- At the firm scopes, Andrew approved the as-shown view ("49 Financial View: No comments, everything is good to go"; "Inflection view: No need to touch these"; record `ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73), and that view draws the chips on the as-of date only. His Cottonwood Trend upgrade decides any firm-scope history design.
- **The history leaf stays served** (read-only, no reader) until that addendum keeps it or retires it under its own pair. FWD-9's head states this. CN-j-1 AC4 is closed by this amendment.
- ENDPOINT text moves (FWD-9 head), so the ratified-text half is re-owed to `3.0.0_SA_CVO`.

-- 1.0.0_SA_CTO~DELL1

**v2.23 (2026-10-15 ~18:5xZ), the Cottonwood Trend addendum, Muni, and the demo session (`1.0.0_SA_CTO~DELL1`):**
- **Records, VERBATIM:**
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_152xZ_MUNI_IS_CUSTOM_MODELS_EVERYWHERE.md`: "Muni is in Custom Models, yes".
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_184xZ_HAPPYLAND_MUNI_IS_CUSTOM_MODEL_OPAL_MUNICIPAL_BONDS.md` @fee736b125
    (laptop): "the happyland ventures Muni portfolio should be considered a Custom Model, Opal Municipal Bonds; it's with Cottonwood. It should be
    included in the Agggregate "Custom Models" group in the global view."
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_162xZ_DEMO_GLOBAL_TREND_USES_VARIANT1_NEXT_PROMOTE.md` @25ef8b9c1a:
    "let's just make the Demo View see the same thing as the global view ... just use the same code as global view" and "it should get added on
    to the next prod promote of the portal."
- **FWD-9 head (f), the Cottonwood Trend.** It is the CRO spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_COTTONWOOD_AUM_TREND_UPGRADE_SPEC_20261015.md`
  @21caa664be, BASE ONLY. The 2026-04-22 extension is not taken: the ramp is custody arriving, not growth, and it would add a cross-product read.
  The spec's rule table and month-end oracle are cited, not restated. The 12 carried model-leg dates are emitted as `carried`, by the producer or
  read-side, whichever the decomposition picks. A producer emission is a served change under a never-widen pair.
- **FWD-9 head (g), Muni.** Opal Muni Income (about $64M, one Cottonwood account, `custom_residual_detail` Opal_Muni_Income) moves from
  Cottonwood's `income_non_model_residual` into `by_model` / `model_aua`. It moves into Custom at Global through the sums. Its display name is
  "Opal Municipal Bonds".
  - Only Muni is named; the 2026-09-21 rule (`build_cottonwood_mdpf_slice.py:933`) stands for every other auto-classified Opal-named model.
  - **Identity check before the move:** the cell confirms that the Opal_Muni_Income account is the Happyland Ventures account, printing a match
    flag and no name. If it is not, the cell stops and reports; nothing wider is inferred.
  - A served change at Cottonwood and Global, under a never-widen pair.
- **FWD-9 head (a), the demo tenant.** A demo-tenant session draws the Global Trend with the internal session's code (Variant 1).
  - **Amended ~19:0xZ, on `3.0.0_SA_CVO` msg 6133** (`L4R_REVIEW_MDPF_CANON_v2.23_RATIFIED_TEXT_20261015.md` @8dc11dc359): a non-internal
    claim with no firmId still opens Global on Variant 2 (`effectiveFirmId = claims?.firmId ?? 'global'`), and ENDPOINT's partition binds it.
  - So round 11 ALSO repairs Variant 2 in one condition: the Models band is never carried forward on or after `per_model_detail_begins`
    (`trendGrouping.ts` roll-forward loop).
  - The repair's test reads the real served object: 0 of 497 rows draw both the band and the model stack, and the drawn groups do not sum above
    the Total.
  - D1-S29 disarms when both changes are on DEV.
  - Variant 1's pre-2026-05-15 lines read 49 Financial's own served series, so a demo session sees them. Andrew was told this the same turn.
  - If the per-firm edge gate (`auth-validator-edge`) refuses a demo session that read, those lines draw nothing for demo. The cell reports
    that; it never widens the gate.
  - Lands on DEV and rides the next portal PROD promote (client-facing, Andrew's word).
- **The category-views history leaf** stays served and read-only, with no required reader. Its retirement is not ordered.
- **Placement:** round 11 cut, after round 10's drain. ENDPOINT text moves (FWD-9 head (a), (f), (g)), so the ratified-text half is re-owed to
  `3.0.0_SA_CVO`.

-- 1.0.0_SA_CTO~DELL1

**v2.24 (2026-10-17 ~01:4xZ), FWD-10, Cottonwood Supervised-only (`1.0.0_SA_CTO~DELL1`, on `4.0.0_SA_CRO~DDD` msg 7097):**
- **Input:** `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/COTTONWOOD_SUPERVISED_GAP_FINDINGS_20261017.md` @f67b4711f1. Andrew's word is the
  outcome itself, so it is added at the next unused number. FWD-1 to FWD-9 are untouched.
- **Ruled, (a), the build: ACCEPTED as the CRO proposes.** `build_cottonwood_mdpf_slice.py` `holdings_total_by_date` reads
  `Account Supervised` and keeps `Supervised` before the collapse and the sum. One filter, at the one producer of Cottonwood's totals, so the
  headline, the breakdown and the Trend's `partner_custody_total` all move together. Cottonwood only. An edit that makes "the firms
  consistent" is refused (`mdpf_category_registry.py` :818-858).
- **Served move:** a never-widen pair, the COO half first. Blast radius: Cottonwood's slice and the Global composite. Every Global leaf is
  read before and after, and 49 Financial and Inflection must be byte-identical. Both branches are named:
  - the model or SMA leg moves (an Unsupervised account carries a model on the build date), so the cell stops and reports;
  - it does not move.
  Rollback: a per-key prior VersionId.
- **Timing:** not on the fire that D1 reads for CN-s-1 V2 (2026-10-17 13:30Z), because one change lands per fire. It is round 12's first
  cell, issued when round 11 drains (CN-s-3 and CN-s-5 are open).
- **Ruled, (b), the $8.86M gap:** it is inside BD, between the Dashboard and the DataMining exports, and was measured before (-8,697,205.48
  on 2026-08-19, `D_05.supervised_split.py:57-68`). Route 1 is taken: one Dashboard export by relationship, from Andrew's own BD login. That
  login is his act. The CRO diffs it against the export in the same turn. Route 2, the vendor question, goes out only if route 1 does not
  name the accounts. Until then, the source-line wording in FWD-10 holds.
- **Portal:** the source line is a client-facing page change. It goes to DEV and waits for Andrew's word before PROD.
- **Ratified-text half re-owed** to `3.0.0_SA_CVO` (an ENDPOINT change).

-- 1.0.0_SA_CTO~DELL1

**v2.25 (2026-10-17 ~01:5xZ), FWD-10 (b) located (`1.0.0_SA_CTO~DELL1`, on `4.0.0_SA_CRO~DDD` msg 7119; change log only, ENDPOINT unchanged):**
- **Input:** the findings ADDENDUM 1 @2c373db08e. The $8,860,829.31 gap is 96 insurance and annuity carrier-feed accounts (DTCCR_ 78, ASLAA_
  13, AEGON_ 3, LNANN_ 1, EQUIT_ 1). The BD Dashboard counts them; the DataMining exports we ingest do not return them. The other 753
  supervised accounts tie at $0.00.
- **Ruled, the display: the 96 COUNT in Cottonwood's supervised total.** Andrew's 2026-10-17 word, "matches that ... number", is later and
  more specific than the 2026-08-24 Insurance exclusion, which gave the reason "we don't take fees on it". 78 of the 96 carry a BD management
  fee. Scope: Cottonwood only. The 49 Financial and Inflection insurance treatment is unchanged. Andrew may reverse this; FWD-10 (b) then
  reads 521.56M with "excluding $8.86M insurance" stated on the page.
- **Ruled, the ingest:** widen Cottonwood's DataMining account set, or its holdings, allocations and attributes templates, to return the
  insurance-feed accounts. Placed in ADVI_COTBKF (Cottonwood's served data), whose next round cuts it. Proof: the 10/15-equivalent build ties
  to 530,421,988.14 supervised. FWD-10 (b) closes on that proof plus the FWD-10 (a) cell.
- **Order:** the (a) filter cell in round 12 does not wait on the ingest. The source line reads per FWD-10 until (b) ties.

-- 1.0.0_SA_CTO~DELL1

**v2.26 (2026-10-17 ~01:5xZ), FWD-10 executed ad hoc (`1.0.0_SA_CTO~DELL1`, on `4.0.0_SA_CRO~DDD` msg 7124; change log only):**
- **Andrew-direct ~01:5xZ** (record `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/ANDREW_DIRECT_20261017_015xZ_COTTONWOOD_530M_MDPF_AND_ADVI_CRO_EXECUTES.md`
  @aca8db2e43): "We want that 530.42m number ... it has to be done for ADVI Advisor Intelligence page too ... probably have you just do it."
  The target is 530.42M, so the 96 insurance-feed accounts count (v2.25 confirmed on his word).
- **Placement superseded:** FWD-10 is NOT round 12's first cell, and the ADVI_COTBKF widen cell is not a next-round cut. `4.0.0_SA_CRO~DDD`
  executes both directly. The never-widen pair and the apply gate still apply: the CRO brings the producer half, and this seat signs the CTO half.
- **Two collisions the half must name:**
  - D1 reads the CN-s-1 V2 Global headline on the 2026-10-17 13:30Z fire against a predicted 2,237.50M. A Cottonwood filter landed before
    that fire moves the same headline. The half states the joint expected Global for that fire, and 2.0.0_SA_COO~D1 reads against it.
  - The Cottonwood silver `account_attributes` organic fire (~2026-10-17 midday, R106) reads the same accounts. Nothing writes Cottonwood
    silver between now and that fire's close read, unless 2.0.0_SA_COO~C1 agrees in writing.

-- 1.0.0_SA_CTO~DELL1

**v2.27 (2026-10-17 ~02:2xZ), ERRATUM to v2.24 and v2.26 on Global (`1.0.0_SA_CTO~DELL1`, on `4.0.0_SA_CRO~DDD` msg 7144; change log only):**
- **The Global headline does NOT move with FWD-10 (a).** Global's Client (non-model) leg is 49 Financial only
  (`dim_mdpf_aggregate_aua_timeseries.py:2294` `GLOBAL_CLIENT_CONSTITUENTS = ("49financial",)`, basis B, read by this seat). Cottonwood enters Global
  only through its model and SMA-additive legs, and the switch moves neither (0 of 130 Unsupervised accounts holds a model). The fold uses the
  in-run Cottonwood leg (`mdpf_gold_consolidator.py:2966-2980`), not a staged key.
- **Struck:** v2.24's "Global's total falls by the same $33.07M", the CVO's v2.24 carry (Global and Global Client Supervised about -$33.07M
  each), and v2.26's joint figure (`2,237.50M - U_cot`). The CN-s-1 V2 prediction of 2,237.50M stands for the 2026-10-17 13:30Z fire. The
  deployed QA read gives 2,237,501,378.84.
- **FWD-10's ENDPOINT clause** "the Global composite folds Cottonwood's supervised book through its sums" stays true, and moves nothing at Global
  today. The never-widen pair's Global before/after print still applies, and should read equal.

-- 1.0.0_SA_CTO~DELL1
