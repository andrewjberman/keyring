# TO POSN_ASTTAX.TO-S4-1 -- fill the blank `sub_asset_class` rows: the real coverage gap in what the registry exists to do (AT2-s-4, FWD-1)

<to_id>POSN_ASTTAX.TO-S4-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~8</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-4` · **Issuance:** round 2. **Independent chain head; depends on `AT2-s-6`.**

---

## THE CELL

`C-CLASSIFIER-PURPOSE`: ETFClassifier is a CURATED TAGGING LIST whose job is keeping securities with
**proper capitalization, proper sub asset class, etc.** The round-1 analysis (addendum A3(4)) reports
`sub_asset_class` populated on **282 of 285** -- **THREE blanks, and those three are the actual gap in
what the registry exists to do.** Not an architecture programme; a small, real, in-purpose fix.

⛔ **RE-TAKE THE COUNT. DO NOT INHERIT IT.** 282/285 is the CTO's figure at its vintage and the table is a
LIVE curated list a person may have extended since. Your denominator is your own.

⭐ **AND `sub_asset_class` IS LOAD-BEARING FOR THE REST OF THIS ROUND:** `AT2-s-2` uses it as the
authoritative signal deciding which tickers go to Commodities and which to Structured. **A blank row is a
row that signal cannot decide.** Check whether any of your blanks is one of the seven `hedge` tickers and
say so explicitly -- if so, this cell gates that one's retag and you file a row saying which.

## THE ACT

1. **Enumerate the blanks** (`S4-AC1`) with the denominator printed -- missing attribute AND empty string
   both count as blank, and they are different shapes in DynamoDB.
2. **Cross-check against the retag set** (`S4-AC2`) -- is any blank one of DBC/GLD/GSG/IAU/SLV/USO/VIXY?
3. **Fill each with the factually correct value** (`S4-AC3`), one at a time, each with its basis. ⛔ **Use
   a value the registry ALREADY uses** where one fits -- round 1 measured 31 distinct values in use. A
   new value is a vocabulary act, not a fill, and needs saying.
4. **Read back** (`S4-AC4`).
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT TOUCH `asset_class` OR `management_style`.** Different fields, different cells
  (`AT2-s-2`, `AT2-s-5`). You write `sub_asset_class` ONLY.
- ⛔ **DO NOT MINT A NEW SUB-ASSET-CLASS VALUE WITHOUT SAYING SO.** Prefer an existing one; if none fits,
  state the new value, why, and that it widens the vocabulary.
- ⛔ **DO NOT BULK-FILL.** Three rows, three factual determinations, three reasons.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W8-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="S4-AC1" cell_refs="AT2-s-4"><invocation>timeout 180 .tools/aws dynamodb scan --table-name etf-classifications --projection-expression "ticker, sub_asset_class" --output json</invocation><expect>the total item count stated as the denominator, the rows whose sub_asset_class is MISSING and the rows whose sub_asset_class is an EMPTY STRING listed separately with their tickers, and LastEvaluatedKey named (paginate and total client-side if present).</expect></criterion> `S4-AC1` -- THE BLANKS, WITH THEIR DENOMINATOR AND BOTH SHAPES OF BLANK DISTINGUISHED.

<criterion id="S4-AC2" cell_refs="AT2-s-4"><invocation>timeout 120 python -c "print('CROSS-CHECK RECORDED IN THE INSTANCE')"</invocation><expect>a stated answer to whether any blank ticker is among DBC, GLD, GSG, IAU, SLV, USO, VIXY -- named either way. If yes, a row is filed noting this cell gates that ticker's retag in AT2-s-2.</expect></criterion> `S4-AC2` -- DOES A BLANK SIT ON THE RETAG'S AUTHORITATIVE SIGNAL.

<criterion id="S4-AC3" cell_refs="AT2-s-4"><invocation>timeout 180 python &lt;your per-row fill script&gt;</invocation><expect>one line per row filled: ticker, the value written, whether that value ALREADY EXISTS in the registry's value set, and the one-sentence factual basis. No row filled without a basis.</expect></criterion> `S4-AC3` -- THE FILL, PER ROW, EACH ON ITS OWN EVIDENCE.

<criterion id="S4-AC4" cell_refs="AT2-s-4"><invocation>timeout 180 .tools/aws dynamodb scan --table-name etf-classifications --projection-expression "ticker, sub_asset_class" --output json</invocation><expect>the re-scan showing ZERO rows missing or empty on sub_asset_class, with the denominator restated. Any remaining blank is named and explained.</expect></criterion> `S4-AC4` -- READ-BACK OVER THE WHOLE TABLE. **A write's return value is not evidence; the served rows are.**

<criterion id="S4-AC5" cell_refs="AT2-s-4" judgment="true"/> `S4-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the filled values are factually right and consistent with the registry's existing vocabulary, rather than merely non-blank. **Record the readings and offer NO verdict.**

<expected_criteria>S4-AC1, S4-AC2, S4-AC3, S4-AC4, S4-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S4-1.blank-sub-asset-class-rows.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~8/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-4`.
<owned_cells>AT2-s-4</owned_cells>
Read-dependencies, NOT claimed: `AT2-s-6` precedes all round-2 cells. `AT2-s-2` consumes `sub_asset_class`
as its authoritative signal, so a blank found here may gate one of its tickers -- reported, never acted on.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB reads and item writes
under this device's operator credentials. A DENIED write is a ROW naming the missing permission.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. ⚠ NOT covered and stated rather than
implied: the 282-of-285 figure is the CTO's round-1 read and NEITHER the issuer NOR this order inherits
it -- AC1 is this project's first independent enumeration of the blanks.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~8/POSN_ASTTAX.TO-S4-1.blank-sub-asset-class-rows.proof_of_spec.json
</proof_of_spec>
