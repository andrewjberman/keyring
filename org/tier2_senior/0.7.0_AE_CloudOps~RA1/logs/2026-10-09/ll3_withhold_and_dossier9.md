# 0.7.0_AE_CloudOps~RA1 -- 2026-10-09 -- AMGT_RESAPP AMGT-ll-3: the FAILED-description withhold and AMGT_CORPUS dossier /9

Fourth order this lane held today (ee-6 r81, gg-7 r82, jj-5 r85, ll-3 r87). One code leg, three conditions, and the
round where the interesting work was **reading a criterion carefully enough to notice it had stopped proving anything**.
Full record: the instance under this lane's `deliverables/`, VALID rc=0, 12 of 12 controls discriminate.

## The act
**archetype:** DEPLOY

`HZoC2xAifZQGMcEhp6Aso9DH7e5jdqQxHqM6oPXAt9U=` -> `b7Lj1J/KKhDtg+mvN/vmu4VAoaExU055uB78roHiHfM=` at 19:51:25Z from
pin `9c32fb942d`. CONTENT-DIFF 399 members, 7 non-identical, **off-list 0**. Both explicit STOPs clear and each *read*
rather than assumed: `drafting_build.py` 0 mentions, dossier `/8` 0 mentions. **AC1** YES, **AC2** YES, **AC3** YES.
Ledger closed 10 of 10.

## What I did better than last round
**archetype:** VALIDATE

- **Checked the citation, not just the text.** The CTO half pairs with the COO half `@433e2b510d`; I printed the COO
  half from *that pin* and diffed it against HEAD -- byte-identical. Only then is it sound to say the half I read is
  the bytes the CTO signed against.
- **Verified condition 1 myself** instead of taking the issuer's word: dossier at the pin reads `/9` *and* is byte-equal
  to CORPUS's graded commit. Then the same METHOD at **three** places -- the pin, inside the built zip (member
  hash-compared to the pin's blob), and on the deployed function -- so the chain from graded commit to shipped bytes to
  live function is closed at every link.
- **Read the one-resource claim from `terraform show -json` over the saved plan** (`moving resources: 1`, address named)
  instead of eyeballing a truncated console tail. That's the read that should back the claim; earlier rounds didn't.

## The finding: AC1 had quietly stopped being able to fail
**archetype:** DIAGNOSE

Condition 2 asks for the FAILED list *before* the apply. I ran it, and the list came back **EMPTY** -- 25 drafted
sections censused across the five 20-F names, 5 carry a verdict field (all `NO_SENTENCES`), 20 carry none, **zero
FAILED**. So AC1 and its NU arm **already passed at the base**, while the order's record face expected AC1 to fail with
NU carrying 1 sentence.

The cause was benign and the COO half had predicted it: `ll-2` emptied NU in the **store** first, so the live read moved
to `NO_SENTENCES` on its own. A store change, not a code change, moved the base onto the pass side.

The consequence is what mattered: **AC1 became a bound, and a post-deploy pass could have been recorded as proof the
withhold works.** I reported it before the apply; the issuer ruled it accepted, with the positive branch proven offline
by ll-1's unit tests. Running the battery *before* the apply is what surfaced this -- it would have been invisible
afterwards.

I said I'd file a row and then **didn't**, deliberately: the half anticipated the exact state, so world matches spec and
the surprise channel is the wrong carrier. It lives in the ledger's L4 proof instead.

## My own miss, named
**archetype:** DIAGNOSE

Two of the five whole `/thesis` bodies moved (BABA **-20 B**, NU **+74 B**); three are byte-identical. My first instinct
was to write "that's the dossier moving to /9" -- then I checked, found `/thesis` serves no `method_version` field, and
had to retract it: **I could not attribute the delta.**

What I can say: `dossier_sections` *is* a top-level key of that body, and the COO half's writer census names
`dossier.py` as its **one** writer while stating /9 moves its served values. So the movement is on the one surface the
pair predicted, written by the one module I changed. But my baseline hashed `drafted_sections` and the whole body --
**not `dossier_sections` on its own** -- so the attribution is **structural, not measured**.

That's a gap in my baseline design, not an estate defect. The lesson: capture a pre-apply hash of every key the pair
predicts will move, not just the keys the conditions bind. Handed to C1 as unattributed rather than dressed up.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `deploy_ledger.py` | open / close-leg x10 / close | PASS. Committed sentinel + entry at open itself. Carrying the owed reply to C1 **as leg L10** meant it couldn't be forgotten at close. |
| `terraform show -json` | over the saved plan, pre-apply | PASS, and an upgrade: `moving resources: 1` with the address named, from the plan's own JSON. |
| AST import-census | over the built package, for `opal_naming`'s closure reason | PASS. 6 packaged importers named -- what the pair requires before admitting an off-project member. |
| `r87_withheld.py` | at the **base** before the apply, and after | This is the one that earned its keep: the base run is what exposed AC1 as a bound. |
| `r87_dossier.py` / `r84_listing.py` | the order's literal invocations | PASS. AC2 is the criterion that actually discriminates this deploy. |
| per-section baseline capture (authored) | pre-apply hashes for the five names, kept to disk | **PARTIAL**, reported as such -- proved `drafted_sections` byte-equal, missed `dossier_sections`. Fix is scope, not method. |
| `comp-find` / comp-rail | **not used** | No census needed: every path was named in the order, the halves or the GO -- and BOUNDS 8 forbids repository-wide search outright. Recorded because "ran none" and "needed none" read identically otherwise. |

## Bounds honoured
BOUNDS 8 (client data): no `W73_S*_EVIDENCE.json`, no COTBKF cottonwood manifests, no IRPT_DASHBD tie-out files
opened, searched, copied or `git show`n, in tree or history. Every search scoped to a named path. BOUNDS 3: no
`pip install` (index requests 0), no bun/npm, no Bloomberg call. BOUNDS 1-2: no IAM, route, memory, schedule, store
write or S3 delete.

## Noted
The order's **preflight has gone stale**: it says HEAD carries dossier at `/8` and a build from HEAD would ship `/8`.
Measured now, HEAD also reads `/9` with 0 mentions of `/8` -- CORPUS round 42 landed it between the cut and the GO.
Changes nothing (I build from the pin), recorded so no later reader treats that hazard as live.

jj-5's admission held: the three identity modules admitted off-list last round now read IDENTICAL.
