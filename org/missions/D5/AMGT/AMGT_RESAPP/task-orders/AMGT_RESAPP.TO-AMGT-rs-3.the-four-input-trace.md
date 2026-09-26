# AMGT_RESAPP task order -- `AMGT-rs-3` -- THE FOUR-INPUT TRACE: where each input that carries eleven failures lives

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rs-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~162</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a read of the repository and, where a served figure is cited, one read of Opal's own deployed function; nothing is granted.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a trace that names a producer by grep hit rather than by the write it performs; AC1 requires each citation to resolve at a commit. Blind spot, stated: ownership is read from the project tree, and a producer shared by two projects is named as shared, not assigned.
EGRESS CLASS, declared: at most ONE AWS READ SURFACE (lambda invoke of Opal's own opal-amgt-scoped-api, GET routes) for served evidence; no write, no vendor.
</preflight>

## 1. THE CELL -- `AMGT-rs-3` (round 44, decomposition s.52)

The round-42 and round-43 analyses find **four inputs carrying eleven of fifteen substance failures** on this endpoint. Before any
of them is built, measure where each LIVES. **Write ONE file,
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~162/FOUR_INPUTS_TRACE.json`, shaped `{"inputs": [...]}`, one object per
input, keyed `input` with exactly these four values:**

- `spans` -- the thesis serves 2 of 23 drafted sentences; 21 are held because the drafting object carries no span field
  (`held_no_span_count 21`, `READ_GATE_ONLY_OBJECT_FIELD_ABSENT`). Outcomes FWD-18, FWD-9, FWD-3.
- `unit_sign` -- the 27 mnemonics the Model tab REFUSES with "unit/sign convention is 'NOT-YET-BUILT'". Outcomes FWD-3, FWD-5, FWD-20.
- `social_chatter` -- social items, and `overlay.chatter` / `overlay.price` served as bare nulls (row Z-S278). Outcomes FWD-11, 13, 15, 16.
- `universe` -- the population the page's rankings and posture comparable read (250 = coverage 89 + holdings 167; the live research
  library is 95; the tenure pool reads 7). Outcomes FWD-17, FWD-19, FWD-15.

**Each object carries:** `producer` (the `path:line` that WRITES the field or table the input needs, not merely a file mentioning it);
`commit` (the commit that line is read at); `owner_project` (read from the project tree: the project whose `<paths>` or row owns that
file, or `shared: A, B` when more than one does); `write_surface` (the S3 prefix or file the producer writes); `served_evidence` (one
measured number from the served plane or the repo, with how it was read); `proposed_cell` (one sentence: what a build cell would
change, in which project).

## 2. BOUNDS

1. **Read only.** You change nothing but your deliverables folder. No server, no deploy, no write to AWS, no vendor call.
2. **A producer is the line that writes.** A file that only reads or mentions the field is not its producer; if you cannot find the
   writer, the object says so in `producer` as `NOT-FOUND: <what was searched>` and AC1 will read it as a defect -- report it.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~162/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rs-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round44/checks/rs-3.AC1.py; echo "exit=$?"</invocation><expect>inputs traced: 4 of 4; missing []; extra []; citation defects 0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~162/AMGT_RESAPP.TO-AMGT-rs-3.the-four-input-trace.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.4 item 5, measure-first: the four inputs sit in other projects' surfaces, and round 45 cuts them where the trace says they live. One mechanical criterion; the trace's content is read at L9 and by the CTO's analysis.

<status>complete</status>

**WORKER CLOSE (`0.9.0_WK_AMGT_RESAPP~162`):** FOUR_INPUTS_TRACE.json written with the four required inputs (spans, unit_sign,
social_chatter, universe), each carrying producer/commit/owner_project/write_surface/served_evidence/proposed_cell. Producers
resolved: lib/research/filings/drafting_build.py:303 (spans), integrations/bloomberg/research/model_block_pull.py:700 (unit_sign,
shared AMGT_RESAPP/AMGT_CORPUS), lib/research/api/scoped_amgt.py:1999-2000 (social_chatter), lib/research/identity/build_universe.py:846-855
(universe) -- all AMGT_RESAPP-owned except unit_sign's, all resolving at HEAD 705dd96375d016310f6b0afc8acb538ddfe78fe0. AC1: inputs
traced 4 of 4, missing [], extra [], citation defects 0, exit=0. No surprise row filed (no premise failure, no missing writer, no
capability gap encountered).
<round>44</round>
<slot>~162</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
