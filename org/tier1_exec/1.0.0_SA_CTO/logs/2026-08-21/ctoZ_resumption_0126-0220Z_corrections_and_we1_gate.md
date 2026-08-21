# 1.0.0_SA_CTO~Z -- resumption 01:26-02:20Z: correcting what my predecessor told Andrew, then clearing my own gate

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE, SCRIBE
**serial:** 1.0.0_SA_CTO~Z (lane ~Z, base-folder log per site-Z convention) - PID 23648 - Monitor `b06vcw1kx` (child pid 2694903)
**Continues:** `ctoZ_session_close_0010-0035Z_atom_decomp_search_failure.md` -- a session Andrew ended by shutting the fabric off.

---

## 1. THE WINDOW IN ONE PARAGRAPH

Fresh seat, launched ~50 minutes after Andrew shut the fabric off over an answer this serial gave him. Startup ran clean. **The predecessor's answer was wrong on both halves and its first correction had made it worse** -- so the window's real work was fixing the record he holds, not the board. Two corrections committed and pushed, one design gate ruled, one new blocking precondition surfaced that nobody in the chain had seen. **The D-family board is now gate-clear at this seat: nothing on it waits on me.**

## 2. STARTUP (per `org/XXX.md`)

`/watcher` -- NOT REGISTERED -> registered; Monitor armed and confirmed by `TaskOutput -> running` plus a `ps` parent-resolves-to-live-wrapper check. **Zero `inbox-watch` processes existed fabric-wide before arming**, so the orphan/peer/context-clear discriminator never came into play. Zero crons (`CronList` empty), per the Step 1b-F CTO row.

A.1 serial file - A.3 **PATH 98 of 101 comp-tools resolve bare, and the EXERCISE half passed** (a forwarder produced its own banner -- resolution is not execution) - B both probes - **B.1 `to-check --all`: 0 TOs at `~Z`, 6 at base** - D hook wired - E context set - Steps 2-4 read.

**A.2 audit-archive: 18 findings**, eight NON-APPEND-EDIT with first divergence at line 1 and live-head an order of magnitude under baseline. **Consistent with RV-0057 F-001** (the archive keys on `(timestamp, logical-log)`, which stopped being unique when the fabric acquired a second device) -- **stated as consistent-with, not proven**; that TO is open and its site-Z half unseated. Surfaced, not chased.

## 3. THE CORRECTIONS -- what he was told, and what is true

| Told to Andrew | Measured |
|---|---|
| `comp-adversary` had **0 runs** | **>= 5 runs, 2 seats, 2026-08-20 ~12:31-12:35Z** -- ~12h before he asked |
| the `atom_decomp` decomposition workflow is **absent** | **`workflows/atom_decomposition/` -- 368 files, 360 GIT-TRACKED, 20 completed run subjects**, engines edited 16:03Z that day |

**Both are absence verdicts drawn from a source structurally incapable of showing presence.** The rail log has no `comp-adversary` write path (its `tool=` census is `comp-which`/`comp-find`/`comp-grep`/`comp-glob`, those four); the binary search asks after an executable that never existed, because the program ships as a **skill plus a `workflows/` python package**.

Grounded on planes that do not share a failure mode: `comp-find` with printed denominators (13 hits / 27,212 files, BANDS SURFACED=2 CONFIG=1 DOC=10), the tools' own `read-vintage` stamps, `git ls-files`, `git` first-add times.

> ### THE PART WORTH KEEPING: THE FIRST CORRECTION MADE IT WORSE
> At ~00:27Z the predecessor fixed the **denominator** (1,157-lifetime mislabelled "today" -> 216) and left the **conclusion** standing. Then corrected the frame a **third** time (23 days -> 2 days since ratification) and called that *"the number that is true."* Three progressively more careful frames around a number that carried no information at any of them.
> **A DENOMINATOR MAKES A COUNT HONEST; IT CANNOT MAKE A BLIND INSTRUMENT SIGHTED.**
> And the withdrawal itself kept a residue -- *"no seat claimed to have run it before he asked"* -- **assembled from the same blind rail it was retracting.** A retraction that keeps the original's evidence base launders it rather than retracting it. **It survived because it was the conservative-looking form**: weaker, hedged, labelled "testimony, not measurement," and therefore read as already discounted.

**Landed:** session log @`ad03c47479` - Andrew-facing deliverable @`d79d073c94` (six anchors, **four** falsified claims, 93/7, corrected **in place with the false text struck**, not deleted). Both pushed by `0.0.0_AB_MSTR~Z` at 0148Z and verified from the remote.

**Stopped it propagating:** `0.0.0_AB_MSTR~Z` was carrying *"the decomposition workflow is absent"* to Andrew's terminal. Flagged same-turn; that seat re-derived it with a **negative control** (`workflows/zzz_no_such_workflow_9999` -> ABSENT) and dropped it. **A converging second wrong answer from a second seat is worse than the first, because agreement reads as corroboration when it is only propagation.**

**The card survives and improved:** whether this fabric should run `atom_decomp` at all is still open -- and is now askable against a record instead of a void. **20 runs exist under `runs/INDEX.json`. What did they change?**

## 4. WE-1 DESIGN GATE -- RULED @`c3e7fc73ac`

`D7_TICKETING.WE-SITEZ` carried *"DESIGN GATE FIRST at 1.0.0_SA_CTO~Z"* -- the one item on the board waiting on this seat.

**Split by the TO's own cut test** (byte-identical under either audience answer -> not blocked): **transport + sender RULED**; *"the DL exists and its creating actor is named"* NOT discharged (tenant-admin act, and its recipient composition **is** the audience question). **The audience stays Andrew's** -- unblocking W-F is not a reason to take that decision back from him.

- **TRANSPORT: SES from the CREATE Lambda write path.** Gateway disqualified **structurally** -- the Bearer is validated before any tool name is dispatched (`server.py:15`, `:92-98`), so every gateway-mediated send inherits the ~1h agent-session dependency and no per-tool exception is possible. The disqualification rests on **entanglement, not impossibility**: a `refresh_token` grant is materially available, but using it means a second refresher racing Claude Code on rotating tokens. **A BACKSTOP MUST NOT BE ENTANGLED WITH THE CREDENTIAL OF THE SYSTEM IT COVERS.**
- **SENDER: `opalinvest.dev`** -- `Verified true / DkimStatus SUCCESS / SigningEnabled true / DOMAIN`, with a **negative control** returning `NotFoundException`.
- **Build-ladder rung 2:** the estate already runs this. `infra/aws/lambda/trade-pipeline/` carries the whole shape and **NEVER#23 is already commit-gate-enforced**. Port it; do **not** clone `ses.tf`'s bounce/complaint SNS topics (moratorium), and **invert** the recipient config (WE-5 is refuse-if-unset; `EMAIL_FROM` has a baked default).

> ### ⛔ THE NEW BLOCKING FINDING -- SES IS IN THE SANDBOX
> `aws sesv2 get-account` -> **`ProductionAccessEnabled: false`**. A sandbox account may send only to **verified** identities, and the 24 individually-verified `EMAIL_ADDRESS` identities in this account are the tell that the estate has been hand-verifying recipients one at a time. **An Exchange DL lives on `@opalinvest.com`, which is not a verified DOMAIN identity here -- so SES -> that DL is rejected today.**
> **THIS IS A DIFFERENT AXIS FROM THE ONE THE TO WAS WATCHING. Criterion (3) is DKIM, and DKIM is fine. DKIM GOVERNS THE SENDER; THE SANDBOX GOVERNS THE RECIPIENT.** A gate checking only criterion (3) would have passed the build into a send that cannot be delivered -- and by the TO's own standard (*"a first line that lands in quarantine is worse than no first line, because it reads as sent"*) a sandbox rejection is worse: deterministic, on every ticket.
> Three paths named with actors, **none chosen by me**: (A) DL on `opalinvest.dev` -- clean today, but audience-coupled; (B) individually verify the DL address; (C) **request production access -- explicitly Andrew's** per `ses.tf`'s own header, prerequisites already built.

**WA's CTO gate checked too, and it was already discharged** -- the reopen/timing grain collision (P1-2) was ruled at `ctoZ_D7_PRECUT_RULINGS_...:31` (`reopened_at[]` served-but-derived, `reopened_count` stored) and the ruling **propagated into the Rule-24 schema record before it was written**, exactly as the TO required. Verified rather than assumed.

## 5. INSTRUMENT FINDINGS THIS WINDOW (the night's running catalogue, continued)

1. **A `--query` naming a field the API does not return prints `None`, not an error.** `list-email-identities --query VerifiedForSendingStatus` returned `None` for all 25 identities including `opalinvest.dev` -- reads as a fabric-wide "nothing is verified" alarm. The field exists only on `get-email-identity`. Caught by dumping one raw record.
2. **A split-line phrase defeats any single-line grep while its positive control passes** (`0.0.0_AB_MSTR~Z`): `grep -c "what DIFFERS"` -> 0, control `"MERGE WINDOW"` -> 2, phrase real at `:220-221`. Reproduced exactly at this seat.
3. **A COUNT CANNOT SEE A MARKER THAT CHANGES A TOKEN'S MEANING WITHOUT CHANGING THE TOKEN** -- strikethrough, a NOT, a quotation, a superseded banner. **With the boundary that makes it usable:** a **PRESENCE** read is safe (strikethrough preserves the token); an **ABSENCE-OF-ERROR** read is poisoned and runs the wrong way -- *"is the false claim gone"* returns 1 from both a corrected and an uncorrected document, so **the honest correction scores worse than leaving the falsehood in.**
4. **Skill BODIES load on invocation, not at session start** (`0.0.0_AB_MSTR~Z`, measured; this seat was the specimen). An escalation premised on "every seat you spawn loads the false text" was retracted -- **the exposure was at the wrong time and the wrong size.** A premise nobody measured travels faster than a measurement because there is nothing to slow it down.

**Deploy-gate protocol correction absorbed and source-confirmed at this seat** (`.tools/safe_deploy_core.py` @`ad03c47479`): the `s3 cp` at `:549` is **unconditional**, the ETag check at `:565` is a **post-write verify**, the only narrowing is `.py`-only at `:350`/`:390`, and `s3_key_exists` at `:404` is an **existence** guard by its own docstring. So **"MATCH" means uploaded-and-verified, never skipped-because-identical**, and **no deploy leg may be called inert from byte-parity.** Declined to author a competing fix -- the corrected text already exists on `origin/CLOUD` (`89cf3cf43d`, `6dedb44870`), not yet ancestors of `SITEZ`.

## 6. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-find` | **PASS, repeatedly decisive** | `EMAIL_FROM` 77/27,212 with **DEF=7** went straight to the rung-2 reuse in one call; `validation_context_declaration` 13/27,212 separated generator from real declarations |
| `comp-find --name "*ITEM_A*"` | **FAIL -- caught** | matched `conversation_item_added` etc. in vendored `openai/` types; a case-insensitive substring glob is not an identifier search |
| `aws sesv2 get-account` | **PASS -- the finding** | rail-checked; no comp-tool models SES account posture (`comp-iam` is TF-DESIRED and `(action)`-only) |
| `aws sesv2 get-email-identity` + negative control | **PASS** | `NotFoundException` on a bogus domain proves the read discriminates |
| `aws sesv2 list-email-identities --query` | **FAIL -- caught** | see sec. 5.1 |
| `to-check.py --all` | PASS | `--all` load-bearing; 0 at `~Z` vs 6 at base is the lane/base split, not idleness |
| `safe-commit.sh` | PASS x3 | risk-reflex CLEAN each time, 1 file vs 1,662 danger nodes |

**Gap unchanged:** `comp-kuzu`/`comp-blast` hang on this box -- named at every use, never a false clean.

## 7. MCP traffic

7 messages sent, 5 received, **all ACKed via `ack_messages`** (4158, 4160, 4163, 4165) -- the READ clock, not the emitted one. WE-1 routed to 3 seats with a per-recipient map: **1 DELIVERED / 2 QUEUED / 0 REFUSED (denominator 3)** -- both queues are seats that are not live, which is a fabric-state fact, not a delivery failure.

## 8. Blockers

- **Reconcile merge** -- `0.0.0_AB_MSTR~Z`, waiting on a laptop quiet frame + Andrew's word. Both pending-apply targets sit behind it.
- **[ANDREW] W-E DL audience** -- internal / mixed / client-facing. Gates only W-F's transport binding, recipient resolution and medium formatting.
- **[ANDREW] SES production access** (new tonight) -- or a tenant-admin path (A)/(B).
- **DL creation** -- tenant admin.
- **No live `~Z` build seats.** MSTR spawns; I do not.

## 9. Current State

Fabric: **2 seats** (`0.0.0_AB_MSTR~Z`, this one). Site-Z D-family: **D6 CLOSED - D8 CLOSED - D7 core COMPLETE-ACCEPTED with an event-gated tail - D9 off-device.** **Nothing on the board is gated at this seat.** Zero crons. HEAD 1 ahead of `origin/SITEZ` (`c3e7fc73ac`, the WE-1 ruling) awaiting the integrator.

## 10. Next Steps

- **[ANDREW]** two cards, both routed via `0.0.0_AB_MSTR~Z`: the **W-E DL audience**, and **SES production access** (path C, his Console act). Neither is urgent -- W-E is P2, off the critical path, and no build seat is live.
- **[2.0.0_SA_COO~Z]** WE-SITEZ status line is stale (*"DESIGN GATE FIRST at 1.0.0_SA_CTO~Z"*); half-discharged is the accurate state. Record maintenance on your own TO, not a gate.
- **[0.5.0_AE_OpalETL~Z]** WE transport/sender build may start; WE-2/WE-3 cannot be **exercised** until the sandbox resolves.
- **[1.0.0_SA_CTO~Z]** event-driven on the Monitor. Nothing self-initiated.
