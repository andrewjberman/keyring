# TO POSN_ASTTAX.TO-S7-1 -- verify the asset_class allocation chain carries the ratified FIVE-class vocabulary end to end, and establish whether VXX is a current holding. GATES THE RETAG (AT2-s-7, FWD-1)

<to_id>POSN_ASTTAX.TO-S7-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~4</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-7` · **Issuance:** round 2. **DEPENDS ON `AT2-s-6`. GATES `AT2-s-2`.**

---

## THE CELL

`C-RETAG-SAFETY` step **(2)**: verify the asset_class allocation chain carries the ratified FIVE-class
vocabulary **before** anything is retagged. The issuer measured the KeyError at the subscript
(`lambda_function.py:239`) and `AT2-s-6` hardens it -- **this cell proves the whole chain, not just that
one line.** A classification value survives several hops between the registry and the rendered page, and
hardening one subscript does not establish that the others carry it.

⭐ **AND ONE FACT THIS CELL MUST SETTLE BECAUSE THE WHOLE SEQUENCE'S URGENCY TURNS ON IT: IS VXX A
CURRENT HOLDING?** The DT brief states VXX is already flowing into Satellites 70/80/90/98. The issuer did
NOT read the models payload and said so. If VXX IS held, retagging it `equity` -> `Structured` fires on
the next generator run; if it is NOT, the exposure is latent. **Either way `AT2-s-6` precedes the retag --
the sequence does not change -- but the grade and the urgency do.**

## THE ACT

1. **Trace the chain** (`S7-AC1`, `S7-AC2`): from `classify_etf()` through every place an `asset_class`
   value is branched, bucketed, keyed or rendered, to what lands in `positioning_data.json`. Enumerate the
   hops with file:line. ⛔ **A grep for the four known strings is NOT the trace** -- a value can be carried
   by a dict key, a comparison chain, a schema field or a frontend contract, and each is a separate hop.
2. **For each hop, state whether `Commodities` / `Structured` / `Alternatives` survive it** (`S7-AC3`).
   A hop that silently drops an unknown class is as fatal to FWD-1 as one that raises.
3. **Establish VXX's held status from the MODELS payload** (`S7-AC4`), not from the brief and not from the
   registry. Name the artifact you read.
4. **State the verdict as a GO / NO-GO for `AT2-s-2`** (`S7-AC5`) with the blocking hops named if NO-GO.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **READ-ONLY. CHANGE NOTHING.** No registry write, no code edit, no deploy. If a hop needs fixing,
  that is a finding and possibly a successor cell -- not an act here. This cell exists to make the retag
  safe to authorise, and a cell that fixes what it is measuring cannot report on it cleanly.
- ⛔ **DO NOT RETAG.** `AT2-s-2` is a different order and is gated on this one's verdict.
- ⛔ **DO NOT CONCLUDE FROM A PAGE.** Any census here uses `--all` or paginates; rule 21 -- an early stop
  and a true absence read identically, and a missed hop is the whole failure mode.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W4-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.
- ⛔ Never pipe a comp-tool census into `head`/`tail`/`sed` -- the denial aborts the whole bash call.

## ACCEPTANCE CRITERIA

<criterion id="S7-AC1" cell_refs="AT2-s-7"><invocation>timeout 300 comp-find 'asset_class' --all</invocation><expect>the printed DENOMINATOR and every hit shown (count shown == denominator), then the subset that lies on the positioning generator's path enumerated with file:line.</expect></criterion> `S7-AC1` -- EVERY SITE THAT TOUCHES THE VALUE, OVER A PRINTED DENOMINATOR, NOT A PAGE.

<criterion id="S7-AC2" cell_refs="AT2-s-7"><invocation>timeout 120 comp-read infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py --enumerate 'asset_class'</invocation><expect>the enumerate DENOMINATOR and every banded hit pasted verbatim, with each occurrence classified as one of: dict-key construction, subscript, comparison branch, output field, or mention.</expect></criterion> `S7-AC2` -- THE HOPS INSIDE THE GENERATOR, BANDED BY WHAT THE CODE ACTUALLY DOES WITH THE VALUE.

<criterion id="S7-AC3" cell_refs="AT2-s-7"><invocation>timeout 120 python &lt;your hop-by-hop harness&gt;</invocation><expect>a table with one row per hop: the hop's file:line, and whether a value of "Commodities" SURVIVES, RAISES, or is SILENTLY DROPPED there. Every hop from AC2 accounted for; the count of hops tested equals the count enumerated.</expect></criterion> `S7-AC3` -- ⭐ **THE DECISIVE TEST, AND "SILENTLY DROPPED" IS A FAILURE TOO.** A hop that neither raises nor carries the value defeats FWD-1 without defeating the page.

<criterion id="S7-AC4" cell_refs="AT2-s-7"><invocation>timeout 180 python &lt;your models-payload read&gt;</invocation><expect>a stated verdict on whether VXX appears in the current models/holdings payload, the ARTIFACT read named with its location and vintage, and the ticker list or count it was drawn from. The DT brief's assertion is NOT acceptable as the evidence.</expect></criterion> `S7-AC4` -- IS VXX ACTUALLY HELD. The issuer did not read this and said so; this is its first read.

<criterion id="S7-AC5" cell_refs="AT2-s-7"><invocation>timeout 120 python -c "print('VERDICT RECORDED IN THE INSTANCE')"</invocation><expect>a GO or NO-GO for AT2-s-2 recorded in the instance, naming every hop that would drop or raise on a five-class value, and naming VXX's held status. A GO requires every hop from AC3 to read SURVIVES.</expect></criterion> `S7-AC5` -- THE GATE ON THE RETAG, STATED AS A VERDICT WITH ITS BASIS.

<criterion id="S7-AC6" cell_refs="AT2-s-7" judgment="true"/> `S7-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the chain is genuinely five-class-safe end to end, or safe only at the hop the previous cell hardened. **Record the readings and offer NO verdict.**

<expected_criteria>S7-AC1, S7-AC2, S7-AC3, S7-AC4, S7-AC5, S7-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S7-1.verify-the-five-class-chain.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~4/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-7`.
<owned_cells>AT2-s-7</owned_cells>
Read-dependencies, NOT claimed: `AT2-s-6` precedes it; `AT2-s-2` is gated on its verdict and is NOT yours.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. ⚠ NOT covered and stated rather than
implied: the issuer measured ONE hop (the :239 subscript) and has NOT traced the chain; VXX's held status
is the DT brief's assertion and was never independently read. Those two gaps are why this cell exists,
and AC3/AC4 are their first measurements.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~4/POSN_ASTTAX.TO-S7-1.verify-the-five-class-chain.proof_of_spec.json
</proof_of_spec>
