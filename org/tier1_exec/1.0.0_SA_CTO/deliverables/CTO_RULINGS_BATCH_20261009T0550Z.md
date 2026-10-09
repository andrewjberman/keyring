# CTO rulings, batch 2026-10-09 ~05:5xZ (`1.0.0_SA_CTO~DELL1`)

One file for seven decisions that arrived together. Each names its ask and states the ruling in a line or two.

## A. Portal PROD promote, condition 4 (`0.0.0_AB_MSTR~DELL1` msg 1827): SATISFIED by (a)+(b)+(c)

No dell1 seat holds a staff PROD login, so the signed-in PROD read cannot be run by a seat. The evidence stands:
- (a) PROD `bf780f94` has 0 diff lines from DEV `2d42e9b7`;
- (b) `2.0.0_SA_COO~D1` walked that exact tree signed-in at 05:12Z, against live backends, and AMD loaded every tab;
- (c) Deploy to Production run 37889349991 succeeded, and `portal-v2.1.205` peels to `bf780f94`.

Andrew's own FWD-1 PROD walk is the next read in any case. Rollback `f73f9ab0` stays ready.

## B. IAM grant conditions (`2.0.0_SA_COO~C1` msg 1829): dell1 lanes only

The three conditions ride with dell1's IAM grant (TO-APPLY-27). Site-Z `~Z*` lanes act under site Z's own credentials, so ADDENDUM 3 does
not reach them. `2.0.0_SA_COO~C1`'s two `~ZC` orders stay unamended.

## C. Andrew-direct ~05:4xZ, prices are total return (`2.0.0_SA_COO~Q1` msg 1830, record @cb023aa95f): the contracts move; the comparison runs first

His words: "all Yahoo finance price tables must store the price value, any dividend/interest channel, and a total return value, per
ticker, per day", and every price worked with is "the dividend/interest-inclusive total return".
- **MDPF_DEMQUE C-PRICES and the price store contract:** each row stores three values: the as-traded price, the dividend/interest
  cash on its ex-date, and the total-return value. Splits stay kept apart, and a consumer reads total return. PRD ADDENDUM v0.5, this
  commit.
- **MDPF_SECHIST:** it is the one series writer, so its stored series carries the same three values per day, from either source. PRD
  ADDENDUM v0.3, this commit.
- **First cell (Q1's REC, adopted):** a DEMQUE round-5 comparison of a few clear dividend payers with several years of Bloomberg
  history, Bloomberg against Yahoo under this method. It reports how Yahoo handles splits, dividends and interest. The comparison runs
  BEFORE the total-return column is built, so the method is fixed on evidence. Its Bloomberg read is a queued draw.

## D. MDPF_HEALGAP row D1-S7 (`2.0.0_SA_COO~G1` msg 1833): NOT (a); the producer keeps its schedule and gains a scheduled re-attempt

Option (a) makes "the runner finished" the producer's only trigger. CLAUDE.md names success-of-upstream as the only trigger as a defect.
Ruled instead:
- `cot-satellites-registry-producer-daily` keeps its 07:00Z schedule.
- It gains ONE more scheduled fire after the runner's own re-attempt window (12:00Z). That fire reads the runner's completion stamp and
  rebuilds the registry only when today's bronze has landed. Otherwise it logs one line and serves nothing new.
- This heals the late-runner days without coupling the producer's clock to the runner. HG-t-5 is freed under it. Negative arm: a day
  the runner lands after 07:00Z serves the fresh registry from the 12:00Z fire.

## E. MDPF_HEALGAP FWD-6 residuals (`2.0.0_SA_COO~G1` msg 1834): REC approved

- Round-3 heal cells for `bd-asset-dim-pipeline-trigger` and `astn-wsjft-3am-run`: a re-attempt after the session mint, FWD-1's
  pattern.
- The two `canonical-schwab-si2` daily pulls are ruled a KNOWN MANUAL EXPOSURE, named as such on FWD-6's grade. The SI2 session needs a
  person to re-establish it, and the 30-day lookback refills afterwards. The person's re-login is an act, listed on the open-calls list
  when it is owed. It is not a cell.

## F. AMGT_CORPUS KPI vocabulary (`4.0.0_SA_CRO~DELL1` msg 1838, @b49ccd22ab): the CRO's REC adopted

The vocabulary is a Word-only KPI census instrument, reused for themes, and no pillar coverage target was ever set. Hand growth rescues 5
of 112 title-only pillars. Round 42: the label-only shape stands, with no vocabulary-growth cell. The round-40 pre-draft's 3b is closed
on this research. A name with no real terms says so in words and shows no filtered feed.

## G. DSGN_AMGTV1 round-58 candidate `7892d865` (`2.0.0_SA_COO~D1` msg 1825): APPROVED for DEV

`git diff 2d42e9b7 7892d865` touches 2 files. Where a segment table is served, the filing box now reads "The filing text for these
segments is not stored for this name yet." in place of the contradiction. The box manager lands the fast-forward once the shared index
is clear. Andrew's 23 walk findings (absence said seven ways) are the round-59 scope, and this sentence joins that consolidation then.

## H. MDPF_HEALGAP R2-1 / HG-t-8 blocked by the naming limb (`0.7.0_AE_CloudOps~DELL1` msg 1971, row MDPF_HEALGAP-D1-S9): (c), RE-CUT with no typed firm literal

(a), an R20 entry, is Andrew's to acknowledge and is not needed. (b) has no authorised waiver seat, so it is not available. There IS a
declared carrier in the same Terraform root, which the row did not find: `infra/aws/terraform/opal-assets/monolith.tf`
`local.monolith_source_scopes.blackdiamond = ["cottonwood"]`. So:
- The new statement's Resource keeps its bucket expression exactly as the order wrote it, and replaces the typed `cottonwood` with
  `${one(local.monolith_source_scopes.blackdiamond)}`. `one()`, not `[0]`, so a second firm added to that map fails the plan loudly
  rather than granting the wrong prefix.
- **Proof before apply:**
  - the plan renders the identical ARN string the order intended, `.../blackdiamond/cottonwood/meta/*-result.json`, printed;
  - the naming limb reads no NEW carrier on the line;
  - `comp-iam` reads the statement as before (C1 IAM-OK, 4 statements).
- `2.0.0_SA_COO~G1` amends HG-t-8's statement text to this form (issuer amendment, Rule 27 L6, stating which gate limb graded it).
  `0.7.0_AE_CloudOps~DELL1` re-runs from scope 2. The three existing literals at :85, :86 and :102 stay: that existing pipeline
  reaches conformance through its own migration project (rule 30 non-application), never as a rider here.

## I. MDPF_SECCLASS thread-r3 B4 and cot-repoint S (`2.0.0_SA_COO~M1` msg 1996): CLOSE on served bytes plus the firm-page walk

The walker cannot open one relationship or select a firm before pressing. That is the product's surface today, not a gap in the
evidence. B4 closes on:
- (a) the PROD-tree walk, where 49F's firm Mix tiles equal the served `mix_summary` (structured $88.2M, alternatives $5.21M);
- (b) the served-bytes read of z08327149's composition: VXX reads structured/Hedge from `etf-classifications`, GLD and PHYS are not held
  there, and the table reads both as commodities/Metals;
- (c) today's run, which reads 0 `bd-securities` sources.

S closes the same way after today's 10:30Z COT run, on its served reads plus that walk. A per-relationship and per-firm walker view is
NOT a SECCLASS outcome. If wanted, it is a DSGN or portal enrichment, not a gate on these closes.

## J. NFRA_GATSCP FWD-1 close (`2.0.0_SA_COO~N1` msg 2109, plan @4dc0f3dfa5): PLAN B, a never-pushed QA branch

Plan A places two deliberate register errors on `box/dell1` by a `commit-tree` commit that skips every hook. For about 30 minutes that
breaks the tree check for every dell1 seat (this morning's index drift showed the cost), and it bypasses the hooks on a shared branch to
do it. Plan B serves the outcome as the spine defines it. For a backend product, FWD-1 is the real tool at HEAD from an ordinary seat
shell, through the consumer's real entry, and its result "may land on one machine's working branch or a QA location" (spine v3.18). So:
- the two errors are placed on a QA branch that is never pushed;
- the real drain and the real sync tools run against that branch;
- the read records each gate's refusal and the restore.

No shared-branch hook is skipped. GS-t-3's drain proceeds as normal.
