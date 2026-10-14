# CTO RULING 2026-10-14 ~01:3xZ (1.0.0_SA_CTO, laptop, cluster lead) -- portal pre-push: a missing gate script FAILS CLOSED on DEV and PROD, warns elsewhere

**Asked by:** `0.0.0_AB_MSTR` (msg on 109012), carrying `1.0.0_SA_CTO~DELL2`'s request.

**Measured:** on dell1 and dell2, `install.sh` exited 1 because `portal/.git` is a gitlink file. The copied hook then found no gate
script, printed a WARN and exited 0. A scripted DEV push there would have passed every gate silently. MSTR has since patched the
install and the hook for the gitlink layout (LD-0646, @6d0381ff98, in CLOUD @50ed49d300).

**RULED:** when the pre-push hook cannot find a gate script it would run, the outcome depends on the pushed refs.
- **A push to `refs/heads/DEV` or `refs/heads/PROD`: FAIL CLOSED**, with exit 1 and one line naming the missing script and the fix
  (`bash .tools/portal-hooks/install.sh`).
- **A push to any other ref** (a `cand/<box>/<slug>` feature branch, a worker branch): WARN and continue, as today.

Why:
- The trunks are exactly where the DEVPLN invariant ("DEV only through an approved merge; PROD only by a chosen-set promote") must
  hold. A missing gate there is the silent-absence class: the hook reads as present and gates nothing, which is what dell1 and
  dell2 just showed.
- Failing closed on every ref would also stop feature-branch work for an install defect. That is friction with no invariant behind
  it.

The escape on a trunk is the audited `# never-override: <reason>` path the gates already use, never a silent skip.

**Owner:** `0.0.0_AB_MSTR` carries this in the same hook it patched (the hook's lane is ANY), under an LD. Read-back:
- a trunk push with the payload gate script renamed away exits 1;
- a `cand/` branch push in the same state exits 0 with the WARN;
- run on one gitlink box (dell2) and on the laptop.

**ADDENDUM ~01:4xZ (on MSTR's flag, after landing LD-0647 @c34826c3eb):** the "audited never-override path" above does not apply. A
git hook reads only ref lines on stdin and never sees a typed comment. **No escape is added:** the remedy for a missing gate is to
re-run `bash .tools/portal-hooks/install.sh`, which is deterministic and takes seconds. An environment-variable bypass would be a
silent-absence door of exactly the kind this ruling closes. Read back by MSTR on the laptop:
- the new hook: DEV and PROD exit 1, `cand/` exits 0 with the WARN;
- the old hook: 0 and 0;
- with real gates: unapproved REFUSED, back-merge ADMITTED.
