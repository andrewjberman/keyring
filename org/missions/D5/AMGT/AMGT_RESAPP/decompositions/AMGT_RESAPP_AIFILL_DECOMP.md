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


## 15. ADDENDUM 6 -- ROUND 107 OF WORKSTREAM `AIFILL`: THE CARRY OF `W452-S1` (CTO round-106 analysis item 3), 2026-10-16 ~02:2xZ

Source: `ledger/ROUND_ANALYSIS.round106.md` item 3 ("COO~R2's W451-S1 and W452-S1, as that lane's round-107 items"); `REMEDIATION_v44` rows `AMGT_RESAPP-D1-W451-S1` and `AMGT_RESAPP-D1-W452-S1` (owner and disarm owner `2.0.0_SA_COO~R2`); `~R1`'s round-108 decomposition (`AMGT_RESAPP_DECOMP.md`) places both as this lane's. This is the workstream's round 107 (round 106 is closed, ADJUDICATION_v133); the key (`AIFILL`, 107) differs from `~R1`'s global round 108. The AI-fill hold stands; nothing here lifts it.

**`W451-S1` is NOT a cell.** Measured at HEAD: `lib/research/aifill/sources.py` lines 244-246 already return `UNSUPPORTED` with note `content type <t>` for a 2xx whose declared type is not text, html or xml, and `tests/test_sources.py::test_a_non_text_content_type_is_unsupported` (image/png, octet-stream, zip) passes; the rung was added at the `gr-2` close (`229d0ed982`, merged `f57f6e049a`, 2026-10-14). The row asked for what was built; it was disarmed and my earlier "carried to round 107" line corrected in `AMGT_RESAPP-D1-S38`. The narrower edge (a 2xx body with no Content-Type header reads OK) is INERT for a false claim and is carried to the CTO as a recommendation of NO.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gs-1` | a CONTRADICTED sentence records the list index of the source that contradicted it and a quote checked mechanically against that source's full text; the system prompt asks for both: `grounding.py` | worker `~481` | worker-light, DIRECT-ACT (one cell, about 15 product lines) | LOCAL | `lib/research/aifill/grounding.py`, `tests/test_grounding.py` (one assertion), one new test module | FWD-41 grounding | `W452-S1` |

**Chain read:** M = 1 (one cell, no edge), N = 1, cap 8. **Contract:** unchanged; `contract.py` line 355 skips every non-SUPPORTED sentence, so a CONTRADICTED sentence may carry a source and a quote with no contract edit (the check's arm 10 reads `_record_shape_problems` on such a record: no problem). **Rule of the cell:** the verdict stays CONTRADICTED and the sentence stays dropped whatever the model's source or quote says; the source and quote are recorded only when the label names a SHOWN source and the quote (12 or more characters, case, spacing and punctuation ignored) is in that source's full text, else both stay null as today. A contradicting source is never a supporting source: it enters neither `used_urls`, `used_labels` nor `kept`.

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round107_aifill_prep/checks/check_gs1_contradicted.py`, 11 arms. At the base: `AIFILL GS-1 ARMS: NO (8 of 11)` (the three build arms FAIL, the eight bound and control arms PASS). The issuer's reference edit in a scratch copy of the package: 11 of 11, and exactly one existing test fails, `tests/test_grounding.py::test_contradicted_is_dropped_and_recorded_as_such` at line 119 (it pins `source is None` for a CONTRADICTED row that names S1 and a valid quote); the cell updates that one assertion.

**The CTO's fork, not taken here:** the row's remedy reads "the record carries the contradicting source index and quote, OR the CTO rules null the contract (round 107 item (g))". No ruling on (g) is in `ROUND_ANALYSIS.round106.md` or `round107.md`; this cell builds the first branch, which the row names as its remedy and which is one reversible assertion if the CTO later rules null.

**Uncovered, with owners:** the five-new-name re-read and the release of the hold (the CVO and the CTO, unchanged); the typeless-body edge (the CTO, recommendation NO); the `gr-7` portal branch registration (this seat, after the re-read is MET).


## 16. ADDENDUM 7 -- ROUND 108 OF WORKSTREAM `AIFILL`: EACH BLOCK CARRIES ITS OWN VALIDATION STATE (CTO msgs 6444 and 6446), 2026-10-16 ~03:3xZ

Source: the CTO's ruling on row `AMGT_RESAPP-D1-S40` (msg 6444: the Opal gateway's `harvest_get_research` is an INTERNAL reader and is accepted; CONDITION: each stored document carries its own validation state, the `revalidate` verdict and the grounding result plus "held" until the CVO's five-name read clears it) and his pick (A) in msg 6446: the state lives in each block, ONE new block key, "a LOCAL cell with no gateway deploy", "use the block contract's existing taxonomy pattern, and carry its four-postulate record in the cell", "cut the cell before the store write". Measured first (msg 6445): `contract.py:499` refuses a document with other than the six top-level keys, and the gateway copies only `as_of`, `generated_at` and `blocks` (`harvest_research.py:263-264`); blocks pass through whole, and each filled block already carries its `grounding` record (the grounding result). The AI-fill hold stands. This is the workstream's round 108 (round 107 is `gs-1`, closed; the gate refuses a second issuance into the same (workstream, round) key).

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gt-1` | the block `validation` key (shape, states, verdicts, the CLEARED-over-REFUSED refusal) in `contract.py`, and `stamp_validation` in a new `validation.py` | worker `~482` | worker-light, DIRECT-ACT (about 70 product lines) | LOCAL | `lib/research/aifill/{contract,validation}.py`, one new test module, a single assertion in an existing contract test if one pins the key rule | FWD-41 store write | CTO 6446 (A) |

**Chain read:** M = 1, N = 1, cap 8. **The key.** `validation` is an OPTIONAL block key (no switch: a present key is always checked, a missing one is no problem), allowed on every block, a NONE block included, because the claim is about the stored block, not its text. Shape: `{"version": "validation/1", "state": "HELD"|"CLEARED", "verdict": "PASS"|"REFUSED", "contract": <the producer version that judged it>, "checked_at": "YYYY-MM-DDTHH:MM:SSZ"}`. Every problem about it starts with the word `validation`. A CLEARED state over a REFUSED verdict is refused.

**FOUR-POSTULATE RECORD (CLAUDE.md rule 24; the block contract's own pattern is a closed tuple per axis, a key set, and a problem line per breach).**
- **(i) MECE over a DECLARED domain.** Domain: a block of a STORED fill document (95 documents x 5 blocks = 475 once the store write lands; 0 carry the key today). `state`: HELD | CLEARED partition "has the CVO's five-name read cleared this block"; every stored block is exactly one. The member hunted by subtraction: a block cleared and later found wrong. It is NOT a third state: a wrong block is rewritten (as a block with the rewrite's own state, or as a NONE block with a reason, a class the contract already has), so the domain holds no WITHDRAWN member; a later need is an enum edit with its own record. `verdict`: PASS | REFUSED partition "does the block, without this key, have a contract problem under the named contract version"; exhaustive and exclusive by construction (the problem list is empty or it is not). **Token census, word-boundary, printed:** `HELD` or `CLEARED` over `lib/research` `*.py`: 97 occurrences in 27 files and ZERO in `lib/research/aifill` (the other meanings are the filings and harvest "held marker" modules, a different object); `REFUSED` or `PASS` over `lib/research/aifill` `*.py`: 27 occurrences in 8 files (`sources.py` and `contract.py` use REFUSED as a SOURCE status, an HTTP answer in `grounding.sources[].status`; `revalidate.py` uses it as its own refusal verdict, which is the sense used here). The word REFUSED therefore sits on two axes by key path (`grounding.sources[].status` against `validation.verdict`); they never share a key, and the cell's tests print both.
- **(ii) SAME GRAIN.** Both axes are per block, stamped at one time by one function; neither is a per-document or per-sentence value, and the grounding result stays where it is (per sentence inside the block's `grounding`, already served whole).
- **(iii) INTENT COHERENCE.** `state` is a human-gate axis (may a reader treat this block as past the CVO's read); `verdict` is a mechanical axis (did the contract pass it). One axis, one intent each; `contract` and `checked_at` are the provenance of the verdict, not a third axis.
- **(iv) STATE COHERENCE (the values one remedy does NOT move).** Clearing the hold moves `state` and `checked_at`, never `verdict` (a rewrite must re-judge and re-stamp, so it moves both in one act, and CLEARED over REFUSED is refused); re-running `revalidate` moves `verdict`, `contract` and `checked_at`, never `state`; rewriting a block's text moves neither until it is re-stamped (a stale stamp is detectable: its `checked_at` precedes the document's `generated_at`).

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round107_aifill_prep/checks/check_gs2_validation.py`, 16 arms. At the base: `AIFILL GS-2 ARMS: NO (1 of 16)` (one control arm passes: a block without the key still validates; the fifteen build arms fail). The issuer's reference edit in a scratch copy: 16 of 16, and the 303 contract and grounding tests (`test_contract_grounding`, `test_contract_v2`, `test_contract_orchestrate`, `test_grounding`) all pass with it, so no existing test needs an edit.

**What this cell does not do:** the stamping of the stored documents (the issuer's act at the store write, under its own never-widen pair, `NEVER_WIDEN_ROUND107_AIFILL_95_KEY_STORE_WRITE_COO_HALF_DRAFT.md`); the clearing of "held" (a later 95-key rewrite under its own pair, after the CVO's read is MET); any gateway change.

## 17. ADDENDUM 8 -- ROUND 109 OF WORKSTREAM `AIFILL`: THE FIVE-NEW-NAME REMEDY (CVO row `AMGT_RESAPP-D1-C-S158`, CTO msg 6571), 2026-10-16 ~07:4xZ

Source: the CVO's five-new-name read after the store write, `surprise-channel/adjudications/ADJUDICATION_v135.md` @1f532a2c3b, NOT MET, and its remediation row `AMGT_RESAPP-D1-C-S158` in `REMEDIATION_v46.md` (ARMED, owner `2.0.0_SA_COO~R2`); the CTO's relay (msg 6571): "The AI-fill hold stays. Round 108 carries clause-level support and the cross-block recency rule." The gate counts workstream rounds: `gs-1` took AIFILL 107 and `gt-1` AIFILL 108, so this cell is AIFILL round 109 (project round 108). The CVO drew `NU_US`, `UNVGY_US`, `NG/_LN`, `QXO_US`, `HSBA_LN` by sha256 over 2026-10-16; of 12 filled blocks, two state claims their sources do not carry and one prints a run-together word.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gu-1` | (a) a SUPPORTED sentence must have every number and name it states in its cited source; (b) the cross-block recency pass over the web management blocks (CTO item (g) of 2026-10-14); (c) the folding of zero-width and hyphen characters | worker `~483` | worker, DIRECT-ACT (about 110 product lines plus tests) | LOCAL | `lib/research/aifill/{contract,grounding,orchestrate}.py`, one new test module | FWD-41 hold lift | CVO C-S158, CTO 6571 |

**Chain read:** M = 1, N = 1, cap 8. **The three mechanisms, measured on the CVO's own findings.**
- (a) QXO team_view: the model graded a sentence SUPPORTED on a quote of its FIRST clause; the clause naming a $3 billion raise with Apollo and Temasek is in no fetched page. The existing check proves the quote is in the source, never that the sentence is. The remedy is mechanical and model-free: the source must carry, as whole normalised words, every number (with a following scale word) and every capitalised name (four letters or more, less a short list of openers, months and job-title words) the sentence states; one missing and the sentence is UNSUPPORTED. A false UNSUPPORTED (a source that writes `$3bn` where the sentence writes `$3 billion`) drops a true sentence; a false SUPPORTED shows a wrong claim. The cell takes the first direction on purpose.
- (b) HSBA team_view states a buyback pause (annual results, February 2026) that the page's own thesis_pillars source (interim results 2026, a `$1bn` buyback) contradicts. The CTO's 2026-10-14 item (g), placed on round 107's list and not built. The remedy: after all five blocks are grounded, each WEB management block is grounded once more against its own pages plus up to four pages cited by the other web blocks (reference sources); a reference page can make a sentence CONTRADICTED, never SUPPORTED; a CONTRADICTED sentence is dropped, its record names the contradicting page and quote; no sentence left is a NONE block with a reason; a check that cannot run withholds the text.
- (c) NG/ printed `Pettigrewafter`: `contract.fold_text` drops a non-ASCII character that is not a letter, and a zero-width space between two words is such a character. Measured at the base: `Pettigrew` + U+200B + `after` folds to `Pettigrewafter`, and U+2011 folds `co-founder` to `cofounder` (U+00A0, U+202F and U+2009 are already rescued by NFKD). The remedy: map U+2010, U+2011, U+2012 and U+2212 to a hyphen, and replace a dropped non-letter that stood between two ASCII alphanumerics by one space, except the characters that join a word (U+00AD, U+200C, U+200D, U+2060, U+FEFF).

**FOUR-POSTULATE RECORD (CLAUDE.md rule 24). No value enum, key set or schema is authored:** the sentence verdicts stay SUPPORTED | UNSUPPORTED | CONTRADICTED, the grounding record keys, the block keys and the NONE-block reason class are unchanged; the two new reasons are plain sentences in the existing NONE class. Two meanings move and are stated: (iii) INTENT COHERENCE: a grounding record's `sources` list may now carry pages the block does not cite (reference sources, after the own ones); `citations` stays the list of pages the kept text rests on, and a reference page is never a `used_url`. (iv) STATE COHERENCE: a CONTRADICTED record's `source` index may point at a reference page; the recency pass moves the block's text, record, citations and token count together, in one rebuilt block; it does not move `validation` (stamped later by the store write, never inside a block builder).

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round108_aifill_prep/checks/check_gu1_remedy.py`, 20 arms. At the base: `AIFILL GU-1 ARMS: NO (8 of 20)` (the eight passing arms are controls and two behaviours the base already has). The issuer's reference edit in a sparse scratch tree (`lib/research/aifill/{contract,grounding,orchestrate}.py`, +124 lines, -14): 20 of 20, ruff clean, ASCII, and the 813 existing aifill tests pass unchanged, so no existing test needs an edit.

**What this cell does not do:** the re-run of the affected names and the re-read (the issuer's act after the merge, a spend the CTO sets); the HELD to CLEARED re-stamp; the hold's restore (`NEVER_WIDEN_ROUND108_AIFILL_HOLD_RESTORE_COO_HALF_DRAFT.md`, void until a read is MET); any change to the served API, the gateway or the page.

## 18. ADDENDUM 9 -- THE LIFT SCOPE `AIFILLHOLD` (round 109): THE HOLD REMOVED (CVO `ADJUDICATION_v136` MET, CTO ruling `CTO_RULING_AIFILL_HOLD_LIFT_20261016.md`, msgs 6620 and 6624), 2026-10-16 ~09:3xZ

Source: the CVO's fresh five-new-name read, MET on correctness (row `AMGT_RESAPP-D1-C-S159`); the CTO's ruling: LIFT through the restore never-widen pair, with SAN FP `mgmt_recent` withheld in the same act. The pair: `ledger/NEVER_WIDEN_ROUND109_AIFILL_HOLD_RESTORE_{COO,CTO}_HALF.md` (COO half sha256 `d4281bce...0e05` @247b2f6a4f, CTO half signed, msg 6624). Leg 1 (this seat, DONE and read back, @c7c8c8b7be): the one `SAN_FP_Equity` re-store, `mgmt_recent` as the contract's NONE block. Leg 2 is this scope's one cell.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-ar-8` | remove the one environment entry `AMGT_AIFILL_ROOT` from `opal-amgt-scoped-api` (one targeted `safe-apply` of `module.scoped_amgt_api`) and read back that the stored documents are served | `0.7.0_AE_CloudOps~RA1` | worker (a CloudOps seat) | WORLD (a deploy) | `infra/aws/terraform/harvest/scoped-amgt-api.tf`, the change-management ledger, `.open_deploys/`, the RA1 deliverables folder | FWD-41 hold lift | CTO 6620 |

**Chain read:** M = 1, N = 1, cap 8. **No schema is authored:** no value enum, key set or contract changes; the restore removes a configuration value and the NONE block already exists in the block contract (the CTO confirmed it, msg 6624). **The undoing of `AMGT-ar-7`:** the hold was added by one entry and is removed by deleting it; the stored documents are read by the handler's own reader unchanged.

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round109_close/restore/check_restore_served.py`. At the base (the hold in place, four names captured live): `AIFILL RESTORE SERVED: NO (8 of 16)`; on responses simulated from the stored documents with the capture as the base for every other key: `YES (16 of 16)`; with one served block altered: `NO (12 of 16)` (the negative control). The earlier-serves census (R97, R95, R94) reads YES at the base and is kept as a control.

**What this cell does not do:** any S3 write (leg 1 was the only one); the HELD to CLEARED re-stamp; round 110 (the generic "describes only its source" rule, the pack-restatement and pronoun rules, the SAN naming sentence); any client-facing page (Security Analysis is Opal-internal).

## 19. ADDENDUM 10 -- ROUND 110 OF WORKSTREAM `AIFILL`: THE FRESH READ'S QUALITY ROWS (CVO row `AMGT_RESAPP-D1-C-S160`, CTO ruling `CTO_RULING_AIFILL_HOLD_LIFT_20261016.md` item 2), 2026-10-16 ~09:3xZ

Source: the CVO's MET read (`ADJUDICATION_v136`) graduated three quality findings as INERT (row `C-S160`, `REMEDIATION_v47`): SAN `mgmt_recent` is the model describing its own source, the ZTS and SAN OPAL_SOURCE bios restate the pack passage the page already shows (round-106 rule (e), still not enforced), and the ENEL, TSM and SAN bios open on an unnamed pronoun because the naming sentence was judged UNSUPPORTED. The CTO placed them on round 110, not blocking the lift: (1) a generic rule that a block whose kept text only describes its source is withheld; (2) the three inert rows. The workstream round is 110.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gv-1` | (a) the specifics check must fold diacritics on the source side and the pack text must not be built with escaped characters; (b) a sentence that only describes its source is not kept; (c) an OPAL_SOURCE management bio that only restates the pack passage is withheld with a reason; (d) a management bio that opens on an unnamed pronoun is withheld with a reason | worker `~484` | worker, DIRECT-ACT (about 60 product lines plus tests) | LOCAL | `lib/research/aifill/{grounding,orchestrate}.py`, one new test module | FWD-41 quality | CTO 6620 item (2), CVO C-S160 |

**Chain read:** M = 1, N = 1, cap 8. **The cause of the pronoun-opening bios is mine, found while reading the CVO's rows against the stored documents:** the specifics check of `AMGT-gu-1` compared an ASCII-folded sentence (`Belen Garijo Lopez`, the form every stored sentence has) with a source that carries `Belen`'s accent, so the naming sentence of any bio with a diacritic in the name was withheld, and the pack text reached the check JSON-escaped (`Belén`). Measured with the shipped functions on a synthetic source: `_missing_specifics` returns `['belen', 'lopez']` for both the plain and the escaped source. Mechanism (a) removes that; the pronoun rule (d) is the backstop for a naming sentence withheld for any other reason. Mechanism (b) is a prompt line plus a short phrase guard (`headline`, `says nothing`, `does not mention/name/identify/state/say`, `refers only`, `no mention of`, `nothing about`) because a model-only instruction is not enforceable; the guard errs toward withholding, the direction the CTO and CVO chose. Mechanism (c) is rule (e): every kept sentence of an OPAL_SOURCE `mgmt_bio` having at least 0.6 of its word 4-grams in the pack passage withholds the block.

**FOUR-POSTULATE RECORD (rule 24): no value enum, key set or schema is authored.** Verdicts, grounding keys and block keys are unchanged; the three new reasons are plain sentences in the existing NONE-block class (state coherence: they move `source_class`, `text` and `reason` together in one rebuilt block, and nothing else).

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round110_aifill_prep/checks/check_gv1_round110.py`, 12 arms. At the base: `AIFILL GV-1 ARMS: NO (6 of 12)` (the six passing arms are controls). The issuer's reference edit in a sparse scratch tree (`grounding.py` and `orchestrate.py`, +61 lines, -10): 12 of 12, ruff clean, ASCII, and the 830 existing aifill tests pass unchanged.

**What this cell does not do:** the re-run and the store write of the affected names (the issuer's acts after the merge, each under a metered run and its own never-widen pair); the HELD to CLEARED re-stamp; any change to the served API or the page.

## 20. ADDENDUM 11 -- ROUND 111 OF WORKSTREAM `AIFILL`: THE TRUNCATION RETRY AND THE SUBJECT RULE (CTO msg 6644), 2026-10-16 ~10:3xZ

Source: the CTO's round-111 scope, not blocking (msg 6644): (1) fix the 9 token-limit truncations (raise the limit or split) and retry only the failed blocks; (2) the pronoun rule tests the opening sentence's subject, not just the first word; and, from the CVO's fresh read of the round-110 set relayed by the CTO (msg 6648: correctness holds, row C-S160 NOT met), (3) the AZN and ISRG OPAL bios still restate the pack passage the page shows (rule (e)) and the AZN bio never names Pascal Soriot. Measured on the round-110 set: 12 blocks "could not be produced" (round 109: 9), 9 of them "model answer was truncated at max_tokens" (the web-search draft calls ran at the seam default of 1500; 5 mgmt_team_view, 4 mgmt_recent) and 3 transient API errors; 5 of the 53 kept bios open on "Before ..." and the ZTS bio on "Earlier she ...", which the first-word rule of `AMGT-gv-1` does not catch.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gw-1` | (a) one shared output limit (`contract.WEB_DRAFT_MAX_TOKENS`, 4000) on every web-search draft call; (b) `orchestrate.retry_failed_blocks`: build again ONLY the blocks that failed; (c) the unnamed-opening rule tests the opening sentence's subject (the CEO's name from the served officer list when there is one, else a pronoun-before-name window); (d) `orchestrate.refinish_document`: the same rule, and the restatement rule, applied to a stored document with no model call; (e) the restatement rule also catches a PARAPHRASE of the pack passage (content-word coverage), not only a word-for-word copy | worker `~485` | worker, DIRECT-ACT (about 95 product lines plus tests) | LOCAL | `lib/research/aifill/{contract,orchestrate}.py`, the five `block_*.py` web draft call sites, one new test module | FWD-41 quality | CTO 6644 |

**Chain read:** M = 1, N = 1, cap 8. **The seam default (1500) is NOT changed:** an existing test pins it, and the limit that matters is the draft call's, so the five block modules pass an explicit limit from the one constant. **The retry does not touch what a reader has read:** every block that did not fail comes back as it was, validation stamp included; a retried block comes back unstamped and the issuer stamps it. **The re-check needs no model:** `refinish_document` applies the subject rule to a stored document so the 95 stored round-110 documents can be checked without a re-run (the issuer fetches each name's served inputs, a GET).

**The restatement rule, measured (the reason it is a paraphrase test).** The CVO read AZN and ISRG as restating the pack; the round-110 rule (4-gram overlap of every kept sentence, 0.6) did not fire on them because both bios are paraphrases (4-gram overlap 0.33 and 0.13). Measured on the 16 kept OPAL bios of the round-110 set against their pack passages (`thesis.dossier_fields.management`, read through the served inputs): content-word coverage 0.62 to 0.89 for ALL 16 (AZN 0.62, ISRG 0.71). An OPAL bio can only state what its sources state, so it restates the passage by construction; the rule withholds a bio of six content words or more with at least 0.6 coverage, beside the verbatim test (kept as it was, any size). **The consequence on the stored round-110 set, applied with no model call:** kept bios 53; the subject rule withholds 16 (AZN, ZTS, HSBA, AMD, V, NU and ten more); the restatement rule withholds 11, which is EVERY remaining OPAL bio; 26 stay, all web bios. So no OPAL bio ships while the pack passage exists; the page shows the research team's passage and the officer table. This is what rule (e) says; it is stated here because it is a large change from the round-109 set (71 bios).

**FOUR-POSTULATE RECORD (rule 24): no value enum, key set or schema is authored.** The new reason texts are not new (`UNNAMED_REASON` is round 110's); a retried block is an ordinary block; no verdict, grounding or block key changes.

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round111_aifill_prep/checks/check_gw1_round111.py`, 14 arms. At the base: `AIFILL GW-1 ARMS: NO (5 of 17)` (the passing arms are controls). The issuer's reference edit in a sparse scratch tree (7 source files, +134 lines, -14): 17 of 17, ruff clean, ASCII, the 845 existing aifill tests pass unchanged, and the earlier checks still read YES (GU-1 20 of 20, GV-1 12 of 12; the GV-1 control "a bio in its own words is kept" was amended to a bio with content the pack does not carry, because a paraphrase is now a restatement).

**What this cell does not do:** the retry of the 12 failed blocks, the re-check of the stored set and their store write (the issuer's acts after the merge, each metered where a model runs and under its own never-widen pair); the HELD to CLEARED re-stamp.

## 21. ADDENDUM 12 -- ROUND 112 OF WORKSTREAM `AIFILL`: THE gr-7 WORDING (CTO msg 6706), 2026-10-16 ~13:3xZ

Source: the issuer's DEV page read of the gr-7 panel (AMD_US_Equity, DEV @fc174c69, live served data) and the CTO's ruling (msg 6706): the AI-written row's count "1 from a web search" sits beside the unchanged line "web search results stored for this name -- nothing has been read from this input for this name yet" and reads as a contradiction; reword the AI row's count as "1 cites a web search made when it was written" and leave the stored-search line as is.

| id | cell | slot | class | risk | write set | serves | item |
|---|---|---|---|---|---|---|---|
| `AMGT-gx-1` | the web part of the AI row in `aiFillStatus`: one WEB_SEARCH block reads `1 cites a web search made when it was written`; N above one reads `N cite web searches made when they were written`; the Opal part and every other row are unchanged | ~486 | worker | LOCAL | `portal/src/pages/SecurityAnalysis/components/InputProvenance.tsx` (one file) on a new feature branch `cand/dell1/aifill-provenance-wording` cut from DEV | FWD-41, CVO row C-S146 (a) | CTO 6706 |

**Why round 112:** round 111 already has its one issuance (`AMGT-gw-1`, closed); `to-pipeline-gate` refuses a second order into a round that has one, so this cell opens the next round of the workstream.

**Chain read:** M = 1, N = 1, cap 8. **Plural is the issuer's reading of the CTO's singular wording:** most names carry two to four web blocks, so a count line that only handled one would print "3 cites"; the plural form is the same sentence with the verb and noun in agreement. Stated to the CTO with the cut. **Why a new branch:** `.tools/open-calls.py add --kind approval` refuses a branch that carries commits already on DEV, and gr-7's commit is on DEV (fc174c69); a follow-up commit on `cand/dell1/aifill-provenance` cannot be registered. The new branch carries one commit and one file.

**FOUR-POSTULATE RECORD (rule 24): no value enum, key set or schema is authored.** The row text is presentation of served counts only (C-PRESENTATION-ONLY); no served value is computed or rewritten.

**Check, dry-run at the base and proven satisfiable:** `deliverables/2.0.0_SA_COO~R2/round111_aifill_prep/checks/check_gr7_wording.cjs`, 12 arms (the 11 of `round106_aifill_prep/checks/check_gr7_provenance.cjs` with two web-count expectations changed, plus one arm for the singular). At the base (DEV @fc174c69): `AIFILL PROVENANCE: NO (9 of 12)`, the three wording arms failing. The issuer's reference edit in a scratch tree reads `AIFILL PROVENANCE: YES (12 of 12)` with `bun run typecheck` rc 0. The older gr-7 check reads NO (9 of 11) against the edit, so it is superseded and must not be used as a bar.

**What this cell does not do:** the push of the branch, the approval row, the merge to DEV and the PROD promote (the issuer's acts); the stored-search line; any page other than Security Analysis; the AI fill documents.
