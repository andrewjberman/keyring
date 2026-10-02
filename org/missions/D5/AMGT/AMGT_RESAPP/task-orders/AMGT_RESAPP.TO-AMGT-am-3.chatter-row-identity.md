# AMGT_RESAPP task order -- `AMGT-am-3` -- FWD-2: CHATTER ROWS SERVE TICKER, CLASSIFICATION AND PLACES_MOVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~206</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c3 --where deployed FAILS at the base: 0 of 95 rows carry the three keys.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-206` (branch `wk-AMGT_RESAPP-206`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-3` (round 63, decomposition s.71)

`lib/research/api/monthly_chatter.py` `read_monthly_chatter` serves each covered row as `security_key`, `display_name`,
`name_source` and `by_month`. Add, beside `display_name`:
- `ticker`: the row's Bloomberg identifier, from `scoped_amgt.resolve_identity(key)["bloomberg"]` or its display ticker;
- `classification`: the same `classification` block the price ranking rows serve (`scoped_amgt._classification_for_ticker`), or null
  plus a plain `classification_reason` when the table holds none;
- `places_moved`: the same field the price ranking rows serve (`scoped_amgt._join_places_moved`, TRENDING/PRICE axis, the served
  date), or null plus a plain `places_moved_reason` when the name is not ranked.
Read each source ONCE per request, never per row.
Tests in `lib/research/api/tests/`.

**AMENDMENT 1 (issuer, 2026-10-02 ~15:2xZ; CTO msg 28553, DSGN FWD-24):** `/security/<key>/overlay`'s `breakout_price` row also serves
`places_moved`, joined from the BREAKOUT/PRICE rankings row the overlay already reads (VLO: the rankings serve 13 while the page prints
#7). A security with no rankings row (ROG_SW_Equity is the one covered name unranked) serves `places_moved` null plus a plain
`places_moved_reason`. Plant both in a test. AC2's check now carries C3 (VLO's overlay equals its rankings row) and C4 (ROG_SW serves the
reason).

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~206/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c7 --where local; echo "exit=$?"</invocation><expect>AMENDMENT 2 (R1): C1 0 false of 94 bars, C2 every served places_moved equals prior rank minus rank; R63 C7 SERVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c8 --where local; echo "exit=$?"</invocation><expect>AMENDMENT 2 (R2): C1 AMD serves Information Technology from sub_asset_class, C2 every bar serves a GICS sector with its source or null with a reason; R63 C8 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~206 <0.9.0_WK_AMGT_RESAPP~206@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~206/AMGT_RESAPP.TO-AMGT-am-3.chatter-row-identity.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

## 7. AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~19:0xZ) -- repair cells R1 + R2 (CTO msg 28666 @5e5c8407c4)

Both come from `3.0.0_SA_CVO~Z` v30 @ae0d4e7082 (DSGN FWD-2), as written in `ledger/ROUND_ANALYSIS.round62.md` (last addendum).
Both are in `lib/research/api/scoped_amgt.py`.
- **R1 (DSGN Z-C-S36, ARMED, a false served reason on PROD).** `read_rankings` joins `security_key` onto each row (via
  `_join_covered_identity`) BEFORE `_join_places_moved`. `_join_places_moved` builds its prior ranks with `_row_identity`, which is
  `security_key or ticker`, over PRIOR rows that carry a `security_key` on only 32 of 94. So 62 of 94 bars serve "not ranked in the
  previous generation (2026-09-30)" for names that WERE ranked in it. Fix: the match reads ONE key form on both sides (for example,
  the same identity join on the prior rows, or one key read identically from both). Do not change rank, score or order.
  Plants: a name ranked in both generations serves `places_moved` = prior rank - rank; a truly new name serves the reason; a prior row
  with no `security_key` still matches its current row.
- **R2 (DSGN Z-C-S37, RULED (a), serving side).** For an equity (`classification.asset_class == "equity"`), `classification.sector` is
  Opal's `sub_asset_class` when that value is one of the 11 GICS sectors (Communication Services, Consumer Discretionary, Consumer
  Staples, Energy, Financials, Health Care, Industrials, Information Technology, Materials, Real Estate, Utilities). Serve it with
  `classification.sector_source: "opal_classification.sub_asset_class"`. Otherwise serve `sector` null with
  `classification.sector_reason` (a plain sentence). Apply it once, in the classification join, so every route that serves
  `classification` serves the same field. Plants: AMD serves Information Technology with the source; a non-equity serves null with the
  reason; a non-GICS sub_asset_class serves null with the reason.
The base, measured by the issuer on deployed and local at ~19:0xZ:
- `r63_served --cell c7`: 62 false of 94 bars (prior 2026-09-30, 94 rows); 32 moved values correct.
- `--cell c8`: AMD sector None; 0 of 94 bars served.

**AC2 and AC3 under this amendment** (AC1 is unchanged; the issuer re-runs c3 at the drain):
- AC2: `r63_served.py --cell c7 --where local` -- C1 0 false of 94, C2 every served places_moved equals prior rank minus rank;
  R63 C7 SERVED: YES; exit=0.
- AC3: `r63_served.py --cell c8 --where local` -- C1 AMD serves Information Technology from sub_asset_class, C2 every bar serves a GICS
  sector with its source or null with a reason; R63 C8 SERVED: YES; exit=0.
Served by am-6 leg 3 under one never-widen pair. Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added
order; GATE (viii) does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** COO~D msg 28526 (DSGN r27 AV-ze-1 reads them the day they serve). Served by am-6.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~206</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~16:1xZ):** ACCEPTED, AMENDMENT 1 included. Worker ~206 `a1fcefa0e8`/`5e26cc7aae`,
drained `514cdf5366`. Re-graded on the shared tree: AC1 in the union run 589 passed exit=0; AC2 c3 local YES (C1 95 of 95, C2 95
of 95, C3 VLO overlay 13 == ranking 13, C4 ROG_SW_Equity places_moved None with a plain reason). Served by am-6.

<status>complete</status>

**ISSUER REOPEN (2.0.0_SA_COO~Z, 2026-10-02 ~19:0xZ):** AMENDMENT 2 (R1 + R2, CTO msg 28666). Re-seated on ~206.

<status>pending</status>
