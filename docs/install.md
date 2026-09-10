# Installation
This SDK supports Python version 3.10 or later

```shell
$ pip install AcmP
```

## How to use?
!!! warning "Warning"
    Due to our driver running with **admin/root authentication**, it's important to execute the project with admin/root privileges.

    Before using this package, please ensure the following items are already installed

* **Windows**
    * Shared driver: `ADVMOT.dll`
        * For PCI-1245: `PCI1245.sys`, `PCI1245.dll`
        * For PCI-1285: `PCI1285.sys`, `PCI1285.dll`
        * For PCI-1203: `PCI1203.sys`, `PCI1203.dll`
        * For PCIE-1203M: `PCIE1203Ms.sys`, `PCIE1203M.dll`
        * For PCIE-1245: `PCIE1245s.sys`, `PCIE1245.dll`
        * For AMC Core: `AMC_Core.dll`
    !!! tips
        You can check the installation using the following commands.
        ```powershell
        ls C:\Windows\ -Recurse -Filter *ADVMOT* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCIE1203* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1203* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1245* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1285* -ErrorAction SilentlyContinue
        ```

* **Linux**
    * Shared driver: `libadvmot.so`
        * For PCIE-1203M: `pcie1203m.ko`, `libpcie1203.so`
        * For PCIE-1245: `pcie1245.ko`, `libpcie1245.so`
    !!! tips
        You can check the installation using the following commands.
        ```shell
        $ lsmod | grep PCI
        $ ls /lib | grep adv
        $ ls /lib | grep pcie
        ```