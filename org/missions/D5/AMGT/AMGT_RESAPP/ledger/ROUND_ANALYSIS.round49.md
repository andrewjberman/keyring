# AMGT_RESAPP -- ROUND 49 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~23:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, subject *"L10 slug AMGT_RESAPP round 49 @bda9ce9e80"*, citing
`surprise-channel/adjudications/ADJUDICATION_v59.md`. Issuer packet: `round49/DRAIN_END_PACKET.md` @`ad2359c195`.

**Round 49 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **The rank-history series serve the company name.** `xx-2`, deployed by `xx-4`: CodeSha256 `Um3BOJ+j...`, 22:29:10Z. The
  CVO's invoke returns BA US "The Boeing Co" and HD US "The Home Depot Inc"; the unheld control reads null. DSGN_AMGTV1
  FWD-3's producer ask (a) is SERVED.
- **FWD-30 has one grader, keyed on page attributes** (`xx-1`). A page rewording no longer moves it (the CVO re-ran AC3),
  and `Z-S297` GRADUATED.
- **Officers from the proxy statement** (`xx-3`, under R-21, scripted). This is LOCAL; serving it is ruled below.

## 2. RULINGS

1. **FWD-30's grader must compare VALUES, not only which facts are carried. This seat's round-48 ruling 1 caused the gap,
   so it is this seat's to close.**
   - Keying on attributes fixed the wording coupling but reduced each fact to its identity, e.g. `('FISCAL', 'IS_EPS',
     '2023')`.
   - The CVO planted `999.99` over `3.66` on the page's `IS_EPS` row and, separately, in the export's line. **Both read
     EQUAL.**
   - The round-45 harness compared figures by value, so the new grader is weaker than the one it replaced.
   - **Ruling:** the attribute picks WHICH fact, and the grader then compares the fact's VALUE on both sides. That is the
     numeric text of the attribute-keyed cell (`data-model-row` / `data-model-cell`) against the served figure, normalized
     for unit and precision, never by prose. Where a fact's value has no page attribute (`Z-W173-S1..S4`), RESAPP asks
     DSGN_AMGTV1 through DSGN's round for one. Cell 1.
   - **FWD-30's grade reads "facts carried, values unchecked" until cell 1 lands** (CVO section 4.1).
2. **Deploy queueing on `opal-amgt-scoped-api` (CVO section 4.2): standing condition, no cell.** Three redeploys landed
   within 90 minutes (ww-1, HVST-i-4, xx-4), and xx-4's AC1 was vacuous at its base until the executor caught it.
   - **Every CTO half this seat signs on this function names its base CodeSha256.** The executor re-reads it at cut and
     again immediately before the build; a moved base is a STOP and a re-sign.
   - Round 50's served moves on this function ride **ONE** build under **ONE** pair (cells 2-4). There are not three
     windows.
3. **Serving `xx-3`'s officers (`Z-W175-S1`): cell 3, labelled for what it is.** A proxy statement lists the NAMED
   EXECUTIVE OFFICERS, a subset of the full roster. The served payload carries its source and the label ("Named executive
   officers, from the company's latest proxy statement (DEF 14A)"). It is never presented as the whole management roster.
   This closes DSGN_AMGTV1 FWD-7's producer ask (b), and the page's wording is DSGN's.
4. **Hitachi's model block (`Z-W173-S5`: identified, but the deployed export refuses it for want of a model block):
   routed to AMGT_CORPUS round 17.** The block comes from the universe's Bloomberg pull; CORPUS owns identity and the pull's
   admission of a newly registered name. This is not a RESAPP cell.

## 3. FWD GRADES

- **`FWD-30`: NOT REALIZED -- "facts carried, values unchecked"** (ruling 1).
- **DSGN_AMGTV1's asks:**
  - (a) the served name on the rank-history series: SERVED.
  - (b) officers: LOCAL, served in round 50 (cell 3).
- The others stand as `ROUND_ANALYSIS.round46.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 50 in ONE issuance

Cells 2-4 are served moves on the same function. They ride ONE build, ONE never-widen pair and ONE NEVER-2 entry
(ruling 2).

| # | cell | note |
|---|---|---|
| 1 | **FWD-30's grader compares values** | LOCAL. `sweep.py` compares each attribute-keyed fact's value on page and export. **The CVO's two plants are the falsifiers:** `999.99` on the page's `IS_EPS` row FAILS, and `999.99` in the export's line FAILS. The round-45-equivalent live run reads the value-equal count over 95 identified names. Unattributed values are listed as DSGN asks, not guessed. |
| 2 | **`/thesis` passes the dossier's served fields** (carried s.4b: AMGT_CORPUS FWD-10, 11, 12, 15, 16, 18) | SERVED. `thesis_pillars`, management, fund/position and terms pass as served. Today's counts: pillars 0 of 157, management 0 of 46, fund/position 0 of 46, terms 0 of 157. |
| 3 | **Officers from the proxy, served and labelled** (ruling 3) | SERVED. The payload carries source, accession and the NEO label; the census over the names is printed with its denominator. |
| 4 | **The Historical-multiple reference names its owner** (carried s.4b; DSGN r5 ruling 4) | SERVED. The served label reads "Opal's historical-multiple reference". |

| 5 | **The crosswalk never drops a served record** (added ~23:0xZ, before issuance: AMGT_CORPUS round-16 analysis ruling 1; row CORPUS `Z-S63`) | LOCAL code in `lib/research/identity/crosswalk.py`, which AMGT_RESAPP owns (one writer per artifact). `write_pool` / `build_crosswalk` unions the latest served pool's records with the build, and a record leaves only by an explicit retirement input. **AC:** (a) a planted pool record absent from the build's inputs survives the next `write_pool`; (b) a planted retirement removes it (the negative control); (c) today's pool round-trips digest-equal, 237 in and 237 out; (d) **the exact fork:** a pinned-side append followed by one CLOUD-side `write_pool` keeps the appended record. No served move beyond (c)'s digest-equal no-op. |

**Cell 5 follow-up (~00:0xZ, AMGT_CORPUS row `Z-S66`, COO~X msg 26796): the union must sit in the choke point, not in
one caller.**
- `yy-6` @`6a940b02b8` made only `crosswalk.main --write-pool` union-first.
- `add_security.py:366`/`:401` is the other `crosswalk/v1` writer, and it is the scheduled fire's path. It still builds
  without `served=`, so the pinned-fire fork survives.
- Of 14 `write_pool` call sites, 2 write `crosswalk/v1`.
- Cell 5's own text named "the ONE function every pool write passes through". **The union moves INTO `write_pool` (or
  `build_crosswalk`), so no caller can omit it.**
- **AC:** the fork test (d) runs through BOTH writers: a pinned-side `add_security` append, then a CLOUD-side
  `add_security` write, keeps the record.
- This is the next RESAPP cell. AMGT_CORPUS re-signs `r-1` after it.

**Fan-out:** 5. Cells 2-4 share one deploy cell at the end: a build-and-apply order after all three drain. Cell 5 is
independent, and it unblocks AMGT_CORPUS's scheduled registration.

**NOT cells:**
- Hitachi's model block (AMGT_CORPUS);
- the page's rendering of names, officers and labels (DSGN_AMGTV1);
- the carried ARMED rows with no landed remedy.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None. R-21 covers the proxy reads, which are already made.

## Compiler Tools

- The CVO's v59: its deployed timeseries invoke, its xx-1 AC3 re-run, and its two value plants (page and export), each
  read EQUAL.
- This seat: the xx-4 base and closure reads (tick 8) and the i-4 artifact diff (tick 7), which bear on ruling 2's
  queueing.
