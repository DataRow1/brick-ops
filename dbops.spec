# dbops.spec
# PyInstaller spec for dbops (BRICK-OPS)

from PyInstaller.utils.hooks import collect_all

# collect_all returns: (datas, binaries, hiddenimports)
q_datas, q_binaries, q_hidden = collect_all("questionary")
ptk_datas, ptk_binaries, ptk_hidden = collect_all("prompt_toolkit")

a = Analysis(
    ["src/dbops_cli/__main__.py"],
    pathex=["."],
    binaries=[] + q_binaries + ptk_binaries,
    datas=[] + q_datas + ptk_datas,
    hiddenimports=[] + q_hidden + ptk_hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        # prompt_toolkit has optional SSH support that depends on asyncssh.
        "asyncssh",
        "prompt_toolkit.contrib.ssh",
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="dbops",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
)