#define MyAppName "PLC X-RAY"
#define MyAppVersion "1.2.0"
#define MyAppPublisher "Reachsey-v1"
#define MyAppExeName "PLC-XRAY.exe"

[Setup]
AppId={{9D8E5B1D-6B2D-4F1B-9D10-1C3A1100B2F4}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\PLC X-RAY
DefaultGroupName=PLC X-RAY
OutputDir=installer-output
OutputBaseFilename=PLC-XRAY-Setup-{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
UninstallDisplayIcon={app}\{#MyAppExeName}

[Files]
Source: "dist\PLC-XRAY.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\PLC X-RAY"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\PLC X-RAY"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch PLC X-RAY"; Flags: nowait postinstall skipifsilent
