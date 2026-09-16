# MDPF_CANON -- the MDPF canon migration: gold as dated parquet in opal-data-mdpf, each firm's served slice in that firm's own bucket, one publisher, and two legacy trees retired only on proof

```json
{
 "project": "MDPF_CANON",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v2.4",
 "step": 4,
 "brief_ref": "docs/briefs/d8-mdpf-canon-migration-brief-20260913.md@fd579d3caf",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "RATIFIED"
}
```

**v2.0 is this PRD MOVED into its tree home and brought current in the same act.** v1.0 and v1.1 lived at
`docs/architecture/MDPF_CANON_PRD.md` (@`dfc492aa83`, @`6f53713982`, rulings folded @`6e0a07d934`), had no PRD header,
and were never decomposed because the project was never registered. That path now carries a moved notice. Its three
stale items are amended here (DEC-1), and its founding content -- A-1 to A-3, rows B1 and B2, and the three
final-step obligations -- is carried forward below.

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
- Its FWD-2 and FWD-6 wait per firm on `ADVI_FIRMBKTS`'s cutover, and FWD-6 also waits on LGIC_ENFORCE's fence (its
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
         kept, and every one of them is kept in the one place built for them
         DONE WHEN  EXERCISED -- someone has actually answered a dated question this way
         ACCEPT     asked "what did 49 Financial's total assets read on a particular day
                    last month", someone answers from the name of the stored file alone,
                    without opening it -- and every stored figure of this kind is in the
                    same one place, full history, one addition per day -- where today the
                    same figures sit in two places under two different naming habits, and
                    the place meant for them is empty
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
```

## CONTRACTS

| contract | direction | shape | consumer / producer |
|---|---|---|---|
| the canonical key string, MDPF's instances | **consumed** (ruled) | `{source}/{scope}/{tier}/{table}/{partition}`, verbatim, with `{source}` = `mdpf` and `{scope}` one of `49financial`, `inflection`, `cottonwood`, `global`, `demo` in the LONG form. The instances: gold at the address `address("mdpf", {scope}, "gold", {artifact}, "date={YYYY-MM-DD}")` returns under R7 -- measured at HEAD: `s3://opal-data-49financial/`, `s3://opal-data-inflection/`, `s3://opal-data-cottonwood/` for the firm scopes and `s3://opal-data-mdpf/` for `global` only (X2's composite branch), `demo` as the builder returns it -- never a typed bucket (Andrew-direct 2026-09-16 ~18:2xZ, call 3: "(a), yes. Should be using LGIC_NAMING patterns in both cases"; this replaces the typed `s3://opal-data-mdpf/mdpf/{scope}/gold/...` instance that contradicted the same sentence's builder mandate, the CVO's finding); state `s3://opal-data-mdpf/mdpf/{scope}/state/...` (R21); bronze `s3://opal-data-assets/mdpf/{scope}/bronze/{feed}/...` (R4); a firm's served slice `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/{leaf}.json` (R7), where `{table}` is the snake_case artifact and the partition slot holds the schema's "named leaf" form: the kebab-case served file itself. The vector: `key("mdpf", "49financial", "platinum", "aum_metrics", "aum-metrics.json")` returns `mdpf/49financial/platinum/aum_metrics/aum-metrics.json`, and `address()` over the same arguments returns it under `s3://opal-data-49financial/`. **Every NEW address comes from `LGIC_ENFORCE`'s `key()` and `address()`, never typed.** The one exception is the combined slice `s3://opal-data-portal-v2/platinum/mdpf/global/...`: it is historical, tier-first, and stays exactly where it is (X2), so no builder produces it and nothing moves it to satisfy this row | ruled by Andrew ~03:2xZ and ratified as `LGIC_NAMING` S1; the builders are `LGIC_ENFORCE`'s |
| the gold artifact | **produced** | parquet only; one partition per day, carrying its date in the key; the full history backfilled from the current JSON to the extent it exists; history is never rewritten. The artifacts are `account_distribution`, `account_units`, `aggregate_aua_timeseries` and `aum_metrics` (snake_case) | the publisher; any reader that needs a figure's vintage |
| the served platinum JSON | **produced**, by the publisher alone | the leaves `aggregate-aua-timeseries`, `account-distribution`, `aum-metrics` and `account-units` (kebab-case), their data-bearing leaves byte-unchanged across every cutover, with `_provenance.written_at` excluded because it advances daily. The publisher is the one place parquet becomes JSON, and it reads only `opal-data-mdpf` | the portal's Model Portfolios page |
| each firm's bucket and its serving grants | **consumed** | the bucket exists, serves, and carries its serving grants, per firm | produced by `ADVI_FIRMBKTS`, per firm; FWD-2 and FWD-6 wait on it for that firm |
| the scoped route for a firm's slice | **produced** | the portal's existing requests keep their URLs (`/api/general/mdpf/{firm}/...`); the portal is frozen, so no caller changes. The edge maps them: `global` keeps its current general handling unchanged, and a firm segment resolves through the registry, aliases included, to one firm and is served, from that firm's bucket at the key above, to two kinds of session only: a session whose validated tenant resolves to that same firm, and an internal Opal staff session (tenant `opal-capital`), for which the path segment IS the selection because the frozen portal's selector sends no `?firm=` on these requests (`ModelPortfolios.tsx:357-358`, Andrew's MDPF_SCOPED.S5). Any other firm's session is refused. This is the boundary the scoped router already enforces by comparing resolved buckets (`shared-advisor-router/index.mjs:367-373` @`40697fe79d`), never a bare segment-equals-tenant test. **Keeping the old URL never keeps general authorization for firm data** | the portal's Model Portfolios page and its wrappers (`aum.ts`, `portal-proxy.ts`); the edge routers and CloudFront behaviours; the router's firm map is `LGIC_ENFORCE`'s generated view |
| the dedicated runner | **produced** | one principal per firm, named by `name()` (`mdpf-49f-runner-role` and its siblings), whose only write grant is `opal-data-{firm}/mdpf/{firm}/platinum/*` in its own firm's bucket; its host is built by this project | the per-firm slice writes |
| the separation rule | **consumed** | `LGIC_ENFORCE`'s scope-derived Deny on each firm bucket, which admits a principal whose name carries that firm in its scope slot. **For FWD-6, "word-for-word what it was before" means the run needs NO edit to it: no exemption row, no carve-out, and the rule's bytes are identical before and after the run** | produced by `LGIC_ENFORCE` (its fence row, and its cell E5 on the template) |
| the decommission standard | **consumed** | for each retiring tree: 45 CONSECUTIVE days in which a named instrument records no data event on the tree except an excluded probe. It starts no earlier than that instrument's observed-live stamp, any other event restarts it, and it counts only once every reader is repointed. Each removal is then its own act | `ADVI_FIRMBKTS`'s FWD-6 window ruling (its tree row @`9819855eda`), on Andrew's ~18:4xZ card 2 and ~03:xxZ word |
| the combined slice's written basis | **produced** | `org/missions/D8/MDPF/MDPF_CANON/deliverables/X2_GLOBAL_BASIS.md`: why the combined all-firms figure reveals nothing about any single firm's clients | the ledger's X2 row (`LGIC_CANON`); anyone moving data later |
| inherited law | **consumed** (ruled) | A-1 to A-3 as quoted above; B1 (repoint the RPS read through `opal-data-assets`) and B2 (the JWT read stays, a standing exception, ledger X1); route (c) and the dedicated runner; Rule 17b; the canon's R4-R7, R11, R12, R16-R19 and R21 | Andrew's words; the law surface; `LGIC_CANON`'s canon |

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
- Every MDPF figure is dated parquet in one bucket.
- Each firm's served slice is in that firm's own bucket, behind a route that asserts the tenant.
- One publisher reads only that bucket, and what people see did not change.
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
| M1 the reader census | FWD-5, FWD-8 | IV.2; IV.3; Part V bullet 3; Part VII bullet 1 | -- | `comp-find` over the corpus, unscoped; Terraform; `EC2_MANIFEST.json`; the portal source | `org/missions/D8/MDPF/MDPF_CANON/deliverables/READER_CENSUS.md` | every reader and writer of both trees, the served key and the old bronze, each with its evidence line and its instrument; IV.2's 16 definitions and 50 config sites as the floor | every reader the unscoped read finds is listed or excluded with a reason, denominator printed; the instrument is named (a name census proves presence, never absence) |
| M2 the emitter | FWD-1 | O1; IV.1; IV.5; Part V bullets 1-2 | C the key string, `key()` and `address()`; P the gold artifact | -- | the address `address()` returns per scope under R7 (the firm bucket for firm scopes, `opal-data-mdpf` for `global`); never typed here | one partition written for today for every artifact and scope; the twins diffed before convergence | a dated question is answered from a key alone; the emitter writes no string it did not get from the builders; no second write path exists |
| M3 the backfill | FWD-1 | O1; A-3 | P the gold artifact | the current JSON artifacts in both trees | the same prefix | every historical date the JSON holds, one partition each, with the count printed against the source's | the full series is the partition set; no date is rewritten |
| M4 the repoints and the seams | FWD-5 | O5; IV.3; IV.4; AC9 | C the key string | the producer scripts M1 names | -- | one reader at a time; each seam's `/seams` read on the MECHANICAL, DECLARATIVE and SEMANTIC axes, grounded on the DEPLOYED artifact | a search finds no producer writing to, reading from, or running code out of the old places, and the leftovers are history; every seam passes all three axes |
| M5 the publisher | FWD-4 | O4; IV.4; the second final-step obligation | C the gold artifact; P the served JSON | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/` | -- | the served leaves diffed on data-bearing values before and after, with the population named (the brief's three denominators, 522, 492 and 13, reconciled first) | every figure is identical; the publisher reads only `opal-data-mdpf`; it is switched last |
| M6 the code homes | FWD-5 | IV.4; the third final-step obligation | -- | `EC2_MANIFEST.json` (the accrual bundle); the gold Lambda's Terraform and source map | the code home in `s3://opal-data-mdpf/`, at the one address LGIC_NAMING-S7 rules (HELD until then) | per artifact class -- the accrual bundle (runner code, R16) and the gold Lambda's zip (a Lambda artifact: R16 does not reach it and it keeps its source-map tie, but R1 grades its key) -- the packaging declarations changed to the ruled address, never an object hand-copied; the frozen rollback objects listed before and after | no resource pulls code from `opal-data-assets/portal/`; the rollback objects are byte-identical |
| M7 the combined slice's basis | FWD-3 | O3; IV.7 | P `X2_GLOBAL_BASIS.md` | `infra/logic/06_CONFORMANCE_LEDGER.md` X2 | `org/missions/D8/MDPF/MDPF_CANON/deliverables/X2_GLOBAL_BASIS.md` | the aggregation level, the minimum firm count, and why no per-firm or per-account row survives | a reader asked why `global` did not move points at the paragraph; the ledger's X2 row cites it |
| M8 the bronze move | FWD-7 | O7; R4 | C the key string, `key()` and `address()` (waits on `LGIC_ENFORCE` E3) | the receiving step; M1's bronze listing | `s3://opal-data-assets/mdpf/{scope}/bronze/` | every destination key generated by `address()`, never typed; the step run on demand; its output read where it landed | the output lands beside every other vendor's, at builder-generated keys; the next routine delivery lands there too, as confirmation only |
| M9 a firm's route and slice | FWD-2 | O2; IV.6; Part V bullet 5 | C the firm's bucket and grants, `key()` and `address()`; P the compatibility route | `public-data-router`, the scoped router and the auth validator at the edge; the live CloudFront behaviours; the portal's callers `aum.ts`, `portal-proxy.ts` and the Model Portfolios page (read, not edited) | `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/` | per firm, after `ADVI_FIRMBKTS` reports that firm's bucket serving; the mapping deployed and proven against today's location before the origin flips; never-widen sign-off (CTO and COO) on every served key | through the page's own request path: a 49 Financial session sees its figures exactly as before; an internal Opal staff session selecting 49 Financial sees the same figures; an Inflection session requesting 49 Financial's exact URL is refused; `global` still loads as before; no portal source is changed |
| M10 the dedicated runner | FWD-6 | O6; IV.8 | C the fence, `key()` and `address()`; P the runner | -- | the runner's host and its per-firm roles | a run for one firm, after `LGIC_ENFORCE` E5 applies the fence; the fence's bytes read before and after | the run writes only builder-generated keys under that firm's `mdpf/{firm}/platinum/`; the fence's bytes are identical before and after, with no exemption row added |
| M11 the retirements and the hold | FWD-8 | O8; IV.9; IV.12 | C the decommission standard | the hold file; the three prior cleanups' kill lists (the negative control) | `org/missions/D8/MDPF/MDPF_CANON/deliverables/` | the hold re-pointed or superseded with the producer's read cited; the read instrument's observed-live stamp; the 45-day record per tree, once every reader is repointed | the record shows no reader or writer for the whole stretch on a named instrument; the hold is true; each removal is its own confirmed act |
| M12 the stale served key | FWD-4, FWD-5 | Part V bullet 10 | P the served JSON | `dim_mdpf_aum_timeseries.py`; the portal's readers of the key | -- | the key's portal readers named; one of the two dispositions chosen | the staged repoint is finished, or the key is retired with its readers named; not both |

## PATHS

| kind | path | cell | use |
|---|---|---|---|
| new | `s3://opal-data-mdpf/mdpf/{scope}/gold/` and `.../state/` | M2, M3 | the gold artifact and its state |
| new | the code home in `s3://opal-data-mdpf/`, at the address LGIC_NAMING-S7 rules: the brief's `code/mdpf/gold/...` or the schema's `mdpf/global/code/gold/...` (the accrual bundle and the gold Lambda's zip, by packaging declaration) | M6 | the code home, HELD on S7 |
| new | `s3://opal-data-assets/mdpf/{scope}/bronze/` | M8 | the bronze home |
| new | `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/{leaf}.json` | M9, M10 | each firm's served slice, at the five-segment key |
| new | `org/missions/D8/MDPF/MDPF_CANON/deliverables/` | M1, M7, M11 | the census, the basis, the retirement records |
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
| 4 | O1 vintage from the key; one bucket | DEC-2; M2, M3 | FWD-1 |
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
| `s3://opal-data-mdpf/mdpf/{scope}/gold/` and `/state/`; the code home at the address LGIC_NAMING-S7 rules | new objects, and packaging declarations for the code (held on S7) | M2, M3, M6 | MDPF_CANON |
| `s3://opal-data-assets/mdpf/{scope}/bronze/` | new objects (the bronze move) | M8 | MDPF_CANON |
| `s3://opal-data-{firm}/mdpf/{firm}/platinum/{table}/` | APPLIED: the served slices move to the five-segment key; never-widen sign-off per served key | M9 | MDPF_CANON, per firm, after `ADVI_FIRMBKTS` delivers that firm |
| `public-data-router`, the scoped router and the CloudFront behaviours for `/api/general/mdpf/{firm}/...` | APPLIED: the tenant-asserting compatibility route; `global` unchanged | M9 | MDPF_CANON, through the infrastructure lane |
| the portal's callers (`aum.ts`, `portal-proxy.ts`, the Model Portfolios page) | read only: their URLs stay, because the portal is frozen | M9 | -- |
| the publisher Lambda and its Terraform | APPLIED: the port to parquet | M5 | MDPF_CANON |
| the producer scripts; `EC2_MANIFEST.json`; `gold-lambda.tf`; `lambda-source-map.json` | edits | M4, M6 | MDPF_CANON; deploys ride their owners' paths (Rule 13) |
| the runner's host and its per-firm IAM roles | APPLIED: new compute and principals | M10 | MDPF_CANON, through the infrastructure lane |
| the hold file | an edit | M11 | its custodian, under the order |
| `docs/architecture/MDPF_CANON_PRD.md` | the moved notice | DEC-1 | 1.0.0_SA_CTO |
| `org/missions/D8/MDPF/MDPF_CANON/deliverables/` | documents | M1, M7, M11 | MDPF_CANON |
| the two retiring trees, the old bronze prefix, and the stale served key | REMOVALS: each its own act, with a human's confirmation, and for the trees the FWD-8 proof | M8, M11, M12 | MDPF_CANON |
| the conformant compute chain; platinum's shape; `platinum/mdpf/global/`; the frozen rollback objects; B2's JWT read; `opal-data-demo`'s slice beyond the demo-tenant ruling | excluded | -- | untouched |
