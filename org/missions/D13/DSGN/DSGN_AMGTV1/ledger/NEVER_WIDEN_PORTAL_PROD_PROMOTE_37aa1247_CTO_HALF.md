# NEVER-WIDEN CO-SIGN -- CTO HALF. Portal PROD promote `18364342 -> 37aa1247` (DSGN rounds 67-68 ONLY)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~16:5xZ. It is signed after the CVO's grades of every order the candidate carries:
- zzr-1 MET (`ADJUDICATION_v42.md` @e252f0964b);
- zzs-1 MET and FWD-27 MET (`ADJUDICATION_v43.md` @04725034ee, msg 2851).

## Measured at signing (portal repo, after a fetch)

- origin `PROD` = `18364342` (portal-v2.1.210), the candidate's base. FIVE single-parent commits sit on it: AV-zzr-1, its amendment 2,
  and AV-zzs-1 with items 4 and 5.
- 7 files, +140 -60. **0** outside `src/pages/SecurityAnalysis/`. **0** added `fetch(`, `apiRequest` or `useQuery`.
- The SA tree EQUALS DEV `c96efe17`'s (reviews @a0b1e341b6 and @d6ab455b18).

## VERDICT

**PROD `37aa1247`: SIGNED.** Blast radius: PROD's ref and its build. Rollback: PROD back to `18364342`. Security Analysis is a staff page, so
no word from Andrew is owed. The COO half is `2.0.0_SA_COO~D1`'s, at this hash. `0.0.0_AB_MSTR~DELL1` runs `/prod-deploy`.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
