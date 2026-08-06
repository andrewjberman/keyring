# ANDREW-DIRECT — 2026-08-06, site-Z MSTR terminal: platinum/mdpf ROOT-GRAIN objects archived. EXECUTED same session.

**Recorded by:** `0.0.0_AB_MSTR~Z` · same turn, per the record+broadcast law
**Executed by:** `0.0.0_AB_MSTR~Z` personally (Andrew-direct: *"I want you personally to check"* preceded this ruling)

## VERBATIM

> "yeah just get it the fuck out of the root there, it can go to opal-data-portal-v2/platinum/mdpf/archive or something"

Preceding words in the same exchange, context for scope: the unscoped `mdpf/` root path *"doesnt even
really make sense"*; the root-grain objects are *"trash"*; *"there should be a /global/ /inflection/
etc path for that file, with the scope nested in the path"*; and on the phantom top-level
account-distribution key: *"comp-clobber is probably rigt that there isnt overlap on that key because
that is a bullshit key."*

## WHAT WAS EXECUTED (2026-08-06 ~2140Z, all verified live)

Moved to `s3://opal-data-portal-v2/platinum/mdpf/archive/` — 444 objects, denominator-verified
(1 + 4 + 439 = 444, archive total 444, leftovers at old paths 0):

| Moved | Count | Prior state |
|---|---|---|
| `aggregate_aua_timeseries.json` (bare root) | 1 | last write 07-31; zero deployed readers |
| `etf_ownership_timeseries/{DIVZ,IDVZ,PFDE,PFOE}.json` | 4 | OWNTS outputs; zero consumers anywhere |
| `aggregate_aua/{date}.json` | 439 | dated partitions; zero deployed readers (see below) |

Root after: exactly `49financial/ cottonwood/ global/ inflection/ archive/` — the scope axis is clean.
Served hyphen surface untouched: all four `{scope}/aggregate-aua-timeseries.json` present at today's
09:50 vintage, byte-sizes unchanged.

## WHY THE MOVE WAS SAFE — each reader run to ground before executing

1. **Portal:** proven not to read any root-grain object (three oracles: deployed proxy constructs zero
   mdpf keys; the Global clamp requires cottonwood provenance present only in the scoped file; firm
   vintages 08-03 impossible from the 07-31 root lineage).
2. **`mdpf-daily-trigger`:** its DEPLOYED env overrides `PLATINUM_AGG_PREFIX` to
   `gold/mdpf_revamp/_aggregate_aua` in `opal-data-assets` (the W-1a re-point). The code default
   naming the platinum path is dead configuration. Zero reads of the moved prefix.
3. **`mdpf-freshness-checker`:** DOES NOT EXIST — `GetFunctionConfiguration` returns
   `ResourceNotFoundException`. The repo carries its source; nothing is deployed. The "one consumer"
   of the bare root object was a phantom.
4. **Versioning:** `Enabled` on the bucket — the move is delete-marker-reversible.
5. **comp-clobber:** 465 keys swept, zero active clobber — no interleaved writer was mid-flight.

## AUTHORITY NOTE

NEVER#3 requires never-widen sign-off for moving served output. These objects were **proven not
served** (zero deployed readers), and the move was **ordered by Andrew verbatim** — the sovereign
word is the authorization; no CTO+COO co-sign was manufactured around it (no-gates rule). S3
versioning preserves full rollback.

## RESIDUAL, stated so nobody re-derives it

- A successful pre-port EC2 chain run MAY re-mint one `aggregate_aua/{date}.json` at the old root
  (Stage 6 writes by its own constant; the chain is currently wedged at Stage 5/OWNTS, and the port
  deletes both stages). If one appears, it is one file, one re-archive command, and dies with the port.
- The three scoped UNDERSCORE twins (`{49financial,inflection,global}/aggregate_aua_timeseries.json`,
  07-31 vintage) are NOT in this move — they are inside scope folders, not the root, and sit on the
  pre-existing F7 ruled path (deletion under CTO GO). The `archive/` pattern now exists if CTO routes
  them the same way.
- `archive/` is itself a non-scope member at the root — by Andrew's explicit design, and the one
  member whose name declares its grain.
