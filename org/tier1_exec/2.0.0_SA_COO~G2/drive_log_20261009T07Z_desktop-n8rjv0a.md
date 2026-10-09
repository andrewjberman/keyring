# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 07Z-10Z (IRPT_YCDGEN rounds 6-7; IRPT_ANLREQ ~G round 2)

## IRPT_ANLREQ
- r1: the <to_id> tags were amended to the short form @3f3ee09cc2; round-close-check reads MAY-CLOSE (9/9).
- r2: AR-g-21 and AR-g-22 issued @beb1d1466d, with I7_SAMPLE.json published (ruled the one sample, R2 AMENDMENT 1). Drained @96fadff10c
  (g21 10 passed) and @7a4d27f997 (g22 40 passed); test_opal_packager is green again. AR-g-23 waits on ~T2's commentary apply.

## IRPT_YCDGEN
- 08:25Z THIRD-EMPTY-TICK: unblock UB-...-1e60 opened. CTO fold: st28 runs ahead of V12. The applier ran U2..W1; V1 read svc->OPAL.
- 08:47Z F1 was denied on the secret until the laptop reader ADD at 09:09Z. 09:13Z F1 (REQ-1f8b...) was accepted, then the resident
  retained it on ClientError. CloudTrail: sts:AssumeRole AccessDenied on irpt-49f-ycharts-research-role (NoSuchEntity). Row D2-S19
  @31b9816847.
- CTO ruling @f29d0d8ca1: round 7 = a research role per allowed firm. YCD-a-7 issued @d5e3459acb and drained @23e39f11d7 (firms 3,
  fence 6 prefixes, regress OK). The r7 pair @4cf3a805c7 was GIVEN @717d42269a, with AMENDMENTs 1 and 2 (the simulate order). The
  applier applied @0617cb243d: 3 roles, AssumeRole = 3 ARNs. The laptop principal 3x3 is clean (msg 3160).
- CTO msg 3063: hold st28 + svc-on-49f to the re-run, bound 13:09:10Z.
- 10:37Z F1 re-run (REQ-448d...): AssumeRole OK, then RetentionRefused, because st28's packaged registry lists the research row as
  [cottonwood]. Built st29 = st28 + that row @f0ff4f1653 (scratch branch, audited override IRPT_COMPLETION_REGISTRY); gate PASS
  (changed 2). TO-APPLY-st29 + packet @33ba944f23; CTO half GIVEN (msg 3183). D2 waits for irpt-generation 0/0.
- Secret reads reported: 09:13Z, 09:36Z, 10:36Z. Host reads reported (SSM 2aa69757, 14ca8aef, 422df389).
