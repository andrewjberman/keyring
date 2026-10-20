# ANDREW_DIRECT 2026-10-20 ~16:30Z -- NFRA_FIDUPL: agent tries first, headful Google Chrome via the Claude-in-Chrome plugin

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-20 ~16:30Z (12:30 PM ET)
- **Amends:** `1.0.0_SA_CTO~DELL1` msg 8705 (headed Chromium under Xvfb) and the CRO hand-seed record
  `ANDREW_DIRECT_20261020_1628Z_FIDUPL_RDP_HANDSEED_WILLING.md`.

## Verbatim (five messages, in order)

> I recommend the agent trying to navigate it first however

> it should be done in a headful browser though.

> i recommend using google chrome

> and that way we can use claude in chrome plugin

> It is better that the agent is able to succesfully navigate this entire thing headful on its own because then we know we
> have that fallback in order if the agent for whatever reason has to do it again.

## What it sets (surfaced, not adjudicated)

1. **Agent-first.** The agent attempts the sign-in before any Andrew hand-seed. The RDP hand-seed (record @74377e98a6) is the
   fallback, not the first move.
2. **Headful**, not headless (a full-UI browser; a more human fingerprint, which bears on the `ATT` device verdict).
3. **Google Chrome specifically**, not Chromium. (This changes the CTO's "headed Chromium" to real Google Chrome.)
4. **Driven via the Claude-in-Chrome plugin** -- an agent navigates the real Chrome, rather than only a scripted Playwright
   driver. The estate's `mcp__claude-in-chrome__*` tooling / `anthropic-skills:chrome-browser`.
5. **Prove the whole login headful, end to end, agent-driven.** The value is a known-good, repeatable fallback: if the login ever
   has to be redone, an agent can navigate the full flow (login -> "Text me the code" -> Quo code -> home) in headful Chrome.

## Build notes for the CTO / CloudOps (not adjudicated)

- Headful on the Linux box still needs a display: real Google Chrome under Xvfb or a VNC-backed X, which is compatible with
  "headful" (the browser renders full UI; it is not `--headless`).
- Running the Claude-in-Chrome plugin on a headless EC2 Linux box is a setup question for CloudOps (the extension + an agent
  session attached to that Chrome). Whether the daily unattended pull also runs through the plugin, or only the fallback does,
  is the CTO's design call.
- The flow to navigate is the one in `RESEARCH_20261020_NFRA_FIDUPL_LOGIN_FLOW_HAR5.md` (@5610d79894): login, click "Text me the
  code", read the Quo code (...3066), submit. The OTP routes to Quo automatically.
