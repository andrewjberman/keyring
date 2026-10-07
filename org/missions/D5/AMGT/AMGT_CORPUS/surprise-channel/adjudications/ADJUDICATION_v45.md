# AMGT_CORPUS ROUND 39 -- L8 COMPILE + L9 -- FWD-22 REALIZED on the 10-07 scheduled fire (96 of 96 pulled); both judgment criteria PASS; Z-S88 DISARMED; FWD-20, 21, 14, 11, 16 each one read or one line short; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-07 ~13:3xZ
**Input:** `2.0.0_SA_COO~X` `ROUND39_DRAIN_END_PACKET.md` @`0d86c83fc0` (88 lines, read to EOF), msg 30945. 6 of 6 cells
terminal. Ledger `amgt-corpus-r39-ao2` CLOSED by the packet.

## ao-2 (SERVED): the skip keys on the pull date, proved by the scheduled fire

**This seat's own read, not the evidence copy.** The scheduled job's log on this device,
`%LOCALAPPDATA%\opal\amgt-induction-daily\`:

| day | `refresh population` line | `REFRESH:` lines |
|---|---|---|
| 2026-10-06 (old rule) | registered 96 with_block 96 already_current 96 pulled 0 bloomberg_calls 0 | 0 |
| 2026-10-07 (pin `662cd2b11d`) | registered 96 with_block 96 already_current 0 pulled 96 bloomberg_calls 768 | 96, all 96 with a raw stamp `20261007T13...` |

- The task `amgt-induction-daily`: last run 2026-10-07T13:00:00Z, result 0, next 2026-10-08T13:00:00Z, start-in
  `opal-pinned\amgt-induction-daily\662cd2b11df0` (read with `Get-ScheduledTask`).
- BA US was re-derived by the plant at 00:10Z today, so its newest DERIVED stamp was already today's before the fire.
  The fire pulled it anyway (log line 27). That is the discriminating case.
- Not read by this seat: the S3 listing of BA's blocks; how many figures moved against the 10-06 blocks.

## The two judgment criteria

Read at full size from `evidence/r39_ao5_walk/`: `tsm_header_amended.png`, `tsm_sheet_a.png`, `tsm_sheet_b.png`,
`asml_sheet_a.png`. The walks were on portal `f8d92450`. That commit and the pushed merge `0c5ab419` are both
ancestors of origin DEV `8ddfe409` (`git merge-base --is-ancestor`, with a positive control). The page was not
re-walked on DEV.

| criterion | grade | what I read |
|---|---|---|
| **ao-3 AC4**: a PM reads each header fact's currency, why each "--" is empty, and each unmeasured reason, in plain words | **PASS** | TSM's fact line reads "Average daily value traded (three months): USD 4,863,543,808; Market capitalisation: USD 2,519,589 million". Every "--" in the two TSM crops and the ASML crop carries a mark, and under TSM's table the two marks are listed once in plain words (ASML's list is outside the crop I read). The two unmeasured tiles read "Not shown: Bloomberg's figure does not say whether it is in units or millions" and "Not shown: Bloomberg does not confirm this figure's currency", with no bare figure. |
| **ao-4 AC2**: 2028E is visible, unclipped, with the history beside it | **PASS** | On TSM and ASML all 13 value columns sit inside the card with a margin to its right edge. The crops I read begin below the year header, so I read 13 unclipped columns (10 history, 3 forward), not the label "2028E" itself. |

**Two findings from the same crops, neither a ground against the criteria:**
- ASML's row label reads "Minority (non-controlling) interest (zero-dominated: no magnitude: 10 of 10 fiscal years
  are zero)". That is a machine phrase on the sheet. It is FWD-20's last clause, below.
- TSM's fact line still opens "Company short name: TAIWAN SEMIC-ADR; Country: TAIWAN". DSGN_AMGTV1 round 47 removes
  the short name on its own candidate, which is not on DEV.

## FWD grades (whole fence, DONE WHEN as written)

| FWD | grade | basis |
|---|---|---|
| 22 | **REALIZED** | "The next scheduled fire is the acceptance." The 13:00Z fire re-pulled 96 of 96 names with a block and every one carries today's stamp; the denominator is printed. Read from the job's own log. |
| 19 | **REALIZED** (unchanged) | 83 + 13 + 1 = 97 on the round-39 census. |
| 20 | **NOT REALIZED** | The three round-38 page defects are cured on the walk (ao-3 AC4). Two things remain. The rendered-rows census (shown / refused / absent / unmapped, unmapped 0) is still not exercised. And one row label is in machine words (ASML, above), against "says why in words a PM reads". |
| 21 | **NOT REALIZED**, one read short | Clipping is cured (ao-4 AC2) and the history is unchanged (ao4 control 2/2, issuer). The limb "a name without forecast years reads the reason" is not in the packet and I have not read it. One walk of such a name closes the row; if no served name lacks forecast years, the census that shows 0 closes it. |
| 14 | **NOT REALIZED**, one line short | The four counts are right: 84 + 0 + 12 + 1 = 97 = folders read. But the instrument's own line prints `fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 sum 96 outside-fence 1`. Its printed sum is 96 against 97 folders, and the fourth class is named "outside-fence", not unresolved-with-reason. The amended DONE WHEN is four counts that sum to the folder count every time. The print is the instrument a reader sees. |
| 11 | **NOT REALIZED** | 1299 HK reads the team's absence with its reason. ASML shows the team's passage, cited to its pack, beside a roster. But that roster is the Bloomberg fallback ("no filing roster could be read"), and the DONE WHEN says "beside the filing roster, with the roster unchanged". No name with both a team passage and a filing roster was walked, and "unchanged" rests on a count of 7. The CTO's 09-26 addendum also still holds the row on a render outcome owed on AMGT_RESAPP. |
| 16 | **NOT REALIZED**, one read short | The docx control is unchanged on the three cases: 0 of 95 names differ from the 2026-09-29 read (issuer's census; I read its tail: 95 names, 285 slots, 102 body). "Still recovers what it recovered before" also covers pillars and management, which were not compared. |
| 10, 15, 18 | **NOT REALIZED** | The issuer's source read finds no control on the page for any of the three (no opener on a pillar, no citation on the header posture line, no filter on the feed). That is a finding, not an unread limb: each needs a build. |
| 12 | **NOT REALIZED** | The SharePoint template is not in the repository, so the rows cannot be compared. It needs the team's workbook. |

## Rows

- `Z-S88` (ARMED): **DISARMED and REMEDIATED** in place in `remediations/REMEDIATION_v3.md`, on this seat's read of
  the fire above.
- `Z-S89`: GRADUATED here to the issuer; `remediations/REMEDIATION_v4.md`. Two served dossiers show a scorecard
  heading and its score ("Management/Board 80") as the team's management passage.
- No worker filed a row (4 seats, 0 rows).

## L10 PRECONDITION

Every cell is terminal and the ledger is closed. `comp-surprise --project AMGT_CORPUS` read 1 ARMED (`Z-S88`) before
this file; it is disarmed here. **MET.**

```json
[
 {
  "id": "AMGT_CORPUS-Z-C-S49",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T13:32:00Z",
  "one_line": "Round 39 L9: FWD-22 REALIZED on the 2026-10-07 13:00Z scheduled fire (96 of 96 pulled on pin 662cd2b11d, against 0 of 96 on 10-06); ao-3 AC4 and ao-4 AC2 PASS on the walk crops; Z-S88 DISARMED; FWD-20 open on the unexercised row census and one machine-phrase row label; FWD-21 one read short (a name without forecast years); FWD-14 one line short (the instrument prints sum 96 of 97); FWD-11 read against a Bloomberg fallback roster, not a filing roster; FWD-16 compared on cases only; Z-S89 GRADUATED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "the scheduled job's own logs on this device, read by 3.0.0_SA_CVO~Z 2026-10-07 ~13:2xZ: 2026-10-06.log already_current 96 pulled 0, 0 REFRESH lines; 2026-10-07.log already_current 0 pulled 96 bloomberg_calls 768, 96 REFRESH lines with raw stamp 20261007T13; BA US at line 27",
    "Get-ScheduledTask amgt-induction-daily: last 2026-10-07T13:00:00Z result 0, next 2026-10-08T13:00:00Z, start-in opal-pinned\\amgt-induction-daily\\662cd2b11df0",
    "deliverables/2.0.0_SA_COO~X/evidence/r39_ao5_walk/ tsm_header_amended.png, tsm_sheet_a.png, tsm_sheet_b.png, asml_sheet_a.png, 1299hk_exec_management.png, asml_exec_roster.png (6 of 12 read at full size)",
    "deliverables/2.0.0_SA_COO~X/evidence/r39_ao6_fwd14_census_20261006.txt: folders_read 97; fence14 ... sum 96 outside-fence 1",
    "git merge-base --is-ancestor f8d92450 and 0c5ab419 against portal origin DEV 8ddfe409: both yes, beside a positive control"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_CORPUS-Z-S89"
  ],
  "spec_asserts": "FWD-22: the next scheduled fire re-pulls every name with a block. FWD-11: the team's management passage is the team's own cited text.",
  "world_is": "The scheduled fire pulled 96 of 96 on the pull-date rule. Two served dossiers (8306_JP_Equity, 8316_JP_Equity) carry 'Management/Board 80' as the management passage, a heading and a score; not walked on the page, and other short non-passage values were not searched for.",
  "notes": "Judgment criteria ao-3 AC4 and ao-4 AC2 are graded here and never by the issuer. The walks were on portal f8d92450, an ancestor of DEV; the page was not re-walked on DEV."
 }
]
```

-- 3.0.0_SA_CVO~Z
