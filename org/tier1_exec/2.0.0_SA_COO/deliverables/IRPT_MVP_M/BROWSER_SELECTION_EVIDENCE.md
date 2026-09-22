# Accepted selection browser handoff — 2026-09-22

State: bounded implementation and producer verification; independent CVO M review pending. This is not M6/M7 or full product acceptance.

Portal checkout: `C:/Users/AndrewBerman/Desktop/ajb_irpt_m_portal`, branch `codex/irpt-m-ui`, based on F final `8e6e2e38cc299c4415d42b0fe627edc50ec35e1b`.

- `e2df1c04a26028516559b72a0f0b62842867497f`: HoldingsTab clears synchronously by full request identity, handles typed refusal, whole-group selection request helper and controlled browser regression.
- `e001b6d59ed08522d6ba98a4fa5a6b695bb065eb`: consumed P typed client `61983ce9`, preserving P author.
- `d4fca0e5692730e9f79c3fa013159ffa63ba5b6b`: header creates and waits for an accepted selection; selected reference, fingerprint and directory revision remain distinct; firm/entitlement context resets state; superseded selection responses cannot win. TabShell mounts custody tabs only after acceptance and removes duplicate inactive-tab and synthetic 1970-date requests. Analysis holdings/composer receive the accepted selection; prospect analysis remains independent.

Header export anchors previously used a directory/scope revision as a report reference. Those fabricated bindings were removed. P must wire exports from actual accepted report identities/revisions; this candidate does not complete export integration.

## Verification on the combined tree

`bun run typecheck`: exit 0. `bun run build`: exit 0; existing stylesheet URL parsing warnings, dynamic/static import warning and large-chunk warnings were reported, not repaired or represented as clean diagnostics.

With `IRPT_CONTRACTS_DIR=C:/Users/AndrewBerman/Desktop/ajb_irpt_m/docs/contracts/investor-reporting/v1`:

`bun test ./src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts ./src/pages/InvestorReporting/__tests__/m-selection/selectionRequest.test.ts`: 11 passed, zero failures. P's seven tests exercise actual captured producer envelopes, canonical route parity and separate retained identity. M's four tests exercise whole client/relationship intent, explicit account narrowing and refusal of a firm-wide expansion.

Earlier focused query/drill/slice run: 28 passed, zero failures. An initial broad substring-filter run unintentionally included more old suites: 56 passed, six browser skips because its dev-server precondition was absent, and one error. It is not an overall green result. An initial new API-test invocation lacked the isolated worktree contract-root environment setting: ten passed, one missing routes-file failure; setting the existing canonical override yielded the 11/0 result above without changing tests.

Actual mounted Chromium/Edge DOM drivers, with this checkout's Vite on localhost:5440:

```text
node src/pages/InvestorReporting/__tests__/m-selection/holdings-race.mjs
node src/pages/InvestorReporting/__tests__/m-selection/header-race.mjs
```

Both passed with zero page errors. Holdings checks A-to-B transition, null clear, late C after D, as-of change, root change and failed fetch. Header drives the actual client combobox and tabs: zero custody requests before approval, exact whole-client request, selected `sel_` ID distinct from fingerprint, no old body while a new selection is pending, late selection suppression, context reset and refused selection. The drivers inject controlled API promises and view fixtures into the actual components. They do not claim live transport/backend, provider or three-firm publication evidence.

The component compiler schema-check could not resolve a nearby types.ts and routed its baked shared-portal path; that instrument is not cited as a successful check of this isolated checkout. Precommit risk map was stale and its TS/HTML gate coverage was zero; the explicit language/build/browser checks above supply the bounded evidence.

Handoff to P and CVO M: exact notices at 20260922T223929Z/223930Z. CVO M ACK at 224004Z begins independent isolated review. Integrators already on P `61983ce9` apply M `e2df1c04` and `d4fca0e5`, not the duplicate P cherry-pick.

## Registry and remaining source work

Pending registry candidate remains `587e782bc6`, generation evidence `3c14153eeb`. CRO report `4d6a4338ae`, final C1-C4 proof `983550adde`, current correction `6d5f979202`; independent CVO M `eb00a0c6b2` plus addendum `da8bc778f7`. M independently reran proof checker bound to exact order with C1-C4: VALID rc0, four rows, zero violations. Issuer closure is shared-repository `39e28f17b1`. G naming-owner review and fresh carrier reconciliation are still due. Pending policy remains non-writable.

R-P07 primitive closure is attributed CVO P `9e6a617405` on `c5eace08c7`; M did not rerun it. Composed retention, concurrency, IAM, physical disposal and full S7 remain outstanding.

Accepted custody publication remains a concrete M4 gap: existing land() overwrites a dated JSON object and advances latest before its post-write size check, with no Gold Parquet/versioned manifest. Current runtime load follows a mutable pointer without a pinned object version/hash. No accepted custody normalization adapter is claimed from that implementation. Y was explicitly told at 224250Z not to substitute caller prices or fixtures while maintained security/price/profile/custody adapters remain incomplete. Source-to-publication-to-browser proof for all three firms is still required.

Push state: LOCAL, no push performed. At 22:41Z, `git ls-remote` measured portal origin DEV `b3d5f59b4534eb653105f9bedc9e178384111c9f` and workspace origin CLOUD `b8136f26dca101d9f0f74818df109f25cae5354d`.
