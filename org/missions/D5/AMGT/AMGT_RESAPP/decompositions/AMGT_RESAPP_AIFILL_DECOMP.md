# AMGT_RESAPP -- DECOMPOSITION OF THE AI FILL (FWD-41), WORKSTREAM `AIFILL`, ROUND 104

Issuer: `2.0.0_SA_COO~R2` (the CTO's naming, round-102 ADDENDUM 1 item 4; `2.0.0_SA_COO~R1` msg 5213). Spec: PRD v0.44 `FWD-41`
(`prd/AMGT_RESAPP_PRD.md`, search "FWD-41"). Companion document, not an edit of `AMGT_RESAPP_DECOMP.md` (that file is `~R1`'s and is appended
by it; s.112c there is this workstream's boundary and reads `~R2` where it reads `~G1`). Task orders carry `<round>104</round>` and
`<workstream>AIFILL</workstream>` (the gate refuses a new order into an issued (workstream, round) key). Round 103 is CLOSED (`~R1`'s keys: the cold start,
`V1`, `V1WALK`); the CTO's round-103 analysis (`ledger/ROUND_ANALYSIS.round103.md`, section 1 and the line after the enrichment list) states that `~R2` "runs FWD-41 on its own lane and round",
so this workstream's first round is numbered 104 beside `~R1`'s workstream-less 104 (the remaining 770 ms and the clean-page fixes); the two keys differ by workstream.

## 1. WHAT FWD-41 ASKS (inlined; the ratified text is the PRD's)

For every one of the 93 names, five blocks of the Security Analysis page serve content with its SOURCE CLASS (Opal source / web search /
none, with a reason) and its citations, marked machine-written (FWD-9), the web path a model call on the EXISTING Anthropic path with its
server-side web search tool, never OpenAI: (1) Exec Management: a management bio summary (new); (2) Exec Management: a recent-developments
block (new); (3) Exec Management: "The research team on management" where the pack states none; (4) Thesis: "The research team's thesis
pillars" where the pack states none; (5) the identity header's company description line (`SecurityOverlay.tsx` `identityDescriptionLine`),
which prints nothing today where none is held. A census of the 93 by 5 blocks prints the source class per cell; the CVO reads five names on PROD.

## 2. MEASURED FACTS THE CUTS REST ON (each read at the cut, 2026-10-13 ~21:3xZ)

1. **The installed Anthropic SDK (`anthropic` 0.45.0) cannot parse the web-search tool's response.** `client.messages.stream(... tools=[web_search_20250305])`
   raised `AttributeError: 'typing.Union' object has no attribute '__discriminator__'` on the server-tool blocks. The same request over plain HTTPS
   (`POST https://api.anthropic.com/v1/messages`, headers `x-api-key`, `anthropic-version: 2023-06-01`) returned in 7.2 s: `server_tool_use` blocks
   (the queries), `web_search_tool_result` blocks, and `text` blocks each carrying `citations` of type `web_search_result_location` with `url`, `title`,
   `cited_text`; usage `server_tool_use.web_search_requests` 2, 21,743 input tokens (about 13 cents at the module's rates). Recorded as
   `deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/fixtures/web_search_response_asml.json`. So the model seam is stdlib HTTPS (build ladder step 3), the key from
   `ANTHROPIC_API_KEY` exactly as `lib/research/filings/analyze.anthropic_call` already requires it; the SDK is not imported.
2. **The page already receives everything the fill needs, and the fill needs no new Opal reader.** `/overlay` serves `name`, `display_name`, `description`
   (`status`, `text`), `top_band.description_line` and `feed.items` (harvested articles: `publisher`, `title`, `url`, `published_date`, `article_key`);
   `/thesis` serves `management` (`management_status`, `officers[]`, `ceo_public_profile`, `ceo_profile_reading`), `dossier_fields` (`management.{status,value}`,
   `thesis_pillars[]`, `pack_shape`), `drafted_sections[]` (`section_id`, `sentences[]` with `text` and resolved `evidence`). Recorded trimmed as
   `fixtures/served_inputs_ASML_NA_Equity.json`. The producer reads those two served bodies by a Lambda invoke (GET), the proven pattern of the V1 census instrument;
   "the pack states none" is therefore decided from the SAME bodies the page renders from.
3. **The address is the naming builder's:** `lib.research.harvest.store.address_of("amgt", "gold", "ai_fill", entity_partition("security_key", key), object_name="ai_fill.json")`
   returns `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<K>/ai_fill.json` (the slash key `BP/_LN_Equity` encodes to `BP-SLASH-_LN_Equity`); the builder
   accepts the new table with no registry row. ONE object per name, overwritten by each run (the document carries its own `as_of`): the serve does one GET and no LIST,
   because the cold overlay is at 3.77 s against a 3.0 s target (the CTO's round-103 analysis, FWD-40 (b); `~R1`'s round 104 item 1).
4. **The data path:** the producer is a LOCAL batch (the `management/batch.py` precedent), writing S3 only on an explicit `--to-s3 --confirm-write`; the serve reads it
   inside `read_thesis_bundle` (the `/thesis` route only; no overlay path gains a read); the page reads it from the thesis bundle the page already holds.
5. **Baseline of the serve file's suite:** `lib/research/api/tests` at the base: 969 passed, 4 failed (date-dependent feed and coverage tests), recorded in
   `round104_aifill_prep/baseline_api_failures.txt`; a cell that edits `scoped_amgt.py` adds none.

## 3. THE CONTRACT (the ratified shape every cell writes against; inlined in each face)

Package `lib/research/aifill/` (new; `lib/research/management/`, `lib/research/filings/` and `lib/research/posture/` are edited by NO cell of this workstream).
Python 3.9 syntax (`from __future__ import annotations`, `Optional`, no `X | Y` at runtime), ASCII source, no non-ASCII in data it writes.

`fill/v1` document, one per security key:
```
{ "schema": "aifill/v1", "security_key": "<K>", "as_of": "YYYY-MM-DD", "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "producer": {"version": "opal-aifill/1.0.0", "model": "claude-opus-5"},
  "blocks": { "mgmt_bio": B, "mgmt_recent": B, "mgmt_team_view": B, "thesis_pillars": B, "identity_description": B } }   # exactly these five
B = { "block_id": "<id>", "source_class": "OPAL_SOURCE" | "WEB_SEARCH" | "NONE", "machine_written": true,
      "text": "<plain ASCII text, 1..1200 chars>" | null, "reason": "<plain sentence>" | null,
      "citations": [ {"source_kind": "opal"|"web", "url": str|null, "title": str|null, "quote": str|null, "ref": str|null} ],
      "opal_inputs": [str], "model_call": {"model","web_search_requests","input_tokens","output_tokens"} | null }
```
Block rules: `NONE` => `text` null, `reason` a non-empty plain sentence (no `_`), no citations. Otherwise `text` non-empty, `reason` null, at least one citation;
a `web` citation has an http(s) `url`; an `opal` citation has a plain-words `ref` (an analyst reads it: no `_ [ ] { }`, no `thesis.`/`overlay.` code path) and may carry a
`url`; `WEB_SEARCH` => at least one web citation, no opal citation, `model_call.web_search_requests >= 1`; `OPAL_SOURCE` => at least one opal citation and no web citation.
`machine_written` is always `true` (FWD-9's marking rides every block). The code-path form of an Opal input goes in `opal_inputs` (never displayed).

Where each block fills (OPAL FIRST, else WEB, else NONE with a reason):

| block | fills where | Opal source (no web search) | web path |
|---|---|---|---|
| `mgmt_bio` | every name | the CEO officer row's facts (role, role start, tenure), a RESOLVED `ceo_public_profile`, or the research team's management passage | one model call with web search about the CEO |
| `mgmt_recent` | every name | feed headlines naming a management event in the last 90 days (headlines only, no article body) | one model call with web search, last 12 months |
| `mgmt_team_view` | the pack states no management passage (`dossier_fields.management` is not SERVED with a value) | none | model call with web search; machine-written, never in the research team's voice |
| `thesis_pillars` | the pack states no pillars (`dossier_fields.thesis_pillars` empty) | two or more served `investment_thesis` filing sentences | model call with web search |
| `identity_description` | the header holds none (`top_band.description_line` empty and `description` not SERVED) | served `company_description` filing sentences | model call with web search, one or two sentences |

A block that does not fill is `NONE` with its reason (for example "The research team's pack already states management."). A model that finds nothing it can
support answers exactly `NO_INFORMATION` and the block is `NONE`. On the Opal path a figure (a digit run) the supplied facts do not hold voids the text (`NONE`, reason names "figure").

The seam every builder gets (`BlockContext`): `ctx.security_key`, `ctx.inputs` (`{"overlay": dict|None, "thesis": dict|None, "errors": {...}}`), `ctx.model`
(`ctx.model(prompt, *, system=None, web_search_max_uses=0, max_tokens=1500)` -> an object with `.text`, `.citations` (list of `{"url","title","cited_text"}`), `.searches`,
`.input_tokens`, `.output_tokens`, `.web_search_requests`, `.model`, `.stop_reason`; it RAISES a `ModelError` on any failure and never returns partial text), `ctx.now`
(tz-aware UTC). A builder is `lib.research.aifill.block_<id>.build_block(ctx) -> dict` and does no I/O of its own.

The served shape (`/thesis` bundle key `ai_fill`): `{"status": "SERVED"|"ABSENT"|"INVALID", "reason": str|None, "source": "pool"|"local"|"none", "read_completed": bool,
"as_of": str|None, "generated_at": str|None, "producer": dict|None, "blocks": {id: B} (SERVED only, else {})}`. A document that fails the serve's own checks is INVALID with
`blocks` empty: nothing is served half-validated.

The page contract (cell fa-8): `data-ai-fill="<block id>"` and `data-ai-source="OPAL_SOURCE|WEB_SEARCH|NONE|UNAVAILABLE"` on each block; a visible chip "Machine-written"; web
citations as links (`target="_blank"`, `rel` containing `noreferrer`); opal citations as their plain `ref` words; an unavailable fill (ABSENT, INVALID, missing) prints a FIXED plain
sentence and the technical reason rides a `data-` attribute (a served technical reason has underscores and paths: shown, it is a raw-code defect).

## 4. THE CELLS (9) -- every cell has text, an owner, a write set, and its checks as files dry-run at the base

| id | cell | slot | class | risk | write set | serves |
|---|---|---|---|---|---|---|
| `AMGT-fa-1` | the contract module and the orchestrator (`contract.py`, `orchestrate.py`, `__init__.py`) | `~420` | worker | LOCAL | `lib/research/aifill/{__init__,contract,orchestrate}.py`, one test module | FWD-41 (all five) |
| `AMGT-fa-2` | the model seam over HTTPS and the served-inputs reader (`model.py`, `inputs.py`) | `~421` | worker | LOCAL | `lib/research/aifill/{model,inputs}.py`, one test module | FWD-41 web path |
| `AMGT-fa-3` | block `mgmt_bio` | `~424` (staged on fa-1) | worker | LOCAL | `lib/research/aifill/block_mgmt_bio.py`, one test module | FWD-41 (1) |
| `AMGT-fa-4` | block `mgmt_recent` | `~425` (staged on fa-1) | worker | LOCAL | `lib/research/aifill/block_mgmt_recent.py`, one test module | FWD-41 (2) |
| `AMGT-fa-5` | blocks `mgmt_team_view`, `thesis_pillars`, `identity_description` | `~426` (staged on fa-1) | worker | LOCAL | three block modules, one test module | FWD-41 (3), (4), (5) |
| `AMGT-fa-6` | the store address and IO, and the run command (`store.py`, `run.py`) | `~427` (staged on fa-1, fa-2, fa-3, fa-4, fa-5) | worker | LOCAL | `lib/research/aifill/{store,run}.py`, one test module | FWD-41 census, thread |
| `AMGT-fa-7` | the serve: `read_ai_fill` and the `/thesis` bundle's `ai_fill` | `~422` (staged on fa-9) | worker | LOCAL | `lib/research/api/scoped_amgt.py` (the AI-fill region and the one wiring line), one test module | FWD-41 serve |
| `AMGT-fa-8` | the page: the shared block component and the five placements | `~423` | worker | LOCAL | `portal/src/pages/SecurityAnalysis/` (named files), a new harness | FWD-41 page |
| `AMGT-fa-9` | the Lambda-safe address constant: one `compute()` entry in the prefixes generator and the regenerated module | `~428` | worker | **WORLD** | `infra/aws/terraform/harvest/gen_harvest_prefixes.py`, `lib/research/api/_harvest_prefixes.py` (by `--write` only), `lib/research/api/tests/test_harvest_prefixes.py` | FWD-41 serve (address, rule 30) |

The classes are `LOCAL` except `fa-9`: the cells change code, tests and records, and a portal change lands on DEV only after the CTO's review. `fa-9` is `WORLD` because its `<paths>` name an
infrastructure file (the L6 gate's floor, spine v3.19, refused fa-7 at LOCAL while it carried that path; the one-line generator entry is split out into its own small order so the serve stays LOCAL).
No cell writes S3, deploys, or calls the model for real (every model call in a cell's checks is a stub or the recorded response); `fa-9` changes a generator and a generated constants module and applies nothing.

**Edges and fan-out.** fa-3, fa-4, fa-5 each import `contract` and `orchestrate` (fa-1), so they are STAGED until fa-1 merges and are cut into worktrees from the merged head;
fa-6 imports all five, so it is STAGED behind them. fa-7 reads `_hp.AI_FILL_GOLD_PREFIX`, the constant fa-9 generates, so it is STAGED behind fa-9's merge. fa-1, fa-2, fa-8, fa-9 have no unmet dependency and are PENDING at the issuance.
fa-2 and fa-7 and fa-8 write against the contract above, not against fa-1's files. M = 4 head chains (the fa-1 tree; fa-2; fa-9 -> fa-7; fa-8); live concurrency is 4 at the issuance, then 3 more when fa-1
merges and 1 more when fa-9 merges, then 1 more behind fa-1..fa-5 (9 orders, cap 8, at most 5 live at once). The dependency edges are real data dependencies (an import), never file contention; no two orders name the same file.

```
fa-1 -> fa-3 ; fa-1 -> fa-4 ; fa-1 -> fa-5 ; (fa-1, fa-2, fa-3, fa-4, fa-5) -> fa-6
fa-2   (independent head)
fa-9 -> fa-7   (fa-7 writes against the contract and reads the constant fa-9 generates; cold-start rule: one GET, /thesis only)
fa-8   (independent head: writes against the contract; portal PROD release at the cut)
fanout:
  cap: 8
  orders_total: 9 (fa-1 to fa-9)
  chains_total: 4
  wave_pending: [fa-1 ~420, fa-2 ~421, fa-8 ~423, fa-9 ~428]
  wave_staged: [fa-3 ~424, fa-4 ~425, fa-5 ~426 (after fa-1 merges), fa-6 ~427 (after fa-1..fa-5), fa-7 ~422 (after fa-9 merges)]
  portal_ref: 63c4f9e3 (the nested portal repository's PROD release, for fa-8)
  no_s3_deletes: true
  egress: none by any order; the issuer's closing real run calls the Anthropic API once per model block (about 4 calls, cents) and reads the served routes
```

## 5. WHAT THIS ROUND DOES NOT CUT, PLACED WITH ITS OWNER (the uncovered list; each is a later act, not a hole)

1. **The thread's real run, by the issuer at the drain** (the "one real run of each outcome", `/dispatch` Step 5): after fa-1..fa-6 merge, `python -m lib.research.aifill.run`
   for ONE name chosen from the V1 census as having real gaps (bj-7's `census_sections.json`), LIVE (served inputs by Lambda invoke, the model for real), `--out` a local
   directory; the document validated; the census line (OPAL/WEB/NONE) and the text of each block read by the issuer. That run is LOCAL (a local file); it is the close record of fa-1..fa-6.
2. **The store write for the names, the function redeploy and the PROD promote** are WORLD / SERVED acts, each with an owner and a gate, none of them a cell of this round:
   - the S3 write (`run --to-s3 --confirm-write`, one name, then the 93): a never-widen sign-off (`CTO + COO`) naming the address, the blast radius (one new key per name under
     `amgt/harvest/gold/ai_fill/`, nothing existing is touched) and the rollback per key (delete the key; the serve answers ABSENT); the new prefix needs the function role's S3 read
     (`comp-iam`: the issuer reads it before the sign-off);
   - the function redeploy carrying fa-7: ONE applier on `opal-amgt-scoped-api` at a time; `~R1`'s round 104 goes first (msg 5213); `~RA1` applies; the build packages `lib/research/api/scoped_amgt.py`
     and the modules it imports (`lib.research.harvest.store` is already a member through `_hp`); the admission-table tool (`r94_admission_table.py`) names the members;
   - the portal: fa-8's branch lands on DEV by the CTO's approval (Opal-internal page, staff only) and reaches PROD by the portal release seat.
3. **The 93-name run and the census** (FWD-41's census, "the CVO reads five names on PROD"): ROUND 105 of this workstream, cut from the CTO's round-104 analysis of this workstream's packet.
4. **The disabled site Z tasks** `OpalResearch-ExecManagement` and `OpalResearch-FilingsAnalyzer` (CTO O2: "re-enabled or replaced"): decided at round 105 once the producer has run; a site Z
   producer path needs `1.0.0_SA_CTO~Z`'s half. This round builds a local command and changes no scheduled task.

## 6. THE FOUR-POSTULATE RECORD

- **(i) MECE.** Domain: FWD-41's five blocks plus its four hops (producer, store, serve, page). Subtraction from the printed denominator: blocks 5 of 5 -> `fa-3` (1), `fa-4` (2), `fa-5` (3, 4, 5);
  hops 4 of 4 -> producer `fa-1..fa-6`, store `fa-6` (address and IO; the write itself placed in s.5), serve `fa-7` with its address constant `fa-9`, page `fa-8`. Uncovered with owners: s.5 items 1 to 4.
- **(ii) Same grain.** One block module per block (fa-3, fa-4); fa-5 groups three blocks of one pattern, each its own module and its own arms; fa-1 and fa-2 each one seam.
- **(iii) Intent coherence.** fa-1 to fa-6 write no served byte and call nothing external; fa-7 changes served code (not deployed here); fa-9 changes a generator and its generated constants and applies nothing; fa-8 changes a branch, never DEV and never PROD.
- **(iv) What a cell does NOT move.** None writes S3, none deploys, none promotes, none edits `lib/research/management/`, `lib/research/filings/`, `lib/research/posture/`, the overlay route,
  `bj-2`'s feed read or any V1 cell's file; fa-7 touches `scoped_amgt.py` in one new region and one wiring line in `read_thesis_bundle`.

## 7. SERIALIZED SHARED SURFACES (with `~R1`, s.112c)

- `lib/research/api/scoped_amgt.py`: `~R1`'s round-104 edits (cold start) and fa-7's region are different regions; the merge order is the drain's. fa-7 is merged through `safe-merge.sh`
  and the file's whole suite is re-run at the drain; the function has ONE applier at a time, and it is not this workstream's until `~R1`'s round-104 apply lands.
- The three page files (`ExecManagementTab.tsx`, `ThesisTab.tsx`, `SecurityOverlay.tsx`) are on DEV whole since the 19:24Z promote; fa-8 branches from DEV's head, and a V1 page cell that edits the same file
  is `~R1`'s to re-sequence (none is open).

## 8. WORKER SLOTS, RESERVED

`0.9.0_WK_AMGT_RESAPP~420` to `~428` (this workstream); `~R1` holds `~408` to `~412` and beyond that its own.

## 9. ISSUER LOG

- 2026-10-13 ~21:5xZ, `2.0.0_SA_COO~R2`: decomposition written, checks dry-run at the base (seven fail as expected, the api-suite control passes).
- 2026-10-13 ~22:3xZ, `2.0.0_SA_COO~R2`: the first commit attempt was REFUSED by `.tools/to-pipeline-gate.py` on two limbs, both amended before any order was issued, so no frozen order moved:
  (1) fa-7 `<risk>LOCAL` below its floor WORLD because its `<paths>` named `infra/aws/terraform/harvest/gen_harvest_prefixes.py`: the generator entry is split into `AMGT-fa-9` (WORLD) and fa-7 is staged behind it and stays LOCAL (the limb that graded the amendment: spine v3.19 L6 / GATE xii);
  (2) `project.json` read `dep_stage='ROUND_CLOSE'` (round 103 closed by `~R1`): the issuance commit flips it `EXECUTING` (spine s.4 carrier 2). Also renumbered round 103 -> 104: round 103 is CLOSED and the CTO's round-103 analysis gives this workstream its own round.

## 10. ADDENDUM 1 -- THE RELEASE SCOPE `AIFILLREL` (round 104), 2026-10-14 ~00:4xZ

The build round's nine cells are terminal (s.4) and the never-widen pair for the store, the read grant and the redeploy is SIGNED in both halves (`ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_{COO,CTO}_HALF.md`;
CTO conditions, msg 5304: `0.7.0_AE_CloudOps~RA1` applies steps 1 and 3 after `~R1`'s apply reads back; AMD is stored and read back before the others; a run projecting over 75 USD stops; the page lands only after step 4).
The gate refuses a new order into the issued (`AIFILL`, 104) key, so the release cells are their own scope of round 104, as `~R1` did for the walk (`V1WALK`, s.112i): `<workstream>AIFILLREL</workstream>`.

| id | cell (the pair's step) | slot | class | risk | write surface | serves |
|---|---|---|---|---|---|---|
| `AMGT-ar-1` | step 1: the adapter role's read grant for the AI-fill prefix (one list entry in `scoped-amgt-api.tf`, a targeted apply, a live re-read) | `0.7.0_AE_CloudOps~RA1` | seat order | WORLD | `infra/aws/terraform/harvest/scoped-amgt-api.tf`, the change-management ledger | FWD-41 serve |
| `AMGT-ar-3` | step 3: the redeploy carrying `fa-7` and `fa-9`, the first cold request driven alone, the served `ai_fill` verified (step 4's read) | `0.7.0_AE_CloudOps~RA1` | seat order, STAGED | WORLD | the function's code, the change-management ledger | FWD-41 serve |

Step 2 (the store) is the issuer's own act under the pair, not a cell: `run --to-s3 --confirm-write`, AMD first, read back by `store.read_document`, then the remaining resolved names, each key written once by its own run, the 75 USD stop applied
from the model calls' reported token counts. Step 4's page landing is a later, separate act under the CTO's approval (call cf85).

**Edges.** `ar-1` has no unmet dependency. `ar-3` waits on ALL of: `2.0.0_SA_COO~R1`'s `AMGT-bk-2` complete and read back (one applier at a time on the function); `ar-1` complete; step 2(a) done (AMD stored and read back). One chain, one
seat: N = 1 of M = 1, cap 8.

```
ar-1 -> ar-3   (and bk-2 [~R1] -> ar-3 ; step 2(a) [issuer] -> ar-3)
fanout:
  cap: 8
  orders_total: 2 (ar-1, ar-3)
  chains_total: 1
  wave_pending: [ar-1]
  wave_staged: [ar-3 (after bk-2 complete, ar-1 complete, AMD stored)]
  no_s3_deletes: true
  egress: none by either order
```

**Uncovered, with owners (not holes):** step 2 (the issuer, above); the page landing (the CTO's approval, then the release seat); the 95-name census and the CVO's five-name read (round 105).

## 11. ADDENDUM 2 -- THE LANDING SCOPE `AIFILLLAND` (round 104), 2026-10-14 ~01:5xZ

Steps 1 to 4 of the never-widen pair are done and read back (the grant live, 95 documents stored, `opal-amgt-scoped-api` redeployed from pin `0447f2df38` and serving `ai_fill` for all 95 names, equal to the stored documents). The CTO ruled that the approved
page candidate lands "live together with fa-7" as a feature cut from PROD through the portal's flow (call cf85, msg 5333). The gate refuses a new order into an issued key, so the landing is its own scope of round 104: `<workstream>AIFILLLAND</workstream>`
(`2.0.0_SA_COO~R1` used `LAND` for the same flow).

| id | cell | slot | class | risk | write surface | serves |
|---|---|---|---|---|---|---|
| `AMGT-ar-5` | the feature cut: the eleven files of the approved candidate `85d5749f`, re-cut onto PROD `7d5cb34d` (the candidate was cut from `63c4f9e3`), the receipt, the approval row | worker `~429` | worker | LOCAL | `portal/src/pages/SecurityAnalysis/` (a branch, never pushed by the worker), the receipt | FWD-41 page |
| `AMGT-ar-6` | the promote: `portal-release-build.sh --features <the list>` then `/prod-deploy`, the CI conclusion read, the receipt | `0.4.0_DT_ClientPlatform` | seat order, STAGED | SERVED | the release flow, the receipt | FWD-41 page |

**Edges.** `ar-5` has no unmet dependency. `ar-6` waits on: `ar-5` complete; the issuer's push of `cand/dell1/aifill-blocks-prod` and the CTO's `approved` on its row; the box manager's merge-forward onto DEV (`.tools/portal-merge-forward.sh`). One chain, two seats: N = 2 of M = 1, cap 8.

```
ar-5 -> ar-6   (push + approved row + merge-forward between them)
fanout:
  cap: 8
  orders_total: 2 (ar-5, ar-6)
  chains_total: 1
  wave_pending: [ar-5 ~429]
  wave_staged: [ar-6 (after ar-5, the push, the approved row and the merge-forward)]
  portal_ref: 7d5cb34d (portal PROD, read at the cut)
  no_s3_deletes: true
  egress: none by either order
```

## 12. ADDENDUM 3 -- ROUND 105 OF WORKSTREAM `AIFILL`: THE NARRATION / TRANSLITERATION DISARM (CVO C-S133), 2026-10-14

Source: the CTO's round-104 analysis (`ledger/ROUND_ANALYSIS.round104.AIFILL.md`, msg 5345) and the CVO's read of the stored documents (C-S133). Measured defects: 11 stored blocks over 10 names open with the model's narration glued to the answer
(`I'll research this now.MUFG announced ...`), caused by `model.parse_response` joining every text block of a web-search reply; and `Nestl` stored for `Nestle` (`fold_text` DROPPED the accented letter). Both are served by the API;
neither has reached a person. The CTO's ruling: the disarm is in the producer, never by hand-editing documents; a full re-validate of all 95 stored documents against the new contract reading 0 refused is the gate for the page to land.

| id | cell | slot | class | risk | write set | serves |
|---|---|---|---|---|---|---|
| `AMGT-fc-1` | the seam keeps only the final answer segment (`parse_response`) | worker `~430` | worker | LOCAL | `lib/research/aifill/model.py`, one new test module (and one existing test if it asserted the old joining) | FWD-41 (all five) |
| `AMGT-fc-2` | the contract: transliterate, refuse a dropped letter, refuse process narration, the name-mangling finder | worker `~431` | worker | LOCAL | `lib/research/aifill/contract.py`, one new test module (and one existing test if it asserted the old drop) | FWD-41 (all five) |
| `AMGT-fc-3` | the five builders: two prompt rules each and truthful refusal reasons | worker `~432` (STAGED on fc-2) | worker | LOCAL | five `block_*.py`, three existing test modules | FWD-41 (all five) |
| `AMGT-fc-4` | the re-validate command (`python -m lib.research.aifill.revalidate`) | worker `~433` (STAGED on fc-2) | worker | LOCAL | `lib/research/aifill/revalidate.py`, one new test module | FWD-41 census gate |

Three lines of defence, each its own cell: the structural fix at the seam (fc-1), the backstop that makes a narrated or letter-dropped document unwritable (fc-2), and the model-facing prompts plus truthful reasons (fc-3). fc-4 is the instrument for the CTO's gate.
No cell writes S3, deploys or calls the model for real; every model call in a check is a stub or the recorded response.

**Edges.** fc-1 and fc-2 write disjoint files and have no unmet dependency (PENDING at the issuance). fc-3 exercises the NEW contract (a narrated reply must be refused and named) and fc-4 calls `contract.name_mangling_problems`, so both are STAGED until fc-2 merges and are cut into worktrees from the merged head.
fc-3 and fc-4 write disjoint files. M = 3 chains (fc-1; fc-2 -> fc-3; fc-2 -> fc-4), 4 orders, cap 8.

```
fc-1   (independent head)
fc-2 -> fc-3 ; fc-2 -> fc-4
fanout:
  cap: 8
  orders_total: 4 (fc-1 to fc-4)
  chains_total: 3
  wave_pending: [fc-1 ~430, fc-2 ~431]
  wave_staged: [fc-3 ~432, fc-4 ~433 (after fc-2 merges)]
  no_s3_deletes: true
  egress: none by any order
```

**Uncovered, with owners (not holes).** (1) The re-run of the narrated and mangled names through the producer (the 10 narrated names, NESN SW, and any name the re-validate then refuses): the issuer, under the round-104 store half (75 USD ceiling, 42.24 USD spent), after fc-1..fc-3 merge, with the driver's retry rule extended
to the two new reasons; each key written once by its own run. (2) The full re-validate of all 95 with `--with-inputs`, 0 refused and 0 missing: the issuer, the gate for the landing. (3) The page landing (`AIFILLLAND` `ar-5`, `ar-6`): held until (2) reads 0 refused; `ar-5` (a branch cut, no push) runs meanwhile.
(4) The CVO's five-name read, including NESN SW and one previously narrated name. (5) Round-106 candidates, not cut: a retry on a reply truncated at max tokens (4 blocks), file-name safety for `*` in `run --out`, source quality (one blog among filings), the spend-ceiling bookkeeping.

## 13. ADDENDUM 4 -- THE HOLD SCOPE `AIFILLHOLD` (round 105), 2026-10-14 ~05:0xZ

The CVO's five-name read on PROD `7db035e4` found 4 of 5 names carrying a stated claim that its cited source does not support (msg 5423); the CTO ruled FWD-41 NOT REALIZED and that the AI-fill blocks come off the PROD page now, until a re-read passes
(`ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md`, ruling 2). The gate refuses a new order into an issued key, so the hold is its own scope of round 105: `<workstream>AIFILLHOLD</workstream>`.

| id | cell | slot | class | risk | write surface | serves |
|---|---|---|---|---|---|---|
| `AMGT-ar-7` | the hold: one environment variable on `opal-amgt-scoped-api` makes `ai_fill` read ABSENT for every name; verified on three names; the restore is the same act reversed (a later order) | `0.7.0_AE_CloudOps~RA1` | seat order | WORLD | `infra/aws/terraform/harvest/scoped-amgt-api.tf` (one map entry), the change-management entry, the deliverable folder | FWD-41 correctness |

Pair: `ledger/NEVER_WIDEN_ROUND105_AIFILL_HOLD_{COO,CTO}_HALF.md`. One chain, one seat: N = 1 of M = 1, cap 8.

```
ar-7   (independent; the restore is a later order, released by the CTO when the five-new-name re-read is MET)
fanout:
  cap: 8
  orders_total: 1 (ar-7)
  chains_total: 1
  wave_pending: [ar-7 -> 0.7.0_AE_CloudOps~RA1]
  no_s3_deletes: true
  egress: none
```

**Uncovered, with owners (not holes):** the round-106 grounding pass (items 4(a) to 4(f) of the ruling): one issuance by `~R2` after the hold lands; the fc-4 proof instance re-seat (ruling 3): `~R2`, now; the restore of the blocks: the CTO's word after a MET re-read.

## 14. ADDENDUM 5 -- ROUND 106 OF WORKSTREAM `AIFILL`: THE GROUNDING PASS (CTO ruling items 4(a) to 4(f)), 2026-10-14 ~06:0xZ

Source: `ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md` item 4 and the CVO's rows C-S143 to C-S146 (`surprise-channel/adjudications/ADJUDICATION_v129.md`). The AI-fill blocks are HELD off the served API (cell `AMGT-ar-7`, applied 05:10Z). Round 106 changes the producer so that no sentence is stored that its cited source does not carry; the CTO's grade is: re-run all 95 names, re-validate them,
then the CVO reads five NEW names drawn by sha256 over the date; the blocks return to the page only after that read is MET (ceiling 150 USD for the grounding pass and the re-run together).

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gr-1` | real sentence ends (never `Ps.`) and answer segments joined with a space: `sentences.py`, the seam | worker `~450` | worker | LOCAL | `lib/research/aifill/{sentences,model}.py`, two test modules | FWD-41 text | 4(b), 4(c) |
| `AMGT-gr-2` | fetch a cited page and say what happened to it: `sources.py` | worker `~451` | worker | LOCAL | `lib/research/aifill/sources.py`, one test module | FWD-41 grounding | 4(a), 4(f) |
| `AMGT-gr-3` | the grounding step: every sentence against the text of its sources, quotes checked mechanically: `grounding.py` | worker `~452` (STAGED on gr-1, gr-2, gr-4) | worker | LOCAL | `lib/research/aifill/grounding.py`, one test module | FWD-41 grounding | 4(a) |
| `AMGT-gr-4` | the contract carries the grounding record and can refuse a block without one (switch OFF here) | worker `~453` | worker | LOCAL | `lib/research/aifill/contract.py`, one test module | FWD-41 grounding | 4(a) |
| `AMGT-gr-5` | the orchestrator grounds every filled block; the run command supplies the fetcher | worker `~454` (STAGED on gr-1 to gr-4) | worker | LOCAL | `orchestrate.py`, `run.py`, three test modules | FWD-41 grounding | 4(a) |
| `AMGT-gr-6` | the five builders use the shared cut; the bio never restates the pack passage | worker `~455` (STAGED on gr-1) | worker | LOCAL | five `block_*.py`, three test modules | FWD-41 text | 4(b), 4(e) |
| `AMGT-gr-7` | the `About this data` panel reads the AI-fill input it renders (portal branch `cand/dell1/aifill-provenance`) | worker `~456` | worker | LOCAL | `portal/src/pages/SecurityAnalysis/{components/InputProvenance,SecurityAnalysis}.tsx`, the receipt | FWD-41 page | 4(d) |
| `AMGT-gr-8` | the contract REQUIRES the record (switch ON); drafts are drafts; the earlier tests follow | worker `~457` (STAGED on gr-5, gr-6) | worker | LOCAL | `contract.py` (one line), the builders' `make_block` calls, the test tree | FWD-41 grounding | 4(a) |

Item 4(f)'s second half ("citations that support no sentence are dropped") is done by the grounding record rule (gr-4's `support` check, gr-5's pruning); its first half (paywall-titled chips) by `sources.is_paywall_title` used in gr-3.

**Edges and fan-out.** gr-1, gr-2, gr-4 and gr-7 are heads with no unmet dependency (PENDING at the issuance). gr-6 imports `sentences` (gr-1). gr-3 imports `sentences` (gr-1), `sources` (gr-2) and is checked against `contract` (gr-4). gr-5 imports `grounding` (gr-3) and `contract` (gr-4). gr-8 follows gr-5 and gr-6.
No two orders name the same file except the test files gr-5, gr-6 and gr-8 each touch for their own breakage, which are serialized by the dependency order. M = 4 head chains (gr-1; gr-2; gr-4; gr-7); live concurrency 4 at the issuance, 1 more when gr-1 merges (gr-6), 1 more when gr-1, gr-2, gr-4 have merged (gr-3), then gr-5, then gr-8: 8 orders, cap 8.

```
gr-1 -> gr-3 ; gr-1 -> gr-5 ; gr-1 -> gr-6
gr-2 -> gr-3 ; gr-2 -> gr-5
gr-4 -> gr-3 ; gr-4 -> gr-5
gr-3 -> gr-5
(gr-5, gr-6) -> gr-8
gr-7   (independent head: a portal branch)
fanout:
  cap: 8
  orders_total: 8 (gr-1 to gr-8)
  chains_total: 4
  wave_pending: [gr-1 ~450, gr-2 ~451, gr-4 ~453, gr-7 ~456]
  wave_staged: [gr-6 ~455 (after gr-1), gr-3 ~452 (after gr-1, gr-2, gr-4), gr-5 ~454 (after gr-3), gr-8 ~457 (after gr-5, gr-6)]
  portal_ref: 7db035e4 (the nested portal repository's PROD release, for gr-7)
  no_s3_deletes: true
  egress: none by any order (stub transports and stub models); the issuer's re-run calls the Anthropic API and fetches the cited pages (declared agent)
```

**Every check was dry-run at the base and proven satisfiable** by the issuer's reference implementation in a scratch tree (gr-1 28 of 28, gr-2 21, gr-3 18, gr-4 26, gr-5 20, gr-6 15, gr-7 11, gr-8 9 of 10 with the tenth arm being the helper file the cell creates); the unchanged builders read 10 FAIL arms in gr-6's check.

**Uncovered, with owners (not holes).** (1) The release of the API hold and the return of the blocks to the page: the CTO's word after the CVO's re-read of five NEW names reads MET; the restore is one `safe-apply` by a CloudOps seat (`AMGT-ar-7`'s reverse). (2) The re-run of all 95 names under the new producer and its re-validate: the issuer, after gr-8 merges, under the CTO's 150 USD ceiling (a store-half addendum names it and the measured spend). (3) The CVO's five-name re-read, names drawn by sha256 over the date. (4) The portal release of gr-7's branch: the issuer registers the approval row after the read is MET; the DT promotes. (5) Round-107 candidates, not cut: PDF text extraction (5 of 78 sampled citations are PDFs and are UNSUPPORTED here); a fetch retry policy; the served API stripping the grounding record from the page payload.
