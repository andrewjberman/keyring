# AMGT_RESAPP task order -- `AMGT-ba-17` -- THE CSC COLUMN CONTRACT: EVERY PRESENT COLUMN CARRIES ITS PERIOD OR HORIZON, ITS CURRENCY AND ITS SOURCE FIELD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~283</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one pure module and its test.
comp-iam: DECLARED-NOT-APPLICABLE -- `build_csc_map()` builds from the module's own tables and the shipped factor registry; no read path is added.
comp-adversary: RUN by the issuer at the cut -- r77_ba17 AC1 FAILS at the base: 5 of 17 columns are PRESENT and 0 of the 5 carry `period_or_horizon`, `currency` or `source_field`. AC2 PASSES: the ABSENT partition is the seventeen minus the five, and each of the 12 carries `derivable_from` and `reason` and no value.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; no pool read.
</preflight>

**Your worktree:** `C:/tmp/r77-283` (branch `wk-AMGT_RESAPP-283`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-283`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-17` (round 77, decomposition s.85)

The CTO's ruling (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @4a89bef967, section C; rows Z-W18-S13 and Z-W21-S6), in its words:

- A PRESENT CSC column carries {value, period or horizon, currency, source field}.
- An ABSENT column carries {derivable_from, reason} and NO value.
- So the ABSENT partition in `csc.py:21-31` is right as written. What is owed is the four fields on the PRESENT columns.

**Build, in `lib/research/peers/csc.py` only.** Each entry of `build_csc_map()["present"]` gains three fields beside what it carries today (the value itself is per peer, on the member rows, and is not this cell's):

| field | rule |
|---|---|
| `period_or_horizon` | the entry's own `horizon` (already derived by rule from the registry name), never a fiscal-year label |
| `currency` | `"USD"` for Mkt Cap and EV (the scanner serves both in USD millions); `"none"` for the two P/E columns, with `currency_reason` saying in plain words that a ratio carries no currency; `"per member"` for Price, with `currency_source` naming where each peer's price currency is read (`lib/research/peers/price_currency.py`: the company's own stored trading-currency figure, or its plain reason) |
| `source_field` | one plain string that names the column's own scanner code or row field (the entry's `code`) and its kind, for example the scanner factor `ev` or the row field `price` |

Rules:
- State a currency only where the module or the registry already states it. The scanner row carries no currency label for a price, so Price is `"per member"`; do not infer one from a country, an exchange or the cap currency.
- The ABSENT entries do not change: no value key is added, `derivable_from` and `reason` stay.
- `present_line()` prints the three new fields beside each column.
- **Plant test** `lib/research/peers/tests/test_csc_present_contract.py`: five of five PRESENT entries carry the three fields; a registry that drops a code downgrades that column to unverified and the subtraction still sums to seventeen.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W283-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no peer-set rebuild, no vendor, SEC or model call, no portal write.
2. No existing key of the map changes name or value; only the three fields (and the two companions) are added. `CSC_COLUMNS` stays the seventeen.
3. `lib/research/peers/engine.py`, `universe.py` and `price_currency.py` are not yours. Whether each peer row carries a value for a PRESENT column is the peer-set producer's surface (row Z-W18-S13's second half); if you measure a gap there, file a row and keep working.
4. Any reason you write is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/peers/csc.py
lib/research/peers/tests/test_csc_present_contract.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~283/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-17"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba17.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>C0-C5 PASS: five of five PRESENT columns carry period_or_horizon, currency and source_field; Mkt Cap and EV state USD, the two P/E columns state none with the reason, Price states per member with its source; R77 BA17 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-17"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba17.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>C1-C3 PASS (the control): 5 present + 12 absent = the seventeen, every ABSENT column carries derivable_from and a reason and no value, no fiscal-year label; R77 BA17 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~283 <0.9.0_WK_AMGT_RESAPP~283@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~283/AMGT_RESAPP.TO-AMGT-ba-17.csc-present-column-fields.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the five PRESENT entries' three new fields as built;
- the peers suite's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Z):** ROUND_ANALYSIS.round76.md @c8bbeeac10 section 4 item 10 (the CSC present-column fields); ruling CTO @4a89bef967 section C. Decomposition s.85. Chain `~283`, wave 0, no inbound edge. Checks dry-run at the base: ba-17 AC1 base: FAIL as expected; ba-17 AC2 base: PASS as expected. The currency vocabulary (`USD` / `none` + reason / `per member` + source) is the issuer's reading of "currency" for a ratio and for an unlabelled price; it is the smallest statement the module can make without inferring. No adapter hookup: the map rides inside each stored peer set (`csc_columns`), so the served table gains the fields when the peer sets are next built (not in this cell). A small cell: `worker-light` was considered and not taken, because the registry reading needs care.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~283</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
