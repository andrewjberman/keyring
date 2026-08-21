# 1.0.0_SA_CTO~Z -- 0220-1325Z: the D7_NOTIFY set end to end, two law edits, and a night in which every real catch came from a seat reporting a near-miss

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE, DIAGNOSE
**serial:** 1.0.0_SA_CTO~Z (lane ~Z, base-folder log per site-Z convention) - PID 23648 - Monitor `b06vcw1kx`
**Continues:** `ctoZ_resumption_0126-0220Z_corrections_and_we1_gate.md` @`14523ffe9f` (same session, no respawn).
**Window:** 2026-08-21T02:20Z -> 13:25Z. **20 commits at this seat.**

---

## 1. THE WINDOW IN ONE PARAGRAPH

Andrew ruled the W-E audience **INTERNAL ONLY**, ratified the three-sided notification plan, and authorised the fabric to widen. **Six TOs were issued and all six landed, were accepted, and were independently validated** -- with `0.5.0_AE_OpalETL~Z` building and `2.0.0_SA_COO~Z` validating. **Nothing was applied, nothing wired, the W-F import edge is still unwritten, zero crons.** Two CLAUDE.md edits landed (Rule 21's case-sensitivity amendment; **Rule 26**, the apply-runs-on-the-owning-device law) plus one correction of my own overstatement. **SES production access was requested and GRANTED**, discharging the blocker I had surfaced ninety minutes earlier.

## 2. WHAT LANDED

| act | pin |
|---|---|
| SES production-access packet rewritten to his framing, **submitted, GRANTED** (200 -> 50,000/day) | `2b97a0165e`, `9c73a31b8d` |
| W-E sec-4 discharged (sandbox blocker gone) | `46d3ce65b5` |
| Audience **INTERNAL ONLY** + three-sided plan | `c1cb35d3aa` |
| `description` released on the immutable-intake-vs-evolving-state principle; three refusal cells ruled | `a3cd3a4732` |
| Re-cut item 3 (13 superseded audience assertions, 2 protected) + the case-sensitivity search finding | `48ac65311b` |
| **LAW:** Rule 21 amendment + the `/drive` clause struck | `5e4a71d604` |
| **LAW CORRECTION:** my own amendment overstated | `b26c8dbbfb` |
| Plan RATIFIED + **D7_NOTIFY TO-SET issued** (six TOs) | `8bcc0d16c5` |
| A-3b reachability control; its `expected_criteria` omission fixed | `9da84434ae`, `17cb81d389` |
| TO-C accepted; TO-D split PROSE/HTML | `a75eb92c83` |
| TO-B's measurements land: A4 -> list page, E-0 created | `24eeaebc1e`, `7843544d22` |
| Stale coordinate fixed (twice -- see sec. 5) | `3a551114f0`, `41b76933dc` |
| **LAW:** **Rule 26** -- the apply runs on the device that owns the work | `95b7eeb458` |
| D-HTML accepted BUILT-NOT-WIRED; **TO-F ACTIVE, wiring HELD as F-0** | `4ab6731e51` |

**THE SET, FINAL STATE:** A/B/C/D/E **accepted + validated**. **F accepted with F-2 recorded FAIL** (a permanent-wedge defect in the live buzz leg -- latent, never fired, not client-reachable). **F-3 UNCOMPUTABLE-BY-CONSTRUCTION because F-0 holds the wiring.**

## 3. RULINGS ISSUED AT THIS GATE

- **`description` RELEASED for the internal email** -- on **IMMUTABLE INTAKE CONTENT vs EVOLVING TICKET STATE**. The requester's body is authored once and cannot diverge, so it is not a second home; `events`/`status`/`claimed_by`/`assignee` stay prohibited **because they evolve**. The rule is *the email carries the intake snapshot in full and NO STATE.*
- **Three refusal cells** -- UNCONFIGURED and UNRESOLVABLE refuse loudly; UNKNOWN-FIRM-with-default resolves to the default. WE-5 re-points at the **resolver**, not the string.
- **E-2 degraded claimer: "An Opal advisor" + a discriminating log.** It discloses a **strict subset** of what he approved, it **generalises rather than invents**, and **(c) sends nothing -- the silence failure he himself named** when approving the submit-ack.
- **Criterion supersession:** a criterion is **a record of what was required then, not a standing rule.** Law outranks it **prospectively**; the acceptance stands; **do not edit it** -- every PASS means *"met criterion X"* and changing X makes the PASS unverifiable. **A project tag is filing metadata and IS correctable** -- but correct it **with the finding recorded**.
- **F-0: the wiring is HELD.** *"Proceed with D E F"* predates the clarified fact that the import edge is a production deploy on the runner plane. **A FIX IS A DEPLOY TOO** -- which is also why the F-2 remedy is routed, not applied.

## 4. FINDINGS THAT CHANGED A BUILD

- **TO-C:** `contentType: "text"` hardcoded at both Teams send sites (8 hits / 71 files) -- so *"clickable hyperlinks"* is **a gateway code change, not a formatting standard.** **A standard written first would have specified markup the renderer discards, and it would have passed review because it matches the documentation.**
- **TO-B:** no per-ticket deep-link route exists (discriminating control on a synthetic fixture) -> A4 resolved **by measurement**. And `/submit-request` is in **3 of 4 firms, NOT inflection** -> **E-0**: a firm-blind client link would send an inflection user to a page that bounces them.
- **F-2:** row contract validates `created_at` by SHAPE, the buzz needs it to PARSE, composer sits outside the per-row try -> **permanent wedge, cursor never advances, everything behind a leading-zero stamp never buzzed.** Severity checked *before* reporting: server-generated (`lambda_function.py:389`), and **0 exit-1 across 173 live passes with a working control.**
- **Buzz-leg reliability, unasked-for and the most decision-relevant:** **63/173 = 36.4% identity-fail, longest window ~130 min overnight.** Nothing lost. *"The next 5-minute fire retries"* is **true and installs the wrong expectation.** **It is Andrew's email-first architecture measured.**

## 5. WHAT I GOT WRONG, AND THE SHAPE OF IT

**Seven self-caught or peer-caught errors at this seat this window.** Recorded because the pattern is one pattern:

| error | mechanism |
|---|---|
| Rule 21 amendment **overstated** -- claimed a blindness I had not measured | verified the miss, **not the guard**; my check reused the same `head -4` truncation that produced it |
| `expected_criteria` omission on A-3b | added a criterion, did not add it to the declared set |
| stale coordinate fixed **1 of 2**, shipped as complete | **my script printed `2` in the same call as the commit** |
| `OPAL_TICKETING` counted as **1**, true **3** | glob covered 7 of 11 files |
| endorsed **Option A** | verified the measurement, **not the cause** |
| `safe-ec2-deploy.sh` reported ABSENT | checked `.tools/`; it lives in `infra/aws/ec2/` |
| `exit 2: 124` published to Andrew | double-counted; **every failed pass writes two lines carrying "exit 2"** |

> **ONE CLASS, SEVEN FACES: A TRUE ANSWER TO A NARROWER QUESTION THAN THE ONE REPORTED ON.** Wrong case, wrong scope, wrong path, wrong shape, wrong domain, truncated output, and a count read against no coverage.
> **AND THE DEFENCE WAS NEVER CARE.** Every one was caught by a control, a peer, or an accident -- **three of the night's catches were explicitly accidental** (a guard hit in normal use, a recollection disagreeing with an instrument, a header read for an unrelated reason). **The reporting culture converted the accidents into findings; nothing converted care into one.**
> ⚠ **AND ONE MORE, FOUND WRITING THIS LOG: I adopted the clock-read remedy at ~09:18Z and then resumed INFERRING stamps** -- messages stamped 09:22 / 09:44 / 10:14 were written against a true clock that is now 13:25Z. **Knowing the failure and adopting its remedy did not survive four hours of turns.**

## 6. Compiler Tools

| tool | use | result |
|---|---|---|
| `proof-of-spec-check.py` | 8 gate re-runs (A/B/C/D/E/F + WA re-checks), positional, `PYTHONIOENCODING=utf-8`, rc unpiped | **PASS** every time; **a bare-form VALID is never accepted as coverage** |
| `comp-find` / `comp-find -i` | ~15 censuses | **PASS, and the source of a law edit** -- case-sensitive by default; `-i` closed a 7-vs-13 miss |
| `aws sesv2 get-account` / `get-email-identity` | SES posture + the grant | **PASS** -- negative-controlled; the **quota move**, not the status string, was the evidence |
| `Get-ScheduledTask` | the two-plane confirmation | **PASS** -- `Execute` is the repo path; 4 of 208 tasks run from the tree |
| `git cat-file` / `%ct` | deployed-commit attribution; the true-UTC ordering | **PASS** -- 9/9 events chronological as narrated |
| `safe-commit.sh` | 20 commits | **PASS**; risk-reflex CLEAN or advisory each time |
| `schtasks` (grep form) | first scheduled-task read | **FAIL** -- returned empty; PowerShell gave the truth |
| `comp-find --name "*ITEM_A*"` | locate a record | **FAIL** -- matched `conversation_item_added` in vendored types |

**What worked:** the **band** (`[TEST]` vs `[HEAD]`) separated a fixture from a finding in one call, repeatedly; **negative controls** on every absence verdict.
**What failed:** three raw searches that returned clean confident zeros (sec. 5).
**Gap:** `.tf` has **no non-ASCII lint** -- the check scopes to `.sh`/`.py`, and a file class that provisions AWS is uncovered. Recorded, unrouted.

## 7. MCP traffic

**~55 messages handled, ~30 sent.** Significant: the audience ruling relay - the SES GRANTED broadcast - two same-turn **law broadcasts** (Rule 21, Rule 26) + one correction of the first - the TO-SET GO - five acceptances - the Option-A withdrawal - the Rule-26 *"read the working tree, not the ref"* correction. **All ACKed via `ack_messages`** (the READ clock, not the emitted one).

## 8. Blockers

**None held at this seat.** Three items sit with **[ANDREW]**, all evidence-cited, none assumption-blocked:
1. **W-A/W-E apply** -- ours under Rule 26; **must be requested as carrying its queue**, not a single change.
2. **D-HTML apply** -- `systemctl restart`, **not** an instance bounce (corrected at source); real cost is `GATEWAY_WORKERS=1` dropping in-flight calls **and every run re-deriving `.env` from four secrets**.
3. **F-2 remedy** -- one line, routes into an existing handled outcome; **latent, never fired, not client-reachable.**

## 9. Current State (zero-context reader)

**D7_NOTIFY: six TOs, all landed.** Instances at `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/D7_NOTIFY.TO-{A..F}_PROOF_OF_SPEC.json`, all VALID rc=0. TO-SET at `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/D7_NOTIFY.TO-SET.md`.
**Built, not applied:** the internal DL email (SES from the CREATE Lambda, pinned `opalinvest.dev` sender, firm-keyed `resolve_recipients`), the client submit-ack + pickup, the Teams prose formatter, D-HTML's markup.
**NOT wired:** `integrations/ticketing/intake/sweep.py` has **no importer outside its own tests** -- the escalation fuse is an absent import edge, and writing it is a live deploy within 5 minutes.
**Law:** CLAUDE.md carries Rule 21 (amended + corrected) and **Rule 26**. `org/XXX.md`'s COO `/drive` clause is **struck**, verbatim preserved.
**Fabric:** 4 seats (MSTR~Z, CTO~Z, AE_OpalETL~Z, COO~Z) + BG. Zero crons anywhere. HEAD carries unpushed commits at this seat; **push is the integrator's.**

## 10. Next Steps

- **[ANDREW]** the three items in sec. 8. Nothing moves without his word.
- **[0.5.0_AE_OpalETL~Z]** standing by; F-2 remedy held, apply request committed at `deliverables/laneZ_APPLY_REQUEST_*.md`.
- **[2.0.0_SA_COO~Z]** register execution with `0.0.0_AB_MSTR~Z` (**resolver fix, not Option A**); the `OPAL_TICKETING` typo is a **separate finding in 3 files, 2 of them closed TOs.**
- **[0.0.0_AB_MSTR~Z]** push; `GW-APPLY` returns to this fabric under Rule 26.
- **[1.0.0_SA_CTO~Z]** event-driven. **Nothing self-initiated.**
