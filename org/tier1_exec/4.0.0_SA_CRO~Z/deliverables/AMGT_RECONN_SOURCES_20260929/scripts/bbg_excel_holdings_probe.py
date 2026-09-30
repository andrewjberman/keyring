"""Read-only Bloomberg Excel access probe. See ../BBG_EXCEL_ACCESS_VERIFIED.md.
Writes evidence under .runtime by default; no production schedule.
Usage: python bbg_excel_holdings_probe.py bbg_excel_probe_queries.json [--output DIR]
"""
import argparse,json,pathlib,time,sys,datetime
import pythoncom,win32com.client,win32process
sys.stdout.reconfigure(encoding='utf-8')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('manifest',type=pathlib.Path)
parser.add_argument('--output',type=pathlib.Path,default=pathlib.Path('.runtime/amgt-reconn-bbg-excel-probes'))
args=parser.parse_args()
OUT=args.output.resolve();OUT.mkdir(parents=True,exist_ok=True)
manifest=args.manifest;name=manifest.stem
tests=json.loads(manifest.read_text(encoding='utf-8'))
report={'at':datetime.datetime.now().astimezone().isoformat(),'queries':tests,'results':{}}
excel=None;book=None
def save():(OUT/f'{name}_results.json').write_text(json.dumps(report,indent=2,default=str),encoding='utf-8')
try:
 excel=win32com.client.DispatchEx('Excel.Application');excel.Visible=False;excel.DisplayAlerts=False
 report['pid']=win32process.GetWindowThreadProcessId(excel.Hwnd)[1];save()
 excel.Workbooks.Open('C:/blp/API/Office Tools/BloombergUI.xla')
 report['xll']=excel.RegisterXLL('C:/blp/API/Office Tools/blpxladdin.xll')
 excel.RegisterXLL('C:/blp/API/Office Tools/brtdwrap.xll')
 book=excel.Workbooks.Add();sheets={}
 for label,query in tests.items():
  sheet=book.Worksheets.Add();sheet.Name=label[:31];sheets[label]=sheet
  sheet.Range('A1').Formula='=BQL.Query("'+query.replace('"','""')+'","showallcols=true")'
 excel.Calculate()
 for step in range(15):
  end=time.monotonic()+2
  while time.monotonic()<end:pythoncom.PumpWaitingMessages();time.sleep(.05)
  excel.Calculate()
  status={label:sheet.Range('A1').Text for label,sheet in sheets.items()}
  print('STATUS',2*(step+1),status,flush=True)
  if step>=3 and not any('Requesting' in v or 'Getting' in v for v in status.values()):break
 for label,sheet in sheets.items():
  nrows=sheet.UsedRange.Rows.Count;ncols=sheet.UsedRange.Columns.Count
  if nrows>10000 or ncols>100:raise RuntimeError(f'{label}: output exceeds probe bounds {nrows}x{ncols}')
  values=sheet.Range(sheet.Cells(1,1),sheet.Cells(max(nrows,2),max(ncols,2))).Value
  rows=[list(row) for row in values if any(v is not None for v in row)]
  rows=[row[:max(i+1 for i,v in enumerate(row) if v is not None)] for row in rows]
  report['results'][label]={'anchor':sheet.Range('A1').Text,'rows':rows,'used_rows':sheet.UsedRange.Rows.Count,'used_cols':sheet.UsedRange.Columns.Count}
  print('RESULT',label,'rows',len(rows),'columns',rows[0] if rows else [],flush=True)
 save();book.SaveAs(str(OUT/f'{name}.xlsx'),FileFormat=51);report['saved']=True;save()
finally:
 if book is not None:book.Close(SaveChanges=False)
 if excel is not None:excel.Quit()
