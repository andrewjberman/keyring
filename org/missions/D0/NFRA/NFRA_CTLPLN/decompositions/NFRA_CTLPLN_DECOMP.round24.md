# NFRA_CTLPLN decomposition -- round 24: the install leaves a log, FWD-16 re-driven with an absent package, FWD-14 after Andrew's sitting (issuer 2.0.0_SA_COO~C; cut 2026-10-16)

**Status: ISSUED in one issuance. FROZEN at the cut.** (A cell cut later in the round, once its dependency clears, is an AMENDMENT of this document stating its gate limb, as `CT-al-4` was in round 22.)

**Input.** `ledger/ROUND_ANALYSIS.round23.md` (1.0.0_SA_CTO) @32c2378d19 sections 1-4 and msg 109546; the CVO's slug `surprise-channel/adjudications/ADJUDICATION_v28.md` @af765ff845; the issuer's `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND23.md` @b13633f07d. **PRD:** v0.31 with round-21 ADDENDUM 1. **Coverage entering the round (CTO table):** REALIZED 1, 3, 5, 24, 28; ADVANCED 2, 4, 6, 7, 8, 10, 11, 12, 14-19, 21, 22, 23, 25, 27; PARKED 9; MOVED 13, 20, 26. **Process facts in force:** sparse worktrees cut by `wk-provision.sh`; removal at merge by `worktree_gc.py --go --only`; the issuer merges first and validates the proof in the main tree; the registry lanes admit only a worker serial to scripts and test batteries; a seat's row carries no worker coordinate; `crossbox-call.py line` needs the commit on origin, so each call costs one push by `0.0.0_AB_MSTR`.

**What round 23 left unproven (the CTO's reading, checked by the issuer).** `duckdb==1.5.0` has been in `requirements.txt` since 2026-10-07; `intake_request.py status --name duckdb --version 1.5.0` reads `APPROVED by=requirements.txt ... reason=listed in requirements.txt` today (issuer read, 2026-10-16 ~00:2xZ), so FWD-16's arm "not approved, then approved" was never exercised; and dell1's install receipt reached the laptop only as MSTR's relayed summary.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-an-1` | `intake_receive.py` keeps the pip run's own log: `prove` and `install` write the child pip's full captured output, its command line and its pinned environment to `receipts/<wheel>.pip.<device>.log` beside the receipt, and the receipt names the log and its SHA-256, so a dell-side receipt shows the `--no-index` run and not only its last line. | FWD-15 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~126` |

## Driven by the issuer in this round (not cells yet; each cell below is cut as an amendment the tick its dependency clears)

The FWD-16 re-drive is ONE chain; its steps wait on a lane's answer and on the CTO's decisions, so no order for them can be cut honestly today.

1. **A lane names the read (crossbox, today).** `1.0.0_SA_CTO~DELL1` is asked to have one named lane on dell1 name ONE one-off read-only job that genuinely needs a package ABSENT from `requirements.txt`, and the package and version (a wheel that exists for `cp314-cp314-win_amd64`). The issuer does not choose the read. **Test of absence, before the request is filed:** `intake_request.py status --name <p> --version <v>` must read `UNKNOWN`.
2. **Status read 1 of 3 ("not approved"):** the issuer files the request and reads the verb. The polars request `REQ-20261015T163055Z-polars` (REFUSED) is read the same way (status read 3 of 3, "refused"). Read keys name and version: the polars request carries version `1.12.0`.
3. **CTO decides** (`intake_request.py decide`); **status read 2 of 3 ("approved")** by the issuer.
4. **Cell `CT-an-2` (cut then):** fetch and checks 1-7 for that package through the checked route (the shape of `CT-al-1`). **CTO signs check 8.** **Cell `CT-an-3` (cut then):** release, pack, Taildrop (the shape of `CT-al-4`). Both use `CT-an-1`'s log from the start.
5. **dell1** receives, runs `verify`, `prove`, `install --target` (the tool installs with `--no-index --no-deps`), then the lane's one read; **dell1 commits on `box/dell1`** the pack's `receipts/` folder (which carries `received_sha256`, the command and, after `CT-an-1`, the pip log) and its terminal output of `verify`, `prove` and `install`. The issuer reads the committed files from `origin/box/dell1`, not a relay.
6. **`requirements.txt` is not touched by any act of this chain.** The issuer reads the file before and after (a `git diff` of the file across the chain reads empty).
7. **duckdb's receipt (FWD-15 for the delivered file):** dell1 commits the duckdb pack's `receipts/` folder and whatever `verify` / `prove` / `install` output it still holds; where it holds none, the duckdb receipt stays as relayed and step 5 proves the arm (CTO ruling 2).

## FWD-14 (no cell)

Both target-side reads are done and neither proves a negative. What is left is a person's act: `c9a4` and `b87f` (Andrew's sitting, with the elevated Security-log read put to him as part of `b87f`). The issuer reads each target's event 1149 and the connection-manager log after the sitting; no cell is cut before then. **FWD-17** (`318f`) is the CTO's ping to Andrew; the record exists. **FWD-9** PARKED; **FWD-2** a qualified wait; **FWD-27's person arms** Andrew's. `W8-S7` waits behind the outcome cells (infra path, WORLD by the path floor, owes the CRO's research when cut).

## Carried with an OWNER and the CONDITION that un-parks each

`W8-S7` (owner the issuer; cut when the CTO wants it ahead of the outcome cells); `S9103`, `S9120`, `W89-S3`, `W12-S1`, `Z-S3` (before 2027-12-01), `S9125` (dell1, before 2026-12-31), `S9119`, `S9128`, `W121-S3`/`S4` (the CTO reads whether the guard closes them at the next main-tree build), as in the round-23 packet section 5.

## Rule 24

**Domain:** the CTO's round-23 section 4 enrichment list (2 items) against the open FWD chain; denominator in the CTO's section 1 table (28 FWDs). **Same grain; one intent; disjoint write surface:** `CT-an-1` writes `intake_receive.py`, `test_intake_receive.py` and its own test file; `CT-an-2`/`CT-an-3` (later) write the journey tests and the intake records of the new package, not `intake_receive.py`. **State coherence:** no cell deploys, pushes or calls AWS; the only network act of the chain is the checked fetch of `CT-an-2`, which is the thing under test and runs on the CTO's approval; no wheel is installed on the laptop.

## Dependency chains and fan-out

Three chains: (1) the log (`CT-an-1`, no dependency, cut now); (2) the FWD-16 re-drive (waits on the lane's named read, then on the CTO's decision and check 8); (3) FWD-14 (waits on Andrew's sitting). `fanout: 1 of 3 chains, cap 8, reason: the log is the only chain with no unmet dependency; the re-drive waits on a lane's answer and the CTO's decisions, FWD-14 on Andrew's sitting`
