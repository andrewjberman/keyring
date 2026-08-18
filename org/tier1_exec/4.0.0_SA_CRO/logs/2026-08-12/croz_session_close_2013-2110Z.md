# 4.0.0_SA_CRO~Z — 2026-08-12 — session close 2013-2110Z

**archetype:** COORDINATE
**secondary_archetypes:** EXPLORE, SCRIBE

Third and final work block. Prior blocks: `croz_w8_bbg_blpapi_pipe_map.md`,
`croz_w7_sharepoint_and_opal_gateway.md`. Window = since `62bca18383`. **8 commits.**

## Window summary

`/open-calls` at this terminal produced two sovereign rulings, then three more arrived by relay, then
Andrew corrected one of my own conclusions. Both TOs closed. No new TO opened.

| Commit | What |
|---|---|
| `4b7cc7b4c1` | **ANDREW-DIRECT record** — two rulings off `/open-calls`, broadcast same turn |
| `a5bee6eadf` | **Part 3 / W9 spec** — document text-extract + provenance registry |
| `ab70cdf126` | **Finished the half-landed `integrations/bloomberg` move** (MSTR~Z caught it) |
| `a389094bc8` | **W7 + W8 TOs flipped to complete**, 7/7 proof-of-spec re-validated as the pre-flip gate |
| `389d604c08` | Rulings 2a/3 absorbed — metering is BYTES; firm isolation promoted |
| `3fe2796ae4` | W8 §2 — inherited structural claims about Bloomberg are PRIORS UNDER TEST |
| `557273c4f3` | W7 addendum (declared bound) + W9 §1c |
| `95852d6f89` | **RETRACTION** — Andrew: the firm-isolation complication does not exist |

## Sovereign rulings received (5)

| # | Ruling | Effect |
|---|---|---|
| 1 | `/open-calls` **Call 1 = A** — Part 3 GO | **Spec-before-build rode INSIDE the option.** Spec only. |
| 2 | `/open-calls` **Call 2 = B** — credential accepted as-is | BG's rotation rec **discharged by decision**, scope-bound |
| 3 | Metering = **downloaded data SIZE** | **Neither model I branched on.** Sizing unit is bytes |
| 4 | Endpoint universe wanted | New scope; **his list is a reference, NOT an array** |
| 5 | **Firm isolation does not bind the SharePoint corpus** | Retraction of my own §1b/§1c |

## The dominant failure class, and a NEW property of it

Everything caught today was **a true statement about one frame asserted in another** — mentions read
as call-sites, file types as executing code, a top-level check as whole-artifact coverage, a
capability wish-list as a service taxonomy, documents *about* a firm as a firm's *own* documents.

⭐ **THE NEW PROPERTY, and it is why this one travelled furthest: A RULING INHERITS AUTHORITY AS IT
MOVES BETWEEN SEATS; A MEASUREMENT DOES NOT.** Every earlier instance was a *measurement* misread —
caught within one or two hops because the next seat re-measured. Ruling 3 was a *ruling* misread:
CTO~Z extended it from the tickets API (a serving surface with real firm logins) to the SharePoint
corpus, I received the extension **and hardened it further** into a first-class requirement plus a
declared blocking condition. **Each relay treated the prior seat's scope as settled rather than as a
claim.** It reached a spec before the sovereign caught it.

**The discriminator, handed to CTO~Z and MSTR~Z: DOES A FIRM USER AUTHENTICATE INTO THIS SURFACE?**
Ruling 3 is about VIEWERS, not provenance. Tickets/portal → binds. W7/W9 document store → does not.
W5 and "every serving surface" → **not adjudicated by me**; same test applies, CTO~Z owns them.

## Self-corrections landed this window

1. **The half-landed move.** `git mv` stages both sides of a rename; my safe-commit pathspec named
   only the DESTINATION, so 17 deletions were orphaned for ~5.5h. **A rename is two paths, and a
   pathspec naming only one commits half a rename — the half it commits is the half that LOOKS DONE.**
   Both trees tracked at HEAD, a pipeline entry point resolvable at a dead path. Verified closed with
   a positive control.
2. **Byte re-pricing.** I counted ROWS because rows were the unit I believed mattered. **The unit was
   wrong, so the instrument was pointed at the wrong quantity.** Traversal re-priced and marked
   ESTIMATED — I never recorded response bytes.
3. **The firm-isolation retraction.** Built a candidate table, a rejected alternative, and a declared
   blocking condition on a premise that did not exist. **A question can be rigorous, well-controlled,
   honestly bounded and still be the WRONG question** — and everything downstream of the bad premise
   was methodologically clean, which is exactly why nothing flagged it. Struck, not deleted.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `"blpapi"`, `"m365-gateway"`, `"IntegrationSpec"`, `--name "tools.py"` | PASS — located the gateway source + the `ms_cloud_extract.py` rung-2 collision |
| `comp-find` | `"pdfminer\|PyPDF\|..."` then re-run with **bare pipes** | **WARN → PASS.** First run used escaped pipes; the tool **warned they were literals** and returned 0 of 25,750. Re-run returned 108. **A zero from a bad pattern is indistinguishable from a real absence, and the tool caught it, not me.** |
| `.tools/proof-of-spec-check.py` | positional, rc per-call, no pipe | PASS — 7/7 groups; run as the **pre-flip gate**, which mattered: instances had been edited twice since first validation |
| `.tools/safe-commit.sh` | 8 commits, pathspec-scoped | PARTIAL — see self-correction 1; the wrapper did exactly what it was told |
| raw `git grep` / `aws` | `# rail-checked:` marked throughout | PASS |

**What worked:** the rail-checked marker discipline; `comp-find`'s own malformed-pattern warning.
**What failed:** three separate checks of mine (a piped `rc=$?` capturing `tail`'s code, a
backslash pattern collapsing in a heredoc, a case-sensitive grep over capitalised prose) — **in all
three the WORK was right and the CHECK was wrong.**
**Gap found:** **no comp-tool models the M365/SharePoint tenant.** Recorded as a SCOPE BOUNDARY
(comp-tools model the AWS/portal estate), not a coverage gap — routed as such, not as a defect.

## Blockers

**NONE.** Nothing is blocked on another agent or on evidence I cannot obtain.

## Current State (zero-context handoff)

- **W7 + W8: CLOSED.** Both TOs `complete`; `to-check --all --assignee 4.0.0_SA_CRO` returns 0.
  7/7 proof-of-spec instances VALID at
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/PROOF_OF_SPEC_W{7,8}_*.json`.
- **`integrations/bloomberg/`** — {mcp, pipeline, auth} + README. Move COMPLETE both limbs; 0 tracked
  files at old paths. **Scheduled Task `OPAL_BBGTML_daily_pull` → `integrations\bloomberg\pipeline\
  scheduled_daily_pull.cmd`, 07:00 naive boundary, next fire 2026-08-13 07:00 ET.** MCP `bloomberg`
  server repointed in per-device `~/.claude.json` (backup `.claude.json.bak-pre-bbg-integrations-move`).
- **`integrations/opal-gateway/`** — README (current state) + `docs/DOC_EXTRACT_REGISTRY_SPEC.md`
  (Part 3, spec only, §1b/§1c retracted-and-struck). Brief at
  `docs/briefs/OPAL_GATEWAY_PROJECT_BRIEF.md`. `integrations/**` → `ANY_EXEC_OR_AE` @`affde927d3`.
- **Secret `bloomberg/terminal/login`** — created, round-trip verified, no value printed or committed.
  Resolved by `integrations/bloomberg/auth/bbg_credentials.py` (exec wrapper; **no print mode**).
  Rotation rec **discharged by Andrew's ruling 2**, scope-bound.
- **Bloomberg transport UP** (`ok:true`). Traversal spend: **4 unique securities, 11 data points**
  of an approved ≤10/≤100 budget. `max_data_points` plumbed into `blp_client` + the MCP tool —
  ⚠ **MCP server restart required** for agents to see the new parameter.
- **My commits ride MSTR~Z's integration push** (seat commits, never seat pushes).

## Next Steps

1. **[Andrew]** Part 4 — Bloomberg data-shape spec + his network-capture idea for the Terminal's
   load-time popups. Not started, held at his sequencing.
2. **[1.0.0_SA_CTO~Z]** Ordering call on the **endpoint-universe** scope (ruling 4) — it sits in
   neither slot of their stated "W9 spec, then W4c-3" queue. Asked 203653Z, unanswered.
3. **[1.0.0_SA_CTO~Z]** W4c-3's three owed measurements, queued behind the above.
4. **[1.0.0_SA_CTO~Z]** Two findings routed, no action owed by me: the `assert_no_content_comms`
   cert is a **field-name substring check** and cannot stop a *named* leak (`doc_plaintext` passes);
   and Ruling 3's bindings on W5 / "every serving surface" need the firm-user-authenticates test run.
5. **[0.0.3_BG_BBGTerminal]** Nothing owed — rotation rec discharged, notified with scope bound.
