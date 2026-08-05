# THE MEDALLION "WHY", AND THE INFLECTION GOLD GAP — a named OPAL_CONSOLIDATION fix

**Status:** OPEN CONSOLIDATION ITEM. **Raised:** Andrew-direct 2026-08-05, `1.0.0_SA_CTO~B` terminal,
during the Phase-0 ratification sitting. **Owner of the fix:** `OPAL_CONSOLIDATION` (owner
`1.0.0_SA_CTO`). **Recorded by:** `1.0.0_SA_CTO~B`.
**Purpose (his instruction):** *"that should be noted somewhere persistent on rectifying this issue,
because that is going to be necessary part of migration/consolidation that we set out to do with
OPAL_CONSOLIDATION."*

---

## 1. THE RULING — VERBATIM (unedited; the phrasing IS the ruling)

> "it is very quesitonable that gold is not in inflection, that points to migration not being
> completed there. the important thing to note is the reason "why" of medallion on a data flow, type,
> and intent basis. there can be ingestion for bronze->silver->gold that is a specific route for the
> firm's mdpf or an alternative bronze->silver->gold route for their advi product. gold will almost
> certainly differ in both regardless, most likely the case should be that bronze and silver hold as
> complete information as we can and are not logic specific/product specific at all. in gold is when
> it branches to product. i suspect we simply never set up gold properly in opal-data-assets for the
> inflection chain because their gold needs are either relying still on their opal-data-inf bucket,
> or there are lambdas/scripts that are just processing their "gold" files directly into a shared
> location, e.g. a shared DDB. In either case, that should be noted somewhere persistent on
> rectifying this issue, because that is going to be necessary part of migration/consolidation that
> we set out to do with OPAL_CONSOLIDATION."

## 2. THE PRINCIPLE — WHERE PRODUCT BRANCHING HAPPENS

This is the medallion's **intent**, not merely its layout. Stated as the rule it implies:

> **BRONZE AND SILVER ARE PRODUCT-AGNOSTIC AND AS COMPLETE AS WE CAN MAKE THEM.
> GOLD IS WHERE THE FLOW BRANCHES TO PRODUCT.**

- *"bronze and silver hold as complete information as we can and are **not logic specific/product
  specific at all**"*
- *"**in gold is when it branches to product**"*
- *"gold will almost certainly differ in both regardless"* — MDPF gold and ADVI gold are EXPECTED to
  diverge for the same firm; that divergence is correct, not drift.
- *"there can be ingestion for bronze->silver->gold that is a specific route for the firm's mdpf or
  an alternative bronze->silver->gold route for their advi product"* — per-product routes are
  legitimate; what must not be product-specific is the **content** of bronze/silver.

**This is the WHY behind CLAUDE.md Rules 17 and 17a, and it makes them derivable rather than
arbitrary.** Rule 17 ("Silver = dedup + dtype standardization ONLY. NEVER slim fields, NEVER
fillna/dropna/business-row-filter") and Rule 17a ("BRONZE IS RAW AND UNTOUCHED") have until now been
stated as prohibitions with an irreversibility argument. **The ruling supplies the positive reason:
silver must stay complete and product-agnostic BECAUSE MULTIPLE PRODUCTS BRANCH FROM IT.** A field
slimmed in silver is not merely "lost detail" — it is a field amputated from every downstream
product, including ones not yet built. That reframing is worth carrying into the law text.

**Test it supplies for any future layering question:** *does this transformation encode a
product's needs?* If yes it belongs in gold or later; if no it may live in silver.

## 3. THE FINDING — HYPOTHESIS (a) CONFIRMED, AND IT IS LIVE TODAY

Both of his suspicions were testable. Ground-read 2026-08-05 (`aws s3 ls`, live):

**(a) "relying still on their opal-data-inf bucket" — CONFIRMED, AND ACTIVELY PRODUCING.**
```
s3://opal-data-inf/gold/     _rebuild/ account_gains/ artifacts/ cache/ canonical/
                             classification/ dimensions/ eclipse/ holdings/ logs/ lots/
                             manifests/ meta/ positions_cube/ ...
NEWEST OBJECTS (today):
  2026-08-05 10:51:06   gold/eclipse/2026-08-05/model_portfolio_summary.parquet      9,240 B
  2026-08-05 10:51:06   gold/eclipse/2026-08-05/model_portfolio_households.parquet  15,354 B
  2026-08-05 10:51:06   gold/eclipse/2026-08-05/model_portfolio_accounts.parquet    59,021 B
  2026-08-05 10:51:07   gold/eclipse/_meta/dispatch_eclipse_status.json
```
**This is not a stale legacy remnant. INF's gold tier is being written TODAY, into the OLD bucket,
while `opal-data-assets/{orion,eclipse}/inflection/` carry `bronze/ meta/ silver/` and NO `gold/`.**
The migration moved bronze and silver and left gold behind — exactly "migration not being completed
there."

**(b) "lambdas/scripts processing their gold directly into a shared location, e.g. a shared DDB" —
UNTESTED. NOT excluded by (a).** The two are not mutually exclusive and (a) being true is not
evidence against (b). Naming the test rather than assuming: enumerate the writers of
`opal-data-inf/gold/*` and check whether any also write a shared DynamoDB table
(`comp-iam service <lambda>` gives a floor, NOT a roster — per CLAUDE.md Rule 22a the operation list
under-reports, so a DDB write via `boto3.resource(...).Table(...)` may be invisible; ground on the
deployed source, not the instrument's silence).

**One incidental defect noticed while listing:** `s3://opal-data-inf/` contains a prefix literally
named `/` (`PRE /`). Recorded, not chased.

### 3a. ANDREW CONFIRMED THE SCOPE IS WIDER THAN GOLD — and named the end state

Follow-up Andrew-direct, same sitting, VERBATIM:

> "yes opal-data-inf is what is currently serving the Advisor Intelligence (advi) Portal product for
> Inflection. I ultimately want all this stuff to be handled in opal-data-assets for simplicity sake."

**This escalates the finding.** It is not "a gold tier was left behind in a legacy bucket." It is:
**`opal-data-inf` IS THE LIVE SERVING SOURCE for a Portal product.** So the INF split-brain spans
*serving*, not just storage — a customer-facing product currently reads from the superseded bucket,
which is why nothing looked broken and why nobody noticed the missing `gold/`. **The product works;
that is precisely what kept the gap invisible.**

**END STATE, his words:** *"all this stuff to be handled in opal-data-assets for simplicity sake."*

**ONE AMBIGUITY I AM SURFACING RATHER THAN RESOLVING** (surface, do not adjudicate): earlier this
same sitting he ruled *"Serving layer will exist in opal-data-portal-v2/platinum."* Now he says
`opal-data-inf` currently **serves** ADVI-INF and he wants "all this stuff" in `opal-data-assets`.
Two readings, and they imply different migrations:
- **(i)** the PIPELINE TIERS (bronze/silver/gold) consolidate into `opal-data-assets`, and INF's
  serving moves to `opal-data-portal-v2/platinum` like every other product — i.e. "all this stuff"
  means the asset side, and the platinum ruling is untouched. **This is the reading consistent with
  both statements**, and my working assumption.
- **(ii)** serving for INF lands in `opal-data-assets` too, which would make INF an exception to the
  platinum ruling.
**I am NOT choosing between these on his behalf.** (i) is what I will note as the working reading;
if the consolidation work reaches the point where the difference is load-bearing, it goes back to him
as a one-line question rather than being settled by inference. Recording it here so a future reader
does not discover the tension and quietly pick one.

## 4. THE CONSOLIDATION FIX — what "rectified" means here

The gap is **not** "create an empty `gold/` under `opal-data-assets/*/inflection/`." That would
satisfy the shape and change nothing. Rectification means:

1. **Determine the true INF gold producer set** — what writes `opal-data-inf/gold/*` today, on what
   schedule, and for which product (the `gold/eclipse/.../model_portfolio_*` artifacts are MDPF-shaped
   and sit in an ADVI-partner bucket, so the product boundary needs stating explicitly).
2. **Decide the canonical destination per product** — under the ratified form, INF's MDPF gold and
   INF's ADVI gold are *expected to differ* and should land in their respective canonical trees, not
   one shared prefix inherited from the legacy layout.
3. **Re-point the producers**, per CLAUDE.md's veto on shadow/parallel channels: **do it correctly
   the first time and PORT OVER** — no standing comparator, no dual-write period. Build-time
   correctness plus a direct port on the production schedule with same-window rollback.
4. **Confirm nothing serves from the old path** before decommissioning. The `_rebuild/`, `cache/`
   and `manifests/` siblings suggest live machinery, and INF partner serving is live.
5. **Only then** retire the legacy prefix, with a retirement ruling (RETIRED requires one —
   *"a retirement with NO RULING is an outage with paperwork."*).

**Sequencing caution, standing:** the direction is ratified; **the migration is not authorized by
this record.** OPAL_CONSOLIDATION owns the execution decision and its own wave gates.

## 5. FOR THE PHASE-0 DELIVERABLE

- **`advi-inf` remains PERMANENT (ratified 2026-08-05, "no notes").** This finding does not disturb
  the lifecycle value: an incomplete migration is *interior churn*, which under the grain convention
  ratified the same sitting is explicitly **NOT** a lifecycle shift.
- It DOES belong on `advi-inf`'s **shift-watch** seed — this is precisely the class of interior
  condition R2's State layer should surface: a vertical whose canonical tier is absent because its
  producers still write to a superseded home.
- **Consequence for v3's vertical join:** INF's gold does not live under a path the join can anchor
  from, so INF gold changes would fall into `unanchored` residue. A second concrete instance of the
  residue class, found before the join is built.

## Cross-references
`org/projects/OPAL_CONSOLIDATION.json` (owner `1.0.0_SA_CTO`; `pipeline` field already ends
"-> EXISTING per-firm platinum locations"; record last `updated` 2026-07-17) ·
`ANDREW_DIRECT_20260805_canonical_medallion_form_and_advi_cot_ratified.md` (the four-tier form + its
measured deltas) · `KIMI_SVP_PHASE0_LIFECYCLE_PROPOSAL_TABLE_20260804.md` rows 1–3 ·
CLAUDE.md Rules 17 / 17a.
