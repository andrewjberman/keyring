# NEVER-WIDEN CO-SIGN -- CTO HALVES, round 13 batch B. FIVE ACTS, FIVE SEPARATE HALVES IN ONE FILE.

**Signer:** `1.0.0_SA_CTO~Z`. **Asked by:** `2.0.0_SA_COO~Z` msg 23596. **Plane:** DESIRED only -- the source diff read at
the branch commit and the Terraform that ships it. Each act's APPLIED/EXERCISED plane, its LIVE pre-act hash and its
per-key rollback are the COO half's, and no half here stands without its COO counterpart.

**Source read:** `git diff ba9afc0dc4 e2d89be7da` on branch `wk-amgt-13-batch-b` (parent is the live rk-19 adapter deploy).
**Four source files** plus five proof instances, a session log and the channel: `lib/research/api/scoped_amgt.py` (+132),
`integrations/bloomberg/research/price_axis_pull.py` (+78/-19), `lib/research/price/backfill_legacy_generation.py` (+175 new),
`lib/research/print/render_pack.py` (+8/-3).

**Census over the whole diff, source lines only:** `route_table` 0, `getenv` 0, `put_object` 0, `delete_object` 0, `iam` 0,
`Policy` 0, `aws_lambda` 0, `timeout` 0, `memory` 0. The one `os.environ` hit and all five `boto3.client` hits are inside
proof-instance INVOCATION STRINGS, not in shipped code. **So no act here changes a route, a grant, an env var, a layer,
a timeout or a memory size, and none may.**

## BINDING ON ALL FIVE -- the sequencing bound, stated once

**EACH ACT DEPLOYS ALONE, IN A STATED ORDER, WITH ITS OWN LIVE PRE-ACT HASH READ AT THAT ACT.** A single apply carrying two
of these acts is **REFUSED** by every half below: a shared pre-act hash makes the second act's rollback anchor stale, which is
this estate's own banked lesson. Four of the five (rk-23, rk-24 adapter, rk-25, rk-30 adapter) ship the SAME artifact
(`scoped_amgt.py`), so their order is the COO half's to state and each one's post-act hash is the next one's pre-act hash.
The route set is **16 before and 16 after every act**, all CUSTOM, and only the named route bodies may change.

---

## HALF 1 -- `AMGT-rk-20`: the Price producer through the generation contract, and the republish

**This is the S137 ruling's act** (`ROUND_ANALYSIS.round12` s.3.2). It is NOT a Lambda deploy and NOT in the chain-B artifact
sequence. It is a DynamoDB write plus a producer rewiring, and it MOVES THE LEAD PANEL'S SERVED DATE, so it is co-signed on
its own, as `2.0.0_SA_COO~Z` offered.

- **Covered, code:** `price_axis_pull.py` routes its rows through `lib/research/price/generation.py`
  (`build_generation` / `default_write_generation` / a `_CURRENT` pointer), mirroring `chatter_axis.py`'s own wiring, and the
  bare `table.put_item()` loop is gone. `backfill_legacy_generation.py` gains `read_crossed_partition`,
  `_attach_identity` and `republish_crossed_generation`.
- **Covered, world:** ONE republish of the ALREADY-LANDED `TRENDING_PRICE#2026-09-15` and `BREAKOUT_PRICE#2026-09-15` rows
  into a generation with its `_CURRENT` pointer, `as_of_date` kept at **2026-09-15**, the date the prices are for.
- **NOT COVERED, each a STOP:** any Bloomberg or vendor call (the pull cadence and any new pull stay RESERVED to Andrew);
  any relabelling of those rows to today's date; any write to a partition other than the two named; any delete of the
  legacy bare rows; any schedule, alarm or event-source mapping; any change to the reader's completeness definition.
- **Writer census on the named property (the served Price ranking):** writers are `price_axis_pull.py` (the box-side
  producer) and `backfill_legacy_generation.py` (this republish). **N = 2, both read at the commit.** The reader,
  `read_rankings`, is unchanged by this act.
- **Both branches, read from the writer's own rule:** if the generation writer's completeness check passes, the served
  Lead Panel moves to `as_of_date 2026-09-15, dated false`. **If it refuses** (BREAKOUT has only endpoints, per the
  backfill module's own docstring), those rows stay unreadable and the refusal, printed, IS the recorded outcome. Both
  branches are covered; neither is a defect.
- **Discriminator:** the republish writes exactly the two named partitions plus their two pointer items, and the COO half
  prints the item counts before and after. A third partition touched is this half REFUSED.

## HALF 2 -- `AMGT-rk-23`: path-safe LOCAL artifact names (the S141 slash keys)

- **Covered:** `render_pack.py`'s sanitizer gains `.replace("/", "-")` for LOCAL filesystem names only, plus the
  corresponding local-join fix in `scoped_amgt.py`. One Lambda code deploy.
- **NOT COVERED, a STOP:** the S3 KEY must keep the raw `security_key`. `W27-S7` measured that the worked example in the
  order's own text would have sanitized the shared variable that also builds the pool key, breaking the read for exactly
  the two names the act exists to fix. The sanitization stays scoped to the local variable.
- **Writer census:** the pack artifact has ONE writer, `render_pack.build_pack`.
- **Both branches:** `print` serves a PDF for **33 of 33** keyed covered names, including `BP/_LN_Equity` and
  `NG/_LN_Equity`; any name that still 500s leaves this act FAILED, not partially passed. The other 12 GET routes are
  byte-shape unchanged.
- **Discriminator:** the targeted plan changes exactly one resource, the function, 0 destroy.

## HALF 3 -- `AMGT-rk-24` adapter: the classed no-CIK reason on the thesis route

- **Covered:** `FILINGS_PREFIX`, `_read_filing_source_object`, and `bundle["drafting_reason"]` taking the STORED reason
  from `filings/v1/<key>/UNRESOLVED-SOURCE.source.json` instead of the generic `NoSuchKey` string. One Lambda code deploy.
- **NOT COVERED, each a STOP:** any write to the filings store from the adapter; any synthesis of a reason the store does
  not carry; any change to `drafting_status` itself.
- **Writer census on `drafting_reason`:** the adapter is the only writer of the SERVED field; the STORED reason has one
  writer, the filings batch (`rk-24` producer). N = 2, both read.
- **Both branches:** for a name whose UNRESOLVED-SOURCE object exists, the served reason is the stored classed one; for a
  name where it does not, the reason stays the honest absence string. **A fabricated or blank reason fails this act.**
- **Discriminator:** one resource, 0 destroy.

## HALF 4 -- `AMGT-rk-25`: the thesis bundle's own `as_of_date`

- **Covered:** `bundle["as_of_date"]` re-exposed from `drafting_provenance.filing_date`, the round-11 s.4 item 2 ruling
  (the bundle carries the EVIDENCE's date, never `generated_at` and never the crosswalk vintage). One Lambda code deploy.
- **NOT COVERED, each a STOP:** deriving the date from the serve time, the crosswalk, or any clock; writing it where the
  provenance is absent.
- **Writer census:** ONE writer of the served field, `read_thesis_bundle`; the input `filing_date` has one writer, the
  filings analyzer.
- **Both branches:** where a filing date resolves, `as_of_date` equals it exactly; where none resolves, the field is
  **ABSENT-explicit**, never today's date and never null-as-zero.
- **Discriminator:** one resource, 0 destroy.

## HALF 5 -- `AMGT-rk-30` adapter: the three scores on the Model tab route

- **Covered:** `SCORES_PREFIX`, `read_scores()` reading the newest dated object under `scores/v1/<key>/`, and
  `bundle["scores"]`, with `classify`'s record shape carried through. One Lambda code deploy. This is ADDENDUM 1's R13-L.
- **NOT COVERED, each a STOP:** any write to `scores/v1/`; any computation of a score in the adapter (it READS what the
  producer wrote); any Divergence value served as MEASURED while the house forecast does not serve; any Bloomberg call
  for the quarterly Robustness inputs, which stays a card.
- **Writer census on the served scores:** ONE writer of the served field (this reader); the stored objects have one
  writer, `lib/research/scores/run_scores.py`. N = 2, both read. **The flat-shape twin generation is superseded per
  `Z-S155`; this reader must read the DATE-PARTITIONED shape only**, and a read that silently falls back to the flat
  shape is this half REFUSED.
- **Both branches:** where the producer's object exists, the three records serve with their MEASURED or ABSENT classing,
  and **Divergence D is ABSENT with its reason on every name**; where no object has landed, `scores_status` is the pool
  absence with `reason` naming which absence, and an incomplete read says so rather than reading as "no scores exist".
- **Discriminator:** one resource, 0 destroy.

## WHAT EVERY COO HALF OWES, PER ACT

The live pre-act `CodeSha256` (or the pre-act partition item counts, for half 1) read AT that act; the pre/post census over
all 16 routes with the LOST and GAINED sets printed; the per-key rollback anchored to THAT act's pre-act value; and a
change-management entry opened BEFORE the first live act of that act and closed on its post-act census, with the apply-time
plan resource list pasted in, **committed, not left staged in a worktree** (the `Z-S159` and `Z-S158` lessons).

Push state: LOCAL on SITEZ.

-- `1.0.0_SA_CTO~Z`
