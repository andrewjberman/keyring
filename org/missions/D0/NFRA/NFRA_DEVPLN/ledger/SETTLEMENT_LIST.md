# NFRA_DEVPLN -- portal settlement list (cell DP-s-1)

- Measured refs (read-only, no fetch): origin/DEV `24877b67`, origin/PROD `10e7664d`, written 2026-10-13T21:25:51Z (UTC).
- Tool: `.tools/portal-settlement-list.py` on the portal repo `portal/`. Every git call is a read.
- Headline: DEV is ahead of PROD by 8 commits; PROD is ahead of DEV by 1 commits; 11 files differ DEV-not-PROD; 6 remote branches hold work not on DEV.
- The class column is the unsure rule (an input). Andrew rules each group once: approve forward, hold on a branch, or drop.

## 1. DEV-not-PROD groups (git diff --name-only origin/PROD...origin/DEV)

| group | class | files changed | commits touching (origin/PROD..origin/DEV) | top three committers (commits) |
|---|---|---|---|---|
| InvestorReporting | client-facing | 0 | 1 | 0.0.0_AB_MSTR~DELL2 (1) |
| SecurityAnalysis | opal-internal | 0 | 0 | none |
| TicketCenter | client-facing | 10 | 7 | 0.0.0_AB_MSTR~DELL2 (3); 0.9.0_WK_IRPT_ANLREQ~90 (2); 0.9.0_WK_IRPT_ANLREQ~87 (1) |
| AdvisorIntelligence | client-facing | 0 | 0 | none |
| api | client-facing | 0 | 0 | none |
| firmAccess | client-facing | 0 | 0 | none |
| other | client-facing | 1 | 1 | Andrew Berman (1) |

## 2. PROD-only commits (git rev-list origin/DEV..origin/PROD): 1

| # | sha | author | date | subject | same patch on DEV (git cherry) |
|---|---|---|---|---|---|
| 1 | 10e7664d | Andrew Berman | 2026-10-13T16:51:48-04:00 | merge feature cand/laptop/contributing-boxes into release/20261013T205139Z | n/a (merge commit; git cherry omits merges) |

## 3. Remote branches with work not on DEV (ahead of origin/DEV; excludes DEV, PROD, HEAD): 6

| branch | ahead | cherry + (patch not on DEV) | cherry - (already on DEV) | merge commits (cherry omits) | tip sha | tip date | owner (tip author) |
|---|---|---|---|---|---|---|---|
| irpt-dev-candidate-3-20260924 | 3 | 2 | 1 | 0 | 7897f891 | 2026-09-24T03:04:43-04:00 | 2.0.0_SA_COO~P |
| cand/laptop/declined-example | 2 | 1 | 0 | 1 | b5222d78 | 2026-10-13T17:08:47-04:00 | Andrew Berman |
| q/dell2/wk-IRPT_BCKEND-167-portal/r1 | 2 | 0 | 2 | 0 | 63b9382a | 2026-10-07T19:19:45-04:00 | 0.9.0_WK_IRPT_BCKEND~167 |
| wk-dsgn-irptv1-r25-61-prodcut | 2 | 2 | 0 | 0 | fc876722 | 2026-10-11T14:16:13-04:00 | 0.9.0_WK_DSGN_IRPTV1~61 |
| irpt-opal-scope-p-portal-20260923 | 1 | 1 | 0 | 0 | e0531491 | 2026-09-23T11:12:24-04:00 | 2.0.0_SA_COO~P |
| wk-IRPT_ANLREQ-51-portal-r4 | 1 | 1 | 0 | 0 | 890f1d0f | 2026-10-11T07:05:45-04:00 | 0.9.0_WK_IRPT_ANLREQ~51 |

## 4. Machine lines

```text
group InvestorReporting class=client-facing files=0 commits=1
group SecurityAnalysis class=opal-internal files=0 commits=0
group TicketCenter class=client-facing files=10 commits=7
group AdvisorIntelligence class=client-facing files=0 commits=0
group api class=client-facing files=0 commits=0
group firmAccess class=client-facing files=0 commits=0
group other class=client-facing files=1 commits=1
```

SETTLEMENT-LIST dev_ahead=8 prod_ahead=1 groups=1 files_total=11 files_other=1 branches=6
