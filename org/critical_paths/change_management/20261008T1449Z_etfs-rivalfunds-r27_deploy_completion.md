# Deploy Completion Record
**Date opened:** 2026-10-08T14:49:08.066912+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T130942Z
**Deploy:** ETFS_RIVALS round 27 (RIV-ho-1, RIV-rk-1, RIV-tw-1): five rivalfunds Lambdas at CLOUD 325bd4e0f8, NO republish; must move no served figure (halves: COO d9f31a4fb0, CTO 4457ff34cf)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply27.tfplan from C:/tmp/rv-r8: 5 aws_lambda_function.stage in place | rc 0, Apply complete 0 added 5 changed 0 destroyed; five live CodeSha256 moved and LastModified after the apply | safe-apply rc=0 from C:/tmp/rv-r8 at pin 325bd4e0f8, 14:56Z-14:57Z 2026-10-08: Apply complete 0 added 5 changed 0 destroyed. Five functions read after: CodeSha256 moved on 5 of 5 (daily 50EIl4Xb.., fetch-holdings 8sq83jGS.., build-silver XcZnD/CP.., build-canonical-shape PTcMhs7W.., publish-page /JVm0SXw..), LastModified 14:56:44Z-14:57:10Z, MemorySize 3008, State Active, LastUpdateStatus Successful. Halt gate: 86 pending messages acknowledged with HALT_ACK (76 known automated ledger nudges; the 10 newer ones were NOT read before the apply). Seat gate printed WARN: a COO does not apply. No republish. | CLOSED 20261008T145844Z |
| L2 | verify | first scheduled run on the round-27 package, 2026-10-09 11:00Z chain and 13:00Z sweep | REPORT lines; funds_updated; table rows against the day before in shape; AI account badges read served | Read by 2.0.0_SA_COO~V1 2026-10-09 13:1xZ (round28/report_lines.py + sweep_read.py, read-only). 11:00Z chain on the round-27 package: fetch-holdings 1.0 s, build-silver 2.4 s, build-canonical-shape 157.9 s, publish-page 177.0 s / 1022 MB; page 2026-10-09 published 11:06:19Z, funds_updated 11 of 13 (CGIC, SCHY lag 2 as on 10-08). A second chain at 11:07:39Z (the pipeline's own late-input catch-up, stale_rebuilt) re-served 2026-10-08 at 11:13:38Z, 13 of 13. The 13:00Z sweep ran on aw-1's package (live 11:20:54Z-11:21:19Z, which superseded this one): etfs-rivalfunds-daily-lambda 504.6 s / 1001 MB, 0 timeout or [ERROR] lines across the five functions 10:55Z-14:00Z; manifest 2026-10-09 regenerated 13:08:34Z, funds_updated 13 of 13; AI rows 26 (13 + 13), ai_grounding served 26 earlier 0. No served figure moved by the deploy act itself. | CLOSED 20261009T130924Z |

## Log

- 20261008T144908Z OPENED by 2.0.0_SA_COO~RV with 2 leg(s)
- 20261008T145844Z LEG L1 closed: safe-apply rc=0 from C:/tmp/rv-r8 at pin 325bd4e0f8, 14:56Z-14:57Z 2026-10-08: Apply complete 0 added 5 changed 0 destro
- 20261009T130924Z LEG L2 closed: Read by 2.0.0_SA_COO~V1 2026-10-09 13:1xZ (round28/report_lines.py + sweep_read.py, read-only). 11:00Z chain on the roun
- 20261009T130942Z CLOSED -- all 2 legs proven
