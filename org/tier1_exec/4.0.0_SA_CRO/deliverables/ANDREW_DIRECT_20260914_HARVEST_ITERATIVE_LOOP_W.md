# Andrew-direct: iterative local publication harvesting

Author: 4.0.0_SA_CRO~W
Channel: direct user message at this Codex terminal
Recorded: 2026-09-14 US Eastern; exact message timestamp unavailable

## Instruction (verbatim)

> we need to create a loop strategy where you just keep looping strategies until you can reliably get 5 articles worth of results from a given ticker from a given publisher reliably. Essentially an iterative loop where you first attempt SA, see what works what doesnt take notes for round 2, then move to FT, see what works what doesnt take notes for round 2, an so on for WSJ and then BBG, then with all those notes cycle back on SA for round 2 looking for a different security, then test same security for round 2 on FT, an so on, through round 3 4 5 6 however long it takes to reliably be able to pull 5 articles for a given ticker. Create this loop and test on the local chromium headful over and over until you suceed with three different tickers in a row on 5 diff articles per ticker on each of the 4 publishers.

## Act

Build and exercise a resumable local headful Chromium loop in the fixed order SA, FT, WSJ, Bloomberg. Use one ticker across all four publishers per round and a different ticker in the following round. Retain failures, quality evidence and round-to-round strategy notes. Require five distinct clean substantive articles per ticker and three consecutive different successful tickers per publisher. Publisher failures reset that publisher's streak; no false success from HTTP status, body length alone, login flags, blocked pages, or retries against one ticker. Keep fetched content and browser state local. User authorizes iterative local testing and fixes; no broad cloud backfill or deployment is implied.

## Andrew's live observation (verbatim)

Channel: direct user message during the headful loop, 2026-09-14 US Eastern; exact timestamp unavailable.

> im seeing the trick on this seeking alpha case where you have to let it go when it starts draining and then re press, keep that in your notes

Operational note: decreasing fill is a cue to release briefly and re-press. Do not hold continuously through the drain or treat the drain as successful completion. Final release follows the checkmark. The shared handler already has a drain-recovery branch; validate its detection threshold against this observation.
