# MDPF_SECCLASS decomposition -- ROUND 25 (2.0.0_SA_COO~M1, dell1, 2026-10-14 ~12:5xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers two cells; the rest of the CTO's list is the issuer's own acts, stated here.

**Cut on:** the CTO round-24 analysis, section 4, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_24_20261014.md` @94da0b08da, `1.0.0_SA_CTO~DELL1` msg 5506), on the CVO's slug
msg 5505 (`ADJUDICATION_v23` @22af7de1a4, `REMEDIATION_v14`). The analysis: FWD-1's Black Diamond page half is REALIZED on the class-path reading; its Positioning limb is
NOT_EVALUATED; D1-S27 is accepted as rounding with a $1,000-per-firm-date bound, checked by this seat on the re-base read. The list:
1. **The e97 re-base as a class** (D1-S36, XA-20261014T014758Z-01a0): the bars and advisors clauses re-based to post-restatement baselines, read on the first scheduled fire
   after the recut; the D1-S27 bound read on the same objects.
2. **FWD-1's Positioning limb, ONE read:** render both Positioning surfaces for GLD, PHYS and VXX; compare class and sub-class with the Black Diamond page values of D1-C-S21.
3. **C_06 writes JSON with sorted keys** (D1-S37; XA-20261014T113939Z-a304's follow-up), under its own never-widen pair.
4. **Conditions carried, not cells:** D1-S39 (a pair that ships `code/gold/lib/` names DB-b-181's classifier radius or the deploy pins the served classifier; owner this seat);
   e57e61's L3 waits on a scheduled new-security run that plans US stocks, and the issuer names that run's date in the packet.
5. **The 4-ticker residue** (HPI, CUBE, GLPI, PCEF): this seat files one request with the list's owner. Not a SECCLASS cell.

## What is a cell and what is the issuer's own act

- **Item 1 is cell `SC-e-101`, then the issuer's timed read.** The read is on the first scheduled fire after the recut (23:00Z tonight). A worker cannot wait for a fire,
  so the cell builds and proves the INSTRUMENT, and captures the post-restatement BASELINE from the served objects as they stand now. Reasoning for the baseline: leg Q
  (ledger `secclass-e97-legq-qa-c06-single-sc1-20261014`, CLOSED) showed two C_06 re-derives of the current inputs rewrite 0 relationships and leave the served content
  equal, so the served objects after the 04:00Z fire ARE a fresh re-derive of the current inputs. The Oct-12 radius files (`R23_RADIUS/`) predate two upstream AUA
  restatements and are stale; they are not edited. The re-base compares the post-fire objects with the new baseline: where the AUA did not move, the value must not move
  (within the $250 rounding the code carries); where it moved, the move must be conserved.
- **Item 3 is cell `SC-e-102`** (a build; nothing is shipped). The ship is a later seat-folder order to `0.7.0_AE_CloudOps~SC1` under a pair this seat writes after the
  build. Scope ruled here (the issuer rules inside its own decomposition): the ONE measured nondeterministic writer, `_write_mix_summary` (the advisors key order moved
  the ETag on every C_06 run, row D1-S37). The relationship writers are not changed: across two leg Q runs 15,543 of 15,544 keys held their ETag, and sorting their payloads would
  rewrite all 15,531 relationship keys once with no content change.
- **Item 2 is the issuer's own read** (the Positioning surfaces are rendered pages; a worker has no browser). Made after the cells drain, on the dev build with the walker
  account, with the screenshots committed under `deliverables/2.0.0_SA_COO/`.
- **Item 4:** the e57e61 date and the D1-S39 condition are statements in the next packet; D1-S39 binds the ship pair of SC-e-102 (C_06 is a script, not `lib/`, so the pair
  states that it ships one file and that the classifier is not in it).
- **Item 5:** the issuer's request to the list's owner; not cut.

## Rule 24 record

- **Domain:** the CTO's five items; two cells.
- **(ii) Same grain:** SC-e-101 is one script over the served mix objects (capture, read, selftest); SC-e-102 is one function's `json.dumps` call and one test.
- **(iii) Intent coherence:** each re-based clause is one check with one expected value drawn from the captured baseline file, never typed into the script.
- **(iv) State coherence:** SC-e-101 writes only repo files and reads S3; SC-e-102 deploys nothing. Neither moves a served object.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-101` | `R25_CHECKS/r25_rebase_read.py` with `capture` (baseline from the served mix objects and the AUA, committed), `read` (re-based bars, advisors, totals and the D1-S27 bound against a baseline), `selftest` (positive and negative fixtures) | FWD-1 (the e97 acceptance clauses) | LOCAL | none |
| `SC-e-102` | `_write_mix_summary` in C_06 writes the payload with `sort_keys=True`; a test that equal content in any insertion order gives identical bytes, with the unsorted control showing the orders differ; the sibling C_06 suites stay green | FWD-1 | SERVED | none |

## Write sets (disjoint)

- **SC-e-101:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/` (new folder) and the surprise channel (append).
- **SC-e-102:** `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`, `data/black_diamond/scripts/gold/tests/test_c06_sorted_keys_r25.py` (new) and the surprise channel (append).

## Chains

Two cells, no edge: two chains. Fan-out 2 of 2, cap 8. Slots ~91 (SC-e-101) and ~92 (SC-e-102), `worker`, haiku (treatment box, MP-20261010). SC-e-101 is cut with
`<direct_act>true</direct_act>` (one LOCAL cell, no product file); SC-e-102 is SERVED and takes the full limbs.

## Carried (not cut)

The client-facing Black Diamond Mix PROD push (Andrew's); the DEMQUE<->SECCLASS sync cell (arrives with the CTO's CONTRACTS rows, a later recut); `TO-DEPLOY-e57e61`
(held; date named in the next packet); the SC-e-102 ship order (after its build and the pair).
