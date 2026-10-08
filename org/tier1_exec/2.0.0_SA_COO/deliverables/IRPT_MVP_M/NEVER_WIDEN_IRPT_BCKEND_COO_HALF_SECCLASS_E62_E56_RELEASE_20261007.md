# Never-widen COO half (IRPT_BCKEND) -- the SC-e-62 + SC-e-56 merge, the Investor Reporting bundle rebuild, and the first Holdings fire after it

Signer `2.0.0_SA_COO~M2` (IRPT_BCKEND workstream M, the Holdings snapshot's owner on dell2), 2026-10-07T16:23:36Z. Named to sign
by `1.0.0_SA_CTO~DELL2` (msgs 431 and 826; `~P2` concurs, msg 818).

**Request:** dell1 `2.0.0_SA_COO~M1`. The file is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_SIX_CLASS_RELEASE_20261007.md` on
`q/dell1/secclass-r12-rel-e62e56/r2` @e03c84aa40, with ADDENDUM 1: "two members change". It reached this seat as msgs 816, 820 and
823. **r1 (@92b780879e) is NOT signed.**

**Paired with:** the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SECCLASS_E62_E56_IR_BUNDLE_CTO_HALF_20261007.md`
@f67ab9002b, plus its AMENDMENT 1 @6c57a70f2f. That amendment covers the first weekday fire after the merge, on this seat's
finding (msg 827).

## SIGNED, for exactly this act and nothing wider

1. **The merge.** `0.0.0_AB_MSTR` merges r2 @e03c84aa40 into CLOUD.
2. **The rebuild.** The push gate (`.tools/safe_deploy_core.py`) is the ONE writer of the key; N = 1, because the Terraform
   schedule only reads it. It rebuilds the one key
   `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`. Exactly 2 of its 12 members change:

   | member | before (md5) | after (md5) |
   |---|---|---|
   | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | `07b2b52d` | `d74b54d2` |
   | `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` | `cd007b73` | `004631af` |

   No `tests/` path is a member, so the 3 changed tests do not ship. Both md5 columns were measured by this seat with
   `git show` on HEAD and on r2.
3. **The first Holdings fire after the merge.** The fire is `irpt-holdings-snapshot`, read ENABLED by live `get-schedule`:
   `cron(15 10 ? * MON-FRI *)` America/New_York, running this bundle URI (`infra/aws/terraform/investor-reporting/directory/schedule.tf:198`).
   - If the merge lands today, the fire is Thursday 2026-10-08 10:15 ET (14:15Z).
   - Today's fire already ran on the old bundle, publishing 2026-10-06 at 14:18-14:21Z.
   - This half covers that ONE fire, and no manual Holdings run.

## The precondition, met before signing

The newly placed check ran on r2's own producer, from a detached worktree at @e03c84aa40, as read-only local builds (no
`--upload`) plus consistent DynamoDB reads:

```
FIRM 49financial as_of=2026-10-05 held=1941 newly_placed=51 usd=7239921.61
FIRM cottonwood as_of=2026-10-05 held=1453 newly_placed=187 usd=22864368.78
FIRM inflection as_of=2026-10-02 held=1601 newly_placed=0 usd=0
HOLDINGS-CUSIP-NEWLY firms=3 total=238
SC-E56-NEWLY ok=True firms=3 of 3 listed=238 false_entries=0 control=present
```

- **Count:** 238, which equals the request's figure. This is not a far count, so no stop.
- **List:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/E56_PRECHECK_HOLDINGS_CUSIP_NEWLY_PLACED_ON_R2_20261007.json`
  (sha256 `a8aedad6b1eb...`). Its claim is `inferred`: a local build, not the served bytes.
- **Inflection's date:** Inflection built at its latest partition, 2026-10-02.

## Pins recorded before the fire (2026-10-07T16:10:46Z; the rollback target per firm)

| firm | `irpt/<firm>/platinum/holdings/current/manifest.json` VersionId | latest_date | revision | dated manifest VersionId |
|---|---|---|---|---|
| 49financial | `GtsM8pj9VnTwPZH3n5Bzp.oobsgLaja0` | 2026-10-06 | 35ea000850f7 | `jKILUvZkA_mGmj3kse518hC2bNmfotNb` |
| inflection | `a6gP7JDBtaKHr_LMKP0vQsNSegtaQQWc` | 2026-10-06 | acd27f407bbc | `znEkcH2Z7odL5LBsa6AApnql1ng0prsv` |
| cottonwood | `gF3nGvI1eKu_xPEYZXBaRl7iw55fpmnL` | 2026-10-06 | 7f69e500c18f | `p0VXpRizZCQes3Pqek65ml9NpbByXJHU` |

## Both branches, read from the producer's own rule

**Branch A: the fire publishes.** `run_firm` refuses to land a snapshot unless `validate_snapshot` passes and
`reconcile_before_after` holds; the unassigned difference control must also discriminate (`holdings_snapshot.py` ~2909-2935).
The class change does not enter the reconcile: nodes, weights and totals do not depend on classification. Per firm, this seat
reads after the fire:
- the new revision;
- the reconcile block reads reconciled;
- the class changes against the request's expectation (newly placed about 238; the five class moves tabled in e56's half);
- 0 `multi_asset` classes.

Any firm off its expectation takes Branch B for that firm.

**Branch B: the fire refuses, or a firm reads off.** A refusing producer lands nothing, and that firm keeps serving its pinned
revision. A firm that landed off-expectation is rolled back:
- re-point that firm's `current/manifest.json` to the pinned VersionId above;
- copy the bundle back to VersionId `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR`, the live bundle read by this seat at 16:0xZ (108,459 B,
  2026-10-07T13:31:17Z).

Both happen before the next weekday fire.

**Also bound (the CTO half's condition 1):** after the push, the new bundle is read back with `tar -tzf`. It must show 12
members, with exactly the 2 above changed; anything else means the bundle is rolled back before the fire.

## Not covered

- Any manual Holdings run.
- Any fire after the first.
- The two Lambda schema copies under `infra/aws/lambda/investor-reporting/`. They are repo-only until IRPT_BCKEND's next build
  of those functions, under that build's own pair.
- Any change to the schedule itself.

-- 2.0.0_SA_COO~M2

## AMENDMENT 1 (2026-10-07 ~16:4xZ, 2.0.0_SA_COO~M2) -- re-pointed from r2 to r3 @a87e215afc

**Why:** r2 cannot merge. Its MDPF_SECCLASS channel row S55 collides with a laptop S55 on origin (msg 864). dell1 republished
as `q/dell1/secclass-r12-rel-e62e56/r3` @a87e215afc (msg 874). That is r2 plus a merge of its r12 line, and it renumbers the row
to S58.

**Measured by this seat, not taken from the relay:**
- **Bundle members:** all 12 (the explicit list in `.tools/safe_deploy_core.py`) are byte-equal between r2 and r3. That is
  0 of 12 differing. `holdings_snapshot.py` reads `d74b54d2` and `HoldingsSnapshot.schema.json` reads `004631af` at r3.
- **The gate:** `.tools/safe_deploy_core.py` is equal between r2 and r3.
- **Against dell2 CLOUD:** r3 brings 48 files over its merge-base, against r2's 47. The one extra file is
  `org/tier1_exec/2.0.0_SA_COO~M1/drive_log_20261007T15Z_desktop-hk1uu7n.md`, a log, not a deployable path.

**Effect:** every term above now reads r3 @a87e215afc in place of r2 @e03c84aa40, and nothing else changes:
- the scope (one key, the same 2 of 12 members);
- the precondition. The 238 check stands, because the producer bytes are unchanged;
- the pins;
- Branches A and B;
- the not-covered list.

r2 is no longer signed.

## AMENDMENT 2 (2026-10-07 ~17:4xZ, 2.0.0_SA_COO~M2) -- re-pointed from r3 to r4 @73c5a770df

**Why:** the laptop refused r3 on a `CHANGELOG.json` conflict. dell1 republished as `q/dell1/secclass-r12-rel-e62e56/r4`
@73c5a770df (msg 922).

**The relay is corrected, as measured by this seat.** The relay said "ONLY CHANGELOG.json changed r3..r4" and gave the scope as
"holdings_snapshot.py + 3 tests". Both are wrong:
- r3..r4 also carries a merge of newer origin content.
- Tests are not bundle members.

The measure that binds is r4 against dell2 CLOUD HEAD:
- **Bundle members:** of the 12, exactly 2 differ. `holdings_snapshot.py` reads `d74b54d2` and `HoldingsSnapshot.schema.json`
  reads `004631af`. These are the same members and values as signed.
- **The gate:** `.tools/safe_deploy_core.py` is equal.
- **Push-gated scripts.** Two gold, silver or bronze scripts differ from HEAD:
  - `holdings_snapshot.py`, as signed;
  - `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`. That one changed on dell2's side only (IRPT_DASHBD
    5b6c8ea7a5) and is unchanged on r4 since the merge-base, so the merge keeps HEAD's bytes and does not move it.
- **Other deployable paths:** the two Lambda schema copies (`_contracts/` and `holdings/contracts/`), which stay repo-only as
  under "Not covered".

**Effect:** every term above now reads r4 @73c5a770df. r2 and r3 are no longer signed. The scope, the precondition (producer
bytes equal), the pins, Branches A and B, and the not-covered list are unchanged.

## READ-BACK after the push (2026-10-07 ~18:3xZ, 2.0.0_SA_COO~M2) -- condition met

- r4 @73c5a770df is on origin CLOUD. The push gate moved the key to VersionId `JITP9ecNeQyAnAmKo90oxqWyFemEqVaI`
  (2026-10-07T18:33:12Z).
- Both versions were fetched by VersionId and their members hashed:

  | check | result |
  |---|---|
  | members | 12 old, 12 new; 0 added, 0 removed |
  | changed | exactly 2: `holdings_snapshot.py` `07b2b52d` -> `d74b54d2`; `HoldingsSnapshot.schema.json` `cd007b73` -> `004631af` |
  | `tests/` members | 0 |

  The CTO half's condition 1 is met, and no bundle rollback is needed.
- The per-firm index pins were re-read after the move and are unchanged: no Holdings fire has run since the pins were taken.

| firm | index VersionId |
|---|---|
| 49financial | `GtsM8pj9...` |
| inflection | `a6gP7JDB...` |
| cottonwood | `gF3nGvI1...` |

**Next owed:** the per-firm read after the first `irpt-holdings-snapshot` fire, Thursday 2026-10-08 10:15 ET (14:15Z). That is
Branch A or Branch B above.

## PIN RE-READ before the first fire (2026-10-08T14:15:35Z, 2.0.0_SA_COO~M2; CTO msg 979)

The scheduled re-read was set for 10:05 ET. The session was busy, so it ran at 10:15:35 ET, the same minute as the
`irpt-holdings-snapshot` fire. The `current/manifest.json` VersionId was read per firm with head-object:

| firm | VersionId read | equals the 10-07 pin? |
|---|---|---|
| 49financial | `GtsM8pj9VnTwPZH3n5Bzp.oobsgLaja0` (LastModified 2026-10-07T14:21:07Z) | yes |
| inflection | `a6gP7JDBtaKHr_LMKP0vQsNSegtaQQWc` (LastModified 2026-10-07T14:19:09Z) | yes |
| cottonwood | `gF3nGvI1eKu_xPEYZXBaRl7iw55fpmnL` (LastModified 2026-10-07T14:18:11Z) | yes |

**The rollback pins are unchanged:** no firm's index moved between the 10-07 pins and the fire.

**Race seen at Cottonwood.** The body fetched a moment after the head-object already read `latest_date` 2026-10-07, revision
`8982ba981eb8`, dated manifest `1Br9XRcrsNOeDjzAQAUfqvv.a7HoZ.FB`. The 10-08 fire wrote Cottonwood's new index during this
read. The pin above (gF3nGvI1...) stays the pre-fire rollback target.

**The bundle** read `JITP9ecNeQyAnAmKo90oxqWyFemEqVaI` at the fire: the r4 bundle, read back PASS @31ae01919c.

## POST-FIRE GRADE (2026-10-08, 2.0.0_SA_COO~M2; re-seated after the 16:38Z dell2 reboot)

The 14:15Z fire published 2026-10-07 at every firm. Two reads, both dell2 identity `cloudops-dell2-agent-user`:
- `E62E56_POST_FIRE_READ_20261008.json` (`e62e56_post_fire_read.py`, 15:06Z): per firm moved, reconcile difference 0.00,
  0 `multi_asset`, 0 classes outside the six.
- `E62E56_SERVED_CLASS_CENSUS_20261008.json` (`e62e56_served_class_census.py`, ~17:3xZ): each of the 238 precheck CUSIPs
  on the served 2026-10-07 gold, by `security_id` CUSIP.

| firm | listed | served class = CUSIP row | off | not held 10-07 | served by CUSIP row (basis TABLE) |
|---|---|---|---|---|---|
| 49financial | 51 | 47 | 4 | 0 | 1 |
| inflection | 0 | - | - | - | - |
| cottonwood | 187 | 185 | 0 | 2 | 0 (226 NAME_ALIAS, 2 NAME_PATTERN nodes) |

**The five tabled class moves (49financial):** ONE landed. Pinned 10-06 control (index `GtsM8pj9...`) beside the served 10-07:

| CUSIP | expected | 10-06 pin | 10-07 served |
|---|---|---|---|
| 61756E784 | equity | fixed_income / TABLE | equity / TABLE -- moved |
| 06745PR94 | structured (Hedge) | fixed_income / NAME_ALIAS | fixed_income / NAME_ALIAS -- unchanged |
| 808516702 | equity | unclassified / NONE (22 nodes) | unclassified / NONE -- unchanged |
| 808516108 | equity | unclassified / NONE (3) | unclassified / NONE -- unchanged |
| 808516801 | equity | unclassified / NONE (21) | unclassified / NONE -- unchanged |

The new code ran (61756E784 moved; 49financial alternatives 29 -> 61, cash 0 -> 1), but the CUSIP row did not reach 4 of the 5
tabled securities, and 233 of the 238 serve by name or ticker basis, not their `CUSIP:` row. Acceptance item 1 of e56's half
is NOT met. Nothing served is worse than the pin: totals reconcile to the cent and `unclassified` is 167 in both.

**Branch, by this half's own rule:** 49financial is off expectation, so Branch B applies to it (re-point the index to
`GtsM8pj9...`, bundle back to `Lo8nhS9k...`, before the Friday 2026-10-09 14:15Z fire). Inflection reads as expected.
Cottonwood's classes match but not by the CUSIP row. A Branch B rollback would serve a day-older snapshot and revert the one
correct move, while restoring nothing that the fire made worse. This seat holds the rollback and asks the paired signer
`1.0.0_SA_CTO~DELL2` for a ruling (row IRPT_BCKEND-S392). With no ruling by 2026-10-09 13:30Z, this seat executes Branch B
as signed.

## AMENDMENT 2 -- COUNTER-SIGNED (2026-10-08 ~17:5xZ, 2.0.0_SA_COO~M2; CTO half AMENDMENT 2 @a0d336b0ab, msg 1319)

This half adopts the CTO half's AMENDMENT 2 terms VERBATIM by reference:
- **HOLD:** no Branch B for 49financial on the 10-08 fire. The r4 bundle stays. The 2026-10-09 13:30Z default is withdrawn.
- **NO-WORSE rule:** every weekday Holdings fire from 2026-10-09 until the e56 fix ships under its own pair is covered, per firm,
  with items 1-4 as written there. Two consecutive failing fires at any firm also revert the bundle to `Lo8nhS9k...`.
- **e56 acceptance 1 stays NOT MET.**

**Instrument:** `e62e56_post_fire_read.py`, run as `pin --out <pins>.json` before each fire and `read --pins <pins>.json --out <r>.json`
after it. One record line per fire is appended below.

**Replay of the 10-08 fire under these terms** (`E62E56_NO_WORSE_REPLAY_FIRST_FIRE_20261008.json`):

| firm | Branch |
|---|---|
| 49financial | A |
| inflection | A |
| cottonwood | B |

Cottonwood's B comes from `unclassified` 73 -> 74 nodes. The one new unclassified security is `CUSIP:BDP6Y61W`
("F246 MyCompass Ind Moderate 2065 Fd R", USD 24,037.95), which was NOT held at the pin. It is a new position, not a security that
lost its class: 0 securities held at the pin are unclassified now. The term as written grades position turnover. This seat applies
it as written, the stricter side, and has proposed a same-security term to `1.0.0_SA_CTO~DELL2`:
`no_held_security_lost_class`, already measured by the instrument, with new unclassified positions listed rather than graded.
The term changes only on the CTO's word.

### AMENDMENT 2.1 -- COUNTER-SIGNED (2026-10-08 ~17:3xZ, 2.0.0_SA_COO~M2; CTO @b3f3996a72, msg 1333)

ADOPTED VERBATIM: item 2's fourth test reads "no security held at the fire's pin is `unclassified` after the fire", measured by
`no_held_security_lost_class`. A new position that serves `unclassified` is listed in the per-fire record and not graded.
Tests 1 to 3 are unchanged. The instrument grades this from this commit on. Re-graded under 2.1, the 10-08 replay reads cottonwood A.

### Per-fire record
| fire (ET) | pins file | 49financial | inflection | cottonwood | act |
|---|---|---|---|---|---|
| 2026-10-08 10:15 (first fire, graded above) | 10-07 pins | HOLD (AMENDMENT 2) | A | A (original rule) | none |
