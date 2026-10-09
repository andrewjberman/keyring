# Registry, LGIC_BLANKFIX round 9 -- the 37 rows written, and three registry-owner rulings

**By:** `4.0.0_SA_CRO` (registry owner of `infra/logic/registry/**`, CTO ruling 106332), 2026-10-09 ~06:2xZ.
**Asked by:** dell1 `2.0.0_SA_COO~B1` msg 1867, relayed by `0.0.0_AB_MSTR` msg 107769. Rows:
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~3/REGISTRY_ROWS_round9.json` and
`HOLES_OWNED_round9.md` beside it, read at box/dell1 @1db8c77646 (not yet on CLOUD at the write).

## Written

`key_rulings.json` +9 (133 -> 142) and `name_rulings.json` +28 (69 -> 97); no duplicate on (bucket, key) or (name, type);
`_cite` stripped. Every row is the worker's draft except the reason text of the four security rows (ruling R9-3 below).
Measured on the real files after the write:

```
VALIDATE: OK 54 system row(s), 14 scope row(s), 0 warning(s) over all 13 registry file(s)
ALL-ROOTS ok=True roots_total=87 mapped=78 unmapped=9 completed=78 stopped=0 items=2264 right=559 fix=1460
  not_asked=212 pattern=23 carded=0 refused=0 hole=10 carded_class_holes=0 source_bucket_holes=0
  event_rule_holes=0 unknown_word_holes=0 other_holes=10 stale_hints=0 uncounted=18
```

hole 51 -> 10, as the worker's copy predicted. The 10 left are `1.0.0_SA_CTO`'s H8 names
(`deliverables/0.9.0_WK_LGIC_BLANKFIX~4/HOLES_OWNED_round8.md`). uncounted reads 18 against round 8's 17; that change came in
with CLOUD, not from these rows, which touch no census input but rulings.

## Rulings

**R9-1. The `trade` token stays UNRESOLVED; the 22 none_owed rows are ADOPTED as drafted.** `systems.json` `unresolved`
records why (measured 2026-09-17): the trade-submission pipeline's projects (TRSB_*) are legacy flat projects with seat owners
and no directive line, so `owner_directive` cannot be written. A registry row does not create an owner. The rows follow the
astn precedent and leave when a mission-tree project claims the pipeline and the token gets a system row. This is a "not yet"
with no cost while it waits: the 22 names keep working under their current names. The root map's default system for
`trade-pipeline` (`portal`, ruling W3-S10) is unchanged; it places the root, it does not resolve the word.

**R9-2. `opal-data-imo`: the 8 none_owed rows are ADOPTED as drafted.** Andrew retired the bucket by card 9
(`systems.json` `refused_keys.retired_basis`). The rows leave when the bucket does. Deleting it is an S3 delete, an act only
Andrew can do; it is not asked here, because nothing waits on it.

**R9-3. No scope row for security; the four security rows are ADOPTED with a corrected reason.** A scope says whom the data
is FOR (`name_rulings.json` `source_owned_bucket`): a firm, a product, a master, or nobody (`global`). `opal-data-security`
and `opal-data-security-access-logs` are the secops system's own stores and belong to no firm or product, so their scope is
`global` (ruling W3-S11, `ROOT_MAP_ROUND8_RULINGS_20261009.md`). A scope row for a system would be a scope that is not
a scope. The drafted reason ("the rows leave when the OpSec owner registers a scope") named a wait that will not come; the
written reason names the real one: where the stores live under the canon is the opsec root's own migration (Rule 30
non-application, R19), never a rename from these lines.

**The two JUDGMENT calls in canonical rows: both ACCEPTED.** Tier `state` for
`opal-security-evidence` `allowlists/partner-egress.json` (a reviewed configuration file the sentinel reads each run) and
for `opal-estate-report` `config/last-trigger.json` (a per-run marker): each is an object a system reads to do its work,
not data a reader consumes, which is what `state` holds.
