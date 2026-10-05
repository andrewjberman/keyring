# NFRA_SPRINTWIN -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-04 ~22:1xZ

**Input:** CVO slug msg 29272, `surprise-channel/adjudications/ADJUDICATION_v1.md` @fafbb9b482 (precondition MET; ARMED 0). The
build is `4.0.0_SA_CRO~Z`'s, solo (Andrew-direct ~18:4xZ). Ledger `sprintwin-union-20261004` is CLOSED @709caf16b1. The served re-run
of 2026-10-04 ran at 21:55Z under Addendum A.

## 1. WHAT THE ROUND DELIVERED

The thread H0-H4, end to end:
- the `sprint` systems row and its homes;
- the device census script, run on both computers;
- `--since/--until` and `--extra-commits` in both census scripts;
- the function's watermark window and union;
- the QA page.

The CVO's own count over the QA window is 336 pushed + 2 site-Z-only + 48 laptop-only = **386**, which equals the page's figure. The
page also states 50 unpushed. `window_end` is the earlier census time (the v0.2 amendment), and the page names both computers.

**Round 1 is CLOSED.**

## 2. GRADES

**FWD-1: REALIZED.** Board (denominator 7): REALIZED 1 (FWD-1); open 6 (FWD-2 to FWD-7).

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **The site-Z census key was overwritten within the day** (CVO observation). `sitez.json` now reads 21:51Z, not the 21:05Z copy the QA trace read. | **CONTRACTS v0.3: one object per census RUN, never overwritten.** The key is `address('sprint','global','bronze','device_census','date=<D>','<device>-<generated_at compact>.json')`, builder output verified (`.../date=2026-10-04/sitez-20261004T215100Z.json`). The run already unions every census file in the window by sha (v0.2), so more files per day change no count. This lands BEFORE FWD-2's dated re-run is graded. | FWD-2's dated re-run reuses its stored watermark, so its inputs must also be the stored inputs. A key whose body changes under it makes the re-run unreproducible, and the old copy is unrecoverable. A write-once object's body must be a function of its key. |
| 2 | **Row Z-S2** (binds FWD-7): under Git Bash, `git show origin/CLOUD:<script> > tmp` path-converts to a bad revision, writes an EMPTY file, and `python tmp` exits 0, sending nothing. | **Part of the FWD-7 cell.** The task's extraction must not pass through MSYS path conversion (native git from PowerShell, or `MSYS_NO_PATHCONV=1`). The task refuses with a non-zero exit when the copy is empty or does not compile. **Plant:** an empty pinned copy exits non-zero and writes no census. This is FWD-7's negative arm. | A scheduled job whose failure reads as success is the one failure FWD-7 exists to prevent. A failed retrieval returns a clean empty value, so the gate goes on the retrieval. |
| 3 | **Row Z-S4:** a flow diagram's `break_after` was a stage NAME, so the marker drew at NaN; the derived viz contract and the render gate passed it. | **Round 2, a small LOCAL repair:** the contract requires `break_after` to be an integer index within the stage list. Plant: a name fails the contract. Last on the list. | The contract checked presence, not type. It is cosmetic (one badge), but the gate passed a value it cannot draw. |
| 4 | **The page reads `opal_ai UNAVAILABLE`** for the other repos' subjects (CVO observation, outside the FWD-1 counts). | **A round-2 READ:** why the function's clone of `opal_ai` is unavailable (access, ref or path). Repair only if the read finds a defect in this project's function. | The page should say why an input did not arrive, and this one says only UNAVAILABLE. It sits outside the ENDPOINT's counts, so it is a read, not a build. |
| 5 | **The order of the enrichment list.** | **The PRD's backlog order, with ruling 1 placed before FWD-2.** FWD-3 includes the first 4:10 PM fire (2026-10-05 20:10Z) under the signed pair. FWD-7 needs each computer's MSTR to register its task. | The backlog order is already dependency-shaped. Ruling 1 gates FWD-2's grade. |

## 4. ENRICHMENT LIST (round 2; builder `4.0.0_SA_CRO~Z`, solo)

1. **FWD-4:** the positive control on one real pushed day. Work kind, project and bin agree per commit, and a commit present in both
   places counts once.
2. **Ruling 1:** census keys per run (CONTRACTS v0.3), with the scripts and the function's listing updated.
3. **FWD-2:** consecutive on-demand runs with one deliberately skipped, summed against git's total for the span. Grade it on the
   per-run keys.
4. **FWD-5:** one run with one device's file held back.
5. **FWD-6:** a note written on a device and not pushed.
6. **FWD-3:** the Scheduler swap, the zoneinfo day, and a dated run after 1 November. Then the 2026-10-05 4:10 PM fire under the
   signed pair.
7. **FWD-7:** each device's Scheduled Task at 15:55 ET with one retry at 16:02, registered by that device's MSTR. The Z-S2 gate and
   its plant form the negative arm.
8. **Z-S4:** the `break_after` contract type check.
9. **The `opal_ai UNAVAILABLE` read.**

## 5. ACTS FOR ANDREW (cited)

None. The laptop's Scheduled Task is the laptop MSTR's act on request (PRD seats line), not his.
