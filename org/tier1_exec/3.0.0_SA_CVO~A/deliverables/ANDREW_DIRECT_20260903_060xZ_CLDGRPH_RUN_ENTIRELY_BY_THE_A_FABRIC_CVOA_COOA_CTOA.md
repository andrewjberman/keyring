# ANDREW-DIRECT 2026-09-03 ~06:0xZ -- NFRA_CLDGRPH is run ENTIRELY by the ~A fabric

**Channel:** Andrew, direct, at the `3.0.0_SA_CVO~A` terminal.
**Received:** 2026-09-03 ~06:05Z (session `918d31e5-1382-4324-8699-9c45bfb8ed69`).
**Recorded by:** `3.0.0_SA_CVO~A`, same turn as receipt, per CLAUDE.md "Andrew-direct instructions -- RECORD + BROADCAST, same turn".

---

## 1. HIS WORDS, VERBATIM

> not acceptable, CLDGRPH needs to be run entirely by this fabric CVO~A COO~A CTO~A

Nothing is paraphrased. The phrasing IS the ruling.

## 2. WHAT IT WAS SAID TO

It was said in reply to this seat's report that it was **idle at L8** and waiting on
`2.0.0_SA_COO~A`'s L5/L6, and that four backlog items had been ruled outside this lane's
envelope. "not acceptable" attaches to that posture.

## 3. SCOPE -- SURFACED, NOT ADJUDICATED

This seat does **not** adjudicate the scope of a sovereign instruction, wider or narrower
(CLAUDE.md s.2, "NEVER convert Andrew's word to ONE agent into a gate/stop on another --
verbatim scope; relay, never adjudicate"). What the words say on their face:

- The project is `NFRA_CLDGRPH`.
- It is run **entirely** by "this fabric", which he then enumerates: `3.0.0_SA_CVO~A`,
  `2.0.0_SA_COO~A`, `1.0.0_SA_CTO~A`.
- He does not re-assign limbs and does not name any other seat.

**What this seat does NOT decide, and flags as needing the CTO's word:** whether "entirely"
places **L7 execution** on these three lanes, and if so which of the three executes. That
reading is available and is the one that collides with the gate in section 4. This seat
states the question; it does not answer it.

## 4. THE MECHANICAL COLLISION -- MEASURED, NOT INFERRED

Andrew's word, read as placing L7 on these lanes, collides with a **live gate that was itself
installed on an Andrew-direct**. Both are his; only he or the gate's owner can resolve which
governs. Measured at source this turn:

`.tools/to-pipeline-gate.py`

```
:86   # TIER-2 SEATS ONLY. A NEW tree task order whose <issued_to> names a Tier-0 serial
:96   TIER01_RE = re.compile(r"^(?:0\.0\.\d+_[A-Z]{2}_|\d+\.\d+\.\d+_SA_)")
:166          if TIER01_RE.match(base):
:168              "<issued_to>%s</issued_to> names a TIER-%s seat. L7 workers are TIER-2 ONLY "
:169              "(Andrew-direct 2026-09-03, @716a9bc7ce call 3, LD-0521)"
:729   # GATE (i) -- Tier-0/1 in <issued_to> on a NEW tree TO is refused
```

`TIER01_RE` matches `\d+\.\d+\.\d+_SA_`. **All three named lanes are `_SA_` serials**, so all
three match. A new tree task order under `NFRA_CLDGRPH` issued to `1.0.0_SA_CTO~A`,
`2.0.0_SA_COO~A` or `3.0.0_SA_CVO~A` is **REFUSED by gate (i)**, mechanically, at commit.

The spine says the same in prose:
`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L7 -- *"Owner: the Tier-2 worker named in
`<issued_to>`. Not engaged: every Tier-0 and Tier-1 seat as a worker."*

**Therefore:** under today's mechanism the ~A fabric can carry L1-L6 and L8-L10 for
`NFRA_CLDGRPH`, and **cannot be issued an L7 task order at all**. The instruction and the gate
cannot both be satisfied as they stand.

## 5. A SECOND THING TO SURFACE, STRUCTURAL RATHER THAN MECHANICAL

If `3.0.0_SA_CVO~A` executes work at L7, it later adjudicates that same work at L9. The CVO's
independence is structural -- *"no implementation stake in the work being reviewed"*
(`org/tier1_exec/3.0.0_SA_CVO/README.md`). A seat grading its own execution is the
self-attribution class this estate has already paid for. **Stated, not decided.** If Andrew's
word puts execution here, this seat executes and says plainly, on every such row, that the
grader and the author are the same seat.

## 6. WHAT THIS SEAT DOES NOT DO

- It does **not** edit `.tools/to-pipeline-gate.py`, the spine, or any other workflow
  mechanism. Andrew's 05:1xZ word (@8e134cc126) withheld that surface from the ~A lanes absent
  `/open-calls` egress, and an agent-made gate is banned outright (CLAUDE.md s.2).
- It does **not** rule that the gate overrides Andrew, nor that Andrew overrides the gate.
- It does **not** narrow "entirely" to keep its own prior idle posture.

## 7. ROUTED, SAME TURN

Broadcast to `1.0.0_SA_CTO~A` and `2.0.0_SA_COO~A` (the two named lanes), and to
`1.0.0_SA_CTO`, `2.0.0_SA_COO` and `0.0.0_AB_MSTR` so that `latest + most-restrictive` has
something to bind on. The gate's owner is `1.0.0_SA_CTO`; the L6 issuance that will meet the
refusal is `2.0.0_SA_COO~A`'s.

## 8. VINTAGE

Local `HEAD` at recording: `88c961297b`. Push state **UNREAD** at this seat -- no `ls-remote`
run this session, so no push claim is made in either direction.
