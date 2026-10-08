# MDPF_SECCLASS decomposition -- ROUND 13, cell 1 (2.0.0_SA_COO~M1, dell1, 2026-10-08 ~18:3xZ)

**Status: DECOMPOSED (cell 1 only).** The issuer is this seat. Order: 1.0.0_SA_CTO~DELL1 msg 1039 (DECISION, SELF-DRIVE tick 17):
"cut this as round-13 cell 1 now, ahead of the rest of the round-12 enrichment list". The rest of round 13 is cut later in its own
issuance; this file then gains those cells. Deadline: land before 2026-10-09 12:30Z, since SECHIST FWD-1 is graded on the ~13:01Z
publish.

**Cut on:**
- 1.0.0_SA_CTO~DELL1's SECHIST round-1 analysis @0141533760, section 2.2: the name hop goes to MDPF_SECCLASS.
- Cell scope from msg 1039: the strip in clean_name(), plus a rewrite of the affected etf-classifications name rows under a
  never-widen pair. The CTO signs the CTO half on receipt.

**State the cell starts from (measured this session):**
1. `infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()` keeps the suffix: "Cisco Systems Inc/Delaware" stays as is, and
   "CISCO SYSTEMS INC /DE/" becomes "Cisco Systems Inc /DE/".
2. `data/etfs/scripts/gold/etf_positioning_publisher.py:241-255` `_display_name` serves the table row's `name` first.
3. etf-classifications consistent scan, 2026-10-08 ~18:2xZ: 10,487 rows. 1,367 names contain "/", and most of those are dates. A
   trailing "/<state or postal code or NEW>" matches exactly 1 row: `CSCO` "Cisco Systems Inc/Delaware". So the rewrite set is 1 row.
4. Check `R13_CHECKS/sc_r13_state_suffix.py` at the base reads ok=False, 8 of 12: all 8 controls pass and the 4 strip cases fail. The
   _shared suite reads 328 passed.
5. `R11_CHECKS/clean_name_write_v2.py` is the estate's conditional name writer. It has a dry run, `--write` behind both halves, and
   `--rollback`, but its set path is hard-coded.

## Rule 24 record

- **Domain:** the clauses of msg 1039's scope. That is 2 clauses: the strip, and the row rewrite under a pair. Each is placed once.
  - The cell `SC-e-74` builds the strip, a 1-row set, the writer's `--set`, and the half request.
  - The issuer's act is the write itself, after both halves read SIGNED.
- **(ii) Same grain:** one name rule and its one row set. **(iii) Intent coherence:** one intent, no served "/<state>" suffix.
- **(iv) State coherence:**
  - The strip changes shipped `_shared` code. Served names change only through the table row (the publisher reads the row) and the
    issuer's write.
  - The cell's code does not move the seed overrides (`ETF_NAME_OVERRIDES`; CSCO has none) or any class.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-74` | clean_name() drops a "/<state>" or "/NEW" incorporation suffix directly after a corporate-form token, pinned by test. Also: the 1-row set for CSCO, `--set` on the v2 writer, and the half request for the write | FWD-14, FWD-3; SECHIST FWD-1 (name hop) | WORLD (shipped `_shared` + one table row, written by the issuer) | -- |

## Write sets

- **SC-e-74:**
  - `infra/aws/lambda/v2_portal/_shared/security_name.py`
  - `infra/aws/lambda/v2_portal/_shared/tests/test_security_name_state_suffix.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py` (adds `--set`; the default stays
    the V2 set)
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_STATE_SUFFIX_NAME_20261008.md`
  - rows appended to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Dependency edges

None. **Chains:** 1 single-cell chain, so M = 1. Fan-out 1 of 1, cap 8.
Issuer-act order: the cell lands, then the half request goes to the CTO, then the `--write` once both halves read SIGNED, before
2026-10-09 12:30Z. The `_shared` deploy to a firm code prefix follows under the deploy lane. It is not needed for the 13:01Z publish,
which reads the row.
