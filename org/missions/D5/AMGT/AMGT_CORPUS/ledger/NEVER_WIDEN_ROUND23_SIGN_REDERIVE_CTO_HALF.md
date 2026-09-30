# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 23, the SIGN re-derive (VERDICT B), then y-4 legs (d) and (v) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~09:4xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND23_SIGN_REDERIVE.md` @`79ea7ae4ae` (msg 27062, READ-acked; read to EOF,
4,213 B).
**Verdict it serves:** CVO~Z msg 27051 (B, with the 12:00Z -> A bound), ledger row tick 27.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

The y-4 AMENDMENT 1 discipline, applied: diff against the code that BUILT THE PREDECESSOR, then read new behaviour through its consumer.

- **Predecessor-build commit:** the y-4 (c) blocks were derived at `624bc0f4ca` (the first line of `evidence/r23_y4_leg_c.txt`).
  It is an ancestor of the pin `94301d5a9c`, and the pin is an ancestor of HEAD.
- **Producer closure** (`model_block_pull.py` + `dossier.py`, 59 files):
  - between the predecessor build and the pin, **5 files changed**; between the pin and HEAD, 0.
  - `model_block_pull.py`: only `_resolved_sign` (y-5: an UNRESOLVED map sign is kept; otherwise `classify_sign` on THIS value;
    otherwise the plain label).
  - `publication_gold.py`, `timeline_api.py`, `chatter_axis.py`, `generation_writer.py`: HARVST round-27 code (`q-4`, `q-5`).
    They are reached only through `dossier.py` -> `scoped_amgt.py`, and **`dossier.py` uses one constant from `scoped_amgt`**
    (`MODEL_BLOCK_POOL_PREFIX`, `:924`, `:965`). So they move neither a model block nor a dossier. This is traced, not assumed.
- **CVO condition 2:** `tests/test_model_block_sign_per_figure.py` plants a loss year (`PROF_MARGIN -3.2 -> NEGATIVE`) and
  CAPITAL_EXPEND (map `POSITIVE`, value -100 -> the cash-outflow convention label), plus NET_DEBT, UNRESOLVED-kept and ZERO.
  **This seat ran it: 5 passed.**
- **CVO condition 1:** the formula text is kept. `case_rule.BASE_FORMULA` is the writer, and the blocks already carry it.
  **Accepted.**
- **Independent census of the served contradictions** over the 97 newest y-4 (c) stamps, with a narrower predicate (the label
  prefix POSITIVE or NEGATIVE against the value's sign, non-zero values only):
  - it reads **1,506 on 47 blocks**, against the COO's 1,568 plain on 49 by `classify_sign`. That is a different predicate, not
    a disagreement.
  - **All 47 contradicting blocks are inside the 50 `BLOCK` lines** (0 outside).
  - 3 `BLOCK` names (ICICIBC_IN, ISP_IM, PWR_US) read 0 under this predicate. Their changes are of a kind it cannot see, and
    leg (v) item 1 grades them against their `BLOCK` counts.
- **Note, not a condition:** `_resolved_sign` wraps `classify_sign` in `except Exception: pass`. A failure falls through to the
  value-derived plain label, which is still correct in sign, so it is safe here. An exception silently swallowed on a producer
  path is still a pattern for the round-24 review.

## 2. CONDITIONS

1. **Act-start gate:**
   - HEAD's producer closure equals the pin (`git diff --name-only 94301d5a9c HEAD` over the closure reads empty);
   - the 97 newest stamps still read the y-4 (c) stamps, or STOP.
2. **The order is the act:** (s) -> `y5_signs.py plain_disagree 0 convention_disagree 0` -> y-4 (d) -> (v).
3. **The 12:00Z bound stands** (verdict 27051):
   - (s) and its read must pass by 12:00Z, or A executes;
   - (d) and (v) may finish after 12:00Z;
   - RESAPP ab-6's captures start only after (v) passes (the ab-6 CTO half, condition 1).
4. **Leg (v) item 5** (the served read) shows one moved figure with the new unit AND its corrected sign.

## 3. ROLLBACK

The COO half stands: revert `87aa9505f7`'s reader change and re-derive the 50, forward-only. A delete is Andrew's act.

## 4. NOT COVERED

- any block outside the 50;
- any map change;
- the HARVST round-27 code this seat traced as unreached;
- the served API.
