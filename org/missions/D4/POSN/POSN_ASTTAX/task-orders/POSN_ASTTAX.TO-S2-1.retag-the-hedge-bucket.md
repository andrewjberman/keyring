# TO POSN_ASTTAX.TO-S2-1 -- the additive five-class reconciliation: the served `hedge` value DISSOLVES and its seven tickers split SIX to Commodities, VIXY to Structured. LAST IN THE CHAIN (AT2-s-2, FWD-1/FWD-2)

<to_id>POSN_ASTTAX.TO-S2-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~5</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-2` · **Issuance:** round 2. ⛔ **STRICTLY LAST. GATED ON `AT2-s-7`'s GO.**

---

## THE CELL

Add `Commodities` and `Alternatives` to the stored vocabulary (stored THREE, ratified FIVE) and move the
seven served `hedge` tickers to ratified classes. `sub_asset_class` is the authoritative signal and already
carries the answer, so **no class edge needs ruling**:

```
  sub in {Gold, Silver, Oil, Commodities} -> Commodities   DBC, GLD, GSG, IAU, SLV, USO   (6)
  sub = Volatility                        -> Structured    VIXY                            (1)
  VXX (served `equity`, sub=Volatility)   -> Structured    per C-VOL-HEDGE-STRUCTURED
```

⛔ **THE `hedge` VALUE DISSOLVES. IT DOES NOT RENAME WHOLESALE.** A wholesale rename files six commodity
holdings as Structured -- including GSG, the GSCI trust the PRD's own table names as its example of a
commodity index. That error was caught at the issuer this round and is now named in the constraint; do not
reintroduce it.

⛔⛔ **THIS ORDER IS A PRODUCTION LANDMINE IF ITS PREDECESSORS HAVE NOT LANDED.** Retagging a HELD ticker
to a class the generator does not carry raises `KeyError`, kills the generator, and blanks the positioning
page for all four partner firms. `AT2-s-6` hardens the generator; `AT2-s-7` proves the whole chain carries
five classes and establishes whether VXX is held. **Both must be terminal and `AT2-s-7` must read GO.**

## THE ACT

1. **Verify BOTH predecessors** (`S2-AC1`) -- `AT2-s-6` `complete` AND `AT2-s-7` `complete` with a GO
   verdict. ⛔ **If either is missing or the verdict is NO-GO, this order STOPS and files a row. It does
   not proceed "carefully".**
2. **Re-take the bucket** (`S2-AC2`) -- the issuer read seven at 06:5xZ; the registry is a live curated
   list and may have moved.
3. **Write the retag per ticker** (`S2-AC3`), each with its `sub_asset_class` basis stated.
4. **Read back** (`S2-AC4`) and **confirm the page still renders** (`S2-AC5`). ⛔ The read-back is not
   enough: the whole risk of this order is downstream of the write.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT TOUCH `management_style`.** Same rows, different field, different cell (`AT2-s-5`). If those
  values are not yet corrected, that is a reason to STOP, not to fix them here.
- ⛔ **DO NOT EDIT THE GENERATOR.** `AT2-s-6` owns that file. If the retag reveals a hop that drops or
  raises, file a row -- do not patch it from this cell.
- ⛔ **DO NOT INVENT AN `Alternatives` MEMBER.** The vocabulary gains the value; nothing in the served
  seven maps to it. A ticker moved to Alternatives in this order is out of scope and unsupported by
  `sub_asset_class`.
- ⛔ **VXX IS ONLY RETAGGED IF `AT2-s-7` ESTABLISHED ITS STATE.** If AC4 there found VXX held, the retag is
  live-impacting and must follow the same read-back and render check.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W5-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="S2-AC1" cell_refs="AT2-s-2"><invocation>timeout 120 grep -n "<status>" ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md ../task-orders/POSN_ASTTAX.TO-S7-1.verify-the-five-class-chain.md</invocation><expect>both status lines pasted verbatim reading `complete`; plus the AT2-s-7 instance's AC5 verdict quoted, reading GO. Anything else and this order STOPS with a row.</expect></criterion> `S2-AC1` -- ⭐ **THE GATE, CHECKED NOT ASSUMED.** This is the criterion that stands between a retag and a blank page.

<criterion id="S2-AC2" cell_refs="AT2-s-2"><invocation>timeout 180 .tools/aws dynamodb scan --table-name etf-classifications --filter-expression "asset_class = :h" --expression-attribute-values '{":h":{"S":"hedge"}}' --projection-expression "ticker, sub_asset_class" --output json</invocation><expect>every member with its sub_asset_class pasted verbatim, the count stated against ScannedCount as denominator, and any ticker NOT among the issuer's seven named explicitly.</expect></criterion> `S2-AC2` -- THE BUCKET RE-TAKEN AT YOUR VINTAGE. **A new member is a finding, not a silent inclusion.**

<criterion id="S2-AC3" cell_refs="AT2-s-2"><invocation>timeout 180 python &lt;your per-ticker retag script&gt;</invocation><expect>one line per ticker: ticker, old asset_class, new asset_class, and the sub_asset_class that justifies it. The six-to-Commodities / VIXY-to-Structured split reproduced exactly, with no ticker written on any basis other than its sub_asset_class.</expect></criterion> `S2-AC3` -- THE SPLIT, PER TICKER, EACH ON ITS OWN EVIDENCE.

<criterion id="S2-AC4" cell_refs="AT2-s-2"><invocation>timeout 120 .tools/aws dynamodb scan --table-name etf-classifications --filter-expression "asset_class = :h" --expression-attribute-values '{":h":{"S":"hedge"}}' --select COUNT --output json</invocation><expect>Count 0 pasted verbatim -- the `hedge` value no longer exists in the served table -- with ScannedCount named as the denominator.</expect></criterion> `S2-AC4` -- THE VALUE IS GONE, NOT MERELY REDUCED. **This is what "dissolves" means, and it is checkable.**

<criterion id="S2-AC5" cell_refs="AT2-s-2"><invocation>timeout 300 python &lt;your generator render check&gt;</invocation><expect>evidence that `calculate_allocations()` completes over the current holdings AFTER the retag and that the five classes are represented, pasted verbatim. A traceback here is a STOP and a row, and the row names the rollback.</expect></criterion> `S2-AC5` -- ⛔ **THE PAGE STILL RENDERS. The read-back proves the registry; only this proves the consumer.**

<criterion id="S2-AC6" cell_refs="AT2-s-2" judgment="true"/> `S2-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether every holding now lands in exactly one of the five ratified classes (FWD-1) and volatility and gold are visibly apart from equity (FWD-2). **Record the readings and offer NO verdict.**

<expected_criteria>S2-AC1, S2-AC2, S2-AC3, S2-AC4, S2-AC5, S2-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S2-1.retag-the-hedge-bucket.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~5/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-2`.
<owned_cells>AT2-s-2</owned_cells>
Read-dependencies, NOT claimed: `AT2-s-6` (hardening) and `AT2-s-7` (chain verification + the GO verdict),
both checked by S2-AC1; `AT2-s-5` writes the same rows on a different field and is not this order's.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB reads and item writes
under this device's operator credentials. A DENIED write is a ROW, never an IAM edit.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. The bucket enumeration is the issuer's live
read at 06:5xZ and AC2 re-takes it. ⚠ NOT covered: this order's SAFETY rests entirely on two predecessor
cells' findings, which is why S2-AC1 verifies them by reading their artifacts rather than trusting the
issuance order.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~5/POSN_ASTTAX.TO-S2-1.retag-the-hedge-bucket.proof_of_spec.json
</proof_of_spec>
