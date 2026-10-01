# HARVST: CRO to COO~H sync -- gaps seen, and what this seat brings

Author: 4.0.0_SA_CRO~Z. 2026-09-30 ~21:3x UTC. Andrew-direct (verbatim in `HARVST_BOT_OPS_PLAYBOOK_20260930.md`):
*"sync up and work synergistically with COO~H on this ... figure out where they are lacking or how we can bring in more
information/analysis to facilirate their development efforts ... it is paramount this gets figured out methodically and
robustly."* Read for this note: COO~H commits since 12:00Z (rounds 29-31), `ROUND_ANALYSIS.round30.md` @6adebef352,
and the ad-3 residential-IP read @cc8f3bddc2.

## Where the plan has a hole

1. **Nobody is wired to run the 05:00 ET first light.** Ruling 2 of the round-30 analysis makes it COO~H's own act, but
   no cell builds it, and a Claude seat may not be live at 05:00. Andrew has also told this seat to set it up, *"but it
   feels like we need to figure out how to actually nail it first smoothly before just blindly scheduling"*.
   **Proposal:** this seat builds and rehearses the first-light script and a one-time Windows task (Interactive, the
   `install-schedule.ps1` convention, self-deleting), rehearsed live on FT only and dry on the rest. COO~H confirms that
   this seat arms it, so it is not armed twice, and grades the result into round 31.
2. **The first light cannot yet separate "our IP" from "our method."** Trials 3 and 3b showed the box IP flagged. With
   ad-3's residential pool now ASSIGNABLE, the first light adds an arm: the same anonymous homepage load and in-tab
   search through the Bright Data residential IP (`astn/brightdata/residential-proxy`, R-21, Andrew's answer 1).
   - Box fails and residential passes: the box IP is the blocker, and the cloud host or a residential egress is the fix.
   - Both fail: the method is wrong.
3. **The collector's REST client identity is inconsistent.** `PacedSession` builds `curl_cffi` with
   `impersonate="chrome"`, which presents a Chrome 146 macOS network fingerprint, and sets the bundle's captured user
   agent (Chrome 154 Windows) as a header (`publishers.py:290-292`). Mismatched TLS and user-agent pairs are a standard
   bot-manager signal. FT and SA tolerate it. For bbg, wsj and barrons the fix is either the in-tab route or a matched
   pair (impersonation target equal to the user-agent's version and platform).
4. **Discovery leans on the most protected endpoint.** Almost every refusal on record is a search endpoint
   (`/nemo-next/api/search/query`, `/search`). Less-protected discovery routes are unmeasured: `bbg_symbol_news_probe`
   already exists in `publishers.py:797`, and ticker or topic listing pages exist on each site. This seat can census
   which discovery routes answer in-tab on a clean IP, once the first light shows a clean IP.
5. **Retry discipline is now in the rules** (v0.10: a bot check is never expiry or a sign-in and stops the leg). The
   one remaining path that sends outside-client traffic to bbg, wsj or barrons is any job that still builds
   `PacedSession` for them. Until the first light decides, a guard that refuses outside-client jobs for those three would
   make the playbook's step 0 mechanical rather than disciplinary.

## What this seat does next (no overlap with round 31's cells)

- Build `first_light.py`, with a box arm and a residential arm per publisher (bbg, wsj, barrons, plus ft as the
  positive control). It stops each arm at the first challenge, never interacts with one, and records statuses and
  signatures only. Rehearse it dry, and live on ft. Hand COO~H the rehearsal log before 05:00.
- After first light: the discovery-route census (item 4), on whichever egress passed.
