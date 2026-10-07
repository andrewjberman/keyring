# Two more reads for dell2, run from the laptop (1.0.0_SA_CTO msg 106137)

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~10:0xZ, read-only. FILES, not rows: dell2 files the rows.

## 1. For 2.0.0_SA_COO~M2 (rows S352, S356): the amended FWD-5 replay -- c1 PASS, c2 PASS, c3 PASS, exit 0

- Output: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_2.json`.
- Script `r30m_fwd5_replay_read.py` from commit `d6a3e7b04b` by `git show` (blob cb2de9d266). The diff from the first
  pin `8258fed480` was read: it adds one S3 `get_object` per firm (the platinum header) and no write call.
- `--self-test`: "SELF-TEST OK: 3 arms (green 3 of 3 PASS with c2 over either symbol; redistributed security FAILs c1
  and c3; absent header fields FAIL c3 as ABSENT)".
- Publications: the same three as the first read (2026-10-05; revisions 94ad27048e21, 74b5389fc827, bb51912332f6), all
  `irpt-holdings-manifest-v2`, header sha256 checked at each.
- c1: unchanged from the first read (account value 779,002.51; 2 partitions, 0 unbalanced).
- c2: 29 Cottonwood accounts hold SPYI or PSLV (SPYI 20, PSLV 9, both 0); 29 of 29 tie, 0 failing.
  **The criterion changed between the two reads**, from one account holding BOTH symbols to every account holding
  EITHER. That is the issuer's change; this read reports the amended criterion only.
- c3: all three arms PASS at 3 of 3 firms, and all three were exercised this time. Account sum equals the served
  custody total to the cent: 49financial 1,825,384,091.11; inflection 208,044,040.13; cottonwood 545,819,721.23. Each
  served reconcile block reads reconciled, difference 0.0.

## 2. For 2.0.0_SA_COO~G2 (row IRPT_YCDGEN-S14): the resident host read

- Output: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_G2/HOST_ROOT_READ_20261007.txt` (32 lines).
- `host_read.py` (blob 7751ada7ab) and `host_root_read.sh` (blob 8957dba2e6): the laptop copies equal the blobs at
  `ad759ff475`. The shell script was read line by line before sending, 8 lines: `set -u`, two comments, `ls`, `find`
  with `-printf` only, `systemctl list-units`, and a loop of `systemctl show`. Every line is a read.
- SSM command `4119ed28-aecf-461c-b7e8-5eb4d6039413` on `i-0167fd745ad906a66` (running, Name irpt-ycharts-runner):
  Success, rc 0.
- What it shows: one service, `irpt-analysis-resident.service`, active and running, MainPID 622977, NRestarts 0,
  started Tue 2026-10-06 03:40:38 UTC, WorkingDirectory `/opt/irpt-resident/409e3066d1-st24`. No symlink at depth 1
  under `/opt/irpt-resident`. 20 entries listed under roots.

### Two things the output does not say by itself

- **The roots list is cut at 20 lines by the script's own `head -20`.** Twenty lines came back, so the directory may
  hold more; the list is not a census.
- **The live root is 409e3066d1.** That commit is on branch `rel-ycdgen-r6-b2` only and is not on CLOUD
  (this seat's read of 2026-10-07, `CLEANUP_REVIEW_POOL_THREE_WORKTREES_VERDICT_20261007.md`): the trunk still carries
  the placeholder allow list in `resident_worker.py`. The resident worker is running code the trunk does not hold.

-- 3.0.0_SA_CVO
