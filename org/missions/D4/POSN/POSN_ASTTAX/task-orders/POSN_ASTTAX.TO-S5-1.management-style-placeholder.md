# TO POSN_ASTTAX.TO-S5-1 -- set `management_style` to the factually-correct value on the rows carrying the `"unknown"` placeholder, so a later allocation decision cannot take the page down (AT2-s-5, FWD-1)

<to_id>POSN_ASTTAX.TO-S5-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~3</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-5` · **Issuance:** round 2. **DEPENDS ON `AT2-s-6` -- do not start before it lands.**

---

## THE CELL

`C-RETAG-SAFETY` step **(1)**. `management_style: "unknown"` is a TRUTHY placeholder the default-to-passive
guard cannot fire on. The issuer measured, by `batch-get-item`, that the seven served `hedge` tickers read:
**DBC, GLD, GSG, IAU, SLV, USO = `"unknown"`; VIXY = `"passive"`.** Those six are exactly the six that
`AT2-s-2` will move to Commodities, and exactly the set the DT brief names as unsafe to hold.

Set the affected rows' `management_style` to the **factually correct** value -- a bullion or commodity trust
is `passive`; a fund that is actually actively managed is `active`. ⛔ **THIS IS A FACTUAL DETERMINATION PER
TICKER, NOT A BULK SET.** "Everything unknown becomes passive" is the same class of error as the wholesale
rename this project already caught: a scope stated in words rather than members.

## THE ACT

1. **Enumerate the population first** (`S5-AC1`) -- every row carrying the placeholder, with its denominator
   printed. The issuer has NOT enumerated this set; only the seven hedge tickers are known.
2. **Decide the scope** (`S5-AC2`): this order's write set is **the rows `AT2-s-2` will touch** -- the six
   commodity tickers -- NOT all 187. ⚠ **A wider sweep is NOT authorised here**: rows nobody holds and
   nobody is about to retag are not this cell's risk, and 187 factual determinations is a different
   project. State the count you are writing and why each is in scope.
3. **Write the corrected values** (`S5-AC3`), then **read them back** (`S5-AC4`). ⛔ A write's own return
   value is not evidence the value is served -- read the row back.
4. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT TOUCH `asset_class`.** Different field, different cell (`AT2-s-2`), and the two orders share
  these exact rows. You write `management_style` ONLY. If you find yourself editing a classification, stop.
- ⛔ **DO NOT ADD ANY HOLDING and DO NOT TOUCH YANG'S MODELS.** Whether GLD is ever held is an ALLOCATION
  decision, explicitly not this project's (DT brief conclusion 2).
- ⛔ **DO NOT BULK-SET.** Per-ticker factual determination, each stated.
- **DO NOT START BEFORE `AT2-s-6` IS COMPLETE.** If the generator is not yet hardened, this cell's write is
  safe on its own but the sequence exists for a reason -- verify `AT2-s-6` is terminal and say so.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W3-S<n>`, appended as ONE new fenced ```json block at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.
- ⛔ Never pipe a comp-tool census into `head`/`tail`/`sed` -- the denial aborts the whole bash call.

## ACCEPTANCE CRITERIA

<criterion id="S5-AC1" cell_refs="AT2-s-5"><invocation>timeout 180 .tools/aws dynamodb scan --table-name etf-classifications --filter-expression "management_style = :u" --expression-attribute-values '{":u":{"S":"unknown"}}' --projection-expression "ticker" --output json</invocation><expect>the full ticker list and its count pasted verbatim, with ScannedCount named as the denominator and LastEvaluatedKey named (paginate and total client-side if present).</expect></criterion> `S5-AC1` -- THE PLACEHOLDER POPULATION, ENUMERATED WITH ITS DENOMINATOR.

<criterion id="S5-AC2" cell_refs="AT2-s-5"><invocation>timeout 120 .tools/aws dynamodb batch-get-item --request-items '{"etf-classifications":{"Keys":[{"ticker":{"S":"DBC"}},{"ticker":{"S":"GLD"}},{"ticker":{"S":"GSG"}},{"ticker":{"S":"IAU"}},{"ticker":{"S":"SLV"}},{"ticker":{"S":"USO"}},{"ticker":{"S":"VIXY"}}]}}' --query 'Responses."etf-classifications"[].{t:ticker.S,m:management_style.S,a:asset_class.S}' --output json</invocation><expect>all seven pasted verbatim, the six carrying "unknown" named, and the WRITE SET for this order stated explicitly as those six with a reason per ticker.</expect></criterion> `S5-AC2` -- THE WRITE SET, NAMED BY MEMBER RATHER THAN BY DESCRIPTION.

<criterion id="S5-AC3" cell_refs="AT2-s-5"><invocation>timeout 180 python &lt;your per-ticker update script&gt;</invocation><expect>one line per ticker written: the ticker, the old value, the new value, and the one-sentence factual reason. No ticker written without a reason.</expect></criterion> `S5-AC3` -- THE WRITE, PER TICKER, EACH WITH ITS BASIS.

<criterion id="S5-AC4" cell_refs="AT2-s-5"><invocation>timeout 120 .tools/aws dynamodb batch-get-item --request-items '{"etf-classifications":{"Keys":[{"ticker":{"S":"DBC"}},{"ticker":{"S":"GLD"}},{"ticker":{"S":"GSG"}},{"ticker":{"S":"IAU"}},{"ticker":{"S":"SLV"}},{"ticker":{"S":"USO"}}]}}' --query 'Responses."etf-classifications"[].{t:ticker.S,m:management_style.S,a:asset_class.S}' --output json</invocation><expect>all six read back with their NEW management_style, pasted verbatim, and asset_class confirmed STILL `hedge` (this order must not have moved it).</expect></criterion> `S5-AC4` -- READ-BACK. **A write's return value is not evidence; the served row is.** This also proves the order stayed out of `AT2-s-2`'s field.

<criterion id="S5-AC5" cell_refs="AT2-s-5"><invocation>timeout 120 grep -n "<status>" ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md</invocation><expect>the status line of the AT2-s-6 order pasted verbatim, showing `complete` -- or, if it is not, this order STOPS and files a row instead of proceeding.</expect></criterion> `S5-AC5` -- THE PREDECESSOR IS ACTUALLY DONE, CHECKED RATHER THAN ASSUMED.

<criterion id="S5-AC6" cell_refs="AT2-s-5" judgment="true"/> `S5-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the six rows are now safe to hold, and whether leaving the wider placeholder population untouched is the right scope or a gap. **Record the readings and offer NO verdict.**

<expected_criteria>S5-AC1, S5-AC2, S5-AC3, S5-AC4, S5-AC5, S5-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S5-1.management-style-placeholder.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~3/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-5`.
<owned_cells>AT2-s-5</owned_cells>
Read-dependency, NOT claimed: `AT2-s-6` (the hardening chain head) must be terminal first; `S5-AC5` checks it.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB reads and item writes
run under this device's operator credentials. A DENIED write is a ROW naming the missing permission, never
an IAM edit by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool; every referent was read live by the issuer
at 07:4xZ-08:0xZ and AC2 re-takes the decisive one. NOT covered: the issuer never enumerated the full
placeholder population -- AC1 is its first read, which is why AC1 precedes the scope decision in AC2.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~3/POSN_ASTTAX.TO-S5-1.management-style-placeholder.proof_of_spec.json
</proof_of_spec>
