# TO IRPT_DASHBD.TO-DB-b-198 -- CONTRACT 0.4.1: the percent-points unit sentence and a unit_scale field on every percent member; and the ABSENT_KIND PROPOSAL (a closed vocabulary for why a figure is absent) with its four-postulate record and a word-boundary token census; no code reads absent_kind

<to_id>IRPT_DASHBD.TO-DB-b-198</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~163</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-104 ANALYSIS item 2 and the rulings on rows W158-S1 and W158-S4 ("the gold stores PERCENT POINTS ... Contract 0.4.1 adds one sentence saying so, and a `unit: percent_points` field on each return member, so a consumer can reject a fraction. The kind becomes a FIELD, `absent_kind`, with a closed vocabulary ... It arrives as a proposal with its four-postulate record (rule 24) before any code uses it.") | **Rows:** IRPT_DASHBD-D2-W163-S<k> | **Decomp cell:** `DB-b-198` (decomposition section 106) | **outcome_ref:** FWD-21 | **depends_on:** none.

**The issuer's reading of the ruling (stated).** The contract's `unit` values are `percent`, `dollars`, `series`, `text`, and the components and every checker key on `unit == "percent"`. Renaming that value would break them, so the ruling's intent ("a consumer can reject a fraction") is met by adding the field **`unit_scale: "percent_points"`** to each member whose `unit` is `percent` and leaving `unit` as it is.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-163` (branch `wk-IRPT_DASHBD-163`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~163/`.

**What exists.** The performance report contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` is at version 0.4.0 (sha256 `45c6c2005663ae5cf356ae890133f90cc1579093be0b0fb27e85c0f3d9710523`; its lineage holds 0.1.0, 0.2.0 and 0.3.0). Its `document.shape` says percent members print "from the decimal fraction to one decimal place", but the sample builder stores PERCENT POINTS (a stored 1.5 means 1.5 percent; the builder's header: "the decimal fraction times 100"), and the round-103 component fix prints the stored scale. The contract's words are wrong and nothing in a member says which scale it holds. Separately the report prints WHY a figure is absent by guessing from reason text; the CTO rules the kind becomes a field of its own, but only after a proposal.

**The cell (`DB-b-198`).**
1. **Contract 0.4.1 (the contract is YOURS to edit in this cell; no other file under `org/standards/`).** Bump `contract_version` to `0.4.1`; add the 0.4.0 bytes to `lineage` as `{"contract_version": "0.4.0", "sha256": "45c6c2005663ae5cf356ae890133f90cc1579093be0b0fb27e85c0f3d9710523", ...}` the way the existing lineage entries are written; in `document.shape` replace the sentence that says percent prints "from the decimal fraction" with one that says a percent member holds PERCENT POINTS (a stored 1.5 means 1.5 percent), printed to one decimal place, and that a consumer must not scale it again (the sentence must contain the words "percent points" and "1.5"); add the field `"unit_scale": "percent_points"` to EVERY member whose `unit` is `percent` and to no other member. Every other byte of every member stays as it is (the checker compares each member to its 0.4.0 version in git history, ignoring only `unit_scale`). Update `open_changes` if it mentions the decimal fraction. The file stays valid JSON, ASCII.
2. **The `absent_kind` proposal** as `ABSENT_KIND_PROPOSAL.md` in your folder, with these sections (the checker looks for the headings): `## Vocabulary` (the CTO's candidate closed set, each member defined in one sentence: `NOT_HELD` the client holds none, so the baseline prints a dash; `NOT_APPLICABLE` the figure does not apply; `NO_SOURCE_YET` Opal has no source for it yet; `INSUFFICIENT_HISTORY` the source holds too little history for the period), the field's proposed home (which carrier holds it: the filled-report absent form `{"absent": "<reason>"}` gains a sibling `kind`? or the contract member? you decide from the code and the shape check `p97 check_sample_shape` that today requires the absent form to be exactly `{"absent": str}`, and state what each choice would change), and who reads it; `## Four-postulate record` (CLAUDE.md rule 24, `rcg/rulings/RULINGS.jsonl` R-0006 and R-0009 for the form), with a sub-heading each for **MECE** (the domain is the sample's ABSENT MEMBERS at member grain: a member holding the absent form, or a per-account map in which every entry is absent: 73 of 117 in the round-103 sample; and the by-row ABSENT ENTRIES: print the denominator for each; classify every one of them into exactly one kind BY SUBTRACTION from the printed denominator, never by a forward list, and print the tally per kind and the remainder, which must be 0; name any member no kind covers), **SAME GRAIN**, **INTENT COHERENCE** (one axis, one intent) and **STATE COHERENCE** (name which values one remedy does NOT move); `## Token census` (a WORD-BOUNDARY census of each of the four tokens over the declared scope `portal/src/pages/InvestorReporting org/standards org/missions/D9/IRPT data/assets/scripts/gold/irpt_reporting`, EXCLUDING your own folder: use `git grep -w -c <TOKEN> -- <scope paths>` with `:(exclude)org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~163`, print the command, the files scanned (`git ls-files` count of the same scope) as the denominator, and each token's count; a token that already exists with another meaning is a finding: say so). The sample you read for the domain is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/HOUSEHOLD_SAMPLE.json` (client data, read-only; counts only in the proposal).
3. **No code reads `absent_kind`.** You add the proposal and the contract fields only: no component, builder or checker is edited; the field is not added to any sample.
4. **Record** `CONTRACT_041_AND_PROPOSAL.json` in your folder with exactly: `proposal_file` (the repo-relative path of `ABSENT_KIND_PROPOSAL.md`); `proposal_sha256`; `census` {`method` (the command shape), `files_scanned`, `tokens` (each of the four tokens -> its integer count)}; `domain` {`absent_members_at_member_grain` (73 expected: the checker recomputes it from the sample), `by_row_absent_entries` (integer)}; `code_reads_absent_kind` false; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts and words only: no figure, no account number; a sha256 value is exempt from the digit rule.

<criterion id="DB104-2-AC1" cell_refs="DB-b-198"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r104/p104_round104.py" . DB104-2-AC1</invocation><expect>DB104-2-AC1 PASS</expect></criterion>
`DB104-2-AC1` -- the contract is 0.4.1 with the 0.4.0 bytes in its lineage; every percent member carries unit_scale percent_points and no other member does; document.shape states percent points with the 1.5 example; no member changed beyond unit_scale (compared with the 0.4.0 version in git history); the proposal file exists and is hashed, carries the Vocabulary, Four-postulate record (MECE, SAME GRAIN, INTENT COHERENCE, STATE COHERENCE) and Token census sections and the four vocabulary members; the census names its method, files scanned and a count per token; the domain's absent-member count equals the sample's; no code reads absent_kind; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB104-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every component, builder, checker, sample and every other contract.
- **No write of any kind to AWS, no deploy, no push, no vendor call, no secret read.** Reads only: repo files and the private sample. A denial is recorded verbatim, not retried by another route. Use `comp-find` or `git grep` (a census command is allowed inside this cell as its method) and never a blind recursive grep for anything else.
- **Client data.** The sample is client data: counts only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a member no vocabulary kind covers exists, say so in the proposal's MECE section (the proposal may then list a fifth candidate for the CTO's ruling); do not force it into a kind. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W163-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~163/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-198.contract-041-percent-points-and-the-absent-kind-proposal.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 106 (round 104), cell `DB-b-198`.
<owned_cells>DB-b-198</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB104-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~163/IRPT_DASHBD.TO-DB-b-198.contract-041-percent-points-and-the-absent-kind-proposal.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB104-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the contract change (version, lineage, the sentence, the number of members given unit_scale); the proposal's vocabulary, the carrier you propose for the field and what it changes; the MECE tally (each kind, the remainder); the census counts; any member no kind covers; row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract edit and a proposal document; nothing is read by code, served, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 6 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
