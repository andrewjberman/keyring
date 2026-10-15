# RULING 2026-10-15 ~06:3xZ (1.0.0_SA_CTO, cluster lead) -- the S3 egress anomaly (10-11..14, $67.99): where each finding goes

**On:** `4.0.0_SA_CRO`'s findings `org/tier1_exec/4.0.0_SA_CRO/deliverables/S3_EGRESS_ANOMALY_20261011_14_FINDINGS_20261015.md`
@b05fee1182, on a muse relay (bus 600e9b14) said to be from Andrew and unconfirmed. Read-only research.

## The finding in one paragraph

- **72% of the egress ($~50 of $67.99) is site Z's data harvest runner re-reading its own bucket.** `opal-data-harvest`
  (8 GB) left S3 541 GB in four days. The runner re-reads a whole silver prefix on every append and on every
  (security, publisher) watermark. That is about 242 full re-reads per Bloomberg cycle, a cost quadratic in what is stored,
  and it has been climbing since 10-02. The workload attribution is INFERRED; the bytes are MEASURED.
- **Second, dell1 agent checks** pulled whole `opal-data-bd` tables (143 GB, IAM user `cloudops-dell1-agent-user`,
  MEASURED).
- **Third, `opal-data-assets`:** 53 GB, reader unread.
- **No tie to the MDPF edge gap.**
- The $2.14 of requests is a separate in-VPC request storm on `opal-313476888478-globgrph`.

## Placement

| gap | ruling | owner |
|---|---|---|
| **E1** the full-prefix re-read in `lib/research/harvest/store.py` and `lib/opal_data_harvest/harvest_grammar.py` | **FIX NOW, first.** It is the live cost, still running. Cache the silver index once per cycle per (source, table), or keep a small per-source manifest object; compaction second. Proof: one cycle's S3 GET bytes before and after, at the same pair count. | **site Z**: the runner's owner. AMGT_HARVST is parked on dell1, and the cycle runner was ruled site Z's for G6 (`2.0.0_SA_COO~O`'s defect cell). `1.0.0_SA_CTO~Z` names the cell. |
| **E2** the harvest bucket's egress is invisible | With E1: the runner prints S3 GET count and bytes per cycle into its own cycle record. That is a record, not an alert, and it is the proof instrument for E1. Bucket request metrics are optional. | site Z, the same cell |
| **E3** dell1 full-table pulls of `opal-data-bd` | Agent checks that need a whole table run in-region, or read the served platinum object. A check that pulls more than about 1 GB out of AWS names why. | **dell1** (`1.0.0_SA_CTO~DELL1` places it, ADVI/MDPF) |
| **E4** `opal-data-assets` reader unknown | One day of request metrics on the bucket names the reader. Then decide. | **dell1** (MDPF_CANON) |
| **E5** the globgrph request storm (in-VPC, about $1-2 a day) | One day of per-prefix request metrics names the reader. Low priority. | NFRA_CTLPLN, as a measure cell in a later round (laptop) |
| **E6** cost attribution needs a hand-parsed CUR | Create the Athena table from the CUR's own shipped template, so a per-bucket question is one SELECT. | NFRA_CTLPLN, the same later round |

**Not built:** no alarm, monitor or cost alert (the standing moratorium). Every instrument above is a record or a query.

**The email** muse asked for (to andrew@fideles.capital) waits: the Gmail connector in this session is expired and the
relay's origin is unconfirmed. The finding goes to Andrew in this terminal.
