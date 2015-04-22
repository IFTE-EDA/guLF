guLF - Gate Size Updater for Logic Friday
=========================================

guLF allows to change the gate sizes used by Logic Friday during gate diagram
synthesis.

[Download guLF v1.0 (for Windows)](https://github.com/IFTE-EDA/guLF/releases/download/v1.0/guLF-1.0.zip)

Introduction
------------

Logic Friday (http://sontrak.com/) is a very good and easy-to-use tool for
logic optimization, analysis, and synthesis. It uses espresso for logic
function minimization and misII for gate diagram synthesis. 

While it supports the optimization of the die area during gate diagram
synthesis, the size of the individual logic gates is fixed and can not be
changed by the user.

guLF allows to change these gate sizes using a simple GUI.

![guLF](https://ifte-eda.github.io/guLF/guLF.png)

How does it work?
-----------------

For gate diagram synthesis, Logic Friday calls the external program misII and
passes a pre-defined gate library containing all gate sizes. guLF wraps misII
and changes the sizes in the gate library prior to executing the original misII
binary.

Building
--------

Requirement: Python, pyinstaller (http://www.pyinstaller.org/)

In the directory of misII.py and guLF.py run:
```
> pyinstaller.exe misII.py
> pyinstaller.exe --noconsole guLF.py
```

These commands create the directories dist/misII and dist/guLF. All files in
dist/misII have to be copied to the directory misii in Logic Friday's
installation directory (**do not overwrite misII.exe**). The second directory
dist/guLF contains all files of the graphical editor (see next section).

Installation
------------

1. Download and install Logic Friday (http://sontrak.com)
2. Go to its installation directory (default: `C:\Program Files (x86)\Logic Friday 1`)
3. Change to directory misii and rename misII.exe to misII-orig.exe
3. Copy all files from directory misII (that comes with guLF) here

The graphical editor guLF does not need to be installed. Just run guLF.exe.

Usage
-----

Use guLF.exe to set the gate sizes. In Logic Friday, choose "Map to Gates" and
select all gate types you want to use. Finally, choose "Die Area" as
optimization type.

