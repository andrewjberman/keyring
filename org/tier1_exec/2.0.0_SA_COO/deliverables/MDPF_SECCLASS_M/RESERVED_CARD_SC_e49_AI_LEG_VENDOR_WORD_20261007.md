# RESERVED card -- MDPF_SECCLASS SC-e-49 AI leg: does Andrew's "full old table" word cover the three firms' missing lists?

**From:** `2.0.0_SA_COO~M1`, 2026-10-07 ~18:3xZ. **For:** Andrew, via `0.0.0_AB_MSTR`.
**Law line naming the class (CLAUDE.md, Agent Autonomy):** "NEVER call an external vendor API without Andrew's explicit per-use word
-- availability is not authorization." Section 2: "relay, never adjudicate wider or narrower; if wider seems plausible, ASK."

## The question

On 2026-10-06 00:03Z Andrew gave the word "RUn on the full old table"
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_0003Z_AI_CLASSIFIER_RUNS_ON_THE_FULL_OLD_TABLE.md`). That record
states the scope: up to 8,495 old-table (`bd-securities`) rows, Kimi K3, name and ticker only, after the direct-match step.

SC-e-49's AI leg sends a different population: **1,172 held securities from three firms' missing lists** (49financial, cottonwood,
inflection) that have no shared classification. The model and the payload are the same, and the count is under the cap. The CTO
read this run as within the word (`CTO_HALF_MDPF_SECCLASS_SC_e49_FWD15_AI_RUN_20261007.md` @6eab3cda67), counting it with the
old-list act toward one ceiling of 8,495 distinct keys. The word names the old table, though, and these keys are not drawn from
it. A wider reading is plausible, so the issuer asks instead of ruling.

## Sized

| | value |
|---|---|
| keys sent | 1,172 (49financial 432, cottonwood 130, inflection 610) |
| model calls | 1,172, at most 2,344 with retry |
| model / payload | kimi-k3 (`etf_classification_model.MODEL`) / the security's name and key only, no client or holding data |
| combined with the old-list act | 2,306 + 1,172 - 157 shared = at most 3,321 distinct keys, under 8,495 |
| includes | 7 cash funds (FIGXX, CSHI, FMPXX, ISVDT, FISXX, QACDS, TOIXX) and 142 CUSIP-keyed entries |

## Already done without the model

The DIRECT leg landed: 278 rows by conditional put, verified 278/278, ledger closed at f31f9d63bf.

## Options

- **Approve** the AI leg over the three missing lists at the numbers above. It runs in chunks of 250, with the contract bound and the
  key and call count printed per chunk.
- **Cap it**, for example to 49financial only (432 keys), with the rest in a later batch.
- **Hold**: the 1,172 keys stay unclassified, and FWD-15 stays short.
