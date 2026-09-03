# ANDREW-DIRECT 2026-09-03 ~02:1xZ -- "Limb check" transcript: the canonical workflow L1-L10 restated, and the COMPEFFICACY pickup point

**Receiving seat:** `1.0.0_SA_CTO` (laptop base, post-restart session)
**Channel:** Andrew at the CTO terminal, mid-turn, handing the seat a voice-transcript FILE:
`C:\Users\AndrewBerman\Desktop\transcripts\Limb check_9364.txt` (4,062 bytes, 46 lines, mtime 2026-09-02 22:06 local).
His covering words at the terminal, VERBATIM: *"I just sent this to COO as well, it details where we are picking up and qualifies that we need to proceed COMPEFFICACY in the canonical pattern and make sure that we are abiding by it."*
**Time:** 2026-09-03 ~02:1xZ UTC.

The body below is the transcript's bytes, unedited (`cat` of the file, no paraphrase -- the phrasing is the ruling). A "what this binds" section follows it.

---

## Verbatim, entire (the transcript file)

I want to pick up here from the rebooted device so that we can proceed through our water test of NFRA underscore comp efficacy in a proper canonical fashion.
So once again, I'm going to briefly run through the RIMS order of the canonical workflow because I want to make sure that we always abide by the exact standard operating procedure.
So L1, that is CRO. The CRO writes a brief. I will discuss with them what the brief is on. They write it.
LIM2, endpoint alignment, that is CTO running their endpoint dash dash forward skill on said brief.
By doing that, they have a pretty good idea what this project is going to be. They've discussed it with me.
So as a result, they can proceed to L3. They register according to the new file tree structure.
They register the project and the macro, the macro project code. They do that whole process.
It is tagged to a fabric. It is tagged to a directive. That is L3.
Now that we've got that registered project, it's L4, also CTO. This is the PRD writing.
Now we're putting that together based on the product arc. It is using the endpoint summary and making sure to include that surface manifest,
which is going to be necessary in the next step. I want you to notice here, L1 is only CRO.
There's no other agents in that. It is always CRO in L1. L2 through L4 is only CTO.
There is no COO engagement. There is no CVO engagement. L2 through L4 is only CTO.
Now, L5, we have COO come out. COO runs the decomposition. They run AtomDecomp.
After that is done, they have those surfaces, which they received from the surface manifest.
Now they're doing a battery. They're running through their lenses. They're running through the comp tools.
We're enriching that data.
When that is put together, they're going to dispatch task orders. LIM 6. You may notice here, there is no CVO engagement.
Let me say that again. There is no CVO engagement in L5 and L6. Nothing.
That is COO activity. Do not get this out of order.
If there's any chance of doing this out of order, we need more gates because this has to be done correctly.
Now, the workers are working. This is L7. They've come online after the L6 dispatch.
If those workers see that the spec asserts it's actually different than the world is, they have their surprise gate.
They can run those surprises right up the ladder to CVO.
Oh, now CVO is engaged. This is the first time in this flow that CVO is engaged. Please note that.
As a result, CVO is going to monitor that surprise channel.
They're going to see what comes through the wire, and they're going to investigate those investigation files.
They are going to move the ones that actually have legs, the ones that are actually problems, to the remediations group.
We have all this covered. That's the adjudication. That's LIM-9, that whole adjudication between the investigations and remediation files.
And now, once – this is a very important part. Please listen.
LIM-10, routing. We do not route until the job is over.
This needs to be a tight circle. So the task orders need to be tight.
They need to be a quick, nice, tight little circle so they can get done.
They're simple task orders so they can get done.
We don't have some big, giant fuck-up so that we can't go through our little circle here.
We need to go through the wheel in order.
That means that no routing, no LIM-10 routing until all task orders are complete.
The surprise channel, all investigations, completely checked by CVO.
Only then do we know if we have to just proceed as normal.
No investigations mattered. There are no remediations. We're good to go.
If that's the case, we just proceed with the next round of L-6 dispatches.
So we just proceed onwards. If there is a problem, a spec error, we are also going back to L-6.
If there was a decomp error, we're going back to L-5.
And if we really fucked up and there's a scope change, obviously we have to go back to L-2.
But that is only happening if the task orders are done.
We finish our work. We keep the cycle. Understand? Great. Thank you.

---

## What this binds (read off the words above; surfaced, not adjudicated)

| Step | Owner per his words | Who is NOT engaged |
|---|---|---|
| L1 brief | `4.0.0_SA_CRO` only ("It is always CRO in L1") | everyone else |
| L2 endpoint (`/endpoint --forward` on the brief) | `1.0.0_SA_CTO` only | "There is no COO engagement. There is no CVO engagement. L2 through L4 is only CTO." |
| L3 register (tree structure, macro/project code, tagged to a fabric and a directive) | `1.0.0_SA_CTO` only | same |
| L4 PRD (from the product arc, using the endpoint summary, INCLUDING the surface manifest) | `1.0.0_SA_CTO` only | same |
| L5 decomposition (atom-decomp on the manifest surfaces, then the battery: lenses + comp-tools, enrich) | `2.0.0_SA_COO` only | "There is no CVO engagement in L5 and L6. Nothing." |
| L6 dispatch task orders | `2.0.0_SA_COO` only | same |
| L7 workers execute; a spec-vs-world mismatch goes up the surprise gate to CVO | workers | -- |
| L8 CVO monitors the surprise channel, investigates the investigation files, moves the ones with legs to remediations | `3.0.0_SA_CVO` -- "This is the first time in this flow that CVO is engaged." | -- |
| L9 adjudication between investigations and remediations | `3.0.0_SA_CVO` | -- |
| L10 routing | ONLY after ALL task orders are complete AND every investigation is checked by CVO | -- |

Routing outcomes at L10: no remediations -> next round of L6 dispatches; spec error -> back to L6; decomp error -> back to L5; scope change -> back to L2. "But that is only happening if the task orders are done."

Task orders: "tight", "simple", "a quick, nice, tight little circle so they can get done."

His gate clause: "If there's any chance of doing this out of order, we need more gates because this has to be done correctly."

## Where COMPEFFICACY picks up (measured at this seat at startup, not recalled)

- L2-L5 landed before the restart: L2 endpoint @`b886c164d2`; L3 registration @`41d11d178d`; L4 PRD v0.2 @`e906c6f156`, v0.3 @`264bc9fa92`; L5 decomp @`e8641a324c` / `ee52600980` (39 cells, NO TO cut). Predecessor log: `org/tier1_exec/1.0.0_SA_CTO/logs/2026-09-03/compefficacy_first_tree_test_run_L2_to_step6_2300-0115Z.md`.
- L6 was OPEN when pencils went down: `2.0.0_SA_COO` had three tree task orders written at 01:0xZ, UNCOMMITTED on disk (COO's own statement in 92876). One of them is addressed to this seat: `NFRA_COMPEFFICACY.TO-CE-DISC-2` (the 4.3 answer-state spellings, STAGE 0 decide-first) -- visible to `/to-check` at 02:06Z as PENDING, issued by `2.0.0_SA_COO`, no GO received at this seat yet.
- Under this word, this seat holds at L6/L7: it executes the CE-disc-2 task order when the COO dispatch arrives (Andrew: "await my further command, which will come from COO"), and otherwise cuts nothing, routes nothing, grades nothing.
