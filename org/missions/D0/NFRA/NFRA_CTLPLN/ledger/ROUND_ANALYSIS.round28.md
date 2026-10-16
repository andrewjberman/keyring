# NFRA_CTLPLN -- ROUND-28 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~12:0xZ)

**On:**
- the issuer's `L8_PACKET_ROUND28.md` and `ROUND28_INPUTS_FOR_ROUND_ANALYSIS.md` @cf7b334a00;
- the CVO's `ADJUDICATION_v32.md` @0c0f95ca4d (msg 109676).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage (CVO v32)

REALIZED 11 (1, 3, 5, 15, 16, 17, 18, 19, 23, 24, 28); ADVANCED 13; PARKED 1 (9); MOVED 3 (13, 20, 26). The newly realized one is
FWD-23: a reader named dell2's seats' work from dell2's list alone.

Check 6 is now platform-aware: the four yfinance wheels pass with no waiver (REAL4 4 of 4), so the waiver stays exceptional.

## 2. Rulings

1. **FWD-8: crossbox call files get ONE writer per box. One cell.**
   - Every box-sync conflict since 00:00Z is on an `org/devices/crossbox/XB-*.json` file that two or three boxes write.
   - The call keeps its id, but each side writes only its own file:
     - the from-side writes `XB-<id>.json` (the ask and the from-side close);
     - each answering box writes `XB-<id>.<box>.json` (ack, answer, close).
   - The tool reads them as one call.
   - Tests:
     - a from-side close and a to-side answer committed on two boxes merge with zero conflicts;
     - the existing calls read the same through the new reader.
   - **After it lands:** one window in which two boxes each complete a full round, read for conflicts by the E8 instrument.
     That window is the FWD-8 grade.
2. **FWD-7 (round-27 ruling 4 applied to the 6 lines on two CI files):**
   - **`infra/aws/lambda/ci/lambda-source-map.json` is NOT a shared carrier.** It is a JSON map that several boxes edit in
     place. That is the same multi-writer shape ruling 1 removes, and it would produce FWD-8's conflicts. One cell splits it
     into one file per function under a folder. Any consumer that needs the whole map reads the folder; no aggregate file is
     stored.
   - **`infra/aws/lambda/ci/record-terraform-deploy.sh` is code: ONE owner, `0.7.0_AE_CloudOps` base, and projects do not edit
     it.** If a project's edit carried data (a function list, a name), that data moves into the per-function files above. The
     cell lists each past project edit and where its data now lives.
   - **The directory-prefix class (15 lines, row W137-S3) is accepted as NOT-SAME-FILE.** Two boxes writing different files
     under one folder do not conflict, and FWD-7's ACCEPT names files. The CVO dispositions W137-S3 on this ruling.
3. **The placement tool's silent zero (row W137-S1): one cell.** `placement-check.py` exits non-zero and prints `ERROR:` when
   `org/missions` is absent, or when it reads fewer live projects than the register lists. A zero without its denominator is
   never an rc-0 answer again.
4. **FWD-25: the forbidden-act half, per kind (6 of 8 kinds started).** One cell runs each started kind's forbidden-act probe
   and records it as flagged or refused. The two kinds not yet started are started by `0.0.0_AB_MSTR` (`/mstr-spawn`) and asked.
5. **FWD-11: round-27 ruling 1 stands and is restated for the CVO.** v32 carries C-S90 as "choice pending", but the choice was
   made: read the laptop's overnight reboot on 2026-10-16, which happened with round 24 in flight (`L8_PACKET_ROUND24.md`
   @52567a1a41 header), against FWD-11. Only if that grades short does a deliberate reboot follow, on Andrew's confirmation
   that his 10-14 hold is spent.
6. **No act, CVO reads (unchanged):** FWD-4, FWD-12, FWD-22.

## 3. ENRICHMENT LIST for round 29 (one issuance)

1. Crossbox call files: one writer per box (ruling 1).
2. Split `lambda-source-map.json` per function, and set the one owner of `record-terraform-deploy.sh` (ruling 2).
3. Make `placement-check.py` fail loud (ruling 3).
4. FWD-25: per-kind forbidden-act probes, plus the two missing kinds (ruling 4).
5. After item 1 merges, the FWD-8 window read.
6. CVO: FWD-11 (ruling 5), FWD-4, FWD-12, FWD-22.
