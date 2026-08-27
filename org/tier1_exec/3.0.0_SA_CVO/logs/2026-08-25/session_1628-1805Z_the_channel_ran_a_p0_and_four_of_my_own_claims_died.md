# CVO session 1628-1805Z -- the channel carried a live P0, and four of my own claims died in it

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Seat spawned by MSTR at 16:3xZ (LD-0455) after the post-reboot fabric came back with no CVO while two
standing CVO functions were accumulating live inbound. `/watcher` armed once (task `bictinzzf`), zero
crons, per XXX.md Step 1b-F CVO base row.

---

## Current State

**THE P0 IS HALF OPEN.** Measured live at 17:53Z on the served keys, `s3://opal-data-portal-v2/
platinum/mdpf/{partner}/aggregate-aua-timeseries.json` (HYPHENATED -- the underscored form and the
`opal-data-cot` bucket are both wrong and both 404 cleanly):

```
49financial  as_of_last 2026-08-24  n=452   healthy
inflection   as_of_last 2026-08-24  n=452   healthy
cottonwood   as_of_last 2026-08-24  n=461   RESTORED 17:36:35Z
global       as_of_last 2026-08-19  n=458   STILL FROZEN -- 4 trading days
```

NEVER#1 discharged on `lib/trading_calendar` at this seat before the word frozen was used:
`expected_last_trading_day(2026-08-25) = 2026-08-25`; `trading_days_behind('2026-08-24') = 1`,
`('2026-08-19') = 4`.

**GLOBAL'S GOLD** (`s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json`) is
`2026-08-20T13:31:05Z`, 75 versions, none after 08-20. **The clean discriminating run exists and it
failed:** a 17:51:57Z run read cottonwood input BYTE-IDENTICAL to the post-fix slice
(md5 `d9c758fe1bf4db07`, 90,066 B, 461 dates through 08-24 -- identical to the 17:30:26Z object) and
global still did not emit. No race; the input's own digest is the control. **Restoring cottonwood
does NOT clear global's coherence gate.**

The live lead is `gold/mdpf_revamp/_aggregate_aua/2026-08-19.json`: **1 version, written
2026-08-19T23:33:16Z**, against controls 08-18 (2 versions, newest 13:31:07Z) and 08-20 (2 versions,
newest 13:31:07Z). The only one of the three with a single version and the only one written outside
the ~13:31Z producer window. Untouched through the freeze, the repair, and all three of today's runs.

**COO has ruled `MDPF_COTREMEDIATION`'s repair scope DISCHARGED and is seating global as its own item
with that partition as its first cell.** Correct: global's defect predates the project.

**ESTATE-REPORT BACKLOG: 17 PENDING** (was 19). Producer record perfect over the epoch
2026-08-04..2026-08-25 -- 22/22 days present, 0 MISSING, 0 FAILED, 0 stale-RUNNING. The failure is
entirely adjudication-side and it is this seat's.

**SURPRISE CHANNEL:** `MDPF_COTREMEDIATION` opened and now 12 items (9 GRADUATED / 2
UNDER_INVESTIGATION / 1 DISMISSED_WITH_REASON; 3 ARMED, all owned). `OPAL_KIMIPIPELINE` +2,
`NFRA_COMPRAIL` +2. Every file re-validated from disk by the protocol's own extractor after every
append; the validator was mutant-controlled before first use.

---

## Blockers

**None at this seat.** Two SOVEREIGN calls are open at Andrew and neither is a blocker on anyone
else's work:

1. **The frozen-corpus question** (`OPAL_KIMIPIPELINE-S5`, ARMED, disarmed same-turn by this seat).
   All 160 estate-report proposals awaiting ratification were generated against a rulings corpus
   frozen at `2026-07-31T02:23:07Z` (commit `649fa25a4`), measured identical across 8 sampled days
   spanning the whole backlog, `corpus_predates_window: True` on every one. Ratifying a proposal that
   contradicts a ruling it cannot see would make the contradiction canonical. COO is carrying it to
   Andrew as a standalone open call rather than a footnote inside 33 decisions.
2. **Estate-report batching.** 160 proposals -> 31 entities -> **60 `(resource,field)` decision
   points** -> **33 whose newest formulation is MEASURED**. 0 of 160 are exact duplicates; 47% of
   decision points carry competing texts, mean 4.6, max 17 (`TS-5-parquet-batch-export`
   classification, 08-11..08-25). **The SKILL's stated oldest-first order is wrong for this backlog**
   -- it would put one field in front of Andrew seventeen times with seventeen different texts.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform~M]** Diagnosis, not a re-run: why does `2026-08-19` carry a
   +469/-469 round-trip with zero net drift. Target is the roster, not cottonwood propagation.
   **Scoring bar for any further global run, pre-registered:** cottonwood gold md5 ==
   `d9c758fe1bf4db07` (or a later object with `as_of_last >= 2026-08-24`) verified AT RUN START.
   Two runs today missed that bar for opposite reasons (17:27:53 predated the input, 17:30:44
   straddled it by 18s).
2. **[3.0.0_SA_CVO]** The `MDPF_COTREMEDIATION` decomp certification, owed to `2.0.0_SA_COO`. CTO
   cleared me to certify on my own judgment (70780) and flagged the decomp contradicts itself at
   `DECOMP.md:247` vs `:115`/`:279` on the source-map row -- do not certify across that until COO's
   reconcile lands.
3. **[3.0.0_SA_CVO]** `/estate-pull` does not read `readjudication_required` (`OPAL_KIMIPIPELINE-S4`,
   ARMED, disarmed same-turn by running the three-field read explicitly; 0 of 23 days carry it,
   positive-controlled). The SKILL edit is the REMEDIATION and is NOT done. Composes with S2 (a
   missing VALUE on the status axis) -- one edit closes both.
4. **[1.0.0_SA_CTO~X]** `comp-surprise` false positive routed (my 174505Z): it applies the
   INVESTIGATION schema to REMEDIATION rows. True channel state is 143 items / 66 ARMED, not 144/67.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `"VendorDriftError"` | PASS | 111 hits / 26,575 files; BANDS DEF=5. **Widened CTO's relay from 1 definition home to 5 across 4 converter families** |
| `comp-find` | `"code/scripts/silver"` | **FAIL (structural)** | 14 hits, correctly denominated, and STRUCTURALLY BLIND -- see Gap |
| `comp-find` | `"CROSS-AXIS COHERENCE GATE"` | PASS | 10 hits; the `[DOC]` band surfaced the 28-hour-old CTO deliverable that answered CTO's discriminating question |
| `comp-find` | `"PROVENANCE_CONTRACT_START"` | PASS | 4 hits, DEF=1; grounded `MDPF_COTREMEDIATION-S7` at source |
| `comp-find` | `--name`, import traces x6 | PASS | closed MSTR's reachability question over an 8-module closure |
| `comp-surprise` | `--armed` (via `.tools/` prefix) | **PARTIAL** | real gap closed; 1 false positive + 2 inflated denominators. Not bare-resolvable at this seat |
| `safe-commit.sh` | x8 | PASS | all `-F`, msg-verify MATCH on every one |
| `lib/trading_calendar` | `expected_last_trading_day` / `trading_days_behind` | PASS | NEVER#1 discharged on own instrument, not cited from a peer |
| jsonschema extractor | protocol s.8, x9 | PASS | mutant-controlled first: a GRADUATED+INFERRED+ARMED item with empty evidence is REFUSED |

**What worked:** `comp-find`'s BAND classification did real work twice -- `[DEF]` separated the five
definition homes from 66 raise-sites in one call, and `[DOC]` surfaced a deliverable nobody would
have grepped for. The protocol's own extractor caught nothing because nothing was malformed, which is
what a validated pipeline looks like.

**What failed:** `comp-surprise` (above). `comp-find` on a runtime-assembled path (below).

**GAP FOUND -- and it is the session's most transferable finding.** `comp-find "code/scripts/silver"`
returned 14 hits over 26,591 files, correctly executed, correctly denominated, and **structurally
incapable of hitting the answer**: the consumer builds that path at runtime from `${CODE_PREFIX}` +
`"/scripts/"`, so the literal never appears in the file that consumes it. **My denominator was TRUE
and certified a sweep that could not have matched.** This is the DESIGNED half of the retrieval-
control law -- no way of calling the tool differently fixes it. The estate has no instrument that
resolves variable-assembled S3 prefixes to their consumers; `comp-estate --resource` was the HUD's
suggestion and does not cover the EC2-sync-to-PYTHONPATH shape. Routed as a coverage defect, not
built.

---

## MCP traffic

**~35 messages handled, 12 sends.** Significant: CTO's root-cause OVERTURN (70743) and the D8 re-mint
+ live outage (70736); AE~B's two BLOCKING items (70783) routed same-turn while a seat held on a live
P0; the `@b9ed1dd82a` law edit (70839) and my two proportionality calibration cases back, **all three
clauses adopted into CLAUDE.md** (70902); MSTR's Tier-0-does-not-talk-to-Tier-2 Andrew-direct (70865);
COO's repair-scope discharge ruling (70976). All ACKed via `ack_messages` -- the READ clock, not the
EMITTED one.

---

## The part worth carrying: four of my own claims died today

Every one was a **correct conclusion resting on a wrong mechanism**, and every one was caught before
it landed anywhere load-bearing -- three by peers, one by my own control.

| # | The claim | How it died |
|---|---|---|
| 1 | 08-06 is a FALSE PENDING, backlog is 18 | My predecessor had already falsified it: the 21:49Z re-run produced a genuinely NEW report. **Right number, wrong route.** Caught by reading the channel before reporting. |
| 2 | The backlog is self-amplifying (same proposal recurring) | Measured 0 of 160 exact duplicates. Caught by my own check. |
| 3 | global's gold is today's 13:31Z write off pre-fix silver | It is **2026-08-20**, five days old. **My own format string (`strftime('%H:%M:%SZ')`) dropped the date**, then I reasoned about which day it was from a time that matched my expectation. Caught by MSTR. |
| 4 | The S3 silver prefix has NO CONSUMER | It has a live one. **My search was structurally blind (Gap, above), and I corroborated it with a July DAG-coverage finding -- two silences read as confirmation.** Caught by AE~B. |

**#4 is the dangerous one and the others are not close.** #1-#3 produced wrong mechanisms. **#4
produced a DELETION WARRANT** -- "writer, no identified consumer, correct and permanent" is the exact
sentence a future seat cites to stop deploying to a prefix, and that sync runs `--delete` onto the
PYTHONPATH of the cottonwood gold legs. CLAUDE.md names this failure for `comp-iam`; I wrote the
estate-search version of it.

**The pattern across all four: my conclusions survived because other seats tested the ground under
them.** A correct conclusion makes nobody re-read the evidence -- which is why #3 needed MSTR to read
a date I had removed, on a finding that was otherwise right.

**And the same discipline paid in the other direction 2/2:** re-deriving CTO's relay with a DIFFERENT
instrument widened it 1 -> 5 homes; re-deriving AE~B's vendor-manifest claim by reading the SCRIPT
SOURCE (where they ran `--check`) confirmed it at a different layer and is why a ruling was safe to
act on in minutes. That is `NFRA_COMPRAIL-S6`'s rule, corroborated on my own errors within the hour:
**re-derive with a different instrument or cite the peer's invocation -- never re-run the same
command.**

---

## Files Modified

See commit messages: `201a00cc20`, `23c825d049`, `63b436a015`, `eda494e261`, `c8b5b87042`,
`fc83dba2e8`, `45f4f53f49`, `092fbe74d1`.

All **LOCAL, riding integration** (`git branch -r --contains` returns empty on each) -- reported as
LOCAL per LD-0367, never bare "landed".
