# IRPT_ANLREQ -- decomposition, round 22 PROXY SUGGESTIONS, ruling (a') -- the search endpoint plus one plain chat call, workstream YR round 21 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's rulings on the proxy suggestion (Andrew's `TIMXX`, rows `D2-S77`, `D2-S78`): B (msg 7112: the Kimi swap advisory behind three gates), (a) (msg 7133: a bounded tool loop, one round, fallback (b)), and (a') (msg 7137): the first cut of ruling B's server cells (`AR-y-246`, `AR-y-247`) found two things -- their `<paths>` omitted the files they write (rows `W79-S1`, `W80-S1`, the issuer's error) and the estate's own QA record (Y5P2, 2026-10-03) shows the single-request web-search design cannot earn a receipt; this seat then read Kimi's documentation (https://platform.kimi.ai/docs/guide/use-web-search): the `$web_search` builtin tool retires on 2026-10-20 and its replacement is `POST /v1/tools/search`. (a') therefore: the server calls the search endpoint and makes ONE plain chat call; the chat call may propose only a ticker that appears in a search result it was given and each proposal cites that result's url, a proposal with no matching result is dropped before provider verification; same three gates (QA receipt, capability wired, the composer as caller), same proof set (TIMXX plus at least 4 known funds, 0 errors), same one-round box, fallback (b) (TIMXX keeps "no match", only the hint wording ships); the capability reaches the resident only inside a signed release pair.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-249` | the swap advisory rebuilt on the search endpoint: a search transport (`kimi_port.kimi_search`), the capability gate on the new shape, one plain chat call, the ticker-in-a-result and cited-url drop rules | `intake/resolution_kimi.py`, `ycharts/generate/kimi_port.py`, the two test files it edits or adds | WORLD |
| `AR-y-250` | gate (1): the QA harness (fixed case list before the run: TIMXX, at least 4 known funds, a nonsense symbol, two injection strings) that earns the flag and yields the receipt, offline with fakes; the live QA designed | `ycharts/generate/kimi_search_qa.py` and its test file | WORLD |
| `AR-y-251` | gates (2) and (3), server side, re-cut with its grant: the capability read from a package member (absent means today's behaviour), the swap advisory asked for a not-found row the typo check left unsuggested, each candidate provider-verified, attached as a new `suggestions` member | `intake/upload_suggestions.py`, `ycharts/generate/resident_worker.py`, `resident_session.py`, one new test file | WORLD |

## Edges and chains

- None blocking the three BUILDS: they build against THE INTERFACE fixed in each order (`KimiAdvisory(..., search_capability=, search=)`, the capability dict, the `candidates` return shape). `AR-y-248` (the portal, running) builds against the `suggestions` wire shape. After the drains: the live QA (a Dell lane, a later order under the signed pair) earns the receipt first; then the resident leg carrying `AR-y-249` to `AR-y-251` with `kimi_search_capability.json` as a package member; then the portal candidate lands on DEV through the CTO. If the live QA fails or the round ends first, fallback (b) ships.

fanout: 3 of 3 chains, cap 8, reason: three independent builds against a fixed interface.
