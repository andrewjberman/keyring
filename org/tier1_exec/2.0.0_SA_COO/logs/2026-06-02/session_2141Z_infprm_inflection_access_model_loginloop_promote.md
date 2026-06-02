# Session Log — 2.0.0_SA_COO — 2026-06-02 ~21:41Z

**Role:** ws COO (Tier-1), primary operational driver. `/drive` 20m cron armed (LD-0082 deterministic loop), `/watcher` healthy, `/allocation` chained per cycle.

**Session focus:** Drove **ADVI_INFPRM** (Inflection external-partner access model) end-to-end from Andrew's localhost smokes — admin/non-admin access model, a login-loop root-cause, the Distribution-untier ruling, and the PROD promote dispatch. Plus: Cognito-memory scrub (Andrew directive), MSTR NO-DELTA tuning, and a 4-project queue-hygiene reclassification.

---

## Through-line (the lesson of the session)

**Andrew's localhost pixel-smoke is ground truth and it repeatedly caught what layer-local RAVC2s + CVO certs could not** — each catch was a *scope/precondition/data-shape* error sitting in a SEAM between correctly-certified layers:
1. W4b shipped CVO-PASS "non-admin Profile-only" — but that was a **scope error** (Andrew's actual model = `[Distribution, Profile]`). Caught at pixel.
2. Joe's Profile "not mapped right" — comp-tools proved the **component** was correct; the gap was a **precondition** (claims.advisorId).
3. Joe **login loop** — the real root was an **infra table-split misunderstanding** (claims come from `opal-partner-{firmId}`, NOT `opal-users-v2`), not anything in the FE or the access model.
4. The Distribution untier — naive edge-relax would **leak PII** because `book.json` co-mingles aggregate + cleartext client roster; needs a **data-layer split**.

Tooling discipline that worked: **comp-transform schema-check / comp-trace / comp-routes** narrowed "Profile isn't mapped right" to invocation-not-component in minutes (Andrew's nudge). **Verify-not-assume** caught the phantom portal sha (`a9434226e` = a main-repo log commit, would've failed DT's checkout) and the wrong provisioning table.

---

## ADVI_INFPRM arc (the dominant work)

**Access model (Andrew-direct):** admins (Peter) = `[Distribution, Books]` (advisor list -> any advisor + Firm Overview + BI); non-admins (Joe) = `[Distribution, Profile]` — **Distribution identical to admin** (no PII, no tiering), Books REPLACED by Profile (AdvisorPublicProfile self-scoped, Profile|Book toggle).

| Leg | What | Commit | Verify |
|---|---|---|---|
| W1/W2-FE | firmId-resolution for external users (firmOverride=undefined -> JWT/explicit firm); the 9 fetch-wrapper throws | 8ff69f18, 794dc54e (revert redundant rewire), e6df1678 | CVO-PASS |
| W4a | provision Peter admin + edge admin-exemption | b3ae5720e | CVO-PASS (no cross-firm leak; firm boundary is a separate non-spoofable JWT-firmId gate) |
| W4b | 49F admin/non-admin tab-gating mirror | 4b8375ab | CVO-PASS — but MODEL was wrong (Profile-only) |
| W4c | Segment relationship-drill firmId-resolution (enabled !!firmOverride->!!firmId; was never firing) | 2790e87e | CVO-PASS |
| W4f | CORRECT non-admin -> [Distribution, Profile]; revert P2-a distribution guard; Profile=literal AdvisorPublicProfile | c009f98c | CVO-PASS |
| W4g | (Profile-tab) SUBSUMED by W4f — comp-tools confirmed component correct; gap was claims.advisorId | — | — |
| W5 | Distribution untier — data-layer split (DS strip display_name -> AE edge L0 -> RD repoint) | 3bce72da1 (ruling) | fast-follow, in motion |
| advisors-guard | re-add isFirmAdmin guard (moot branch, defense-in-depth) = portal DEV HEAD | 23982a8c | CVO strictly-additive |

**Joe LOGIN-LOOP root (KEY infra correction, AE 486556175):** JWT identity claims (advisorId/firmRole/advisorName/advisorRole) come from **`opal-partner-{firmId}` (= opal-partner-inflection)**, NOT `opal-users-v2` (which is **auth/password only**). Joe existed only in opal-users-v2 -> partnerIdentity=null -> JWT had no advisorId -> non-admin edge gate (auth-validator-edge:312) forbade his session -> portal (api-client.ts:74/85) read the 403 as unauth -> sign-in redirect -> loop. Fix = create Joe's opal-partner-inflection entry (advisorKey=joe_brandenburg, advisorRole=architect=Group3->toggle visible, firmRole=user). Decoded a fresh Joe JWT to PROVE it (advisorId+firmId present -> :312 passes -> no loop). Peter was always admin in the partner table (stale-JWT only; the W4a opal-users-v2 edit was inert).

**Andrew rulings (sovereign):**
- PII-parity: KEEP pseudonymized (intentional).
- Access: admins full Books; non-admins Profile-only-tab BUT keep Distribution (corrected from W4b).
- **No user-type tiering on Distribution** ("no PII there; misguided + not desired") -> SUPERSEDES CTO ruling-(a) (cross-advisor 403 by-design). Cross-advisor drill must work for non-admins -> the W5 untier.
- Ship-path A: "yep this works ... get the tree cleaned up, dev pushed, prod deployed."

**Distribution-untier seam (CTO W5 + AE trace):** `book.json` co-mingles the Distribution aggregate (`relationship_stacked_periods`) WITH a client roster carrying **cleartext display_name** (49F real names). Edge tier_policy is one-policy-all-firms, so a path-relax would leak 49F's roster. Resolution = **DATA-LAYER SPLIT**: DS emits `relationship_periods.json` (stacks={client_key, aua}+totals, display_name STRIPPED; FE pseudonymizes from client_key) at L0/non-.004a; `book.json` stays L1+.004a (admin/Books). Chain: DS emit -> AE comp-pii proof + edge L0-allowlist diff -> CTO pre-apply approval -> RD FE repoint -> CVO re-verify.

**PROMOTE (Andrew-direct, ship-path A):** MSTR spawned 0.4.0_DT; COO dispatched the single 5-phase canonical portal DEV->PROD promote. HEAD=**23982a8c** (CTO-verified full sha; contains c009f98c + advisors-guard), ROLLBACK=a33c230f, 15-ahead, ci-green. Bundle = INFPRM all-legs + INFOTD (AUM/Count) + INFNNA-W2FE + S5 + NNA-tooltip, all CVO-cleared, backend/data already live. Cross-advisor untier = accepted fast-follow gap (graceful placeholder today).

---

## Other items

- **Cognito memory scrub (Andrew directive):** "we do not use Cognito... we use Dynamodb. wipe any mention." Deleted 2 Cognito-saturated memory files; consolidated into one positively-framed `project_opal_auth_custom_jwt_dynamodb.md` (then corrected it for the table-split); scrubbed MEMORY.md + the "incognito" false-positive. memory/ now zero "cognito" substrings. (3rd Andrew correction on this — root was contrast-framed memories keeping the wrong term alive in context.)
- **MSTR NO-DELTA directive:** stop MCP'ing `[ALLOCATION-NO-DELTA]` to MSTR each cycle — write to the brief, MCP only on DELTA. Banked `feedback_allocation_no_delta_brief_only_not_mstr_mcp.md`; complied.
- **Queue-hygiene (MSTR-delegated):** 4 stale-active projects -> inactive (CVO wrote 516f7f4f4): ADVI_SHARED, ADVI_VALFIN, SXPL_RESTIN, TRSB_LEDGER (each with a reactivation note). Hot-list 12->8.
- **BDPL_CNPRCS.WP-11:** DS verified the scoped-override correction already realized continuously; no re-run (db9befb5d).
- **INFNNA Phase 2:** W4 RIGID gate MET (CVO 1852Z); ships in the DT promote (INFNNA-W2FE).

## Memories banked / corrected this session
- `project_opal_auth_custom_jwt_dynamodb.md` — auth = custom RS256 JWT; **TWO tables** (opal-users-v2 auth / opal-partner-{firmId} claims); NO managed IdP. (Corrected mid-session after the Joe-loop table finding.)
- `feedback_allocation_no_delta_brief_only_not_mstr_mcp.md` — NO-DELTA to brief, not MSTR.

---

## State at close + carry-forward

- **PROMOTE in flight** — DT executing the 5-phase DEV->PROD on 23982a8c. **NEXT:** confirm PROD live (portal-v* tag + CloudFront invalidation) + CVO e2e on SERVED PROD (Peter [Distribution,Books] / Joe [Distribution,Profile] / AUM+Count+NNA). Relay to Andrew.
- **W5 untier fast-follow** — DS dispatched the relationship_periods.json strip-emit (long pole). Chain: DS emit -> AE edge diff (CTO pre-apply) -> RD repoint -> CVO. **CARRY-FORWARD:** RD~C was wound down post-FE (MSTR); the W5 FE-repoint will need an **RD respawn** (MCP MSTR [ALLOCATION-REQUEST]) sequenced when DS-emit nears done.
- **Andrew PROD smoke** pending once live (Peter + Joe on PROD; the cross-advisor drill shows placeholder until the untier lands).
- **MDPF_SCOPED** OPS1 AC4#2 = Wed 6/3 scheduled gate (future, attest).
- Live set at close: DT (promote), DS (W5 emit), AE (edge, gated on DS), CTO (edge approval + DT hand), CVO (post-promote e2e). RD~C wound down. RD~B/DT-was-offline.
