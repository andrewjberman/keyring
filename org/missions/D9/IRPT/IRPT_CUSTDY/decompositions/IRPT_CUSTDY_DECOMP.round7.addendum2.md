# IRPT_CUSTDY decomposition -- ROUND 7, ADDENDUM 2 (issuer 2.0.0_SA_COO~K2; 2026-10-09 ~01:1xZ, dell2)

**Status: ISSUED.** Workstream `~K2-E2`. Naming: the product is the "Performance client statement" (Andrew-direct ~21:2xZ,
@b15e76c232; PRD v0.4); code ids `CUSTODY_REPORT`, `irpt-custody-x10-v1` and `custody-report-read` are unchanged.

**What it does:** splits cell `CU-g-2` (E2, `IRPT_CUSTDY_DECOMP.round7.md`) into `CU-g-5` and `CU-g-6`. It is an issuer ruling
inside this decomposition. No ENDPOINT change; FWD-1 is unchanged.

## Why

- **The cell as written needs the PROD print page.** "One `CUSTODY_REPORT` export per household reaching READY" renders through the
  PROD portal (round-6 ADDENDUM 1 @c3addc6f25, break 5). The print page `63b9382a` is on neither portal branch. It is carried as an
  ACT for Andrew on the dell2 open-calls list (row `dell2-20261008T192510Z-0347`), sequenced after E2, and is part of his IRPT
  frontend mapping with the CRO (Andrew-direct ~21:1xZ).
- **The data half is unblocked separately.** IRPT_BCKEND ADDENDA 9-11 put the writer in place, and ADDENDUM 10 (msg 1513) says:
  "~K2: E2a retains its real report through E10's function."
  - The writer function and its route `POST /api/scoped/investor-reporting/custody-report` are live (IB-pr-378, ledger CLOSED
    4/4).
  - The IAM leg is applied (22:47:14Z).
  - ~P2's packet (18d4c45c1d) owes the real persist, the owner read and the other-firm refusal "after IRPT_CUSTDY E2a retains a
    real submission".

## The cells

| cell | what exists at the end | serves | gate | placement | risk | workstream |
|---|---|---|---|---|---|---|
| `CU-g-5` | ONE real Performance client statement submission for ONE real household is retained under `irpt-custody-x10-v1`, and its household document is persisted through the live writer route. The submission's ref, the persisted object's ref and its revision are in the deliverable. | FWD-1 | irpt-ycharts-generate release 5 (E11) LIVE: submissions request `irpt-custody-x10-v1` | dell2 | SERVED | `~K2-E2` |
| `CU-g-6` | that statement's export reaches READY through the PROD print page; one rendered statement is read against hop 3 (JUDGMENT, CVO) | FWD-1 | dell2 open-calls row 0347 (print page `63b9382a` on portal PROD; Andrew) | dell2 | SERVED | `~K2-E2`, cut at its gate |

**Not in CU-g-5:** the owner read by reference and the other-firm `OBJECT_NOT_COVERED` read. ~P2 owes them in IRPT_BCKEND after this
cell retains the submission (packet 18d4c45c1d). This cell hands them the refs.

**Ordering and fan-out:** CU-g-5's order is committed now and spawned the tick release 5 reads live. That is the only act left,
and it needs no word. CU-g-6 is cut at its gate.
