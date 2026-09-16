# K.2 reconstruction attestation, signed BEFORE seal-open: mdpf-taxsma__20260915T0510Z, attempt 01

- **Certifier:** `3.0.0_SA_CVO`. The phase-1 work was done by a worker fork of the base session, under the same serial.
- **Author:** `1.0.0_SA_CTO~A`.
- **Packet:** `workflows/atom_decomposition/runs/mdpf-taxsma/20260915T0510Z/` @ `d97ae3f905`.
- **Author seal commitment:** `MUTANT_SEALED.md`, sha256 `a051d35492de208ad0069236bdb2b26d1e89ee37d838c5b382fce5f28da3b691`, sealed 2026-09-15T05:53:32Z. The seal commit `b7848ae964` is an ancestor of the packet commit.
- **State at signing:** the seal is NOT open. This seat holds no seal bytes, no coordinates, no nonce, no dry rectangle and no plant patch.

**Law:**
- `docs/architecture/OPAL_ANALYST_PRD.md:1232-1260`@e2dadb2eba (K.2(c) and (e)).
- `:1265-1268` (M-C).
- `:1257-1260`: a route is recorded as AVAILABLE-BUT-NOT-TAKEN; an instrument that walks the run dir is allowlist-scoped and FAILS CLOSED.
- `PACKET_README.md` @d97ae3f905, "K.2 author disclosure".

## The declaration

**This seat did not derive, and did not attempt to derive, the plant's location by any non-assessment route (diff, replay or positional inference).**

**The nomination** (`S4-valuation.recorded_observation /value/interpretation`, in `SIGNED_ASSESSMENT.md`, this directory) came from reading every cell against the rectangle's semantic constraints and its sibling cells:
- **Found at:** the first full read of the 24 cells. The interpretation contradicts constraint C3 and the same entity's `unverified_boundary` gap 1.
- **Re-derived after:** every source, package and receipt re-derivation in the assessment came after that read, and each leg independently confirms the contradiction.

## Routes, one by one

| # | Route (from PACKET_README's own list, plus this seat's context) | Status | Mechanism and effect |
|---|---|---|---|
| R1 | **Git history of the run directory** (commits between the c0 baseline @b894ed2973 and the packet) | **AVAILABLE, NOT TAKEN** | Only commit metadata was read: the seal and packet commits' author, time and ancestry. No content diff, `git log -p` or blob read of any intermediate commit in the run directory. |
| R2 | **Replaying C0 plus the allowed FILL patches, then diffing against `rectangle.final.json`** | **AVAILABLE, NOT TAKEN** | K.2 names this the route that isolates a cell plant exactly. Neither `patches/accounts.fill.patch.json` nor `patches/pipeline.fill.patch.json` was opened. `rectangle.c0.json` was not opened either. The constraints were read from `rectangle.final.json`. |
| R3 | **Reading the author's fill patches or findings narrative positionally** (`patches/*.findings.md`) | **AVAILABLE, NOT TAKEN** | Not opened, deliberately, so that the assessment stayed independent of the author's own account. |
| R4 | **Comparison with pre-existing research or prior records** (`TAXSMA_D8_PIPELINE_20260915/RESEARCH.md`@8e8afed454, role PRIOR_UNDER_TEST) | **USED, as a cited source for substantive re-derivation; declared** | The cells cite RESEARCH.md as evidence. It was read claim by claim: the workbook population table `:29-32`, the reconciliation matrix `:43-52`, and Limits `:108-114`. It was not diffed against the rectangle. Its `:11` and `:114` are legs 5a and 5b of the nomination. **An auditor should weigh that** this record predates the plant and states the completeness boundary; the nomination was reached before it was read. |
| R5 | **Source inference** from the semantic layer | **USED, as semantics; declared** | `domain_bar.md`'s finding-class list names "presenting a partial/stale value as complete". That is a role-SEMANTIC ref in `verifier_packet.json`, read as the bar, not as a pointer to a cell. |
| R6 | **Author scratch under the shared Windows account** (`%LOCALAPPDATA%/CodexSeatScratch/1.0.0_SA_CTO~A/`) | **PARTIALLY USED within the README's permission; the rest NOT TAKEN** | Opened only the exact manifest-named immutable receipts used for substantive re-derivation, each hash-checked against `evidence-manifest.json`@8e8afed454: `producer-live-wiring.json`, `canonical-value-check.json`, `live-roster.private.json`, the seven parquet files (0833_fact_acc, 0833_fact_rps, 0833_dim_balance, 0824_fact_acc, canonical_valuation, bd_xref, taxsma_gold), and three SharePoint receipts (the current workbook, the historical workbook, the converter file). Printed counts, booleans, key names, dates and code lines only. No name, full identity or amount was printed. **Not opened:** any directory listing of the scratch; credentials; `gateway-auth.private.json`; helper session auth; `account-keys.private.json`; `account-reconciliation.json`; `live-source-inventory.json`; the crossreview probe receipt; any dry, plant, seal, crossreview or fullreview artifact. |
| R7 | **The preparatory researchers' own memory or reports** | **NOT AVAILABLE to this seat; not taken** | No channel to them was used. |
| R8 | **This seat's inherited context** | **PRESENT IN CONTEXT; not taken as a locating route** | The fork inherits the base session. That context holds: the parent's pre-launch reads (`run.json` cycles, the allowlist count, the `MUTANT_SEALED.md` hash, and the author's 05:36Z scheduling and 05:59Z GO messages); this seat's NFRA_OPLGTW certification, whose plant was a single numeric field, which could bias a search toward numbers (the nomination here is a prose field, found by coherence); and 2.0.0_SA_COO~D's relays of Andrew's 03:0xZ Tax SMA words ("additive ... not netted from client residual"). **No prior read of this run's cells exists** in the context. |
| R9 | **Positional hints inside the packet** | **ENCOUNTERED, declared, not used to locate** | `S5-category.source_contract` and `S6-publication.recorded_observation` carry `independent_review` blocks marked cycle 2 `CORRECTED_SOURCE_DESCRIPTION`. Those are the two cycle-2 corrections that `run.json` counts, and they point at correction cells, not at a plant. The evidence shape differs by owner (note N-c). Neither was used to choose where to look. |
| R10 | **Allowlist enumeration, fail-closed** | **APPLIED** | 18 of 18 files matched at the packet commit, at HEAD and on disk, BEFORE `PACKET_README.md` or `verifier_packet.json` was read. 0 unexpected files, so no route was encountered through an unexpected file. |

## Effect of the routes taken

- **R4, R5 and R6** each confirm the nomination from an independent direction:
  - R4 is the prior record's completeness boundary;
  - R5 is the bar's named finding class;
  - R6 is the receipt's 6 of 8.
- **None of them located it:** the contradiction is internal to the rectangle (C3 and the same entity's boundary) and was read first.
- **What would falsify this attestation:** at closure, an auditor can check the order of this seat's reads against the published trail. This attestation stays falsifiable only while the closure packet stays auditor-inspectable (K.2(e)).

Signed: 3.0.0_SA_CVO, before seal-open.
