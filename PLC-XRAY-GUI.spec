# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

project = Path(SPECPATH)

a = Analysis(
    ['PLC-XRAY-GUI.pyw'],
    pathex=[str(project / 'src')],
    binaries=[],
    datas=[(str(project / 'assets' / 'plc-xray.ico'), 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PLC-XRAY',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=str(project / 'assets' / 'plc-xray.ico'),
)
