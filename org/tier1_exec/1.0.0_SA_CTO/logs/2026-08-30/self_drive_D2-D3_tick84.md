# /self-drive D2 & D3 — tick 84 (2026-08-30 08:42Z) — state: ARMED

Covers tick 84 and the inter-tick acts since the tick-83 log (`63475dfe5d`, LOCAL; origin @`0ae699e57b` at the
08:22Z CLOSE). Cron `1c261f82` :07/:37 (fired 08:42Z on idle). Paired `/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **24 → 25** (register) == **25** (`to-check`):
ADVI_BDPARITY 5 → 6 (`P2-1-AE`, the feed-selector apply, cut at `0.8.0_AE_CloudComp~Y` @30c8b1c9c6). Claims 342
of 342, lag 0. Ledger **19 / 0 unconsumed**. Delivery state 50 of 50 READ at the tick's open.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 5** (R1–R5, unchanged). No pitch.

## Verdicts since the tick-83 log (§3)

**0 on pitched calls.** Grades read: CVO 86714 the three 08-11 overwrite diffs PASS (with the `_ingested_at`
source read); CVO 86749 the B-5 neighbour column PASS.

## Driver's own acts (tick 83 → 84)

1. **Two of the gate's own clauses WITHDRAWN on measurement.** (a) 86702's "a field whose name claims a vintage
   and whose value is the key is a value not carrying its claim, worse than absence" — the CVO read
   `_ingested_at` at source: the asof partition date is the DESIGNED semantic (`runner_common.py:16/:88`,
   Atom 9 "never a clock", for byte-reproducible re-runs); withdrawn (86727). The B-5 ruling (the neighbours'
   inferred instant from S3 object metadata, never an in-object field) STANDS and is now grounded IN the
   design; two real findings adopted — `a07:352` stamps a wall CLOCK under the same name (two intents, one
   field; a DS cell after M-3) and `a04:44-46` builds dim_calendar's span from the partition tree observed at
   run time (its manifest span end IS an in-object vintage). (b) 86534's premise "a P14-produced partition
   (written 2026-08-28T09:5xZ, 534 of 535) → the 08-28 map" — AE~L measured the column per partition from
   object metadata (86737): the campaign ran 08-28T00:46Z..08-29T12:46Z (224/311), 533 on the 08-28 map and 2
   on 08-27, the 08-10 and 08-18 neighbours both on 08-28; the conclusion holds, the time and the count were
   the gate's unverified numbers, and AE~L nearly announced a false 224/311 two-vintage split by probing at
   the gate's quoted time — the class ("a timestamp in a ruling is a claim, not a coordinate") owned here and
   then measured at the issuer too (86752). The 534-vs-535 count reconciled by PRODUCER vs TIME (534 P14 +
   the Saturday floor's 08-28 at ~12:46Z); the log form is the discriminator, one listing at AE~L.
2. **The three overwrite diffs accepted** (86702): dim_boundary / dim_security NO-OP on a comparator whose
   positive control fired (14,675 / 12,264 cells), dim_calendar +13 additive with 0 changed cells across the
   526 shared days; the dim_boundary conditional measured-and-not-met; the ledger RE-DATED on the M-3 gate
   (NEVER-2 disposition concurred 86652: no rollback of the six).
3. **inf-silver-chain plan shape complete** (86672/86689): check (i) fires 4 of 4 drift with the denominator
   asserted (the first tool-visible detection of the 111-day drift, two derivations); the wired check + three
   refusal arms before the build; (ii) labelled CONTROL; (iii)/(vi) gain RAW CR == 0 beside the LF sha (the CVO:
   an LF-normalised oracle is blind to CRLF by construction); DS~V put both assertions into the manifest's own
   declaration @50231665b0; the apply word waits for the (iv) rows; EXERCISED = two arms of opposite polarity
   at DS~V after the next scheduled fire (content-equal vs the dispatch writer; DIFFERENT in the 08-11 columns
   vs the chain's last stale output).
4. **The BD puller's feed selector read at the artifact and ACCEPTED** (86665; the docstring-only re-sha
   verified 26 of 26 code lines identical, 86721): the literal "default PERFORMANCE only" WITHDRAWN — it would
   silently starve `OPAL_TAXSMA_PT2`'s silver build; the caller narrows. Face P2-1-AE at AE~Y: PA-3 on the
   gate's word on the PA-2 rows (code row, zero env rows, LF sha + raw CR 0 on the downloaded zip).
5. **P2-1 R3 placement ruled** (86588): the harness's six at the cell grain; request-side members by emitter;
   NOT-RESOLVABLE at the account grain; VACUOUS at the differenced-window grain. R1 corrected the number in
   this seat's own recap: pass 2 does not batch (N=50 ≈ 2.1 h). The ask reaches Andrew on the graded re-cut.
6. **The manifest deadlock** broken and discharged; the ack-guard's first production catch recorded (state →
   EXERCISED; the pre-fix client text renders a refusal as a no-op until relaunch); the ledger tool's
   HELD_STATUS mislabel queued (2 of 2 held entries external-gated, both labelled SOVEREIGN).

## In motion, not mine

DS~N: M-2/M-3 against ~12:40Z (else before Monday's fire); the 12:50Z fire read; AE base: (ii)–(iv) → the apply
word; AE~Y: PA-1/PA-2 → the word; DS~C: the P2-1 re-cut; AE~L: the log-form listing, the re-drive after M-3;
the ~12:18Z V-4 check; S1e at the next 04:35Z fire.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, `to-check.py --all`, claims scan (both `prds[]` shapes), `get_delivery_state`
(50/50); `git show <pin>:<patch>` + python difflib on the two patch versions (the gate's own instrument for the
byte-identical-hunks condition). No comp-find, no comp-state.

state: ARMED · next log at a verdict or tick 90 (floor)
