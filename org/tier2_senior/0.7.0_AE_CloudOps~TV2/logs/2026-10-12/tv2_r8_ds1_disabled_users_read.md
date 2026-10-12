# What sign-in, the authorizer and the table say about a disabled user — 0.7.0_AE_CloudOps~TV2

**archetype:** READ

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-READ-R8-ds1.disabled-users-authorizer-and-status-values-dell2 (read at `733c0943cd`)
**Status:** COMPLETE — AC1 `DS1-READ-OK`

---

## First of all, because the order asks for it first

**One of the two disabled internal rows reads as a PERSON.** Digest `04fc361f3802`: a single given name at an
**external company domain**, `userType` null, carrying the **internal** firm id `opal-capital`, `updatedAt`
2026-07-14, never on any ticket.

The other, `e95c05c7ae90`, is tooling: a hyphenated handle on `opal.test` with `userType "Dev"`.

**My first heuristic got this wrong and would have buried it.** It tested whether the domain equals
`opalinvest.com` — which classes *every external person* as non-human, since a person at a partner firm or
vendor has an external domain by definition. It rendered that given name as "looks like a service/tool
handle". Re-read on the **form of the local-part** instead, it reads as a person. That correction happened
before anything was written.

---

## The three answers

**(a) Does sign-in refuse a disabled user? YES.** It reads `status` and admits **exactly** `'active'` —
the guard is `status !== 'active'`, so every other value is refused, including an absent attribute
(`types.ts:25` declares `status?: string`).

```
auth.ts:106   login(), after the credential check
auth.ts:255   the MFA REDEMPTION re-check -- "an account disabled between the password
              check and the code submission must not get a session"
auth.ts:538   the REFRESH path (answer b)
```

**(b) Does refresh refuse a user disabled since sign-in? YES**, `auth.ts:538`, whose comment states the
intent: a disabled or removed user must not mint fresh access tokens for the 7-day window, mirroring
login()'s guard with the *same error string* so the two are indistinguishable.

**(c) Does either authorizer read the row's status per request? NO — neither does.** Zero hits for
`status`, `disabled`, `getUser`, `GetItem`, `GetCommand` or `QueryCommand` in both files, against working
positive controls, **checked on HEAD *and* on the deployed build input**. The deployed authorizer's only
users-table read is a `ScanCommand` filtered `SK = :meta AND parentFirmId = :parent` projecting `firmId`
(lines 84-94), inside `getAllDescendants` → `computeAllowedFirms`. It reads the firm hierarchy, never the
caller's own PROFILE row.

**So a token issued before the disabling keeps working until it expires** — and the window is **~15 minutes,
not 7 days**:

```
jwt.ts:17   ACCESS_TOKEN_EXPIRY  = '15m'
jwt.ts:18   REFRESH_TOKEN_EXPIRY = '7d'
```

The refresh path *is* guarded (b), so the 7 days cannot be used to mint a new access token after the
disabling. The 7d figure bounds the token *shape's* life, not a disabled user's reach. Read from the code's
constants; no token was read.

**What that does *not* bound: the direct-invoke path.** Row `D2-S46` records that a holder of
`lambda:InvokeFunction` presents any caller context with no token at all — no sign-in, no expiry, no 15
minutes. That is how this project's own R6 and R7 proofs were run.

---

## (d) The deployed-versus-source question, where a pointer misled

| function | live hash vs map | source vs recorded commit | verdict |
|---|---|---|---|
| `opalinvest-auth-handler` (sign-in) | equal | **0 changed files** under `src/` | **TIED three ways** — and the three guards verified present *at* that commit |
| `opal-portal-authorizer` | equal | **188 lines apart** | tied to its **artifact**, not to HEAD's source |
| `opal-portal-rest-authorizer` | equal | no `last_deployed_commit` in the map | **NOT TIED** |

The order's pointer names the authorizer's source as "450 lines". **The deployed build input is 262.** The
file I first read is not what runs. The 188 added lines are a render-token path
(`getRenderPublicKeyPem`, `isRenderAudienceToken`, `authorizeRenderToken`…); the single added line mentioning
DynamoDB is a comment. **I re-measured the status absence against `git show 26ffa22b79:<path>` and it holds
there too** — so the answer stands, but it stands on the deployed input rather than on luck.

---

## The status values, and the two populations

```
PROFILE rows                     56        (86 items scanned, no unread page)
  active                         54
  disabled                        2
  SUM                            56  ==  56   PASS
internal (opal-capital)          23  ->  active 21, disabled 2
rows with an ABSENT status        0
disabledAt / enabled / active / deleted / lastUpdated / modifiedAt   0 rows each
updatedAt                        53 of 56 (a last-touched timestamp, not a state; 3 rows lack it)
```

**`status` is the only attribute carrying this meaning, and it holds exactly two values.** So:

- **sign-in admits the 54 rows whose status is `active`**
- **the ticket service's no-row rule — live since 2026-10-12T00:22:08Z — admits all 56**, because it reads
  whether a row *exists*

**The difference is exactly the 2 disabled rows, both internal.** Refused at sign-in, admitted by the ticket
service. That is the sentence the CTO's contract change waits on, and one of those two reads as a person.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | over the sign-in source, **both pages** | PASS | 44 hits / 13 files; page 2 held `status?: string` |
| grep on named files + controls | the two authorizers | PASS | 0 hits against controls of 4 and 2 |
| git show / diff --numstat | the recorded deploy commits | PASS | **caught the 188-line drift** |
| get-function-configuration ×3 | three functions | PASS | both live hashes == map hashes |
| dynamodb scan, projection, no filter | users; tickets | PASS | 86 items, no unread page |

**What worked:** re-measuring the authorizer absence against the **deployed build input** rather than HEAD.
CLAUDE.md 22a says to diff deployed bytes against the build input and never by filename — the order's pointer
*was* a filename, and the build input turned out to be 188 lines behind it.

**What failed:** my person/non-human heuristic (above). Also three rail denials taught me to use `comp-find`
with `--limit` and not to pipe a census into `head`.

**Gap found:** none new to file. The drift is covered by 22a; the direct-invoke exposure is already the CTO's
row `D2-S46`.

---

## Decisions Made

1. **Reported the person-shaped row first**, as the order requires, and said plainly that my own first
   heuristic would have hidden it.
2. **Re-measured the authorizer absence on the deployed build input**, not HEAD, once the hashes showed the
   drift.
3. **Gave the practical window as ~15 minutes, not 7 days**, because the refresh guard closes the long path —
   reporting "7 days" would have overstated the exposure by two orders of magnitude.
4. **Named the direct-invoke path as unbounded by any of this**, so the 15 minutes is not read as the whole
   answer.
5. **Said NOT TIED where I could not tie**, rather than inferring: the rest-authorizer has no commit in the
   map, and a matching artifact hash never proves which source built it.
6. **Checked all 11 cited paths exist** before writing, since AC1 fails on a dead citation.
7. **Kept every address out**, carrying the email **domain** for the two disabled rows because for one of them
   the domain is the evidence.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r8_ds1/DISABLED_USERS_READ_20261012.json`, proof_of_spec, this log, TO status | this commit |

No AWS write, nothing invoked, no ledger entry.

---

## Blockers

None owed by this seat. The contract sentence is the CTO's to write from this read; row `D2-S50` (ARMED) and
`D2-S46` are both that seat's.

---

## Current State

Sign-in and refresh both refuse any user whose `status` is not exactly `active`. Neither authorizer re-checks
the row per request, so a token already minted lives out its 15 minutes. The ticket service, since 00:22:08Z,
admits any caller whose row exists — including the two disabled rows, one of which reads as a person.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` writes the contract sentence: which status values admit a caller, and who that locks
   out. The candidate populations are measured above — 54 active, 2 disabled, no absent.
2. If the disabled gap is to be closed in the ticket service, that is a further release and a further pair.
