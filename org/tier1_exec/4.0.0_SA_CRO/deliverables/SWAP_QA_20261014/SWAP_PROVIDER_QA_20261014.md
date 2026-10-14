# Provider QA -- the web-search swap and the replacement function (C-SWAP), 2026-10-14 ~18:1xZ-18:4xZ

**Run by:** `4.0.0_SA_CRO~DELL2` at the dell2 terminal, overseen by Andrew (record
`ANDREW_DIRECT_20261014_181xZ_WEBSEARCH_AND_REPLACEMENT_NOW_ANDREW_OVERSEES.md`).

**What it exercised:** the live Moonshot API (`https://api.moonshot.ai/v1/chat/completions`, key from `astn/kimi/api-key`, never printed),
through the repo's own prompt and parser (`infra/aws/lambda/investor-reporting/intake/resolution_kimi.py`, `prompt_for` and `_parse`).
Read-only lookups were made against `etf-classifications` (DynamoDB `get_item`) and yfinance.

**Nothing was written to Opal state; no code was changed.** The receipts are the JSON files in this folder (01-07), each carrying its
`qa_receipt_sha256`.

**Why it was needed:** the swap is gated off in code ("Swap refuses until provider QA has established actual web-search support and
pinned its exact tool configuration", `resolution_kimi.py:5-6`, gate `:159-165`).

## Findings

| # | What | Result | Receipt |
|---|---|---|---|
| 1 | Typo check (kind `check`), kimi-k3, no search | **WORKS.** "QULA" -> QUAL, confidence 0.75; 10.5 s one-shot, 17.9 s in the loop run | 01 |
| 2 | kimi-k3 web search, `tools=[{"type":"builtin_function","function":{"name":"$web_search"}}]` | Round 1 asks to search (`finish_reason: tool_calls`). **Today's code path fails here:** `KimiAdvisory.call` sends ONE request and requires `stop`, so a search turn is `KIMI_FINISH_UNSUPPORTED` | 01 |
| 3 | kimi-k3 echo round (returning the `$web_search` arguments as a `role: tool` message) | **FAILS at Moonshot** every time: 400 "Invalid request: tokenization failed". Tried the minimal echo, the full echo, `content: null`, no tool name, and thinking disabled | 01, 02 |
| 4 | Models on this key (`GET /v1/models`) | `kimi-k2.6`, `kimi-k2.7-code`, `kimi-k2.7-code-highspeed`, `kimi-k3` | -- |
| 5 | kimi-k2.6 echo round | **WORKS** (200, stop): 15.6 s with thinking on, 22.4 s with thinking off at temperature 0.6 (k2.6 refuses any other temperature when thinking is off) | -- |
| 6 | **Identification** with search, k2.6, three holdings Yahoo cannot price and the registry lacks: BREIT, SREIT, KPEC | **3 of 3 correctly identified with real sources:** Blackstone REIT (Real Estate), Starwood REIT (Real Estate), KKR Private Equity Conglomerate (Alternatives / Private Equity). Cited URLs answer 200 or 403 (403 = a bot-blocked real site) | 03-07 |
| 7 | Turnaround per holding | thinking off: **24-45 s** (one search plus at most one repair turn). Thinking on: about 80 s, and KPEC's round 2 hung past the 240 s swap budget twice | 03-06 |
| 8 | Model-proposed replacement ETFs | **NOT reliable:** | 03-07 |
|   | -- answer shape | Without a repair turn, the model often ends with prose ("Let me search for...") and no JSON (`KIMI_BADJSON`) | 05 |
|   | -- source links | It proposes candidates with no source URLs, and the parser rejects the WHOLE answer (`KIMI_SCHEMA_INVALID`, `_parse` requires 1-10 sources per candidate). BREIT: VNQ had one, SCHH and USRT had none | 07 |
|   | -- registry fit | Its picks can sit outside Opal's registry: KPEC -> PSP, PEX and BIZD are all priced by Yahoo, none is in `etf-classifications` | 06 |
|   | -- good case | BREIT with thinking on -> VNQ, priced by Yahoo and in the registry as alternatives / Real Estate | 03 |
| 9 | A designated-proxy table (C-SWAP step 4) | **Does not exist.** `org/standards/MDPF_SECCLASS_CONTRACT.json` has no proxy key | -- |

## What works today, and what makes the replacement function work

**Works:**
- the typo check;
- web-search IDENTIFICATION and CLASSIFICATION of an unknown holding (kimi-k2.6, thinking off, 24-45 s).

**Needed, smallest set:**
1. **The tool-call loop in `KimiAdvisory`:** echo each `$web_search` call's arguments as a `role: tool` message until `stop` (at most 4
   rounds), plus one JSON repair turn. Today the code is one-shot.
2. **The swap model is `kimi-k2.6`** (kimi-k3 stays for the check). The gate's `cap["model"] != MODEL` test and the
   `request_fields` allow-list (`tools`, `tool_choice` only) must admit k2.6 and `thinking: {"type":"disabled"}` / `temperature: 0.6`.
   Pinned configuration: `{"model":"kimi-k2.6","temperature":0.6,"thinking":{"type":"disabled"},"tools":[{"type":"builtin_function","function":{"name":"$web_search"}}]}`.
3. **The replacement is picked DETERMINISTICALLY, not by the model.** The model identifies and classifies (that is reliable). Opal then
   picks the replacement from `etf-classifications` by `asset_class` / `sub_asset_class` (its GSIs), keeping the first match Yahoo prices
   with the longest history. This is C-SWAP's own design, steps 3-4. It needs one choice from Andrew or the CTO: either a short
   designated proxy per sub-class, or the "longest Yahoo history in the sub-class" rule.
4. **Model-proposed candidates, if kept at all, are advisory:** dropped individually when they lack sources or fail the Yahoo/registry
   check, never failing the whole answer.

**Order, per Andrew ~17:5xZ:** Yahoo -> YCharts -> replacement (identify with search, then the deterministic proxy) -> if all fail, the
report runs without the security and names it.

## Not tested

- More than three unknown holdings.
- A CUSIP-only holding.
- `kimi-k2.7-code*` models.
- `tool_choice` forcing.
- Cost per call (token usage is in the receipts).
- Whether a Moonshot account limit throttles a burst.
- Anything inside the deployed resident (these were local calls).

-- 4.0.0_SA_CRO~DELL2
