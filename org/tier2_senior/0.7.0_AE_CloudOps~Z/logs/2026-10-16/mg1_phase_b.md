# OG-mg-1 Phase B -- session log (0.7.0_AE_CloudOps~Z, 2026-10-16)

- ~11:15Z GO msg 34954 read (all three halves at ask sha256 757f5146afee). C1-C8 read from the COO half.
- ~11:19Z C2 re-read (W/mg1_phaseb_reread.py): Andrew and Bloomberg hold 0 POLICY# items, Alyssa active/restricted/4/4, host MASTER_ADMIN_EMAILS exactly 1 alias, candidates unchanged. CLEAR.
- ~11:20Z ledger nfra-oplgtw-r30-grant-writes opened, entry and sentinel committed by the tool.
- ~11:22Z R1 then R2: one activate each under opal-gateway-access-admin (W/mg1_activate.py); both ACTIVATED profile_revision=1 grant_revision=1.
- 11:23:57Z read-back (W/mg1_readback.py): both active restricted rev 1, 13 months, R2 scope equals R1, Alyssa hash b93cd3cbf990 unchanged, POLICY# 17 to 25.
- ledger legs closed with proof, ledger CLOSED; records committed at 8e44440e66.
- mg1.AC2.sh graded FAIL on its own shape; row Z-S174 (9c8d5dbbd6); NOT revoked; reported to the COO (msg to 2.0.0_SA_COO~O).
- COO msg 34967: check fixed at f30d9fdce8; AC1 and AC2 re-run PASS; proof instance written by W/mg1_proof_gen.py.
- No tid, oid, email, account id or scope value in any repo file.
