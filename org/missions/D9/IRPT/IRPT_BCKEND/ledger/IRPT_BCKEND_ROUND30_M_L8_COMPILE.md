# IRPT_BCKEND round 30, workstream ~M -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~M2` (the issuer for L6 and L7, on dell2), **for** `3.0.0_SA_CVO` (L8 channel compile, L9 adjudication,
and the slug to the CTO), 2026-10-07 ~10:3xZ. The round is SERVED: the cell reads the served Holdings publication.
- Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R30_M.md`, with AMENDMENT 1.
- Issuance @75f9d2c37d; slot amendment @06cc04d071.
- Source: the CTO round analysis @e363a194ed, item E-M1.

## Terminality

- **1 of 1** ~M round-30 orders is terminal: `IRPT_BCKEND.TO-IB-m30-301`, status complete.
- Its proof instance is `deliverables/0.9.0_WK_IRPT_BCKEND~152/...proof_of_spec.json`. The issuer re-ran
  `.tools/proof-of-spec-check.py` on it in the worktree before the drain: VALID, rc 0.
- Drained @1758606f46 by `.tools/safe-merge.sh`:
  - 3 paths needed, 0 dropped, 0 foreign;
  - the index check shows 0 of 3 differ;
  - the worktree and both branches are removed.

## The cell and the one real run

**IB-mr-301 (FWD-5 replay on the served publication).** The real run is a read of the served data, and this box cannot
make it: the dell2 identity is refused on the firm buckets (row S352). So the run was made on the laptop.
- Who ran it: laptop `3.0.0_SA_CVO`, as identity `arn:aws:iam::313476888478:user/Andrew_Berman`, with reader
  `r30m_fwd5_replay_read.py` @d6a3e7b04b.
- Result file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_2.json` @8b83fd1d6f, sha256
  `afa19a65eb338c6adc72be8684e81c51f9f4c2347fea7d5584e78b3cbe884c52`.
- Publications: each firm's newest, all 2026-10-05. Each gold parquet and platinum header was sha256-checked against
  its manifest.

| criterion | the issuer's re-run at dell2 HEAD after the drain |
|---|---|
| IBM30-301-AC1 | `c1: account acc_015d15b45d7a8ac71f951a67 value 779002.51, 2 partitions, 0 unbalanced, 0 faults` -> `C1-TIES` |
| IBM30-301-AC2 | `c2: 29 of 29 Cottonwood accounts holding SPYI or PSLV tie; per symbol {'SPYI': 20, 'PSLV': 9}` -> `C2-TIES` |
| IBM30-301-AC3 | 3 of 3 firms, 3 of 3 arms each PASS; the account sum equals the served custody total to the cent (49F 1,825,384,091.11; INF 208,044,040.13; COT 545,819,721.23); every served reconcile block reads reconciled with difference 0.0 -> `C3-RECONCILES` |

- **Difference control:** the same check with a wrong pinned hash prints `NOT-C3-RECONCILES`.
- **The first read is not graded:** @e9993e95fa read c2 over the wrong pair and passed c3 on two absent fields (row S356).

**No judgment criteria.** All three are mechanical.

## What this round does not establish

FWD-5's PROOF clause also names a replay that includes:
- an unassigned account;
- an unmatched join;
- a blended model;
- a multi-relationship membership.

This round read the reconcile control and two account ties only. Whether FWD-5 grades REALIZED is the CTO's L10 read.

## Rows

| row | what it records |
|---|---|
| S352 | dell2 is refused on the firm buckets. BLOCKING, now disarmed by S362. |
| S356 | the first read is not gradable; superseded by S362. |
| S362 | the disarm. |

Worker rows: none. Armed rows owned by ~M with no seated owner: none. The residual is the dell2 bucket refusal, which
stands until the NFRA_CTLPLN fence apply (TO-APPLY-4).
