# NFRA_MCPINDEX task order -- `MX-a-8` -- Black Diamond's analysis record, refreshed against today's silver, naming its FIRST tool (FWD-4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-a-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~21</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only analysis.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only S3 listings and object reads under the operator's own credentials; nothing granted.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-a-3 record is the pattern.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-a-8` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, ruling B5)

**Why.** FWD-4 (`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md:132-136`): "a property with no analysis
ships no tool". Black Diamond's record (`deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-blackdiamond.result.md`, MX-a-3)
was read 2026-09-21. Since then the four BD Playwright documents were stripped to merge-only and the transaction leg
moved to the REST producer (MX-s-14), so its live-prefix and freshness facts are stale. The first BD tool (MX-t-13) is
cut from THIS record.

**The act:**
1. Read MX-a-3's order (`task-orders/NFRA_MCPINDEX.TO-MX-a-3.analysis-blackdiamond.md:30-58`) and its record. Keep its
   structure. Re-read every live fact at today's state: `s3://opal-data-bd/silver/` (object count, bytes, newest
   partition per prefix), grain, freshness field and latest value, and the producer per leg.
2. Write `deliverables/0.9.0_WK_NFRA_MCPINDEX~21/analysis-blackdiamond.r5.result.md`. Its first line after the title is
   `read_at: YYYY-MM-DD` (the UTC date of your live read). It carries these 9 sections as headings, in this order:
   `Live prefixes`, `Grain`, `Freshness`, `Scope rule`, `Never-sum`, `Common questions`, `Question to tool`,
   `Read fence`, `No-data`.
3. **Scope rule.** Name the key segment that separates firms and state that a principal resolves only its own firm.
   The first tool never reads across firms.
4. **The FIRST tool.** In `Question to tool`, pick ONE question class that is fresh, answerable from one prefix and
   commonly asked. Give it one tool with a C3-valid name starting `bd_` and name every other question's route
   (a later tool, or the typed query). In `Read fence`, list the exact prefixes that tool reads and nothing wider;
   MX-t-13 builds the read role from that list.
5. A leg that is stale or dead today is named as such in `Freshness`, with its newest date. It never feeds the first tool.
6. Run AC1, write J1's material (the record itself), and commit.

## 2. BOUNDS

1. Read-only. No write to any bucket, no schedule, no document, no role.
2. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W21-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-a-8" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/a8.AC1.sh; echo "exit=$?"</invocation><expect>sections 9 of 9; read_at on or after 2026-09-30 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-a-8" judgment="true"><!-- a8.J1, graded at L9 by 3.0.0_SA_CVO~O, never self-graded (record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO): is the record sufficient for a builder holding only it to cut the first BD tool -- one question class, one bd_* tool, an exact read fence, a firm scope rule -- with every live fact carrying its read date? --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-a-8.analysis-blackdiamond-r5.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B5 and round-5 order item 4. MX-a-3 is complete; this is its
refresh, because B5 cuts the record and its first tool this round. Dry-run at base: a8.AC1 FAIL (record absent). Chain
head of MX-t-13 -> MX-r-7.

<status>pending</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
