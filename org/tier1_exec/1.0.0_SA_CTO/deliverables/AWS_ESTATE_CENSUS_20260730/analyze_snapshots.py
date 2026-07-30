"""Snapshot/AMI detail analysis (Andrew: "1288 snapshots need more detail on").

Joins snapshots.json x images.json x volumes.json x instances.json:
classifies every snapshot, every AMI, prints kill-candidate classes with
denominators. Read-only; no AWS calls.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

snaps = json.load(open("snapshots.json"))["Snapshots"]
images = json.load(open("images.json"))["Images"]
vols = {v["id"] for v in json.load(open("volumes.json"))}
insts = json.load(open("instances.json"))

# AMI -> snapshot refs
ami_snap = defaultdict(list)
for im in images:
    for bdm in im.get("BlockDeviceMappings", []):
        sid = bdm.get("Ebs", {}).get("SnapshotId")
        if sid:
            ami_snap[im["ImageId"]].append(sid)
snap_amis = defaultdict(list)
for ami, sids in ami_snap.items():
    for sid in sids:
        snap_amis[sid].append(ami)

# instance lineage refs (live = not terminated)
live_insts = [i for i in insts if i["state"] != "terminated"]
ami_in_use = Counter(i["ami"] for i in live_insts)

# classify AMIs by name prefix + age band + referenced
img_by_id = {im["ImageId"]: im for im in images}
print(f"AMIs: {len(images)} | referenced by a live instance: "
      f"{sum(1 for im in images if im['ImageId'] in ami_in_use)}")
pref = Counter()
for im in images:
    name = im.get("Name", "?")
    pref[name.rsplit("-", 1)[0][:48]] += 1
print("top AMI name-stems (stem: count):")
for p, c in pref.most_common(20):
    print(f"  {p}: {c}")
print("AMI creation by month:")
for m, c in sorted(Counter(im["CreationDate"][:7] for im in images).items()):
    print(f"  {m}: {c}")

# classify snapshots
cls = Counter()
gb = Counter()
orphans = []
for s in snaps:
    sid = s["SnapshotId"]
    desc = s.get("Description", "")
    if sid in snap_amis:
        c = "ami-backed"
    elif "policy-0c0c24e7981c5522c" in desc or "dlm" in desc.lower():
        c = "dlm-managed"
    elif s.get("VolumeId") in vols:
        c = "manual-volume-extant"
    else:
        c = "ORPHAN (no AMI ref, source volume gone)"
        orphans.append(s)
    cls[c] += 1
    gb[c] += s["VolumeSize"]
print(f"\nsnapshot classes (n={len(snaps)}):")
for c, n in cls.most_common():
    print(f"  {c}: {n} snaps, {gb[c]} GB(vol-size upper bound)")

print("\norphan detail by month:")
for m, c in sorted(Counter(s["StartTime"][:7] for s in orphans).items()):
    print(f"  {m}: {c}")
odesc = Counter(s.get("Description", "")[:64] for s in orphans)
print("orphan description patterns (top 15):")
for d, c in odesc.most_common(15):
    print(f"  {c:4d}  {d!r}")

# kill-candidate class: AMIs NOT referenced by any live instance
unref = [im for im in images if im["ImageId"] not in ami_in_use]
unref_snaps = {sid for im in unref for sid in ami_snap[im["ImageId"]]}
unref_gb = sum(s["VolumeSize"] for s in snaps if s["SnapshotId"] in unref_snaps)
print(f"\nKILL-CANDIDATE: AMIs unreferenced by any live instance: {len(unref)} "
      f"AMIs -> {len(unref_snaps)} snapshots, {unref_gb} GB upper bound")
print("unreferenced-AMI age by month:")
for m, c in sorted(Counter(im["CreationDate"][:7] for im in unref).items()):
    print(f"  {m}: {c}")
print("\nAMIs REFERENCED by live instances (keep, lineage):")
for ami, n in ami_in_use.most_common():
    im = img_by_id.get(ami)
    nm = im.get("Name", "?") if im else "(AMI DELETED/foreign)"
    print(f"  {ami}  x{n} instances  {nm[:60]}")

json.dump(
    {
        "unreferenced_amis": [
            {"id": im["ImageId"], "name": im.get("Name", ""),
             "created": im["CreationDate"],
             "snapshots": ami_snap[im["ImageId"]]}
            for im in unref
        ],
        "orphan_snapshots": [
            {"id": s["SnapshotId"], "start": s["StartTime"],
             "gb": s["VolumeSize"], "desc": s.get("Description", "")}
            for s in orphans
        ],
    },
    open("snapshot_kill_candidates.json", "w"), indent=1,
)
print("\nwrote snapshot_kill_candidates.json")
