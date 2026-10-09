# ADHOC_PARTNER_ROSTER -- surprise channel, investigations

Named by `ADHOC.partner-roster-t1-into-live-readers` `<conditions>`. Append rows; keep working.

```json
{
  "id": "ADHOC_PARTNER_ROSTER-D1-S1",
  "project": "ADHOC_PARTNER_ROSTER",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-09T02:28Z",
  "one_line": "The bundle mint reads the WORKING TREE, not the index blob, so on this box leg A1 would package CRLF roster bytes into the served bundle and stamp sha256 9d8ed608.. where criterion C2 requires 4c104d9b..",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G1",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe_deploy_core.py build_bundle_payload: `src = WORKSPACE / spec['repo_path']...` then `data = src.read_bytes()` -- the WORKTREE file, with no newline normalization.",
      "safe_deploy_core.py deploy_file:908 uses `_index_blob(rel_path)` instead, whose docstring reads: 'the bytes git HAS RECORDED ... the INDEX, not the worktree. BYTES, never text: decoding here would re-introduce the newline translation this whole change exists to remove ... never a worktree fallback, because falling back to the worktree on a lookup failure would silently restore exactly the behaviour being replaced.' The loose per-file leg was hardened against this exact hazard; the BUNDLE leg was never converted.",
      "git ls-files --eol -- data/mdpf/config/partner_roster.json  ->  i/lf  w/crlf  attr/   (CRLF in the worktree, LF in the index, and NO gitattributes rule covers it: the .gitattributes:153 glob is data/mdpf/config/*.yaml and this file is .json)",
      "sha256 of the bytes the mint WOULD read (worktree): 9d8ed608c2111af398c591cbe7f8a74e6520418ea92c532cd8eebe53d3911087",
      "sha256 required by criterion C2 and by both signed halves (HEAD blob, LF): 4c104d9bb8509b89456ad46f41dc07bec1eb39c5caa045149d26a20e33ff64a6 -- identical to the INDEX blob sha, confirming index==HEAD here",
      "byte arithmetic closes it: worktree 27826 bytes - blob 27433 bytes = 393 = the exact CR count in the worktree copy",
      "the mint was NOT run. This row is a pre-act read, so nothing was served wrong; the hazard is that the next mint of ANY bundle whose member is CRLF in the minting box's worktree stamps a sha that does not match its own authority."
    ]
  },
  "spec_asserts": "The order's criterion 2 and both never-widen halves require the re-minted bundle's metadata roster-authority-sha256 to equal `git show HEAD:data/mdpf/config/partner_roster.json | sha256sum` (4c104d9b..), and the COO half specifies the act as 'the safe-deploy in-flow mint from HEAD (LF bytes)'.",
  "world_is": "The in-flow mint materializes each member from the WORKING TREE via src.read_bytes(), not from the committed authority. On this box that file is CRLF, so the mint would package 27826 CRLF bytes and stamp 9d8ed608.., failing C2 and republishing a SERVED bundle whose roster bytes are not HEAD's. The two remedies -- re-normalizing data/mdpf/config/partner_roster.json, or changing build_bundle_payload to use _index_blob like deploy_file already does -- are both OUTSIDE this order's declared <paths> (change_management/, .open_deploys/, this seat's folder), so neither is this seat's to make.",
  "notes": "SCOPE IS WIDER THAN THIS ORDER: the defect is in the shared bundle-mint path, so it reaches every declared bundle (accrual_bridge and the IRPT holdings bundles), on any Windows worktree, for any text member. It is invisible on a box whose checkout happens to be LF, which is why it has survived. Leg A1 is held, NOT failed -- the act was never attempted. Leg B is unaffected and proceeds: B1's input is explicitly `git show HEAD:...` bytes assembled in a scratch build, never the worktree copy. Related, same mechanism, found earlier tonight on a different file and recorded at 8430c79f13: data/mdpf/config/route_bindings.yaml is i/lf w/crlf DESPITE carrying eol=lf, because an eol attribute governs checkout and never rewrites a file already in the tree."
}
```
