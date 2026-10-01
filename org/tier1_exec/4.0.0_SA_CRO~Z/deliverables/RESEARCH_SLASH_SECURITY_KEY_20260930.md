# Research: a '/' in security_key (BP/_LN_Equity, NG/_LN_Equity) -- past patterns and writer census

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~10:5x UTC. Asked by 1.0.0_SA_CTO~Z (msg 27101, self-drive AMGT ops tick 31;
row Z-S64; CVO v26 s.3). Read-only: code reads and one S3 listing; nothing changed.

## Answer in one paragraph

**The estate already has a third option, built and tested but only half adopted: C-SLASH-SAFE-KEY (AMGT-rk-76, R19-B).**
The canonical security_key keeps its '/' (the identity is untouched). Every path or partition boundary encodes it through
one reversible function: `crosswalk.slash_safe_key("BP/_LN_Equity") == "BP-SLASH-_LN_Equity"`, with
`security_key_from_slash_safe` as the exact inverse and `security_key_partition` as the one way into a builder address.
`opal_naming.key()` admits the encoded partition and refuses the raw slash
(`lib/research/identity/tests/test_slash_safe_key.py:63-77`). Seven production modules already use it. About ten
path-building sites and 30 live pool objects do not. **Recommendation: finish that adoption (option c), neither (a) nor
(b).**

## 1. How the estate keys a '/' today

- **The identity keeps the slash on purpose.** `crosswalk.py:109-116`: the root is "Preserved VERBATIM (uppercased) -- a
  share-class or line distinction is never normalised away". A trailing '/' ('BP/ LN', 'NG/ LN') is Bloomberg's own root
  spelling; a '/' followed by more characters ('BRK/B US') is a share class. So BRK/B-style names would produce keys like
  `BRK/B_US_Equity`: the problem is general, not limited to two London names. C-ONE-IDENTITY (`crosswalk.py:1-30`) says the
  key is resolved once and carried unchanged, and is never made by stripping or appending.
- **What opal_naming allows:** a raw '/' inside a partition is refused by the builder; the encoded form is admitted
  (test above, with the negative control live).
- **Adopted callers of the encoder (production, 7 modules):** `lib/research/harvest/store.py` (`entity_partition`,
  `tests/test_store.py:155`), `lib/research/corpus/{extract,typed,key_glob_census}.py`,
  `lib/research/coverage/run_reader.py`, `lib/research/freshness/build_view.py`, `lib/research/api/scoped_amgt.py` (the
  routes; `api/tests/test_slash_safe_security_route.py`).
- **Positional parsing already exists in one place:** the harvest M1 move treats "the entity is the WHOLE text before the
  last two segments" (`lib/research/harvest/tests/test_m1_move.py:144`). That is option (b), working for one reader.

## 2. The un-adopted sites (raw security_key interpolated into a path)

| Site | Kind | Path shape |
|---|---|---|
| `lib/research/filings/drafting_build.py:398` | writer | `drafting/v1/%s.json` |
| `lib/research/filings/analyze.py:1638` | writer | `drafting/v1/%s.json` |
| `lib/research/ledger/ledger.py:70` | writer | `packs/{security_key}/input_ledger.json` |
| `integrations/bloomberg/research/pull_consumer.py:57` | writer | `packs/{security_key}/status.json` |
| management/v1 writer (`lib/research/management/`, interface M-1) | writer | `management/v1/{key}/{as_of}.json` |
| peers/v1 writer (interface R-1) | writer | `peers/v1/{key}/{as_of}.json` |
| posture/v1 writer (`lib/research/posture/judge.py:8`, interface O-1) | writer | `posture/v1/{key}/{as_of}.json` |
| model-block producer (`derived/model_block/<key>/<stamp>/`) | writer | `derived/model_block/%s/...` |
| `lib/research/posture/packs.py:65, 107, 109, 114`; `lib/research/peers/engine.py:168` | readers | local `model_block_%s.json`; pool drafting/management/peers |
| `lib/research/social/collect.py:461` | writer (local) | `%s_%s.json` |

On a local filesystem the raw form is worse than a census break: `model_block_BP/_LN_Equity.json` writes into a directory
named `model_block_BP`.

**Live objects already written under raw-slash prefixes** (`opal-data-harvest`, read ~10:5x UTC, positive control
`packs/CAT_US_Equity/` = 1): `packs/BP/` 1, `packs/NG/` 1, `derived/model_block/BP/` 6, `derived/model_block/NG/` 6,
`peers/v1/BP/` 7, `peers/v1/NG/` 7, `posture/v1/BP/` 1, `posture/v1/NG/` 1 -- **30 objects**. Under the encoded
`packs/*-SLASH-` prefix: 0. `drafting/v1` and `management/v1` hold nothing for either name.

## 3. The three options, sized

| Option | What changes | Census |
|---|---|---|
| (a) slash-free canonical key | The identity itself: the crosswalk builder's root rule, `registrations.json` (12 occurrences of the two keys), every served surface keyed on the value, and the 30 objects; C-ONE-IDENTITY's "preserved verbatim" becomes a contract change | Largest. Re-opens for every future share class (BRK/B), because the rule that preserves Bloomberg punctuation stays |
| (b) positional parse in every reader | Each reader that splits a key on '/' learns the key's position | 32 `split('/')`-family sites in 19 production files under `lib/research` to audit (not all touch security keys), plus every future reader. Unenforceable: a new reader that forgets fails silently |
| **(c) finish C-SLASH-SAFE-KEY** | Route the ~10 raw-path sites in section 2 through `slash_safe_key` / `security_key_partition`; move the 30 objects to their encoded prefixes | Smallest. The identity, the crosswalk and the served key are unchanged; the encoder, its inverse, its refusals and the builder admission already exist and are tested; censuses that split on '/' work because no path segment can carry a slash |

## 4. Recommendation

**(c).** It is the estate's own ratified pattern (C-SLASH-SAFE-KEY, PRD v0.15 :857-858, "An entity id sits in a
partition, never in the builder's free-form object argument"), it costs the least, and it generalises to share classes
without touching identity. The 30 objects move in the same window as their writers switch (no parallel copies kept
running), each a copy plus a read-back before its raw-prefix original is removed. A grep-level check that refuses a raw
`security_key` interpolated into a pool path would keep the next writer from re-opening it; none exists today.

## Not claimed

Full reader-side enumeration (the 32 split sites were counted, not individually classified), and whether any portal URL
carries the raw key (the API routes are already slash-safe per their test).
