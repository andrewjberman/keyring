# DSGN_AMGTV1 -- ROUND 2 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~09:4xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26544, READ-acked, subject *"L10 SLUG DSGN_AMGTV1 round 2 @6f1ecd4229"*,
citing `surprise-channel/adjudications/ADJUDICATION_v3.md` @`426064a1b0` + `ADJUDICATION_v4.md` @`6f1ecd4229`. Issuer packet
`deliverables/2.0.0_SA_COO~D/round2/DRAIN_END_READ.md` @`e724da66a2` (msg 26534). Rows `Z-S1` and `W4-S1` were ruled the same tick at
`CTO_RULING_DSGN_AMGTV1_R2_ZS1_W4S1_20260929.md` @`06d51bce50`.

**Round 2 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

7 of 7 orders terminal. On the signed-in walk (Valero and INTU), check hits went from 32 to 8. The CVO's L9 verdicts:
- **e-3: PASS.** Header money reads one way, in the served currency.
- **e-4: PASS.** Model lines are named in words, and each of the 18 refused lines has one sentence.
- **e-2: PASS on Valero, UNGRADED live on INTU.** The API did not serve `team_cases` until `vv-4`.
- **e-1, e-5, e-6: PARTIAL.** The dark band, captions, slash key and reasons pass, but machine strings remain on the face:
  `(S13)`, `crosswalk/v1`, `generation: none ...`, the lead panel's source line (`generation ... | state COMPLETE | ... 127.0.0.1:8194`),
  `WMB_US_Equity`, `claude-opus-5`, and "BLOOMBERG SESSION: NOT REPORTED".

## 2. THE CVO'S TWO DECISIONS

1. **INTU's live sentence is FALSE, not merely unserved -- RULED: the absence sentence names the gap the page can see.** Where the
   payload carries no `team_cases` field, the page says the team's case is "not served on this page yet". It says "not in the pack"
   only when the served field itself reads ABSENT with the dossier's own reason. A value carries its claim. `vv-4` is now applied:
   `team_cases` is served for 84 of 95 names, so INTU's re-walk must render the team's own case.
2. **FWD-11's raw-code check is a one-shape blacklist -- RULED: the walk judgment is FWD-11's oracle, and the mechanical check
   inverts.** It stops listing forbidden shapes. Instead it prints every visible token that is not ordinary prose (a word, a
   number, a money figure, a date or a ticker), with its surface and count, so each one is judged. A zero then means "nothing
   non-prose is visible", not "none of the shapes we already know". This is the issuer's own instrument note (s.5 item 4), widened
   to its class.

## 3. FWD GRADES

- **`FWD-9`: REALIZED.** Its bar is a walk on a name with missing lines: every line in words, and every missing line one sentence
  saying whether the data is missing or the page cannot yet show it. The CVO graded e-4 PASS on that walk (shot `030`).
- **`FWD-1`: NOT REALIZED.** Hop 3 needs the served company name (AMGT_RESAPP round 48). Hop 6 on Valero is met by its honest label
  (ruling `Z-S1`).
- **`FWD-4`: NOT REALIZED.** The format passes, but its bar is a walk "on names in more than one currency", and Valero and INTU are
  both USD. Round 3's walk adds a non-USD name.
- **`FWD-6`:** the team's own case is walked on INTU now that `vv-4` serves it.
- **`FWD-2`, `FWD-10`, `FWD-11`:** PARTIAL on the machine strings in s.1.
- **1 of 11 REALIZED.** This analysis ends in an enrichment list.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 3 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **Every machine string named in s.1 off the face** | FWD-11, FWD-2, FWD-10 | into words, or behind a "details" affordance a PM opens on purpose; the inverted check of decision 2 prints what remains |
| 2 | **The team-case absence names the gap the page can see** | FWD-6, FWD-1 hop 6 | decision 1; INTU renders the served case |
| 3 | **The page/export parity harness keys on data and opens card windows** | FWD-30 parity (W4-S1 (a)) | also closes AMGT_RESAPP `Z-S297`: the harness cannot see cites inside click-open card windows (vv-4 AC2 84 of 95, page-side) |
| 4 | **Exec Management's absence in words** | FWD-7 | "ABSENT (ZERO_OFFICERS)" becomes a sentence saying where the list came from |
| 5 | **The last dark bands, money form and chart caption** | FWD-11, FWD-4 | Model and Posture headers to one band per page; the remaining `$` form; the Thesis chart caption's mnemonic |

**The round's one real run:** the signed-in walk on Valero, INTU, and **one non-USD name with a team case** (from the 84), for FWD-4's
bar. **Fan-out:** 5 cells, cap 8.
**NOT cells:** the served name (AMGT_RESAPP round 48); the export's wording from one source (AMGT_RESAPP round 48, W4-S1 (b)).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Remove the merged worker worktrees `/c/tmp/wk-dsgn-amgtv1-{1..8}`, if he wishes [CLAUDE.md Agent Autonomy: recursive deletion].

## 6. WHAT THIS ANALYSIS DOES NOT DO
It changes no ENDPOINT line. `FWD-9` is graded REALIZED on the CVO's judgment; no other outcome moves.

## Compiler Tools
The CVO's PNG judgments (v3) and its L10 close (v4), and the COO's DRAIN_END_READ read to EOF, taken as measurements; FWD-4's and
FWD-9's DONE WHEN lines read at the PRD's ENDPOINT section.
