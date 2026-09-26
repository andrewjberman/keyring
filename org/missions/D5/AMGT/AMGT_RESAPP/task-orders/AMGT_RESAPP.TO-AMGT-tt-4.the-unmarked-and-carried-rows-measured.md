# AMGT_RESAPP task order -- `AMGT-tt-4` -- THE UNMARKED AND CARRIED ROWS, MEASURED NOW -- W130-S1 FIRST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-tt-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~165</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a read of the repository and of any Opal surface a row names; nothing is granted.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a disposition copied from the row's own text instead of the resolver: AC1 runs _latest_dispositions itself and requires every row's disposition to equal it, and every open row to carry a command re-run today. Blind spot, stated: the CVO dispositions; this cell measures.
EGRESS CLASS, declared: NONE beyond reads of Opal-owned surfaces a row names; no write, no vendor.
</preflight>

## 1. THE CELL -- `AMGT-tt-4` (round 45, decomposition s.53)

The round-44 L8 compile found **14 of 626 row ids** without the `-Z-` fabric marker (all worker rows: W130-S1, W135-S1, W136-S1,
W137-S1, W137-S2, W138-S1, W140-S1, W140-S2, W141-S1, W144-S1, W146-S1, W148-S1, W150-S1, W152-S1, each prefixed `AMGT_RESAPP-`), one
of them BLOCKING (W130-S1), and **9 carried rows** still owed (Z-S236, Z-S237, Z-S238, Z-S248, Z-S251, Z-S255, Z-W158-S1, Z-S276, and
W130-S1). A census anchored on `-Z-` never sees the fourteen. **Measure all 22 ids where they stand today.**

Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~165/CARRIED_ROWS.json`, shaped `{"rows": [...]}`, one row per
id, **`AMGT_RESAPP-W130-S1` FIRST**. Each row carries: `id`; `disposition` (what `.tools/surprise-row-gate.py`'s
`_latest_dispositions(".", "AMGT_RESAPP")` reads for it now -- import the file with importlib); `owner` (the row's `disarm_owner`, or
who the row's own text names); `closes_when` (one sentence: the act that would close it); and, for every row the resolver does NOT
read as GRADUATED or DISMISSED_WITH_REASON, `measured_now` {`command`, `rc`, `excerpt`}: the row's own claim re-run against the world
today (e.g. for W130-S1, run the naming gate on the file the row names and record what it prints). The rows live in
`org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/`.

## 2. BOUNDS

1. **Measure, never disposition.** You change nothing but your deliverables folder: no row edited, no adjudication written
   (a disposition is the CVO's). A finding that is new is ONE investigation row, appended, and you keep working.
2. No write to AWS, no deploy, no vendor call.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~165/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-tt-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-4.AC1.py; echo "exit=$?"</invocation><expect>rows 22 of 22; missing []; extra []; defects 0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~165/AMGT_RESAPP.TO-AMGT-tt-4.the-unmarked-and-carried-rows-measured.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.6 items 3 and 5. Base: AC1 FAILS (no table; the resolver reads 68 files, 627 items, 11 of the 22 open). One mechanical criterion; the table's content feeds the CVO's L9 dispositions.

<status>pending</status>
<status>complete</status>
<round>45</round>
<slot>~165</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
