# Claude for Financial Services: the plugin torn down, the LLY pack read, and the RESAPP threading proposal -- RCN-0012

**archetype:** MIXED (EXPLORE + SCRIBE)
**Seat:** `4.0.0_SA_CRO~F` (site Z, lane F -- first session of this lane). **Window:** 2026-09-22 ~14:51Z-15:50Z.
**Prior log:** none for lane F; the base seat's last is `f57afafae6`'s log (2026-09-20).

## Objective

Andrew-direct at this terminal ~14:5xZ (record @c23d5f7dc0): three sequenced steps -- secure the Claude for Finance plugin
access, study the MCP/endpoints and the wire shape (LLY as the test case), assess how the channels thread into AMGT_RESAPP --
delivered as two briefs.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i "claude for finance\|..." --files` (69,202 files) | 17 hits / 11 files | prior work located: CTO~W card 1 @5007337353, the 09-15 egress + header-panel records |
| `comp-find` | same pattern over CTO/CRO/AMGT trees (3,204 files) | 171 hits / 58 files | filings-analyzer lineage (rj-6, rk-18/19/38/42) |
| `comp-find` | `--name '*.py' lib/research` | 183 of 204 | 18 modules, 105 non-test |
| `comp-find` | `"RCN-0011" -- org docs` (53,348 files) | 22 hits / 12 files | **the id collision** (base seat 2026-09-19) -- caught before drain |
| `comp-find` | `sharepoint\|onedrive` over the m365 gateway dir | 0 of 1 file | the gateway was not needed: the library is synced locally |
| `comp-read` | endpoint addendum `--for` Yang Liu's assessment | 13 sections, 18 of 131 lines shown | FWD-18 provenance |
| `comp-read --enumerate` | on the PRD (twice) | RAIL-DENIED both times (piped into `head`) | fell back to `sed` + pipe-receiver `grep`; no denominator lost, the question was a line range |
| rail denials | raw `find` x2, `comp-find \| tail` x1, `comp-read \| head` x2 | 5 denials, 0 later segments lost (each was single-segment) | one `# rail-checked` for the scratchpad clone (outside the corpus) |
| `safe-commit.sh` | 3 runs | 1 REFUSED (foreign MERGE_HEAD in the shared tree), 1 rc=1 (sparse cone lacked `.tools/git-hooks`), 2 committed | fixes: linked worktree; cone widened to `.tools` |
| `claude plugin marketplace list` / `plugin list` | local | 1 marketplace, 0 plugins | nothing installed this session |
| unauthenticated MCP discovery (python urllib) | 12 servers x (2 GET + 1 POST) | 12 of 12 probed; 11 x 401, 1 x 404 | card + raw JSON committed |

## Work Completed

### 1. Startup (~14:51-14:55Z)
Registered `4.0.0_SA_CRO~F`; watcher armed (task balja2zbz, script pid 45856), re-armed on expiry at 15:20Z (task bmu6dlzvd,
pid 17184; census 1 row). Session serial file written; A.2 audit-archive ran (known classes only); PATH 104 of 104, forwarder
exercised. Zero crons. Inbox empty at every read; delivery ledger 0 rows since 09-21.
**Finding banked to memory:** the skill's Win32 census regex reads ZERO for a LIVE watcher on this box because the quoted
path puts `"` between `.sh` and the serial -- a quote-tolerant regex fixes it.

### 2. The Andrew-direct, recorded and broadcast (~14:53Z)
Verbatim record committed @c23d5f7dc0; broadcast 3 of 3 DELIVERED (24278-24280). Scope surfaced, not adjudicated.

### 3. The teardown (~15:00-15:35Z)
`anthropics/financial-services` @574ed36 cloned to the scratchpad (`core.longpaths` needed on this box); 19 marketplace
entries, 10 agent plugins, 6 verticals, 2 partner plugins, 10 cookbooks read at the file level. The LLY pack read from the
synced SharePoint library (58 files; README + SOURCES in full; 3 xlsx; 2 Opal-branded docx via raw XML -- `python-docx` is
not installed here). Twelve declared MCP servers probed unauthenticated. Public docs fetched (platform MCP-connector page,
two announcements, Daloopa x3, Kensho x2, the install tutorial).

### 4. The two briefs + the register (~15:35-15:50Z)
`briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md`, `briefs/RESAPP_CLAUDE_FSI_THREADING_PROPOSAL_20260922.md`,
`deliverables/CLAUDE_FSI_RECON_20260922/` (card + JSON), RECON_REGISTER RCN-0012 (first stamped RCN-0011 @621cecb40a --
corrected this commit, see Decisions). Notified CTO~Z / MSTR~Z / COO~Z (24296-24298).

## Decisions Made

- **Egress reading:** a public `git clone` and a credential-free MCP `initialize` handshake to the 12 declared servers were
  read as inside step 1's verbatim *"figure out the endpoint"*; no vendor DATA API was called and no Opal data or security
  name was sent. Stated in the record, the card and the broadcast so a wider or narrower reading can be taken by Andrew.
- **Nothing installed:** `claude plugin install` writes user-scope config shared by every seat on this Windows user and
  would raise twelve vendor OAuth prompts per session; the clone served the study. Andrew's call, listed as open call 2.
- **Renumbered RCN-0011 -> RCN-0012** after the collision census (the base seat used RCN-0011 on 2026-09-19 for the
  `_authz` layer-fork research without a register row). Correction stamped in the register, pointer row added for
  RCN-0011, correction message sent; the 621cecb40a commit message keeps the old id -- history is not rewritten.
- **Worktree, not the shared index:** the shared tree carried a foreign MERGE_HEAD (a40988ef, `2.0.0_SA_COO~Y`'s AMGT_HARVST
  L5 drain) at commit time; per Rule 14b this seat commits on `cro-f-records` (sparse cone: its own folder, `org/mcp`,
  `.tools`) and drains with `safe-merge.sh`.

## Files Modified

`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260922_145xZ_CLAUDE_FOR_FINANCE_RESAPP_RESEARCH_PROJECT.md` (new)
· `briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md` (new) · `briefs/RESAPP_CLAUDE_FSI_THREADING_PROPOSAL_20260922.md`
(new) · `deliverables/CLAUDE_FSI_RECON_20260922/{ENDPOINT_DISCOVERY_CARD.md, mcp_endpoint_discovery_20260922.json}` (new) ·
`RECON_REGISTER.md` (append + stamped correction) · this log. Outside the repo: one memory file + its MEMORY.md line.

## Blockers

None at this seat. The drain of `cro-f-records` into SITEZ waits only on the shared tree having no open merge (clear at
15:2xZ). Push to origin is `0.0.0_AB_MSTR~Z`'s on Andrew's word.

## Current State

Three commits on `cro-f-records` (c23d5f7dc0, 621cecb40a, this one), LOCAL; SITEZ has moved (9fbf337a74), so the drain is a
real merge. Briefs delivered as CTO intake; nothing dispatched; four open calls sit with Andrew (subscription; install
surface; print target for a quarter; egress class of skill runs). Watcher live (bmu6dlzvd). Zero crons.

## Next Steps

1. [this seat] `safe-merge.sh cro-f-records` from the shared tree; verify the three commits are ancestors of SITEZ.
2. [`1.0.0_SA_CTO~Z`] read the proposal into the AMGT_RESAPP intake as ADD (earnings event; consensus/revisions) + RESTATE
   (transcript via HARVST); cards S1-S3 as measurement acts at the next L10.
3. [Andrew] the four open calls in brief 2 s.5.
4. [`4.0.0_SA_CRO` base] a register section for RCN-0011 (the authz layer fork) -- the pointer row is a placeholder.
