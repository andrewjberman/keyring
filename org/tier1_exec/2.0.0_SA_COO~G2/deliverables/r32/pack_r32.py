import gzip
import hashlib
import io
import os
import sys
import tarfile
src, out, fmtname, gzmode = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
PREFIX = len(sys.argv) > 5 and sys.argv[5] == "dotslash"
fmt = {"pax": tarfile.PAX_FORMAT, "gnu": tarfile.GNU_FORMAT, "ustar": tarfile.USTAR_FORMAT}[fmtname]
rels = []
for root, dirs, files in os.walk(src):
    for f in files:
        rels.append(os.path.relpath(os.path.join(root, f), src).replace(os.sep, "/"))
order = ["SHA256SUMS"] + sorted(r for r in rels if r != "SHA256SUMS")
raw = io.BytesIO()
with tarfile.open(fileobj=raw, mode="w", format=fmt) as tar:
    for name in order:
        data = open(os.path.join(src, name), "rb").read()
        info = tarfile.TarInfo(name=("." + "/" + name) if PREFIX else name)
        info.size = len(data)
        info.mode = 0o644
        info.mtime = 0
        info.uid = info.gid = 0
        info.uname = info.gname = ""
        tar.addfile(info, io.BytesIO(data))
tar_bytes = raw.getvalue()
if gzmode == "gzip":
    gz = gzip.compress(tar_bytes, compresslevel=9, mtime=0)
else:
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as g:
        g.write(tar_bytes)
    gz = buf.getvalue()
open(out, "wb").write(gz)
print(len(order), len(gz), hashlib.sha256(gz).hexdigest())
