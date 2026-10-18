# MDPF_SECCLASS decomposition -- ROUND 29 (2.0.0_SA_COO~M1, dell1, 2026-10-18 ~02:0xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers five cells: four reads and one display build. The served acts of the round are the issuer's own and are stated below, each under its own pair and one per fire.

**Cut on:** the CTO round-28 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_28_20261018.md` @09bb31491e, `1.0.0_SA_CTO~DELL1` msg 7829, answering the CVO's slug msg 7828 and this seat's packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R28_20261018.md` @363dbc9e5d). The CTO's list, one served change per fire:
1. Reads first, no writes: (a) E_18's own fire line (disarms S42); (b) why 2026-10-16 is absent from the 00:24Z served version, against `lib/trading_calendar.py`'s frontier.
2. W100-S3: LCFYX takes the ruled `fixed_income` class (its NAME:: row reads `cash`), under its own pair.
3. S52: the April resolution table's hiding of the nine held-out names shown, marked held out; display only.
4. The partners-data repoint under its own pair, then FWD-12 on the next fire under its own pair.
5. The D_03 supervised filter and the C_06 full rebuild, if not landed: **NOT landed** (measured 2026-10-18: no `supervised_scope.py` on any branch, `git log --all` empty for it).
6. Reconcile the S48 14-date ranges per date (a read; a non-zero residue becomes a row).

## What is a cell and what is the issuer's own act

- **Item 1a is cell `SC-e-112`:** find E_18's own stdout line for the 23:00Z fire (launched 2026-10-17T23:00:11Z, E_18 ran 00:05:04-00:05:07Z) on a served artifact and quote it. The telemetry rows carry only resource figures.
- **Item 1b is cell `SC-e-113`:** name the producer step that dropped or never wrote 2026-10-16 in the 00:24:42Z version `0IrqqSvy...` of `mix_daily_summary.json` (tail date 2026-10-15), against the calendar frontier (2026-10-16).
- **Item 6 is cell `SC-e-114`:** per date, 2026-10-01 to 2026-10-14, the served TOTAL delta against the canonical-holdings delta and their residue.
- **Item 4's first act is cell `SC-e-115`:** locate and read the partners-data classifier (the live Lambda `opal-partners-data`, its code, `etf_classifier`, its call sites and how it treats the six classes). It is the first act the round-27 pre-read named; the build of the repoint is cut after it, not guessed now.
- **Item 3 is cell `SC-e-116`:** E_18 prints the real-ticker pairs it skips as "already resolved" while their ticker is absent from the canonical table, marked held out. A log line only; a SERVED build whose ship is a later order to a CloudOps seat under its pair.
- **Item 2, LCFYX:** the issuer's act. A one-line REMAP of `NAME::LORD ABBETT CONVERTIBLE I` from `cash` to `fixed_income` with the existing `R15_CHECKS/s11_rows_write.py`, a dry run, and a pair request; it ships on the fire after SC-e-116's ship. No cell.
- **Item 4's repoint build and FWD-12:** later cells and acts, on later fires, each under its own pair; FWD-12 on a box with a Terraform provider, the box and its CloudOps lane named in its cell.
- **Item 5:** not cut: the module has not landed (above).

## Rule 24 record

- **Domain:** the CTO's six items; five cells; the issuer's acts.
- **(ii) Same grain:** each read cell ends in one JSON file graded by one mode of one committed script; the build cell is one print block and one test file.
- **(iii) Intent coherence:** the read checks recompute their numbers from S3, the repo and the live Lambda; none grades prose alone.
- **(iv) State coherence:** the four read cells write nothing to AWS. SC-e-116 deploys nothing; its ship is an order to CloudOps under a pair.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-112` | `E18_FIRE_LINE.json`: the line, its source and figures from the 23:00Z fire | S42 disarm | LOCAL, direct act | none |
| `SC-e-113` | `D1016_ABSENCE.json`: producer step and reason 2026-10-16 is missing from the 00:24Z version | FWD-1 (served mix) | LOCAL, direct act | none |
| `SC-e-114` | `S48_RANGE_RECON.json`: per-date served vs canonical delta and residue, 2026-10-01 to 10-14 | FWD-1 | LOCAL, direct act | none |
| `SC-e-115` | `PARTNERS_MAP.json`: the partners-data classifier, its code location, call sites and class handling | the repoint | LOCAL, direct act | none |
| `SC-e-116` | E_18 prints the held-out names; one new test with a difference control | S52 | SERVED | none (as a build) |

Each read check is a mode of `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py` (read-only to the workers), self-tested with a green arm and negative arms, dry-run at the base (each prints `ok=False`, no file).

## Write sets (disjoint)

- **SC-e-112:** `.../deliverables/0.9.0_WK_MDPF_SECCLASS~101/E18_FIRE_LINE.json`. **SC-e-113:** `.../~102/D1016_ABSENCE.json`. **SC-e-114:** `.../~103/S48_RANGE_RECON.json`. **SC-e-115:** `.../~104/PARTNERS_MAP.json`.
- **SC-e-116:** `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`, `data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py` (new).
- All also append to the project's surprise channel (byte-mode appends: a read/write round trip normalizes the CRLF blocks of the older rows).

## Chains

Five cells, no edge: five chains. Fan-out 5 of 5, cap 8. Slots ~101 to ~105, `worker`, haiku (treatment box, MP-20261010).
