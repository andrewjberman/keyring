# MDPF_SECCLASS round 8 -- the CTO's L10 answer (round-N analysis, round 9's enrichment list)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07, under laptop `1.0.0_SA_CTO` ruling 106047 (1): a Dell CTO writes L10 for its box's projects.
**Input:** `3.0.0_SA_CVO`'s slug msg 179 (`surprise-channel/adjudications/ADJUDICATION_v7.md` @cb765997e2, which closes on ADJUDICATION_v6 and
`remediations/REMEDIATION_v6.md` @dde7a18c30; 18 of 18 orders terminal at `q/dell1/secclass-r8/r3`; 0 BLOCKING; S50 DISARMED);
`2.0.0_SA_COO~M1`'s drain-end packet `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R8_20261007.md` @572829ce3b.
**Output:** this analysis plus PRD ADDENDUM v0.13 and FWD-12's amended title (same commit). `2.0.0_SA_COO~M1` recuts round 9 in ONE issuance from section 4.

## 1. Coverage read, per outcome (proof-of-spec at HEAD, CVO compile)

| FWD | Grade after round 8 | Why |
|---|---|---|
| FWD-1 (thread) | LIVE for IR Holdings; NOT LIVE for BD pages | unchanged; the BD writer stops wait on the reader switch (FWD-5 order) |
| FWD-5 | NOT REALIZED | SC-e-38 measured 5 readers that need the old list; no canonical producer has a live write (W25-S6) |
| FWD-9 | NOT REALIZED | history half unfilled (W15-S1); 7 stocks have no Bloomberg id (W14-S5) |
| FWD-11 | NOT REALIZED | no current held input on dell1 (W26-S3); the first model run is unsigned (e31/e32 half) |
| FWD-12 | NOT REALIZED | the one source covers 114 of 3,507 rows (S44); ruled in section 2.1 |
| FWD-14 | NOT REALIZED | 2,624 unnamed rows (S45); clean_name defects (W28-S5) |
| FWD-15 | NOT REALIZED | 1,046 held with no old row (W26-S8); ruled in section 2.3 |
| FWD-16 | NOT REALIZED | 3 screen disagreements (W23-S2) |
| FWD-17 | NOT REALIZED | population and held definition open (W25-S2); cash unreachable (W26-S6) |
| FWD-2,3,4,6,7,8,10,13 | as at round 7 | no round-8 cell graded them |

## 2. ENDPOINT rulings (PRD ADDENDUM v0.13 carries 2.1 and 2.2; the rest are contract notes)

2.1 **S44, FWD-12's population.** FWD-12's DONE WHEN and ACCEPT grade "every holding in an ETF's view". Its title's "each security"
over-reads them. Amended in place (id unchanged): the shared list carries the sector and industry group of each security an Opal ETF
holds. **What is no longer promised:** a sector on rows no Opal ETF holds (rival-fund stocks, client securities, unheld old rows). The
source stays the Bloomberg characteristics leg the ETF producer already reads. The round-9 census grades coverage over the four Opal
ETFs' held universe. A held security the leg does not return is a C-PULL cell at site Z under the daily vehicle's existing vendor use;
nothing is guessed from a name.

2.2 **S45, FWD-14's source.** No wording change: FWD-14 grades names "beside each holding". The source for a held row with no name
is the custody feed's security name for that position, passed through `clean_name` once W28-S5 is repaired. An AI-made row keeps
FWD-11's clean name. Unheld unnamed rows are not graded by FWD-14.

2.3 **W26-S8, FWD-15's 1,046.** The path is FWD-11's producer run over FWD-15's own list (held, no entry, per firm), held-first, after
the direct-match plan. Vendor: FWD-11's recorded word (ADDENDUM, C-VENDOR at :433), the same model and the same payload (name and
ticker); no new word is needed for it.

2.4 **W25-S2, FWD-17's population and "held".** The population is the whole old list, held or not (FWD-17's own ACCEPT: "held today or
not"), counted at the round-9 census with its denominator. "Held" means present with a non-zero market value in the latest served
holdings partition of any of the three firms on the census as-of. It is read by a seat whose principal the firm buckets admit (2.9).
The "58" is retired as a stale count.

2.5 **W26-S6, cash.** The contract's closed `sub_asset_class` list is the bound for every class, cash included. A DIRECT or AI verdict
lands if it is a member of the contract's list, not only of the values the table happens to hold. The 15 old cash rows are re-planned
under that bound.

2.6 **W24-S2, sectors.** 11, as GICS defines them: Real Estate is added to the contract's `gics_sector` values with its pinned test and
the issuer's check.

2.7 **W24-S1, vendor spellings.** The contract's closed industry-group list carries the full GICS names. The writer maps the vendor's
30-character spelling to the full name through a decode table declared in the same contract file. A spelling not in the table leaves
the field empty, and the row is listed.

2.8 **W23-S2, the three screen disagreements.** Each is a FWD-16 cell in round 9's list (the IR securities table's Cash fold,
PerfrpAllocation's raw class labels, and the third screen the census named).

2.9 **W25-S1, dell1 cannot read the firm buckets.** Access is the laptop's (roles and policies, ruling 106047 (1)). Until a read-only
grant lands, dell1 grades every held set as `inferred`, and a grade that needs the served bytes is read by a laptop seat and filed
as a row. The read-only request goes to the laptop as a C-ROLE-REQUEST from `2.0.0_SA_COO~M1`.

2.10 **W25-S6 and packet item 3, FWD-5's order.** It confirms this seat's SC-e-35 refusal (@a92652a41a). No old-list writer stop
uploads until every real reader resolves canonical-first and names a canonical producer with a live write count above 0. W25-S5
widens the reader census to `data/black_diamond` and to runtime-assembled names first.

## 3. Rulings on the rows that ask this seat

- **C-S13 (49F $6.5M in no class):** the residual is served as its own line, "Unclassified", so the top-level mix sums to 1.0. That
  matches FWD-13's rule that a security the list does not hold is shown as unclassified. Owner `2.0.0_SA_COO~M1`; a served move under
  its own pair.
- **S27:** YES. After a symbol miss the producer falls back to `CUSIP:<security_id>` (C-IDENTITY: the CUSIP rows exist for exactly
  this). It is a served move under never-widen.
- **S28:** the producer stops writing a GICS sector into `sub_asset_class`. Sector lands only in `gics_sector` (FWD-12). An existing
  row is not rewritten before FWD-12's writer runs.
- **S30 (Inflection AUA 1.873x):** outside MDPF_SECCLASS, since it is not a classification defect. It goes to the laptop
  `1.0.0_SA_CTO` for placement (placement is the laptop's), with the row as its evidence.
- **W14-S5 (7 rival stocks with no Bloomberg id):** they get TICKER-namespace rows (the bare-ticker key form C-IDENTITY already
  admits), classified by the direct plan, then FWD-11. FWD-9's domain is not narrowed.
- **S47:** fixed in ADDENDUM v0.13's manifest note: S13's four files sit under `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/`
  and `.../yang_pipeline/positioning/`, and `01_market_overview/lambdas/`; S26 under `.../yang_pipeline/positioning/yang-generate-positioning/`.

## 4. Round 9 -- the ENRICHMENT LIST, in order (M1 cuts it in ONE issuance)

1. W25-S5 then FWD-5: the widened reader census, then one reader-switch cell per real reader (canonical-first, producer named, live
   count). The writer stops SC-e-35/36/37 re-issue only after that.
2. SC-e-29 (FWD-12, ETF view): after SC-e-28's apply and the issuer's sector write, the build runs on dell1 and the release at site Z
   (ruling 106047 (2)), under 2.1's population.
3. W28-S5, then FWD-14 (2.2): repair `clean_name`, regenerate the e34 row set, then the clean-name write under its pair.
4. FWD-15 (2.3) and FWD-17 (2.4, 2.5): the per-firm missing list, then FWD-11 over it held-first; the whole-old-list census under the
   held definition.
5. FWD-16 (2.8): three screen cells.
6. Contract edits (2.5-2.7): one cell, with tests.
7. C-S13, S27, S28: producer fixes, each a served move under its own pair.
8. Carried: S11 (resolve_tickers run, vendor check first), S14, S15, S20, S22, S29/S36 reads, W13-S1/S3/S5, W15-S1/S2, W16-S3/S4,
   W20-S1, S32, W22-S1, W23-S5, W24-S3/S4/S6, W25-S3/S4, W26-S3/S7, S49 (worker faces forbid every install and download). S46 closes on
   its own condition: the six-class module is on CLOUD and in both firm buckets (ETag 3a033c04 read by this seat at 10:5xZ), and the
   low_confidence answer is recorded as option (b), no seed run (CTO half @b39e54dc9e). M1 files the closing row.

## 5. Not decided here

- Andrew's acts: none new. FWD-5's final delete stays his (FWD-5 DONE WHEN).
- The ratified-text half re-opens for `3.0.0_SA_CVO` on 2.1 (an ENDPOINT wording change).
