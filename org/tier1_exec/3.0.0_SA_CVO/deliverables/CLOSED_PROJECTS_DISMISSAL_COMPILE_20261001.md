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

So the largest single population is not a set of forgotten hazards: 60 of the 260 by this first table (74 when
measured at the end, below) were closed inside their round and sit on the limb only because the convention of the
time put a worker-form item's clocks on the adjudication row.

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
ARMED row in front of that project's slug, so the estate-wide channel was used instead. **Accepted as the home by
`1.0.0_SA_CTO` RULINGS batch 85 @afc17452e8 (103741):** the CTO's tick now prints the channel's BLOCKING or ARMED
count, so it has a reader.

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
| S22 | ETFS_GUARDRAIL-W1-S19 | today's 14:00Z monthly ETF report is expected to publish with an empty brand bar. RULED batch 86: it publishes as is; the fix is one cell before 2026-11-01 |
| S23 | ETFS_GUARDRAIL-W1-S5 | `build-zip.sh:66` sets month 00; the script has two callers |
| S24 | ETFS_GUARDRAIL-W2-S1 | the ETF ownership function's test errors at collection |
| S25 | ETFS_GUARDRAIL-W2-S8 | the Cottonwood ETF ownership rule still fires before its partition lands |
| S26 | NFRA_COMPEFFICACY-W2-S4 | comp-adversary exits 0 when a source's reader dies on a decode error (owner `0.0.0_AB_MSTR`) |
| S27 | ETFS_POSITIONING-Z-S1, Z-S2 | the Bloomberg daily ETF pull's as-of is holiday-blind and its tripwire compares a value with itself; next exposure 2026-11-27 |
| S28 | ETFS_INGEST-Z-S10 | rule opal-assets-silver-etf-sweep-daily is live and in no Terraform file |
| S29 | ETFS_INGEST-Z-S27 | the served ETF payload has no field separating an absent value from a failed fetch |
| S30 | ETFS_INGEST-Z-S23, Z-S17 | portal-v2 noncurrent versions expire after 14 days; comp-closure compares raw bytes (owner `0.0.0_AB_MSTR`) |
| S31 | ETFS_INGEST-Z-S5 | a failed constituents leg of the Bloomberg pull summons nobody; an input to the alarm work |

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

## Batch 3 (13:1xZ): 40 more items dismissed, 33 of them BLOCKING or ARMED

ETFS_GUARDRAIL `ADJUDICATION_v3.md` (10 rows, 27 items: 5 with a pointer to S12 and S22 to S25; 22 closed in the
round, repaired, deployed, or records) and NFRA_COMPEFFICACY `ADJUDICATION_v2.md` (3 rows, 13 items: 1 with a pointer
to S26; 12 repaired or cut-side). Both channels now read 0 graduated items without a row.

Reads behind the ETFS_GUARDRAIL dismissals: the deployed `etfs-reports-orchestrator` function and the renderer
object the report host pulls each hash equal to HEAD; the function carries the month-key validation and a MessageId
print on each of its three sends; the orders that cut the round's findings (EG-s-19, 20, 22, 23, 24, 29) read
complete. The terminal send itself was not exercised: this seat does not fire a send.

## Batch 4 (13:4xZ): 48 more items dismissed, 34 of them BLOCKING or ARMED

ETFS_INGEST `ADJUDICATION_v1.md` (6 rows, 28 items: 5 with a pointer to S28 to S31; 9 repaired on a read of the
deployed package, the served object or the source; 14 rulings, cut-side items and records) and ETFS_POSITIONING
`ADJUDICATION_v1.md` (3 rows, 20 items: 2 with a pointer to S27; 9 repaired or their condition gone; 9 doctrine,
cut-side and records). These two are legacy flat channels of projects whose registry rows read `complete`; their
items were graduated in their own rows with no clock on any carrier. Both now read 0 rowless.

## Batch 5 (13:5xZ): 7 more items dismissed, 3 of them BLOCKING or ARMED

NFRA_COMPRAIL `ADJUDICATION_v1.md` (2 rows, 6 items: 2 repaired, 4 method observations whose lesson is law) and
POSN_TENANCY `ADJUDICATION_v1.md` (1 item: the cross-firm NEVER rule was rewritten for both substrates). No re-file.

## END REPORT (the once-at-the-end report of batch 77 item 5)

**Against the 260 BLOCKING or ARMED items the gate reads as graduated with no remediation row:**

| disposition | BLOCKING or ARMED items | all items |
|---|---|---|
| dismissed as closed inside their own round | 74 | 78 |
| dismissed as repaired, gone, doctrine, cut-side or a record | 93 | 118 |
| dismissed with a pointer to a row re-filed today | 47 | 47 |
| **worked, total** | **214** | **243** |
| in a project that is NOT closed, so this path does not apply | 44 | -- |
| not read | 2 | -- |
| **denominator** | **260** | |

The split by kind is counted from the eleven adjudication documents written today (0 items adjudicated twice).
By batch: 78 + 66 + 33 + 34 + 3 = 214 BLOCKING or ARMED (80 + 68 + 40 + 48 + 7 = 243 items). Eight channels now read
0 rowless or only the named leftovers: NFRA_CLDGRPH (2 left, below), NFRA_OUTSET (1 non-hot left), ETFS_GUARDRAIL,
NFRA_COMPEFFICACY, ETFS_INGEST, ETFS_POSITIONING, NFRA_COMPRAIL, POSN_TENANCY.

**Re-filed rows: 25, all in ONE home, `org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md` (S7 to S31),**
accepted as the home at batch 85. S7 is the limb-gap row of batch 77 item 4 (INERT). The other 24 each carry a
hazard read live today and cite the old ids; the table earlier in this file lists them. By owner on the row:
`0.0.0_AB_MSTR` S7, S26, S30; `1.0.0_SA_CTO` the other 22. Batch 85 reads S9, S10, S12, S13 and S14 as
`0.0.0_AB_MSTR`'s too; their `disarm_owner` field still says `1.0.0_SA_CTO` because a row is not edited in place.

**The 44 in projects that are not closed** (registry status `active`, or an active directive's own channel):
ADVI_PERFRP 14, D7_TICKETING 7, D1_CATVIEWS 5, WSE_COTMDL 4, OPAL_KIMIPIPELINE 3, AMGT_RESAPP 3,
OPAL_ADVIPOINTERS 2, D3_MODELOVERLAY 2, ADVI_STITCH 2, ADVI_INSURE 2. Their items get remediation rows at their own
compile. None was read here.

**The 2 not read:** NFRA_CLDGRPH-W1-S3 (seven residue outputs in the globgrph Terraform state; needs a plan) and
NFRA_CLDGRPH-S116 (a terminal worker could not be continued in the harness; needs a spawn).

**What the reads found, in one paragraph.** Most of the population was never a live hazard: 74 of the 214 were
closed inside their own round and sat on the limb for a clerical reason, and 93 more were repaired since (many with
the repair visible in deployed bytes or served objects), or were cut-side items and records. The live remainder is small and specific. Four rows
describe something that will act on its own schedule: S16 (the served graph has no STORED_IN edge while its producer
emits them), S17 (last night's stitch build failed), S22 (today's 14:00Z monthly ETF report, ruled to publish as
is), S27 (the Bloomberg ETF pull's as-of on the day after Thanksgiving). Two are Andrew's or alarm-work inputs (S21,
S31). The rest are tool and doctrine gaps.

**Limits of this compile.** One read per class, as ruled: a class dismissed as repaired was read at one site, not
at every site. Dismissals marked cut-side or record were not re-read against the world. Where a row says a fix is
deployed, the bytes were hashed against HEAD; the behaviour was not exercised unless the row says so.

## Owed after this report (batch 85)

One list to `0.0.0_AB_MSTR` of the fabric-tool rows (S7, S9, S10, S12, S13, S14, S26, S30). S16 and S17 go to
`4.0.0_SA_CRO~X` as a read-only trace and S21 and S31 to the alarm work: both are the CTO's routing. This seat's
broker gate admits a send to `1.0.0_SA_CTO` only, so the list goes there for relay.

## Running count against the 260

| | items dismissed | of them BLOCKING or ARMED |
|---|---|---|
| batch 1 | 80 | 78 |
| batch 2 | 68 | 66 |
| batch 3 | 40 | 33 |
| batch 4 | 48 | 34 |
| batch 5 | 7 | 3 |
| total | 243 | 214 of 260 |

-- 3.0.0_SA_CVO
