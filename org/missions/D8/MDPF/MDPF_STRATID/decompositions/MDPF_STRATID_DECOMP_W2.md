# MDPF_STRATID decomposition -- WORKSTREAM 2 (S01 matcher, S02 one list, S03 rules as data, S08 unidentified list)

**Issuer:** `2.0.0_SA_COO~S1` (dell1), cut 2026-10-09 ~04:5xZ. **Opened by:** PRD ADDENDUM v0.4 @`c690447ee7` (`1.0.0_SA_CTO~DELL1`),
the fold of `UB-20261009T040755Z-d866` (CRO approach; CVO SIGNED). Round 1 (`MDPF_STRATID_DECOMP.md`) is untouched: its surface is
frozen until its FWD-1 read at the 2026-10-09 13:30Z scheduled fire. Rule 27: a workstream is a scope, not a round; one issuer.

## Inputs (GUARD 2: measured, not held)

- S04 Eclipse census: `deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md` @`59a3be55de`, NONE-FOUND over 1363 names,
  graded MET (`C-S1`). So the matcher has no Eclipse sleeve to find today; it is built to serve Eclipse once sleeve names are ingested.
- S07 Muni read: `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_S07_MUNI_VERIFY_20261009.md` @`67e20ee89f`, UNDETERMINED.
  So the Muni rule is DATA with member `null`; `Opal_Muni_Income` goes on the S08 list; no Muni dollar counts (C-MUNI-VERIFY). The
  person's check is queued on dell1's open calls.
- Today's identity rules: `data/assets/scripts/silver/rebalancer_schemas.py:218-233` (`OPAL_SMA_NAME_RULES`, `opal_sma_member_of`),
  read by the Cottonwood slice, pair and dim (`build_cottonwood_mdpf_slice.py:651,726,760`; `build_cottonwood_mdpf_pair.py:148`;
  `build_dim_model_portfolio.py:324`). The ETF list `infra/aws/etfs/config/etf_universe.json` (deployed to
  `s3://opal-data-etfs/config/etf_universe.json`) carries 4 tickers and no names; its three readers take only `tickers`
  (`_load_universe`, cot `:101`, inf `:88`, bd `:57`), so added keys move nothing they read (check `w2_1_loaders`, PASS at base).
- Real neighbour measured 2026-10-09 ~04:5xZ: Cottonwood Rebalancer silver latest date 2026-10-08, 362 distinct names over
  `fact_model_roster.model_name` + `fact_model_definition.{model_name,sleeve_name,component_name}`.

## Rulings the issuer makes inside this decomposition

- **W1. GUARD 1 binds the issuer too:** no workstream-2 branch is merged into `box/dell1` before the 13:30Z FWD-1 read is committed.
  Reason: a `box/dell1` push uploads changed scripts to the code prefix the EC2 runner syncs at run time, which is a deploy by push.
  Workers build on their own branches now; the drain waits for the read. No order writes AWS.
- **W2. The list's home is the existing file** (C-ONE-LIST: no new address). `etf_universe.json` gains `full_names`
  (`{ticker: {"name", "source"}}`) and `sma_name_rules` (`[{"member": <id>|null, "pattern": <regex>, "source"}]`). `tickers` does not
  move. The S3 copy is written by the issuer at the drain, after the read, never by a worker.
- **W3. Today's partial-name prior art is kept as DATA, not code:** "Pathfinder Disciplined" -> `pfde`, "Pathfinder Focused
  Opportunit" -> `pfoe` become `sma_name_rules` rows citing the Andrew-direct 2026-10-01 record, so the matcher reproduces today's
  answers on every one of the 362 names (seam `w2_2_seam`).
- **W4. A rule row with `member: null` identifies a strategy that is NOT counted** (Muni until C-MUNI-VERIFY). The matcher returns
  None for it and reports it as a null-member hit; S08 lists it with that reason.
- **W5. Runtime wiring is the drain's, not a cell's.** The cells build the matcher, its data and the list function and prove them on
  real names. Pointing the deployed silver/slice path at the S3 copy (IAM read of `opal-data-etfs/config/` by the runner role) and
  serving the S08 list at a builder-produced address are drain acts after the read, under their own entries.

## Rule 24

Domain: PRD surfaces S01, S02, S03, S08 (the addendum's scope). S04 and S07 are inputs (done). S05, S06 and S09 are round 1's.
Three write sets, one intent each: the list data (ST-w-1), the matcher and its one call-site delegation (ST-w-2), the unidentified list
(ST-w-3). No remainder. State coherence: ST-w-1 moves no figure (data only, repo only); ST-w-2 moves no figure (same answers on the 362
real names; any gain is printed); ST-w-3 moves no figure (a list). None touches the slice, registry, consolidator, aum-metrics,
`mdpf-gold-lambda`, the S3 list or any served key.

## The cells

| cell | what | serves | placement | risk | chain / slot |
|---|---|---|---|---|---|
| `ST-w-1` | `etf_universe.json` gains `full_names` (each with its cited owned source) and `sma_name_rules` (the two Pathfinder prior-art rows, a Muni row with `member: null`, and any further row a measured name justifies); `tickers` unchanged | FWD-5, FWD-4 | repo only | WORLD (gate floor: infra/ path) | A, `0.9.0_WK_MDPF_STRATID~4` |
| `ST-w-2` | `data/assets/scripts/silver/opal_strategy_matcher.py`: `StrategyMatcher(cfg)` (ticker whole word, full name, data rules; two members raise; null-member hits reported) and `load_strategy_config()`; `rebalancer_schemas.opal_sma_member_of` delegates to it with today's answers; census of every hard-coded identity copy, each REPLACED or KEPT with a reason | FWD-5, FWD-4 | repo only | LOCAL | B, `~5` |
| `ST-w-3` | `data/assets/scripts/silver/opal_unidentified.py`: `unidentified_candidates(rows, member_of, cfg)` -> rows `{firm_id, name, dollars, reason}` for names that look Opal ("Opal" as a word, a list ticker as a word, a full name or rule pattern) and matched no counted member; a recorded list for Cottonwood's latest date | FWD-7 | repo + one document | LOCAL | C, `~6` |

## Interface contracts (fixed here; cells build against them in parallel)

- **List schema (ST-w-1 -> ST-w-2, ST-w-3):** `{"tickers": [..], "full_names": {"<T>": {"name": str, "source": str}},
  "sma_name_rules": [{"member": str|null, "pattern": str, "source": str}], ...existing keys}`.
- **Matcher (ST-w-2 -> ST-w-3, the drain):** `StrategyMatcher(cfg).member_of(name) -> str|None` (raises `ValueError` on two members);
  `.hit(name) -> {"member": str|None, "rule": str}|None` (a null-member hit returns `{"member": None, ...}`).
  Ticker members are the lower-cased ticker. `rebalancer_schemas.opal_sma_member_of(name)` keeps its signature.
- **ST-w-3** imports only `rebalancer_schemas.opal_sma_member_of` (stable today) and takes `cfg` as a dict, so it does not wait on W2-2.

## Write sets (disjoint)

- **ST-w-1:** `infra/aws/etfs/config/etf_universe.json`; the channel.
- **ST-w-2:** `data/assets/scripts/silver/opal_strategy_matcher.py` (new), `data/assets/scripts/silver/rebalancer_schemas.py` (the rule block
  and `opal_sma_member_of` only), `data/assets/scripts/silver/tests/test_opal_strategy_matcher.py` (new),
  `deliverables/0.9.0_WK_MDPF_STRATID~5/IDENTITY_COPY_CENSUS.md`; the channel.
- **ST-w-3:** `data/assets/scripts/silver/opal_unidentified.py` (new), `data/assets/scripts/silver/tests/test_opal_unidentified.py` (new),
  `deliverables/0.9.0_WK_MDPF_STRATID~6/UNIDENTIFIED_STRATEGY_CANDIDATES.md`; the channel.
- Checks (issuer's, dry-run at the base 2026-10-09 ~04:5xZ): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/`.
  `w2_1_list` FAIL as expected; `w2_1_loaders` PASS as expected (bound); `w2_2_tests`, `w2_2_seam`, `w2_2_census`, `w2_3_tests`,
  `w2_3_seam` FAIL as expected. Seam positive control: `w2_2_seam` with a stand-in matcher equal to today's rules reads
  `DENOMINATOR: 362`, `same: 362`, `W22-SEAM-OK`, so its real-data path is exercised.

## Edges and fan-out

No edge: each cell builds against the contracts above; ST-w-2's seam reads ST-w-1's file and is graded at the drain on the merged tree
(at build it uses the worker's own copy of the list per the contract). `fanout: 3 of 3 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule moves; nothing is wired into a running path in this workstream (W5).
- `comp-iam`: DECLARED-NOT-APPLICABLE for the cells (read-only S3 under the worker's own credentials, no runtime change). Named for
  the drain (W5): the runner role's read of `s3://opal-data-etfs/config/` is not measured; the drain runs `comp-iam` before wiring.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- the one hazard it would name is recorded here: a matcher that reads S3 at run time
  fails differently from a constant; ST-w-2 fails closed (raises) when the config is unreadable, never silently falls back to code.
- C-NAMES / Rule 30: no new address or resource name (W2). S08's served address is a drain act through `lib/opal_naming.py`.

## The issuer's acts at the drain (not cells), all after the 13:30Z read is committed

1. Merge the three branches (`safe-merge.sh`), run `w2_2_seam` on the merged tree (ST-w-1's real file), the silver test suite once.
2. Writer census of every reader of `opal_sma_member_of` (5 call sites above) before any wiring.
3. Under a change-management entry: write the amended list to `s3://opal-data-etfs/config/etf_universe.json` (rollback: the prior
   object version) and read it back; `comp-iam` the runner role; wire the slice path; the next scheduled run reads the same answers.
4. FWD-4 and FWD-5 are EXERCISED "on purpose": a test ticker/rule row added to a copy of the list is found with no code edit (the
   ST-w-2 tests), then once on the real path at the drain.

## Amendments (issuer rulings at the drain read, 2026-10-09 ~05:1xZ)

- **A1 (ST-w-3 contract, the issuer's defect): an Opal MODEL is not an unidentified strategy.** Worker `~6` @`bd9cb30a48` built the
  contract as written and listed 38 of 45 Opal-looking names, most of them ordinary Opal Models (`Opal Satellite 40..80`,
  `Opal Short-Term`, `Opal Fixed Income`) as `NO_MEMBER` (row `MDPF_STRATID-D1-W6-S1`). C-SLEEVE and the PRD BOUNDARY ("reclassifying
  an Opal Model as an SMA" is out of scope) say those are not candidates. Ruling: the list excludes a name that is an Opal Model figure
  (Rebalancer `fact_model_roster.is_opal` true, or a registry Model member), and lists it only if it ALSO matches a sleeve rule. This
  is a narrow re-cut of the function's predicate, carried to the next workstream-2 issuance with the drain; the order stands complete.
- **A2 (ST-w-1 names): the cited fund names may be stale.** ST-w-1 sourced the four names from the net-assets producer's FUNDS table
  (`etfs-netassets-daily/lambda_function.py:104-113`: "Polen Dividend Income ETF", "Polen International Dividend Income ETF", ...),
  while Cottonwood's model definitions carry a component named `OPAL INTERNATIONAL DIVIDEND INCOME ETF` (2026-10-08). Ruling: before
  the S3 write at the drain, the names are re-read against the fund's current legal name, and `full_names` carries the current name
  (a former name may ride as a second rule row). No figure moves on this: a full-name match only ADDS a member where today's rules
  had none, and the seam prints every gain.
- **A3 (row ids, the issuer's defect):** the orders named the surprise-row id form `MDPF_STRATID-W2-W<n>-S<k>`, which the row gate
  refuses; the dell1 worker form `MDPF_STRATID-D1-W<n>-S<k>` is correct and stands.
- **A4 (cell `ST-w-4`, cut 2026-10-09 ~05:2xZ under A1):** `unidentified_candidates` excludes a name that is an Opal Model figure
  (an `opal_models` set the caller passes: Rebalancer `fact_model_roster.model_name` where `is_opal` is true) unless the name also
  matches a sleeve rule (ticker, full name or `sma_name_rules`); the Cottonwood record is re-made with an `EXCLUDED-AS-MODEL:` line.
  Write set = ST-w-3's (`opal_unidentified.py`, its test file, the record), continued by slot `~6` on its branch
  `wk-MDPF_STRATID-w2-6`. Serves FWD-7. LOCAL. Checks `w2_4_tests`, `w2_4_seam`: FAIL as expected on `~6`'s branch @`bd9cb30a48`.
- **A5 (cell `ST-w-5`, cut 2026-10-09 ~05:3xZ): disarm of row `MDPF_STRATID-D1-W5-S1` (ARMED, disarm owner this issuer).** ST-w-2
  (`~5` @`694ae230d1`) makes `rebalancer_schemas.py` import `opal_strategy_matcher.py`; six carriers ship the first without the second
  (`w2_5_ship` FAIL 6 of 6 on `~5`'s branch). Until ST-w-5 is terminal the hazard is held by ruling W1 (no workstream-2 merge before the
  13:30Z read) AND by this one: **the `~5` branch never merges without ST-w-5 on it.** ST-w-5 adds the matcher beside
  `rebalancer_schemas.py` in each carrier, continued by slot `~5` on its branch. WORLD (gate floor: infra/ and .tools/ paths); it deploys
  nothing. The live gold lambda is unaffected: its deployed package is the pin-148f715f8c build and nothing rebuilds it before the read.
- **A6 (ruling on row `MDPF_STRATID-D1-W6-S2`, BLOCKING, the issuer's defect): `opal_models` = the union of `is_opal` model names in
  `fact_model_roster` AND `fact_model_definition`.** Five Opal models (`Opal Short-Term`, `Opal Fixed Income`, `Opal Long-Term Aggressive`,
  `Opal Moderate Income`, `Opal_Moderate_Income_Tax_Efficient`) appear only in the definition table, so the roster-only source left them
  listed (`~6` @`a53204441c`: LISTED 12, W24-SEAM-BAD on `Opal Short-Term`). TO-W2-3's amendment text is changed to the union; the
  function and tests do not change. The order's grant gains this decomposition file so the worker's branch carries cell `ST-w-4`
  (row D1-W6-S3). Graded by: to-pipeline-gate on the modified order.
