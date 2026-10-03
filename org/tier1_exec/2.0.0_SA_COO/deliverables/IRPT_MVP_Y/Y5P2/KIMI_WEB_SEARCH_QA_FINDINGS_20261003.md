# Y-5 packet 2 -- the Kimi swap gate's web-search QA: findings (2026-10-03 ~06:4xZ-07:0xZ)

**Author:** `2.0.0_SA_COO~Y`. **Vendor:** Kimi (Moonshot), VEW-3, "can be called freely". No YCharts call; no client data.
**Instrument:** `live_walk/kimi_web_search_qa.py`.
- It sends one swap-shaped request (`resolution_kimi.prompt_for("swap", "TIMXX")`, Case A's gated fund) with Moonshot's
  built-in tool `{"type": "builtin_function", "function": {"name": "$web_search"}}`.
- It echoes each `$web_search` call's arguments back as a `tool` message (the provider's protocol), at most 4 sends.
- It parses the last answer with the advisory's own `_parse("swap", ...)`.
- The key is read by name and never printed.

**Receipts:** `Y5P2/KIMI_WEB_SEARCH_QA_RECEIPT_TIMXX_*.json`, 9 runs. Each holds shapes only plus the transcript's sha256.

## Conclusion

`KIMI_WEB_SEARCH_UNVERIFIED` STANDS. No run produced a schema-valid swap answer. The swap gate stays closed, and Y-5's
user-named proxy (served) remains the path for a real untracked asset.

## What the runs measured

| model | variant | send 1 | send 2 (the echo) | parse |
|---|---|---|---|---|
| `kimi-k3` (the advisory's model) | as returned | `tool_calls` `$web_search`, 9.0 s | **400 "Invalid request: tokenization failed"** | -- |
| `kimi-k3` | tool message without `name` | `tool_calls`, 8.3 s | 400, the same | -- |
| `kimi-k3` | assistant `content` null | `tool_calls`, 10.8 s | 400, the same | -- |
| `kimi-k2-turbo-preview` | control | 404: not a model this key can use | -- | -- |
| `kimi-k2.6` | the swap budget (32,000 tokens, 240 s) | `tool_calls`, 14.1 s | timed out at 240.7 s | -- |
| `kimi-k2.6` | 8,000 tokens | `tool_calls`, 9.0 s | `stop`, 11.3 s | `KIMI_SCHEMA_INVALID`: the answer echoed the request's data object |
| `kimi-k2.6` | instruction as a system message | `tool_calls`, 11.8 s | `stop`, 10.7 s | `KIMI_BADJSON`: prose ("I'll search for ETF alternatives ...") |
| `kimi-k2.6` | JSON mode, user prompt | `tool_calls`, 8.7 s | **500 InternalServerError** | -- |
| `kimi-k2.6` | JSON mode, system prompt | `tool_calls`, 8.6 s | 500, the same | -- |

The models this key can use (`GET /v1/models`, ids only): `kimi-k2.6`, `kimi-k2.7-code`, `kimi-k2.7-code-highspeed`,
`kimi-k3`.

## What this means for packet 2's design

1. **The advisory's model cannot complete a built-in search.** `kimi-k3` asks for `$web_search` but refuses the echo
   (3 shapes). A swap on `kimi-k3` with the built-in tool cannot work.
2. **A single send never suffices.** Every model answers the first send with `tool_calls`. `KimiAdvisory.call` sends once
   and `_parse` requires `finish_reason == "stop"`, so a configuration of `request_fields` alone (the current
   `search_capability` shape) cannot pin web search. Packet 2 needs a bounded tool loop inside the call's deadline.
3. **`kimi-k2.6` accepts the echo, but the swap prompt does not yield the schema** in 2 shapes, and JSON mode breaks the
   echo. A working design is therefore unproven on the models this key holds.

**Options for the ruling** (the model and the source are a design decision; nothing is built):
- (a) **Two steps.** `kimi-k2.6` with `$web_search` returns free text. Then ONE `kimi-k3` call with no tools structures
  that text into the swap schema. Both run inside the swap's deadline. Each proposal is still verified by the provider read
  and approved by the user (Y-5).
- (b) **No web search.** The swap proposes from the model's own knowledge and the estate's etf-classifications catalogue
  (the rows Y-3 admits). The swap prompt's "use the configured web search" clause and the `sources` requirement are
  dropped or relaxed.
- (c) **Hold.** The served user-named proxy (Y-5) covers Case D. The swap stays closed until a provider change.

**Recommendation:** (c) now, with (b) as the next build if a suggested proxy is wanted. The served path already gives
Case D its READY Overview (SGOV named by the user). (a) adds a second model and a third vendor call to every untracked
row for an advisory the user must approve anyway.
