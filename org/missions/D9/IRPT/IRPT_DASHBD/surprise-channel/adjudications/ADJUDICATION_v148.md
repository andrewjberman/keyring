# IRPT_DASHBD: CVO adjudication, round 149 packet 5 (~D2): the hop-2 reader, three APPLIED pairs (Cottonwood landing rewrite, 49F publish hop-2, Cottonwood publisher 0.4.0 republish) and the Performance tab cells

<sweep_watermark>2026-10-17T00:33Z</sweep_watermark>

**Basis.** L8 compile, L9 grades and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-17T00:33Z, on msg 10050. The packet is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND149_READER_AND_THREE_APPLIED_PAIRS_DRAIN_END_20261016.md` @941f3ad0ce; its sha256 is 575f0699c0f9bd5f (7,696 bytes), verified. Section 2 was read first. All AWS reads were read-only, and nothing below carries a client value.

## Mechanical criteria, re-run (33)

**Reader cells, at HEAD:**
- **PASS (8):** DB170-1-AC3, DB173-1-AC2, DB173-1-AC3, DB174-1-AC1, DB174-1-AC3, DB178-1-AC1, DB178-1-AC2, DB178-1-AC3.
- **FAIL by supersession (4):** a later cell of the same round moved each target. They passed at their drains per the packet; not re-run at the merges.
  - DB170-1-AC1 and DB173-1-AC1: they pin byte-identity to the base.
  - DB170-1-AC2: its fake S3 lists no ETag, which DB-b-306's per-version cache now needs (`handler.py:654-655`).
  - DB174-1-AC2: it expects raw ids, which DB-b-310 now mints.

**Applier cells, on fresh reads:** DBC176-1/2/3-AC1, DBC179-1/2/3-AC1 and DBC182-1/2/3-AC1 all PASS.

**Portal cells.** Run in an isolated clone of the portal repo, at each cell's own head, under the branch name the checkers require (nothing pushed; the clone's link to the shared node_modules removed after).
- **DBP175 x3: PASS** @1779d676.
- **DBP177 x3: PASS** @75a71ae3.
- **DBP180 @efd86d6c:** AC1 PASS, AC3 PASS, AC2 FAIL.
- **DBP181 @355b3bf8:** AC1 PASS, AC3 PASS, AC2 FAIL; AC2 also FAILS @efd86d6c.
- **Why the two FAILs:** the checkers p180 and p181 were amended at 2cbe47ffdf to DB-b-316's targets (a probe that a snapshot without nodes never throws, page owner msg 10063; and the words "advisor" or "one-firm" in the firm-gate test). That came after orders 313 and 314 were complete, so two complete orders now carry criteria their landed heads fail. The fix is DB-b-316, not landed.

**p178 `--selftest`:** it aborts here ("the reference lacks the anchor for 'account_id is left raw'"). The packet's "red on five handler mutants" is not reproduced, so W248-S1 stands.

## (a) L9 -- the served and gold movements against the signed packets

**DB-b-308 (Cottonwood landing rewrite, ten events): PASS.** This seat's own read compared each of the 66 landed days' current version against its oldest:
- 66 days, each key holding 2 versions; 53,328 rows before and after.
- `history_scope_claim` reads inferred on all rows; FULL on 2,828 rows and PARTIAL_HISTORY on 50,500.
- Only `external_flow` (844 rows) and `total_return_daily` (798 rows) changed. They changed on exactly the ten October days, and each day's count EQUALS the signed table's (R2 packet lines 29-40).

The halves:
- the R2 packet hashes 962ef131ff27 at current bytes;
- COO half REVISION 2 @be783a1b8e, branches A to D;
- CTO half REVISION 2 @f362eb8cb5;
- ADDENDUM 1 hashes e6f1f4b4759f, is "SIGNED by the COO" in its own header, and is countersigned by the CTO @d2994a4773;
- rollback is the prior version per key.

**DB-b-315 (Cottonwood publisher 0.4.0, full republish): PASS.** This seat's own read compared all 939 series (1,878 keys), current against the newest prior version without a claim (publisher 0.3.0):
- 102 PARTIAL to FULL, 0 back;
- 826 a day newer;
- 657 `total_return_daily` restated on common days;
- 659 `external_flow` restated;
- 118 drawdown sets changed;
- `value`, `income` and `holdings_price_return` 0 each;
- `history_scope_claim` inferred on 939.

Every count equals the signed packet's (packet line 31).

The halves bind sha256 584a774339a1, which equals the current bytes: COO @de90b2bb6f and CTO @f78b555c93. Both name the branches and a rollback per key (the prior artifact version and the prior object versions).

- **Is 657 named in the COO-signed half?** YES: "657 series show a restated daily return on past days" (COO half section 1).
- **Not named as a client effect:** 659 `external_flow` and 118 drawdown changes. Both are in the signed packet; the CTO half says "Nothing else visible moves". PROD's performance views (`DashboardPerformance.tsx`, `PerformanceDocument.tsx`) render neither field (grep at origin/PROD), so that holds today. The fields are served, so a later view that renders them would make the restatement visible.

**DB-b-312 (49F publish hop-2): PASS.**
- The halves bind e6af7a92148d at current bytes: COO @a30664edac, CTO @6aaa28e481, branches A to D, rollback to artifact `41lfCmfJ...`.
- DBC179 passes on fresh reads.

**v143's 49F stop-rule ADDENDUM 1:** the COO half is now countersigned (@15a01e89a8, section 8), "COUNTERSIGNED, LATE", written after Act 5 and stated as such. The act ran on the CTO half alone.

## (b) L9 -- minted composed account ids (W247-S1): FAIL as the contract's reading

The contract is `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.5.4, unchanged since 6459608700):
- **line 157:** `"account_id": "account_activity_daily account_id (custodian account form)"`;
- **line 126:** "accounts one entry per account of the household in account_id order, each entry {account_id, last4, first_data_date, window_status}";
- **lines 138-143:** `account_entry_fields` lists account_id, last4, first_data_date and window_status, with no id-form or claim field.

DB-b-310 replaces every composed account id with `ids.opaque_account(firm, raw)` (`handler.py:579-601`) and keeps the raw-id order (`:582-583`), so:
- the id is no longer the custodian form;
- the entries are not in the order of their own `account_id`;
- **no claim travels:** a consumer cannot tell a minted id from a source id by any field.

Minting is the right policy: no raw id leaves the function, and it matches `IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json:71` ("The issued opaque account id"). But it landed without the contract change. Owed, in one drain: contract 0.5.5 naming the minted id form and its claim, plus the order rule.

## (c) L9 -- the section-4 rows

| row | disposition here | evidence |
|---|---|---|
| S128 (relationship-id join matched 0 of 4,012) | DISMISSED: the design was replaced | DB-b-306 joins through the minted account ids (DB174-1-AC1/AC3 PASS). The reader on the real partition inside the function is NOT established (the packet's own limit). |
| S129 (25-day dry run timed out at 900 s) | DISMISSED: resolved | ADDENDUM 1 ten events, countersigned. The gold read above matches the table exactly. |
| S130 (`iam.tf` fmt deviation) | DISMISSED | It predates the order and is outside the plan (0/1/0). The root's owner may reformat in its own pair. |
| IB2-S1, IB2-S2 | no such rows | Not in any investigation file. The AE's message names them; their content is S129 and S130. |
| W247-S1 (raw id in the composed document) | UNDER_INVESTIGATION | The minting closed the leak; the contract (b) is not updated. |
| W248-S1 (p178 selftest aborts on an anchor) | UNDER_INVESTIGATION | Reproduced at HEAD (above). |
| W246-S7 | DISMISSED by W246-S10: ACCEPTED | The grant was widened by one test file. DBP177 passes. |
| W246-S8 (no account focus at Global) | UNDER_INVESTIGATION | A Global-path gap on a client-facing page; Andrew's smoke should be told before the approval. Owner: the page owner. |
| W246-S9 (print URL carries no client id) | UNDER_INVESTIGATION | Issuer's call, open. |
| W249-S1 (local branch in a dead worktree) | DISMISSED | Process only. The cell landed at f26fb258 and was folded at efd86d6c. |
| W250-S1 (Inflection test form) | DISMISSED | Form only. The test asserts PATH A (the words are present; DBP181-1-AC1 and AC3 PASS). |
| MDPF_SECCLASS-D2-S1 | not this channel's | The Sector panel is worded-absent by CTO ruling. The row stays with MDPF_SECCLASS. |

## Also

**Ledger union across worktrees: 100 trees read; 148 distinct sentinel files in the union.**
- **The three pairs' closures are NOT COMMITTED.** At box/dell2 HEAD (95ced15883), all three sentinels exist with status OPEN:
  - `irpt-dashbd-cottonwood-landing-codeupdate-rewrite-r2-20261016`;
  - `irpt-dashbd-49f-publish-hop2-reader-readgrant-20261016`;
  - `irpt-dashbd-cottonwood-publish-hop2-scope-republish-20261016`.
- **The CLOSED edits live only in this box's shared working tree:** each sentinel shows `D` and each deploy_completion file `M`, uncommitted.
- **How far the OPEN state reaches:** 19 trees carry the 308 sentinel, 11 the 312 sentinel and 6 the 315 sentinel.
- **The world is done:** measured above. The owed act is the commit of the three closures; owner: the applier `0.7.0_AE_CloudOps~IB2` or the issuer.

**Performance tab: no client-facing page has changed on portal DEV or PROD.** The candidate heads 355b3bf8 and efd86d6c are ancestors of neither origin/DEV (4d4dc68c) nor origin/PROD (fa21a303). No approval was needed yet; Andrew's approval row stays OPEN, per the packet.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S85",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T00:33:00Z",
  "one_line": "Round 149 packet 5 (~D2): (a) PASS -- the 308 gold (66 days, 844/798 per day equal to the signed table) and the 315 served series (102/826/657/659/118, value 0) match the signed packets on this seat's own reads; halves bound at current bytes, branches, rollback; 657 named in the COO half; the 49F addendum is now COO-countersigned, late. (b) FAIL -- minting contradicts contract 0.5.4 line 157 (custodian form), breaks the order rule, and carries no claim. Mechanical: 25 PASS, 6 FAIL by supersession or a checker amended after completion. The three pairs' ledger closures are uncommitted: box/dell2 HEAD reads all three OPEN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S128", "IRPT_DASHBD-D2-S129", "IRPT_DASHBD-D2-S130", "IRPT_DASHBD-D2-W247-S1", "IRPT_DASHBD-D2-W248-S1", "IRPT_DASHBD-D2-W246-S8", "IRPT_DASHBD-D2-W246-S9", "IRPT_DASHBD-D2-W246-S10", "IRPT_DASHBD-D2-W249-S1", "IRPT_DASHBD-D2-W250-S1"],
  "spec_asserts": "The signed packets: R2 table (844 external_flow / 798 total_return_daily rows on ten days, no other column); 0.4.0 republish (102 PARTIAL to FULL, 826, 657, 659, value/income/holdings_price_return 0). Contract IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json 0.5.4 line 157: account_id is the custodian account form; line 126: accounts in account_id order. NEVER-2: a deploy ledger is closed at completion.",
  "world_is": "Gold: 66 days x 2 versions, 53,328 rows, only external_flow 844 and total_return_daily 798 on the ten days, per-day equal; claim inferred on all rows. Served: 939 series, 102/0/826/657/659/118, value/income/hpr 0, claim inferred 939. handler.py:579-601 mints ids, keeps raw order, no claim field. box/dell2 HEAD 95ced15883 carries the three sentinels with status OPEN; the CLOSED edits are uncommitted in the shared tree. DBP180-1-AC2 and DBP181-1-AC2 fail at their heads after checker amendment 2cbe47ffdf.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "sha256 of the packet blob @941f3ad0ce: 575f0699c0f9bd5f, 7,696 bytes",
    "the 33 invocations of TO-DB-b-302/305/306/310/308/312/315/307/309/313/314 (checks/r149/p1*.py . <id>); portal ones in an isolated clone at 1779d676, 75a71ae3, efd86d6c, 355b3bf8",
    "read-only list_object_versions + get_object over irpt/cottonwood/gold/account_return_daily/ (66 days) and irpt/cottonwood/platinum/reporting/ (1,878 keys); counts only",
    "sha256 at current bytes: R2 962ef131ff27, ADDENDUM 1 e6f1f4b4759f, 49F hop-2 e6af7a92148d, 0.4.0 584a774339a1; halves be783a1b8e, f362eb8cb5, d2994a4773, a30664edac, 6aaa28e481, de90b2bb6f, f78b555c93; 49F addendum COO countersign 15a01e89a8",
    "org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json:126,138-143,157; org/standards/IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json:71; infra/aws/lambda/investor-reporting/reporting-publish/handler.py:579-601",
    "git worktree list --porcelain (100 trees) + git ls-tree HEAD org/critical_paths/.open_deploys/ per tree; git show HEAD:<sentinel> status OPEN; git status D/M on the three sentinels and completion files",
    "portal: git merge-base --is-ancestor 355b3bf8|efd86d6c origin/DEV (4d4dc68c) and origin/PROD (fa21a303) -> not ancestors"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owed: (1) commit the three ledger closures (owner 0.7.0_AE_CloudOps~IB2 or 2.0.0_SA_COO~D2): HEAD reads them OPEN; (2) contract 0.5.5 for the minted account id (form, claim, order) in one drain with the producer (owner 2.0.0_SA_COO~D2, ruling 1.0.0_SA_CTO); (3) DB-b-316 lands the p180/p181 targets the amended checkers already demand; until then orders 313/314 are complete with failing criteria; (4) p178's selftest anchor (W248-S1); (5) tell Andrew's smoke about W246-S8 (no account focus at Global)."
 }
]
```
