# TO DSGN_IRPTV1.TO-IV-e-47 -- UIR-07, the Global merge: full-name matches first by the server's predicate, each firm's served order kept otherwise

<to_id>DSGN_IRPTV1.TO-IV-e-47</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~25</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 (UIR-07) | **Decomp cell:** `IV-e-47` (decomp v7 addendum 2) | **outcome_ref:** FWD-3 (UIR-07) | **depends_on:** IV-e-37 (same slot, its ClientSearch.tsx changes) | **slot:** ~25, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-47` -- UIR-07, Global view. 1.0.0_SA_CTO's ruling (101590, 101594; PRD v0.16): the directory search ranks an exact full-name match
first on the server (served, 33 of 33 targets at rank 1). In Global mode the page asks each permitted firm and CONCATENATES the answers,
so an exact match sits anywhere from 1 to 12 depending on firm order. The ONE exception to "the page never re-ranks":

- **In Global only**, the merge of the per-firm answers puts full-name matches first, using the server's predicate: the entry's name
  tokens equal the query's tokens, in any order (case-insensitive; a comma and extra whitespace are not tokens). Every other row keeps
  each firm's served order, and the firms keep their current relative order.
- Never within one firm's list: a single-firm search renders exactly the served order, unchanged.
- Acceptance line (CTO): "anna thiessen" in Global puts the client first in both orders.

**Where it lives:** `header/ClientSearch.tsx` :98-106 (the Global `Promise.allSettled` over each firm's browse, then
`setRows(toOptions(entries, firms))`) and `header/search.ts` `toOptions` :144. This slot's IV-e-37 commit (d6e6eda3) already changed
`ClientSearch.tsx` (grouping by firm, the result count, the keystroke fix): build on it. Read the server's predicate where the record
names it (`handler.full_name_match`, 2.0.0_SA_COO~P record @80833001cb) and mirror it; do not invent a different rule.

**Environment:** this slot's portal worktree, carrying IV-e-37 and IV-e-38. The test file does not exist: write it against a stubbed
api with SYNTHETIC names only (no real client name, no firm token in the file): arms for (1) "first last" in Global, (2) "last first"
in Global, (3) a single-firm search renders served order untouched, (4) non-matching rows keep each firm's served order. Do not start
any server.

### ACCEPTANCE

<criterion id="IVE47-AC1" cell_refs="IV-e-47"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-25/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~25; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-47.global-merge.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: GLOBAL-MERGE-OK</expect></criterion>
`IVE47-AC1` -- the four arms above, each named; prints `VERDICT: GLOBAL-MERGE-OK` only when every arm holds.

<criterion id="IVE47-AC2" cell_refs="IV-e-47" judgment="true"/>
`IVE47-AC2` -- graded at L9 by `3.0.0_SA_CVO` on the issuer's live walk of portal DEV: "anna thiessen" and "thiessen anna" in Global
put the client first. RECORD; never self-graded.

<expected_criteria>IVE47-AC1, IVE47-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else is READ, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client name or figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/header/ClientSearch.tsx
portal/src/pages/InvestorReporting/header/search.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-47.global-merge.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 2, cell `IV-e-47`.
<owned_cells>IV-e-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE47-AC1, IVE47-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-47.global-merge.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE47-AC1,IVE47-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W25-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- ClientSearch.tsx :98-106 read at portal DEV 6757223a (setRows(toOptions(entries, firms)) over the concatenated per-firm answers); the server side is P's record @80833001cb.
lane: the <paths> block IS the grant; same slot as IV-e-37 (which last edited ClientSearch.tsx), queued after IV-e-38 (disjoint paths).
</preflight>

Seating: slot ~25, queue position 3 of 3, after IV-e-38 on the same worktree (CTO 101594: "after IV-e-37 drains" is met by building on
IV-e-37's commit in the same worktree; the chain drains once).
