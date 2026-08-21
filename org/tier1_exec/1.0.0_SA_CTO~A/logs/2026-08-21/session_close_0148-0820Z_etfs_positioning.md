# CTO~A session -- ETFS_POSITIONING commissioned, researched, registered, and shipped (2026-08-21 01:48-08:20Z)

**archetype:** MIXED
**secondary_archetypes:** EXPLORE (primary), VALIDATE, SCRIBE, COORDINATE

**Serial:** `1.0.0_SA_CTO~A` · window: whole session (first log; prior entry `2026-08-11/w1b_enrichment_and_divergence_read_0120-0155Z.md`)

---

## Andrew-direct received + recorded (three, same terminal, all same-turn recorded)

1. **~02:1xZ** -- commission ETFS_POSITIONING: fold an ETF view onto the Positioning page, same
   shape, DIVZ/IDVZ/PFDE/PFOE instead of the five models. Four steps: AJ's daily email; what
   `opal-data-etfs` already gives us; atom-decomp the exact page shape; residue -> Bloomberg via
   MSTR -> MSTR~Z. VERBATIM: *"There is virtually no frontend work here involved aside from a clever
   toggle... The real work will be procuring the data to be able to deliver that same shape."*
2. **~02:5xZ** -- check the snapshots; **characteristics are a declared Bloomberg dependency**
   (*"clearly nobody has access to the characteristics, but that's fine, as long as we have the
   shape, we can get this done through Bloomberg"*); hand the directive to SiteZ + alert MSTR.
3. **~05:5xZ** -- **REVERSE the placement**: *"it probably makes more sense to decidedly own it here
   and just have MSTR~Z specifically operate on a defined deliverable."* Plus: read Yang's actual
   `/terminal-upload` Bloomberg scripting for the model Positioning shape incl. time-span, and
   reappropriate it for the ETFs.

Durable records: PRD s.0 / s.0.1 / s.6.3a. Broadcast: MSTR, COO, base CTO (see MCP note below).

## Commits (this author line, this window)

| commit | UTC | what |
|---|---|---|
| `e0c7276d00` | 02:44Z | ETFS_POSITIONING registered -- PRD + Bloomberg ask + project JSON + REGISTRY row |
| `1575dfab1e` | 03:12Z | snapshot check closed + characteristics ruling + SITEZ placement + D4 identity |
| `bfda227643` | 03:30Z | correction: a FALSE `Z` in my own committed record |
| `12c6a5e1b6` | 05:53Z | registry row -- comp-state true positive, row was 3 commits stale |
| `2a2da42e3f` | 08:03Z | the actual Bloomberg field spec from Yang's code + ownership reversal (**UNPUSHED**) |

Also landed by MSTR on my specification: `e4d002af41` (D4 row -> SITEZ; now needs a second flip).

## The findings, with denominators

- **AJ's US Bank EagleSTAR feed covers PFDE + PFOE ONLY** -- the file states its own denominator,
  `Fund List` sheet `Grand Total : 2`. Exactly the two funds we already had. **It does not close the
  gap that motivated the project.** Four attachments staged to SharePoint `ETF/EagleSTAR Samples/`
  with sha256 per file.
- **Andrew's weighted-holdings hypothesis CONFIRMED by exercise:** `silver/holdings.weight_pct`
  already exists and sums **99.99 (PFDE) / 99.98 (PFOE)**.
- **DIVZ/IDVZ constituents have never existed in the estate.** All 69 holdings files downloaded,
  every row scanned: **7,550 rows, `source='filepoint'` 7,550 of 7,550, DIVZ 0, IDVZ 0**, positive
  control PFDE=5,920. Cross-tree, each tree named: `opal-data-assets/trueshares/` 370 objects,
  **0** keys matching "holding" vs positive control **220** "netassets". Snapshots (70 objects) are
  **fund-level only** -- 4 records, 2,876 B, no constituent array.
  **Mechanism from the producer's own snapshot note:** filepoint ships an `ETF_Holdings.csv`;
  TrueShares ships only a netassets HTML page. A source never wired, not a pipeline dropping rows --
  agreeing with base CTO's deployed-bytes D4 finding from the data side.
- **The Positioning shape pinned on the SERVED artifact:** 8,150 B gzip / 73,487 B decompressed,
  **two** live holdings forms, `returns{1D..1Y}`, null tolerance already 59/110 on `beta`.
  **The page README is materially drifted** (claims 35KB; documents a `components/` dir, `DurationTab`
  and `AttributionTab` that do not exist; describes one of the two holdings forms).
- **Yang's Bloomberg pull FOUND and it is on this device** -- the live project is OneDrive-synced,
  not terminal-only. `dc_return` {PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS} + `dc_characteristic`
  (9 fields), `date_end = today+BDay(-1)`, `date_start = date_end+YearEnd(-6)` = **~6 years daily**.
  **PROVEN to be the Positioning source: 7 of the 9 `dc_characteristic` KEYS are verbatim field names
  in the served `current_holdings[]` rows.**
- **THE GRAIN CHANGES (key engineering finding):** model books hold FUNDS, ETF books hold SINGLE
  STOCKS, so 4 of 9 characteristic fields are fund-only and return correctly-empty on a stock.
  A naive re-point reads as a Bloomberg failure and is a category error.
- **Frontend correction:** `'UST'` is hardcoded in **5 files** under `portal/src/pages/Positioning/`;
  the "clever toggle" needs one book-set source first.

## Errors I made, caught, and corrected (all self-disclosed)

1. **ALL FIVE of my MCP sends went out SUBJECT-ONLY.** `send_message`'s parameter is `body`; I passed
   `message=`. Silently dropped, and the tool returned "Message delivered" every time. **I believed I
   had satisfied the record+broadcast law on an Andrew-direct and had not** (~26 min). Caught by MSTR
   (its subject promised a spec the body lacked) and base CTO. All resent + **verified at the
   delivered artifact**. Rule 22b names the exact oracle I trusted and forbids it.
2. **A FALSE `Z` in my own committed PRD** -- "2026-08-20 ~22:0xZ" was local EDT, wrong by 4h AND one
   calendar day, on a sovereign instruction's timestamp. Caught by applying the CLAUDE.md retrieval
   clause that landed mid-session. **Residual: `e0c7276d00`'s SUBJECT still carries it and is
   immutable (NEVER#7) -- the file is right, the subject stays wrong, no third source.**
3. **"Holdings come from YCharts templates"** -- wrong framing, Andrew corrected it. The Positioning
   data is Bloomberg; the Excel is our own model composition (Date/Ticker/Weight), **weights only**.
   Load-bearing: weights are ours, characteristics are Bloomberg's.
4. **A worthless gate test** -- ran `owned-paths-check.sh` with argv to see if it would refuse me; it
   reads staged files, so both the negative test and the positive control returned rc=0. **An
   instrument that could not have failed proves nothing**; went by the declared rule and said so.
5. **A false-negative in my own verifier** -- grepped a phrase spanning a line wrap on a 3,617 B
   message and read EMPTY. The byte count contradicted it. Nearly resent an already-delivered message.
6. **`--since` on `git log` dropped 3 of my 5 commits** while building this log -- local-date
   filtering, the same cross-midnight class as (2). Widened and re-derived.

## MCP traffic

~14 messages handled; 10 acked (64197, 64207, 64245, 64256, 64264, 64266, 64277, 64337, 64345, 64667).
Significant: **shipped the bounded deliverable to MSTR~Z over agentbus** (MessageId
`fe025fca-5e73-46e6-8d41-b100b95a4dd7`, 6,184 B) -- SENT confirmed, **NOT delivered until ~Z acks**;
D4 row specification to MSTR (landed) + the second flip (pending); push request for `2a2da42e3f`;
COO confirmed **no decomposition owed**; routed MSTR's CLAUDE.md landing ask to base CTO (addressed
to BASE_EXEC, not my lane -- not mine to self-adjudicate).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | routed the opal-data-etfs question | PASS -> `comp-estate` |
| `comp-estate` | `--list`, `positioning` | PASS -- found the served thread + producers |
| `comp-find` | `PORTFOLIO_ORDER`, `save_email_attachment_to_site`, `--name` x3 | PASS, denominators + bands printed |
| `comp-state` | `--self-test` then `--project` + full | **PASS 4/4**, then a **TRUE POSITIVE on my own registry row** |
| `.tools/to-check.py` | `--all --assignee` x2 | PASS -- 0 TOs at this lane |
| `audit-archive-invoker` | startup A.2 | rc=0, 0 findings |
| `owned-paths-check.sh` | negative + positive control | **UNINFORMATIVE** -- reads staged files, not argv |

**What worked:** `comp-state`'s self-test gate then its report -- it caught a real 3-commit drift in
my own record that no amount of re-reading my summary would have surfaced. **What failed:** the
owned-paths argv test (see above). **Gap found:** `send_message` returns a success receipt on an
empty body -- gate candidate proposed by 0.7.0, seconded by base CTO and MSTR; I proposed dropping
the long-subject conjunct from its trigger, since my shortest-subject send was equally empty.

## Blockers

**NONE.** Nothing at this lane is blocked or waiting on another agent.

## Current State

`ETFS_POSITIONING` is a registered, active project (`org/projects/ETFS_POSITIONING.json`), macro
ETFS, Phase 0 research COMPLETE, **build NOT authorized**. It is **directive D4** ("ETF positioning
variant"), not a new directive. Artifacts: `docs/architecture/ETFS_POSITIONING_PRD.md` (the whole
picture; s.3.3 the data census, s.4 the shape rectangle, s.6.3a the Bloomberg spec, s.6.3b the grain
finding, s.9 placement) and `docs/architecture/ETFS_POSITIONING_BLOOMBERG_ASK.md` **v2** (the bounded
work order). Registry row current as of `12c6a5e1b6`.

**Ownership: LAPTOP fabric.** Site Z holds ONE bounded pull, shipped over agentbus.

⛔ **`2a2da42e3f` IS NOT ON origin/CLOUD** (local 4 ahead; push is integrator-only). **A site-Z pull
right now returns the SUPERSEDED v1 ask.** This is why the agentbus message carries the entire spec
inline and warns them off the repo copy. Push requested of MSTR.

## Next Steps

- **[ANDREW]** The one sovereign call: ship two full books (PFDE/PFOE) + two fund-level-only shells
  (DIVZ/IDVZ), or hold the page until DIVZ/IDVZ constituents exist.
- **[0.0.0_AB_MSTR]** (a) push `2a2da42e3f`; (b) the D4 SECOND placement flip, SITEZ -> laptop-owned
  with a scoped site-Z execution leg (cells specified in my 0804Z message).
- **[0.0.0_AB_MSTR~Z]** ack `fe025fca-5e73-46e6-8d41-b100b95a4dd7` and run the bounded pull.
- **[1.0.0_SA_CTO]** MSTR's CLAUDE.md landing ask (still uncommitted in MSTR's tree) -- base-exec's,
  free to be refused as accretion.
- **[LAPTOP, unassigned]** unify the 5 hardcoded model-list sites; Rule-24 four-postulate test on the
  ETF `sub_asset_class` vocabulary (a stock's GICS sector is a different GRAIN from a duration
  bucket); decide the `TS_HOLDINGS_ENABLED` wiring vs Bloomberg route.
