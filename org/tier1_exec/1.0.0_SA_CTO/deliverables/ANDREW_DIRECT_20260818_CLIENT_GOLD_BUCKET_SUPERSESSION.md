# ANDREW-DIRECT 2026-08-18 ~1730Z (CTO terminal) -- THE CLIENT-GOLD-BUCKET SUPERSESSION (ADVI gold home -> per-client bucket; `opal-data-49financial` minted as the template)

**Channel:** Andrew at the `1.0.0_SA_CTO` terminal. **Recorded by:** 1.0.0_SA_CTO same turn; broadcast COO/MSTR/AE/DS~A/CVO same turn.

## VERBATIM (the proposal, ~1728Z)

> "Something I want to cover on the matter of the templated advisor intelligence pipeline is the location of the gold parquet layer. I think a cool way to do this is we keep bronze (raw ingest) /silver (typed parquet) in opal-data-assets bucket, then the gold runner reads those silver parquets, and essentially creates the gold parquet layer in a client-specific bucket, I recommend using a new one entirely for 49 so there is no confusion and we can use it as a clean slate for templating structure, i.e. "opal-data-49financial". The gold bucket in there is essentially designed to hold parquet columnar data for all our transformations. I want this gold data to be standardized nomenclature, this is the standardization layer where ALL firms, no matter what the shape of their bronze/silver (as it will vary by vendor), becomes flattened to opal nomenclature/shape in gold. This way when the platinum portal publisher publishes to json in opal-data-portal-v2, we still maintain a client-specific location for agentic query which will be a lot easier to analyze than having to deal with JSON. Is this description in line with the current vision of the refactor 5 step process?"

## VERBATIM (the ratification, ~1730Z, on the CTO assessment naming the supersession + grammar + three seams)

> "Ratified, proceed with the re-point before the P2 apply"

## WHAT THIS SUPERSEDES, PRECISELY

The 08-11 gold-home ruling (@a9c159f134 / CLAUDE.md 17b amendment: product gold at `opal-data-assets/portal/gold/{product}/{scope}/`) is **SUPERSEDED FOR ADVI**: the ADVI gold home is now the PER-CLIENT bucket. Everything else in the ratified pattern is UNCHANGED -- bronze/silver in `opal-data-assets/{vendor}/{firm}/`, gold-is-parquet `{table}/date={D}/`, gold as THE standardization layer (all firms flatten to opal nomenclature/shape -- the shape-transposition doctrine), ONE publisher per served key reading parquet and writing JSON to `opal-data-portal-v2/platinum/`, five-phase order, P5 gate.

## THE RATIFIED GRAMMAR (template = `opal-data-{firm_id}`, canonical full firm name, never a truncation)

```
opal-data-49financial/                          bucket = the FIRM (clean slate; the templating structure)
  gold/{product}/{table}/date={D}/data.parquet  {product} axis kept (advi first; a future product joins with no second migration)
  gold/{product}/dimensions/{dim}/date={D}/
  _code/                                        the deploy target moves WITH the product root (atom 2);
                                                the 1720Z portal/gold/advi/_code ruling RE-POINTS here
```
**Born-with controls:** versioning ON · block-public-access · the cross-firm IAM Deny minted AT CREATION (the NEVER#2 pattern on day one) · publisher read-grant scoped to this bucket only. **Dual purpose by design:** the platinum publisher's parquet source AND the client-specific agentic-query location (columnar, not JSON).

## THE THREE SEAMS (ruled with it)

1. **Scope: ADVI now.** MDPF gold STAYS at `opal-data-assets/portal/gold/mdpf/` through its live P4/P5 (mid-cleanup); migrate-or-not later on its own act.
2. **Global/cross-firm gold artifacts** stay at the assets root by construction (no client bucket exists for "global").
3. **Publisher IAM** becomes per-client-bucket (the 49F ADVI publisher can only ever read 49F's bucket).

## EXECUTION (CTO-routed, ONE act, BEFORE the P2 apply -- his sequencing word)

AE: TF-mint the bucket + policies + swap the staged IAM grants (my per-apply gate) -> DS~A: `aws s3 sync` the existing root (4,222 objects) + flip `runner_common.py:31 OUT_ROOT`/BUCKET + `safe_deploy_core` row + `_code` home (if already minted at the old path, MOVE it -- no twin; the two-homes class) -> AE: P2-FLOOR TF draft target updated in the same window -> CVO: pin re-anchor (frame is key-names; roots re-cite) -> the OLD `portal/gold/advi/` prefix is deleted after the new root is live-verified (migrate-before-kill; it has zero consumers -- platinum/advi is empty). P2 build proceeds 08-19 against the new root.
