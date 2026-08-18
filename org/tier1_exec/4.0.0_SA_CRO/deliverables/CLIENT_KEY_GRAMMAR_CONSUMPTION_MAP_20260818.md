# CLIENT-KEY GRAMMAR CONSUMPTION MAP — 49F ADVI (P4 input)

**Author:** `4.0.0_SA_CRO` · 2026-08-18 ~16:0xZ · **archetype:** TRACE
**Commission:** `ADVI_49F_END_TO_END_PUSH_PLAN_20260818.md` §2 CRO row ("consumption map for
client-key grammar"); discharges `OPAL_ADVIPOINTERS_PRD.md` §5.B.5 ("client **key grammar** waits on
the consumption map") and turns §10's PRESUME-CONTRACT into a measured contract.
**Method:** every claim below is a live read (S3 listing / served bytes / portal source at the cited
line) — no repo-prose claim is load-bearing. Portal source read at submodule HEAD (portal on DEV);
served artifacts read 2026-08-18 ~15:5xZ.

---

## 1. THE QUESTION

The 49F P4 publisher (DS~B, `d_publisher_base` fleet) re-derives client identity on the canonical
spine (`rel_<hash>`, A_01 grammar), while the served product rides the Black Diamond household spine
(`z########`). The two-identity-systems fact is measured: **0/201 key overlap under any id and any
normalisation** (PRD §10). The grammar decision — may the publisher re-base the served client key —
needs the denominator no one had: **every consumer of the served key, and what each uses it FOR.**

## 2. THE KEY SPACES, MEASURED LIVE (2026-08-18)

| plane | grammar | denominator (live read) |
|---|---|---|
| `s3://opal-data-bd/gold/entities/clients/{key}/` prefixes | `z########` = 3,612 · `acct_z…` = 138 · literal `0` = 1 | 3,751 PRE entries; **zero `rel_*`** |
| `s3://opal-data-bd/gold/artifacts/clients_tab.json` `clients[].key` | `z…` + one `0` ("No Relationship") | 3,049 rows, as_of 2026-08-18T04:58Z |
| served detail payload `client_key` field | `z…` (e.g. `z08327149`, byte-read) | sample read, generated_at 2026-08-16 |
| `s3://opal-data-inf/platinum/clients/{id}/` (INF, for contrast) | native integer household_id | 1,317 PRE entries |
| canonical 49F gold (`dimensions/dim_relationship`) | `rel_<hash>` (A_01) | producer-side only; serves nowhere today |

⚠ `opal-partners-data/lambda_function.py:930` docstring example reads `'rel_z0812893211'` — **prose,
falsified by the served bytes above** (the live prefix space and payload carry bare `z…`). Do not
cite that docstring as the key contract.

## 3. THE CONSUMPTION MAP — every consumer, and what the key IS to each

| # | consumer (file:line) | reads | the key is used as | bind class |
|---|---|---|---|---|
| C1 | `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx:220,421-428` (BooksTab picker → L3) | `clients_tab.json` `clients[]` roster → `selectedClientKey` | **JOIN HANDLE**: queryKey `['advisor-book-client',…]` → C5's Lambda route param | HARD — byte-match required roster↔detail-tree |
| C2 | `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:137,188-192` (L2 advisor book → L3) | advisor book payload `book.clients[].client_key` | **JOIN HANDLE**: same queryKey/fetch chain as C1 | HARD — byte-match book↔detail-tree |
| C3 | `AdvisorBookClientDetail.tsx:39-40,103-105` | prop `clientKey` | accepted for parent symmetry, **explicitly unused** (`void clientKey`) | NONE |
| C4 | `DistributionTab.tsx:1977-2013,2348,2403` (BI stacks) | per-period `stacks[].client_key` | **chart column key + ordinal derivation**, local to one artifact | SOFT — internal consistency within the artifact only |
| C5 | Lambda `opal-partners-data/lambda_function.py:932-934` route `/api/scoped/partners/books/relationship/{clientKey}/platinum-summary` | — | **S3 PATH SEGMENT**: `gold/entities/clients/{client_key}/detail.json`; charset gate `isalnum or '_'` (`:932`) | HARD — FE key must equal the S3 prefix |
| C6 | same Lambda `:1125` timeseries route | — | S3 path segment: `gold/entities/clients/{id}/aua_timeseries.json` | HARD |
| C7 | `ClientsTab.tsx:538-580` deeplink hh→advisor lookup | `client_directory.json` (INF-only today; `:536` says 49F/BD "don't have client_directory.json") | **CROSS-ARTIFACT MAP KEY** | HARD where the tenant has a directory; 49F N/A today |
| C8 | `getPlatinumClientDetailStatic` (`advisor-intelligence.ts:1101-1297`, INF static path) | `platinum/clients/{hhId}/{detail,composition,top_holdings,timeseries}.json` + per-account `accounts/{acctId}/timeseries.json` | S3 path segment (INF native-int space) | HARD (INF) — the same publisher pattern 49F P4 will emit |
| C9 | `platinum/firm/cumulative_chart.json` `adv_drill` categories (Lambda `:816-818`) | client labels with **embedded** z-ids in the label string ("Chan, William & Shelley (z08327149)") | **DISPLAY STRING ONLY** (pseudonymization retired `:829`, authorization is the gate) | SOFT — cosmetic, but a grammar flip makes labels disagree with keys |

**Negative findings (measured, load-bearing):**
- **No URL persistence anywhere in ADVI**: `useSearchParams`/`useParams` — zero hits under
  `portal/src/pages/AdvisorIntelligence/`. `booksClientKey` is React state
  (`_partners/inflection/index.tsx:200,266`). **No bookmark/deeplink URL carries a client key**, so a
  grammar flip breaks no saved links.
- **No durable client-side storage**: the key lives only in component state + react-query cache
  (session-scoped; `gcTime` on unmount noted at `AdvisorBookView.tsx:194`).
- `platinum/firm/clients-tab-slim.json` omits `clients[]` entirely (`types.ts:980`) — the slim
  family is key-free.

## 4. WHAT THE MAP CONCLUDES (the grammar decision, framed for CTO/COO)

1. **The `z…` grammar is a SERVED CONTRACT with 6 hard bind points** (C1/C2/C5/C6/C7-class/C8-class)
   spanning 4 artifact families + 1 Lambda route — but **every bind resolves at runtime from a
   served roster**; nothing durable (URL, storage) holds the key. So a re-base is *possible* as an
   **atomic all-families flip** (roster + book + entities tree + directory + BI stacks in one
   window), and *only* as one — a partial flip breaks the C1/C2→C5 join silently (the FE would ask
   for a key the tree no longer spells).
2. **The blocking fact is identity coverage, not charset or plumbing**: `rel_` keys pass C5's
   charset gate (`isalnum or '_'`), but the canonical derivation covers a **different population** —
   0/201 overlap, `A_06` is SmartX-**account**-grain (no household crosswalk exists,
   `d04_clients_tab.py` header), and `d05`'s two-hop crosswalk reaches the EXACT-class subset only
   (1,652 aligned pairs vs 3,612 served households). **A grammar flip today would re-key the product
   onto a spine that cannot yet name every served household.**
3. **Recommendation (CRO, consulted): the 49F P4 publisher ADOPTS the served `z…` grammar for v1**
   — the publishers keep emitting served keys in the served grammar (the port-fidelity doctrine:
   a faithful port is the strongest parity evidence), `rel_<hash>` stays the canonical-internal
   join in gold parquet, and the grammar flip is a NAMED FUTURE ACT gated on the household spine
   map (PRD §10's open hop: who produces `gold/dimensions/client_dimension.parquet`, and is the
   household grouping DERIVED or a VENDOR GIVEN). That act, when it comes, is a per-key serve-shape
   change under NEVER#3 discipline with this map as its blast radius.
4. PRESUME-CONTRACT is hereby DISCHARGED INTO A MEASURED CONTRACT — the presumption held; it is now
   enumerated instead of presumed.

## 5. BLIND SPOTS / DENOMINATORS

- Portal read at the DEV submodule HEAD in this worktree; the PROD build could differ (not read —
  DT owns the promote surface). The Lambda read is the REPO copy; per Rule 22a its deployed bytes
  were not byte-verified here (the 0.8.0 census covers that axis). Neither gap changes §4: the
  served S3 bytes — the strongest evidence — carry `z…` exclusively.
- The `acct_z…` (138) prefixes are account-grain residents in the household tree — not classified
  here beyond existence; the P4 per-key census (DS~B) should carry them a disposition.
- Consumers OUTSIDE the portal (agentic/query-index readers) were not swept; the proposed platinum
  agentic query index is unbuilt (`ADVI_PLATINUM_AGENTIC_QUERY_INDEX_STRATEGY_20260806.md`,
  proposal-only), so the portal is believed the full consumer set today — believed, not proven.
