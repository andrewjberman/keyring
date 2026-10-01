# Window packet -- E3, the Multi-Comp arm, on the st9 resident: leg P (ONE liveness read), leg S (ONE operator sign-in, only if the session is not live), leg J (ONE Multi-Comp job attempt); the trial of E2

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~15:0xZ.
**Authority:** CTO rulings batch 88 item 4 (E3: "the Multi-Comp arm, as batch 61 item 8 named it first"; E2 "rides the
next attempt") and batch 89; Andrew-direct 2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`)
for leg J; his standing word of 2026-09-23 item 3 for legs P and S, with batch 88 item 3's standing terms for the
sign-in. Comparison permission: `ANDREW_DIRECT_20260927_195xZ_COMPARISON_PERMISSION_YES_AND_PURGE_S19_SCREENSHOTS.md`
(the catalogue's own `permission_ref`). **Precondition, met:** st9 is installed (`ST9/INSTALL_OUTPUT_20261001.txt`:
running root `481166a8f2-st9` since 14:59:17Z; `resident_worker` `49305eeb90d80034`, `recipe` `3a4e58515476b841` with
`READ_BACK_POLLS = 1`; ledger `irpt-resident-st9-20261001` CLOSED). **Ledger:** `irpt-e3-multicomp-20261001` (legs P1,
S1, J1, J2, J3). **Runner:** `live_walk/e3_multicomp_run.sh` (the hop-8 runner with this window's folder, root, base
and the two keys); every leg refuses unless the running root is the st9 root.

## The legs

- **Leg P, one GET, no sign-in:** `live_walk/session_probe_host.sh` (sha256 `d3fef0997c999014..`, unchanged). `LIVE`:
  leg J runs. `NOT_LIVE:<status>`: leg S runs. `CHALLENGED`, `RAISED`, `NOT_RUN`: the packet ends.
- **Leg S, ONE operator sign-in, only on `NOT_LIVE`:** `live_walk/leg_s_host.sh` (sha256 `c2ec45793fbfbabe..`,
  unchanged), under batch 88 item 3's standing terms: at most once in 24 hours (none has been used since they were set;
  the last sign-in from the host was 08:21Z). `AUTHENTICATED`: leg J runs, not sooner than 600 seconds later. `FAILED`
  or `CHALLENGED`: the packet ends; the standing terms end until the CTO reads the reason token.
- **Leg J, one Multi-Comp job attempt:** `svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of
  `aapl-vnq-12.03.csv` (35 bytes, sha256 `bb079cbf..0960ddc`), ONE K5 POST with `comparison_keys`
  `opal_short_term`, `opal_intermediate_term`. The variant is the chain's own rule on the key count (two keys:
  `multicomp`, template 14141847), never typed; the runner's plan validated this K5 body at 14:48Z with no network
  call. The two keys are the ones the maintained catalogue records as that template's own live-proven comparisons
  (`templates.json`, `live_proven` true, identity VERIFIED 2026-09-27). No retry; a 60-minute deadline. Evidence base
  `E3_MULTICOMP/E3_multicomp_cottonwood`.

Write set and vendor calls as the hop-7 packet lists them, with the Multi-Comp template in place of the Overview's:
two symbol lookups (sessionless since st7), one holdings upload, one model portfolio, its status reads, the report
validation and ONE report generation naming the job's portfolio and the two catalogue models, one PDF download. The
two models are Opal's own; nothing of another firm's is read or written.

## What is new in this attempt, and what each stop reads

| | what is read |
|---|---|
| **E2, first live run** (CTO half of st9, item 1) | EVERY receive of the job is quoted in the outcome with its time and its status answer: `READ_BACK_PENDING:CALCULATING` with a redelivery about 120 seconds later, or `READ_BACK_DONE`. If the single status read of a later receive is challenged, E2 is withdrawn (batch 88). If the job dead-letters still calculating, it is redriven ONCE with `ST6/redrive_one.py` and reported; a second such job withdraws E2 by rollback to st8 without a further ruling |
| **the Multi-Comp variant on served code** | the printed-comparisons check (`COMPARISON_NOT_PRINTED` names a chosen model the PDF does not print); the printed-type line `TOLERANCE_TYPE ... name=` for the job's own row beside the two models' Dynamic rows; then certification of a Multi-Comp PDF, which today's code has not met. A refusal at the printed-type check prints the census and keeps the PDF (st7), and the status read comes first |
| the upload does not read NORMALIZED | the `RESOLVE ... PROVIDER_READ_UNAVAILABLE:<CLASS>` lines; K5 is not made |
| the job reads EVICTED | reported FIRST; the resident's own sign-in then prints its reason token and keeps its stderr |
| the job reads READY | `job_status_route_read.py` (both status forms and the sections route); `case_trace.py cottonwood <REQ>`, which checks the variant against the key count, each key's frozen identity against the catalogue, and that the PDF prints exactly the chosen models; the page walk is asked of `2.0.0_SA_COO~D` |

## Stops

1. Both halves at HEAD naming this file's blob, before any leg.
2. Before each leg: the running root is `481166a8f2-st9`; no non-terminal job; both queues 0/0.
3. Each leg ONCE; the runner refuses a leg whose output file exists. At most ONE sign-in by the operator.
4. Leg J: ONE login to Opal, EXACTLY one K4 POST and one K5 POST. If the upload does not read NORMALIZED, K5 is not
   made and the attempt is over.
5. If the session is displaced after leg P or leg S and before the job's first read, the job reads EVICTED and the
   resident takes its one refresh by itself. It is reported first; no further sign-in is made from the host today.
6. At the 60-minute deadline a job still non-terminal is reported to `1.0.0_SA_CTO` before anything is posted or
   redriven, except the ONE redrive of a dead-lettered still-calculating job that the st9 half's item 1 already orders.
7. Each output file is read for values before it is committed. A kept PDF is not committed and not uploaded anywhere.
8. Any deviation not named here stops the window for a new half.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~15:0xZ, on this packet's bytes at the commit that carries it. The two host scripts are unchanged;
the runner is the hop-8 runner with its folder, root, base, ledger and keys set by the wrapper; the K5 body was
validated offline.

## CTO half -- 1.0.0_SA_CTO

(owed)
