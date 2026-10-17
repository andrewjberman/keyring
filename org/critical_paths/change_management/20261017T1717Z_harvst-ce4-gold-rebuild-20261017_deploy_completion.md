# Deploy Completion Record
**Date opened:** 2026-10-17T17:17:23.433987+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T193624Z
**Deploy:** AMGT_HARVST HVST-ce-4: ADD-ONLY gold rebuild in s3 opal-data-harvest for the 31 names of ce4_securities.txt (sha256 7881772d..): amgt/harvest/gold/research-continuation/security_key=<KEY>/<sha16>.json and amgt/harvest/gold/research_dossier/security_key=<KEY>/as_of=<as_of>.<sha16>.json, at most 62 new keys, from a worktree at 344ea6a5fc; window 2026-10-17 17:20Z to 19:30Z; canary UNH then KMB read served first; manifest ce4_written.out; no S3 delete
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at 344ea6a5fc; ce4_securities.txt sha256 equals 7881772d..; CPA control and UNH/KMB BEFORE reads | ce4_before.out | PASS. ce4_before.out: worktree C:/tmp/ce4-build detached at 344ea6a5fc429f4c42f0c84837558885ef4da2f2 (0 status lines; main-tree lib/research diff vs the pin EMPTY); ce4_securities.txt sha256 7881772da6e204818fd50a02050cc7456b7de5a6d0912b6d663817f12930c67b = the signed value, 31 names; CONTROL BEFORE CPA_US_Equity fund IDVZ and position 1-2% IDVZ (as_of 2026-10-12, continuation dc143a9f2ecaad5e, dossier 2bd09162c4f47b3b); UNH both fields absent (as_of 2026-10-11); KMB dossier fields excluded, 7 strings with a Mexico id all inside the exclusion lists | CLOSED 20261017T172159Z |
| B1 | verify | canary in-memory builds (continuation.build, dossier build) for UNH and KMB, Mexico-id scans 0 and 0, UNH PFOE line_only true | ce4_before.out | PASS. In-memory builds (ce4_run.py build, writes nothing): UNH continuation/4 fund PFOE, position 'Maintain positions in PFOE and DIVZ', line_only True, Mexico-id scan 0 and 0; KMB fund None position None (COO half branch X), scan 0 and 0 (ce4_before.out, ce4_build_UNH.out, ce4_build_KMB.out) | CLOSED 20261017T172159Z |
| C1 | activation | canary writes UNH then KMB (continuation then dossier) and both read SERVED | ce4_written.out + ce4_canary.out | PASS. Canary written serially (ce4_written.out): UNH continuation 4d837586380648bd.json (29433 B) 17:22:02Z and dossier as_of=2026-10-17.f73f295a3671b8da.json (127204 B) 17:26:17Z; KMB continuation 45655bdb28726aaa.json (33122 B) 17:26:43Z and dossier as_of=2026-10-17.f0f5962f23f22bbd.json (186592 B) 17:29:37Z; every put put_performed True existed False, VersionIds in the manifest. Read SERVED at 17:3xZ (ce4_canary.out): UNH fund PFOE, position text 'Maintain positions in PFOE and DIVZ' line_only true, as_of 2026-10-17; KMB both fields absent with their reasons (branch X), misfiled_fields_excluded [], no served string with either Mexico id | CLOSED 20261017T173005Z |
| R1 | activation | the other 29 serially in file order, each built value equal to the ce2_census line, every put in ce4_written.out | ce4_written.out | PASS. The other 29 written serially in file order (ce4_written.out): each build checked against its ce2_census line before the write (BRANCH A, 0 Mexico ids), continuation then dossier. The first driver process died silently after NOW's continuation (18:37:11Z, cause not established, ce4_before.out); NOW completed in the foreground 18:50:15Z and the rest run to ZTS 19:27:01Z, all by 19:30Z. Manifest: 31 WROTE continuation, 31 WROTE dossier, 62 distinct keys, 0 NOT-WRITTEN, 1 EXISTED-NOT-REWRITTEN (NOW continuation); no GoldImmutableError, no put error. Read-only rebuild of the first 18 at 19:29Z: Branch A 18 of 18 (ce4_recheck.out) | CLOSED 20261017T193056Z |
| V1 | verify | served reads: UNH, KMB, first/middle/last of the other 29, control CPA equal to the step-0 reading; ce4_served.out ends SERVED_CANARY, SERVED_SAMPLE_AND_CONTROL, WRITTEN continuation=31 dossier=31 | ce4_served.out | PASS. ce4_served.out (served reads 19:3xZ): control CPA_US_Equity equal to the step-0 reading (content_sha256 61b9977a.., fund IDVZ, 2% position); UNH PFOE line_only true; KMB absent with reasons, misfiled_fields_excluded [], 0 Mexico ids in served fields; 8035_JP IDVZ 'CANDIDATE FOR IDVZ', MNST PFOE 'CANDIDATE FOR PFOE', ZTS PFOE 'INCREASE POSITION IN PFOE', each equal to its census line; ends SERVED_CANARY=PASS, SERVED_SAMPLE_AND_CONTROL=PASS, WRITTEN continuation=31 dossier=31 | CLOSED 20261017T193056Z |
| Z1 | git | proof instance VALID, ledger close and the manifest committed, report to the issuer | checker last line + commit hash | PASS. Deliverables, the write manifest ce4_written.out (62 keys) and the proof instance committed at b03ad544b1 (LOCAL; origin box/dell1 read 248b7d3d12); proof-of-spec-check on the committed bytes: VALID (rc=0). Report to the issuer follows this close; the ledger close is COMMITTED next. Window 17:20Z to 19:30Z: first put 17:22:02Z, last put 19:27:01Z | CLOSED 20261017T193624Z |

## Log

- 20261017T171723Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
- 20261017T172159Z LEG S0 closed: PASS. ce4_before.out: worktree C:/tmp/ce4-build detached at 344ea6a5fc429f4c42f0c84837558885ef4da2f2 (0 status lines; ma
- 20261017T172159Z LEG B1 closed: PASS. In-memory builds (ce4_run.py build, writes nothing): UNH continuation/4 fund PFOE, position 'Maintain positions in
- 20261017T173005Z LEG C1 closed: PASS. Canary written serially (ce4_written.out): UNH continuation 4d837586380648bd.json (29433 B) 17:22:02Z and dossier 
- 20261017T193056Z LEG R1 closed: PASS. The other 29 written serially in file order (ce4_written.out): each build checked against its ce2_census line befo
- 20261017T193056Z LEG V1 closed: PASS. ce4_served.out (served reads 19:3xZ): control CPA_US_Equity equal to the step-0 reading (content_sha256 61b9977a..
- 20261017T193624Z LEG Z1 closed: PASS. Deliverables, the write manifest ce4_written.out (62 keys) and the proof instance committed at b03ad544b1 (LOCAL; 
- 20261017T193624Z CLOSED -- all 6 legs proven
