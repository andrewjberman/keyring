# CTO ROUND-81 ANALYSIS -- ADVI_COTBKF -- answering the round-80 L10 slug (2026-10-13 ~16:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7077, `surprise-channel/remediations/REMEDIATION_v49.md` @7aceb5d4a1. L9 both
PASS. Row `ADVI_COTBKF-D2-W155-S1` (served price errors) has graduated ARMED to this seat. **Prior:** round-80 analysis. **No PRD
addendum this round.** The backfill floor below is Andrew's law and binds by reading.

## 1. What round 80 did

- **CB-cb-1** found SERVED price errors in the minted copy:
  - APH served at 0.50 of the store on 48 account-days (one account, 2025-02-11 to 2025-04-21);
  - CTVA at 0.150 of the store on 115 account-days;
  - HON's two served copies disagree (S3 folds in);
  - in all, five securities are off 1.0. The cause is not established; none of the ratios is a split ratio.
- **CB-cb-2:** dell1 landed 7 of 15 funds; 8 were rejected `LOW_TRADE_AGREEMENT`.
- **Cell 3** merged. The issuer disarmed W155-S1 on D2-S131's hold, without re-measuring the minted table's readers. The CVO refused
  that disarm.

## 2. Rulings

1. **W155-S1 stays ARMED, with this seat as owner, and its disarm is one of two measured facts.**
   - **(a)** A read of EVERY consumer of the minted table finds none. Use the dependency graph first (CLAUDE.md rule 20), then each
     consumer's own code or config. A consumer with a page means a person sees these prices.
   - **(b)** The served prices are corrected and re-read.

   If (a) finds no consumer, the row disarms and the correction is ordinary work. If it finds one, the correction is this
   project's first cell after it, and it moves served output only under a never-widen pair.
2. **Cause, by stage, not by ratio.** A whole split ratio was the wrong lens: 0.150 and 0.50 are what the served value is AFTER
   some stage. For each of the five securities, on one served day each, read the value at every stage that touches it: vendor
   Close, store row, build price, minted copy, served row. The first stage where the ratio leaves 1.0 is the cause's address.
3. **Andrew's backfill law (ANDREW_DIRECT_20261013_141xZ, record @82c7c92449 on box/dell1, with its two addenda) binds this
   project from now on:**
   - a client account's history starts at its earliest record in the system, and nothing earlier is read, built or served;
   - nothing before 2012-01-01 under any account;
   - a non-client need takes 365 days before the point of the need.

   The decomposition's date bounds are re-read against this. A cell whose window begins earlier is narrowed at its next cut, not
   re-run.
4. **OPEN_CORRECTIONS `closes_when`** still quotes v0.9's split arm. The issuer amends it to v0.10's wording in this round's issuance
   commit, and states that no gate limb graded it.
5. **The build series after 2026-06-05** (row: one-day steps on APH, CTVA and KLAC) is read under item 1: does that range feed anything
   served? If not, it is held; it is not a defect until it is served.

## 3. ENRICHMENT LIST for round 81 (ONE issuance)

1. **The consumer read of the minted table** (ruling 1a). Graph query, then each consumer's code. Report: consumers, each with
   whether it serves a page and which dates it reads. 0 consumers needs a positive control: the graph names a known consumer of a
   sibling table.
2. **The stage read** (ruling 2), five securities, one served day each. Counts and ratios only, with no account value.
3. **The date-bound re-read** (ruling 3): each cell window and each built partition range in the decomposition, against the earliest
   client record and the 2012 floor. Report which bounds move. Nothing is deleted here.
4. **The `closes_when` amendment** (ruling 4), in the issuance commit.

## 4. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2
