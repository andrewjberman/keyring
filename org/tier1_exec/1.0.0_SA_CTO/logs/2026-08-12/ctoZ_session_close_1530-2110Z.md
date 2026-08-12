# CTO~Z session log — OPAL_ANALYST driven to 12/16, three access layers chartered, and five of my own sovereign-facing claims corrected — 2026-08-12 1530-2110Z

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE
**Serial:** `1.0.0_SA_CTO~Z` (lane log in the BASE folder per the site-Z owned-paths convention).
**Prior log:** `2026-08-11/ctoZ_w1_close_instruments_launch_integration_close_1730-1950Z.md`.
**Window:** 28 commits on this lane; ~60 MCP dispatches; 5 Andrew-direct records; 1 security finding.
⚠ **KNOWN GAP, NOT MINE TO FILL:** the 2026-08-12 00:07-07:55Z `~Z` session (~25 commits on this lane)
was never logged. A different instance; I have no context for it and will not fabricate one.

## The arc

**1. Startup into a dead fabric.** Watcher armed (task `bpemm57sx`); `/cygdrive/c` resolved rather than
trusting the doc's hardcoded `/c/`. Found every OPAL_ANALYST seat dead since ~07:55Z. **Cause (MSTR~Z,
measured): a PLANNED N-able RMM restart as SYSTEM at 07:52:45Z** — zero Kernel-Power 41, no crash dump.
**It recurs on the MSP's schedule, on both devices, and nothing respawns seats.** Converted that into a
structural rule rather than a note: **unit granularity is a hazard control**, commit at every increment
boundary. That discipline is why the respawn cost minutes.

**2. Andrew-direct x5, all recorded verbatim + broadcast same turn.**
`@504f4d7ae0` ~1545Z — **site Z is MECHANICAL-WORK ONLY; NFRA_TOOLCHECK moves to the laptop** (c4/c3
ontology needs him hands-on). A routing ruling with a stated mechanism, not a stop.
`@f09cbd13ef` ~1702Z — **three ACCESS LAYERS** + a sovereign-requested read-only gate on `0.0.3`.
`@8205c18a46` ~1948Z — **document-extract GO, SPEC ONLY** (the clause rode *inside* the option).
`@e56e9e2d4c` ~2020Z — **four rulings** (below).
Plus the ~2035Z correction: *"That is a reference, not an array."*

**3. Staffing + driving.** Spawn request to MSTR~Z -> 5 seats (CVO~Z certifier, 0.5.0 + DE~Z authors,
COO~Z driver, CRO~Z). Argued explicitly against adding authors: **the certifier is the bottleneck and
cannot certify its own work**, so a third author lengthens the queue. Held that line all session.

**4. Program result: 12 of 16 units certified**, every one having caught its planted mutant.
CLOSED this window: **W7** (SharePoint reach+registry, 3/3) · **W8** (BBG pipe map, 4/4 + 9/9
negative-controlled, **2 vendor calls, ZERO pulls**) · **W4c-1** ticket-center. **W4b** advanced c11->c17,
frontier 72->47, consumer_set 35/35. **W4c-3** three planes + reconciliation, then a clean wind-down.

**5. The day's real output was defects nobody was looking for.**
⛔ **`opal-ticket-api` STAMPS caller identity and never CHECKS it** — `_actor()` extracts email/userType/
firmId and every use is a label; the only `ConditionExpression`s are state-machine guards; `list_tickets`
applies no firm scoping. **Any authenticated user reads/mutates any firm's tickets.** Read from deployed
bytes (3,838-B zip, 273 lines), **three independent derivations**, one rejected counter-example. Record
`@10d3723054`, scope amended `@ebb401d804`.
⛔ **A live page answers "49 Financial's AUA" three ways** — $1,778,539,360 / $1,778,539,390 /
$1,911,578,939 — and **its own by-architect percentages are computed against the FIRST while printed
beside the THIRD.** Separately: the breakdown sums to 81.3% with its own residual row *inside* that 81.3%,
so **$332,834,180 unaccounted in a table that looks complete.** Routed to the laptop fabric via MSTR~Z.
✅ **`trade-workflow-handler` does authorization properly** (verified principal never the body; fail-closed
with no auth context; approver cannot execute their own approved trade) — **and has ONE invocation in 30
days**, so proven in source, unproven in use. Both halves reported.

**6. The SoD census and the review pass I took.** CVO~Z's census: **9 of 13 certified units were signed by
a certifier who authored cells in the rectangle** — and its reframing is the value: *not* self-passing, but
**in nine units the Plane-B/C semantics were never independently reviewed by anyone** (the author is barred
by K4; the certifier wrote them). **I took the review pass** as the only seat authoring none of those cells.
Unit 1 found **TWO FALSE CELLS in the unit its author called "the wave's control case"** — including an
analyst-facing instruction that would have told a client *"the lookback is not available"* about an artifact
**keyed by lookback**. Depth probe over the other 8: **150 cells -> 1 candidate -> VERIFIES TRUE**, so the
class is **isolated, not systematic**; corroborated independently by CVO~Z's own 507-cell self-audit.

## Rulings issued (PRD `docs/architecture/OPAL_ANALYST_PRD.md`)

| ref | ruling |
|---|---|
| §9.10 | **The two enumeration planes' blind spots INTERSECT** — a zero disagreement set is NOT evidence of coverage. Credit 0.5.0. |
| §9.10.1 | **PLANE D** (served-plane enumeration at rest) is a REQUIRED third plane; it closes the A∩B region. |
| §9.10.2/.3 | One-firm closure **WITHDRAWN** where both firms are in frame -> **the UNION with firm as a declared PER-ENTITY dimension.** |
| §9.10.4 | **Plane D is firm-scoped by construction** — it must declare which firm it enumerated. |
| §9.10.5/.6 | A bound in the prose does not bind the cell · a convention holding for 3 of 4 is a heuristic, and it fails in **BOTH** directions. |
| §9.10.7 | **A readiness join keyed on STATUS cannot see a PROVENANCE hold**; a held measurement does not become unheld by being consumed. |
| §10 / §10.8 | The three access layers · **FIRM ISOLATION as a standing requirement** · the firm axis is NOT the bucket axis · metering is BYTES · his surface list is a REFERENCE. |
| §10.5.1 | **"Part 3" meant two things** (Bloomberg vs document-extract) -> resolved as **W9, SPEC ONLY.** |

Doctrine: `@1726f75c90` (a producer-side timer measures the ARTIFACT; only a consumer-generated status
measures the AGENT) · `@901eb2789a` (**a uniform zero across a set containing one known-true member is a
broken instrument** — five seats, one session). CLAUDE.md: `@ccb6d051e6` (correcting a FALSE sentence I
landed there this morning) · `@61be414e59` (**a law edit has two delivery surfaces and the commit is only
one of them**).

## My own errors, all caught by seats re-measuring rather than accepting my figure

1. **A FALSE SENTENCE IN CLAUDE.md** — I bound "the name exists only as a record of its own nonexistence."
   The key exists in `opal-data-inf`, 324 B. A **firm-scoped absence generalised to nonexistence**, written
   into the law file. Corrected `@ccb6d051e6`.
2. **249 cells** propagated to four recipients as a seat's frontier; the frontier was **75**.
3. **A path-fragment lint** whose two limbs DE~Z falsified before applying either — one **would have deleted
   a finding**.
4. **"72 executing places" -> "1 + a directory name" -> "5" -> 12.** Three wrong magnitudes on one question.
   **I corrected a count by substituting another count instead of decomposing it.** Stopped relaying and
   pointed at the artifact that owns it.
5. **Call-1 recommendation REJECTED** — I recommended bd/inf be one firm with a tenant partition. **Two
   different firms.** The topology was real; the inference was backwards.
6. **"Bloomberg is completely mapped"** — retracted on his challenge. We mapped **the slice we use**, not
   Bloomberg; and no live traversal occurred (transport down since 17:30Z).
7. **A negative control measuring `basename`** — `$(basename $P)` expanded first and clobbered `$?`, so all
   six seats read PERMITTED on a permissions grant over credential-adjacent code. Re-run correctly: scoped.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-state --self-test` + `comp-state` | PASS 3/3, twice | Gate held both /exec-sum runs; drift rows triaged as BM25 lexical false-positives |
| `comp-which` (A.3 exercise) | PASS | 91 of 97 resolve bare; forwarder RAN (own banner), not just resolved |
| `owned-paths-validate.py --check-agent` | PASS after a FAILED first attempt | First invocation put the agent in the YAML slot -> uniform rc=1 readable as "all refused"; corrected |
| `proof-of-spec-check.py` (RAVC-4 on W4c-1) | PASS, rc=0, 7 rows 0 violations | **Negative-controlled myself**: bogus id -> rc=1, no-args -> rc=2 |
| `ssot_validate.py --self-test` | PASS 13/13 | Exercised the M-9 fix on this box; the discriminating case asserts merged CONTENT not rc |
| `bg-concierge-gate` test suite | PASS 34/34 | Andrew's ~1702Z gate ask was ALREADY SATISFIED — rung 2, nothing built |
| `aws s3api head-object` / `s3 cp` (read-only) | PASS | Review-pass grounding: correlations artifact, aum-metrics at 84 nested keys |
| `git merge-base --is-ancestor` | PASS | Discriminated "fix predates the reproduction" — it did not |

**What worked:** exercising rather than reading — the gate suite, the validator self-test and the
proof-of-spec negative control each converted an assumption into a verdict.
**What failed:** three of my own ad-hoc instruments (the agent-in-YAML-slot invocation, the
`$?`-after-substitution control, the camelCase slug generator that mis-mapped 3 of 15 pages in BOTH
directions). All three produced clean, confident, wrong output.
**Gap found:** **no comp-tool answers "is this served-key enumeration CLOSED"** — routed by CRO~Z, and per
Rule 22 a coverage gap is a defect. **It is OFF this device** (tooling is the class Andrew moved to the
laptop), so it routes to MSTR~Z for cross-device carry rather than being built here.

## Blockers

**NONE at this seat.** Two items are AT ANDREW and both are answered or defaulted:
- Firm boundary — **ANSWERED ~2020Z** (two firms). The 78 held cells are unblocked.
- `0.0.3` session-log question — **DISSOLVED by measurement**: BG holds no owned-paths lane and its own
  fence denies all git mutation; its commits carry committer `0.0.0_AB_MSTR` (integrator sweep). No conflict
  with the logging law existed.

## Current State (zero-context handoff)

**PROGRAM: OPAL_ANALYST, 12 of 16 units CERTIFIED.**
APPROVED (11 pages + news): `portfolios` `cma` `positioning` `attribution` `factor-tilts` `valuations`
`correlations` `macro` `market` `security-scanner` `ticket-center` + `news-subsystem`.
**NOT APPROVED (4):** `advisor-intelligence` (W4b, IN FLIGHT at c17 — `0.5.0_AE_OpalETL~Z`) ·
`trade-submission` (W4c-3, IN FLIGHT, handed off INCOMPLETE — three owed limbs re-routed to
`4.0.0_SA_CRO~Z`) · `portfolio-management` (W4c-2, NOT STARTED) · `data-refresh` (W4c-4, NOT STARTED).
**TAIL, resequenced `W5 -> W7 -> W8 -> W6` + W9 parallel:** W7 CLOSED · W8 CLOSED (traverse+read mandate
only) · **W5 has SIX measured preconditions and has NOT started** (per-key expansion · read
`final.certified.json` and refuse on absence · key off `certification.json` verdict never file presence ·
transliterate non-ASCII, 51 emoji · carry each date with a DECLARED KIND AND DURABILITY, **not** stripped ·
resolve corrections by machine-readable precedence) · W6 guardrails LAST · **W9 doc-extract SPEC ONLY.**
**MY OPEN WORK:** the Plane-B/C review pass, **1 of 9 units done**; 8 remain with a sharpened probe. Plus 3
artifacts outside the cache-coherence invariant (no vintage field at all) awaiting a ruling.
**SEATS:** 8 live at window close — CTO~Z, COO~Z (10-min drive loop, scoped), CVO~Z, `0.5.0_AE_OpalETL~Z`,
`4.0.0_SA_CRO~Z`, `0.0.3_BG_BBGTerminal`, MSTR~Z. **`0.1.0_DE_MarketIntelligence~Z` wound down on context
with a verified 92-line handoff — nothing it produced needs re-deriving.**

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Continue the Plane-B/C review pass (8 units). Rule on the 3 no-vintage artifacts.
   Route the enumeration-closure comp-tool gap to MSTR~Z for the laptop.
2. **[0.5.0_AE_OpalETL~Z]** W4b to seal — vintage_grain and producer are the open axes; then W4c-2/W4c-4.
3. **[3.0.0_SA_CVO~Z]** Corrections owed on `/correlations` are LANDED and verified; next is W4b's 78
   now-unblocked semantic cells under the union form.
4. **[4.0.0_SA_CRO~Z]** W9 spec (rung 2 first) -> W4c-3's three owed limbs. **Bloomberg endpoint universe
   is NEW scope from ~2020Z and NOT started.**
5. **[2.0.0_SA_COO~Z]** Keep the scoped drive loop; the push/pull bound is built into the scan.
6. **[ANDREW]** The tickets remediation decision (remedy now SPECIFIED by Ruling 3, with a working
   reference implementation) and the AUA discrepancy, which MSTR~Z carried to the laptop fabric.
