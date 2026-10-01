# Surprise-channel backlog census -- rows no adjudication or remediation names (`3.0.0_SA_CVO`, 2026-10-01 ~08:1xZ)

**Why this exists.** Grading MDPF_COTREMEDIATION for its close found its channel uncompiled for 37 days (21 rows, three
BLOCKING). The review asked whether other projects carry the same thing; this is that read. **Instrument:** the row
gate's own resolver, `.tools/surprise-row-gate.py` `_latest_dispositions(root, code)` (index read), called for every
project code that has a channel on either root. An item is undispositioned when its latest disposition is
UNDER_INVESTIGATION or empty: no adjudication row names it in `adjudicates`, no remediation row carries its id, and
its own row holds no disposition. Class, standing and fabric are read from the item's own row. Registry status is
read from `org/projects/<CODE>.json` or the tree's `project.json`.

## The numbers

| scope | items | undispositioned | of those BLOCKING or ARMED |
|---|---|---|---|
| all 56 channels (0 did not run) | 4,745 | 739 | 198 |
| rows whose `fabric` is not `site-z` (laptop, or unstated on older rows) | -- | 295 | 125 |
| of those, in projects whose registry row reads closed or complete (11 projects) | -- | 135 | 81 |

Site Z's rows (444 undispositioned, 73 BLOCKING or ARMED) are `3.0.0_SA_CVO~Z`'s lane and are counted only in the
first line.

## Rows whose fabric is not site-z, by project

| BLOCKING or ARMED | undispositioned | project | registry status |
|---|---|---|---|
| 20 | 42 | ETFS_GUARDRAIL | closed |
| 19 | 23 | ETFS_INGEST | complete |
| 16 | 23 | NFRA_CLDGRPH | closed |
| 15 | 25 | NFRA_OUTSET | closed |
| 7 | 72 | DSGN_IRPTV1 | active |
| 7 | 24 | MDPF_TAXSMA | active |
| 7 | 9 | IRPT_DASHBD | active |
| 6 | 16 | IRPT_BCKEND | active |
| 6 | 13 | ADVI_INSURE | active |
| 6 | 9 | ETFS_POSITIONING | complete |
| 4 | 6 | MDPF_GLOBAL | active |
| 2 | 8 | D1_CATVIEWS | active |
| 2 | 5 | IRPT_FNTEND | closed |
| 2 | 2 | NFRA_GLOBGRPH | complete |
| 1 | 2 | POSN_TENANCY | complete |
| 1 | 2 | ADVI_FIRMBKTS | active |
| 1 | 1 | WSE_COTMDL | active |
| 1 | 1 | NFRA_OPLGTW | active |
| 1 | 1 | LGIC_CANON | active |
| 1 | 1 | ESTATE_GOVERNANCE | no row |
| 0 | 2 | OPAL_KIMIPIPELINE | active |
| 0 | 2 | NFRA_COMPEFFICACY | closed |
| 0 | 1 | NFRA_CSE, NFRA_COMPRAIL (complete); MDPF_SECCLASS, LGIC_ENFORCE, AMGT_RESAPP (active); D7_TICKETING (no row) | -- |

MDPF_COTREMEDIATION reads 0 after today's compile (@24e1f3273c).

## What the numbers are and are not

- **They are the gate's reading, not a judgment that 125 hazards are live.** The MDPF_COTREMEDIATION compile is the
  sample: of its 11 BLOCKING-or-ARMED rows, 4 closed on a live read, 1 was dismissed and 6 stayed open with an owner. A row filed
  ARMED in August is often moot by October; nobody has looked.
- **A row can be handled in the world and still count here.** A CTO ruling, an order or a fix that never wrote the
  row's id into an adjudication or remediation document leaves the item undispositioned by this instrument. That is
  the instrument's blind side, and it is the same blind side the row gate has at a close.
- **Older adjudication documents resolve less than they look.** Rows written before the `adjudicates` field existed
  name their items in prose; the resolver does not read prose. ETFS_GUARDRAIL and NFRA_OUTSET show this (28 and 12
  adjudication rows, `adjudicates` empty on the ones read). Some of their 67 rows are therefore dispositioned in
  words and counted here. The count for those two is an upper bound.
- **Four active IRPT and Tax projects (121 rows, 27 BLOCKING or ARMED) are live FAST lanes**; their rows are
  moving hourly and are compiled at the lease end or the next drain-end packet, as the session log says.

## What this seat can do about it, and what it needs

The compile is this seat's work (L8/L9). One closure compile of 21 rows took about 35 minutes with live reads. The
11 closed or complete projects are about 135 rows; the remaining inactive ones about 40. The order matters because
the closure plan closes projects: a project should not close a second time over rows nobody graded, and three of the
closure plan's own members appear above (ADVI_FIRMBKTS, LGIC_CANON, MDPF_TAXSMA).

-- 3.0.0_SA_CVO

## ADDENDUM, 2026-10-01 ~09:3xZ -- a second population the first count did not see

Compiling ADVI_FIRMBKTS, the commit gate refused the new rows because five items an adjudication had marked
GRADUATED carried no remediation row. Those five read "dispositioned" in the table above. The gate has a limb for
exactly this (`_graduated_without_row` over `_remediation_ids_for_project`, the S74 limb); run over all 56 channels
(0 did not run):

| scope | GRADUATED items with no remediation row | of those BLOCKING or ARMED |
|---|---|---|
| all fabrics | 852 | -- |
| rows whose `fabric` is not `site-z` | 313 | 260 |

| BLOCKING or ARMED | rowless | project | registry status |
|---|---|---|---|
| 103 | 105 | NFRA_CLDGRPH | closed |
| 35 | 38 | NFRA_OUTSET | closed |
| 30 | 35 | ETFS_GUARDRAIL | closed |
| 18 | 28 | ETFS_INGEST | complete |
| 16 | 20 | ETFS_POSITIONING | complete |
| 14 | 17 | ADVI_PERFRP | active |
| 11 | 13 | NFRA_COMPEFFICACY | closed |
| 7 | 11 | D7_TICKETING | no row |
| 5 | 7 | D1_CATVIEWS | active |
| 4 | 4 | WSE_COTMDL | active |
| 3 | 9 | AMGT_RESAPP | active |
| 3 | 4 | OPAL_KIMIPIPELINE | active |
| 2 | 6 | NFRA_COMPRAIL | complete |
| 2 | 3 | OPAL_ADVIPOINTERS, ADVI_INSURE (active) | -- |
| 2 | 2 | D3_MODELOVERLAY, ADVI_STITCH (active) | -- |
| 1 | 1 | POSN_TENANCY | complete |
| 0 | 5 | COT_CANON458 | closed |

**What this number is.** It is the gate's own rule, so it is what the gate will enforce: the next commit that adds a
remediation row to any of these channels is refused until every rowless item in that channel has a row in the same
commit. For NFRA_CLDGRPH that is 105 rows before the first of its 23 undispositioned rows can be graduated.

**What it is not.** It is not 313 forgotten hazards. NFRA_CLDGRPH's later remediation documents carry rows keyed by
the adjudication row's id (`NFRA_CLDGRPH-C-S69` and the like), not by the investigation item's id; the limb matches
ids exactly, so an item remediated under its adjudication's id counts as rowless. How many of the 313 are that
convention and how many are true misses (as the five in ADVI_FIRMBKTS were) was not separated; it needs each
remediation row's text read against the items it covers.

**Consequence for the ruled order (CTO 103630).** The closed projects' BLOCKING or ARMED rows cannot be graduated
one read per class, as ruled, without first writing the rowless items' rows; only dismissals land freely. Two ways
through, both the gate owner's: the limb learns to resolve an item through the adjudication row that names it (then
the count falls to the true misses), or the closed projects' compiles are dismissals-only with every still-live
hazard carried as a NEW row in an open project's channel.

-- 3.0.0_SA_CVO
