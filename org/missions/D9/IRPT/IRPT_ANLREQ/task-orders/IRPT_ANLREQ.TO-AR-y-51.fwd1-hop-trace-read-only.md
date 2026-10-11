# TO IRPT_ANLREQ.TO-AR-y-51 -- FWD-1 traced hop by hop, read-only: what is live, what is built and not live, what has no code

<to_id>IRPT_ANLREQ.TO-AR-y-51</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (records only: one table. Nothing is built, uploaded, applied, pushed or changed.)
**Decomp cell:** `AR-y-51` (`decompositions/IRPT_ANLREQ_DECOMP_R5_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it. The portal's code is readable at `C:/dev/wk-irpt-anlreq-51/portal` (READ ONLY; use
  `git -C C:/dev/wk-irpt-anlreq-51/portal show origin/DEV:<path>` and `origin/PROD:<path>` to read a branch without changing anything).

### THE CELL (`AR-y-51`, inlined)

*ONE table: every hop of FWD-1 from the filed ticket to the report opened on it, each with its state, its owner, what it waits on
today, the evidence and a claim word. Read-only.*

Why: the project has run four rounds and its first outcome, FWD-1, is not live end to end. The CTO will use this table either to cut
the remaining hops in order across three lanes, or to carry the case for a closer to Andrew. It has to be true hop by hop, and it has
to say plainly where it does not know.

1. **Read FWD-1's own text** in `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (the ENDPOINT section; quote it with its line
   number as `fwd1_text_source`). Then read the three L8 packets for what each round built and applied:
   `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE_ADDENDUM_1_RELEASES_20261011.md`,
   `.../IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_20261011.md` with its `..._ADDENDUM_1_20261011.md`, and
   `.../IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md`. They are other seats' summaries: starting points, never evidence of a hop's state.
2. **Lay the journey out as hops**, in order, from "a person files an Analysis Request ticket" to "the finished report is opened on
   that ticket". Expect something like: the form and its submit; the upload and its acceptance; the request record and its ticket
   binding; the generation job and its producer; the retained report; the package and its ATTACH to the ticket; the ticket's package
   block; the report opened from it. Use the hops the code and the PRD actually show, not this list. A hop is one hand-over between
   two components: if you find yourself writing "and" in a hop, split it.
3. **For each hop, decide its state by evidence you read yourself:**
   - `LIVE`: the code is deployed where the journey runs. Evidence is a live read or an applied-artifact record you opened: for a
     Lambda, `aws lambda get-function-configuration --function-name <name> --query '[CodeSha256,LastModified]'` (single-resource reads
     are allowed; use the `.tools/aws` shim) compared with the source map's `artifact_sha256` for that function AND the presence of the
     hop's code in the commit the entry pins; for the portal, the code present at `origin/PROD` (client and staff pages run PROD) -- say
     DEV-only when it is on `origin/DEV` and not PROD, and count that as `BUILT_NOT_LIVE`.
   - `BUILT_NOT_LIVE`: the code exists on a branch or in the tree and is not what is deployed. Say where it is and what it waits on.
   - `NO_CODE`: you searched for it and it is not there. Say what you searched and over what (a search that returns nothing is only
     evidence when you name its scope).
   - `NOT_DETERMINED`: you could not tell. Say what you would need. This is an honest answer and better than a guess.
4. **Owner** of each hop, one of: `IRPT_ANLREQ_Y` (this workstream), `IRPT_ANLREQ_G` (workstream G: the resident releases, the packager
   and the attach), `TCKT_VNEXT` (the ticket service), `PORTAL` (a portal page or its contract readers; DSGN_IRPTV1 owns Investor
   Reporting pages), `IRPT_BCKEND`, `IRPT_YCDGEN`, `OTHER` (name it in `waits_on`). Decide it from who issued the order that built or
   will build the hop (the task-order files under `org/missions/D*/<MACRO>/<CODE>/task-orders/` and `org/tier2_senior/*/task_orders/`).
5. **`waits_on`**: what, today, stands between this hop and LIVE -- an order id and its status as the order file reads at HEAD, a
   release that was rolled back, a push that needs a human word, another hop. `NOTHING` when it is live.
   Facts you will meet and must re-read rather than copy: irpt-status release 5 was applied and ROLLED BACK on 2026-10-11 (live is
   revision 6, `6idtFvAm...`), so nothing from rounds 3 or 4 is live on that function; the Ticket Center changes of round 3 are on portal
   DEV; a resident release `st30` and a ticket-service release were being applied this morning by other seats (read their order files'
   statuses and the live digests; do not assume either way).
6. **Write two files** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/trace/`:
   - `FWD1_HOP_TRACE.json`: `{"fwd1_text_source": "<file>:<line>", "fwd1_text": "<the quoted text>", "read_at": "<UTC time>",
     "tree_head": "<git rev-parse --short HEAD>", "hops": [{"n": 1, "hop": "<from what to what, one sentence>", "state": "...",
     "owner": "...", "waits_on": "...", "evidence": ["<file:line, or the command and what it printed, or order path and status>", ...],
     "claim": "measured|inferred|inherited"}, ...], "first_hop_not_live": <n or null>, "not_determined": [<n>, ...]}`.
     `claim`: `measured` when you ran the read yourself; `inferred` when you reasoned from code; `inherited` when you rest on another
     seat's record (name it in the evidence). A `LIVE` state may not rest on `inferred`.
   - `FWD1_HOP_TRACE.md`: the same as ONE table (n, hop, state, owner, waits on, claim), then two short paragraphs: where the journey
     first stops, and what you could not determine. Plain words; no verdict on what should be done.
7. Commit both. No name of a client, no figure, no signed link, no document content anywhere.

### ACCEPTANCE

<criterion id="AR51-y-AC1" cell_refs="AR-y-51"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r5/trace_check.py --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y51-TRACE-OK</expect></criterion>
`AR51-y-AC1`: the trace file exists and every hop has a state, an owner, what it waits on, evidence and a claim word; no LIVE rests on
an inference. The check grades the table's FORM; whether each state is true is read by the issuer and the CTO.

<expected_criteria>AR51-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ ONLY on everything else, the world included: single-resource `get` / `describe` reads through `.tools/aws`; no list or
  enumeration call; no invoke of any function; no request to any API route; no build; no upload; no push; no edit of any product file.
- If a read is refused, record the refusal as the evidence and the hop as `NOT_DETERMINED`; do not look for another identity.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R5_Y.md</decomp_doc>
<owned_cells>AR-y-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR51-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-51.fwd1-hop-trace-read-only.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-51`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR51-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- read-only; the write set is two record files in the worker's own folder. comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- single-resource reads the box's identity already makes; a refused read is recorded, never worked around.
comp-adversary: DECLARED-NOT-APPLICABLE -- the cell decides nothing and changes nothing; its failure mode is a state copied from a summary, which the face forbids (a LIVE may not rest on an inference, and the check refuses that).
lane: the worker's own deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO ruling msg 4860 (the read-only trace before any closer is carried to Andrew). DIRECT-ACT path: one cell, LOCAL, records only.
- `AR51-y-AC1` base: FAIL as expected (no trace file), run by the issuer before the cut.
- Seating: slot ~52 is reused; its round-3 order is terminal.
