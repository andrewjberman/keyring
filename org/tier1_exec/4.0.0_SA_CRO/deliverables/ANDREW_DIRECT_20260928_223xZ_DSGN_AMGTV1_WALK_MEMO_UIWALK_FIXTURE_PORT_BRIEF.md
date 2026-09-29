# ANDREW-DIRECT 2026-09-28 ~22:3xZ -- DSGN_AMGTV1: walk-memo transcript, /ui-walk, fixture-port analysis, brief

**Channel:** the 4.0.0_SA_CRO~Z terminal on site Z (Claude Code session c0f72437), typed by Andrew.
**Received by:** 4.0.0_SA_CRO~Z. **Recorded:** 2026-09-28T22:4xZ, same turn.

## VERBATIM

> I need you to use transcriber solution openai-whisper to transcribe the below memo: "C:\Users\Opal
> Bloomberg\Downloads\AMGT WALK_3557.m4a" using the attached folder of snapshots as references that are mentioned in
> the transcript: "C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Pictures\Screenshots\AMGT_walk_v1". After you have
> done this, and the transcript is finished processing and you have analyzed it fully and completely, breaking up
> relevant chunks for the various surfaces (Lead Panel by Trending/Breakout/Security, by Chatter/Price, by
> Rank/Chart), Lead Panel with Security on the timeline matter and associated backend/data/adapters, Thesis tab, Exec
> Mgmt tab, Peers tab, Model tab, and Posture Tab, tracking all my feedback. I then want you to do a /ui-walk of those
> same surfaces (on the localhost:5174 build), and scan for UI that needs to be updated. After doing these things and
> synthesizing all this information, i want you to analyze the various fixtures which should be ported for AMGT
> frontend use and associated systems. This includes the "Positioning" page "Holdings Breakdown" and associated
> ETFClassifier table setup (which I mentioned should include the securities added to AMGT), the "Philosophy"/"Model
> Portfolio page cards with associated popup modals, the Global RSI Modal from "Market Overview" page, as well as the
> various charts displayed throughout "Model Portfolios" and "Factor Charts", lastly check out the News Scanner
> Pipeline and how that resolves in the "Topic Cloud" on the "Market Overview" Page. I want to be reusing the same
> chart components and styliing where relevant so we can expedite in-pattern design styling for the various surfaces
> covered by the AMGT "Security Analysis" Portal page and application. All of this should be synthesized in a
> structured brief that covers the current state and how it needs to be evolved which will be the basis for a new
> project, DSGN_AMGTV1, on this box the sitez box.

## What this seat reads it as (the phrasing above is the ruling; this is not a paraphrase of it)

- The deliverable is an L1 brief for a NEW project code `DSGN_AMGTV1`, on site Z. L2 (endpoint) and L3 (register)
  stay with 1.0.0_SA_CTO / 1.0.0_SA_CTO~Z. This record does not register the project.
- "use transcriber solution openai-whisper" is the word for the local install of `openai-whisper` (PyPI) plus
  its model weights download. The audio is transcribed on this box and is not sent off it.
- The /ui-walk runs on localhost:5174 only, per the skill's own guard.
