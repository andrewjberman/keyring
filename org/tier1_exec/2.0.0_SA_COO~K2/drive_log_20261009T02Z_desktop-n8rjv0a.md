# 2.0.0_SA_COO~K2 drive log -- 2026-10-08 23Z to 2026-10-09 02Z (desktop-n8rjv0a)

IRPT_CUSTDY tick lines from org/mcp/drive_ticks/2.0.0_SA_COO~K2.md since the 22Z log (@62ac1555ad):

- 23:23-23:30Z msgs 1910/1931: Step F applied 23:24:52Z (dell2 writes its own IAM roles/policies via 0.7.0_AE_CloudOps~DELL2).
- 23:34Z E2a gate not measured open (~P2's log headline vs body); 23:55Z NO-OP.
- 00:21Z msg 1972 law edit 538f0f51a7 (box/* is a shared branch; seats commit to box/dell2). 00:33-00:40Z Step G applied; the
  /mdpf/custody_source write Deny stays. No IRPT_CUSTDY effect.
- 00:27Z IAM leg applied 22:47:14Z (b8d0c40390) and IB-pr-378 route live (RouteId jtwlf6l); last gate E11.
- 00:42Z release 4 (E11) rolled back (row D2-S16). 01:08Z release 5 issued.
- 01:1xZ empty tick -> /next-calls --drive (switch empty_tick=on, measured): ADDENDUM 2 split E2 into CU-g-5 (data half) and CU-g-6
  (PROD print page); TO-CU-g-2a committed @1e4740e63d. The gate first refused 'CU-g-2a' as a cell id (no letter suffix), so the
  cells were renamed CU-g-5 / CU-g-6.
- 01:39Z release 5 LIVE at 4HEH1aDN; worker 0.9.0_WK_IRPT_CUSTDY~18 spawned on TO-CU-g-2a.
- 01:5xZ CU-g-5 BLOCKED. The worker stopped before any AWS write (0 of 2). Row W18-S1 drained @c562748b71. Issuer verified in the
  repo: reports/generate_installed.py:172 raises CUSTODY_FACTORY_REQUIRED, and custody_submission.py has only test importers.
  DECISION ask to the CTO (msgs 2119-2121). Ruled (msg 2123): ~Y2 ships the custody factory as release 6; bearer = the
  service-principal pattern (token in Secrets Manager, read by the applier under the pair).
- 01:56Z msg 2141: keep-driving ON for every box and COO (Andrew-direct ~01:5xZ); already applied here.
- 02:14Z release 6 in progress: ~Y2 published the AcceptedCustodyReader port contract (859ae01405); ~M2 built holdings_publication_for
  (dd546a3c02); CTO ADDENDUM 13 (1aee15882f). CU-g-5 re-spawns on release 6 LIVE, its order amended then for the principal and the
  applier-held token. CU-g-6 on the print page (row 0347).
- Housekeeping: worktree /c/tmp/wk-irpt-custdy-18 left in place (recursive delete needs human confirmation; merged, worktree_gc
  removes it at 24h idle).

## Compiler Tools

- to-pipeline-gate at commit: refused 4 cell-id violations on the first cut, then OK after the rename; it caught a grammar error the
  author did not see.
- comp-find 'CustodyFactoryRequired' (5 hits / 595 files) and --name generate_installed.py (2 / 84,518): located the live handler,
  which the worker's path and this seat's first grep had placed in the wrong package.
- open-calls.py mode get: empty_tick=on (default ON, then SET 01:53:41Z).
