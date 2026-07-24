# 2026-07-24 — Session 1600-1630Z: MDPF promote pre-flight caught an ORG-WIDE GitHub Actions billing block

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Came up to take the MDPF promote (W-4/W-5/W-5b, portal DEV). Pre-flight failed for a reason nobody in
the fabric was tracking: **GitHub Actions is refused at dispatch across the entire Opal-Capital org.**
No promote fired. Nothing staged. Finding is with Andrew via COO; sovereign-class (only he can clear a
billing block).

## The finding

GitHub's own check-run annotation, verbatim, pulled independently on jobs in BOTH repos:

> "The job was not started because recent account payments have failed or your spending limit needs to
> be increased. Please check the 'Billing & plans' section in your settings"

Confirmed on:
- `Opal-Capital/portal` — job `89524549044` (CI - Build & Validate, DEV head `d1ba89b9`, 15:40Z)
- `Opal-Capital/ajb_workspace` — job in run `30107975250` (Comp Tool Tests, 16:07Z)

## It is not "CI is red." The jobs never start.

The discriminator, **positive-controlled against a known-real failure before I trusted it**:

```
BLOCKED (today)      steps=0   runner=""                       dead in ~2s   NO LOG EXISTS
REAL FAIL (07-23)    steps=16  runner="GitHub Actions 1000003037"            failed step "Run ESLint"
```

`gh run view --log-failed` on a blocked job returns **`log not found`** — an absence that reads exactly
like a pass if you stop there. This is why it sat unremarked through ~80 runs: on every dashboard we
own, *refused* and *failed* are the same colour.

## Scale + onset (bounded by measurement, not asserted)

| Repo | Evidence |
|---|---|
| `ajb_workspace` | **100 of the last 100 runs `failure`. Zero successes.** Oldest in window 2026-07-24T14:22:02Z — the entire visible history is inside the outage. |
| `portal` | Onset bounded: 07-23T22:39:15Z real runner assigned (working) → 07-24T14:27:06Z blocked. |

## What is down

- `ajb_workspace`: **`lambda-deploy.yml` (LAMBDA DEPLOYS)**, **`ec2-deploy.yml` (EC2 DEPLOYS)**,
  `comp-tool-tests.yml`, `drift-producer-push.yml` + `stitch-source-push.yml` (feeds for the nightly
  stitch-produce CodeBuild and the drift producer), `surface-check-publish.yml`,
  `shared-infra-drift.yml`, `trigger-map-drift.yml`, `inf-pipeline-lib-parity.yml`.
- `portal`: `deploy.yml` (all three jobs `runs-on: ubuntu-latest`), `ci.yml`, and the **Surface-Check
  Gate** that CLAUDE.md Rule 20 calls the non-bypassable backstop.

**Anyone holding work that ends in a deploy is blocked and does not know it.**

## The failure shape — and my own correction to it

Had the GO arrived and I fired:

```
origin/PROD advances · git push returns 0 · NO build · NO S3 sync · NO CloudFront invalidation · NO TAG
```

COO's first report to Andrew said a tag *would* have landed and framed it as "the repo asserting
success while the site stayed unchanged." **That overstates it.** The auto-tag is the `tag` job inside
`deploy.yml` (`:120`, `runs-on: ubuntu-latest`) — refused with the other two. With no tag minted, my
standing `git rev-parse <tag>^{commit}` peel against `origin/PROD` **fails loudly rather than passing
falsely.** A signal survives.

I sent that correction up; COO accepted it and carried it to Andrew rather than quietly adjusting notes
(his words: *"I overstated the severity, in a report about a failure class defined by things looking
better than they are"*).

**The true residual hazard is narrower and still real:** PROD branch advanced, deploy absent, and the
failure surfacing as *"my verification tooling cannot find anything"* rather than *"the deploy failed."*
An absence that has to be correctly **read** as an absence. That is the version that belongs in doctrine
— not "green all the way."

## Unresolved (stated as unresolved)

`lambda-deploy.yml` and `ec2-deploy.yml` render with their raw **file path** as the run name and have
**zero jobs at all**, where billing-blocked runs elsewhere carry one job with zero steps. May be GitHub
failing before it resolves `name:`, or a separate workflow-parse problem underneath the outage. **If it
is a parse error it will still be broken after the bill is paid — and will be easy to mistake for
"fixed" when the other workflows return.** `.github/workflows/inf-pipeline-lib-parity.yml` is modified
in the working tree, so workflows are being edited in this window. Not chased; flagged to CTO.

Also flagged, NOT measured: `drift-producer-push` / `stitch-source-push` have not fed since ~14:2xZ, so
downstream graph/drift artifacts may be frozen at that vintage **while still answering queries
normally**. I did not verify the downstream vintages — that is 0.7.0/0.8.0's instrument and I am not
asserting a staleness finding I did not run. Mechanism only.

## Promote state (held, zero-context handoff)

- **HELD** on three reasons: (1) GitHub billing — the hard one; (2) DE's render precondition — since
  answered, 4-for-4 prediction match, cottonwood 445/447 holes; (3) push-scope call (Andrew ~1600Z:
  pushes Tier-1 only, COO primary push operator) — **moot as a promote-blocker**, since neither of us
  can make Actions run.
- Target pinned **`d1ba89b9`**. Set is **FIVE** commits, not three — my measured delta surfaced two
  `tooling(ui-smoke)` commits (`8602d0f7`, `3e681423`) COO had not scoped in. If DE pushes again, STOP
  and surface; do not widen.
- `origin/PROD` = `17256834` (v2.1.148), local PROD ref == origin/PROD, main tree **on DEV** (Rule 19
  held), local DEV == origin/DEV. **Nothing staged: no ephemeral worktree, no merge prepared.**
- Prohibitions ACKed and held: no route around CI, no push, no Andrew ping (CTO owns it).

## Next Steps

- **[Andrew]** clear GitHub billing. Nothing in the fabric can substitute.
- **[me]** on clear: **re-run the full pre-flight from scratch** — today's CI evidence is a different
  vintage. **Assert `runner_name` is non-empty before reading any green as meaningful**; a still-refused
  re-run looks identical to today's instant failure, and the first green after a billing fix is exactly
  when someone will be in a hurry.
- **[1.0.0_SA_CTO]** the Rule 20 backstop is down fabric-wide for portal; the raw-path/zero-job anomaly
  on `lambda-deploy`/`ec2-deploy` wants a look post-clear.
- **[0.7.0_AE / 0.8.0_AE]** graph/drift artifact vintages, if the producers have been dark since 14:2xZ.

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| (none — with cause) | -- | The question was "why is this CI run failing," and the tool that owns it is the GitHub Actions API itself — no comp-tool models GitHub run/job/annotation state. Verification ran on live primitives, which is the sharper test here: `gh api .../actions/runs/{id}/jobs` for `runner_name` + step counts, `gh api .../check-runs/{id}/annotations` for GitHub's own failure text (the decisive evidence), and `gh run list --json` for onset bounding. Repo/branch/delta state read directly via `git rev-parse` / `git log`, not recollected. |

What worked: **positive-controlling the discriminator against a known-real ESLint failure before
trusting it** — without that control, "steps=0" is just a number and the billing block reads as an
ordinary red. Bounding onset by two measured observations instead of asserting it. Checking the SECOND
repo instead of stopping at the one my task was in — that is what turned a portal finding into an
org-wide one, and I had already sent the under-scoped version before widening it.

What failed: nothing tool-wise. `gh run view --log-failed` returning `log not found` is the one trap —
it is a broken-retrieval-yields-clean-output case, and taking it at face value would have ended the
investigation at "no log, must be transient."

Gap found: **no comp-tool route for GitHub Actions / CI state.** `comp-which` has nothing for "why did
this workflow run fail" or "is CI healthy." Given portal CI is a named blocking gate in Rule 20, a
CI-health route that distinguishes *refused* from *failed* would have surfaced this at 14:2xZ instead
of 16:2xZ. Logged rather than worked around silently.
