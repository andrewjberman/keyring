# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` grades landed pins after the fact while the lease is FAST.
Drive: the /closer-drive loop resumed on Andrew-direct "recs approved for all" (CTO 101296); cron 312e843c.
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-27T14:5xZ (b). Earlier forms of this file are in git (`git log -p -- <this file>`).

## Pins (served)

| What | Value | Ledger |
|---|---|---|
| irpt-performance-adapter | `bOefL9nx..` since 05:22:03Z (09-27) = Ll6t4VPa + COT actual_start (backend 05778597eb, publish f360e6c80e); earlier: P-REOPEN-01, both timing lines, S147 fix M; NO armed plan since 04:34:55Z (`approved_performance_plan = null`, no session grant) | irpt-reopen-authz / irpt-adapter-timing2 / irpt-authz-memo-20260926 / irpt-performance-cot-one-use-1-20260927 / irpt-cot-actual-window-20260927 CLOSED |
| irpt-ycharts-generate | `G/TqLPdL..` since 02:15:03Z (09-27) = hop-3 six + the cross-viewer title binding (f8c72944f3) | irpt-cross-viewer-title-20260927 CLOSED |
| Resident (i-0167fd745ad906a66) | `/opt/irpt-resident/fe64236bbb-dx` since 14:50:22Z = cw + ~Y's W13 diagnostics (ec5804f6e0); cw = wf + the W11 fixes (b6739556ea); rollback roots cw, wf, rb, xv, rr, h7, fe64236bbb, f624e8a72f kept | irpt-resident-waf-refresh-20260927 / irpt-resident-capture-env-20260927 / irpt-resident-w13-diagnostics-20260927 CLOSED |
| irpt-status | `bMMJ/bQ+5..` since 19:56:53Z (+interactive_access.py); irpt-status-role reads BY VERSION | irpt-status-reads-20260926 CLOSED |
| irpt-directory-search | `o1TXq5PH..` since 22:54:12Z: UIR-07 exact full-name match first in search AND browse(q) (49b935c213); -target apply | irpt-uir07-search-rank-20260926 CLOSED |
| irpt-export-render | render ON behind the S148 fence | irpt-export-deploy-b-20260926 |
| Backend branch | `irpt-smoke-p-backend-20260923` @3aa870163d (not pushed) |  |
| Publish worktree | `irpt-p-publish-20260923` (source-map record after f360e6c80e; not pushed) |  |
| Push state | LOCAL, unread against origin this turn; MSTR pushes |  |

## Live thread

- **49F Performance, account-level:** served. A second authorized viewer now reopens a retained report (arm 1 PASS);
  window 4's K7 refusal was this defect.
- **Hop 3 (Analysis generate):** the title producer, the packaged settings path and template-lane admission are served
  in generate AND the resident, content-proven 6/6 (`IRPT_MVP_P/HOP3_DEPLOYED_CONTENT_PROOF_20260926.md`).
- **Hops 8-9 (status reads):** served; ~Y's no-overlay proof 4/4; IAM 10/10.
- **Next window (CTO 101441/101466):** ONE window runs upload, generate, READY, sections and history for Analysis. It
  is cut once ~Y's offline pre-flight of hops 5-9 is pinned. K5's measured write set: ~Y 101484 @f36c5ee4c4.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance DONE at all three: 49F (account-level, reopen fixed); INF RPT-df47a1fc (one Orion call, 7.98%); COT RPT-b683f188 (one claim, 2 BD requests, -1.18%, reopen served). Analysis: breaks at hop 6 (YCharts WAF on the read-back). Export: render ON; the first real export is not run (K8) |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | Next-list item 3. Real-data run RPT-b683f188 exposed an overstated window (actual 01-02 = the provider's calendar grid; the account's series starts 07-21). FIXED and served (bOefL9nx): the recorded bytes now give actual 07-21..09-22. The retained RPT-b683f188 is immutable and still shows 01-02; a corrected COT report on real data needs ONE new COT use: both halves and a ledger (Andrew's session egress word, MSTR 101850) |

## Write claims

None. Window 8 CLOSED 04:46:35Z (ledger @f293962a58).

## Next-list (in order)

Andrew-direct 02:5xZ "yes to all three" (@6039c2f680): all three calls USED (window 7; INF; COT). Andrew at ~Y 04:01Z
"yes, run the Analysis window" (W8-2): USED. Any further window or vendor use needs a new word.

1. **Analysis hop 6 (the live-thread break):** window 13 (14:11-14:33Z) ran the fifth attempt on resident cw.
   REQ-2119def4 went ATTENTION VENDOR_READ_BACK_REFUSED, and portfolio 2363820 is kept. It got CLOSER:
   - capture_env worked (no LEASE_NOT_HELD), but the form sign-in met CAPTURE_FAILED:UNEXPECTED_CHALLENGE and stored
     nothing;
   - on redelivery the saved-portfolio read worked (7 of 7 fields present), and ONE value differs: level_as_of_type.
   Bounds held (4 status GETs, 1 saved GET, 1 attempted re-capture). Running re-capture total: 1 attempted, 0 completed.
   ~Y's W13 diagnostics (ec5804f6e0: the journal names the stored value and the capture's runner reason) are SERVED as
   resident `fe64236bbb-dx` since 14:50:22Z (@cfbc1989ff). Next: window 14 on ~Y's ask, cut on window 13's te2. **K8, the first real export:** window 12's POST was refused because the submit omitted selected_tenant. ~D's fix
   IV-e-64 is drained at local portal DEV 55bbdd71. The window-14 packet (blob 423314f1, @a68848d634) is out for both
   halves. The next Analysis attempt is window 15.
in.
3. **A corrected COT report (IRPT_BCKEND-S157, criterion 3 on real data):** unblocked. Andrew-direct relayed by MSTR
   101850 reads "they have egress for full session", and the loop prompt permits vendor uses, each ledgered. It needs
   ONE new COT use: plan 2 on the same account through cot_one_use_plan.py (no vendor call), a packet, both halves,
   a ledger, the arm, ONE read, and a disarm to null. The read is bOefL9nx's first real-data COT report, and it must
   disclose 07-21 as the actual start.
   MEASURED 12:29:54Z (COT_S157_PRECHECK_20260927.json, cot_direct_read.py, plan OFF, V1 direct invoke): the same
   account and window 01-01..09-22 REOPENED RPT-b683f188 through the retained pointer (PERFORMANCE_ACCEPTED is keyed
   by selection and window, not by viewer). It showed actual 01-02..09-22 with the series from 07-21, and made 0
   vendor calls (COT claims 2 -> 2). So:
   - plan 2 as built (sha 8bd7774e, 01-01..09-22) would never be spent;
   - the corrected read needs a different window, e.g. 01-01..09-21, re-built and signed;
   - the page's COT YTD view keeps the overstated face for 01-01..09-22 until the holdings as-of advances
     (S152/R4, Monday), or until the pointer is superseded, which is a served move needing its own half.
4. **S152** (INF holdings 3 trading days behind): ~M's; it disarms on the R4 Monday enable.

**DONE this stretch:**
- Window 13 (the fifth Analysis attempt) opened 14:11:33Z and closed 14:33:10Z: 0 outside the classes; writes = K4/K5; bounds held.
- Window 12 (K8 re-cut) opened 13:35:19Z and closed 14:03:20Z: the export refused at submit, nothing written; 0 outside the classes.
- Window 11 (the fourth Analysis attempt) opened 12:56:51Z and closed 13:22:00Z: 0 outside the classes; writes = K4/K5 only; bounds held (@ledger irpt-ui-walk-principal-w11-20260927).
- Andrew-direct "rec approved" (/open-calls CALL 1): ledger irpt-p-live-scope-20260923 CLOSED on the agent walks (@22c2fc699d).
- Window 10 opened 06:19:10Z and closed 06:32:17Z. K7 reopened a 49F report (8.05%); K8 was not run (the page refused); 0 outside the classes; 0 new media in git.
- S157 filed (COT retained face overstates its window) and named in the release item (@52f078fe1e).
- Window 9 (~D's read-only round-7 walk) opened 05:37:40Z and closed 05:48:24Z: 0 outside the classes (@eade2ba0f5).
- Resident wf served 05:54:14Z (@f57a08f106 OPEN; CLOSED this commit).
- COT window disclosure (criterion 3): actual_start is now the account's first series point; served bOefL9nx,
  DELTA=0 on every reachable surface (ledger irpt-cot-actual-window-20260927).
- INF signed-in Performance: plan 7f64b166, ONE Orion call, RPT-df47a1fc PARTIAL, 7.98% (01-01..09-22).
- COT signed-in Performance: plan 22f0a988, arm-OFF pre-check 3/3, armed 04:29:10Z (1/1/1), ONE claim 04:31:30Z,
  2 BD requests (provider evidence ART-36a64d88), RPT-b683f188 PARTIAL, -1.18%, reopen served; disarmed to null
  04:34:55Z (0/1/1). Ledger @ffe4269b12.
- Window 8 closed: route audit 0 outside the classes; write set traced; users equal (@f293962a58). Finding: the
  auth-log by-name read is blind (the handler logs method+path only), so K1 absent is the proof.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| The kept test inputs and reports from windows 1-6 in cottonwood (UPLOAD#/INPUT#/analysis#/REPORT# rows and objects owned by deleted walk principals) must be excluded from any firm viewer's lists, or removed, before the route opens to firm users; include by KEY irpt-jobs cottonwood / REQ-3a1b73a8dead02a17a09043b, the window-6 job left SUBMITTING, since a tenant-wide job listing would show it as never finishing (CTO 101678); and by KEY cottonwood REPORT#RPT-b683f188c2e13da7865eeceace6334c3, COT's K12 report whose retained face overstates its window (IRPT_BCKEND-S157, CTO 101825); closes as not needed only if EVERY reader lists by owner (4.0.0_SA_CRO 101609) | the release cutter | the route opening to firm users |
| MSTR removed the backend worktree's Terraform provider caches (101858): run `terraform init` in a root before its next safe-apply | 2.0.0_SA_COO~P | the next apply in irpt-smoke-p-backend-20260923 |
| The backend worktree's directory Terraform root predates M's holdings resources (a full plan would destroy 11); UIR-07 used -target | 2.0.0_SA_COO~P | the next directory-root apply: merge CLOUD into the backend worktree first |
| `build-and-upload.sh` deletes tracked performance/*.py from the publish tree on each adapter build | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| `build-and-upload.sh` zips a source_dir JSON with the checkout's EOL (CRLF here), and its artifact record passes through MSYS path conversion (`/iFh..` became `C:/Program Files/Git/iFh..`) | 1.0.0_SA_CTO to route (ci/ owner) | the next build of a function whose hash starts with `/`, or that hashes a JSON member |
| The performance root's per-apply `approved_performance_plan` variable is null now; any later arm passes its plan file, and the disarm is null | 2.0.0_SA_COO~P | the next per-use word |
| 49F engine: 9 funded non-computable accounts; 219 of 5194 divergent vs BD | 1.0.0_SA_CTO to route (49F engine lane) | the engine lane's next c02 act |
| ~D's COT card read HOW MUCH -$40,348.28 (a negative client total) on ****0441 | 2.0.0_SA_COO~D | ~D's next COT face review |
| The adapter answers an internal viewer's Performance GET that lacks `selected_tenant` with UNAVAILABLE/UNEXPECTED (BucketUnmapped at the directory-bucket map), not a named refusal (w10 06:25:22Z, corr-27a7339e0e20) | 2.0.0_SA_COO~P | the next adapter deploy, or a firm user seeing UNEXPECTED |
| 49F directory lists 790 not-terminated accounts the custodian shows empty/absent | 2.0.0_SA_COO~M | M's next directory refresh |

## Limits

No vendor call is made by this seat without its per-use word; the INF use fires only on a signed-in request. Nothing
here is pushed.
