# ETFS_RIVALS -- ROUND 10 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~01:0xZ

**Input:** CVO~RV slug msg 29838. Compile `surprise-channel/adjudications/ADJUDICATION_v10.Z.md` @85301da213; there is no
REMEDIATION_v10. Review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R10_REVIEW_20261006.md` (77 lines, read in full).

## 1. WHAT THE ROUND DELIVERED

| cell | state |
|---|---|
| RIV-eg-1, S25's guard (no all-empty or all-error G4) | **Live** on the Terminal vehicle from the shared tree (equal to 0997603f5d). There is no Lambda leg. AC1 re-run by the CVO: PASS 0 |
| RIV-iam-1, the round-9 table grants | **Applied** (CTO half @4e9b59ea50, ledger CLOSED). Simulate reads allow on the 4 grants and deny on both negative controls. My read: live equals AFTER on both roles |
| RIV-ok-1, one key per security | Drained, **not deployed** (round-9 addendum 2) |
| RIV-rp-2, the code-class replay tool | Drained. The dry run moves 1,323 rows in the 4 classes and 0 outside them. **The served replay is held** on `_g5_target` (rows Z-W3-S23 and Z-S42) |
| The Z-S31 repair | Live @409b855114 |
| D12 Step B | CLOSED 8/8 |

**Round 10 is CLOSED.** Nothing graduates.

## 2. GRADES (CVO~RV L9)

| item | grade |
|---|---|
| RIV-ok-1 J1 | **NOT_EVALUATED.** Moved to round 11 by addendum 2, because it is not served |
| Z-W3-S22, rp-2 AC1 (b): labels and fills | **CONFIRMED, with condition C-S42.** 4,950 rows (9,892 cells) of G1 revision labels and 5,287 filled cells move. Both are effects of the 4 classes, and 0 trade-fact or G3 label cells move outside them |

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **C-S42 and the review's s.5:** the dry census records no G5 keys, so a G5 written between the dry run and the served replay would change the base unseen | **Adopted as written.** The served replay's never-widen half lists, PER FUND, the relabelled rows and filled cells (4,950 and 5,287 in total) in its blast radius. At its own start it records the newest G5 key per planned date and re-runs `plan` against those keys. It **STOPs** if any key differs from the plan's. W6-S2's first-window precondition rides the same half. |
| 2 | **C-S38:** `g5_drift.json` still attributes the 9,467-row data-arrival class to cause commit `4fa3e25f5e` | **A round-11 record fix.** Re-label that class's cause as "data arrival (later G3 pulls)" in the drift record, per round-9 ruling 3. It moves no data. |
| 3 | **P2: the 2026-10-06 vehicle carries six proofs** (eg-1 live, nm-3 names, S24's budget, the D12 leg, iam-1's first data run, S31's disarm) | **One read grades all six,** at the CVO's 13:30Z read, after MSTR~Z's 10:45Z P0 probe (round-8 ruling 1). A capacity refusal is ONE cause, never six findings. A blocked Terminal falls back to the pre-signed interim restore (round-9 ruling 2). |
| 4 | **The NBIS label** ('NBIS US Equity' against 'NBIS_US_Equity') | Graded with ok-1's round-11 J1, as the review routes it. |

## 4. ENRICHMENT LIST (round 11, ONE issuance by `2.0.0_SA_COO~RV`)

1. **`_g5_target`, FIRST.** A same-input pass at a NEW code version writes a new revision; at the SAME code version it still writes
   nothing. Both arms are the criterion (round-9 addendum 2).
2. **The served replay** of the 4 code classes (1,323 rows), under a pair carrying ruling 1. Proof: a census in which only those 4
   classes, plus their labels and fills, move.
3. **The ok-1 deploy, AFTER the replay.** Its J1 includes the NBIS label.
4. **The C-S38 drift-record fix** (ruling 2).
5. **The six first-run reads** from the 2026-10-06 vehicle, graded once (ruling 3). This is a grade, not a build cell. S31's disarm is
   `2.0.0_SA_COO~RV`'s at that run.

## 5. ACTS FOR ANDREW (cited)

None. The vehicle's Bloomberg use runs under his existing word for the OPAL_BBGTML pull. The backfill ran under "Backfill is approved
for IDVZ/PFOE" (@4bd948e824).

## ADDENDUM 1 (2026-10-06 ~02:5xZ) -- item 3, the ok-1 deploy, is a no-op on live data (COO~RV msg 29868, row Z-S43 @f75c6e02d0)

**The finding.** ok-1 joins on CUSIP/ISIN, but the duplicate pairs do not share one:
- WCMG's Nebius row in G1 is `NBIS_US_Equity` with no CUSIP or ISIN;
- GQGU's is CUSIP `N97284108` plus ISIN plus ticker NBIS.

A 10-05 refresh publish at the ok-1 code is byte-identical to the control, and Nebius shows twice in both. Broadcom and Intuit are not
duplicates.

**Ruling: (A).**
1. **Hold the ok-1 deploy.** (B) is refused: a deploy measured to change nothing adds a deploy's risk for no effect.
2. **Round-12 cell:** add Bloomberg's own key (`PARSEKYABLE_DES`) to the EXISTING G4 reference request for each CUSIP/ISIN-keyed
   security, and ok-1's join reads it.
   - This is one more field on the vendor leg Andrew already worded. There is no new vendor leg.
   - It stays **inside S24's daily budget**, with the added points per run measured and printed.
3. **The census is not only Nebius.** After the field lands, list every (CUSIP/ISIN key, ticker key) pair the join merges across all
   funds, with a count. A name merged that is not the same security is the failure arm.
4. **ok-1's J1 is graded after that deploy,** under its own pair. The NBIS label from ruling 4 rides it.

## ADDENDUM 2 (2026-10-06 ~11:5xZ) -- RIV-e-1 eats the vehicle's window when Bloomberg is down (MSTR~Z msg 30005)

**A correction of mine first.** At ~11:2xZ (msg 30002) I told COO~RV to leave RIV-e-1 retrying, "it proceeds on its own if Andrew
signs in". That premise was false. `OPAL_BBGTML_daily_pull` has `ExecutionTimeLimit PT30M`, and Task Scheduler killed it at 11:30:01Z
(Last Result 0x41306). So a sign-in does not resume it. The names stage and the D12 leg never ran today. Recovery is MSTR~Z's re-run on
the first OK probe after the sign-in.

**The finding.** With the DAPI precondition already FAILED (the vehicle logged it and skipped the pull), RIV-e-1
(`rivalfunds.enrichment_bloomberg`) still ran. It retried blpapi sessions about once a minute until the 30-minute kill, so every stage
after it lost its turn.

**Ruling: a round-12 cell for `2.0.0_SA_COO~RV`, beside the PARSEKYABLE_DES cell (ADDENDUM 1).**
- `enrichment_bloomberg` bounds its session attempts (a small fixed count) and exits with a DISTINCT code when Bloomberg is unreachable,
  so the vehicle reaches its later stages.
- First measure whether the names stage and the D12 leg need Bloomberg. If they do, the bound still matters: a failed day then ends in
  minutes, with each stage's own clear refusal, instead of one silent timeout.
- eg-1's guard is unchanged (no empty G4 lands).
- **The change is in `data/etfs/scripts/rivalfunds/`, which is ETFS_RIVALS's own code.** The vehicle script under
  `integrations/bloomberg/` is under Andrew's no-modify order and is NOT touched.
- **Proof:** a plant with blpapi refused, in which the module exits within the bound with its distinct code, plus a control in which a
  reachable session still enriches.

## ADDENDUM 3 (2026-10-06 ~16:4xZ) -- Z-S47: every ticker mention links to its modal (COO~RV msg 30147)

**Andrew's word:** `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261006_163xZ_RIVALFUNDS_SECURITY_LINKS_GONE_EVERY_TICKER_MENTION_LINKS.md`
@05c469e083. **Cause, as COO~RV measured it:** the served 10-05 and 10-06 pages carry `data-holding-dialogs="off"` and 0 links. The
all-or-nothing fallback at `render.py:1793-1802` (`DIALOG_SOFT_CAP` 1,950,000 B, set under the gateway's 2 MB refusal) strips every
dialog once the page is over the cap. The closed audit block is 1,119,671 B of the 1,813,001 B page.

**Ruling: route (B), a round-12 cell for `2.0.0_SA_COO~RV`.** The audit trail moves to its own dated object, and the main page keeps
every dialog.
- **Why not (A).** "Latest N trades per fund" removes trades. FWD-5's DONE WHEN reads "for every fund Andrew reads its trades", and the
  trade log is that outcome's carrier. FWD-18 asks that trade detail and holdings lists "stay one step away", which allows them to
  move, not to be cut. (A) also leaves the cap to bite again as the log grows every day.
- **Why not (C).** Partial dialogs leave dead text. That breaks FWD-21's ACCEPT ("no ticker on the page is dead text") and Andrew's
  "any mention".
- **Round-8 ruling 3 (link once per face) is SUPERSEDED** by Andrew's word: every ticker mention is a link. The cost is a button per
  mention. The dialog count does not change, because dialogs are written once per security by `_sec_dialogs`.

**The cell's shape:**
1. **Renderer** (`data/etfs/scripts/rivalfunds/`):
   - The publisher writes a second platinum object for the day, the audit trail (trades, holdings, status). Its address is
     `lib/opal_naming.py` output, never typed (rule 30).
   - The main page replaces the closed block with a plain link to it, keeping the "one step away" wording.
   - The modals open by `popovertarget`, which works within one document only. So the audit page carries its own dialogs for the
     securities it names, from the same `_sec_dialogs`. The no-script rule holds on both pages, and FWD-21 holds on both.
2. **Gateway** (`infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` plus the read policy from `gen_rivalfunds_location.py`):
   - Add one route, `GET /rivalfunds/YYYY-MM-DD/audit`, behind the same identity wall.
   - This is a deploy under a never-widen pair. The publisher's switch to the split page lands only after the route serves, so
     the link is never a 404.
3. **The fallback stops being silent.** Over the cap, the pre-publish check prints the dialogs-off state as a FAIL line. The day still
   publishes, and a surprise row is filed. A silent strip is what hid this defect.

**Proof:**
- On the 10-06 data, the main page renders with every dialog and at least 20% headroom under `DIALOG_SOFT_CAP`. Print the bytes.
- Every ticker mention on both pages is a `popovertarget` button whose target exists in the same document. Print the count of
  mentions, the count of buttons, and 0 dead.
- The audit page serves through the gateway, signed in.
- A planted over-cap page prints the FAIL line (the failure arm).
