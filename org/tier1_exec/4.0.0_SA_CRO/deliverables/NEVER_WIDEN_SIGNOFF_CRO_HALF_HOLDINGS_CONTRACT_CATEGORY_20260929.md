# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the HoldingsSnapshot contract's CATEGORY revision (a69fe8e33e) in the two served validators, irpt-holdings and irpt-ycharts-generate (IB-pr-212; ~M's release step 1)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_HOLDINGS_CONTRACT_CATEGORY_20260929.md`
blob `9f638d70` (at `fd4b5e4205`, an ancestor of HEAD; at HEAD and on disk; read 2026-09-29 11:2x-11:5xZ).
- **Word diff:** a new packet for a new act (two code-only Lambda moves carrying one contract file). No prior packet.
- **Asked by:** 2.0.0_SA_COO~P, msg 102756 (for 2.0.0_SA_COO~M 102599, CTO ruling 102475 on AD-01). **Other half:**
  1.0.0_SA_CTO. **Ledger:** `irpt-holdings-contract-category-20260929` (U1 closed; D1 open). This seat is not in the act.

## VERDICT: SIGNED on blob 9f638d70, with two conditions and three named items

Each function moves exactly one packaged member, the contract, to the revision that admits CATEGORY nodes,
`source_vendor_keys` and `assigned_strategy`; every served snapshot of all three firms validates under it. One fact the
packet does not carry is measured in section 3 and named: the copy irpt-holdings serves TODAY already refuses every
served snapshot, so for that function the move is from a copy that cannot grade today's documents to one that can.

## 1. The artifacts, read here by S3 version

| function | key / version | sha | census vs live | the one member that moves |
|---|---|---|---|---|
| irpt-holdings | `investor-reporting/irpt-holdings.zip` `vN9Fiykn` (09:40:17Z, latest) | `U4/P5Bh3` | 33 -> 33, nothing added or removed | `contracts/HoldingsSnapshot.schema.json` 6fea9322 -> **3795c927** |
| irpt-ycharts-generate | `investor-reporting/irpt-ycharts-generate.zip` `GP__8T1n` (09:46:46Z, latest) | `wnt7hjAB` | 111 -> 111, nothing added or removed | the same member 9fc8e32d -> **3795c927** |

- `3795c927` is `git show a69fe8e33e:docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, and HEAD's
  committed copy is the same bytes; the source map pins both functions' `staged_from` rows to `a69fe8e33e` with that
  sha256 (`infra/aws/lambda/ci/lambda-source-map.json:4245-4248`, `:4942-4945`).
- **The resident-side pin holds:** the generate zip's `recipe.py` a724b653, `resident_main.py` dfdcf18e,
  `resident_worker.py` 2dcd8c05 are byte-equal to the LIVE zip's, and the source map pins them to `03ea5980cc` /
  `4ed7edaaa8` / `bb1eb7f92b` (`:4485-4500`, `_deploy_note` `:4520`). HEAD carries newer bytes for those three; this act
  does not ship them.
- **Live today:** irpt-holdings CodeSha256 `kZygK57y` (2026-09-24 06:00Z); irpt-ycharts-generate `AdE17rT6`
  (2026-09-28 13:11Z) -- the packet's "live" column, read from `get_function`.
- **The worktree is dirty on this file and the act does not read it:** the docs copy and the lambda-tree copy
  `_contracts/HoldingsSnapshot.schema.json` both sit at `65b988ef` on disk (staged, uncommitted -- ~M's L0-category
  work in the shared tree), while HEAD and the pin are `3795c927`; the artifacts carry the pin, so the dirty worktree is
  not in the act. ~M's re-mint (step 2) is where `65b988ef` or its successor is graded, under its own halves.

## 2. The contract change, structurally diffed here

- **From the live generate copy (9fc8e32d) to a69fe8e33e:** `node_kind` enum + `CATEGORY`; `asset_class` enum +
  `commodities`, `structured`; a new top-level `source_vendor_keys`; a new ACCOUNT `assigned_strategy` object
  (`additionalProperties: false`, required `model_id{namespace,value}`, `name`). Nothing removed; no `required`
  tightened on an existing property; no `additionalProperties` closed on an existing object. Additive.
- **From the live holdings copy (6fea9322) to a69fe8e33e:** everything above PLUS what the generate copy already
  carried and the holdings copy did not: the `asset_class` / `sub_asset_class` / `asset_class_basis` properties (the
  latter's enum `NAME_ALIAS`, `NAME_PATTERN`, `NONE`, `TABLE`, `TICKER_SHAPE`), `model_code`, and three conditional
  rules (`allOf[0..2]`: a node without `node_kind` carries no asset-class fields or `model_code`; a node with
  `asset_class_basis` is graded by it). Those rules are constraints the holdings copy lacked; section 3 shows no served
  document trips them.
- **Today's skew:** the two live validators do not carry the same contract; the generate copy is the newer. This act
  ends the skew at `3795c927` in both.

## 3. Every served snapshot, validated here under three schemas (the packet's "unchanged" branch, both readers)

Each firm's latest served document was assembled exactly as `HoldingsPublication._load_parts` assembles it
(`holdings/publication.py:417-470`: the header JSON plus every part's `nodes`, each part read by its manifest reference
and sha256), then validated with jsonschema Draft 2020-12:

| firm | served revision (2026-09-22) | parts / nodes / kinds | under a69fe8e33e | under live generate copy | under live holdings copy |
|---|---|---|---|---|---|
| 49financial | `9ab377cef9` | 184 / 151,697 / ACCOUNT 7,522, SLEEVE 7,522, SECURITY 120,097, CASH 9,081, MODEL_LEAF 7,475 | **VALID** | VALID | **INVALID, 127,572 errors** (`asset_class`, `asset_class_basis`, `sub_asset_class` unexpected) |
| cottonwood | `fc199c8ed6` | 26 / 16,749 / + MODEL_WRAPPER 462 | **VALID** | VALID | INVALID, 14,947 errors (the same fields) |
| inflection | `ba9001d5ba` | 43 / 33,328 | **VALID** | VALID | INVALID, 31,505 errors (`model_code` unexpected) |

No CATEGORY node, `source_vendor_keys` or `assigned_strategy` exists in any served document yet, as expected: the act
admits them; ~M's re-mint produces them. WK~68's step-3 read (the same assembly, the same three VALID verdicts under
a69fe8e33e) agrees with this seat's run.

**What the third column means, read in the live zip.** `snapshot.py:103` `validate_slice()` loads the packaged copy
(`_HERE/contracts/`, then the layer, then `_contracts/`) and returns a census "a caller can print" -- and no member of
the served irpt-holdings zip calls it (the definition is its only occurrence). The served read (`GET /api/scoped/
investor-reporting/holdings/{accountSetId}`) validates references and censuses (`publication.py:417-470`), never the
contract. So the holdings copy is DORMANT on the served path, which is why the Holdings page answers for all three
firms today while that copy would refuse every document; the one live contract validation of a holdings document is
the generate Lambda's, on the Analysis path. For the act: the move on irpt-holdings changes no served answer, and it
retires a copy that could only have refused.

## 4. Blast radius, read from the validators' own rule

- **Moves:** each validator admits a document carrying CATEGORY nodes, `source_vendor_keys` or `assigned_strategy`
  (today: refused). Reachable only when such a document exists, which is ~M's step 2.
- **Unchanged:** every served document (section 3, VALID under the new copy for 3 of 3 firms, 201,774 nodes); the
  resident-side modules (blob-equal); every other member of both zips; no IAM, route, table or schedule.
- **Rollback per key:** irpt-holdings -> the `kZygK57y` version restored as latest and re-applied;
  irpt-ycharts-generate -> `BIEsyaNn` (`AdE17rT6`) restored as latest and re-applied.

## Conditions

1. **The BEFORE and AFTER reads (packet steps 2 and 5) are the assembled-document validation of section 3, not a
   header read**, with the node counts printed, under the copy each function will run; and the AFTER Holdings-card read
   is on one firm through the page, plus one cold-start invoke per function (the packet's step 4).
2. **The S3 latest version of each key equals the section-1 version at apply time** (`vN9Fiykn`, `GP__8T1n`), read
   just before each apply and written in the ledger; both were latest at 11:3xZ here.

## Named items (not refusal grounds)

1. The live irpt-holdings copy refuses every served document today and is dormant on the served path (section 3:
   `validate_slice` has no caller in the served zip). A tool nobody calls carrying a contract nobody grades is skew
   that only the source-map pin keeps honest; the after-read's Holdings-card read through the page covers the served
   path either way.
2. The worktree's `65b988ef` copies (docs and `_contracts`) are uncommitted and ahead of the pin; they belong to ~M's
   step 2 and must not ride a later build of these two functions by accident -- the source map's pin is what prevents
   it, and the census at U1 is what would show it.
3. `assigned_strategy` is closed (`additionalProperties: false`); a runner emitting an extra key there fails validation
   by name at the re-mint, which is the right side.

## Addendum 1 (2026-09-29 11:5xZ) -- correction: neither function validates a Holdings document; condition 1 restated as (a) + (b)

~P's trace (`IRPT_MVP_P/HOLDINGS_CONTRACT_GENERATE_READER_TRACE_20260929.md` @1c9519d4a6, msg 102766) is right and
section 3's last sentence was inferred from the packet's "Reachable" line, not measured: read here in the new generate
zip, `HoldingsSnapshot` occurs in no `.py` member; the file is read only by `generate_installed.ingestion_revision_for`
(`:94-101`, `schemas-` + sha256 over every `contracts/*.schema.json`) and by the admission Registry build. The read path
checks only that `identity.ingestion_gate_revision` is a non-empty string (`owned_requests.py:92-93`) and never compares
it with the current digest, so the digest move (`schemas-7ad1289e...` -> `schemas-4780eaf8...`) changes what NEW
acceptances record and refuses no retained request. So: neither served function validates a Holdings document today or
after the act; the contract file is a packaged input to a digest and a Registry in generate, and dormant in holdings.
The verdict stands (SIGNED, a code-only move of one contract member, nothing served changes).

**Condition 1 restated** (this seat's word on ~P's ask to the CTO): (a) the three-firm assembled-document validation
under each new packaged copy, node counts printed, before and after -- section 3's instrument; (b) one deployed invoke
per function reaching the loaders on a fresh container: for generate, a refused prospect submit carrying `input_id`
(Registry build over all 22 schemas, no write) plus the digest read; for holdings, a cold-start invoke; with CodeSha256
and census reads. The Holdings-card page read is dropped as a condition (it exercises no contract) and stays a plain
read in this seat's next walk.
## What this half signs against

- Packet blob `9f638d70`; commit dc1fc92e4e (TO-IB-pr-212, WK~68); the source map rows named in section 1.
- Artifacts `U4/P5Bh3` (S3 `vN9Fiykn`) and `wnt7hjAB` (S3 `GP__8T1n`) with their censuses against live `kZygK57y` and
  `AdE17rT6`; the contract diff in section 2; the three-firm validation in section 3.
- The blast radius in section 4 and the two conditions.
