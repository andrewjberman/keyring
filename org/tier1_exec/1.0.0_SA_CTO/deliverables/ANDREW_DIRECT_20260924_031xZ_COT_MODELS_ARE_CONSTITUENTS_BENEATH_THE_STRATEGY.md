# Andrew-direct 2026-09-24 ~03:1xZ at the 1.0.0_SA_CTO terminal -- the COT "Strategy" is not the model; the models are its constituents

Seat: 1.0.0_SA_CTO (Claude). Context: the CTO's ~03:0xZ reply to Andrew described Anna's Holdings tree as
"one model leaf, a custom Rebalancer strategy named after the client, not an Opal model" (from M's
measurement 100055 of the accepted COT publication ac3adb97: ACCOUNT > SLEEVE "Models" > MODEL_LEAF
rebalance_model_type=Strategy is_opal=False > 30 SECURITY).

## VERBATIM

"This is how I know you're wrong, you called it a "Strategy". The "Models" are constituents at a drilldown
level beneath the "Strategy". You need to study the implementation of "Model Portfolios" and how mdpf
pipeline for cot (cottonwood) scans for "primary" and "custom" models as constituent portfolios. You can
do further research by looking at the implementation of the Cottonwood "Satellites" on "Positioning" page
to see how there are models but also "Client" (non-model) securities involved (in the Satellites case, it
is GLD)."

## WHAT IT ESTABLISHES

1. The Rebalancer STRATEGY (e.g. "Anna *9238") is a wrapper. Its CONSTITUENT model portfolios ("primary"
   and "custom" models, which is where Opal models live) sit one drill level beneath it, and CLIENT
   (non-model) securities sit beside those models (the Positioning page's Cottonwood Satellites: models
   plus a client-held GLD).
2. The Holdings producer build_cot collapsed that level: it emitted ONE MODEL_LEAF carrying the strategy's
   name with the account's securities directly beneath it. The CTO's statement "Opal model breakdown is
   empty for Anna by data" was WRONG: the data the producer read lacks the level; the estate's MDPF COT
   pipeline already scans it.
3. Standing instruction: study the MDPF COT implementation (primary/custom constituent scan) and the
   Positioning Satellites implementation BEFORE ruling the corrected tree.

## ROUTING (CTO 100063, 100066)

- 2.0.0_SA_COO~M: STOP any COT Holdings rebuild/publication; study and report (i) the MDPF COT
  constituent decomposition, (ii) the Satellites model-vs-client representation, (iii) build_cot's
  current attribution and what it must read, (iv) the proposed COT node tree for Anna's accounts.
- 1.0.0_SA_CTO: the same study on its own instrument (an Explore read of the MDPF pipeline, the
  Positioning page and build_cot), compared against M's before the ruling.
- 2.0.0_SA_COO~P: adapter label/facts patch HELD except the shape-neutral additive carry; no wording
  that names the wrapper a model or asserts no Opal model beneath it.
- Withdrawn: CTO 100057 item (4) first bullet. Standing: the fence, status and cutover rulings.

Push state LOCAL at write (origin/CLOUD f96a0b9dd4 per MSTR 99987).
