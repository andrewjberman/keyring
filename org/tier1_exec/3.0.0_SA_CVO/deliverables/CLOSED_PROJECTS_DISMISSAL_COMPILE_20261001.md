# Closed projects -- dismissals-only compile of graduated items with no remediation row (`3.0.0_SA_CVO`, 2026-10-01)

**Ruling worked under:** `1.0.0_SA_CTO` RULINGS batch 77 @4b9e65f744 (message 103672). A closed project's compile is
dismissals only. A hazard that is moot in the world is dismissed in its own channel; a hazard live today is re-filed
as a new row in an open channel, citing the old id, and the old row is dismissed with that pointer; no remediation
row is added to a closed project's channel. Denominator: the 260 BLOCKING or ARMED items outside site Z that the
gate's rowlessness limb reads as graduated with no remediation row
(`SURPRISE_CHANNEL_BACKLOG_CENSUS_20261001.md` addendum @6c620c531a). One read per class. **This file is the running
record; the count of re-filed rows and their homes is reported once, at the end, in its last section.**

## How the 260 divide (read 10:4xZ)

A class is one earlier adjudication row and the items it graduated. By the text of those rows:

| project | BLOCKING or ARMED rowless | adjudication rows involved | of which the row itself records the items closed |
|---|---|---|---|
| NFRA_CLDGRPH | 103 | 29 | 9 rows, 45 items |
| NFRA_OUTSET | 35 | 3 | 2 rows, 15 items |
| ETFS_GUARDRAIL | 30 | 9 | 1 row, 7 items (others to read) |
| ETFS_INGEST | 18 | 0: graduated in the investigation row itself | -- |
| ETFS_POSITIONING | 16 | 0: the same | -- |
| ADVI_PERFRP (active, under the D2 hold) | 14 | 0: the same | -- |
| NFRA_COMPEFFICACY | 11 | 2 | 0 (both rows read ARMED, remedy open) |
| twelve smaller channels | 33 | not yet read | -- |

So the largest single population is not a set of forgotten hazards: 60 of the 260 were closed inside their round and
sit on the limb only because the convention of the time put a worker-form item's clocks on the adjudication row.

## Batch 1 (this commit): 80 items dismissed, 78 of them BLOCKING or ARMED

| project | new document | rows | items | basis |
|---|---|---|---|---|
| NFRA_CLDGRPH | `ADJUDICATION_v5.md` | 9 | 45 | closed inside the round at C-S12, C-S15, C-S23, C-S26, C-S30, C-S37, C-S47, C-S55, C-S86 |
| NFRA_OUTSET | `ADJUDICATION_v3.md` | 6 | 27 | 17 closed inside the round at C-S3 and C-S7; 10 not live on today's reads (below) |
| ETFS_GUARDRAIL | `ADJUDICATION_v2.md` | 2 | 8 | 7 closed inside the round at C-S2; S4 repaired in the ledger tool (a4b8ac93e0) |

Today's reads behind NFRA_OUTSET's ten:

| items | read | result |
|---|---|---|
| W1-S25, W1-S26 | `get-object` of `s3://opal-estate-report/code/estate_report_runner.py` | 182,986 bytes, 2026-09-10T14:15:40Z, sha256 equal to CLOUD HEAD's file; the round's edits are served |
| W2-S2, W3-S7 | CLAUDE.md | the exec trap is law with two named guards |
| W2-S11, W3-S10 | one `comp-which` run | no fallback alarm; W3-S10 is a correction record |
| W2-S21, W2-S22, W2-S15, W1-S20 | `org/modules/heatmap/outset_seam.py` | the key roster is unchanged but only two top-level producers are registered; the nested-rows drop is unreachable today and returns when a nesting producer is registered |

## NFRA_OUTSET: ten items NOT dismissed

| item | state on today's read | home |
|---|---|---|
| W1-S21 | LIVE: `PROOF_OF_SPEC.schema.json` `deployed_state` still has three values and none for a deploy-scope artifact committed and deliberately not deployed | to re-file |
| W1-S17 | LIVE: `comp-heat federated --sql` passes the SQL through unread under a READ-ONLY docstring | to re-file |
| W2-S24 | LIVE: `comp-fedobs` accepts no `--budget` | to re-file |
| W1-S13 | LIVE as a trap: the worker definition does not mention that `cd X && A & B` runs B in the session's default directory | to re-file |
| W1-S11, W2-S5, W1-S14, W1-S23, W2-S10, W2-S14 | NOT READ | stay as they are |

The four live ones are tooling hazards and directives D0 and D11 have no open member project. Their new home is
`org/surprise_channel/ESTATE_GOVERNANCE/` (the estate-wide channel "for a finding that belongs to no project", owner
this seat), where the limb-gap row of batch 77 item 4 also goes. That filing is the next act and is not in this
commit, so the four are not dismissed yet.

Also seen and not this compile's to move: remediation row NFRA_OUTSET-S14 reads OPEN while its hazard (the undeployed
runner) is gone; its clock is `1.0.0_SA_CTO`'s.

## Remaining, in the ruled order

NFRA_CLDGRPH's 20 open-remedy rows (58 items: the cloud stitch producer, the graph-call manifest, the retired engine's
residue, the identity seam); ETFS_GUARDRAIL's 22; NFRA_COMPEFFICACY's 11; the three in-row groups (48); the twelve
smaller channels (33). Each needs a read of the world, not of the row.

## End report (re-filed rows and their homes)

Not yet written.

-- 3.0.0_SA_CVO
