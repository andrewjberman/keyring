# 1.0.0_SA_CTO~Z -- D12 from acceptance to a fully-verified production ship: promote, pilot, Act B/C, and the rotation defect that six seats got wrong before one mail-free experiment closed it (0147-0935Z)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE, COORDINATE

**Seat:** `1.0.0_SA_CTO~Z` (lane ~Z; base folder, lane named in title)
**Window:** 2026-09-01 0147Z -> 0935Z. Prior log `465963fed8` covered 2355-0147Z.
**Device:** site Z. 6 seats live through the window (MSTR~Z, CTO~Z, COO~Z, AE_CloudOps~Z, DE_ClientPlatform~Z, CVO~Z); AE went dark ~07:4xZ and COO respawned it.

---

## Summary

D12 went from accepted-backend to a fully-verified production ship. Andrew invoked `/prod-deploy` and
said "all of this needs to be pushed"; the portal promoted to PROD (v2.1.174), the MFA pilot enrolled
on his own reaffirmed override, he completed a real MFA login, and every D12 property was then verified
on the client production actually serves. The rotation "defect" his login surfaced consumed six
premature conclusions across three seats (four mine) before a mail-free store-recovery experiment
closed it as no-defect. Two follow-on deploys shipped from Andrew's own design instincts (Act B opt-in,
Act C idempotency). My acceptance queue is empty at close.

---

## Andrew-direct in-window (recorded verbatim, broadcast same-turn per law)

| ~Time | VERBATIM (first clause) | Effect |
|---|---|---|
| ~06:1xZ | "I think all of this needs to be pushed" + `/prod-deploy` | promote authorized |
| ~06:5xZ | "All of its good , go" (on the explicit 7-commit passenger list) | scope confirmed incl. laptop perfrp |
| ~07:1xZ | "Try just me and aj@opalinvest.com" | named-human pilot cohort |
| ~07:2xZ | "My email is andrew@opalinvest.com" | gate (id) closed on his own word |
| ~07:3xZ | "Yeah i asked explicitly for andrew@ and aj@" (after the pre-Act-B objection) | sovereign OVERRIDE of the Act B gate |
| ~07:4xZ | "why can't we just adjust the lambda ... to be called at the appropriate button" | independently described Act B |
| ~08:5xZ | "should be idempotent anyway" | the real fix; ruled W3 ACT C |

---

## Delivered

| Artifact | Commit / ref |
|---|---|
| portal DEV->PROD promote v2.1.174 | PROD `529f3093`, tag `portal-v2.1.174`, CI run 33479722920 SUCCESS |
| workspace portal pointer bump | `a8305b3339` (SITEZ, LOCAL) |
| deploy ledger CLOSED-COMPLETE | `e9ef2a9e46` |
| Act B (send removed from login), protective commit under AE authorship | `6379a937e7` |
| Act B deployed | CodeSha256 `nsltFOQw...` @08:19Z |
| Act C (idempotency) deployed | CodeSha256 `oExO72Sr...` @08:56Z |

**Promote executed via /prod-deploy under the Step-0 Andrew-direct exemption (non-DT). All three push
legs by the site-Z integrator `0.0.0_AB_MSTR~Z` (LD-0367): DEV be39451b->89ecfd89, PROD fc3a4421->
529f3093, CLOUD pointer inside the integrator's held CLOUD integration.**

---

## The promote -- three in-flight holds, zero half-landed states

1. **LD-0367 canary:** the DEV push (Step 1a) is integrator-only; it blocked at my seat BEFORE any
   worktree/merge -> clean stop, routed to the integrator. No half-landed state existed at any point.
2. **Passenger hold (mine):** the merge carried 5 non-D12 `~D`-lane perfrp commits as passengers
   (a promote ships all of DEV). I HELD the PROD push and surfaced the full 7-commit list to Andrew
   before the irreversible step; his "All of its good , go" discharged it. His earlier bus verbatim
   ("laptop fabric has performance reporting edges to push, i want all of it pushed") independently
   corroborated the scope.
3. **Integrator 9-vs-7 count hold:** MSTR held its own PROD push until 9 raw commits reconciled to
   my 7 + 2 merge-topology commits. No hidden passengers.

Parity gate EMPTY (PROD tree == DEV tree). Two-plane post-promote verification: DE bundle-plane PASS
(entry chunk flipped to index-CQCRJQRU.js, every MFA token inverted from pre-promote 0), COO API-plane
PASS (promote API-invisible, backend untouched).

---

## Pilot -- enrolled on a sovereign override, then Andrew logged in

Gate was (a) Act B deployed AND (b) named cohort. Andrew named the cohort, was given the measured
pre-Act-B consequence IN FULL (a code mailed before opt-in + a screen falsely saying none was sent --
his own original complaint reproduced), and REAFFIRMED. Per CLAUDE.md a reaffirmed concern is the
sovereign's decision: gate (a) discharged by his word, not overridden by my judgement. COO wrote
`mfaEnabled=true` on exactly `usr_7f83e30de95f` (andrew@) + `usr_a5ae550bd45a` (aj@), read-back
confirmed, census HUMAN 0->2 / SERVICE 0 / FIXTURE 0. "me" resolved on his own prior verbatim (the
session-held address was andrew.opalinvest2@gmail.com -- an inferred guess would have gated the wrong
identity; confirm-not-infer was load-bearing). Andrew then completed a real MFA login on prod.

---

## The rotation defect -- six premature conclusions, one experiment

Andrew's login surfaced "two codes, the older one verified." The row burned SIX confident wrong
answers across three seats before it closed:
- display-order (CVO) -- falsified by MSTR's mail-server seconds-precision timestamps
- two-logins (MSTR) -- falsified by COO's CloudWatch (1 issued, 1 rotated)
- receipt-order (CVO) -- falsified by CVO's OWN arithmetic (6.1s send gap arrived as 1.0s receipt gap
  -> >=5s differential transit -> receipt order carries zero information)
- **mine, FOUR: (1) DE1-1 wrong oracle (`mfa_challenge_issued` fires at login, not send); (2) DE1-1
  missing validity condition (the oracle is blind under deployed Act-A bytes); (3) retraction on dead
  grounds (I retracted a true claim citing CVO's display-order after MSTR had measured it false);
  (4) F-8 amplification (I filed a security defect + reopened W3-3 off COO's MAPPING-A verdict without
  checking the mapping premise or that the code I could read was correct).**

Every failure shared ONE buried dependency: mail ordering. Resolved by MSTR's mail-free experiment
(recover both codes from `(salt, codeHash)` at the store, verify the superseded one): superseded code
-> **401 (log: reason=wrong_code, attempts=1 -> the hash comparison ran and rejected)**, control -> 200,
step-4 A!=B. **F-8 CLOSED -- rotation binds, no defect.** The recurring lesson, banked-worthy: I keep
concluding from the readable plane (source) when the claim lives on the deployed plane; source!=deployed
fired 4x on this handler.

---

## Act B / Act C (Andrew's own designs, shipped)

- **Act B** (issue-not-send): I committed it PROTECTIVELY under AE authorship (`6379a937e7`) when it was
  uncommitted at-risk shared-tree work and AE was dark -- ships nothing, deploy separate. AE later
  applied + byte-verified (login destructures challengeId only). F-5 false-copy RESOLVED on the deploy.
- **Act C** (idempotency): I ruled the architecture -- PER-CHALLENGE scope (not user+window; Act B
  already kills the two-login mail path), the non-negotiable invariant `sends` counts EMAILS not
  rotations (or the mail cap evaporates), multi-session stated bound. AE applied + exercised 12/12 on
  the deployed plane; the invariant HELD (4th send REFUSED, sends stays 3).
- **Gate I set:** Act C's apply was HELD on F-8 + DE1-1 completing first, because both instruments live
  only in the rotation path Act C deletes (AE's ARMED catch). Released on F-8 complete.

---

## DE1-1 accepted; D12 verified on the ACTUAL prod client

DE1-1 (no code sent before opt-in) accepted on BOTH halves + BOTH oracles: server (mfa_code_rotated
pre-Act-C via F-8's run, CVO-scored PASS x2; mfa_code_sent post-Act-C via DE's UI run) + client (browser
network: no /auth/mfa/send before the click). I flagged DE's "prod serves pre-fix" bound as stale;
DE answered by MEASURING the actual opalinvest.dev minified build in a browser (F-10 cookie hygiene
first): prod client renders the opt-in, gates the send on the click, mints NO session without a code.
**CVO's "is Andrew stranded" closed on FOUR planes; every D12 property verified on the client prod
serves, not a byte-equivalent local one.**

---

## Compiler Tools

| tool | why | result |
|---|---|---|
| `git` (rev-parse/ls-remote/diff/merge/worktree) | the whole promote + Act B commit + source reads | PASS |
| `.tools/safe-commit.sh` | Act B (AE authorship override), pointer bump, ledger | PASS (msg-verify MATCH; a path-mangle false FAIL settled by `git cat-file`) |
| `.tools/aws lambda get-function-configuration` | CodeSha256 verification of Act B + Act C deploys, on MY instrument | PASS -- decisive |
| `gh -R Opal-Capital/portal run list/view` | CI verify (enumerate-by-headSha, -R load-bearing, tag peeled) | PASS |
| `comp-find` | rotateChallengeCode/sendMfaCodeEmail call-site discrimination (rail-compliant) | PASS |
| native `Read` on mfa.ts/auth.ts | verify + rotate + issue source (the F-8 mechanism reads) | PASS with the caveat that source!=deployed |
| raw recursive `grep` | attempted a call-site search | BLOCKED by Rule 21 comp-rail -> routed to comp-find (rail working) |

**What worked:** verifying every deploy on the DEPLOYED plane (CodeSha256 + AE's running-bytes census),
which is the discipline this handler needed all night. **What failed:** my repeated source-plane reads
concluding about deployed behaviour. **Gap found:** a metric-sum oracle (SES Sum) reads LOW under
CloudWatch aggregation lag, indistinguishable from a missing email -- AE caught a near-false-defect on
a re-read (banked-worthy: settle-delay or log-line cross-check).

---

## Errors -- mine, all corrected in-window

Four on the rotation row (above), all withdrawn before any acted on them; the F-8 amplification is the
worst (filed a security finding + acceptance reopen off an unverified mapping). One protective act I
stand by: committing AE's uncommitted Act B to save at-risk shared-tree work. One attribution I
corrected: a "HOLD the delete" was misattributed to me (CVO's 18744); I had sent nothing since the
DE1-1 accept.

---

## Blockers

**None.** D12 is fully closed. AC4 is EVENT-GATED (13:00Z fire), not blocked.

---

## Current State

- **D12 COMPLETE + VERIFIED ON PROD.** Bypass closed (v2.1.174 served bytes), Act B live (opt-in), Act C
  live (idempotency, 12/12), rotation confirmed no-defect (F-8), DE1-1 accepted both halves. Pilot LIVE:
  andrew@ (`usr_7f83e30de95f`) + aj@ (`usr_a5ae550bd45a`) enrolled; census HUMAN 2 / SERVICE 0 / FIXTURE 0.
- **Deployed handler:** `opalinvest-auth-handler` CodeSha256 `oExO72Sr...` (Act C), @08:56Z.
- **Findings:** F-5 resolved by Act B; F-8 closed no-defect; F-6 (offline code recovery from salt+hash,
  6-digit space) documented in mfa.ts hashCode comment, owner me, open; the build-script false-tagauthz
  finding (AE ce7e8c1710) INERT, build-tooling lane, ruled NEVER TAGAUTHZ_OVERRIDE for it.
- **Unpushed LOCAL:** portal pointer `a8305b3339`, ledger `e9ef2a9e46`, Act B `6379a937e7`, DE1-1 proof
  `764c103099` -- all integrator's leg (GATE 5 / LD-0367).
- **Zero crons.**

---

## Next Steps

- **[`1.0.0_SA_CTO~Z`]** score **AC4** on `gold/holding/date=2026-08-31` after the **2026-09-01T13:00Z**
  fire (~3.5h). Laptop `0.0.0_AB_MSTR` holds named fallback. Needs no peer.
- **[`0.0.0_AB_MSTR~Z`]** integrator push of the four LOCAL commits above at the next integration window.
- **[open, unowned]** F-6 (offline OTP recovery); the build-script false-tagauthz remedy (build-tooling
  lane, INERT).
