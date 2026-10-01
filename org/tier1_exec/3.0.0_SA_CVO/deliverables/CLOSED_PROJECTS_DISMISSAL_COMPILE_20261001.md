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

## Batch 2 (12:2xZ): 68 more items dismissed, 66 of them BLOCKING or ARMED; 15 rows filed in the estate-wide channel

**Home of every re-filed row: `org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md`** (rows S7 to S11
@531b115ff1, S12 to S21 @22746eedf5). Directives D0 and D11 have no open member project and the graph pipeline has
no project with a seat. Filing a tooling hazard in an unrelated open project (Investor Reporting, say) would put an
ARMED row in front of that project's slug, so the estate-wide channel was used instead. **That is a departure from
the letter of batch 77 item 2 ("an open project that has a seat") and it is `1.0.0_SA_CTO`'s to overrule:** no drive
loop reads this channel today.

| new row | from | the hazard, on today's read |
|---|---|---|
| S7 | batch 77 item 4 | the row gate's rowlessness limb compares ids exactly (INERT, owner `0.0.0_AB_MSTR`) |
| S8 | NFRA_OUTSET-W1-S21 | `deployed_state` has no value for a deploy-scope artifact committed and not deployed |
| S9 | NFRA_OUTSET-W1-S17 | `comp-heat federated --sql` is unrestricted under a read-only docstring |
| S10 | NFRA_OUTSET-W1-S13, W2-S10 | two worker traps are in no worker face or doctrine |
| S11 | NFRA_OUTSET-W1-S14 | the graph_nodes metadata prefix did not list in 280 seconds; count not obtained |
| S12 | NFRA_CLDGRPH-W1-S11, W1-S27 | the halt gate never reads OPAL_AGENT_SERIAL |
| S13 | NFRA_CLDGRPH-W2-S19 | proof-of-spec-check's `introduces` rung matches substrings |
| S14 | NFRA_CLDGRPH-W1-S24 | the vendored jq emits CRLF and no doctrine line says so |
| S15 | NFRA_CLDGRPH-W4-S4, W4-S6, W6-S3, W7-S2 | the graph call manifest and three modules still describe the retired local engine |
| S16 | fourteen NFRA_CLDGRPH rows (the identity seam, the retirement, the unexplained mover) | the served graph has 0 STORED_IN edges while `derive_stitch.py:339` still emits them; SERVED_FROM's 27 land on bucket-policy nodes |
| S17 | NFRA_CLDGRPH-W3-S10 | the 2026-10-01 03:00Z stitch build FAILED (exit 2) after seven good nights; log not read |
| S18 | NFRA_CLDGRPH-W1-S8 | the resource-summaries producer has no trigger |
| S19 | NFRA_CLDGRPH-W3-S16 | a graph test file collects zero tests |
| S20 | NFRA_CLDGRPH-W1-S43 | the graph bucket is unversioned and dated snapshot keys are overwritten |
| S21 | NFRA_CLDGRPH-W2-S72, S104, S106 | the alert topic every derive publishes to still has an SMS subscription; RESERVED FOR ANDREW, no answer on record |

Dismissal documents of this batch: NFRA_OUTSET `ADJUDICATION_v4.md` (8 rows, 10 items: 5 with a pointer, 5 not
live) and NFRA_CLDGRPH `ADJUDICATION_v6.md` (16 rows, 58 items: 29 with a pointer, 29 repaired, gone or cut-side).

**What changed my reading of NFRA_CLDGRPH.** It was closed on 2026-09-23 on Andrew's word, "not a graded close", with
no outcome claimed realized. Round 9's fixes did land (the key-collision fix is in the running updater, which hashes
equal to HEAD), but the question rounds 7 to 9 circled is open on the served plane today: row S16.

**Not dismissed, because not read:** NFRA_CLDGRPH-W1-S3 (seven residue outputs in the globgrph Terraform state;
needs a plan) and NFRA_CLDGRPH-S116 (a terminal worker could not be continued in the harness; needs a spawn).

**Also seen, not this compile's to move:** NFRA_OUTSET-S14's remediation row reads OPEN while the runner it names is
deployed and equal to HEAD (clock: `1.0.0_SA_CTO`). NFRA_CLDGRPH's `REMEDIATION_v4.md` is an UNTRACKED draft of
2026-09-10 holding 12 rows the gate refused; under batch 77 it stays uncommitted, and ten of its rows are covered by
the dismissals above. Row NFRA_CLDGRPH-W4-S10 (the workflow route has never published correctly, owner
`0.0.0_AB_MSTR`) is outside the rowless set and was not touched.

## Running count against the 260

| | items dismissed | of them BLOCKING or ARMED |
|---|---|---|
| batch 1 | 80 | 78 |
| batch 2 | 68 | 66 |
| total | 148 | 144 of 260 |

## Remaining, in the ruled order

ETFS_GUARDRAIL 22; NFRA_COMPEFFICACY 11; the three groups graduated in their own rows (ETFS_INGEST 18,
ETFS_POSITIONING 16, ADVI_PERFRP 14); the twelve smaller channels (33); the two unread items above. Each needs a
read of the world, not of the row.

## End report (re-filed rows and their homes)

Not yet written; the table above is its running form.

-- 3.0.0_SA_CVO
