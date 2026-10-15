# ANDREW-DIRECT 2026-10-15 ~20:4xZ (16:4x ET) -- the rivalfunds AI writer moves from gpt-5.4 to GPT 6 ("astra")

**Channel:** typed at the `2.0.0_SA_COO~RV` terminal (dell1), in this order, VERBATIM:

1. "upgrade the model to GPT6"
2. "gpt 6 astra"
3. "what im saying is that the openai model being used for that analysis should be updated from 5.4 to 6 because it needs to be smarter and not make mistakes on figure representations."

**Context (his own two earlier messages at the same terminal, same hour):** "Currently 11 of 13 funds are current for rivalfunds, need to know why. Also need to understand "why" there is a grounding fail, that should not be happening, is that a model issue?"
The page it concerns is the 2026-10-15 rivalfunds page (TXUE's two AI items served as Grounding FAIL; surprise rows `ETFS_RIVALS-D1-S17` and `-S18`, commit `67884d5199`).

## What the seat did with it (measured, read-only, 2026-10-15)

- "GPT 6 astra" resolves to the OpenAI model id `gpt-6-astra` (listed among 133 models by the project key `rivalfunds/openai-api-key`; the other GPT 6 ids listed are `gpt-6-luna`, `gpt-6-sol`, `gpt-6.1-sol`; the seat took the one he named).
- A model-string change alone breaks the stage: `gpt-6-astra` answers HTTP 400 to `temperature: 0.2`, which both clients send. The cell RIV-yb-1 carries the request change with the model.
- Trial of the production chain (prompt `a1-chain/8`, page day 2026-10-15, 13 funds, 27 calls, nothing written to S3): `gpt-6-astra` 26 of 26 items PASS with 1 correction; the stored 13:00Z sweep on `gpt-5.4` was 24 of 26 PASS with 9 corrections.
  Script and output: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/astra_trial/`.
- Scope: his word is carried as he said it. It joins round 31 (the fix-only round Andrew ruled on bbd5, "Call bbd5: yes fix only round now") as the cell `RIV-yb-1`; the CTO is told in one line. Round 31 issuance: `1af8b0dba8`.
