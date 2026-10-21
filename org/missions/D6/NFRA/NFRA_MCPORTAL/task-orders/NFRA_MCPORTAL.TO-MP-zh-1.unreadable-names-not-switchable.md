# NFRA_MCPORTAL task order -- `MP-zh-1` -- WORKSTREAM OGH ROUND 1: the page never writes a channel or tool name the gateway cannot read (FWD-29, row NFRA_OPLGTW-Z-S447)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zh-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zh-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~48</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the tests plant the contrary (an unreadable name; a readable one) and assert each behaves as the face says.
EGRESS CLASS, declared: none. Make no network call (the tests mock fetch).
</preflight>

## 1. THE CELL -- `MP-zh-1` (workstream OGH round 1, decomposition section OGH1.1)

You have two worktrees, nested: the workspace worktree `C:/tmp/mp-ogh-48` (branch `wk-NFRA_MCPORTAL-48`) and, inside it, the mcportal worktree `C:/tmp/mp-ogh-48/mcportal` (branch `wk-NFRA_MCPORTAL-48-mcportal`), based on mcportal `a577f99` (origin DEV). `node_modules` is linked. Do not run `bun install` or `bun add`. Begin each shell call with `cd C:/tmp/mp-ogh-48 &&`. Commit code in the mcportal worktree with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~48 <0.9.0_WK_NFRA_MCPORTAL~48@opal.agent>`. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~48 <0.9.0_WK_NFRA_MCPORTAL~48@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind. There is NO DOM under `bun test` here (bun 1.3.x has no `document`): test pure functions and server-rendered markup only; do not try to mount a component.

**What was found.** The gateway reads a person's access record strictly: every entry of `channels_allow` and `channels_deny` must match `^[a-z][a-z0-9_]{0,63}$`, and every entry of `tools_allow` and `tools_deny` must match `^[a-z][a-z0-9_]{0,99}$` (gateway source `app/data_entitlement.py` lines 250 and 254, applied at 591-594). One entry that does not match makes the WHOLE record unreadable, and then every tool of that person fails closed. The grant writer checks only that an entry is a non-empty string of at most 128 characters, so it accepts what the gateway cannot read. The People panel's channel switch writes `channels_deny: [<channel id>]` (`src/pages/people/personAccess.ts`, `channelToggleChange`), and five of the fourteen real channel ids carry a hyphen: `opal-data-assets`, `opal-data-etfs`, `opal-data-harvest`, `opal-data-mdpf`, `opal-data-portal-v2`. Turning one of those OFF, from the People page or from `/opalgateway`, would write a record the gateway reads as unreadable. Both pages share one access view and one panel, so one fix covers both.

Build (in `mcportal/src/pages/people/` and `mcportal/src/pages/opalgateway/`):
1. **Two pure functions** exported from `personAccess.ts`: `channelIdReadable(id)` is true only when `id` matches `^[a-z][a-z0-9_]{0,63}$`; `toolNameReadable(name)` is true only when `name` matches `^[a-z][a-z0-9_]{0,99}$`. Each carries a comment naming the gateway file and lines above.
2. **The view.** In the shared access view, a channel switch whose `channel.id` is not readable, and a tool switch whose `tool.name` is not readable, is rendered DISABLED, and its row says once, in the page's existing note style, `Not switchable yet: the gateway cannot read this name.` A readable name switches exactly as today.
3. **The guard.** The panel's post path refuses, with no request sent and a notice saying why, any change that would put an unreadable name into any of the four lists (`tools_allow`, `tools_deny`, `channels_allow`, `channels_deny`). Do it the way the last-admin guard refuses (`postUnlessStopLocked` in `personAccess.ts` is the pattern: a pure check in front of the post that resolves to null), as a pure function that is unit-tested.
4. **TWO tests**, each by its exact name, as the literal first argument of its `test(...)` (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; synthetic fixtures only; in `src/pages/opalgateway/opalgateway.test.tsx` or a sibling test file there):
   - `a channel or tool whose name the gateway cannot read has a disabled switch and builds no change, while a readable one switches as before`
   - `no change that puts an unreadable name into any of the four lists is ever posted`
All existing tests keep their names and pass. If an existing test toggles a channel or tool with an unreadable name and expects it to switch, REPORT it: file, test, old assertion, new assertion; you may change that one assertion (and only that kind). `bun test src` now reads 93 or more pass and 0 fail.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway (Python) file, no Lambda, no Terraform, no `package.json` or `bun.lock`, no deploy, no network call. Do NOT edit `src/api/admin.ts`.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it.
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author. Do not print a real name, email or account.

## 3. SURFACES

<paths>
mcportal/src/pages/opalgateway/
mcportal/src/pages/people/personAccess.ts
mcportal/src/pages/people/PersonAccessPanel.tsx
mcportal/src/pages/people/PersonAccessView.tsx
mcportal/src/pages/people/people.test.tsx
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~48/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md` (the colour law: use the page's existing classes; no new colours), the gateway file `infra/aws/ec2/opal-gateway/app/data_entitlement.py`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W48-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them). `surfaced_at` = `date -u +%FT%TZ`. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zh-1"><invocation>cd C:/tmp/mp-ogh-48 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zh1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests present in sources 2 of 2.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-zh-1"><invocation>cd C:/tmp/mp-ogh-48 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zh1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)tsc rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~48/NFRA_MCPORTAL.TO-MP-zh-1.unreadable-names-not-switchable.proof_of_spec.json`, run `proof-of-spec-check.py` on it as the worker rules say, and report once, with: the output of AC1 and AC2; the mcportal commit hash or hashes and the workspace commit hash; every existing assertion you changed (file, test, old, new), or none; `bun run build` in the nested worktree (rc); any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at once on `2.0.0_SA_COO~O`'s row `NFRA_OPLGTW-Z-S447` and the CTO's hazard message (15:17Z): the shipped panel can write a hyphen channel id that the gateway reader calls Malformed once the mount (`OG-mp-1`, batch17, not before 2026-10-22T06:00Z) is live. Measured by the issuer (served capture of the 14 channel ids against the reader's pattern; `personAccess.ts` :34). A SEPARATE workstream (OGH) because `to-pipeline-gate` allows one issuance per workstream round and OGP, OGW round 2 already have theirs; the write surface overlaps the DONE `MP-zp-1` files only (no live order). Must ship in the batch17 bundle pin: the issuer re-sends the new mcportal commit to `2.0.0_SA_COO~O` at the drain and asks MSTR~Z to advance DEV. Checks dry-run at base in the provisioned slot-48 worktree (mcportal a577f99, 2026-10-21 ~16:5xZ): zh1.AC1 FAIL as expected (`bun test src` 91 pass, 0 fail; named tests present in sources 0 of 2; min 93); zh1.AC2 passes at base (tsc rc 0) by design: a type-check guard against the worker's edit, not a build criterion.

<status>pending</status>
<round>1</round>
<workstream>OGH</workstream>
<slot>~48</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
