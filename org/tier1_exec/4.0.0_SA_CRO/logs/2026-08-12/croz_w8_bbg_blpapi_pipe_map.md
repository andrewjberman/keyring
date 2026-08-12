# 4.0.0_SA_CRO~Z — 2026-08-12 — OPAL_ANALYST.W8 BBG blpapi pipe map

**archetype:** EXPLORE

Session spawned ~1705Z by `0.0.0_AB_MSTR~Z` on `1.0.0_SA_CTO~Z`'s request, under Andrew-direct
~1702Z @`f09cbd13ef`. Mandate: map the BBG blpapi pipes — what is served where and how — **by
traversal and read only. Downloads expressly forbidden. Quota-sized asks only.**

## Startup
`/watcher` armed (Monitor `bw0s0an45`, confirmed running). Registered PID 18552, identity clean —
no conflict, serial absent before this session. **A.3 PATH: 91 of 97 comp-tools resolve bare**, and
the mandatory EXERCISE line passed (a forwarder RAN, produced its own banner — resolution is not
execution). Owned-paths hook already wired. `to-check --all --assignee 4.0.0_SA_CRO` -> **0 TOs**;
the W8 TO had not landed. Flagged it to MSTR~Z and started anyway — Andrew's word is the
authorization; the TO documents work rather than permitting it. TO subsequently landed @`f917c0786b`
and CTO~Z confirmed the sequence was correct.

**Watcher-skill path defect (not fixed, not mine):** the skill and `org/XXX.md` both hardcode
`/Users/AndrewBerman/Desktop/ajb_workspace`. This box is `/cygdrive/c/Users/Opal Bloomberg/...`.
I resolved the real path and matched all six live sibling watchers. A wrong prefix arms NOTHING and
still returns a task id.

## Work — five increments, committed at every boundary
| Inc | Commit | Content |
|---|---|---|
| 1 | `52f215db0f` | Ingress: services, request types, session openers, transport |
| 2 | `8c5d1c5674` | Request universe + the BBG-origin join over served surfaces |
| 3 | `2e679c3b8c` | Live transport reading + sized-pull menu |
| 4 | `750b3bb5d2` | **Self-correction**: mixed-grain denominator + unclosed enumeration |
| 5 | (this) | Registry + unverified-premise register |

Boundary-committing was mandated because the box died at 07:52Z on a planned N-able RMM restart and
nothing respawns seats. It recurs on the MSP's schedule.

## What the work actually added
The estate already had a probed service map (`NFRA_BBGMCP_PRD`) and a field-grain lineage map
(`yang-pipeline-lineage-map`, 17 artifacts). **Build-ladder rung 2: I reused both rather than
re-deriving.** The gap was that the lineage map *starts* at `data.pkl`. W8 supplied the missing
upstream segment — 3 `HistoricalDataRequest`s, 165 identifiers, 22 categories, field vocabulary
enumerated — and **joined** it: 14 of 19 served keys are Bloomberg-origin, rendered as per-page
blast radius.

## Findings
1. **The egress line belongs on the CALL SHAPE, not the tool name.** `reference_data` sits on the
   permitted side and can still harvest at N securities x M fields, iterated; a name-based rule
   reads GREEN on that. Found in my own authorization before making any call. Adopted verbatim by
   CTO~Z into PRD §10.3 and into the TO under my credit.
2. **The only entitlement discriminator is itself a pull**, so I did not run it, and did not
   substitute `bloomberg_health` for it.
3. **Live DAPI finding** — `health` ok:false twice, no listener on 8194 across 3 probes, `bbcomm`
   alive. Routed to `0.0.3_BG_BBGTerminal`; **deliberately not called an outage** (07:00 run
   succeeded end-to-end, portal correctly serves T-1). BG re-measured independently and **confirmed
   it**: layer-1 `IO_ERROR`, bbcomm restart eliminated, network path open, escalated to Andrew
   (MFA-gated). My reading was a true alarm.
4. **BG runbook prose contradicted its own table** about `bloomberg_health` — and the prose half is
   what reached me at spawn, so I partly talked myself down from a true signal. Sent as a
   contradiction rather than editing their file; they corrected it and source-confirmed my
   hypothesis (health is blind to LOGIN STATE, not to transport).
5. **SELF-CORRECTION, prompted by COO~Z:** my "12 of 17" was a **Rule-24 same-grain violation** —
   rows counting 1 key, 3 keys, and 79 files on one axis — over an inherited row-count I read as a
   key-count. Corrected to **14 of 19** at key grain. Blast-radius verdicts unaffected; the error
   was in the counting axis, not the finding.
6. **The enumeration is not closed.** Live served keys sit outside the inherited map
   (`json/macro/macro_data_fred.json`, 1d old). And a **live same-leaf-name twin**:
   `json/valuation/` (LIVE, this morning) vs `json/valuations/` (~229d, dormant) — Rule 25's exact
   hazard, dormant-because-KEY-MIGRATED. **Recorded; nothing proposed. Not a deletion warrant.**

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `comp-find "blpapi"` | 53 hits / 25,663 files, bands DEF=6 SURFACED=21 DOC=26 — located the 3 in-repo session openers |
| `comp-find` | `comp-find "//blp/"` | 35 hits — surfaced `NFRA_BBGMCP_PRD` and its openService-probed service table (build-ladder rung 2) |
| `comp-find` | `comp-find "model_portfolio_benchmarks"` | 565 hits — resolved the served key to its producer Lambda |
| `comp-find` | `comp-find "yang-pipeline-trigger"` / `"YangDataPipeline"` | 399 / 320 hits — surfaced `yang-pipeline-lineage-map.md`, which made re-deriving the downstream map unnecessary |
| `comp-which` | `comp-which "how do I grep the repo"` | A.3 EXERCISE — forwarder RAN (own banner), not merely resolved |
| raw `aws s3 ls` | `# rail-checked:` marked, twice | denominator + successor discrimination on served keys. **Gap: no comp-tool answers "is this served-key enumeration CLOSED"** — `comp-freshness` keys on registered entries (these are unregistered) and `comp-estate` served names are under the CLAUDE.md PC-003 accuracy warning, so neither could be the corroborating plane. Recorded as a coverage gap per Rule 22's "a comp-tool coverage gap is a DEFECT" |

**Denominator discipline:** every count in the deliverable carries what it is out of and what its
instrument is blind to, per MSTR~Z 170828Z. `--query length()` was never used on a paginated call;
the 963-key listing was materialised and counted client-side.

## Vendor egress — the number that matters
**Total Bloomberg calls this session: 2, both `bloomberg_health`.** Zero pulls. Zero downloads.
A sized-pull menu was **offered with exact numbers and my recommendation was to run none**, which
CTO~Z pre-declared a full PASS rather than a shortfall.

## Open / not mine
- Increment 3's pull menu stands unexercised pending Andrew's word (egress-widening goes to him
  directly, never as a relay summary).
- DAPI recovery is `0.0.3_BG_BBGTerminal` + Andrew (MFA). Next scheduled pull 2026-08-13 07:00 ET.
- The unclosed served-key enumeration and the `valuation`/`valuations` twin are recorded for
  CTO~Z's routing. **No act proposed on either** — moving a served key is NEVER#3.
