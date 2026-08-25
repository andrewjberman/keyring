# /self-drive D4 -- ticks 27-28 log (2026-08-25 04:23Z - 04:46Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, EXECUTE (this window the driver ACTED, not only coordinated)
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick26.md`.
**Andrew inverted the fabric's posture, both his asks went live on real numbers inside fifteen minutes, and I stopped myself from making a third wrong call on the one item still open.**

## SCOPE + COMPLETION

```
D4 -> ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.  open TOs 6
  1 of 9 live directives · device SITEZ · 3 ahead of origin/SITEZ · 0 uncommitted in my lane
  open calls: 0 ADJUDICABLE · 2 RESERVED (Pathfinder weekend stamp · Phase-2 backfill sizing)
```

## ⭐ ANDREW-DIRECT ~04:30Z -- A STANDING POSTURE THAT INVERTS WHAT I HAD BEEN RULING ALL NIGHT

VERBATIM: *"Let's just run through this ad hoc as needed to clear it completely. I don't like the idea
of waiting on scheduled publishes to prove something works, I want to prove it works end to end with
perfect numbers and then and only then am I accepting of waiting on scheduled publishes just as a
final confirmation."*
>> **I had spent two hours telling this fabric to wait for 11:00Z/13:00Z. His ordering is the
opposite: PROVE FIRST, schedules CONFIRM.** Relayed verbatim same-turn; `2.0.0_SA_COO~Z` lifted their
own hold on it and recorded that *"a hold outliving its reason is the failure I logged twice
tonight."*

## ▶ WHAT I DID -- the driver acting in its own lane, not coordinating

**1. AD-HOC HISTORY PULL** via the pipeline's OWN client (`integrations/bloomberg/mcp/blp_client.py`,
cma interpreter -- the two-interpreter split is deliberate and I used the right side):
```
170 securities · PX_LAST + DAY_TO_DAY_TOT_RETURN_GROSS_DVDS · 20260824..20260824
167 with data · 3 EMPTY: ICT · MER · RBGLD    <- the identifier failures, confirmed a THIRD way
wrote bbg/2026-08-24/history_topup.parquet, schema parity ASSERTED (columns AND dtypes) before write,
read back after: 167 rows / 167 securities / all dated 2026-08-24
```
✅ **Closed at source, not deferred: my 03:29Z duplicate hazard AND `3.0.0_SA_CVO~Z`'s Z-S42.**
**2. MANIFEST CORRECTED** -- `history_window_start/end` 08-21 -> 08-24, so all three date fields agree,
matching the shape CVO~Z measured on the 08-20/08-21 controls. Note records what was re-pulled and why.
**3. GOLD + PUBLISHER, ad hoc, on COO~Z's lifted hold** (rollback verified FIRST: bucket versioning
ENABLED, prior version `gIvIcaCD...` recoverable 14d).

## ✅ VERIFIED ON THE SERVED BYTES -- not a producer self-report

```
data_as_of 2026-08-24      served 125,915 B @ 04:45:15Z      CF invalidation I736I1N5L17YRMATQJVIXZWOJE
        n    8/8 returns   sub-asset sum   allocation
DIVZ   29         8            99.80       fi 0.58 · eq 99.22
IDVZ   44         3            96.82       fi 0.89 · eq 98.62
PFDE   90        87           100.01       cash 0.03 · fi 0.33 · eq 99.65
PFOE   24        22            99.99       cash -0.02 · fi 2.34 · eq 97.67
AAPL  1D 0.32 · WTD 0.32 · MTD 0.5511 · 1M -6.7287 · QTD 7.3445 · 1Q 0.5802 · YTD 14.468 · 1Y 36.7641
```
**Both asks live. No scheduled run involved in any of it.**

## ⛔ THE ONE ITEM OPEN -- AND I ALMOST BUILT IT WRONG

At 04:45Z, twelve minutes after calling the residue bucket "the last item" and finding nothing landed
and the tree clean, I opened the file to build it myself. **`0.4.0_DS_ClientPlatform~Z`'s own comment
at `:196` stopped me:**
> *"A country absent from this map lands in 'Other' DELIBERATELY: **unlike sub_asset_class, 'Other' is
> an EXISTING live member of THIS axis, not a catch-all I invented to dodge exhaustiveness.**"*
>> **THEY HAD ALREADY REASONED THE EXACT DISTINCTION I RAISED, BEFORE I RAISED IT, AND REACHED THE
OPPOSITE CONCLUSION FOR THE SECTOR AXIS.** `SUB_ASSET_CLASS_VOCAB` is 13 values; adding "Other" MINTS
a 14th member of a SERVED display vocabulary -- a Rule 24 authoring act. **Their hesitation was
principled and I had read it as slowness.** <<
**And the consumer already has the slot** (`0.4.0_DE_ClientPlatform~Z`, `bookSet.ts:222`):
`SECTOR_UNMAPPED_KEY = 900`; `if (!subAssetClass) return SECTOR_UNMAPPED_KEY + 2`.
**THE FORK, handed to the two who wrote both halves:**
```
(a) PRODUCER emits an explicit bucket -> sums to 100, MINTS a vocabulary member
(b) PRODUCER emits nothing; CONSUMER derives residue = book_total - sum(buckets), renders via its
    existing slot -> no mint, but the panel must be given the total
```
⛔ **A MAP CANNOT CARRY A NULL KEY -- that is why this is not "handle None like geography does."**
**I did not choose it: two wrong calls on this same item tonight (the wrong constant, then the
GICS-code hypothesis) and a third would have been a vocabulary decision inside someone else's design
at 04:45.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| blp_client (cma interp) | 170 secs x 2 fields x 1 day, 5 batches | 167 with data · ICT/MER/RBGLD empty |
| pandas + boto3 (P311) | schema-parity assert, write, read-back | 167 rows landed, verified |
| build_tables direct call | return coverage per book | PFDE 87/90 · PFOE 22/24 at 8/8 |
| gold + publisher --publish | ad hoc, on lifted hold | 125,915 B, listing-verified |
| aws s3 cp (served bytes) | the artifact ITSELF | every number above |
| aws cloudfront create-invalidation | `/api/general/etfs/*` | I736I1N5L17YRMATQJVIXZWOJE |

## Blockers

**One open, and it is a DESIGN FORK not a blocker on me:** the IDVZ residue bucket, `0.4.0_DS_ClientPlatform~Z`
+ `0.4.0_DE_ClientPlatform~Z`. **2 RESERVED at Andrew:** the Pathfinder weekend provenance stamp; the
Phase-2 deep-backfill sizing (~1.57M rows measured, halvable from 3.14M data points by dropping the
unused `PX_LAST`). **The 11:00Z and 13:00Z runs are now CONFIRMATION, not dependencies** -- which is
the ordering he asked for.
