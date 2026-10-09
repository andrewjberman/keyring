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
