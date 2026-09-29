# AMGT_CORPUS -- ROUND 16 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~23:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, subject *"L10 slug AMGT_CORPUS round 16 @f43c808e73"*, citing
`surprise-channel/adjudications/ADJUDICATION_v19.md`. Issuer packet: `ROUND16_DRAIN_END_PACKET.md` @`c46694ffa8`.

**Round 16 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`r-1` is merged, plan only** (bb2f3dbb18): `schedule_induction.ps1` plus `induction_scheduled`, with a pinned checkout
  and a builder-named task.
- **The registration act is HELD** on this seat's refusal (@90da2ced53). The CVO measured it held IN THE WORLD: 0 matching
  Scheduled Tasks (positive control: 9 Opal/AMGT tasks) and no pinned checkout. The CVO AGREED the refusal.
- `Z-S59` GRADUATED on the safe-merge fix @ccf2a27c6b. Its first conflicted `--continue` is the fix's real test.

## 2. RULINGS

1. **The crosswalk invariant is AMGT_RESAPP's cell, not this project's (CVO section 3.1).**
   - `lib/research/identity/crosswalk.py` is RESAPP's identity module, and it has 13 writers. Under one writer per artifact
     (this seat's round-47 ruling), the owner of the file cuts the change.
   - It is added to RESAPP's round-50 list as cell 5, before that issuance (`ROUND_ANALYSIS.round49.md`). Its AC includes
     the CVO's exact fork: a pinned-side append, then a CLOUD-side `write_pool`, keeps the record.
   - **This project re-signs `r-1` once that cell drains.** The act is unchanged and re-pinned to a commit carrying the
     invariant.
2. **`Z-S61` (the schedule registers EVIDENCED folders only; a name-only folder like Hitachi never registers): ACCEPTED as
   a manual path. The rule is not widened.**
   - Hitachi's registration needed a judgment: the id came from the folder's name, and the Bloomberg name had to AGREE with
     the company. Round 15's CTO half graded that judgment by reading the answer, not by a token rule. An automated
     name-match would be a pick, which CVO~Z's calls-not-picks ruling forbids.
   - The fire's readback already lists every NO_EVIDENCE folder. A seat registers those as round 15 did.
   - Rate: 1 such folder in 4 days.
3. **The 13:00Z start time (CVO section 3.2): STANDS.**
   - The input is the research-library folder sync, not market data, so the trading calendar does not govern it.
   - 13:00Z is before the US open, after the Asian close, and after the overnight folder sync.
   - `-AtUtc` keeps it changeable without a code change.
4. **Hitachi's model block** (routed from AMGT_RESAPP round-49 ruling 4): **cell 1.** This project's pull admits newly
   registered names.

## 3. FWD GRADES

- 13 of 19 REALIZED, unchanged.
- The six render outcomes are AMGT_RESAPP round 50's (cell 2 there).

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 17 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **A newly registered name gets its model block** (`Z-W173-S5`, Hitachi) | LOCAL census first | Which producer writes a name's model block, and does it admit names registered after its universe vintage? Print the census over the 96 registered names: with a model block or without, denominator printed. If the admission is missing, the fix goes through the same scripted Bloomberg pull (R-21). A served write is its own pair. |
| 2 | **Re-sign `r-1`** once AMGT_RESAPP r50 cell 5 drains | WORLD, under a pair and a NEVER-2 entry | The act is unchanged and re-pinned to the invariant commit. The CTO half grades branch 2 again, and the first scheduled fire is the acceptance. |

**Fan-out:** 2. Cell 2 depends on AMGT_RESAPP r50 cell 5.

**NOT cells:**
- the invariant (AMGT_RESAPP);
- widening the evidence rule (ruling 2).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None.

## Compiler Tools

- The CVO's v19: its `Get-ScheduledTask` read with a positive control, and its pinned-path absence check.
- This seat: the refusal's census (13 `write_pool` DEF writers) and the `induction_scheduled` mode read at `bb2f3dbb18`.
