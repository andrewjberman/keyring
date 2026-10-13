# IRPT_ANLREQ -- decomposition, round 22 PROXY SUGGESTIONS (ruling B), workstream YR round 20 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's ruling B (msg 7112, in answer to the issuer's ask on the read `AR-y-244`, record `0.9.0_WK_IRPT_ANLREQ~76/r22/PROXY_SUGGESTION_READ.json` @398c0c0644): the proxy suggestion for a ticker the provider does not know (Andrew's `TIMXX`, rows `D2-S77`, `D2-S78`) comes from the Kimi swap advisory that is already built (`intake/resolution_kimi.py` kind `swap`, refused until its capability is verified), behind its own three gates in this order -- (1) a provider QA receipt, (2) `search_capability` wired where the resident builds `KimiAdvisory`, (3) the composer as caller. The user must pick a suggestion; it never fills the box or the request on its own; each is shown with its provider verification and the label "suggested"; no suggestion is shown as nothing, not as an error. Negative arm: `TIMXX` still shows no match until gates (1) to (3) read met. No new service is added.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-246` | gate (1): the QA harness (`ycharts/generate/kimi_search_qa.py`) that earns the capability flag and yields the receipt, tested offline with a fake port; the live QA designed, not run | one new source file, one new test file | WORLD |
| `AR-y-247` | gates (2) and (3), server side: the capability read from one existing mechanism (absent means today's behaviour), the swap advisory asked for a not-found row the typo check left unsuggested, each candidate provider-verified, attached as a new `suggestions` member; default off | `intake/upload_suggestions.py`, `ycharts/generate/resident_worker.py` / `resident_session.py` as needed, one new test file | WORLD |
| `AR-y-248` | gate (3), portal side: the proxy row shows each suggestion as "suggested" with its verification and a Use button; nothing fills itself; the hint says what to type | a portal candidate branch (`src/` only) | LOCAL |

## Edges and chains

- None blocking the three BUILDS: `AR-y-248` builds against the wire shape fixed in its order (the optional `suggestions` member), `AR-y-247` produces it, `AR-y-246` is independent. Release order after the drains: the live QA (a Dell lane, a later order) earns the receipt first; then the resident leg carrying `AR-y-247` with the capability configured; then the portal candidate lands on DEV through the CTO. Until the receipt exists, `TIMXX` still shows no match.

fanout: 3 of 3 chains, cap 8, reason: three independent builds against a fixed wire shape and a fixed capability shape.
