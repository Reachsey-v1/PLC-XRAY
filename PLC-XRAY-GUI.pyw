import json, tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from plcxray import __version__
from plcxray.parser import parse_project
from plcxray.analyzer import analyze

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title(f'PLC-XRAY Professional v{__version__}'); self.geometry('1200x760'); self.minsize(1000,650)
        self.ir=None; self._ui()
    def _ui(self):
        self.configure(bg='#101418')
        top=tk.Frame(self,bg='#171c22',height=54); top.pack(fill='x')
        tk.Label(top,text='PLC-XRAY',font=('Segoe UI',18,'bold'),fg='white',bg='#171c22').pack(side='left',padx=18,pady=12)
        for label,cmd in [('Open Project',self.open_project),('Analyze',self.analyze_project),('Export JSON',self.export_json)]:
            ttk.Button(top,text=label,command=cmd).pack(side='left',padx=6,pady=10)
        body=tk.Frame(self,bg='#101418'); body.pack(fill='both',expand=True,padx=14,pady=14)
        left=tk.Frame(body,bg='#171c22',width=220); left.pack(side='left',fill='y')
        tk.Label(left,text='ENGINEERING',fg='#9fb3c8',bg='#171c22',font=('Segoe UI',9,'bold')).pack(anchor='w',padx=14,pady=(16,8))
        for x in ('Overview','Programs / POUs','Devices','Diagnostics','Evidence'):
            tk.Label(left,text=x,fg='#e8edf2',bg='#171c22',font=('Segoe UI',10),anchor='w').pack(fill='x',padx=14,pady=7)
        center=tk.Frame(body,bg='#f4f6f8'); center.pack(side='left',fill='both',expand=True)
        self.header=tk.Label(center,text='No project loaded',anchor='w',font=('Segoe UI',14,'bold'),bg='#f4f6f8',fg='#18212b'); self.header.pack(fill='x',padx=20,pady=(18,8))
        self.summary=tk.Text(center,height=7,bg='white',fg='#18212b',relief='flat'); self.summary.pack(fill='x',padx=20,pady=8)
        self.table=ttk.Treeview(center,columns=('status','title','detail'),show='headings');
        for c,w in [('status',130),('title',260),('detail',560)]: self.table.heading(c,text=c.title()); self.table.column(c,width=w,anchor='w')
        self.table.pack(fill='both',expand=True,padx=20,pady=10)
        self.status=tk.Label(self,text='READ-ONLY • Native GX Works verification not executed',anchor='w',bg='#0b0e11',fg='#b8c2cc'); self.status.pack(fill='x')
    def open_project(self):
        p=filedialog.askopenfilename(filetypes=[('GX Works project','*.gxw'),('All files','*.*')])
        if not p:return
        try:
            self.ir=parse_project(p); self.render()
        except Exception as e: messagebox.showerror('Import failed',str(e))
    def analyze_project(self):
        if not self.ir: return messagebox.showinfo('PLC-XRAY','Open a GXW project first.')
        self.render()
    def render(self):
        ir=self.ir; self.header.config(text=Path(ir.path).name)
        self.summary.delete('1.0','end'); self.summary.insert('end',f'Format: {ir.format}\nSHA-256: {ir.sha256}\nSize: {ir.file_size:,} bytes\nStreams: {len(ir.streams)}   POUs: {len(ir.pous)}   Labels: {len(ir.labels)}   Devices: {len(ir.devices)}\nVerification: NOT VERIFIED — native GX Works compile/open not executed')
        for x in self.table.get_children(): self.table.delete(x)
        for f in analyze(ir): self.table.insert('', 'end',values=(f.status,f.title,f.detail))
        self.status.config(text='READ-ONLY • Imported successfully • Native GX Works verification REQUIRED')
    def export_json(self):
        if not self.ir:return messagebox.showinfo('PLC-XRAY','Open a project first.')
        p=filedialog.asksaveasfilename(defaultextension='.json',filetypes=[('JSON','*.json')])
        if p: Path(p).write_text(json.dumps(self.ir.to_dict(),indent=2,default=str),encoding='utf-8')

if __name__=='__main__': App().mainloop()
