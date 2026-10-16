# Drive log -- 2.0.0_SA_COO~MP, NFRA_MCPORTAL, 2026-10-16 ~17:3xZ to ~18:3xZ (host opal_bloomberg, site Z)

Substantive ticks only; the runtime file is `org/mcp/drive_ticks/2.0.0_SA_COO~MP.md` (gitignored). Push state is stated in the commit message that carries this log.

| time (Z) | limb | outcome | act |
|---|---|---|---|
| ~17:27 | wait | WAIT | no new mail; manifest unchanged; the 16Z log block committed (8845ad84f4); a different project's gateway deploy (HARVST) open in the ledger |
| ~17:57 | wait on a live owner | WAIT | `~Z` opened `nfra-oplgtw-gateway-release-batch2` at 17:53Z (OG-ap-28 Phase B, release commit bf9d23b518, on live base d14445961d); the release's manifest reads mcportal_commit 59e802a (read from the commit), so MP-pf-11's cue rides it; wait recorded with `--owed-ledger` against `0.7.0_AE_CloudOps~Z` |
| ~18:00 | /next-calls --drive FREE option | DRIVE FORWARD | built mcportal 59e802a locally, wrote `pf11.host.sh` from its hashes; the host already serves that bundle (SSM 115eccd3, PASS) and the old bundle's check FAILs the same minute (SSM c8354d18, the negative control); `pf9.real.sh` with `MP_REAL_WANT=59e802a MP_REAL_CUE=1` on the served body of 18:01:02Z: 390 of 390, 1280 of 1280, 0 offenders, the Indexes cue on 14 of 14 boxes (6 scroll); kept real-data page deleted; record f90c035d06; the CTO told in one message |
| ~18:27 | wait | WAIT | `~Z`'s manifest commit is on the local trunk (deployed bf9d23b518, mcportal 59e802a); the batch2 ledger entry is still OPEN (unclosed legs: deploy, served-read, standing-clauses); no mail |

Open: `~Z` closing `nfra-oplgtw-gateway-release-batch2`; the CTO's word that Andrew is ready (call 21d9, then the MP-v-2 window f0d2); calls def4, 21c5, 8ed7 are Andrew's acts; PD held by the CTO until OG-cp-1 and Andrew's sitting; MP-pd-7 is staged to ~NFRA1 (MSTR~Z is told at the GO); Z-W28-S1 and Z-W32-S1 are the issuer's two armed rows, carried on purpose (Z-S73).
