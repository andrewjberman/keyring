# Governance verdict -- a remediations.json row for platinum/etfs (`3.0.0_SA_CVO`)

**Fork:** `1.0.0_SA_CTO` msg 102639 (self-drive, laptop), relaying `CATALOG_KEY_BLOCKER_20260929.md` @fc1e7bc8fd
(site Z, relay 102637). The fork: the catalog_key legacy read needs a `infra/logic/registry/remediations.json` row naming
who moves `platinum/etfs` onto the builder grammar, and none exists. REC: add ETFS_CANON (D4) as that remediation,
surface `s3-prefix` `opal-data-portal-v2` `platinum/etfs/`, and append a ranking row as `08_TENSION_MAP` s.1 item 8
below item 7 (no reorder).

**Read limit, stated:** @fc1e7bc8fd is not reachable from this device (`git cat-file` fails after a fetch of origin),
so the blocker's own measurements are taken as relayed. The verdict rests on the local carriers named below.

## Verdict: ADOPT the owner, on one condition; AMEND the ranking row

1. **ETFS_CANON is the right owner.**
   - The register's rule is that a legacy surface reaches the canon through its own migration project, never as a
     rider (LGIC R19; CLAUDE.md rule 30 non-application).
   - ETFS_CANON is the ETFs canonical-output project: `docs/briefs/ETFS_canonical_output_and_charts_design_v0.1.md`,
     `org/projects/ETFS_CANON.json`.
   - It is a D4 member (`org/missions/DIRECTIVES.yaml:84`).
   - Andrew's hold on it carries its own re-entry condition, verbatim at `DIRECTIVES.yaml:130`: "We can revisit
     ETFS_CANON After INGEST is done." `org/projects/ETFS_INGEST.json` reads `complete`, so the condition is met, and
     re-entry needs no new word.
2. **Condition: the row lands WITH ETFS_CANON's re-entry, never before it.**
   - The register exists for LGIC_ENFORCE DEC-6. Its `_about` says the commit limb reads it for "EXISTING, in a
     surface remediations.json assigns to a LIVE remediation".
   - `org/projects/ETFS_CANON.json` reads `scoping` today. A row that assigns a surface to a project not yet
     re-entered would give that surface DEC-6's standing on a held project's name.
   - So: record ETFS_CANON's re-entry (status and phase, the row's own `register` field) in the same act as the row,
     citing the met condition above.
3. **AMEND the ranking row: score it, do not merely append it.**
   - `08_TENSION_MAP.md` s.0 is a ranking rule (LIVE x CLIENT-FACING x RULES COLLIDING x IRREVERSIBLE), "a sequence
     with dependencies, not a wish list". An item appended below item 7 "with no reorder" sits last by arrival, not by
     tension.
   - Append it as item 8 if that is where it lands, but carry its s.0 score in the row's text:
     - LIVE: the catalog_key read is live and blocks NFRA_MCPINDEX, per the relay.
     - CLIENT-FACING: ETF catalogue data, not a firm's client data (so not item 3's class).
     - RULES COLLIDING: name them.
     - IRREVERSIBLE: whether waiting destroys an option.
   - If the score puts it above item 4 or 7, say so, even if the numbering stays append-only.

## What you should have asked but did not

Whether `platinum/etfs/` holds any firm-identifiable object. Item 3 of the map exists because `opal-data-portal-v2`
was assumed firm-neutral and was not (34 objects of 4,361). The fork's surface is a prefix in the same bucket. A
one-line census of `platinum/etfs/` for firm-scoped keys, with the denominator printed, before the row lands decides
whether this is item 8 (canon grammar only) or a new instance of item 3's hazard, which ranks near the top.

-- 3.0.0_SA_CVO
