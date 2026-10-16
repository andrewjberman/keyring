# Drive log 2026-10-16 00Z (covers 21:42Z to 00:50Z) -- 2.0.0_SA_COO~G2 (dell2)

Scope: IRPT_YCDGEN and IRPT_ANLREQ workstream G (ENGINE). Push state: LOCAL on box/dell2 (not read at the remote).

| project | limb | rounds | acts fired |
|---|---|---|---|
| IRPT_ANLREQ ~G | EXECUTING | 21 to 25 | R21: AR-g-92 build (w197), W197-S1 ruled, merged; pair packet r32 @8c4ecd6fc7; CTO half 8693; apply order TO-APPLY-R32R to AQ2 @75160639c8; r32 APPLIED 22:09Z (record and ledger read by the issuer). R22: AR-g-96 door decision tree (w198) merged @78e28b386b. R23: AR-g-98 swap pass+pool builder (w199) and AR-g-99 Yahoo history port (w200) merged. R24: AR-g-100 producer swap (w202), AR-g-102 r33 Lambda source rows + GetItem policy (w201) merged; AR-g-105 six-object delete order to U7 (Andrew's call 2106). R25: AR-g-101 resident swap-pool binding (w203) merged. |

- Every cell: issuer-owned check dry-run at base, a reference build in a scratch tree, mutants (AR-g-96: 9, AR-g-98: 27, AR-g-99: 14, AR-g-102: 18, AR-g-100: 15, AR-g-101: 13) each failing its check; each merged branch re-verified by the issuer on the merged tree.
- Release 33 census on the merged tree: `release-census.py irpt-ycharts-generate --pin HEAD` prints changed_members=8 (five re-pinned rows, two native members, `ticket_confirmation.py` added), exactly the order's prediction.
- Rulings recorded as rows: S129 (W197-S1), S130 (W198-S1 stale prose left), S131 (W199-S1 chunk equality measured), S132 (W200-S1 account-id read), S133 (W201-S1 proof clause).
- CTO rulings used: 8693 (r32 half, AQ2 applier), 8711 (swap compose then r33 then r34), 8714 (pool = dated snapshot, no IAM), 8723 (no class: "not analysed", classifier later). Live reads: BREIT, SREIT, KPEC, TIMXX have no etf-classifications row.
- Next: r33 build record (AR-g-103), r33 pair packet and applier order, r34 tooling (pool export under an applier order, release build, pair), U7's delete report.
