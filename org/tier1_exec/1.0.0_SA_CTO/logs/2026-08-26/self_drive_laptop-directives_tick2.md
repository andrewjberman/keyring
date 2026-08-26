# /self-drive laptop directives — ticks 1–2 (2026-08-26 13:35Z–14:52Z)

**archetype:** COORDINATE
**state:** ARMED · cadence 30m · cron `9dc4dcd3` (session-only; carrier = XXX.md:516 CTO row)

## Scope (per-tick predicate resolution, register authority)

`laptop directives` → **7 of 11 live** [D0 D1 D2 D3 D5 D8 D10] → **13 register members** (+0 claimed;
scan 332 JSONs both ticks, 0 claimed-not-member lag). Device: laptop (path-derived).
Scope is the PREDICATE form per CVO adjudication 72162 — carrier updated @`eb92fd6a87`, broadcast 3/3.

## Calls pitched / verdicts received

- **Tick 1 pitched:** scope re-resolution 5→7 (msg 72159→CVO). **VERDICT 72162: RE-RESOLVE TO 7**,
  amendment (D5+D10 both print UNMEASURABLE), carve-outs (D10-1/2/3 stay at Andrew; no MDPF-path
  invoke during a live acceptance read). **Acts:** carrier rewritten to predicate form + two decayed
  claims fixed @`eb92fd6a87`; broadcast 72163-65.
- **Tick 2 pitched:** none — zero new ADJUDICABLE calls at this seat (every in-scope open item has a
  live owner and a same-day verdict; see scope state).

## Scope state (owners' movement this window, cited not claimed)

| D | state |
|---|---|
| D8 | TO-ACCEPT-0826 EXECUTED by this seat (FAIL-diagnosed, scheduled path exonerated, instance VALID @`02df062ea5`); COO 72211: **holds open → 08-27 13:30Z fire**; key fix P0 at `0.6.2_AE_PartnerETL~A`; **rename-vs-new at Andrew** |
| D1 | Sole blocker RULED (COO 72259): RECON_TOLERANCE form adopted, control/repair independence split, DS lane asked of MSTR — D1 is moving again; D1-i-2 waits for first clean 12/12 |
| D2 | AC1+AC2 closed (COO 72211); AC3 held for emission re-take; WS5 grants descoped (COO 72276); provenance-stamp spec routed (DS~R → COO → me: STRUCTURALLY-INAPPLICABLE vs NOT-DERIVABLE-UPSTREAM) |
| D3 | Advisor-level verdict VENDOR-SIDE confirmed (DS~S 72193 + CVO 72204); my BD_DIM_436 finding amended @`b14184f649` (over-strong clause retracted; two-step Andrew card); producer placement TARGET ruled (runners_49f/ + _code/), EXECUTION held on the LD-0405-class card at Andrew (my 14:51Z reply to COO 72268) |
| D0 | TO three-field schema: CVO REWORK verdict 72233 + COO option-(a) ruling 72239; my 4 landing conditions pre-stated (72249-51); revision at `0.8.0_AE_CloudComp~F` |
| D5 | UNMEASURABLE (deliberately empty, LD-0454) — at Andrew's prioritization word |
| D10 | UNMEASURABLE (empty by design) — D10-1/-2/-3 RESERVED at Andrew |

## Completion test

**NOT DONE — 2 of 13 members complete** (NFRA_DEPLOYCENSUS, ADVI_BDPLAT_RESTORE).
UNMEASURABLE: D5, D10 (member sets deliberately empty — held at Andrew, NOT register defects).
UNREACHABLE-by-driver: none among the 11 active members — all have live owners or lanes this window.

## RESERVED at Andrew (in scope)

'Opal Fixed Income' rename-vs-new (D8, highest leverage) · BD dim-436 two-step read+amend (D2/D3) ·
D10-1 product-vs-firm · D10-2 legacy bd/cot/inf · D10-3 EC2-vs-lambda threshold · D5 prioritization ·
MDPF_CANON §7.2 · MDPF_GLOBAL join-vs-absorb · LD-0405 reading (fabric-class; gates D3 placement execution).

## Fabric notes

- **ANDREW-DIRECT 14:50Z recorded @`28714f7650` + broadcast:** tier-1 seats do not disturb
  `1.0.0_SA_CTO~X` (separate work product). Binds this driver's broadcasts too.
- Non-loop work this window (own lane, full detail in `session_1313Z_acceptance_and_selfdrive.md`):
  acceptance execution; 16-file prompt.md watcher-path sweep (7 lane commits, CVO+COO verified 0/40
  residual); LD-0405 dual-reading finding — my reading on record, conduct rule adopted (check the
  open-card set before remediating a surfaced class).
- MSTR published the 170 → origin/CLOUD @`0eb75b207e`; this session's commits ride integration.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| directives-check.py | `--json`, both ticks | 11 live / LAPTOP 7 / member set + flags |
| claims scan (skill §0.3 form) | PRD-path over org/projects/*.json, both dict/str shapes | 332 scanned, 8 claims, 0 lag, 0 crashes |
| agentbus-sqs.sh device | device guard | laptop (path-derived) |
| to-check.py | tick-1 open-TO frame | 28 in-scope of 95 estate-wide |

state: ARMED — next log at tick 4 or completion.
