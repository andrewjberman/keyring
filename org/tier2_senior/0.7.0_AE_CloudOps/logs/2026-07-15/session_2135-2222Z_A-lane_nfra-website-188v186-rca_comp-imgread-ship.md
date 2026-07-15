# Session 2135-2222Z (~A lane) -- NFRA_WEBSITE .188-vs-.186 RCA (photo-parse misread CONFIRMED) + comp-imgread canonized

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.7.0_AE_CloudOps~A | **Session:** 2026-07-15 21:35Z start (fresh lane session) | **Window:** session start -> 22:22Z

## What happened (Andrew-direct tasking, mid-startup)

Startup per XXX.md completed (registered ~A PID 7656, Monitor b0ypvrq6b armed, zero crons,
LD-0290 serial file written, /cloud-ops loaded). Mid-turn Andrew-direct: work NFRA_WEBSITE,
check Patricia's recent message, explain why we told her a number ending in 8 when it was
actually 6 (suspected photo parsing). Verbatim recorded + broadcast same turn per protocol.

### 1. RCA: photo-parse misread CONFIRMED (deliverable @ bbb575f3b)

Our 20:29:16Z email to Patricia (TWLC) quoted the opalinvest.com apex A record as
`185.230.63.188`; the row is `185.230.63.186`. Grounded on FOUR independent axes:
- Sent mail body (m365 gateway): `.188` stated as the row-identifier.
- Live DNS (8.8.8.8 + authoritative ns47.domaincontrol.com): apex = .186/.107/.171; no .188.
- Patricia's GoDaddy screenshots read at the PIXEL level (saved server-side to SharePoint
  OpalCapital/Website/DNS_VERIFY_20260715/, rendered in the authenticated Playwright browser):
  25-record zone, THREE apex A rows (.107/.171/.186), zero .188.
- Estate: comp-grep `185\.230\.63\.188` = 0 matches / 22,119 files (denominator printed).
Provenance (audit lake s3://opal-mcp-audit/audit/dt=2026-07-15/): search_email 20:22:59Z ->
read_email 20:24:10Z -> create_draft 20:26:00Z (master_admin) -> sent 20:29:16Z. The draft
carries screenshot-ONLY details (1-hour TTLs; row position vs the NS rows) that contradict
estate records (~86400s) -- the drafter read the image; the trailing 6 flipped to 8
(closed-glyph vision confusion on a downsampled 2940x1912 screenshot). No client damage:
Patricia self-corrected and completed the TTL change; go-live call Thu Jul 16 4:00pm ET.

### 2. Collateral actionable CLOSED BY MEASUREMENT

Concern: zone has THREE apex A rows; Patricia confirmed "both of these" (one A + www CNAME)
-> .107/.171 TTLs unverified. Measured at the authoritative NS: apex A RRset = ALL THREE
values at ttl=600; www CNAME ttl=600 (RRset shares one TTL -- the three UI rows are one set).
The 10-minute flip/rollback window for Thursday is REAL. COO's deadlined board item closed
with this evidence (RAVC closed 21:55Z); no email to Patricia needed.

### 3. comp-imgread canonized (Andrew-direct follow-on; @ 5861a974f)

`.tools/comp-imgread <image> [--crop|--grid|--scale|--out]` -- native-resolution region tiler:
60px seam overlap (digit strings never split), LANCZOS magnify to ~1500px long side (cap 4x),
guarded tesseract second channel (absent on this box -- printed, never silent), hypothesis
banner on every run, RUN-IMGREAD rail log. EXERCISED BEFORE TRUST: negative control (missing
file -> loud rc=2); positive control on the ACTUAL incident screenshot (at 2.08x the .186
trailing 6 is unambiguous). py_compile + ruff py39 clean. Registered: comp-coverage-map
meta_tools (vision-primitive, routable:false) committed; graph-call-manifest exclusion line
EDITED IN WORKING TREE but ANY_EXEC lane-held (owned-paths gate correctly blocked AE author)
-- RAVC-1 to CTO 22:11Z to land it under his line. manifest-check completeness PASS on the
working tree. Memory updated: feedback_photo_parsed_numbers_are_hypotheses_ground_before_outward_quote
(two-step rule: comp-imgread tiles, then ground on live state before outward quote).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-grep | `NFRA_WEBSITE` / `patricia` (2 runs) | PASS | located PRD, TO-1/TO-2, Patricia IAM/WP-admin context |
| comp-grep | `185\.230\.63` estate trace | PASS | Wix IPs .107/.171/.186 consistent across RUNBOOK/tls-cutover/TOs |
| comp-grep | `185\.230\.63\.188` | PASS (0 hits) | THE decisive absence: 0/22,119 files, denominator printed |
| comp-grep | `TTL to 600` | PASS | RUNBOOK step-7 located; no draft provenance in repo |
| comp-manifest-check | `completeness` (pre + post registration) | PASS | registration invariant green with comp-imgread excluded-with-reason |
| comp-imgread | negative + positive control runs | PASS | new tool exercised on the incident artifact before trust |
| comp-pulse / comp-surface-check | auto in safe-commit (3 commits) | PASS/HOLD-heeded | risk-reflex HOLD on graph-call-manifest.yaml -> routed that file to CTO lane instead of forcing |

What worked: comp-grep's printed denominator made the 0-matches claim citable; the owned-paths
gate + risk-reflex HOLD steered the manifest edit to the correct lane. What failed: bare
`comp-manifest-check` (no subcommand) prints help -- cost one retry. Gap found: no comp tool
reads image content (closed this window by shipping comp-imgread); m365 gateway lacks an
attachment->local download tool (flagged to CTO, gateway lane).

## Deployment Sequence + Verification (AE)

No AWS deploys this window (no TF, no Lambda, no EC2). Ships were repo-tooling commits:
- bbb575f3b RCA record; 5861a974f comp-imgread + coverage-map (both safe-commit, my author).
- Verification pasted evidence: nslookup authoritative output (apex A x3 ttl=600, www ttl=600),
  comp-imgread positive-control tile read, manifest-check `registration-invariant PASS ...
  (tools_index 58 + excluded 15 + entries-tools 60)`.

## MCP traffic

7 significant: Andrew-direct record broadcast x3 (COO/CTO/MSTR, 21:52-21:53Z); COO ACK received
(deadlined the TTL item); my CLOSED-BY-MEASUREMENT reply to COO (21:55Z); RAVC-1 to CTO
(manifest landing + CLAUDE.md table-row candidate + gateway gap, 22:11Z).

## Blockers

None. OPEN (not blocked): RAVC-1 at CTO -- graph-call-manifest.yaml comp-imgread exclusion
line sits in the shared working tree awaiting his author (D6 invariant is working-tree-green,
committed-state-red until landed).

## Current State (zero-context handoff)

- NFRA_WEBSITE: staging live at https://new.opalinvest.com; apex + www TTLs measured 600s at
  ns47.domaincontrol.com; go-live call Thu 2026-07-16 4:00-4:30pm ET (Patricia/TWLC + Andrew).
  Cutover = replace the THREE apex A rows (.107/.171/.186, one RRset) with 18.208.18.213 per
  infra/website/RUNBOOK.md; rollback = point back at the Wix IPs.
- RCA record: org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_WEBSITE_DNS_IP_MISQUOTE_FINDINGS_20260715.md @ bbb575f3b.
- New tool: .tools/comp-imgread @ 5861a974f (usage: comp-imgread <image>, then Read each tile).
  Screenshots preserved: SharePoint OpalCapital / Shared Documents / Website/DNS_VERIFY_20260715/.
- Pre-existing ~A queue unchanged and event-gated: tonight 22:00Z ETF fire -> cell-3 swap +
  orion resize + batched ETF notification rules (CTO tonight-clean word); DC1/DC2 crawl TOs
  pending; EC2 gold-runner box apply gated on CTO AM GO.

## Next Steps

- [1.0.0_SA_CTO] land the working-tree graph-call-manifest.yaml comp-imgread line (RAVC-1
  22:11Z); rule on the CLAUDE.md Compiler Tools table-row candidate + m365 attachment-download
  gateway gap.
- [0.7.0_AE_CloudOps~A] Thu go-live support if called: the flip is 3 A-row edits, 600s TTL,
  RUNBOOK steps 8-12; tonight's 22:00Z event queue stands.
- [any agent] reading digits off a screenshot: comp-imgread first, ground on live state second.
